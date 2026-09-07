# Methodology

## What this is

A service discovery, verification and evaluation project for AI agents. The
user question is: which service can complete this task, and at what cost,
setup effort and human involvement?

Service discovery, [user-needs research](./contributing.md#research-user-needs),
test design and execution build on one another. The [flight findings](./flights.zh-CN.md)
show the current pilot. Research records preserve public user
reports, analyst inferences and hypotheses separately; test feasibility must
not determine which real needs are worth recording.

The [catalog standard](./catalog-standard.zh-CN.md) covers candidate discovery
and documented routes. The legacy index and its experiments remain available.
Public-source claims, request-shape checks, onboarding and real task results
are distinct evidence levels. There is no overall quality score or certification.

## Principles

1. **URL = an entrypoint or source.** Most "does X exist?" questions are answered by the link
   itself. A link can be probed weekly, but does not establish eligibility or task success.
2. **Facts before scores.** The discovery catalog has no ranking. Existing
   experiment summaries are limited to their published task and aggregation
   definitions; they do not establish a general best service.
3. **Evidence or `unknown`.** Every `supported`/`partial` check carries an
   official evidence URL and a verification date. When evidence can't be found,
   the honest answer is `unknown` — never a guess.
4. **A missing entrypoint means "no known URL."** The directory vouches for the
   links it lists; it does not claim to prove absence.
5. **Freshness is per-fact, not per-file.** Each check carries its own
   `verified` date. URL liveness is machine-checked weekly
   (`generated/link-health.json`). A provider is flagged `Stale` when any check
   is older than 180 days.
6. **Machines first.** Everything a script can verify is verified by a script
   (`probe` for URLs; the official MCP registry as an authority for MCP
   servers). Source interpretation, onboarding and independent task verification require separate evidence.

## Field semantics

Legacy check definitions live in [`data/fields.yaml`](../data/fields.yaml).
New discovery fields live in [`schema/catalog.schema.json`](../schema/catalog.schema.json)
and the [catalog standard](./catalog-standard.zh-CN.md).

Check status enum:

| Status | Meaning | Evidence | Notes |
| --- | --- | --- | --- |
| `supported` | Clearly supported | required | optional |
| `partial` | Limited: beta, region-, plan- or product-restricted | required | **required** |
| `unsupported` | An official source states it is not supported | recommended | recommended |
| `unknown` | Checked, no reliable evidence found yet | — | optional |
| `not_applicable` | Meaningless for this class of service | — | **required** |

Why not `yes`/`no`: bare `yes`/`no` are booleans in YAML 1.1 parsers (PyYAML
and friends) and strings in YAML 1.2 parsers — the same file would mean
different things to different consumers. The enum avoids every YAML reserved
word, and `verified` dates are quoted strings for the same reason.

Evidence for `unsupported`: official statements of absence are rare. Acceptable
evidence: an official issue/forum reply, a changelog removal notice, an explicit
documented limitation. "I couldn't find it" is `unknown`, not `unsupported`.

## Inclusion rules

1. Task-relevant service products, including unknown, gated, paused and retired
   access routes. Accounts, public APIs and self-serve eligibility are not
   required for candidate discovery. Standalone libraries/frameworks are not
   service providers; their integrations can be recorded as routes.
2. Entries are named at product precision: `Docker Hub`, not `Docker`.
3. Multi-product giants (AWS, GCP, Azure) need a `scope` field declaring which
   surface the entry covers — honest "all partial" rows carry no information.
   They are intentionally excluded from the seed set.
4. Renames/acquisitions: keep the id, add `aliases`. Dead services: set
   `archived: true` with a reason — history stays.
5. New services enter through the [candidate pool](./candidate-pool.md)
   (`data/candidates/`) and are promoted into the index only after a passing
   M1 agent run plus an evidence review.

## Related projects (and why we don't duplicate them)

- [Fern Agent Score](https://buildwithfern.com/agent-score) /
  [Agent-Friendly Docs Spec](https://github.com/fern-api/agent-score) and
  [Cloudflare Agent Readiness](https://blog.cloudflare.com/agent-readiness/)
  score **documentation sites**. We link docs and record what they can't see:
  signup, auth, sandboxes, billing, idempotency, policy.
- The [official MCP Registry](https://registry.modelcontextprotocol.io/) is the
  authority for MCP servers; we point at it and cross-check against it rather
  than maintaining a rival registry.
- [llms.txt hub](https://llmstxthub.com/) indexes llms.txt files; here llms.txt
  is one field among many.

## Governance

- Vendors may submit with `submitted_by: vendor`. Legacy checks need technical
  documentation; discovery also accepts labeled official sites and publisher
  listings as source claims, never as measured quality.
- Disputes: open an issue with official evidence. Documented facts change with sources. Reproducible experience reports belong
  in onboarding/task records and do not silently overwrite documentation claims.
- Referencing this directory ("listed with an Official MCP badge") is fine, but
  data updates whenever evidence changes — nothing here is a certification.

## License

Code is MIT. Data (`data/`, `generated/`) is CC BY 4.0 — build on it freely,
with attribution.
