// One exploratory search per configured airport. Run again only for an explicit
// verification attempt; these calls are not independent Agent benchmark runs.
// Usage: node scripts/flights-smoke.mjs
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import * as yaml from 'js-yaml';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const taskFile = 'data/experiments/tasks/travel-flights.yaml';
const taskText = fs.readFileSync(path.join(root, taskFile), 'utf8');
const task = yaml.load(taskText);
const input = task.inputs;
if (input.cabin !== 'economy' || input.max_stops !== 0 ||
    ![input.departure_local.from, input.departure_local.until, input.arrival_local_before]
      .every(t => /^\d{2}:00$/.test(t))) {
  throw new Error('This pilot adapter handles economy nonstop and whole-hour filters only.');
}
if (input.departure_date <= new Date().toISOString().slice(0, 10)) {
  throw new Error('Task date has expired. Create a new task version before querying.');
}
const batchDate = new Date().toISOString().slice(0, 10);
const dir = path.join(root, `data/experiments/results/travel-flights/${batchDate}-smoke`);
fs.mkdirSync(dir, { recursive: true });
const priorCalls = fs.readdirSync(dir).filter(f => f.endsWith('-kiwi.json')).reduce((total, file) => {
  const run = JSON.parse(fs.readFileSync(path.join(dir, file), 'utf8'));
  return total + (run.task_id === task.id ? run.calls.length : 0);
}, 0);
if (priorCalls + input.origin_airports.length > task.budget.max_search_calls_per_service) {
  throw new Error('Pilot search-call budget exhausted. Review existing evidence before further queries.');
}
const started = new Date();
const output = path.join(dir, `${started.toISOString().replaceAll(':', '-')}-kiwi.json`);
const record = {
  task_id: task.id, task_file: taskFile,
  task_sha256: crypto.createHash('sha256').update(taskText).digest('hex'),
  task,
  mode: task.mode, service: 'kiwi', route: 'search-mcp',
  endpoint: 'https://mcp.kiwi.com', started_at: started.toISOString(),
  environment: { os: os.platform(), arch: os.arch(), node: process.version,
    sdk: JSON.parse(fs.readFileSync(path.join(root, 'node_modules/@modelcontextprotocol/sdk/package.json'))).version,
    network_egress_region: 'unverified', isolation: 'current Codex session, no service credentials supplied' },
  cost: { service_cash_spent: 0, service_billing_verified: false, agent_usd: null,
    note: 'No account, key, payment method or paid model invocation; current session cost unmeasured.' },
  limitations: ['Point of sale cannot be pinned by the exposed tool schema.',
    'Transport and tool latency excludes research, coding, reasoning and environment repair time.'],
  calls: [], http: [],
};
const save = () => fs.writeFileSync(output, JSON.stringify(record, null, 2) + '\n');
const errorInfo = e => ({ name: e.name, message: e.message, cause: e.cause?.message, code: e.cause?.code });
const client = new Client({ name: 'afs-flight-smoke', version: '0.1.0' });
const transport = new StreamableHTTPClientTransport(new URL(record.endpoint), {
  fetch: async (url, init) => {
    const event = { method: init?.method ?? 'GET', started_at: new Date().toISOString() };
    const t = performance.now();
    record.http.push(event);
    try {
      const response = await fetch(url, { ...init,
        signal: AbortSignal.any([...(init?.signal ? [init.signal] : []), AbortSignal.timeout(60000)]) });
      event.status = response.status;
      return response;
    } catch (e) { event.error = errorInfo(e); throw e; }
    finally { event.headers_elapsed_ms = Math.round(performance.now() - t); }
  },
});
save();
try {
  const t = performance.now();
  await client.connect(transport, { timeout: 20000 });
  record.connection_ms = Math.round(performance.now() - t);
  record.server = client.getServerVersion();
  record.tools = await client.listTools(undefined, { timeout: 20000 });
  save();
  const [year, month, day] = input.departure_date.split('-');
  for (const airport of input.origin_airports) {
    const args = { flyFrom: airport, flyTo: input.destination_airport,
      departureDate: `${day}/${month}/${year}`, departureDateFlexDays: 0,
      adults: input.adults, children: input.children, infants: input.infants,
      cabinClass: 'M', currency: input.currency, locale: 'en', max_sector_stopovers: 0,
      dtime_from: Number(input.departure_local.from.slice(0, 2)),
      dtime_to: Number(input.departure_local.until.slice(0, 2)),
      atime_to: Number(input.arrival_local_before.slice(0, 2)), sort: 'price' };
    const call = { tool: 'search-flight', arguments: args, started_at: new Date().toISOString() };
    const t = performance.now();
    record.calls.push(call);
    try { call.response = await client.callTool({ name: call.tool, arguments: args }, undefined,
      { timeout: task.budget.per_call_timeout_seconds * 1000 }); }
    catch (e) { call.error = errorInfo(e); }
    call.elapsed_ms = Math.round(performance.now() - t);
    save();
    console.log(JSON.stringify({ airport, elapsed_ms: call.elapsed_ms, error: call.error,
      response: call.response?.structuredContent ?? call.response }, null, 2));
  }
} catch (e) { record.error = errorInfo(e); process.exitCode = 1; }
finally {
  await client.close();
  record.finished_at = new Date().toISOString();
  record.elapsed_ms = Date.now() - started.getTime();
  save();
  console.log(`Evidence: ${output}`);
}
