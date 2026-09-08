import fs from 'node:fs';
import path from 'node:path';
import { ROOT } from './lib.ts';
import type { Evaluation } from './evaluations.ts';

const translations = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/translations/tasks.en.json'), 'utf8'));
const fields = ['description', 'inputs', 'expected_output', 'success', 'failure'] as const;

/** Translate display text only; frozen prompts, hashes and comparison keys stay unchanged. */
export function taskDisplay(task: Evaluation['task'], zh: boolean): Evaluation['task'] {
  if (zh || !fields.some(key => /\p{Script=Han}/u.test(task[key] ?? ''))) return task;
  const translated = translations[`${task.id}/${task.version}`];
  if (!translated?.source_variants.some((source: Record<string, string>) => fields.every(key => source[key] === task[key]))) {
    throw new Error(`English display translation missing or stale: ${task.id}/${task.version}`);
  }
  return { ...task, ...Object.fromEntries(fields.map(key => [key, translated[key]])) };
}
