公开证据节选；独立核验原文件 SHA256：e69e60aef3bf5788f1c0a41e129a8b517c13883d588415aafa5ec3e3a2f4961e。原始材料私有保存，以下编辑不改验收结论。

# Exa 接入验收核验摘要（脱敏）

来源：本次执行采集的工具记录与工作文件；未包含账号、密钥或会话标识。

## 指定入口与接入方式
- 入口：`https://mcp.exa.ai/mcp`（官方匿名远程 MCP，streamable HTTP）。
- `initialize` 经 curl JSON-RPC 调用返回 HTTP 200，serverInfo = `exa-search-server`，版本 `3.2.1`，协议 `2025-06-18`；请求未带 `Authorization`/`x-api-key` 头，即 keyless。
- `tools/list` 返回 `web_search_exa`、`web_fetch_exa`。
- 仅访问 exa.ai 域；工具记录中未出现其他搜索引擎或代理服务的调用。

## 真实搜索
- 查询：`official Python 3.13 release announcement blog post on python.org`
- objective：Find the official python.org blog post announcing the release of Python 3.13 and the exact release date.
- numResults：5；调用 exit=0，原始响应 5428 字节（`search-result.raw.json`）。
- 返回结果含标题与 URL，例如：
  - `Python 3.13.0 (final) released | Python Insider` — https://blog.python.org/2024/10/python-3130-final-released/
  - `Python Release Python 3.13.0` — https://www.python.org/downloads/release/python-3130/
- 独立复核：上述 blog.python.org 页面可访问，正文含 “Python 3.13.0 is now available” 与 “October 7, 2024”，与答复一致。

## 配置持久化
- 连接配置写入 `/home/node/service-tools/service-config.json`（endpoint、transport、协议、工具列表、keyless auth），执行时 JSON 校验通过；运行回执的 retained-files 列出该文件。
- 该配置不含 API key 或任何秘密。

## 账号与人工介入
- 本轮未提供账号；全程 keyless，无注册、无登录、无 OAuth、无付费、无人工操作。

## 免费规则来源
- 官方文档 https://exa.ai/docs/reference/exa-mcp Authentication 表：`Keyless | Free rate-limited usage without sign-in or API key | Connect to https://mcp.exa.ai/mcp`。
- 同页 Troubleshooting：“The connection is using Exa's free rate limits.”
- 本次观察：使用 keyless 入口、无 API key，`web_search_exa` 调用返回 HTTP 200 且未出现 429，符合该免费规则。


本轮按相同web-search-001/v2任务比较，旧v1不合并统计。接入和业务均为匿名公开入口，额度余量未知，同一服务器出口IP；持久化配置经检查未含业务答案。执行原始返回与三份事前独立官方参考均私有保留；来源链由独立验收核对，没有额外最低页面数要求。单次试跑只说明这次任务，不是普遍可靠性排名。
