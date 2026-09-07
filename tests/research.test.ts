import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { test } from 'node:test';
import { ROOT, loadCategories } from '../scripts/lib.ts';
import { generateResearch, initializeResearch, loadResearch, researchIssues, researchSummary, type Research } from '../scripts/research.ts';

const categories = loadCategories();
const today = '2026-09-07';
// Research evolves with evidence; provenance behavior must not freeze the live pilot.
const pilot = () => JSON.parse(fs.readFileSync(new URL('./fixtures/research-hypotheses.json', import.meta.url), 'utf8')) as Research;
const errors = (p: unknown) => researchIssues(p, 'travel/flights', categories, today);
function reported(): Research {
  const p = pilot();
  p.sources.user = {
    url: 'https://example.com/original-request', kind: 'public_user_report', checked_on: today,
    origin_group: 'original-request', summary: 'Synthetic test fixture: a user asks for help choosing a flight.',
  };
  p.needs[0].basis = 'reported';
  p.needs[0].evidence = ['user'];
  return p;
}

test('unsourced discussion examples remain hypotheses, not observed demand', () => {
  const p = pilot();
  assert.deepEqual(errors(p), []);
  assert.equal(researchSummary(p).needs.reported, 0);
  assert.equal(researchSummary(p).needs.hypothesis, 3);
  assert(p.scenarios.every(s => s.status === 'candidate'));
  assert.equal(p.search_log.length, 0); // No fabricated retrospective search history.
});

test('tools flag provider documentation labeled as user-reported demand', () => {
  const p = pilot();
  p.needs[0].basis = 'reported';
  p.needs[0].evidence = ['kiwi-mcp-docs'];
  assert.match(errors(p).join('\n'), /public_user_report/);
  p.needs[0].basis = 'inferred';
  assert.deepEqual(errors(p), []);
  p.needs[0].evidence = [];
  assert.match(errors(p).join('\n'), /requires evidence/);
});

test('supported needs remain in scope when a test is blocked, with no popularity quota', () => {
  const p = reported();
  p.scenarios[0].status = 'retained';
  p.scenarios[0].testability = 'blocked';
  p.scenarios[0].testability_notes = 'Current tools cannot independently verify the desired result.';
  assert.deepEqual(errors(p), []); // One original report suffices to record a real need.
  p.needs[0].basis = 'hypothesis';
  assert.match(errors(p).join('\n'), /keep as candidate/);
});

test('tools flag broken links between evidence, needs, scenarios and capabilities', () => {
  const p = pilot();
  p.needs[0].evidence = ['missing-source'];
  p.needs[0].conflicts_with = ['missing-need'];
  p.scenarios[0].need_ids = ['missing-need'];
  p.capability_candidates[0].catalog_id = 'hotels.book';
  const result = errors(p).join('\n');
  assert.match(result, /missing-source/);
  assert.match(result, /missing-need/);
  assert.match(result, /not defined for this classification/);
  p.needs.push(structuredClone(p.needs[0]));
  assert.match(errors(p).join('\n'), /duplicate id/);
});

test('dates, file identity and claimed source independence are checked', () => {
  const p = pilot();
  p.sources.copy = { ...p.sources['kiwi-mcp-docs'], origin_group: 'different-group' };
  assert.match(errors(p).join('\n'), /same source URL/);
  p.sources.copy.origin_group = 'kiwi-mcp-guide';
  assert.equal(researchSummary(p).source_groups, 1);
  assert.deepEqual(errors(p), []);
  p.sources.copy.checked_on = '2026-02-30';
  p.search_log.push({ searched_on: '2026-09-08', query: 'example query', channel: 'web', source_ids: ['missing'], notes: 'Test only.' });
  p.classification = 'travel/hotels';
  const result = errors(p).join('\n');
  assert.match(result, /real, non-future date/);
  assert.match(result, /classification must match/);
});

test('scenario capability links remain optional, flag missing targets and survive generation', () => {
  const p = pilot();
  assert.deepEqual(errors(p), []); // Existing briefs need no new fields.
  p.scenarios[0].capability_ids = ['search-offers', 'missing-capability'];
  assert.match(errors(p).join('\n'), /capability_ids references missing id: missing-capability/);
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'afs-capability-links-'));
  try {
    fs.mkdirSync(path.join(root, 'data/research/travel'), { recursive: true });
    const source = path.join(root, 'data/research/travel/flights.yaml');
    fs.writeFileSync(source, JSON.stringify(p));
    generateResearch(root, categories, root);
    assert(fs.readFileSync(path.join(root, 'generated/research.md'), 'utf8').includes('missing-capability（待关联）'));
    p.scenarios[0].capability_ids = ['search-offers'];
    assert.deepEqual(errors(p), []);
    fs.writeFileSync(source, JSON.stringify(p));
    generateResearch(root, categories, root);
    const result = JSON.parse(fs.readFileSync(path.join(root, 'generated/research.json'), 'utf8')).research[0];
    assert.deepEqual(result.scenarios[0].capability_ids, ['search-offers']);
    assert.equal(result.scenarios[0].status, 'candidate');
    assert.equal(result.scenarios[0].testability, 'unknown');
    assert(fs.readFileSync(path.join(root, 'generated/research.md'), 'utf8').includes(p.capability_candidates[0].outcome));
  } finally { fs.rmSync(root, { recursive: true, force: true }); }
});

test('the same template starts hotel and email research without flight assumptions or overwrites', () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'afs-research-init-'));
  try {
    const otherCategories = structuredClone(categories);
    otherCategories.find(c => c.id === 'communication')!.subcategories = [{ id: 'email', name: 'Email', description: 'Test classification', capabilities: [] }];
    for (const classification of ['travel/hotels', 'communication/email']) {
      const file = initializeResearch(classification, root, otherCategories);
      const content = fs.readFileSync(file, 'utf8');
      assert(!content.includes('flights'));
      assert.throws(() => initializeResearch(classification, root, otherCategories), /EEXIST/);
      assert.equal(fs.readFileSync(file, 'utf8'), content);
    }
    for (const pack of loadResearch(root)) assert.deepEqual(researchIssues(pack.data, pack.classification, otherCategories, today), []);
    initializeResearch('learning/languages', root); // Exploration may precede the category dictionary.
    assert(loadResearch(root).some(p => p.classification === 'learning/languages'));
    assert.throws(() => initializeResearch('../../escape', root), /safe category/);
    const invalid = path.join(root, 'data/research/travel/invalid.yaml');
    fs.writeFileSync(invalid, 'version: [broken');
    assert(loadResearch(root).find(p => p.classification === 'travel/invalid')!.parseError);
  } finally { fs.rmSync(root, { recursive: true, force: true }); }
});

test('new formats, unresolved references and malformed drafts remain visible without blocking generation', () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'afs-research-evolve-'));
  try {
    const file = initializeResearch('travel/hotels', root);
    fs.writeFileSync(file, 'version: 2\nnew_expression: Keep this evolving research.\n');
    const draft = path.join(root, 'data/research/travel/draft.yaml');
    fs.writeFileSync(draft, 'unfinished: [');
    const p = pilot();
    p.needs[0].evidence = ['not-linked-yet'];
    // JSON is valid YAML and lets this fixture focus on preservation semantics.
    fs.writeFileSync(path.join(root, 'data/research/travel/flights.yaml'), JSON.stringify(p));
    generateResearch(root, categories, root);
    const result = JSON.parse(fs.readFileSync(path.join(root, 'generated/research.json'), 'utf8'));
    const hotels = result.research.find((r: any) => r.classification === 'travel/hotels');
    assert.equal(hotels.raw.new_expression, 'Keep this evolving research.');
    assert(hotels.diagnostics.length > 0);
    assert.equal(result.research.find((r: any) => r.classification === 'travel/draft').raw_text, 'unfinished: [');
    assert.equal(result.research.find((r: any) => r.classification === 'travel/flights').needs[0].evidence[0], 'not-linked-yet');
    assert(fs.readFileSync(path.join(root, 'generated/research.md'), 'utf8').includes('待关联'));
  } finally { fs.rmSync(root, { recursive: true, force: true }); }
});

test('full generation publishes the current research without changing its evidence or scenario status', () => {
  const output = fs.mkdtempSync(path.join(os.tmpdir(), 'afs-research-build-'));
  try {
    execFileSync(process.execPath, ['--import', 'tsx', 'scripts/generate.ts'], { cwd: ROOT, env: { ...process.env, AFS_OUTPUT_DIR: output }, stdio: 'pipe' });
    const data = JSON.parse(fs.readFileSync(path.join(output, 'generated/research.json'), 'utf8'));
    assert.match(data.notice, /not a benchmark/);
    const p = data.research.find((r: Research) => r.classification === 'travel/flights');
    const source = loadResearch().find(r => r.classification === 'travel/flights')!.data as Research;
    assert.deepEqual(p.summary, researchSummary(source));
    assert.deepEqual(p.sources, source.sources);
    assert.deepEqual(p.needs, source.needs);
    assert.deepEqual(p.scenarios, source.scenarios);
    assert.deepEqual(p.search_log, source.search_log);
    assert(fs.readFileSync(path.join(output, 'generated/research.md'), 'utf8').includes(source.title));
    assert(fs.readFileSync(path.join(output, 'README.zh-CN.md'), 'utf8').includes('./docs/flights.zh-CN.md'));
  } finally { fs.rmSync(output, { recursive: true, force: true }); }
});

test('survey evidence and reading metadata survive generation without becoming individual reports', () => {
  const p = pilot();
  p.sources.survey = {
    url: 'https://example.com/survey', kind: 'survey_report', checked_on: today,
    origin_group: 'survey-2025', summary: 'Synthetic aggregate finding.',
    title: 'Synthetic survey', published_on: '2025-11-05', language: 'en',
    locator: 'Methods and aggregate results', access: 'page_text',
    limitations: 'Aggregate preferences do not measure task frequency.',
  };
  p.needs[0].evidence = ['survey'];
  p.needs[0].basis = 'inferred';
  assert.deepEqual(errors(p), []);
  p.needs[0].basis = 'reported';
  assert.match(errors(p).join('\n'), /public_user_report/);
  p.needs[0].basis = 'inferred';
  p.sources.survey.published_on = '2026-09-08';
  assert.match(errors(p).join('\n'), /published_on/);
  p.sources.survey.published_on = '2025-11-05';
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'afs-survey-view-'));
  try {
    fs.mkdirSync(path.join(root, 'data/research/travel'), { recursive: true });
    fs.writeFileSync(path.join(root, 'data/research/travel/flights.yaml'), JSON.stringify(p));
    generateResearch(root, categories, root);
    const result = JSON.parse(fs.readFileSync(path.join(root, 'generated/research.json'), 'utf8'));
    assert.deepEqual(result.research[0].sources.survey, p.sources.survey);
    assert.equal(result.research[0].summary.needs.reported, 0);
  } finally { fs.rmSync(root, { recursive: true, force: true }); }
});
