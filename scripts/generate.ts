/**
 * Generates README.md, README.zh-CN.md, generated/providers.json and
 * generated/matrix.csv from data/. Never edit those outputs by hand.
 */
import fs from 'node:fs';
import path from 'node:path';
import * as yaml from 'js-yaml';
import { ROOT, GENERATED_DIR, loadFields, loadCategories, loadProviders, loadCandidates, daysSince, type Provider, type Check } from './lib.ts';

const STALE_DAYS = 180;
const REPO = 'Olorinm/agent-friendly-services';
const RAW_JSON = `https://raw.githubusercontent.com/${REPO}/main/generated/providers.json`;

const fields = loadFields();
const categories = loadCategories();
const providers = loadProviders()
  .map((p) => p.data)
  .sort((a, b) => a.id.localeCompare(b.id));
// Candidate pool: same schema, zero verification — rendered separately and
// never mixed into providers.json/matrix (docs/candidate-pool.md).
const candidates = loadCandidates()
  .map((p) => p.data)
  .sort((a, b) => a.id.localeCompare(b.id));

// ---------------------------------------------------------------------------
// Agent runs (published subset of experiment results; docs/agent-verification.md)
// ---------------------------------------------------------------------------
interface AgentRun {
  provider: string; layer: string; route?: string; milestone?: string; task?: string; rep: number;
  model: string; date: string; contaminated?: string; run_error?: string;
  agent_claims: { result?: string; wrong_attempts?: number; friction_notes?: string[] } | null;
  verified_independently: boolean | 'n/a'; num_turns: number; duration_ms: number;
  total_cost_usd: number; transcript: string;
}
const PUBLISHED_DIR = path.join(ROOT, 'data/experiments/published');
const AGENT_RUNS = './generated/agent-runs.md';
const agentRunsByProvider = new Map<string, AgentRun[]>();
const dryFireRunsByProvider = new Map<string, AgentRun[]>();
if (fs.existsSync(PUBLISHED_DIR)) {
  for (const pid of fs.readdirSync(PUBLISHED_DIR)) {
    const dir = path.join(PUBLISHED_DIR, pid);
    if (!fs.statSync(dir).isDirectory()) continue;
    const all = fs.readdirSync(dir).filter((f) => f.endsWith('.yaml'))
      .map((f) => yaml.load(fs.readFileSync(path.join(dir, f), 'utf8')) as AgentRun)
      .filter((r) => !r.contaminated && !r.run_error && daysSince(r.date) <= STALE_DAYS);
    const real = all.filter((r) => r.layer === 'real');
    const dryFire = all.filter((r) => r.layer === 'dry-fire');
    if (real.length) agentRunsByProvider.set(pid, real);
    if (dryFire.length) dryFireRunsByProvider.set(pid, dryFire);
  }
}

// M1 (first-call / dry-fire) verdict: majority over published dry-fire reps.
// Dry-fire runs carry no credential, so the pass evidence is the transcript
// itself (a documented auth-error from the correct endpoint), reviewed before
// publication — docs/publication-protocol.md.
function m1Status(pid: string): { verdict: 'pass' | 'fail'; date: string; transcript: string } | null {
  const runs = dryFireRunsByProvider.get(pid) ?? [];
  if (!runs.length) return null;
  const passes = runs.filter((r) => r.agent_claims?.result === 'pass').length;
  const latest = [...runs].sort((a, b) => a.date.localeCompare(b.date)).at(-1)!;
  return { verdict: passes * 2 > runs.length ? 'pass' : 'fail', date: latest.date, transcript: latest.transcript };
}

const ROUTE_ORDER = ['http', 'cli', 'mcp'];
// Task-ladder milestones (data/experiments/tasks/): runs recorded before the
// ladder existed carry no milestone field and count as "core".
const MILESTONE_ORDER = ['core', 'lifecycle', 'billing'];
const runMilestone = (r: AgentRun) => r.milestone ?? 'core';
const median = (xs: number[]) => [...xs].sort((a, b) => a - b)[Math.floor(xs.length / 2)];

interface RouteAgg {
  route: string; reps: number; passes: number; majorityPass: boolean; medTurns: number;
  secs: [number, number]; cost: [number, number]; models: string[]; date: string; runs: AgentRun[];
}
function milestonesOf(pid: string): string[] {
  const seen = [...new Set((agentRunsByProvider.get(pid) ?? []).map(runMilestone))];
  return seen.sort((a, b) => {
    const ia = MILESTONE_ORDER.indexOf(a); const ib = MILESTONE_ORDER.indexOf(b);
    return (ia === -1 ? 99 : ia) - (ib === -1 ? 99 : ib) || a.localeCompare(b);
  });
}

// Aggregates one provider's runs for one route on one milestone. Badges, the
// 🏆 marker and the route-comparison table are all pinned to the "core"
// milestone so they stay comparable as ladders grow.
function routeAggs(pid: string, milestoneId = 'core'): RouteAgg[] {
  return ROUTE_ORDER.flatMap((route) => {
    const rs = (agentRunsByProvider.get(pid) ?? []).filter((r) => r.route === route && runMilestone(r) === milestoneId);
    if (!rs.length) return [];
    const passes = rs.filter((r) => r.verified_independently === true && r.agent_claims?.result === 'pass').length;
    const secs = rs.map((r) => Math.round(r.duration_ms / 1000));
    const cost = rs.map((r) => r.total_cost_usd);
    return [{
      route, reps: rs.length, passes, majorityPass: passes * 2 > rs.length,
      medTurns: median(rs.map((r) => r.num_turns)),
      secs: [Math.min(...secs), Math.max(...secs)] as [number, number],
      cost: [Math.min(...cost), Math.max(...cost)] as [number, number],
      models: [...new Set(rs.map((r) => r.model))],
      date: rs.map((r) => r.date).sort().at(-1)!,
      runs: rs,
    }];
  });
}
const isAgentVerified = (pid: string) => routeAggs(pid).some((a) => a.majorityPass);

// 🏆 top measured per category — mechanically derived, never editorial:
// majority-pass on the baseline (http) route, fewest median turns, then lowest cost.
// It changes hands automatically whenever a better run lands.
const topMeasured = new Map<string, string>();
for (const cat of loadCategories()) {
  const cands = providers
    .map((p) => ({ p, http: routeAggs(p.id).find((a) => a.route === 'http') }))
    .filter((x) => x.p.category === cat.id && x.http?.majorityPass)
    .sort((a, b) => a.http!.medTurns - b.http!.medTurns || a.http!.cost[1] - b.http!.cost[1]);
  if (cands.length) topMeasured.set(cat.id, cands[0].p.id);
}

// ---------------------------------------------------------------------------
// Derivations
// ---------------------------------------------------------------------------
function checkStatus(p: Provider, id: string): Check['status'] | 'missing' {
  return p.checks?.[id]?.status ?? 'missing';
}

function badges(p: Provider): string[] {
  const b: string[] = [];
  if (p.entrypoints.mcp_official) b.push('Official MCP');
  if (p.entrypoints.llms_txt) b.push('llms.txt');
  if (p.entrypoints.openapi) b.push('OpenAPI');
  if (p.entrypoints.cli) b.push('CLI');
  if (p.entrypoints.agent_docs) b.push('Agent Docs');
  if (checkStatus(p, 'sandbox_or_test_mode') === 'supported') b.push('Sandbox');
  if (checkStatus(p, 'self_serve_signup') === 'supported' && checkStatus(p, 'api_key_self_serve') === 'supported') b.push('Self-serve');
  if (checkStatus(p, 'idempotency') === 'supported') b.push('Idempotent API');
  if (isStale(p)) b.push('Stale');
  return b;
}

function verifiedDates(p: Provider): string[] {
  return Object.values(p.checks ?? {})
    .map((c) => c.verified)
    .filter((d): d is string => Boolean(d))
    .sort();
}

function isStale(p: Provider): boolean {
  const dates = verifiedDates(p);
  if (dates.length === 0) return true;
  return daysSince(dates[0]) > STALE_DAYS;
}

function lastVerified(p: Provider): string | null {
  const dates = verifiedDates(p);
  return dates.length ? dates[dates.length - 1] : null;
}

function unknownChecks(p: Provider): string[] {
  return Object.keys(fields.checks).filter((id) => {
    const s = checkStatus(p, id);
    return s === 'unknown' || s === 'missing';
  });
}

const SYM: Record<string, string> = {
  supported: '✓',
  partial: '◐',
  unsupported: '✗',
  not_applicable: 'n/a',
  unknown: '—',
  missing: '—',
};

function entrySym(p: Provider, field: string): string {
  return p.entrypoints[field] ? '✓' : '—';
}

function selfServeSym(p: Provider): string {
  const a = checkStatus(p, 'self_serve_signup');
  const b = checkStatus(p, 'api_key_self_serve');
  if (a === 'supported' && b === 'supported') return '✓';
  if ([a, b].includes('unsupported')) return '✗';
  if ([a, b].includes('partial')) return '◐';
  return '—';
}

// ---------------------------------------------------------------------------
// generated/providers.json
// ---------------------------------------------------------------------------
fs.mkdirSync(GENERATED_DIR, { recursive: true });

const jsonOut = {
  name: 'agent-friendly-services',
  description: 'A community-maintained, evidence-backed directory of service entry points for AI agents.',
  spec: {
    status_enum: ['supported', 'partial', 'unsupported', 'unknown', 'not_applicable'],
    entrypoint_semantics: 'A missing entrypoint means "no known URL", not "confirmed absent".',
    stale_after_days: STALE_DAYS,
  },
  generated_at: new Date().toISOString(),
  counts: {
    providers: providers.length,
    categories: categories.length,
    entrypoint_urls: providers.reduce((n, p) => n + Object.values(p.entrypoints).flat().length, 0),
    checks_answered: providers.reduce(
      (n, p) => n + Object.values(p.checks ?? {}).filter((c) => c.status !== 'unknown').length,
      0,
    ),
  },
  categories,
  fields,
  providers: providers.map((p) => ({
    ...p,
    derived: {
      badges: badges(p).filter((b) => b !== 'Stale'),
      stale: isStale(p),
      last_verified: lastVerified(p),
      unknown_checks: unknownChecks(p),
    },
  })),
};
fs.writeFileSync(path.join(GENERATED_DIR, 'providers.json'), JSON.stringify(jsonOut, null, 2) + '\n');

// ---------------------------------------------------------------------------
// generated/candidates.json — the unverified pool, deliberately a SEPARATE
// file so providers.json consumers (MCP server, agents) never ingest
// unverified claims by accident.
// ---------------------------------------------------------------------------
const candidatesOut = {
  description: 'Candidate pool: submitted, not yet verified. Entry and promotion rules: docs/candidate-pool.md.',
  generated_at: new Date().toISOString(),
  count: candidates.length,
  candidates: candidates.map((p) => ({
    id: p.id,
    name: p.name,
    category: p.category,
    homepage: p.homepage,
    summary: p.summary,
    submitted_by: p.submitted_by,
    entrypoints: p.entrypoints,
    m1: m1Status(p.id),
  })),
};
fs.writeFileSync(path.join(GENERATED_DIR, 'candidates.json'), JSON.stringify(candidatesOut, null, 2) + '\n');

// ---------------------------------------------------------------------------
// generated/matrix.csv
// ---------------------------------------------------------------------------
const csvCols = ['id', 'name', 'category', 'mcp_official', 'llms_txt', 'openapi', 'cli', 'sandbox', 'self_serve', 'last_verified'];
const csvRows = providers.map((p) =>
  [
    p.id,
    p.name,
    p.category,
    entrySym(p, 'mcp_official') === '✓',
    entrySym(p, 'llms_txt') === '✓',
    entrySym(p, 'openapi') === '✓',
    entrySym(p, 'cli') === '✓',
    checkStatus(p, 'sandbox_or_test_mode'),
    selfServeSym(p) === '✓',
    lastVerified(p) ?? '',
  ].join(','),
);
fs.writeFileSync(path.join(GENERATED_DIR, 'matrix.csv'), [csvCols.join(','), ...csvRows].join('\n') + '\n');

// ---------------------------------------------------------------------------
// README.md
// ---------------------------------------------------------------------------
const catName = (id: string) => categories.find((c) => c.id === id)?.name ?? id;

// Link health (written by `npm run probe`); tolerate absence.
let linkHealth: { checked_at: string; ok: number; inconclusive: number; broken: number } | null = null;
try {
  linkHealth = JSON.parse(fs.readFileSync(path.join(GENERATED_DIR, 'link-health.json'), 'utf8'));
} catch {
  /* no probe results yet */
}

function shieldText(s: string): string {
  return encodeURIComponent(s.replace(/-/g, '--').replace(/_/g, '__')).replace(/%20/g, '_');
}

const verifiedCount = providers.filter((p) => isAgentVerified(p.id)).length;

const badgeParts = [
  `![Providers](https://img.shields.io/badge/providers-${providers.length}-2563eb)`,
  verifiedCount ? `[![Agent-verified](https://img.shields.io/badge/agent--verified-${verifiedCount}-10b981)](${AGENT_RUNS})` : null,
  linkHealth
    ? `[![Link health](https://img.shields.io/badge/link_health-${shieldText(`${linkHealth.ok} ok, ${linkHealth.broken} broken`)}-${linkHealth.broken > 0 ? 'e11d48' : '10b981'})](./generated/link-health.json)`
    : null,
  `[![Last update](https://img.shields.io/github/last-commit/${REPO}?label=last%20update&color=8b5cf6)](https://github.com/${REPO}/commits/main)`,
  `[![Data: CC BY 4.0](https://img.shields.io/badge/data-CC_BY_4.0-64748b)](./LICENSE-DATA)`,
].filter(Boolean);

const activeCategories = categories.filter((c) => providers.some((p) => p.category === c.id));

function agentCell(p: Provider): string {
  const routes = routeAggs(p.id).filter((a) => a.majorityPass).map((a) => a.route[0]);
  return routes.length ? `[✓ ${routes.join('·')}](${AGENT_RUNS.replace('./generated/', './')}#${p.id})` : '—';
}

function providerRow(p: Provider, linkPrefix = ''): string {
  // The Agent cell links relative to generated/ when the matrix is rendered there,
  // and via the README prefix otherwise.
  const agent = linkPrefix === ''
    ? agentCell(p)
    : agentCell(p).replace('(./', '(./generated/');
  return `| [${p.name}](${linkPrefix}#${p.id}) | ${entrySym(p, 'mcp_official')} | ${entrySym(p, 'llms_txt')} | ${entrySym(p, 'openapi')} | ${entrySym(p, 'cli')} | ${SYM[checkStatus(p, 'sandbox_or_test_mode')]} | ${selfServeSym(p)} | ${agent} | ${lastVerified(p) ?? '—'} |`;
}

// linkPrefix: '' inside providers.md (anchors are local), DETAILS from the READMEs.
// heading: '###' in providers.md; bold text in the READMEs so the collapsed matrix
// doesn't steal the category headings' anchor slugs from the TOC.
function matrixTables(linkPrefix: string, heading: (name: string) => string): string {
  return activeCategories
    .map((cat) => {
      const list = providers.filter((p) => p.category === cat.id);
      return `${heading(cat.name)}

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
${list.map((p) => providerRow(p, linkPrefix)).join('\n')}`;
    })
    .join('\n\n');
}

function entrypointLinks(p: Provider): string {
  const parts: string[] = [];
  for (const [id, def] of Object.entries(fields.entrypoints)) {
    const v = p.entrypoints[id];
    if (!v) continue;
    if (Array.isArray(v)) parts.push(...v.map((u, i) => `[${def.name}${v.length > 1 ? ` ${i + 1}` : ''}](${u})`));
    else parts.push(`[${def.name}](${v})`);
  }
  return parts.join(' · ');
}

function checksBlock(p: Provider): string {
  const lines: string[] = [];
  const groups: Record<string, string[]> = { supported: [], partial: [], unsupported: [], not_applicable: [] };
  for (const [id, def] of Object.entries(fields.checks)) {
    const c = p.checks?.[id];
    if (!c || c.status === 'unknown') continue;
    const label = c.evidence ? `[${def.name}](${c.evidence})` : def.name;
    const note = c.notes ? ` — ${c.notes}` : '';
    if (c.status === 'supported') groups.supported.push(label);
    else if (c.status === 'partial') groups.partial.push(`${label}${note}`);
    else if (c.status === 'unsupported') groups.unsupported.push(`${label}${note}`);
    else if (c.status === 'not_applicable') groups.not_applicable.push(`${label}${note}`);
  }
  if (groups.supported.length) lines.push(`- **Supported:** ${groups.supported.join(' · ')}`);
  for (const item of groups.partial) lines.push(`- **Partial:** ${item}`);
  for (const item of groups.unsupported) lines.push(`- **Not supported:** ${item}`);
  for (const item of groups.not_applicable) lines.push(`- **N/A:** ${item}`);
  const unknowns = unknownChecks(p);
  if (unknowns.length) lines.push(`- **Unknown (help wanted):** ${unknowns.map((id) => `\`${id}\``).join(', ')}`);
  return lines.join('\n');
}

const totalUnknown = providers.reduce((n, p) => n + unknownChecks(p).length, 0);

// Per-provider "Agent runs" table (fact sheets + agent-runs.md). linkBase: path
// prefix from the rendering file to the repo root.
function agentRunsTable(p: Provider, linkBase: string): string {
  const rows = milestonesOf(p.id).flatMap((mid) => routeAggs(p.id, mid).map((a) =>
    `| ${mid} · ${a.route} | ${a.passes}/${a.reps} pass | ${a.medTurns} | ${a.secs[0]}–${a.secs[1]} s | $${a.cost[0].toFixed(2)}–$${a.cost[1].toFixed(2)} | ${a.models.join(', ')} | ${a.date} | ${a.runs.map((r, i) => `[${i + 1}](${linkBase}data/experiments/published/${p.id}/${r.transcript})`).join(' ')} |`));
  if (!rows.length) return '';
  return `| Milestone · route | Verdict | Median turns | Wall time | Cost/run | Model | Date | Transcripts |
| --- | --- | --- | --- | --- | --- | --- | --- |
${rows.join('\n')}`;
}

// generated/providers.md — the full per-provider fact sheets (kept out of the README).
const providersMd = `<!-- GENERATED FILE — do not edit. Run \`npm run generate\`. Source of truth: data/ -->

# Provider Details

Every known entry point and verified capability fact, with evidence links and dates.
Symbols: ✓ supported/available · ◐ partial · ✗ not supported · n/a not applicable · — unknown.
Agent column: routes with a majority of independently verified real-task passes (h=http c=cli m=mcp; see [agent-runs.md](./agent-runs.md)).
A missing link means **"no known URL"**, not "confirmed absent"; \`unknown\` means "checked, no reliable evidence found yet".
Links are probed weekly ([link-health.json](./link-health.json)); machine-readable version: [providers.json](./providers.json).

## Matrix

${matrixTables('', (name) => `### ${name}`)}

## Providers

${providers
  .map((p) => {
    const b = badges(p);
    return `### ${p.name} <a id="${p.id}"></a>

> ${p.summary}

**Category:** ${catName(p.category)}${p.scope ? ` · **Scope:** ${p.scope}` : ''}${p.submitted_by === 'vendor' ? ' · *vendor-submitted*' : ''}${b.length ? ` · ${b.map((x) => `\`${x}\``).join(' ')}` : ''}

**Links:** ${entrypointLinks(p)}

${checksBlock(p)}
${agentRunsTable(p, '../') ? `\n**Agent runs** — a real agent climbed this category's [task ladder](../data/experiments/tasks/${p.category}.yaml), every result independently verified ([method](../docs/agent-verification.md) · [all runs](./agent-runs.md#${p.id})):\n\n${agentRunsTable(p, '../')}\n` : ''}${p.notes?.length ? `\n${p.notes.map((n) => `> ${n}`).join('\n')}\n` : ''}`;
  })
  .join('\n')}
`;
fs.writeFileSync(path.join(GENERATED_DIR, 'providers.md'), providersMd);

// generated/agent-runs.md — measured agent runs, route comparison first.
const measured = providers.filter((p) => agentRunsByProvider.has(p.id));
const routeCmpRows = measured.map((p) => {
  const cells = ROUTE_ORDER.map((route) => {
    const a = routeAggs(p.id).find((x) => x.route === route);
    return a ? `${a.majorityPass ? '✓' : '✗'} ${a.passes}/${a.reps} · ${a.medTurns}t · $${a.cost[0].toFixed(2)}–${a.cost[1].toFixed(2)}` : '—';
  });
  const crown = topMeasured.get(p.category) === p.id ? ' 🏆' : '';
  return `| [${p.name}](#${p.id})${crown} (${catName(p.category)}) | ${cells.join(' | ')} |`;
});
const agentRunsMd = `<!-- GENERATED FILE — do not edit. Run \`npm run generate\`. Source of truth: data/experiments/published/ -->

# Agent Runs

Real AI agents climbing each category's [pinned task ladder](../data/experiments/tasks/) against the live service — unattended, in a pinned clean environment, with the runner (not the agent) verifying every result through the provider's API. Milestones: **core** = the category's basic realistic task · **lifecycle** = set up → use → evolve → tear down · **billing** = machine-readable usage/billing reality. Method, environment and hard rules: [agent-verification.md](../docs/agent-verification.md).

Every run publishes its model, date, metrics and full transcript ([what gets published, and how](../docs/publication-protocol.md)). Results expire after ${STALE_DAYS} days. Providers can dispute any run by opening an issue — we rerun under the same pinned conditions.

${measured.length === 0 ? 'No published runs yet — the first provisioned batch is in progress.\n' : `## Route comparison

The same **core-milestone** task, over each way an agent can reach the provider (**http** = official docs + raw API calls, the universal baseline · **cli** = the provider's official CLI · **mcp** = the provider's official MCP server). The route-vs-baseline delta shows whether a provider's agent tooling actually pays off. 🏆 = best measured result in its category (majority-pass on the baseline route, fewest median turns) — it changes hands automatically whenever a better run lands.

| Provider | http (baseline) | cli | mcp |
| --- | --- | --- | --- |
${routeCmpRows.join('\n')}

Cell format: verdict · passes/reps · median turns · cost per run.

## Runs by provider

${measured
  .map((p) => {
    const notes = routeAggs(p.id).flatMap((a) =>
      a.runs.flatMap((r) => (r.agent_claims?.friction_notes ?? []).map((n) => `- *(${a.route} rep${r.rep})* ${n}`)));
    return `### ${p.name} <a id="${p.id}"></a>

Task: \`${(agentRunsByProvider.get(p.id) ?? [])[0]?.task}\` ([definition](../data/experiments/tasks/${p.category}.yaml)) · [provider facts](./providers.md#${p.id})

${agentRunsTable(p, '../')}
${notes.length ? `\n**Run notes** (agent-reported, verbatim):\n\n${notes.join('\n')}` : ''}`;
  })
  .join('\n\n')}`}
`;
fs.writeFileSync(path.join(GENERATED_DIR, 'agent-runs.md'), agentRunsMd);

// README.md / README.zh-CN.md — awesome-style: one bullet per provider, details linked.
// Provider names, summaries and category headings stay English in both languages
// (single-source data, stable anchors); only the surrounding prose is translated.
const DETAILS = './generated/providers.md';

function awesomeLinks(p: Provider, allFactsLabel: string): string {
  const e = p.entrypoints;
  const parts: string[] = [];
  if (e.api_reference) parts.push(`[API](${e.api_reference})`);
  if (e.graphql && !e.api_reference) parts.push(`[GraphQL](${e.graphql})`);
  if (e.mcp_official) parts.push(`[MCP](${e.mcp_official})`);
  if (e.llms_txt) parts.push(`[llms.txt](${e.llms_txt})`);
  if (e.openapi) parts.push(`[OpenAPI](${e.openapi})`);
  if (e.cli) parts.push(`[CLI](${e.cli})`);
  parts.push(`[${allFactsLabel}](${DETAILS}#${p.id})`);
  return parts.join(' · ');
}

function awesomeEntry(p: Provider, labels: { allFacts: string; verified: string; vendor: string }): string {
  const summary = p.summary.replace(/\s+/g, ' ').trim().replace(/\.$/, '');
  const crown = topMeasured.get(p.category) === p.id ? ' 🏆' : '';
  const badge = isAgentVerified(p.id) ? ` · **[🤖✓ ${labels.verified}](${AGENT_RUNS}#${p.id})**` : '';
  const vendor = p.submitted_by === 'vendor' ? ` · *${labels.vendor}*` : '';
  return `- **[${p.name}](${p.entrypoints.docs})**${crown} — ${summary}. ${awesomeLinks(p, labels.allFacts)}${badge}${vendor}`;
}

// GitHub heading slugs: lowercase, strip punctuation, each space becomes one hyphen.
const toc = activeCategories
  .map((c) => `[${c.name}](#${c.name.toLowerCase().replace(/[^a-z0-9\s-]/g, '').replace(/\s/g, '-')})`)
  .join(' · ');

function categorySections(labels: { allFacts: string; verified: string; vendor: string }): string {
  return activeCategories
    .map((cat) => {
      const list = providers.filter((p) => p.category === cat.id);
      return `## ${cat.name}

${list.map((p) => awesomeEntry(p, labels)).join('\n')}`;
    })
    .join('\n\n');
}

// Candidate-pool section: identity + M1 verdict only. Vendor claims stay in
// the candidate's YAML until promotion — rendering them here would make them
// look endorsed.
function candidateRow(p: Provider): string {
  const m1 = m1Status(p.id);
  const m1Cell = m1
    ? `[${m1.verdict === 'pass' ? '✓ pass' : '✗ fail'} · ${m1.date}](./data/experiments/published/${p.id}/${m1.transcript})`
    : 'pending';
  return `| [${p.name}](${p.homepage}) | ${catName(p.category)} | ${p.submitted_by} | ${m1Cell} | [yaml](./data/candidates/${p.id}.yaml) |`;
}

const candidatePoolEn = candidates.length
  ? `## Candidate pool

Submitted, **not yet verified** — listed for transparency only ([how the pool works](./docs/candidate-pool.md)). An entry is promoted into the index above once an agent passes the M1 first-call run against it and its evidence survives review; until then its claims live only in its YAML file.

| Candidate | Category | Submitted by | M1 first-call | Claims |
| --- | --- | --- | --- | --- |
${candidates.map(candidateRow).join('\n')}

`
  : '';

const candidatePoolZh = candidates.length
  ? `## 候选池

已提交、**尚未验证** —— 仅为透明而列出（[候选池规则](./docs/candidate-pool.md)）。条目要晋升进上方正式索引，必须先通过 M1 首次调用实测、且证据经得起复核；在此之前，其声明只存在于它自己的 YAML 文件里。

| 候选 | 类别 | 提交方 | M1 首次调用 | 声明 |
| --- | --- | --- | --- | --- |
${candidates.map(candidateRow).join('\n')}

`
  : '';

const readme = `<!-- GENERATED FILE — do not edit. Run \`npm run generate\`. Source of truth: data/ -->

# Agent-Friendly Services

English | [简体中文](./README.zh-CN.md)

Where AI agents plug into ${providers.length} popular services: docs, APIs, official MCP servers, llms.txt, CLIs. Every link machine-probed weekly; every capability fact backed by official evidence and a date ([methodology](./docs/methodology.md)) — plus **[measured agent runs](${AGENT_RUNS})**: real agents completing real tasks against the live service, independently verified, transcripts included. 🏆 marks the best measured result in a category — held until someone measures better.

${badgeParts.join('\n')}

**🤖 Agents** — add the MCP server, or fetch the whole dataset as one JSON file:

\`\`\`bash
# MCP server — tools: search_providers, get_provider, list_categories, get_stats
claude mcp add agent-friendly-services -- npx -y github:${REPO}

# Or skip the server: the same data as one JSON file
curl -s ${RAW_JSON}
\`\`\`

Other MCP clients: command \`npx\`, args \`["-y", "github:${REPO}"]\` ([details](./mcp/)). Repo map: [\`llms.txt\`](./llms.txt) · contribution manual: [\`AGENTS.md\`](./AGENTS.md).

**🧑‍💻 Humans** — browse below: each name links to the docs, the trailing links are what officially exists (a missing link means "no known URL", not "confirmed absent"). Full fact sheets with evidence and dates: [provider details](${DETAILS}#providers) · measured runs & route comparison: [agent runs](${AGENT_RUNS}) · spreadsheet: [\`matrix.csv\`](./generated/matrix.csv).

**🏢 Vendors** — fix your own entry in one PR with documentation (not marketing) as evidence. New services enter the [candidate pool](./docs/candidate-pool.md) and are promoted only after a measured agent run — claims are tested, not argued ([rules](./docs/contributing.md)).

<details open>
<summary><b>Capability matrix</b> — all ${providers.length} providers at a glance (✓ supported · ◐ partial · ✗ unsupported · — unknown · Agent: verified routes, h=http c=cli m=mcp)</summary>

${matrixTables(DETAILS, (name) => `**${name}**`)}

</details>

---

${toc}

${categorySections({ allFacts: 'all facts →', verified: 'agent-verified', vendor: 'vendor-submitted' })}

${candidatePoolEn}## Contributing

One fact = one contribution: report a broken link (2 min, [issue form](../../issues/new/choose)) · resolve one of the **${totalUnknown} open \`unknown\`s** (15 min) · add a provider (1–2 h, [inclusion rules](./docs/methodology.md#inclusion-rules)). CI validates everything mechanical; humans only review evidence quality. Full guide: [\`docs/contributing.md\`](./docs/contributing.md).

Have a coding agent? Point it at a checkout and paste:

\`\`\`text
Read AGENTS.md, then resolve one "unknown" check: find official evidence, update
the provider YAML (or leave it unknown if evidence is genuinely missing), run
npm run validate, and open a small PR.
\`\`\`

## Related

[Fern Agent Score](https://buildwithfern.com/agent-score) (docs-site readiness scoring — we deliberately don't duplicate it) · [Cloudflare Agent Readiness](https://blog.cloudflare.com/agent-readiness/) · [official MCP Registry](https://registry.modelcontextprotocol.io/) · [llms.txt hub](https://llmstxthub.com/)

## License

Code: [MIT](./LICENSE) · Data (\`data/\`, \`generated/\`): [CC BY 4.0](./LICENSE-DATA)
`;

fs.writeFileSync(path.join(ROOT, 'README.md'), readme);

const readmeZh = `<!-- 生成文件 — 请勿手改。运行 \`npm run generate\`。数据源：data/ -->

# Agent-Friendly Services（智能体友好服务索引）

[English](./README.md) | 简体中文

AI 智能体接入 ${providers.length} 个主流服务的入口索引：文档、API、官方 MCP 服务器、llms.txt、CLI。所有链接每周机器探测；每条能力事实都附官方证据链接和验证日期（[方法论](./docs/methodology.md)）—— 还有 **[实测运行数据](${AGENT_RUNS})**：真实 agent 在真实服务上完成真实任务，结果独立校验、transcript 全文公开。🏆 标记类别内实测最优 —— 谁测得更好归谁。

${badgeParts.join('\n')}

**🤖 智能体** —— 添加 MCP 服务器，或直接把完整数据集当一个 JSON 文件拉取：

\`\`\`bash
# MCP 服务器 —— 工具：search_providers、get_provider、list_categories、get_stats
claude mcp add agent-friendly-services -- npx -y github:${REPO}

# 不装服务器也行：同一份数据就是一个 JSON 文件
curl -s ${RAW_JSON}
\`\`\`

其他 MCP 客户端：command \`npx\`，args \`["-y", "github:${REPO}"]\`（[详情](./mcp/)）。仓库地图：[\`llms.txt\`](./llms.txt) · 智能体贡献手册：[\`AGENTS.md\`](./AGENTS.md)。

**🧑‍💻 人类** —— 直接往下浏览：服务名链到官方文档，后面跟着的是官方确认存在的入口（没有链接表示"暂无已知 URL"，不代表"确认不存在"）。带证据和日期的完整事实表：[提供商详情](${DETAILS}#providers) · 实测运行与路线对比：[agent runs](${AGENT_RUNS}) · 表格版：[\`matrix.csv\`](./generated/matrix.csv)。

**🏢 服务商** —— 欢迎自己维护自己的条目：一个 PR、以文档（而非营销页）为证据。新服务先进入[候选池](./docs/candidate-pool.md)，通过 agent 实测后才晋升 —— 声明靠实测说话（[规则](./docs/contributing.md)）。

> 提供商简介与详情页保持英文原文（数据单一来源，避免翻译漂移）；本页仅翻译框架文字。

<details open>
<summary><b>能力矩阵表</b> —— ${providers.length} 家提供商一览（✓ 支持 · ◐ 部分 · ✗ 不支持 · — 未知 · Agent 列：已验证路线，h=http c=cli m=mcp）</summary>

${matrixTables(DETAILS, (name) => `**${name}**`)}

</details>

---

${toc}

${categorySections({ allFacts: '全部事实 →', verified: '实测验证', vendor: '厂商提交' })}

${candidatePoolZh}## 参与贡献

一条事实 = 一次贡献：报告失效链接（2 分钟，[issue 表单](../../issues/new/choose)） · 解决 **${totalUnknown} 个待查 \`unknown\`** 中的一个（15 分钟） · 新增一个提供商（1–2 小时，[收录规则](./docs/methodology.md#inclusion-rules)）。机械性检查全部由 CI 完成，人工只审证据质量。完整指南：[\`docs/contributing.md\`](./docs/contributing.md)。

有编程智能体？让它打开本仓库的检出目录，然后粘贴：

\`\`\`text
Read AGENTS.md, then resolve one "unknown" check: find official evidence, update
the provider YAML (or leave it unknown if evidence is genuinely missing), run
npm run validate, and open a small PR.
\`\`\`

## 相关项目

[Fern Agent Score](https://buildwithfern.com/agent-score)（文档站就绪度打分 —— 我们刻意不重复它的工作） · [Cloudflare Agent Readiness](https://blog.cloudflare.com/agent-readiness/) · [官方 MCP Registry](https://registry.modelcontextprotocol.io/) · [llms.txt hub](https://llmstxthub.com/)

## 许可证

代码：[MIT](./LICENSE) · 数据（\`data/\`、\`generated/\`）：[CC BY 4.0](./LICENSE-DATA)
`;

fs.writeFileSync(path.join(ROOT, 'README.zh-CN.md'), readmeZh);

console.log(`✓ README.md, README.zh-CN.md, generated/providers.json, generated/candidates.json, generated/matrix.csv, generated/agent-runs.md`);
console.log(`  ${providers.length} providers · ${candidates.length} candidates · ${jsonOut.counts.entrypoint_urls} entry links · ${totalUnknown} unknowns open`);
