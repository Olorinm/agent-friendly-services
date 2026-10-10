公开证据节选；独立核验原文件 SHA256：7486bd6ffd630aa2e4841c5dc424ddc07ccff2aeb76b1b0b34679bf5914cdae8。原始材料私有保存，以下编辑不改验收结论。

# 验收摘要：exa 服务调用、来源链与免费规则

## 1. 指定服务与调用方式
- 指定服务：exa（官方匿名远程 MCP），入口 `https://mcp.exa.ai/mcp`。
- 本次实际调用：执行者用脚本经 `initialize` + `notifications/initialized` + `tools/call`
  连接该入口，调用工具 `web_search_exa`、`web_fetch_exa`。请求头无 API key（`auth.headers = {}`、
  `auth.mode = keyless`，见 `service-config.json`），初始化返回 HTTP 200、`serverInfo.name=exa-search-server`。
- 记录位置：原始调用与响应见执行副本 `execution/artifacts/mcp_call.py`、`search1.json`、`search2.json`、`fetch1.json`
  （原始工具记录与 wire 属私有材料，未作为公开证据引用）。

## 2. 来源链（结论 <- 指定 exa 搜索结果/抓取）
- exa `web_search_exa` 第 1 次（`search1.json`）返回：
  - `https://docs.python.org/3/whatsnew/3.13.html`（3.13 What's New，含 free-threaded 默认状态/启用/告警说明）
  - `https://docs.python.org/3/howto/free-threading-python.html`（自由线程使用指南）
  - `https://blog.python.org/2024/10/python-3130-final-released/`（Python Insider 官方发布公告）
- exa `web_search_exa` 第 2 次（`search2.json`）返回：
  - `https://docs.python.org/3/howto/free-threading-extensions.html`（C API 扩展对自由线程的支持）
- exa `web_fetch_exa`（`fetch1.json`）直接读取 3.13 版本页：
  - `https://docs.python.org/3.13/howto/free-threading-python.html`
  - `https://docs.python.org/3.13/howto/free-threading-extensions.html`
- 执行者最终答复（`execution/answer.md`）引用的官方页面为上述文档的 3.13 版本链接
  （whatsnew / free-threading-python / free-threading-extensions）以及官方博客 `blog.python.org`。
  3.13 版本链接与 exa 返回的 `/3/` 文档为同一官方文档的版本固定等价地址，可追溯到搜索结果。
- 未发现使用其他搜索引擎或模型记忆替代来源发现；结果中出现的第三方站点（如 infoworld）未被用作结论依据。

## 3. 免费规则与本次适用（Exa 官方文档）
- 免费规则来源（Exa 官方 MCP 文档，`https://exa.ai/docs/reference/exa-mcp`，验收环境直读官方页）：
  - 认证方式表：`Keyless`——"Free rate-limited usage without sign-in or API key"，连接 `https://mcp.exa.ai/mcp`。
  - 故障排查：keyless 连接使用 "Exa's free rate limits"；登录 OAuth 或自带 API key 才会使用自有 plan/额度。
  - 可用工具表：`web_search_exa`、`web_fetch_exa` 为 "Enabled by default"；`agent_run` 需 OAuth/API key，
    keyless 免费额度不可用。
- 本次适用观察：
  - 本次运行使用无鉴权 keyless 连接（无 API key、无 OAuth、未登录、未付费），只调用默认工具
    `web_search_exa` / `web_fetch_exa`（未调用需鉴权的 `agent_run`），且调用成功返回内容。
  - 无任何付费/绑定支付/超额行为，也无计费回执。据此本次落在 keyless 免费限流额度内。

## 4. 人工介入
- 本次 exa 匿名入口无需注册、无需 API key 或 OAuth；执行由 opencode `run` 自动完成，
  未观察到被测执行期间需要人类参与。


本轮按相同web-search-001/v2任务比较，旧v1不合并统计。接入和业务均为匿名公开入口，额度余量未知，同一服务器出口IP；持久化配置经检查未含业务答案。执行原始返回与三份事前独立官方参考均私有保留；来源链由独立验收核对，没有额外最低页面数要求。单次试跑只说明这次任务，不是普遍可靠性排名。
