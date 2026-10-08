Docs confirm anonymous scraping without a key. Now making the actual call to the specified endpoint.
Call succeeded. Saving configuration to the persistent directory.
**接通成功，服务可用。**

- **页面标题**：Example Domain
- **内容概述**：该域名仅用于文档示例，页面明确声明它并非一项服务，建议不要将其用于测试或监控目的。
- 实测请求：`POST https://api.firecrawl.dev/v2/scrape`，body `{"url":"https://example.com/","formats":["markdown"]}`，返回 HTTP 200 / `success:true` / `metadata.statusCode:200`，消耗 1 credit。
- 原始响应快照：`[WORKSPACE]/scrape-response.json`

**配置位置**（持久目录，权限 600，无秘密）：
`/home/node/service-tools/service-config.json` —— 记录了端点、方法、无鉴权、请求体模板与本次验证结果；通用依赖目录 `/home/node/service-tools/installed-tools` 已就绪（本次用 curl 直调，无需额外依赖）。

**接入步骤**
1. 直接向 `https://api.firecrawl.dev/v2/scrape` 发 POST，`Content-Type: application/json`，body 含 `url` 与 `formats`（如 `["markdown"]`）。
2. 解析响应：`data.markdown` 为正文，`data.metadata.title/statusCode/sourceURL` 为页面信息。
3. 无 Key，无需注册/登录。

**门槛与说明**
- 全程使用官方匿名免费档，未注册、未提供账号/Key/支付方式，未越过免费范围。
- 未遇到验证码、资质或权限阻碍；本次一次请求即成功（服务端命中缓存）。
- 匿名档存在官方限流且限额较低；若后续需要更高频率，需自行申请 API Key 并以私有文件保存，本轮不具备也不应使用。
- 未检索其他任务/历史，未调用其他 Agent，任务产物仅留在本题目录。