/**
 * Probes every URL in the dataset (entrypoints, evidence, homepages) and
 * writes generated/link-health.json.
 *
 * Classification:
 *   ok           2xx/3xx — the page answers
 *   inconclusive 401/403/405/429 or a bot challenge — a human should re-check;
 *                NEVER treated as broken (WAFs routinely block CI runners)
 *   broken       404/410/5xx or repeated network failure
 *
 * Usage: npm run probe [-- --only=stripe,github]
 */
import fs from 'node:fs';
import path from 'node:path';
import { GENERATED_DIR, loadProviders, providerUrls } from './lib.ts';

const UA = 'agent-friendly-services-probe/0.1 (link health check; non-commercial index)';
const TIMEOUT_MS = 15_000;
const CONCURRENCY = 8;

type Cls = 'ok' | 'inconclusive' | 'broken';

interface Result {
  url: string;
  class: Cls;
  status: number | null;
  detail?: string;
  sources: string[];
}

const only = process.argv
  .find((a) => a.startsWith('--only='))
  ?.slice('--only='.length)
  .split(',');

async function fetchStatus(url: string, method: 'HEAD' | 'GET'): Promise<{ status: number } | { error: string }> {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), TIMEOUT_MS);
  try {
    const res = await fetch(url, {
      method,
      redirect: 'follow',
      signal: ctrl.signal,
      headers: { 'user-agent': UA, accept: '*/*' },
    });
    // Drain tiny bit / cancel body so sockets free up.
    try {
      await res.body?.cancel();
    } catch {
      /* ignore */
    }
    return { status: res.status };
  } catch (e) {
    return { error: e instanceof Error ? (e.cause as Error | undefined)?.message ?? e.message : String(e) };
  } finally {
    clearTimeout(timer);
  }
}

function classify(status: number): Cls {
  if (status >= 200 && status < 400) return 'ok';
  if ([401, 403, 405, 407, 429].includes(status)) return 'inconclusive';
  return 'broken';
}

async function probe(url: string): Promise<Omit<Result, 'sources' | 'url'>> {
  let r = await fetchStatus(url, 'HEAD');
  // Many servers reject HEAD (405) or treat it oddly — retry with GET on any non-2xx.
  if ('error' in r || r.status >= 300) {
    const g = await fetchStatus(url, 'GET');
    if (!('error' in g)) r = g;
    else if ('error' in r) {
      // two network failures in a row
      const retry = await fetchStatus(url, 'GET');
      if ('error' in retry) return { class: 'broken', status: null, detail: retry.error };
      r = retry;
    }
  }
  if ('error' in r) return { class: 'broken', status: null, detail: r.error };
  return { class: classify(r.status), status: r.status };
}

async function main() {
  const providers = loadProviders().filter((p) => !only || only.includes(p.data.id));
  const byUrl = new Map<string, string[]>();
  for (const p of providers) {
    for (const { url, source } of providerUrls(p.data)) {
      const tag = `${p.data.id}:${source}`;
      byUrl.set(url, [...(byUrl.get(url) ?? []), tag]);
    }
  }

  const urls = [...byUrl.keys()];
  console.log(`Probing ${urls.length} unique URLs from ${providers.length} providers...`);

  const results: Result[] = [];
  let cursor = 0;
  async function worker() {
    while (cursor < urls.length) {
      const url = urls[cursor++];
      const r = await probe(url);
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

  fs.mkdirSync(GENERATED_DIR, { recursive: true });
  fs.writeFileSync(
    path.join(GENERATED_DIR, 'link-health.json'),
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
