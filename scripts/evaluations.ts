import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { ROOT, type Provider } from './lib.ts';

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
  fs.writeFileSync(path.join(dir, 'evaluations.json'), JSON.stringify({ schema_version: 1, evaluations: sorted }, null, 2) + '\n');
  const rows = sorted.map(r => {
    const link = `../data/experiments/evaluations/${r.run_id}.json`;
    return `| ${cell(r.service_id)} / ${cell(r.route_id)} | ${cell(r.task.id)} (${cell(r.task.version ?? r.task.sha256.slice(0, 8))}) | [${r.status}](${link}) | ${cell(r.started_at)} | ${cell(r.harness.version)} / ${cell(r.model)} / ${cell(r.reasoning_effort)} | ${r.usage ? `${r.usage.input_tokens} / ${r.usage.cached_input_tokens} / ${r.usage.output_tokens}` : 'unknown'} | ${r.elapsed_seconds}s | ${cell(r.service_cost_usd)} | ${cell(r.human_interventions)} |`;
  });
  fs.writeFileSync(path.join(dir, 'evaluations.md'), `<!-- GENERATED — npm run generate; source: data/experiments/evaluations/ -->
# 任务实测结果

每行只说明该服务入口在该任务和运行配置下的观察。Agent消耗只记录token，不换算货币；缓存输入已含在输入总数中。服务调用费用单独记录，unknown不等于0。点击结果可查看冻结的任务、独立复核与选取的证据；原始日志仍在本地。历史记录保留，不把不同任务、配置或日期直接平均成服务排名。

| 服务 / 入口 | 任务 / 版本 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
${rows.join('\n')}
`);
}
