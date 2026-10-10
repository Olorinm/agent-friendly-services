#!/usr/bin/env node
// Reusable atomic CSV book importer for Turso/libSQL.
// Usage: node import-books.mjs <file.csv> <reject_case|accept_case>
//
// Reads a UTF-8 CSV whose first line is "book_id,title" and inserts every data
// row into the authorized target table inside ONE database transaction.
// If any row violates a constraint (e.g. duplicate primary key), the whole
// transaction is rolled back, so no partial batch is ever committed.
//
// Credentials are NOT stored in this file. The SQL token is read from the
// private credentials file (default /home/node/service-tools/credentials.json)
// and the database URL from the service config file
// (default /home/node/service-tools/service-config.json). Both can be
// overridden with TURSO_DB_TOKEN / TURSO_DB_URL env vars.

import { readFileSync } from "node:fs";
import { createClient } from "@libsql/client";

const CREDENTIALS_PATH =
  process.env.TURSO_CREDENTIALS_PATH ||
  "/home/node/service-tools/credentials.json";
const CONFIG_PATH =
  process.env.TURSO_SERVICE_CONFIG_PATH ||
  "/home/node/service-tools/service-config.json";

const ALLOWED_TABLES = ["reject_case", "accept_case"];

function fail(message) {
  console.error(JSON.stringify({ ok: false, error: message }, null, 2));
  process.exit(2);
}

function resolveConnection() {
  let token = process.env.TURSO_DB_TOKEN;
  let url = process.env.TURSO_DB_URL;

  if (!token) {
    try {
      token = JSON.parse(readFileSync(CREDENTIALS_PATH, "utf8")).TURSO_DB_TOKEN;
    } catch (err) {
      fail(`cannot read TURSO_DB_TOKEN from ${CREDENTIALS_PATH}: ${err.message}`);
    }
  }
  if (!url) {
    try {
      url = JSON.parse(readFileSync(CONFIG_PATH, "utf8")).database.libsql_url;
    } catch (err) {
      fail(`cannot read database URL from ${CONFIG_PATH}: ${err.message}`);
    }
  }
  if (!token) fail("empty TURSO_DB_TOKEN");
  if (!url) fail("empty database URL");
  return { url, token };
}

// Minimal RFC-4180-ish CSV parse (handles quoted fields and escaped quotes).
function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = "";
  let inQuotes = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (inQuotes) {
      if (c === '"') {
        if (text[i + 1] === '"') {
          field += '"';
          i++;
        } else {
          inQuotes = false;
        }
      } else {
        field += c;
      }
    } else if (c === '"') {
      inQuotes = true;
    } else if (c === ",") {
      row.push(field);
      field = "";
    } else if (c === "\n") {
      row.push(field);
      rows.push(row);
      row = [];
      field = "";
    } else if (c === "\r") {
      // skip; handled by \n
    } else {
      field += c;
    }
  }
  if (field.length > 0 || row.length > 0) {
    row.push(field);
    rows.push(row);
  }
  return rows.filter((r) => !(r.length === 1 && r[0] === ""));
}

async function main() {
  const [csvPath, targetTable] = process.argv.slice(2);
  if (!csvPath || !targetTable) {
    fail("usage: node import-books.mjs <file.csv> <reject_case|accept_case>");
  }
  if (!ALLOWED_TABLES.includes(targetTable)) {
    fail(`target table must be one of ${ALLOWED_TABLES.join(", ")}`);
  }

  let text;
  try {
    text = readFileSync(csvPath, "utf8");
  } catch (err) {
    fail(`cannot read CSV ${csvPath}: ${err.message}`);
  }

  const rows = parseCsv(text);
  if (rows.length === 0) fail("empty CSV");
  const header = rows[0].map((h) => h.trim());
  const idIdx = header.indexOf("book_id");
  const titleIdx = header.indexOf("title");
  if (idIdx === -1 || titleIdx === -1) {
    fail(`CSV header must contain book_id and title, got: ${header.join(",")}`);
  }

  const records = rows.slice(1).map((r, n) => {
    const bookId = Number((r[idIdx] ?? "").trim());
    const title = (r[titleIdx] ?? "").trim();
    if (!Number.isInteger(bookId)) {
      fail(`row ${n + 2}: book_id is not an integer: ${r[idIdx]}`);
    }
    if (title === "") fail(`row ${n + 2}: empty title`);
    return { bookId, title };
  });

  const { url, token } = resolveConnection();
  const db = createClient({ url, authToken: token });

  const summary = {
    target_table: targetTable,
    csv: csvPath,
    rows_in_file: records.length,
    book_ids: records.map((r) => r.bookId),
    committed: false,
    db_error: null,
  };

  await db
    .transaction("write")
    .then(async (tx) => {
      try {
        for (const rec of records) {
          // Real database insert: duplicate/invalid keys must be rejected by
          // the database itself, never skipped or pre-filtered locally.
          await tx.execute({
            sql: `INSERT INTO ${targetTable} (book_id, title) VALUES (?, ?)`,
            args: [rec.bookId, rec.title],
          });
        }
        await tx.commit();
        summary.committed = true;
      } catch (err) {
        try {
          await tx.rollback();
        } catch (rollbackErr) {
          summary.rollback_error = rollbackErr.message;
        }
        summary.db_error = {
          code: err.code ?? null,
          message: err.message,
        };
      }
    })
    .catch((err) => {
      summary.db_error = { code: err.code ?? null, message: err.message };
    });

  db.close();
  console.log(JSON.stringify(summary, null, 2));
  process.exit(summary.committed ? 0 : 1);
}

main().catch((err) => {
  fail(`unexpected error: ${err.stack || err.message}`);
});
