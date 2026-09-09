import { taskDisplay } from './task-display.ts';
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

/** Homepage selection is chronological, never a claim of the cheapest or best route.
 * Keep a whole recorded protocol; do not select a different route for each task. */
export function selectServiceBoards(boards: Board[]): Board[] {
  const entries = boards.flatMap(board => board.rows.map(row => ({ board, row })));
  const chosen = new Map<string, typeof entries[number]>();
  const latest = (row: BoardRow) => row.runs.filter(r => r.status !== 'invalid_run')
    .map(r => r.started_at).sort().at(-1) ?? '';
  entries.sort((a, b) => latest(b.row).localeCompare(latest(a.row))
    || b.board.latest.localeCompare(a.board.latest) || a.row.route_id.localeCompare(b.row.route_id));
  for (const entry of entries) if (!chosen.has(entry.row.service_id)) chosen.set(entry.row.service_id, entry);
  return boards.map(board => ({ ...board, rows: board.rows.filter(row => chosen.get(row.service_id)?.row === row) }))
    .filter(board => board.rows.length);
}

export const interfaceLabel = (type: string | undefined, zh = false) => type === 'web' ? (zh ? '网页' : 'Web')
  : type === 'mobile' ? (zh ? '移动应用' : 'Mobile') : type?.toUpperCase() ?? '—';

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
export const boardHeader = (zh: boolean, withAccess = false) => {
  const headings = zh ? ['服务', '完成率', 'Token', '模型费用', '服务费用'] : ['Service', 'Resolution rate', 'Tokens', 'Model cost', 'Service cost'];
  if (withAccess) headings.push(...(zh ? ['测试方式', '接入资料'] : ['Tested via', 'Access links']));
  return `| ${headings.join(' | ')} |\n| --- | ---: | ---: | ---: | ---: |${withAccess ? ' --- | --- |' : ''}`;
};
/** Display rows together without pooling measurements from different comparison groups. */
export function renderBoardRows(boards: Board[], names: Map<string, string>, prefix = './', serviceLinks?: Map<string, { profile: string; access: string }>, interfaces = new Map<string, string>(), zh = false) {
  const entries = boards.flatMap(board => board.rows.map(row => ({ board, row })));
  return entries.sort((a, b) => (names.get(a.row.service_id) ?? a.row.service_id).localeCompare(names.get(b.row.service_id) ?? b.row.service_id)
    || a.row.route_id.localeCompare(b.row.route_id) || a.board.id.localeCompare(b.board.id)).map(({ board, row }) => {
    const m = row.metrics;
    const repeated = entries.filter(e => e.row.service_id === row.service_id).length > 1;
    const name = cell(names.get(row.service_id) ?? row.service_id) + (repeated ? ` / ${cell(row.route_id)}` : '');
    const evidence = `${prefix}generated/evaluations.md#${board.id}`;
    const links = serviceLinks?.get(row.service_id);
    const rate = m.resolution_rate === null ? '—' : `${Number((100 * m.resolution_rate).toFixed(1))}%`;
    return `| [${name}](${links?.profile ?? evidence}) | ${links && rate !== '—' ? `[${rate}](${evidence})` : rate} | ${tokenLabel(m.tokens)} | ${moneyLabel(m.model_cost_usd)} | ${m.service_cost_usd !== null && row.runs.some(r => r.status !== 'invalid_run' && r.service_cost?.kind === 'estimated') ? '~' : ''}${moneyLabel(m.service_cost_usd)} |${serviceLinks ? ` [${interfaceLabel(interfaces.get(`${row.service_id}/${row.route_id}`), zh)}](${row.runs[0].entry_url}) | ${links?.access ?? '—'} |` : ''}`;
  }).join('\n');
}

export function renderBoardDetails(boards: Board[], names: Map<string, string>, zh: boolean, prefix = './', interfaces = new Map<string, string>()) {
  if (!boards.length) return '';
  const entries = boards.flatMap(board => board.rows.map(row => ({ board, row })));
  const runs = entries.flatMap(e => e.row.runs);
  // Deduplicate readable task content, not historical hashes or display titles alone.
  // This changes prose only; the comparison groups and their measurements stay frozen.
  const taskKey = (t: Evaluation['task']) => stable([t.description, t.inputs, t.expected_output, t.success, t.failure]);
  const tasks = [...new Map(boards.flatMap(b => b.tasks).map(t => [taskKey(t), t])).values()];
  const label = (cn: string, en: string) => zh ? cn : en;
  const displayTasks = tasks.map(t => taskDisplay(t, zh));
  const completion = (t: Evaluation['task']) => t.success || t.expected_output || '—';
  const taskText = tasks.length === 1
    ? `**${label('任务：', 'Task: ')}${cell(displayTasks[0].description)}**\n\n${cell(displayTasks[0].inputs)}\n\n${label('完成标准：', 'Completion criteria: ')}${cell(completion(displayTasks[0]))}`
    : `| ${label('任务及条件', 'Task and conditions')} | ${label('完成标准', 'Completion criteria')} |\n| --- | --- |\n` + displayTasks.map(t => `| ${cell(t.description)}<br>${cell(t.inputs)} | ${cell(completion(t))} |`).join('\n');
  const config = (r: Evaluation) => `${r.harness.version} · ${r.model} / ${r.reasoning_effort} · ${r.budget_seconds % 60 === 0 ? `${r.budget_seconds / 60} ${label('分钟', 'min')}` : `${r.budget_seconds}s`}`;
  const configs = [...new Set(runs.map(config))];
  const dates = [...new Set(runs.map(r => new Date(r.started_at).toISOString().slice(0, 10)))].sort();
  const date = dates.length === 1 ? dates[0] : `${dates[0]} – ${dates.at(-1)}`;
  const varyingTasks = new Set(entries.map(({ board }) => stable(board.tasks.map(taskKey).sort()))).size > 1;
  const preparation = (r: Evaluation) => String(r.environment.service_credentials ?? 'none').startsWith('provided:')
    ? label('已预供服务凭据', 'Service credentials supplied') : label('未预供账号或密钥', 'No account or key supplied');
  const preparations = [...new Set(runs.map(preparation))];
  const varying = varyingTasks || configs.length > 1 || preparations.length > 1;
  const headers = [label('服务', 'Service'),
    ...(varyingTasks ? [label('本次任务', 'Tasks covered')] : []),
    ...(configs.length > 1 ? [label('测试配置', 'Configuration')] : []),
    ...(preparations.length > 1 ? [label('起点', 'Starting resources')] : [])];
  const rows = entries.map(({ board, row }) => {
    const repeated = entries.filter(e => e.row.service_id === row.service_id).length > 1;
    const values = [`[${cell(names.get(row.service_id) ?? row.service_id)}${repeated ? ` / ${interfaceLabel(interfaces.get(`${row.service_id}/${row.route_id}`), zh)}` : ''}](${prefix}generated/evaluations.md#${board.id})`,
      ...(varyingTasks ? [board.tasks.map(t => cell(taskDisplay(t, zh).description)).join('<br>')] : []),
      ...(configs.length > 1 ? [cell(config(row.runs[0]))] : []),
      ...(preparations.length > 1 ? [preparation(row.runs[0])] : [])];
    return `| ${values.join(' | ')} |`;
  });
  const table = varying ? `| ${headers.join(' | ')} |\n| ${headers.map(() => '---').join(' | ')} |\n${rows.join('\n')}` : '';
  const setup = `**${label('测试配置：', 'Test configuration:')}** ${configs.length === 1 ? `${cell(configs[0])} · ` : ''}${date}${label('（UTC）', ' (UTC)')}${preparations.length === 1 ? ` · ${preparations[0]}` : ''}`;
  const notes: string[] = [];
  if (runs.some(r => !r.environment.host || !r.harness.launcher_sha256)) notes.push(label(
    '部分早期记录缺少环境信息，尚待统一复跑。', 'Some early records lack environment details and await a controlled rerun.'));
  const files = [...new Set(tasks.map(t => t.file))];
  const links = files.map((file, i) => `[${label('任务定义', 'Task definitions')}${files.length > 1 ? ` ${i + 1}` : ''}](${prefix}${zh ? file : 'generated/tasks.en.md#' + boards.find(b => b.task_file === file)!.tasks[0].id + '-' + boards.find(b => b.task_file === file)!.tasks[0].version})`).join(' · ')
    + ` · [${label('完整运行记录与证据', 'Full runs and evidence')}](${prefix}generated/evaluations.md)`;
  return [taskText, table, setup, notes.join(' '), links].filter(Boolean).join('\n\n');
}
