# Agent verification (experimental)

Everything else in this index is a **documented fact** with an official evidence
URL. This track is different: we run an actual AI agent against the provider and
record whether it completed a canonical task **without any human intervention**.
That is the closest thing to a direct measurement of agent-friendliness — and
because it is an *experiment result*, not a timeless fact, it is labeled and
stored differently from checks.

## What is measured

**The zero-touch first call:** starting from the provider's official docs and
given nothing but a valid API key in an environment variable, can an agent make
its first successful authenticated API call — choosing the right endpoint,
auth scheme, and format from documentation alone, with no human answering
questions?

This deliberately measures the **post-credential** path. Account signup is out
of scope: CAPTCHA, phone verification and card checks exist specifically to
require a human, and we do not attempt or automate bypassing them. The signup
gates themselves are recorded as documented facts (tier T0 below), not tested.

## Tiers

| Tier | Credentials | What the agent does | What it produces |
| --- | --- | --- | --- |
| **T0** — docs recon | none | Reads official docs only; maps the path from "new user" to "first successful call"; lists every step that requires a human, with evidence URLs; writes the exact first-call command | Human-gate list (feeds normal checks), candidate command for T1 |
| **T1** — live run | API key in env | Must achieve a documented 2xx authenticated call using only official docs; no human available | Pass/fail → the **Agent-verified** badge |

Hard rules baked into the task prompt for both tiers:

- Never create accounts, never attempt signup, never try to get past any
  human-verification mechanism.
- No human is available. If information is missing, the run records `unknown`
  or fails — it never guesses.

## Honest labeling

A run result is only meaningful with its context, so every recorded result
carries: the **model** that ran it, the **date**, the **tier**, and a link to
the full **transcript** committed to this repo. The badge renders as
`Agent-verified (<model>, <YYYY-MM>)` — never as a bare checkmark. Results
older than the standard staleness window (180 days) stop counting.

A T1 failure is recorded too, with the failure point (wrong auth scheme in
docs, undocumented required header, …). Failures are arguably the most useful
signal this index can give a provider.

## Storage

- `data/experiments/first-call/<provider>.yaml` — latest result per provider
  (result, tier, model, date, steps, transcript path, notes).
- `data/experiments/first-call/transcripts/<provider>-<date>.md` — the run
  transcript (evidence).

`generate.ts` will surface T1 passes as an **Agent-verified** badge once the
first batch of keyed runs lands. Experiments never override documented checks;
they sit alongside them.

## Running

```bash
# T0 (no credentials needed):
npm run agent-verify -- --provider=groq

# T1 (key required; never commit keys):
AFS_KEY_GROQ=... npm run agent-verify -- --provider=groq --tier=t1
```

The runner (`scripts/agent-verify.ts`) builds a standardized prompt from the
provider's entry in the dataset and executes it headlessly via `claude -p`
with a capped number of turns. Same prompt for every provider — comparability
is the point. Cadence: manual for now; monthly once keys are provisioned
(weekly would be needless spend — this changes slowly).

## Why this is not a score

One badge, mechanically earned, transcript attached. No ranking, no weighting,
no aggregate number — a provider either completed the canonical task under the
stated conditions or it didn't, and you can read the transcript to see why.
