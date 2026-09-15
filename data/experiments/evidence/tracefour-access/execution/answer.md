api-docs 页面返回了 403，让我换个方式抓取文档并直接探测指定入口。
入口和文档都撞上了 Cloudflare 人机验证（"Just a moment..." managed challenge）。让我再做几项探测，确认是否有可直连的 API 子域或其他合法入口。
所有路径均返回 403，站点整体处于 Cloudflare 托管质询（managed challenge）之后，且不存在 api 子域。让我抓取响应头留证，并检查容器内是否有可用的浏览器环境（仅确认现状，不用于绕过质询）。
确认了硬性阻碍：响应头 `cf-mitigated: challenge` 表明 Cloudflare 对所有自动化请求发出质询。按授权范围我不绕过人机验证。现在把探测脚本、结果留档到工作目录，并把连接配置（含真实状态）存到持久目录。
接入未成功，卡点如下：

**结论：服务被 Cloudflare 人机验证拦截，无法用指定方式（REST 直连 HTTP）访问。**

**实测证据**（脚本与结果已留档 `probe-tracefour.sh` / `probe-results.txt`）：
- 指定入口 `https://tracefour.com/v1` 及 `/v1/quotes`、`/v1/health`、文档页 `/api-docs`、甚至 `/robots.txt` 全部返回 **HTTP 403**，响应头 `cf-mitigated: challenge`、`server: cloudflare`，响应体为 "Just a moment..." JavaScript 质询页（managed challenge）
- 无备用 API 子域：`api.tracefour.com` 无 DNS 记录；全站均在同一质询之后
- 容器内无浏览器/playwright；managed 质询需 JavaScript 或人工交互，且绕过反爬不在授权范围内，故未尝试绕过

**已保存**：`/home/node/service-tools/service-config.json`（入口、认证方式、状态=blocked、阻塞详情、恢复条件），`installed-tools/` 目录已建（无需依赖，REST 直连即可）。

**未完成**：未取得任何业务数据，无法验证查询功能。若要接通，需服务方提供免质询的 API 域名/令牌，或使用能通过 Cloudflare 的网络出口；后续会话可重跑探测脚本确认是否已放行。