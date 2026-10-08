# Atomic CSV Book Importer

`importer.py` reads a UTF-8 CSV (`book_id,title` header) and inserts every row
into one authorised table inside a **single database transaction**. Any error
(e.g. a duplicate primary key) rolls the entire batch back, so a half-imported
batch is never left behind.

## Usage

```bash
PYTHONPATH=/home/node/service-tools/installed-tools \
python3 importer.py <path-to.csv> --table <reject_case|accept_case>
```

- `<path-to.csv>`: path to the UTF-8 CSV file to import.
- `--table`: one of the two authorised target tables (`reject_case`, `accept_case`).
- Exit code `0` = whole batch committed; `2` = batch rejected and rolled back.
- Output is JSON: rows read, rows inserted, committed flag, and the real
  database error when rejected.

## Credentials

The DSN is **not** stored in the importer. It is read from the
`NEW_DATABASE_URL` environment variable, or from the private credentials file
`/home/node/service-tools/credentials.json` when that variable is unset
(override the path with `BOOKS_CREDENTIALS_FILE`).

## Design notes

- Rows are read from the actual file; no expected final state is hardcoded.
- Exactly one `INSERT` per data row, wrapped in one implicit transaction
  (`with conn:` commits on success / rolls back on error).
- No `UPDATE`/`DELETE`/`REPLACE`, no DDL, no pre-screening that would hide the
  duplicate from the database. The conflict is raised by the database itself.
