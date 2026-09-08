/** Link reachability only: an HTTP response does not establish task success. */
export type LinkClass = 'ok' | 'inconclusive' | 'broken';

export function classifyStatus(status: number): LinkClass {
  if (status >= 200 && status < 400) return 'ok';
  // Other client errors can mean a protocol, method, auth or negotiation mismatch.
  if (status === 404 || status === 410 || status >= 500) return 'broken';
  return 'inconclusive';
}

export async function probeUrl(url: string, options: { mcp?: boolean; timeoutMs?: number } = {}) {
  const accept = options.mcp ? 'application/json, text/event-stream' : '*/*';
  async function request(method: 'HEAD' | 'GET'): Promise<{ status: number; method: string } | { error: string }> {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), options.timeoutMs ?? 15_000);
    try {
      const response = await fetch(url, {
        method, redirect: 'follow', signal: controller.signal,
        headers: { 'user-agent': 'agent-friendly-services-probe/0.1 (link health check; non-commercial index)', accept },
      });
      // SSE can remain open indefinitely. Headers suffice; do not consume the stream.
      try { await response.body?.cancel(); } catch { /* ignore cancellation errors */ }
      return { status: response.status, method };
    } catch (error) {
      return { error: error instanceof Error ? (error.cause as Error | undefined)?.message ?? error.message : String(error) };
    } finally { clearTimeout(timer); }
  }
  let response = await request('HEAD');
  if ('error' in response || response.status >= 300) {
    const get = await request('GET');
    if (!('error' in get)) response = get;
    else if ('error' in response) response = await request('GET');
  }
  if ('error' in response) return { class: 'broken' as const, status: null, detail: response.error, accept };
  return { class: classifyStatus(response.status), status: response.status, method: response.method, accept };
}
