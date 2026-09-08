import type { Category, Provider } from './lib.ts';
import type { Evaluation } from './evaluations.ts';

export function taxonomyErrors(categories: Category[]): string[] {
  const errors: string[] = [];
  const ids = new Set<string>();
  for (const cat of categories) {
    if (!/^[a-z0-9][a-z0-9-]*$/.test(cat.id) || ids.has(cat.id)) errors.push(`Invalid or duplicate category: ${cat.id}`);
    ids.add(cat.id);
    const children = new Set<string>();
    for (const sub of cat.subcategories ?? []) {
      if (!/^[a-z0-9][a-z0-9-]*$/.test(sub.id) || children.has(sub.id)) errors.push(`Invalid or duplicate subcategory: ${cat.id}/${sub.id}`);
      children.add(sub.id);
      const caps = new Set<string>();
      for (const cap of sub.capabilities) {
        if (!/^[a-z0-9-]+\.[a-z0-9-]+$/.test(cap.id) || caps.has(cap.id)) errors.push(`Invalid or duplicate capability: ${cap.id}`);
        caps.add(cap.id);
      }
    }
  }
  return errors;
}

export function calendarDateValid(value: string, today: string): boolean {
  const timestamp = Date.parse(`${value}T00:00:00Z`);
  return /^\d{4}-\d{2}-\d{2}$/.test(value) && Number.isFinite(timestamp)
    && new Date(timestamp).toISOString().slice(0, 10) === value && value <= today;
}

/** Called after JSON Schema validation, so field shapes are known here. */
export function catalogErrors(p: Provider, categories: Category[], today: string): string[] {
  if (!p.catalog) return [];
  const errors: string[] = [];
  const catalog = p.catalog;
  const taxonomy = new Map<string, NonNullable<Category['subcategories']>[number]>(
    categories.flatMap(c => (c.subcategories ?? []).map(s => [`${c.id}/${s.id}`, s] as const)),
  );
  const allowedCaps = new Set<string>();
  for (const id of catalog.classifications) {
    const sub = taxonomy.get(id);
    if (!sub) errors.push(`Unknown classification: ${id}; add it to data/categories.yaml first.`);
    else sub.capabilities.forEach(c => allowedCaps.add(c.id));
  }
  for (const [id, source] of Object.entries(catalog.sources)) {
    if (!calendarDateValid(source.checked_on, today)) errors.push(`sources.${id}.checked_on must be a real, non-future calendar date.`);
  }
  const routeIds = new Set<string>();
  for (const route of catalog.routes) {
    if (routeIds.has(route.id)) errors.push(`Duplicate route id: ${route.id}`);
    routeIds.add(route.id);
    for (const cap of Object.keys(route.capabilities ?? {})) {
      if (!allowedCaps.has(cap)) errors.push(`routes.${route.id}: capability ${cap} does not belong to this service's classifications.`);
    }
    for (const cost of route.costs ?? []) {
      if (cost.unit === 'money' && !cost.currency) errors.push(`routes.${route.id}: money costs require an ISO currency.`);
      if (cost.unit !== 'money' && cost.currency) errors.push(`routes.${route.id}: currency only applies to unit: money.`);
    }
  }
  const byId = new Map(catalog.routes.map(r => [r.id, r]));
  for (const route of catalog.routes) {
    const visited = new Set([route.id]);
    let via = route.via;
    while (via) {
      if (!byId.has(via)) { errors.push(`routes.${route.id}.via references missing route: ${via}`); break; }
      if (visited.has(via)) { errors.push(`routes.${route.id}.via forms a cycle.`); break; }
      visited.add(via);
      via = byId.get(via)!.via;
    }
  }
  function walk(value: unknown, at: string) {
    if (!value || typeof value !== 'object') return;
    for (const [key, child] of Object.entries(value)) {
      if (key === 'evidence' && Array.isArray(child)) {
        for (const ref of child) if (!Object.hasOwn(catalog.sources, ref)) errors.push(`${at}.evidence references missing source: ${ref}`);
      } else walk(child, `${at}.${key}`);
    }
  }
  walk(catalog.routes, 'routes');
  return errors;
}

export function catalogService(p: Provider, pool: 'provider' | 'candidate', evaluations: Evaluation[] = []) {
  const runs = evaluations.filter(r => r.service_id === p.id);
  return {
    id: p.id, name: p.name, category: p.category, homepage: p.homepage,
    summary: p.summary, submitted_by: p.submitted_by, tags: p.tags ?? [], notes: p.notes ?? [],
    record_pool: pool,
    evidence_level: runs.length ? 'public_sources_and_task_runs' : p.catalog ? 'public_sources_only' : 'legacy_record',
    // Records apply only to their exact route/task; do not promote source claims.
    route_tests: runs.length ? 'recorded' : 'not_recorded',
    task_runs: runs,
    catalog: p.catalog ? { ...p.catalog, routes: p.catalog.routes.map(r => ({ ...r,
      task_run_ids: runs.filter(run => run.route_id === r.id).map(run => run.run_id),
    })) } : null,
  };
}
