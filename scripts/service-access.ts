import type { Provider } from './lib.ts';

/** Public links only. A documented entry point is not a successful task test. */
export function serviceAccess(p: Provider, zh = false): [string, string][] {
  const links: [string, string][] = [];
  const add = (label: string, value: string | string[] | undefined) => {
    for (const url of [value ?? []].flat()) {
      if (/^https?:\/\//.test(url) && !links.some(([n, u]) => n === label && u === url)) links.push([label, url]);
    }
  };
  add(zh ? '文档' : 'Docs', p.entrypoints.docs);
  for (const route of p.catalog?.routes ?? []) {
    add(zh ? '文档' : 'Docs', route.docs);
    add(route.interface === 'web' ? (zh ? '网页' : 'Web') : route.interface.toUpperCase(), route.entry_url);
  }
  for (const [field, label] of Object.entries({ api_reference: 'API', cli: 'CLI', sdks: 'SDK', mcp_official: 'MCP' })) {
    add(label, p.entrypoints[field]);
  }
  return links;
}
