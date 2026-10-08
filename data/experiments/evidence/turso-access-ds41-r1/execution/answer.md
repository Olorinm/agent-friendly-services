已接通。指定方式为 Turso Platform API（`https://api.turso.tech/v1/`）管理的 libSQL 数据库 + 官方 SQL HTTP 接口 `/v2/pipeline`。

**本轮资源（非秘密）**
- 数据库名/ID：`[SERVICE_SECRET]` / `[SERVICE_SECRET]`，类型 libSQL、区域 aws-us-east-1，复用既有组 `[SERVICE_SECRET]`（未新建父资源，避免超出 starter 的 1 组配额）。
- 连接标识已存 `/home/node/service-tools/service-config.json`；Token、URL 等秘密存 `/home/node/service-tools/credentials.json`（0600，含 API Token、DB Auth Token、创建/过期时间）。答复不含秘密。

**接入步骤**
1. 用提供的 `TURSO_API_TOKEN` 查组织（`[SERVICE_SECRET]`）与套餐。
2. `POST /organizations/{org}/databases` 创建本轮专用空库。
3. `POST .../databases/{db}/auth/tokens?expiration=7d&authorization=full-access` 签发数据库 Token。
4. `POST https://<host>/v2/pipeline` 执行只读查询验证。结果 HTTP 200：`SELECT 1` 返回 `1`，`sqlite_version()` 返回 `3.47.0`，`sqlite_master` 表计数为 `0`（空库，未建表、未写入业务数据）。

**人工门槛与自主性**
- Token/组织由本轮私有 `credentials.json` 提供（既有账号，非本轮注册），全程无验证码、无需人工介入、无需特殊申请。
- 未启用 overages、未绑卡；仅新建 1 个空库。

**免费/到期限制**
- 账号套餐 `starter`，价格 0，`overages=false`。配额：读 5亿行/写 1000万行/库 100个/存储 5GB/组 1个/同步 3GB/月，超限即停不自动扣费。
- 数据库 Token 有效期 7 天（`TURSO_TEST_DB_AUTH_TOKEN_EXPIRES_UTC` 已记录，约 2026-10-15 到期）；到期需重新签发。`installed-tools` 已建（本轮仅用 curl/Python 标准库，无需额外依赖）。