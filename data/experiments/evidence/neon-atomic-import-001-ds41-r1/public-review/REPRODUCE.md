# Reproduce this two-case observation

Download evidence files under their original names; put the two CSVs in `materials/`. Use a **new empty authorized database**, never an existing application database. Run `initial-state.sql` once with a trusted database client before invoking the importer. Keep credentials outside published source.

Neon: an existing authorized unclaimed Claimable parent, one new logical database, issued pooled connection. Published observation used PostgreSQL17.11 and an existing parent with shared100MB/1GB/72h limits; future resources/versions may differ.

```sh
python3 -m pip install --target ./deps --index-url https://pypi.tuna.tsinghua.edu.cn/simple psycopg2-binary==2.9.13
# Set NEW_DATABASE_URL privately for your new PostgreSQL database.
PYTHONPATH=./deps python3 importer.py materials/batch-reject.csv --table reject_case
PYTHONPATH=./deps python3 importer.py materials/batch-corrected.csv --table accept_case
```

The error run is expected to return a nonzero importer exit (Turso1/Neon2) and a real duplicate-key error. The corrected run returns0. Independently read both tables and complete schema after processes exit: reject_case must contain only100/已有书目; accept_case must contain100/101/102/103 and the exact CSV titles. Review the recorded source/transaction/error path as well as table state; do not rerun for a better score or delete rows to imitate rollback. The original trial kept full tool records, isolated graders and frozen peer outputs.

The fixture and captured importer reproduce functional operations; generating the same code with a stochastic model is not guaranteed. Model:DeepSeekV4.1Flash high,OpenCode1.18.35; task/sourcecommit05ed74c and runner-sourcepreflight in verification.json; actual budgets, startup/retaineddependencies and versions there. End-to-end Agent time includes research, installation and corrections and is not SQL latency. Fees are snapshot-price model estimates or separately sourced servicefees, not provider invoice. No crash/concurrency/generalACID certification.
