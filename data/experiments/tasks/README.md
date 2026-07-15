# Real-task definitions — milestone ladders

One file per category, holding that category's **milestone ladder**. Milestones
pin the real-task scenarios so runs are comparable within a category and the
verdict never depends on the agent's mid-run judgment about what "the task"
means. See `docs/agent-verification.md` for the method.

Top-level fields:

- `provisioning` — the minimum a human must supply before any real run. This
  list is itself a published friction fact.
- `milestones` — the ladder, in climbing order (see below).
- `reset_commands` — per-provider commands the runner executes **before every
  rep** to wipe `afs-*` artifacts, so no rep can imitate visible prior work.
- `cleanup` — how created state is removed. Test modes / free tiers are
  mandatory where they exist.
- `provider_overrides` — provider pins that apply to every milestone (e.g.
  "data plane only").

Each milestone:

- `id` — `core` (the category's basic realistic task; all badges and the route
  comparison pin to it), `lifecycle` (set up → use → evolve → tear down →
  verifiable receipt), `billing` (machine-readable usage/billing reality).
- `scenario` — the realistic user request given to the agent, with `{{NONCE}}`
  replaced per run by the runner (a unique string, so independent verification
  can match exactly).
- `verification` — how the runner independently confirms success. `method:
  state` = fetch the created state itself; `re-execute` = run the runner's own
  pinned query. `expect: nonce` = output must contain the run's nonce;
  `expect: success` = the command must succeed with a non-empty numeric
  response.
- `verify_commands` — per-provider command templates the runner executes for
  that confirmation (placeholders: `{{NONCE}}`, `{{CURLRC}}`,
  `{{provision.*}}` from the local `<id>.provision.yaml`). Public on purpose:
  they define what counts as a pass. Added per provider as it gets its first
  provisioned run — a milestone without a `verify_commands` entry for a
  provider refuses to run. Secret-bearing values (e.g. a Redis URI with a
  password) live only in `verify_commands`/`reset_commands` placeholders like
  `{{provision.uri}}` — never in `scenario`, which goes into the agent's
  prompt.
- `provider_overrides` — pinned targets where the category scenario is
  ambiguous for a specific provider (key-value stores, class-naming rules,
  index-level lifecycles …).

Tasks are route-agnostic: the same scenario, nonce and verification run over
every access route (HTTP baseline / official CLI / official MCP — see
`docs/agent-verification.md`). Route provisioning (curl config file, CLI env
vars, MCP config) is harness environment, not task data.

Ladder semantics: `--ladder` climbs milestones in order and stops at the first
one without a majority pass across reps; `--milestone=<id>` runs one rung.

Task definitions are data: challenge them by PR like any other fact here.
