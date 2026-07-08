# AGENTS.md

This repository is a machine-readable directory of agent-friendly services.
You (an agent) can contribute to it end-to-end. This file tells you how.

## Source of truth

- Provider data: `data/providers/*.yaml` — one file per provider
- Field definitions: `data/fields.yaml` — what every entrypoint and check means
- Categories: `data/categories.yaml`
- `README.md` and `generated/` are **build outputs. Never edit them.** CI regenerates them on main.

## Add a provider

1. Copy an existing file in `data/providers/`. Use a lowercase id equal to the filename (`modal.yaml` → `id: modal`).
2. Check inclusion rules first: hosted service + account system + API surface. Libraries and frameworks don't qualify. Name the product precisely (`Docker Hub`, not `Docker`).
3. Fill `entrypoints` with public, login-free official URLs. **Omit what you cannot find** — a missing entrypoint means "no known URL", and that is fine.
4. Fill the checks you can verify. Status enum: `supported | partial | unsupported | unknown | not_applicable`.
5. Every `supported`/`partial` needs an official evidence URL and a `verified` date. `partial` and `not_applicable` also need `notes`.
6. Dates are quoted strings: `verified: "2026-07-07"`. Update only the checks you actually verified.
7. Run `npm run validate`. Fix what it reports — the messages tell you how.
8. Optionally run `npm run probe -- --only=<id>` to confirm your URLs answer.

## Update a provider

1. Change only the fields you re-verified; update only their `verified` dates.
2. Leave everything you did not check untouched.

## Resolve an `unknown` (the easiest contribution)

1. Pick any check marked `unknown` (each provider's "Unknown (help wanted)" line in [`generated/providers.md`](./generated/providers.md) lists them; machine-readable in `generated/providers.json` under `derived.unknown_checks`).
2. **Start with the provider's `llms.txt` if it has one**: fetch it and grep for the check's keywords (`idempot`, `revoke`, `scope`, `sandbox`, `preview`, `usage`, `billing`, `deprecat`, `oauth`). It indexes the canonical docs pages far more reliably than guessing URLs — and sometimes contains facts itself (agent-access policies, hosted MCP endpoints).
3. Otherwise find official evidence (docs > API reference > official repo > changelog > official blog).
4. Prefer documentation pages over console/dashboard URLs as evidence — docs are probeable and quotable; login pages aren't. If the page redirects, record the post-redirect canonical URL.
5. For `unsupported` (absence claims), quote the decisive sentence in `notes` — absence needs stronger backing than presence.
6. Set the status, add `evidence` and `verified`, run `npm run validate`, open a PR.
7. If you find no reliable evidence, leave it `unknown`. Do not guess.

## Hard rules

- Do not invent URLs or evidence. `unknown` is a valid, welcome answer.
- Never write bare `yes`/`no` anywhere — YAML 1.1 parsers read them as booleans.
- Evidence must be official sources; marketing pages don't count for checks.
- If you work for the provider, set `submitted_by: vendor`.
- Do not edit `README.md` or `generated/` — CI will reject the PR.
- One provider per PR. Do not change `data/fields.yaml` or `schema/` in the same PR as provider data.
