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
    return {
      file,
      relFile: path.relative(ROOT, file),
      raw,
      data: yamlLoad(raw) as Provider,
    };
  });
}

export function loadProviders(): LoadedProvider[] {
  return loadDir(PROVIDERS_DIR);
}

/** Candidate-pool entries (data/candidates/): same schema as providers, but
 *  unverified — nobody has reviewed the evidence and no agent run has passed.
 *  See docs/candidate-pool.md for entry/promotion rules. */
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
  return urls;
}

export function daysSince(dateStr: string): number {
  const then = new Date(`${dateStr}T00:00:00Z`).getTime();
  return Math.floor((Date.now() - then) / 86_400_000);
}
