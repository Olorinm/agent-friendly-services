import test from 'node:test';
import fs from 'node:fs';
import { ROOT } from '../scripts/lib.ts';
import assert from 'node:assert/strict';
import { estimateModelCost, type PriceSnapshot } from '../scripts/model-costs.ts';
import { buildBoards, summarize, renderBoardRows, renderBoardDetails } from '../scripts/leaderboard.ts';
import type { Evaluation } from '../scripts/evaluations.ts';

const prices = (extra = {}): PriceSnapshot => ({ source: 'https://example.com/prices', revision: 'test', fetched_at: '2026-09-08', sha256: 'test',
  models: { example: { input_cost_per_token: .000002, output_cost_per_token: .00001,
    cache_read_input_token_cost: .0000002, cache_creation_input_token_cost: .0000025, ...extra } } });
const run = (overrides: Partial<Evaluation> = {}): Evaluation => ({
  run_id: 'one', service_id: 'a', route_id: 'api', model: 'example', reasoning_effort: 'high',
  started_at: '2026-09-08T00:00:00Z', harness: { name: 'test', version: '1', mode: 'exec', launcher_sha256: 'x' },
  task: { id: 'one', version: 'v1', sha256: 'one', file: 'tasks.md' },
  environment: { service_credentials: 'none', prompt_style: 'natural' }, budget_seconds: 600,
  status: 'completed', usage: { input_tokens: 1000, cached_input_tokens: 600, output_tokens: 100 },
  model_cost: { amount_usd: .2, kind: 'estimated', reason: 'fixture', pricing: null }, service_cost_usd: 0,
  ...overrides,
} as Evaluation);

test('LiteLLM rates bill cache reads, writes and output separately; reasoning is not counted twice', () => {
  const result = estimateModelCost(run({ usage: { input_tokens: 1000, cached_input_tokens: 600,
    cache_write_input_tokens: 100, output_tokens: 100, reasoning_output_tokens: 70 } }), prices());
  assert.equal(result.amount_usd, .00197); // 300 input + 600 reads + 100 writes + 100 output
  assert.equal(result.kind, 'estimated');
  assert.equal(estimateModelCost(run({ usage: null }), prices()).amount_usd, null);
  assert.equal(estimateModelCost(run({ model: 'missing' }), prices()).amount_usd, null);
  assert.equal(estimateModelCost(run(), null).amount_usd, null);
});

test('context price tiers are never selected using cumulative session input as a request length', () => {
  const table = prices({ input_cost_per_token_above_272k_tokens: .000004 });
  assert.notEqual(estimateModelCost(run(), table).amount_usd, null);
  const result = estimateModelCost(run({ usage: { input_tokens: 400000, cached_input_tokens: 100000, output_tokens: 100 } }), table);
  assert.equal(result.amount_usd, null);
  assert.match(result.reason, /per-request/);
  assert.equal(estimateModelCost(run(), prices({ cache_read_input_token_cost: undefined })).amount_usd, null);
});

test('summary includes failed trials, excludes environment failures, and never fills missing usage with zero', () => {
  const a = run();
  const b = run({ run_id: 'two', status: 'not_completed', usage: { input_tokens: 3000, cached_input_tokens: 2000, output_tokens: 100 }, service_cost_usd: .4 });
  const invalid = run({ run_id: 'bad', status: 'invalid_run', usage: null });
  const value = summarize([a, b, invalid]);
  assert.equal(value.resolution_rate, .5);
  assert.equal(value.tokens, 2100); // total input already includes cached tokens
  assert.equal(value.service_cost_usd, .2);
  assert.equal(value.invalid, 1);
  assert.equal(summarize([a, { ...b, usage: null }]).tokens, null);
  assert.equal(summarize([a, { ...b, model_cost: undefined }]).model_cost_usd, null);
  assert.equal(summarize([a, { ...b, service_cost_usd: null }]).service_cost_usd, null);
  assert.equal(summarize([invalid]).resolution_rate, null);
});

test('boards pool identical task sets and repetitions, but separate versions, models, budgets, preparation and routes', () => {
  const a = run();
  const b = run({ run_id: 'b', service_id: 'b' });
  assert.equal(buildBoards([a, b]).length, 1);
  for (const patch of [
    { model: 'different' }, { budget_seconds: 300 }, { environment: { service_credentials: 'provided: KEY' } },
    { task: { ...b.task, sha256: 'new', version: 'v2' } },
  ]) assert.equal(buildBoards([a, { ...b, ...patch }]).length, 2);
  const task2 = { ...a.task, id: 'two', sha256: 'two' };
  assert.equal(buildBoards([a, { ...a, run_id: 'a2', task: task2 }, b]).length, 2);
  const both = buildBoards([a, { ...a, run_id: 'a2', task: task2 }, b, { ...b, run_id: 'b2', task: task2 }]);
  assert.equal(both.length, 1);
  assert.equal(both[0].tasks.length, 2);
  assert.equal(both[0].rows[0].metrics.trials, 2);
  assert.equal(buildBoards([a, { ...a, run_id: 'repeat' }, b]).length, 2);
  assert.equal(buildBoards([a, { ...a, route_id: 'mcp', run_id: 'mcp' }])[0].rows.length, 2);
});

test('historical task versions are retained in records but not pooled into current scores', () => {
  const old = run({ started_at: '2026-09-01T00:00:00Z' });
  const current = run({ run_id: 'new', task: { ...old.task, sha256: 'new', version: 'v2' } });
  const records = [old, current];
  assert.deepEqual(buildBoards(records)[0].rows[0].runs.map(r => r.run_id), ['new']);
  assert.equal(records.length, 2);
});

test('per-request billing applies context tiers to each call, with final totals reconciled', () => {
  const table = prices({ input_cost_per_token_above_1000_tokens: .000004,
    cache_read_input_token_cost_above_1000_tokens: .0000004, output_cost_per_token_above_1000_tokens: .00002 });
  const a = { input_tokens: 1000, cached_input_tokens: 200, output_tokens: 100 };
  const b = { input_tokens: 1500, cached_input_tokens: 500, output_tokens: 100 };
  const measured = (requests: typeof a[]) => run({ usage: {
    input_tokens: requests.reduce((n, r) => n + r.input_tokens, 0),
    cached_input_tokens: requests.reduce((n, r) => n + r.cached_input_tokens, 0),
    output_tokens: requests.reduce((n, r) => n + r.output_tokens, 0),
  }, request_usage: { status: 'complete', requests, method: 'session token_usage_record', reason: 'reconciled', source_sha256: 'a'.repeat(64) } });
  assert.equal(estimateModelCost(measured([a, a]), table).amount_usd, .00528);
  assert.equal(estimateModelCost(measured([a, b]), table).amount_usd, .00884);
  assert.equal(estimateModelCost(measured([a, b]), table).request_count, 2);
  const mismatch = measured([a, b]);
  mismatch.usage!.input_tokens++;
  assert.equal(estimateModelCost(mismatch, table).amount_usd, null);
  const partial = measured([a, b]);
  partial.request_usage!.status = 'incomplete';
  assert.equal(estimateModelCost(partial, table).amount_usd, null);
});


test('one display can contain separate comparison groups without combining their scores', () => {
  const a = run({ service_id: 'a', status: 'not_completed' });
  const b = run({ service_id: 'b', budget_seconds: 300 });
  const boards = buildBoards([a, b]);
  const original = JSON.stringify(boards);
  const names = new Map([['a', 'Alpha'], ['b', 'Beta']]);
  const rows = renderBoardRows(boards, names);
  assert.equal(rows.split('\n').length, 2);
  assert.match(rows, /Alpha.*0%/);
  assert.match(rows, /Beta.*100%/);
  assert(rows.indexOf('Alpha') < rows.indexOf('Beta')); // Alphabetical, not a cross-condition ranking.
  assert(!rows.includes('Tasks') && !rows.includes('<details>'));
  assert(!renderBoardDetails(boards, names, true).includes('<details>'));
  assert.equal(JSON.stringify(boards), original);
});


test('both homepages show one flights table with measured and untested services, and one disclosure', () => {
  for (const file of ['README.md', 'README.zh-CN.md']) {
    const page = fs.readFileSync(`${ROOT}/${file}`, 'utf8');
    const anchors = [...page.matchAll(/<a id="([^"]+)"/g)].map(m => m[1]);
    assert.equal(new Set(anchors).size, anchors.length);
    const section = page.split('<a id="services-travel-flights"></a>')[1].split('<a id="services-databases"></a>')[0];
    const visible = section.replace(/<details>[\s\S]*?<\/details>/g, '');
    assert.equal((visible.match(/<table /g) ?? []).length, 1);
    assert.equal((section.match(/<details>/g) ?? []).length, 1);
    for (const service of ['Kiwi.com', 'Ignav Flights', 'SerpApi', 'Amadeus']) assert(visible.includes(service));
    assert(!visible.includes('flights-search-001'));
    const detail = section.split('<details>')[1];
    assert.equal(detail.split('gpt-6-astra / xhigh').length - 1, 1);
    assert.equal(detail.split(file.includes('zh-CN') ? '找到9月25日米兰飞往荷兰的机票' : 'Find flights from Milan to the Netherlands on September 25').length - 1, 1);
    const readableDetail = detail.replace(/\]\([^)]+\)/g, ']');
    assert(!readableDetail.includes('flights-search-001') && !readableDetail.includes('legacy'));
    if (!file.includes('zh-CN')) assert(!/\p{Script=Han}/u.test(readableDetail));
    assert(!detail.includes('Amadeus') && !detail.includes('AirGateway'));
    assert(detail.includes(file.includes('zh-CN') ? '测了什么，怎么测的' : 'What we tested and how'));
  }
});


test('details explain shared tasks and configuration once, retaining access differences', () => {
  const task = { ...run().task, description: 'Find a flight', inputs: 'One adult', expected_output: 'Flight and price', success: 'Matches the live response', failure: 'No matching flight' };
  const a = run({ task, service_id: 'a', entry_url: 'https://example.com/mcp' });
  const b = run({ service_id: 'b', route_id: 'public-playground', task: { ...task, sha256: 'historical-other-hash' }, entry_url: 'https://example.com/playground' });
  const names = new Map([['a', 'Alpha'], ['b', 'Beta']]);
  const interfaces = new Map([['a/api', 'mcp'], ['b/public-playground', 'web']]);
  const text = renderBoardDetails(buildBoards([a, b]), names, true, './', interfaces);
  assert.equal(text.split('Find a flight').length - 1, 1);
  assert.equal(text.split('example / high').length - 1, 1);
  assert.match(text, /Flight and price/);
  assert.match(text, /MCP/);
  assert.match(text, /网页 Playground/);
  assert.match(text, /Beta 的网页试跑成绩不代表/);
  assert(!text.includes('historical-other-hash'));
  const changed = { ...b, budget_seconds: 300, task: { ...task, inputs: 'Two adults', sha256: 'changed' } };
  const varying = renderBoardDetails(buildBoards([a, changed]), names, true, './', interfaces);
  assert.match(varying, /One adult/);
  assert.match(varying, /Two adults/);
  assert.match(varying, /本次任务/);
  assert.match(varying, /5 分钟/);
  assert.match(varying, /10 分钟/);
});
