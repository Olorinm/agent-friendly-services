Actual executor answer with financial quote values omitted; unchanged original SHA256 af6e033e22f960c45f8347154d46112d3f02999f31c52da1096e65da2e85272f.

I have the docs. Now let me check connectivity to the MCP endpoint and understand its protocol behavior.
`?apikey=` and `Authorization: Bearer <key>` both authenticate. Bearer keeps the key out of the URL, so I'll use that. Now let me build a proper MCP client.
Cloudflare blocks Python's default User-Agent (curl worked). Adding a UA header.
133 tools exposed. Now test the free `PING` tool (no data quota), then one real data query.
`PING` works end-to-end. Now one real data query via MCP (`GLOBAL_QUOTE`).
Data query succeeded (IBM quote for 2026-10-07). Now let me save the persistent config.
接入成功，指定方式（官方托管 MCP）已验证可用。

**验证结果**
- 握手 `initialize` → OK（服务端 alphavantage-mcp-server 1.0.0）；`tools/list` → 133 个工具。
- 免费工具 `PING` → `pong`（不占数据额度）。
- 真实数据查询 `GLOBAL_QUOTE(symbol="IBM")` → 2026-10-07 收盘 [market value retained privately]（1 次金融数据请求，在 3 次接入额度内）。

**采用的认证**：非交互 `Authorization: Bearer <key>`，key 运行时从 `credentials.json` 读取，不落入 URL（文档中 `?apikey=` 的旧方式也可用但会把 key 写进 URL，故未采用）。Cloudflare 会 403 封禁 Python 默认 UA，已用 curl 式 UA 规避。

**持久配置（不含 key）**
- 连接配置：`/home/node/service-tools/service-config.json`
- 可复用客户端：`/home/node/service-tools/installed-tools/mcp_client.py`
- 查询示例：`python3 .../mcp_client.py call TIME_SERIES_DAILY '{"symbol":"IBM","outputsize":"compact"}'`
- Key 仅存于 `/home/node/service-tools/credentials.json`。

**额度**：账号为免费档，25 次/日且 REST 与 MCP 共享；本轮仅用 1 次数据请求。未调用任何付费端点。无阻碍项。