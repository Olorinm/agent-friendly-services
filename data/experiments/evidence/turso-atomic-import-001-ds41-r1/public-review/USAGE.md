# 书目批量导入器（Turso/libSQL 原子导入）

## 文件
- `import-books.mjs` — 可复用导入器（Node ESM，依赖 `@libsql/client`）
- 凭据不写在导入器里：SQL token 读取私有文件 `/home/node/service-tools/credentials.json`；
  数据库 URL 读取 `/home/node/service-tools/service-config.json`（可用环境变量
  `TURSO_CREDENTIALS_PATH` / `TURSO_DB_TOKEN` / `TURSO_DB_URL` 覆盖）。

## 用法
```bash
npm install @libsql/client          # 首次
node import-books.mjs <file.csv> <reject_case|accept_case>
```
- CSV 首行必须是 `book_id,title`；每一行都实际发给数据库，不做重复预检。
- 只接受 `reject_case` / `accept_case` 两个授权目标表，避免误写其他表。
- 整批放在一个数据库事务里：全部成功才 `COMMIT`；任意一行被数据库拒绝
  （如重复主键）就 `ROLLBACK`，绝不留下半批数据，也不忽略/替换冲突记录。
- 退出码：0 = 整批已提交；1 = 整批被拒绝（stderr/stdout 输出 JSON 结果）。

## 两次实测结果
1. 错误样本 → `reject_case`
```bash
node import-books.mjs materials/batch-reject.csv reject_case   # 退出码 1
```
```json
{ "target_table": "reject_case", "rows_in_file": 3, "book_ids": [101,100,102],
  "committed": false,
  "db_error": { "code": "SQLITE_CONSTRAINT",
    "message": "SQLite error: UNIQUE constraint failed: reject_case.book_id" } }
```
数据库中由 `book_id=100` 主键冲突触发拒绝，整批回滚；其后 `reject_case` 仅剩原有
`(100, 已有书目)`，未出现 101/102。

2. 更正样本 → `accept_case`
```bash
node import-books.mjs materials/batch-corrected.csv accept_case   # 退出码 0
```
```json
{ "target_table": "accept_case", "rows_in_file": 3, "book_ids": [101,103,102],
  "committed": true, "db_error": null }
```
`accept_case` 终态：`(100,已有书目)`、`(101,候选书目甲)`、`(102,候选书目乙)`、`(103,更正编号书目)`。
