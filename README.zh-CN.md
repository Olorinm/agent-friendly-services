<!-- 生成文件 — 修改 scripts/generate.ts，再运行 npm run generate。 -->

# Agent-Friendly Services

[English](./README.md) | 简体中文

**帮你找到能让 Agent 完成任务的服务，并用实测比较哪个更可靠、更省事、更有性价比。**

我们关注普通个人能用上的服务，收集候选，再用真实任务逐步验证。你可以按分类浏览，点服务名查看接入条件和资料，也可以直接打开文档开始使用。

<a id="all-services"></a>

## 服务目录（112）

用量和费用均为每次有效试跑的平均值，包含成功与失败；模型费用按保存的 LiteLLM 价表估算，服务费用按记录来源核验（估算额标 ~）。— 表示未知或未测。仅在相同任务版本、重复次数与配置内比较；任务、提前准备和样本可展开查看。

[旅行](#services-travel) · [数据库](#services-databases) · [网页搜索与数据](#services-web-search-data) · [协作办公与存储](#services-productivity-storage) · [AI 模型](#services-ai-models) · [Agent 工具](#services-agent-tooling) · [代码执行](#services-code-execution) · [开发工具](#services-developer-tools) · [云服务与部署](#services-cloud-hosting) · [支付与账单](#services-payments-billing) · [通信](#services-communication) · [监控与安全](#services-observability-security) · [电商与营销](#services-commerce-marketing)

<a id="services-travel"></a>

### 旅行 (26)

<a id="services-travel-flights"></a>

#### 航空机票

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="12%" align="right">Token 用量</th><th width="12%" align="right">模型费用</th><th width="12%" align="right">服务费用</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#ignav">Ignav Flights</a></td><td align="right"><a href="./generated/evaluations.md#comparison-45effe165cf4">100%</a></td><td align="right">212.9k</td><td align="right">$0.93</td><td align="right">$0</td><td align="left"><a href="https://ignav.com/docs">文档</a> · <a href="https://ignav.com/playground">网页</a> · <a href="https://ignav.com/docs">API</a> · <a href="https://ignav.com/docs/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#kiwi">Kiwi.com</a></td><td align="right"><a href="./generated/evaluations.md#comparison-c77feef961a0">100%</a></td><td align="right">209.6k</td><td align="right">$0.84</td><td align="right">$0</td><td align="left"><a href="https://www.kiwi.com/en/pages/mcp/">文档</a> · <a href="https://mcp.kiwi.com">MCP</a> · <a href="https://media.kiwi.com/articles-and-interviews/better-for-business-kiwi-com-takes-a-new-approach-to-partnerships/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#airgateway">AirGateway Platform API</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://support.airgateway.com/en-US/kb/article/4/introduction-to-airgateway-platform-api">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#amadeus-flights">Amadeus Flight APIs</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://developers.amadeus.com/blog/comparing-open-source-flight-data-sources">API</a> · <a href="https://developers.amadeus.com/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#apiheya-air-scraper">apiheya Air Scraper</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://rapidapi.com/apiheya/api/sky-scrapper/playground/apiendpoint_6856e0a6-2804-43cd-9cc0-bb377022981e">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#aviasales">Aviasales via Travelpayouts</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://support.travelpayouts.com/hc/en-us/articles/210995808-How-to-get-access-to-the-Aviasales-Search-API">API</a> · <a href="https://support.travelpayouts.com/hc/en-us/articles/203956163-Aviasales-Data-API">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#bright-data-serp">Bright Data SERP API</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://docs.brightdata.com/api-reference/serp/google-flights/currency">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#duffel-flights">Duffel Flights API</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://duffel.com/docs/api/overview/test-mode">API</a> · <a href="https://duffel.com/guides/getting-started">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#expedia-xap-flights">Expedia XAP Flight Listings</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://developers.expediagroup.com/xap-apis/api/shopping-apis/flight-listings">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#flight-mcp">Flight MCP</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://flight-mcp.com/docs">API</a> · <a href="https://flight-mcp.com/docs">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#flightapi-io">FlightAPI.io Flight Price API</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://www.flightapi.io/documentation/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#kayak-affiliate">KAYAK Affiliate API</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://developers.kayak.com/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#letsfg">LetsFG Personal Flight Search</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://letsfg.co/for-agents">MCP</a> · <a href="https://github.com/letsfg/letsfg">CLI</a> · <a href="https://github.com/letsfg/letsfg">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#lufthansa-partner">Lufthansa Partner Fare API</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://developer.lufthansa.com/page">API</a> · <a href="https://developer.lufthansa.com/docs/read/api_partner/offers">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#sabre-air">Sabre Air APIs</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://github.com/SabreDevStudio/SabreAPIsWorkflows/blob/master/SabreAPIsTestSuites/README.md">API</a> · <a href="https://developer.sabre.com/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#scrapingdog-flights">Scrapingdog Google Flights API</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://www.scrapingdog.com/documentation/google-flights-api/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#searchapi">SearchApi Google Flights</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://www.searchapi.io/docs/google-flights-api">API</a> · <a href="https://www.searchapi.io/integrations/mcp">文档</a> · <a href="https://www.searchapi.io/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#serpapi">SerpApi</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://serpapi.com/search-api">文档</a> · <a href="https://serpapi.com/google-flights-api">API</a> · <a href="https://github.com/serpapi/serpapi-mcp">MCP</a> · <a href="https://serpapi.com/search-api">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#skootle-google-flights">Skootle Google Flights Scraper</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://apify.com/skootle/google-flights-scraper">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#skyscanner">Skyscanner Travel APIs</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://developers.skyscanner.net/docs/getting-started/authentication">API</a> · <a href="https://developers.skyscanner.net/docs/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#travelport-tripservices">Travelport TripServices</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://developer.travelport.com/docs/getting-started">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#trip-com-flights">Trip.com Flight Distribution</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#qunar-flights">去哪儿机票合作</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#tongcheng-flights">同程机票合作</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#ctrip-flights">携程机票合作</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#fliggy-domestic-flights">飞猪国内机票开放平台</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://open.alitrip.com/businessDetail.htm?tagId=85">API</a></td></tr>
</tbody>
</table>

现有试跑的任务或条件尚未统一，暂不排名。

<details>
<summary>测了什么，怎么测的</summary>

**任务：找到9月25日米兰飞往荷兰的机票**

2026-09-25；本题出发范围约定为MXP/LIN/BGY，抵达荷兰任一客运机场；1名成人、单程、经济舱，允许中转；本轮指定的服务入口

完成标准：至少一个符合条件的航班方案，包含各航段机场、航班号、当地起降日期时间、搜索报价与币种，以及查询来源；至少一个方案满足日期、路线和旅客条件；关键信息与执行器取得的真实服务响应相符。仅验搜索结果，不验全网最低价或支付成功

| 服务 | 本次使用的入口 | 提前准备 | 样本 |
| --- | --- | --- | --- |
| Ignav Flights | [网页 Playground](https://ignav.com/playground) | 未提供账号或密钥 | [1 次](./generated/evaluations.md#comparison-45effe165cf4) |
| Kiwi.com | [MCP](https://mcp.kiwi.com) | 未提供账号或密钥 | [1 次](./generated/evaluations.md#comparison-c77feef961a0) |

**测试配置：** codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 分钟 · 2026-09-07（UTC）。

部分早期记录缺少环境信息，尚待统一复跑。 Ignav Flights 的网页试跑成绩不代表其 API 或 MCP 的表现。

[任务定义](./data/experiments/tasks/travel-flights.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-databases"></a>

### 数据库 (13)

<a id="services-databases-hosted-relational"></a>

#### 托管关系型数据库

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="12%" align="right">Token 用量</th><th width="12%" align="right">模型费用</th><th width="12%" align="right">服务费用</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#neon">Neon</a></td><td align="right"><a href="./generated/evaluations.md#comparison-fdecec09a4b6">100%</a></td><td align="right">465.4k</td><td align="right">—</td><td align="right">$0</td><td align="left"><a href="https://neon.com/docs">文档</a> · <a href="https://neon.new/">API</a> · <a href="https://api-docs.neon.tech">API</a> · <a href="https://neon.com/docs/reference/neon-cli">CLI</a> · <a href="https://github.com/neondatabase/mcp-server-neon">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#turso">Turso</a></td><td align="right"><a href="./generated/evaluations.md#comparison-1420586eae17">100%</a></td><td align="right">767.6k</td><td align="right">—</td><td align="right">$0</td><td align="left"><a href="https://docs.turso.tech/cli/introduction">CLI</a> · <a href="https://docs.turso.tech/api-reference/introduction">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#aiven">Aiven</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://aiven.io/docs/tools/cli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#cloudflare">Cloudflare</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://developers.cloudflare.com">文档</a> · <a href="https://developers.cloudflare.com/d1/get-started/">CLI</a> · <a href="https://developers.cloudflare.com/api/">API</a> · <a href="https://developers.cloudflare.com/workers/wrangler/">CLI</a> · <a href="https://developers.cloudflare.com/fundamentals/api/reference/sdks/">SDK</a> · <a href="https://github.com/cloudflare/mcp-server-cloudflare">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#planetscale">PlanetScale</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://planetscale.com/docs/cli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#supabase">Supabase</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://supabase.com/docs">文档</a> · <a href="https://supabase.com/docs/guides/api">API</a> · <a href="https://supabase.com/docs/reference/api/introduction">API</a> · <a href="https://supabase.com/docs/guides/cli">CLI</a> · <a href="https://supabase.com/docs/reference">SDK</a> · <a href="https://supabase.com/docs/guides/getting-started/mcp">MCP</a></td></tr>
</tbody>
</table>

现有试跑的任务或条件尚未统一，暂不排名。

<details>
<summary>测了什么，怎么测的</summary>

**任务：为我的个人待办应用准备一个独立的远程数据库，验证新增、修改和重新连接后读取待办事项**

仅合成测试数据：id=1,title=Buy milk,done=false；id=2,title=Read book,done=false；id=3,title=Walk dog,done=true。写入三项，再把 id=2 改为 done=true。允许创建无需付费的临时数据库；不能动已有项目

完成标准：保存数据后结束写入进程，用另一个全新进程连接同一远程数据库，返回按 id 排序的全部待办、未完成项及总数/完成数；说明资源到期或免费限制；提供可核对的非敏感请求、SQL、真实响应、分开进程执行的证据；实际在指定服务的远程数据库中保存和更新；新进程读回三项且只有 id=1 未完成，总数3、完成数2，标题未变；证据证明独立连接和远程执行。凭据只保存在工作目录私有文件，不得进入 evidence 或最终答案。限时资源可完成此题，但必须明确到期限制

| 服务 | 本次使用的入口 | 提前准备 | 样本 |
| --- | --- | --- | --- |
| Neon | [API](https://neon.new/) | 未提供账号或密钥 | [1 次](./generated/evaluations.md#comparison-fdecec09a4b6) |
| Turso | [API](https://docs.turso.tech/api-reference/introduction) | [已提供本服务凭据](./generated/evaluations.md#comparison-1420586eae17) | [1 次](./generated/evaluations.md#comparison-1420586eae17) |

**测试配置：** codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 分钟 · 2026-09-07（UTC）。

提前准备不计入上表的 Token 用量和耗时，具体步骤见准备详情。

[任务定义](./data/experiments/tasks/databases.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-databases-other"></a>

#### 其他服务

尚未实测

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="48%" align="left">用途</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#chroma">Chroma</a></td><td align="left">Open-source embedding database with a hosted Chroma Cloud, official CLI, official MCP server, and llms.txt.</td><td align="left"><a href="https://docs.trychroma.com">文档</a> · <a href="https://docs.trychroma.com/docs/overview/introduction">API</a> · <a href="https://docs.trychroma.com/docs/cli/install">CLI</a> · <a href="https://github.com/chroma-core/chroma-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#mongodb-atlas">MongoDB Atlas</a></td><td align="left">Managed MongoDB with a versioned Admin API, published OpenAPI spec, llms.txt, official CLI and MCP server.</td><td align="left"><a href="https://www.mongodb.com/docs/atlas/">文档</a> · <a href="https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/">API</a> · <a href="https://www.mongodb.com/docs/atlas/cli/">CLI</a> · <a href="https://www.mongodb.com/docs/drivers/">SDK</a> · <a href="https://github.com/mongodb-js/mongodb-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#pinecone">Pinecone</a></td><td align="left">Managed vector database for search and RAG, with llms.txt, an official MCP server, and self-serve keys.</td><td align="left"><a href="https://docs.pinecone.io">文档</a> · <a href="https://docs.pinecone.io/reference/api/introduction">API</a> · <a href="https://github.com/pinecone-io/cli">CLI</a> · <a href="https://docs.pinecone.io/guides/operations/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#qdrant">Qdrant</a></td><td align="left">Open-source vector database with a managed cloud, llms.txt, an official MCP server, and a free cluster tier.</td><td align="left"><a href="https://qdrant.tech/documentation">文档</a> · <a href="https://api.qdrant.tech">API</a> · <a href="https://qdrant.tech/documentation/interfaces">SDK</a> · <a href="https://github.com/qdrant/mcp-server-qdrant">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#redis">Redis (Redis Cloud)</a></td><td align="left">In-memory data platform for caching, vector search and real-time apps; Redis Cloud has a REST management API, official MCP server, redis-cli, and llms.txt.</td><td align="left"><a href="https://redis.io/docs/latest">文档</a> · <a href="https://redis.io/docs/latest/operate/rc/api/">API</a> · <a href="https://redis.io/docs/latest/develop/tools/cli/">CLI</a> · <a href="https://github.com/redis/mcp-redis">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#upstash">Upstash</a></td><td align="left">Serverless Redis, Kafka-successor queues, and vector storage with REST APIs, llms.txt, an official MCP server, and a free tier.</td><td align="left"><a href="https://upstash.com/docs">文档</a> · <a href="https://upstash.com/docs/devops/developer-api/introduction">API</a> · <a href="https://github.com/upstash/cli">CLI</a> · <a href="https://github.com/upstash/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#weaviate">Weaviate</a></td><td align="left">Open-source vector database with REST/GraphQL/gRPC APIs, Weaviate Cloud free sandboxes, an official CLI, MCP server, and llms.txt.</td><td align="left"><a href="https://docs.weaviate.io">文档</a> · <a href="https://docs.weaviate.io/weaviate/api/rest">API</a> · <a href="https://github.com/weaviate/weaviate-cli">CLI</a> · <a href="https://github.com/weaviate/mcp-server-weaviate">MCP</a></td></tr>
</tbody>
</table>

<a id="services-web-search-data"></a>

### 网页搜索与数据 (10)

<a id="services-web-search-data-web-search"></a>

#### 网页搜索

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="12%" align="right">Token 用量</th><th width="12%" align="right">模型费用</th><th width="12%" align="right">服务费用</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#exa">Exa / public-mcp</a></td><td align="right"><a href="./generated/evaluations.md#comparison-87ab787b88b3">100%</a></td><td align="right">931.5k</td><td align="right">—</td><td align="right">$0</td><td align="left"><a href="https://docs.exa.ai">文档</a> · <a href="https://exa.ai/docs/reference/exa-mcp">文档</a> · <a href="https://mcp.exa.ai/mcp">MCP</a> · <a href="https://exa.ai/docs/reference/search">API</a> · <a href="https://docs.exa.ai/reference/getting-started">API</a> · <a href="https://docs.exa.ai/sdks/typescript-sdk-specification">SDK</a> · <a href="https://github.com/exa-labs/exa-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#exa">Exa / search-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-9dbe771526ac">0%</a></td><td align="right">—</td><td align="right">—</td><td align="right">$0</td><td align="left"><a href="https://docs.exa.ai">文档</a> · <a href="https://exa.ai/docs/reference/exa-mcp">文档</a> · <a href="https://mcp.exa.ai/mcp">MCP</a> · <a href="https://exa.ai/docs/reference/search">API</a> · <a href="https://docs.exa.ai/reference/getting-started">API</a> · <a href="https://docs.exa.ai/sdks/typescript-sdk-specification">SDK</a> · <a href="https://github.com/exa-labs/exa-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#firecrawl">Firecrawl</a></td><td align="right"><a href="./generated/evaluations.md#comparison-b5f21fc39ab4">100%</a></td><td align="right">346.8k</td><td align="right">—</td><td align="right">$0</td><td align="left"><a href="https://docs.firecrawl.dev">文档</a> · <a href="https://docs.firecrawl.dev/features/search">API</a> · <a href="https://docs.firecrawl.dev/api-reference/introduction">API</a> · <a href="https://docs.firecrawl.dev/sdks/overview">SDK</a> · <a href="https://docs.firecrawl.dev/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#brave-search">Brave Search API</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://api-dashboard.search.brave.com/app/documentation">文档</a> · <a href="https://brave.com/search/api/">API</a> · <a href="https://github.com/brave/brave-search-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#serpapi">SerpApi</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://serpapi.com/search-api">文档</a> · <a href="https://serpapi.com/google-flights-api">API</a> · <a href="https://github.com/serpapi/serpapi-mcp">MCP</a> · <a href="https://serpapi.com/search-api">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#serper">Serper</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://serper.dev/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#tavily">Tavily</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://docs.tavily.com">文档</a> · <a href="https://docs.tavily.com/documentation/quickstart">API</a> · <a href="https://docs.tavily.com/documentation/api-reference/introduction">API</a> · <a href="https://docs.tavily.com/sdk">SDK</a> · <a href="https://docs.tavily.com/documentation/mcp">MCP</a></td></tr>
</tbody>
</table>

现有试跑的任务或条件尚未统一，暂不排名。

<details>
<summary>测了什么，怎么测的</summary>

**任务：我准备把 Python 应用升级到 3.13，查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并给出官方依据**

目标版本 Python 3.13；官方来源范围 python.org；使用本轮指定搜索服务发现来源，可直接读取它返回的来源页面；不依赖模型记忆或其他搜索引擎提供答案

完成标准：中文简答覆盖默认状态、启用方式、C 扩展兼容性；至少两个不同的官方页面 URL；每个结论对应来源内容；保存指定服务的搜索请求与真实响应、所用网页内容和访问时间；三个问题均有正确答案且由 Python 3.13 官方资料支持；至少两个不同官方 URL 出现在指定服务的真实搜索响应中；证据可核对。直接抓取搜索返回页面允许，但内置联网检索只可用于服务接入文档，不能替代被测搜索

| 服务 | 本次使用的入口 | 提前准备 | 样本 |
| --- | --- | --- | --- |
| Exa | [MCP](https://mcp.exa.ai/mcp) | 未提供账号或密钥 | [1 次](./generated/evaluations.md#comparison-87ab787b88b3) |
| Exa | [API](https://exa.ai/docs/reference/search) | [已提供本服务凭据](./generated/evaluations.md#comparison-9dbe771526ac) | [1 次](./generated/evaluations.md#comparison-9dbe771526ac) |
| Firecrawl | [API](https://docs.firecrawl.dev/features/search) | 未提供账号或密钥 | [1 次](./generated/evaluations.md#comparison-b5f21fc39ab4) |

**测试配置：** codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 分钟 · 2026-09-07（UTC）。

提前准备不计入上表的 Token 用量和耗时，具体步骤见准备详情。

[任务定义](./data/experiments/tasks/web-search.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-web-search-data-other"></a>

#### 其他服务

尚未实测

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="48%" align="left">用途</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#apify">Apify</a></td><td align="left">Web scraping and automation platform with thousands of ready-made actors, a versioned API, llms.txt, and an official MCP server.</td><td align="left"><a href="https://docs.apify.com">文档</a> · <a href="https://docs.apify.com/api/v2">API</a> · <a href="https://docs.apify.com/cli">CLI</a> · <a href="https://docs.apify.com/sdk">SDK</a> · <a href="https://docs.apify.com/platform/integrations/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#jina">Jina AI</a></td><td align="left">Search-foundation APIs (Reader for URL-to-markdown, embeddings, reranker, deep search) with an official remote MCP server, an agent-targeted llms.txt, and a keyless trial path.</td><td align="left"><a href="https://docs.jina.ai">文档</a> · <a href="https://docs.jina.ai">API</a> · <a href="https://github.com/jina-ai/MCP">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#perplexity">Perplexity API</a></td><td align="left">Sonar API for web-grounded answers and search, with llms.txt, an official MCP server, and documented usage tiers.</td><td align="left"><a href="https://docs.perplexity.ai">文档</a> · <a href="https://github.com/ppl-ai/modelcontextprotocol">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#xquik">Xquik</a></td><td align="left">Hosted X data and account automation service with a REST API, official MCP server, OpenAPI, SDKs, HMAC webhooks, and OAuth 2.1.</td><td align="left"><a href="https://docs.xquik.com">文档</a> · <a href="https://docs.xquik.com/api-reference/overview">API</a> · <a href="https://docs.xquik.com/sdks">SDK</a> · <a href="https://docs.xquik.com/mcp/overview">MCP</a></td></tr>
</tbody>
</table>

<a id="services-productivity-storage"></a>

### 协作办公与存储 (10)

<a id="services-productivity-storage-collaborative-tables"></a>

#### 在线任务表

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="12%" align="right">Token 用量</th><th width="12%" align="right">模型费用</th><th width="12%" align="right">服务费用</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#grist">Grist</a></td><td align="right"><a href="./generated/evaluations.md#comparison-6203194a76cd">100%</a></td><td align="right">540.8k</td><td align="right">—</td><td align="right">$0</td><td align="left"><a href="https://support.getgrist.com/api/">API</a> · <a href="https://docs.getgrist.com/api/mcp">MCP</a> · <a href="https://pypi.org/project/grist-api/">SDK</a> · <a href="https://www.npmjs.com/package/grist-api">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#notion">Notion</a></td><td align="right"><a href="./generated/evaluations.md#comparison-6203194a76cd">100%</a></td><td align="right">215.5k</td><td align="right">$0.75</td><td align="right">$0</td><td align="left"><a href="https://developers.notion.com">文档</a> · <a href="https://developers.notion.com/reference/intro">API</a> · <a href="https://github.com/makenotion/notion-sdk-js">SDK</a> · <a href="https://developers.notion.com/cli/get-started/overview">CLI</a> · <a href="https://mcp.notion.com/mcp">MCP</a> · <a href="https://developers.notion.com/docs/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#airtable">Airtable</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://airtable.com/developers">文档</a> · <a href="https://airtable.com/developers/web/api/introduction">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#baserow">Baserow Cloud</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://baserow.io/docs/apis/rest-api">API</a> · <a href="https://baserow.io/user-docs/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#coda">Coda / Superhuman Docs</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://coda.io/developers/apis/v1">API</a> · <a href="https://coda.io/apis/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#google-sheets">Google Sheets</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://developers.google.com/workspace/sheets/api/guides/concepts">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#lark">Lark</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://open.larksuite.com/document/home/index">文档</a> · <a href="https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create">API</a> · <a href="https://github.com/larksuite/cli">CLI</a> · <a href="https://github.com/larksuite/lark-openapi-mcp">MCP</a> · <a href="https://open.larksuite.com/document/server-docs/getting-started/server-api-list">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#feishu">飞书 Feishu</a></td><td align="right">待实测</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/create">API</a> · <a href="https://github.com/larksuite/cli">CLI</a> · <a href="https://github.com/larksuite/lark-openapi-mcp">MCP</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我把这份读书会会议记录里的待办整理成在线任务表，给我链接，再告诉我还有哪些没完成、各自什么时候到期。**

读书会筹备会记录（2026年9月8日）：林青负责确认场地，9月15日前搞定；周舟负责整理书单，9月16日前完成；陈禾负责制作海报，原定9月18日完成。这三件事开会时都还没做完。会后补充：周舟说书单已经整理好了，海报的截止时间改到9月20日，其他安排不变。

完成标准：可访问的私有在线任务表链接；未完成事项及负责人、截止日期；远端表中恰好包含三项行动、负责人和最终截止日期正确、书单已完成且另两项未完成；答复给出该表链接并正确列出两项未完成事项及日期；准备者通过服务API独立读取确认。允许自由选择字段与操作顺序，不要求先写入旧状态或输出证据文件

| 服务 | 本次使用的入口 | 提前准备 | 样本 |
| --- | --- | --- | --- |
| Grist | [API](https://support.getgrist.com/api/) | [已提供本服务凭据](./generated/evaluations.md#comparison-6203194a76cd) | [1 次](./generated/evaluations.md#comparison-6203194a76cd) |
| Notion | [API](https://developers.notion.com/reference/intro) | [已提供本服务凭据](./generated/evaluations.md#comparison-6203194a76cd) | [1 次](./generated/evaluations.md#comparison-6203194a76cd) |

**测试配置：** codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 分钟 · 2026-09-08（UTC）。

提前准备不计入上表的 Token 用量和耗时，具体步骤见准备详情。

[任务定义](./data/experiments/tasks/collaborative-tables.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-productivity-storage-other"></a>

#### 其他服务

尚未实测

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="48%" align="left">用途</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#dropbox">Dropbox</a></td><td align="left">File storage and sync with a scoped-OAuth HTTP API, self-serve app creation, and webhooks.</td><td align="left"><a href="https://www.dropbox.com/developers/documentation">文档</a> · <a href="https://www.dropbox.com/developers/documentation/http/documentation">API</a> · <a href="https://github.com/dropbox/dbxcli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#linear">Linear</a></td><td align="left">Issue tracking and product planning with a GraphQL API, llms.txt, an official MCP server, and webhooks.</td><td align="left"><a href="https://linear.app/developers">文档</a> · <a href="https://linear.app/docs/mcp">MCP</a></td></tr>
</tbody>
</table>

<a id="services-ai-models"></a>

### AI 模型 (23)

尚未实测

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="48%" align="left">用途</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#qwen">Alibaba Qwen (Model Studio)</a></td><td align="left">Qwen model family via Alibaba Cloud Model Studio's OpenAI-compatible API, with an official open-source coding CLI agent (qwen-code).</td><td align="left"><a href="https://www.alibabacloud.com/help/en/model-studio/">文档</a> · <a href="https://www.alibabacloud.com/help/en/model-studio/models">API</a> · <a href="https://github.com/QwenLM/qwen-code">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#anthropic">Anthropic</a></td><td align="left">Claude model APIs with agent-focused documentation, llms.txt, and the company behind the MCP standard itself.</td><td align="left"><a href="https://docs.anthropic.com">文档</a> · <a href="https://docs.anthropic.com/en/api">API</a> · <a href="https://docs.anthropic.com/en/docs/claude-code">CLI</a> · <a href="https://docs.anthropic.com/en/api/client-sdks">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#cartesia">Cartesia</a></td><td align="left">Low-latency voice models (Sonic TTS, Ink STT) with a documented API, official MCP server, llms.txt, and a free tier.</td><td align="left"><a href="https://docs.cartesia.ai">文档</a> · <a href="https://docs.cartesia.ai/api-reference">API</a> · <a href="https://github.com/cartesia-ai/cartesia-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#cerebras">Cerebras Inference</a></td><td align="left">Wafer-scale inference for open models at very high tokens/sec, OpenAI-compatible API, llms.txt, and a standing free tier.</td><td align="left"><a href="https://inference-docs.cerebras.ai">文档</a> · <a href="https://inference-docs.cerebras.ai/api-reference/chat-completions">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#cohere">Cohere</a></td><td align="left">Enterprise LLM platform (command, embed, rerank) with llms.txt, documented API versioning, free trial keys, and error/rate-limit docs.</td><td align="left"><a href="https://docs.cohere.com">文档</a> · <a href="https://docs.cohere.com/reference/about">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#deepgram">Deepgram</a></td><td align="left">Speech-to-text and voice AI API with a public OpenAPI spec, llms.txt, scoped API keys, and $200 free credit without a card.</td><td align="left"><a href="https://developers.deepgram.com/docs">文档</a> · <a href="https://developers.deepgram.com/reference">API</a> · <a href="https://developers.deepgram.com/docs/deepgram-sdks">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#deepseek">DeepSeek</a></td><td align="left">OpenAI-compatible LLM API (DeepSeek-V3/R1) with transparent per-token pricing, a detailed changelog, and self-serve keys.</td><td align="left"><a href="https://api-docs.deepseek.com">文档</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#elevenlabs">ElevenLabs</a></td><td align="left">Voice AI (TTS, STT, agents) with a public OpenAPI spec, llms.txt, an official MCP server, and a free tier.</td><td align="left"><a href="https://elevenlabs.io/docs">文档</a> · <a href="https://elevenlabs.io/docs/api-reference/introduction">API</a> · <a href="https://github.com/elevenlabs/elevenlabs-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fal">fal.ai</a></td><td align="left">Generative media platform (image, video, audio models) with queue/streaming APIs, an official CLI/serving framework, llms.txt, and self-serve keys.</td><td align="left"><a href="https://fal.ai/docs">文档</a> · <a href="https://fal.ai/docs/model-apis">API</a> · <a href="https://github.com/fal-ai/fal">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fireworks">Fireworks AI</a></td><td align="left">Fast open-model inference and fine-tuning with an OpenAI-compatible API, official firectl CLI, llms.txt, and published pricing.</td><td align="left"><a href="https://docs.fireworks.ai">文档</a> · <a href="https://docs.fireworks.ai/api-reference/introduction">API</a> · <a href="https://docs.fireworks.ai/tools-sdks/firectl/firectl">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#gemini-api">Gemini API</a></td><td align="left">Google's Gemini model APIs via AI Studio, with generous free tier and documented API versioning.</td><td align="left"><a href="https://ai.google.dev/gemini-api/docs">文档</a> · <a href="https://ai.google.dev/api">API</a> · <a href="https://github.com/google-gemini/gemini-cli">CLI</a> · <a href="https://ai.google.dev/gemini-api/docs/libraries">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#groq">Groq</a></td><td align="left">Ultra-low-latency LLM inference with an OpenAI-compatible API, llms.txt, and self-serve keys with a free tier.</td><td align="left"><a href="https://console.groq.com/docs">文档</a> · <a href="https://console.groq.com/docs/api-reference">API</a> · <a href="https://console.groq.com/docs/libraries">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#hugging-face">Hugging Face</a></td><td align="left">Model hub and inference platform with fine-grained tokens, OAuth, an official MCP server, and a full Hub API.</td><td align="left"><a href="https://huggingface.co/docs">文档</a> · <a href="https://huggingface.co/docs/hub/api">API</a> · <a href="https://huggingface.co/docs/huggingface_hub/guides/cli">CLI</a> · <a href="https://huggingface.co/docs/huggingface_hub">SDK</a> · <a href="https://huggingface.co/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#luma">Luma AI (Dream Machine)</a></td><td align="left">Dream Machine video and image generation via the Luma API, with llms.txt and published API pricing.</td><td align="left"><a href="https://docs.lumalabs.ai">文档</a> · <a href="https://docs.lumalabs.ai/reference">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#minimax">MiniMax</a></td><td align="left">MiniMax text, speech, video and music models via the international platform API, with an official MCP server.</td><td align="left"><a href="https://platform.minimax.io/docs">文档</a> · <a href="https://platform.minimax.io/docs/api-reference">API</a> · <a href="https://github.com/MiniMax-AI/MiniMax-MCP">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#mistral">Mistral AI</a></td><td align="left">European LLM provider (La Plateforme) with llms.txt, an open OpenAPI-based docs repo, a free experiment tier, and self-serve keys.</td><td align="left"><a href="https://docs.mistral.ai">文档</a> · <a href="https://docs.mistral.ai/api">API</a> · <a href="https://docs.mistral.ai/getting-started/clients">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#moonshot">Moonshot AI (Kimi)</a></td><td align="left">Kimi models (K2 line) via an OpenAI-compatible API on the international Kimi platform, with an official terminal CLI agent (kimi-cli).</td><td align="left"><a href="https://platform.kimi.ai/docs">文档</a> · <a href="https://platform.kimi.ai/docs/api/chat">API</a> · <a href="https://github.com/MoonshotAI/kimi-cli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#openai">OpenAI</a></td><td align="left">GPT model APIs with an official OpenAPI spec, agents guides, and a large SDK ecosystem.</td><td align="left"><a href="https://developers.openai.com/api/docs">文档</a> · <a href="https://platform.openai.com/docs/api-reference">API</a> · <a href="https://platform.openai.com/docs/libraries">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#openrouter">OpenRouter</a></td><td align="left">Unified OpenAI-compatible API over hundreds of models from many labs, with one key, per-model pricing, automatic fallbacks, and an llms.txt.</td><td align="left"><a href="https://openrouter.ai/docs">文档</a> · <a href="https://openrouter.ai/docs/api-reference/overview">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#replicate">Replicate</a></td><td align="left">Run and fine-tune open-source models via a simple predictions API, with llms.txt, webhooks, and an official CLI.</td><td align="left"><a href="https://replicate.com/docs">文档</a> · <a href="https://replicate.com/docs/reference/http">API</a> · <a href="https://github.com/replicate/cli">CLI</a> · <a href="https://replicate.com/docs/reference/client-libraries">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#together-ai">Together AI</a></td><td align="left">Inference and fine-tuning platform for open-source models with an OpenAI-compatible API and llms.txt.</td><td align="left"><a href="https://docs.together.ai">文档</a> · <a href="https://docs.together.ai/reference/chat-completions">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#xai">xAI (Grok API)</a></td><td align="left">xAI's Grok models via an OpenAI-compatible REST API, with an llms.txt and self-serve console keys.</td><td align="left"><a href="https://docs.x.ai">文档</a> · <a href="https://docs.x.ai/developers/rest-api-reference/inference">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#zai">Z.ai (GLM)</a></td><td align="left">GLM models via Z.ai's OpenAI-compatible international API, with llms.txt, published pricing, and self-serve keys.</td><td align="left"><a href="https://docs.z.ai">文档</a> · <a href="https://docs.z.ai/api-reference">API</a></td></tr>
</tbody>
</table>

<a id="services-agent-tooling"></a>

### Agent 工具 (5)

尚未实测

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="48%" align="left">用途</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#composio">Composio</a></td><td align="left">Tool and integration layer for AI agents (hundreds of app connectors with managed auth), with llms.txt and a hosted MCP directory.</td><td align="left"><a href="https://docs.composio.dev">文档</a> · <a href="https://mcp.composio.dev">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#mem0">Mem0</a></td><td align="left">Memory layer for AI agents (hosted platform + open-source), with REST API, llms.txt, and the official OpenMemory MCP server.</td><td align="left"><a href="https://docs.mem0.ai">文档</a> · <a href="https://docs.mem0.ai/api-reference">API</a> · <a href="https://docs.mem0.ai/openmemory/overview">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#n8n">n8n</a></td><td align="left">Workflow automation platform with native AI/agent nodes, a public REST API, official hosted MCP server, CLI, and llms.txt; fair-code and self-hostable.</td><td align="left"><a href="https://docs.n8n.io">文档</a> · <a href="https://docs.n8n.io/api/">API</a> · <a href="https://docs.n8n.io/hosting/cli-commands/">CLI</a> · <a href="https://docs.n8n.io/connect/connect-to-n8n-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#vapi">Vapi</a></td><td align="left">Voice-agent orchestration API (calls, turn-taking, tool use over phone/web) with an official MCP server and an llms.txt that opens with instructions for AI agents.</td><td align="left"><a href="https://docs.vapi.ai">文档</a> · <a href="https://docs.vapi.ai/api-reference">API</a> · <a href="https://github.com/VapiAI/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#zapier">Zapier</a></td><td align="left">Automation platform bridging 7000+ apps, with llms.txt and an official MCP endpoint that gives agents access to those integrations.</td><td align="left"><a href="https://docs.zapier.com">文档</a> · <a href="https://github.com/zapier/zapier-platform">CLI</a> · <a href="https://zapier.com/mcp">MCP</a></td></tr>
</tbody>
</table>

<a id="services-code-execution"></a>

### 代码执行 (4)

尚未实测

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="48%" align="left">用途</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#browserbase">Browserbase</a></td><td align="left">Headless browser infrastructure for AI agents and automation, with session APIs and an official MCP server.</td><td align="left"><a href="https://docs.browserbase.com">文档</a> · <a href="https://docs.browserbase.com/reference">API</a> · <a href="https://docs.browserbase.com/reference">SDK</a> · <a href="https://github.com/browserbase/mcp-server-browserbase">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#e2b">E2B</a></td><td align="left">Isolated cloud sandboxes for running AI-generated code, with llms.txt, an official MCP server, and self-serve keys.</td><td align="left"><a href="https://e2b.dev/docs">文档</a> · <a href="https://e2b.dev/docs/cli">CLI</a> · <a href="https://e2b.dev/docs/sdk-reference">SDK</a> · <a href="https://github.com/e2b-dev/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#modal">Modal</a></td><td align="left">Serverless compute for Python with first-class Sandboxes for agent code execution, llms.txt, and an official CLI.</td><td align="left"><a href="https://modal.com/docs">文档</a> · <a href="https://modal.com/docs/reference">API</a> · <a href="https://modal.com/docs/reference/cli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#steel">Steel</a></td><td align="left">Cloud browser API for AI agents (sessions, CDP, anti-bot) — open-source and self-hostable, with llms.txt and a free tier.</td><td align="left"><a href="https://docs.steel.dev">文档</a> · <a href="https://docs.steel.dev/api-reference">API</a></td></tr>
</tbody>
</table>

<a id="services-developer-tools"></a>

### 开发工具 (4)

尚未实测

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="48%" align="left">用途</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#atlassian">Atlassian (Jira &amp; Confluence)</a></td><td align="left">Jira, Confluence and the Atlassian Cloud platform — REST APIs, an official remote MCP server (OAuth 2.1), and the acli CLI.</td><td align="left"><a href="https://developer.atlassian.com">文档</a> · <a href="https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/">API</a> · <a href="https://developer.atlassian.com/cloud/acli/">CLI</a> · <a href="https://github.com/atlassian/atlassian-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#github">GitHub</a></td><td align="left">Code hosting, collaboration, and automation with REST and GraphQL APIs, an official CLI, and an official MCP server.</td><td align="left"><a href="https://docs.github.com">文档</a> · <a href="https://docs.github.com/rest">API</a> · <a href="https://cli.github.com">CLI</a> · <a href="https://github.com/octokit">SDK</a> · <a href="https://github.com/github/github-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#gitlab">GitLab</a></td><td align="left">DevOps platform with REST and GraphQL APIs, scoped tokens, llms.txt, and an official CLI.</td><td align="left"><a href="https://docs.gitlab.com">文档</a> · <a href="https://docs.gitlab.com/api/rest/">API</a> · <a href="https://gitlab.com/gitlab-org/cli">CLI</a> · <a href="https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#postman">Postman</a></td><td align="left">API development platform with a public Postman API, llms.txt, official CLI, and self-serve keys.</td><td align="left"><a href="https://learning.postman.com">文档</a> · <a href="https://learning.postman.com/docs/developer/postman-api/intro-api/">API</a> · <a href="https://learning.postman.com/docs/postman-cli/postman-cli-overview/">CLI</a> · <a href="https://github.com/postmanlabs/postman-mcp-server">MCP</a></td></tr>
</tbody>
</table>

<a id="services-cloud-hosting"></a>

### 云服务与部署 (6)

尚未实测

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="48%" align="left">用途</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#cloudflare">Cloudflare</a></td><td align="left">Edge network, Workers serverless platform, storage, and AI services with agent-focused docs and official MCP servers.</td><td align="left"><a href="https://developers.cloudflare.com">文档</a> · <a href="https://developers.cloudflare.com/d1/get-started/">CLI</a> · <a href="https://developers.cloudflare.com/api/">API</a> · <a href="https://developers.cloudflare.com/workers/wrangler/">CLI</a> · <a href="https://developers.cloudflare.com/fundamentals/api/reference/sdks/">SDK</a> · <a href="https://github.com/cloudflare/mcp-server-cloudflare">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fly-io">Fly.io</a></td><td align="left">Run full-stack apps and machines close to users, with a spec'd Machines API, scoped macaroon tokens, and official MCP docs.</td><td align="left"><a href="https://fly.io/docs">文档</a> · <a href="https://fly.io/docs/machines/api/">API</a> · <a href="https://fly.io/docs/flyctl/">CLI</a> · <a href="https://fly.io/docs/mcp/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#netlify">Netlify</a></td><td align="left">Web platform for deploying sites and functions, with an OpenAPI-specified API, llms.txt, official CLI and MCP server.</td><td align="left"><a href="https://docs.netlify.com">文档</a> · <a href="https://open-api.netlify.com">API</a> · <a href="https://docs.netlify.com/cli/get-started/">CLI</a> · <a href="https://docs.netlify.com/welcome/build-with-ai/netlify-mcp-server/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#railway">Railway</a></td><td align="left">App/database hosting with a public GraphQL API, official CLI, llms.txt, and usage-based pricing.</td><td align="left"><a href="https://docs.railway.com">文档</a> · <a href="https://docs.railway.com/reference/public-api">API</a> · <a href="https://github.com/railwayapp/cli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#render">Render</a></td><td align="left">Cloud hosting for web services, static sites and databases with a REST API, official CLI, official MCP server, and llms.txt.</td><td align="left"><a href="https://render.com/docs">文档</a> · <a href="https://api-docs.render.com/reference/introduction">API</a> · <a href="https://github.com/render-oss/cli">CLI</a> · <a href="https://github.com/render-oss/render-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#vercel">Vercel</a></td><td align="left">Frontend cloud for deploying web apps, with a REST API, CLI, official MCP server, and AI SDK ecosystem.</td><td align="left"><a href="https://vercel.com/docs">文档</a> · <a href="https://vercel.com/docs/rest-api">API</a> · <a href="https://vercel.com/docs/cli">CLI</a> · <a href="https://vercel.com/docs/rest-api/sdk">SDK</a> · <a href="https://vercel.com/docs/mcp/vercel-mcp">MCP</a></td></tr>
</tbody>
</table>

<a id="services-payments-billing"></a>

### 支付与账单 (4)

尚未实测

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="48%" align="left">用途</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#lemonsqueezy">Lemon Squeezy</a></td><td align="left">Merchant-of-record payments for digital products/SaaS with a JSON:API REST API, documented test mode, and self-serve keys.</td><td align="left"><a href="https://docs.lemonsqueezy.com">文档</a> · <a href="https://docs.lemonsqueezy.com/api">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#paas-build">paas.build</a></td><td align="left">Agent-native payment facilitator (the AI-builder product of UniPaaS, FCA-authorised No. 929994) — opens a real merchant account via progressive KYB and creates checkouts through MCP or REST.</td><td align="left"><a href="https://paas.build/agents">文档</a> · <a href="https://github.com/UNIPaaS/paas-build-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#paddle">Paddle</a></td><td align="left">Merchant-of-record billing platform with a versioned API, full sandbox, llms.txt, and webhooks.</td><td align="left"><a href="https://developer.paddle.com">文档</a> · <a href="https://developer.paddle.com/api-reference/overview">API</a> · <a href="https://github.com/PaddleHQ/paddle-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#stripe">Stripe</a></td><td align="left">Payments, billing, subscriptions, and financial infrastructure with a famously complete API surface.</td><td align="left"><a href="https://docs.stripe.com">文档</a> · <a href="https://docs.stripe.com/api">API</a> · <a href="https://docs.stripe.com/stripe-cli">CLI</a> · <a href="https://docs.stripe.com/sdks">SDK</a> · <a href="https://docs.stripe.com/mcp">MCP</a></td></tr>
</tbody>
</table>

<a id="services-communication"></a>

### 通信 (6)

尚未实测

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="48%" align="left">用途</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#discord">Discord</a></td><td align="left">Chat platform with a versioned bot/OAuth2 API, official OpenAPI spec (preview), webhooks, and documented rate limits.</td><td align="left"><a href="https://discord.com/developers/docs/intro">文档</a> · <a href="https://discord.com/developers/docs/reference">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#lark">Lark</a></td><td align="left">Collaboration suite (messaging, docs, calendar) with an open platform, llms.txt, an official CLI with 200+ commands and agent skills, and an official OpenAPI MCP server.</td><td align="left"><a href="https://open.larksuite.com/document/home/index">文档</a> · <a href="https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create">API</a> · <a href="https://github.com/larksuite/cli">CLI</a> · <a href="https://github.com/larksuite/lark-openapi-mcp">MCP</a> · <a href="https://open.larksuite.com/document/server-docs/getting-started/server-api-list">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#resend">Resend</a></td><td align="left">Email API for developers with test mode, scoped API keys, idempotency support, and an official MCP server.</td><td align="left"><a href="https://resend.com/docs">文档</a> · <a href="https://resend.com/docs/api-reference/introduction">API</a> · <a href="https://resend.com/docs/sdks">SDK</a> · <a href="https://github.com/resend/mcp-send-email">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#slack">Slack</a></td><td align="left">Workspace messaging platform with a mature Web API, granular OAuth scopes, an OpenAPI spec, and llms.txt.</td><td align="left"><a href="https://api.slack.com">文档</a> · <a href="https://api.slack.com/methods">API</a> · <a href="https://docs.slack.dev/tools/slack-cli">CLI</a> · <a href="https://tools.slack.dev">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#telegram">Telegram Bot API</a></td><td align="left">Free bot platform with instant token issuance via BotFather, webhooks, a documented test environment, and a detailed changelog.</td><td align="left"><a href="https://core.telegram.org/bots">文档</a> · <a href="https://core.telegram.org/bots/api">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#twilio">Twilio</a></td><td align="left">Programmable messaging and voice APIs with test credentials, an OpenAPI spec, llms.txt, and an official CLI.</td><td align="left"><a href="https://www.twilio.com/docs">文档</a> · <a href="https://www.twilio.com/docs/usage/api">API</a> · <a href="https://www.twilio.com/docs/twilio-cli">CLI</a> · <a href="https://www.twilio.com/docs/libraries">SDK</a> · <a href="https://github.com/twilio-labs/mcp">MCP</a></td></tr>
</tbody>
</table>

<a id="services-observability-security"></a>

### 监控与安全 (3)

尚未实测

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="48%" align="left">用途</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#datadog">Datadog</a></td><td align="left">Observability platform with a full REST API, llms.txt, documented OAuth for integrations, rate limits, and webhooks.</td><td align="left"><a href="https://docs.datadoghq.com">文档</a> · <a href="https://docs.datadoghq.com/api/latest/">API</a> · <a href="https://github.com/DataDog/datadog-ci">CLI</a> · <a href="https://docs.datadoghq.com/bits_ai/mcp_server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#grafana">Grafana (Grafana Cloud)</a></td><td align="left">Observability platform (dashboards, metrics, logs, traces) with a documented HTTP API, official MCP server, llms.txt, and a standing free cloud tier.</td><td align="left"><a href="https://grafana.com/docs">文档</a> · <a href="https://grafana.com/docs/grafana/latest/developers/http_api/">API</a> · <a href="https://github.com/grafana/mcp-grafana">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#sentry">Sentry</a></td><td align="left">Error monitoring and performance tracing with llms.txt, an official MCP server, scoped auth tokens, and a full API.</td><td align="left"><a href="https://docs.sentry.io">文档</a> · <a href="https://docs.sentry.io/api/">API</a> · <a href="https://docs.sentry.io/cli/">CLI</a> · <a href="https://docs.sentry.io/platforms/">SDK</a> · <a href="https://docs.sentry.io/product/sentry-mcp/">MCP</a></td></tr>
</tbody>
</table>

<a id="services-commerce-marketing"></a>

### 电商与营销 (1)

尚未实测

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="48%" align="left">用途</th><th width="26%" align="left">接入方式</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#shopify">Shopify</a></td><td align="left">Commerce platform with versioned GraphQL APIs, llms.txt, official MCP docs, access-scoped tokens, free development stores, and a CLI.</td><td align="left"><a href="https://shopify.dev/docs">文档</a> · <a href="https://shopify.dev/docs/api">API</a> · <a href="https://shopify.dev/docs/api/shopify-cli">CLI</a> · <a href="https://shopify.dev/docs/apps/build/storefront-mcp">MCP</a></td></tr>
</tbody>
</table>

## 给 Agent 的入口

[查询指引](./llms.txt) · [服务 JSON](./generated/catalog.json) · [实测 JSON](./generated/evaluations.json) · [MCP 配置](./mcp/README.md)

通过 `search_services` 查找候选，再用 `get_service` 查看接入条件和实测依据。同一份数据也可以直接读取 JSON。

## 方法与贡献

如果你知道我们漏掉的服务、有想测的真实任务，或发现资料已经过时，欢迎提供线索或纠错。

[核心理念](./AGENTS.md) · [收录标准](./docs/catalog-standard.zh-CN.md) · [机票阶段结论](./docs/flights.zh-CN.md) · [任务设计](./data/experiments/tasks/AGENTS.md) · [执行与验收](./data/experiments/AGENTS.md) · [全部实测与证据](./generated/evaluations.md) · [参与贡献](./docs/contributing.md) · [提出问题](https://github.com/Olorinm/agent-friendly-services/issues)

代码：[MIT](./LICENSE) · 数据：[CC BY 4.0](./LICENSE-DATA)。
