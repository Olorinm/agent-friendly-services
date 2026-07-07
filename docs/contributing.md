# Contributing

Every fact in this directory is a small, self-contained contribution. Pick your
size:

| Effort | Contribution | How |
| --- | --- | --- |
| 2 min | Report a broken or wrong link | [Issue form](../../issues/new/choose) |
| 15 min | Resolve one `unknown` check | Find official evidence, PR one status change |
| 15 min | Add a missing entrypoint URL (llms.txt, OpenAPI, MCP…) | PR one line |
| 1–2 h | Add a provider | New YAML file, see below |
| ongoing | Adopt a category as steward | Say hi in an issue |

Every open `unknown` is a ready-made first contribution: see each provider's
**"Unknown (help wanted)"** line in [`generated/providers.md`](../generated/providers.md),
or `derived.unknown_checks` in `generated/providers.json`.

## Add a provider

1. Check the [inclusion rules](./methodology.md#inclusion-rules): hosted
   service + account system + API surface; product-precision naming.
2. Copy the closest existing file in `data/providers/`; the filename is the id.
3. Fill what you can verify; omit or mark `unknown` what you can't. A narrow,
   solid entry beats a complete-looking guessed one.
4. `npm run validate` (schema + rules, readable errors) and optionally
   `npm run probe -- --only=<id>` (checks your URLs answer).
5. Open a PR. One provider per PR.

Minimum bar: `id`, `name`, `category`, `homepage`, `summary`, `submitted_by`,
`entrypoints.docs`, and at least 4 answered checks with evidence.

## Evidence rules

- Priority: official docs > API reference > official repo > changelog >
  official blog > trusted community source (last resort, checks only).
- Entrypoint URLs must be login-free and official (exception: `mcp_community`).
- `supported`/`partial` ⇒ evidence URL + `verified: "YYYY-MM-DD"` (quoted).
- `partial`/`not_applicable` ⇒ a `notes` line explaining scope or why.
- Replacing a dead link: prefer the page's new location; if it's gone, use a
  `web.archive.org` snapshot and note it.
- Update `verified` **only** on checks you actually re-verified.

## Contribute with your agent

This repo is designed so a coding agent can contribute end-to-end. Paste this
into Claude Code, Codex, or similar, from a checkout of this repo:

```text
Read AGENTS.md. Then resolve one "unknown" check (listed per provider in
generated/providers.md): research official evidence on the provider's docs site, update
the provider YAML accordingly (or leave it unknown if evidence is genuinely
missing), run `npm run validate`, and prepare a one-line-change PR.
```

Maintainers review agent PRs by the same standard as human PRs: is the evidence
official and does it say what the status claims?

## Vendors

You're welcome to maintain your own entry. Set `submitted_by: vendor`, use
documentation (not marketing pages) as evidence, and expect maintainers to
push back on optimistic `supported`s. Disagree with a status? Open an issue
with official evidence.

## What maintainers review

Schema compliance (CI does this), evidence reliability, over-optimistic
statuses, category and naming rules, duplicates. **Not** reviewed: fame,
"worthiness", subjective quality — the directory records facts only.
