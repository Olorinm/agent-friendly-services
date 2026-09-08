<!-- GENERATED — edit source records; run npm run generate. -->
# Service profiles

Access and pricing are source claims; task results apply only to the recorded conditions.

<a id="airgateway"></a>

## AirGateway Platform API

Air distribution API with sandbox keys, production certification and an agency application.

[Website](https://airgateway.com/) · [Source record](../data/candidates/airgateway.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://support.airgateway.com/en-US/kb/article/4/introduction-to-airgateway-platform-api)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [agency-api (api)](https://support.airgateway.com/en-US/kb/article/4/introduction-to-airgateway-platform-api) | application / restricted | Requires: company, industry_license, approval; This does not prove the absence of other individual-facing AirGateway products. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://support.airgateway.com/en-US/kb/article/4/introduction-to-airgateway-platform-api) — checked 2026-09-07
- [official_site](https://airgateway.com/agencies/) — checked 2026-09-07

<a id="airtable"></a>

## Airtable

Spreadsheet-database hybrid with a REST API, scoped personal access tokens, OAuth, webhooks, and documented rate limits.

[Website](https://www.airtable.com) · [Source record](../data/providers/airtable.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://airtable.com/developers) · [API](https://airtable.com/developers/web/api/introduction)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [web-api (api)](https://airtable.com/developers/web/api/introduction) | self_serve / documented | Requirements not fully recorded; Create a personal access token with required scopes and selected test resources.; PAT scopes plus selected workspace/base access required. Base creation is documented on all plans; do not infer paid-only access from outdated posts. |

### Service pricing

[Official pricing](https://airtable.com/pricing)

- web-api: 1000 API calls / workspace/month (free_allowance; Free plan; includes metadata/schema calls, 5 requests/second/base.)

- web-api: 1000 records / base (free_allowance; Free plan storage limit across all tables in a base.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://support.airtable.com/articles/6292134965-getting-started-with-airtable-s-web-api) — checked 2026-09-08
- [official_docs](https://airtable.com/developers/web/guides/personal-access-tokens) — checked 2026-09-08
- [official_docs](https://support.airtable.com/articles/2277136852-airtable-plans-overview) — checked 2026-09-08
- [official_docs](https://support.airtable.com/articles/7735693959-managing-api-call-limits-in-airtable) — checked 2026-09-08

<a id="aiven"></a>

## Aiven

Managed databases including free hosted PostgreSQL. Account signup and provisioning remain untested; free lifecycle limits need checking before production use.

[Website](https://aiven.io/) · [Source record](../data/candidates/aiven.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[CLI](https://aiven.io/docs/tools/cli)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [postgres-cli (cli)](https://aiven.io/docs/tools/cli) | self_serve / documented | Requirements not fully recorded; Managed databases including free hosted PostgreSQL. Account signup and provisioning remain untested; free lifecycle limits need checking before production use. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://aiven.io/docs/tools/cli) — checked 2026-09-07
- [official_site](https://aiven.io/free-postgresql-database) — checked 2026-09-07

<a id="qwen"></a>

## Alibaba Qwen (Model Studio)

Qwen model family via Alibaba Cloud Model Studio's OpenAI-compatible API, with an official open-source coding CLI agent (qwen-code).

[Website](https://www.alibabacloud.com/en/product/modelstudio) · [Source record](../data/providers/qwen.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://www.alibabacloud.com/help/en/model-studio/) · [API](https://www.alibabacloud.com/help/en/model-studio/models) · [CLI](https://github.com/QwenLM/qwen-code)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/qwen.yaml).

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/qwen.yaml).

<a id="amadeus-flights"></a>

## Amadeus Flight APIs

Historical Self-Service flight API and the current Enterprise portal; individual onboarding must be re-established.

[Website](https://developers.amadeus.com/) · [Source record](../data/candidates/amadeus-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://developers.amadeus.com/blog/comparing-open-source-flight-data-sources) · [API](https://developers.amadeus.com/)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [former-self-service (api)](https://developers.amadeus.com/blog/comparing-open-source-flight-data-sources) | retired / unknown | Requirements not fully recorded; Retain this historical access path. Stale tutorials do not establish current self-service signup. |
| [enterprise-api (api)](https://developers.amadeus.com/) | unknown / unknown | Requirements not fully recorded; Current portal lead; personal eligibility, application requirements, costs and current flight endpoints remain unknown. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_announcement](https://developers.amadeus.com/blog/comparing-open-source-flight-data-sources) — checked 2026-09-07
- [official_site](https://developers.amadeus.com/) — checked 2026-09-07

<a id="anthropic"></a>

## Anthropic

Claude model APIs with agent-focused documentation, llms.txt, and the company behind the MCP standard itself.

[Website](https://www.anthropic.com) · [Source record](../data/providers/anthropic.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.anthropic.com) · [API](https://docs.anthropic.com/en/api) · [CLI](https://docs.anthropic.com/en/docs/claude-code) · [SDK](https://docs.anthropic.com/en/api/client-sdks)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/anthropic.yaml).

### Service pricing

[Official pricing](https://www.anthropic.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/anthropic.yaml).

<a id="apify"></a>

## Apify

Web scraping and automation platform with thousands of ready-made actors, a versioned API, llms.txt, and an official MCP server.

[Website](https://apify.com) · [Source record](../data/providers/apify.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.apify.com) · [API](https://docs.apify.com/api/v2) · [CLI](https://docs.apify.com/cli) · [SDK](https://docs.apify.com/sdk) · [MCP](https://docs.apify.com/platform/integrations/mcp)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/apify.yaml).

### Service pricing

[Official pricing](https://apify.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/apify.yaml).

<a id="apiheya-air-scraper"></a>

## apiheya Air Scraper

An apiheya flight-data product distributed through RapidAPI; distinct from the official Skyscanner partner API.

[Website](https://rapidapi.com/apiheya/api/sky-scrapper/pricing) · [Source record](../data/candidates/apiheya-air-scraper.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://rapidapi.com/apiheya/api/sky-scrapper/playground/apiendpoint_6856e0a6-2804-43cd-9cc0-bb377022981e)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [rapidapi-product (api)](https://rapidapi.com/apiheya/api/sky-scrapper/playground/apiendpoint_6856e0a6-2804-43cd-9cc0-bb377022981e) | unknown / unknown | Requires: platform_account; Publisher is apiheya; RapidAPI is the marketplace. Upstream identity is not established by a product slug. |

### Service pricing

- rapidapi-product: 20 requests / month (free_allowance; Listed Basic plan; card requirements and included flight endpoints unverified.)

### Task results

Not yet task-tested.

### Sources

- [publisher_listing](https://rapidapi.com/apiheya/api/sky-scrapper/playground/apiendpoint_6856e0a6-2804-43cd-9cc0-bb377022981e) — checked 2026-09-07
- [publisher_listing](https://rapidapi.com/apiheya/api/sky-scrapper/pricing) — checked 2026-09-07

<a id="atlassian"></a>

## Atlassian (Jira & Confluence)

Jira, Confluence and the Atlassian Cloud platform — REST APIs, an official remote MCP server (OAuth 2.1), and the acli CLI.

[Website](https://www.atlassian.com) · [Source record](../data/providers/atlassian.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://developer.atlassian.com) · [API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/) · [CLI](https://developer.atlassian.com/cloud/acli/) · [MCP](https://github.com/atlassian/atlassian-mcp-server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/atlassian.yaml).

### Service pricing

[Official pricing](https://www.atlassian.com/software/jira/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/atlassian.yaml).

<a id="aviasales"></a>

## Aviasales via Travelpayouts

Travelpayouts-distributed live flight search and a separately accessible historical price-data API.

[Website](https://www.aviasales.com/) · [Source record](../data/candidates/aviasales.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://support.travelpayouts.com/hc/en-us/articles/210995808-How-to-get-access-to-the-Aviasales-Search-API) · [API](https://support.travelpayouts.com/hc/en-us/articles/203956163-Aviasales-Data-API)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [live-search-api (api)](https://support.travelpayouts.com/hc/en-us/articles/210995808-How-to-get-access-to-the-Aviasales-Search-API) | application / restricted | Requires: platform_account, approval, traffic |
| [cached-data-api (api)](https://support.travelpayouts.com/hc/en-us/articles/203956163-Aviasales-Data-API) | self_serve / unknown | Requires: platform_account; Historical user-search cache for price trends and inspiration. Each method has its own time window; no fresh search is triggered. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://support.travelpayouts.com/hc/en-us/articles/210995808-How-to-get-access-to-the-Aviasales-Search-API) — checked 2026-09-07
- [official_docs](https://support.travelpayouts.com/hc/en-us/articles/203956083-Requirements-for-Aviasales-data-API-access) — checked 2026-09-07
- [official_docs](https://support.travelpayouts.com/hc/en-us/articles/203956163-Aviasales-Data-API) — checked 2026-09-07

<a id="baserow"></a>

## Baserow Cloud

Hosted collaborative tables; free workspace and scoped row-access tokens. Schema management uses a different credential.

[Website](https://baserow.io/) · [Source record](../data/candidates/baserow.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://baserow.io/docs/apis/rest-api) · [MCP](https://baserow.io/user-docs/mcp-server)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [database-api (api)](https://baserow.io/docs/apis/rest-api) | self_serve / documented | Requirements not fully recorded; Generate a database token and select permitted tables and operations.; Database token can read/create/update/delete rows in permitted tables; creating the table/schema requires a short-lived JWT. A precreated table changes the test setup. |
| [native-mcp (mcp)](https://baserow.io/user-docs/mcp-server) | unknown / unknown | Requirements not fully recorded; Create a workspace MCP endpoint in account settings and securely store its private URL.; Workspace admin creates a unique secret-bearing endpoint URL; the URL is itself a credential and must not be published. Documented tools read schema/list tables and create/update/delete rows, but do not list table creation. Cloud plan availability is not yet verified; do not assume this route can provision task 001 from an empty container. |

### Service pricing

- database-api: 3000 rows / workspace (free_allowance; Cloud Free plan. 2 GB storage. JWT/schema access and database row tokens are distinct.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://baserow.io/docs/apis/rest-api) — checked 2026-09-08
- [official_docs](https://baserow.io/user-docs/personal-api-tokens) — checked 2026-09-08
- [official_site](https://baserow.io/pricing) — checked 2026-09-08
- [official_docs](https://baserow.io/user-docs/mcp-server) — checked 2026-09-08

<a id="brave-search"></a>

## Brave Search API

Independent web search index with a developer API, self-serve registration, and a free plan.

[Website](https://brave.com/search/api/) · [Source record](../data/providers/brave-search.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://api-dashboard.search.brave.com/app/documentation) · [API](https://brave.com/search/api/) · [MCP](https://github.com/brave/brave-search-mcp-server)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [search-api (api)](https://brave.com/search/api/) | self_serve / documented | Requires: payment_method; Free-plan card verification is required. No card supplied in this pilot; onboarding restriction does not establish poor search quality. |

### Service pricing

[Official pricing](https://brave.com/search/api/)

### Task results

Not yet task-tested.

### Sources

- [official_site](https://brave.com/search/api/) — checked 2026-09-07

<a id="bright-data-serp"></a>

## Bright Data SERP API

SERP API with a documented Google Flights request; structured fare extraction and onboarding need verification.

[Website](https://brightdata.com/) · [Source record](../data/candidates/bright-data-serp.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://docs.brightdata.com/api-reference/serp/google-flights/currency)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [google-flights-serp (api)](https://docs.brightdata.com/api-reference/serp/google-flights/currency) | unknown / unknown | Requirements not fully recorded; Requires a SERP zone. Do not apply other Bright Data products’ payment requirements to this route. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://docs.brightdata.com/api-reference/serp/google-flights/currency) — checked 2026-09-07
- [official_docs](https://docs.brightdata.com/general/account/billing-and-pricing/payment-verification) — checked 2026-09-07
- [official_docs](https://docs.brightdata.com/cn/scraping-automation/serp-api/quickstart) — checked 2026-09-07

<a id="browserbase"></a>

## Browserbase

Headless browser infrastructure for AI agents and automation, with session APIs and an official MCP server.

[Website](https://www.browserbase.com) · [Source record](../data/providers/browserbase.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.browserbase.com) · [API](https://docs.browserbase.com/reference) · [SDK](https://docs.browserbase.com/reference) · [MCP](https://github.com/browserbase/mcp-server-browserbase)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/browserbase.yaml).

### Service pricing

[Official pricing](https://www.browserbase.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/browserbase.yaml).

<a id="cartesia"></a>

## Cartesia

Low-latency voice models (Sonic TTS, Ink STT) with a documented API, official MCP server, llms.txt, and a free tier.

[Website](https://cartesia.ai) · [Source record](../data/providers/cartesia.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.cartesia.ai) · [API](https://docs.cartesia.ai/api-reference) · [MCP](https://github.com/cartesia-ai/cartesia-mcp)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/cartesia.yaml).

### Service pricing

[Official pricing](https://www.cartesia.ai/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/cartesia.yaml).

<a id="cerebras"></a>

## Cerebras Inference

Wafer-scale inference for open models at very high tokens/sec, OpenAI-compatible API, llms.txt, and a standing free tier.

[Website](https://cloud.cerebras.ai) · [Source record](../data/providers/cerebras.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://inference-docs.cerebras.ai) · [API](https://inference-docs.cerebras.ai/api-reference/chat-completions)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/cerebras.yaml).

### Service pricing

[Official pricing](https://www.cerebras.ai/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/cerebras.yaml).

<a id="chroma"></a>

## Chroma

Open-source embedding database with a hosted Chroma Cloud, official CLI, official MCP server, and llms.txt.

[Website](https://www.trychroma.com) · [Source record](../data/providers/chroma.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.trychroma.com) · [API](https://docs.trychroma.com/docs/overview/introduction) · [CLI](https://docs.trychroma.com/docs/cli/install) · [MCP](https://github.com/chroma-core/chroma-mcp)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/chroma.yaml).

### Service pricing

[Official pricing](https://www.trychroma.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/chroma.yaml).

<a id="cloudflare"></a>

## Cloudflare

Edge network, Workers serverless platform, storage, and AI services with agent-focused docs and official MCP servers.

[Website](https://www.cloudflare.com) · [Source record](../data/providers/cloudflare.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://developers.cloudflare.com) · [CLI](https://developers.cloudflare.com/d1/get-started/) · [API](https://developers.cloudflare.com/api/) · [CLI](https://developers.cloudflare.com/workers/wrangler/) · [SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/) · [MCP](https://github.com/cloudflare/mcp-server-cloudflare)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [d1-cli (cli)](https://developers.cloudflare.com/d1/get-started/) | self_serve / documented | Requirements not fully recorded; D1 Workers Free: 5 million reads/day, 100,000 writes/day, 5 GB total storage. Account authorization required; Wrangler local mode is not a remote database test. Existing paid projects are excluded. |

### Service pricing

[Official pricing](https://www.cloudflare.com/plans/)

- d1-cli: 5 GB / account (free_allowance; D1 total storage on Workers Free; separate daily row quotas.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://developers.cloudflare.com/d1/get-started/) — checked 2026-09-07
- [official_docs](https://developers.cloudflare.com/d1/platform/pricing/) — checked 2026-09-07

<a id="coda"></a>

## Coda / Superhuman Docs

Docs and tables with a free REST API; current API page is branded Superhuman Docs.

[Website](https://coda.io/) · [Source record](../data/candidates/coda.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://coda.io/developers/apis/v1) · [MCP](https://coda.io/apis/mcp)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [rest-api (api)](https://coda.io/developers/apis/v1) | self_serve / unknown | Requirements not fully recorded; API available in free and paid workspaces. Creating docs requires a Doc Maker role; row writes may be asynchronous. Table/schema creation support must be verified for the task. |
| [hosted-mcp (mcp)](https://coda.io/apis/mcp) | self_serve / unknown | Requirements not fully recorded; Official hosted MCP; connector setup needs authorization. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://coda.io/developers/apis/v1) — checked 2026-09-08
- [official_docs](https://help.coda.io/hc/en-us/articles/44722661982989-Connect-to-the-Coda-MCP) — checked 2026-09-08

<a id="cohere"></a>

## Cohere

Enterprise LLM platform (command, embed, rerank) with llms.txt, documented API versioning, free trial keys, and error/rate-limit docs.

[Website](https://cohere.com) · [Source record](../data/providers/cohere.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.cohere.com) · [API](https://docs.cohere.com/reference/about)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/cohere.yaml).

### Service pricing

[Official pricing](https://cohere.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/cohere.yaml).

<a id="composio"></a>

## Composio

Tool and integration layer for AI agents (hundreds of app connectors with managed auth), with llms.txt and a hosted MCP directory.

[Website](https://composio.dev) · [Source record](../data/providers/composio.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.composio.dev) · [MCP](https://mcp.composio.dev)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/composio.yaml).

### Service pricing

[Official pricing](https://composio.dev/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/composio.yaml).

<a id="datadog"></a>

## Datadog

Observability platform with a full REST API, llms.txt, documented OAuth for integrations, rate limits, and webhooks.

[Website](https://www.datadoghq.com) · [Source record](../data/providers/datadog.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.datadoghq.com) · [API](https://docs.datadoghq.com/api/latest/) · [CLI](https://github.com/DataDog/datadog-ci) · [MCP](https://docs.datadoghq.com/bits_ai/mcp_server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/datadog.yaml).

### Service pricing

[Official pricing](https://www.datadoghq.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/datadog.yaml).

<a id="deepgram"></a>

## Deepgram

Speech-to-text and voice AI API with a public OpenAPI spec, llms.txt, scoped API keys, and $200 free credit without a card.

[Website](https://deepgram.com) · [Source record](../data/providers/deepgram.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://developers.deepgram.com/docs) · [API](https://developers.deepgram.com/reference) · [SDK](https://developers.deepgram.com/docs/deepgram-sdks)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/deepgram.yaml).

### Service pricing

[Official pricing](https://deepgram.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/deepgram.yaml).

<a id="deepseek"></a>

## DeepSeek

OpenAI-compatible LLM API (DeepSeek-V3/R1) with transparent per-token pricing, a detailed changelog, and self-serve keys.

[Website](https://www.deepseek.com) · [Source record](../data/providers/deepseek.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://api-docs.deepseek.com)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/deepseek.yaml).

### Service pricing

[Official pricing](https://api-docs.deepseek.com/quick_start/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/deepseek.yaml).

<a id="discord"></a>

## Discord

Chat platform with a versioned bot/OAuth2 API, official OpenAPI spec (preview), webhooks, and documented rate limits.

[Website](https://discord.com) · [Source record](../data/providers/discord.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://discord.com/developers/docs/intro) · [API](https://discord.com/developers/docs/reference)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/discord.yaml).

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/discord.yaml).

<a id="dropbox"></a>

## Dropbox

File storage and sync with a scoped-OAuth HTTP API, self-serve app creation, and webhooks.

[Website](https://www.dropbox.com) · [Source record](../data/providers/dropbox.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://www.dropbox.com/developers/documentation) · [API](https://www.dropbox.com/developers/documentation/http/documentation) · [CLI](https://github.com/dropbox/dbxcli)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/dropbox.yaml).

### Service pricing

[Official pricing](https://www.dropbox.com/plans)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/dropbox.yaml).

<a id="duffel-flights"></a>

## Duffel Flights API

Flight API whose self-serve test environment must be distinguished from live account activation.

[Website](https://duffel.com/) · [Source record](../data/candidates/duffel-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://duffel.com/docs/api/overview/test-mode) · [API](https://duffel.com/guides/getting-started)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [test-api (api)](https://duffel.com/docs/api/overview/test-mode) | self_serve / unknown | Requirements not fully recorded; Duffel Airways test prices and schedules are fictitious. Test-token success cannot establish live fare access. |
| [live-api (api)](https://duffel.com/guides/getting-started) | unknown / unknown | Requires: email_verification, identity_verification; Verify email and submit individual or business details; Live permissions, market coverage and pricing must be checked using a real eligible account. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://duffel.com/guides/getting-started) — checked 2026-09-07
- [official_docs](https://duffel.com/docs/api/overview/test-mode) — checked 2026-09-07

<a id="e2b"></a>

## E2B

Isolated cloud sandboxes for running AI-generated code, with llms.txt, an official MCP server, and self-serve keys.

[Website](https://e2b.dev) · [Source record](../data/providers/e2b.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://e2b.dev/docs) · [CLI](https://e2b.dev/docs/cli) · [SDK](https://e2b.dev/docs/sdk-reference) · [MCP](https://github.com/e2b-dev/mcp-server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/e2b.yaml).

### Service pricing

[Official pricing](https://e2b.dev/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/e2b.yaml).

<a id="elevenlabs"></a>

## ElevenLabs

Voice AI (TTS, STT, agents) with a public OpenAPI spec, llms.txt, an official MCP server, and a free tier.

[Website](https://elevenlabs.io) · [Source record](../data/providers/elevenlabs.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://elevenlabs.io/docs) · [API](https://elevenlabs.io/docs/api-reference/introduction) · [MCP](https://github.com/elevenlabs/elevenlabs-mcp)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/elevenlabs.yaml).

### Service pricing

[Official pricing](https://elevenlabs.io/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/elevenlabs.yaml).

<a id="exa"></a>

## Exa

Search API built for AI — semantic web search, content retrieval, and research endpoints with an official MCP server.

[Website](https://exa.ai) · [Source record](../data/providers/exa.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.exa.ai) · [Docs](https://exa.ai/docs/reference/exa-mcp) · [MCP](https://mcp.exa.ai/mcp) · [API](https://exa.ai/docs/reference/search) · [API](https://docs.exa.ai/reference/getting-started) · [SDK](https://docs.exa.ai/sdks/typescript-sdk-specification) · [MCP](https://github.com/exa-labs/exa-mcp-server)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [public-mcp (mcp)](https://mcp.exa.ai/mcp) | self_serve / documented | Requirements not fully recorded; Public search MCP has a casual-use free plan; own key lifts limits. Additional agent_run tool requires authentication and separate usage charges; it is excluded from this pilot. API signup credits are not a quota guarantee for anonymous MCP. |
| [search-api (api)](https://exa.ai/docs/reference/search) | self_serve / documented | Requirements not fully recorded; Free account signup advertised at USD 20 initial credits plus USD 10/month; onboarding may be needed for part of initial credits. No payment method required. Anonymous MCP quota is separate. |

### Service pricing

[Official pricing](https://exa.ai/pricing)

- search-api: 20 USD / one_time (free_allowance; Published signup credits; some may require onboarding. Actual account award should be checked.)

- search-api: 10 USD / month (free_allowance; Free account monthly allowance, not anonymous MCP quota.)

### Task results

| Task | Tested route | Result | Date |
| --- | --- | --- | --- |
| I am upgrading a Python app to 3.13. Find out whether free threading is enabled by default, how to enable it, and what compatibility limits apply to existing C extensions, with official sources | public-mcp | [completed](../data/experiments/evaluations/codex-20260907T112257.401366Z-exa.json) | 2026-09-07 |
| I am upgrading a Python app to 3.13. Find out whether free threading is enabled by default, how to enable it, and what compatibility limits apply to existing C extensions, with official sources | search-api | [not_completed](../data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json) | 2026-09-07 |

### Sources

- [official_docs](https://exa.ai/docs/reference/exa-mcp) — checked 2026-09-07
- [official_site](https://exa.ai/pricing) — checked 2026-09-07
- [official_docs](https://exa.ai/docs/reference/search) — checked 2026-09-07

<a id="expedia-xap-flights"></a>

## Expedia XAP Flight Listings

Travel Redirect/XAP flight listings product whose new API applications are currently paused.

[Website](https://developers.expediagroup.com/xap-apis/api/start-guide/getting-started) · [Source record](../data/candidates/expedia-xap-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://developers.expediagroup.com/xap-apis/api/shopping-apis/flight-listings)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [flight-listings-api (api)](https://developers.expediagroup.com/xap-apis/api/shopping-apis/flight-listings) | paused / restricted | Requirements not fully recorded |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://developers.expediagroup.com/xap-apis/api/start-guide/getting-started) — checked 2026-09-07
- [official_docs](https://developers.expediagroup.com/xap-apis/api/shopping-apis/flight-listings) — checked 2026-09-07

<a id="fal"></a>

## fal.ai

Generative media platform (image, video, audio models) with queue/streaming APIs, an official CLI/serving framework, llms.txt, and self-serve keys.

[Website](https://fal.ai) · [Source record](../data/providers/fal.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://fal.ai/docs) · [API](https://fal.ai/docs/model-apis) · [CLI](https://github.com/fal-ai/fal)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/fal.yaml).

### Service pricing

[Official pricing](https://fal.ai/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/fal.yaml).

<a id="firecrawl"></a>

## Firecrawl

Web scraping and crawling API that turns websites into LLM-ready markdown, with an official MCP server.

[Website](https://www.firecrawl.dev) · [Source record](../data/providers/firecrawl.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.firecrawl.dev) · [API](https://docs.firecrawl.dev/features/search) · [API](https://docs.firecrawl.dev/api-reference/introduction) · [SDK](https://docs.firecrawl.dev/sdks/overview) · [MCP](https://docs.firecrawl.dev/mcp-server)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [public-search-api (api)](https://docs.firecrawl.dev/features/search) | self_serve / documented | Requirements not fully recorded; Current search docs explicitly permit starting without a key. Anonymous quota is unquantified; account free credits cannot be assumed for this route. |
| [account-search-api (api)](https://docs.firecrawl.dev/features/search) | self_serve / documented | Requirements not fully recorded; Search: 2 credits per 10 results; extra scraping can consume credits. |

### Service pricing

[Official pricing](https://www.firecrawl.dev/pricing)

- account-search-api: 1000 credits / month (free_allowance; Account Free plan; separate from anonymous access.)

### Task results

| Task | Tested route | Result | Date |
| --- | --- | --- | --- |
| I am upgrading a Python app to 3.13. Find out whether free threading is enabled by default, how to enable it, and what compatibility limits apply to existing C extensions, with official sources | public-search-api | [completed](../data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json) | 2026-09-07 |

### Sources

- [official_docs](https://docs.firecrawl.dev/features/search) — checked 2026-09-07
- [official_site](https://www.firecrawl.dev/pricing) — checked 2026-09-07

<a id="fireworks"></a>

## Fireworks AI

Fast open-model inference and fine-tuning with an OpenAI-compatible API, official firectl CLI, llms.txt, and published pricing.

[Website](https://fireworks.ai) · [Source record](../data/providers/fireworks.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.fireworks.ai) · [API](https://docs.fireworks.ai/api-reference/introduction) · [CLI](https://docs.fireworks.ai/tools-sdks/firectl/firectl)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/fireworks.yaml).

### Service pricing

[Official pricing](https://fireworks.ai/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/fireworks.yaml).

<a id="flight-mcp"></a>

## Flight MCP

Authenticated flight lookup and a separate, restricted public cache exposed through REST and MCP.

[Website](https://flight-mcp.com/) · [Source record](../data/candidates/flight-mcp.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://flight-mcp.com/docs) · [MCP](https://flight-mcp.com/docs)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [authenticated-api (api)](https://flight-mcp.com/docs) | self_serve / unknown | Requirements not fully recorded |
| [authenticated-mcp (mcp)](https://flight-mcp.com/docs) | self_serve / unknown | Requirements not fully recorded |
| [public-cache-api (api)](https://flight-mcp.com/docs) | self_serve / unknown | Requirements not fully recorded; Only 10 specified directed routes, one adult, economy, USD, en-US and US point of sale; per-date weekly cache refresh over 180 days. Does not trigger fresh queries for arbitrary routes. |
| [public-cache-mcp (mcp)](https://flight-mcp.com/docs) | self_serve / unknown | Requirements not fully recorded; Only 10 specified directed routes, one adult, economy, USD, en-US and US point of sale; per-date weekly cache refresh over 180 days. Does not trigger fresh queries for arbitrary routes. |

### Service pricing

- authenticated-api: 300 new_fetches / month (free_allowance; Authenticated free plan; cache hits do not consume this allowance.)

- authenticated-mcp: 300 new_fetches / month (free_allowance; Authenticated free plan; cache hits do not consume this allowance.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://flight-mcp.com/docs) — checked 2026-09-07
- [official_site](https://flight-mcp.com/pricing) — checked 2026-09-07

<a id="flightapi-io"></a>

## FlightAPI.io Flight Price API

Flight-price search for one-way, round-trip and multi-city itineraries, with credit-based usage.

[Website](https://www.flightapi.io/) · [Source record](../data/candidates/flightapi-io.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://www.flightapi.io/documentation/)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [price-api (api)](https://www.flightapi.io/documentation/) | self_serve / unknown | Requirements not fully recorded; Trial quota units, card requirements and new-account endpoint access still need verification. |

### Service pricing

- price-api: 2 credits / request (usage; One-way or round-trip flight-price query.)

- price-api: 5 credits / request (usage; Multi-city flight-price query.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://www.flightapi.io/documentation/getting-started/) — checked 2026-09-07
- [official_docs](https://www.flightapi.io/documentation/) — checked 2026-09-07
- [official_site](https://www.flightapi.io/) — checked 2026-09-07

<a id="fly-io"></a>

## Fly.io

Run full-stack apps and machines close to users, with a spec'd Machines API, scoped macaroon tokens, and official MCP docs.

[Website](https://fly.io) · [Source record](../data/providers/fly-io.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://fly.io/docs) · [API](https://fly.io/docs/machines/api/) · [CLI](https://fly.io/docs/flyctl/) · [MCP](https://fly.io/docs/mcp/)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/fly-io.yaml).

### Service pricing

[Official pricing](https://fly.io/docs/about/pricing/)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/fly-io.yaml).

<a id="gemini-api"></a>

## Gemini API

Google's Gemini model APIs via AI Studio, with generous free tier and documented API versioning.

[Website](https://ai.google.dev) · [Source record](../data/providers/gemini-api.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://ai.google.dev/gemini-api/docs) · [API](https://ai.google.dev/api) · [CLI](https://github.com/google-gemini/gemini-cli) · [SDK](https://ai.google.dev/gemini-api/docs/libraries)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/gemini-api.yaml).

### Service pricing

[Official pricing](https://ai.google.dev/gemini-api/docs/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/gemini-api.yaml).

<a id="github"></a>

## GitHub

Code hosting, collaboration, and automation with REST and GraphQL APIs, an official CLI, and an official MCP server.

[Website](https://github.com) · [Source record](../data/providers/github.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.github.com) · [API](https://docs.github.com/rest) · [CLI](https://cli.github.com) · [SDK](https://github.com/octokit) · [MCP](https://github.com/github/github-mcp-server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/github.yaml).

### Service pricing

[Official pricing](https://github.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/github.yaml).

<a id="gitlab"></a>

## GitLab

DevOps platform with REST and GraphQL APIs, scoped tokens, llms.txt, and an official CLI.

[Website](https://gitlab.com) · [Source record](../data/providers/gitlab.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.gitlab.com) · [API](https://docs.gitlab.com/api/rest/) · [CLI](https://gitlab.com/gitlab-org/cli) · [MCP](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/gitlab.yaml).

### Service pricing

[Official pricing](https://about.gitlab.com/pricing/)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/gitlab.yaml).

<a id="google-sheets"></a>

## Google Sheets

Online spreadsheets with a no-additional-cost API; Cloud project and OAuth setup are still prerequisites.

[Website](https://workspace.google.com/products/sheets/) · [Source record](../data/candidates/google-sheets.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://developers.google.com/workspace/sheets/api/guides/concepts)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [sheets-api (api)](https://developers.google.com/workspace/sheets/api/guides/concepts) | self_serve / unknown | Requirements not fully recorded; Configure a Cloud project and OAuth consent/client, then authorize selected account access.; Quickstart requires a Google account, Cloud project, enabled Sheets API and OAuth client/consent setup. Service accounts are another route, not assumed preconfigured. |

### Service pricing

- sheets-api: 0 USD / standard API usage (usage; Sheets API standard use has no additional cost; per-minute quotas apply.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://developers.google.com/workspace/sheets/api/quickstart/python) — checked 2026-09-08
- [official_docs](https://developers.google.com/workspace/sheets/api/limits) — checked 2026-09-08

<a id="grafana"></a>

## Grafana (Grafana Cloud)

Observability platform (dashboards, metrics, logs, traces) with a documented HTTP API, official MCP server, llms.txt, and a standing free cloud tier.

[Website](https://grafana.com) · [Source record](../data/providers/grafana.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://grafana.com/docs) · [API](https://grafana.com/docs/grafana/latest/developers/http_api/) · [MCP](https://github.com/grafana/mcp-grafana)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/grafana.yaml).

### Service pricing

[Official pricing](https://grafana.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/grafana.yaml).

<a id="grist"></a>

## Grist

Hosted relational spreadsheets with a free personal site, REST API and official MCP.

[Website](https://www.getgrist.com/) · [Source record](../data/candidates/grist.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://support.getgrist.com/api/) · [MCP](https://docs.getgrist.com/api/mcp) · [SDK](https://pypi.org/project/grist-api/) · [SDK](https://www.npmjs.com/package/grist-api)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [rest-api (api)](https://support.getgrist.com/api/) | self_serve / documented | Requirements not fully recorded; Sign in and generate an API key in account settings.; Account API key grants the user’s existing access. Use a separate free test account; personal site is freely available. |
| [hosted-mcp (mcp)](https://docs.getgrist.com/api/mcp) | self_serve / documented | Requirements not fully recorded; Hosted server accepts API keys or interactive OAuth; available on all plans. Calls share the API pool. |
| [python-sdk (sdk)](https://pypi.org/project/grist-api/) | unknown / unknown | Requirements not fully recorded; Official Python client linked by Grist REST API guide; SDK installation does not remove account permission requirements. |
| [javascript-sdk (sdk)](https://www.npmjs.com/package/grist-api) | unknown / unknown | Requirements not fully recorded; Official JavaScript/TypeScript client linked by Grist REST API guide; npm page fetch returned 403 during public research, not a service failure. |

### Service pricing

- rest-api: 5000 records / document (free_allowance; Hosted Free plan; API quota must also be checked for the selected site.)

### Task results

| Task | Tested route | Result | Date |
| --- | --- | --- | --- |
| Turn a book-club planning meeting's action items into an online task table, update their progress, and tell me what remains unfinished | rest-api | [completed](../data/experiments/evaluations/codex-20260908T032113.556233Z-grist.json) | 2026-09-08 |
| Turn the action items in these book-club meeting notes into an online task table, give me its link, and tell me what is still unfinished and when each item is due | rest-api | [completed](../data/experiments/evaluations/codex-20260908T035504.472694Z-grist.json) | 2026-09-08 |

### Sources

- [official_docs](https://support.getgrist.com/api/) — checked 2026-09-08
- [official_docs](https://support.getgrist.com/rest-api/) — checked 2026-09-08
- [official_site](https://www.getgrist.com/pricing/) — checked 2026-09-08
- [official_docs](https://support.getgrist.com/mcp/) — checked 2026-09-08

<a id="groq"></a>

## Groq

Ultra-low-latency LLM inference with an OpenAI-compatible API, llms.txt, and self-serve keys with a free tier.

[Website](https://groq.com) · [Source record](../data/providers/groq.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://console.groq.com/docs) · [API](https://console.groq.com/docs/api-reference) · [SDK](https://console.groq.com/docs/libraries)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/groq.yaml).

### Service pricing

[Official pricing](https://groq.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/groq.yaml).

<a id="hugging-face"></a>

## Hugging Face

Model hub and inference platform with fine-grained tokens, OAuth, an official MCP server, and a full Hub API.

[Website](https://huggingface.co) · [Source record](../data/providers/hugging-face.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://huggingface.co/docs) · [API](https://huggingface.co/docs/hub/api) · [CLI](https://huggingface.co/docs/huggingface_hub/guides/cli) · [SDK](https://huggingface.co/docs/huggingface_hub) · [MCP](https://huggingface.co/mcp)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/hugging-face.yaml).

### Service pricing

[Official pricing](https://huggingface.co/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/hugging-face.yaml).

<a id="ignav"></a>

## Ignav Flights

Flight search and purchase-link API with email signup and an official MCP; individual eligibility remains untested.

[Website](https://ignav.com/) · [Source record](../data/candidates/ignav.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://ignav.com/docs) · [Web](https://ignav.com/playground) · [API](https://ignav.com/docs) · [MCP](https://ignav.com/docs/mcp)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [public-playground (web)](https://ignav.com/playground) | self_serve / unknown | Requirements not fully recorded; Public trial UI; limits and selectable markets may differ from the customer API. Experimental observations remain separate from catalog claims. |
| [flights-api (api)](https://ignav.com/docs) | self_serve / unknown | Requires: email_verification; Verify signup email |
| [official-mcp (mcp)](https://ignav.com/docs/mcp) | unknown / unknown | Requirements not fully recorded; Uses Ignav credentials. The API route records published account pricing; MCP tool billing and coverage need confirmation. |

### Service pricing

- flights-api: 1000 requests / one_time (free_allowance; One-time account allowance, not monthly.)

- flights-api: 2 USD / 1000 successful requests (usage; Successful HTTP 200 responses; search and booking-link retrieval are separate calls.)

### Task results

| Task | Tested route | Result | Date |
| --- | --- | --- | --- |
| Find flights from Milan to the Netherlands on September 25 | public-playground | [completed](../data/experiments/evaluations/codex-20260907T083644.877057Z-ignav.json) | 2026-09-07 |

### Sources

- [official_site](https://ignav.com/playground) — checked 2026-09-07
- [official_site](https://ignav.com/signup) — checked 2026-09-07
- [official_site](https://ignav.com/pricing) — checked 2026-09-07
- [official_docs](https://ignav.com/docs) — checked 2026-09-07
- [official_docs](https://ignav.com/docs/mcp) — checked 2026-09-07
- [official_docs](https://ignav.com/docs/amadeus-self-service-shutdown) — checked 2026-09-07

<a id="jina"></a>

## Jina AI

Search-foundation APIs (Reader for URL-to-markdown, embeddings, reranker, deep search) with an official remote MCP server, an agent-targeted llms.txt, and a keyless trial path.

[Website](https://jina.ai) · [Source record](../data/providers/jina.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.jina.ai) · [API](https://docs.jina.ai) · [MCP](https://github.com/jina-ai/MCP)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/jina.yaml).

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/jina.yaml).

<a id="kayak-affiliate"></a>

## KAYAK Affiliate API

Affiliate flight APIs with a business application and an optional requested sandbox.

[Website](https://affiliates.kayak.com/) · [Source record](../data/candidates/kayak-affiliate.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://developers.kayak.com/)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [affiliate-api (api)](https://developers.kayak.com/) | application / unknown | Requires: company, website, approval; Submit business application for review |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_site](https://affiliates.kayak.com/) — checked 2026-09-07
- [official_docs](https://developers.kayak.com/) — checked 2026-09-07

<a id="kiwi"></a>

## Kiwi.com

Flight search through a publicized MCP path and the separately gated Tequila partnership API.

[Website](https://www.kiwi.com/) · [Source record](../data/candidates/kiwi.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://www.kiwi.com/en/pages/mcp/) · [MCP](https://mcp.kiwi.com) · [API](https://media.kiwi.com/articles-and-interviews/better-for-business-kiwi-com-takes-a-new-approach-to-partnerships/)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [search-mcp (mcp)](https://mcp.kiwi.com) | self_serve / unknown | Requirements not fully recorded |
| [tequila-api (api)](https://media.kiwi.com/articles-and-interviews/better-for-business-kiwi-com-takes-a-new-approach-to-partnerships/) | invite_only / unknown | Requires: invitation; Keep invitation-only Tequila separate from the search MCP. Current endpoints and task coverage need further research. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

| Task | Tested route | Result | Date |
| --- | --- | --- | --- |
| Find flights from Milan to the Netherlands on September 25 | search-mcp | [completed](../data/experiments/evaluations/codex-20260907T083627.884537Z-kiwi.json) | 2026-09-07 |
| Find flights from Milan to the Netherlands on September 25 | search-mcp | [invalid_run](../data/experiments/evaluations/codex-20260907T091621.435575Z-kiwi.json) | 2026-09-07 |
| Find flights from Milan to the Netherlands on September 25 | search-mcp | [completed](../data/experiments/evaluations/codex-20260907T092329.724439Z-kiwi.json) | 2026-09-07 |

### Sources

- [official_docs](https://www.kiwi.com/en/pages/mcp/) — checked 2026-09-07
- [official_announcement](https://media.kiwi.com/articles-and-interviews/better-for-business-kiwi-com-takes-a-new-approach-to-partnerships/) — checked 2026-09-07

<a id="lark"></a>

## Lark

Collaboration suite (messaging, docs, calendar) with an open platform, llms.txt, an official CLI with 200+ commands and agent skills, and an official OpenAPI MCP server.

[Website](https://www.larksuite.com) · [Source record](../data/providers/lark.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://open.larksuite.com/document/home/index) · [API](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create) · [CLI](https://github.com/larksuite/cli) · [MCP](https://github.com/larksuite/lark-openapi-mcp) · [API](https://open.larksuite.com/document/server-docs/getting-started/server-api-list)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [base-api (api)](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create) | self_serve / unknown | Requirements not fully recorded; Requires a platform app, authorized identity and Base scopes/resource permissions. Ordinary-person onboarding from a fresh account is not tested. |
| [official-cli (cli)](https://github.com/larksuite/cli) | self_serve / unknown | Requirements not fully recorded; Official CLI covers Base and supports individuals. Account signup, app creation and permission setup still need separate verification. |
| [official-mcp (mcp)](https://github.com/larksuite/lark-openapi-mcp) | self_serve / unknown | Requirements not fully recorded; Local official MCP package uses platform app credentials; identity and tenant domains must match. |

### Service pricing

[Official pricing](https://www.larksuite.com/en_us/plans)

- base-api: 2000 rows / table (free_allowance; Starter Base table limit; access still depends on tenant/app scopes.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create.md) — checked 2026-09-08
- [official_repo](https://github.com/larksuite/cli) — checked 2026-09-08
- [official_repo](https://github.com/larksuite/lark-openapi-mcp) — checked 2026-09-08
- [official_site](https://www.larksuite.com/en_us/plans) — checked 2026-09-08

<a id="lemonsqueezy"></a>

## Lemon Squeezy

Merchant-of-record payments for digital products/SaaS with a JSON:API REST API, documented test mode, and self-serve keys.

[Website](https://www.lemonsqueezy.com) · [Source record](../data/providers/lemonsqueezy.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.lemonsqueezy.com) · [API](https://docs.lemonsqueezy.com/api)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/lemonsqueezy.yaml).

### Service pricing

[Official pricing](https://www.lemonsqueezy.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/lemonsqueezy.yaml).

<a id="letsfg"></a>

## LetsFG Personal Flight Search

Personal flight search through MCP, CLI and SDKs, with a human payment-method authorization step.

[Website](https://letsfg.co/) · [Source record](../data/candidates/letsfg.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[MCP](https://letsfg.co/for-agents) · [CLI](https://github.com/letsfg/letsfg) · [SDK](https://github.com/letsfg/letsfg)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [personal-mcp (mcp)](https://letsfg.co/for-agents) | unknown / documented | Requires: payment_method; Complete browser consent and connect a payment method |
| [personal-cli (cli)](https://github.com/letsfg/letsfg) | unknown / unknown | Requirements not fully recorded; Official repository advertises this interface (Python/JS for SDK). Installation version, current auth compatibility and route-specific gates remain unverified due to documentation drift. |
| [personal-sdk (sdk)](https://github.com/letsfg/letsfg) | unknown / unknown | Requirements not fully recorded; Official repository advertises this interface (Python/JS for SDK). Installation version, current auth compatibility and route-specific gates remain unverified due to documentation drift. |

### Service pricing

- personal-mcp: 0 USD / search (usage; Personal flight-search claim only; excludes booking, payment authorization and the separate Developer API.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://letsfg.co/for-agents) — checked 2026-09-07
- [official_repo](https://github.com/letsfg/letsfg) — checked 2026-09-07

<a id="linear"></a>

## Linear

Issue tracking and product planning with a GraphQL API, llms.txt, an official MCP server, and webhooks.

[Website](https://linear.app) · [Source record](../data/providers/linear.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://linear.app/developers) · [MCP](https://linear.app/docs/mcp)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/linear.yaml).

### Service pricing

[Official pricing](https://linear.app/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/linear.yaml).

<a id="lufthansa-partner"></a>

## Lufthansa Partner Fare API

Lufthansa fare methods are partner-scoped; the developer portal currently pauses new Open API registrations.

[Website](https://developer.lufthansa.com/page) · [Source record](../data/candidates/lufthansa-partner.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://developer.lufthansa.com/page) · [API](https://developer.lufthansa.com/docs/read/api_partner/offers)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [open-api-registration (api)](https://developer.lufthansa.com/page) | paused / unknown | Requirements not fully recorded; Public schedule and status APIs are not evidence of consumer fare-search capability. |
| [partner-offers-api (api)](https://developer.lufthansa.com/docs/read/api_partner/offers) | unknown / unknown | Requirements not fully recorded; Public schedule/status APIs do not establish fare-search access. A readable registration form does not override the pause notice. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_announcement](https://developer.lufthansa.com/page) — checked 2026-09-07
- [official_docs](https://developer.lufthansa.com/docs) — checked 2026-09-07
- [official_docs](https://developer.lufthansa.com/docs/read/api_partner/offers) — checked 2026-09-07

<a id="luma"></a>

## Luma AI (Dream Machine)

Dream Machine video and image generation via the Luma API, with llms.txt and published API pricing.

[Website](https://lumalabs.ai) · [Source record](../data/providers/luma.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.lumalabs.ai) · [API](https://docs.lumalabs.ai/reference)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/luma.yaml).

### Service pricing

[Official pricing](https://lumalabs.ai/api/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/luma.yaml).

<a id="mem0"></a>

## Mem0

Memory layer for AI agents (hosted platform + open-source), with REST API, llms.txt, and the official OpenMemory MCP server.

[Website](https://mem0.ai) · [Source record](../data/providers/mem0.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.mem0.ai) · [API](https://docs.mem0.ai/api-reference) · [MCP](https://docs.mem0.ai/openmemory/overview)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/mem0.yaml).

### Service pricing

[Official pricing](https://mem0.ai/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/mem0.yaml).

<a id="minimax"></a>

## MiniMax

MiniMax text, speech, video and music models via the international platform API, with an official MCP server.

[Website](https://platform.minimax.io) · [Source record](../data/providers/minimax.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://platform.minimax.io/docs) · [API](https://platform.minimax.io/docs/api-reference) · [MCP](https://github.com/MiniMax-AI/MiniMax-MCP)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/minimax.yaml).

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/minimax.yaml).

<a id="mistral"></a>

## Mistral AI

European LLM provider (La Plateforme) with llms.txt, an open OpenAPI-based docs repo, a free experiment tier, and self-serve keys.

[Website](https://mistral.ai) · [Source record](../data/providers/mistral.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.mistral.ai) · [API](https://docs.mistral.ai/api) · [SDK](https://docs.mistral.ai/getting-started/clients)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/mistral.yaml).

### Service pricing

[Official pricing](https://mistral.ai/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/mistral.yaml).

<a id="modal"></a>

## Modal

Serverless compute for Python with first-class Sandboxes for agent code execution, llms.txt, and an official CLI.

[Website](https://modal.com) · [Source record](../data/providers/modal.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://modal.com/docs) · [API](https://modal.com/docs/reference) · [CLI](https://modal.com/docs/reference/cli)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/modal.yaml).

### Service pricing

[Official pricing](https://modal.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/modal.yaml).

<a id="mongodb-atlas"></a>

## MongoDB Atlas

Managed MongoDB with a versioned Admin API, published OpenAPI spec, llms.txt, official CLI and MCP server.

[Website](https://www.mongodb.com/products/platform/atlas-database) · [Source record](../data/providers/mongodb-atlas.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://www.mongodb.com/docs/atlas/) · [API](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/) · [CLI](https://www.mongodb.com/docs/atlas/cli/) · [SDK](https://www.mongodb.com/docs/drivers/) · [MCP](https://github.com/mongodb-js/mongodb-mcp-server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/mongodb-atlas.yaml).

### Service pricing

[Official pricing](https://www.mongodb.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/mongodb-atlas.yaml).

<a id="moonshot"></a>

## Moonshot AI (Kimi)

Kimi models (K2 line) via an OpenAI-compatible API on the international Kimi platform, with an official terminal CLI agent (kimi-cli).

[Website](https://platform.kimi.ai) · [Source record](../data/providers/moonshot.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://platform.kimi.ai/docs) · [API](https://platform.kimi.ai/docs/api/chat) · [CLI](https://github.com/MoonshotAI/kimi-cli)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/moonshot.yaml).

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/moonshot.yaml).

<a id="n8n"></a>

## n8n

Workflow automation platform with native AI/agent nodes, a public REST API, official hosted MCP server, CLI, and llms.txt; fair-code and self-hostable.

[Website](https://n8n.io) · [Source record](../data/providers/n8n.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.n8n.io) · [API](https://docs.n8n.io/api/) · [CLI](https://docs.n8n.io/hosting/cli-commands/) · [MCP](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/n8n.yaml).

### Service pricing

[Official pricing](https://n8n.io/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/n8n.yaml).

<a id="neon"></a>

## Neon

Serverless Postgres with instant branching, a full management API, official MCP server, and agent-oriented docs.

[Website](https://neon.com) · [Source record](../data/providers/neon.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://neon.com/docs) · [API](https://neon.new/) · [API](https://api-docs.neon.tech) · [CLI](https://neon.com/docs/reference/neon-cli) · [MCP](https://github.com/neondatabase/mcp-server-neon)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [ephemeral-api (api)](https://neon.new/) | unknown / documented | Requirements not fully recorded; No-account, 72-hour ephemeral hosted Postgres. Tests can establish short-term persistence only; this is not a permanent free production database. Connection strings and claim URLs are private credentials. |

### Service pricing

[Official pricing](https://neon.com/pricing)

### Task results

| Task | Tested route | Result | Date |
| --- | --- | --- | --- |
| Prepare a separate remote database for my personal todo app and verify adding, updating and reading todos after reconnecting | ephemeral-api | [completed](../data/experiments/evaluations/codex-20260907T112258.549053Z-neon.json) | 2026-09-07 |

### Sources

- [official_site](https://neon.new/) — checked 2026-09-07
- [official_announcement](https://neon.com/blog/neon-launchpad) — checked 2026-09-07

<a id="netlify"></a>

## Netlify

Web platform for deploying sites and functions, with an OpenAPI-specified API, llms.txt, official CLI and MCP server.

[Website](https://www.netlify.com) · [Source record](../data/providers/netlify.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.netlify.com) · [API](https://open-api.netlify.com) · [CLI](https://docs.netlify.com/cli/get-started/) · [MCP](https://docs.netlify.com/welcome/build-with-ai/netlify-mcp-server/)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/netlify.yaml).

### Service pricing

[Official pricing](https://www.netlify.com/pricing/)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/netlify.yaml).

<a id="notion"></a>

## Notion

Connected workspace with a versioned REST API, capability-scoped integrations, llms.txt, and an official MCP server.

[Website](https://www.notion.com) · [Source record](../data/providers/notion.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://developers.notion.com) · [API](https://developers.notion.com/reference/intro) · [SDK](https://github.com/makenotion/notion-sdk-js) · [CLI](https://developers.notion.com/cli/get-started/overview) · [MCP](https://mcp.notion.com/mcp) · [MCP](https://developers.notion.com/docs/mcp)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [rest-api (api)](https://developers.notion.com/reference/intro) | self_serve / documented | Requirements not fully recorded; Create internal connection and grant only the test page, or create a PAT in a dedicated test workspace.; Internal connection requires workspace owner creation and explicit page sharing; PAT acts with creator permissions in the selected workspace. Free-plan PAT creation is restricted to workspace owners; being a free member alone is insufficient. |
| [javascript-sdk (sdk)](https://github.com/makenotion/notion-sdk-js) | self_serve / unknown | Requirements not fully recorded; Official client library over the REST API; credentials and resource grants remain necessary. |
| [official-cli (cli)](https://developers.notion.com/cli/get-started/overview) | self_serve / unknown | Requirements not fully recorded; Official CLI discovered in current docs; measure separately from raw REST. |
| [hosted-mcp (mcp)](https://mcp.notion.com/mcp) | self_serve / unknown | Requirements not fully recorded; Official hosted MCP requires interactive OAuth. Token-based open-source server is no longer actively maintained. |

### Service pricing

[Official pricing](https://www.notion.com/pricing)

- rest-api: 0 USD / month (free_allowance; Free workspace subscription; API limits and resource permissions still apply.)

### Task results

| Task | Tested route | Result | Date |
| --- | --- | --- | --- |
| Turn a book-club planning meeting's action items into an online task table, update their progress, and tell me what remains unfinished | rest-api | [completed](../data/experiments/evaluations/codex-20260908T032850.330773Z-notion.json) | 2026-09-08 |
| Turn the action items in these book-club meeting notes into an online task table, give me its link, and tell me what is still unfinished and when each item is due | rest-api | [completed](../data/experiments/evaluations/codex-20260908T035504.906378Z-notion.json) | 2026-09-08 |

### Sources

- [official_docs](https://developers.notion.com/reference/intro) — checked 2026-09-08
- [official_docs](https://developers.notion.com/guides/get-started/authorization) — checked 2026-09-08
- [official_docs](https://developers.notion.com/guides/get-started/personal-access-tokens) — checked 2026-09-08
- [official_site](https://www.notion.com/pricing) — checked 2026-09-08
- [official_repo](https://github.com/makenotion/notion-sdk-js) — checked 2026-09-08
- [official_docs](https://developers.notion.com/cli/get-started/overview) — checked 2026-09-08
- [official_docs](https://developers.notion.com/guides/mcp/get-started-with-mcp) — checked 2026-09-08

<a id="openai"></a>

## OpenAI

GPT model APIs with an official OpenAPI spec, agents guides, and a large SDK ecosystem.

[Website](https://openai.com) · [Source record](../data/providers/openai.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://developers.openai.com/api/docs) · [API](https://platform.openai.com/docs/api-reference) · [SDK](https://platform.openai.com/docs/libraries)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/openai.yaml).

### Service pricing

[Official pricing](https://platform.openai.com/docs/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/openai.yaml).

<a id="openrouter"></a>

## OpenRouter

Unified OpenAI-compatible API over hundreds of models from many labs, with one key, per-model pricing, automatic fallbacks, and an llms.txt.

[Website](https://openrouter.ai) · [Source record](../data/providers/openrouter.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://openrouter.ai/docs) · [API](https://openrouter.ai/docs/api-reference/overview)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/openrouter.yaml).

### Service pricing

[Official pricing](https://openrouter.ai/models)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/openrouter.yaml).

<a id="paas-build"></a>

## paas.build

Agent-native payment facilitator (the AI-builder product of UniPaaS, FCA-authorised No. 929994) — opens a real merchant account via progressive KYB and creates checkouts through MCP or REST.

[Website](https://paas.build) · [Source record](../data/candidates/paas-build.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://paas.build/agents) · [MCP](https://github.com/UNIPaaS/paas-build-mcp)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/candidates/paas-build.yaml).

### Service pricing

[Official pricing](https://paas.build/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/candidates/paas-build.yaml).

<a id="paddle"></a>

## Paddle

Merchant-of-record billing platform with a versioned API, full sandbox, llms.txt, and webhooks.

[Website](https://www.paddle.com) · [Source record](../data/providers/paddle.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://developer.paddle.com) · [API](https://developer.paddle.com/api-reference/overview) · [MCP](https://github.com/PaddleHQ/paddle-mcp-server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/paddle.yaml).

### Service pricing

[Official pricing](https://www.paddle.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/paddle.yaml).

<a id="perplexity"></a>

## Perplexity API

Sonar API for web-grounded answers and search, with llms.txt, an official MCP server, and documented usage tiers.

[Website](https://www.perplexity.ai) · [Source record](../data/providers/perplexity.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.perplexity.ai) · [MCP](https://github.com/ppl-ai/modelcontextprotocol)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/perplexity.yaml).

### Service pricing

[Official pricing](https://docs.perplexity.ai/getting-started/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/perplexity.yaml).

<a id="pinecone"></a>

## Pinecone

Managed vector database for search and RAG, with llms.txt, an official MCP server, and self-serve keys.

[Website](https://www.pinecone.io) · [Source record](../data/providers/pinecone.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.pinecone.io) · [API](https://docs.pinecone.io/reference/api/introduction) · [CLI](https://github.com/pinecone-io/cli) · [MCP](https://docs.pinecone.io/guides/operations/mcp-server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/pinecone.yaml).

### Service pricing

[Official pricing](https://www.pinecone.io/pricing/)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/pinecone.yaml).

<a id="planetscale"></a>

## PlanetScale

PostgreSQL single-node plans start at USD 5/month. No free writable database allowance verified; not provisioned in this no-payment round. Public pricing SQL is read-only and does not meet the task.

[Website](https://planetscale.com/) · [Source record](../data/candidates/planetscale.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[CLI](https://planetscale.com/docs/cli)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [database-cli (cli)](https://planetscale.com/docs/cli) | self_serve / documented | Requirements not fully recorded; PostgreSQL single-node plans start at USD 5/month. No free writable database allowance verified; not provisioned in this no-payment round. Public pricing SQL is read-only and does not meet the task. |

### Service pricing

- database-cli: 5 USD / month (minimum_spend; Postgres single-node starting plan; configuration, region and other resources may cost more.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://planetscale.com/docs/cli) — checked 2026-09-07
- [official_site](https://planetscale.com/pricing) — checked 2026-09-07

<a id="postman"></a>

## Postman

API development platform with a public Postman API, llms.txt, official CLI, and self-serve keys.

[Website](https://www.postman.com) · [Source record](../data/providers/postman.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://learning.postman.com) · [API](https://learning.postman.com/docs/developer/postman-api/intro-api/) · [CLI](https://learning.postman.com/docs/postman-cli/postman-cli-overview/) · [MCP](https://github.com/postmanlabs/postman-mcp-server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/postman.yaml).

### Service pricing

[Official pricing](https://www.postman.com/pricing/)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/postman.yaml).

<a id="qdrant"></a>

## Qdrant

Open-source vector database with a managed cloud, llms.txt, an official MCP server, and a free cluster tier.

[Website](https://qdrant.tech) · [Source record](../data/providers/qdrant.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://qdrant.tech/documentation) · [API](https://api.qdrant.tech) · [SDK](https://qdrant.tech/documentation/interfaces) · [MCP](https://github.com/qdrant/mcp-server-qdrant)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/qdrant.yaml).

### Service pricing

[Official pricing](https://qdrant.tech/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/qdrant.yaml).

<a id="railway"></a>

## Railway

App/database hosting with a public GraphQL API, official CLI, llms.txt, and usage-based pricing.

[Website](https://railway.com) · [Source record](../data/providers/railway.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.railway.com) · [API](https://docs.railway.com/reference/public-api) · [CLI](https://github.com/railwayapp/cli)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/railway.yaml).

### Service pricing

[Official pricing](https://railway.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/railway.yaml).

<a id="redis"></a>

## Redis (Redis Cloud)

In-memory data platform for caching, vector search and real-time apps; Redis Cloud has a REST management API, official MCP server, redis-cli, and llms.txt.

[Website](https://redis.io) · [Source record](../data/providers/redis.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://redis.io/docs/latest) · [API](https://redis.io/docs/latest/operate/rc/api/) · [CLI](https://redis.io/docs/latest/develop/tools/cli/) · [MCP](https://github.com/redis/mcp-redis)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/redis.yaml).

### Service pricing

[Official pricing](https://redis.io/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/redis.yaml).

<a id="render"></a>

## Render

Cloud hosting for web services, static sites and databases with a REST API, official CLI, official MCP server, and llms.txt.

[Website](https://render.com) · [Source record](../data/providers/render.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://render.com/docs) · [API](https://api-docs.render.com/reference/introduction) · [CLI](https://github.com/render-oss/cli) · [MCP](https://github.com/render-oss/render-mcp-server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/render.yaml).

### Service pricing

[Official pricing](https://render.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/render.yaml).

<a id="replicate"></a>

## Replicate

Run and fine-tune open-source models via a simple predictions API, with llms.txt, webhooks, and an official CLI.

[Website](https://replicate.com) · [Source record](../data/providers/replicate.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://replicate.com/docs) · [API](https://replicate.com/docs/reference/http) · [CLI](https://github.com/replicate/cli) · [SDK](https://replicate.com/docs/reference/client-libraries)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/replicate.yaml).

### Service pricing

[Official pricing](https://replicate.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/replicate.yaml).

<a id="resend"></a>

## Resend

Email API for developers with test mode, scoped API keys, idempotency support, and an official MCP server.

[Website](https://resend.com) · [Source record](../data/providers/resend.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://resend.com/docs) · [API](https://resend.com/docs/api-reference/introduction) · [SDK](https://resend.com/docs/sdks) · [MCP](https://github.com/resend/mcp-send-email)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/resend.yaml).

### Service pricing

[Official pricing](https://resend.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/resend.yaml).

<a id="sabre-air"></a>

## Sabre Air APIs

Air API workflows with assigned credentials, plus a separately researched Agentic API/MCP lead.

[Website](https://developer.sabre.com/) · [Source record](../data/candidates/sabre-air.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://github.com/SabreDevStudio/SabreAPIsWorkflows/blob/master/SabreAPIsTestSuites/README.md) · [MCP](https://developer.sabre.com/)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [air-workflow-api (api)](https://github.com/SabreDevStudio/SabreAPIsWorkflows/blob/master/SabreAPIsTestSuites/README.md) | application / unknown | Requirements not fully recorded; Contact sales to obtain EPR, IPCC and password; This older workflow is evidence for its own credential path only. |
| [agentic-mcp-lead (mcp)](https://developer.sabre.com/) | unknown / unknown | Requirements not fully recorded; Current developer homepage advertises Agentic API/MCP. Exact product, tools and onboarding need research; do not copy legacy workflow gates onto it. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_repo](https://github.com/SabreDevStudio/SabreAPIsWorkflows/blob/master/SabreAPIsTestSuites/README.md) — checked 2026-09-07
- [official_site](https://developer.sabre.com/) — checked 2026-09-07

<a id="scrapingdog-flights"></a>

## Scrapingdog Google Flights API

Google Flights extraction endpoint charged in platform credits rather than one credit per flight search.

[Website](https://www.scrapingdog.com/) · [Source record](../data/candidates/scrapingdog-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://www.scrapingdog.com/documentation/google-flights-api/)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [flights-api (api)](https://www.scrapingdog.com/documentation/google-flights-api/) | self_serve / unknown | Requirements not fully recorded |

### Service pricing

- flights-api: 5 credits / flight request (usage; Do not equate platform free credits to the same number of flight searches.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://www.scrapingdog.com/documentation/google-flights-api/) — checked 2026-09-07
- [official_docs](https://www.scrapingdog.com/documentation/) — checked 2026-09-07

<a id="searchapi"></a>

## SearchApi Google Flights

Google Flights extraction API and a hosted MCP integration supporting token or browser authorization.

[Website](https://www.searchapi.io/) · [Source record](../data/candidates/searchapi.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://www.searchapi.io/docs/google-flights-api) · [Docs](https://www.searchapi.io/integrations/mcp) · [MCP](https://www.searchapi.io/mcp)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [google-flights-api (api)](https://www.searchapi.io/docs/google-flights-api) | self_serve / unknown | Requirements not fully recorded |
| [hosted-mcp (mcp)](https://www.searchapi.io/mcp) | unknown / unknown | Requirements not fully recorded; Authorize in browser when choosing OAuth; Supports browser OAuth or a separate MCP token. Which tools expose the flight task remains untested. |

### Service pricing

- google-flights-api: 100 requests / trial (free_allowance; Product-page trial; whether shared across engines requires account verification.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://www.searchapi.io/docs/google-flights-api) — checked 2026-09-07
- [official_site](https://www.searchapi.io/google-flights-api) — checked 2026-09-07
- [official_docs](https://www.searchapi.io/integrations/mcp) — checked 2026-09-07

<a id="sentry"></a>

## Sentry

Error monitoring and performance tracing with llms.txt, an official MCP server, scoped auth tokens, and a full API.

[Website](https://sentry.io) · [Source record](../data/providers/sentry.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.sentry.io) · [API](https://docs.sentry.io/api/) · [CLI](https://docs.sentry.io/cli/) · [SDK](https://docs.sentry.io/platforms/) · [MCP](https://docs.sentry.io/product/sentry-mcp/)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/sentry.yaml).

### Service pricing

[Official pricing](https://sentry.io/pricing/)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/sentry.yaml).

<a id="serpapi"></a>

## SerpApi

Real-time JSON API for Google and other search engines' results, with an official MCP server, llms.txt, and a free monthly quota.

[Website](https://serpapi.com) · [Source record](../data/providers/serpapi.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://serpapi.com/search-api) · [API](https://serpapi.com/google-flights-api) · [MCP](https://github.com/serpapi/serpapi-mcp) · [API](https://serpapi.com/search-api)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [google-flights-api (api)](https://serpapi.com/google-flights-api) | self_serve / unknown | Requirements not fully recorded; A third-party Google Flights data service. Not a Google-operated API. |
| [official-mcp (mcp)](https://github.com/serpapi/serpapi-mcp) | unknown / unknown | Requirements not fully recorded; Official to SerpApi. Flight tool coverage and access gates are unconfirmed; do not inherit API-route results. |
| [web-search-api (api)](https://serpapi.com/search-api) | self_serve / unknown | Requirements not fully recorded; Separate from Google Flights API. Existing flight evaluations do not establish web search performance. |

### Service pricing

[Official pricing](https://serpapi.com/pricing)

- google-flights-api: 250 searches / month (free_allowance; Platform search allowance; flight-endpoint entitlement and shared usage untested.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://serpapi.com/google-flights-api) — checked 2026-09-07
- [official_site](https://serpapi.com/users/sign_up) — checked 2026-09-07
- [official_site](https://serpapi.com/pricing) — checked 2026-09-07
- [official_repo](https://github.com/serpapi/serpapi-mcp) — checked 2026-09-07
- [official_docs](https://serpapi.com/search-api) — checked 2026-09-07

<a id="serper"></a>

## Serper

Google results API with signup trial queries; actual account flow and authentication remain untested.

[Website](https://serper.dev/) · [Source record](../data/candidates/serper.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://serper.dev/)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [search-api (api)](https://serper.dev/) | self_serve / documented | Requirements not fully recorded; Google results API with signup trial queries; actual account flow and authentication remain untested. |

### Service pricing

- search-api: 2500 queries / one_time (free_allowance; Advertised initial free queries, no monthly renewal claimed.)

### Task results

Not yet task-tested.

### Sources

- [official_site](https://serper.dev/) — checked 2026-09-07

<a id="shopify"></a>

## Shopify

Commerce platform with versioned GraphQL APIs, llms.txt, official MCP docs, access-scoped tokens, free development stores, and a CLI.

[Website](https://www.shopify.com) · [Source record](../data/providers/shopify.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://shopify.dev/docs) · [API](https://shopify.dev/docs/api) · [CLI](https://shopify.dev/docs/api/shopify-cli) · [MCP](https://shopify.dev/docs/apps/build/storefront-mcp)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/shopify.yaml).

### Service pricing

[Official pricing](https://www.shopify.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/shopify.yaml).

<a id="skootle-google-flights"></a>

## Skootle Google Flights Scraper

A Skootle-published flight-scraping Actor hosted on Apify, billed by startup and output records.

[Website](https://apify.com/skootle/google-flights-scraper) · [Source record](../data/candidates/skootle-google-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://apify.com/skootle/google-flights-scraper)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [apify-actor-api (api)](https://apify.com/skootle/google-flights-scraper) | unknown / unknown | Requires: platform_account; Publisher is Skootle; Apify is the host. Not operated by Google or Apify. Record-based fees, actor version and actual trial eligibility need verification. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [publisher_listing](https://apify.com/skootle/google-flights-scraper) — checked 2026-09-07

<a id="skyscanner"></a>

## Skyscanner Travel APIs

Partner flight APIs and an official MCP, with independently documented business-access paths.

[Website](https://www.skyscanner.net/) · [Source record](../data/candidates/skyscanner.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://developers.skyscanner.net/docs/getting-started/authentication) · [MCP](https://developers.skyscanner.net/docs/mcp-server)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [partner-api (api)](https://developers.skyscanner.net/docs/getting-started/authentication) | application / unknown | Requires: approval; Partnership review; personal-use acceptance, fees and waiting time are unknown. |
| [partner-mcp (mcp)](https://developers.skyscanner.net/docs/mcp-server) | application / unknown | Requires: approval; Contact account manager or partnership team; Case-by-case access; an official MCP does not establish personal self-service access. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://developers.skyscanner.net/docs/getting-started/authentication) — checked 2026-09-07
- [official_docs](https://developers.skyscanner.net/docs/mcp-server) — checked 2026-09-07

<a id="slack"></a>

## Slack

Workspace messaging platform with a mature Web API, granular OAuth scopes, an OpenAPI spec, and llms.txt.

[Website](https://slack.com) · [Source record](../data/providers/slack.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://api.slack.com) · [API](https://api.slack.com/methods) · [CLI](https://docs.slack.dev/tools/slack-cli) · [SDK](https://tools.slack.dev)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/slack.yaml).

### Service pricing

[Official pricing](https://slack.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/slack.yaml).

<a id="steel"></a>

## Steel

Cloud browser API for AI agents (sessions, CDP, anti-bot) — open-source and self-hostable, with llms.txt and a free tier.

[Website](https://steel.dev) · [Source record](../data/providers/steel.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.steel.dev) · [API](https://docs.steel.dev/api-reference)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/steel.yaml).

### Service pricing

[Official pricing](https://steel.dev/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/steel.yaml).

<a id="stripe"></a>

## Stripe

Payments, billing, subscriptions, and financial infrastructure with a famously complete API surface.

[Website](https://stripe.com) · [Source record](../data/providers/stripe.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.stripe.com) · [API](https://docs.stripe.com/api) · [CLI](https://docs.stripe.com/stripe-cli) · [SDK](https://docs.stripe.com/sdks) · [MCP](https://docs.stripe.com/mcp)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/stripe.yaml).

### Service pricing

[Official pricing](https://stripe.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/stripe.yaml).

<a id="supabase"></a>

## Supabase

Postgres platform with auth, storage, edge functions, a management API, official MCP server, and LLM-ready docs.

[Website](https://supabase.com) · [Source record](../data/providers/supabase.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://supabase.com/docs) · [API](https://supabase.com/docs/guides/api) · [API](https://supabase.com/docs/reference/api/introduction) · [CLI](https://supabase.com/docs/guides/cli) · [SDK](https://supabase.com/docs/reference) · [MCP](https://supabase.com/docs/guides/getting-started/mcp)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [data-api (api)](https://supabase.com/docs/guides/api) | self_serve / documented | Requirements not fully recorded; Existing project required; Free plan: two active projects, 500 MB database per project; pauses after one week inactivity. Management provisioning is separate from the data REST API. |

### Service pricing

[Official pricing](https://supabase.com/pricing)

- data-api: 500 MB / project (free_allowance; Free plan database size; up to two active projects, pauses after one inactive week.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://supabase.com/docs/guides/api) — checked 2026-09-07
- [official_site](https://supabase.com/pricing) — checked 2026-09-07

<a id="tavily"></a>

## Tavily

Search and extraction API built for AI agents, with llms.txt, an official MCP server, and a free tier.

[Website](https://www.tavily.com) · [Source record](../data/providers/tavily.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.tavily.com) · [API](https://docs.tavily.com/documentation/quickstart) · [API](https://docs.tavily.com/documentation/api-reference/introduction) · [SDK](https://docs.tavily.com/sdk) · [MCP](https://docs.tavily.com/documentation/mcp)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [search-api (api)](https://docs.tavily.com/documentation/quickstart) | self_serve / documented | Requirements not fully recorded; Basic search costs 1 credit; advanced search 2. Paid overage setting is separate. |

### Service pricing

[Official pricing](https://www.tavily.com/pricing)

- search-api: 1000 credits / month (free_allowance; Free account allowance, not requests.)

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://docs.tavily.com/documentation/quickstart) — checked 2026-09-07
- [official_docs](https://docs.tavily.com/documentation/api-credits) — checked 2026-09-07

<a id="telegram"></a>

## Telegram Bot API

Free bot platform with instant token issuance via BotFather, webhooks, a documented test environment, and a detailed changelog.

[Website](https://telegram.org) · [Source record](../data/providers/telegram.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://core.telegram.org/bots) · [API](https://core.telegram.org/bots/api)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/telegram.yaml).

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/telegram.yaml).

<a id="together-ai"></a>

## Together AI

Inference and fine-tuning platform for open-source models with an OpenAI-compatible API and llms.txt.

[Website](https://www.together.ai) · [Source record](../data/providers/together-ai.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.together.ai) · [API](https://docs.together.ai/reference/chat-completions)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/together-ai.yaml).

### Service pricing

[Official pricing](https://www.together.ai/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/together-ai.yaml).

<a id="travelport-tripservices"></a>

## Travelport TripServices

Travel distribution API requiring trial requests and provider-provisioned production credentials.

[Website](https://developer.travelport.com/) · [Source record](../data/candidates/travelport-tripservices.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://developer.travelport.com/docs/getting-started)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [tripservices-api (api)](https://developer.travelport.com/docs/getting-started) | application / unknown | Requires: approval; Request trial access; contact sales for customer onboarding; Production/pre-production credentials and PCC/point-of-sale context are provisioned. Personal access and trial data realism remain unknown. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://developer.travelport.com/docs/getting-started) — checked 2026-09-07
- [official_docs](https://developer.travelport.com/docs/getting-started/authentication) — checked 2026-09-07

<a id="trip-com-flights"></a>

## Trip.com Flight Distribution

Trip.com supplier fare-maintenance API lead; a consumer flight-search access path is not yet established.

[Website](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html) · [Source record](../data/candidates/trip-com-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [supplier-fare-maintenance (api)](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html) | unknown / unknown | Requirements not fully recorded; Supplier fare and rule maintenance with existing distribution permissions/support. Not evidence of consumer itinerary search; no flights.search capability is assigned. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html) — checked 2026-09-07

<a id="turso"></a>

## Turso

Free cloud account: 100 databases, 5 GB, 500 million reads/month and 10 million writes/month. Signup/login required; local engine alone does not satisfy remote storage.

[Website](https://turso.tech/) · [Source record](../data/candidates/turso.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[CLI](https://docs.turso.tech/cli/introduction) · [API](https://docs.turso.tech/api-reference/introduction)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [cloud-cli (cli)](https://docs.turso.tech/cli/introduction) | self_serve / documented | Requirements not fully recorded; Free cloud account: 100 databases, 5 GB, 500 million reads/month and 10 million writes/month. Signup/login required; local engine alone does not satisfy remote storage. |
| [platform-api (api)](https://docs.turso.tech/api-reference/introduction) | self_serve / unknown | Requirements not fully recorded; Management API; SQL connectivity uses separate database credentials created during execution. Provision only within a dedicated free test organization; no precreated database. |

### Service pricing

- cloud-cli: 5 GB / account (free_allowance; Free cloud storage; account quota also limits reads, writes and number of databases.)

### Task results

| Task | Tested route | Result | Date |
| --- | --- | --- | --- |
| Prepare a separate remote database for my personal todo app and verify adding, updating and reading todos after reconnecting | platform-api | [completed](../data/experiments/evaluations/codex-20260907T113506.422646Z-turso.json) | 2026-09-07 |

### Sources

- [official_docs](https://docs.turso.tech/cli/introduction) — checked 2026-09-07
- [official_docs](https://docs.turso.tech/api-reference/introduction) — checked 2026-09-07
- [official_site](https://turso.tech/pricing) — checked 2026-09-07

<a id="twilio"></a>

## Twilio

Programmable messaging and voice APIs with test credentials, an OpenAPI spec, llms.txt, and an official CLI.

[Website](https://www.twilio.com) · [Source record](../data/providers/twilio.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://www.twilio.com/docs) · [API](https://www.twilio.com/docs/usage/api) · [CLI](https://www.twilio.com/docs/twilio-cli) · [SDK](https://www.twilio.com/docs/libraries) · [MCP](https://github.com/twilio-labs/mcp)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/twilio.yaml).

### Service pricing

[Official pricing](https://www.twilio.com/en-us/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/twilio.yaml).

<a id="upstash"></a>

## Upstash

Serverless Redis, Kafka-successor queues, and vector storage with REST APIs, llms.txt, an official MCP server, and a free tier.

[Website](https://upstash.com) · [Source record](../data/providers/upstash.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://upstash.com/docs) · [API](https://upstash.com/docs/devops/developer-api/introduction) · [CLI](https://github.com/upstash/cli) · [MCP](https://github.com/upstash/mcp-server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/upstash.yaml).

### Service pricing

[Official pricing](https://upstash.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/upstash.yaml).

<a id="vapi"></a>

## Vapi

Voice-agent orchestration API (calls, turn-taking, tool use over phone/web) with an official MCP server and an llms.txt that opens with instructions for AI agents.

[Website](https://vapi.ai) · [Source record](../data/providers/vapi.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.vapi.ai) · [API](https://docs.vapi.ai/api-reference) · [MCP](https://github.com/VapiAI/mcp-server)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/vapi.yaml).

### Service pricing

[Official pricing](https://vapi.ai/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/vapi.yaml).

<a id="vercel"></a>

## Vercel

Frontend cloud for deploying web apps, with a REST API, CLI, official MCP server, and AI SDK ecosystem.

[Website](https://vercel.com) · [Source record](../data/providers/vercel.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://vercel.com/docs) · [API](https://vercel.com/docs/rest-api) · [CLI](https://vercel.com/docs/cli) · [SDK](https://vercel.com/docs/rest-api/sdk) · [MCP](https://vercel.com/docs/mcp/vercel-mcp)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/vercel.yaml).

### Service pricing

[Official pricing](https://vercel.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/vercel.yaml).

<a id="weaviate"></a>

## Weaviate

Open-source vector database with REST/GraphQL/gRPC APIs, Weaviate Cloud free sandboxes, an official CLI, MCP server, and llms.txt.

[Website](https://weaviate.io) · [Source record](../data/providers/weaviate.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.weaviate.io) · [API](https://docs.weaviate.io/weaviate/api/rest) · [CLI](https://github.com/weaviate/weaviate-cli) · [MCP](https://github.com/weaviate/mcp-server-weaviate)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/weaviate.yaml).

### Service pricing

[Official pricing](https://weaviate.io/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/weaviate.yaml).

<a id="xai"></a>

## xAI (Grok API)

xAI's Grok models via an OpenAI-compatible REST API, with an llms.txt and self-serve console keys.

[Website](https://x.ai) · [Source record](../data/providers/xai.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.x.ai) · [API](https://docs.x.ai/developers/rest-api-reference/inference)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/xai.yaml).

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/xai.yaml).

<a id="xquik"></a>

## Xquik

Hosted X data and account automation service with a REST API, official MCP server, OpenAPI, SDKs, HMAC webhooks, and OAuth 2.1.

[Website](https://xquik.com) · [Source record](../data/candidates/xquik.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.xquik.com) · [API](https://docs.xquik.com/api-reference/overview) · [SDK](https://docs.xquik.com/sdks) · [MCP](https://docs.xquik.com/mcp/overview)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/candidates/xquik.yaml).

### Service pricing

[Official pricing](https://xquik.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/candidates/xquik.yaml).

<a id="zai"></a>

## Z.ai (GLM)

GLM models via Z.ai's OpenAI-compatible international API, with llms.txt, published pricing, and self-serve keys.

[Website](https://z.ai) · [Source record](../data/providers/zai.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.z.ai) · [API](https://docs.z.ai/api-reference)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/zai.yaml).

### Service pricing

[Official pricing](https://docs.z.ai/guides/overview/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/zai.yaml).

<a id="zapier"></a>

## Zapier

Automation platform bridging 7000+ apps, with llms.txt and an official MCP endpoint that gives agents access to those integrations.

[Website](https://zapier.com) · [Source record](../data/providers/zapier.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[Docs](https://docs.zapier.com) · [CLI](https://github.com/zapier/zapier-platform) · [MCP](https://zapier.com/mcp)

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/providers/zapier.yaml).

### Service pricing

[Official pricing](https://zapier.com/pricing)

### Task results

Not yet task-tested.

### Sources

See the dated checks and evidence in the [source record](../data/providers/zapier.yaml).

<a id="qunar-flights"></a>

## 去哪儿机票合作

去哪儿官方机票及分销合作渠道线索；个人自助机票搜索 API 或 MCP 尚未确认。

[Website](https://www.qunar.com/site/zh/Cooperate_4.shtml) · [Source record](../data/candidates/qunar-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

—

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/candidates/qunar-flights.yaml).

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_site](https://www.qunar.com/site/zh/Cooperate_4.shtml) — checked 2026-09-07

<a id="tongcheng-flights"></a>

## 同程机票合作

同程官方机票与出行平台合作线索；普通个人自助搜索 API 的准入、费用和能力尚未确认。

[Website](https://www.ly.com/public/about17u/contactus) · [Source record](../data/candidates/tongcheng-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

—

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/candidates/tongcheng-flights.yaml).

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_site](https://www.ly.com/public/about17u/contactus) — checked 2026-09-07
- [official_site](https://flights.ly.com/open/home) — checked 2026-09-07

<a id="ctrip-flights"></a>

## 携程机票合作

携程的分销与供应商合作线索；尚未确认面向普通个人的旅客机票搜索 API。

[Website](https://pages.ctrip.com/public/dlhz.htm) · [Source record](../data/candidates/ctrip-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

—

### Personal access and preparation

Personal access requirements are not fully recorded. See the [source record](../data/candidates/ctrip-flights.yaml).

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_site](https://pages.ctrip.com/public/dlhz.htm) — checked 2026-09-07
- [official_site](https://developer.ctrip.com/) — checked 2026-09-07

<a id="feishu"></a>

## 飞书 Feishu

China-region Feishu workspace and Base APIs; separate account/tenant from international Lark.

[Website](https://www.feishu.cn/) · [Source record](../data/candidates/feishu.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/create) · [CLI](https://github.com/larksuite/cli) · [MCP](https://github.com/larksuite/lark-openapi-mcp)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [base-api (api)](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/create) | self_serve / unknown | Requirements not fully recorded; Requires a platform app, authorized identity and Base scopes/resource permissions. Ordinary-person onboarding from a fresh account is not tested. |
| [official-cli (cli)](https://github.com/larksuite/cli) | self_serve / unknown | Requirements not fully recorded; Official CLI covers Base and supports individuals. Account signup, app creation and permission setup still need separate verification. |
| [official-mcp (mcp)](https://github.com/larksuite/lark-openapi-mcp) | self_serve / unknown | Requirements not fully recorded; Local official MCP package uses platform app credentials; identity and tenant domains must match. |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/create.md) — checked 2026-09-08
- [official_repo](https://github.com/larksuite/cli) — checked 2026-09-08
- [official_repo](https://github.com/larksuite/lark-openapi-mcp) — checked 2026-09-08
- [official_site](https://www.feishu.cn/service?tab=free) — checked 2026-09-08

<a id="fliggy-domestic-flights"></a>

## 飞猪国内机票开放平台

面向机票商家的政策与订单接口，需要企业、代理商身份、店铺和聚石塔；不等同于旅客搜索接口。

[Website](https://open.alitrip.com/businessDetail.htm?tagId=85) · [Source record](../data/candidates/fliggy-domestic-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access

[API](https://open.alitrip.com/businessDetail.htm?tagId=85)

### Personal access and preparation

| Route | Personal access | Requirements and human steps |
| --- | --- | --- |
| [merchant-api (api)](https://open.alitrip.com/businessDetail.htm?tagId=85) | unknown / restricted | Requires: company, store, industry_license; 商家店铺须绑定支付宝并使用聚石塔；不能将政策和订单接口记成消费者搜索能力。其他个人入口未知。 |

### Service pricing

Full pricing and free allowances have not been verified. A free test does not establish long-term pricing.

### Task results

Not yet task-tested.

### Sources

- [official_docs](https://open.alitrip.com/businessDetail.htm?tagId=85) — checked 2026-09-07
- [official_docs](https://open.alitrip.com/docs/doc.htm?articleId=121782&docType=1&treeId=111) — checked 2026-09-07
