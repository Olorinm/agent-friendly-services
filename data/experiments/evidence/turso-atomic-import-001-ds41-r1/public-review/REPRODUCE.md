# Reproduce this two-case observation

Download evidence files under their original names; put the two CSVs in `materials/`. Use a **new empty authorized database**, never an existing application database. Run `initial-state.sql` once with a trusted database client before invoking the importer. Keep credentials outside published source.

Turso: same libSQL cloud engine, existing starter account, official client pinned by captured package-lock.

```sh
npm ci
# Set TURSO_DB_URL and TURSO_DB_TOKEN privately for your new libSQL database.
node import-books.mjs materials/batch-reject.csv reject_case
node import-books.mjs materials/batch-corrected.csv accept_case
```

The error run is expected to return a nonzero importer exit (Turso1/Neon2) and a real duplicate-key error. The corrected run returns0. Independently read both tables and complete schema after processes exit: reject_case must contain only100/已有书目; accept_case must contain100/101/102/103 and the exact CSV titles. Review the recorded source/transaction/error path as well as table state; do not rerun for a better score or delete rows to imitate rollback. The original trial kept full tool records, isolated graders and frozen peer outputs.

The fixture and captured importer reproduce functional operations; generating the same code with a stochastic model is not guaranteed. Model:DeepSeekV4.1Flash high,OpenCode1.18.35; task/sourcecommit05ed74c and runner-sourcepreflight in verification.json; actual budgets, startup/retaineddependencies and versions there. End-to-end Agent time includes research, installation and corrections and is not SQL latency. Fees are snapshot-price model estimates or separately sourced servicefees, not provider invoice. No crash/concurrency/generalACID certification.
