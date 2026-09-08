import { createHash } from 'node:crypto';
import type { Evaluation } from './evaluations.ts';

const stable = (value: unknown): string => {
  if (Array.isArray(value)) return JSON.stringify(value.map(v => JSON.parse(stable(v))));
  if (value && typeof value === 'object') return JSON.stringify(Object.fromEntries(
    Object.entries(value).sort(([a], [b]) => a.localeCompare(b)).map(([k, v]) => [k, JSON.parse(stable(v))])));
  return JSON.stringify(value ?? null);
};
const configKey = (r: Evaluation) => stable({ model: r.model, effort: r.reasoning_effort,
  harness: r.harness, budget: r.budget_seconds, host: r.environment.host,
  isolation: r.environment.isolation, prompt_style: r.environment.prompt_style ?? 'legacy',
  input_delivery: r.environment.input_delivery ?? 'inline',
  credentials: String(r.environment.service_credentials ?? 'none').startsWith('provided:') ? 'provided' : 'none',
  web_search: r.environment.web_search });
const mean = (values: (number | null)[]) => values.length && values.every(v => v !== null && Number.isFinite(v))
  ? values.reduce<number>((sum, v) => sum + v!, 0) / values.length : null;
export function summarize(runs: Evaluation[]) {
  const valid = runs.filter(r => r.status !== 'invalid_run');
  return {
    passed: valid.filter(r => r.status === 'completed').length,
    failed: valid.filter(r => r.status === 'not_completed').length,
    invalid: runs.length - valid.length,
    trials: valid.length,
    resolution_rate: valid.length ? valid.filter(r => r.status === 'completed').length / valid.length : null,
    tokens: mean(valid.map(r => r.usage ? r.usage.input_tokens + r.usage.output_tokens : null)),
    model_cost_usd: mean(valid.map(r => r.model_cost?.amount_usd ?? null)),
    service_cost_usd: mean(valid.map(r => r.service_cost_usd)),
  };
}
export interface BoardRow { service_id: string; route_id: string; runs: Evaluation[]; metrics: ReturnType<typeof summarize> }
export interface Board { id: string; task_file: string; tasks: Evaluation['task'][]; rows: BoardRow[]; latest: string }

/** Latest recorded protocol per service/route; compare only identical frozen task sets and settings. */
export function buildBoards(records: Evaluation[]): Board[] {
  const byRoute = new Map<string, Evaluation[]>();
  for (const run of records) {
    const key = `${run.task.file}:${run.service_id}:${run.route_id}`;
    byRoute.set(key, [...(byRoute.get(key) ?? []), run]);
  }
  const boards = new Map<string, Board>();
  for (const runs of byRoute.values()) {
    runs.sort((a, b) => b.started_at.localeCompare(a.started_at) || b.run_id.localeCompare(a.run_id));
    const reference = runs.find(r => r.status !== 'invalid_run') ?? runs[0];
    const config = configKey(reference);
    const matching = runs.filter(r => configKey(r) === config);
    const latestTask = new Map<string, string>();
    for (const run of matching) if (!latestTask.has(run.task.id)) latestTask.set(run.task.id, run.task.sha256);
    const selected = matching.filter(r => r.task.sha256 === latestTask.get(r.task.id));
    const tasks = [...new Map(selected.map(r => [r.task.id, r.task])).values()].sort((a, b) => a.id.localeCompare(b.id));
    // Equal task weighting: compare the same task set and repeat count; never silently pool easier subsets.
    const manifest = tasks.map(t => [t.id, t.sha256, selected.filter(r => r.task.id === t.id && r.status !== 'invalid_run').length]);
    const key = stable([reference.task.file, config, manifest]);
    if (!boards.has(key)) boards.set(key, { id: `comparison-${createHash('sha256').update(key).digest('hex').slice(0, 12)}`,
      task_file: reference.task.file, tasks, rows: [], latest: reference.started_at });
    const board = boards.get(key)!;
    board.rows.push({ service_id: reference.service_id, route_id: reference.route_id, runs: selected, metrics: summarize(selected) });
    if (reference.started_at > board.latest) board.latest = reference.started_at;
  }
  return [...boards.values()].sort((a, b) => b.latest.localeCompare(a.latest) || a.id.localeCompare(b.id)).map(board => ({ ...board,
    rows: board.rows.sort((a, b) => (b.metrics.resolution_rate ?? -1) - (a.metrics.resolution_rate ?? -1) || a.service_id.localeCompare(b.service_id)) }));
}
const cell = (value: unknown) => String(value ?? 'unknown').replaceAll('|', '\\|').replaceAll('\n', ' ');
export const tokenLabel = (n: number | null) => n === null ? '—' : n >= 1e6 ? `${(n / 1e6).toFixed(2)}M` : n >= 1000 ? `${(n / 1000).toFixed(1)}k` : String(Math.round(n));
export const moneyLabel = (n: number | null) => n === null ? '—' : n === 0 ? '$0' : n < .01 ? `$${n.toFixed(4)}` : `$${n.toFixed(2)}`;
export const boardHeader = (zh: boolean) => zh
  ? '| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |\n| --- | ---: | ---: | ---: | ---: |'
  : '| Service | Resolution rate | Tokens | Model cost | Service cost |\n| --- | ---: | ---: | ---: | ---: |';
/** Display rows together without pooling measurements from different comparison groups. */
export function renderBoardRows(boards: Board[], names: Map<string, string>, prefix = './') {
  const entries = boards.flatMap(board => board.rows.map(row => ({ board, row })));
  return entries.sort((a, b) => (names.get(a.row.service_id) ?? a.row.service_id).localeCompare(names.get(b.row.service_id) ?? b.row.service_id)
    || a.row.route_id.localeCompare(b.row.route_id) || a.board.id.localeCompare(b.board.id)).map(({ board, row }) => {
    const m = row.metrics;
    const repeated = entries.filter(e => e.row.service_id === row.service_id).length > 1;
    const name = cell(names.get(row.service_id) ?? row.service_id) + (repeated ? ` / ${cell(row.route_id)}` : '');
    return `| [${name}](${prefix}generated/evaluations.md#${board.id}) | ${m.resolution_rate === null ? '—' : `${Number((100 * m.resolution_rate).toFixed(1))}%`} | ${tokenLabel(m.tokens)} | ${moneyLabel(m.model_cost_usd)} | ${m.service_cost_usd !== null && row.runs.some(r => r.status !== 'invalid_run' && r.service_cost?.kind === 'estimated') ? '~' : ''}${moneyLabel(m.service_cost_usd)} |`;
  }).join('\n');
}

export function renderBoardDetails(boards: Board[], names: Map<string, string>, zh: boolean, prefix = './') {
  return boards.map(board => {
    const first = board.rows[0].runs[0];
    const title = board.tasks.map(t => `${t.id} ${t.version ?? t.sha256.slice(0, 8)}`).join(', ');
    const details = board.rows.map(row => {
      const m = row.metrics;
      return `- ${cell(names.get(row.service_id) ?? row.service_id)} / ${cell(row.route_id)}: ${zh ? '完成 / 失败 / 环境无效' : 'passed / failed / invalid'} = ${m.passed} / ${m.failed} / ${m.invalid}; ` +
        row.runs.map(r => `[${r.started_at.slice(0, 10)}](${prefix}data/experiments/evaluations/${r.run_id}.json)`).join(', ');
    }).join('\n');
    return `**[${cell(title)}](${prefix}generated/evaluations.md#${board.id})**\n\n${cell(first.model)} / ${cell(first.reasoning_effort)} · ${cell(first.harness.version)} · ${first.budget_seconds}s · ${cell(first.environment.prompt_style ?? 'legacy')} · ${String(first.environment.service_credentials ?? 'none').startsWith('provided:') ? (zh ? '预供凭据' : 'credentials provided') : (zh ? '未供凭据' : 'no credentials')}\n\n${board.tasks.map(t => `- ${cell(t.description)}`).join('\n')}\n\n${details}`;
  }).join('\n\n');
}
