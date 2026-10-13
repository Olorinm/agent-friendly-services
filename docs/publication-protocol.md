# Publication protocol

The current [task workflow](../data/experiments/AGENTS.md) stages independently reviewed records in `evaluations/` and selected evidence in `evidence/`; local generated views include them for review. Staging, generation and source audits do not authorize external publication or messages to vendors. The `published/`, badge and dispute rules under the legacy heading below describe the historical pipeline, not the current task workflow.

## Current task workflow

Apply the [independent grading rules](../scripts/roles/grading/AGENTS.md#证据充分性与来源声明) frozen for each session. The revised evidence and source-claim rules apply only to new sessions that explicitly freeze the revised instructions. A complete, traceable field projection from a real call can support the required facts without a saved full HTTP body. Check the actual request, parameters, parsing and output; summaries, printed constants and synthetic answers are not service evidence. Identify which specific claim an omission or truncation prevents verifying. Proven errors and insufficient materials remain distinct.

Citing an abstract supplied or indexed by a service differs from claiming an additional publisher visit, a word-for-word comparison or independently verified identical text. Preserve that difference in claim strength. Do not add a publisher request when the user did not require one, infer disagreement from missing comparison evidence, or use peer votes to supply a source. Apply the same evidence boundary to comparable claims.

Keep original assessments and frozen inputs. Resolve a historical dispute through an explicit, separately linked source audit or clarification that records source hashes, the disputed claims, the explanation and its scope. It supplements the original assessment; it does not silently replace the verdict or retroactively apply new instructions. Changing these documents does not release an existing publication hold. The controller must document how the particular source or interpretation issue was resolved before releasing it. Until then, defer affected numerical comparisons or disclose the unresolved issue beside the preserved grades; missing or invalid evidence must not be presented as a business failure.

If a dispute needs a new trial, obtain the required authorization and freeze its task, inputs and conditions as a new session, recording any changes. Independently assess its own evidence and retain the earlier record. A majority of reruns does not rewrite an earlier verdict. Source audits are targeted follow-ups, not an automatic second grading stage.

Select only the minimum sanitized public evidence and review the actual copies for private content. A hold on publishing an evidence file does not by itself change a supported task outcome. Publication follows the user's authorization; sending a message to a vendor or another person requires explicit user instructions and is not automatically authorized by this protocol.

## Legacy publication rules (historical description)

The following rules retain the earlier pipeline's publication policy for context. Its transcript publication, automatic rerun, majority-supersession and right-of-response provisions are not instructions for current task runs or permission to contact a vendor.

Every run first lands in `data/experiments/results/<id>/` — local,
**gitignored**. Publication means a human copies a run's `.yaml` + `.md`
transcript into `data/experiments/published/<id>/` and commits. The generated
pages (README badges, 🏆, `generated/agent-runs.md`, the candidate-pool M1
column) build **only** from the published set. Nothing publishes
automatically.

### Before publishing anything

1. **Friction attribution** ([definitions](./agent-verification.md#friction-attribution)):
   every friction note is labeled provider / harness / model. A run whose
   failure was caused by the harness is invalid — it is rerun, never
   published as a provider result. Model-caused confusion is kept and
   labeled, and is never phrased as a provider defect.
2. **Credential hygiene**: grep the transcript for key fragments, tokens,
   and `Authorization` headers before it leaves the machine. The runner's
   prompts forbid printing credentials; verify anyway.

### Verified passes and M1 (dry-fire) results

Publishable after the checks above. Dry-fire runs use no credentials and
exercise only public documentation, so both passes and fails are publishable
— an M1 fail on a candidate is precisely the signal the pool exists to
surface.

### Negative real-task results (fail / blocked) — extra gate

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

### Disputes and reruns

The legacy policy allowed anyone — provider or bystander — to dispute a
published run by opening an issue. It called for a rerun within 7 days, ×3
reps, with the same pinned environment and model unless the pin itself was
the dispute. The newest majority result then superseded the old one on
generated pages; superseded runs stayed in git history. This historical
rule does not govern current task disputes, whose source-audit and
preservation rules are described above.

### Expiry and repins

- Published results stop counting after **180 days** (`generate.ts`); stale
  rows disappear from pages automatically. Re-runs refresh them.
- Changing the pinned model or agent version starts a new wave; runs from
  different pins are never averaged together (the `Model` column keeps every
  row honest).

### Who may publish

Maintainers, by commit. Community members propose publication by PR-ing the
run files with the checklist above filled in the PR body.
