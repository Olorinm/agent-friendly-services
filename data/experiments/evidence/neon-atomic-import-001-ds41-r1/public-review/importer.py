#!/usr/bin/env python3
"""Atomic CSV batch importer for the personal book catalogue.

Reads a UTF-8 CSV with header ``book_id,title`` and inserts every data row
into one authorised target table inside a single database transaction.
If any row fails (e.g. duplicate primary key) the whole batch is rolled
back, so no partial batch is ever left behind.

The database DSN is read from the ``NEW_DATABASE_URL`` environment variable,
or from the private credentials file when that variable is unset.  Secrets
are never stored in this file.
"""

import argparse
import csv
import json
import os
import sys

import psycopg2
from psycopg2 import sql

ALLOWED_TABLES = ("reject_case", "accept_case")
CREDENTIALS_FILE = os.environ.get(
    "BOOKS_CREDENTIALS_FILE", "/home/node/service-tools/credentials.json"
)
EXPECTED_COLUMNS = ["book_id", "title"]


def load_dsn():
    dsn = os.environ.get("NEW_DATABASE_URL")
    if dsn:
        return dsn
    with open(CREDENTIALS_FILE, encoding="utf-8") as handle:
        return json.load(handle)["NEW_DATABASE_URL"]


def read_rows(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(
                "unexpected CSV header %r, expected %r"
                % (reader.fieldnames, EXPECTED_COLUMNS)
            )
        for line_no, record in enumerate(reader, start=2):
            rows.append((int(record["book_id"]), record["title"]))
    if not rows:
        raise ValueError("no data rows in %s" % path)
    return rows


def import_file(dsn, table, path):
    """Insert all rows of ``path`` into ``table`` atomically.

    Returns a result dict.  On any database error the transaction is rolled
    back and ``committed`` is False.
    """
    rows = read_rows(path)
    conn = psycopg2.connect(dsn)
    try:
        with conn:  # opens a transaction, COMMIT on success / ROLLBACK on error
            with conn.cursor() as cur:
                insert = sql.SQL(
                    "INSERT INTO {tbl} (book_id, title) VALUES (%s, %s)"
                ).format(tbl=sql.Identifier(table))
                for book_id, title in rows:
                    cur.execute(insert, (book_id, title))
        return {
            "table": table,
            "file": path,
            "rows_read": len(rows),
            "rows_inserted": len(rows),
            "committed": True,
            "error": None,
        }
    except Exception as exc:  # noqa: BLE001 - report the real database error
        return {
            "table": table,
            "file": path,
            "rows_read": len(rows),
            "rows_inserted": 0,
            "committed": False,
            "error": {
                "type": type(exc).__name__,
                "pgcode": getattr(exc, "pgcode", None),
                "diag": getattr(getattr(exc, "diag", None), "message_primary", None),
                "message": str(exc).strip().splitlines()[0] if str(exc).strip() else "",
            },
        }
    finally:
        conn.close()


def main(argv=None):
    parser = argparse.ArgumentParser(description="Atomic CSV book importer")
    parser.add_argument("csv_path", help="path to UTF-8 CSV (book_id,title)")
    parser.add_argument(
        "--table",
        required=True,
        choices=ALLOWED_TABLES,
        help="authorised target table",
    )
    args = parser.parse_args(argv)

    result = import_file(load_dsn(), args.table, args.csv_path)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["committed"] else 2


if __name__ == "__main__":
    sys.exit(main())
