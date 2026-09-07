import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { execFileSync, spawnSync } from 'node:child_process';
import { test } from 'node:test';
import { ROOT, loadProviders, loadCandidates } from '../scripts/lib.ts';
import { evaluationErrors, loadEvaluations } from '../scripts/evaluations.ts';
import { catalogService } from '../scripts/catalog.ts';
import { searchServices } from '../mcp/catalog.mjs';

test('task selection and reviewed-result recorder reject contaminated or mislabeled input', () => {
  execFileSync('python3', ['tests/trials_test.py'], { cwd: ROOT, stdio: 'pipe' });
});

test('evaluation evidence tampering and cached-token double counting are detected', () => {
  const providers = [...loadProviders(), ...loadCandidates()].map(p => p.data);
  const records = loadEvaluations();
  assert(records.length >= 2);
  for (const record of records) {
    assert.deepEqual(evaluationErrors(record, providers), []);
    for (const item of record.evidence) {
      assert.equal(spawnSync('git', ['check-ignore', '--no-index', '-q', item.path], { cwd: ROOT }).status, 1,
        `Selected evidence must be available to a future checkout: ${item.path}`);
    }
  }
  const modified = structuredClone(records[0]);
  modified.evidence[0].sha256 = '0'.repeat(64);
  assert(evaluationErrors(modified, providers).some(s => s.includes('hash mismatch')));
  modified.usage!.cached_input_tokens = modified.usage!.input_tokens + 1;
  assert(evaluationErrors(modified, providers).some(s => s.includes('subset')));
  modified.review.checks[0].passed = false;
  assert(evaluationErrors(modified, providers).some(s => s.includes('passing checks')));
});

test('a public-playground pass never becomes a customer API or MCP pass', () => {
  const ignav = loadCandidates().find(p => p.data.id === 'ignav')!.data;
  const data = { services: [catalogService(ignav, 'candidate', loadEvaluations())] };
  const web = searchServices(data, { interface: 'web' })[0];
  assert.equal(web.route_tests, 'recorded');
  assert(web.routes.every((r: any) => r.task_runs.length > 0));
  for (const route of ['api', 'mcp']) {
    const service = searchServices(data, { interface: route })[0];
    assert.equal(service.route_tests, 'not_recorded');
    assert(service.routes.every((r: any) => r.task_runs.length === 0));
  }
});

test('public evaluation records and selected evidence omit local paths and Codex session IDs', () => {
  const privatePath = /(?:\/Users\/[^/\s]+|\/private\/var\/folders\/|\/private\/tmp\/afs-codex-)/;
  const sessionID = /"thread_id"\s*:\s*"[0-9a-f]{8}-[0-9a-f-]{27,}"/i;
  for (const record of loadEvaluations()) {
    assert(!/[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}/i.test(record.review.reviewer));
    const copies = [JSON.stringify(record), ...record.evidence.map(item => fs.readFileSync(path.join(ROOT, item.path), 'utf8'))];
    for (const text of copies) {
      assert(!text.includes(ROOT), `Repository path exposed in ${record.run_id}`);
      assert(!text.includes(os.homedir()), `Home path exposed in ${record.run_id}`);
      assert(!privatePath.test(text), `Local path exposed in ${record.run_id}`);
      assert(!sessionID.test(text), `Codex session ID exposed in ${record.run_id}`);
    }
  }
});
