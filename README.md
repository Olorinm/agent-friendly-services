<!-- GENERATED — edit scripts/generate.ts; run npm run generate. -->

# Agent-Friendly Services

English | [简体中文](./README.zh-CN.md)

**Find services that let your Agent complete tasks, and use real tests to compare reliability, setup effort and cost.**

Finding a service is only the start. Before your Agent can use it, you may need to read the docs, create an account and work out whether the available API actually does what you need. We collect the options and test them on real tasks, so you and your Agent have less of that work to repeat. We focus on what an ordinary personal user can access, including the hurdles along the way.

## Browse the services

Pick a category below to see its candidates, the tasks we designed and the results we recorded.

| Category / subcategory | Candidates | Task definitions | Recorded runs | Services with runs |
| --- | ---: | --- | ---: | --- |
| Databases / Hosted Relational Databases | [6](./generated/catalog.md#databases-hosted-relational) | [Tasks](./data/experiments/tasks/databases.md) | [2](./generated/evaluations.md#databases-hosted-relational) | Neon, Turso |
| Productivity / Storage / Collaborative Tables | [8](./generated/catalog.md#productivity-storage-collaborative-tables) | [Tasks](./data/experiments/tasks/collaborative-tables.md) | [4](./generated/evaluations.md#productivity-storage-collaborative-tables) | Grist, Notion |
| Travel / Flights | [26](./generated/catalog.md#travel-flights) | [Tasks](./data/experiments/tasks/travel-flights.md) | [4](./generated/evaluations.md#travel-flights) | Ignav Flights, Kiwi.com |
| Web Search / Data / Web Search | [6](./generated/catalog.md#web-search-data-web-search) | [Tasks](./data/experiments/tasks/web-search.md) | [3](./generated/evaluations.md#web-search-data-web-search) | Exa, Firecrawl |

[Full service list](#all-services) · [All candidates and access routes](./generated/catalog.md) · [All task results and evidence](./generated/evaluations.md) · [Legacy provider index (76)](./generated/providers.md)

Open a result to see what the Agent accomplished, what it needed, and the tokens, time and service charges involved. Each run includes its task, model, date and supporting evidence so you can judge how closely it matches your situation.

This is a growing collection. Untested services and access restrictions stay visible, and run counts include earlier task versions and unsuccessful attempts. A successful run is useful evidence; it takes more comparable runs to recommend a service with confidence.

## Let your Agent use the directory

You can give your Agent the query guide below and ask it to find options for your task, check the access requirements and explain its choice using the available evidence.

[Query guide](./llms.txt) · [Catalog JSON](./generated/catalog.json) · [Results JSON](./generated/evaluations.json) · [MCP setup](./mcp/README.md)

Use `search_services` to filter by category/subcategory and access route, then `get_service` to inspect eligibility, costs and task evidence. Without MCP:

```sh
curl -s https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/catalog.json
```

<a id="all-services"></a>

## All services (112)

Usage and costs are means per valid trial, including successes and failures. Model costs are estimates from saved LiteLLM prices; service charges retain their evidence basis (~ marks estimates). — means unknown or untested. Compare only identical task versions, repeat counts and settings; expand for setup and history.

[AI Models](#services-ai-models) · [Agent Tooling](#services-agent-tooling) · [Code Execution](#services-code-execution) · [Developer Tools](#services-developer-tools) · [Cloud / Hosting](#services-cloud-hosting) · [Databases](#services-databases) · [Web Search / Data](#services-web-search-data) · [Payments / Billing](#services-payments-billing) · [Communication](#services-communication) · [Productivity / Storage](#services-productivity-storage) · [Observability / Security](#services-observability-security) · [Commerce / Marketing](#services-commerce-marketing) · [Travel](#services-travel)

<a id="services-ai-models"></a>

### AI Models (23)

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Alibaba Qwen (Model Studio)](./generated/providers.md#qwen) | Not yet task-tested | — | — | — |
| [Anthropic](./generated/providers.md#anthropic) | Not yet task-tested | — | — | — |
| [Cartesia](./generated/providers.md#cartesia) | Not yet task-tested | — | — | — |
| [Cerebras Inference](./generated/providers.md#cerebras) | Not yet task-tested | — | — | — |
| [Cohere](./generated/providers.md#cohere) | Not yet task-tested | — | — | — |
| [Deepgram](./generated/providers.md#deepgram) | Not yet task-tested | — | — | — |
| [DeepSeek](./generated/providers.md#deepseek) | Not yet task-tested | — | — | — |
| [ElevenLabs](./generated/providers.md#elevenlabs) | Not yet task-tested | — | — | — |
| [fal.ai](./generated/providers.md#fal) | Not yet task-tested | — | — | — |
| [Fireworks AI](./generated/providers.md#fireworks) | Not yet task-tested | — | — | — |
| [Gemini API](./generated/providers.md#gemini-api) | Not yet task-tested | — | — | — |
| [Groq](./generated/providers.md#groq) | Not yet task-tested | — | — | — |
| [Hugging Face](./generated/providers.md#hugging-face) | Not yet task-tested | — | — | — |
| [Luma AI (Dream Machine)](./generated/providers.md#luma) | Not yet task-tested | — | — | — |
| [MiniMax](./generated/providers.md#minimax) | Not yet task-tested | — | — | — |
| [Mistral AI](./generated/providers.md#mistral) | Not yet task-tested | — | — | — |
| [Moonshot AI (Kimi)](./generated/providers.md#moonshot) | Not yet task-tested | — | — | — |
| [OpenAI](./generated/providers.md#openai) | Not yet task-tested | — | — | — |
| [OpenRouter](./generated/providers.md#openrouter) | Not yet task-tested | — | — | — |
| [Replicate](./generated/providers.md#replicate) | Not yet task-tested | — | — | — |
| [Together AI](./generated/providers.md#together-ai) | Not yet task-tested | — | — | — |
| [xAI (Grok API)](./generated/providers.md#xai) | Not yet task-tested | — | — | — |
| [Z.ai (GLM)](./generated/providers.md#zai) | Not yet task-tested | — | — | — |

<a id="services-agent-tooling"></a>

### Agent Tooling (5)

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Composio](./generated/providers.md#composio) | Not yet task-tested | — | — | — |
| [Mem0](./generated/providers.md#mem0) | Not yet task-tested | — | — | — |
| [n8n](./generated/providers.md#n8n) | Not yet task-tested | — | — | — |
| [Vapi](./generated/providers.md#vapi) | Not yet task-tested | — | — | — |
| [Zapier](./generated/providers.md#zapier) | Not yet task-tested | — | — | — |

<a id="services-code-execution"></a>

### Code Execution (4)

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Browserbase](./generated/providers.md#browserbase) | Not yet task-tested | — | — | — |
| [E2B](./generated/providers.md#e2b) | Not yet task-tested | — | — | — |
| [Modal](./generated/providers.md#modal) | Not yet task-tested | — | — | — |
| [Steel](./generated/providers.md#steel) | Not yet task-tested | — | — | — |

<a id="services-developer-tools"></a>

### Developer Tools (4)

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Atlassian (Jira & Confluence)](./generated/providers.md#atlassian) | Not yet task-tested | — | — | — |
| [GitHub](./generated/providers.md#github) | [Legacy trials](./generated/agent-runs.md#github) | — | — | — |
| [GitLab](./generated/providers.md#gitlab) | Not yet task-tested | — | — | — |
| [Postman](./generated/providers.md#postman) | Not yet task-tested | — | — | — |

<a id="services-cloud-hosting"></a>

### Cloud / Hosting (6)

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Cloudflare](./generated/providers.md#cloudflare) | Not yet task-tested | — | — | — |
| [Fly.io](./generated/providers.md#fly-io) | Not yet task-tested | — | — | — |
| [Netlify](./generated/providers.md#netlify) | Not yet task-tested | — | — | — |
| [Railway](./generated/providers.md#railway) | Not yet task-tested | — | — | — |
| [Render](./generated/providers.md#render) | Not yet task-tested | — | — | — |
| [Vercel](./generated/providers.md#vercel) | Not yet task-tested | — | — | — |

<a id="services-databases"></a>

### Databases (13)

<a id="services-databases-hosted-relational"></a>

#### Hosted Relational Databases

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Neon](./generated/evaluations.md#comparison-fdecec09a4b6) | 100% | 465.4k | — | $0 |
| [Turso](./generated/evaluations.md#comparison-1420586eae17) | 100% | 767.6k | — | $0 |
| [Aiven](./data/candidates/aiven.yaml) | Not yet task-tested | — | — | — |
| [Cloudflare](./generated/providers.md#cloudflare) | Not yet task-tested | — | — | — |
| [PlanetScale](./data/candidates/planetscale.yaml) | Not yet task-tested | — | — | — |
| [Supabase](./generated/providers.md#supabase) | Not yet task-tested | — | — | — |

Existing trials use different or incompletely recorded conditions; these results are not ranked.

<details>
<summary>What we tested and how</summary>

**Task：为我的个人待办应用准备一个独立的远程数据库，验证新增、修改和重新连接后读取待办事项**

仅合成测试数据：id=1,title=Buy milk,done=false；id=2,title=Read book,done=false；id=3,title=Walk dog,done=true。写入三项，再把 id=2 改为 done=true。允许创建无需付费的临时数据库；不能动已有项目

Completion criteria：保存数据后结束写入进程，用另一个全新进程连接同一远程数据库，返回按 id 排序的全部待办、未完成项及总数/完成数；说明资源到期或免费限制；提供可核对的非敏感请求、SQL、真实响应、分开进程执行的证据；实际在指定服务的远程数据库中保存和更新；新进程读回三项且只有 id=1 未完成，总数3、完成数2，标题未变；证据证明独立连接和远程执行。凭据只保存在工作目录私有文件，不得进入 evidence 或最终答案。限时资源可完成此题，但必须明确到期限制

| Service | Tested access | Preparation | Trials |
| --- | --- | --- | --- |
| Neon | [API](https://neon.new/) | No account or key supplied | [1](./generated/evaluations.md#comparison-fdecec09a4b6) |
| Turso | [API](https://docs.turso.tech/api-reference/introduction) | [Service credentials provided](./generated/evaluations.md#comparison-1420586eae17) | [1](./generated/evaluations.md#comparison-1420586eae17) |

**Test configuration：** codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 min · 2026-09-07 (UTC)。

Preparation is outside the measured tokens and time; follow the preparation links for the steps.

[Task definitions](./data/experiments/tasks/databases.md) · [Full runs and evidence](./generated/evaluations.md)

</details>

<a id="services-databases-other"></a>

#### Other services

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Chroma](./generated/providers.md#chroma) | Not yet task-tested | — | — | — |
| [MongoDB Atlas](./generated/providers.md#mongodb-atlas) | Not yet task-tested | — | — | — |
| [Pinecone](./generated/providers.md#pinecone) | Not yet task-tested | — | — | — |
| [Qdrant](./generated/providers.md#qdrant) | Not yet task-tested | — | — | — |
| [Redis (Redis Cloud)](./generated/providers.md#redis) | Not yet task-tested | — | — | — |
| [Upstash](./generated/providers.md#upstash) | Not yet task-tested | — | — | — |
| [Weaviate](./generated/providers.md#weaviate) | Not yet task-tested | — | — | — |

<a id="services-web-search-data"></a>

### Web Search / Data (10)

<a id="services-web-search-data-web-search"></a>

#### Web Search

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Exa / public-mcp](./generated/evaluations.md#comparison-87ab787b88b3) | 100% | 931.5k | — | $0 |
| [Exa / search-api](./generated/evaluations.md#comparison-9dbe771526ac) | 0% | — | — | $0 |
| [Firecrawl](./generated/evaluations.md#comparison-b5f21fc39ab4) | 100% | 346.8k | — | $0 |
| [Brave Search API](./generated/providers.md#brave-search) | Not yet task-tested | — | — | — |
| [SerpApi](./generated/providers.md#serpapi) | Not yet task-tested | — | — | — |
| [Serper](./data/candidates/serper.yaml) | Not yet task-tested | — | — | — |
| [Tavily](./generated/providers.md#tavily) | Not yet task-tested | — | — | — |

Existing trials use different or incompletely recorded conditions; these results are not ranked.

<details>
<summary>What we tested and how</summary>

**Task：我准备把 Python 应用升级到 3.13，查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并给出官方依据**

目标版本 Python 3.13；官方来源范围 python.org；使用本轮指定搜索服务发现来源，可直接读取它返回的来源页面；不依赖模型记忆或其他搜索引擎提供答案

Completion criteria：中文简答覆盖默认状态、启用方式、C 扩展兼容性；至少两个不同的官方页面 URL；每个结论对应来源内容；保存指定服务的搜索请求与真实响应、所用网页内容和访问时间；三个问题均有正确答案且由 Python 3.13 官方资料支持；至少两个不同官方 URL 出现在指定服务的真实搜索响应中；证据可核对。直接抓取搜索返回页面允许，但内置联网检索只可用于服务接入文档，不能替代被测搜索

| Service | Tested access | Preparation | Trials |
| --- | --- | --- | --- |
| Exa | [MCP](https://mcp.exa.ai/mcp) | No account or key supplied | [1](./generated/evaluations.md#comparison-87ab787b88b3) |
| Exa | [API](https://exa.ai/docs/reference/search) | [Service credentials provided](./generated/evaluations.md#comparison-9dbe771526ac) | [1](./generated/evaluations.md#comparison-9dbe771526ac) |
| Firecrawl | [API](https://docs.firecrawl.dev/features/search) | No account or key supplied | [1](./generated/evaluations.md#comparison-b5f21fc39ab4) |

**Test configuration：** codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 min · 2026-09-07 (UTC)。

Preparation is outside the measured tokens and time; follow the preparation links for the steps.

[Task definitions](./data/experiments/tasks/web-search.md) · [Full runs and evidence](./generated/evaluations.md)

</details>

<a id="services-web-search-data-other"></a>

#### Other services

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Apify](./generated/providers.md#apify) | Not yet task-tested | — | — | — |
| [Jina AI](./generated/providers.md#jina) | Not yet task-tested | — | — | — |
| [Perplexity API](./generated/providers.md#perplexity) | Not yet task-tested | — | — | — |
| [Xquik](./data/candidates/xquik.yaml) | [Legacy first-call check](./data/experiments/published/xquik/2026-07-15-dry-fire-rep3.md) | — | — | — |

<a id="services-payments-billing"></a>

### Payments / Billing (4)

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Lemon Squeezy](./generated/providers.md#lemonsqueezy) | Not yet task-tested | — | — | — |
| [paas.build](./data/candidates/paas-build.yaml) | [Legacy first-call check](./data/experiments/published/paas-build/2026-07-15-dry-fire-rep3.md) | — | — | — |
| [Paddle](./generated/providers.md#paddle) | Not yet task-tested | — | — | — |
| [Stripe](./generated/providers.md#stripe) | Not yet task-tested | — | — | — |

<a id="services-communication"></a>

### Communication (6)

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Discord](./generated/providers.md#discord) | Not yet task-tested | — | — | — |
| [Lark](./generated/providers.md#lark) | Not yet task-tested | — | — | — |
| [Resend](./generated/providers.md#resend) | Not yet task-tested | — | — | — |
| [Slack](./generated/providers.md#slack) | Not yet task-tested | — | — | — |
| [Telegram Bot API](./generated/providers.md#telegram) | Not yet task-tested | — | — | — |
| [Twilio](./generated/providers.md#twilio) | Not yet task-tested | — | — | — |

<a id="services-productivity-storage"></a>

### Productivity / Storage (10)

<a id="services-productivity-storage-collaborative-tables"></a>

#### Collaborative Tables

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Grist](./generated/evaluations.md#comparison-6203194a76cd) | 100% | 540.8k | — | $0 |
| [Notion](./generated/evaluations.md#comparison-6203194a76cd) | 100% | 215.5k | $0.75 | $0 |
| [Airtable](./generated/providers.md#airtable) | Not yet task-tested | — | — | — |
| [Baserow Cloud](./data/candidates/baserow.yaml) | Not yet task-tested | — | — | — |
| [Coda / Superhuman Docs](./data/candidates/coda.yaml) | Not yet task-tested | — | — | — |
| [Google Sheets](./data/candidates/google-sheets.yaml) | Not yet task-tested | — | — | — |
| [Lark](./generated/providers.md#lark) | Not yet task-tested | — | — | — |
| [飞书 Feishu](./data/candidates/feishu.yaml) | Not yet task-tested | — | — | — |

<details>
<summary>What we tested and how</summary>

**Task：帮我把这份读书会会议记录里的待办整理成在线任务表，给我链接，再告诉我还有哪些没完成、各自什么时候到期。**

读书会筹备会记录（2026年9月8日）：林青负责确认场地，9月15日前搞定；周舟负责整理书单，9月16日前完成；陈禾负责制作海报，原定9月18日完成。这三件事开会时都还没做完。会后补充：周舟说书单已经整理好了，海报的截止时间改到9月20日，其他安排不变。

Completion criteria：可访问的私有在线任务表链接；未完成事项及负责人、截止日期；远端表中恰好包含三项行动、负责人和最终截止日期正确、书单已完成且另两项未完成；答复给出该表链接并正确列出两项未完成事项及日期；准备者通过服务API独立读取确认。允许自由选择字段与操作顺序，不要求先写入旧状态或输出证据文件

| Service | Tested access | Preparation | Trials |
| --- | --- | --- | --- |
| Grist | [API](https://support.getgrist.com/api/) | [Service credentials provided](./generated/evaluations.md#comparison-6203194a76cd) | [1](./generated/evaluations.md#comparison-6203194a76cd) |
| Notion | [API](https://developers.notion.com/reference/intro) | [Service credentials provided](./generated/evaluations.md#comparison-6203194a76cd) | [1](./generated/evaluations.md#comparison-6203194a76cd) |

**Test configuration：** codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 min · 2026-09-08 (UTC)。

Preparation is outside the measured tokens and time; follow the preparation links for the steps.

[Task definitions](./data/experiments/tasks/collaborative-tables.md) · [Full runs and evidence](./generated/evaluations.md)

</details>

<a id="services-productivity-storage-other"></a>

#### Other services

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Dropbox](./generated/providers.md#dropbox) | Not yet task-tested | — | — | — |
| [Linear](./generated/providers.md#linear) | Not yet task-tested | — | — | — |

<a id="services-observability-security"></a>

### Observability / Security (3)

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Datadog](./generated/providers.md#datadog) | Not yet task-tested | — | — | — |
| [Grafana (Grafana Cloud)](./generated/providers.md#grafana) | Not yet task-tested | — | — | — |
| [Sentry](./generated/providers.md#sentry) | Not yet task-tested | — | — | — |

<a id="services-commerce-marketing"></a>

### Commerce / Marketing (1)

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Shopify](./generated/providers.md#shopify) | Not yet task-tested | — | — | — |

<a id="services-travel"></a>

### Travel (26)

<a id="services-travel-flights"></a>

#### Flights

| Service | Resolution rate | Tokens | Model cost | Service cost |
| --- | ---: | ---: | ---: | ---: |
| [Ignav Flights](./generated/evaluations.md#comparison-45effe165cf4) | 100% | 212.9k | $0.93 | $0 |
| [Kiwi.com](./generated/evaluations.md#comparison-c77feef961a0) | 100% | 209.6k | $0.84 | $0 |
| [AirGateway Platform API](./data/candidates/airgateway.yaml) | Not yet task-tested | — | — | — |
| [Amadeus Flight APIs](./data/candidates/amadeus-flights.yaml) | Not yet task-tested | — | — | — |
| [apiheya Air Scraper](./data/candidates/apiheya-air-scraper.yaml) | Not yet task-tested | — | — | — |
| [Aviasales via Travelpayouts](./data/candidates/aviasales.yaml) | Not yet task-tested | — | — | — |
| [Bright Data SERP API](./data/candidates/bright-data-serp.yaml) | Not yet task-tested | — | — | — |
| [Duffel Flights API](./data/candidates/duffel-flights.yaml) | Not yet task-tested | — | — | — |
| [Expedia XAP Flight Listings](./data/candidates/expedia-xap-flights.yaml) | Not yet task-tested | — | — | — |
| [Flight MCP](./data/candidates/flight-mcp.yaml) | Not yet task-tested | — | — | — |
| [FlightAPI.io Flight Price API](./data/candidates/flightapi-io.yaml) | Not yet task-tested | — | — | — |
| [KAYAK Affiliate API](./data/candidates/kayak-affiliate.yaml) | Not yet task-tested | — | — | — |
| [LetsFG Personal Flight Search](./data/candidates/letsfg.yaml) | Not yet task-tested | — | — | — |
| [Lufthansa Partner Fare API](./data/candidates/lufthansa-partner.yaml) | Not yet task-tested | — | — | — |
| [Sabre Air APIs](./data/candidates/sabre-air.yaml) | Not yet task-tested | — | — | — |
| [Scrapingdog Google Flights API](./data/candidates/scrapingdog-flights.yaml) | Not yet task-tested | — | — | — |
| [SearchApi Google Flights](./data/candidates/searchapi.yaml) | Not yet task-tested | — | — | — |
| [SerpApi](./generated/providers.md#serpapi) | Not yet task-tested | — | — | — |
| [Skootle Google Flights Scraper](./data/candidates/skootle-google-flights.yaml) | Not yet task-tested | — | — | — |
| [Skyscanner Travel APIs](./data/candidates/skyscanner.yaml) | Not yet task-tested | — | — | — |
| [Travelport TripServices](./data/candidates/travelport-tripservices.yaml) | Not yet task-tested | — | — | — |
| [Trip.com Flight Distribution](./data/candidates/trip-com-flights.yaml) | Not yet task-tested | — | — | — |
| [去哪儿机票合作](./data/candidates/qunar-flights.yaml) | Not yet task-tested | — | — | — |
| [同程机票合作](./data/candidates/tongcheng-flights.yaml) | Not yet task-tested | — | — | — |
| [携程机票合作](./data/candidates/ctrip-flights.yaml) | Not yet task-tested | — | — | — |
| [飞猪国内机票开放平台](./data/candidates/fliggy-domestic-flights.yaml) | Not yet task-tested | — | — | — |

Existing trials use different or incompletely recorded conditions; these results are not ranked.

<details>
<summary>What we tested and how</summary>

**Task：找到9月25日米兰飞往荷兰的机票**

2026-09-25；本题出发范围约定为MXP/LIN/BGY，抵达荷兰任一客运机场；1名成人、单程、经济舱，允许中转；本轮指定的服务入口

Completion criteria：至少一个符合条件的航班方案，包含各航段机场、航班号、当地起降日期时间、搜索报价与币种，以及查询来源；至少一个方案满足日期、路线和旅客条件；关键信息与执行器取得的真实服务响应相符。仅验搜索结果，不验全网最低价或支付成功

| Service | Tested access | Preparation | Trials |
| --- | --- | --- | --- |
| Ignav Flights | [Web Playground](https://ignav.com/playground) | No account or key supplied | [1](./generated/evaluations.md#comparison-45effe165cf4) |
| Kiwi.com | [MCP](https://mcp.kiwi.com) | No account or key supplied | [1](./generated/evaluations.md#comparison-c77feef961a0) |

**Test configuration：** codex-cli 0.153.4 · gpt-6-astra / xhigh · 10 min · 2026-09-07 (UTC)。

Some early records lack environment details and await a controlled rerun. The web results for Ignav Flights do not establish API or MCP performance.

[Task definitions](./data/experiments/tasks/travel-flights.md) · [Full runs and evidence](./generated/evaluations.md)

</details>

## Help us fill the gaps

Know a service we missed, have a task you would like tested, or found something that has changed? Issues and PRs are welcome. A useful lead or a correction is a contribution too.

[Principles](./AGENTS.md) · [Inclusion standards](./docs/catalog-standard.zh-CN.md) · [Task design](./data/experiments/tasks/AGENTS.md) · [Execution and review](./data/experiments/AGENTS.md) · [Contributing](./docs/contributing.md) · [Flight findings](./docs/flights.zh-CN.md)

Code: [MIT](./LICENSE) · Data: [CC BY 4.0](./LICENSE-DATA).
