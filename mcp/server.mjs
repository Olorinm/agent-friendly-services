#!/usr/bin/env node
// MCP server for the Agent-Friendly Services Index.
// Serves generated/providers.json — fetched live from GitHub raw (15-min cache)
// so it always reflects main; falls back to the local checkout copy when offline.
//
// Run:  npx -y github:Olorinm/agent-friendly-services
// Add:  claude mcp add agent-friendly-services -- npx -y github:Olorinm/agent-friendly-services

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';
import { searchServices } from './catalog.mjs';

const DATA_URL =
  process.env.AFS_DATA_URL ??
  'https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/providers.json';
const LOCAL_DATA = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  '..',
  'generated',
  'providers.json'
);
const CACHE_TTL_MS = 15 * 60 * 1000;
const CATALOG_URL = process.env.AFS_CATALOG_URL ??
  'https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/catalog.json';
const LOCAL_CATALOG = path.join(path.dirname(LOCAL_DATA), 'catalog.json');

let cache = null;
let cachedAt = 0;

async function loadData() {
  if (process.env.AFS_DATA_DIR) return JSON.parse(fs.readFileSync(path.join(process.env.AFS_DATA_DIR, 'providers.json'), 'utf8'));
  if (cache && Date.now() - cachedAt < CACHE_TTL_MS) return cache;
  try {
    const res = await fetch(DATA_URL, {
      headers: { 'user-agent': 'agent-friendly-services-mcp/0.1' },
      signal: AbortSignal.timeout(10_000),
    });
    if (!res.ok) throw new Error(`HTTP ${res.status} from ${DATA_URL}`);
    cache = await res.json();
    cachedAt = Date.now();
    return cache;
  } catch (err) {
    if (fs.existsSync(LOCAL_DATA)) {
      cache = JSON.parse(fs.readFileSync(LOCAL_DATA, 'utf8'));
      cachedAt = Date.now();
      return cache;
    }
    if (cache) return cache; // stale beats nothing
    throw err;
  }
}

let catalogCache = null;
let catalogCachedAt = 0;
async function loadCatalog() {
  if (process.env.AFS_DATA_DIR) return JSON.parse(fs.readFileSync(path.join(process.env.AFS_DATA_DIR, 'catalog.json'), 'utf8'));
  if (catalogCache && Date.now() - catalogCachedAt < CACHE_TTL_MS) return catalogCache;
  try {
    const res = await fetch(CATALOG_URL, { signal: AbortSignal.timeout(10_000) });
    if (!res.ok) throw new Error(`HTTP ${res.status} from ${CATALOG_URL}`);
    const data = await res.json();
    if (data.schema_version !== 1 || !Array.isArray(data.services)) throw new Error('Unsupported discovery catalog format');
    catalogCache = data;
    catalogCachedAt = Date.now();
    return data;
  } catch (err) {
    if (fs.existsSync(LOCAL_CATALOG)) {
      catalogCache = JSON.parse(fs.readFileSync(LOCAL_CATALOG, 'utf8'));
      catalogCachedAt = Date.now();
      return catalogCache;
    }
    if (catalogCache) return catalogCache;
    throw err;
  }
}

// Capability filters an agent can require. Entrypoint filters mean "a known
// official URL exists"; check filters mean the check is verified `supported`.
const REQUIREMENTS = {
  official_mcp: (p) => Boolean(p.entrypoints.mcp_official),
  llms_txt: (p) => Boolean(p.entrypoints.llms_txt),
  openapi: (p) => Boolean(p.entrypoints.openapi),
  graphql: (p) => Boolean(p.entrypoints.graphql),
  cli: (p) => Boolean(p.entrypoints.cli),
  agent_docs: (p) => Boolean(p.entrypoints.agent_docs),
  webhooks: (p) => Boolean(p.entrypoints.webhooks),
  sandbox: (p) => p.checks?.sandbox_or_test_mode?.status === 'supported',
  self_serve: (p) =>
    p.checks?.self_serve_signup?.status === 'supported' &&
    p.checks?.api_key_self_serve?.status === 'supported',
  free_tier: (p) => p.checks?.free_tier_or_trial?.status === 'supported',
  oauth: (p) => p.checks?.oauth_support?.status === 'supported',
  scoped_tokens: (p) => p.checks?.scoped_tokens?.status === 'supported',
  idempotency: (p) => p.checks?.idempotency?.status === 'supported',
};
const REQUIREMENT_KEYS = Object.keys(REQUIREMENTS);

function card(p) {
  const agentEntrypoints = {};
  for (const key of ['mcp_official', 'llms_txt', 'openapi', 'graphql', 'cli', 'agent_docs']) {
    if (p.entrypoints[key]) agentEntrypoints[key] = p.entrypoints[key];
  }
  return {
    id: p.id,
    name: p.name,
    category: p.category,
    summary: p.summary,
    homepage: p.homepage,
    docs: p.entrypoints.docs,
    ...agentEntrypoints,
    badges: p.derived.badges,
    last_verified: p.derived.last_verified,
    ...(p.derived.stale ? { stale: true } : {}),
  };
}

function json(value) {
  return { content: [{ type: 'text', text: JSON.stringify(value, null, 2) }] };
}

const server = new McpServer({ name: 'agent-friendly-services', version: '0.1.0' });

server.registerTool('search_services', {
  title: 'Discover services and access routes',
  description: 'Search candidates and access routes, including gated/unknown access. Documented access fields are public-source claims. Separately reviewed task_runs give outcomes, Agent token usage, service costs and configuration for the matching route only; invalid_run is not a service failure. Interface, capability and personal-access filters must match the SAME route. Missing service costs mean unknown; Agent usage is not converted to money. Use get_service for full review and evidence.',
  inputSchema: {
    query: z.string().optional(),
    category: z.string().optional().describe('Top-level category, e.g. travel.'),
    subcategory: z.string().optional().describe('Full category/subcategory path, e.g. travel/flights.'),
    interface: z.enum(['api', 'sdk', 'cli', 'mcp', 'web', 'mobile']).optional(),
    capability: z.string().optional().describe('Documented outcome, e.g. flights.search; not a measured pass.'),
    personal_access: z.enum(['documented', 'restricted', 'unknown']).optional(),
  },
}, async (filters) => {
  const data = await loadCatalog();
  const validCategories = data.categories.map(c => c.id);
  const validSubcategories = data.categories.flatMap(c => (c.subcategories ?? []).map(s => `${c.id}/${s.id}`));
  const validCapabilities = [...new Set(data.categories.flatMap(c => (c.subcategories ?? []).flatMap(s => s.capabilities.map(x => x.id))))];
  if (filters.category && !validCategories.includes(filters.category)) return json({ error: 'Unknown category', valid_categories: validCategories });
  if (filters.subcategory && !validSubcategories.includes(filters.subcategory)) return json({ error: 'Unknown subcategory', valid_subcategories: validSubcategories });
  if (filters.capability && !validCapabilities.includes(filters.capability)) return json({ error: 'Unknown capability', valid_capabilities: validCapabilities });
  const services = searchServices(data, filters);
  return json({ generated_at: data.generated_at, evidence_notice: data.description, count: services.length, services });
});

server.registerTool('get_service', {
  title: 'Get service discovery record',
  description: 'Get identity, documented routes, source evidence, eligibility, human steps and published cost units, plus separately reviewed task_runs with frozen task, harness/model/effort, date, actual token usage, service costs, outcome and evidence. A run does not certify other tasks or routes. Agent usage is tokens only; unknown service costs remain unknown. invalid_run is an execution environment failure, not a service verdict.',
  inputSchema: { id: z.string() },
}, async ({ id }) => {
  const data = await loadCatalog();
  const service = data.services.find(s => s.id === id.toLowerCase().trim());
  return service ? json({ generated_at: data.generated_at, evidence_notice: data.description, persona: data.persona, service })
    : json({ error: `No service with id "${id}". Use search_services to discover ids.` });
});

server.registerTool(
  'search_providers',
  {
    title: 'Search providers',
    description:
      'Search the Agent-Friendly Services Index for service providers matching your needs. ' +
      'Filter by category (see list_categories), required capabilities, and/or a free-text query. ' +
      'All filters are AND-ed. Returns compact provider cards; use get_provider for the full ' +
      'evidence-backed profile. A missing entrypoint means "no known official URL", not ' +
      'confirmed absence.',
    inputSchema: {
      query: z
        .string()
        .optional()
        .describe('Free-text match against provider id, name, summary, and tags (case-insensitive substring).'),
      category: z
        .string()
        .optional()
        .describe('Category id to filter by, e.g. "databases" or "web-search-data". Use list_categories for valid ids.'),
      require: z
        .array(z.enum(REQUIREMENT_KEYS))
        .optional()
        .describe(
          'Capabilities every result must have. Entrypoint filters (official_mcp, llms_txt, openapi, graphql, cli, agent_docs, webhooks) require a known official URL; check filters (sandbox, self_serve, free_tier, oauth, scoped_tokens, idempotency) require verified "supported" status.'
        ),
    },
  },
  async ({ query, category, require: required }) => {
    const data = await loadData();
    let results = data.providers;
    if (category) {
      const valid = data.categories.some((c) => c.id === category);
      if (!valid) {
        return json({
          error: `Unknown category "${category}".`,
          valid_categories: data.categories.map((c) => c.id),
        });
      }
      results = results.filter((p) => p.category === category);
    }
    if (required?.length) {
      results = results.filter((p) => required.every((r) => REQUIREMENTS[r](p)));
    }
    if (query) {
      const q = query.toLowerCase();
      results = results.filter((p) =>
        [p.id, p.name, p.summary, ...(p.tags ?? [])].join(' ').toLowerCase().includes(q)
      );
    }
    return json({
      count: results.length,
      generated_at: data.generated_at,
      providers: results.map(card),
      ...(results.length === 0
        ? {
            hint:
              'No matches. Try fewer filters, or check list_categories for valid category ids. ' +
              `Valid require values: ${REQUIREMENT_KEYS.join(', ')}.`,
          }
        : {}),
    });
  }
);

server.registerTool(
  'get_provider',
  {
    title: 'Get provider profile',
    description:
      'Get the full evidence-backed profile of one provider by id: every known entrypoint URL ' +
      '(docs, API reference, OpenAPI spec, llms.txt, MCP server, CLI, status page, pricing, ' +
      'signup, API keys, webhooks, rate limits, ...) plus verified checks with official evidence ' +
      'URLs and verification dates. Check statuses: supported | partial | unsupported | unknown ' +
      '| not_applicable — "unknown" means not yet verified, not "no".',
    inputSchema: {
      id: z.string().describe('Provider id, e.g. "stripe", "vercel", "e2b". Find ids via search_providers.'),
    },
  },
  async ({ id }) => {
    const data = await loadData();
    const provider = data.providers.find((p) => p.id === id.toLowerCase().trim());
    if (!provider) {
      const q = id.toLowerCase().trim();
      const prefixLen = (a, b) => {
        let i = 0;
        while (i < a.length && i < b.length && a[i] === b[i]) i++;
        return i;
      };
      const suggestions = data.providers
        .filter(
          (p) =>
            p.id.includes(q) ||
            q.includes(p.id) ||
            p.name.toLowerCase().includes(q) ||
            prefixLen(p.id, q) >= 4
        )
        .map((p) => p.id);
      return json({
        error: `No provider with id "${id}".`,
        ...(suggestions.length ? { did_you_mean: suggestions } : {}),
        all_ids: data.providers.map((p) => p.id),
      });
    }
    return json({ generated_at: data.generated_at, provider });
  }
);

server.registerTool(
  'list_categories',
  {
    title: 'List categories',
    description:
      'List all categories in the index with descriptions and provider counts. ' +
      'Category ids are valid inputs for search_providers.',
    inputSchema: {},
  },
  async () => {
    const data = await loadData();
    const counts = {};
    for (const p of data.providers) counts[p.category] = (counts[p.category] ?? 0) + 1;
    return json({
      generated_at: data.generated_at,
      categories: data.categories.map((c) => ({ ...c, providers: counts[c.id] ?? 0 })),
    });
  }
);

server.registerTool(
  'get_stats',
  {
    title: 'Index stats',
    description:
      'Snapshot of the index and the state of agent readiness across it: provider/URL/check ' +
      'counts, plus how many providers publish llms.txt, an official MCP server, an OpenAPI ' +
      'spec, a CLI, and agent-specific docs.',
    inputSchema: {},
  },
  async () => {
    const data = await loadData();
    const total = data.providers.length;
    const have = (fn) => data.providers.filter(fn).length;
    return json({
      generated_at: data.generated_at,
      counts: data.counts,
      adoption: {
        llms_txt: `${have(REQUIREMENTS.llms_txt)}/${total}`,
        official_mcp: `${have(REQUIREMENTS.official_mcp)}/${total}`,
        openapi: `${have(REQUIREMENTS.openapi)}/${total}`,
        cli: `${have(REQUIREMENTS.cli)}/${total}`,
        agent_docs: `${have(REQUIREMENTS.agent_docs)}/${total}`,
        sandbox_supported: `${have(REQUIREMENTS.sandbox)}/${total}`,
        self_serve: `${have(REQUIREMENTS.self_serve)}/${total}`,
      },
      unknown_checks_open: data.providers.reduce(
        (n, p) => n + (p.derived.unknown_checks?.length ?? 0),
        0
      ),
      contribute: 'https://github.com/Olorinm/agent-friendly-services/blob/main/docs/contributing.md',
    });
  }
);

const transport = new StdioServerTransport();
await server.connect(transport);
