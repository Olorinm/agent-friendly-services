/**
 * Validates all provider files against the schema and the project rules.
 * Errors are written for humans AND agents: every error says what is wrong
 * and how to fix it. Exit code 1 if anything fails.
 */
import fs from 'node:fs';
import path from 'node:path';
import Ajv from 'ajv';
import { ROOT, loadFields, loadCategories, loadProviders, loadCandidates } from './lib.ts';

const errors: Map<string, string[]> = new Map();

function fail(file: string, message: string) {
  if (!errors.has(file)) errors.set(file, []);
  errors.get(file)!.push(message);
}

// ---------------------------------------------------------------------------
// Repo-level consistency: schema and fields.yaml must define the same fields.
// ---------------------------------------------------------------------------
const fields = loadFields();
const categories = loadCategories();
const schema = JSON.parse(fs.readFileSync(path.join(ROOT, 'schema', 'provider.schema.json'), 'utf8'));

const schemaEntrypoints = Object.keys(schema.properties.entrypoints.properties).sort();
const fieldEntrypoints = Object.keys(fields.entrypoints).sort();
const schemaChecks = Object.keys(schema.properties.checks.properties).sort();
const fieldChecks = Object.keys(fields.checks).sort();

if (JSON.stringify(schemaEntrypoints) !== JSON.stringify(fieldEntrypoints)) {
  fail('schema/provider.schema.json', `entrypoint fields drifted from data/fields.yaml.\n    schema: ${schemaEntrypoints.join(', ')}\n    fields: ${fieldEntrypoints.join(', ')}\n    Fix: keep both files in sync (fields.yaml is the source of truth).`);
}
if (JSON.stringify(schemaChecks) !== JSON.stringify(fieldChecks)) {
  fail('schema/provider.schema.json', `check fields drifted from data/fields.yaml.\n    schema: ${schemaChecks.join(', ')}\n    fields: ${fieldChecks.join(', ')}\n    Fix: keep both files in sync (fields.yaml is the source of truth).`);
}

const categoryIds = new Set(categories.map((c) => c.id));

// ---------------------------------------------------------------------------
// Provider files
// ---------------------------------------------------------------------------
const ajv = new Ajv({ allErrors: true });
const validateSchema = ajv.compile(schema);

// Candidate-pool files (data/candidates/) follow the exact same schema and
// rules — what makes them candidates is only that nobody has verified the
// claims yet (docs/candidate-pool.md). Ids must be unique across both pools.
const providers = loadProviders();
const candidates = loadCandidates();
const seenIds = new Map<string, string>();
const today = new Date().toISOString().slice(0, 10);

for (const { relFile, raw, data } of [...providers, ...candidates]) {
  // --- raw-text lint: YAML traps -------------------------------------------
  for (const [lineNo, line] of raw.split('\n').entries()) {
    const bareBool = line.match(/^\s*(status|archived)\s*:\s*(yes|no|on|off|Yes|No|True|False)\s*(#.*)?$/);
    if (bareBool && bareBool[1] === 'status') {
      fail(relFile, `line ${lineNo + 1}: status is "${bareBool[2]}", which is not a valid status and is a YAML 1.1 boolean trap.\n    Fix: use one of supported | partial | unsupported | unknown | not_applicable.`);
    }
    const bareDate = line.match(/^\s*verified\s*:\s*(\d{4}-\d{2}-\d{2})\s*(#.*)?$/);
    if (bareDate) {
      fail(relFile, `line ${lineNo + 1}: verified date must be a quoted string so every YAML parser reads it as text.\n    Fix: verified: "${bareDate[1]}"`);
    }
  }

  // --- JSON schema ----------------------------------------------------------
  if (!validateSchema(data)) {
    for (const err of validateSchema.errors ?? []) {
      const where = err.instancePath.replaceAll('/', '.').replace(/^\./, '') || '(root)';
      let msg = `${where} ${err.message}`;
      if (err.keyword === 'enum' && where.endsWith('.status')) {
        msg += `.\n    Allowed: supported | partial | unsupported | unknown | not_applicable (never bare yes/no).`;
      } else if (err.keyword === 'pattern' && String(err.schema).startsWith('^https://')) {
        msg += `.\n    Fix: use a full https:// URL.`;
      } else if (err.keyword === 'additionalProperties') {
        msg += ` ("${(err.params as { additionalProperty: string }).additionalProperty}").\n    Fix: only fields defined in data/fields.yaml are allowed.`;
      }
      fail(relFile, msg);
    }
  }

  if (!data || typeof data !== 'object') continue;

  // --- id and category ------------------------------------------------------
  const expectedId = path.basename(relFile, '.yaml');
  if (data.id && data.id !== expectedId) {
    fail(relFile, `id is "${data.id}" but the filename says "${expectedId}".\n    Fix: rename the file or change the id — they must match.`);
  }
  if (data.id) {
    const dup = seenIds.get(data.id);
    if (dup) fail(relFile, `id "${data.id}" is already used by ${dup}.`);
    seenIds.set(data.id, relFile);
  }
  if (data.category && !categoryIds.has(data.category)) {
    fail(relFile, `category "${data.category}" is not in data/categories.yaml.\n    Fix: use one of ${[...categoryIds].join(', ')} — or propose a new category in an issue first.`);
  }

  // --- check-level rules ----------------------------------------------------
  for (const [checkId, check] of Object.entries(data.checks ?? {})) {
    if (!check || typeof check !== 'object') continue;
    const where = `checks.${checkId}`;
    if ((check.status === 'supported' || check.status === 'partial') && !check.evidence) {
      fail(relFile, `${where}.status is "${check.status}" but evidence is missing.\n    Fix: add ${where}.evidence (an official URL), or change status to "unknown".`);
    }
    if ((check.status === 'partial' || check.status === 'not_applicable') && !check.notes) {
      fail(relFile, `${where}.status is "${check.status}" but notes are missing.\n    Fix: add ${where}.notes explaining the limitation (partial) or why the check does not apply (not_applicable).`);
    }
    if (check.verified && check.verified > today) {
      fail(relFile, `${where}.verified is "${check.verified}", which is in the future.\n    Fix: use the date you actually verified it.`);
    }
    if ((check.status === 'supported' || check.status === 'partial' || check.status === 'unsupported') && !check.verified) {
      fail(relFile, `${where}.status is "${check.status}" but has no verified date.\n    Fix: add ${where}.verified: "YYYY-MM-DD" (the date you checked the evidence).`);
    }
  }

  if (data.archived && !data.archived_reason) {
    fail(relFile, `archived is true but archived_reason is missing.\n    Fix: add a short archived_reason.`);
  }
}

// ---------------------------------------------------------------------------
// Report
// ---------------------------------------------------------------------------
if (errors.size > 0) {
  let count = 0;
  for (const [file, msgs] of errors) {
    console.error(`\n${file}`);
    for (const msg of msgs) {
      console.error(`  ${msg}`);
      count++;
    }
  }
  console.error(`\n✗ ${count} error(s) in ${errors.size} file(s).`);
  process.exit(1);
} else {
  const nChecks = [...providers, ...candidates].reduce((n, p) => n + Object.keys(p.data.checks ?? {}).length, 0);
  const cand = candidates.length ? ` + ${candidates.length} candidate(s)` : '';
  console.log(`✓ ${providers.length} providers${cand}, ${nChecks} checks, 0 errors.`);
}
