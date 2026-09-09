import type { Provider } from './lib.ts';
import type { Evaluation } from './evaluations.ts';
import { type Board, summarize, tokenLabel, moneyLabel, interfaceLabel } from './leaderboard.ts';
import { taskDisplay } from './task-display.ts';

const cell = (v: unknown) => String(v ?? '—').replaceAll('|', '\\|').replaceAll('\n', ' ');
const table = (headers: string[], rows: string[][]) => `| ${headers.join(' | ')} |\n| ${headers.map(() => '---').join(' | ')} |\n${rows.map(row => `| ${row.join(' | ')} |`).join('\n')}`;
const recordLink = (r: Evaluation) => `../data/experiments/evaluations/${r.run_id}.json`;
const routeName = (p: Provider, id: string) => {
  const route = p.catalog?.routes.find(r => r.id === id);
  const type = interfaceLabel(route?.interface);
  return type === '—' || p.catalog!.routes.filter(r => r.interface === route!.interface).length > 1
    ? `${type} (${cell(id)})` : type;
};

/** Supplied credentials are evidence of the starting state, not an autonomous signup score.
 * Historical runs have no separately metered setup; never repurpose execution measurements. */
export function renderSetup(p: Provider, records: Evaluation[]) {
  const latest = [...records].sort((a, b) => b.started_at.localeCompare(a.started_at));
  const rows = (p.catalog?.routes ?? []).map(route => {
    const r = latest.find(r => r.route_id === route.id);
    const supplied = r && String(r.environment.service_credentials ?? 'none').startsWith('provided:');
    const state = !r ? '—' : supplied ? 'Credentials supplied before trial' : 'No account or key supplied';
    return [routeName(p, route.id), r ? `[${state}](${recordLink(r)})` : state, '—', '—', '—'];
  });
  return table(['Route', 'Starting resources', 'Setup tokens', 'Setup time', 'Human involvement'], rows);
}

/** Compare routes within each task. Each row retains its frozen task and protocol;
 * different versions/configurations are labelled, never averaged together. */
export function renderServiceResults(p: Provider, boards: Board[], records: Evaluation[]) {
  const entries = boards.flatMap(board => board.rows.filter(row => row.service_id === p.id).map(row => ({ board, row })));
  if (!entries.length) return '—';
  const tasks = new Map<string, Evaluation['task']>();
  for (const { board } of entries) for (const t of board.tasks) tasks.set(`${t.file}:${t.id}:${t.version}`, t);
  const sections = [...tasks].map(([key, task]) => {
    const display = taskDisplay(task, false);
    const matching = entries.flatMap(({ board, row }) => {
      const runs = row.runs.filter(r => `${r.task.file}:${r.task.id}:${r.task.version}` === key);
      return runs.length ? [{ board, row, runs }] : [];
    });
    const conditions = [...new Set(matching.map(e => e.board.id))];
    const label = (id: string) => String.fromCharCode(65 + conditions.indexOf(id));
    const rows = matching.map(({ board, row, runs }) => {
      const m = summarize(runs);
      const rate = m.resolution_rate === null ? '—' : `${Number((100 * m.resolution_rate).toFixed(1))}%`;
      const evidence = `./evaluations.md#${board.id}`;
      const estimate = runs.some(r => r.status !== 'invalid_run' && r.service_cost?.kind === 'estimated');
      return [routeName(p, row.route_id), `[${m.trials}](${evidence})`, rate === '—' ? rate : `[${rate}](${evidence})`,
        tokenLabel(m.tokens), moneyLabel(m.model_cost_usd), `${m.service_cost_usd !== null && estimate ? '~' : ''}${moneyLabel(m.service_cost_usd)}`,
        ...(conditions.length > 1 ? [label(board.id)] : [])];
    });
    for (const route of p.catalog?.routes ?? []) if (!matching.some(e => e.row.route_id === route.id)) {
      rows.push([routeName(p, route.id), '—', '—', '—', '—', '—', ...(conditions.length > 1 ? ['—'] : [])]);
    }
    const config = (r: Evaluation) => `${cell(r.harness.version)} · ${cell(r.model)} / ${cell(r.reasoning_effort)} · ${r.budget_seconds}s`;
    const commonConfigs = [...new Set(matching.map(e => config(e.runs[0])))];
    const dates = [...new Set(matching.flatMap(e => e.runs).map(r => r.started_at.slice(0, 10)))].sort().join(', ');
    const shared = `${commonConfigs.length === 1 ? commonConfigs[0] + ' · ' : ''}${dates} (UTC)`;
    const taskVariants = [...new Set(matching.map(e => e.runs[0].task.sha256))];
    const configs = conditions.map(id => {
      const entry = matching.find(e => e.board.id === id)!;
      const r = entry.runs[0];
      const credentials = String(r.environment.service_credentials ?? 'none').startsWith('provided:') ? 'Credentials supplied' : 'No account or key supplied';
      return `${conditions.length > 1 ? `**${label(id)}:** ${routeName(p, r.route_id)} · ` : ''}${commonConfigs.length > 1 ? config(r) + ' · ' : ''}${credentials}${taskVariants.length > 1 ? ` · Task variant ${taskVariants.indexOf(r.task.sha256) + 1}` : ''} · [Full configuration and evidence](./evaluations.md#${id})`;
    });
    const invalid = matching.flatMap(e => e.runs).filter(r => r.status === 'invalid_run');
    const failures = matching.flatMap(e => e.runs).filter(r => r.status !== 'completed');
    const reasons = failures.map(r => `- ${routeName(p, r.route_id)}: [${r.status === 'invalid_run' ? 'Invalid run' : 'Not completed'}](${recordLink(r)}) — ${cell(r.reason)}`);
    return `#### ${cell(display.description)}\n\n${table(['Route', 'Trials', 'Resolution rate', 'Tokens', 'Model cost', 'Service cost', ...(conditions.length > 1 ? ['Conditions'] : [])], rows)}\n\n`
      + `<details>\n<summary>Task, conditions and evidence</summary>\n\n${cell(display.inputs)}\n\n**Completion:** ${cell(display.success)}\n\n${shared}\n\n${configs.join('\n\n')}\n\n[Task definition](./tasks.en.md#${task.id}-${task.version})${invalid.length ? `\n\nInvalid runs: ${invalid.length}` : ''}${reasons.length ? `\n\n${reasons.join('\n')}` : ''}\n\n</details>`;
  });
  const history = [...records].sort((a, b) => b.started_at.localeCompare(a.started_at)).map(r =>
    [cell(r.task.id) + ` ${cell(r.task.version)}`, routeName(p, r.route_id), `[${r.status}](${recordLink(r)})`, r.started_at.slice(0, 10)]);
  return sections.join('\n\n') + `\n\n<details>\n<summary>Run history (${records.length})</summary>\n\n${table(['Task', 'Route', 'Result', 'Date (UTC)'], history)}\n\n</details>`;
}
