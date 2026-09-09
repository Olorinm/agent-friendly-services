import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { ROOT } from './lib.ts';
import type { Evaluation } from './evaluations.ts';

export interface PriceSnapshot {
  source: string; revision: string; fetched_at: string; sha256: string;
  models: Record<string, Record<string, unknown>>;
}
export interface ModelCost {
  amount_usd: number | null;
  kind: 'estimated' | 'unknown';
  reason: string;
  pricing: { source: string; revision: string; fetched_at: string; sha256: string; model: string; tier: string } | null;
  rates?: Record<string, number>;
  request_count?: number;
}
export function loadPrices(root = ROOT): PriceSnapshot | null {
  const file = path.join(root, 'data/pricing/litellm.json');
  if (!fs.existsSync(file)) return null;
  const value = JSON.parse(fs.readFileSync(file, 'utf8')) as PriceSnapshot;
  const hash = createHash('sha256').update(JSON.stringify(value.models)).digest('hex');
  if (value.sha256 !== hash) throw new Error('LiteLLM snapshot hash mismatch; run npm run pricing:update');
  return value;
}
const rate = (value: unknown): value is number => typeof value === 'number' && Number.isFinite(value) && value >= 0;

/** Use the stored LiteLLM standard-tier prices; never substitute a different model. */
export function estimateModelCost(run: Pick<Evaluation, 'model' | 'usage' | 'request_usage'>, prices: PriceSnapshot | null): ModelCost {
  return calculate(run, prices);
}
function calculate(run: Pick<Evaluation, 'model' | 'usage' | 'request_usage'>, prices: PriceSnapshot | null, singleRequest = false): ModelCost {
  const key = prices?.models[run.model] ? run.model : run.model.startsWith("glm-") ? `zai/${run.model}` : `openai/${run.model}`;
  const entry = prices?.models[key];
  const pricing = prices && entry ? { source: prices.source, revision: prices.revision,
    fetched_at: prices.fetched_at, sha256: prices.sha256, model: key, tier: 'standard' } : null;
  const unknown = (reason: string): ModelCost => ({ amount_usd: null, kind: 'unknown', reason, pricing });
  if (!entry) return unknown('No matching model in the saved LiteLLM price table.');
  if (run.request_usage) {
    const detail = run.request_usage;
    if (detail.status !== 'complete' || !Array.isArray(detail.requests) || !detail.requests.length || !run.usage)
      return unknown('Per-request usage capture is incomplete.');
    for (const field of ['input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'output_tokens', 'reasoning_output_tokens'] as const) {
      const sum = detail.requests.reduce((n, r) => n + (r[field] ?? 0), 0);
      if (sum !== (run.usage[field] ?? 0)) return unknown('Per-request usage does not match session totals.');
    }
    const costs = detail.requests.map(usage => calculate({ model: run.model, usage }, prices, true));
    const missing = costs.find(c => c.amount_usd === null);
    if (missing) return missing;
    return { amount_usd: Number(costs.reduce((n, c) => n + c.amount_usd!, 0).toFixed(10)), kind: 'estimated',
      pricing: pricing ? { ...pricing, tier: 'standard; context tier selected per request' } : null,
      request_count: costs.length, reason: 'Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees.' };
  }
  const usage = run.usage;
  if (!usage) return unknown('Token usage was not reported.');
  const { input_tokens: input, cached_input_tokens: cached, output_tokens: output } = usage;
  const write = usage.cache_write_input_tokens ?? 0;
  if (![input, cached, output, write].every(v => Number.isInteger(v) && v >= 0) || cached + write > input)
    return unknown('Invalid token accounting.');
  // Aggregate session input cannot identify the context tier of each API call.
  // If even aggregate input is below every threshold, all calls must be below it.
  const thresholds = Object.keys(entry).flatMap(k => {
    const m = k.match(/_above_(\d+)(k)?_tokens/);
    return m ? [Number(m[1]) * (m[2] ? 1000 : 1)] : [];
  });
  if (!singleRequest && thresholds.some(limit => input > limit))
    return unknown('Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier.');
  if (usage.cache_write_input_tokens === undefined && entry.litellm_provider === 'anthropic')
    return unknown('Cache-write usage is missing.');
  const priceFor = (base: string) => {
    if (!singleRequest) return entry[base];
    const tiers = Object.keys(entry).flatMap(k => {
      if (!k.startsWith(`${base}_above_`)) return [];
      const m = k.slice(base.length).match(/^_above_(\d+)(k)?_tokens$/);
      return m ? [{ key: k, limit: Number(m[1]) * (m[2] ? 1000 : 1) }] : [];
    }).filter(t => input > t.limit).sort((a, b) => b.limit - a.limit);
    return entry[tiers[0]?.key ?? base];
  };
  const rates: Record<string, number> = {};
  const terms: [string, number, unknown][] = [
    ['input', input - cached - write, priceFor('input_cost_per_token')],
    ['cache_read', cached, priceFor('cache_read_input_token_cost')],
    ['cache_write', write, priceFor('cache_creation_input_token_cost')],
    ['output', output, priceFor('output_cost_per_token')],
  ];
  let amount = 0;
  for (const [name, count, price] of terms) {
    if (!count) continue;
    if (!rate(price)) return unknown(`Missing LiteLLM ${name} rate.`);
    rates[name] = price;
    amount += count * price;
  }
  return { amount_usd: Number(amount.toFixed(10)), kind: 'estimated', pricing, rates,
    reason: 'Actual recorded usage × saved LiteLLM standard API rates; estimate at the snapshot date, not an account charge. Excludes non-token tool fees.' };
}
