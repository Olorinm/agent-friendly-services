/**
 * Generates README.md, generated/providers.json and generated/matrix.csv
 * from data/. Never edit those outputs by hand.
 */
import fs from 'node:fs';
import path from 'node:path';
import { ROOT, GENERATED_DIR, loadFields, loadCategories, loadProviders, daysSince, type Provider, type Check } from './lib.ts';

const STALE_DAYS = 180;

const fields = loadFields();
const categories = loadCategories();
const providers = loadProviders()
  .map((p) => p.data)
  .sort((a, b) => a.id.localeCompare(b.id));

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

function providerRow(p: Provider): string {
  return `| [${p.name}](#${p.id}) | ${entrySym(p, 'mcp_official')} | ${entrySym(p, 'llms_txt')} | ${entrySym(p, 'openapi')} | ${entrySym(p, 'cli')} | ${SYM[checkStatus(p, 'sandbox_or_test_mode')]} | ${selfServeSym(p)} | ${lastVerified(p) ?? '—'} |`;
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
const gapFields = ['llms_txt', 'openapi', 'mcp_official', 'agent_docs'] as const;
const gaps = gapFields
  .map((f) => ({ f, missing: providers.filter((p) => !p.entrypoints[f]).map((p) => p.id) }))
  .filter((g) => g.missing.length > 0);

const readme = `<!-- GENERATED FILE — do not edit. Run \`npm run generate\`. Source of truth: data/ -->

# Agent-Friendly Services

A community-maintained, evidence-backed directory of **service entry points for AI agents**: where the docs are, how to authenticate, what is machine-readable, and how fresh that information is.

**${providers.length} providers · ${jsonOut.counts.entrypoint_urls} verified entry links · ${jsonOut.counts.checks_answered} evidence-backed capability checks**

- 🤖 Agents: start with [\`generated/providers.json\`](./generated/providers.json) (full machine-readable dataset) and [\`llms.txt\`](./llms.txt)
- 🧑‍💻 Humans: browse the matrix below
- 🛠 Contributors: read [\`AGENTS.md\`](./AGENTS.md) and [\`docs/contributing.md\`](./docs/contributing.md) — every \`unknown\` below is a 15-minute contribution

## How To Read This

- **URL = fact.** Most questions ("is there an OpenAPI spec?") are answered with the link itself. Links are probed weekly ([\`generated/link-health.json\`](./generated/link-health.json)).
- **Checks** record behavior a URL can't express (self-serve signup, scoped tokens, idempotency…). \`supported\`/\`partial\` always carry an official evidence link and a verification date.
- **A missing link means "no known URL"**, not "confirmed absent". \`unknown\` means "checked, no reliable evidence found yet". Nobody guesses.
- Symbols: ✓ supported/available · ◐ partial · ✗ not supported · n/a not applicable · — unknown
- No scores, no tiers, no editorial ranking — only verifiable facts.

## Service Matrix

${categories
  .map((cat) => {
    const list = providers.filter((p) => p.category === cat.id);
    if (list.length === 0) return '';
    return `### ${cat.name}

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- |
${list.map(providerRow).join('\n')}`;
  })
  .filter(Boolean)
  .join('\n\n')}

## Providers

${providers
  .map((p) => {
    const b = badges(p);
    return `### ${p.name} <a id="${p.id}"></a>

> ${p.summary}

**Category:** ${catName(p.category)}${p.scope ? ` · **Scope:** ${p.scope}` : ''}${b.length ? ` · ${b.map((x) => `\`${x}\``).join(' ')}` : ''}

**Links:** ${entrypointLinks(p)}

${checksBlock(p)}
${p.notes?.length ? `\n${p.notes.map((n) => `> ${n}`).join('\n')}\n` : ''}`;
  })
  .join('\n')}

## Help Wanted 🌱

The fastest way to contribute is to resolve an \`unknown\`: find official evidence, add the URL, open a PR. **${totalUnknown} unknowns are open right now.**

${gaps.map((g) => `- \`${g.f}\` link unknown for: ${g.missing.map((id) => `[${id}](#${id})`).join(', ')}`).join('\n')}

You can also [add a provider](./docs/contributing.md#add-a-provider) (there is an issue form), report a broken link, or send your coding agent: this repo is designed so an agent pointed at [\`AGENTS.md\`](./AGENTS.md) can contribute end-to-end.

## Methodology

Facts only, evidence required, \`unknown\` is honest, freshness is tracked per check, links are probed weekly. Full write-up: [\`docs/methodology.md\`](./docs/methodology.md).

Related projects: [Fern Agent Score](https://buildwithfern.com/agent-score) and the [Agent-Friendly Docs Spec](https://github.com/fern-api/agent-score) (docs-site readiness scoring — we deliberately don't duplicate it), [Cloudflare Agent Readiness](https://blog.cloudflare.com/agent-readiness/), the [official MCP Registry](https://registry.modelcontextprotocol.io/) (authoritative MCP source we sync against), [llms.txt hub](https://llmstxthub.com/).

## License

Code: [MIT](./LICENSE) · Data (\`data/\`, \`generated/\`): [CC BY 4.0](./LICENSE-DATA)
`;

fs.writeFileSync(path.join(ROOT, 'README.md'), readme);

console.log(`✓ README.md, generated/providers.json, generated/matrix.csv`);
console.log(`  ${providers.length} providers · ${jsonOut.counts.entrypoint_urls} entry links · ${totalUnknown} unknowns open`);
