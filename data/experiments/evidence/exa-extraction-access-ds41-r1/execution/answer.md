接入成功。

**结果**
- 标题：**Example Domain**
- 概述：这是一个仅用于文档示例的保留域名，本身并非可供测试或监控使用的真实服务。
- 服务：Exa 官方匿名远程 MCP（`https://mcp.exa.ai/mcp`），工具 `web_fetch_exa`，无需账号/Key。

**配置与产物位置**
- 持久配置：`/home/node/service-tools/service-config.json`（endpoint、传输方式、工具入参、认证=keyless；无秘密）
- 可复用调用脚本：`[WORKSPACE]/exa_mcp_call.py`
- 原始响应快照：`[WORKSPACE]/fetch_result.sse`
- 结果：`[WORKSPACE]/result.json`

**接入步骤**
1. `POST /mcp` 发 `initialize`（protocolVersion `2024-11-05`），从响应头 `Mcp-Session-Id` 取会话 ID。
2. 发 `notifications/initialized`。
3. 带 `Mcp-Session-Id` 发 `tools/call`，`web_fetch_exa` 参数 `{"urls":["..."],"maxCharacters":N}`。
4. 解析 SSE 的 `data:` JSON，取 `result.content[0].text`。

**遇到的门槛**
- 不是普通 REST：必须走 MCP 的 initialize→initialized→调用 三步握手并使用会话头。
- Cloudflare：Python `urllib` 默认 UA 被 403 拦截，需显式设置 UA（脚本已用 `curl/8.5.0` 解决）。
- keyless 为免费限流模式，超限会返回 429；`agent_run` 需 OAuth/Key，本轮未启用（也不影响网页提取）。
- 未注册、未用 Key、未付款；未提供账号故无账号来源可说明。