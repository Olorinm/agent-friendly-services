import fs from 'node:fs';
import path from 'node:path';
import { Ajv } from 'ajv';
import { dump, load } from 'js-yaml';
import { ROOT, loadCategories, type Category } from './lib.ts';
import { calendarDateValid } from './catalog.ts';

export interface Research {
  version: 1;
  classification: string;
  title: string;
  purpose: string;
  audience: string;
  scope: { include: string[]; exclude: string[] };
  sources: Record<string, {
    url: string; kind: 'public_user_report' | 'documented_workflow' | 'provider_docs' | 'industry_standard' | 'survey_report';
    checked_on: string; origin_group: string; summary: string; limitations?: string;
    title?: string; published_on?: string; language?: string; locator?: string;
    access?: 'page_text' | 'indexed_text';
  }>;
  search_log: { searched_on: string; query: string; channel: string; source_ids: string[]; notes: string }[];
  needs: {
    id: string; actor: string; trigger: string; outcome: string; constraints: string[];
    basis: 'reported' | 'inferred' | 'hypothesis'; evidence: string[]; reasoning: string;
    conflicts_with?: string[]; open_questions?: string[];
  }[];
  scenarios: {
    id: string; title: string; need_ids: string[]; request: string; assumptions: string[];
    capability_ids?: string[];
    variants?: string[]; status: 'candidate' | 'retained' | 'deferred'; reason: string;
    testability: 'unknown' | 'feasible' | 'blocked'; testability_notes?: string;
  }[];
  capability_candidates: {
    id: string; outcome: string; need_ids: string[]; evidence: string[]; reasoning: string; catalog_id?: string;
  }[];
  gaps: string[];
}

const ajv = new Ajv({ allErrors: true });
const validate = ajv.compile<Research>(JSON.parse(fs.readFileSync(path.join(ROOT, 'schema/research.schema.json'), 'utf8')));
const classifications = (categories: Category[]) => categories.flatMap(c => (c.subcategories ?? []).map(s => `${c.id}/${s.id}`));

/** Advisory checks for the current view, not admission rules for research. */
export function researchIssues(value: unknown, expectedClassification: string, categories: Category[], today: string): string[] {
  if (!validate(value)) return (validate.errors ?? []).map(e => `${e.instancePath || '(root)'} ${e.message}`);
  const data = value;
  const errors: string[] = [];
  if (data.classification !== expectedClassification) errors.push('classification must match data/research/<category>/<subcategory>.yaml.');
  if (!classifications(categories).includes(data.classification)) errors.push(`Unknown classification: ${data.classification}`);
  const checkRefs = (refs: string[], known: Set<string>, at: string) => {
    for (const ref of refs) if (!known.has(ref)) errors.push(`${at} references missing id: ${ref}`);
  };
  const ids = (rows: { id: string }[], at: string) => {
    const result = new Set<string>();
    for (const row of rows) {
      if (result.has(row.id)) errors.push(`${at}: duplicate id ${row.id}`);
      result.add(row.id);
    }
    return result;
  };
  const sourceIds = new Set(Object.keys(data.sources));
  const needIds = ids(data.needs, 'needs');
  ids(data.scenarios, 'scenarios');
  const capabilityIds = ids(data.capability_candidates, 'capability_candidates');
  const originalUrls = new Map<string, string>();
  for (const [id, source] of Object.entries(data.sources)) {
    if (!calendarDateValid(source.checked_on, today)) errors.push(`sources.${id}.checked_on must be a real, non-future date.`);
    if (source.published_on && !calendarDateValid(source.published_on, source.checked_on)) errors.push(`sources.${id}.published_on must be a real date no later than checked_on.`);
    try {
      const url = new URL(source.url);
      url.hash = '';
      const group = originalUrls.get(url.href);
      if (group && group !== source.origin_group) errors.push(`sources.${id}: the same source URL cannot count as different origin_groups.`);
      originalUrls.set(url.href, source.origin_group);
    } catch { errors.push(`sources.${id}.url must be a valid public URL.`); }
  }
  for (const [i, search] of data.search_log.entries()) {
    if (!calendarDateValid(search.searched_on, today)) errors.push(`search_log[${i}].searched_on must be a real, non-future date.`);
    checkRefs(search.source_ids, sourceIds, `search_log[${i}]`);
  }
  for (const need of data.needs) {
    checkRefs(need.evidence, sourceIds, `needs.${need.id}.evidence`);
    checkRefs(need.conflicts_with ?? [], needIds, `needs.${need.id}.conflicts_with`);
    if (need.conflicts_with?.includes(need.id)) errors.push(`needs.${need.id} cannot conflict with itself.`);
    if (need.basis !== 'hypothesis' && !need.evidence.length) errors.push(`needs.${need.id}: ${need.basis} requires evidence; use hypothesis for an unsourced idea.`);
    if (need.basis === 'reported' && !need.evidence.some(id => data.sources[id]?.kind === 'public_user_report')) {
      errors.push(`needs.${need.id}: reported requires a public_user_report; provider documentation cannot establish a reported user need.`);
    }
  }
  const needs = new Map(data.needs.map(n => [n.id, n]));
  for (const scenario of data.scenarios) {
    checkRefs(scenario.need_ids, needIds, `scenarios.${scenario.id}`);
    checkRefs(scenario.capability_ids ?? [], capabilityIds, `scenarios.${scenario.id}.capability_ids`);
    if (scenario.status === 'retained' && scenario.need_ids.some(id => needs.get(id)?.basis === 'hypothesis')) {
      errors.push(`scenarios.${scenario.id}: keep as candidate while linked needs are unsourced hypotheses.`);
    }
    // A sourced need may be retained even when its testability is blocked.
  }
  const [category, subcategory] = data.classification.split('/');
  const knownCapabilities = new Set(categories.find(c => c.id === category)?.subcategories?.find(s => s.id === subcategory)?.capabilities.map(c => c.id));
  for (const cap of data.capability_candidates) {
    checkRefs(cap.need_ids, needIds, `capability_candidates.${cap.id}.need_ids`);
    checkRefs(cap.evidence, sourceIds, `capability_candidates.${cap.id}.evidence`);
    if (cap.catalog_id && !knownCapabilities.has(cap.catalog_id)) errors.push(`capability_candidates.${cap.id}: catalog_id is not defined for this classification.`);
  }
  return errors;
}

export function loadResearch(root = ROOT) {
  const base = path.join(root, 'data/research');
  const files: string[] = [];
  function visit(dir: string) {
    if (!fs.existsSync(dir)) return;
    for (const entry of fs.readdirSync(dir, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
      const file = path.join(dir, entry.name);
      if (entry.isDirectory()) visit(file);
      else if (entry.isFile() && entry.name.endsWith('.yaml')) files.push(file);
    }
  }
  visit(base);
  return files.map(file => {
    const relFile = path.relative(root, file).split(path.sep).join('/');
    const classification = path.relative(base, file).slice(0, -5).split(path.sep).join('/');
    const raw = fs.readFileSync(file, 'utf8');
    try { return { relFile, classification, raw, data: load(raw), parseError: undefined }; }
    catch (error) { return { relFile, classification, raw, data: undefined, parseError: String(error) }; }
  });
}

export function initializeResearch(classification: string, destinationRoot = ROOT, categories = loadCategories()): string {
  if (!/^[a-z0-9][a-z0-9-]*\/[a-z0-9][a-z0-9-]*$/.test(classification)) throw new Error('Use a safe category/subcategory path; traversal and absolute paths are not supported.');
  if (!classifications(categories).includes(classification)) console.warn(`New research classification: ${classification}. The category dictionary can be updated as the research evolves.`);
  const draft = load(fs.readFileSync(path.join(ROOT, 'templates/research.yaml'), 'utf8')) as Research;
  draft.classification = classification;
  draft.title = `${classification} 用户需求与场景研究`;
  const file = path.join(destinationRoot, 'data/research', `${classification}.yaml`);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, '# Generated blank brief; no research has been performed.\n' + dump(draft, { lineWidth: 110 }), { flag: 'wx' });
  return file;
}

export function researchSummary(data: Research) {
  return {
    classification: data.classification,
    sources: Object.keys(data.sources).length,
    source_groups: new Set(Object.values(data.sources).map(s => s.origin_group)).size,
    needs: Object.fromEntries(['reported', 'inferred', 'hypothesis'].map(b => [b, data.needs.filter(n => n.basis === b).length])),
    scenarios: Object.fromEntries(['candidate', 'retained', 'deferred'].map(s => [s, data.scenarios.filter(n => n.status === s).length])),
    gaps: data.gaps.length,
  };
}

export function generateResearch(outputRoot: string, categories = loadCategories(), sourceRoot = ROOT) {
  const packs = loadResearch(sourceRoot).map(p => {
    const issues = p.parseError ? [p.parseError] : researchIssues(p.data, p.classification, categories, new Date().toISOString().slice(0, 10));
    if (!validate(p.data)) return {
      source_file: p.relFile, classification: p.classification, view: 'raw' as const,
      diagnostics: issues, raw: p.data ?? null, raw_text: p.raw,
    };
    return { source_file: p.relFile, ...p.data, view: 'structured' as const,
      diagnostics: issues, summary: researchSummary(p.data) };
  });
  const out = path.join(outputRoot, 'generated');
  fs.mkdirSync(out, { recursive: true });
  fs.writeFileSync(path.join(out, 'research.json'), JSON.stringify({
    schema_version: 1, generated_at: new Date().toISOString(),
    notice: 'Demand research, not a benchmark or usage-frequency estimate. Diagnostics are advisory. Unrecognized formats are retained as raw records; update the tools as research evolves. Mechanical checks do not verify source truth.',
    research: packs,
  }, null, 2) + '\n');
  const cell = (s: string) => s.replaceAll('|', '\\|').replaceAll('\n', ' ');
  const lines = ['<!-- GENERATED FILE — do not edit. -->', '# 用户需求与场景研究', '',
    '本页展示研究档案，不代表正式测试集或市场频率统计。reported 是公开用户表达，inferred 是资料推断，hypothesis 是待找证据的想法。来源组计数仅辅助去重。', '',
    '[维护说明](../docs/contributing.md#research-user-needs) · [完整数据](./research.json)', ''];
  for (const pack of packs) {
    if (pack.view === 'raw') {
      lines.push(`## ${pack.classification}`, '', `[研究原文](../${pack.source_file})`, '',
        '当前展示工具暂不识别此格式，原始内容已保存在 research.json。可根据研究需要迭代格式或工具。', '',
        ...pack.diagnostics.map(d => `- 提示：${d}`), '');
      continue;
    }
    lines.push(`## ${pack.classification}`, '', `[${pack.title}](../${pack.source_file})`, '', pack.purpose, '',
      `来源 ${pack.summary.sources}；公开表达 ${pack.summary.needs.reported}；推断 ${pack.summary.needs.inferred}；假设 ${pack.summary.needs.hypothesis}。`, '',
      '| 需求 | 用户与触发情境 | 希望得到的结果 | 依据类型 | 来源 |', '| --- | --- | --- | --- | --- |');
    for (const n of pack.needs) lines.push(`| ${n.id} | ${cell(`${n.actor}：${n.trigger}`)} | ${cell(n.outcome)} | ${n.basis} | ${n.evidence.map(id => pack.sources[id] ? `[${id}](${pack.sources[id].url})` : `${id}（待关联）`).join(', ') || '尚无'} |`);
    const capabilities = new Map(pack.capability_candidates.map(c => [c.id, c.outcome]));
    lines.push('', '| 场景 | 关联需求 | 所需基础能力 | 研究状态 | 测试可行性 | 原因 |', '| --- | --- | --- | --- | --- | --- |');
    for (const s of pack.scenarios) lines.push(`| ${cell(s.title)} | ${s.need_ids.join(', ')} | ${(s.capability_ids ?? []).map(id => cell(capabilities.get(id) ?? `${id}（待关联）`)).join('<br>') || '待拆解'} | ${s.status} | ${s.testability} | ${cell(s.reason)} |`);
    lines.push('', '待研究与覆盖缺口：', '', ...pack.gaps.map(g => `- ${g}`), '');
    if (pack.diagnostics.length) lines.push('工具提示（供复核，不阻止记录）：', '', ...pack.diagnostics.map(d => `- ${d}`), '');
  }
  fs.writeFileSync(path.join(out, 'research.md'), lines.join('\n').trimEnd() + '\n');
}
