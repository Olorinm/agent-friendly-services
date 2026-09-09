import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { ROOT, loadProviders, loadCandidates, type Provider } from '../scripts/lib.ts';
import { serviceAccess } from '../scripts/service-access.ts';
const services = [...loadProviders(), ...loadCandidates()].map(p => p.data);
const get = (id: string) => services.find(p => p.id === id)!;

test('access links point to typed documentation; actual service endpoints stay separate', () => {
  assert.deepEqual(serviceAccess(get('ignav')), [['API', 'https://ignav.com/docs'], ['MCP', 'https://ignav.com/docs/mcp']]);
  assert.deepEqual(serviceAccess(get('kiwi')), [['MCP', 'https://www.kiwi.com/en/pages/mcp/']]);
  assert.equal(get('kiwi').catalog!.routes[0].entry_url, 'https://mcp.kiwi.com');
  assert.equal(serviceAccess(get('amadeus-flights')).length, 0);
  assert.equal(get('amadeus-flights').catalog!.routes.length, 2);
  assert.equal(serviceAccess(get('alipay')).length, 0);
});

test('explicit setup docs replace ambiguous MCP entrypoints without deleting the originals', () => {
  for (const id of ['hugging-face', 'composio', 'zapier']) {
    const p = get(id);
    assert.equal(serviceAccess(p).find(([label]) => label === 'MCP')![1], p.entrypoints.mcp_docs);
    assert.notEqual(p.entrypoints.mcp_docs, p.entrypoints.mcp_official);
  }
  const p = { entrypoints: { docs: 'https://example.com/docs', mcp_official: 'https://mcp.example.com/mcp' } } as Provider;
  assert.deepEqual(serviceAccess(p), [['Docs', 'https://example.com/docs']]);
  assert.deepEqual(serviceAccess(p, true), [['文档', 'https://example.com/docs']]);
});

test('quickstarts are preferred, generic Docs disappear, shared guides are linked only once', () => {
  assert.equal(serviceAccess(get('exa')).find(([n]) => n === 'API')![1], 'https://docs.exa.ai/reference/getting-started');
  const p = { entrypoints: { docs: 'https://example.com/docs', api_reference: 'https://example.com/docs/quickstart', sdks: 'https://example.com/docs/quickstart' } } as Provider;
  assert.deepEqual(serviceAccess(p), [['API / SDK', 'https://example.com/docs/quickstart']]);
});

test('generated Agent links match the homepage selector for every catalog service', () => {
  const catalog = JSON.parse(fs.readFileSync(`${ROOT}/generated/catalog.json`, 'utf8'));
  for (const p of services) {
    const published = catalog.services.find((s: any) => s.id === p.id);
    assert.deepEqual(published.access_links, serviceAccess(p).map(([label, url]) => ({ label, url, kind: 'documentation' })));
    assert.equal(new Set(published.access_links.map((l: any) => l.url)).size, published.access_links.length);
  }
});
