公开证据节选；独立核验原文件 SHA256：d21f0c3ecba01c2a3a136b52146f059032e6b047e3fe7b47f14318f951e41b63。原始材料私有保存，以下编辑不改验收结论。

# 指定入口接入证据（摘录自本次运行工具记录）

1. `POST https://claimable.neon.tech/v1/agent/identity`
   body: `{"type":"anonymous","capabilities":["postgres"],"source":"opencode-agent-ds41"}`
   → HTTP 201
2. 返回非秘密字段：
   - project.id = `[SERVICE_SECRET]`
   - project.branch_id = `[SERVICE_SECRET]`
   - project.expires_at = `2026-10-11T12:36:21.796Z`
   - scopes = `postgres.read postgres.write data_api.configure auth.configure`
   - capabilities = `[{"capability":"postgres","granted":true}]`
3. `POST /v1/oauth2/token`（grant_type=jwt-bearer）→ `expires_in: 3600`
4. `GET /v1/projects/[SERVICE_SECRET]/credentials`（Bearer token）→ 返回 `database_url`、同 `expires_at`，`services: {}`

使用的入口为 ENVIRONMENT.md 指定的 `claimable.neon.tech/v1/agent/identity`，
非旧 neon.new 入口，未 claim 到付费组织。秘密（identity_assertion / claim_token /
access_token / database_url / 密码）已从本摘录移除。


附加独立核验摘录；原文件 SHA256：0efad79699187ebf0bd22f41af2563d94d1846aebb01d952d2eebceb9ac32984

# 只读连通性查询证据（摘录自本次运行工具记录）

执行命令：`python3 verify_connection.py`（使用 pg8000 连接服务返回的 database_url，执行只读 SQL）

实际返回：
```
version: PostgreSQL 17.11 (fcae950) on aarch64-unknown-linux-gnu, com
database: neondb
user: neondb_owner
server_time: 2026-10-08 12:39:13.591840+00:00
public_tables: 0
READONLY_QUERY_OK
```

查询语句为 `SELECT version(), current_database(), current_user, now()` 与
`SELECT count(*) FROM information_schema.tables WHERE table_schema='public'`，均为只读。
`public_tables: 0` 表明目标库为空，未预建业务表。
（已移除数据库密码/URL/断言等秘密，仅保留业务结果字段。）
