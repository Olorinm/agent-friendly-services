import test from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';
import { once } from 'node:events';
import { classifyStatus, probeUrl } from '../scripts/link-probe.ts';

test('protocol and client errors are inconclusive; missing endpoints and server errors remain broken', () => {
  for (const status of [400, 401, 403, 405, 406, 407, 415, 422, 429]) assert.equal(classifyStatus(status), 'inconclusive');
  for (const status of [404, 410, 500, 502, 503]) assert.equal(classifyStatus(status), 'broken');
  for (const status of [200, 204, 301]) assert.equal(classifyStatus(status), 'ok');
});

test('MCP link probe negotiates SSE after rejected HEAD and cancels an open stream', async () => {
  const requests: string[] = [];
  const server = http.createServer((req, res) => {
    requests.push(`${req.method} ${req.headers.accept}`);
    if (req.method === 'HEAD') { res.writeHead(405).end(); return; }
    if (!req.headers.accept?.includes('text/event-stream')) { res.writeHead(406).end(); return; }
    res.writeHead(200, { 'content-type': 'text/event-stream' });
    res.write(': connected\n\n'); // Deliberately leave the connection open.
  });
  server.listen(0, '127.0.0.1');
  await once(server, 'listening');
  try {
    const url = `http://127.0.0.1:${(server.address() as any).port}/mcp`;
    assert.equal((await probeUrl(url, { timeoutMs: 1000 })).class, 'inconclusive');
    const result = await probeUrl(url, { mcp: true, timeoutMs: 1000 });
    assert.equal(result.status, 200);
    assert.equal(result.class, 'ok');
    assert.equal(result.method, 'GET');
    assert(requests.includes('GET application/json, text/event-stream'));
  } finally { server.closeAllConnections(); server.close(); }
});
