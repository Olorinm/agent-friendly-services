# Import Results (Neon DB `[SERVICE_SECRET]`)

Target tables are the two independent tables prepared by the controller:
`reject_case` and `accept_case`, each `book_id INTEGER PRIMARY KEY NOT NULL`,
`title TEXT NOT NULL`, initially containing only `100 / 已有书目`.

## Run 1 — error sample: `materials/batch-reject.csv` -> `reject_case`

Command:

```bash
PYTHONPATH=/home/node/service-tools/installed-tools \
python3 importer.py materials/batch-reject.csv --table reject_case
```

Outcome (exit 2, whole batch rejected):

```json
{
  "table": "reject_case",
  "file": "materials/batch-reject.csv",
  "rows_read": 3,
  "rows_inserted": 0,
  "committed": false,
  "error": {
    "type": "UniqueViolation",
    "pgcode": "23505",
    "diag": "duplicate key value violates unique constraint \"reject_case_pkey\"",
    "message": "duplicate key value violates unique constraint \"reject_case_pkey\""
  }
}
```

The file contains `book_id=100`, which collides with the existing row. The
insert of `101` was executed inside the transaction, then the database itself
raised the duplicate-primary-key error on `100`; the transaction was rolled
back and nothing from the file persisted.

## Run 2 — corrected sample: `materials/batch-corrected.csv` -> `accept_case`

Command:

```bash
PYTHONPATH=/home/node/service-tools/installed-tools \
python3 importer.py materials/batch-corrected.csv --table accept_case
```

Outcome (exit 0, all rows saved):

```json
{
  "table": "accept_case",
  "file": "materials/batch-corrected.csv",
  "rows_read": 3,
  "rows_inserted": 3,
  "committed": true,
  "error": null
}
```

## Final table contents (read-back for verification)

| table       | book_id | title        |
|-------------|---------|--------------|
| reject_case | 100     | 已有书目     |
| accept_case | 100     | 已有书目     |
| accept_case | 101     | 候选书目甲   |
| accept_case | 102     | 候选书目乙   |
| accept_case | 103     | 更正编号书目 |

- `reject_case` still holds only the original `100 / 已有书目`; no partial data
  (`101`, `102`) leaked in.
- `accept_case` holds the original `100` plus all three corrected rows
  (`101`, `102`, `103`); the original row is unchanged.
