import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { ROOT, type Provider } from './lib.ts';
import type { ModelCost } from './model-costs.ts';
import { buildBoards, selectServiceBoards, moneyLabel } from './leaderboard.ts';

export interface Evaluation {
  schema_version: 1;
  run_id: string; service_id: string; route_id: string; entry_url: string;
  task: { id: string; file: string; version: string | null; sha256: string; description: string;
    inputs: string; expected_output: string; success: string; failure: string };
  prompt_sha256: string;
  harness: { name: string; version: string; mode: string; launcher?: string; launcher_sha256?: string };
  model: string; reasoning_effort: string; started_at: string; ended_at: string;
  elapsed_seconds: number; budget_seconds: number; environment: Record<string, unknown>;
  status: 'completed' | 'not_completed' | 'invalid_run'; reason: string;
  usage: null | { input_tokens: number; cached_input_tokens: number; output_tokens: number;
    reasoning_output_tokens?: number; cache_write_input_tokens?: number };
  request_usage?: { status: 'complete' | 'incomplete'; method: string; reason: string; source_sha256: string | null;
    requests: NonNullable<Evaluation['usage']>[]; totals?: NonNullable<Evaluation['usage']> };
  model_cost?: ModelCost;
  service_cost?: { kind: 'reported' | 'estimated' | 'confirmed_free' | 'unknown'; amount_usd: number | null;
    sources: string[]; note: string; items?: { quantity: number; unit: string; usd_per_unit: number }[] };
  service_cost_usd: number | null; human_interventions: number | null;
  review: { method: string; reviewer: string; reviewed_at: string;
    checks: { criterion: string; passed: boolean; evidence: string }[] };
  evidence: { path: string; sha256: string; note: string; source_sha256?: string; redactions?: string[] }[];
  provenance: { local_run_dir: string; run_sha256: string; events_sha256: string | null;
    answer_sha256: string | null; review_sha256: string; privacy_note?: string };
}

export function loadEvaluations(root = ROOT): Evaluation[] {
  const dir = path.join(root, 'data/experiments/evaluations');
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter(f => f.endsWith('.json')).sort().map(f => {
    const value = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
    if (value.run_id !== f.slice(0, -5)) throw new Error(`${f}: run_id must match filename`);
    return value;
  });
}

const nonnegative = (v: unknown) => typeof v === 'number' && Number.isFinite(v) && v >= 0;
const hash = (v: unknown) => typeof v === 'string' && /^[a-f0-9]{64}$/.test(v);
const text = (v: unknown) => typeof v === 'string' && v.trim().length > 0;
const timestamp = (v: unknown) => typeof v === 'string' && /(?:Z|[+-]\d{2}:\d{2})$/.test(v) && Number.isFinite(Date.parse(v));

/** Checks provenance and consistency; it does not replace external task review. */
export function evaluationErrors(v: any, providers: Provider[], root = ROOT): string[] {
  const errors: string[] = [];
  if (v?.schema_version !== 1) errors.push('schema_version must be 1');
  if (!/^[a-zA-Z0-9._-]+$/.test(v?.run_id ?? '')) errors.push('invalid run_id');
  const provider = providers.find(p => p.id === v?.service_id);
  if (!provider?.catalog?.routes.some(r => r.id === v?.route_id)) errors.push('unknown service/route identity');
  if (!/^https:\/\/\S+$/.test(v?.entry_url ?? '')) errors.push('entry_url must be HTTPS');
  for (const field of ['id', 'file', 'description', 'inputs', 'expected_output', 'success', 'failure']) {
    if (!text(v?.task?.[field])) errors.push(`task.${field} is required`);
  }
  if (!hash(v?.task?.sha256) || !hash(v?.prompt_sha256)) errors.push('task and prompt SHA256 are required');
  for (const field of ['name', 'version', 'mode']) if (!text(v?.harness?.[field])) errors.push(`harness.${field} is required`);
  if (!text(v?.model) || !text(v?.reasoning_effort)) errors.push('model and reasoning_effort are required');
  if (!timestamp(v?.started_at) || !timestamp(v?.ended_at) || Date.parse(v.ended_at) < Date.parse(v.started_at)) errors.push('valid ordered timestamps with timezone are required');
  if (!nonnegative(v?.elapsed_seconds) || !nonnegative(v?.budget_seconds) || v.budget_seconds === 0) errors.push('invalid elapsed time or budget');
  if (!['completed', 'not_completed', 'invalid_run'].includes(v?.status) || !text(v?.reason)) errors.push('status and reason are required');
  for (const key of ['service_cost_usd', 'human_interventions']) {
    if (v?.[key] !== null && !nonnegative(v?.[key])) errors.push(`${key}: use a nonnegative measurement or null, not an inferred zero`);
  }
  if (v?.human_interventions !== null && !Number.isInteger(v?.human_interventions)) errors.push('human_interventions must be integer or null');
  if (v?.usage !== null) {
    for (const key of ['input_tokens', 'cached_input_tokens', 'output_tokens']) {
      if (!Number.isInteger(v?.usage?.[key]) || v.usage[key] < 0) errors.push(`invalid usage.${key}`);
    }
    if (v?.usage?.cached_input_tokens > v?.usage?.input_tokens) errors.push('cached input is a subset of input tokens');
  }
  if (v.request_usage) {
    const detail = v.request_usage;
    if (!['complete', 'incomplete'].includes(detail.status) || !text(detail.method) || !text(detail.reason)
        || !Array.isArray(detail.requests) || (detail.source_sha256 !== null && !hash(detail.source_sha256))) errors.push('invalid request_usage');
    if (detail.status === 'complete') {
      if (!hash(detail.source_sha256) || !detail.requests?.length || !v.usage) errors.push('complete request_usage needs source hash, requests and final totals');
      for (const key of ['input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'output_tokens', 'reasoning_output_tokens']) {
        if (!Array.isArray(detail.requests) || detail.requests.some((r: any) => !Number.isInteger(r[key] ?? 0) || (r[key] ?? 0) < 0)
            || detail.requests.reduce((sum: number, r: any) => sum + (r[key] ?? 0), 0) !== (v.usage?.[key] ?? 0)) errors.push(`request_usage mismatch: ${key}`);
      }
    }
  }
  if (v.service_cost) {
    const fee = v.service_cost;
    if (!['reported', 'estimated', 'confirmed_free', 'unknown'].includes(fee.kind)
        || !text(fee.note) || !Array.isArray(fee.sources) || fee.sources.some((x: unknown) => !text(x))
        || (fee.kind !== 'unknown' && (!fee.sources.length || !nonnegative(fee.amount_usd))) || fee.amount_usd !== v.service_cost_usd
        || (fee.kind === 'unknown' && fee.amount_usd !== null)
        || (fee.kind === 'confirmed_free' && fee.amount_usd !== 0)) errors.push('invalid service_cost basis');
    if (fee.kind === 'estimated') {
      if (!Array.isArray(fee.items) || !fee.items.length || fee.items.some((x: any) =>
        !nonnegative(x.quantity) || !nonnegative(x.usd_per_unit) || !text(x.unit))
        || Math.abs(fee.items.reduce((sum: number, x: any) => sum + x.quantity * x.usd_per_unit, 0) - fee.amount_usd) > 1e-9)
        errors.push('service_cost estimate does not match usage × price');
    }
  }
  const checks = v?.review?.checks;
  if (v?.review?.method !== 'external_agent' || !text(v?.review?.reviewer) || !timestamp(v?.review?.reviewed_at)
      || !Array.isArray(checks) || checks.some((c: any) => !text(c?.criterion) || typeof c?.passed !== 'boolean' || !text(c?.evidence))) {
    errors.push('an external review with evidence-backed checks is required');
  }
  if (v?.status === 'completed' && (!Array.isArray(checks) || !checks.length || checks.some((c: any) => c.passed !== true) || !hash(v?.provenance?.answer_sha256))) errors.push('completed requires passing checks and final-answer provenance');
  for (const key of ['run_sha256', 'review_sha256']) if (!hash(v?.provenance?.[key])) errors.push(`provenance.${key} is required`);
  const evidence = v?.evidence;
  if (!Array.isArray(evidence) || !evidence.length) errors.push('selected evidence is required');
  for (const item of Array.isArray(evidence) ? evidence : []) {
    const expected = `data/experiments/evidence/${v.run_id}/`;
    const file = typeof item?.path === 'string' ? path.resolve(root, item.path) : '';
    if (typeof item?.path !== 'string' || !item.path.startsWith(expected) || !file.startsWith(path.resolve(root, expected) + path.sep)
        || !fs.existsSync(file) || !fs.statSync(file).isFile()
        || !fs.realpathSync(file).startsWith(fs.realpathSync(root) + path.sep)) {
      errors.push('evidence must be an existing file inside this run’s evidence directory');
    } else if (createHash('sha256').update(fs.readFileSync(file)).digest('hex') !== item.sha256) errors.push(`evidence hash mismatch: ${item.path}`);
  }
  return errors;
}

const cell = (v: unknown) => String(v ?? 'unknown').replaceAll('|', '\\|').replaceAll('\n', ' ');
export function generateEvaluations(records: Evaluation[], outputRoot: string) {
  const dir = path.join(outputRoot, 'generated');
  fs.mkdirSync(dir, { recursive: true });
  const sorted = [...records].sort((a, b) => b.started_at.localeCompare(a.started_at) || a.run_id.localeCompare(b.run_id));
  const boards = buildBoards(records);
  const summaryRow = (row: typeof boards[number]['rows'][number]) => ({ service_id: row.service_id,
    route_id: row.route_id, metrics: row.metrics, run_ids: row.runs.map(r => r.run_id) });
  const serviceSummaries = [...new Set(records.map(r => r.task.file))].flatMap(file =>
    selectServiceBoards(boards.filter(b => b.task_file === file)).flatMap(b => b.rows.map(row => ({
      task_file: file, ...summaryRow(row), comparison_id: b.id,
      selection: row.metrics.trials ? 'most_recent_valid_route_protocol' : 'no_valid_trials',
    }))));
  fs.writeFileSync(path.join(dir, 'evaluations.json'), JSON.stringify({ schema_version: 1,
    evaluations: sorted, service_summaries: serviceSummaries,
    comparisons: boards.map(b => ({ ...b, rows: b.rows.map(summaryRow) })),
  }, null, 2) + '\n');
  const row = (r: Evaluation) => {
    const link = `../data/experiments/evaluations/${r.run_id}.json`;
    return `| ${cell(r.service_id)} / ${cell(r.route_id)} | ${cell(r.task.id)} (${cell(r.task.version ?? r.task.sha256.slice(0, 8))}) | ${cell(r.environment.service_credentials)} | ${cell(r.environment.prompt_style ?? 'legacy')} | [${r.status}](${link}) | ${cell(r.started_at)} | ${cell(r.harness.version)} / ${cell(r.model)} / ${cell(r.reasoning_effort)} | ${r.usage ? `${r.usage.input_tokens} / ${r.usage.cached_input_tokens} / ${r.usage.output_tokens}` : 'unknown'} | ${r.elapsed_seconds}s | ${cell(r.service_cost_usd)} | ${cell(r.human_interventions)} |`;
  };
  // Classify the task, not the provider: one provider may serve several domains.
  // This is a current display label, not a rewrite of frozen historical evidence.
  const groups = new Map<string, Map<string, Evaluation[]>>();
  for (const r of sorted) {
    const file = path.resolve(ROOT, r.task.file);
    const taskText = file.startsWith(ROOT + path.sep) && fs.existsSync(file)
      ? fs.readFileSync(file, 'utf8') : '';
    const classification = taskText.match(/^分类：(.+)$/m)?.[1].trim() ?? '未标明分类';
    if (!groups.has(classification)) groups.set(classification, new Map());
    const tasks = groups.get(classification)!;
    const key = `${r.task.file}:${r.task.id}:${r.task.version ?? r.task.sha256}:${r.task.sha256}`;
    if (!tasks.has(key)) tasks.set(key, []);
    tasks.get(key)!.push(r);
  }
  const header = `| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |`;
  const sections = [...groups].map(([classification, tasks]) => `${classification.match(/（([a-z0-9/-]+)）/) ? `<a id="${classification.match(/（([a-z0-9/-]+)）/)![1].replaceAll('/', '-')}"></a>\n\n` : ''}## ${cell(classification)}\n\n` +
    [...tasks.values()].map(runs => {
      const task = runs[0].task;
      return `### ${cell(task.id)} / ${cell(task.version ?? task.sha256.slice(0, 8))}\n\n${cell(task.description)}\n\n${header}\n${runs.map(row).join('\n')}`;
    }).join('\n\n')).join('\n\n');
  fs.writeFileSync(path.join(dir, 'evaluations.md'), `<!-- GENERATED — npm run generate; source: data/experiments/evaluations/ -->
# 任务实测结果

每行只说明该服务入口在该任务和运行配置下的观察。Token用量为输入总数（含缓存）加输出，缓存不重复相加。模型费用根据保存的LiteLLM价格表自动估算，估价日期不冒充运行日期；服务费用单独记录，unknown不等于0。点击结果可查看冻结的任务、独立复核与选取的证据；原始日志仍在本地。免费账号的注册准备若发生在计时前，说明保存在 environment.preparation_note；表中 token 与耗时不包含这部分准备。历史记录保留，不把不同任务、配置或日期直接平均成服务排名。

按任务所属大类 / 子类分组，再展示同一任务版本和冻结内容的运行。分类标题来自当前任务表，仅用于导航；历史任务、结果和用量不改写。同组仍需核对接入前提与模型等配置，不能仅按耗时排序判断优劣。

输入方式 legacy 是带明确测试要求的初期试跑，Agent 的开销包含证据保存与整理；natural 只提供用户任务、资料及运行环境，使用自动会话日志与外部远端复核。不同方式分别记录；单次测量都不代表典型开销，跨版本差异也可能来自业务要求、执行路径和缓存变化。

${sections}

## 汇总条件与费用依据

${buildBoards(records).map(board => `<a id="${board.id}"></a>\n\n### ${board.tasks.map(t => `${cell(t.id)} ${cell(t.version)}`).join(', ')}\n\n` + board.rows.map(row => {
  const first = row.runs[0];
  return `**${cell(row.service_id)} / ${cell(row.route_id)}** — ${row.metrics.passed} 完成 / ${row.metrics.failed} 未完成 / ${row.metrics.invalid} 环境无效。\n\n${cell(first.harness.version)} / ${cell(first.model)} / ${cell(first.reasoning_effort)} · ${first.budget_seconds}s · ${cell(first.environment.prompt_style ?? 'legacy')} · ${cell(first.environment.service_credentials)}\n\n准备：${cell(first.environment.preparation_note)}\n\n` + row.runs.map(r => {
    const price = r.model_cost;
    return `- [${r.run_id}](../data/experiments/evaluations/${r.run_id}.json)：模型费用 ${moneyLabel(price?.amount_usd ?? null)}；${cell(price?.reason)}${price?.pricing ? ` [LiteLLM价格快照](${price.pricing.source})（${price.pricing.fetched_at}，${price.pricing.tier}）` : ''}。服务费用 ${moneyLabel(r.service_cost_usd)}；${cell(r.service_cost ? `${r.service_cost.kind}: ${r.service_cost.note}; ${r.service_cost.sources.join('; ')}` : '旧记录新增实付金额；沿用原复核，不补造回执或估算依据。')}`;
  }).join('\n');
}).join('\n\n')).join('\n\n')}
`);
}
