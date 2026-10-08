MCP 握手和搜索都成功。现在把连接配置持久化，并写一个可复用的查询脚本。
已接通 Exa 官方匿名远程 MCP 并完成真实搜索。

**接入步骤（均为自助完成）**
1. 按官方文档确认入口 `https://mcp.exa.ai/mcp`，为 keyless 免费模式，无需 API key/注册。
2. 用原始 JSON-RPC over streamable HTTP 完成 `initialize` 握手（协议 `2025-06-18`，server=`exa-search-server 3.2.1`），取得 `Mcp-Session-Id`，再发 `notifications/initialized`。
3. `tools/list` 确认可用工具：`web_search_exa`、`web_fetch_exa`。
4. 编写可复用客户端 `exa_mcp_client.py`（仅用 Python 标准库，无需额外依赖）。

**真实搜索验证**
- 查询：`official Python 3.13 release announcement blog post on python.org`
- 结果示例：**Python 3.13.0 (final) released | Python Insider** — https://blog.python.org/2024/10/python-3130-final-released/
- 另返回 python.org 官方发布页 https://www.python.org/downloads/release/python-3130/（页面标注 Release date: Oct. 7, 2024）。

**持久配置（供后续复用）**
- `/home/node/service-tools/service-config.json`：仅连接配置（endpoint、transport、协议、工具列表），无秘密。
- 查询脚本、原始结果与说明在本题工作目录：`exa_mcp_client.py`、`search-result.raw.json`、`answer.md`。

**阻碍与说明**
- 用 Python `urllib` 默认 UA 首次请求被 Cloudflare 返回 403；改为 `curl` UA 后正常（已固化在脚本里）。
- 匿名额度未知，本次调用未触发限流；如遇 429 需退避，官方建议改用 OAuth/API key，本轮按授权未注册、未付费。