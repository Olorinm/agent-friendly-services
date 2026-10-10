import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { ROOT, loadCandidates, loadProviders } from '../scripts/lib.ts';
import { loadEvaluations, generateEvaluations } from '../scripts/evaluations.ts';
import { loadResultNotes } from '../scripts/result-notes.ts';
import { buildBoards } from '../scripts/leaderboard.ts';
import { renderServiceResults } from '../scripts/service-results.ts';
import { catalogService } from '../scripts/catalog.ts';
import { searchServices } from '../mcp/catalog.mjs';

test('added context reaches readers and MCP without replacing the recorded verdict or metrics', () => {
  const records = loadEvaluations();
  const before = JSON.stringify(records);
  const notes = loadResultNotes();
  const id = 'capitol-access-oc11835-r1';
  const run = records.find(r => r.run_id === id)!;
  const provider = [...loadProviders(), ...loadCandidates()].find(p => p.data.id === run.service_id)!.data;
  const runs = records.filter(r => r.service_id === provider.id);
  const text = renderServiceResults(provider, buildBoards(runs), runs);
  const position = text.indexOf(notes[id].en);
  assert(position >= 0 && position < text.indexOf('<summary>Task, conditions and evidence</summary>', position));
  const results = searchServices({ services: [catalogService(provider, 'candidate', runs)] }, {});
  const visible = results[0].routes.flatMap(r => r.task_runs).find(r => r.run_id === id);
  assert.equal(visible.status, 'not_completed');
  assert.equal(visible.additional_context.zh, notes[id].zh);
  const temp = fs.mkdtempSync(path.join(os.tmpdir(), 'afs-result-notes-'));
  try {
    generateEvaluations(records, temp);
    const output = JSON.parse(fs.readFileSync(path.join(temp, 'generated/evaluations.json'), 'utf8'));
    assert.deepEqual(output.result_notes, notes);
    assert.equal(output.evaluations.find(r => r.run_id === id).status, run.status);
    assert(!('additional_context' in output.evaluations.find(r => r.run_id === id)));
    assert(fs.readFileSync(path.join(temp, 'generated/evaluations.md'), 'utf8').includes(notes[id].zh));
    assert.equal(JSON.stringify(records), before);
  } finally { fs.rmSync(temp, { recursive: true, force: true }); }
});

test('context cannot silently attach to a changed original record', () => {
  const id = 'capitol-access-oc11835-r1';
  const temp = fs.mkdtempSync(path.join(os.tmpdir(), 'afs-result-notes-binding-'));
  const dir = path.join(temp, 'data/experiments');
  try {
    fs.mkdirSync(path.join(dir, 'evaluations'), { recursive: true });
    const record = path.join(dir, 'evaluations', id + '.json');
    fs.copyFileSync(path.join(ROOT, 'data/experiments/evaluations', id + '.json'), record);
    fs.writeFileSync(path.join(dir, 'result-notes.json'), JSON.stringify({ schema_version: 1, notes: { [id]: loadResultNotes()[id] } }));
    assert.equal(Object.keys(loadResultNotes(temp)).length, 1);
    fs.appendFileSync(record, '\n');
    assert.throws(() => loadResultNotes(temp), /does not match original record/);
  } finally { fs.rmSync(temp, { recursive: true, force: true }); }
});
