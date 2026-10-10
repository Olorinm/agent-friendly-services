已通过指定 Neon Claimable 匿名 API 接通，创建本轮专用空库并完成只读连通性验证。

**资源标识**
- 项目 `[SERVICE_SECRET]`，分支 `[SERVICE_SECRET]`
- 数据库 `neondb`，用户 `neondb_owner`，主机 `[SERVICE_SECRET]:5432`（TLS 必需）
- 项目到期 `2026-10-11T12:36:21.796Z`（UTC，即创建后 72 小时）

**只读验证结果**（未写入任何业务数据/表）
- `PostgreSQL 17.11`，连接用户 `neondb_owner`，`public` schema 表数 = 0
- 查询 `SELECT version(), current_database(), current_user, now()` 成功，`READONLY_QUERY_OK`

**接入步骤（均由我自助完成，无需预置账号/Key）**
1. `POST https://claimable.neon.tech/v1/agent/identity`，`{"type":"anonymous","capabilities":["postgres"],"source":"opencode-agent-ds41"}` → 返回 `identity_assertion`、项目与到期时间（HTTP 201）。
2. 用断言换 60 分钟 `access_token`：`POST /v1/oauth2/token`（`grant_type=...jwt-bearer`）。
3. `GET /v1/projects/{id}/credentials` 取 `database_url`。
4. 用 pg8000 客户端执行一次只读查询验证连通。
5. 保存配置：秘密（identity_assertion、claim_token、access_token、database_url、数据库密码）写入 `/home/node/service-tools/credentials.json`（权限 600）；非秘密连接配置写入 `/home/node/service-tools/service-config.json`（600）。依赖安装在 `/home/node/service-tools/installed-tools`。工作目录仅留脚本，原始含密响应已删除。答复不含任何秘密。

**人工门槛（需人工介入）**
- 匿名身份只能创建“未认领(unclaimed)”项目，能力仅限 `postgres`（含可先建 Data API/Auth，但需认领后 Functions/存储/AI 等）。
- 若要长期保留该项目，需人工认领：`POST /v1/projects/{id}/claim` 生成 15 分钟有效的 claim code，浏览器打开 `https://claimable.neon.tech/claim` 登录 Neon 并选择目标组织；认领后身份断言/令牌/库密码会被吊销，需从目标组织重新取连接串。
- 无预提供账号；本项目未 claim 到任何付费组织。

**免费与到期限制（服务返回为准）**
- 未认领项目 72 小时后到期：`2026-10-11T12:36:21.796Z`；上限 100 MB 存储 / 1 GB 传输。
- claim code 有效期 15 分钟（`expires_in: 900`）；身份断言约 3 天有效，访问令牌 3600 秒且无 refresh token，过期需用断言重新换取。
- 全程未付款、未绑卡、未开启超额；仅新建 1 个空库，未读取/修改任何既有用户库。

**阻碍**：无。唯一外部依赖为 Postgres 客户端（psql 未预装），已用纯 Python 的 `pg8000` 安装到 `installed-tools` 解决。