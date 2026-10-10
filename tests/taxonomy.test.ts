import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { Ajv } from 'ajv';
import { ROOT, loadCategories, loadProviders, loadCandidates } from '../scripts/lib.ts';
import { catalogErrors, catalogService, taxonomyErrors } from '../scripts/catalog.ts';
import { categoryTree, searchServices } from '../mcp/catalog.mjs';
import { flattenCategories, inClassification, classificationCapabilities } from '../scripts/taxonomy.mjs';
import { loadEvaluations } from '../scripts/evaluations.ts';
import { buildBoards } from '../scripts/leaderboard.ts';
import { loadTaskClassifications, taskClassificationErrors } from '../scripts/task-classifications.ts';

const categories = loadCategories();
const providers = [...loadProviders(), ...loadCandidates()].map(record => record.data);
const data = { categories, services: providers.map(p => catalogService(p, 'candidate', loadEvaluations())) };
const finance = 'web-search-data/financial-data';
const today = new Date().toISOString().slice(0, 10);
const ids = (filters: Record<string, string>) => searchServices(data, filters).map(s => s.id);

test('classification paths accept deeper branches, inherit only ancestor capabilities and require definitions', () => {
  const tree = structuredClone(categories);
  const fx = tree.find(c => c.id === 'web-search-data')!.subcategories!.find(c => c.id === 'financial-data')!.subcategories!.find(c => c.id === 'fx')!;
  fx.subcategories = [{ ...fx, id: 'reference-rates', capabilities: [] }];
  const p = structuredClone(providers.find(p => p.id === 'frankfurter')!);
  p.catalog!.classifications = [`${finance}/fx/reference-rates`];
  const valid = new Ajv().compile(JSON.parse(fs.readFileSync(`${ROOT}/schema/catalog.schema.json`, 'utf8')));
  assert.equal(valid(p.catalog), true);
  assert.deepEqual(catalogErrors(p, tree, today), []);
  p.catalog!.routes[0].capabilities!['prices.latest'] = { value: 'documented', evidence: ['docs'] };
  assert.match(catalogErrors(p, tree, today).join('\n'), /prices.latest does not belong/);
  assert(inClassification(p, finance));
  assert(!inClassification(p, `${finance}/fx/reference`));
  const researchScope = classificationCapabilities(tree, finance, true).map(c => c.id);
  assert(researchScope.includes('fx.history') && researchScope.includes('prices.latest'));
  assert(!researchScope.includes('web.fetch'));
  assert(!classificationCapabilities(tree, finance).length, 'parent service membership cannot assert child-only capabilities');
  delete fx.inclusion;
  assert.match(taxonomyErrors(tree).join('\n'), /Missing category inclusion/);
});

test('all legacy identities have a sourced classification, while narrow evidence gaps stay explicit', () => {
  assert(providers.every(p => p.catalog?.classifications.length && Object.keys(p.catalog.sources).length));
  assert.equal(new Set(providers.map(p => p.id)).size, providers.length);
  assert(ids({ classification: 'databases/vector' }).includes('chroma'));
  assert(ids({ classification: 'communication/voice-agents' }).includes('vapi'));
  assert(ids({ classification: 'productivity-storage/document-collaboration' }).includes('notion'));
  assert(!ids({ classification: 'web-search-data/web-search' }).includes('xquik'));
  for (const id of ['factset-data', 'joinquant-data', 'lseg-data', 'nasdaq-data-link']) {
    const p = providers.find(p => p.id === id)!;
    assert.deepEqual(p.catalog!.classifications, [finance]);
    assert(p.catalog!.notes?.length);
  }
  const modern = { category: 'communication', catalog: { classifications: ['productivity-storage/collaborative-tables'] } };
  assert(!inClassification(modern, 'communication'), 'legacy primary category must not silently add modern membership');
});

test('financial parent queries include all child types once, while prices and disclosures stay distinct', () => {
  const parent = ids({ classification: finance });
  assert.equal(parent.length, new Set(parent).size);
  for (const suffix of ['fx', 'prices', 'statements', 'disclosures', 'macro']) {
    for (const id of ids({ classification: `${finance}/${suffix}` })) assert(parent.includes(id));
  }
  assert(ids({ classification: `${finance}/disclosures` }).includes('bargo-congress'));
  assert(!ids({ classification: `${finance}/prices` }).includes('bargo-congress'));
  assert(ids({ classification: `${finance}/prices` }).includes('agentservices'));
  assert(!ids({ classification: `${finance}/fx` }).includes('agentservices'));
  assert(!ids({ classification: `${finance}/prices`, capability: 'prices.history' }).includes('agentservices'));
  assert(!ids({ classification: `${finance}/fx`, capability: 'prices.latest' }).length);
  const financeNode = flattenCategories(categoryTree(data)).find(n => n.path === finance)!;
  assert.equal(financeNode.services, parent.length);
});

test('search results cannot masquerade as specified-URL extraction or inherit a search trial', () => {
  const searchOnly = structuredClone(providers.find(p => p.id === 'exa')!);
  searchOnly.catalog!.classifications = ['web-search-data/web-search'];
  assert.match(catalogErrors(searchOnly, categories, today).join('\n'), /web.fetch does not belong/);
  const searchEvaluations = loadEvaluations().filter(e => e.task.id === 'web-search-001');
  const searchData = { categories, services: providers.map(p => catalogService(p, 'candidate', searchEvaluations)) };
  const fetch = searchServices(searchData, { classification: 'web-search-data/web-extraction', capability: 'web.fetch' });
  const firecrawl = fetch.find(s => s.id === 'firecrawl')!;
  assert(firecrawl.routes.some(r => r.id === 'public-scrape-api'));
  assert(firecrawl.routes.some(r => r.id === 'account-scrape-api'));
  assert(fetch.find(s => s.id === 'tavily')!.routes.some(r => r.id === 'extract-api'));
  assert(fetch.find(s => s.id === 'jina')!.routes.some(r => r.id === 'reader-api'));
  assert(fetch.every(s => s.route_tests === 'not_recorded' && s.routes.every(r => !r.task_runs.length)));
  const search = searchServices(searchData, { classification: 'web-search-data/web-search' });
  assert(search.find(s => s.id === 'exa')!.routes.some(r => r.task_runs.length));
});

test('shared finance setup is separated from FX business results in queries and comparison means', () => {
  // Scope the historical fixture to these task families; new macro trials must
  // not alter the setup/FX separation this regression exercises.
  const fixtureEvaluations = loadEvaluations().filter(e => ['financial-fx-001', 'financial-access-001'].includes(e.task.id));
  const fixtureData = { categories, services: providers.map(p => catalogService(p, 'candidate', fixtureEvaluations)) };
  const fx = searchServices(fixtureData, { classification: `${finance}/fx` }).find(s => s.id === 'ecb-data')!;
  const runs = fx.routes.flatMap(r => r.task_runs);
  assert(runs.length > 0);
  assert.deepEqual(new Set(runs.map(r => r.task.id)), new Set(['financial-fx-001']));
  assert(runs.every(r => r.phase === 'business'));
  const all = searchServices(fixtureData, { classification: finance }).find(s => s.id === 'ecb-data')!;
  assert(all.routes.flatMap(r => r.task_runs).some(r => r.phase === 'setup'));
  const boards = buildBoards(fixtureEvaluations).filter(b => b.rows.some(r => r.service_id === 'ecb-data'));
  assert.deepEqual(new Set(boards.map(b => `${b.classification}:${b.phase}`)), new Set([`${finance}:setup`, `${finance}/fx:business`]));
  assert(boards.every(b => b.tasks.length === 1));
  assert(boards.filter(b => b.phase === 'business').every(b => b.rows.every(r => r.metrics.trials === 1)));
  assert(boards.filter(b => b.phase === 'setup').every(b => b.tasks[0].id === 'financial-access-001'));
  const macro = searchServices(fixtureData, { classification: `${finance}/macro` }).find(s => s.id === 'ecb-data')!;
  assert.equal(macro.route_tests, 'not_recorded');
});

test('task display mapping covers executable tasks and rejects dangling or duplicate assignments', () => {
  const mappings = loadTaskClassifications();
  assert.deepEqual(taskClassificationErrors(), []);
  assert.match(taskClassificationErrors([...mappings, mappings[0]]).join('\n'), /Duplicate task classification/);
  assert.match(taskClassificationErrors(mappings.slice(1)).join('\n'), /lacks display classification/);
  assert.match(taskClassificationErrors([{ ...mappings[0], classification: `${finance}/typo` }]).join('\n'), /Unknown task classification/);
});
