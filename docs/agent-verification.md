# Agent verification (experimental)

Everything else in this index is a **documented fact** with an official evidence
URL. This track is different: we run an actual AI agent against the provider and
record whether it completed a realistic task **without any human intervention**.
That is the closest thing to a direct measurement of agent-friendliness — and
because it is an *experiment result*, not a timeless fact, it is labeled and
stored differently from checks.

## The three layers

| Layer | Credentials | What the agent does | What it produces |
| --- | --- | --- | --- |
| **Recon** (`t0`) | none | Reads official docs only; maps the path from "new user" to "first successful call"; lists every human gate with evidence URLs | Human-gate list, candidate first-call command |
| **Dry-fire** | none | Builds the canonical first call from docs alone and EXECUTES it with an obviously-fake credential. Pass = the provider's documented auth-failure (401/403 with documented error shape) from the correct endpoint — proving endpoint, method, headers and request shape were derivable from docs | Verdict + friction facts; scales to every provider with zero provisioning |
| **Real task** | provisioned | Completes a category-specific real user scenario end-to-end (see task definitions below) | Verdict + friction facts + cost — the strongest signal, only where credentials are provisioned |

The layers are complementary, not competing: dry-fire covers the whole index
cheaply; real-task runs light up provider by provider as credentials are
provisioned.

## Standard measurement environment

A run is only comparable if the environment is pinned. Every published result
records all of the following, and runs with a different environment are
different experiments:

- **Machine**: a fresh environment with no prior state (no cached logins, no
  provider SDKs preinstalled, no shell history).
- **Agent + model**: pinned and recorded (e.g. Claude Code headless, model id).
- **Tool surface**: pinned per access route (see below). The baseline route is
  web fetch/search + `curl` via shell — no provider SDKs, no provider CLIs —
  so the task must be solvable from HTTP + docs alone.
- **Credentials as files, never env vars or prompt text**: each credential is
  provisioned as a curl config file (`curl -K <file>`), so the secret never
  appears in command text, transcripts, or the prompt, and restrictive shell
  permission matchers cannot block variable expansion. (Calibration found that
  env-var injection can fail *inside the harness* and the failure then
  masquerades as provider friction.)
- **Turn cap**: 40 agent turns (calibration showed 25 is too tight for
  higher-friction providers).
- **Repetitions**: 3 independent runs per provider per task. The published
  verdict is the majority; a split verdict is **recorded as a finding**, not
  averaged away — disagreement usually means the provider's docs or API
  structure genuinely confuse agents (e.g. multiple API planes with only one
  documented).
- **Harness pre-flight**: before a batch, the harness runs a known-good task
  end-to-end to prove the environment itself adds no friction.

## Access routes

A real task can be run over up to three routes — same scenario, same nonce,
same independent verification; only the way the agent reaches the provider
changes:

| Route | Available for | Tool surface | Credential delivery |
| --- | --- | --- | --- |
| **HTTP + docs** (baseline) | every provider | web fetch/search + `curl` | curl config file (`-K`) |
| **Official CLI** | providers shipping one | web fetch/search + the CLI only | the CLI's own native mechanism (env var / config file), never expanded in command text |
| **Official MCP** | providers shipping one | the MCP server's tools only (no shell) | harness-side MCP config — the agent never touches the secret at all |

The baseline keeps every provider comparable; the CLI and MCP routes measure
whether the provider's agent-facing investments actually pay off. The
route-vs-baseline delta (turns, wall time, cost, wrong attempts, docs
consulted) is itself a published fact — calibration on one provider showed the
official MCP server completing the task in 4 turns with zero documentation
lookups where the HTTP baseline needed 8–13 turns, and that the MCP route is
structurally safer because the credential never enters the agent's
environment. An MCP/CLI route that *fails* where the baseline passes is
recorded with the failure point — that is exactly the feedback those tools'
maintainers need. If the MCP/CLI tools are insufficient for part of the task,
the agent must report that as the failure reason, not work around it via other
means.

## Task definitions

Real-task scenarios live in `data/experiments/tasks/<category>.yaml` — one
realistic user scenario per category, so results are comparable **within** a
category (we never compare across categories; the index does not rank).

Each task file pins, as reviewable data:

- **scenario** — what a real user would ask an agent to do;
- **provisioning** — the minimum a human must supply up front (a key, a test
  store, a bot already in a channel …). This manifest is itself a core
  friction fact: the more a human must pre-provide, the less autonomous the
  agent can be;
- **verification** — how the runner *independently* confirms success;
- **cleanup** — how created state is removed (test modes and free tiers are
  mandatory where they exist).

Task definitions are data, so they are PR-challengeable like any other fact in
this repo. Where a uniform category task is ambiguous for a specific provider
(e.g. a provider with separate management and data planes), the target is
pinned per provider in the task file rather than left to the agent's judgment
mid-run — calibration showed verdicts flip on exactly this ambiguity.

## Independent verification

The runner never trusts the agent's self-report. After the agent finishes:

- **Stateful tasks** (created an issue, a record, a deployment): the runner
  fetches the created resource itself through the provider's API and checks it
  matches (exact title/nonce), then performs cleanup.
- **Stateless tasks** (an inference call, a search): the runner re-executes the
  agent's final command and checks the response for the expected content.

Only an independently verified pass is a pass.

## Friction attribution

The verdict alone has little discrimination (most major providers pass);
the signal is in the friction: turns used, wrong attempts, wall time, cost,
and the agent's friction notes. Before publishing, every friction note is
attributed to one of:

- **provider** — the thing this index measures (undocumented header, wrong
  example in docs, auth scheme mismatch, only-dashboard flows …);
- **harness** — our environment got in the way (permission matcher, sandbox
  limits); these invalidate the run rather than count against the provider;
- **model** — the agent misread or hallucinated despite correct docs; kept,
  labeled, because "today's models get confused here" is real information for
  providers, but it is never phrased as a provider defect.

## Honest labeling

Every recorded result carries: the **model**, the **agent harness**, the
**date**, the **layer**, the run **metrics** (turns, wall time, cost, wrong
attempts), and a link to the full **transcript** committed to this repo. The
badge renders as `Agent-verified (<model>, <YYYY-MM>)` — never a bare
checkmark. Results older than 180 days stop counting.

Failures are recorded too, with the failure point — arguably the most useful
signal this index can give a provider. Hard rules baked into every prompt:
never create accounts, never attempt signup, never try to get past any
human-verification mechanism (CAPTCHA, phone, card, KYC); official sources
only; no human is available — say "unknown" rather than guess; mutate only the
designated test resources.

## Storage

- `data/experiments/tasks/<category>.yaml` — pinned task definitions.
- `data/experiments/first-call/<provider>.yaml` — latest result per provider.
- `data/experiments/first-call/transcripts/<provider>-<date>.md` — evidence.

`generate.ts` will surface verified real-task passes as an **Agent-verified**
badge once the first provisioned batch lands. Experiments never override
documented checks; they sit alongside them.

## Running

```bash
# Recon (no credentials needed):
npm run agent-verify -- --provider=groq

# Real task (credential file required; never commit credentials):
npm run agent-verify -- --provider=github --task=real
```

The runner (`scripts/agent-verify.ts`) builds a standardized prompt from the
provider's dataset entry plus the category task file and executes it headlessly
via `claude -p` with the pinned environment above. Cadence: manual for now;
monthly once provisioned (weekly would be needless spend — this changes
slowly).

## Why this is not a score

Verdict + metrics + attributed friction facts + transcript. No ranking, no
weighting, no aggregate number — a provider either completed the pinned task
under the pinned conditions or it didn't, and you can read the transcript to
see why.
