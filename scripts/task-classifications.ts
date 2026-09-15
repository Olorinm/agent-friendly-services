import fs from 'node:fs';
import path from 'node:path';
import { ROOT, loadYamlFile, loadCategories, type Category } from './lib.ts';
import { flattenCategories } from './taxonomy.mjs';

export interface TaskClassification {
  file: string;
  id: string;
  classification: string;
  phase: 'setup' | 'business';
}

export function loadTaskClassifications(root = ROOT): TaskClassification[] {
  const file = path.join(root, 'data/experiments/task-classifications.yaml');
  return fs.existsSync(file) ? loadYamlFile<{ tasks: TaskClassification[] }>(file).tasks : [];
}

const registered = loadTaskClassifications();

/** Display metadata is separate from immutable task prompts and hashes. */
export function taskClassification(task: { file: string; id: string }): Pick<TaskClassification, 'classification' | 'phase'> {
  const entry = registered.find(row => row.file === task.file && row.id === task.id);
  return entry ? { classification: entry.classification, phase: entry.phase }
    : { classification: 'unclassified', phase: 'business' };
}

export function taskClassificationErrors(entries = loadTaskClassifications(), categories: Category[] = loadCategories(), root = ROOT): string[] {
  const errors: string[] = [], seen = new Set<string>();
  const paths = new Set(flattenCategories(categories).map(node => node.path));
  if (!Array.isArray(entries)) return ['Task classifications must be an array'];
  for (const entry of entries) {
    if (!entry || typeof entry.file !== 'string' || typeof entry.id !== 'string' || typeof entry.classification !== 'string') {
      errors.push('Malformed task classification entry');
      continue;
    }
    const key = `${entry.file}#${entry.id}`;
    if (seen.has(key)) errors.push(`Duplicate task classification: ${key}`);
    seen.add(key);
    if (!paths.has(entry.classification)) errors.push(`Unknown task classification: ${entry.classification}`);
    if (!['setup', 'business'].includes(entry.phase)) errors.push(`Invalid task phase: ${key}`);
    const file = path.resolve(root, entry.file);
    if (!file.startsWith(path.resolve(root, 'data/experiments/tasks') + path.sep) || !fs.existsSync(file)) {
      errors.push(`Missing or unsafe task file: ${entry.file}`);
      continue;
    }
    const ids = fs.readFileSync(file, 'utf8').split('\n').filter(line => /^\| [a-z][a-z0-9-]+ \| v[0-9]/.test(line))
      .map(line => line.split('|')[1].trim());
    if (!ids.includes(entry.id)) errors.push(`Task classification refers to missing task: ${key}`);
  }
  const dir = path.join(root, 'data/experiments/tasks');
  for (const name of fs.readdirSync(dir).filter(name => name.endsWith('.md'))) {
    const file = `data/experiments/tasks/${name}`;
    for (const row of fs.readFileSync(path.join(root, file), 'utf8').split('\n')) {
      if (/^\| [a-z][a-z0-9-]+ \| v[0-9]/.test(row)) {
        const key = `${file}#${row.split('|')[1].trim()}`;
        if (!seen.has(key)) errors.push(`Task lacks display classification: ${key}`);
      }
    }
  }
  return errors;
}
