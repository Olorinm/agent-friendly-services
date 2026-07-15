# Standard measurement server

The pinned, clean machine that runs the agent-verification layers
([method](../docs/agent-verification.md)) on a schedule. Everything the agent
measures should reflect the provider — never this machine — so the machine is
boring on purpose: a fresh small VPS, pinned toolchain, per-rep fresh working
directories (the runner handles that), and credentials that never enter the
repo.

## What the maintainer provides

1. A Debian/Ubuntu VPS (2 vCPU / 4 GB RAM is plenty) with SSH access.
2. An Anthropic API key **with a monthly spend cap**, placed in `~/.afs/env`.
3. Per-provider credentials, as they get provisioned, in `~/.afs/credentials/`
   (`<id>.curlrc`, `<id>.env`, `<id>.mcp.json`, `<id>.provision.yaml`,
   chmod 600 — see the runner header in `scripts/agent-verify.ts`).

## Setup

```bash
bash ops/setup-server.sh
```

Idempotent. Installs git/jq/redis-cli, Node 20, the claude CLI, clones the
repo to `~/afs/repo`, creates the credentials skeleton, and registers the
weekly cron.

## What runs when

| When | What | Cost ballpark |
| --- | --- | --- |
| Mon 03:17 UTC weekly | `scripts/sweep-candidates.sh` — M1 dry-fire ×3 over the candidate pool | ≈ $1 per candidate |
| manual | grandfathered M1 sweep over index entries: `bash scripts/sweep-candidates.sh <id> <id> ...` | ≈ $80 for all 76 |
| manual, per provisioned category | ladder runs: `npm run agent-verify -- --provider=<id> --layer=real --ladder --reps=3` (± `--route=cli/mcp`) | ≈ $1–5 per provider·route |

## Where results go

`data/experiments/results/<id>/` on this machine — **gitignored, never pushed
automatically**. A human reviews each batch (friction attribution, credential
hygiene) and publishes the reviewable subset to `data/experiments/published/`
per the [publication protocol](../docs/publication-protocol.md). The generated
pages update from the published set only.
