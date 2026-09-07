# The candidate pool

`data/candidates/` records services relevant to a user task, including unknown
access paths, business-only products, invitation requirements, paused
applications and retired routes. Ordinary individuals need to know about
these barriers; self-serve access is not an inclusion requirement.

The [catalog standard](./catalog-standard.zh-CN.md) defines the discovery
format. Identity, a category/subcategory and a dated first-party source are
enough to start. Documentation, credentials and answered legacy checks are
not required. `routes: []` means no route has been established, not that no API
exists. Existing legacy candidates remain compatible.

## Publication

- `generated/candidates.json` retains the compact legacy candidate list.
- `generated/catalog.json` includes discovery records from both pools, with
  labeled public-source claims, per-source dates and route boundaries.
- `generated/catalog.md` provides a readable route comparison.
- MCP `search_services` / `get_service` expose discovery records. Legacy
  `search_providers` / `get_provider` do not inherit these new route claims.

An entry in `data/providers/` can gain new, untested routes. Keep one identity
file and never copy its old verification badges onto those routes. Existing
M1 runs and task experiments remain available through the old views; they are
not yet linked to catalog route IDs.

## Verification and promotion

The existing legacy-index promotion gate remains: evidence review and a
majority pass across at least three published M1 first-call repetitions under
the [verification method](./agent-verification.md) and
[publication protocol](./publication-protocol.md). Moving an entry into that
index also requires its legacy documentation entrypoint and reviewed checks.
Discovery-only records cannot be promoted by simply moving the file.

M1 establishes request-shape evidence, not successful onboarding or task
completion. Do not describe an entry as task-tested because it passed M1.
Future results must identify the concrete route, task, environment,
permissions, dates, costs, human intervention and independent verification.
There is no automatic promotion or overall score in the discovery catalog.

## Maintenance

Keep failed, restricted and retired routes with sources and dates. Never infer
service death from failed web probes: authentication, bot protection, dynamic
pages and protocol endpoints can prevent ordinary HTTP reads. Archive a whole
product only when reliable evidence establishes it has ended; one retired
route need not invalidate its other routes.

Use precise product names and stable IDs. SDKs/CLIs/MCP wrappers are routes;
independently operated hosted products can have their own identities. Official
means official to the listed product, not necessarily to its upstream data
source. Vendors must disclose `submitted_by: vendor`.
