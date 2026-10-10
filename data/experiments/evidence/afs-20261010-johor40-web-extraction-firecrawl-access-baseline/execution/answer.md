Found the persistent tools dir `/home/node/service-tools`. Now let me read the official Firecrawl docs.
Docs confirm keyless anonymous scrape. Now let me make the extraction request (single attempt, real UA).
Extraction succeeded (HTTP 200, `success:true`, title `Example Domain`, served from Firecrawl's default cache). Now saving the persistent config and private evidence.
接通成功。

**结果（示例网页 https://example.com/）**
- 页面标题：**Example Domain**
- 内容概述：example.com 是 IANA 保留、专供文档示例使用且无需授权的域名（页面提示它并非一项服务，不建议用于测试或监控）。

**调用方式（匿名免费入口，未用 Key）**
- `POST https://api.firecrawl.dev/v2/scrape`，匿名 keyless 免费；body `{"url":"https://example.com/","formats":["markdown"]}`，UA 为实名的 `agent-friendly-services/20261010`。
- 本次 HTTP 200、`success:true`、`data.metadata.title=Example Domain`、`creditsUsed:1`、`cacheState:hit`（服务默认缓存，未强制 fresh）。

**配置保存位置**（持久目录，无秘密/key）
- `/home/node/service-tools/service-config.json`（endpoint、请求体、响应字段映射、缓存与限额说明、验证记录）
- 原始证据（私有，本轮工作目录）：`evidence/scrape_example_com.response.json`、`evidence/scrape_example_com.headers.txt`

**接入步骤**
1. 读官方文档确认 keyless 匿名 scrape 支持 `POST /v2/scrape`（无需 Authorization）。
2. 用 curl 直接发单条请求，带真实 UA，`formats:["markdown"]`。
3. 从 `data.metadata.title` 取标题、`data.markdown` 取正文，落盘配置与证据。

**门槛与说明**
- 无需注册：官方明确 keyless 免费支持 Search/Scrape/Parse，因此未创建任何账号，也无已有账号可用。
- 限额未知：IP 每日有“请求数”和“积分”双重上限，超限返回 429；剩余额度官方未公开，无法推断。本次仅 1 次请求，未触发 403/429/付费限制。
- 缓存：默认 2 天缓存，本次命中缓存属正常行为，按要求保留默认缓存。
- 无硬性阻碍，接入可用。