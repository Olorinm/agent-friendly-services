# Publication protocol

Every run first lands in `data/experiments/results/<id>/` — local,
**gitignored**. Publication means a human copies a run's `.yaml` + `.md`
transcript into `data/experiments/published/<id>/` and commits. The generated
pages (README badges, 🏆, `generated/agent-runs.md`, the candidate-pool M1
column) build **only** from the published set. Nothing publishes
automatically.

## Before publishing anything

1. **Friction attribution** ([definitions](./agent-verification.md#friction-attribution)):
   every friction note is labeled provider / harness / model. A run whose
   failure was caused by the harness is invalid — it is rerun, never
   published as a provider result. Model-caused confusion is kept and
   labeled, and is never phrased as a provider defect.
2. **Credential hygiene**: grep the transcript for key fragments, tokens,
   and `Authorization` headers before it leaves the machine. The runner's
   prompts forbid printing credentials; verify anyway.

## Verified passes and M1 (dry-fire) results

Publishable after the checks above. Dry-fire runs use no credentials and
exercise only public documentation, so both passes and fails are publishable
— an M1 fail on a candidate is precisely the signal the pool exists to
surface.

## Negative real-task results (fail / blocked) — extra gate

1. **Terms check**: a good-faith read of the provider's public terms for
   clauses restricting publication of test/benchmark results
   (DeWitt-style). Record the check (URL + date) in the run YAML under
   `terms_check`. If such a clause exists, publish the row as
   **"results withheld by provider terms"** — that fact itself is published,
   the metrics are not.
2. **Right of response**: publishing a negative result opens (or links) a
   tracking issue mentioning the provider's public repo/handle where one
   exists. Disputes get a rerun — see below.
3. **Wording**: observed facts only ("the documented example returns 404"),
   no adjectives, no advice dressed as findings.

## Disputes and reruns

Anyone — provider or bystander — can dispute a published run by opening an
issue. The disputed run is rerun within 7 days, ×3 reps, same pinned
environment and model unless the pin itself was the dispute. The newest
majority result supersedes the old one on the generated pages; superseded
runs stay in git history. Fixing your docs and asking for a rerun is the
intended happy path.

## Expiry and repins

- Published results stop counting after **180 days** (`generate.ts`); stale
  rows disappear from pages automatically. Re-runs refresh them.
- Changing the pinned model or agent version starts a new wave; runs from
  different pins are never averaged together (the `Model` column keeps every
  row honest).

## Who may publish

Maintainers, by commit. Community members propose publication by PR-ing the
run files with the checklist above filled in the PR body.
