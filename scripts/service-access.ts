import type { Provider } from './lib.ts';

const METHODS = ['api', 'sdk', 'cli', 'mcp'] as const;
/** Legacy MCP fields may be service endpoints or marketing pages. Only recognize
 * documentation/repository locations here; new records should use explicit docs. */
function legacyMcpDocs(url: string) {
  const u = new URL(url);
  return /(^|[.-])(docs|documentation|developer|developers)([.-]|$)/i.test(u.hostname)
    || /\/(docs?|guides?|reference|integrations?|user-docs)\//i.test(u.pathname)
    || (['github.com', 'gitlab.com'].includes(u.hostname) && u.pathname.split('/').filter(Boolean).length >= 2);
}
const values = (value: string | string[] | undefined) => [value ?? []].flat().filter(url => /^https:\/\//.test(url));
const priority = (url: string) => /(?:quick[-_]?start|getting-started|get-started|installation|\/install(?:\/|$))/i.test(url) ? 2
  : /(?:introduction|overview)/i.test(url) ? 1 : 0;

/** Curated reading links, not executable endpoints or proof of successful tests.
 * Route docs take priority; the original entry_url stays in service details. */
export function serviceAccess(p: Provider, zh = false): [string, string][] {
  const entries = p.entrypoints ?? {};
  const typed: [string, string][] = [];
  for (const method of METHODS) {
    const routeDocs = (p.catalog?.routes ?? []).filter(r => r.interface === method).flatMap(r => values(r.docs));
    const fallback = method === 'api' ? values(entries.api_reference)
      : method === 'sdk' ? values(entries.sdks)
      : method === 'cli' ? values(entries.cli)
      : values(entries.mcp_docs).length ? values(entries.mcp_docs)
      : values(entries.mcp_official).filter(legacyMcpDocs);
    const urls = [...new Set([...routeDocs, ...fallback])];
    // Prefer a known onboarding guide to endpoint reference; stable order breaks ties.
    urls.sort((a, b) => priority(b) - priority(a));
    if (urls[0]) typed.push([method.toUpperCase(), urls[0]]);
  }
  if (!typed.length) {
    const docs = values(entries.docs)[0] ?? (p.catalog?.routes ?? []).flatMap(r => values(r.docs))[0];
    return docs ? [[zh ? '文档' : 'Docs', docs]] : [];
  }
  // One shared guide can explain multiple methods; link to it once without hiding a method.
  const byUrl = new Map<string, string[]>();
  for (const [label, url] of typed) byUrl.set(url, [...(byUrl.get(url) ?? []), label]);
  return [...byUrl].map(([url, labels]) => [labels.join(' / '), url]);
}
