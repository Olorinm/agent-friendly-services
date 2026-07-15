# The candidate pool

New services do not enter the index directly. They enter `data/candidates/` —
the **candidate pool** — and are promoted only after an agent actually runs
against them. Claims are tested, not argued: maintainers never have to judge
whether a submission is "notable enough" or "too promotional", and vendors
never have to lobby. The measurement decides.

## Entering the pool (mechanical bar, no editorial judgment)

A candidate PR is merged when all of these hold:

1. The YAML follows the exact same schema and rules as `data/providers/`
   (`npm run validate` passes — candidates are validated too).
2. The service is real and reachable: `homepage` and `entrypoints` answer
   (`npm run probe -- --only=<id>`).
3. [Inclusion rules](./methodology.md#inclusion-rules) are met — note that a
   self-serve **agent-native pay-per-call scheme (e.g. x402) counts as an
   access path**; an account system is not mandatory.
4. `submitted_by` is honest (`vendor` if you work on the service).
5. One provider per PR.

Maintainers still reject fraud, malware, and impersonation. That is the only
human judgment at the door.

## What being a candidate means

- Listed in the README **Candidate pool** table: identity, entrypoint file,
  M1 status. Nothing else.
- The claims inside the candidate's YAML are **not rendered** anywhere and the
  entry is **not** in `generated/providers.json` (agents consuming the dataset
  never ingest unverified claims). Candidates live in
  [`generated/candidates.json`](../generated/candidates.json), clearly labeled.
- Candidate URLs are probed weekly like everyone else's.

## Promotion into the index

Both gates, in any order:

1. **M1 first-call run passes** — majority of ≥3 published dry-fire reps on the
   standard environment: an agent, starting from the docs entry point with no
   credentials, constructs the provider's canonical first API call and proves
   the request shape is right (documented auth-error with a fake credential;
   for credential-less/x402 APIs, the documented response of a harmless read).
   Method: [agent-verification.md](./agent-verification.md); what may be
   published and how: [publication-protocol.md](./publication-protocol.md).
2. **Evidence review** — a maintainer or contributor verifies every
   `supported`/`partial` claim against its evidence URL under the normal
   [evidence rules](./contributing.md#evidence-rules) and the decision rubrics
   in `data/fields.yaml`.

Promotion is then a `git mv data/candidates/<id>.yaml data/providers/<id>.yaml`
— the file itself does not change, and history preserves who submitted what.

## Failing M1

A failed M1 is published like any other run (transcript included) and shown in
the candidate row. It is data, not punishment: the candidate stays in the pool,
and anyone — including the vendor — can fix the docs or the service and open an
issue to request a rerun. Reruns follow the
[dispute rules](./publication-protocol.md).

## Account-less services (x402, fully public APIs)

Explicitly in scope — they are the most agent-native access model there is.
But map the checks honestly: account-shaped checks (`self_serve_signup`,
`api_key_self_serve`, `oauth_support`, `scoped_tokens`, `token_revocation`)
are `not_applicable` **with a note** for a service that has no accounts or
keys. Marking them `supported` because "no key is even needed" is inflation
and will be corrected in review.

## Demotion

An index entry can be moved back to the pool by PR when its service dies
(homepage/docs broken across two consecutive weekly probes) or when a disputed
run fails its rerun. `archived: true` remains the right call for services that
are gone for good.

## Grandfathering

The 76 entries indexed before the pool existed (2026-07-15) were
evidence-reviewed at inclusion time. They get M1 runs through the same sweep
as candidates, published the same way — the index converges on "everything
measured" from both directions.
