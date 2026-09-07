// Pure discovery filters, shared by the MCP server and regression tests.
export function matchingRoutes(service, filters) {
  return (service.catalog?.routes ?? []).filter(r =>
    (!filters.interface || r.interface === filters.interface) &&
    (!filters.capability || r.capabilities?.[filters.capability]?.value === 'documented') &&
    (!filters.personal_access || (r.personal_access?.value ?? 'unknown') === filters.personal_access)
  );
}

export function searchServices(data, filters) {
  return data.services.filter(s => {
    const classes = s.catalog?.classifications ?? [];
    if (filters.category && s.category !== filters.category && !classes.some(c => c.split('/')[0] === filters.category)) return false;
    if (filters.subcategory && !classes.includes(filters.subcategory)) return false;
    if (filters.query && ![s.id, s.name, s.summary, ...(s.tags ?? []), ...classes, ...(s.catalog?.routes ?? []).map(r => r.upstream ?? '')].join(' ').toLowerCase().includes(filters.query.toLowerCase())) return false;
    const routeFilter = filters.interface || filters.capability || filters.personal_access;
    return !routeFilter || matchingRoutes(s, filters).length > 0;
  }).map(s => ({
    id: s.id, name: s.name, category: s.category, classifications: s.catalog?.classifications ?? [],
    summary: s.summary, record_pool: s.record_pool, evidence_level: s.evidence_level,
    route_tests: (s.task_runs ?? []).some(run => matchingRoutes(s, filters).some(r => r.id === run.route_id)) ? 'recorded' : 'not_recorded',
    routes: matchingRoutes(s, filters).map(r => ({
      id: r.id, interface: r.interface, entry_url: r.entry_url,
      availability: r.availability?.value ?? 'unknown',
      personal_access: r.personal_access?.value ?? 'unknown',
      data_kind: r.data_kind?.value ?? 'unknown',
      upstream: r.upstream ?? 'unknown',
      task_runs: (s.task_runs ?? []).filter(run => run.route_id === r.id).map(run => ({
        run_id: run.run_id, task: run.task, status: run.status, reason: run.reason,
        harness: run.harness, model: run.model, reasoning_effort: run.reasoning_effort,
        started_at: run.started_at, ended_at: run.ended_at,
        usage: run.usage, elapsed_seconds: run.elapsed_seconds,
        service_cost_usd: run.service_cost_usd,
        human_interventions: run.human_interventions,
        record: `data/experiments/evaluations/${run.run_id}.json`,
      })),
    })),
  }));
}
