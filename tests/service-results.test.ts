import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { ROOT, loadCandidates, loadProviders } from '../scripts/lib.ts';
import { buildBoards } from '../scripts/leaderboard.ts';
import { loadEvaluations } from '../scripts/evaluations.ts';
import { renderServiceResults, renderSetup } from '../scripts/service-results.ts';
import { loadPrices, estimateModelCost } from '../scripts/model-costs.ts';

const providers = [...loadProviders(), ...loadCandidates()].map(p => p.data);
const records = loadEvaluations().map(r => ({ ...r, model_cost: estimateModelCost(r, loadPrices()) }));

test('Kiwi details show current MCP costs, retain untested API and keep old runs out of the mean', () => {
  const p = providers.find(p => p.id === 'kiwi')!;
  const runs = records.filter(r => r.service_id === p.id);
  const text = renderServiceResults(p, buildBoards(runs), runs);
  assert.match(text, /209\.6k \| \$0\.84 \| \$0/);
  assert.match(text, /\| API \| — \| — \| — \| — \| — \|/);
  assert(!text.includes('CLI'));
  assert.match(text, /Run history \(3\)/);
  const setup = renderSetup(p, runs);
  assert(!setup.includes('209.6k') && !setup.includes('Autonomous'));
  assert.match(setup, /\| — \| — \| — \|/);
});

test('historical Exa MCP success and API failure remain separate without later trials changing the fixture', () => {
  const p = providers.find(p => p.id === 'exa')!;
  const runs = records.filter(r => r.service_id === p.id && r.started_at.startsWith('2026-09-07'));
  const text = renderServiceResults(p, buildBoards(runs), runs);
  assert.match(text, /\| Conditions \|/);
  assert.match(text, /\| API .*\[0%\]/);
  assert.match(text, /\| MCP .*\[100%\]/);
  assert.match(text, /931\.5k/);
  assert(!text.includes('50%'));
});

test('supplied and unspecified account descriptions never become anonymous starting resources', () => {
  const p = providers.find(p => p.id === 'exa')!;
  const base = structuredClone(records.find(r => r.service_id === p.id)!);
  const conditions = ['none', 'controller-registered ordinary free API key', 'pre-existing management account', 'unknown'];
  const samples = conditions.map((value, i) => ({ ...structuredClone(base), run_id: `credential-fixture-${i}`, service_id: `credential-service-${i}`,
    environment: { ...base.environment, service_credentials: value } }));
  assert.equal(buildBoards(samples).length, 4, 'different credential prerequisites must not be pooled');
  for (const sample of samples.slice(1)) {
    const text = renderSetup(p, [sample]);
    assert(!text.includes('No account or key supplied'));
    assert.match(text, /controller-registered|pre-existing|preparation unknown/);
  }
});

test('machine summaries identify exactly one selected protocol per service and task family', () => {
  const json = JSON.parse(fs.readFileSync(`${ROOT}/generated/evaluations.json`, 'utf8'));
  const keys = json.service_summaries.map((s: any) => `${s.classification}:${s.phase}:${s.task_file}:${s.service_id}`);
  assert.equal(new Set(keys).size, keys.length);
  const kiwi = json.service_summaries.find((s: any) => s.service_id === 'kiwi');
  assert.equal(kiwi.route_id, 'search-mcp');
  assert.equal(kiwi.metrics.tokens, 209551);
  assert.equal(kiwi.metrics.trials, 1);
});
