/**
 * Generates README.md, README.zh-CN.md, generated/providers.json and
 * generated/matrix.csv from data/. Never edit those outputs by hand.
 */
import fs from 'node:fs';
import path from 'node:path';
import { ROOT, GENERATED_DIR, loadFields, loadCategories, loadProviders, daysSince, type Provider, type Check } from './lib.ts';

const STALE_DAYS = 180;
const REPO = 'Olorinm/agent-friendly-services';
const RAW_JSON = `https://raw.githubusercontent.com/${REPO}/main/generated/providers.json`;

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

const badgeParts = [
  `![Providers](https://img.shields.io/badge/providers-${providers.length}-2563eb)`,
  linkHealth
    ? `[![Link health](https://img.shields.io/badge/link_health-${shieldText(`${linkHealth.ok} ok, ${linkHealth.broken} broken`)}-${linkHealth.broken > 0 ? 'e11d48' : '10b981'})](./generated/link-health.json)`
    : null,
  `[![Last update](https://img.shields.io/github/last-commit/${REPO}?label=last%20update&color=8b5cf6)](https://github.com/${REPO}/commits/main)`,
  `[![Data: CC BY 4.0](https://img.shields.io/badge/data-CC_BY_4.0-64748b)](./LICENSE-DATA)`,
].filter(Boolean);

const activeCategories = categories.filter((c) => providers.some((p) => p.category === c.id));

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

// generated/providers.md — the full per-provider fact sheets (kept out of the README).
const providersMd = `<!-- GENERATED FILE — do not edit. Run \`npm run generate\`. Source of truth: data/ -->

# Provider Details

Every known entry point and verified capability fact, with evidence links and dates.
Symbols: ✓ supported/available · ◐ partial · ✗ not supported · n/a not applicable · — unknown.
A missing link means **"no known URL"**, not "confirmed absent"; \`unknown\` means "checked, no reliable evidence found yet".
Links are probed weekly ([link-health.json](./link-health.json)); machine-readable version: [providers.json](./providers.json).

## Matrix

${activeCategories
  .map((cat) => {
    const list = providers.filter((p) => p.category === cat.id);
    return `### ${cat.name}

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- |
${list.map(providerRow).join('\n')}`;
  })
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
`;
fs.writeFileSync(path.join(GENERATED_DIR, 'providers.md'), providersMd);

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

function awesomeEntry(p: Provider, allFactsLabel: string): string {
  const summary = p.summary.replace(/\s+/g, ' ').trim().replace(/\.$/, '');
  return `- **[${p.name}](${p.entrypoints.docs})** — ${summary}. ${awesomeLinks(p, allFactsLabel)}`;
}

// GitHub heading slugs: lowercase, strip punctuation, each space becomes one hyphen.
const toc = activeCategories
  .map((c) => `[${c.name}](#${c.name.toLowerCase().replace(/[^a-z0-9\s-]/g, '').replace(/\s/g, '-')})`)
  .join(' · ');

function categorySections(allFactsLabel: string): string {
  return activeCategories
    .map((cat) => {
      const list = providers.filter((p) => p.category === cat.id);
      return `## ${cat.name}

${list.map((p) => awesomeEntry(p, allFactsLabel)).join('\n')}`;
    })
    .join('\n\n');
}

const readme = `<!-- GENERATED FILE — do not edit. Run \`npm run generate\`. Source of truth: data/ -->

# Agent-Friendly Services

English | [简体中文](./README.zh-CN.md)

Where AI agents plug into ${providers.length} popular services: docs, APIs, official MCP servers, llms.txt, CLIs. Every link machine-probed weekly; every capability fact backed by official evidence and a date. No scores, no tiers — [facts only](./docs/methodology.md).

${badgeParts.join('\n')}

**🤖 Agents** — add the MCP server, or fetch the whole dataset as one JSON file:

\`\`\`bash
# MCP server — tools: search_providers, get_provider, list_categories, get_stats
claude mcp add agent-friendly-services -- npx -y github:${REPO}

# Or skip the server: the same data as one JSON file
curl -s ${RAW_JSON}
\`\`\`

Other MCP clients: command \`npx\`, args \`["-y", "github:${REPO}"]\` ([details](./mcp/)). Repo map: [\`llms.txt\`](./llms.txt) · contribution manual: [\`AGENTS.md\`](./AGENTS.md).

**🧑‍💻 Humans** — browse below: each name links to the docs, the trailing links are what officially exists (a missing link means "no known URL", not "confirmed absent"). At-a-glance comparison: [capability matrix](${DETAILS}#matrix) · full fact sheets with evidence and dates: [provider details](${DETAILS}#providers) · spreadsheet: [\`matrix.csv\`](./generated/matrix.csv).

**🏢 Vendors** — fix your own entry in one PR with documentation (not marketing) as evidence; promotional PRs are declined ([rules](./docs/contributing.md)).

---

${toc}

${categorySections('all facts →')}

## Contributing

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

AI 智能体接入 ${providers.length} 个主流服务的入口索引：文档、API、官方 MCP 服务器、llms.txt、CLI。所有链接每周机器探测；每条能力事实都附官方证据链接和验证日期。不打分、不分级 —— [只记录事实](./docs/methodology.md)。

${badgeParts.join('\n')}

**🤖 智能体** —— 添加 MCP 服务器，或直接把完整数据集当一个 JSON 文件拉取：

\`\`\`bash
# MCP 服务器 —— 工具：search_providers、get_provider、list_categories、get_stats
claude mcp add agent-friendly-services -- npx -y github:${REPO}

# 不装服务器也行：同一份数据就是一个 JSON 文件
curl -s ${RAW_JSON}
\`\`\`

其他 MCP 客户端：command \`npx\`，args \`["-y", "github:${REPO}"]\`（[详情](./mcp/)）。仓库地图：[\`llms.txt\`](./llms.txt) · 智能体贡献手册：[\`AGENTS.md\`](./AGENTS.md)。

**🧑‍💻 人类** —— 直接往下浏览：服务名链到官方文档，后面跟着的是官方确认存在的入口（没有链接表示"暂无已知 URL"，不代表"确认不存在"）。一眼对比各家能力：[能力矩阵表](${DETAILS}#matrix) · 带证据和日期的完整事实表：[提供商详情](${DETAILS}#providers) · 表格版：[\`matrix.csv\`](./generated/matrix.csv)。

**🏢 服务商** —— 欢迎自己维护自己的条目：一个 PR、以文档（而非营销页）为证据；推广性 PR 会被拒绝（[规则](./docs/contributing.md)）。

> 提供商简介与详情页保持英文原文（数据单一来源，避免翻译漂移）；本页仅翻译框架文字。

---

${toc}

${categorySections('全部事实 →')}

## 参与贡献

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

console.log(`✓ README.md, README.zh-CN.md, generated/providers.json, generated/matrix.csv`);
console.log(`  ${providers.length} providers · ${jsonOut.counts.entrypoint_urls} entry links · ${totalUnknown} unknowns open`);
