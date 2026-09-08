# Contributing

Every fact in this directory is a small, self-contained contribution. Pick your
size:

Keep durable findings, their supporting evidence and reusable tools in the
repository. Update existing source records; discussion drafts and duplicate
process reports do not need separate committed documents. Generated views
come from those records. See [AGENTS.md](../AGENTS.md) for the project principles.

For the current task-evaluation workflow, follow [execution and review instructions](../data/experiments/AGENTS.md): reuse the candidate and task tables, launch a fresh measured Agent, independently review the evidence, record the outcome, and regenerate the [results table](../generated/evaluations.md) and catalog. The `agent-verify` command below is a separate legacy experiment runner.

| Effort | Contribution | How |
| --- | --- | --- |
| 2 min | Report a broken or wrong link | [Issue form](../../issues/new/choose) |
| 15 min | Resolve one `unknown` check | Find official evidence, PR one status change |
| 15 min | Add a missing entrypoint URL (llms.txt, OpenAPI, MCP…) | PR one line |
| 1–2 h | Add a provider (enters the [candidate pool](./candidate-pool.md)) | New YAML file, see below |
| ongoing | Adopt a category as steward | Say hi in an issue |

Every open `unknown` is a ready-made first contribution: see each provider's
**"Unknown (help wanted)"** line in [`generated/providers.md`](../generated/providers.md),
or `derived.unknown_checks` in `generated/providers.json`.

## Research user needs

Keep essential sources, task adaptations and coverage limits beside the task table.
For larger research rounds, optionally use `data/research/<category>/<subcategory>.yaml`,
extending a record or creating one with `npm run research:init -- <category/subcategory>`.
The [flight findings](./flights.zh-CN.md) show the current pilot.

1. Research real goals and constraints through public original discussions,
   actual workflows and relevant surveys. Use provider docs to understand
   capabilities; they do not establish user demand. Seek different users,
   preferences and failure cases; document coverage gaps.
2. Keep source URLs, reading dates, faithful summaries and limitations beside
   the findings. Distinguish user reports, analyst inferences and hypotheses.
   Note partial/indexed access and author corrections; group reposts and
   survey derivatives without counting them as independent evidence. Public
   sample counts do not establish market frequency.
3. Derive scenarios from those needs, recording sources and added assumptions.
   Start testing with a few real tasks, identify their required capabilities,
   and increase constraints or completion depth as useful. Explain selection
   and what each task adds. Untested or difficult needs remain in the record.
4. Use `npm run validate` and `npm run generate` to check references and update
   views. Research diagnostics are advisory and do not verify source meaning.
   Formats, templates and tools can evolve; search logs are optional supporting
   material, not a required standalone deliverable.

Research scenarios are not executable tests. A runnable task adds concrete
inputs, environment, budget, ending conditions and independent verification,
and retains the source of the user need (inline or in a research scenario). Publish measured outcomes with their
conditions and evidence; keep setup effort, service costs, Agent token usage and
human involvement visible. Never fill an unmeasured cost with zero.

## Add a candidate

1. Follow the [catalog standard](./catalog-standard.zh-CN.md). Search both data
   pools for an existing identity; use precise product names and stable IDs.
2. Add a file in `data/candidates/` with identity, classification and dated
   first-party sources. Routes, API docs, credentials and legacy checks can be
   unknown. Restricted and paused services are useful records too.
3. Keep per-route capabilities, eligibility, human steps and cost units separate.
   Every known fact references a source; missing facts mean unknown, never zero.
4. Run `npm run validate` and `npm test`. Preview with `AFS_OUTPUT_DIR` to avoid
   changes to generated files. Optional link probes are not functional tests.
5. Keep routine contributions focused on one product. Schema migrations may
   need representative records to demonstrate the model.

Legacy-format records remain compatible. The [candidate pool](./candidate-pool.md)
explains the distinction between directory membership and task verification.

## Evidence rules

The rules below describe legacy checks. Catalog sources can also be official
registration/pricing pages or publisher listings, explicitly labeled as public
claims. They never establish measured task performance.


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

New vendor submissions go through the [candidate pool](./candidate-pool.md)
like everyone else's — the fastest way to get promoted is to make your docs
good enough that an agent's first call just works. Vendor-submitted entries
are labeled `vendor-submitted` wherever they render.

## What maintainers review

Schema compliance (CI does this), evidence reliability, over-optimistic
statuses, category and naming rules, duplicates. **Not** reviewed: fame,
"worthiness", subjective quality — the directory records facts only.

### Link-health maintenance

`npm run probe -- --only=kiwi,hugging-face` writes a targeted report to the ignored
`data/experiments/results/selected-link-health.json`; it does not replace the full
weekly report. Use `--output=path` to choose another destination.

Known MCP entry points are probed with `Accept: application/json, text/event-stream`.
A 406 or 405 is inconclusive, not a dead link. Protocol discovery can establish that
an MCP server answers, but does not prove a user task succeeds. Full reports retain
`checked_at` for the full sweep; a selectively refreshed entry has its own
`checked_at`, with `last_partial_check_at` on the report. Unchecked entries keep their
original dates.
