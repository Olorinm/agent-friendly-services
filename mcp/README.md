# MCP Server

A stdio MCP server exposing the [Agent-Friendly Services Index](../README.md). It fetches
[`generated/providers.json`](../generated/providers.json) live from `main` (15-minute cache),
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
