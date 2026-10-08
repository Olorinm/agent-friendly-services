Now let me connect to the Exa MCP endpoint. First, initialize the MCP session.
Session initialized. Now let me run the full flow (initialized notification, list tools, real search) with a script.
Cloudflare blocks the default Python User-Agent. Adding one.
Connection works and tools are listed, but the anonymous free tier returned a rate-limit notice. Let me retry a few times with backoff.
Search succeeded (the earlier rate-limit was transient). Now saving the persistent config.
接入完成，已通过 Exa 官方匿名远程 MCP 做过一次真实网页搜索。

**搜索查询**：`history of the Python programming language`
**结果示例**：
- Title: `History of Python` — https://en.wikipedia.org/wiki/History_of_Python
- Title: `Introduction and Overview - The History of Python` — https://gvanrossum.github.io/python-history/introduction-and-overview.html

**完成的接入步骤**
1. 确认入口 `https://mcp.exa.ai/mcp` 为官方 keyless 匿名 MCP，无需账号/Key（官方文档已核对）。
2. 用 streamable-HTTP 完成 MCP 握手：`initialize` → `notifications/initialized` → `tools/list` → `tools/call`；服务端返回 `Mcp-Session-Id`，响应为 SSE，逐行解析 `data:` 得到 JSON-RPC。
3. 实际调用 `web_search_exa` 拿到真实网页结果并读取返回内容（工具列表：`web_search_exa`、`web_fetch_exa`）。
4. 连接配置写入持久目录：`/home/node/service-tools/service-config.json`；任务脚本与一次搜索结果只放在本题工作目录（`exa_mcp_search.py`、`exa_search_retry.py`、`exa_search_result.json`）。

**账号来源与自助步骤**：本轮无账号、无 Key、无支付方式，完全使用匿名免 Key 入口，未注册、未付费，全流程由我自行按官方文档完成。

**遇到的阻碍**
- Python 默认 User-Agent 被 Cloudflare 拦截（HTTP 403），改为 curl 风格 UA 后正常。
- 匿名免费层有限流：首次搜索返回 `ai.exa/rateLimited=true` 的限流提示；重试（短等待后）即成功。这是官方免费额度的固有现象，非配置错误。
- `agent_run` 等付费/研究工具未启用，符合"仅免费匿名"的授权范围。

后续搜索所需配置位置：`/home/node/service-tools/service-config.json`（无秘密，故不需要私有密钥文件）。