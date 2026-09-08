import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { test } from 'node:test';
import { Ajv } from 'ajv';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js';
import { ROOT, loadCategories, loadProviders, providerUrls, type Provider } from '../scripts/lib.ts';
import { calendarDateValid, catalogErrors, catalogService, taxonomyErrors } from '../scripts/catalog.ts';
import { searchServices } from '../mcp/catalog.mjs';

const ajv = new Ajv({ allErrors: true });
ajv.addSchema(JSON.parse(fs.readFileSync(path.join(ROOT, 'schema/catalog.schema.json'), 'utf8')));
const valid = ajv.compile(JSON.parse(fs.readFileSync(path.join(ROOT, 'schema/provider.schema.json'), 'utf8')));
const categories = loadCategories();
const today = '2026-09-07';
function fixture(): Provider {
  return {
    id: 'example', name: 'Example', category: 'travel', homepage: 'https://example.com/',
    summary: 'A candidate with publicly documented access.', submitted_by: 'community', entrypoints: {}, checks: {},
    catalog: {
      version: 1, classifications: ['travel/flights'],
      sources: { docs: { url: 'https://example.com/docs', checked_on: today, kind: 'official_docs' } },
      routes: [],
    },
  };
}
function withRoute() {
  const p = fixture();
  p.catalog!.routes.push({ id: 'api', interface: 'api', maintainer: 'official', entry_url: 'https://example.com/api', evidence: ['docs'] });
  return p;
}

test('a sourced discovery candidate needs no docs, account, callable route or legacy checks', () => {
  const p = fixture();
  const { entrypoints, checks, ...minimal } = p;
  assert.equal(valid(minimal), true, JSON.stringify(valid.errors));
  assert.deepEqual(catalogErrors(p, categories, today), []);
  p.catalog!.sources = {};
  assert.equal(valid(p), false);
});

test('known facts require evidence; unknown stays unknown; rejection needs an explanation', () => {
  const p = withRoute(), r = p.catalog!.routes[0];
  r.personal_access = { value: 'unknown' };
  assert.equal(valid(p), true);
  r.personal_access = { value: 'documented' };
  assert.equal(valid(p), false);
  r.personal_access.evidence = ['docs'];
  assert.equal(valid(p), true);
  r.personal_access.value = 'restricted';
  assert.equal(valid(p), false);
  r.personal_access.notes = 'Requires an industry licence absent from the persona.';
  assert.equal(valid(p), true);
  r.personal_access.value = 'tested_pass';
  assert.equal(valid(p), false);
});

test('dangling evidence is rejected wherever it appears, including costs and human steps', () => {
  const p = withRoute(), r = p.catalog!.routes[0];
  r.human_steps = [{ step: 'Verify email', stage: 'signup', evidence: ['missing'] }];
  r.costs = [{ kind: 'usage', amount: 1, unit: 'credits', per: 'request', scope: 'search', evidence: ['missing'] }];
  assert.equal(catalogErrors(p, categories, today).filter(x => x.includes('missing source')).length, 2);
  r.evidence = ['constructor'];
  assert.equal(catalogErrors(p, categories, today).filter(x => x.includes('missing source')).length, 3);
});

test('classification and capability must exist and belong together', () => {
  const p = withRoute();
  p.catalog!.routes[0].capabilities = { 'flights.search': { value: 'documented', evidence: ['docs'] } };
  assert.deepEqual(catalogErrors(p, categories, today), []);
  p.catalog!.classifications = ['travel/hotels'];
  assert.match(catalogErrors(p, categories, today).join('\n'), /does not belong/);
  p.catalog!.classifications = ['travel/flightz'];
  assert.match(catalogErrors(p, categories, today).join('\n'), /Unknown classification/);
  assert.match(taxonomyErrors([...categories, categories[0]]).join('\n'), /duplicate category/);
});

test('calendar validation rejects impossible and future dates without rolling over', () => {
  for (const date of ['2026-02-30', '2026-13-01', '2026-09-08', 'garbage']) assert.equal(calendarDateValid(date, today), false);
  assert.equal(calendarDateValid('2024-02-29', today), true);
  const p = fixture();
  p.catalog!.sources.docs.checked_on = '2026-02-30';
  assert.match(catalogErrors(p, categories, today).join('\n'), /calendar date/);
});

test('route references reject duplicates, missing targets and dependency cycles', () => {
  const p = withRoute(), r = p.catalog!.routes[0];
  r.via = 'missing';
  assert.match(catalogErrors(p, categories, today).join('\n'), /missing route/);
  r.via = 'api';
  assert.match(catalogErrors(p, categories, today).join('\n'), /cycle/);
  delete r.via;
  p.catalog!.routes.push({ ...r });
  assert.match(catalogErrors(p, categories, today).join('\n'), /Duplicate route/);
});

test('money cannot be confused with credits; cost amounts and scope are explicit', () => {
  const p = withRoute();
  const cost = { kind: 'usage', amount: 2, unit: 'money', per: '1000 successful requests', scope: 'search only', evidence: ['docs'] };
  p.catalog!.routes[0].costs = [cost];
  assert.match(catalogErrors(p, categories, today).join('\n'), /require an ISO currency/);
  Object.assign(cost, { currency: 'USD' });
  assert.deepEqual(catalogErrors(p, categories, today), []);
  cost.unit = 'credits';
  assert.match(catalogErrors(p, categories, today).join('\n'), /only applies/);
  cost.amount = -1;
  assert.equal(valid(p), false);
});

test('URL probing includes sources and routes but never labels them task-tested', () => {
  const p = withRoute();
  assert(providerUrls(p).some(x => x.url === 'https://example.com/docs'));
  assert(providerUrls(p).some(x => x.url === 'https://example.com/api'));
  assert.equal(catalogService(p, 'provider').route_tests, 'not_recorded');
});

test('route filters cannot combine one route’s access with another route’s capability', () => {
  const p = withRoute();
  p.category = 'web-search-data';
  p.catalog!.routes[0].capabilities = { 'flights.search': { value: 'documented', evidence: ['docs'] } };
  p.catalog!.routes[0].personal_access = { value: 'restricted', evidence: ['docs'], notes: 'Invitation required.' };
  p.catalog!.routes.push({ id: 'mcp', interface: 'mcp', maintainer: 'official', entry_url: 'https://example.com/mcp', evidence: ['docs'], personal_access: { value: 'documented', evidence: ['docs'] } });
  const data = { services: [catalogService(p, 'provider'), catalogService(fixture(), 'candidate')] };
  assert.equal(searchServices(data, { category: 'travel' }).length, 2);
  assert.equal(searchServices(data, { capability: 'flights.search', personal_access: 'documented' }).length, 0);
  assert.equal(searchServices(data, { capability: 'flights.search', interface: 'mcp' }).length, 0);
  assert.equal(searchServices(data, { capability: 'flights.search', interface: 'api' }).length, 1);
});

test('discovery-only records cannot accidentally start the legacy paid verification runner', () => {
  assert.throws(() => execFileSync(process.execPath, ['--import', 'tsx', 'scripts/agent-verify.ts', '--provider=kiwi', '--layer=dry-fire'], { cwd: ROOT, stdio: 'pipe' }), /Discovery-only candidate/);
});

test('generated data and the real MCP protocol preserve legacy behavior and expose flight discovery', { timeout: 30000 }, async () => {
  const output = fs.mkdtempSync(path.join(os.tmpdir(), 'afs-catalog-test-'));
  const client = new Client({ name: 'catalog-regression', version: '1.0.0' });
  let connected = false;
  try {
    execFileSync(process.execPath, ['--import', 'tsx', 'scripts/generate.ts'], { cwd: ROOT, env: { ...process.env, AFS_OUTPUT_DIR: output }, stdio: 'pipe' });
    const read = (name: string) => JSON.parse(fs.readFileSync(path.join(output, 'generated', name), 'utf8'));
    const old = read('providers.json'), catalog = read('catalog.json');
    assert.equal(old.providers.length, loadProviders().length);
    assert(old.providers.every((p: any) => !p.catalog));
    assert.equal(catalog.services.filter((p: any) => p.id === 'serpapi').length, 1);
    assert(fs.readFileSync(path.join(output, 'generated/catalog.md'), 'utf8').includes('public-source claims'));
    assert(fs.readFileSync(path.join(output, 'README.zh-CN.md'), 'utf8').includes('收录标准'));
    const transport = new StdioClientTransport({ command: process.execPath, args: [path.join(ROOT, 'mcp/server.mjs')], env: { AFS_DATA_DIR: path.join(output, 'generated') }, stderr: 'pipe' });
    await client.connect(transport); connected = true;
    const names = (await client.listTools()).tools.map(t => t.name);
    for (const name of ['search_services', 'get_service', 'search_providers', 'get_provider', 'list_categories', 'get_stats']) assert(names.includes(name));
    const call = async (name: string, args: Record<string, unknown> = {}) => {
      const response = await client.callTool({ name, arguments: args });
      assert(!response.isError, JSON.stringify(response));
      return JSON.parse((response.content as { type: string; text: string }[])[0].text);
    };
    const flights = await call('search_services', { subcategory: 'travel/flights' });
    assert(flights.services.some((p: any) => p.id === 'kiwi'));
    assert(flights.services.some((p: any) => p.id === 'serpapi'));
    assert(flights.services.some((p: any) => p.id === 'qunar-flights' && p.routes.length === 0));
    const kiwi = (await call('get_service', { id: 'KIWI' })).service;
    assert.equal(kiwi.route_tests, 'recorded');
    assert(kiwi.task_runs.some((run: any) => run.route_id === 'search-mcp' && run.status === 'completed' && run.usage.input_tokens > 0));
    for (const run of kiwi.task_runs) {
      assert(!('agent_cost_usd' in run) && !('agent_cost_note' in run));
      assert('service_cost_usd' in run);
      assert(['estimated', 'unknown'].includes(run.model_cost.kind));
      assert(run.model_cost.pricing.sha256);
    }
    const searchedRuns = flights.services.find((s: any) => s.id === 'kiwi').routes.flatMap((r: any) => r.task_runs);
    assert(searchedRuns.length > 0);
    for (const run of searchedRuns) {
      assert(!('agent_cost_usd' in run));
      assert.deepEqual(run.usage, kiwi.task_runs.find((r: any) => r.run_id === run.run_id).usage);
      assert.deepEqual(run.model_cost, kiwi.task_runs.find((r: any) => r.run_id === run.run_id).model_cost);
    }
    assert.equal(kiwi.catalog.routes.find((r: any) => r.id === 'tequila-api').task_run_ids.length, 0);
    assert(kiwi.catalog.routes.find((r: any) => r.id === 'search-mcp').task_run_ids.length > 0);
    const onlyApi = (await call('search_services', { query: 'kiwi', interface: 'api' })).services[0];
    assert.equal(onlyApi.route_tests, 'not_recorded');
    assert(onlyApi.routes.every((r: any) => r.task_runs.length === 0));
    assert.equal(kiwi.catalog.routes.find((r: any) => r.id === 'tequila-api').availability.value, 'invite_only');
    assert.notEqual(kiwi.catalog.routes.find((r: any) => r.id === 'search-mcp').availability.value, 'invite_only');
    const cache = (await call('get_service', { id: 'flight-mcp' })).service.catalog.routes.find((r: any) => r.id === 'public-cache-mcp');
    assert.equal(cache.data_kind.value, 'cached');
    assert.equal((await call('search_providers', { query: 'kiwi' })).count, 0);
    assert.equal((await call('get_provider', { id: 'serpapi' })).provider.id, 'serpapi');
    assert((await call('search_services', { subcategory: 'travel/typo' })).error);
    assert((await call('get_service', { id: 'missing' })).error);
  } finally {
    if (connected) await client.close();
    fs.rmSync(output, { recursive: true, force: true });
  }
});
