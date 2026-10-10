Now I understand the protocol. Let me probe the endpoint connectivity and set up directories.
Hosted MCP is reachable and authenticates with the API key (session established). Now let me build a reusable MCP JSON-RPC client script in the task directory.
Discovery succeeded. Let me extract the tool names and the key schemas from the saved log.
Now I'll add rate-limiting (≥2s between ops) to the client, then run profile + org discovery.
Account confirmed. Now let me confirm the parent workspace via `list_workspaces`.
Parent workspace `[PRIVATE_WORKSPACE_ID]` confirmed empty. Now creating the new empty document via hosted MCP.
Document created. Now re-reading its metadata through a fresh hosted-MCP session to confirm the same remote resource.
Document confirmed identical (same id/workspace/url). Now let me gather the official free-tier limits to report accurately.
Everything verified. Now saving the reusable connection config to the authorized persistent location.
接入完成。以下是结果。

## 空间链接
- 新建空文档：https://docs.getgrist.com/[PRIVATE_DOC_URL_ID]/[SERVICE_SECRET]
- 容器标识：workspace `[PRIVATE_WORKSPACE_ID]`(`[SERVICE_SECRET]`) / doc `[PRIVATE_DOC_ID]`
- 站点：Personal(`docs-218066`, org [PRIVATE_ORG_ID])，账号 Sheila Nader / osokuruk606@gmail.com

通过 hosted-MCP 真实执行并**重新读取**元数据确认是同一远端资源（`get_doc_info` 返回同一 id、workspace [PRIVATE_WORKSPACE_ID]、URL、access=owners、createdAt 2026-10-10T11:01:00Z）。文档为空：仅有 Grist 默认的无列 `Table1`，未预建任何业务字段/记录。

## 接入步骤（自助）
1. 账号与 API key 由总控提供，非我注册；仅使用凭据文件 `/home/node/service-tools/credentials.json` 中的密钥。
2. 入口：`https://docs.getgrist.com/api/mcp`（hosted Grist 的 MCP 默认开启，无需自建服务）。传输为 Streamable HTTP 的 JSON-RPC 2.0，认证用 `Authorization: Bearer <API_KEY>`。
3. `initialize`（protocolVersion 2025-06-18）→ 服务端回 `Mcp-Session-Id` → 发 `notifications/initialized` → `tools/list` 发现 51 个 `grist_*` 工具 → `tools/call`。
4. 执行序列：`get_user_profile`/`list_orgs` → `list_workspaces`（确认父工作区空白）→ `create_doc` → `get_doc_info`+`get_tables` 复读校验。服务操作单线程、间隔≥2s；本阶段约 13 次服务操作，未触发 403/429。

## 人工门槛
- 本轮**无需人工介入**：API-key 认证跳过浏览器授权。无验证码、无资质审核、无付款/绑卡。
- 对比说明：Claude/ChatGPT 等走交互式 OAuth/CIMD 的客户端需要人工在同意页选择 scope 与可访问资源；本 API-key 路径全自动。若后续要访问新资源，仅需替换资源指针，不需要重新授权整个连接。

## 免费限制（官方文档）
- 计划：personalFree。文档数不限（团队站点软上限 1000 篇）。
- 单文档：5,000 行、约 10MB 数据、500 表、内部附件 1GB；组织附件 50GB；单次上传 50MB；免费团队 10 名成员，每文档 2 名免费访客。
- API：**REST 与 MCP 共用同一站点池，每月 3,000 次**（剩余额度未提供，记为未知）；免费计划限速约 5 请求/秒/文档，并发 10，单请求体 ≤1MB。MCP 当前无额外服务费，模型费用另计。

## 配置保存位置
- 持久连接配置：`/home/node/service-tools/service-config.json`（权限 600；含入口、传输、认证方式、站点、当前资源指针、配额说明，不含密钥）。
- 密钥仍仅存 `/home/node/service-tools/credentials.json`，未复制、未输出。
- 本题记录：工作目录 `grist_access_result.json`、客户端脚本 `grist_mcp.py`、日志 `logs/`。未安装额外依赖（Python 标准库即可）。

无未完成项。