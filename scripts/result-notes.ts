import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { ROOT } from './lib.ts';

export interface ResultNote {
  record_sha256: string;
  added_at: string;
  zh: string;
  en: string;
}

/** Controller context is separate from the original external verdict and metrics. */
export function loadResultNotes(root = ROOT): Record<string, ResultNote> {
  const file = path.join(root, 'data/experiments/result-notes.json');
  if (!fs.existsSync(file)) return {};
  const value = JSON.parse(fs.readFileSync(file, 'utf8'));
  if (value.schema_version !== 1 || !value.notes || typeof value.notes !== 'object' || Array.isArray(value.notes))
    throw new Error('Invalid result-notes document');
  for (const [id, raw] of Object.entries(value.notes)) {
    const note = raw as ResultNote;
    if (!/^[a-zA-Z0-9._-]+$/.test(id) || !note || !(['zh', 'en'] as const).every(k => typeof note[k] === 'string' && note[k].trim())
        || !/^[a-f0-9]{64}$/.test(note.record_sha256 ?? '') || typeof note.added_at !== 'string'
        || !/(?:Z|[+-]\d{2}:\d{2})$/.test(note.added_at) || !Number.isFinite(Date.parse(note.added_at)))
      throw new Error('Invalid result note: ' + id);
    const record = path.join(root, 'data/experiments/evaluations', id + '.json');
    if (!fs.existsSync(record) || createHash('sha256').update(fs.readFileSync(record)).digest('hex') !== note.record_sha256)
      throw new Error('Result note does not match original record: ' + id);
  }
  return value.notes;
}

export function resultNotesFor(runs: { run_id: string }[], root = ROOT): Record<string, ResultNote> {
  if (!runs.length) return {};
  const ids = new Set(runs.map(r => r.run_id));
  return Object.fromEntries(Object.entries(loadResultNotes(root)).filter(([id]) => ids.has(id)));
}
