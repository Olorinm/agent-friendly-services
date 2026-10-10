// Pure discovery filters, shared by the MCP server and regression tests.
import { flattenCategories, inClassification, serviceClassifications, withinClassification } from '../scripts/taxonomy.mjs';

const scopes = filters => [filters.category, filters.classification, filters.subcategory].filter(Boolean);

export function categoryTree(data) {
  const walk = (nodes, parent = '') => nodes.map(node => {
    const path = parent ? `${parent}/${node.id}` : node.id;
    const members = data.services.filter(service => inClassification(service, path));
    return { ...node, path, services: new Set(members.map(s => s.id)).size,
      providers: new Set(members.filter(s => s.record_pool === 'provider').map(s => s.id)).size,
      candidates: new Set(members.filter(s => s.record_pool === 'candidate').map(s => s.id)).size,
      subcategories: walk(node.subcategories ?? [], path) };
  });
  return walk(data.categories);
}

export function matchingRuns(service, route, filters, categories = []) {
  const owner = filters.capability && flattenCategories(categories).find(node =>
    node.capabilities?.some(cap => cap.id === filters.capability))?.path;
  return (service.task_runs ?? []).filter(run => run.route_id === route.id
    && [...scopes(filters), ...(owner ? [owner] : [])].every(scope =>
      run.classification && withinClassification(run.classification, scope)));
}
export function matchingRoutes(service, filters) {
  return (service.catalog?.routes ?? []).filter(r =>
    (!filters.interface || r.interface === filters.interface) &&
    (!filters.capability || r.capabilities?.[filters.capability]?.value === 'documented') &&
    (!filters.personal_access || (r.personal_access?.value ?? 'unknown') === filters.personal_access)
  );
}

export function searchServices(data, filters) {
  return data.services.filter(s => {
    const classes = serviceClassifications(s);
    if (!scopes(filters).every(scope => inClassification(s, scope))) return false;
    if (filters.capability && scopes(filters).length && data.categories) {
      const owner = flattenCategories(data.categories).find(node => node.capabilities?.some(cap => cap.id === filters.capability))?.path;
      if (!owner || !scopes(filters).every(scope => withinClassification(owner, scope) || withinClassification(scope, owner))) return false;
    }
    if (filters.query && ![s.id, s.name, s.summary, ...(s.tags ?? []), ...classes, ...(s.catalog?.routes ?? []).map(r => r.upstream ?? '')].join(' ').toLowerCase().includes(filters.query.toLowerCase())) return false;
    const routeFilter = filters.interface || filters.capability || filters.personal_access;
    return !routeFilter || matchingRoutes(s, filters).length > 0;
  }).map(s => ({
    id: s.id, name: s.name, category: s.category, classifications: serviceClassifications(s),
    summary: s.summary, record_pool: s.record_pool, evidence_level: s.evidence_level,
    route_tests: matchingRoutes(s, filters).some(r => matchingRuns(s, r, filters, data.categories).length) ? 'recorded' : 'not_recorded',
    notes: s.catalog?.notes ?? [],
    routes: matchingRoutes(s, filters).map(r => ({
      id: r.id, interface: r.interface, entry_url: r.entry_url,
      availability: r.availability?.value ?? 'unknown',
      personal_access: r.personal_access?.value ?? 'unknown',
      data_kind: r.data_kind?.value ?? 'unknown',
      upstream: r.upstream ?? 'unknown',
      capabilities: r.capabilities ?? {}, notes: r.notes ?? '',
      task_runs: matchingRuns(s, r, filters, data.categories).map(run => ({
        classification: run.classification, phase: run.phase,
        run_id: run.run_id, task: run.task, status: run.status, reason: run.reason,
        ...(run.outcome ? { outcome: run.outcome } : {}),
        ...(run.request_usage ? { request_usage: run.request_usage } : {}),
        ...(s.result_notes?.[run.run_id] ? { additional_context: s.result_notes[run.run_id] } : {}),
        harness: run.harness, model: run.model, reasoning_effort: run.reasoning_effort,
        started_at: run.started_at, ended_at: run.ended_at,
        usage: run.usage, elapsed_seconds: run.elapsed_seconds,
        environment: run.environment, budget_seconds: run.budget_seconds,
        service_cost_usd: run.service_cost_usd,
        model_cost: run.model_cost ?? null, service_cost: run.service_cost ?? null,
        human_interventions: run.human_interventions,
        record: `data/experiments/evaluations/${run.run_id}.json`,
      })),
    })),
  }));
}
