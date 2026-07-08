# Real-task definitions

One file per category. These pin the real-task scenario so runs are comparable
within a category and the verdict never depends on the agent's mid-run judgment
about what "the task" means. See `docs/agent-verification.md` for the method.

Fields:

- `scenario` — the realistic user request given to the agent, with `{{NONCE}}`
  replaced per run by the runner (a unique string, so independent verification
  can match exactly).
- `provisioning` — the minimum a human must supply before the run. This list is
  itself a published friction fact.
- `verification` — how the runner independently confirms success (`state` =
  fetch the created resource itself; `re-execute` = rerun the agent's final
  command and check the response).
- `verify_commands` — per-provider command templates the runner executes for
  that confirmation (placeholders: `{{NONCE}}`, `{{CURLRC}}`,
  `{{provision.*}}` from the local `<id>.provision.yaml`). Public on purpose:
  they define what counts as a pass. Added per provider as it gets its first
  provisioned run — not spec'd ahead of testing.
- `cleanup` — how created state is removed. Test modes / free tiers are
  mandatory where they exist.
- `provider_overrides` — pinned targets where the category scenario is
  ambiguous for a specific provider.

Tasks are route-agnostic: the same scenario, nonce and verification run over
every access route (HTTP baseline / official CLI / official MCP — see
`docs/agent-verification.md`). Route provisioning (curl config file, CLI env
vars, MCP config) is harness environment, not task data.

Task definitions are data: challenge them by PR like any other fact here.
