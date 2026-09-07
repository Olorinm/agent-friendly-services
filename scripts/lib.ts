import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { load as yamlLoad } from 'js-yaml';

export const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const PROVIDERS_DIR = path.join(ROOT, 'data', 'providers');
export const CANDIDATES_DIR = path.join(ROOT, 'data', 'candidates');
export const GENERATED_DIR = path.join(ROOT, 'generated');

export interface Check {
  status: 'supported' | 'partial' | 'unsupported' | 'unknown' | 'not_applicable';
  evidence?: string;
  verified?: string;
  notes?: string;
}

export interface Provider {
  id: string;
  name: string;
  category: string;
  homepage: string;
  summary: string;
  submitted_by: 'community' | 'vendor';
  tags?: string[];
  scope?: string;
  aliases?: string[];
  archived?: boolean;
  archived_reason?: string;
  entrypoints: Record<string, string | string[]>;
  checks: Record<string, Check>;
  notes?: string[];
  catalog?: Catalog;
}

/** All catalog facts are source claims. They never imply a successful task run. */
export interface Fact {
  value: string;
  evidence?: string[];
  notes?: string;
}
export interface AccessRoute {
  id: string;
  interface: 'api' | 'sdk' | 'cli' | 'mcp' | 'web' | 'mobile';
  maintainer: 'official' | 'third_party' | 'unknown';
  entry_url: string;
  docs?: string;
  evidence: string[];
  upstream?: string;
  via?: string;
  notes?: string;
  availability?: Fact;
  personal_access?: Fact;
  auth?: Fact;
  data_kind?: Fact;
  capabilities?: Record<string, Fact>;
  requirements?: Record<string, Fact>;
  human_steps?: { step: string; stage: string; evidence: string[]; notes?: string }[];
  costs?: { kind: string; amount: number; unit: string; currency?: string; per: string; scope: string; evidence: string[] }[];
}
export interface Catalog {
  version: 1;
  classifications: string[];
  sources: Record<string, { url: string; checked_on: string; kind: string; notes?: string }>;
  routes: AccessRoute[];
  notes?: string[];
}

export interface FieldDef {
  name: string;
  description: string;
  verification: 'probe' | 'registry' | 'manual';
}

export interface Fields {
  entrypoints: Record<string, FieldDef>;
  checks: Record<string, FieldDef>;
}

export interface Category {
  id: string;
  name: string;
  description: string;
  subcategories?: { id: string; name: string; description: string; capabilities: { id: string; description: string }[] }[];
}

export function loadYamlFile<T = unknown>(file: string): T {
  return yamlLoad(fs.readFileSync(file, 'utf8')) as T;
}

export function loadFields(): Fields {
  return loadYamlFile<Fields>(path.join(ROOT, 'data', 'fields.yaml'));
}

export function loadCategories(): Category[] {
  return loadYamlFile<{ categories: Category[] }>(path.join(ROOT, 'data', 'categories.yaml')).categories;
}

function yamlFiles(dir: string): string[] {
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => f.endsWith('.yaml'))
    .sort()
    .map((f) => path.join(dir, f));
}

export function providerFiles(): string[] {
  return yamlFiles(PROVIDERS_DIR);
}

export interface LoadedProvider {
  file: string;
  relFile: string;
  raw: string;
  data: Provider;
}

function loadDir(dir: string): LoadedProvider[] {
  return yamlFiles(dir).map((file) => {
    const raw = fs.readFileSync(file, 'utf8');
    const parsed = yamlLoad(raw) as Provider;
    return {
      file,
      relFile: path.relative(ROOT, file),
      raw,
      data: parsed && typeof parsed === 'object'
        ? { ...parsed,
          entrypoints: parsed.entrypoints === undefined ? {} : parsed.entrypoints,
          checks: parsed.checks === undefined ? {} : parsed.checks,
        } : parsed,
    };
  });
}

export function loadProviders(): LoadedProvider[] {
  return loadDir(PROVIDERS_DIR);
}

/** Candidate identity and source claims; directory membership is not a test result. */
export function loadCandidates(): LoadedProvider[] {
  return loadDir(CANDIDATES_DIR);
}

/** All URLs found in a provider file, tagged with where they came from. */
export function providerUrls(p: Provider): { url: string; source: string }[] {
  const urls: { url: string; source: string }[] = [];
  for (const [key, value] of Object.entries(p.entrypoints ?? {})) {
    if (typeof value === 'string') urls.push({ url: value, source: `entrypoints.${key}` });
    else if (Array.isArray(value)) value.forEach((u, i) => urls.push({ url: u, source: `entrypoints.${key}[${i}]` }));
  }
  for (const [key, check] of Object.entries(p.checks ?? {})) {
    if (check?.evidence) urls.push({ url: check.evidence, source: `checks.${key}.evidence` });
  }
  if (p.homepage) urls.push({ url: p.homepage, source: 'homepage' });
  for (const [id, source] of Object.entries(p.catalog?.sources ?? {})) {
    urls.push({ url: source.url, source: `catalog.sources.${id}.url` });
  }
  for (const route of p.catalog?.routes ?? []) {
    // entry_url can be a protocol endpoint: an HTTP probe is not a functional test.
    urls.push({ url: route.entry_url, source: `catalog.routes.${route.id}.entry_url` });
    if (route.docs) urls.push({ url: route.docs, source: `catalog.routes.${route.id}.docs` });
  }
  return urls;
}

export function daysSince(dateStr: string): number {
  const then = new Date(`${dateStr}T00:00:00Z`).getTime();
  return Math.floor((Date.now() - then) / 86_400_000);
}
