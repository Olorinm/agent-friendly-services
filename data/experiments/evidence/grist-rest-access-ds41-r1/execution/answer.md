已完成接入。通过指定入口 Grist REST API 在既有工作区内新建了 1 个空文档并回读确认。

**空间链接**
- 文档（后续任务表容器）：https://docs.getgrist.com/doc/[SERVICE_SECRET]
- 父工作区：`[SERVICE_SECRET]`（id `[SERVICE_SECRET]`，org Personal / `[SERVICE_SECRET]`）

**实际做了什么**
1. 用 `credentials.json` 里的 API key 调 `GET /api/workspaces/[SERVICE_SECRET]`，确认父工作区存在、可写、`docs` 为空。
2. `POST /api/workspaces/[SERVICE_SECRET]/docs` 新建空文档 `[SERVICE_SECRET]` → 得到 docId `[SERVICE_SECRET]`、urlId `[SERVICE_SECRET]`。
3. 重新 `GET /api/docs/[SERVICE_SECRET]` 回读元数据，并 `GET /api/workspaces/[SERVICE_SECRET]` 看到该文档已挂在同一工作区下，确认是同一远端资源；未建任何业务字段/记录（保留服务自带的空白占位表）。
4. 仅用 curl/REST，无额外依赖需安装；`installed-tools/` 已建但为空。

**配置保存位置（无密钥）**
- `/home/node/service-tools/service-config.json`：api 入口、org/workspace/doc 标识与链接、鉴权指向。
- 密钥仍在私有文件 `/home/node/service-tools/credentials.json`，答复不含密钥。

**接入步骤 / 人工门槛**
- 本轮 API key 与父工作区由总控预先创建，**非我自主注册**；创建 API key 需登录 Grist 账号后在 Settings→API 生成，属人工步骤。
- 全程无验证码；调用用 `Authorization: Bearer <key>` 即可，无审批/资质门槛。
- 自助可复现路径：登录取 key → `POST /workspaces/{id}/docs` 建文档 → `GET /docs/{id}` 回读。

**免费限制（personalFree，来自 API 实际返回 + 官方 limits 页）**
- API：**3,000 次/月/组织**，REST 与 MCP **共享**该额度；免费计划限约 5 请求/秒/文档，并发上限 10（超限 429），单请求 body 1MB。**本轮实际剩余额度未知**。
- 文档：5,000 行、约 10MB 数据；附件 1GB/文档、50GB/组织；最多 500 张表/文档。
- 共享：每文档最多 2 位免费访客；`maxSharesPerWorkspace: 0`（免费个人不可向工作区做团队共享）。
- 上传/导入单次 ≤50MB；文档数为软限制。
- 未购买、未绑卡、未分享、未开启超额。