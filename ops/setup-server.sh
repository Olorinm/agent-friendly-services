#!/usr/bin/env bash
set -euo pipefail
# One-shot setup for the AFS standard measurement server (Debian/Ubuntu).
# Run as a normal user with sudo rights. Safe to re-run.
#
# What this machine is: the pinned, clean environment that runs the
# agent-verification layers (docs/agent-verification.md) on a schedule —
# weekly M1 dry-fire sweep over the candidate pool, credentialed ladder runs
# when the maintainer provisions a category. Results stay on this machine
# (gitignored) until a human reviews and publishes them
# (docs/publication-protocol.md).

AFS_HOME="${AFS_HOME:-$HOME/afs}"
REPO_URL="${AFS_REPO_URL:-https://github.com/Olorinm/agent-friendly-services.git}"

echo "== packages =="
sudo apt-get update -y
sudo apt-get install -y git jq curl ca-certificates redis-tools

if ! command -v node >/dev/null 2>&1 || [ "$(node -v | sed 's/^v//' | cut -d. -f1)" -lt 20 ]; then
  echo "== node 20 (NodeSource) =="
  curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
  sudo apt-get install -y nodejs
fi

if ! command -v claude >/dev/null 2>&1; then
  echo "== claude CLI =="
  sudo npm install -g @anthropic-ai/claude-code
fi

echo "== repo =="
mkdir -p "$AFS_HOME" "$AFS_HOME/logs"
if [ -d "$AFS_HOME/repo/.git" ]; then
  git -C "$AFS_HOME/repo" pull --ff-only
else
  git clone "$REPO_URL" "$AFS_HOME/repo"
fi
(cd "$AFS_HOME/repo" && npm install --silent)

echo "== credentials skeleton =="
install -d -m 700 "$HOME/.afs" "$HOME/.afs/credentials"
if [ ! -f "$HOME/.afs/env" ]; then
  cat > "$HOME/.afs/env" <<'EOF'
# Filled by the maintainer; keep chmod 600. Sourced by the cron sweep.
ANTHROPIC_API_KEY=
# Optional override; default is ~/.afs/credentials
# AFS_CRED_DIR=
EOF
fi
chmod 600 "$HOME/.afs/env"

echo "== cron: weekly M1 sweep over the candidate pool (Mon 03:17 UTC) =="
CRON_LINE="17 3 * * 1 . \$HOME/.afs/env && export ANTHROPIC_API_KEY && cd $AFS_HOME/repo && git pull --ff-only >/dev/null && npm install --silent && bash scripts/sweep-candidates.sh >> $AFS_HOME/logs/sweep-\$(date +\%F).log 2>&1"
(crontab -l 2>/dev/null | grep -v 'sweep-candidates.sh' || true; echo "$CRON_LINE") | crontab -

echo
echo "Done. Remaining manual steps:"
echo "  1. Put the Anthropic API key (with a monthly spend cap) into ~/.afs/env"
echo "  2. Drop provider credentials into ~/.afs/credentials/ as <id>.curlrc /"
echo "     <id>.env / <id>.mcp.json / <id>.provision.yaml (chmod 600 each)"
echo "  3. Test: cd $AFS_HOME/repo && bash scripts/sweep-candidates.sh"
