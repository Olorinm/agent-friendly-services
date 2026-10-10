公开证据节选；独立核验原文件 SHA256：b2c3b0a7526bfe8542f83a3dbd31064bdc2c777534b0a67df7ccfb95ecc0797e。原始材料私有保存，以下编辑不改验收结论。

# Turso 远端写入 / 全新进程读取 证据摘录

来源：本次执行运行器采集的工具调用记录（官方 SQL HTTP 接口 `/v2/pipeline`）。已删除账号、数据库/资源标识、主机名与全部密钥；仅保留业务字段。

## 1. 业务前连通性与空库确认（同一凭据端点）
请求：`{"requests":[{"type":"execute","stmt":{"sql":"SELECT name FROM sqlite_master WHERE type='table';"}},{"type":"close"}]}`
响应：`results[0].response.result.rows = []`（无任何表 → 该库业务前为空库，非本地模拟）

## 2. 写入程序（独立进程 write_todos.py，进程退出码 0）
- 建表 `todos(id INTEGER PRIMARY KEY, title TEXT NOT NULL, done INTEGER NOT NULL DEFAULT 0)`
- 插入三条：id=1 Buy milk/false、id=2 Read book/false、id=3 Walk dog/true
- 执行 `UPDATE todos SET done=? WHERE id=?`（id=2 → true），其他字段不变
- 输出：
  - `INSERTED: [(1, 'Buy milk', False), (2, 'Read book', False), (3, 'Walk dog', True)]`
  - `UPDATED: id=2 -> done=true (other fields unchanged)`
  - `AFTER WRITE: id1=0, id2=1, id3=1`
  - `WRITE_PROGRAM_DONE` / `WRITE_EXIT=0`

## 3. 全新读取程序（另一次独立调用、不同进程 read_todos.py，进程退出码 0）
- 不引用写入程序模块，重新连接同一凭据端点读取
- 输出：
  - `ALL_TODOS: [{"id":1,"title":"Buy milk","done":false},{"id":2,"title":"Read book","done":true},{"id":3,"title":"Walk dog","done":true}]`
  - `PENDING_TODOS: [{"id":1,"title":"Buy milk"}]`
  - `TOTAL: 3` / `COMPLETED: 2` / `PENDING: 1`
  - `READ_EXIT=0`

结论：写入进程退出后，由另一全新进程重连同一远程端点读回三条，id 升序、仅 id=1 未完成、总数 3 / 完成 2，标题与写入一致。


附加独立核验摘录；原文件 SHA256：62c9e14788647a71efcfc26c8c4de736a23a2548a32f80821da23d8c17bb48ff

# Turso 免费 / 到期限制 证据摘录

来源：本次执行工具记录对 Turso Platform API 与官方文档的真实请求响应。已删除账号、组织/数据库标识与密钥。

## 账号套餐与超额设置（GET /v1/organizations/{org}，2026-10-08）
- `plan_id: "starter"`
- `overages: false`（未启用超额计费）
- `blocked_reads: false`, `blocked_writes: false`, `payment_failing_since` 无效

## 套餐配额（GET /v1/organizations/{org}/plans）
- starter：`price: "0"`（monthly）
- quotas：`rowsRead 500000000`、`rowsWritten 10000000`、`databases 100`、`storage 5000000000`(5GB)、`groups 1`、`locations 3`、`bytesSynced 3000000000`(3GB)

## 本次实际用量（GET /v1/organizations/{org}/usage，业务读写之后）
- `total: rows_read 0, rows_written 0, storage_bytes 8192, bytes_synced 0`
（远低于免费额度；账号无支付方式，overages 关闭）

## 官方价格页（https://turso.tech/pricing，本次抓取）
- Free：`$0/month`；100 databases；5GB storage；500M rows read/month；10M rows written/month；3GB sync

## 归档 / 到期规则（https://docs.turso.tech/api-reference/groups/unarchive，本次抓取）
- “Databases get archived after 10 days of inactivity for users on a free plan.”（免费套餐数据库 10 天无活动被归档，可 unarchive 恢复，非删除）
- 业务阶段数据库 Token 以 `expiration=7d` 参数签发（接入阶段配置），执行者答复披露为 7 天有效、2026-10-15 12:37 UTC 到期。


总控公开说明：服务用量端点当时返回0行，但真实业务日志证明已发生写入和读取。此处0仅为当时观察到的计数，不能解释为业务没有读写或计量已实时更新；免费判断另有starter零价套餐与overages关闭的依据。
