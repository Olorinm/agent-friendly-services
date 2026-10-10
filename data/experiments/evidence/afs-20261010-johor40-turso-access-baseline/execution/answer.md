Database created. Now issuing a database auth token and storing it privately.
Read-only query succeeded (SQLite 3.47.0, 0 user tables, rows_written 0). Saving config now.
已通过指定方式接通 Turso 数据库服务，创建了本轮专用空库并完成只读连通性验证。

## 结果

**本轮资源**
- 数据库名 `[SERVICE_SECRET]`（唯一新建，libSQL/logical，空库）
- DbId `[SERVICE_SECRET]`
- 主区域 `[SERVICE_SECRET]`，group `[SERVICE_SECRET]`，org `[SERVICE_SECRET]`
- SQL over HTTP 端点 `[SERVICE_SECRET]`
- libSQL URL `[SERVICE_SECRET]`

**只读验证**（`/v2/pipeline`，未建表、未写业务数据）
- `SELECT sqlite_version(), (SELECT count(*) FROM sqlite_master WHERE type='table')`
- 返回：`version=3.47.0`，`user_tables=0`，`rows_read=1`，`rows_written=0`（证据见 `query-result.json`）

**配置位置**
- 秘密（SQL 库 token）与资源标识：`/home/node/service-tools/credentials.json`（新增键 `[SERVICE_SECRET]`，权限 600）
- 通用连接信息（无秘密，引用上面 token 位置）：`/home/node/service-tools/service-config.json`

## 接入步骤（本 Agent 已完成）
1. 读取总控提供的 `TURSO_API_TOKEN`/org/group；`GET /v1/organizations/{org}/databases` 确认现状（1/100）。
2. `POST /v1/organizations/{org}/databases` 以 `{"name":"[SERVICE_SECRET]","group":"[SERVICE_SECRET]"}` 创建空库。
3. `POST /v1/organizations/{org}/databases/[SERVICE_SECRET]/auth/tokens?expiration=never&authorization=[SERVICE_SECRET]` 自行签发 SQL 库 token。
4. `POST {host}/v2/pipeline` 带 `Authorization: Bearer <jwt>` 做只读查询。
5. 保存资源与 token 到持久目录；工作目录内不留 token 明文。

## 人工门槛
- 无需注册/验证码/绑卡：账户由总控预置，纯 API 自助完成。
- 唯一需第三方介入的是**破坏性资源变更**（创建/删除数据库、签发 token）——本轮已按授权自行执行；无 CLI/MCP 依赖（按要求未使用）。

## 免费与到期限制
- 套餐：Starter，价格 0，overages=false（总控已核实），不得开启付费/超额。
- 当前用量：1→2/100 数据库；存储约 49KB/5GB；rows_read 267/500M、rows_written 59/10M。本库为空，仅 1 行读取。
- token `expiration=never`，但账号套餐/配额可能变化；固定 50 美元窗口截止 `2026-10-10T13:53:59Z`。
- 首次出现 403/429 或付费要求时应停止（本轮未触发）。

失败重试：第 1 次 pipeline 查询因 SQL 内层引号被当作标识符报错，改为单引号后重试成功（共约 6 次服务操作，预算 40 内）。未读取任何既有业务库。