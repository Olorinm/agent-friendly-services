# Methodology

## What this is

A directory of **service entry points for AI agents**, with a small set of
evidence-backed capability facts. The core question it answers: *an agent needs
to use service X — where does it start, how does it authenticate, what is
machine-readable, and how fresh is that information?*

It is deliberately **not** a certification body, a score, or a ranking.

## Principles

1. **URL = fact.** Most "does X exist?" questions are answered by the link
   itself. The link is simultaneously the data, the evidence, and the thing a
   script can probe weekly.
2. **Facts, not scores.** No tiers, no weights, no editorial judgment. Badges
   shown in the README map 1:1 to fields — nothing is composed or ranked.
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
   servers). Humans spend their time only on the 12 behavioral checks.

## Field semantics

Canonical definitions live in [`data/fields.yaml`](../data/fields.yaml) —
that file, not this document, is the source of truth.

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

1. Hosted service with an API surface and a self-serve access path — an
   account system, or an agent-native pay-per-call scheme (e.g. x402) for
   account-less services. Libraries, frameworks, and self-hosted-only software
   don't qualify.
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

- Vendors may submit or update their own entries with `submitted_by: vendor`;
  evidence must be documentation, not marketing pages.
- Disputes: open an issue with official evidence. Facts change when evidence
  changes; experience reports don't move statuses.
- Referencing this directory ("listed with an Official MCP badge") is fine, but
  data updates whenever evidence changes — nothing here is a certification.

## License

Code is MIT. Data (`data/`, `generated/`) is CC BY 4.0 — build on it freely,
with attribution.
