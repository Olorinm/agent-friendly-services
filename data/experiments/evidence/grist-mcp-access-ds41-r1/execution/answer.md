已完成接入并验证。

## 空间链接
https://docs.getgrist.com/[SERVICE_SECRET]/[SERVICE_SECRET]

- 文档 ID：`[SERVICE_SECRET]`，名称 `[SERVICE_SECRET]`，位于给定工作区 `[SERVICE_SECRET]`（[SERVICE_SECRET]，Personal 站点），创建时间 2026-10-08T13:46Z，访问级别 owners。
- 状态：空文档，仅含服务自动附带的占位表 `Table1`（A/B/C 三列），未建业务字段或记录。
- 复核：用 `grist_get_doc_info` 重新读取，返回的 id/name/workspace 与创建结果一致，确认是同一远端资源。

## 接入步骤（真实自助）
1. 用预提供的 API key 以 HTTP Streamable 方式连接官方 MCP `https://docs.getgrist.com/api/mcp`，请求头 `Authorization: Bearer <GRIST_API_KEY>`。
2. 依次发送 `initialize`（协议 `2025-06-18`）→ `notifications/initialized` → `tools/list`/`tools/call`。托管版 MCP 已开启，无需额外开关。
3. 在给定工作区调用 `grist_create_doc` 新建文档，再用 `grist_get_doc_info` 读取元数据确认。
4. 连接配置已存到 `/home/node/service-tools/service-config.json`（工作区/文档标识、链接、默认表、免费额度、调用方式）；密钥仍在 `/home/node/service-tools/credentials.json`，未复制到任何配置。
- 未安装通用依赖（Node 内置 fetch 足够），故未产生 installed-tools；接入脚本只在当前工作目录 `mcp-client.mjs` / `mcp-call.mjs` / `mcp-tools.json`。

## 人工门槛 / 额外申请
- 无。用现成 Personal 账号 API key 即可自助完成，未做注册、OAuth 授权页、邀请或分享；非本轮自主注册，账号来源为预提供。
- 唯一门槛是密钥需人工预置（本轮已提供）。

## 免费限制（官方，Free Personal）
- API：3,000 次/月，全站点文档共享（REST 与 MCP 合并计数）；约 5 请求/秒/文档；并发 10/文档；请求体 ≤1MB。
- 文档：行数 5,000/文档，数据 10MB/文档，表 500（软限），附件 1GB/文档、50GB/组织。
- 文档数不限（团队站点可能上限 1,000），协作者 10 名成员、每文档 2 名免费访客。
- 实际剩余额度未通过 MCP 暴露，记为未知。