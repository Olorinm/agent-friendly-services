#!/usr/bin/env bash
set -uo pipefail
# M1 sweep: dry-fire ×REPS over every candidate-pool entry, or over the
# provider ids passed as arguments (works for index entries too — the
# grandfathered M1 sweep uses this same script).
#
# Results land in data/experiments/results/<id>/ (gitignored). Publication is
# a manual, reviewed step: docs/publication-protocol.md. The runner skips reps
# that already have a result file for today, so re-running is cheap.

cd "$(dirname "$0")/.."
REPS="${REPS:-3}"

ids=("$@")
if [ ${#ids[@]} -eq 0 ]; then
  shopt -s nullglob
  for f in data/candidates/*.yaml; do
    ids+=("$(basename "$f" .yaml)")
  done
  if [ ${#ids[@]} -eq 0 ]; then
    echo "candidate pool is empty — nothing to sweep"
    exit 0
  fi
fi

echo "M1 sweep over: ${ids[*]} (reps=$REPS)"
fail=0
for id in "${ids[@]}"; do
  echo "=== $id ==="
  npm run agent-verify --silent -- --provider="$id" --layer=dry-fire --reps="$REPS" || { echo "RUNNER ERROR for $id"; fail=1; }
done
echo "Sweep complete. Review data/experiments/results/ before publishing (docs/publication-protocol.md)."
exit "$fail"
