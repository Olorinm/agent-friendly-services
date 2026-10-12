/**
 * Generates README.md, README.zh-CN.md, generated/providers.json and
 * generated/matrix.csv from data/. Never edit those outputs by hand.
 */
import fs from 'node:fs';
import path from 'node:path';
import * as yaml from 'js-yaml';
import { ROOT, legacyTaskCategory, loadFields, loadCategories, loadProviders, loadCandidates, daysSince, type Provider, type Check } from './lib.ts';
import { catalogService } from './catalog.ts';
import { flattenCategories, inClassification, serviceClassifications, withinClassification, classificationLabel } from './taxonomy.mjs';
import { generateResearch } from './research.ts';
import { loadPrices, estimateModelCost } from './model-costs.ts';
import { readmeTable } from './readme-table.ts';
import { taskDisplay } from './task-display.ts';
import { taskClassification } from './task-classifications.ts';
import { serviceAccess } from './service-access.ts';
import { renderServiceResults, renderSetup } from './service-results.ts';
import { buildBoards, selectServiceBoards, renderBoardRows, renderBoardDetails, boardHeader, credentialText, interfaceLabel, moneyLabel, type Board, type BoardRow } from './leaderboard.ts';
import { loadEvaluations, evaluationErrors, generateEvaluations, type Evaluation } from './evaluations.ts';

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
  description: 'Service discovery, access_links for integration documentation, documented access routes and separately reviewed task_runs. Documentation links are not executable endpoints. Source claims do not imply task success. Each run applies only to its route, task, configuration and date; invalid_run is not a service failure. Missing fields mean unknown, never zero cost or no requirements.',
  persona: 'Ordinary individual without a company, store, industry credentials, public website, audience or supplier contract. Country/payment eligibility must be checked separately.',
  categories,
  services,
};
fs.writeFileSync(path.join(GENERATED_DIR, 'catalog.json'), JSON.stringify(catalogOut, null, 2) + '\n');
const cell = (v: string) => v.replaceAll('|', '\\|').replaceAll('\n', ' ');
const catalogRows = (items: typeof services, classification: string) => items.filter(s => s.catalog).flatMap(s => {
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
    const observed = s.task_runs.filter(run => run.route_id === r.id && withinClassification(run.classification, classification)).map(run =>
      `[${cell(run.task.id)}: ${run.status} (${run.started_at.slice(0, 10)})](../data/experiments/evaluations/${run.run_id}.json)`).join('; ') || 'not recorded';
    return `| ${identity} | ${c.classifications.join(', ')} | [${r.id} (${r.interface})](${r.entry_url}) | ${r.data_kind?.value ?? 'unknown'} | ${r.availability?.value ?? 'unknown'} | ${r.personal_access?.value ?? 'unknown'} | ${cell(detail)} | ${observed} |`;
  });
});
fs.writeFileSync(path.join(GENERATED_DIR, 'catalog.md'), `<!-- GENERATED FILE — do not edit. -->
# Service discovery catalog

Access, requirements and published costs below are **public-source claims**. Source URLs and per-fact dates are in each linked YAML and [catalog.json](./catalog.json). Separately reviewed task observations appear in the last column and the [results table](./evaluations.md); they do not certify other routes or tasks. Missing routes/fields mean unknown. See the [collection standard](../docs/catalog-standard.zh-CN.md).

Each row is an access route, not an independent data supplier. Services without an established route remain discoverable. No cost/quality ranking is implied.

${flattenCategories(categories).filter(node => services.some(s => inClassification(s, node.path))).map(node => {
  const items = services.filter(s => serviceClassifications(s).includes(node.path));
  const children = (node.subcategories ?? []).filter(child => services.some(s => inClassification(s, `${node.path}/${child.id}`)));
  const links = children.map(child => `[${child.name}](#${node.path.replaceAll('/', '-')}-${child.id})`).join(' · ');
  return `\n<a id="${node.path.replaceAll('/', '-')}"></a>\n\n## ${classificationLabel(categories, node.path)}\n\n${node.description}\n\n**Includes:** ${node.inclusion}\n\n**Boundary:** ${node.exclusion}\n\n${links}${items.length ? `\n\n| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n${catalogRows(items, node.path).join('\n')}` : ''}`;
}).join('\n')}
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
${agentRunsTable(p, '../') ? `\n**Agent runs** — a real agent climbed this category's [task ladder](../data/experiments/tasks/${legacyTaskCategory(p)}.yaml), every result independently verified ([method](../docs/agent-verification.md) · [all runs](./agent-runs.md#${p.id})):\n\n${agentRunsTable(p, '../')}\n` : ''}${p.notes?.length ? `\n${p.notes.map((n) => `> ${n}`).join('\n')}\n` : ''}`;
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

Task: \`${(agentRunsByProvider.get(p.id) ?? [])[0]?.task}\` ([definition](../data/experiments/tasks/${legacyTaskCategory(p)}.yaml)) · [provider facts](./providers.md#${p.id})

${agentRunsTable(p, '../')}
${notes.length ? `\n**Run notes** (agent-reported, verbatim):\n\n${notes.join('\n')}` : ''}`;
  })
  .join('\n\n')}`}
`;
fs.writeFileSync(path.join(GENERATED_DIR, 'agent-runs.md'), agentRunsMd);

// README is the entry point; detailed catalogs and historical experiments have their own pages.
// Show services in their recorded categories; cross-category services share one source record.
const listedServices = [...providers, ...candidates].sort((a, b) => a.name.localeCompare(b.name));
const priority = ['travel', 'databases', 'search-scraping', 'maps-geo', 'weather-calendar', 'financial-data', 'scholarly', 'productivity-storage'];
const listedCategories = categories.filter(c => listedServices.some(p => inClassification(p, c.id)))
  .sort((a, b) => (priority.includes(a.id) ? priority.indexOf(a.id) : 99) - (priority.includes(b.id) ? priority.indexOf(b.id) : 99));
const accessLinks = (p: Provider, zh: boolean) => serviceAccess(p, zh).map(([name, url]) => `[${name}](${url})`).join(' · ') || '—';
const profileUrl = (id: string, prefix = './') => `${prefix}generated/services.md#${id}`;

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
  const rawLinks: [string, string][] = Object.entries({ docs: 'Docs', api_reference: 'API reference', cli: 'CLI', sdks: 'SDK', mcp_official: 'MCP entry', mcp_docs: 'MCP setup' })
    .flatMap(([field, label]) => [p.entrypoints[field] ?? []].flat().map(url => [label, url] as [string, string]));
  const extraLinks = rawLinks.filter(([, url], i) => !routeUrls.has(url) && rawLinks.findIndex(([, other]) => other === url) === i)
    .map(([name, url]) => `[${name}](${url})`).join(' · ');
  const costClaims = routes.flatMap(r => (r.costs ?? []).map(c => `- ${cell(r.id)}: ${c.amount} ${c.currency ?? c.unit} / ${cell(c.per)} (${cell(c.kind)}; ${cell(c.scope)})`));
  const pricing = [p.entrypoints.pricing ? `[Official pricing](${[p.entrypoints.pricing].flat()[0]})` : '', ...costClaims].filter(Boolean).join('\n\n') || '—';
  const recorded = evaluations.filter(r => r.service_id === p.id);
  const results = renderServiceResults(p, boards.filter(b => b.phase === 'business'), recorded.filter(r => taskClassification(r.task).phase === 'business'));
  const setupRecords = recorded.filter(r => taskClassification(r.task).phase === 'setup');
  const setupResults = renderServiceResults(p, boards.filter(b => b.phase === 'setup'), setupRecords);
  const scopeNotes = [...(p.catalog?.notes ?? []), ...(p.notes ?? [])];
  const sources = Object.values(p.catalog?.sources ?? {}).map(x => `- [${cell(x.kind)}](${x.url}) — checked ${x.checked_on}`).join('\n');
  return `<a id="${p.id}"></a>\n\n## ${p.name}\n\n${p.summary}\n\n**Classification:** ${serviceClassifications(p).map(id => classificationLabel(categories, id)).join('; ')}\n\n[Website](${p.homepage}) · [Source record](${source}) · [Back to directory](./directory.md)\n\n### Documentation and access <a id="${p.id}-access"></a>\n\n${extraLinks ? `${extraLinks}\n\n` : ''}${access}\n\n### Service pricing\n\n${pricing}\n\n${recorded.length ? `### Setup observations\n\n${renderSetup(p, recorded)}${setupRecords.length ? `\n\n${setupResults}` : ''}\n\n` : ''}### Task results\n\n${results}\n\n${scopeNotes.length ? `### Notes\n\n${scopeNotes.map(note => `- ${note}`).join('\n')}\n\n` : ''}### Sources\n\n${sources || '—'}`;
});
fs.writeFileSync(path.join(GENERATED_DIR, 'services.md'), `<!-- GENERATED — edit source records; run npm run generate. -->\n# Service profiles\n\nToken and costs are means per valid trial, including successes and failures; invalid runs are excluded. Model costs use saved LiteLLM prices; ~ marks estimated service charges. — means no data. Setup costs are separate from business task costs. Access and pricing are source claims; a listed route does not establish task support. Compare only matching tasks and conditions.\n\n${profiles.join('\n\n')}\n`);
// prefix: path from the rendering file to the repo root.
function serviceList(zh: boolean, prefix = './'): string {
  const navigation = listedCategories.map(c => `[${zh ? c.name_zh ?? c.name : c.name}](#services-${c.id})`).join(' · ');
  const names = new Map(listedServices.map(p => [p.id, p.name]));
  const interfaces = new Map(listedServices.flatMap(p => (p.catalog?.routes ?? []).map(r => [`${p.id}/${r.id}`, r.interface] as [string, string])));
  const links = new Map(listedServices.map(p => [p.id, { profile: profileUrl(p.id, prefix), access: accessLinks(p, zh) }]));
  const renderResults = (groupBoards: typeof boards, members: typeof listedServices) => {
    const selected = selectServiceBoards(groupBoards);
    const measured = new Set(selected.flatMap(b => b.rows.map(r => r.service_id)));
    const pending = members.filter(p => !measured.has(p.id));
    const measuredRows = renderBoardRows(selected, names, prefix, links, interfaces, zh);
    const table = readmeTable(`${boardHeader(zh, true)}\n${[measuredRows, ...pending.map(p =>
      `| [${cell(p.name)}](${profileUrl(p.id, prefix)}) | — | — | — | — | — | ${accessLinks(p, zh)} |`)].filter(Boolean).join('\n')}`, true);
    const details = renderBoardDetails(selected, names, zh, prefix, interfaces);
    return `${table}${details ? `\n\n<details>\n<summary>${zh ? '测了什么，怎么测的' : 'What we tested and how'}</summary>\n\n${details}\n\n</details>` : ''}`;
  };
  const renderNode = (node: typeof categories[number], id: string, depth: number): string => {
    const members = listedServices.filter(p => inClassification(p, id));
    const scopedBoards = boards.filter(b => b.classification === id);
    const children = (node.subcategories ?? []).filter(child => listedServices.some(p => inClassification(p, `${id}/${child.id}`))
      || boards.some(b => withinClassification(b.classification, `${id}/${child.id}`)));
    if (!members.length && !scopedBoards.length && !children.length) return '';
    const direct = members.filter(p => serviceClassifications(p).includes(id));
    const business = scopedBoards.filter(b => b.phase === 'business');
    const setup = scopedBoards.filter(b => b.phase === 'setup');
    const content: string[] = [];
    if (setup.length) content.push(`<details>\n<summary>${zh ? '接入测试（单独记录）' : 'Setup tests (recorded separately)'}</summary>\n\n${renderResults(setup, [])}\n\n</details>`);
    if (direct.length || business.length) {
      if (children.length && direct.length) content.push(zh ? '以下服务暂按本层范围收录，细分缺口见服务详情。' : 'These services remain at this scope; see their profiles for unresolved classification details.');
      content.push(business.length ? renderResults(business, direct) : readmeTable(
        `${zh ? '| 服务 | 用途 | 接入资料 |' : '| Service | Purpose | Access links |'}\n| --- | --- | --- |\n${direct.map(p =>
          `| [${cell(p.name)}](${profileUrl(p.id, prefix)}) | ${cell(p.summary)} | ${accessLinks(p, zh)} |`).join('\n')}`, false));
    }
    content.push(...children.map(child => renderNode(child, `${id}/${child.id}`, depth + 1)));
    return `<a id="services-${id.replaceAll('/', '-')}"></a>\n\n${'#'.repeat(Math.min(depth + 3, 6))} ${zh ? node.name_zh ?? node.name : node.name} (${members.length})\n\n${content.join('\n\n')}`;
  };
  return `${navigation}\n\n${listedCategories.map(c => renderNode(c, c.id, 0)).join('\n\n')}`;
}

// Full directory: every listed service with its test details. The homepage links here.
const directoryPage = (zh: boolean) => `<!-- ${zh ? '生成文件 — 修改 scripts/generate.ts，再运行 npm run generate。' : 'GENERATED — edit scripts/generate.ts; run npm run generate.'} -->

# ${zh ? `完整服务目录（${listedServices.length}）` : `Service directory (${listedServices.length})`}

${zh ? '[← 返回首页](../README.zh-CN.md) · [English](./directory.md)' : '[← Back to overview](../README.md) · [简体中文](./directory.zh-CN.md)'}

${zh ? `Token 和费用按有效试跑取平均，包含成功与失败；环境无效不计入。模型费用按 LiteLLM 估算，服务费用估算额标 ~。— 表示暂无数据。

完成率描述 Agent 在记录的环境及约束下是否交付完整任务，不等于服务可用率；未完成须结合具体阻碍及已验证的服务能力阅读。只测一次且完成，也会显示 100%。次数、任务与条件见[完整结果](./evaluations.md)；有限观察不能证明长期可靠性。

每个分类内按任务组展示服务最近取得有效结果的测试方式，接入测试单独展示，其他方式见服务详情。当前不排名，仅在任务与条件一致时比较。准备说明不同的记录分别统计，包括包下载源或请求上限的变化；历次试跑均保留在完整记录中。` : `Tokens and costs are means per valid trial, including successes and failures; invalid runs are excluded. Model costs use LiteLLM prices; ~ marks estimated service charges. — means no data.

Resolution rates describe complete task delivery by the tested Agent under the recorded conditions, not service availability. Read incomplete runs alongside their blockers and any verified service-side results. A single completed trial displays 100%. Open the [full results](./evaluations.md) for counts, tasks and conditions; these limited observations do not establish long-term reliability.

Within each classification and task family, each service shows its most recently tested route with valid results; other routes and setup are in the service details. These are observations, not a ranking: compare only matching tasks and conditions. Different preparation notes are kept separate, including changes to package sources or request limits; all earlier trials remain in the full records.`}

${serviceList(zh, '../')}
`;
fs.writeFileSync(path.join(GENERATED_DIR, 'directory.md'), directoryPage(false));
fs.writeFileSync(path.join(GENERATED_DIR, 'directory.zh-CN.md'), directoryPage(true));

// Homepage: what is measured, curated findings, then only the tested classifications.
const highlights = (yaml.load(fs.readFileSync(path.join(ROOT, 'data/highlights.yaml'), 'utf8')) as
  { highlights: { date: string; zh: string; en: string; link: string }[] }).highlights;
const serviceNames = new Map(listedServices.map(p => [p.id, p.name]));
const routeInterfaces = new Map(listedServices.flatMap(p => (p.catalog?.routes ?? []).map(r => [`${p.id}/${r.id}`, r.interface] as [string, string])));
const validRuns = evaluations.filter(r => r.status !== 'invalid_run');
const testedIds = new Set(validRuns.map(r => r.service_id));
const lastRun = validRuns.map(r => r.started_at).sort().at(-1)?.slice(0, 10) ?? '—';
const directoryUrl = (zh: boolean, id?: string) => `./generated/directory${zh ? '.zh-CN' : ''}.md${id ? `#services-${id.replaceAll('/', '-')}` : ''}`;

// Starting point recorded for the run, never inferred from the task outcome.
type AccessKind = 'anonymous' | 'self-serve' | 'supplied' | 'unknown';
function accessKind(r: Evaluation): AccessKind {
  const value = credentialText(r).toLowerCase();
  if (/created inside measured execution|generated anonymous/.test(value)) return 'self-serve';
  if (value.startsWith('provided') || /existing|registered|preprovided/.test(value)) return 'supplied';
  if (value.startsWith('none')) return 'anonymous';
  return 'unknown';
}
// Whether a person must register before the Agent starts, from the least demanding
// recorded starting point. Identities the Agent creates during the run need no prior signup.
const SIGNUP: Record<Exclude<AccessKind, 'unknown'>, [string, string]> = {
  anonymous: ['✅', '✅'],
  'self-serve': ['✅', '✅'],
  supplied: ['❌', '❌'],
};
const signupLabel = (runs: Evaluation[], zh: boolean) => {
  const kinds = new Set(runs.map(accessKind));
  const kind = (['anonymous', 'self-serve', 'supplied'] as const).find(k => kinds.has(k));
  return kind ? SIGNUP[kind][zh ? 0 : 1] : '—';
};

// One leaderboard per classification: one row per service and interface, pooling every
// valid trial recorded for that classification (setup tasks of an ancestor included).
function leaderboard(zh: boolean, id: string): { id: string; cells: string[][] } | null {
  const recorded = (r: Evaluation) => taskClassification(r.task).classification;
  // A run recorded at a parent (a shared setup task) belongs with the service's own subcategory
  // when the service has no deeper results to share it with.
  const own = (r: Evaluation) => {
    const c = recorded(r);
    if (evaluations.some(x => x.service_id === r.service_id && recorded(x).startsWith(`${c}/`))) return c;
    const service = listedServices.find(p => p.id === r.service_id);
    return (service && serviceClassifications(service).find(x => x.startsWith(`${c}/`))) ?? c;
  };
  const here = evaluations.filter(r => own(r) === id);
  const deeper = new Set(evaluations.filter(r => own(r).startsWith(`${id}/`)).map(r => r.service_id));
  const services = new Set(here.map(r => r.service_id).filter(s => !deeper.has(s) || here.some(r => r.service_id === s && taskClassification(r.task).phase === 'business')));
  // Ancestor-level setup runs count toward the closest classification where the service has results.
  const ancestors = evaluations.filter(r => id.startsWith(`${own(r)}/`) && services.has(r.service_id));
  const routes = new Map<string, Evaluation[]>();
  for (const run of [...here.filter(r => services.has(r.service_id)), ...ancestors]) {
    // Route IDs also distinguish entry URL revisions; users compare by interface.
    const key = `${run.service_id}/${interfaceLabel(routeInterfaces.get(`${run.service_id}/${run.route_id}`), zh)}`;
    routes.set(key, [...(routes.get(key) ?? []), run]);
  }
  const rows = [...routes.entries()].map(([key, runs]) => {
    const valid = runs.filter(r => r.status !== 'invalid_run');
    const passed = valid.filter(r => r.status === 'completed').length;
    const costs = valid.map(r => r.model_cost?.amount_usd == null ? null : r.model_cost.amount_usd + (r.service_cost_usd ?? 0)).filter((v): v is number => v !== null);
    return { key, runs, valid, passed, rate: valid.length ? passed / valid.length : null,
      cost: costs.length ? costs.reduce((a, b) => a + b, 0) / costs.length : null };
  }).filter(row => row.runs.length);
  if (!rows.length) return null;
  rows.sort((a, b) => (b.rate ?? -1) - (a.rate ?? -1) || b.valid.length - a.valid.length || (a.cost ?? Infinity) - (b.cost ?? Infinity));
  const cells = rows.map(row => {
    const [service, via] = row.key.split('/');
    const latest = [...row.runs].sort((a, b) => b.started_at.localeCompare(a.started_at))[0];
    const rate = row.rate === null ? (zh ? '环境无效' : 'invalid run') : `**${Math.round(100 * row.rate)}%**（${row.passed}/${row.valid.length}）`;
    return [`[${cell(serviceNames.get(service) ?? service)}](${profileUrl(service)})`, zh ? rate : rate.replace('（', ' (').replace('）', ')'),
      moneyLabel(row.cost), `[${via}](${latest.entry_url})`, signupLabel(row.valid.length ? row.valid : row.runs, zh)];
  });
  return { id, cells };
}

// GitHub sizes each table to its content and ignores width attributes. Padding every
// header past the widest cell in its column gives all leaderboards identical columns.
const textWidth = (markdown: string) => [...markdown.replace(/\[([^\]]*)\]\([^)]*\)/g, '$1').replaceAll('**', '')]
  .reduce((sum, ch) => sum + (/[\u2E80-\uFFEF]|\p{Extended_Pictographic}/u.test(ch) ? 1 : .6), 0);
function leaderboardTables(zh: boolean, boards: { id: string; cells: string[][] }[]): string[] {
  const headers = zh ? ['服务', '通过率', '平均费用', '方式', '免注册'] : ['Service', 'Pass rate', 'Avg. cost', 'Via', 'No signup'];
  const NBSP_EM = .28;
  const padded = headers.map((header, i) => {
    const widest = Math.max(textWidth(header), ...boards.flatMap(b => b.cells.map(row => textWidth(row[i]))));
    const pad = Math.max(0, Math.ceil((widest + 1 - textWidth(header)) / NBSP_EM));
    // Centre short headers over centred columns; otherwise pad after the text.
    return i === 4 ? `${'&nbsp;'.repeat(Math.floor(pad / 2))}${header}${'&nbsp;'.repeat(Math.ceil(pad / 2))}` : `${header}${'&nbsp;'.repeat(pad)}`;
  });
  // Top-level categories become sections; tables are titled relative to their category.
  const title = (id: string) => classificationLabel(categories, id, zh).split(' / ').slice(id.includes('/') ? 1 : 0).join(' · ');
  return boards.map(board => `### ${title(board.id)} [→](${directoryUrl(zh, board.id)})\n\n| ${padded.join(' | ')} |\n| :--- | ---: | ---: | :--- | :---: |\n${board.cells.map(row => `| ${row.join(' | ')} |`).join('\n')}`);
}

function homepage(zh: boolean): string {
  const label = (cn: string, en: string) => zh ? cn : en;
  const nodes = listedCategories.flatMap(c => flattenCategories([c]).map(n => n.path));
  const measured = nodes.map(id => leaderboard(zh, id)).filter(b => b !== null);
  // Pad against every table on the page so columns line up across sections too.
  const tables = leaderboardTables(zh, measured);
  const rendered = new Map(measured.map((board, i) => [board.id, tables[i]]));
  const shown = listedCategories.filter(c => measured.some(b => withinClassification(b.id, c.id)));
  const sections = shown.map(c => `<a id="results-${c.id}"></a>\n\n## ${zh ? c.name_zh ?? c.name : c.name}\n\n${measured
    .filter(b => withinClassification(b.id, c.id)).map(b => rendered.get(b.id)).join('\n\n')}`);
  const navigation = shown.map(c => `[${zh ? c.name_zh ?? c.name : c.name}](#results-${c.id})`).join(' · ');
  const directory = listedCategories.map(c => {
    const members = listedServices.filter(p => inClassification(p, c.id));
    const tested = members.filter(p => testedIds.has(p.id)).length;
    return `- [${zh ? c.name_zh ?? c.name : c.name}](${directoryUrl(zh, c.id)}) — ${zh ? `${members.length} 个服务，已实测 ${tested}` : `${members.length} services, ${tested} tested`}`;
  });
  return `<!-- ${label('生成文件 — 修改 scripts/generate.ts，再运行 npm run generate。', 'GENERATED — edit scripts/generate.ts; run npm run generate.')} -->

# Agent-Friendly Services

${zh ? '[English](./README.md) | 简体中文' : 'English | [简体中文](./README.zh-CN.md)'}

**${label('哪些服务能让 AI Agent 真正把事办成？我们让 Agent 用真实任务去试，记录通过率、费用和接入门槛。',
  'Which services let an AI Agent actually get the job done? We have Agents try real tasks and record pass rate, cost and access requirements.')}**

${label(`**${listedServices.length}** 个服务 · **${testedIds.size}** 个已实测 · **${validRuns.length}** 次有效试跑 · 最近一次 ${lastRun}`,
  `**${listedServices.length}** services · **${testedIds.size}** tested · **${validRuns.length}** valid trials · latest ${lastRun}`)}

${label(
  '**通过率**：该子类所有任务（含接入任务）中通过独立验收的试跑比例，括号内为通过数 / 有效试跑数。**平均费用**：每次试跑的模型费用（按 LiteLLM 价表估算）加有记录的服务费，取平均。**免注册**：✅ 不用事先注册即可使用 · ❌ 需要事先准备账号或密钥。环境故障导致的无效试跑不计入。点子类标题旁的 → 查看各任务明细。',
  '**Pass rate**: share of valid trials, across all tasks in the subcategory including setup, that passed independent review (passed / valid trials). **Avg. cost**: mean per trial of estimated model cost (LiteLLM rates) plus recorded service charges. **No signup**: ✅ usable without registering first · ❌ an account or key must be prepared first. Runs invalidated by environment faults are excluded. Use → beside a subcategory for per-task results.')}

${navigation}

${sections.join('\n\n')}

## ${label('怎么测的', 'How we test')}

${label(
  '每次试跑都是全新会话和隔离容器，被测 Agent 只拿到用户任务和服务入口，看不到答案或其他服务的结果；另起一个会话按事先冻结的标准验收。用量取自运行器抓包，证据带哈希，可复查、可复跑。样本还少，结果是观察，不是长期可靠性的证明。',
  'Each trial runs in a fresh session and isolated container. The tested Agent gets only the user task and service entry point, never answers or other services\' results; a separate session reviews it against frozen criteria. Usage comes from runner capture and evidence carries hashes, so results can be checked and rerun. Samples are still small: these are observations, not proof of long-term reliability.')} [${label('方法', 'Method')}](./AGENTS.md)

## ${label('最新发现', 'Latest findings')}

${highlights.map(h => `- ${zh ? h.zh : h.en} [${label('证据', 'Evidence')}](./${h.link})`).join('\n')}

## ${label('完整目录', 'Full directory')}

${label('所有收录的服务（包括还没测的），以及每个任务的原文、配置和逐次结果：', 'Every listed service, including untested ones, with each task\'s text, configuration and per-trial results:')}

${directory.join('\n')}

${label('想测某个服务或任务？欢迎', 'Want a service or task tested? ')}[${label('提 Issue', 'Open an issue')}](https://github.com/${REPO}/issues)${label('。', '.')}

## ${label('给 Agent 的入口', 'For your Agent')}

[${label('查询指引', 'Query guide')}](./llms.txt) · [${label('服务 JSON', 'Catalog JSON')}](./generated/catalog.json) · [${label('实测 JSON', 'Results JSON')}](./generated/evaluations.json) · [${label('MCP 配置', 'MCP setup')}](./mcp/README.md)

## ${label('方法与贡献', 'Methods and contributions')}

[${label('核心理念', 'Principles')}](./AGENTS.md) · [${label('收录标准', 'Inclusion standards')}](./docs/catalog-standard.zh-CN.md) · [${label('机票阶段结论', 'Flight findings')}](./docs/flights.zh-CN.md) · [${label('任务设计', 'Task design')}](./data/experiments/tasks/AGENTS.md) · [${label('执行与验收', 'Execution and review')}](./data/experiments/AGENTS.md) · [${label('全部实测与证据', 'All results and evidence')}](./generated/evaluations.md) · [${label('参与贡献', 'Contributing')}](./docs/contributing.md)

${label('代码：', 'Code: ')}[MIT](./LICENSE) · ${label('数据：', 'Data: ')}[CC BY 4.0](./LICENSE-DATA)
`;
}
fs.writeFileSync(path.join(OUTPUT_ROOT, 'README.md'), homepage(false));
fs.writeFileSync(path.join(OUTPUT_ROOT, 'README.zh-CN.md'), homepage(true));

console.log(`✓ Generated homepages, service profiles, catalogs and evaluations (${listedServices.length} services).`);
