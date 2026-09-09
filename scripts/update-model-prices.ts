/** Refresh only models used in recorded trials. Generation itself remains offline. */
import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { ROOT } from './lib.ts';
import { loadEvaluations } from './evaluations.ts';
const repo = 'https://api.github.com/repos/BerriAI/litellm/commits/main';
async function get(url: string) {
  const response = await fetch(url, { headers: { 'User-Agent': 'agent-friendly-services' }, signal: AbortSignal.timeout(30000) });
  if (!response.ok) throw new Error(`Price fetch failed: HTTP ${response.status}`);
  return response.json();
}
const { sha: revision } = await get(repo);
if (!/^[0-9a-f]{40}$/.test(revision)) throw new Error('Invalid LiteLLM revision');
const source = `https://raw.githubusercontent.com/BerriAI/litellm/${revision}/model_prices_and_context_window.json`;
const table = await get(source);
const wanted = [...new Set([...loadEvaluations().map(r => r.model), ...process.argv.slice(2)])].sort();
const models: Record<string, Record<string, unknown>> = {};
for (const model of wanted) {
  const key = table[model] ? model : model.startsWith("glm-") ? `zai/${model}` : `openai/${model}`;
  if (!table[key]) { console.warn(`No LiteLLM price for ${model}`); continue; }
  models[key] = table[key];
}
const output = path.join(ROOT, 'data/pricing/litellm.json');
fs.mkdirSync(path.dirname(output), { recursive: true });
fs.writeFileSync(output, JSON.stringify({ source, revision, fetched_at: new Date().toISOString(),
  sha256: createHash('sha256').update(JSON.stringify(models)).digest('hex'), models }, null, 2) + '\n');
console.log(`Saved LiteLLM prices for ${Object.keys(models).length} model(s). Run npm run generate.`);
