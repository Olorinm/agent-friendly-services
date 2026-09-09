/**
 * Generates README.md, README.zh-CN.md, generated/providers.json and
 * generated/matrix.csv from data/. Never edit those outputs by hand.
 */
import fs from 'node:fs';
import path from 'node:path';
import * as yaml from 'js-yaml';
import { ROOT, loadFields, loadCategories, loadProviders, loadCandidates, daysSince, type Provider, type Check } from './lib.ts';
import { catalogService } from './catalog.ts';
import { generateResearch } from './research.ts';
import { loadPrices, estimateModelCost } from './model-costs.ts';
import { readmeTable } from './readme-table.ts';
import { taskDisplay } from './task-display.ts';
import { serviceAccess } from './service-access.ts';
import { renderServiceResults, renderSetup } from './service-results.ts';
import { buildBoards, selectServiceBoards, renderBoardRows, renderBoardDetails, boardHeader } from './leaderboard.ts';
import { loadEvaluations, evaluationErrors, generateEvaluations } from './evaluations.ts';

// Isolated preview/CI generation, without changing checked-in build outputs.
const OUTPUT_ROOT = process.env.AFS_OUTPUT_DIR ? path.resolve(process.env.AFS_OUTPUT_DIR) : ROOT;
const GENERATED_DIR = path.join(OUTPUT_ROOT, 'generated');

const STALE_DAYS = 180;
const REPO = 'Olorinm/agent-friendly-services';
const RAW_JSON = `https://raw.githubusercontent.com/${REPO}/main/generated/catalog.json`;

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

generateResearch(OUTPUT_ROOT, categories);

const prices = loadPrices();
const evaluations = loadEvaluations().map(run => ({ ...run, model_cost: estimateModelCost(run, prices) }));
for (const result of evaluations) {
  const errors = evaluationErrors(result, [...providers, ...candidates]);
  if (errors.length) throw new Error(`${result.run_id}: ${errors.join('; ')}`);
}
generateEvaluations(evaluations, OUTPUT_ROOT);

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
function m1Status(pid: string): { verdict: 'pass' | 'fail'; passes: number; reps: number; date: string; transcript: string } | null {
  const runs = dryFireRunsByProvider.get(pid) ?? [];
  if (!runs.length) return null;
  const passes = runs.filter((r) => r.agent_claims?.result === 'pass').length;
  const latest = [...runs].sort((a, b) => a.date.localeCompare(b.date)).at(-1)!;
  return { verdict: passes * 2 > runs.length ? 'pass' : 'fail', passes, reps: runs.length, date: latest.date, transcript: latest.transcript };
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
  providers: providers.map(({ catalog, ...p }) => ({
    ...p, // New route claims are published separately, without legacy verification badges.
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
    notes: p.notes ?? [],
    m1: m1Status(p.id),
  })),
};
fs.writeFileSync(path.join(GENERATED_DIR, 'candidates.json'), JSON.stringify(candidatesOut, null, 2) + '\n');

// Searchable discovery catalog across both pools. Membership in the legacy
// provider index never promotes a newly documented route to a tested result.
const services = [
  ...providers.map(p => catalogService(p, 'provider', evaluations)),
  ...candidates.map(p => catalogService(p, 'candidate', evaluations)),
].sort((a, b) => a.id.localeCompare(b.id));
const catalogOut = {
  schema_version: 1,
  generated_at: new Date().toISOString(),
  description: 'Service discovery, documented access routes and separately reviewed task_runs. Source claims do not imply task success. Each run applies only to its route, task, configuration and date; invalid_run is not a service failure. Missing fields mean unknown, never zero cost or no requirements.',
  persona: 'Ordinary individual without a company, store, industry credentials, public website, audience or supplier contract. Country/payment eligibility must be checked separately.',
  categories,
  services,
};
fs.writeFileSync(path.join(GENERATED_DIR, 'catalog.json'), JSON.stringify(catalogOut, null, 2) + '\n');
const cell = (v: string) => v.replaceAll('|', '\\|').replaceAll('\n', ' ');
const catalogRows = (items: typeof services) => items.filter(s => s.catalog).flatMap(s => {
  const c = s.catalog!;
  const identity = `[${cell(s.name)}](../data/${s.record_pool === 'provider' ? 'providers' : 'candidates'}/${s.id}.yaml)`;
  if (!c.routes.length) return [`| ${identity} | ${c.classifications.join(', ')} | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |`];
  return c.routes.map(r => {
    const requirements = Object.entries(r.requirements ?? {}).filter(([, v]) => v.value === 'required').map(([k]) => k);
    const detail = [
      requirements.length ? `Requires: ${requirements.join(', ')}` : 'Requirements incomplete',
      ...(r.costs ?? []).map(x => `${x.amount} ${x.currency ?? x.unit} / ${x.per} (${x.kind}; ${x.scope})`),
      ...(r.human_steps ?? []).map(x => `Human: ${x.step}`),
      r.notes ?? '',
    ].filter(Boolean).join('; ');
    const observed = s.task_runs.filter(run => run.route_id === r.id).map(run =>
      `[${cell(run.task.id)}: ${run.status} (${run.started_at.slice(0, 10)})](../data/experiments/evaluations/${run.run_id}.json)`).join('; ') || 'not recorded';
    return `| ${identity} | ${c.classifications.join(', ')} | [${r.id} (${r.interface})](${r.entry_url}) | ${r.data_kind?.value ?? 'unknown'} | ${r.availability?.value ?? 'unknown'} | ${r.personal_access?.value ?? 'unknown'} | ${cell(detail)} | ${observed} |`;
  });
});
fs.writeFileSync(path.join(GENERATED_DIR, 'catalog.md'), `<!-- GENERATED FILE — do not edit. -->
# Service discovery catalog

Access, requirements and published costs below are **public-source claims**. Source URLs and per-fact dates are in each linked YAML and [catalog.json](./catalog.json). Separately reviewed task observations appear in the last column and the [results table](./evaluations.md); they do not certify other routes or tasks. Missing routes/fields mean unknown. See the [collection standard](../docs/catalog-standard.zh-CN.md).

Each row is an access route, not an independent data supplier. Services without an established route remain discoverable. No cost/quality ranking is implied.

${[...new Set(services.flatMap(s => s.catalog?.classifications ?? []))].sort().map(classification => `\n<a id="${classification.replaceAll('/', '-')}"></a>\n\n## ${classification}\n\n| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n${catalogRows(services.filter(s => s.catalog?.classifications.includes(classification))).join('\n')}`).join('\n')}
`);

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

// README is the entry point; detailed catalogs and historical experiments have their own pages.
// Derive coverage from task files and recorded runs so new domains appear on generation.
const taskDir = 'data/experiments/tasks';
const taskPages = fs.readdirSync(path.join(ROOT, taskDir)).filter(f => f.endsWith('.md') && f !== 'AGENTS.md')
  .sort().map(file => {
    const relative = `${taskDir}/${file}`;
    const source = fs.readFileSync(path.join(ROOT, relative), 'utf8');
    const classification = source.match(/^分类：(.+)$/m)?.[1].trim();
    if (!classification) return null;
    const ids = classification.match(/（([^）]+)）/)?.[1] ?? classification;
    const runs = evaluations.filter(r => r.task.file === relative);
    const serviceNames = [...new Set(runs.map(r => r.service_id))].sort()
      .map(id => [...providers, ...candidates].find(p => p.id === id)?.name ?? id).join(', ');
    return { relative, classification: classification.replace(/（[^）]+）/, '').trim(), ids, runs, serviceNames };
  }).filter(p => p !== null);
// Show services in their recorded categories; cross-category services share one source record.
const listedServices = [...providers, ...candidates].sort((a, b) => a.name.localeCompare(b.name));
const categoryZh: Record<string, string> = { travel: '旅行', databases: '数据库', 'web-search-data': '网页搜索与数据', 'productivity-storage': '协作办公与存储', 'ai-models': 'AI 模型', 'agent-tooling': 'Agent 工具', 'code-execution': '代码执行', 'developer-tools': '开发工具', 'cloud-hosting': '云服务与部署', 'payments-billing': '支付与账单', communication: '通信', 'observability-security': '监控与安全', 'commerce-marketing': '电商与营销' };
const priority = ['travel', 'databases', 'web-search-data', 'productivity-storage'];
const listedCategories = categories.filter(c => listedServices.some(p => p.category === c.id || p.catalog?.classifications.some(id => id.startsWith(`${c.id}/`))))
  .sort((a, b) => (priority.includes(a.id) ? priority.indexOf(a.id) : 99) - (priority.includes(b.id) ? priority.indexOf(b.id) : 99));
const accessLinks = (p: Provider, zh: boolean, compact = false) => {
  const links = serviceAccess(p, zh);
  const names = [...new Set(links.map(([name]) => name))];
  return (compact ? names.map(name => {
    const matches = links.filter(([n]) => n === name);
    return [name, matches.length === 1 ? matches[0][1] : `./generated/services.md#${p.id}-access`];
  }) : links).map(([name, url]) => `[${name}](${url})`).join(' · ') || '—';
};
const profileUrl = (id: string) => `./generated/services.md#${id}`;

// One readable profile per service, generated from the same records as the tables.
const taskTranslations = [...new Map(evaluations.map(r => [`${r.task.id}/${r.task.version}`, r.task])).values()].map(task => {
  const t = taskDisplay(task, false);
  return `<a id="${t.id}-${t.version}"></a>\n\n## ${t.description}\n\n${t.id} ${t.version} · [Original task definition](../${t.file})\n\n**Inputs:** ${t.inputs}\n\n**Expected output:** ${t.expected_output}\n\n**Completion criteria:** ${t.success}\n\n**Failure criteria:** ${t.failure}`;
});
fs.writeFileSync(path.join(GENERATED_DIR, 'tasks.en.md'), `<!-- GENERATED — display translations, not execution prompts. -->\n# Evaluated tasks\n\nEnglish translations of the recorded task versions. Original prompts and evidence remain unchanged; language requirements below describe the actual tests.\n\n${taskTranslations.join('\n\n')}\n`);
const boards = buildBoards(evaluations);
const profiles = listedServices.map(p => {
  const pool = providers.some(x => x.id === p.id) ? 'providers' : 'candidates';
  const source = `../data/${pool}/${p.id}.yaml`;
  const routes = p.catalog?.routes ?? [];
  const access = routes.length ? `| Route | Docs | Personal access | Requirements and human steps |\n| --- | --- | --- | --- |\n` + routes.map(r => {
    const requirements = Object.entries(r.requirements ?? {}).filter(([, v]) => v.value === 'required').map(([k]) => k);
    const preparation = [requirements.length ? `Requires: ${requirements.join(', ')}` : '', ...(r.human_steps ?? []).map(x => x.step), r.notes ?? ''].filter(Boolean).join('; ');
    const admission = [r.availability?.value, r.personal_access?.value].filter(v => v && v !== 'unknown').map(v => v!.replaceAll('_', ' ')).join(' / ') || '—';
    return `| [${cell(r.id)} (${r.interface.toUpperCase()})](${r.entry_url}) | ${r.docs ? `[Docs](${r.docs})` : '—'} | ${cell(admission)} | ${cell(preparation || '—')} |`;
  }).join('\n') : '—';
  const routeUrls = new Set(routes.flatMap(r => [r.entry_url, r.docs]));
  const extraLinks = serviceAccess(p).filter(([, url]) => !routeUrls.has(url))
    .map(([name, url]) => `[${name}](${url})`).join(' · ');
  const costClaims = routes.flatMap(r => (r.costs ?? []).map(c => `- ${cell(r.id)}: ${c.amount} ${c.currency ?? c.unit} / ${cell(c.per)} (${cell(c.kind)}; ${cell(c.scope)})`));
  const pricing = [p.entrypoints.pricing ? `[Official pricing](${[p.entrypoints.pricing].flat()[0]})` : '', ...costClaims].filter(Boolean).join('\n\n') || '—';
  const recorded = evaluations.filter(r => r.service_id === p.id);
  const results = renderServiceResults(p, boards, recorded);
  const sources = Object.values(p.catalog?.sources ?? {}).map(x => `- [${cell(x.kind)}](${x.url}) — checked ${x.checked_on}`).join('\n');
  return `<a id="${p.id}"></a>\n\n## ${p.name}\n\n${p.summary}\n\n[Website](${p.homepage}) · [Source record](${source}) · [Back to directory](../README.md#all-services)\n\n### Documentation and access <a id="${p.id}-access"></a>\n\n${extraLinks ? `${extraLinks}\n\n` : ''}${access}\n\n### Service pricing\n\n${pricing}\n\n${recorded.length ? `### Setup observations\n\n${renderSetup(p, recorded)}\n\n` : ''}### Task results\n\n${results}\n\n${p.notes?.length ? `### Notes\n\n${p.notes.map(note => `- ${note}`).join('\n')}\n\n` : ''}### Sources\n\n${sources || '—'}`;
});
fs.writeFileSync(path.join(GENERATED_DIR, 'services.md'), `<!-- GENERATED — edit source records; run npm run generate. -->\n# Service profiles\n\nToken and costs are means per valid trial, including successes and failures; invalid runs are excluded. Model costs use saved LiteLLM prices; ~ marks estimated service charges. — means no data. Setup costs are separate from business task costs. Access and pricing are source claims; a listed route does not establish task support. Compare only matching tasks and conditions.\n\n${profiles.join('\n\n')}\n`);
function serviceList(zh: boolean): string {
  const navigation = listedCategories.map(c => `[${zh ? categoryZh[c.id] ?? c.name : c.name}](#services-${c.id})`).join(' · ');
  const sections = listedCategories.map(c => {
    const categoryBoards = boards.filter(b => taskPages.find(t => t.relative === b.task_file)?.ids.split('/')[0] === c.id);

    const rows = listedServices.filter(p => p.category === c.id || p.catalog?.classifications.some(id => id.startsWith(`${c.id}/`))).map(p => {
      const identity = `[${cell(p.name)}](${profileUrl(p.id)})`;
      return { id: p.id, classifications: p.catalog?.classifications ?? [],
        unmeasured: `| ${identity} | — | — | — | — | — | ${accessLinks(p, zh, true)} |`,
        directory: `| ${identity} | ${cell(p.summary)} | ${accessLinks(p, zh, true)} |` };
    });
    const names = new Map(listedServices.map(p => [p.id, p.name]));
    const subcategories = (c.subcategories ?? []).filter(sub =>
      rows.some(r => r.classifications.includes(`${c.id}/${sub.id}`))
      || categoryBoards.some(b => taskPages.find(t => t.relative === b.task_file)?.ids === `${c.id}/${sub.id}`));
    const groups = subcategories.map(sub => {
      const id = `${c.id}/${sub.id}`;
      const task = taskPages.find(t => t.ids === id);
      return { id, name: zh ? (task?.classification.split(' / ').at(-1) ?? sub.name) : sub.name,
        rows: rows.filter(r => r.classifications.includes(id)),
        boards: categoryBoards.filter(b => taskPages.find(t => t.relative === b.task_file)?.ids === id) };
    });
    const remaining = rows.filter(r => !groups.some(g => g.rows.includes(r)));
    if (remaining.length || !groups.length) groups.push({ id: `${c.id}/other`, name: zh ? '其他服务' : 'Other services', rows: remaining,
      boards: categoryBoards.filter(b => !groups.some(g => g.boards.includes(b))) });
    const content = groups.map(group => {
      const measured = new Set(group.boards.flatMap(b => b.rows.map(r => r.service_id)));
      const pending = group.rows.filter(r => !measured.has(r.id));
      const selected = selectServiceBoards(group.boards);
      const interfaces = new Map(listedServices.flatMap(p => (p.catalog?.routes ?? []).map(r => [`${p.id}/${r.id}`, r.interface] as [string, string])));
      const measuredRows = renderBoardRows(selected, names, './', new Map(listedServices.map(p => [p.id, { profile: profileUrl(p.id), access: accessLinks(p, zh, true) }])), interfaces, zh);
      const table = group.boards.length
        ? readmeTable(`${boardHeader(zh, true)}\n${[measuredRows, ...pending.map(r => r.unmeasured)].filter(Boolean).join('\n')}`, true)
        : readmeTable(`${zh ? '| 服务 | 用途 | 接入资料 |' : '| Service | Purpose | Access links |'}\n| --- | --- | --- |\n${group.rows.map(r => r.directory).join('\n')}`, false);
      const details = renderBoardDetails(selected, names, zh, './', interfaces);
      const heading = subcategories.length ? `<a id="services-${group.id.replaceAll('/', '-')}"></a>\n\n#### ${group.name}\n\n` : '';
      return `${heading}${table}${details ? `\n\n<details>\n<summary>${zh ? '测了什么，怎么测的' : 'What we tested and how'}</summary>\n\n${details}\n\n</details>` : ''}`;
    }).join('\n\n');
    return `<a id="services-${c.id}"></a>\n\n### ${zh ? categoryZh[c.id] ?? c.name : c.name} (${rows.length})\n\n${content}`;
  });
  return `${navigation}\n\n${sections.join('\n\n')}`;
}

const readme = `<!-- GENERATED — edit scripts/generate.ts; run npm run generate. -->

# Agent-Friendly Services

English | [简体中文](./README.zh-CN.md)

**Find services that let your Agent complete tasks, and use real tests to compare reliability, setup effort and cost.**

We collect options for ordinary personal users and test them on real tasks. Browse the services below, open a name for its access requirements and sources, or follow a documentation link to get started.

<a id="all-services"></a>

## Services (${listedServices.length})

Tokens and costs are means per valid trial, including successes and failures; invalid runs are excluded. Model costs use LiteLLM prices; ~ marks estimated service charges. — means no data.

Each service shows its most recently tested route with valid results; other routes and setup are in the service details. These are observations, not a ranking: compare only matching tasks and conditions.

${serviceList(false)}

## For your Agent

[Query guide](./llms.txt) · [Catalog JSON](./generated/catalog.json) · [Results JSON](./generated/evaluations.json) · [MCP setup](./mcp/README.md)

Use \`search_services\` to find candidates, then \`get_service\` to check access requirements and test evidence. The same data is available directly as JSON.

## Methods and contributions

Know a service we missed, have a task you would like tested, or found something that has changed? A lead or correction is welcome.

[Principles](./AGENTS.md) · [Inclusion standards](./docs/catalog-standard.zh-CN.md) · [Flight findings](./docs/flights.zh-CN.md) · [Task design](./data/experiments/tasks/AGENTS.md) · [Execution and review](./data/experiments/AGENTS.md) · [All results and evidence](./generated/evaluations.md) · [Contributing](./docs/contributing.md) · [Issues](https://github.com/${REPO}/issues)

Code: [MIT](./LICENSE) · Data: [CC BY 4.0](./LICENSE-DATA).
`;
fs.writeFileSync(path.join(OUTPUT_ROOT, 'README.md'), readme);

const readmeZh = `<!-- 生成文件 — 修改 scripts/generate.ts，再运行 npm run generate。 -->

# Agent-Friendly Services

[English](./README.md) | 简体中文

**帮你找到能让 Agent 完成任务的服务，并用实测比较哪个更可靠、更省事、更有性价比。**

我们关注普通个人能用上的服务，收集候选，再用真实任务逐步验证。你可以按分类浏览，点服务名查看接入条件和资料，也可以直接打开文档开始使用。

<a id="all-services"></a>

## 服务目录（${listedServices.length}）

Token 和费用按有效试跑取平均，包含成功与失败；环境无效不计入。模型费用按 LiteLLM 估算，服务费用估算额标 ~。— 表示暂无数据。

每个服务展示最近取得有效结果的测试方式，其他方式和接入准备见服务详情。当前不排名，仅在任务与条件一致时比较。

${serviceList(true)}

## 给 Agent 的入口

[查询指引](./llms.txt) · [服务 JSON](./generated/catalog.json) · [实测 JSON](./generated/evaluations.json) · [MCP 配置](./mcp/README.md)

通过 \`search_services\` 查找候选，再用 \`get_service\` 查看接入条件和实测依据。同一份数据也可以直接读取 JSON。

## 方法与贡献

如果你知道我们漏掉的服务、有想测的真实任务，或发现资料已经过时，欢迎提供线索或纠错。

[核心理念](./AGENTS.md) · [收录标准](./docs/catalog-standard.zh-CN.md) · [机票阶段结论](./docs/flights.zh-CN.md) · [任务设计](./data/experiments/tasks/AGENTS.md) · [执行与验收](./data/experiments/AGENTS.md) · [全部实测与证据](./generated/evaluations.md) · [参与贡献](./docs/contributing.md) · [提出问题](https://github.com/${REPO}/issues)

代码：[MIT](./LICENSE) · 数据：[CC BY 4.0](./LICENSE-DATA)。
`;
fs.writeFileSync(path.join(OUTPUT_ROOT, 'README.zh-CN.md'), readmeZh);

console.log(`✓ Generated homepages, service profiles, catalogs and evaluations (${listedServices.length} services).`);
