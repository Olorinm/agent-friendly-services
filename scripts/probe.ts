/**
 * Probes every URL in the dataset (entrypoints, evidence, homepages) and
 * writes generated/link-health.json.
 *
 * Classification:
 *   ok           2xx/3xx — the page answers
 *   inconclusive client/auth/protocol errors (including 406) — re-check the request;
 *                NEVER treated as broken (WAFs routinely block CI runners)
 *   broken       404/410/5xx or repeated network failure
 *
 * Usage: npm run probe [-- --only=stripe,github] [--output=path]
 * Targeted checks default to ignored local output, preserving the full weekly report.
 */
import fs from 'node:fs';
import path from 'node:path';
import { ROOT, GENERATED_DIR, loadProviders, loadCandidates, providerUrls } from './lib.ts';

import { probeUrl } from './link-probe.ts';

const CONCURRENCY = 8;
const only = process.argv.find(a => a.startsWith('--only='))?.slice('--only='.length).split(',');
const output = process.argv.find(a => a.startsWith('--output='))?.slice('--output='.length)
  ?? path.join(only ? path.join(ROOT, 'data/experiments/results') : GENERATED_DIR, only ? 'selected-link-health.json' : 'link-health.json');

async function main() {
  // Candidate-pool URLs are probed too — a dead link in a candidate is a fact
  // worth surfacing before anyone reviews it.
  const providers = [...loadProviders(), ...loadCandidates()].filter((p) => !only || only.includes(p.data.id));
  const byUrl = new Map<string, string[]>();
  for (const p of providers) {
    for (const { url, source } of providerUrls(p.data)) {
      const tag = `${p.data.id}:${source}`;
      byUrl.set(url, [...(byUrl.get(url) ?? []), tag]);
    }
  }

  const mcpUrls = new Set(providers.flatMap(p => [
    ...[p.data.entrypoints.mcp_official ?? []].flat(),
    ...(p.data.catalog?.routes ?? []).filter(r => r.interface === 'mcp').map(r => r.entry_url),
  ]));
  const urls = [...byUrl.keys()];
  console.log(`Probing ${urls.length} unique URLs from ${providers.length} providers...`);

  const results: (Awaited<ReturnType<typeof probeUrl>> & { url: string; sources: string[] })[] = [];
  let cursor = 0;
  async function worker() {
    while (cursor < urls.length) {
      const url = urls[cursor++];
      const r = await probeUrl(url, { mcp: mcpUrls.has(url) });
      results.push({ url, ...r, sources: byUrl.get(url)! });
      const mark = r.class === 'ok' ? '·' : r.class === 'inconclusive' ? '?' : '✗';
      process.stdout.write(mark);
    }
  }
  await Promise.all(Array.from({ length: CONCURRENCY }, worker));
  process.stdout.write('\n');

  results.sort((a, b) => a.url.localeCompare(b.url));
  const summary = {
    ok: results.filter((r) => r.class === 'ok').length,
    inconclusive: results.filter((r) => r.class === 'inconclusive').length,
    broken: results.filter((r) => r.class === 'broken').length,
  };

  fs.mkdirSync(path.dirname(output), { recursive: true });
  fs.writeFileSync(
    output,
    JSON.stringify({ checked_at: new Date().toISOString(), total: results.length, ...summary, results }, null, 2) + '\n',
  );

  console.log(`\nok ${summary.ok} · inconclusive ${summary.inconclusive} · broken ${summary.broken}`);
  for (const cls of ['broken', 'inconclusive'] as const) {
    const list = results.filter((r) => r.class === cls);
    if (list.length) {
      console.log(`\n${cls.toUpperCase()}:`);
      for (const r of list) console.log(`  [${r.status ?? r.detail}] ${r.url}\n      ${r.sources.join(', ')}`);
    }
  }
  // Broken links fail the run so weekly CI can open an issue; inconclusive never fails.
  if (summary.broken > 0) process.exitCode = 2;
}

await main();
