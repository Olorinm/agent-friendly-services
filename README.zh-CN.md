<!-- 生成文件 — 修改 scripts/generate.ts，再运行 npm run generate。 -->

# Agent-Friendly Services

[English](./README.md) | 简体中文

**帮你找到能让 Agent 完成任务的服务，并用实测比较哪个更可靠、更省事、更有性价比。**

让 Agent 帮忙找机票、准备数据库或整理会议待办，往往还得先选服务、读文档、申请账号，再试试到底能不能用。我们把这些选择收集起来，用真实任务逐步验证，让你和你的 Agent 少走一些重复的弯路。我们关注普通个人能用上的服务，注册、权限和付费门槛也会一并记录。

## 看看有哪些服务

按下面的分类，可以找到候选服务、我们设计的任务，以及已经留下的实测结果。

| 大类 / 子类 | 候选服务 | 任务定义 | 实测记录 | 有运行记录的服务 |
| --- | ---: | --- | ---: | --- |
| 数据库 / 托管关系型数据库 | [6](./generated/catalog.md#databases-hosted-relational) | [任务](./data/experiments/tasks/databases.md) | [2](./generated/evaluations.md#databases-hosted-relational) | Neon, Turso |
| 协作办公与存储 / 在线任务表 | [8](./generated/catalog.md#productivity-storage-collaborative-tables) | [任务](./data/experiments/tasks/collaborative-tables.md) | [4](./generated/evaluations.md#productivity-storage-collaborative-tables) | Grist, Notion |
| 旅行 / 航空机票 | [26](./generated/catalog.md#travel-flights) | [任务](./data/experiments/tasks/travel-flights.md) | [4](./generated/evaluations.md#travel-flights) | Ignav Flights, Kiwi.com |
| 网页搜索与数据 / 网页搜索 | [6](./generated/catalog.md#web-search-data-web-search) | [任务](./data/experiments/tasks/web-search.md) | [3](./generated/evaluations.md#web-search-data-web-search) | Exa, Firecrawl |

[浏览大名单](#all-services) · [全部候选与接入方式](./generated/catalog.md) · [全部实测与证据](./generated/evaluations.md) · [旧版服务索引（76）](./generated/providers.md)

点开实测记录，可以看到 Agent 实际做成了什么、需要哪些准备，以及用了多少 token、时间和服务费用。每次运行也保留任务、模型、日期与证据，方便你判断结果是否适用于自己的情况。

资料还在持续积累。未测的服务、遇到的接入门槛都会保留，运行次数也包含历史版本和未成功的尝试。一次成功能提供参考；要推荐谁更值得用，还需要更多可比的结果。

## 也可以交给你的 Agent 来查

把下面的查询指引交给你的 Agent，让它结合你的任务寻找候选、核对接入条件，再根据已有证据说明推荐理由。

[查询指引](./llms.txt) · [服务 JSON](./generated/catalog.json) · [实测 JSON](./generated/evaluations.json) · [MCP 配置](./mcp/README.md)

通过 `search_services` 按分类和接入方式检索，再用 `get_service` 查看个人准入条件、费用与实测依据。不安装 MCP 也可直接读取：

```sh
curl -s https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/catalog.json
```

<a id="all-services"></a>

## 服务大名单（112）

用量和费用均为每次有效试跑的平均值，包含成功与失败；模型费用按保存的 LiteLLM 价表估算，服务费用按记录来源核验（估算额标 ~）。— 表示未知或未测。仅在相同任务版本、重复次数与配置内比较；历史记录和接入细节可展开查看。

[AI Models](#services-ai-models) · [Agent Tooling](#services-agent-tooling) · [Code Execution](#services-code-execution) · [Developer Tools](#services-developer-tools) · [Cloud / Hosting](#services-cloud-hosting) · [Databases](#services-databases) · [Web Search / Data](#services-web-search-data) · [Payments / Billing](#services-payments-billing) · [Communication](#services-communication) · [Productivity / Storage](#services-productivity-storage) · [Observability / Security](#services-observability-security) · [Commerce / Marketing](#services-commerce-marketing) · [Travel](#services-travel)

<a id="services-ai-models"></a>

### AI Models (23)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Alibaba Qwen (Model Studio)](./generated/providers.md#qwen) | 待实测 | — | — | — |
| [Anthropic](./generated/providers.md#anthropic) | 待实测 | — | — | — |
| [Cartesia](./generated/providers.md#cartesia) | 待实测 | — | — | — |
| [Cerebras Inference](./generated/providers.md#cerebras) | 待实测 | — | — | — |
| [Cohere](./generated/providers.md#cohere) | 待实测 | — | — | — |
| [Deepgram](./generated/providers.md#deepgram) | 待实测 | — | — | — |
| [DeepSeek](./generated/providers.md#deepseek) | 待实测 | — | — | — |
| [ElevenLabs](./generated/providers.md#elevenlabs) | 待实测 | — | — | — |
| [fal.ai](./generated/providers.md#fal) | 待实测 | — | — | — |
| [Fireworks AI](./generated/providers.md#fireworks) | 待实测 | — | — | — |
| [Gemini API](./generated/providers.md#gemini-api) | 待实测 | — | — | — |
| [Groq](./generated/providers.md#groq) | 待实测 | — | — | — |
| [Hugging Face](./generated/providers.md#hugging-face) | 待实测 | — | — | — |
| [Luma AI (Dream Machine)](./generated/providers.md#luma) | 待实测 | — | — | — |
| [MiniMax](./generated/providers.md#minimax) | 待实测 | — | — | — |
| [Mistral AI](./generated/providers.md#mistral) | 待实测 | — | — | — |
| [Moonshot AI (Kimi)](./generated/providers.md#moonshot) | 待实测 | — | — | — |
| [OpenAI](./generated/providers.md#openai) | 待实测 | — | — | — |
| [OpenRouter](./generated/providers.md#openrouter) | 待实测 | — | — | — |
| [Replicate](./generated/providers.md#replicate) | 待实测 | — | — | — |
| [Together AI](./generated/providers.md#together-ai) | 待实测 | — | — | — |
| [xAI (Grok API)](./generated/providers.md#xai) | 待实测 | — | — | — |
| [Z.ai (GLM)](./generated/providers.md#zai) | 待实测 | — | — | — |

<a id="services-agent-tooling"></a>

### Agent Tooling (5)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Composio](./generated/providers.md#composio) | 待实测 | — | — | — |
| [Mem0](./generated/providers.md#mem0) | 待实测 | — | — | — |
| [n8n](./generated/providers.md#n8n) | 待实测 | — | — | — |
| [Vapi](./generated/providers.md#vapi) | 待实测 | — | — | — |
| [Zapier](./generated/providers.md#zapier) | 待实测 | — | — | — |

<a id="services-code-execution"></a>

### Code Execution (4)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Browserbase](./generated/providers.md#browserbase) | 待实测 | — | — | — |
| [E2B](./generated/providers.md#e2b) | 待实测 | — | — | — |
| [Modal](./generated/providers.md#modal) | 待实测 | — | — | — |
| [Steel](./generated/providers.md#steel) | 待实测 | — | — | — |

<a id="services-developer-tools"></a>

### Developer Tools (4)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Atlassian (Jira & Confluence)](./generated/providers.md#atlassian) | 待实测 | — | — | — |
| [GitHub](./generated/providers.md#github) | [历史实测](./generated/agent-runs.md#github) | — | — | — |
| [GitLab](./generated/providers.md#gitlab) | 待实测 | — | — | — |
| [Postman](./generated/providers.md#postman) | 待实测 | — | — | — |

<a id="services-cloud-hosting"></a>

### Cloud / Hosting (6)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Cloudflare](./generated/providers.md#cloudflare) | 待实测 | — | — | — |
| [Fly.io](./generated/providers.md#fly-io) | 待实测 | — | — | — |
| [Netlify](./generated/providers.md#netlify) | 待实测 | — | — | — |
| [Railway](./generated/providers.md#railway) | 待实测 | — | — | — |
| [Render](./generated/providers.md#render) | 待实测 | — | — | — |
| [Vercel](./generated/providers.md#vercel) | 待实测 | — | — | — |

<a id="services-databases"></a>

### Databases (13)

<a id="services-databases-hosted-relational"></a>

#### 托管关系型数据库

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Neon](./generated/evaluations.md#comparison-fdecec09a4b6) | 100% | 465.4k | — | $0 |
| [Turso](./generated/evaluations.md#comparison-1420586eae17) | 100% | 767.6k | — | $0 |
| [Aiven](./data/candidates/aiven.yaml) | 待实测 | — | — | — |
| [Cloudflare](./generated/providers.md#cloudflare) | 待实测 | — | — | — |
| [PlanetScale](./data/candidates/planetscale.yaml) | 待实测 | — | — | — |
| [Supabase](./generated/providers.md#supabase) | 待实测 | — | — | — |

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

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Chroma](./generated/providers.md#chroma) | 待实测 | — | — | — |
| [MongoDB Atlas](./generated/providers.md#mongodb-atlas) | 待实测 | — | — | — |
| [Pinecone](./generated/providers.md#pinecone) | 待实测 | — | — | — |
| [Qdrant](./generated/providers.md#qdrant) | 待实测 | — | — | — |
| [Redis (Redis Cloud)](./generated/providers.md#redis) | 待实测 | — | — | — |
| [Upstash](./generated/providers.md#upstash) | 待实测 | — | — | — |
| [Weaviate](./generated/providers.md#weaviate) | 待实测 | — | — | — |

<a id="services-web-search-data"></a>

### Web Search / Data (10)

<a id="services-web-search-data-web-search"></a>

#### 网页搜索

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Exa / public-mcp](./generated/evaluations.md#comparison-87ab787b88b3) | 100% | 931.5k | — | $0 |
| [Exa / search-api](./generated/evaluations.md#comparison-9dbe771526ac) | 0% | — | — | $0 |
| [Firecrawl](./generated/evaluations.md#comparison-b5f21fc39ab4) | 100% | 346.8k | — | $0 |
| [Brave Search API](./generated/providers.md#brave-search) | 待实测 | — | — | — |
| [SerpApi](./generated/providers.md#serpapi) | 待实测 | — | — | — |
| [Serper](./data/candidates/serper.yaml) | 待实测 | — | — | — |
| [Tavily](./generated/providers.md#tavily) | 待实测 | — | — | — |

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

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Apify](./generated/providers.md#apify) | 待实测 | — | — | — |
| [Jina AI](./generated/providers.md#jina) | 待实测 | — | — | — |
| [Perplexity API](./generated/providers.md#perplexity) | 待实测 | — | — | — |
| [Xquik](./data/candidates/xquik.yaml) | [历史首次调用检查](./data/experiments/published/xquik/2026-07-15-dry-fire-rep3.md) | — | — | — |

<a id="services-payments-billing"></a>

### Payments / Billing (4)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Lemon Squeezy](./generated/providers.md#lemonsqueezy) | 待实测 | — | — | — |
| [paas.build](./data/candidates/paas-build.yaml) | [历史首次调用检查](./data/experiments/published/paas-build/2026-07-15-dry-fire-rep3.md) | — | — | — |
| [Paddle](./generated/providers.md#paddle) | 待实测 | — | — | — |
| [Stripe](./generated/providers.md#stripe) | 待实测 | — | — | — |

<a id="services-communication"></a>

### Communication (6)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Discord](./generated/providers.md#discord) | 待实测 | — | — | — |
| [Lark](./generated/providers.md#lark) | 待实测 | — | — | — |
| [Resend](./generated/providers.md#resend) | 待实测 | — | — | — |
| [Slack](./generated/providers.md#slack) | 待实测 | — | — | — |
| [Telegram Bot API](./generated/providers.md#telegram) | 待实测 | — | — | — |
| [Twilio](./generated/providers.md#twilio) | 待实测 | — | — | — |

<a id="services-productivity-storage"></a>

### Productivity / Storage (10)

<a id="services-productivity-storage-collaborative-tables"></a>

#### 在线任务表

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Grist](./generated/evaluations.md#comparison-6203194a76cd) | 100% | 540.8k | — | $0 |
| [Notion](./generated/evaluations.md#comparison-6203194a76cd) | 100% | 215.5k | $0.75 | $0 |
| [Airtable](./generated/providers.md#airtable) | 待实测 | — | — | — |
| [Baserow Cloud](./data/candidates/baserow.yaml) | 待实测 | — | — | — |
| [Coda / Superhuman Docs](./data/candidates/coda.yaml) | 待实测 | — | — | — |
| [Google Sheets](./data/candidates/google-sheets.yaml) | 待实测 | — | — | — |
| [Lark](./generated/providers.md#lark) | 待实测 | — | — | — |
| [飞书 Feishu](./data/candidates/feishu.yaml) | 待实测 | — | — | — |

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

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Dropbox](./generated/providers.md#dropbox) | 待实测 | — | — | — |
| [Linear](./generated/providers.md#linear) | 待实测 | — | — | — |

<a id="services-observability-security"></a>

### Observability / Security (3)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Datadog](./generated/providers.md#datadog) | 待实测 | — | — | — |
| [Grafana (Grafana Cloud)](./generated/providers.md#grafana) | 待实测 | — | — | — |
| [Sentry](./generated/providers.md#sentry) | 待实测 | — | — | — |

<a id="services-commerce-marketing"></a>

### Commerce / Marketing (1)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Shopify](./generated/providers.md#shopify) | 待实测 | — | — | — |

<a id="services-travel"></a>

### Travel (26)

<a id="services-travel-flights"></a>

#### 航空机票

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Ignav Flights](./generated/evaluations.md#comparison-45effe165cf4) | 100% | 212.9k | $0.93 | $0 |
| [Kiwi.com](./generated/evaluations.md#comparison-c77feef961a0) | 100% | 209.6k | $0.84 | $0 |
| [AirGateway Platform API](./data/candidates/airgateway.yaml) | 待实测 | — | — | — |
| [Amadeus Flight APIs](./data/candidates/amadeus-flights.yaml) | 待实测 | — | — | — |
| [apiheya Air Scraper](./data/candidates/apiheya-air-scraper.yaml) | 待实测 | — | — | — |
| [Aviasales via Travelpayouts](./data/candidates/aviasales.yaml) | 待实测 | — | — | — |
| [Bright Data SERP API](./data/candidates/bright-data-serp.yaml) | 待实测 | — | — | — |
| [Duffel Flights API](./data/candidates/duffel-flights.yaml) | 待实测 | — | — | — |
| [Expedia XAP Flight Listings](./data/candidates/expedia-xap-flights.yaml) | 待实测 | — | — | — |
| [Flight MCP](./data/candidates/flight-mcp.yaml) | 待实测 | — | — | — |
| [FlightAPI.io Flight Price API](./data/candidates/flightapi-io.yaml) | 待实测 | — | — | — |
| [KAYAK Affiliate API](./data/candidates/kayak-affiliate.yaml) | 待实测 | — | — | — |
| [LetsFG Personal Flight Search](./data/candidates/letsfg.yaml) | 待实测 | — | — | — |
| [Lufthansa Partner Fare API](./data/candidates/lufthansa-partner.yaml) | 待实测 | — | — | — |
| [Sabre Air APIs](./data/candidates/sabre-air.yaml) | 待实测 | — | — | — |
| [Scrapingdog Google Flights API](./data/candidates/scrapingdog-flights.yaml) | 待实测 | — | — | — |
| [SearchApi Google Flights](./data/candidates/searchapi.yaml) | 待实测 | — | — | — |
| [SerpApi](./generated/providers.md#serpapi) | 待实测 | — | — | — |
| [Skootle Google Flights Scraper](./data/candidates/skootle-google-flights.yaml) | 待实测 | — | — | — |
| [Skyscanner Travel APIs](./data/candidates/skyscanner.yaml) | 待实测 | — | — | — |
| [Travelport TripServices](./data/candidates/travelport-tripservices.yaml) | 待实测 | — | — | — |
| [Trip.com Flight Distribution](./data/candidates/trip-com-flights.yaml) | 待实测 | — | — | — |
| [去哪儿机票合作](./data/candidates/qunar-flights.yaml) | 待实测 | — | — | — |
| [同程机票合作](./data/candidates/tongcheng-flights.yaml) | 待实测 | — | — | — |
| [携程机票合作](./data/candidates/ctrip-flights.yaml) | 待实测 | — | — | — |
| [飞猪国内机票开放平台](./data/candidates/fliggy-domestic-flights.yaml) | 待实测 | — | — | — |

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

## 一起补全这份资料

如果你知道我们漏掉的服务、有想测的真实任务，或发现资料已经过时，欢迎提 Issue 或 PR。提供一条线索、纠正一个事实，都能帮上忙。

[核心理念](./AGENTS.md) · [收录标准](./docs/catalog-standard.zh-CN.md) · [任务设计](./data/experiments/tasks/AGENTS.md) · [执行与验收](./data/experiments/AGENTS.md) · [参与贡献](./docs/contributing.md) · [机票阶段结论](./docs/flights.zh-CN.md)

代码：[MIT](./LICENSE) · 数据：[CC BY 4.0](./LICENSE-DATA)。
