# MCP Server

A stdio MCP server exposing the [Agent-Friendly Services Index](../README.md). It fetches
[`generated/providers.json`](../generated/providers.json) and the discovery
[`generated/catalog.json`](../generated/catalog.json) from `main` (15-minute cache),
so it always serves the latest published data — no reinstall needed when the index updates.
If the network is unavailable and you run it from a checkout, it falls back to the local copy.

## Install

**Claude Code:**

```bash
claude mcp add agent-friendly-services -- npx -y github:Olorinm/agent-friendly-services
```

**Any MCP client** (Claude Desktop, Cursor, Windsurf, ...):

```json
{
  "mcpServers": {
    "agent-friendly-services": {
      "command": "npx",
      "args": ["-y", "github:Olorinm/agent-friendly-services"]
    }
  }
}
```

Requires Node.js >= 18. From a checkout you can also run it directly: `node mcp/server.mjs`.

## Tools

| Tool | Input | Returns |
|---|---|---|
| `search_providers` | `query?`, `category?`, `require?` (e.g. `["official_mcp", "sandbox"]`) | Compact provider cards matching all filters |
| `search_services` | `query?`, `category?`, `subcategory?`, `interface?`, `capability?`, `personal_access?` | Discovery across both pools, with source claims and separate task observations for matching routes |
| `get_service` | `id` | Full discovery sources, route eligibility, human steps, published costs, limitations and reviewed task records |
| `get_provider` | `id` (e.g. `"stripe"`) | Full profile: every entrypoint URL + verified checks with evidence and dates |
| `list_categories` | — | All categories with descriptions and provider counts |
| `get_stats` | — | Index counts + agent-readiness adoption (llms.txt, official MCP, OpenAPI, ...) |

`require` values — entrypoint presence: `official_mcp`, `llms_txt`, `openapi`, `graphql`, `cli`,
`agent_docs`, `webhooks`; verified-`supported` checks: `sandbox`, `self_serve`, `free_tier`,
`oauth`, `scoped_tokens`, `idempotency`.

Reading the results: a missing entrypoint means **"no known official URL"**, not confirmed
absence; check status `unknown` means "not yet verified", not "no". See
[methodology](../docs/methodology.md).

## Configuration

| Env var | Default | Purpose |
|---|---|---|
| `AFS_DATA_URL` | raw `main` providers.json | Point at a fork or a local snapshot for testing |
| `AFS_CATALOG_URL` | raw `main` catalog.json | Override discovery data independently |
| `AFS_DATA_DIR` | unset | Read both JSON files from this local directory, without network access |

For local previews, generate into `AFS_OUTPUT_DIR=/private/tmp/afs-preview`
and run with `AFS_DATA_DIR=/private/tmp/afs-preview/generated`.

Discovery example: `search_services` with `subcategory: "travel/flights"` and
`interface: "mcp"`. Add `capability: "flights.search"` only to require a
documented search capability; unknown coverage is excluded by that filter.
All route filters apply to the same route. Use `get_service` before making
an access decision: `documented` is a source claim, not an observed success.
Country eligibility, missing requirements and missing costs remain unknown.
`list_categories` and `get_stats` retain legacy index counts; they do not count
the discovery candidate pool. Taxonomy is also available in `catalog.json`.
# Current task results

`search_services` returns reviewed `task_runs` under the matching access route; `get_service` includes full frozen task, runtime configuration, usage, review and evidence. Agent consumption is recorded as input, cached-input and output tokens, without monetary conversion; cached input is already included in input. Service call costs are recorded separately and stay null when unknown. Other routes do not inherit a pass, and `invalid_run` is not a service failure. For an unpublished local checkout, set `AFS_DATA_DIR` to its absolute `generated/` directory; default remote data changes only after publication.

Model cost estimates are in `task_runs[].model_cost` (amount, snapshot provenance and unknown reason). New service charges include `service_cost` with reported/free/estimated/unknown basis; historical `service_cost_usd` values remain unchanged. `generated/evaluations.json` also exposes `comparisons` with resolution rates and per-valid-trial mean tokens/model costs/service costs. Failures contribute to means; invalid environments do not, and missing values are never zero-filled. Refresh model prices with `npm run pricing:update`, then run `npm run generate` offline.
