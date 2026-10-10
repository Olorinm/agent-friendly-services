<!-- 生成文件 — 修改 scripts/generate.ts，再运行 npm run generate。 -->

# Agent-Friendly Services

[English](./README.md) | 简体中文

**帮你找到能让 Agent 完成任务的服务，并用实测比较哪个更可靠、更省事、更有性价比。**

我们关注普通个人能用上的服务，收集候选，再用真实任务逐步验证。你可以按分类浏览，点服务名查看接入条件和资料，也可以直接打开文档开始使用。

<a id="all-services"></a>

## 服务目录（194）

Token 和费用按有效试跑取平均，包含成功与失败；环境无效不计入。模型费用按 LiteLLM 估算，服务费用估算额标 ~。— 表示暂无数据。

完成率描述 Agent 在记录的环境及约束下是否交付完整任务，不等于服务可用率；未完成须结合具体阻碍及已验证的服务能力阅读。只测一次且完成，也会显示 100%。次数、任务与条件见[完整结果](./generated/evaluations.md)；有限观察不能证明长期可靠性。

每个分类内按任务组展示服务最近取得有效结果的测试方式，接入测试单独展示，其他方式见服务详情。当前不排名，仅在任务与条件一致时比较。准备说明不同的记录分别统计，包括包下载源或请求上限的变化；历次试跑均保留在完整记录中。

[旅行](#services-travel) · [数据库](#services-databases) · [搜索与数据获取](#services-web-search-data) · [办公与协作](#services-productivity-storage) · [AI 服务](#services-ai-models) · [Agent 基础设施与自动化](#services-agent-tooling) · [开发工具](#services-developer-tools) · [云计算与托管](#services-cloud-hosting) · [支付与计费](#services-payments-billing) · [通信](#services-communication) · [电商](#services-commerce-marketing)

<a id="services-travel"></a>

### 旅行 (27)

<a id="services-travel-flights"></a>

#### 机票 (27)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#ignav">Ignav Flights</a></td><td align="right"><a href="./generated/evaluations.md#comparison-77a51e093709">100%</a></td><td align="right">212.9k</td><td align="right">$0.93</td><td align="right">$0</td><td align="left"><a href="https://ignav.com/playground">网页</a></td><td align="left"><a href="https://ignav.com/docs">API</a> · <a href="https://ignav.com/docs/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#kiwi">Kiwi.com</a></td><td align="right"><a href="./generated/evaluations.md#comparison-521dd3fb476a">100%</a></td><td align="right">209.6k</td><td align="right">$0.84</td><td align="right">$0</td><td align="left"><a href="https://mcp.kiwi.com">MCP</a></td><td align="left"><a href="https://www.kiwi.com/en/pages/mcp/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#airgateway">AirGateway Platform API</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://support.airgateway.com/en-US/kb/article/4/introduction-to-airgateway-platform-api">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#amadeus-flights">Amadeus Flight APIs</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#apiheya-air-scraper">apiheya Air Scraper</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#aviasales">Aviasales via Travelpayouts</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://support.travelpayouts.com/hc/en-us/articles/210995808-How-to-get-access-to-the-Aviasales-Search-API">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#bright-data-serp">Bright Data SERP API</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.brightdata.com/api-reference/serp/google-flights/currency">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#duffel-flights">Duffel Flights API</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://duffel.com/guides/getting-started">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#expedia-xap-flights">Expedia XAP Flight Listings</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://developers.expediagroup.com/xap-apis/api/shopping-apis/flight-listings">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#flight-mcp">Flight MCP</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://flight-mcp.com/docs">API / MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#flightapi-io">FlightAPI.io Flight Price API</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.flightapi.io/documentation/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#kayak-affiliate">KAYAK Affiliate API</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://developers.kayak.com/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#letsfg">LetsFG Personal Flight Search</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://github.com/letsfg/letsfg">SDK / CLI</a> · <a href="https://letsfg.co/for-agents">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#lufthansa-partner">Lufthansa Partner Fare API</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://developer.lufthansa.com/docs/read/api_partner/offers">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#sabre-air">Sabre Air APIs</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://github.com/SabreDevStudio/SabreAPIsWorkflows/blob/master/SabreAPIsTestSuites/README.md">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#scrapingdog-flights">Scrapingdog Google Flights API</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.scrapingdog.com/documentation/google-flights-api/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#searchapi">SearchApi</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.searchapi.io/docs/google">API</a> · <a href="https://www.searchapi.io/integrations/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#serpapi">SerpApi</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://serpapi.com/google-flights-api">API</a> · <a href="https://github.com/serpapi/serpapi-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#skootle-google-flights">Skootle Google Flights Scraper</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#skyaccess">SkyAccess</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://github.com/sky-access/skyaccess-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#skyscanner">Skyscanner Travel APIs</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://developers.skyscanner.net/docs/getting-started/authentication">API</a> · <a href="https://developers.skyscanner.net/docs/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#travelport-tripservices">Travelport TripServices</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://developer.travelport.com/docs/getting-started">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#trip-com-flights">Trip.com Flight Distribution</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#qunar-flights">去哪儿机票合作</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#tongcheng-flights">同程机票合作</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#ctrip-flights">携程机票合作</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#fliggy-domestic-flights">飞猪国内机票开放平台</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left">—</td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：找到9月25日米兰飞往荷兰的机票**

2026-09-25；本题出发范围约定为MXP/LIN/BGY，抵达荷兰任一客运机场；1名成人、单程、经济舱，允许中转；本轮指定的服务入口

完成标准：至少一个方案满足日期、路线和旅客条件；关键信息与执行器取得的真实服务响应相符。仅验搜索结果，不验全网最低价或支付成功

**测试配置：** codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 分钟 · 2026-09-07（UTC） · 未预供账号或密钥

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/travel-flights.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-databases"></a>

### 数据库 (13)

<a id="services-databases-hosted-relational"></a>

#### 托管关系型数据库 (6)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#neon">Neon</a></td><td align="right"><a href="./generated/evaluations.md#comparison-7a86e94d64f8">100%</a></td><td align="right">167.2k</td><td align="right">$0.01</td><td align="right">—</td><td align="left"><a href="https://claimable.neon.tech/v1/agent/identity">API</a></td><td align="left"><a href="https://neon.com/docs/reference/claimable-neon">API</a> · <a href="https://neon.com/docs/reference/neon-cli">CLI</a> · <a href="https://github.com/neondatabase/mcp-server-neon">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#turso">Turso</a></td><td align="right"><a href="./generated/evaluations.md#comparison-7a86e94d64f8">100%</a></td><td align="right">232.6k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://api.turso.tech/v1/">API</a></td><td align="left"><a href="https://docs.turso.tech/api-reference/quickstart">API</a> · <a href="https://docs.turso.tech/sdk/ts/quickstart">SDK</a> · <a href="https://docs.turso.tech/quickstart">CLI</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我通过指定方式接通这个数据库服务，准备一个本轮专用的空远程测试数据库，做一次不写入业务数据的查询确认可用，并保存后续连接配置；说明接入步骤、人工门槛和免费或到期限制。**

指定服务、入口、允许使用的账户或注册身份及其来源见 ENVIRONMENT.md。按需注册、授权、安装和配置；无需账号的入口直接使用。仅新建本轮独立测试数据库及必需的最小父资源，不访问既有用户数据库。用一次只读数据库查询确认能连接，不创建业务表或记录。将资源标识和必要连接配置保存在本轮指定持久目录，秘密仅存私有文件，答复只给配置位置。已有账号来源、自助步骤、人工介入、特殊申请和具体阻碍如实说明。

完成标准：通过指定服务及入口完成必要接入，新建本轮独立空数据库并真实查询成功；所需安装和配置可供新会话复用且不泄露凭据；已有账号不算本轮自助注册，免账号入口不强行注册，免费或期限依据及未知项如实说明。仅有安装、资源列表、创建回执或健康检查不足以证明数据库可查询。

**测试配置：** 1.18.35 · deepseek-flash / high · 5 分钟 · 2026-10-08（UTC） · 接入准备: Preprovided existing authorized parent identity; executor creates one fresh empty logical database

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/databases-v2.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#neon">Neon / claimable-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-2f500bd738e2">100%</a></td><td align="right">274.8k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://claimable.neon.tech/v1/agent/identity">API</a></td><td align="left"><a href="https://neon.com/docs/reference/claimable-neon">API</a> · <a href="https://neon.com/docs/reference/neon-cli">CLI</a> · <a href="https://github.com/neondatabase/mcp-server-neon">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#neon">Neon / claimable-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-bfa31194c37d">100%</a></td><td align="right">479.4k</td><td align="right">$0.03</td><td align="right">—</td><td align="left"><a href="https://claimable.neon.tech/v1/agent/identity">API</a></td><td align="left"><a href="https://neon.com/docs/reference/claimable-neon">API</a> · <a href="https://neon.com/docs/reference/neon-cli">CLI</a> · <a href="https://github.com/neondatabase/mcp-server-neon">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#neon">Neon / claimable-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-eb4cee33eee8">100%</a></td><td align="right">142.3k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://claimable.neon.tech/v1/agent/identity">API</a></td><td align="left"><a href="https://neon.com/docs/reference/claimable-neon">API</a> · <a href="https://neon.com/docs/reference/neon-cli">CLI</a> · <a href="https://github.com/neondatabase/mcp-server-neon">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#neon">Neon / ephemeral-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-b514e81afd38">100%</a></td><td align="right">465.4k</td><td align="right">—</td><td align="right">$0</td><td align="left"><a href="https://neon.new/">API</a></td><td align="left"><a href="https://neon.com/docs/reference/claimable-neon">API</a> · <a href="https://neon.com/docs/reference/neon-cli">CLI</a> · <a href="https://github.com/neondatabase/mcp-server-neon">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#turso">Turso / platform-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-07edbec76825">100%</a></td><td align="right">767.6k</td><td align="right">—</td><td align="right">$0</td><td align="left"><a href="https://docs.turso.tech/api-reference/introduction">API</a></td><td align="left"><a href="https://docs.turso.tech/api-reference/quickstart">API</a> · <a href="https://docs.turso.tech/sdk/ts/quickstart">SDK</a> · <a href="https://docs.turso.tech/quickstart">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#turso">Turso / platform-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-3961c742b40e">0%</a></td><td align="right">—</td><td align="right">—</td><td align="right">$0</td><td align="left"><a href="https://api.turso.tech/v1/">API</a></td><td align="left"><a href="https://docs.turso.tech/api-reference/quickstart">API</a> · <a href="https://docs.turso.tech/sdk/ts/quickstart">SDK</a> · <a href="https://docs.turso.tech/quickstart">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#turso">Turso / platform-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-785fde9d2ce4">100%</a></td><td align="right">276.6k</td><td align="right">$0.02</td><td align="right">$0</td><td align="left"><a href="https://api.turso.tech/v1/">API</a></td><td align="left"><a href="https://docs.turso.tech/api-reference/quickstart">API</a> · <a href="https://docs.turso.tech/sdk/ts/quickstart">SDK</a> · <a href="https://docs.turso.tech/quickstart">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#turso">Turso / platform-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-eb4cee33eee8">100%</a></td><td align="right">327.9k</td><td align="right">$0.02</td><td align="right">$0</td><td align="left"><a href="https://api.turso.tech/v1/">API</a></td><td align="left"><a href="https://docs.turso.tech/api-reference/quickstart">API</a> · <a href="https://docs.turso.tech/sdk/ts/quickstart">SDK</a> · <a href="https://docs.turso.tech/quickstart">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#aiven">Aiven</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://aiven.io/docs/tools/api">API</a> · <a href="https://aiven.io/docs/products/postgresql/howto/connect-python">SDK</a> · <a href="https://aiven.io/docs/tools/cli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#cloudflare">Cloudflare</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/get/">API</a> · <a href="https://developers.cloudflare.com/api/typescript/resources/kv/subresources/namespaces/subresources/values/methods/get/">SDK</a> · <a href="https://developers.cloudflare.com/d1/get-started/">CLI</a> · <a href="https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#planetscale">PlanetScale</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://planetscale.com/docs/cli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#supabase">Supabase</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://supabase.com/docs/reference/api/introduction">API</a> · <a href="https://supabase.com/docs/reference">SDK</a> · <a href="https://supabase.com/docs/guides/cli">CLI</a> · <a href="https://supabase.com/docs/guides/getting-started/mcp">MCP</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

| 任务及条件 | 完成标准 |
| --- | --- |
| 我的个人书目目录要按文件批量导入，遇到重复编号不能留下半批数据。请做一个可复用的导入器，用数据库的整批原子操作或事务保护，在提供的两个独立测试表中分别实际验证错误样本整批拒绝、更正样本全部保存，原有书目不变。交付导入器、简短用法和两次结果，凭据单独保存。<br>两张远程测试表的实际名称、连接配置与角色对应见 ENVIRONMENT.md；它们都有 book_id（非空整数主键）、title（非空文本），最初各只有 book_id=100、title=已有书目。附件 attachments/batch-reject.csv 与 attachments/batch-corrected.csv 均为 UTF-8 CSV，首行为 book_id,title。错误文件只导入 reject_case 对应表，更正文件只导入 accept_case 对应表；两个表互不覆盖。同一个交付的导入器应接受文件路径和这两个授权目标表之一，实际读取文件内容，不把预期终态写死。错误样本须实际触发数据库的重复主键拒绝，不能只在本地预检后跳过；不得忽略或替换冲突记录。每个文件作为一个整体提交或拒绝，可使用数据库支持的单条原子批量写入或整批事务，不限定语言、客户端或 SQL 条数。不能通过 UPDATE、DELETE、替换记录、改约束、清空、删除或重建表来修复或伪装回滚；未提交事务内的正常回滚允许。完成后保留两个表的结果供核对，说明每个样本的实际结果和遇到的数据库错误。 | 通过指定服务真实运行同一交付导入器：错误文件由数据库拒绝，整批没有已提交新增记录，原有记录不变；更正文件的全部记录提交到另一个表，原有记录不变。结构与约束保持不变，实际执行路径使用可核对的数据库整批原子操作或正确事务处理，无提交后补偿删改。导入器及简短用法可留存且与实际执行相符，两次结果如实说明。 |
| 帮我给个人待办应用做一次备份恢复演练：把源库导出成可下载留存的逻辑备份，在同一服务中新建一个独立空数据库，用这份备份实际恢复，保持源库不变。恢复结束后重新连接新库核对，交付备份、简短恢复方法、新库位置、各表行数和核对结果，并说明新库的免费或到期限制。<br>源库是本轮接入后由准备者填入合成数据的专用远程数据库，其身份和连接配置见 ENVIRONMENT.md；它包含 lists 与 todos 两张业务表。lists 有 id、name；todos 有 id、list_id、title、done、note，list_id 关联 lists.id。备份和恢复须保留两张表的字段名、数据类型含义、主键、外键、非空约束、默认值及全部原始记录；清单归属、完成状态、文本内容，以及备注空字符串与缺值的区别都要保留。恢复目标必须是本次新建且起初没有业务表的独立远程数据库；可以与源库共享项目或计算资源。备份应包含重建所需的业务结构和数据，以后源库不可用时也能在兼容 SQL 引擎中恢复，不只是一条依赖原服务的快照或分支链接。不要求跨不同 SQL 方言恢复，不备份服务内部表、账号权限或宿主机。源库在此期间没有其他写入者；不得修改或删除源库业务表和记录。 | 在指定服务及入口从真实源库导出覆盖两表逻辑结构与全部记录的备份，实际使用该备份恢复到本次独立新建且起初空白的远程目标；新连接可读回等价业务结构和全部原始记录，源库业务结构与记录未变。交付可留存备份、可用简短恢复方法、新库位置、准确的各表行数与核对结果，并如实说明已知期限或免费条件。凭据只存私有配置，不进入交付答案或公开证据。 |
| 为我的个人待办应用准备一个独立的远程数据库，用附件数据验证新增和修改后的保存情况。写入程序退出后，用一个全新的程序重新连接同一数据库读取；给我按 id 排列的全部待办、未完成待办，以及总数和完成数，并说明数据库的免费或到期限制。<br>仅合成测试数据：id=1,title=Buy milk,done=false；id=2,title=Read book,done=false；id=3,title=Walk dog,done=true。写入三项，再把 id=2 改为 done=true，其他内容不变。使用本轮接入阶段新建并明确交付的独立空远程测试数据库，其标识和私有连接配置见 ENVIRONMENT.md；允许复用安装和认证，不继承业务表、数据、答案或调用脚本。不得访问或修改既有用户项目。 | 实际在指定服务的远程数据库中新增三项并修改 id=2，随后写入进程结束，另一全新进程重新连接同一数据库读回三项；只有 id=1 未完成，总数 3、完成数 2，标题与其他原值不变；最终全部待办按 id 排序。真实请求、响应和进程记录支持远程保存与独立读取；正确说明有依据的免费或到期限制，无法确认的细项如实标未知。凭据只保存在工作目录私有文件，不进入公开证据或最终答案。限时资源可完成此题，但必须明确期限，不声称永久可用。 |
| 为我的个人待办应用准备一个独立的远程数据库，验证新增、修改和重新连接后读取待办事项<br>仅合成测试数据：id=1,title=Buy milk,done=false；id=2,title=Read book,done=false；id=3,title=Walk dog,done=true。写入三项，再把 id=2 改为 done=true。允许创建无需付费的临时数据库；不能动已有项目 | 实际在指定服务的远程数据库中保存和更新；新进程读回三项且只有 id=1 未完成，总数3、完成数2，标题未变；证据证明独立连接和远程执行。凭据只保存在工作目录私有文件，不得进入 evidence 或最终答案。限时资源可完成此题，但必须明确到期限制 |

| 服务 | 本次任务 | 测试配置 | 起点 |
| --- | --- | --- | --- |
| [Neon / API](./generated/evaluations.md#comparison-eb4cee33eee8) | 我的个人书目目录要按文件批量导入，遇到重复编号不能留下半批数据。请做一个可复用的导入器，用数据库的整批原子操作或事务保护，在提供的两个独立测试表中分别实际验证错误样本整批拒绝、更正样本全部保存，原有书目不变。交付导入器、简短用法和两次结果，凭据单独保存。 | 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 | 接入准备: Preprovided existing authorized parent identity; executor creates one fresh empty logical database |
| [Turso / API](./generated/evaluations.md#comparison-eb4cee33eee8) | 我的个人书目目录要按文件批量导入，遇到重复编号不能留下半批数据。请做一个可复用的导入器，用数据库的整批原子操作或事务保护，在提供的两个独立测试表中分别实际验证错误样本整批拒绝、更正样本全部保存，原有书目不变。交付导入器、简短用法和两次结果，凭据单独保存。 | 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 | 接入准备: Preprovided existing authorized parent identity; executor creates one fresh empty logical database |
| [Neon / API](./generated/evaluations.md#comparison-bfa31194c37d) | 帮我给个人待办应用做一次备份恢复演练：把源库导出成可下载留存的逻辑备份，在同一服务中新建一个独立空数据库，用这份备份实际恢复，保持源库不变。恢复结束后重新连接新库核对，交付备份、简短恢复方法、新库位置、各表行数和核对结果，并说明新库的免费或到期限制。 | 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 | 接入准备: none initially; generated anonymous Claimable project credentials |
| [Turso / API](./generated/evaluations.md#comparison-3961c742b40e) | 帮我给个人待办应用做一次备份恢复演练：把源库导出成可下载留存的逻辑备份，在同一服务中新建一个独立空数据库，用这份备份实际恢复，保持源库不变。恢复结束后重新连接新库核对，交付备份、简短恢复方法、新库位置、各表行数和核对结果，并说明新库的免费或到期限制。 | 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 | 接入准备: existing authorized Turso management account |
| [Neon / API](./generated/evaluations.md#comparison-2f500bd738e2) | 为我的个人待办应用准备一个独立的远程数据库，用附件数据验证新增和修改后的保存情况。写入程序退出后，用一个全新的程序重新连接同一数据库读取；给我按 id 排列的全部待办、未完成待办，以及总数和完成数，并说明数据库的免费或到期限制。 | 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 | 接入准备: none initially; executor obtains anonymous scoped test credentials |
| [Turso / API](./generated/evaluations.md#comparison-785fde9d2ce4) | 为我的个人待办应用准备一个独立的远程数据库，用附件数据验证新增和修改后的保存情况。写入程序退出后，用一个全新的程序重新连接同一数据库读取；给我按 id 排列的全部待办、未完成待办，以及总数和完成数，并说明数据库的免费或到期限制。 | 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 | 接入准备: pre-existing Turso management account |
| [Turso / API](./generated/evaluations.md#comparison-07edbec76825) | 为我的个人待办应用准备一个独立的远程数据库，验证新增、修改和重新连接后读取待办事项 | codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 分钟 | 已预供服务凭据 |
| [Neon / API](./generated/evaluations.md#comparison-b514e81afd38) | 为我的个人待办应用准备一个独立的远程数据库，验证新增、修改和重新连接后读取待办事项 | codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 分钟 | 未预供账号或密钥 |

**测试配置：** 2026-09-07 – 2026-10-08（UTC）

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义 1](./data/experiments/tasks/database-atomic-import.md) · [任务定义 2](./data/experiments/tasks/database-restore.md) · [任务定义 3](./data/experiments/tasks/databases-v2.md) · [任务定义 4](./data/experiments/tasks/databases.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-databases-vector"></a>

#### 向量数据库 (6)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#chroma">Chroma</a></td><td align="left">Open-source embedding database with a hosted Chroma Cloud, official CLI, official MCP server, and llms.txt.</td><td align="left"><a href="https://docs.trychroma.com/docs/overview/introduction">API</a> · <a href="https://docs.trychroma.com/docs/cli/install">CLI</a> · <a href="https://github.com/chroma-core/chroma-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#pinecone">Pinecone</a></td><td align="left">Managed vector database for search and RAG, with llms.txt, an official MCP server, and self-serve keys.</td><td align="left"><a href="https://docs.pinecone.io/reference/api/introduction">API</a> · <a href="https://github.com/pinecone-io/cli">CLI</a> · <a href="https://docs.pinecone.io/guides/operations/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#qdrant">Qdrant</a></td><td align="left">Open-source vector database with a managed cloud, llms.txt, an official MCP server, and a free cluster tier.</td><td align="left"><a href="https://api.qdrant.tech">API</a> · <a href="https://qdrant.tech/documentation/interfaces">SDK</a> · <a href="https://github.com/qdrant/mcp-server-qdrant">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#redis">Redis (Redis Cloud)</a></td><td align="left">In-memory data platform for caching, vector search and real-time apps; Redis Cloud has a REST management API, official MCP server, redis-cli, and llms.txt.</td><td align="left"><a href="https://redis.io/docs/latest/operate/rc/api/">API</a> · <a href="https://redis.io/docs/latest/develop/tools/cli/">CLI</a> · <a href="https://github.com/redis/mcp-redis">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#upstash">Upstash</a></td><td align="left">Serverless Redis, Kafka-successor queues, and vector storage with REST APIs, llms.txt, an official MCP server, and a free tier.</td><td align="left"><a href="https://upstash.com/docs/devops/developer-api/introduction">API</a> · <a href="https://github.com/upstash/cli">CLI</a> · <a href="https://github.com/upstash/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#weaviate">Weaviate</a></td><td align="left">Open-source vector database with REST/GraphQL/gRPC APIs, Weaviate Cloud free sandboxes, an official CLI, MCP server, and llms.txt.</td><td align="left"><a href="https://docs.weaviate.io/weaviate/api/rest">API</a> · <a href="https://github.com/weaviate/weaviate-cli">CLI</a> · <a href="https://github.com/weaviate/mcp-server-weaviate">MCP</a></td></tr>
</tbody>
</table>

<a id="services-databases-document"></a>

#### 文档数据库 (2)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#mongodb-atlas">MongoDB Atlas</a></td><td align="left">Managed MongoDB with a versioned Admin API, published OpenAPI spec, llms.txt, official CLI and MCP server.</td><td align="left"><a href="https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/">API</a> · <a href="https://www.mongodb.com/docs/drivers/">SDK</a> · <a href="https://www.mongodb.com/docs/atlas/cli/">CLI</a> · <a href="https://github.com/mongodb-js/mongodb-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#redis">Redis (Redis Cloud)</a></td><td align="left">In-memory data platform for caching, vector search and real-time apps; Redis Cloud has a REST management API, official MCP server, redis-cli, and llms.txt.</td><td align="left"><a href="https://redis.io/docs/latest/operate/rc/api/">API</a> · <a href="https://redis.io/docs/latest/develop/tools/cli/">CLI</a> · <a href="https://github.com/redis/mcp-redis">MCP</a></td></tr>
</tbody>
</table>

<a id="services-databases-key-value"></a>

#### 键值数据库 (3)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#cloudflare">Cloudflare</a></td><td align="left">Edge network, Workers serverless platform, storage, and AI services with agent-focused docs and official MCP servers.</td><td align="left"><a href="https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/get/">API</a> · <a href="https://developers.cloudflare.com/api/typescript/resources/kv/subresources/namespaces/subresources/values/methods/get/">SDK</a> · <a href="https://developers.cloudflare.com/d1/get-started/">CLI</a> · <a href="https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#redis">Redis (Redis Cloud)</a></td><td align="left">In-memory data platform for caching, vector search and real-time apps; Redis Cloud has a REST management API, official MCP server, redis-cli, and llms.txt.</td><td align="left"><a href="https://redis.io/docs/latest/operate/rc/api/">API</a> · <a href="https://redis.io/docs/latest/develop/tools/cli/">CLI</a> · <a href="https://github.com/redis/mcp-redis">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#upstash">Upstash</a></td><td align="left">Serverless Redis, Kafka-successor queues, and vector storage with REST APIs, llms.txt, an official MCP server, and a free tier.</td><td align="left"><a href="https://upstash.com/docs/devops/developer-api/introduction">API</a> · <a href="https://github.com/upstash/cli">CLI</a> · <a href="https://github.com/upstash/mcp-server">MCP</a></td></tr>
</tbody>
</table>

<a id="services-web-search-data"></a>

### 搜索与数据获取 (58)

以下服务暂按本层范围收录，细分缺口见服务详情。

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#xquik">Xquik</a></td><td align="left">Hosted X data and account automation service with a REST API, official MCP server, OpenAPI, SDKs, HMAC webhooks, and OAuth 2.1.</td><td align="left"><a href="https://docs.xquik.com/api-reference/overview">API</a> · <a href="https://docs.xquik.com/sdks">SDK</a> · <a href="https://docs.xquik.com/mcp/overview">MCP</a></td></tr>
</tbody>
</table>

<a id="services-web-search-data-scholarly-search"></a>

#### 学术文献检索 (3)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#crossref">Crossref</a></td><td align="right"><a href="./generated/evaluations.md#comparison-e571efbd864f">100%</a></td><td align="right">220.9k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://api.crossref.org/works">API</a></td><td align="left"><a href="https://www.crossref.org/documentation/retrieve-metadata/rest-api/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#openalex">OpenAlex</a></td><td align="right"><a href="./generated/evaluations.md#comparison-e571efbd864f">100%</a></td><td align="right">168.2k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://api.openalex.org/works">API</a></td><td align="left"><a href="https://help.openalex.org/api/authentication/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我接通这个学术文献检索服务，通过指定方式做一次真实文献查询，确认能查到可识别的论文记录，并保存后续查询需要的本地配置；说明接入步骤和实际阻碍。**

服务、指定入口、允许使用的账号或注册资料及其来源见 ENVIRONMENT.md。自行选择一个小型文献查询，报告实际查到的题名及可识别的文献链接或标识，并注明来源。无需账号的入口直接使用；需注册或授权时仅使用本轮提供的身份资料。必要配置保存在本轮持久目录，秘密仅存私有文件；答复给出配置位置、已有账号来源、自助步骤、人工介入或额外申请要求。

完成标准：按指定方式完成必要注册、认证、安装和配置；真实响应含可识别文献，答复与响应一致，配置可供新会话复用且不泄露秘密。免注册入口不强行注册，已有账号不冒充本轮自助注册。

**测试配置：** 1.18.35 · deepseek-flash / high · 5 分钟 · 2026-10-08（UTC） · 接入准备: none; currentofficialkeylesspublicroute, no account/email/payment supplied; lowvolumebibliographicmetadata only

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/scholarly-search.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#crossref">Crossref</a></td><td align="right"><a href="./generated/evaluations.md#comparison-b5f2b1f41c23">100%</a></td><td align="right">72.9k</td><td align="right">$0.0064</td><td align="right">$0</td><td align="left"><a href="https://api.crossref.org/works">API</a></td><td align="left"><a href="https://www.crossref.org/documentation/retrieve-metadata/rest-api/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#openalex">OpenAlex</a></td><td align="right"><a href="./generated/evaluations.md#comparison-b5f2b1f41c23">100%</a></td><td align="right">104.5k</td><td align="right">$0.0083</td><td align="right">$0</td><td align="left"><a href="https://api.openalex.org/works">API</a></td><td align="left"><a href="https://help.openalex.org/api/authentication/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#semantic-scholar">Semantic Scholar</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://api.semanticscholar.org/api-docs/graph">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：请用指定服务根据附件中的阅读笔记找到那篇论文，为我的笔记补齐文献条目：原文题名、全部作者（保持原顺序）、发表年份、期刊名和可点击的 DOI 链接；用中文简单说明为什么匹配这些线索，并注明检索来源。**

阅读笔记：2015 年，Nature，一位作者姓 Bengio，题名包含 deep learning。需要找到这篇论文的正式发表记录。作者可用完整姓名或规范的姓与名字首字母表示，但不要省略作者；不限定 APA、MLA 等引用格式。可以沿本次指定服务返回的 DOI 或出版链接核对原始书目信息；不要用其他学术库或通用网页搜索替代指定服务查询，也不要凭记忆填补缺失字段。只需书目信息，不需要获取或概括全文。

完成标准：实际通过指定服务取得与全部笔记线索相符的论文记录；交付的必要书目信息与事前冻结的出版社官方参考一致，作者无遗漏或错序，DOI 链接指向同一论文；匹配说明有数据依据，来源可核对。允许合理大小写、标点、作者姓名缩写及 DOI URL 形式差异；不要求特定结果排名、输出文件、额外字段或引用格式。

**测试配置：** 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 · 2026-10-08（UTC） · 接入准备: none; currentofficialkeylesspublicroute, no account/email/payment supplied; lowvolumebibliographicmetadata only

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/scholarly-search.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-web-search-data-web-search"></a>

#### 网页搜索 (9)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#exa">Exa</a></td><td align="right"><a href="./generated/evaluations.md#comparison-5244b7150d7c">100%</a></td><td align="right">294.5k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://mcp.exa.ai/mcp">MCP</a></td><td align="left"><a href="https://docs.exa.ai/reference/getting-started">API</a> · <a href="https://docs.exa.ai/sdks/typescript-sdk-specification">SDK</a> · <a href="https://exa.ai/docs/get-started/exa-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#firecrawl">Firecrawl</a></td><td align="right"><a href="./generated/evaluations.md#comparison-5244b7150d7c">100%</a></td><td align="right">106.4k</td><td align="right">$0.0082</td><td align="right">$0</td><td align="left"><a href="https://api.firecrawl.dev/v2/search">API</a></td><td align="left"><a href="https://docs.firecrawl.dev/api-reference/introduction">API</a> · <a href="https://docs.firecrawl.dev/sdks/overview">SDK</a> · <a href="https://docs.firecrawl.dev/mcp-server">MCP</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我接通这个搜索服务，通过指定方式做一次简单的真实网页搜索，确认能用，并保存后续搜索需要的本地配置；说明完成了哪些接入步骤，遇到阻碍也请说明。**

服务、指定入口、允许使用的账户或注册资料及其来源见 ENVIRONMENT.md。自行选择一个普通公开主题做小型搜索，给出查询内容和至少一条搜索结果的标题、网页链接。无需账号的入口直接使用；需注册或授权时仅使用本轮提供的身份资料。将必要连接配置保存在本轮指定的持久目录，秘密只保存在私有文件中，答复只给配置位置。说明已有账号来源、实际自助完成的步骤、人工介入或额外申请要求。

完成标准：按指定方式完成必要注册、认证、安装与配置，真实搜索返回至少一条含标题和有效网页 URL 的结果，答复与响应一致；所需配置可供新会话复用且不泄露秘密。免注册入口不强行注册；已有账号不算本轮自助注册，人工步骤和额外申请如实记录。仅文档示例、健康检查、工具清单、安装成功或保存配置不足以证明接通搜索。

**测试配置：** 1.18.35 · deepseek-flash / high · 5 分钟 · 2026-10-08（UTC） · 接入准备: none; documented anonymous public route

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/web-search.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#exa">Exa / public-mcp</a></td><td align="right"><a href="./generated/evaluations.md#comparison-db274edc24f6">100%</a></td><td align="right">230.6k</td><td align="right">$0.02</td><td align="right">—</td><td align="left"><a href="https://mcp.exa.ai/mcp">MCP</a></td><td align="left"><a href="https://docs.exa.ai/reference/getting-started">API</a> · <a href="https://docs.exa.ai/sdks/typescript-sdk-specification">SDK</a> · <a href="https://exa.ai/docs/get-started/exa-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#exa">Exa / public-mcp</a></td><td align="right"><a href="./generated/evaluations.md#comparison-f351c20d0bf2">100%</a></td><td align="right">183.4k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://mcp.exa.ai/mcp">MCP</a></td><td align="left"><a href="https://docs.exa.ai/reference/getting-started">API</a> · <a href="https://docs.exa.ai/sdks/typescript-sdk-specification">SDK</a> · <a href="https://exa.ai/docs/get-started/exa-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#firecrawl">Firecrawl / public-search-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-3f655dc71038">100%</a></td><td align="right">346.8k</td><td align="right">—</td><td align="right">$0</td><td align="left"><a href="https://docs.firecrawl.dev/features/search">API</a></td><td align="left"><a href="https://docs.firecrawl.dev/api-reference/introduction">API</a> · <a href="https://docs.firecrawl.dev/sdks/overview">SDK</a> · <a href="https://docs.firecrawl.dev/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#firecrawl">Firecrawl / public-search-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-f351c20d0bf2">100%</a></td><td align="right">245.2k</td><td align="right">$0.02</td><td align="right">$0</td><td align="left"><a href="https://api.firecrawl.dev/v2/search">API</a></td><td align="left"><a href="https://docs.firecrawl.dev/api-reference/introduction">API</a> · <a href="https://docs.firecrawl.dev/sdks/overview">SDK</a> · <a href="https://docs.firecrawl.dev/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#agentservices">AgentServices</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://github.com/vbkotecha/agentservices-api/blob/main/docs/buyer-quickstart.md">API</a> · <a href="https://github.com/vbkotecha/agentservices-api/blob/main/sdk/README.md">SDK</a> · <a href="https://github.com/vbkotecha/agentservices-api/blob/main/README.md#using-as-mcp-server-claude-desktop-cursor-etc">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#brave-search">Brave Search API</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://github.com/brave/brave-search-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#perplexity">Perplexity API</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://github.com/ppl-ai/modelcontextprotocol">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#searchapi">SearchApi</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.searchapi.io/docs/google">API</a> · <a href="https://www.searchapi.io/integrations/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#serpapi">SerpApi</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://serpapi.com/google-flights-api">API</a> · <a href="https://github.com/serpapi/serpapi-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#serper">Serper</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://serper.dev/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#tavily">Tavily</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.tavily.com/documentation/quickstart">API</a> · <a href="https://docs.tavily.com/sdk">SDK</a> · <a href="https://docs.tavily.com/documentation/keyless">MCP</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

| 任务及条件 | 完成标准 |
| --- | --- |
| 我准备把 Python 应用升级到 3.13，请用中文简要查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并附上支持这些结论的官方页面链接。<br>目标版本 Python 3.13；官方来源范围 python.org。使用本轮指定搜索服务发现来源；可直接读取搜索结果页面及其中指向的官方文档。所引用的官方依据应能追溯到这些搜索结果；不依赖模型记忆或其他搜索引擎提供答案。 | 三个问题均有正确答案且由 Python 3.13 官方资料支持；最终提供的官方链接与结论对应，真实来源能追溯到指定服务的搜索结果及其官方文档链接。直接读取这些来源页面允许；其他搜索引擎不能替代指定服务发现来源。来源链与回答可通过运行器采集的实际调用、响应和所读内容核对；不要求执行者另外编写审计日志。 |
| 我准备把 Python 应用升级到 3.13，查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并给出官方依据<br>目标版本 Python 3.13；官方来源范围 python.org；使用本轮指定搜索服务发现来源，可直接读取它返回的来源页面；不依赖模型记忆或其他搜索引擎提供答案 | 三个问题均有正确答案且由 Python 3.13 官方资料支持；至少两个不同官方 URL 出现在指定服务的真实搜索响应中；证据可核对。直接抓取搜索返回页面允许，但内置联网检索只可用于服务接入文档，不能替代被测搜索 |

| 服务 | 本次任务 | 测试配置 | 起点 |
| --- | --- | --- | --- |
| [Exa / MCP](./generated/evaluations.md#comparison-f351c20d0bf2) | 我准备把 Python 应用升级到 3.13，请用中文简要查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并附上支持这些结论的官方页面链接。 | 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 | 接入准备: none; documented anonymous public route |
| [Firecrawl / API](./generated/evaluations.md#comparison-f351c20d0bf2) | 我准备把 Python 应用升级到 3.13，请用中文简要查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并附上支持这些结论的官方页面链接。 | 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 | 接入准备: none; documented anonymous public route |
| [Exa / MCP](./generated/evaluations.md#comparison-db274edc24f6) | 我准备把 Python 应用升级到 3.13，查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并给出官方依据 | 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 | 未预供账号或密钥 |
| [Firecrawl / API](./generated/evaluations.md#comparison-3f655dc71038) | 我准备把 Python 应用升级到 3.13，查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并给出官方依据 | codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 分钟 | 未预供账号或密钥 |

**测试配置：** 2026-09-07 – 2026-10-08（UTC）

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义 1](./data/experiments/tasks/web-search-v2.md) · [任务定义 2](./data/experiments/tasks/web-search.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-web-search-data-web-extraction"></a>

#### 网页内容提取 (6)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#exa">Exa</a></td><td align="right"><a href="./generated/evaluations.md#comparison-bde1a47b7eaa">100%</a></td><td align="right">165.8k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://mcp.exa.ai/mcp">MCP</a></td><td align="left"><a href="https://docs.exa.ai/reference/getting-started">API</a> · <a href="https://docs.exa.ai/sdks/typescript-sdk-specification">SDK</a> · <a href="https://exa.ai/docs/get-started/exa-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#firecrawl">Firecrawl</a></td><td align="right"><a href="./generated/evaluations.md#comparison-bde1a47b7eaa">100%</a></td><td align="right">186.8k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://api.firecrawl.dev/v2/scrape">API</a></td><td align="left"><a href="https://docs.firecrawl.dev/api-reference/introduction">API</a> · <a href="https://docs.firecrawl.dev/sdks/overview">SDK</a> · <a href="https://docs.firecrawl.dev/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#jina">Jina AI</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://r.jina.ai/">API</a></td><td align="left"><a href="https://jina.ai/reader/">API</a> · <a href="https://github.com/jina-ai/MCP">MCP</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我接通这个网页内容提取服务，通过指定方式读取附件里的示例网页，给我页面标题和一句内容概述，确认能用；保存后续调用所需配置，并说明接入步骤和遇到的门槛。**

示例网页：https://example.com/ 。服务、指定入口、允许使用的账户或注册身份及其来源见 ENVIRONMENT.md。无需账号的入口直接使用；需注册或授权时只使用本轮提供的身份资料。通过指定服务提取此 URL 的正文，不用搜索摘要或绕过服务直读网页代替。将必要配置保存在本轮指定的持久目录，秘密仅存私有文件，答复只给配置位置；如实说明已有账号来源、自助步骤、人工介入、额外申请及具体阻碍。

完成标准：通过指定入口完成必要注册、认证、安装与配置，真实提取指定网页且标题、概述与返回正文相符；必要配置可供新会话复用且不泄露秘密。免账号入口不强行注册，已有账号不算本轮自助注册，实际人工和额外申请如实记录。仅安装、健康检查、工具清单或搜索结果不足以证明正文提取可用。

| 服务 | 起点 |
| --- | --- |
| [Exa](./generated/evaluations.md#comparison-bde1a47b7eaa) | 接入准备: none; anonymous public extraction routes, no account/email/token/payment supplied |
| [Firecrawl](./generated/evaluations.md#comparison-bde1a47b7eaa) | 接入准备: none; anonymous public extraction routes, no account/email/token/payment supplied |
| [Jina AI](./generated/evaluations.md#comparison-4582424b2cd6) | 未预供账号或密钥 |

**测试配置：** 1.18.35 · deepseek-flash / high · 5 分钟 · 2026-10-08（UTC）

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/web-extraction.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#exa">Exa / public-mcp</a></td><td align="right"><a href="./generated/evaluations.md#comparison-032f75889210">100%</a></td><td align="right">312.8k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://mcp.exa.ai/mcp">MCP</a></td><td align="left"><a href="https://docs.exa.ai/reference/getting-started">API</a> · <a href="https://docs.exa.ai/sdks/typescript-sdk-specification">SDK</a> · <a href="https://exa.ai/docs/get-started/exa-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#exa">Exa / public-mcp</a></td><td align="right"><a href="./generated/evaluations.md#comparison-c49d8e01e18c">0%</a></td><td align="right">745.5k</td><td align="right">$0.06</td><td align="right">$0</td><td align="left"><a href="https://mcp.exa.ai/mcp">MCP</a></td><td align="left"><a href="https://docs.exa.ai/reference/getting-started">API</a> · <a href="https://docs.exa.ai/sdks/typescript-sdk-specification">SDK</a> · <a href="https://exa.ai/docs/get-started/exa-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#firecrawl">Firecrawl / public-scrape-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-032f75889210">100%</a></td><td align="right">264.2k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://api.firecrawl.dev/v2/scrape">API</a></td><td align="left"><a href="https://docs.firecrawl.dev/api-reference/introduction">API</a> · <a href="https://docs.firecrawl.dev/sdks/overview">SDK</a> · <a href="https://docs.firecrawl.dev/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#firecrawl">Firecrawl / public-scrape-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-c49d8e01e18c">100%</a></td><td align="right">365.7k</td><td align="right">$0.02</td><td align="right">—</td><td align="left"><a href="https://api.firecrawl.dev/v2/scrape">API</a></td><td align="left"><a href="https://docs.firecrawl.dev/api-reference/introduction">API</a> · <a href="https://docs.firecrawl.dev/sdks/overview">SDK</a> · <a href="https://docs.firecrawl.dev/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#agentservices">AgentServices</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://github.com/vbkotecha/agentservices-api/blob/main/docs/buyer-quickstart.md">API</a> · <a href="https://github.com/vbkotecha/agentservices-api/blob/main/sdk/README.md">SDK</a> · <a href="https://github.com/vbkotecha/agentservices-api/blob/main/README.md#using-as-mcp-server-claude-desktop-cursor-etc">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#apify">Apify</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.apify.com/api/v2">API</a> · <a href="https://docs.apify.com/sdk">SDK</a> · <a href="https://docs.apify.com/cli">CLI</a> · <a href="https://docs.apify.com/platform/integrations/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#jina">Jina AI</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://jina.ai/reader/">API</a> · <a href="https://github.com/jina-ai/MCP">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#tavily">Tavily</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.tavily.com/documentation/quickstart">API</a> · <a href="https://docs.tavily.com/sdk">SDK</a> · <a href="https://docs.tavily.com/documentation/keyless">MCP</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

| 任务及条件 | 完成标准 |
| --- | --- |
| 我在把一份旧扫描手册整理成可检索的表格。请从材料指定的 TTB Table No. 4 中，把 Proof 从 1.0 到 2.0 的这一小段转成 CSV，保留两种 gallons per pound 数值，给我文件和官方来源链接。只抄录原表，不做计税或其他业务计算。<br>官方 PDF：https://www.ttb.gov/system/files/images/pdfs/foia_Gauging_Manual_Tables/Table_4.pdf 。使用 TTB Gauging Manual 的 TABLE NO. 4 / GALLONS PER POUND，原文件共 21 页。目标是物理第 2 页（印刷页码 532）左半表，Proof 从 1.0 到 2.0，含两端，共 11 行。CSV 使用 UTF-8，列名为 proof、wine_gallons_per_pound、proof_gallons_per_pound；按 Proof 升序，保留原表印出的全部数值精度，不换算单位、不重新计算或四舍五入。通过本轮指定的内容提取服务取得此 PDF 的目标表文字，可自行整理它返回的文本、Markdown、HTML 或结构化内容；不以其他网页、搜索摘要、模型记忆、直接下载后本地解析或 OCR、裁剪重传后的 PDF，或仅取得原 PDF 链接/二进制替代服务对原 URL 的正文提取。若指定 URL 返回的目标表实质不同，请说明差异，不拼接其他版本。 | 指定服务实际返回原 URL 的目标表内容；CSV 三列、11 行的 Proof 与两种 gallons per pound 数值对应准确，保留原表数值精度，无漏行、重复、额外行或顺序混淆；文件可用，答复含文件位置与官方来源。允许不改变数值的前导零、尾零及无损空白、换行差异。不要求特定解析库、服务返回格式、OCR 模式、页码字段、缓存策略或审计日志。 |
| 我想把官方假日表用于个人日历整理。请从附件给定的网页提取 2027 年假日安排，做成按日期排序的 CSV 文件，包含表中全部假日的日期、星期和英文名称；按网页列出的日期记录，并给我文件和来源链接。<br>官方页面：https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/ 。只整理其中的“2027 Holiday Schedule”表，不混入其他年份或页面说明。CSV 使用 UTF-8，列名为 date、weekday、holiday；date 为 YYYY-MM-DD，weekday 为英文完整星期名，holiday 保留表中的英文名称，去掉脚注标记。日期按表中公布值记录，不自行换成节日的日历日期。通过本轮指定的网页内容提取服务取得此 URL 的内容，允许自行处理服务返回的 HTML、文本或结构化内容；不用其他网站、日历数据集、模型记忆、搜索摘要或绕过指定服务直读原网页代替。 | 指定服务真实取得该网页的目标表内容；CSV 三列与输入约定一致，全部假日逐项日期、星期、名称正确，无漏行、重复或其他年份，日期升序，脚注标记不混入字段；文件确实存在且可解析，答复含文件位置及来源链接。允许不改变含义的空白、换行和直弯撇号差异；不要求特定解析库、调用次数或服务原始返回格式。 |

| 服务 | 本次任务 | 起点 |
| --- | --- | --- |
| [Firecrawl / API](./generated/evaluations.md#comparison-c49d8e01e18c) | 我在把一份旧扫描手册整理成可检索的表格。请从材料指定的 TTB Table No. 4 中，把 Proof 从 1.0 到 2.0 的这一小段转成 CSV，保留两种 gallons per pound 数值，给我文件和官方来源链接。只抄录原表，不做计税或其他业务计算。 | 接入准备: none; anonymous public extraction routes, no account/email/token/payment supplied |
| [Exa / MCP](./generated/evaluations.md#comparison-c49d8e01e18c) | 我在把一份旧扫描手册整理成可检索的表格。请从材料指定的 TTB Table No. 4 中，把 Proof 从 1.0 到 2.0 的这一小段转成 CSV，保留两种 gallons per pound 数值，给我文件和官方来源链接。只抄录原表，不做计税或其他业务计算。 | 接入准备: none; anonymous public extraction routes, no account/email/token/payment supplied |
| [Exa / MCP](./generated/evaluations.md#comparison-032f75889210) | 我想把官方假日表用于个人日历整理。请从附件给定的网页提取 2027 年假日安排，做成按日期排序的 CSV 文件，包含表中全部假日的日期、星期和英文名称；按网页列出的日期记录，并给我文件和来源链接。 | 未预供账号或密钥 |
| [Firecrawl / API](./generated/evaluations.md#comparison-032f75889210) | 我想把官方假日表用于个人日历整理。请从附件给定的网页提取 2027 年假日安排，做成按日期排序的 CSV 文件，包含表中全部假日的日期、星期和英文名称；按网页列出的日期记录，并给我文件和来源链接。 | 未预供账号或密钥 |

**测试配置：** 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 · 2026-10-08（UTC）

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义 1](./data/experiments/tasks/web-extraction-pdf.md) · [任务定义 2](./data/experiments/tasks/web-extraction.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-web-search-data-geocoding"></a>

#### 地理编码 (5)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#nominatim">Nominatim Public API</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://nominatim.openstreetmap.org/search">API</a></td><td align="left"><a href="https://nominatim.org/release-docs/latest/api/Search/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#photon">Photon Public Demo API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-3bcbfb46bd35">100%</a></td><td align="right">253.5k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://photon.komoot.io/api/">API</a></td><td align="left"><a href="https://photon.komoot.io/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我接通这个地理编码服务，通过指定方式做一次真实地点查询，确认能把地点或地址转成坐标，并保存后续查询需要的本地配置；说明接入步骤和实际阻碍。**

服务、指定入口、允许使用的账号或注册资料及其来源见 ENVIRONMENT.md。自行选一个公开地点做小型查询，给出匹配地点、明确标注纬度和经度的坐标及来源。无需账号的入口直接使用；需注册或授权时仅使用本轮提供的身份资料。必要配置保存在本轮持久目录，秘密仅存私有文件；答复给出配置位置、已有账号来源、自助步骤、人工介入或额外申请要求。

完成标准：按指定方式完成必要注册、认证、安装和配置；真实响应含可识别地点和有效经纬度，答复与响应一致，配置可供新会话复用且不泄露秘密。免注册入口不强行注册，已有账号不冒充本轮自助注册。

**测试配置：** 1.18.35 · deepseek-flash / high · 5 分钟 · 2026-10-08（UTC） · 接入准备: none; official low-volume public route selected deliberately for one public-venue research task

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/geocoding.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#photon">Photon Public Demo API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-c820e750045c">100%</a></td><td align="right">100.3k</td><td align="right">$0.0090</td><td align="right">$0</td><td align="left"><a href="https://photon.komoot.io/api/">API</a></td><td align="left"><a href="https://photon.komoot.io/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#geoapify">Geoapify</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://apidocs.geoapify.com/docs/geocoding/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#geocode-maps-co">Geocode Maps.co</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://geocode.maps.co/docs/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#locationiq">LocationIQ</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.locationiq.com/docs/search-forward-geocoding">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#nominatim">Nominatim Public API</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://nominatim.org/release-docs/latest/api/Search/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：我想在旅行地图上标记大英博物馆。请用指定服务把附件中的场馆地址转成可用坐标，用中文给出匹配地点名称、明确标注纬度和经度的 WGS84 十进制度坐标、服务实际返回的地址信息和数据来源，并说明这是场馆、入口还是更粗略的定位。**

地点：The British Museum；地址：Great Russell Street, London WC1B 3DG, United Kingdom。用途是行程概览中的场馆标记，定位到场馆本身即可，场馆中心或入口都可以；相对场馆官方位置点，200 米以内的地点级位置误差可接受，无需精确到门口。街道、邮编或城市中心不能冒充场馆。只用本轮指定服务的实际查询结果；没有返回的地址字段如实注明，不补造，输入地址与服务返回地址分开说明；未提供足够精度时如实说明。

完成标准：通过指定服务真实查询并匹配到伦敦大英博物馆或其入口；最终坐标与该对象的真实响应一致，坐标轴及单位正确，并位于事前冻结的官方场馆位置点 200 米内，允许合理展示舍入。名称、位置和返回对象的语义共同支持场馆身份，不能仅凭落在半径内把粗略区域对象当场馆。来源、实际返回的地址及粒度说明可核对，未返回字段不捏造；不要求两家服务坐标相同、地址逐字相同或提供固定字段集。

**测试配置：** 1.18.35 · deepseek-flash / high · 10 分钟 · 2026-10-08（UTC） · 接入准备: none; official low-volume public route selected deliberately for one public-venue research task

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/geocoding.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-web-search-data-route-planning"></a>

#### 路线规划 (2)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#osrm">OSRM Public Demo API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-6d420b99e4b1">100%</a></td><td align="right">57.9k</td><td align="right">$0.0054</td><td align="right">—</td><td align="left"><a href="https://router.project-osrm.org/route/v1/driving">API</a></td><td align="left"><a href="https://project-osrm.org/docs/v26.5.0/http">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#valhalla">Valhalla Public Demo API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-6d420b99e4b1">100%</a></td><td align="right">281.3k</td><td align="right">$0.01</td><td align="right">—</td><td align="left"><a href="https://valhalla1.openstreetmap.de/route">API</a></td><td align="left"><a href="https://valhalla.github.io/valhalla/api/route/api-reference/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我接通这个路线规划服务，通过指定入口查询附件两个点之间的一段小汽车路线，告诉我服务给出的距离和估算驾驶时间，确认可以用；保存后续调用所需配置，并说明接入步骤和实际门槛。**

接通用的示例位于美国 Seattle 的 I-5。WGS84 十进制度：起点纬度 47.628282、经度 -122.327649；终点纬度 47.619214、经度 -122.328222。按起点到终点查询普通小汽车路线，不用步行、骑行或公交，不做地址搜索。通过 ENVIRONMENT.md 指定的服务和入口取得真实路线，给出返回距离和估算驾驶时间并标明单位。无需账号的入口直接使用；需额外身份、授权或人工操作时说明阻碍，不借用本机账号。必要安装和通用配置存本轮指定持久目录，秘密不出现在答复中；如实说明自助步骤、人工介入和额外申请。

完成标准：必要安装、配置和认证完成，实际按给定起终点及小汽车模式查询指定入口并取得有效路线；答复距离与时间正确反映该响应，通用配置可供新会话复用，不泄露秘密，接入来源与人工门槛如实说明。不要求接入阶段另交路线文件或证明预计用时等于实测驾驶时间。

**测试配置：** 1.18.35 · deepseek-flash / high · 5 分钟 · 2026-10-08（UTC） · 接入准备: none; anonymous FOSSGIS public demos, no account/token/email/payment supplied

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/route-planning.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#osrm">OSRM Public Demo API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-f0300fd67f1a">100%</a></td><td align="right">166.3k</td><td align="right">$0.01</td><td align="right">—</td><td align="left"><a href="https://router.project-osrm.org/route/v1/driving">API</a></td><td align="left"><a href="https://project-osrm.org/docs/v26.5.0/http">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#valhalla">Valhalla Public Demo API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-f0300fd67f1a">100%</a></td><td align="right">182.1k</td><td align="right">$0.01</td><td align="right">—</td><td align="left"><a href="https://valhalla1.openstreetmap.de/route">API</a></td><td align="left"><a href="https://valhalla.github.io/valhalla/api/route/api-reference/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：我在整理旅行地图，想保存从附件南侧点到北侧点、开车穿过金门大桥的路线。请给出总里程、服务估算的驾驶时间、主要道路和行驶方向，交付一份可留存到地图中的路线文件，并注明来源。**

美国 San Francisco Bay 的 Golden Gate Bridge 公路段。WGS84 十进制度：A 南侧点纬度 37.810193、经度 -122.477383；B 北侧点纬度 37.830233、经度 -122.479740。普通小汽车，从 A 到 B 沿金门大桥公路向北，不加中途停靠或绕回，不改走其他桥、渡轮、步行或骑行路线。这是行程地图记录，不需车道级精度：实际路线的起终点允许分别匹配在给定点 50 米内的同一公路上；跨桥线路相对所述公路中心线的道路级位置偏差允许 50 米。不指定出发时刻，只要指定服务给出的普通路线估算，不要求实时交通、当前开放状态或到达时间保证。距离用公里、驾驶时间用分钟并标明是估算；保留主要道路名称和北行方向的简短概述，不必逐条转写所有导航指令。文件为 GPX track 或 WGS84 GeoJSON LineString 之一（GeoJSON 可包在 Feature 或 FeatureCollection 中），保存同一真实服务路线的连续形状和起终点顺序，供以后放入地图，不只保存两个标记或自行连接起终点代替服务路线。通过本轮指定服务查询，不用另一服务、预存轨迹或模型记忆补答案。

完成标准：实际使用指定入口按 A→B 和小汽车模式取得路线；交付文件来自同一返回线路，坐标轴、顺序及连续性正确，起终点分别满足可见的 50 米范围，沿独立官方道路参考确认的金门大桥公路走廊向北且满足可见的 50 米道路级容差；没有其他桥、渡轮、步行路线、增加停靠或绕回。距离和时间按服务响应正确换算为公里、分钟，允许合理舍入；主要道路、方向、文件位置与来源准确。不同服务的路线细节、距离和估算时间不必相同，不以另一家结果或独立参考线长度作统一数值答案。

**测试配置：** 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 · 2026-10-08（UTC） · 接入准备: none; anonymous FOSSGIS public demos, no account/token/email/payment supplied

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/route-planning.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-web-search-data-public-holidays"></a>

#### 公共节假日 (2)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#nager-date">Nager.Date</a></td><td align="right"><a href="./generated/evaluations.md#comparison-0ce2de00d325">100%</a></td><td align="right">63.8k</td><td align="right">$0.0064</td><td align="right">$0</td><td align="left"><a href="https://nagerholidays.com/api/v4/Holidays">API</a></td><td align="left"><a href="https://nagerholidays.com/api">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#openholidays">OpenHolidays API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-0ce2de00d325">100%</a></td><td align="right">145.0k</td><td align="right">$0.0091</td><td align="right">$0</td><td align="left"><a href="https://openholidaysapi.org/PublicHolidays">API</a></td><td align="left"><a href="https://www.openholidaysapi.org/en/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我接通这个公共节假日查询服务，通过指定方式做一次真实的小范围假日查询，确认能查到日期和名称，并保存后续查询所需配置；说明接入步骤和实际阻碍。**

服务、指定入口、允许使用的账号或注册资料及其来源见 ENVIRONMENT.md。自行选择一个服务支持的国家或地区及年份，做一次小型公共节假日查询；报告查询范围、一个实际返回节日的日期与名称，并注明所用服务及查询来源。无需账号的入口直接使用；需要注册或授权时仅使用本轮提供的身份。必要配置保存在指定持久目录，秘密只存私有文件；答复给出配置位置、账号来源、自助步骤、人工介入和额外申请要求。

完成标准：按指定方式完成必要注册、授权、安装或配置；真实假日查询返回可识别的日期和名称，答复及范围与响应相符，配置可供新会话复用且不泄露秘密。免账号入口不强行注册，已有账号不算本轮自助注册。

**测试配置：** 1.18.35 · deepseek-flash / high · 5 分钟 · 2026-10-08（UTC） · 接入准备: none; anonymous publicAPI, no account/email/key/payment supplied

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/public-holidays.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#nager-date">Nager.Date</a></td><td align="right"><a href="./generated/evaluations.md#comparison-39d86ae45d95">100%</a></td><td align="right">158.8k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://nagerholidays.com/api/v4/Holidays">API</a></td><td align="left"><a href="https://nagerholidays.com/api">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#openholidays">OpenHolidays API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-39d86ae45d95">100%</a></td><td align="right">174.3k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://openholidaysapi.org/PublicHolidays">API</a></td><td align="left"><a href="https://www.openholidaysapi.org/en/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：我在整理明年在柏林的个人日程。请通过指定服务查出 2027 年适用于德国柏林州的全部公共节假日，按日期列出日期和节日名称，给出总数并注明查询来源。**

地区：德国 Berlin（柏林州，德国境内的整个州，不是其他同名城市）；时间：当地公历 2027-01-01 至 2027-12-31，含首尾。包括全国适用及柏林州适用的公共节假日，不混入只在其他州适用的节日、学校假期、仅纪念而非公共假日的日子或普通星期日。公共节假日即使落在周六或周日也照列，使用节日在柏林的实际当地日期，不自行移到工作日或推算补休。日期须明确到年、月、日；名称可用服务返回的德文或英文，无须中文翻译，同一节日同一天只列一次。这里仅整理日期供日程参考，不要求判断商店或银行营业、工作安排、工资或个人休假权益。通过本轮指定服务取得真实假日数据；可查其官方文档理解地区与日期含义，不用其他假日服务、网页日历、示例或记忆替代查询。

完成标准：实际查询指定服务并正确限定柏林州及 2027 年；交付清单与事前冻结的独立官方日期参考对应，完整且无重复、无越界节日，日期与节日身份正确并按日期升序，总数准确，来源可追溯真实查询。允许德英文名称、正常标点和等价节日译名差异，不以供应商字段名、是否服务端过滤或响应条目排列作为完成条件。

**测试配置：** 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 · 2026-10-08（UTC） · 接入准备: none; anonymous publicAPI, no account/email/key/payment supplied

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/public-holidays.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-web-search-data-weather-data"></a>

#### 天气数据 (2)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#met-norway">MET Norway Locationforecast</a></td><td align="right"><a href="./generated/evaluations.md#comparison-7e7df525d550">100%</a></td><td align="right">112.5k</td><td align="right">$0.0082</td><td align="right">$0</td><td align="left"><a href="https://api.met.no/weatherapi/locationforecast/2.0/compact">API</a></td><td align="left"><a href="https://docs.api.met.no/doc/GettingStarted.html">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#open-meteo">Open-Meteo</a></td><td align="right"><a href="./generated/evaluations.md#comparison-7e7df525d550">100%</a></td><td align="right">238.5k</td><td align="right">$0.02</td><td align="right">$0</td><td align="left"><a href="https://api.open-meteo.com/v1/forecast">API</a></td><td align="left"><a href="https://open-meteo.com/en/docs">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我接通这个天气服务，通过指定方式做一次真实天气查询，确认能用，并保存后续查询需要的本地配置；说明完成的接入步骤和实际阻碍。**

服务、指定入口、允许使用的账号或注册资料及其来源见 ENVIRONMENT.md。自行选择一个公开地点做小型查询，报告地点、天气数值与单位及其预报或观测时间。无需账号的入口直接使用；需注册或授权时仅使用本轮提供的身份资料。必要配置保存在本轮持久目录，秘密仅存私有文件；答复给出配置位置、已有账号来源、自助步骤、人工介入或额外申请要求。

完成标准：按指定方式完成必要注册、认证、安装和配置，真实响应含可识别地点、有效时间及至少一个天气数值，答复与响应一致且注明单位；配置可供新会话复用且不泄露秘密。免注册入口不强行注册，已有账号不冒充本轮自助注册。

**测试配置：** 1.18.35 · deepseek-flash / high · 5 分钟 · 2026-10-08（UTC） · 接入准备: none; official public read-only free noncommercial route

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/weather-data.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#met-norway">MET Norway Locationforecast</a></td><td align="right"><a href="./generated/evaluations.md#comparison-728ca7b6aa38">100%</a></td><td align="right">115.2k</td><td align="right">$0.0088</td><td align="right">$0</td><td align="left"><a href="https://api.met.no/weatherapi/locationforecast/2.0/compact">API</a></td><td align="left"><a href="https://docs.api.met.no/doc/GettingStarted.html">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#open-meteo">Open-Meteo</a></td><td align="right"><a href="./generated/evaluations.md#comparison-728ca7b6aa38">100%</a></td><td align="right">35.5k</td><td align="right">$0.0042</td><td align="right">$0</td><td align="left"><a href="https://api.open-meteo.com/v1/forecast">API</a></td><td align="left"><a href="https://open-meteo.com/en/docs">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：我 10 月 10 日上午要去伦敦市中心散步，请用中文把当地时间 09:00–12:00 三个小时的预报气温和降水量整理成小表，标明单位、数据来源和查询时间（注明时区），并简要指出哪些时段预计有降水。**

日期为 2026-10-10；地点为伦敦市中心，直接使用给定的 WGS84 坐标：纬度 51.5074、经度 -0.1278，不需另找地址或地理编码。当地时区 Europe/London。表格分别列出 09:00–10:00、10:00–11:00、11:00–12:00 三个完整小时区间；每行气温取该区间开始整点的近地面气温，使用摄氏度；降水使用该整小时累计总降水量，单位毫米，雨雪按水当量合计。只用本轮指定服务在查询时提供的预报；缺失数据如实说明，不把缺失当零，也不把较长时段的总量平均分配成小时数值。

完成标准：实际通过指定服务取得该坐标附近、覆盖全部指定时段的预报；表格的有效时间、时区、温度时点、降水累计区间和单位转换正确，数值与本次真实预报响应一致，允许按展示精度正确舍入；三个区间无遗漏或重复，缺失不伪装成零；来源和查询时间可核对，降水说明由所用数据支持。各服务按其本次真实预报独立核验，不以不同预报模型数值相同或未来实况是否命中作为本题通过标准。

**测试配置：** 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 · 2026-10-08（UTC） · 接入准备: none; official public read-only free noncommercial route

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/weather-data.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-web-search-data-financial-data"></a>

#### 金融数据 (33)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#alpha-vantage">Alpha Vantage</a></td><td align="right"><a href="./generated/evaluations.md#comparison-29077cd73ecd">100%</a></td><td align="right">564.6k</td><td align="right">$0.03</td><td align="right">—</td><td align="left"><a href="https://mcp.alphavantage.co/mcp">MCP</a></td><td align="left"><a href="https://www.alphavantage.co/documentation/">API</a> · <a href="https://mcp.alphavantage.co/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#bargo-congress">Bargo Congress Trades API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-a3477334d9b4">100%</a></td><td align="right">97.5k</td><td align="right">$0.0068</td><td align="right">$0</td><td align="left"><a href="https://www.bargo.ai/free-apis/congress/v1">API</a></td><td align="left"><a href="https://www.bargo.ai/free-apis/congress">API / MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#capitol-exposed">CapitolExposed</a></td><td align="right"><a href="./generated/evaluations.md#comparison-a3477334d9b4">0%</a></td><td align="right">300.5k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://www.capitolexposed.com/api/v1">API</a></td><td align="left"><a href="https://www.capitolexposed.com/api-docs">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#ecb-data">ECB Data Portal API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-8a11046c9744">100%</a></td><td align="right">123.3k</td><td align="right">$0.0086</td><td align="right">—</td><td align="left"><a href="https://data-api.ecb.europa.eu/service/">API</a></td><td align="left"><a href="https://data.ecb.europa.eu/help/api/data-examples">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#frankfurter">Frankfurter</a></td><td align="right"><a href="./generated/evaluations.md#comparison-8a11046c9744">100%</a></td><td align="right">113.3k</td><td align="right">$0.0081</td><td align="right">$0</td><td align="left"><a href="https://api.frankfurter.dev/v2/">API</a></td><td align="left"><a href="https://frankfurter.dev/">API</a> · <a href="https://frankfurter.dev/mcp/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#sec-edgar">SEC EDGAR Data APIs</a></td><td align="right"><a href="./generated/evaluations.md#comparison-33be83cbd5a7">100%</a></td><td align="right">111.5k</td><td align="right">$0.0100</td><td align="right">$0</td><td align="left"><a href="https://data.sec.gov/">API</a></td><td align="left"><a href="https://www.sec.gov/search-filings/edgar-application-programming-interfaces">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#tracefour">Tracefour</a></td><td align="right"><a href="./generated/evaluations.md#comparison-f170f4b6c34f">0%</a></td><td align="right">107.3k</td><td align="right">$0.0071</td><td align="right">$0</td><td align="left"><a href="https://tracefour.com/v1">API</a></td><td align="left"><a href="https://tracefour.com/api-docs">API</a> · <a href="https://tracefour.com/api-docs/mcp">MCP</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我把这个金融数据服务接好，确认能用指定方式查询数据，并保存后续调用需要的配置；如果接不通，说明卡在哪里。**

服务、指定调用方式、提供的账户或注册资料见运行环境。无需账号的入口直接使用；需注册的入口仅使用本轮提供的身份资料。保存必要连接配置供后续任务使用。

完成标准：按指定方式完成必要注册、认证和配置，并成功查询一项真实金融数据；所需配置可用于新的会话。不需要账号时不强行注册；仅文档、健康检查或配置文件不足以证明可查询数据。

| 服务 | 测试配置 | 起点 |
| --- | --- | --- |
| [Alpha Vantage](./generated/evaluations.md#comparison-29077cd73ecd) | 1.18.35 · deepseek-flash / high · 5 分钟 | 接入准备: controller-registered ordinary free API key; same existing account for REST and MCP |
| [SEC EDGAR Data APIs](./generated/evaluations.md#comparison-33be83cbd5a7) | 1.18.35 · deepseek-flash / high · 5 分钟 | 接入准备: none; contact identity only |
| [ECB Data Portal API](./generated/evaluations.md#comparison-8a11046c9744) | 1.18.35 · deepseek-flash / high · 5 分钟 | 未预供账号或密钥 |
| [Frankfurter](./generated/evaluations.md#comparison-8a11046c9744) | 1.18.35 · deepseek-flash / high · 5 分钟 | 未预供账号或密钥 |
| [Bargo Congress Trades API](./generated/evaluations.md#comparison-a3477334d9b4) | 1.18.35 · glm-5.3-flash / high · 15 分钟 | 未预供账号或密钥 |
| [CapitolExposed](./generated/evaluations.md#comparison-a3477334d9b4) | 1.18.35 · glm-5.3-flash / high · 15 分钟 | 未预供账号或密钥 |
| [Tracefour](./generated/evaluations.md#comparison-f170f4b6c34f) | 1.18.29 · glm-5.3-flash / high · 10 分钟 | 未预供账号或密钥 |

**测试配置：** 2026-09-15 – 2026-10-08（UTC）

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/financial-data.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

以下服务暂按本层范围收录，细分缺口见服务详情。

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#factset-data">FactSet Data APIs</a></td><td align="left">Financial-data API catalog; retained as an institutional candidate while product-specific access is researched.</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#joinquant-data">JoinQuant JQData</a></td><td align="left">Chinese-market data candidate. The official documentation returned a non-Mainland-China region restriction during research.</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#lseg-data">LSEG Data Platform</a></td><td align="left">Financial-data platform and Python library with licensed desktop and cloud access paths.</td><td align="left"><a href="https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/quick-start">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#nasdaq-data-link">Nasdaq Data Link</a></td><td align="left">Marketplace for financial and economic datasets with free and separately subscribed products.</td><td align="left"><a href="https://docs.data.nasdaq.com/docs/getting-started">API</a></td></tr>
</tbody>
</table>

<a id="services-web-search-data-financial-data-fx"></a>

##### 汇率数据 (7)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#ecb-data">ECB Data Portal API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-8c4b61fb41be">100%</a></td><td align="right">58.3k</td><td align="right">$0.0053</td><td align="right">$0</td><td align="left"><a href="https://data-api.ecb.europa.eu/service/">API</a></td><td align="left"><a href="https://data.ecb.europa.eu/help/api/data-examples">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#frankfurter">Frankfurter</a></td><td align="right"><a href="./generated/evaluations.md#comparison-8c4b61fb41be">100%</a></td><td align="right">51.8k</td><td align="right">$0.0052</td><td align="right">$0</td><td align="left"><a href="https://api.frankfurter.dev/v2/">API</a></td><td align="left"><a href="https://frankfurter.dev/">API</a> · <a href="https://frankfurter.dev/mcp/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#alpha-vantage">Alpha Vantage</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.alphavantage.co/documentation/">API</a> · <a href="https://mcp.alphavantage.co/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fmp">Financial Modeling Prep (FMP)</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://site.financialmodelingprep.com/developer/docs">API</a> · <a href="https://site.financialmodelingprep.com/developer/docs/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#open-exchange-rates">Open Exchange Rates</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.openexchangerates.org/reference/api-introduction">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#tiingo">Tiingo</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.tiingo.com/documentation/general/overview">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#twelve-data">Twelve Data</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://twelvedata.com/docs/introduction/quickstart">API / SDK</a> · <a href="https://github.com/twelvedata/twelvedata-cli">CLI</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：把这三笔美元支出按发生当日的欧洲央行参考汇率折算成欧元，列出每笔金额和合计，并给出汇率出处。**

合成支出：2026-08-14，80.00 USD；2026-08-15，125.00 USD；2026-08-17，39.90 USD。若当日未发布汇率，使用此前最近一个发布日；逐笔四舍五入到欧分，再加总。不计手续费。

完成标准：使用指定日期对应的 ECB USD/EUR 参考数据；非发布日回退正确；币种方向及乘除关系正确；三笔金额和按规定舍入后的合计与独立计算一致；核心汇率来自指定服务。

**测试配置：** 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 · 2026-10-08（UTC） · 未预供账号或密钥

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/financial-data.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-web-search-data-financial-data-prices"></a>

##### 资产行情 (15)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#alpha-vantage">Alpha Vantage</a></td><td align="right"><a href="./generated/evaluations.md#comparison-965a5e31dfe6">100%</a></td><td align="right">214.9k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://mcp.alphavantage.co/mcp">MCP</a></td><td align="left"><a href="https://www.alphavantage.co/documentation/">API</a> · <a href="https://mcp.alphavantage.co/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#agentservices">AgentServices</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://github.com/vbkotecha/agentservices-api/blob/main/docs/buyer-quickstart.md">API</a> · <a href="https://github.com/vbkotecha/agentservices-api/blob/main/sdk/README.md">SDK</a> · <a href="https://github.com/vbkotecha/agentservices-api/blob/main/README.md#using-as-mcp-server-claude-desktop-cursor-etc">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#alpaca-market-data">Alpaca Market Data</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.alpaca.markets/us/docs/about-market-data-api">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#bloomberg-data-license">Bloomberg Data License</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#coingecko">CoinGecko</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.coingecko.com/docs/setting-up-your-api-key">API</a> · <a href="https://docs.coingecko.com/ai-integration/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#coinmarketcap">CoinMarketCap</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#eodhd">EODHD</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://eodhd.com/financial-apis/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#financial-datasets">Financial Datasets</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.financialdatasets.ai/quickstart">API</a> · <a href="https://docs.financialdatasets.ai/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fmp">Financial Modeling Prep (FMP)</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://site.financialmodelingprep.com/developer/docs">API</a> · <a href="https://site.financialmodelingprep.com/developer/docs/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#finnhub">Finnhub</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://finnhub.io/docs/api/quote">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#massive">Massive (formerly Polygon.io)</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://massive.com/docs/rest/quickstart">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#simfin">SimFin</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://github.com/SimFin/simfin#readme">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#tiingo">Tiingo</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.tiingo.com/documentation/general/overview">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#tushare">Tushare Pro</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://tushare.pro/document/1?doc_id=40">API / SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#twelve-data">Twelve Data</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://twelvedata.com/docs/introduction/quickstart">API / SDK</a> · <a href="https://github.com/twelvedata/twelvedata-cli">CLI</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我画出苹果公司 2026 年 8 月的每日收盘价走势，使用不复权价格，并附上 CSV 和数据来源。**

苹果公司 Apple Inc.，纳斯达克 AAPL，美元计价；2026-08-01 至 2026-08-31；常规交易日的日收盘价，不含盘前盘后。

完成标准：日期覆盖该月全部交易日且不含伪造的休市日；无重复、缺失或错误币种；价格与事前冻结的同口径参考序列一致，差异超过报价精度时逐项复核；图表与 CSV 数值一致；数据确实来自指定服务。

**测试配置：** 1.18.35 · deepseek-flash / high · 10 分钟 · 2026-10-08（UTC） · 接入准备: controller-registered ordinary free API key; same existing account for REST and MCP

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/financial-data.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-web-search-data-financial-data-statements"></a>

##### 公司财务数据 (7)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#alpha-vantage">Alpha Vantage</a></td><td align="right"><a href="./generated/evaluations.md#comparison-85831928a49a">100%</a></td><td align="right">188.6k</td><td align="right">$0.02</td><td align="right">$0</td><td align="left"><a href="https://www.alphavantage.co/query">API</a></td><td align="left"><a href="https://www.alphavantage.co/documentation/">API</a> · <a href="https://mcp.alphavantage.co/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#sec-edgar">SEC EDGAR Data APIs</a></td><td align="right"><a href="./generated/evaluations.md#comparison-01f9c83debc7">100%</a></td><td align="right">96.3k</td><td align="right">$0.0084</td><td align="right">$0</td><td align="left"><a href="https://data.sec.gov/">API</a></td><td align="left"><a href="https://www.sec.gov/search-filings/edgar-application-programming-interfaces">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#eodhd">EODHD</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://eodhd.com/financial-apis/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#financial-datasets">Financial Datasets</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.financialdatasets.ai/quickstart">API</a> · <a href="https://docs.financialdatasets.ai/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fmp">Financial Modeling Prep (FMP)</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://site.financialmodelingprep.com/developer/docs">API</a> · <a href="https://site.financialmodelingprep.com/developer/docs/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#simfin">SimFin</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://github.com/SimFin/simfin#readme">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#tushare">Tushare Pro</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://tushare.pro/document/1?doc_id=40">API / SDK</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：比较苹果和微软 2025 财年的营收、净利润和经营现金流，做成表格并附原始财报出处。**

Apple Inc. / AAPL 与 Microsoft / MSFT；各公司自身的 2025 财年全年合并报表；使用截至 2026-09-09 已公开的 GAAP 报告。注明各自财年结束日期，金额统一为十亿美元。

完成标准：六个指标与事前保存的各公司 2025 年报匹配，允许显示单位带来的舍入；不混用自然年、单季度、TTM 或调整后利润；财年结束日期和单位正确；原始披露能支持所列指标；核心数据来自指定服务。

| 服务 | 起点 |
| --- | --- |
| [Alpha Vantage](./generated/evaluations.md#comparison-85831928a49a) | 接入准备: controller-registered ordinary free API key |
| [SEC EDGAR Data APIs](./generated/evaluations.md#comparison-01f9c83debc7) | 接入准备: none; contact identity only |

**测试配置：** 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 · 2026-10-08（UTC）

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/financial-data.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-web-search-data-financial-data-disclosures"></a>

##### 交易披露 (12)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#bargo-congress">Bargo Congress Trades API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-1d87fed8bbbd">50%</a></td><td align="right">—</td><td align="right">—</td><td align="right">$0</td><td align="left"><a href="https://www.bargo.ai/free-apis/congress/v1">API</a></td><td align="left"><a href="https://www.bargo.ai/free-apis/congress">API / MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#capitol-exposed">CapitolExposed</a></td><td align="right"><a href="./generated/evaluations.md#comparison-60de41521941">100%</a></td><td align="right">227.5k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://www.capitolexposed.com/api/v1">API</a></td><td align="left"><a href="https://www.capitolexposed.com/api-docs">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#alpha-vantage">Alpha Vantage</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.alphavantage.co/documentation/">API</a> · <a href="https://mcp.alphavantage.co/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#capitol-trades">Capitol Trades</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#congress-stock-tracker">Congress Stock Tracker</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.congressstock.com/congress-trading-api">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#eodhd">EODHD</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://eodhd.com/financial-apis/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#financial-datasets">Financial Datasets</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.financialdatasets.ai/quickstart">API</a> · <a href="https://docs.financialdatasets.ai/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fmp">Financial Modeling Prep (FMP)</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://site.financialmodelingprep.com/developer/docs">API</a> · <a href="https://site.financialmodelingprep.com/developer/docs/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#insynet">Insynet</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://insynet.se/developers">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#quiver-quantitative">Quiver Quantitative</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.quiverquant.com/api-setup/">API</a> · <a href="https://api.quiverquant.com/mcp-server/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#tracefour">Tracefour</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://tracefour.com/api-docs">API</a> · <a href="https://tracefour.com/api-docs/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#us-house-disclosures">U.S. House Financial Disclosures</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left">—</td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

| 任务及条件 | 完成标准 |
| --- | --- |
| 帮我整理 Richard W. Allen 在 2026 年 8 月向美国众议院提交的股票买卖披露，列出股票、买卖方向、交易日期、提交日期和金额区间，并附原始申报出处。<br>申报人 Richard W. Allen，佐治亚州第 12 选区（GA12）；按官方提交日期筛选 2026-08-01 至 2026-08-31，截至 2026-09-15 已公开的定期交易申报（PTR）。包括申报中的家庭成员交易，金额以美元区间保留。股票指普通股，不包含期权、基金、债券或其他资产；不要把该月提交的记录解释成该月发生的交易。结果供本人阅读，不需要数据导出文件。 | 匹配事前冻结的官方年度索引和原始 PTR 中全部适用记录，字段和金额区间正确，无重复或无依据的记录；指定服务的真实查询支持这些披露，必要时可从原始文件核对日期与出处。提交日以官方索引为准，不混用交易日、通知日或服务抓取/发布日。不得把金额中点、估算价格或家庭成员交易表述为议员本人精确成交金额。来源可追溯到具体原始申报，仅列门户首页不足。 |
| 我的关注名单里有 Richard W. Allen、Donald Sternoff Beyer Jr、Rob Bresnahan 和 Ed Case。查一下他们 2026 年 8 月提交的披露中有哪些苹果股票买卖，列出明细；没有匹配记录的人也请说明，并附原始申报出处。<br>按官方提交日期筛选 2026-08-01 至 2026-08-31、截至 2026-09-15 已公开的美国众议院 PTR；包括家庭成员，普通股买卖，不含期权、基金、债券。结果供本人阅读，不需导出文件。 关注名单：Allen（GA12）、Beyer（VA08）、Bresnahan（PA08）、Case（HI01）；股票为 Apple Inc.（AAPL）。不能把服务未收录或查不到直接等同于没有交易，也不能从披露推断当前持仓。 | 四位身份与期间正确，全部匹配明细与冻结官方索引及 PTR 一致；无匹配结论同时有指定服务查询和官方范围核对依据，不能由报错或空响应单独推出。金额保留区间，来源定位到具体申报。 |
| 比较 Richard W. Allen 和 Ed Case 在 2026 年 8 月提交的股票披露：从交易发生到正式提交分别隔了多久？列出每笔的日期和天数，再按申报人汇总笔数、最短和最长间隔，并附原始申报出处。<br>按官方提交日期筛选 2026-08-01 至 2026-08-31、截至 2026-09-15 已公开的美国众议院 PTR；包括家庭成员，普通股买卖，不含期权、基金、债券。结果供本人阅读，不需导出文件。 Allen（GA12）、Case（HI01）。间隔按官方提交日减交易日的自然日计算，同日记 0；不使用通知日或平台上架日，不判断是否违法或是否值得跟投。 | 两位全部匹配交易及日期与独立冻结参考一致；逐笔自然日差、笔数、最短和最长值均正确；无记录时不编造统计；核心记录来自指定服务，官方索引或 PTR 可用于日期核对。 |
| 帮我核对这条待查说法：“Ed Case 本人在 2026 年 8 月 18 日主动买入了恰好 8,000 美元的苹果股票。”请逐项判断交易归属、日期、金额和交易性质，写出有依据的更正，并附原始申报出处。<br>按官方提交日期筛选 2026-08-01 至 2026-08-31、截至 2026-09-15 已公开的美国众议院 PTR；包括家庭成员，普通股买卖，不含期权、基金、债券。结果供本人阅读，不需导出文件。 Ed Case（HI01），Apple Inc.（AAPL）。引号内是研究者编写的合成待查说法，不是真实新闻引文；仅核对该月提交的相关披露。区分本人、配偶或共同持有，交易日和提交日，以及金额区间和精确金额；交易性质以原始说明为准，无依据就说无法确认。 | 真实指定服务记录与具体官方申报共同支持核对；归属、日期、金额、交易性质均与冻结参考相符；不能把区间中点当精确成交额、申报人当交易所有人，或遗漏影响说法真假的原始备注。 |

| 服务 | 测试配置 |
| --- | --- |
| [Bargo Congress Trades API](./generated/evaluations.md#comparison-1d87fed8bbbd) | 1.18.35 · glm-5.3-flash / high · 15 分钟 |
| [CapitolExposed](./generated/evaluations.md#comparison-60de41521941) | 1.18.29 · glm-5.3-flash / high · 15 分钟 · 独立验收（本轮无其他服务答案可参考） |

**测试配置：** 2026-09-15 – 2026-10-08（UTC） · 未预供账号或密钥

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/financial-data.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-web-search-data-financial-data-macro"></a>

##### 宏观经济指标 (5)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#alpha-vantage">Alpha Vantage</a></td><td align="left">Stock prices, company financials, FX, crypto and economic indicators. Free keys have a daily quota; premium endpoints are separate.</td><td align="left"><a href="https://www.alphavantage.co/documentation/">API</a> · <a href="https://mcp.alphavantage.co/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#ecb-data">ECB Data Portal API</a></td><td align="left">European Central Bank statistical data, including historical reference exchange rates, through SDMX REST.</td><td align="left"><a href="https://data.ecb.europa.eu/help/api/data-examples">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#eodhd">EODHD</a></td><td align="left">Historical market prices, fundamentals, economic datasets and congressional trades, with dataset-specific plan entitlements.</td><td align="left"><a href="https://eodhd.com/financial-apis/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fred">FRED / ALFRED</a></td><td align="left">Economic time series through a keyed API or an official account-authorized MCP; API and MCP registration are separate.</td><td align="left"><a href="https://fred.stlouisfed.org/docs/api/fred/">API</a> · <a href="https://fred.stlouisfed.org/help/data/connecting-fred-to-ai-services/FRED-MCP-Connector">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#world-bank-data">World Bank Indicators API</a></td><td align="left">Country-level economic and development indicators through the public Indicators API.</td><td align="left"><a href="https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation">API</a></td></tr>
</tbody>
</table>

<a id="services-productivity-storage"></a>

### 办公与协作 (15)

<a id="services-productivity-storage-qr-codes"></a>

#### 二维码图片 (2)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#goqr">goQR QR Code API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-1c64f31025f0">100%</a></td><td align="right">113.9k</td><td align="right">$0.0078</td><td align="right">—</td><td align="left"><a href="https://api.qrserver.com/v1/create-qr-code/">API</a></td><td align="left"><a href="https://goqr.me/api/doc/create-qr-code/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#quickchart">QuickChart</a></td><td align="right"><a href="./generated/evaluations.md#comparison-1c64f31025f0">100%</a></td><td align="right">127.3k</td><td align="right">$0.0082</td><td align="right">$0</td><td align="left"><a href="https://quickchart.io/qr">API</a></td><td align="left"><a href="https://quickchart.io/documentation/qr-codes/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我接通这个二维码服务，通过指定入口生成一张测试二维码并保存图片，确认我能开始使用；留下后续调用需要的通用配置，并说明接入步骤和实际门槛。**

测试内容为 https://example.com/ 。保存可打开的 PNG 二维码图片，扫码内容逐字就是这个网址。通过 ENVIRONMENT.md 指定的服务和入口生成；无需账号的入口直接使用。必要安装和通用配置保存在本轮指定持久目录；说明自助完成的步骤、人工介入、额外申请或具体阻碍，秘密不出现在答复中。

完成标准：必要安装和配置完成，通过指定服务实际生成并保存可打开的 PNG，独立离线解码内容与测试网址逐字相同；通用配置可供新会话复用，接入来源、人工步骤和阻碍如实说明，未泄露秘密。接入阶段不要求特定像素尺寸、配色、静区宽度或手机实扫。

**测试配置：** 1.18.35 · deepseek-flash / high · 5 分钟 · 2026-10-08（UTC） · 接入准备: none; public static QR APIs, no account/key/email/payment supplied

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/qr-codes.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#goqr">goQR QR Code API</a></td><td align="right"><a href="./generated/evaluations.md#comparison-0f505e0eb8fb">100%</a></td><td align="right">58.9k</td><td align="right">$0.0059</td><td align="right">$0</td><td align="left"><a href="https://api.qrserver.com/v1/create-qr-code/">API</a></td><td align="left"><a href="https://goqr.me/api/doc/create-qr-code/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#quickchart">QuickChart</a></td><td align="right"><a href="./generated/evaluations.md#comparison-0f505e0eb8fb">100%</a></td><td align="right">145.8k</td><td align="right">$0.0084</td><td align="right">$0</td><td align="left"><a href="https://quickchart.io/qr">API</a></td><td align="left"><a href="https://quickchart.io/documentation/qr-codes/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我把材料里的国家公园旅行指南链接做成一张静态二维码 PNG，放进我打印的旅行资料。按材料里的尺寸和配色制作，扫码直接得到完整原链接，并把图片文件交给我。**

原始链接：https://www.nps.gov/zion/planyourvisit/loader.cfm?csModule=security/getfile&pageid=8166212 。图片为 600×600 像素，黑色码块、不透明白色背景，允许码块边缘有灰度抗锯齿；图里只放这一个二维码，不加文字或 logo。扫码内容必须逐字等于上面的完整原始链接，不使用短链接、跳转跟踪链接，也不要增删或改写查询参数。通过本轮指定服务生成这张图片并保存到本地，答复给出文件位置；不用访问链接目标，也不用做实物打印或手机扫描。

完成标准：实际通过指定服务生成二维码并交付可打开的 PNG 文件，尺寸恰为 600×600，白底不透明、码块黑色且只有灰度边缘，没有额外文字或 logo；独立离线解码所得原始字节与可见的完整 ASCII URL 逐字相同，无缺失、改写或跟踪跳转包装，答复指出真实文件位置。允许不同 QR 版本、纠错等级、掩码、PNG 色彩模式与压缩方式；不要求两服务图片像素或文件哈希相同，不用静区模块数、DPI 或实物打印表现判定完成。

**测试配置：** 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 · 2026-10-08（UTC） · 接入准备: none; public static QR APIs, no account/key/email/payment supplied

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/qr-codes.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-productivity-storage-collaborative-tables"></a>

#### 协作表格 (8)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#grist">Grist</a></td><td align="right"><a href="./generated/evaluations.md#comparison-5bcdeb33cbc4">100%</a></td><td align="right">357.7k</td><td align="right">$0.02</td><td align="right">$0</td><td align="left"><a href="https://docs.getgrist.com/api/mcp">MCP</a></td><td align="left"><a href="https://support.getgrist.com/api/">API</a> · <a href="https://support.getgrist.com/rest-api/">SDK</a> · <a href="https://support.getgrist.com/mcp/">MCP</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我通过指定方式接通这个在线表格服务，新建一个本轮专用的空测试空间，读取它确认可用，并保存后续创建任务表所需的配置；给我空间链接，说明接入步骤、人工门槛和免费限制。**

服务、指定入口、允许使用的账户或注册身份及来源见 ENVIRONMENT.md。按需注册、授权、安装和配置；已有账号如实说明来源。新建一个可容纳后续任务表的独立空测试容器，例如工作区、base 或父文档，名称带本轮环境提供的标识。通过指定方式重新读取该容器的元数据，确认访问的是同一远端资源；本阶段不整理会议内容、不预建业务字段或记录。保存必要安装、容器标识和连接配置到本轮指定持久目录，秘密仅存私有文件，答复只给配置位置。说明真实自助步骤、人工介入、额外申请和已知免费限制；无法完成时说明具体阻碍。

完成标准：完成必要接入，通过指定服务及入口新建本轮独立空容器，并重新读取同一远端容器的元数据确认可访问；链接和标识一致，必要配置可供新会话复用且不泄露秘密。未预建业务字段、记录或答案；实际账号来源、自助步骤、人工门槛和免费限制如实说明。只有注册、安装、工具列表、创建回执或本地模拟不足以证明接通。

**测试配置：** 1.18.35 · deepseek-flash / high · 5 分钟 · 2026-10-08（UTC） · 已预供服务凭据

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/collaborative-tables-access.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#grist">Grist / hosted-mcp</a></td><td align="right"><a href="./generated/evaluations.md#comparison-892c10c8ee63">100%</a></td><td align="right">200.6k</td><td align="right">$0.01</td><td align="right">$0</td><td align="left"><a href="https://docs.getgrist.com/api/mcp">MCP</a></td><td align="left"><a href="https://support.getgrist.com/api/">API</a> · <a href="https://support.getgrist.com/rest-api/">SDK</a> · <a href="https://support.getgrist.com/mcp/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#grist">Grist / hosted-mcp</a></td><td align="right"><a href="./generated/evaluations.md#comparison-cb6f4b024594">100%</a></td><td align="right">769.0k</td><td align="right">$0.03</td><td align="right">$0</td><td align="left"><a href="https://docs.getgrist.com/api/mcp">MCP</a></td><td align="left"><a href="https://support.getgrist.com/api/">API</a> · <a href="https://support.getgrist.com/rest-api/">SDK</a> · <a href="https://support.getgrist.com/mcp/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#grist">Grist / rest-api</a></td><td align="right"><a href="./generated/evaluations.md#comparison-ab4e4c0d9054">100%</a></td><td align="right">540.8k</td><td align="right">—</td><td align="right">$0</td><td align="left"><a href="https://support.getgrist.com/api/">API</a></td><td align="left"><a href="https://support.getgrist.com/api/">API</a> · <a href="https://support.getgrist.com/rest-api/">SDK</a> · <a href="https://support.getgrist.com/mcp/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#notion">Notion</a></td><td align="right"><a href="./generated/evaluations.md#comparison-8cc2ab7b2dcd">100%</a></td><td align="right">215.5k</td><td align="right">$0.75</td><td align="right">$0</td><td align="left"><a href="https://developers.notion.com/reference/intro">API</a></td><td align="left"><a href="https://developers.notion.com/guides/get-started/internal-connections">API</a> · <a href="https://github.com/makenotion/notion-sdk-js">SDK</a> · <a href="https://developers.notion.com/cli/get-started/overview">CLI</a> · <a href="https://developers.notion.com/guides/mcp/get-started-with-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#airtable">Airtable</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://airtable.com/developers/web/api/introduction">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#baserow">Baserow Cloud</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://baserow.io/docs/apis/rest-api">API</a> · <a href="https://baserow.io/user-docs/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#coda">Coda / Superhuman Docs</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://coda.io/developers/apis/v1">API</a> · <a href="https://help.coda.io/hc/en-us/articles/44722661982989-Connect-to-the-Coda-MCP">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#google-sheets">Google Sheets</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://developers.google.com/workspace/sheets/api/quickstart/python">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#lark">Lark</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://open.larksuite.com/document/server-docs/getting-started/server-api-list">API</a> · <a href="https://github.com/larksuite/cli">CLI</a> · <a href="https://github.com/larksuite/lark-openapi-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#feishu">飞书 Feishu</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/create.md">API</a> · <a href="https://github.com/larksuite/cli">CLI</a> · <a href="https://github.com/larksuite/lark-openapi-mcp">MCP</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

| 任务及条件 | 完成标准 |
| --- | --- |
| 我和室友按一人一半分摊共同支出。请把材料里的 10 月账目做成在线账本，保留每笔日期、用途、付款人和人民币金额，并在表里显示各自已付、应分摊金额，以及谁还需补给谁多少钱。以后追加账目或修正金额时，汇总要自动更新，不用再找 Agent 或运行本地脚本。给我私人表格链接、当前结算数和一句话说明在哪里继续记账；不要实际转账、邀请或通知任何人。<br>两位合成人员是林青、周舟，所有列出的支出都由两人各承担 50%，本题尚无补差转账。记录如下（日期 / 用途 / 付款人 / 人民币元）：2026-10-01 / 房租 / 林青 / 1800.00；2026-10-02 / 超市采购（一） / 周舟 / 156.40；2026-10-03 / 电费 / 林青 / 92.60；2026-10-04 / 家居用品 / 周舟 / 48.00；2026-10-05 / 宽带 / 周舟 / 100.00；2026-10-07 / 超市采购（二） / 林青 / 203.00。每笔明细完整保留一次；金额及汇总以人民币元表示，精确到分。只做这两人本月的共同支出，不混入个人支出、退款、其他币种、已转账记录或其他月份，不需要第三人、按类别统计或银行连接。在线账本中的汇总要由明细持续计算：用户新增同类明细或修改现有金额后，各自已付、应分摊及补差方向与金额会相应更新，无需修改汇总值、再次运行本地程序或调用 Agent。字段名、表结构和计算实现可以自行选择。执行时只录入这六笔；交付后验收会在同一个本轮专用文档中模拟新增一笔这两人之间的本月共同支出，再修正一笔现有明细的金额，核对自动更新；不会改分摊比例、加入新人或引入上述范围外条件。验证后保留这些合成变更，并在测评记录中说明；你的当前结算答复仍按最初六笔核对。 | 通过指定服务入口在本轮新空容器建立真实在线账本，完整保留六笔初始明细；在线汇总及初次答复中的两人已付、应分摊和补差方向、金额与输入一致，链接指向该账本，继续记账说明可用。执行结束后，总控仅在该新文档按事前冻结的合成材料追加一笔明细、再修正一笔已有金额，不修改公式、结构或汇总值，不启动执行 Agent；各阶段的独立远端读取均证明明细和在线汇总正确相应变化。独立验收 Agent 核对初态、追加态、修正态原始回执与参考，不获得凭据或运行执行者自评代码。不要求特定字段名、公式语法、固定表数量或显示布局；按人民币分核对金额，允许正常原生数值表示误差。 |
| 把附件里的读书会会议待办整理成在线任务表，包含负责人、截止日期和完成状态。给我链接，并列出未完成事项、负责人和截止日期。<br>读书会筹备会记录（2026年9月8日）：林青负责确认场地，9月15日前搞定；周舟负责整理书单，9月16日前完成；陈禾负责制作海报，原定9月18日完成。这三件事开会时都还没做完。会后补充：周舟说书单已经整理好了，海报的截止时间改到9月20日，其他安排不变。 | 远端表恰好三项：确认场地/林青/2026-09-15/未完成、整理书单/周舟/2026-09-16/已完成、制作海报/陈禾/2026-09-20/未完成；答复的链接指向该表，未完成清单与远端一致。总控在执行结束后，以自己的可信只读 API 请求重新取得本轮新表的元数据、字段和全部记录，冻结原始回执、读取时间、资源对应关系及哈希；独立验收 Agent 核对脱敏回执、用户答复和冻结参考，不继承执行凭据、不执行被测者的代码。字段命名与操作顺序自由。 |
| 帮我把这份读书会会议记录里的待办整理成在线任务表，给我链接，再告诉我还有哪些没完成、各自什么时候到期。<br>读书会筹备会记录（2026年9月8日）：林青负责确认场地，9月15日前搞定；周舟负责整理书单，9月16日前完成；陈禾负责制作海报，原定9月18日完成。这三件事开会时都还没做完。会后补充：周舟说书单已经整理好了，海报的截止时间改到9月20日，其他安排不变。 | 远端表中恰好包含三项行动、负责人和最终截止日期正确、书单已完成且另两项未完成；答复给出该表链接并正确列出两项未完成事项及日期；准备者通过服务API独立读取确认。允许自由选择字段与操作顺序，不要求先写入旧状态或输出证据文件 |

| 服务 | 本次任务 | 测试配置 |
| --- | --- | --- |
| [Grist / MCP](./generated/evaluations.md#comparison-cb6f4b024594) | 我和室友按一人一半分摊共同支出。请把材料里的 10 月账目做成在线账本，保留每笔日期、用途、付款人和人民币金额，并在表里显示各自已付、应分摊金额，以及谁还需补给谁多少钱。以后追加账目或修正金额时，汇总要自动更新，不用再找 Agent 或运行本地脚本。给我私人表格链接、当前结算数和一句话说明在哪里继续记账；不要实际转账、邀请或通知任何人。 | 1.18.35 · deepseek-flash / high · 10 分钟 |
| [Grist / MCP](./generated/evaluations.md#comparison-892c10c8ee63) | 把附件里的读书会会议待办整理成在线任务表，包含负责人、截止日期和完成状态。给我链接，并列出未完成事项、负责人和截止日期。 | 1.18.35 · deepseek-flash / high · 10 分钟 |
| [Notion](./generated/evaluations.md#comparison-8cc2ab7b2dcd) | 帮我把这份读书会会议记录里的待办整理成在线任务表，给我链接，再告诉我还有哪些没完成、各自什么时候到期。 | codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 分钟 |
| [Grist / API](./generated/evaluations.md#comparison-ab4e4c0d9054) | 帮我把这份读书会会议记录里的待办整理成在线任务表，给我链接，再告诉我还有哪些没完成、各自什么时候到期。 | codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 分钟 |

**测试配置：** 2026-09-08 – 2026-10-08（UTC） · 已预供服务凭据

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义 1](./data/experiments/tasks/collaborative-tables-shared-expenses.md) · [任务定义 2](./data/experiments/tasks/collaborative-tables-v4.md) · [任务定义 3](./data/experiments/tasks/collaborative-tables.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-productivity-storage-project-management"></a>

#### 项目与任务管理 (4)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#atlassian">Atlassian (Jira &amp; Confluence)</a></td><td align="left">Jira, Confluence and the Atlassian Cloud platform — REST APIs, an official remote MCP server (OAuth 2.1), and the acli CLI.</td><td align="left"><a href="https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/">API</a> · <a href="https://developer.atlassian.com/cloud/acli/">CLI</a> · <a href="https://github.com/atlassian/atlassian-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#github">GitHub</a></td><td align="left">Code hosting, collaboration, and automation with REST and GraphQL APIs, an official CLI, and an official MCP server.</td><td align="left"><a href="https://docs.github.com/en/rest/quickstart">API</a> · <a href="https://github.com/octokit">SDK</a> · <a href="https://cli.github.com">CLI</a> · <a href="https://github.com/github/github-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#gitlab">GitLab</a></td><td align="left">DevOps platform with REST and GraphQL APIs, scoped tokens, llms.txt, and an official CLI.</td><td align="left"><a href="https://docs.gitlab.com/api/rest/">API</a> · <a href="https://gitlab.com/gitlab-org/cli">CLI</a> · <a href="https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#linear">Linear</a></td><td align="left">Issue tracking and product planning with a GraphQL API, llms.txt, an official MCP server, and webhooks.</td><td align="left"><a href="https://linear.app/docs/mcp">MCP</a></td></tr>
</tbody>
</table>

<a id="services-productivity-storage-document-collaboration"></a>

#### 文档协作 (4)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#atlassian">Atlassian (Jira &amp; Confluence)</a></td><td align="left">Jira, Confluence and the Atlassian Cloud platform — REST APIs, an official remote MCP server (OAuth 2.1), and the acli CLI.</td><td align="left"><a href="https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/">API</a> · <a href="https://developer.atlassian.com/cloud/acli/">CLI</a> · <a href="https://github.com/atlassian/atlassian-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#coda">Coda / Superhuman Docs</a></td><td align="left">Docs and tables with a free REST API; current API page is branded Superhuman Docs.</td><td align="left"><a href="https://coda.io/developers/apis/v1">API</a> · <a href="https://help.coda.io/hc/en-us/articles/44722661982989-Connect-to-the-Coda-MCP">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#lark">Lark</a></td><td align="left">Collaboration suite (messaging, docs, calendar) with an open platform, llms.txt, an official CLI with 200+ commands and agent skills, and an official OpenAPI MCP server.</td><td align="left"><a href="https://open.larksuite.com/document/server-docs/getting-started/server-api-list">API</a> · <a href="https://github.com/larksuite/cli">CLI</a> · <a href="https://github.com/larksuite/lark-openapi-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#notion">Notion</a></td><td align="left">Connected workspace with a versioned REST API, capability-scoped integrations, llms.txt, and an official MCP server.</td><td align="left"><a href="https://developers.notion.com/guides/get-started/internal-connections">API</a> · <a href="https://github.com/makenotion/notion-sdk-js">SDK</a> · <a href="https://developers.notion.com/cli/get-started/overview">CLI</a> · <a href="https://developers.notion.com/guides/mcp/get-started-with-mcp">MCP</a></td></tr>
</tbody>
</table>

<a id="services-productivity-storage-file-sharing"></a>

#### 文件共享 (1)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#dropbox">Dropbox</a></td><td align="left">File storage and sync with a scoped-OAuth HTTP API, self-serve app creation, and webhooks.</td><td align="left"><a href="https://www.dropbox.com/developers/documentation/http/documentation">API</a> · <a href="https://github.com/dropbox/dbxcli">CLI</a></td></tr>
</tbody>
</table>

<a id="services-ai-models"></a>

### AI 服务 (25)

<a id="services-ai-models-model-access"></a>

#### 模型接入 (21)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#agentservices">AgentServices</a></td><td align="left">Market data, web search and extraction, and model access through REST, MCP and a JavaScript SDK; selected free tools, x402 payments on REST, and a documented OAuth/prepaid-credit MCP path.</td><td align="left"><a href="https://github.com/vbkotecha/agentservices-api/blob/main/docs/buyer-quickstart.md">API</a> · <a href="https://github.com/vbkotecha/agentservices-api/blob/main/sdk/README.md">SDK</a> · <a href="https://github.com/vbkotecha/agentservices-api/blob/main/README.md#using-as-mcp-server-claude-desktop-cursor-etc">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#qwen">Alibaba Qwen (Model Studio)</a></td><td align="left">Qwen model family via Alibaba Cloud Model Studio's OpenAI-compatible API, with an official open-source coding CLI agent (qwen-code).</td><td align="left"><a href="https://www.alibabacloud.com/help/en/model-studio/models">API</a> · <a href="https://github.com/QwenLM/qwen-code">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#anthropic">Anthropic</a></td><td align="left">Claude model APIs with agent-focused documentation, llms.txt, and the company behind the MCP standard itself.</td><td align="left"><a href="https://docs.anthropic.com/en/api">API</a> · <a href="https://docs.anthropic.com/en/api/client-sdks">SDK</a> · <a href="https://docs.anthropic.com/en/docs/claude-code">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#cerebras">Cerebras Inference</a></td><td align="left">Wafer-scale inference for open models at very high tokens/sec, OpenAI-compatible API, llms.txt, and a standing free tier.</td><td align="left"><a href="https://inference-docs.cerebras.ai/api-reference/chat-completions">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#cohere">Cohere</a></td><td align="left">Enterprise LLM platform (command, embed, rerank) with llms.txt, documented API versioning, free trial keys, and error/rate-limit docs.</td><td align="left"><a href="https://docs.cohere.com/reference/about">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#deepseek">DeepSeek</a></td><td align="left">OpenAI-compatible LLM API (DeepSeek-V3/R1) with transparent per-token pricing, a detailed changelog, and self-serve keys.</td><td align="left"><a href="https://api-docs.deepseek.com">文档</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fal">fal.ai</a></td><td align="left">Generative media platform (image, video, audio models) with queue/streaming APIs, an official CLI/serving framework, llms.txt, and self-serve keys.</td><td align="left"><a href="https://fal.ai/docs/model-apis">API</a> · <a href="https://github.com/fal-ai/fal">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fireworks">Fireworks AI</a></td><td align="left">Fast open-model inference and fine-tuning with an OpenAI-compatible API, official firectl CLI, llms.txt, and published pricing.</td><td align="left"><a href="https://docs.fireworks.ai/api-reference/introduction">API</a> · <a href="https://docs.fireworks.ai/tools-sdks/firectl/firectl">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#gemini-api">Gemini API</a></td><td align="left">Google's Gemini model APIs via AI Studio, with generous free tier and documented API versioning.</td><td align="left"><a href="https://ai.google.dev/api">API</a> · <a href="https://ai.google.dev/gemini-api/docs/libraries">SDK</a> · <a href="https://github.com/google-gemini/gemini-cli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#groq">Groq</a></td><td align="left">Ultra-low-latency LLM inference with an OpenAI-compatible API, llms.txt, and self-serve keys with a free tier.</td><td align="left"><a href="https://console.groq.com/docs/api-reference">API</a> · <a href="https://console.groq.com/docs/libraries">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#hugging-face">Hugging Face</a></td><td align="left">Model hub and inference platform with fine-grained tokens, OAuth, an official MCP server, and a full Hub API.</td><td align="left"><a href="https://huggingface.co/docs/hub/api">API</a> · <a href="https://huggingface.co/docs/huggingface_hub">SDK</a> · <a href="https://huggingface.co/docs/huggingface_hub/guides/cli">CLI</a> · <a href="https://huggingface.co/docs/hub/agents-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#minimax">MiniMax</a></td><td align="left">MiniMax text, speech, video and music models via the international platform API, with an official MCP server.</td><td align="left"><a href="https://platform.minimax.io/docs/api-reference">API</a> · <a href="https://github.com/MiniMax-AI/MiniMax-MCP">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#mistral">Mistral AI</a></td><td align="left">European LLM provider (La Plateforme) with llms.txt, an open OpenAPI-based docs repo, a free experiment tier, and self-serve keys.</td><td align="left"><a href="https://docs.mistral.ai/api">API</a> · <a href="https://docs.mistral.ai/getting-started/clients">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#moonshot">Moonshot AI (Kimi)</a></td><td align="left">Kimi models (K2 line) via an OpenAI-compatible API on the international Kimi platform, with an official terminal CLI agent (kimi-cli).</td><td align="left"><a href="https://platform.kimi.ai/docs/api/chat">API</a> · <a href="https://github.com/MoonshotAI/kimi-cli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#openai">OpenAI</a></td><td align="left">GPT model APIs with an official OpenAPI spec, agents guides, and a large SDK ecosystem.</td><td align="left"><a href="https://platform.openai.com/docs/api-reference">API</a> · <a href="https://platform.openai.com/docs/libraries">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#openrouter">OpenRouter</a></td><td align="left">Unified OpenAI-compatible API over hundreds of models from many labs, with one key, per-model pricing, automatic fallbacks, and an llms.txt.</td><td align="left"><a href="https://openrouter.ai/docs/api-reference/overview">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#replicate">Replicate</a></td><td align="left">Run and fine-tune open-source models via a simple predictions API, with llms.txt, webhooks, and an official CLI.</td><td align="left"><a href="https://replicate.com/docs/reference/http">API</a> · <a href="https://replicate.com/docs/reference/client-libraries">SDK</a> · <a href="https://github.com/replicate/cli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#together-ai">Together AI</a></td><td align="left">Inference and fine-tuning platform for open-source models with an OpenAI-compatible API and llms.txt.</td><td align="left"><a href="https://docs.together.ai/reference/chat-completions">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#xai">xAI (Grok API)</a></td><td align="left">xAI's Grok models via an OpenAI-compatible REST API, with an llms.txt and self-serve console keys.</td><td align="left"><a href="https://docs.x.ai/developers/rest-api-reference/inference">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#xiurouter">XiuRouter</a></td><td align="left">Hosted model gateway with documented OpenAI, Anthropic and Gemini API protocols, scoped keys and request-level usage records.</td><td align="left"><a href="https://docs.xiu.ai/en/router/quickstart/">API</a> · <a href="https://docs.xiu.ai/router/integrations/vercel-ai-sdk/">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#zai">Z.ai (GLM)</a></td><td align="left">GLM models via Z.ai's OpenAI-compatible international API, with llms.txt, published pricing, and self-serve keys.</td><td align="left"><a href="https://docs.z.ai/api-reference">API</a></td></tr>
</tbody>
</table>

<a id="services-ai-models-speech-synthesis"></a>

#### 语音合成 (3)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#cartesia">Cartesia</a></td><td align="left">Low-latency voice models (Sonic TTS, Ink STT) with a documented API, official MCP server, llms.txt, and a free tier.</td><td align="left"><a href="https://docs.cartesia.ai/api-reference">API</a> · <a href="https://github.com/cartesia-ai/cartesia-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#deepgram">Deepgram</a></td><td align="left">Speech-to-text and voice AI API with a public OpenAPI spec, llms.txt, scoped API keys, and $200 free credit without a card.</td><td align="left"><a href="https://developers.deepgram.com/reference">API</a> · <a href="https://developers.deepgram.com/docs/deepgram-sdks">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#elevenlabs">ElevenLabs</a></td><td align="left">Voice AI (TTS, STT, agents) with a public OpenAPI spec, llms.txt, an official MCP server, and a free tier.</td><td align="left"><a href="https://elevenlabs.io/docs/api-reference/introduction">API</a> · <a href="https://github.com/elevenlabs/elevenlabs-mcp">MCP</a></td></tr>
</tbody>
</table>

<a id="services-ai-models-speech-recognition"></a>

#### 语音识别 (3)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#cartesia">Cartesia</a></td><td align="left">Low-latency voice models (Sonic TTS, Ink STT) with a documented API, official MCP server, llms.txt, and a free tier.</td><td align="left"><a href="https://docs.cartesia.ai/api-reference">API</a> · <a href="https://github.com/cartesia-ai/cartesia-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#deepgram">Deepgram</a></td><td align="left">Speech-to-text and voice AI API with a public OpenAPI spec, llms.txt, scoped API keys, and $200 free credit without a card.</td><td align="left"><a href="https://developers.deepgram.com/reference">API</a> · <a href="https://developers.deepgram.com/docs/deepgram-sdks">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#elevenlabs">ElevenLabs</a></td><td align="left">Voice AI (TTS, STT, agents) with a public OpenAPI spec, llms.txt, an official MCP server, and a free tier.</td><td align="left"><a href="https://elevenlabs.io/docs/api-reference/introduction">API</a> · <a href="https://github.com/elevenlabs/elevenlabs-mcp">MCP</a></td></tr>
</tbody>
</table>

<a id="services-ai-models-image-generation"></a>

#### 图像生成 (2)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#fal">fal.ai</a></td><td align="left">Generative media platform (image, video, audio models) with queue/streaming APIs, an official CLI/serving framework, llms.txt, and self-serve keys.</td><td align="left"><a href="https://fal.ai/docs/model-apis">API</a> · <a href="https://github.com/fal-ai/fal">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#luma">Luma AI (Dream Machine)</a></td><td align="left">Dream Machine video and image generation via the Luma API, with llms.txt and published API pricing.</td><td align="left"><a href="https://docs.lumalabs.ai/reference">API</a></td></tr>
</tbody>
</table>

<a id="services-ai-models-video-generation"></a>

#### 视频生成 (2)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#fal">fal.ai</a></td><td align="left">Generative media platform (image, video, audio models) with queue/streaming APIs, an official CLI/serving framework, llms.txt, and self-serve keys.</td><td align="left"><a href="https://fal.ai/docs/model-apis">API</a> · <a href="https://github.com/fal-ai/fal">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#luma">Luma AI (Dream Machine)</a></td><td align="left">Dream Machine video and image generation via the Luma API, with llms.txt and published API pricing.</td><td align="left"><a href="https://docs.lumalabs.ai/reference">API</a></td></tr>
</tbody>
</table>

<a id="services-agent-tooling"></a>

### Agent 基础设施与自动化 (5)

以下服务暂按本层范围收录，细分缺口见服务详情。

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#cog-depot">Cog Depot</a></td><td align="left">Hosted marketplace for agents to discover counterparties, negotiate capability exchanges and obtain direct contact details after paying platform fees.</td><td align="left"><a href="https://cogdepot.com/docs">API</a> · <a href="https://github.com/cogdepot/mcp-server#install">MCP</a></td></tr>
</tbody>
</table>

<a id="services-agent-tooling-memory"></a>

#### Agent 记忆 (1)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#mem0">Mem0</a></td><td align="left">Memory layer for AI agents (hosted platform + open-source), with REST API, llms.txt, and the official OpenMemory MCP server.</td><td align="left"><a href="https://docs.mem0.ai/api-reference">API</a> · <a href="https://docs.mem0.ai/openmemory/overview">MCP</a></td></tr>
</tbody>
</table>

<a id="services-agent-tooling-tool-integrations"></a>

#### 工具连接 (2)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#composio">Composio</a></td><td align="left">Tool and integration layer for AI agents (hundreds of app connectors with managed auth), with llms.txt and a hosted MCP directory.</td><td align="left"><a href="https://docs.composio.dev/docs/composio-connect">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#zapier">Zapier</a></td><td align="left">Automation platform bridging 7000+ apps, with llms.txt and an official MCP endpoint that gives agents access to those integrations.</td><td align="left"><a href="https://github.com/zapier/zapier-platform">CLI</a> · <a href="https://docs.zapier.com/mcp/get-started/quickstart">MCP</a></td></tr>
</tbody>
</table>

<a id="services-agent-tooling-workflow-automation"></a>

#### 工作流自动化 (2)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#n8n">n8n</a></td><td align="left">Workflow automation platform with native AI/agent nodes, a public REST API, official hosted MCP server, CLI, and llms.txt; fair-code and self-hostable.</td><td align="left"><a href="https://docs.n8n.io/api/">API</a> · <a href="https://docs.n8n.io/hosting/cli-commands/">CLI</a> · <a href="https://docs.n8n.io/connect/connect-to-n8n-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#zapier">Zapier</a></td><td align="left">Automation platform bridging 7000+ apps, with llms.txt and an official MCP endpoint that gives agents access to those integrations.</td><td align="left"><a href="https://github.com/zapier/zapier-platform">CLI</a> · <a href="https://docs.zapier.com/mcp/get-started/quickstart">MCP</a></td></tr>
</tbody>
</table>

<a id="services-developer-tools"></a>

### 开发工具 (8)

<a id="services-developer-tools-dependency-advisories"></a>

#### 依赖漏洞公告 (2)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#github">GitHub</a></td><td align="right"><a href="./generated/evaluations.md#comparison-7a5fd0fd8e1a">100%</a></td><td align="right">185.8k</td><td align="right">$0.01</td><td align="right">—</td><td align="left"><a href="https://api.github.com/advisories">API</a></td><td align="left"><a href="https://docs.github.com/en/rest/quickstart">API</a> · <a href="https://github.com/octokit">SDK</a> · <a href="https://cli.github.com">CLI</a> · <a href="https://github.com/github/github-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#osv">OSV.dev</a></td><td align="right"><a href="./generated/evaluations.md#comparison-7a5fd0fd8e1a">100%</a></td><td align="right">178.5k</td><td align="right">$0.01</td><td align="right">—</td><td align="left"><a href="https://api.osv.dev/v1/query">API</a></td><td align="left"><a href="https://google.github.io/osv.dev/quickstart/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：帮我接通这个依赖漏洞公告服务，通过指定方式做一次真实查询，确认能取得可识别的公告记录，并保存后续查询需要的本地配置；说明接入步骤和实际阻碍。**

服务、指定入口及本轮允许使用的身份或凭据见 ENVIRONMENT.md。自行选择一个小型公开公告查询，报告实际取得的公告标识、关联包名和来源。无需账号的入口直接使用；需要注册或授权时仅使用本轮提供的资料。必要配置保存在本轮持久目录，秘密只存私有文件；答复给出配置位置、已有账号来源、自助步骤及实际人工或申请要求。

完成标准：按指定方式完成必要安装、认证和配置，实际响应含可识别的公告及关联包，答复与响应一致；配置可供新会话复用且不泄露秘密。无需账号不强行注册，已有账号不冒充本轮自助注册。

**测试配置：** 1.18.35 · deepseek-flash / high · 5 分钟 · 2026-10-08（UTC） · 接入准备: none; anonymous public advisory API, no account/email/token/payment supplied

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/dependency-advisories.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#github">GitHub</a></td><td align="right"><a href="./generated/evaluations.md#comparison-644e634b8512">100%</a></td><td align="right">75.8k</td><td align="right">$0.0076</td><td align="right">$0</td><td align="left"><a href="https://api.github.com/advisories">API</a></td><td align="left"><a href="https://docs.github.com/en/rest/quickstart">API</a> · <a href="https://github.com/octokit">SDK</a> · <a href="https://cli.github.com">CLI</a> · <a href="https://github.com/github/github-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#osv">OSV.dev</a></td><td align="right"><a href="./generated/evaluations.md#comparison-644e634b8512">100%</a></td><td align="right">201.0k</td><td align="right">$0.02</td><td align="right">$0</td><td align="left"><a href="https://api.osv.dev/v1/query">API</a></td><td align="left"><a href="https://google.github.io/osv.dev/quickstart/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：我在整理项目的两条依赖安全告警。请用指定服务逐条核对当前版本是否仍在公告的受影响版本范围内，给出 5.2.x 分支中各自最早的修复版本；告诉我仅处理这两条至少需要升级到哪个版本，并附上可核对的依据链接。**

依赖笔记：生态 PyPI，包 Django，当前版本 5.2.6；待核对告警 CVE-2025-57833、CVE-2025-59681。只核对这两条的包版本匹配和修复边界，不要求列出所有漏洞或选择当前最新版本，也不判断本项目的代码、数据库配置或漏洞可利用性。用中文简要说明判断及查询来源。可以沿本次指定服务记录中的引用链接核对维护者公告或发布记录；不要用其他漏洞库、通用网页搜索或模型记忆代替指定服务查询。没有查到记录时说明未知，不据此断言没有影响。不安装、升级或修改项目。

完成标准：真实查询指定服务，答复逐条正确判断给定包版本是否匹配两条告警，修复版本属于所要求的 5.2.x 分支，最低升级边界正确；结论与实际服务记录或从记录可追溯的维护者引用链相符，并由事前独立取得的维护者发布参考核对。来源链接能支持对应判断，不将未命中当作不受影响，不把本题结论扩大为全部漏洞已修复或应用不可利用。

**测试配置：** 1.18.35 · deepseek-flash / high · 10 分钟 · 独立验收可参考同期 2 份同题答案 · 2026-10-08（UTC） · 接入准备: none; anonymous public advisory API, no account/email/token/payment supplied

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/dependency-advisories.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-developer-tools-monitoring"></a>

#### 监控与故障排查 (3)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#datadog">Datadog</a></td><td align="left">Observability platform with a full REST API, llms.txt, documented OAuth for integrations, rate limits, and webhooks.</td><td align="left"><a href="https://docs.datadoghq.com/api/latest/">API</a> · <a href="https://github.com/DataDog/datadog-ci">CLI</a> · <a href="https://docs.datadoghq.com/bits_ai/mcp_server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#grafana">Grafana (Grafana Cloud)</a></td><td align="left">Observability platform (dashboards, metrics, logs, traces) with a documented HTTP API, official MCP server, llms.txt, and a standing free cloud tier.</td><td align="left"><a href="https://grafana.com/docs/grafana/latest/developers/http_api/">API</a> · <a href="https://github.com/grafana/mcp-grafana">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#sentry">Sentry</a></td><td align="left">Error monitoring and performance tracing with llms.txt, an official MCP server, scoped auth tokens, and a full API.</td><td align="left"><a href="https://docs.sentry.io/api/">API</a> · <a href="https://docs.sentry.io/platforms/">SDK</a> · <a href="https://docs.sentry.io/cli/">CLI</a> · <a href="https://docs.sentry.io/product/sentry-mcp/">MCP</a></td></tr>
</tbody>
</table>

<a id="services-developer-tools-code-hosting"></a>

#### 代码托管与评审 (3)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#atlassian">Atlassian (Jira &amp; Confluence)</a></td><td align="left">Jira, Confluence and the Atlassian Cloud platform — REST APIs, an official remote MCP server (OAuth 2.1), and the acli CLI.</td><td align="left"><a href="https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/">API</a> · <a href="https://developer.atlassian.com/cloud/acli/">CLI</a> · <a href="https://github.com/atlassian/atlassian-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#github">GitHub</a></td><td align="left">Code hosting, collaboration, and automation with REST and GraphQL APIs, an official CLI, and an official MCP server.</td><td align="left"><a href="https://docs.github.com/en/rest/quickstart">API</a> · <a href="https://github.com/octokit">SDK</a> · <a href="https://cli.github.com">CLI</a> · <a href="https://github.com/github/github-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#gitlab">GitLab</a></td><td align="left">DevOps platform with REST and GraphQL APIs, scoped tokens, llms.txt, and an official CLI.</td><td align="left"><a href="https://docs.gitlab.com/api/rest/">API</a> · <a href="https://gitlab.com/gitlab-org/cli">CLI</a> · <a href="https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server">MCP</a></td></tr>
</tbody>
</table>

<a id="services-developer-tools-api-development"></a>

#### API 开发与测试 (1)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#postman">Postman</a></td><td align="left">API development platform with a public Postman API, llms.txt, official CLI, and self-serve keys.</td><td align="left"><a href="https://learning.postman.com/docs/developer/postman-api/intro-api/">API</a> · <a href="https://learning.postman.com/docs/postman-cli/postman-cli-overview/">CLI</a> · <a href="https://github.com/postmanlabs/postman-mcp-server">MCP</a></td></tr>
</tbody>
</table>

<a id="services-cloud-hosting"></a>

### 云计算与托管 (11)

<a id="services-cloud-hosting-code-sandboxes"></a>

#### 代码沙箱 (3)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#daytona">Daytona</a></td><td align="left">Hosted sandboxes with SDK, CLI and API access for code execution and file transfer.</td><td align="left"><a href="https://www.daytona.io/docs/en/">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#e2b">E2B</a></td><td align="left">Isolated cloud sandboxes for running AI-generated code, with llms.txt, an official MCP server, and self-serve keys.</td><td align="left"><a href="https://docs.e2b.dev/quickstart">SDK</a> · <a href="https://e2b.dev/docs/cli">CLI</a> · <a href="https://github.com/e2b-dev/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#modal">Modal</a></td><td align="left">Serverless compute for Python with first-class Sandboxes for agent code execution, llms.txt, and an official CLI.</td><td align="left"><a href="https://modal.com/docs/reference">API</a> · <a href="https://modal.com/docs/guide/sandboxes">SDK</a> · <a href="https://modal.com/docs/reference/cli">CLI</a></td></tr>
</tbody>
</table>

<a id="services-cloud-hosting-browser-environments"></a>

#### 浏览器运行环境 (2)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#browserbase">Browserbase</a></td><td align="left">Headless browser infrastructure for AI agents and automation, with session APIs and an official MCP server.</td><td align="left"><a href="https://docs.browserbase.com/reference">API / SDK</a> · <a href="https://github.com/browserbase/mcp-server-browserbase">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#steel">Steel</a></td><td align="left">Cloud browser API for AI agents (sessions, CDP, anti-bot) — open-source and self-hostable, with llms.txt and a free tier.</td><td align="left"><a href="https://docs.steel.dev/api-reference">API</a></td></tr>
</tbody>
</table>

<a id="services-cloud-hosting-app-hosting"></a>

#### 应用部署 (6)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#cloudflare">Cloudflare</a></td><td align="left">Edge network, Workers serverless platform, storage, and AI services with agent-focused docs and official MCP servers.</td><td align="left"><a href="https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/get/">API</a> · <a href="https://developers.cloudflare.com/api/typescript/resources/kv/subresources/namespaces/subresources/values/methods/get/">SDK</a> · <a href="https://developers.cloudflare.com/d1/get-started/">CLI</a> · <a href="https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fly-io">Fly.io</a></td><td align="left">Run full-stack apps and machines close to users, with a spec'd Machines API, scoped macaroon tokens, and official MCP docs.</td><td align="left"><a href="https://fly.io/docs/machines/api/">API</a> · <a href="https://fly.io/docs/flyctl/">CLI</a> · <a href="https://fly.io/docs/mcp/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#netlify">Netlify</a></td><td align="left">Web platform for deploying sites and functions, with an OpenAPI-specified API, llms.txt, official CLI and MCP server.</td><td align="left"><a href="https://open-api.netlify.com">API</a> · <a href="https://docs.netlify.com/cli/get-started/">CLI</a> · <a href="https://docs.netlify.com/welcome/build-with-ai/netlify-mcp-server/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#railway">Railway</a></td><td align="left">App/database hosting with a public GraphQL API, official CLI, llms.txt, and usage-based pricing.</td><td align="left"><a href="https://docs.railway.com/reference/public-api">API</a> · <a href="https://github.com/railwayapp/cli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#render">Render</a></td><td align="left">Cloud hosting for web services, static sites and databases with a REST API, official CLI, official MCP server, and llms.txt.</td><td align="left"><a href="https://api-docs.render.com/reference/introduction">API</a> · <a href="https://github.com/render-oss/cli">CLI</a> · <a href="https://github.com/render-oss/render-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#vercel">Vercel</a></td><td align="left">Frontend cloud for deploying web apps, with a REST API, CLI, official MCP server, and AI SDK ecosystem.</td><td align="left"><a href="https://vercel.com/docs/rest-api">API</a> · <a href="https://vercel.com/docs/rest-api/sdk">SDK</a> · <a href="https://vercel.com/docs/cli">CLI</a> · <a href="https://vercel.com/docs/mcp/vercel-mcp">MCP</a></td></tr>
</tbody>
</table>

<a id="services-payments-billing"></a>

### 支付与计费 (19)

<a id="services-payments-billing-accept-payments"></a>

#### 收款 (19)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#paas-build">paas.build</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left"><a href="https://paas.build/openapi.json">API</a></td><td align="left"><a href="https://paas.build/SKILL.md">API</a> · <a href="https://paas.build/agents">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#paddle">Paddle</a></td><td align="right"><a href="./generated/evaluations.md#comparison-3a57cb066008">0%</a></td><td align="right">455.2k</td><td align="right">$1.20</td><td align="right">$0</td><td align="left"><a href="https://developer.paddle.com/sdks/sandbox/">API</a></td><td align="left"><a href="https://developer.paddle.com/api-reference/overview">API</a> · <a href="https://github.com/PaddleHQ/paddle-mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#adyen">Adyen</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.adyen.com/api-explorer/Checkout/latest/post/paymentLinks">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#airwallex">Airwallex</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.airwallex.com/docs/api/payments/payment_links/api">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#alipay">Alipay</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left">—</td></tr>
<tr><td align="left"><a href="./generated/services.md#checkout-com">Checkout.com</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://api-reference.checkout.com/tag/Payment-Links/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#creem">Creem</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.creem.io/getting-started/test-mode">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#dodo-payments">Dodo Payments</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.dodopayments.com/introduction">API</a> · <a href="https://github.com/dodopayments/dodopayments-cli">CLI</a> · <a href="https://docs.dodopayments.com/developer-resources/mcp-server">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fastspring">FastSpring</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://developer.fastspring.com/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#lemonsqueezy">Lemon Squeezy</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.lemonsqueezy.com/guides/developer-guide/taking-payments">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#mollie">Mollie</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.mollie.com/reference/create-payment-link">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#paypal">PayPal</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://developer.paypal.com/api/rest">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#pingxx">Ping++</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.pingxx.com/api/%E8%AE%A4%E8%AF%81.html">API</a> · <a href="https://www.pingxx.com/docs/client/web.html">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#polar">Polar</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://polar.sh/docs/integrate/sandbox">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#razorpay">Razorpay</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://razorpay.com/docs/api/payments/payment-links/create-standard/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#square">Square</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://developer.squareup.com/reference/square/checkout-api/CreatePaymentLink">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#stripe">Stripe</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.stripe.com/payment-links/create">API</a> · <a href="https://docs.stripe.com/sdks">SDK</a> · <a href="https://docs.stripe.com/stripe-cli">CLI</a> · <a href="https://docs.stripe.com/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#wechat-pay">WeChat Pay</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://pay.wechatpay.cn/doc/v3/merchant/4012791877">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#whop">Whop</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.whop.com/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：我要卖一份电子书《城市散步指南》，标价12美元，一次性付款。先在测试环境做好收款页面，把顾客能打开的链接给我。**

商品为电子书《城市散步指南》，标价12 USD，一次性收费，数量1；不需要交付电子书文件

完成标准：评测 Agent 独立读取远端商品/订单/结账资源，并打开返回链接；确认名称、标价12 USD、数量1和一次性收费一致，页面可继续进入测试付款流程。动态税费如存在单独显示；不要求支付成功

**测试配置：** codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 分钟 · 2026-09-08 – 2026-09-09（UTC） · 已预供服务凭据

[任务定义](./data/experiments/tasks/payment-acceptance.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-communication"></a>

### 通信 (23)

<a id="services-communication-mailboxes"></a>

#### 邮箱 (13)

<details>
<summary>接入测试（单独记录）</summary>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#agentmail">AgentMail</a></td><td align="right"><a href="./generated/evaluations.md#comparison-183e17ccb640">0%</a></td><td align="right">783.4k</td><td align="right">$0.03</td><td align="right">—</td><td align="left"><a href="https://api.agentmail.to/v0/">API</a></td><td align="left"><a href="https://docs.agentmail.to/agent-onboarding">API</a> · <a href="https://docs.agentmail.to/quickstart">SDK</a> · <a href="https://docs.agentmail.to/integrations/cli">CLI</a> · <a href="https://docs.agentmail.to/integrations/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#mail-tm">Mail.tm</a></td><td align="right"><a href="./generated/evaluations.md#comparison-183e17ccb640">100%</a></td><td align="right">116.2k</td><td align="right">$0.0070</td><td align="right">$0</td><td align="left"><a href="https://api.mail.tm">API</a></td><td align="left"><a href="https://docs.mail.tm/">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：为这次自动化测试准备一个临时收件邮箱，给我地址，并保存后续读取收件箱需要的访问信息。**

使用服务提供的域名，新建一个仅供本次测试使用的收件邮箱，不复用既有邮箱。只需本次测试期间使用，不要求长期保留或自定义域名。可以为此建立服务必需的最小免费匿名身份及认证信息，不使用现有服务账号或任何人类邮箱完成验证；需要这些条件时说明阻碍。确认能够读取该邮箱的收件箱列表，说明当前是否有邮件。将密码、令牌或会话信息保存在本地私有文件中，答复只给文件位置，不输出秘密。

完成标准：指定服务返回实际邮箱地址；真实收件箱读取成功；已保存的访问状态可由评测者在独立请求中复用到同一邮箱；答复与实际状态相符，秘密不出现在答复中。

**测试配置：** 1.18.35 · deepseek-flash / high · 5 分钟 · 2026-10-08（UTC） · 接入准备: none initially; one fresh anonymous mailbox and necessary identity created inside measured execution

部分记录未公开主机信息或启动器哈希；具体环境与限制见完整记录。

[任务定义](./data/experiments/tasks/mailboxes-v2.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

</details>

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="12%" align="right">完成率</th><th width="11%" align="right">Token</th><th width="11%" align="right">模型费用</th><th width="11%" align="right">服务费用</th><th width="9%" align="left">测试方式</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#guerrilla-mail">Guerrilla Mail</a></td><td align="right"><a href="./generated/evaluations.md#comparison-e42af771b245">0%</a></td><td align="right">85.3k</td><td align="right">$0.28</td><td align="right">$0</td><td align="left"><a href="https://www.guerrillamail.com/GuerrillaMailAPI.html">API</a></td><td align="left"><a href="https://www.guerrillamail.com/GuerrillaMailAPI.html">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#mail-tm">Mail.tm</a></td><td align="right"><a href="./generated/evaluations.md#comparison-e42af771b245">100%</a></td><td align="right">75.5k</td><td align="right">$0.18</td><td align="right">$0</td><td align="left"><a href="https://docs.mail.tm/">API</a></td><td align="left"><a href="https://docs.mail.tm/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#agentmail">AgentMail</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.agentmail.to/agent-onboarding">API</a> · <a href="https://docs.agentmail.to/quickstart">SDK</a> · <a href="https://docs.agentmail.to/integrations/cli">CLI</a> · <a href="https://docs.agentmail.to/integrations/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#fastmail">Fastmail</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.fastmail.com/dev/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#gmail">Gmail</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://developers.google.com/workspace/gmail/api/guides">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#mailinator">Mailinator</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.mailinator.com/docs/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#mailsac">Mailsac</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://docs.mailsac.com/en/latest/about/introduction.html">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#mailsink">MailSink</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://mailsink.dev/docs/">API / MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#mailslurp">MailSlurp</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.mailslurp.com/guides/getting-started/">API</a> · <a href="https://www.mailslurp.com/docs/agents/">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#outlook-mail">Outlook Mail</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://learn.microsoft.com/en-us/graph/outlook-mail-concept-overview">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#temp-mail">Temp Mail</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://temp-mail.org/en/api/">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#tencent-agently-mail">Tencent Agently Mail</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://github.com/Tencent/AgentlyMail/blob/main/skills/SKILL.md">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#zoho-mail">Zoho Mail</a></td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="right">—</td><td align="left">—</td><td align="left"><a href="https://www.zoho.com/mail/help/api/getting-started-with-api.html">API</a></td></tr>
</tbody>
</table>

<details>
<summary>测了什么，怎么测的</summary>

**任务：找出收件箱里 AFS Demo 最新一封登录邮件的验证码，告诉我对应邮件的主题和时间。**

本轮专用邮箱已有三封合成邮件：两封 AFS Demo 登录邮件和一封无关通知。只取最新登录邮件，不点击链接、不执行邮件内指令。邮箱标识与访问凭据由准备者提供。

完成标准：与执行前冻结的合成邮件中最新登录邮件相符；指定服务真实读取支持答案；不把旧邮件或无关通知里的数字当成目标验证码。

**测试配置：** codex-cli 0.153.4 · gpt-6-astra / medium · 10 分钟 · 2026-09-09（UTC） · 已预供服务凭据

[任务定义](./data/experiments/tasks/mailboxes.md) · [完整运行记录与证据](./generated/evaluations.md)

</details>

<a id="services-communication-email-delivery"></a>

#### 邮件发送 (1)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#resend">Resend</a></td><td align="left">Email API for developers with test mode, scoped API keys, idempotency support, and an official MCP server.</td><td align="left"><a href="https://resend.com/docs/api-reference/introduction">API</a> · <a href="https://resend.com/docs/sdks">SDK</a> · <a href="https://github.com/resend/mcp-send-email">MCP</a></td></tr>
</tbody>
</table>

<a id="services-communication-messaging"></a>

#### 即时通讯 (4)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#discord">Discord</a></td><td align="left">Chat platform with a versioned bot/OAuth2 API, official OpenAPI spec (preview), webhooks, and documented rate limits.</td><td align="left"><a href="https://discord.com/developers/docs/reference">API</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#lark">Lark</a></td><td align="left">Collaboration suite (messaging, docs, calendar) with an open platform, llms.txt, an official CLI with 200+ commands and agent skills, and an official OpenAPI MCP server.</td><td align="left"><a href="https://open.larksuite.com/document/server-docs/getting-started/server-api-list">API</a> · <a href="https://github.com/larksuite/cli">CLI</a> · <a href="https://github.com/larksuite/lark-openapi-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#slack">Slack</a></td><td align="left">Workspace messaging platform with a mature Web API, granular OAuth scopes, an OpenAPI spec, and llms.txt.</td><td align="left"><a href="https://api.slack.com/methods">API</a> · <a href="https://tools.slack.dev">SDK</a> · <a href="https://docs.slack.dev/tools/slack-cli">CLI</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#telegram">Telegram Bot API</a></td><td align="left">Free bot platform with instant token issuance via BotFather, webhooks, a documented test environment, and a detailed changelog.</td><td align="left"><a href="https://core.telegram.org/bots/api">API</a></td></tr>
</tbody>
</table>

<a id="services-communication-sms"></a>

#### 短信发送 (1)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#twilio">Twilio</a></td><td align="left">Programmable messaging and voice APIs with test credentials, an OpenAPI spec, llms.txt, and an official CLI.</td><td align="left"><a href="https://www.twilio.com/docs/usage/api">API</a> · <a href="https://www.twilio.com/docs/libraries">SDK</a> · <a href="https://www.twilio.com/docs/twilio-cli">CLI</a> · <a href="https://github.com/twilio-labs/mcp">MCP</a></td></tr>
</tbody>
</table>

<a id="services-communication-voice-calls"></a>

#### 语音通话 (2)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#twilio">Twilio</a></td><td align="left">Programmable messaging and voice APIs with test credentials, an OpenAPI spec, llms.txt, and an official CLI.</td><td align="left"><a href="https://www.twilio.com/docs/usage/api">API</a> · <a href="https://www.twilio.com/docs/libraries">SDK</a> · <a href="https://www.twilio.com/docs/twilio-cli">CLI</a> · <a href="https://github.com/twilio-labs/mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#vapi">Vapi</a></td><td align="left">Voice-agent orchestration API (calls, turn-taking, tool use over phone/web) with an official MCP server and an llms.txt that opens with instructions for AI agents.</td><td align="left"><a href="https://docs.vapi.ai/api-reference">API</a> · <a href="https://github.com/VapiAI/mcp-server">MCP</a></td></tr>
</tbody>
</table>

<a id="services-communication-voice-agents"></a>

#### 语音 Agent (4)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#cartesia">Cartesia</a></td><td align="left">Low-latency voice models (Sonic TTS, Ink STT) with a documented API, official MCP server, llms.txt, and a free tier.</td><td align="left"><a href="https://docs.cartesia.ai/api-reference">API</a> · <a href="https://github.com/cartesia-ai/cartesia-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#deepgram">Deepgram</a></td><td align="left">Speech-to-text and voice AI API with a public OpenAPI spec, llms.txt, scoped API keys, and $200 free credit without a card.</td><td align="left"><a href="https://developers.deepgram.com/reference">API</a> · <a href="https://developers.deepgram.com/docs/deepgram-sdks">SDK</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#elevenlabs">ElevenLabs</a></td><td align="left">Voice AI (TTS, STT, agents) with a public OpenAPI spec, llms.txt, an official MCP server, and a free tier.</td><td align="left"><a href="https://elevenlabs.io/docs/api-reference/introduction">API</a> · <a href="https://github.com/elevenlabs/elevenlabs-mcp">MCP</a></td></tr>
<tr><td align="left"><a href="./generated/services.md#vapi">Vapi</a></td><td align="left">Voice-agent orchestration API (calls, turn-taking, tool use over phone/web) with an official MCP server and an llms.txt that opens with instructions for AI agents.</td><td align="left"><a href="https://docs.vapi.ai/api-reference">API</a> · <a href="https://github.com/VapiAI/mcp-server">MCP</a></td></tr>
</tbody>
</table>

<a id="services-commerce-marketing"></a>

### 电商 (1)

<table width="100%">
<thead><tr><th width="26%" align="left">服务</th><th width="54%" align="left">用途</th><th width="20%" align="left">接入资料</th></tr></thead>
<tbody>
<tr><td align="left"><a href="./generated/services.md#shopify">Shopify</a></td><td align="left">Commerce platform with versioned GraphQL APIs, llms.txt, official MCP docs, access-scoped tokens, free development stores, and a CLI.</td><td align="left"><a href="https://shopify.dev/docs/api">API</a> · <a href="https://shopify.dev/docs/api/shopify-cli">CLI</a> · <a href="https://shopify.dev/docs/apps/build/storefront-mcp">MCP</a></td></tr>
</tbody>
</table>

## 给 Agent 的入口

[查询指引](./llms.txt) · [服务 JSON](./generated/catalog.json) · [实测 JSON](./generated/evaluations.json) · [MCP 配置](./mcp/README.md)

通过 `search_services` 查找候选，再用 `get_service` 查看接入条件和实测依据。同一份数据也可以直接读取 JSON。

## 方法与贡献

如果你知道我们漏掉的服务、有想测的真实任务，或发现资料已经过时，欢迎提供线索或纠错。

[核心理念](./AGENTS.md) · [收录标准](./docs/catalog-standard.zh-CN.md) · [机票阶段结论](./docs/flights.zh-CN.md) · [任务设计](./data/experiments/tasks/AGENTS.md) · [执行与验收](./data/experiments/AGENTS.md) · [全部实测与证据](./generated/evaluations.md) · [参与贡献](./docs/contributing.md) · [提出问题](https://github.com/Olorinm/agent-friendly-services/issues)

代码：[MIT](./LICENSE) · 数据：[CC BY 4.0](./LICENSE-DATA)。
