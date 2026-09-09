<!-- GENERATED — edit source records; run npm run generate. -->
# Service profiles

Token and costs are means per valid trial, including successes and failures; invalid runs are excluded. Model costs use saved LiteLLM prices; ~ marks estimated service charges. — means no data. Setup costs are separate from business task costs. Access and pricing are source claims; a listed route does not establish task support. Compare only matching tasks and conditions.

<a id="adyen"></a>

## Adyen

Payment processing with hosted Pay by Link checkout; test merchant accounts and live onboarding have separate requirements.

[Website](https://www.adyen.com/) · [Source record](../data/candidates/adyen.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="adyen-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [payment-links-api (API)](https://docs.adyen.com/api-explorer/Checkout/latest/post/paymentLinks) | [Docs](https://docs.adyen.com/api-explorer/Checkout/latest/post/paymentLinks) | — | Requires merchantAccount and API credentials. Test cards and test accounts are documented; test account admission and individual eligibility have not been verified. Live setup needs approval and merchant terms. Pay by Link is described as supplementary to an online store checkout. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://docs.adyen.com/api-explorer/Checkout/latest/post/paymentLinks) — checked 2026-09-08
- [official_docs](https://docs.adyen.com/unified-commerce/pay-by-link/create-payment-links/customer-area) — checked 2026-09-08
- [official_docs](https://docs.adyen.com/unified-commerce/pay-by-link?locale=en-us) — checked 2026-09-08

<a id="airgateway"></a>

## AirGateway Platform API

Air distribution API with sandbox keys, production certification and an agency application.

[Website](https://airgateway.com/) · [Source record](../data/candidates/airgateway.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="airgateway-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [agency-api (API)](https://support.airgateway.com/en-US/kb/article/4/introduction-to-airgateway-platform-api) | [Docs](https://support.airgateway.com/en-US/kb/article/4/introduction-to-airgateway-platform-api) | application / restricted | Requires: company, industry_license, approval; This does not prove the absence of other individual-facing AirGateway products. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://support.airgateway.com/en-US/kb/article/4/introduction-to-airgateway-platform-api) — checked 2026-09-07
- [official_site](https://airgateway.com/agencies/) — checked 2026-09-07

<a id="airtable"></a>

## Airtable

Spreadsheet-database hybrid with a REST API, scoped personal access tokens, OAuth, webhooks, and documented rate limits.

[Website](https://www.airtable.com) · [Source record](../data/providers/airtable.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="airtable-access"></a>

[Docs](https://airtable.com/developers)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [web-api (API)](https://airtable.com/developers/web/api/introduction) | [Docs](https://airtable.com/developers/web/api/introduction) | self serve / documented | Create a personal access token with required scopes and selected test resources.; PAT scopes plus selected workspace/base access required. Base creation is documented on all plans; do not infer paid-only access from outdated posts. |

### Service pricing

[Official pricing](https://airtable.com/pricing)

- web-api: 1000 API calls / workspace/month (free_allowance; Free plan; includes metadata/schema calls, 5 requests/second/base.)

- web-api: 1000 records / base (free_allowance; Free plan storage limit across all tables in a base.)

### Task results

—

### Sources

- [official_docs](https://support.airtable.com/articles/6292134965-getting-started-with-airtable-s-web-api) — checked 2026-09-08
- [official_docs](https://airtable.com/developers/web/guides/personal-access-tokens) — checked 2026-09-08
- [official_docs](https://support.airtable.com/articles/2277136852-airtable-plans-overview) — checked 2026-09-08
- [official_docs](https://support.airtable.com/articles/7735693959-managing-api-call-limits-in-airtable) — checked 2026-09-08

<a id="airwallex"></a>

## Airwallex

Hosted payment links with fixed or customer-selected amounts and payment status webhooks.

[Website](https://www.airwallex.com/) · [Source record](../data/candidates/airwallex.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="airwallex-access"></a>

[Docs](https://www.airwallex.com/docs/payments/payment-links/payment-links-via-api)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [payment-links-api (API)](https://www.airwallex.com/docs/api/payments/payment_links/api) | [Docs](https://www.airwallex.com/docs/api/payments/payment_links/api) | — | API requires an access token and merchant configuration. Sandbox examples are documented, but individual account eligibility, activation and full fees are not established here. Payment success is reported separately from link creation. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://www.airwallex.com/docs/payments/payment-links/payment-links-via-api) — checked 2026-09-08
- [official_docs](https://www.airwallex.com/docs/api/payments/payment_links/api) — checked 2026-09-08

<a id="aiven"></a>

## Aiven

Managed databases including free hosted PostgreSQL. Account signup and provisioning remain untested; free lifecycle limits need checking before production use.

[Website](https://aiven.io/) · [Source record](../data/candidates/aiven.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="aiven-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [postgres-cli (CLI)](https://aiven.io/docs/tools/cli) | [Docs](https://aiven.io/docs/tools/cli) | self serve / documented | Managed databases including free hosted PostgreSQL. Account signup and provisioning remain untested; free lifecycle limits need checking before production use. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://aiven.io/docs/tools/cli) — checked 2026-09-07
- [official_site](https://aiven.io/free-postgresql-database) — checked 2026-09-07

<a id="qwen"></a>

## Alibaba Qwen (Model Studio)

Qwen model family via Alibaba Cloud Model Studio's OpenAI-compatible API, with an official open-source coding CLI agent (qwen-code).

[Website](https://www.alibabacloud.com/en/product/modelstudio) · [Source record](../data/providers/qwen.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="qwen-access"></a>

[Docs](https://www.alibabacloud.com/help/en/model-studio/) · [API reference](https://www.alibabacloud.com/help/en/model-studio/models) · [CLI](https://github.com/QwenLM/qwen-code)

—

### Service pricing

—

### Task results

—

### Sources

—

<a id="alipay"></a>

## Alipay

Online merchant payment integrations for websites and apps through Alipay APIs and SDKs.

[Website](https://open.alipay.com/) · [Source record](../data/candidates/alipay.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="alipay-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [web-app-api (API)](https://open.alipay.com/module/webApp) | — | application | Requires: approval; Application setup, signing keys and review are documented for launch. Merchant qualification, supported currencies and a task-compatible sandbox still need verification. Web/app integration is not proof of a standalone shareable checkout link. |

### Service pricing

—

### Task results

—

### Sources

- [official_site](https://open.alipay.com/module/webApp) — checked 2026-09-08
- [official_site](https://open.alipay.com/) — checked 2026-09-08

<a id="amadeus-flights"></a>

## Amadeus Flight APIs

Historical Self-Service flight API and the current Enterprise portal; individual onboarding must be re-established.

[Website](https://developers.amadeus.com/) · [Source record](../data/candidates/amadeus-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="amadeus-flights-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [former-self-service (API)](https://developers.amadeus.com/blog/comparing-open-source-flight-data-sources) | — | retired | Retain this historical access path. Stale tutorials do not establish current self-service signup. |
| [enterprise-api (API)](https://developers.amadeus.com/) | — | — | Current portal lead; personal eligibility, application requirements, costs and current flight endpoints remain unknown. |

### Service pricing

—

### Task results

—

### Sources

- [official_announcement](https://developers.amadeus.com/blog/comparing-open-source-flight-data-sources) — checked 2026-09-07
- [official_site](https://developers.amadeus.com/) — checked 2026-09-07

<a id="anthropic"></a>

## Anthropic

Claude model APIs with agent-focused documentation, llms.txt, and the company behind the MCP standard itself.

[Website](https://www.anthropic.com) · [Source record](../data/providers/anthropic.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="anthropic-access"></a>

[Docs](https://docs.anthropic.com) · [API reference](https://docs.anthropic.com/en/api) · [CLI](https://docs.anthropic.com/en/docs/claude-code) · [SDK](https://docs.anthropic.com/en/api/client-sdks)

—

### Service pricing

[Official pricing](https://www.anthropic.com/pricing)

### Task results

—

### Notes

- Anthropic authored the MCP standard; no first-party MCP server exposing the Anthropic API was found at review time (mcp_official intentionally absent).
- Claude Code is listed as cli — it is an agent CLI rather than an API-management CLI.

### Sources

—

<a id="apify"></a>

## Apify

Web scraping and automation platform with thousands of ready-made actors, a versioned API, llms.txt, and an official MCP server.

[Website](https://apify.com) · [Source record](../data/providers/apify.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="apify-access"></a>

[Docs](https://docs.apify.com) · [API reference](https://docs.apify.com/api/v2) · [CLI](https://docs.apify.com/cli) · [SDK](https://docs.apify.com/sdk) · [MCP entry](https://docs.apify.com/platform/integrations/mcp)

—

### Service pricing

[Official pricing](https://apify.com/pricing)

### Task results

—

### Notes

- mcp.apify.com hosts the official remote MCP server; the docs page above explains setup.

### Sources

—

<a id="apiheya-air-scraper"></a>

## apiheya Air Scraper

An apiheya flight-data product distributed through RapidAPI; distinct from the official Skyscanner partner API.

[Website](https://rapidapi.com/apiheya/api/sky-scrapper/pricing) · [Source record](../data/candidates/apiheya-air-scraper.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="apiheya-air-scraper-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [rapidapi-product (API)](https://rapidapi.com/apiheya/api/sky-scrapper/playground/apiendpoint_6856e0a6-2804-43cd-9cc0-bb377022981e) | — | — | Requires: platform_account; Publisher is apiheya; RapidAPI is the marketplace. Upstream identity is not established by a product slug. |

### Service pricing

- rapidapi-product: 20 requests / month (free_allowance; Listed Basic plan; card requirements and included flight endpoints unverified.)

### Task results

—

### Sources

- [publisher_listing](https://rapidapi.com/apiheya/api/sky-scrapper/playground/apiendpoint_6856e0a6-2804-43cd-9cc0-bb377022981e) — checked 2026-09-07
- [publisher_listing](https://rapidapi.com/apiheya/api/sky-scrapper/pricing) — checked 2026-09-07

<a id="atlassian"></a>

## Atlassian (Jira & Confluence)

Jira, Confluence and the Atlassian Cloud platform — REST APIs, an official remote MCP server (OAuth 2.1), and the acli CLI.

[Website](https://www.atlassian.com) · [Source record](../data/providers/atlassian.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="atlassian-access"></a>

[Docs](https://developer.atlassian.com) · [API reference](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/) · [CLI](https://developer.atlassian.com/cloud/acli/) · [MCP entry](https://github.com/atlassian/atlassian-mcp-server)

—

### Service pricing

[Official pricing](https://www.atlassian.com/software/jira/pricing)

### Task results

—

### Sources

—

<a id="aviasales"></a>

## Aviasales via Travelpayouts

Travelpayouts-distributed live flight search and a separately accessible historical price-data API.

[Website](https://www.aviasales.com/) · [Source record](../data/candidates/aviasales.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="aviasales-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [live-search-api (API)](https://support.travelpayouts.com/hc/en-us/articles/210995808-How-to-get-access-to-the-Aviasales-Search-API) | [Docs](https://support.travelpayouts.com/hc/en-us/articles/210995808-How-to-get-access-to-the-Aviasales-Search-API) | application / restricted | Requires: platform_account, approval, traffic |
| [cached-data-api (API)](https://support.travelpayouts.com/hc/en-us/articles/203956163-Aviasales-Data-API) | [Docs](https://support.travelpayouts.com/hc/en-us/articles/203956163-Aviasales-Data-API) | self serve | Requires: platform_account; Historical user-search cache for price trends and inspiration. Each method has its own time window; no fresh search is triggered. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://support.travelpayouts.com/hc/en-us/articles/210995808-How-to-get-access-to-the-Aviasales-Search-API) — checked 2026-09-07
- [official_docs](https://support.travelpayouts.com/hc/en-us/articles/203956083-Requirements-for-Aviasales-data-API-access) — checked 2026-09-07
- [official_docs](https://support.travelpayouts.com/hc/en-us/articles/203956163-Aviasales-Data-API) — checked 2026-09-07

<a id="baserow"></a>

## Baserow Cloud

Hosted collaborative tables; free workspace and scoped row-access tokens. Schema management uses a different credential.

[Website](https://baserow.io/) · [Source record](../data/candidates/baserow.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="baserow-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [database-api (API)](https://baserow.io/docs/apis/rest-api) | [Docs](https://baserow.io/docs/apis/rest-api) | self serve / documented | Generate a database token and select permitted tables and operations.; Database token can read/create/update/delete rows in permitted tables; creating the table/schema requires a short-lived JWT. A precreated table changes the test setup. |
| [native-mcp (MCP)](https://baserow.io/user-docs/mcp-server) | [Docs](https://baserow.io/user-docs/mcp-server) | — | Create a workspace MCP endpoint in account settings and securely store its private URL.; Workspace admin creates a unique secret-bearing endpoint URL; the URL is itself a credential and must not be published. Documented tools read schema/list tables and create/update/delete rows, but do not list table creation. Cloud plan availability is not yet verified; do not assume this route can provision task 001 from an empty container. |

### Service pricing

- database-api: 3000 rows / workspace (free_allowance; Cloud Free plan. 2 GB storage. JWT/schema access and database row tokens are distinct.)

### Task results

—

### Sources

- [official_docs](https://baserow.io/docs/apis/rest-api) — checked 2026-09-08
- [official_docs](https://baserow.io/user-docs/personal-api-tokens) — checked 2026-09-08
- [official_site](https://baserow.io/pricing) — checked 2026-09-08
- [official_docs](https://baserow.io/user-docs/mcp-server) — checked 2026-09-08

<a id="brave-search"></a>

## Brave Search API

Independent web search index with a developer API, self-serve registration, and a free plan.

[Website](https://brave.com/search/api/) · [Source record](../data/providers/brave-search.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="brave-search-access"></a>

[Docs](https://api-dashboard.search.brave.com/app/documentation) · [MCP entry](https://github.com/brave/brave-search-mcp-server)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [search-api (API)](https://brave.com/search/api/) | — | self serve / documented | Requires: payment_method; Free-plan card verification is required. No card supplied in this pilot; onboarding restriction does not establish poor search quality. |

### Service pricing

[Official pricing](https://brave.com/search/api/)

### Task results

—

### Notes

- Detailed API docs live inside the dashboard domain but are publicly readable without login (verified at review time).

### Sources

- [official_site](https://brave.com/search/api/) — checked 2026-09-07

<a id="bright-data-serp"></a>

## Bright Data SERP API

SERP API with a documented Google Flights request; structured fare extraction and onboarding need verification.

[Website](https://brightdata.com/) · [Source record](../data/candidates/bright-data-serp.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="bright-data-serp-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [google-flights-serp (API)](https://docs.brightdata.com/api-reference/serp/google-flights/currency) | [Docs](https://docs.brightdata.com/api-reference/serp/google-flights/currency) | — | Requires a SERP zone. Do not apply other Bright Data products’ payment requirements to this route. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://docs.brightdata.com/api-reference/serp/google-flights/currency) — checked 2026-09-07
- [official_docs](https://docs.brightdata.com/general/account/billing-and-pricing/payment-verification) — checked 2026-09-07
- [official_docs](https://docs.brightdata.com/cn/scraping-automation/serp-api/quickstart) — checked 2026-09-07

<a id="browserbase"></a>

## Browserbase

Headless browser infrastructure for AI agents and automation, with session APIs and an official MCP server.

[Website](https://www.browserbase.com) · [Source record](../data/providers/browserbase.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="browserbase-access"></a>

[Docs](https://docs.browserbase.com) · [API reference](https://docs.browserbase.com/reference) · [MCP entry](https://github.com/browserbase/mcp-server-browserbase)

—

### Service pricing

[Official pricing](https://www.browserbase.com/pricing)

### Task results

—

### Notes

- Stagehand (the company's agent framework) is a separate open-source project and not assessed here.

### Sources

—

<a id="cartesia"></a>

## Cartesia

Low-latency voice models (Sonic TTS, Ink STT) with a documented API, official MCP server, llms.txt, and a free tier.

[Website](https://cartesia.ai) · [Source record](../data/providers/cartesia.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="cartesia-access"></a>

[Docs](https://docs.cartesia.ai) · [API reference](https://docs.cartesia.ai/api-reference) · [MCP entry](https://github.com/cartesia-ai/cartesia-mcp)

—

### Service pricing

[Official pricing](https://www.cartesia.ai/pricing)

### Task results

—

### Sources

—

<a id="cerebras"></a>

## Cerebras Inference

Wafer-scale inference for open models at very high tokens/sec, OpenAI-compatible API, llms.txt, and a standing free tier.

[Website](https://cloud.cerebras.ai) · [Source record](../data/providers/cerebras.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="cerebras-access"></a>

[Docs](https://inference-docs.cerebras.ai) · [API reference](https://inference-docs.cerebras.ai/api-reference/chat-completions)

—

### Service pricing

[Official pricing](https://www.cerebras.ai/pricing)

### Task results

—

### Sources

—

<a id="checkout-com"></a>

## Checkout.com

Payment Links API for hosted checkout, with separate sandbox and production API hosts.

[Website](https://www.checkout.com/) · [Source record](../data/candidates/checkout-com.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="checkout-com-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [payment-links-api (API)](https://api-reference.checkout.com/tag/Payment-Links/) | [Docs](https://api-reference.checkout.com/tag/Payment-Links/) | — | API secret key and account-specific host required. Sandbox endpoints are documented; obtaining an account, individual merchant admission and negotiated fees remain unverified. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://api-reference.checkout.com/tag/Payment-Links/) — checked 2026-09-08

<a id="chroma"></a>

## Chroma

Open-source embedding database with a hosted Chroma Cloud, official CLI, official MCP server, and llms.txt.

[Website](https://www.trychroma.com) · [Source record](../data/providers/chroma.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="chroma-access"></a>

[Docs](https://docs.trychroma.com) · [API reference](https://docs.trychroma.com/docs/overview/introduction) · [CLI](https://docs.trychroma.com/docs/cli/install) · [MCP entry](https://github.com/chroma-core/chroma-mcp)

—

### Service pricing

[Official pricing](https://www.trychroma.com/pricing)

### Task results

—

### Sources

—

<a id="cloudflare"></a>

## Cloudflare

Edge network, Workers serverless platform, storage, and AI services with agent-focused docs and official MCP servers.

[Website](https://www.cloudflare.com) · [Source record](../data/providers/cloudflare.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="cloudflare-access"></a>

[Docs](https://developers.cloudflare.com) · [API reference](https://developers.cloudflare.com/api/) · [CLI](https://developers.cloudflare.com/workers/wrangler/) · [SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/) · [MCP entry](https://github.com/cloudflare/mcp-server-cloudflare)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [d1-cli (CLI)](https://developers.cloudflare.com/d1/get-started/) | [Docs](https://developers.cloudflare.com/d1/get-started/) | self serve / documented | D1 Workers Free: 5 million reads/day, 100,000 writes/day, 5 GB total storage. Account authorization required; Wrangler local mode is not a remote database test. Existing paid projects are excluded. |

### Service pricing

[Official pricing](https://www.cloudflare.com/plans/)

- d1-cli: 5 GB / account (free_allowance; D1 total storage on Workers Free; separate daily row quotas.)

### Task results

—

### Sources

- [official_docs](https://developers.cloudflare.com/d1/get-started/) — checked 2026-09-07
- [official_docs](https://developers.cloudflare.com/d1/platform/pricing/) — checked 2026-09-07

<a id="coda"></a>

## Coda / Superhuman Docs

Docs and tables with a free REST API; current API page is branded Superhuman Docs.

[Website](https://coda.io/) · [Source record](../data/candidates/coda.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="coda-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [rest-api (API)](https://coda.io/developers/apis/v1) | [Docs](https://coda.io/developers/apis/v1) | self serve | API available in free and paid workspaces. Creating docs requires a Doc Maker role; row writes may be asynchronous. Table/schema creation support must be verified for the task. |
| [hosted-mcp (MCP)](https://coda.io/apis/mcp) | [Docs](https://help.coda.io/hc/en-us/articles/44722661982989-Connect-to-the-Coda-MCP) | self serve | Official hosted MCP; connector setup needs authorization. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://coda.io/developers/apis/v1) — checked 2026-09-08
- [official_docs](https://help.coda.io/hc/en-us/articles/44722661982989-Connect-to-the-Coda-MCP) — checked 2026-09-08

<a id="cohere"></a>

## Cohere

Enterprise LLM platform (command, embed, rerank) with llms.txt, documented API versioning, free trial keys, and error/rate-limit docs.

[Website](https://cohere.com) · [Source record](../data/providers/cohere.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="cohere-access"></a>

[Docs](https://docs.cohere.com) · [API reference](https://docs.cohere.com/reference/about)

—

### Service pricing

[Official pricing](https://cohere.com/pricing)

### Task results

—

### Sources

—

<a id="composio"></a>

## Composio

Tool and integration layer for AI agents (hundreds of app connectors with managed auth), with llms.txt and a hosted MCP directory.

[Website](https://composio.dev) · [Source record](../data/providers/composio.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="composio-access"></a>

[Docs](https://docs.composio.dev) · [MCP entry](https://mcp.composio.dev) · [MCP setup](https://docs.composio.dev/docs/composio-connect)

—

### Service pricing

[Official pricing](https://composio.dev/pricing)

### Task results

—

### Notes

- MCP setup documentation checked on 2026-09-09: https://docs.composio.dev/docs/composio-connect. The server or product entry remains separately recorded in mcp_official.

### Sources

—

<a id="creem"></a>

## Creem

Digital-product checkout and billing APIs with separate test mode and reviewed merchant accounts.

[Website](https://www.creem.io/) · [Source record](../data/candidates/creem.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="creem-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [sandbox-api (API)](https://docs.creem.io/getting-started/test-mode) | [Docs](https://docs.creem.io/getting-started/test-mode) | self serve | Requires: platform_account; Use dashboard Test Mode and obtain a test API key.; Test mode has separate API keys, products and test-api.creem.io. Production account review includes the product website and individual or business identity; do not infer automatic approval from sandbox access. |

### Service pricing

[Official pricing](https://docs.creem.io/getting-started/introduction)

### Task results

—

### Notes

- Official introduction checked 2026-09-08 quotes a headline 3.9% + USD 0.40 transaction rate. The full applicable fee schedule and payouts have not been verified; this is not a measured sandbox charge.

### Sources

- [official_docs](https://docs.creem.io/getting-started/test-mode) — checked 2026-09-08
- [official_docs](https://docs.creem.io/merchant-of-record/account-reviews/account-reviews) — checked 2026-09-08
- [official_docs](https://docs.creem.io/getting-started/introduction) — checked 2026-09-08

<a id="datadog"></a>

## Datadog

Observability platform with a full REST API, llms.txt, documented OAuth for integrations, rate limits, and webhooks.

[Website](https://www.datadoghq.com) · [Source record](../data/providers/datadog.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="datadog-access"></a>

[Docs](https://docs.datadoghq.com) · [API reference](https://docs.datadoghq.com/api/latest/) · [CLI](https://github.com/DataDog/datadog-ci) · [MCP entry](https://docs.datadoghq.com/bits_ai/mcp_server)

—

### Service pricing

[Official pricing](https://www.datadoghq.com/pricing)

### Task results

—

### Sources

—

<a id="deepgram"></a>

## Deepgram

Speech-to-text and voice AI API with a public OpenAPI spec, llms.txt, scoped API keys, and $200 free credit without a card.

[Website](https://deepgram.com) · [Source record](../data/providers/deepgram.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="deepgram-access"></a>

[Docs](https://developers.deepgram.com/docs) · [API reference](https://developers.deepgram.com/reference) · [SDK](https://developers.deepgram.com/docs/deepgram-sdks)

—

### Service pricing

[Official pricing](https://deepgram.com/pricing)

### Task results

—

### Sources

—

<a id="deepseek"></a>

## DeepSeek

OpenAI-compatible LLM API (DeepSeek-V3/R1) with transparent per-token pricing, a detailed changelog, and self-serve keys.

[Website](https://www.deepseek.com) · [Source record](../data/providers/deepseek.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="deepseek-access"></a>

[Docs](https://api-docs.deepseek.com)

—

### Service pricing

[Official pricing](https://api-docs.deepseek.com/quick_start/pricing)

### Task results

—

### Sources

—

<a id="discord"></a>

## Discord

Chat platform with a versioned bot/OAuth2 API, official OpenAPI spec (preview), webhooks, and documented rate limits.

[Website](https://discord.com) · [Source record](../data/providers/discord.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="discord-access"></a>

[Docs](https://discord.com/developers/docs/intro) · [API reference](https://discord.com/developers/docs/reference)

—

### Service pricing

—

### Task results

—

### Notes

- The official OpenAPI spec is published by Discord but marked public preview / subject to change.

### Sources

—

<a id="dodo-payments"></a>

## Dodo Payments

Merchant-of-record checkout for one-time and subscription sales, with test mode, APIs, CLI and MCP documentation.

[Website](https://dodopayments.com/) · [Source record](../data/candidates/dodo-payments.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="dodo-payments-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [sandbox-api (API)](https://docs.dodopayments.com/introduction) | [Docs](https://docs.dodopayments.com/introduction) | — | Requires: platform_account; Use test API keys and simulated payments. Individual accounts are documented, but live payments and payouts require product review, identity verification and bank verification. Accepted ID countries apply; sandbox access does not certify live eligibility. |
| [official-cli (CLI)](https://github.com/dodopayments/dodopayments-cli) | [Docs](https://github.com/dodopayments/dodopayments-cli) | — | Official CLI for payments and billing resources. Authentication and environment must be prepared; this route has not been task-tested. |
| [live-api (API)](https://docs.dodopayments.com/introduction) | [Docs](https://docs.dodopayments.com/introduction) | application / documented | Requires: approval, identity_verification; Individual account type is documented, subject to product, identity and bank review plus accepted-country restrictions. Live payments and payouts require approval. No live account was created or approved in this research. |
| [payments-mcp (MCP)](https://mcp.dodopayments.com/sse) | [Docs](https://docs.dodopayments.com/developer-resources/mcp-server) | — | Transactional MCP. Initial OAuth setup asks for the merchant API key and test/live environment; explicitly select test. This is separate from the documentation-only Knowledge MCP and has not been task-tested. |

### Service pricing

—

### Task results

—

### Notes

- Official introduction links both knowledge MCP (documentation retrieval) and payments MCP. They are different capabilities; only the transactional server should be considered for payment execution.

### Sources

- [official_docs](https://docs.dodopayments.com/introduction) — checked 2026-09-08
- [official_docs](https://docs.dodopayments.com/miscellaneous/testing-process) — checked 2026-09-08
- [official_docs](https://docs.dodopayments.com/miscellaneous/verification-process) — checked 2026-09-08
- [official_repo](https://github.com/dodopayments/dodopayments-cli) — checked 2026-09-08
- [official_docs](https://docs.dodopayments.com/developer-resources/mcp-server) — checked 2026-09-08
- [official_docs](https://docs.dodopayments.com/miscellaneous/accepted-countries-and-territories) — checked 2026-09-08

<a id="dropbox"></a>

## Dropbox

File storage and sync with a scoped-OAuth HTTP API, self-serve app creation, and webhooks.

[Website](https://www.dropbox.com) · [Source record](../data/providers/dropbox.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="dropbox-access"></a>

[Docs](https://www.dropbox.com/developers/documentation) · [API reference](https://www.dropbox.com/developers/documentation/http/documentation) · [CLI](https://github.com/dropbox/dbxcli)

—

### Service pricing

[Official pricing](https://www.dropbox.com/plans)

### Task results

—

### Sources

—

<a id="duffel-flights"></a>

## Duffel Flights API

Flight API whose self-serve test environment must be distinguished from live account activation.

[Website](https://duffel.com/) · [Source record](../data/candidates/duffel-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="duffel-flights-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [test-api (API)](https://duffel.com/docs/api/overview/test-mode) | [Docs](https://duffel.com/docs/api/overview/test-mode) | self serve | Duffel Airways test prices and schedules are fictitious. Test-token success cannot establish live fare access. |
| [live-api (API)](https://duffel.com/guides/getting-started) | [Docs](https://duffel.com/guides/getting-started) | — | Requires: email_verification, identity_verification; Verify email and submit individual or business details; Live permissions, market coverage and pricing must be checked using a real eligible account. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://duffel.com/guides/getting-started) — checked 2026-09-07
- [official_docs](https://duffel.com/docs/api/overview/test-mode) — checked 2026-09-07

<a id="e2b"></a>

## E2B

Isolated cloud sandboxes for running AI-generated code, with llms.txt, an official MCP server, and self-serve keys.

[Website](https://e2b.dev) · [Source record](../data/providers/e2b.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="e2b-access"></a>

[Docs](https://e2b.dev/docs) · [CLI](https://e2b.dev/docs/cli) · [SDK](https://e2b.dev/docs/sdk-reference) · [MCP entry](https://github.com/e2b-dev/mcp-server)

—

### Service pricing

[Official pricing](https://e2b.dev/pricing)

### Task results

—

### Sources

—

<a id="elevenlabs"></a>

## ElevenLabs

Voice AI (TTS, STT, agents) with a public OpenAPI spec, llms.txt, an official MCP server, and a free tier.

[Website](https://elevenlabs.io) · [Source record](../data/providers/elevenlabs.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="elevenlabs-access"></a>

[Docs](https://elevenlabs.io/docs) · [API reference](https://elevenlabs.io/docs/api-reference/introduction) · [MCP entry](https://github.com/elevenlabs/elevenlabs-mcp)

—

### Service pricing

[Official pricing](https://elevenlabs.io/pricing)

### Task results

—

### Sources

—

<a id="exa"></a>

## Exa

Search API built for AI — semantic web search, content retrieval, and research endpoints with an official MCP server.

[Website](https://exa.ai) · [Source record](../data/providers/exa.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="exa-access"></a>

[Docs](https://docs.exa.ai) · [API reference](https://docs.exa.ai/reference/getting-started) · [SDK](https://docs.exa.ai/sdks/typescript-sdk-specification) · [MCP entry](https://github.com/exa-labs/exa-mcp-server)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [public-mcp (MCP)](https://mcp.exa.ai/mcp) | [Docs](https://exa.ai/docs/reference/exa-mcp) | self serve / documented | Public search MCP has a casual-use free plan; own key lifts limits. Additional agent_run tool requires authentication and separate usage charges; it is excluded from this pilot. API signup credits are not a quota guarantee for anonymous MCP. |
| [search-api (API)](https://exa.ai/docs/reference/search) | [Docs](https://exa.ai/docs/reference/search) | self serve / documented | Free account signup advertised at USD 20 initial credits plus USD 10/month; onboarding may be needed for part of initial credits. No payment method required. Anonymous MCP quota is separate. |

### Service pricing

[Official pricing](https://exa.ai/pricing)

- search-api: 20 USD / one_time (free_allowance; Published signup credits; some may require onboarding. Actual account award should be checked.)

- search-api: 10 USD / month (free_allowance; Free account monthly allowance, not anonymous MCP quota.)

### Setup observations

| Route | Starting resources | Setup tokens | Setup time | Human involvement |
| --- | --- | --- | --- | --- |
| MCP | [No account or key supplied](../data/experiments/evaluations/codex-20260907T112257.401366Z-exa.json) | — | — | — |
| API | [Credentials supplied before trial](../data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json) | — | — | — |

### Task results

#### I am upgrading a Python app to 3.13. Find out whether free threading is enabled by default, how to enable it, and what compatibility limits apply to existing C extensions, with official sources

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost | Conditions |
| --- | --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-9dbe771526ac) | [0%](./evaluations.md#comparison-9dbe771526ac) | — | — | $0 | A |
| MCP | [1](./evaluations.md#comparison-87ab787b88b3) | [100%](./evaluations.md#comparison-87ab787b88b3) | 931.5k | — | $0 | B |

<details>
<summary>Task, conditions and evidence</summary>

Target Python 3.13; official sources under python.org. Discover sources through the search service assigned to this trial; directly reading the pages it returns is allowed. Do not answer from model memory or another search engine.

**Completion:** All three questions are answered correctly and supported by official Python 3.13 documentation. At least two distinct official URLs appear in the specified service's real search response, with verifiable evidence. Fetching those pages directly is allowed; built-in web search may only locate service integration documentation and must not replace the tested search service.

codex-cli 0.153.4 · gpt-6-astra / xhigh · 600s · 2026-09-07 (UTC)

**A:** API · Credentials supplied · [Full configuration and evidence](./evaluations.md#comparison-9dbe771526ac)

**B:** MCP · No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-87ab787b88b3)

[Task definition](./tasks.en.md#web-search-001-v1)

- API: [Not completed](../data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json) — The authenticated Exa API returned real search results, but the executor spent its 10-search allowance on source discovery/evidence work and reached the 600-second wall-clock limit without a final answer. This is a task-budget failure, not API unavailability. CLI emitted no turn.completed usage event before interruption: tokens remain unknown, not zero. Free account was prepared outside measured time; no payment.

</details>

<details>
<summary>Run history (2)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| web-search-001 v1 | API | [not_completed](../data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json) | 2026-09-07 |
| web-search-001 v1 | MCP | [completed](../data/experiments/evaluations/codex-20260907T112257.401366Z-exa.json) | 2026-09-07 |

</details>

### Sources

- [official_docs](https://exa.ai/docs/reference/exa-mcp) — checked 2026-09-07
- [official_site](https://exa.ai/pricing) — checked 2026-09-07
- [official_docs](https://exa.ai/docs/reference/search) — checked 2026-09-07

<a id="expedia-xap-flights"></a>

## Expedia XAP Flight Listings

Travel Redirect/XAP flight listings product whose new API applications are currently paused.

[Website](https://developers.expediagroup.com/xap-apis/api/start-guide/getting-started) · [Source record](../data/candidates/expedia-xap-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="expedia-xap-flights-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [flight-listings-api (API)](https://developers.expediagroup.com/xap-apis/api/shopping-apis/flight-listings) | [Docs](https://developers.expediagroup.com/xap-apis/api/shopping-apis/flight-listings) | paused / restricted | — |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://developers.expediagroup.com/xap-apis/api/start-guide/getting-started) — checked 2026-09-07
- [official_docs](https://developers.expediagroup.com/xap-apis/api/shopping-apis/flight-listings) — checked 2026-09-07

<a id="fal"></a>

## fal.ai

Generative media platform (image, video, audio models) with queue/streaming APIs, an official CLI/serving framework, llms.txt, and self-serve keys.

[Website](https://fal.ai) · [Source record](../data/providers/fal.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="fal-access"></a>

[Docs](https://fal.ai/docs) · [API reference](https://fal.ai/docs/model-apis) · [CLI](https://github.com/fal-ai/fal)

—

### Service pricing

[Official pricing](https://fal.ai/pricing)

### Task results

—

### Sources

—

<a id="fastspring"></a>

## FastSpring

Checkout and subscription platform with API, JavaScript checkout libraries and order webhooks.

[Website](https://fastspring.com/) · [Source record](../data/candidates/fastspring.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="fastspring-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [official-api (API)](https://developer.fastspring.com/) | [Docs](https://developer.fastspring.com/) | — | Official docs establish API, checkout and subscription integration options. Individual admission, store activation, sandbox prerequisites and applicable fees have not been checked in this discovery pass. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://developer.fastspring.com/) — checked 2026-09-08

<a id="firecrawl"></a>

## Firecrawl

Web scraping and crawling API that turns websites into LLM-ready markdown, with an official MCP server.

[Website](https://www.firecrawl.dev) · [Source record](../data/providers/firecrawl.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="firecrawl-access"></a>

[Docs](https://docs.firecrawl.dev) · [API reference](https://docs.firecrawl.dev/api-reference/introduction) · [SDK](https://docs.firecrawl.dev/sdks/overview) · [MCP entry](https://docs.firecrawl.dev/mcp-server)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [public-search-api (API)](https://docs.firecrawl.dev/features/search) | [Docs](https://docs.firecrawl.dev/features/search) | self serve / documented | Current search docs explicitly permit starting without a key. Anonymous quota is unquantified; account free credits cannot be assumed for this route. |
| [account-search-api (API)](https://docs.firecrawl.dev/features/search) | [Docs](https://docs.firecrawl.dev/features/search) | self serve / documented | Search: 2 credits per 10 results; extra scraping can consume credits. |

### Service pricing

[Official pricing](https://www.firecrawl.dev/pricing)

- account-search-api: 1000 credits / month (free_allowance; Account Free plan; separate from anonymous access.)

### Setup observations

| Route | Starting resources | Setup tokens | Setup time | Human involvement |
| --- | --- | --- | --- | --- |
| API (public-search-api) | [No account or key supplied](../data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json) | — | — | — |
| API (account-search-api) | — | — | — | — |

### Task results

#### I am upgrading a Python app to 3.13. Find out whether free threading is enabled by default, how to enable it, and what compatibility limits apply to existing C extensions, with official sources

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API (public-search-api) | [1](./evaluations.md#comparison-b5f21fc39ab4) | [100%](./evaluations.md#comparison-b5f21fc39ab4) | 346.8k | — | $0 |
| API (account-search-api) | — | — | — | — | — |

<details>
<summary>Task, conditions and evidence</summary>

Target Python 3.13; official sources under python.org. Discover sources through the search service assigned to this trial; directly reading the pages it returns is allowed. Do not answer from model memory or another search engine.

**Completion:** All three questions are answered correctly and supported by official Python 3.13 documentation. At least two distinct official URLs appear in the specified service's real search response, with verifiable evidence. Fetching those pages directly is allowed; built-in web search may only locate service integration documentation and must not replace the tested search service.

codex-cli 0.153.4 · gpt-6-astra / xhigh · 600s · 2026-09-07 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-b5f21fc39ab4)

[Task definition](./tasks.en.md#web-search-001-v1)

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| web-search-001 v1 | API (public-search-api) | [completed](../data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json) | 2026-09-07 |

</details>

### Sources

- [official_docs](https://docs.firecrawl.dev/features/search) — checked 2026-09-07
- [official_site](https://www.firecrawl.dev/pricing) — checked 2026-09-07

<a id="fireworks"></a>

## Fireworks AI

Fast open-model inference and fine-tuning with an OpenAI-compatible API, official firectl CLI, llms.txt, and published pricing.

[Website](https://fireworks.ai) · [Source record](../data/providers/fireworks.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="fireworks-access"></a>

[Docs](https://docs.fireworks.ai) · [API reference](https://docs.fireworks.ai/api-reference/introduction) · [CLI](https://docs.fireworks.ai/tools-sdks/firectl/firectl)

—

### Service pricing

[Official pricing](https://fireworks.ai/pricing)

### Task results

—

### Sources

—

<a id="flight-mcp"></a>

## Flight MCP

Authenticated flight lookup and a separate, restricted public cache exposed through REST and MCP.

[Website](https://flight-mcp.com/) · [Source record](../data/candidates/flight-mcp.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="flight-mcp-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [authenticated-api (API)](https://flight-mcp.com/docs) | [Docs](https://flight-mcp.com/docs) | self serve | — |
| [authenticated-mcp (MCP)](https://flight-mcp.com/docs) | [Docs](https://flight-mcp.com/docs) | self serve | — |
| [public-cache-api (API)](https://flight-mcp.com/docs) | [Docs](https://flight-mcp.com/docs) | self serve | Only 10 specified directed routes, one adult, economy, USD, en-US and US point of sale; per-date weekly cache refresh over 180 days. Does not trigger fresh queries for arbitrary routes. |
| [public-cache-mcp (MCP)](https://flight-mcp.com/docs) | [Docs](https://flight-mcp.com/docs) | self serve | Only 10 specified directed routes, one adult, economy, USD, en-US and US point of sale; per-date weekly cache refresh over 180 days. Does not trigger fresh queries for arbitrary routes. |

### Service pricing

- authenticated-api: 300 new_fetches / month (free_allowance; Authenticated free plan; cache hits do not consume this allowance.)

- authenticated-mcp: 300 new_fetches / month (free_allowance; Authenticated free plan; cache hits do not consume this allowance.)

### Task results

—

### Sources

- [official_docs](https://flight-mcp.com/docs) — checked 2026-09-07
- [official_site](https://flight-mcp.com/pricing) — checked 2026-09-07

<a id="flightapi-io"></a>

## FlightAPI.io Flight Price API

Flight-price search for one-way, round-trip and multi-city itineraries, with credit-based usage.

[Website](https://www.flightapi.io/) · [Source record](../data/candidates/flightapi-io.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="flightapi-io-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [price-api (API)](https://www.flightapi.io/documentation/) | [Docs](https://www.flightapi.io/documentation/) | self serve | Trial quota units, card requirements and new-account endpoint access still need verification. |

### Service pricing

- price-api: 2 credits / request (usage; One-way or round-trip flight-price query.)

- price-api: 5 credits / request (usage; Multi-city flight-price query.)

### Task results

—

### Sources

- [official_docs](https://www.flightapi.io/documentation/getting-started/) — checked 2026-09-07
- [official_docs](https://www.flightapi.io/documentation/) — checked 2026-09-07
- [official_site](https://www.flightapi.io/) — checked 2026-09-07

<a id="fly-io"></a>

## Fly.io

Run full-stack apps and machines close to users, with a spec'd Machines API, scoped macaroon tokens, and official MCP docs.

[Website](https://fly.io) · [Source record](../data/providers/fly-io.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="fly-io-access"></a>

[Docs](https://fly.io/docs) · [API reference](https://fly.io/docs/machines/api/) · [CLI](https://fly.io/docs/flyctl/) · [MCP entry](https://fly.io/docs/mcp/)

—

### Service pricing

[Official pricing](https://fly.io/docs/about/pricing/)

### Task results

—

### Notes

- fly.io/llms.txt publishes an explicit AI-agent access policy: automated LLM clients are asked to identify via an AI-Agent request header (telemetry only, not authentication).

### Sources

—

<a id="gemini-api"></a>

## Gemini API

Google's Gemini model APIs via AI Studio, with generous free tier and documented API versioning.

[Website](https://ai.google.dev) · [Source record](../data/providers/gemini-api.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="gemini-api-access"></a>

[Docs](https://ai.google.dev/gemini-api/docs) · [API reference](https://ai.google.dev/api) · [CLI](https://github.com/google-gemini/gemini-cli) · [SDK](https://ai.google.dev/gemini-api/docs/libraries)

—

### Service pricing

[Official pricing](https://ai.google.dev/gemini-api/docs/pricing)

### Task results

—

### Sources

—

<a id="github"></a>

## GitHub

Code hosting, collaboration, and automation with REST and GraphQL APIs, an official CLI, and an official MCP server.

[Website](https://github.com) · [Source record](../data/providers/github.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="github-access"></a>

[Docs](https://docs.github.com) · [API reference](https://docs.github.com/rest) · [CLI](https://cli.github.com) · [SDK](https://github.com/octokit) · [MCP entry](https://github.com/github/github-mcp-server)

—

### Service pricing

[Official pricing](https://github.com/pricing)

### Task results

—

### Notes

- Multi-product platform; this entry covers the core developer platform only (see scope).

### Sources

—

<a id="gitlab"></a>

## GitLab

DevOps platform with REST and GraphQL APIs, scoped tokens, llms.txt, and an official CLI.

[Website](https://gitlab.com) · [Source record](../data/providers/gitlab.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="gitlab-access"></a>

[Docs](https://docs.gitlab.com) · [API reference](https://docs.gitlab.com/api/rest/) · [CLI](https://gitlab.com/gitlab-org/cli) · [MCP entry](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server)

—

### Service pricing

[Official pricing](https://about.gitlab.com/pricing/)

### Task results

—

### Sources

—

<a id="google-sheets"></a>

## Google Sheets

Online spreadsheets with a no-additional-cost API; Cloud project and OAuth setup are still prerequisites.

[Website](https://workspace.google.com/products/sheets/) · [Source record](../data/candidates/google-sheets.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="google-sheets-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [sheets-api (API)](https://developers.google.com/workspace/sheets/api/guides/concepts) | [Docs](https://developers.google.com/workspace/sheets/api/quickstart/python) | self serve | Configure a Cloud project and OAuth consent/client, then authorize selected account access.; Quickstart requires a Google account, Cloud project, enabled Sheets API and OAuth client/consent setup. Service accounts are another route, not assumed preconfigured. |

### Service pricing

- sheets-api: 0 USD / standard API usage (usage; Sheets API standard use has no additional cost; per-minute quotas apply.)

### Task results

—

### Sources

- [official_docs](https://developers.google.com/workspace/sheets/api/quickstart/python) — checked 2026-09-08
- [official_docs](https://developers.google.com/workspace/sheets/api/limits) — checked 2026-09-08

<a id="grafana"></a>

## Grafana (Grafana Cloud)

Observability platform (dashboards, metrics, logs, traces) with a documented HTTP API, official MCP server, llms.txt, and a standing free cloud tier.

[Website](https://grafana.com) · [Source record](../data/providers/grafana.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="grafana-access"></a>

[Docs](https://grafana.com/docs) · [API reference](https://grafana.com/docs/grafana/latest/developers/http_api/) · [MCP entry](https://github.com/grafana/mcp-grafana)

—

### Service pricing

[Official pricing](https://grafana.com/pricing)

### Task results

—

### Sources

—

<a id="grist"></a>

## Grist

Hosted relational spreadsheets with a free personal site, REST API and official MCP.

[Website](https://www.getgrist.com/) · [Source record](../data/candidates/grist.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="grist-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [rest-api (API)](https://support.getgrist.com/api/) | [Docs](https://support.getgrist.com/api/) | self serve / documented | Sign in and generate an API key in account settings.; Account API key grants the user’s existing access. Use a separate free test account; personal site is freely available. |
| [hosted-mcp (MCP)](https://docs.getgrist.com/api/mcp) | [Docs](https://support.getgrist.com/mcp/) | self serve / documented | Hosted server accepts API keys or interactive OAuth; available on all plans. Calls share the API pool. |
| [python-sdk (SDK)](https://pypi.org/project/grist-api/) | [Docs](https://support.getgrist.com/rest-api/) | — | Official Python client linked by Grist REST API guide; SDK installation does not remove account permission requirements. |
| [javascript-sdk (SDK)](https://www.npmjs.com/package/grist-api) | [Docs](https://support.getgrist.com/rest-api/) | — | Official JavaScript/TypeScript client linked by Grist REST API guide; npm page fetch returned 403 during public research, not a service failure. |

### Service pricing

- rest-api: 5000 records / document (free_allowance; Hosted Free plan; API quota must also be checked for the selected site.)

### Setup observations

| Route | Starting resources | Setup tokens | Setup time | Human involvement |
| --- | --- | --- | --- | --- |
| API | [Credentials supplied before trial](../data/experiments/evaluations/codex-20260908T035504.472694Z-grist.json) | — | — | — |
| MCP | — | — | — | — |
| SDK (python-sdk) | — | — | — | — |
| SDK (javascript-sdk) | — | — | — | — |

### Task results

#### Turn the action items in these book-club meeting notes into an online task table, give me its link, and tell me what is still unfinished and when each item is due

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-6203194a76cd) | [100%](./evaluations.md#comparison-6203194a76cd) | 540.8k | — | $0 |
| MCP | — | — | — | — | — |
| SDK (python-sdk) | — | — | — | — | — |
| SDK (javascript-sdk) | — | — | — | — | — |

<details>
<summary>Task, conditions and evidence</summary>

Book-club planning meeting, September 8, 2026: Lin Qing will confirm the venue by September 15; Zhou Zhou will prepare the reading list by September 16; Chen He will make the poster, originally due September 18. All three were unfinished during the meeting. Follow-up: Zhou Zhou has finished the reading list, and the poster deadline has moved to September 20. Everything else stays the same.

**Completion:** The remote table contains exactly three actions with correct owners and final deadlines. The reading list is complete and the other two are incomplete. The answer links to the table and correctly lists the two unfinished items and their dates. The evaluator independently verifies the data through the service API. Fields and operation order are unrestricted; inserting the old state first or producing evidence files is not required.

codex-cli 0.153.4 · gpt-6-astra / xhigh · 600s · 2026-09-08 (UTC)

Credentials supplied · [Full configuration and evidence](./evaluations.md#comparison-6203194a76cd)

[Task definition](./tasks.en.md#collaborative-tables-001-v2)

</details>

<details>
<summary>Run history (2)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| collaborative-tables-001 v2 | API | [completed](../data/experiments/evaluations/codex-20260908T035504.472694Z-grist.json) | 2026-09-08 |
| collaborative-tables-001 v1 | API | [completed](../data/experiments/evaluations/codex-20260908T032113.556233Z-grist.json) | 2026-09-08 |

</details>

### Sources

- [official_docs](https://support.getgrist.com/api/) — checked 2026-09-08
- [official_docs](https://support.getgrist.com/rest-api/) — checked 2026-09-08
- [official_site](https://www.getgrist.com/pricing/) — checked 2026-09-08
- [official_docs](https://support.getgrist.com/mcp/) — checked 2026-09-08

<a id="groq"></a>

## Groq

Ultra-low-latency LLM inference with an OpenAI-compatible API, llms.txt, and self-serve keys with a free tier.

[Website](https://groq.com) · [Source record](../data/providers/groq.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="groq-access"></a>

[Docs](https://console.groq.com/docs) · [API reference](https://console.groq.com/docs/api-reference) · [SDK](https://console.groq.com/docs/libraries)

—

### Service pricing

[Official pricing](https://groq.com/pricing)

### Task results

—

### Sources

—

<a id="hugging-face"></a>

## Hugging Face

Model hub and inference platform with fine-grained tokens, OAuth, an official MCP server, and a full Hub API.

[Website](https://huggingface.co) · [Source record](../data/providers/hugging-face.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="hugging-face-access"></a>

[Docs](https://huggingface.co/docs) · [API reference](https://huggingface.co/docs/hub/api) · [CLI](https://huggingface.co/docs/huggingface_hub/guides/cli) · [SDK](https://huggingface.co/docs/huggingface_hub) · [MCP entry](https://huggingface.co/mcp) · [MCP setup](https://huggingface.co/docs/hub/agents-mcp)

—

### Service pricing

[Official pricing](https://huggingface.co/pricing)

### Task results

—

### Notes

- MCP setup documentation checked on 2026-09-09: https://huggingface.co/docs/hub/agents-mcp. The server or product entry remains separately recorded in mcp_official.

### Sources

—

<a id="ignav"></a>

## Ignav Flights

Flight search and purchase-link API with email signup and an official MCP; individual eligibility remains untested.

[Website](https://ignav.com/) · [Source record](../data/candidates/ignav.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="ignav-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [public-playground (WEB)](https://ignav.com/playground) | [Docs](https://ignav.com/docs) | self serve | Public trial UI; limits and selectable markets may differ from the customer API. Experimental observations remain separate from catalog claims. |
| [flights-api (API)](https://ignav.com/docs) | [Docs](https://ignav.com/docs) | self serve | Requires: email_verification; Verify signup email |
| [official-mcp (MCP)](https://ignav.com/docs/mcp) | [Docs](https://ignav.com/docs/mcp) | — | Uses Ignav credentials. The API route records published account pricing; MCP tool billing and coverage need confirmation. |

### Service pricing

- flights-api: 1000 requests / one_time (free_allowance; One-time account allowance, not monthly.)

- flights-api: 2 USD / 1000 successful requests (usage; Successful HTTP 200 responses; search and booking-link retrieval are separate calls.)

### Setup observations

| Route | Starting resources | Setup tokens | Setup time | Human involvement |
| --- | --- | --- | --- | --- |
| Web | [No account or key supplied](../data/experiments/evaluations/codex-20260907T083644.877057Z-ignav.json) | — | — | — |
| API | — | — | — | — |
| MCP | — | — | — | — |

### Task results

#### Find flights from Milan to the Netherlands on September 25

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| Web | [1](./evaluations.md#comparison-45effe165cf4) | [100%](./evaluations.md#comparison-45effe165cf4) | 212.9k | $0.93 | $0 |
| API | — | — | — | — | — |
| MCP | — | — | — | — | — |

<details>
<summary>Task, conditions and evidence</summary>

September 25, 2026; depart from MXP, LIN or BGY and arrive at any passenger airport in the Netherlands; one adult, one-way, economy; connections allowed; use the service entry point specified for this trial.

**Completion:** At least one itinerary matches the date, route and passenger requirements. Key details agree with the real service response obtained by the runner. Only search results are assessed, not the lowest price across all sites or successful payment.

codex-cli 0.153.4 · gpt-6-astra / xhigh · 600s · 2026-09-07 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-45effe165cf4)

[Task definition](./tasks.en.md#flights-search-001-v1)

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| flights-search-001 v1 | Web | [completed](../data/experiments/evaluations/codex-20260907T083644.877057Z-ignav.json) | 2026-09-07 |

</details>

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

### Documentation and access <a id="jina-access"></a>

[Docs](https://docs.jina.ai) · [MCP entry](https://github.com/jina-ai/MCP)

—

### Service pricing

—

### Task results

—

### Sources

—

<a id="kayak-affiliate"></a>

## KAYAK Affiliate API

Affiliate flight APIs with a business application and an optional requested sandbox.

[Website](https://affiliates.kayak.com/) · [Source record](../data/candidates/kayak-affiliate.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="kayak-affiliate-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [affiliate-api (API)](https://developers.kayak.com/) | [Docs](https://developers.kayak.com/) | application | Requires: company, website, approval; Submit business application for review |

### Service pricing

—

### Task results

—

### Sources

- [official_site](https://affiliates.kayak.com/) — checked 2026-09-07
- [official_docs](https://developers.kayak.com/) — checked 2026-09-07

<a id="kiwi"></a>

## Kiwi.com

Flight search through a publicized MCP path and the separately gated Tequila partnership API.

[Website](https://www.kiwi.com/) · [Source record](../data/candidates/kiwi.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="kiwi-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [search-mcp (MCP)](https://mcp.kiwi.com) | [Docs](https://www.kiwi.com/en/pages/mcp/) | self serve | — |
| [tequila-api (API)](https://media.kiwi.com/articles-and-interviews/better-for-business-kiwi-com-takes-a-new-approach-to-partnerships/) | — | invite only | Requires: invitation; Keep invitation-only Tequila separate from the search MCP. Current endpoints and task coverage need further research. |

### Service pricing

—

### Setup observations

| Route | Starting resources | Setup tokens | Setup time | Human involvement |
| --- | --- | --- | --- | --- |
| MCP | [No account or key supplied](../data/experiments/evaluations/codex-20260907T092329.724439Z-kiwi.json) | — | — | — |
| API | — | — | — | — |

### Task results

#### Find flights from Milan to the Netherlands on September 25

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| MCP | [1](./evaluations.md#comparison-c77feef961a0) | [100%](./evaluations.md#comparison-c77feef961a0) | 209.6k | $0.84 | $0 |
| API | — | — | — | — | — |

<details>
<summary>Task, conditions and evidence</summary>

September 25, 2026; depart from MXP, LIN or BGY and arrive at any passenger airport in the Netherlands; one adult, one-way, economy; connections allowed; use the service entry point specified for this trial.

**Completion:** At least one itinerary matches the date, route and passenger requirements. Key details agree with the real service response obtained by the runner. Only search results are assessed, not the lowest price across all sites or successful payment.

codex-cli 0.153.4 · gpt-6-astra / xhigh · 600s · 2026-09-07 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-c77feef961a0)

[Task definition](./tasks.en.md#flights-search-001-v1)

</details>

<details>
<summary>Run history (3)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| flights-search-001 v1 | MCP | [completed](../data/experiments/evaluations/codex-20260907T092329.724439Z-kiwi.json) | 2026-09-07 |
| flights-search-001 v1 | MCP | [invalid_run](../data/experiments/evaluations/codex-20260907T091621.435575Z-kiwi.json) | 2026-09-07 |
| flights-search-001 v1 | MCP | [completed](../data/experiments/evaluations/codex-20260907T083627.884537Z-kiwi.json) | 2026-09-07 |

</details>

### Sources

- [official_docs](https://www.kiwi.com/en/pages/mcp/) — checked 2026-09-07
- [official_announcement](https://media.kiwi.com/articles-and-interviews/better-for-business-kiwi-com-takes-a-new-approach-to-partnerships/) — checked 2026-09-07

<a id="lark"></a>

## Lark

Collaboration suite (messaging, docs, calendar) with an open platform, llms.txt, an official CLI with 200+ commands and agent skills, and an official OpenAPI MCP server.

[Website](https://www.larksuite.com) · [Source record](../data/providers/lark.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="lark-access"></a>

[Docs](https://open.larksuite.com/document/home/index) · [API reference](https://open.larksuite.com/document/server-docs/getting-started/server-api-list)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [base-api (API)](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create) | [Docs](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create.md) | self serve | Requires a platform app, authorized identity and Base scopes/resource permissions. Ordinary-person onboarding from a fresh account is not tested. |
| [official-cli (CLI)](https://github.com/larksuite/cli) | [Docs](https://github.com/larksuite/cli) | self serve | Official CLI covers Base and supports individuals. Account signup, app creation and permission setup still need separate verification. |
| [official-mcp (MCP)](https://github.com/larksuite/lark-openapi-mcp) | [Docs](https://github.com/larksuite/lark-openapi-mcp) | self serve | Local official MCP package uses platform app credentials; identity and tenant domains must match. |

### Service pricing

[Official pricing](https://www.larksuite.com/en_us/plans)

- base-api: 2000 rows / table (free_allowance; Starter Base table limit; access still depends on tenant/app scopes.)

### Task results

—

### Sources

- [official_docs](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create.md) — checked 2026-09-08
- [official_repo](https://github.com/larksuite/cli) — checked 2026-09-08
- [official_repo](https://github.com/larksuite/lark-openapi-mcp) — checked 2026-09-08
- [official_site](https://www.larksuite.com/en_us/plans) — checked 2026-09-08

<a id="lemonsqueezy"></a>

## Lemon Squeezy

Merchant-of-record payments for digital products/SaaS with a JSON:API REST API, documented test mode, and self-serve keys.

[Website](https://www.lemonsqueezy.com) · [Source record](../data/providers/lemonsqueezy.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="lemonsqueezy-access"></a>

[Docs](https://docs.lemonsqueezy.com) · [API reference](https://docs.lemonsqueezy.com/api)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [sandbox-api (API)](https://docs.lemonsqueezy.com/guides/developer-guide/taking-payments) | [Docs](https://docs.lemonsqueezy.com/guides/developer-guide/taking-payments) | — | Requires: platform_account; Use test-mode products and API keys; test resources do not automatically become live products. Store activation and live merchant eligibility must be checked separately. Merchant-of-record checkout applies to digital products/SaaS. |

### Service pricing

[Official pricing](https://www.lemonsqueezy.com/pricing)

### Task results

—

### Sources

- [official_docs](https://docs.lemonsqueezy.com/help/getting-started/test-mode) — checked 2026-09-08
- [official_docs](https://docs.lemonsqueezy.com/guides/developer-guide/taking-payments) — checked 2026-09-08

<a id="letsfg"></a>

## LetsFG Personal Flight Search

Personal flight search through MCP, CLI and SDKs, with a human payment-method authorization step.

[Website](https://letsfg.co/) · [Source record](../data/candidates/letsfg.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="letsfg-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [personal-mcp (MCP)](https://letsfg.co/for-agents) | [Docs](https://letsfg.co/for-agents) | documented | Requires: payment_method; Complete browser consent and connect a payment method |
| [personal-cli (CLI)](https://github.com/letsfg/letsfg) | [Docs](https://github.com/letsfg/letsfg) | — | Official repository advertises this interface (Python/JS for SDK). Installation version, current auth compatibility and route-specific gates remain unverified due to documentation drift. |
| [personal-sdk (SDK)](https://github.com/letsfg/letsfg) | [Docs](https://github.com/letsfg/letsfg) | — | Official repository advertises this interface (Python/JS for SDK). Installation version, current auth compatibility and route-specific gates remain unverified due to documentation drift. |

### Service pricing

- personal-mcp: 0 USD / search (usage; Personal flight-search claim only; excludes booking, payment authorization and the separate Developer API.)

### Task results

—

### Sources

- [official_docs](https://letsfg.co/for-agents) — checked 2026-09-07
- [official_repo](https://github.com/letsfg/letsfg) — checked 2026-09-07

<a id="linear"></a>

## Linear

Issue tracking and product planning with a GraphQL API, llms.txt, an official MCP server, and webhooks.

[Website](https://linear.app) · [Source record](../data/providers/linear.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="linear-access"></a>

[Docs](https://linear.app/developers) · [MCP entry](https://linear.app/docs/mcp)

—

### Service pricing

[Official pricing](https://linear.app/pricing)

### Task results

—

### Sources

—

<a id="lufthansa-partner"></a>

## Lufthansa Partner Fare API

Lufthansa fare methods are partner-scoped; the developer portal currently pauses new Open API registrations.

[Website](https://developer.lufthansa.com/page) · [Source record](../data/candidates/lufthansa-partner.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="lufthansa-partner-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [open-api-registration (API)](https://developer.lufthansa.com/page) | — | paused | Public schedule and status APIs are not evidence of consumer fare-search capability. |
| [partner-offers-api (API)](https://developer.lufthansa.com/docs/read/api_partner/offers) | [Docs](https://developer.lufthansa.com/docs/read/api_partner/offers) | — | Public schedule/status APIs do not establish fare-search access. A readable registration form does not override the pause notice. |

### Service pricing

—

### Task results

—

### Sources

- [official_announcement](https://developer.lufthansa.com/page) — checked 2026-09-07
- [official_docs](https://developer.lufthansa.com/docs) — checked 2026-09-07
- [official_docs](https://developer.lufthansa.com/docs/read/api_partner/offers) — checked 2026-09-07

<a id="luma"></a>

## Luma AI (Dream Machine)

Dream Machine video and image generation via the Luma API, with llms.txt and published API pricing.

[Website](https://lumalabs.ai) · [Source record](../data/providers/luma.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="luma-access"></a>

[Docs](https://docs.lumalabs.ai) · [API reference](https://docs.lumalabs.ai/reference)

—

### Service pricing

[Official pricing](https://lumalabs.ai/api/pricing)

### Task results

—

### Sources

—

<a id="mem0"></a>

## Mem0

Memory layer for AI agents (hosted platform + open-source), with REST API, llms.txt, and the official OpenMemory MCP server.

[Website](https://mem0.ai) · [Source record](../data/providers/mem0.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="mem0-access"></a>

[Docs](https://docs.mem0.ai) · [API reference](https://docs.mem0.ai/api-reference) · [MCP entry](https://docs.mem0.ai/openmemory/overview)

—

### Service pricing

[Official pricing](https://mem0.ai/pricing)

### Task results

—

### Sources

—

<a id="minimax"></a>

## MiniMax

MiniMax text, speech, video and music models via the international platform API, with an official MCP server.

[Website](https://platform.minimax.io) · [Source record](../data/providers/minimax.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="minimax-access"></a>

[Docs](https://platform.minimax.io/docs) · [API reference](https://platform.minimax.io/docs/api-reference) · [MCP entry](https://github.com/MiniMax-AI/MiniMax-MCP)

—

### Service pricing

—

### Task results

—

### Sources

—

<a id="mistral"></a>

## Mistral AI

European LLM provider (La Plateforme) with llms.txt, an open OpenAPI-based docs repo, a free experiment tier, and self-serve keys.

[Website](https://mistral.ai) · [Source record](../data/providers/mistral.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="mistral-access"></a>

[Docs](https://docs.mistral.ai) · [API reference](https://docs.mistral.ai/api) · [SDK](https://docs.mistral.ai/getting-started/clients)

—

### Service pricing

[Official pricing](https://mistral.ai/pricing)

### Task results

—

### Sources

—

<a id="modal"></a>

## Modal

Serverless compute for Python with first-class Sandboxes for agent code execution, llms.txt, and an official CLI.

[Website](https://modal.com) · [Source record](../data/providers/modal.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="modal-access"></a>

[Docs](https://modal.com/docs) · [API reference](https://modal.com/docs/reference) · [CLI](https://modal.com/docs/reference/cli)

—

### Service pricing

[Official pricing](https://modal.com/pricing)

### Task results

—

### Sources

—

<a id="mollie"></a>

## Mollie

Payment links and payment APIs with isolated test mode and a simulated checkout screen.

[Website](https://www.mollie.com/) · [Source record](../data/candidates/mollie.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="mollie-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [sandbox-api (API)](https://docs.mollie.com/reference/create-payment-link) | [Docs](https://docs.mollie.com/reference/create-payment-link) | — | Requires: platform_account; Uses a Test API key (or testmode with supported tokens). Test checkout is a simulator, not the live payment page. Account admission and live payment-method activation remain prerequisites to check separately. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://docs.mollie.com/reference/create-payment-link) — checked 2026-09-08
- [official_docs](https://docs.mollie.com/reference/testing) — checked 2026-09-08
- [official_docs](https://docs.mollie.com/reference/authentication) — checked 2026-09-08

<a id="mongodb-atlas"></a>

## MongoDB Atlas

Managed MongoDB with a versioned Admin API, published OpenAPI spec, llms.txt, official CLI and MCP server.

[Website](https://www.mongodb.com/products/platform/atlas-database) · [Source record](../data/providers/mongodb-atlas.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="mongodb-atlas-access"></a>

[Docs](https://www.mongodb.com/docs/atlas/) · [API reference](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/) · [CLI](https://www.mongodb.com/docs/atlas/cli/) · [SDK](https://www.mongodb.com/docs/drivers/) · [MCP entry](https://github.com/mongodb-js/mongodb-mcp-server)

—

### Service pricing

[Official pricing](https://www.mongodb.com/pricing)

### Task results

—

### Sources

—

<a id="moonshot"></a>

## Moonshot AI (Kimi)

Kimi models (K2 line) via an OpenAI-compatible API on the international Kimi platform, with an official terminal CLI agent (kimi-cli).

[Website](https://platform.kimi.ai) · [Source record](../data/providers/moonshot.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="moonshot-access"></a>

[Docs](https://platform.kimi.ai/docs) · [API reference](https://platform.kimi.ai/docs/api/chat) · [CLI](https://github.com/MoonshotAI/kimi-cli)

—

### Service pricing

—

### Task results

—

### Sources

—

<a id="n8n"></a>

## n8n

Workflow automation platform with native AI/agent nodes, a public REST API, official hosted MCP server, CLI, and llms.txt; fair-code and self-hostable.

[Website](https://n8n.io) · [Source record](../data/providers/n8n.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="n8n-access"></a>

[Docs](https://docs.n8n.io) · [API reference](https://docs.n8n.io/api/) · [CLI](https://docs.n8n.io/hosting/cli-commands/) · [MCP entry](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)

—

### Service pricing

[Official pricing](https://n8n.io/pricing)

### Task results

—

### Sources

—

<a id="neon"></a>

## Neon

Serverless Postgres with instant branching, a full management API, official MCP server, and agent-oriented docs.

[Website](https://neon.com) · [Source record](../data/providers/neon.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="neon-access"></a>

[Docs](https://neon.com/docs) · [API reference](https://api-docs.neon.tech) · [CLI](https://neon.com/docs/reference/neon-cli) · [MCP entry](https://github.com/neondatabase/mcp-server-neon)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [ephemeral-api (API)](https://neon.new/) | — | documented | No-account, 72-hour ephemeral hosted Postgres. Tests can establish short-term persistence only; this is not a permanent free production database. Connection strings and claim URLs are private credentials. |

### Service pricing

[Official pricing](https://neon.com/pricing)

### Setup observations

| Route | Starting resources | Setup tokens | Setup time | Human involvement |
| --- | --- | --- | --- | --- |
| API | [No account or key supplied](../data/experiments/evaluations/codex-20260907T112258.549053Z-neon.json) | — | — | — |

### Task results

#### Prepare a separate remote database for my personal todo app and verify adding, updating and reading todos after reconnecting

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-fdecec09a4b6) | [100%](./evaluations.md#comparison-fdecec09a4b6) | 465.4k | — | $0 |

<details>
<summary>Task, conditions and evidence</summary>

Synthetic test data only: id=1,title=Buy milk,done=false; id=2,title=Read book,done=false; id=3,title=Walk dog,done=true. Insert all three, then set done=true for id=2. A temporary database requiring no payment may be created; existing projects must not be modified.

**Completion:** Data is actually saved and updated in the specified service's remote database. A fresh process reads back all three items with unchanged titles; only id=1 is incomplete, with three total and two completed. Evidence establishes an independent connection and remote execution. Credentials stay in private workspace files and must not appear in evidence or the final answer. Temporary resources are acceptable if their expiry is disclosed.

codex-cli 0.153.4 · gpt-6-astra / xhigh · 600s · 2026-09-07 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-fdecec09a4b6)

[Task definition](./tasks.en.md#database-todos-001-v1)

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| database-todos-001 v1 | API | [completed](../data/experiments/evaluations/codex-20260907T112258.549053Z-neon.json) | 2026-09-07 |

</details>

### Sources

- [official_site](https://neon.new/) — checked 2026-09-07
- [official_announcement](https://neon.com/blog/neon-launchpad) — checked 2026-09-07

<a id="netlify"></a>

## Netlify

Web platform for deploying sites and functions, with an OpenAPI-specified API, llms.txt, official CLI and MCP server.

[Website](https://www.netlify.com) · [Source record](../data/providers/netlify.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="netlify-access"></a>

[Docs](https://docs.netlify.com) · [API reference](https://open-api.netlify.com) · [CLI](https://docs.netlify.com/cli/get-started/) · [MCP entry](https://docs.netlify.com/welcome/build-with-ai/netlify-mcp-server/)

—

### Service pricing

[Official pricing](https://www.netlify.com/pricing/)

### Task results

—

### Sources

—

<a id="notion"></a>

## Notion

Connected workspace with a versioned REST API, capability-scoped integrations, llms.txt, and an official MCP server.

[Website](https://www.notion.com) · [Source record](../data/providers/notion.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="notion-access"></a>

[Docs](https://developers.notion.com) · [MCP entry](https://developers.notion.com/docs/mcp)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [rest-api (API)](https://developers.notion.com/reference/intro) | [Docs](https://developers.notion.com/reference/intro) | self serve / documented | Create internal connection and grant only the test page, or create a PAT in a dedicated test workspace.; Internal connection requires workspace owner creation and explicit page sharing; PAT acts with creator permissions in the selected workspace. Free-plan PAT creation is restricted to workspace owners; being a free member alone is insufficient. |
| [javascript-sdk (SDK)](https://github.com/makenotion/notion-sdk-js) | [Docs](https://github.com/makenotion/notion-sdk-js) | self serve | Official client library over the REST API; credentials and resource grants remain necessary. |
| [official-cli (CLI)](https://developers.notion.com/cli/get-started/overview) | [Docs](https://developers.notion.com/cli/get-started/overview) | self serve | Official CLI discovered in current docs; measure separately from raw REST. |
| [hosted-mcp (MCP)](https://mcp.notion.com/mcp) | [Docs](https://developers.notion.com/guides/mcp/get-started-with-mcp) | self serve | Official hosted MCP requires interactive OAuth. Token-based open-source server is no longer actively maintained. |

### Service pricing

[Official pricing](https://www.notion.com/pricing)

- rest-api: 0 USD / month (free_allowance; Free workspace subscription; API limits and resource permissions still apply.)

### Setup observations

| Route | Starting resources | Setup tokens | Setup time | Human involvement |
| --- | --- | --- | --- | --- |
| API | [Credentials supplied before trial](../data/experiments/evaluations/codex-20260908T035504.906378Z-notion.json) | — | — | — |
| SDK | — | — | — | — |
| CLI | — | — | — | — |
| MCP | — | — | — | — |

### Task results

#### Turn the action items in these book-club meeting notes into an online task table, give me its link, and tell me what is still unfinished and when each item is due

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-6203194a76cd) | [100%](./evaluations.md#comparison-6203194a76cd) | 215.5k | $0.75 | $0 |
| SDK | — | — | — | — | — |
| CLI | — | — | — | — | — |
| MCP | — | — | — | — | — |

<details>
<summary>Task, conditions and evidence</summary>

Book-club planning meeting, September 8, 2026: Lin Qing will confirm the venue by September 15; Zhou Zhou will prepare the reading list by September 16; Chen He will make the poster, originally due September 18. All three were unfinished during the meeting. Follow-up: Zhou Zhou has finished the reading list, and the poster deadline has moved to September 20. Everything else stays the same.

**Completion:** The remote table contains exactly three actions with correct owners and final deadlines. The reading list is complete and the other two are incomplete. The answer links to the table and correctly lists the two unfinished items and their dates. The evaluator independently verifies the data through the service API. Fields and operation order are unrestricted; inserting the old state first or producing evidence files is not required.

codex-cli 0.153.4 · gpt-6-astra / xhigh · 600s · 2026-09-08 (UTC)

Credentials supplied · [Full configuration and evidence](./evaluations.md#comparison-6203194a76cd)

[Task definition](./tasks.en.md#collaborative-tables-001-v2)

</details>

<details>
<summary>Run history (2)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| collaborative-tables-001 v2 | API | [completed](../data/experiments/evaluations/codex-20260908T035504.906378Z-notion.json) | 2026-09-08 |
| collaborative-tables-001 v1 | API | [completed](../data/experiments/evaluations/codex-20260908T032850.330773Z-notion.json) | 2026-09-08 |

</details>

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

### Documentation and access <a id="openai-access"></a>

[Docs](https://developers.openai.com/api/docs) · [API reference](https://platform.openai.com/docs/api-reference) · [SDK](https://platform.openai.com/docs/libraries)

—

### Service pricing

[Official pricing](https://platform.openai.com/docs/pricing)

### Task results

—

### Sources

—

<a id="openrouter"></a>

## OpenRouter

Unified OpenAI-compatible API over hundreds of models from many labs, with one key, per-model pricing, automatic fallbacks, and an llms.txt.

[Website](https://openrouter.ai) · [Source record](../data/providers/openrouter.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="openrouter-access"></a>

[Docs](https://openrouter.ai/docs) · [API reference](https://openrouter.ai/docs/api-reference/overview)

—

### Service pricing

[Official pricing](https://openrouter.ai/models)

### Task results

—

### Sources

—

<a id="paas-build"></a>

## paas.build

Agent-native payment facilitator (the AI-builder product of UniPaaS, FCA-authorised No. 929994) — opens a real merchant account via progressive KYB and creates checkouts through MCP or REST.

[Website](https://paas.build) · [Source record](../data/candidates/paas-build.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="paas-build-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [rest-api (API)](https://paas.build/openapi.json) | [Docs](https://paas.build/SKILL.md) | restricted | PayFac powered by UniPaaS; merchant retains tax responsibilities. Official materials limit onboarding to UK/EU/US merchants. Sandbox and production tokens differ. A 2026-09-08 sandbox-only account and token were prepared successfully. A fresh Codex trial created a remote checkout but hit a browser launch permission failure, so it is invalid for completion-rate comparison. Independent browser review showed only the checkout shell; customer usability remains unverified. |
| [official-mcp (MCP)](https://paas.build/mcp) | [Docs](https://paas.build/agents) | — | Discovery verified four tools on 2026-09-08. Default onboarding can provision both environments and send notifications; explicitly prepare sandbox-only access. Protocol discovery is not task completion. |

### Service pricing

[Official pricing](https://paas.build/pricing)

### Setup observations

| Route | Starting resources | Setup tokens | Setup time | Human involvement |
| --- | --- | --- | --- | --- |
| API | [Credentials supplied before trial](../data/experiments/evaluations/codex-20260908T113239.160717Z-paas-build.json) | — | — | — |
| MCP | — | — | — | — |

### Task results

#### I want to sell an ebook titled “城市散步指南” for a one-time price of 12 USD. Set up its checkout page in the test environment and give me a link customers can open.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [0](./evaluations.md#comparison-bc10c53a81ca) | — | — | — | — |
| MCP | — | — | — | — | — |

<details>
<summary>Task, conditions and evidence</summary>

Ebook title: 城市散步指南; price 12 USD; one-time charge; quantity 1. Delivering the ebook file is not required.

**Completion:** The evaluator independently reads the remote product, order or checkout resource and opens the returned link. The name, 12 USD base price, quantity 1 and one-time charge must match, and the page must allow proceeding to simulated payment. Any dynamic taxes are shown separately; successful payment is not required.

codex-cli 0.153.4 · gpt-6-astra / xhigh · 600s · 2026-09-08 (UTC)

Credentials supplied · [Full configuration and evidence](./evaluations.md#comparison-bc10c53a81ca)

[Task definition](./tasks.en.md#payment-acceptance-001-v1)

Invalid runs: 1

- API: [Invalid run](../data/experiments/evaluations/codex-20260908T113239.160717Z-paas-build.json) — The executor created a real sandbox checkout, but macOS sandbox permissions prevented Chromium from launching. Exclude this trial from service completion-rate comparisons. Independent post-run browser inspection also showed only the checkout shell, without the product, amount or payment form; this is a separate observed usability issue requiring a fresh run after environment repair.

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| payment-acceptance-001 v1 | API | [invalid_run](../data/experiments/evaluations/codex-20260908T113239.160717Z-paas-build.json) | 2026-09-08 |

</details>

### Notes

- Sandbox preparation on 2026-09-08 used env=sandbox and notify=false. The API returned a sandbox vendor token with acceptPayments=true and no production account; whoami returned HTTP 200 with env=sandbox. No identity verification, address or real payment was needed for this sandbox setup. This does not establish production eligibility. The first task trial is an invalid run because the executor could not launch Chromium.
- Maintenance review 2026-09-08: issue #5 is partially fixed. Invalid-vendor checkout now returns 401; whoami rejects missing/invalid tokens correctly. Missing checkout vendorId still returns the old HTTP 400 error shape. Evidence: https://github.com/Olorinm/agent-friendly-services/blob/main/data/maintenance/paas-build-2026-09-08.json.
- OpenAPI documents whoami, but current SKILL.md and llms.txt omit it. Remote MCP discovery succeeds and lists four tools (add_payments, identify_business, go_live, create_checkout), without whoami. Protocol discovery and invalid-credential probes are not successful user-task evaluations.
- Official documentation limits merchant onboarding to UK/EU/US-based businesses or individuals. The merchant remains responsible for VAT/sales tax. Exact eligibility, identity checks, refund/dispute fees and valid-token behavior remain unverified in this review.
- The official MCP source defaults add_payments to provisioning both sandbox and production and to sending notifications. A sandbox benchmark must explicitly constrain the environment and record real account/identity prerequisites; synthetic test details are restricted to sandbox resources and must not be used to activate production merchants.

### Sources

- [official_docs](https://paas.build/SKILL.md) — checked 2026-09-08
- [official_docs](https://paas.build/openapi.json) — checked 2026-09-08
- [official_site](https://paas.build/accept-payments-without-a-company) — checked 2026-09-08
- [official_site](https://paas.build/pricing) — checked 2026-09-08
- [official_site](https://paas.build/mcp) — checked 2026-09-08

<a id="paddle"></a>

## Paddle

Merchant-of-record billing platform with a versioned API, full sandbox, llms.txt, and webhooks.

[Website](https://www.paddle.com) · [Source record](../data/providers/paddle.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="paddle-access"></a>

[Docs](https://developer.paddle.com) · [API reference](https://developer.paddle.com/api-reference/overview) · [MCP entry](https://github.com/PaddleHQ/paddle-mcp-server)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [sandbox-api (API)](https://developer.paddle.com/sdks/sandbox/) | [Docs](https://developer.paddle.com/sdks/sandbox/) | self serve | Requires: platform_account; Register the separate sandbox account and obtain its API key.; Create a separate sandbox account with sandbox credentials. Sandbox does not require the domain and checkout approvals needed for live sales. Merchant-of-record responsibilities and live account review differ from payment processing alone. On 2026-09-09, sandbox email verification completed and a seven-day API key was created with scoped permissions. An authenticated sandbox products read returned HTTP 200 with an empty catalog. No KYC, production activation or payment was performed. Account setup alone is not a completed checkout task. The first ebook checkout task was not completed: POST /products rejected ebooks with product_tax_category_not_approved. The authenticated sandbox dashboard showed eBook Not Requested and SaaS Approved, with a notice that category approval must be requested in a live account. No live application was made. This result concerns the default account and ebook scenario, not approved categories or all Paddle checkouts. |

### Service pricing

[Official pricing](https://www.paddle.com/pricing)

### Setup observations

| Route | Starting resources | Setup tokens | Setup time | Human involvement |
| --- | --- | --- | --- | --- |
| API | [Credentials supplied before trial](../data/experiments/evaluations/codex-20260909T032011.000426Z-paddle.json) | — | — | — |

### Task results

#### I want to sell an ebook titled “城市散步指南” for a one-time price of 12 USD. Set up its checkout page in the test environment and give me a link customers can open.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-1149cab0b0f0) | [0%](./evaluations.md#comparison-1149cab0b0f0) | 455.2k | $1.20 | $0 |

<details>
<summary>Task, conditions and evidence</summary>

Ebook title: 城市散步指南; price 12 USD; one-time charge; quantity 1. Delivering the ebook file is not required.

**Completion:** The evaluator independently reads the remote product, order or checkout resource and opens the returned link. The name, 12 USD base price, quantity 1 and one-time charge must match, and the page must allow proceeding to simulated payment. Any dynamic taxes are shown separately; successful payment is not required.

codex-cli 0.153.4 · gpt-6-astra / xhigh · 600s · 2026-09-09 (UTC)

Credentials supplied · [Full configuration and evidence](./evaluations.md#comparison-1149cab0b0f0)

[Task definition](./tasks.en.md#payment-acceptance-001-v1)

- API: [Not completed](../data/experiments/evaluations/codex-20260909T032011.000426Z-paddle.json) — The default newly registered Paddle sandbox account rejected creation of the ebook product with product_tax_category_not_approved for ebooks. No product, transaction or customer checkout link was created. This is an account/category access barrier for this scenario, not evidence that Paddle cannot serve any product or approved account. The dedicated browser connected successfully but had no dashboard login, as disclosed. Independent authenticated dashboard inspection shows eBook Not Requested, SaaS Approved, and a notice that category approval must be requested in the live account; no live application was made.

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| payment-acceptance-001 v1 | API | [not_completed](../data/experiments/evaluations/codex-20260909T032011.000426Z-paddle.json) | 2026-09-09 |

</details>

### Sources

- [official_docs](https://developer.paddle.com/sdks/sandbox/) — checked 2026-09-08
- [official_docs](https://developer.paddle.com/get-started/quickstart/) — checked 2026-09-08

<a id="paypal"></a>

## PayPal

Online payment acceptance through Orders API and buyer approval checkout; separate sandbox buyer and business seller accounts.

[Website](https://www.paypal.com/) · [Source record](../data/candidates/paypal.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="paypal-access"></a>

[Docs](https://developer.paypal.com/api/rest/postman/)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [sandbox-api (API)](https://developer.paypal.com/api/rest) | [Docs](https://developer.paypal.com/api/rest) | self serve | Requires: platform_account; Create a developer account and obtain sandbox app client credentials.; Developer dashboard supplies sandbox buyer and seller accounts and app credentials. Going live requires a Business account; merchant country and personal eligibility need separate checks. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://developer.paypal.com/api/rest) — checked 2026-09-08
- [official_docs](https://developer.paypal.com/sandbox-testing/overview/) — checked 2026-09-08
- [official_docs](https://developer.paypal.com/api/rest/postman/) — checked 2026-09-08

<a id="perplexity"></a>

## Perplexity API

Sonar API for web-grounded answers and search, with llms.txt, an official MCP server, and documented usage tiers.

[Website](https://www.perplexity.ai) · [Source record](../data/providers/perplexity.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="perplexity-access"></a>

[Docs](https://docs.perplexity.ai) · [MCP entry](https://github.com/ppl-ai/modelcontextprotocol)

—

### Service pricing

[Official pricing](https://docs.perplexity.ai/getting-started/pricing)

### Task results

—

### Sources

—

<a id="pinecone"></a>

## Pinecone

Managed vector database for search and RAG, with llms.txt, an official MCP server, and self-serve keys.

[Website](https://www.pinecone.io) · [Source record](../data/providers/pinecone.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="pinecone-access"></a>

[Docs](https://docs.pinecone.io) · [API reference](https://docs.pinecone.io/reference/api/introduction) · [CLI](https://github.com/pinecone-io/cli) · [MCP entry](https://docs.pinecone.io/guides/operations/mcp-server)

—

### Service pricing

[Official pricing](https://www.pinecone.io/pricing/)

### Task results

—

### Sources

—

<a id="pingxx"></a>

## Ping++

Unified payment integration across payment channels, with API keys, a web SDK and simulated test transactions.

[Website](https://www.pingxx.com/) · [Source record](../data/candidates/pingxx.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="pingxx-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [sandbox-api (API)](https://www.pingxx.com/api/%E8%AE%A4%E8%AF%81.html) | [Docs](https://www.pingxx.com/api/%E8%AE%A4%E8%AF%81.html) | — | Requires: platform_account; Dashboard provides separate test/live API keys; test transactions are documented as simulated and without actual transaction fees. Channel-specific merchant permissions may still be needed for live use. Current individual admission and channel fees need verification. |
| [web-sdk (SDK)](https://www.pingxx.com/docs/client/web.html) | [Docs](https://www.pingxx.com/docs/client/web.html) | — | Web SDK consumes server-created Charge credentials and invokes the selected payment channel. This is not a separate merchant account or a waiver of channel admission. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://www.pingxx.com/api/%E8%AE%A4%E8%AF%81.html) — checked 2026-09-08
- [official_docs](https://www.pingxx.com/docs/client/web.html) — checked 2026-09-08
- [official_site](https://www.pingxx.com/wiki/alipayapps) — checked 2026-09-08

<a id="planetscale"></a>

## PlanetScale

PostgreSQL single-node plans start at USD 5/month. No free writable database allowance verified; not provisioned in this no-payment round. Public pricing SQL is read-only and does not meet the task.

[Website](https://planetscale.com/) · [Source record](../data/candidates/planetscale.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="planetscale-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [database-cli (CLI)](https://planetscale.com/docs/cli) | [Docs](https://planetscale.com/docs/cli) | self serve / documented | PostgreSQL single-node plans start at USD 5/month. No free writable database allowance verified; not provisioned in this no-payment round. Public pricing SQL is read-only and does not meet the task. |

### Service pricing

- database-cli: 5 USD / month (minimum_spend; Postgres single-node starting plan; configuration, region and other resources may cost more.)

### Task results

—

### Sources

- [official_docs](https://planetscale.com/docs/cli) — checked 2026-09-07
- [official_site](https://planetscale.com/pricing) — checked 2026-09-07

<a id="polar"></a>

## Polar

Merchant-of-record service for digital products, with checkout APIs and a separate developer sandbox.

[Website](https://polar.sh/) · [Source record](../data/candidates/polar.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="polar-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [sandbox-api (API)](https://polar.sh/docs/integrate/sandbox) | [Docs](https://polar.sh/docs/integrate/sandbox) | self serve | Requires: platform_account; Create a sandbox account and organization, then issue sandbox credentials.; Create a separate sandbox account and organization; production credentials cannot be reused. Sandbox customer email delivery is restricted. Live payouts depend on Polar's supported seller countries and Stripe Connect Express, not the Stripe Payments country list. |

### Service pricing

[Official pricing](https://polar.sh/)

### Task results

—

### Notes

- Pricing checked 2026-09-08: new organizations on Starter pay a published 5% + USD 0.50 per transaction. Older Early Member pricing and paid plans differ; international-card, payout and dispute fees may apply. This is a published pricing claim, not a measured sandbox charge.

### Sources

- [official_docs](https://polar.sh/docs/integrate/sandbox) — checked 2026-09-08
- [official_docs](https://docs.polar.sh/documentation/polar-as-merchant-of-record/supported-countries) — checked 2026-09-08
- [official_site](https://polar.sh/) — checked 2026-09-08
- [official_announcement](https://polar.sh/blog/introducing-polar-plans) — checked 2026-09-08

<a id="postman"></a>

## Postman

API development platform with a public Postman API, llms.txt, official CLI, and self-serve keys.

[Website](https://www.postman.com) · [Source record](../data/providers/postman.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="postman-access"></a>

[Docs](https://learning.postman.com) · [API reference](https://learning.postman.com/docs/developer/postman-api/intro-api/) · [CLI](https://learning.postman.com/docs/postman-cli/postman-cli-overview/) · [MCP entry](https://github.com/postmanlabs/postman-mcp-server)

—

### Service pricing

[Official pricing](https://www.postman.com/pricing/)

### Task results

—

### Sources

—

<a id="qdrant"></a>

## Qdrant

Open-source vector database with a managed cloud, llms.txt, an official MCP server, and a free cluster tier.

[Website](https://qdrant.tech) · [Source record](../data/providers/qdrant.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="qdrant-access"></a>

[Docs](https://qdrant.tech/documentation) · [API reference](https://api.qdrant.tech) · [SDK](https://qdrant.tech/documentation/interfaces) · [MCP entry](https://github.com/qdrant/mcp-server-qdrant)

—

### Service pricing

[Official pricing](https://qdrant.tech/pricing)

### Task results

—

### Sources

—

<a id="railway"></a>

## Railway

App/database hosting with a public GraphQL API, official CLI, llms.txt, and usage-based pricing.

[Website](https://railway.com) · [Source record](../data/providers/railway.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="railway-access"></a>

[Docs](https://docs.railway.com) · [API reference](https://docs.railway.com/reference/public-api) · [CLI](https://github.com/railwayapp/cli)

—

### Service pricing

[Official pricing](https://railway.com/pricing)

### Task results

—

### Sources

—

<a id="razorpay"></a>

## Razorpay

Payment Links API for collecting specified amounts through hosted checkout, including a documented test mode.

[Website](https://razorpay.com/) · [Source record](../data/candidates/razorpay.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="razorpay-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [payment-links-api (API)](https://razorpay.com/docs/api/payments/payment-links/create-standard/) | [Docs](https://razorpay.com/docs/api/payments/payment-links/create-standard/) | — | Documentation limits test-mode creation to 30 payment links per business before contacting support. API-key access, merchant geography, KYC and production eligibility need preparation checks; a documented test endpoint does not establish individual admission. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://razorpay.com/docs/api/payments/payment-links/create-standard/) — checked 2026-09-08

<a id="redis"></a>

## Redis (Redis Cloud)

In-memory data platform for caching, vector search and real-time apps; Redis Cloud has a REST management API, official MCP server, redis-cli, and llms.txt.

[Website](https://redis.io) · [Source record](../data/providers/redis.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="redis-access"></a>

[Docs](https://redis.io/docs/latest) · [API reference](https://redis.io/docs/latest/operate/rc/api/) · [CLI](https://redis.io/docs/latest/develop/tools/cli/) · [MCP entry](https://github.com/redis/mcp-redis)

—

### Service pricing

[Official pricing](https://redis.io/pricing)

### Task results

—

### Sources

—

<a id="render"></a>

## Render

Cloud hosting for web services, static sites and databases with a REST API, official CLI, official MCP server, and llms.txt.

[Website](https://render.com) · [Source record](../data/providers/render.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="render-access"></a>

[Docs](https://render.com/docs) · [API reference](https://api-docs.render.com/reference/introduction) · [CLI](https://github.com/render-oss/cli) · [MCP entry](https://github.com/render-oss/render-mcp-server)

—

### Service pricing

[Official pricing](https://render.com/pricing)

### Task results

—

### Notes

- The docs llms.txt directs agents to an official hosted MCP endpoint: https://mcp.render.com/mcp (authenticated account-scoped actions).

### Sources

—

<a id="replicate"></a>

## Replicate

Run and fine-tune open-source models via a simple predictions API, with llms.txt, webhooks, and an official CLI.

[Website](https://replicate.com) · [Source record](../data/providers/replicate.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="replicate-access"></a>

[Docs](https://replicate.com/docs) · [API reference](https://replicate.com/docs/reference/http) · [CLI](https://github.com/replicate/cli) · [SDK](https://replicate.com/docs/reference/client-libraries)

—

### Service pricing

[Official pricing](https://replicate.com/pricing)

### Task results

—

### Sources

—

<a id="resend"></a>

## Resend

Email API for developers with test mode, scoped API keys, idempotency support, and an official MCP server.

[Website](https://resend.com) · [Source record](../data/providers/resend.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="resend-access"></a>

[Docs](https://resend.com/docs) · [API reference](https://resend.com/docs/api-reference/introduction) · [SDK](https://resend.com/docs/sdks) · [MCP entry](https://github.com/resend/mcp-send-email)

—

### Service pricing

[Official pricing](https://resend.com/pricing)

### Task results

—

### Sources

—

<a id="sabre-air"></a>

## Sabre Air APIs

Air API workflows with assigned credentials, plus a separately researched Agentic API/MCP lead.

[Website](https://developer.sabre.com/) · [Source record](../data/candidates/sabre-air.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="sabre-air-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [air-workflow-api (API)](https://github.com/SabreDevStudio/SabreAPIsWorkflows/blob/master/SabreAPIsTestSuites/README.md) | [Docs](https://github.com/SabreDevStudio/SabreAPIsWorkflows/blob/master/SabreAPIsTestSuites/README.md) | application | Contact sales to obtain EPR, IPCC and password; This older workflow is evidence for its own credential path only. |
| [agentic-mcp-lead (MCP)](https://developer.sabre.com/) | — | — | Current developer homepage advertises Agentic API/MCP. Exact product, tools and onboarding need research; do not copy legacy workflow gates onto it. |

### Service pricing

—

### Task results

—

### Sources

- [official_repo](https://github.com/SabreDevStudio/SabreAPIsWorkflows/blob/master/SabreAPIsTestSuites/README.md) — checked 2026-09-07
- [official_site](https://developer.sabre.com/) — checked 2026-09-07

<a id="scrapingdog-flights"></a>

## Scrapingdog Google Flights API

Google Flights extraction endpoint charged in platform credits rather than one credit per flight search.

[Website](https://www.scrapingdog.com/) · [Source record](../data/candidates/scrapingdog-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="scrapingdog-flights-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [flights-api (API)](https://www.scrapingdog.com/documentation/google-flights-api/) | [Docs](https://www.scrapingdog.com/documentation/google-flights-api/) | self serve | — |

### Service pricing

- flights-api: 5 credits / flight request (usage; Do not equate platform free credits to the same number of flight searches.)

### Task results

—

### Sources

- [official_docs](https://www.scrapingdog.com/documentation/google-flights-api/) — checked 2026-09-07
- [official_docs](https://www.scrapingdog.com/documentation/) — checked 2026-09-07

<a id="searchapi"></a>

## SearchApi Google Flights

Google Flights extraction API and a hosted MCP integration supporting token or browser authorization.

[Website](https://www.searchapi.io/) · [Source record](../data/candidates/searchapi.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="searchapi-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [google-flights-api (API)](https://www.searchapi.io/docs/google-flights-api) | [Docs](https://www.searchapi.io/docs/google-flights-api) | self serve | — |
| [hosted-mcp (MCP)](https://www.searchapi.io/mcp) | [Docs](https://www.searchapi.io/integrations/mcp) | — | Authorize in browser when choosing OAuth; Supports browser OAuth or a separate MCP token. Which tools expose the flight task remains untested. |

### Service pricing

- google-flights-api: 100 requests / trial (free_allowance; Product-page trial; whether shared across engines requires account verification.)

### Task results

—

### Sources

- [official_docs](https://www.searchapi.io/docs/google-flights-api) — checked 2026-09-07
- [official_site](https://www.searchapi.io/google-flights-api) — checked 2026-09-07
- [official_docs](https://www.searchapi.io/integrations/mcp) — checked 2026-09-07

<a id="sentry"></a>

## Sentry

Error monitoring and performance tracing with llms.txt, an official MCP server, scoped auth tokens, and a full API.

[Website](https://sentry.io) · [Source record](../data/providers/sentry.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="sentry-access"></a>

[Docs](https://docs.sentry.io) · [API reference](https://docs.sentry.io/api/) · [CLI](https://docs.sentry.io/cli/) · [SDK](https://docs.sentry.io/platforms/) · [MCP entry](https://docs.sentry.io/product/sentry-mcp/)

—

### Service pricing

[Official pricing](https://sentry.io/pricing/)

### Task results

—

### Sources

—

<a id="serpapi"></a>

## SerpApi

Real-time JSON API for Google and other search engines' results, with an official MCP server, llms.txt, and a free monthly quota.

[Website](https://serpapi.com) · [Source record](../data/providers/serpapi.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="serpapi-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [google-flights-api (API)](https://serpapi.com/google-flights-api) | [Docs](https://serpapi.com/google-flights-api) | self serve | A third-party Google Flights data service. Not a Google-operated API. |
| [official-mcp (MCP)](https://github.com/serpapi/serpapi-mcp) | [Docs](https://github.com/serpapi/serpapi-mcp) | — | Official to SerpApi. Flight tool coverage and access gates are unconfirmed; do not inherit API-route results. |
| [web-search-api (API)](https://serpapi.com/search-api) | [Docs](https://serpapi.com/search-api) | self serve | Separate from Google Flights API. Existing flight evaluations do not establish web search performance. |

### Service pricing

[Official pricing](https://serpapi.com/pricing)

- google-flights-api: 250 searches / month (free_allowance; Platform search allowance; flight-endpoint entitlement and shared usage untested.)

### Task results

—

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

### Documentation and access <a id="serper-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [search-api (API)](https://serper.dev/) | — | self serve / documented | Google results API with signup trial queries; actual account flow and authentication remain untested. |

### Service pricing

- search-api: 2500 queries / one_time (free_allowance; Advertised initial free queries, no monthly renewal claimed.)

### Task results

—

### Sources

- [official_site](https://serper.dev/) — checked 2026-09-07

<a id="shopify"></a>

## Shopify

Commerce platform with versioned GraphQL APIs, llms.txt, official MCP docs, access-scoped tokens, free development stores, and a CLI.

[Website](https://www.shopify.com) · [Source record](../data/providers/shopify.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="shopify-access"></a>

[Docs](https://shopify.dev/docs) · [API reference](https://shopify.dev/docs/api) · [CLI](https://shopify.dev/docs/api/shopify-cli) · [MCP entry](https://shopify.dev/docs/apps/build/storefront-mcp)

—

### Service pricing

[Official pricing](https://www.shopify.com/pricing)

### Task results

—

### Sources

—

<a id="skootle-google-flights"></a>

## Skootle Google Flights Scraper

A Skootle-published flight-scraping Actor hosted on Apify, billed by startup and output records.

[Website](https://apify.com/skootle/google-flights-scraper) · [Source record](../data/candidates/skootle-google-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="skootle-google-flights-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [apify-actor-api (API)](https://apify.com/skootle/google-flights-scraper) | — | — | Requires: platform_account; Publisher is Skootle; Apify is the host. Not operated by Google or Apify. Record-based fees, actor version and actual trial eligibility need verification. |

### Service pricing

—

### Task results

—

### Sources

- [publisher_listing](https://apify.com/skootle/google-flights-scraper) — checked 2026-09-07

<a id="skyscanner"></a>

## Skyscanner Travel APIs

Partner flight APIs and an official MCP, with independently documented business-access paths.

[Website](https://www.skyscanner.net/) · [Source record](../data/candidates/skyscanner.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="skyscanner-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [partner-api (API)](https://developers.skyscanner.net/docs/getting-started/authentication) | [Docs](https://developers.skyscanner.net/docs/getting-started/authentication) | application | Requires: approval; Partnership review; personal-use acceptance, fees and waiting time are unknown. |
| [partner-mcp (MCP)](https://developers.skyscanner.net/docs/mcp-server) | [Docs](https://developers.skyscanner.net/docs/mcp-server) | application | Requires: approval; Contact account manager or partnership team; Case-by-case access; an official MCP does not establish personal self-service access. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://developers.skyscanner.net/docs/getting-started/authentication) — checked 2026-09-07
- [official_docs](https://developers.skyscanner.net/docs/mcp-server) — checked 2026-09-07

<a id="slack"></a>

## Slack

Workspace messaging platform with a mature Web API, granular OAuth scopes, an OpenAPI spec, and llms.txt.

[Website](https://slack.com) · [Source record](../data/providers/slack.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="slack-access"></a>

[Docs](https://api.slack.com) · [API reference](https://api.slack.com/methods) · [CLI](https://docs.slack.dev/tools/slack-cli) · [SDK](https://tools.slack.dev)

—

### Service pricing

[Official pricing](https://slack.com/pricing)

### Task results

—

### Sources

—

<a id="square"></a>

## Square

Hosted payment links and payment APIs with a free developer sandbox; merchant availability depends on country.

[Website](https://squareup.com/) · [Source record](../data/candidates/square.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="square-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [sandbox-api (API)](https://developer.squareup.com/reference/square/checkout-api/CreatePaymentLink) | [Docs](https://developer.squareup.com/reference/square/checkout-api/CreatePaymentLink) | self serve | Requires: platform_account; Create an application and select its sandbox seller account and access token.; Requires a Square account, application and sandbox seller location. Sandbox is free; live merchant eligibility is separate. Hosted checkout behavior must be checked before treating a sandbox link as a usable customer page. |

### Service pricing

- sandbox-api: 0 USD / sandbox API call (usage; Documented free sandbox API calls; not live processing or model usage.)

### Task results

—

### Sources

- [official_docs](https://developer.squareup.com/reference/square/checkout-api/CreatePaymentLink) — checked 2026-09-08
- [official_docs](https://developer.squareup.com/docs/devtools/sandbox/overview) — checked 2026-09-08

<a id="steel"></a>

## Steel

Cloud browser API for AI agents (sessions, CDP, anti-bot) — open-source and self-hostable, with llms.txt and a free tier.

[Website](https://steel.dev) · [Source record](../data/providers/steel.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="steel-access"></a>

[Docs](https://docs.steel.dev) · [API reference](https://docs.steel.dev/api-reference)

—

### Service pricing

[Official pricing](https://steel.dev/pricing)

### Task results

—

### Sources

—

<a id="stripe"></a>

## Stripe

Payments, billing, subscriptions, and financial infrastructure with a famously complete API surface.

[Website](https://stripe.com) · [Source record](../data/providers/stripe.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="stripe-access"></a>

[Docs](https://docs.stripe.com) · [API reference](https://docs.stripe.com/api) · [CLI](https://docs.stripe.com/stripe-cli) · [SDK](https://docs.stripe.com/sdks) · [MCP entry](https://docs.stripe.com/mcp)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [sandbox-api (API)](https://docs.stripe.com/payment-links/create) | [Docs](https://docs.stripe.com/payment-links/create) | — | Requires: platform_account; Use isolated sandbox resources and test API keys. One-time and recurring product prices are documented. Live account activation, merchant country eligibility and tax responsibilities require separate checks. |

### Service pricing

[Official pricing](https://stripe.com/pricing)

### Task results

—

### Notes

- Agent tooling (MCP, agent toolkit) evolves quickly; re-check quarterly.

### Sources

- [official_docs](https://docs.stripe.com/payment-links/create) — checked 2026-09-08
- [official_docs](https://docs.stripe.com/testing?numbers-or-method-or-token=tokens) — checked 2026-09-08
- [official_site](https://stripe.com/global) — checked 2026-09-08

<a id="supabase"></a>

## Supabase

Postgres platform with auth, storage, edge functions, a management API, official MCP server, and LLM-ready docs.

[Website](https://supabase.com) · [Source record](../data/providers/supabase.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="supabase-access"></a>

[Docs](https://supabase.com/docs) · [API reference](https://supabase.com/docs/reference/api/introduction) · [CLI](https://supabase.com/docs/guides/cli) · [SDK](https://supabase.com/docs/reference) · [MCP entry](https://supabase.com/docs/guides/getting-started/mcp)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://supabase.com/docs/guides/api) | [Docs](https://supabase.com/docs/guides/api) | self serve / documented | Existing project required; Free plan: two active projects, 500 MB database per project; pauses after one week inactivity. Management provisioning is separate from the data REST API. |

### Service pricing

[Official pricing](https://supabase.com/pricing)

- data-api: 500 MB / project (free_allowance; Free plan database size; up to two active projects, pauses after one inactive week.)

### Task results

—

### Sources

- [official_docs](https://supabase.com/docs/guides/api) — checked 2026-09-07
- [official_site](https://supabase.com/pricing) — checked 2026-09-07

<a id="tavily"></a>

## Tavily

Search and extraction API built for AI agents, with llms.txt, an official MCP server, and a free tier.

[Website](https://www.tavily.com) · [Source record](../data/providers/tavily.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="tavily-access"></a>

[Docs](https://docs.tavily.com) · [API reference](https://docs.tavily.com/documentation/api-reference/introduction) · [SDK](https://docs.tavily.com/sdk) · [MCP entry](https://docs.tavily.com/documentation/mcp)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [search-api (API)](https://docs.tavily.com/documentation/quickstart) | [Docs](https://docs.tavily.com/documentation/quickstart) | self serve / documented | Basic search costs 1 credit; advanced search 2. Paid overage setting is separate. |

### Service pricing

[Official pricing](https://www.tavily.com/pricing)

- search-api: 1000 credits / month (free_allowance; Free account allowance, not requests.)

### Task results

—

### Sources

- [official_docs](https://docs.tavily.com/documentation/quickstart) — checked 2026-09-07
- [official_docs](https://docs.tavily.com/documentation/api-credits) — checked 2026-09-07

<a id="telegram"></a>

## Telegram Bot API

Free bot platform with instant token issuance via BotFather, webhooks, a documented test environment, and a detailed changelog.

[Website](https://telegram.org) · [Source record](../data/providers/telegram.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="telegram-access"></a>

[Docs](https://core.telegram.org/bots) · [API reference](https://core.telegram.org/bots/api)

—

### Service pricing

—

### Task results

—

### Sources

—

<a id="together-ai"></a>

## Together AI

Inference and fine-tuning platform for open-source models with an OpenAI-compatible API and llms.txt.

[Website](https://www.together.ai) · [Source record](../data/providers/together-ai.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="together-ai-access"></a>

[Docs](https://docs.together.ai) · [API reference](https://docs.together.ai/reference/chat-completions)

—

### Service pricing

[Official pricing](https://www.together.ai/pricing)

### Task results

—

### Sources

—

<a id="travelport-tripservices"></a>

## Travelport TripServices

Travel distribution API requiring trial requests and provider-provisioned production credentials.

[Website](https://developer.travelport.com/) · [Source record](../data/candidates/travelport-tripservices.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="travelport-tripservices-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [tripservices-api (API)](https://developer.travelport.com/docs/getting-started) | [Docs](https://developer.travelport.com/docs/getting-started) | application | Requires: approval; Request trial access; contact sales for customer onboarding; Production/pre-production credentials and PCC/point-of-sale context are provisioned. Personal access and trial data realism remain unknown. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://developer.travelport.com/docs/getting-started) — checked 2026-09-07
- [official_docs](https://developer.travelport.com/docs/getting-started/authentication) — checked 2026-09-07

<a id="trip-com-flights"></a>

## Trip.com Flight Distribution

Trip.com supplier fare-maintenance API lead; a consumer flight-search access path is not yet established.

[Website](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html) · [Source record](../data/candidates/trip-com-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="trip-com-flights-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [supplier-fare-maintenance (API)](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html) | [Docs](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html) | — | Supplier fare and rule maintenance with existing distribution permissions/support. Not evidence of consumer itinerary search; no flights.search capability is assigned. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html) — checked 2026-09-07

<a id="turso"></a>

## Turso

Free cloud account: 100 databases, 5 GB, 500 million reads/month and 10 million writes/month. Signup/login required; local engine alone does not satisfy remote storage.

[Website](https://turso.tech/) · [Source record](../data/candidates/turso.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="turso-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [cloud-cli (CLI)](https://docs.turso.tech/cli/introduction) | [Docs](https://docs.turso.tech/cli/introduction) | self serve / documented | Free cloud account: 100 databases, 5 GB, 500 million reads/month and 10 million writes/month. Signup/login required; local engine alone does not satisfy remote storage. |
| [platform-api (API)](https://docs.turso.tech/api-reference/introduction) | [Docs](https://docs.turso.tech/api-reference/introduction) | self serve | Management API; SQL connectivity uses separate database credentials created during execution. Provision only within a dedicated free test organization; no precreated database. |

### Service pricing

- cloud-cli: 5 GB / account (free_allowance; Free cloud storage; account quota also limits reads, writes and number of databases.)

### Setup observations

| Route | Starting resources | Setup tokens | Setup time | Human involvement |
| --- | --- | --- | --- | --- |
| CLI | — | — | — | — |
| API | [Credentials supplied before trial](../data/experiments/evaluations/codex-20260907T113506.422646Z-turso.json) | — | — | — |

### Task results

#### Prepare a separate remote database for my personal todo app and verify adding, updating and reading todos after reconnecting

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-1420586eae17) | [100%](./evaluations.md#comparison-1420586eae17) | 767.6k | — | $0 |
| CLI | — | — | — | — | — |

<details>
<summary>Task, conditions and evidence</summary>

Synthetic test data only: id=1,title=Buy milk,done=false; id=2,title=Read book,done=false; id=3,title=Walk dog,done=true. Insert all three, then set done=true for id=2. A temporary database requiring no payment may be created; existing projects must not be modified.

**Completion:** Data is actually saved and updated in the specified service's remote database. A fresh process reads back all three items with unchanged titles; only id=1 is incomplete, with three total and two completed. Evidence establishes an independent connection and remote execution. Credentials stay in private workspace files and must not appear in evidence or the final answer. Temporary resources are acceptable if their expiry is disclosed.

codex-cli 0.153.4 · gpt-6-astra / xhigh · 600s · 2026-09-07 (UTC)

Credentials supplied · [Full configuration and evidence](./evaluations.md#comparison-1420586eae17)

[Task definition](./tasks.en.md#database-todos-001-v1)

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| database-todos-001 v1 | API | [completed](../data/experiments/evaluations/codex-20260907T113506.422646Z-turso.json) | 2026-09-07 |

</details>

### Sources

- [official_docs](https://docs.turso.tech/cli/introduction) — checked 2026-09-07
- [official_docs](https://docs.turso.tech/api-reference/introduction) — checked 2026-09-07
- [official_site](https://turso.tech/pricing) — checked 2026-09-07

<a id="twilio"></a>

## Twilio

Programmable messaging and voice APIs with test credentials, an OpenAPI spec, llms.txt, and an official CLI.

[Website](https://www.twilio.com) · [Source record](../data/providers/twilio.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="twilio-access"></a>

[Docs](https://www.twilio.com/docs) · [API reference](https://www.twilio.com/docs/usage/api) · [CLI](https://www.twilio.com/docs/twilio-cli) · [SDK](https://www.twilio.com/docs/libraries) · [MCP entry](https://github.com/twilio-labs/mcp)

—

### Service pricing

[Official pricing](https://www.twilio.com/en-us/pricing)

### Task results

—

### Sources

—

<a id="upstash"></a>

## Upstash

Serverless Redis, Kafka-successor queues, and vector storage with REST APIs, llms.txt, an official MCP server, and a free tier.

[Website](https://upstash.com) · [Source record](../data/providers/upstash.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="upstash-access"></a>

[Docs](https://upstash.com/docs) · [API reference](https://upstash.com/docs/devops/developer-api/introduction) · [CLI](https://github.com/upstash/cli) · [MCP entry](https://github.com/upstash/mcp-server)

—

### Service pricing

[Official pricing](https://upstash.com/pricing)

### Task results

—

### Sources

—

<a id="vapi"></a>

## Vapi

Voice-agent orchestration API (calls, turn-taking, tool use over phone/web) with an official MCP server and an llms.txt that opens with instructions for AI agents.

[Website](https://vapi.ai) · [Source record](../data/providers/vapi.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="vapi-access"></a>

[Docs](https://docs.vapi.ai) · [API reference](https://docs.vapi.ai/api-reference) · [MCP entry](https://github.com/VapiAI/mcp-server)

—

### Service pricing

[Official pricing](https://vapi.ai/pricing)

### Task results

—

### Sources

—

<a id="vercel"></a>

## Vercel

Frontend cloud for deploying web apps, with a REST API, CLI, official MCP server, and AI SDK ecosystem.

[Website](https://vercel.com) · [Source record](../data/providers/vercel.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="vercel-access"></a>

[Docs](https://vercel.com/docs) · [API reference](https://vercel.com/docs/rest-api) · [CLI](https://vercel.com/docs/cli) · [SDK](https://vercel.com/docs/rest-api/sdk) · [MCP entry](https://vercel.com/docs/mcp/vercel-mcp)

—

### Service pricing

[Official pricing](https://vercel.com/pricing)

### Task results

—

### Sources

—

<a id="weaviate"></a>

## Weaviate

Open-source vector database with REST/GraphQL/gRPC APIs, Weaviate Cloud free sandboxes, an official CLI, MCP server, and llms.txt.

[Website](https://weaviate.io) · [Source record](../data/providers/weaviate.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="weaviate-access"></a>

[Docs](https://docs.weaviate.io) · [API reference](https://docs.weaviate.io/weaviate/api/rest) · [CLI](https://github.com/weaviate/weaviate-cli) · [MCP entry](https://github.com/weaviate/mcp-server-weaviate)

—

### Service pricing

[Official pricing](https://weaviate.io/pricing)

### Task results

—

### Sources

—

<a id="wechat-pay"></a>

## WeChat Pay

Merchant payment APIs including Native QR checkout; merchant credentials and channel-specific setup are required.

[Website](https://pay.weixin.qq.com/) · [Source record](../data/candidates/wechat-pay.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="wechat-pay-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [native-api (API)](https://pay.wechatpay.cn/doc/v3/merchant/4012791877) | [Docs](https://pay.wechatpay.cn/doc/v3/merchant/4012791877) | — | Native checkout is a QR payment flow, not a browser-hosted card checkout. Merchant admission, individual eligibility and an applicable free sandbox remain unknown in this discovery pass; do not simulate success by using a live small-value payment. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://pay.wechatpay.cn/doc/v3/merchant/4012791877) — checked 2026-09-08

<a id="whop"></a>

## Whop

Payment APIs and checkout integration for existing apps, with TypeScript, Python and Ruby SDKs.

[Website](https://whop.com/) · [Source record](../data/candidates/whop.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="whop-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [official-api (API)](https://docs.whop.com/) | [Docs](https://docs.whop.com/) | — | Docs describe dashboard API keys and checkout integration. Merchant eligibility, sandbox coverage, service responsibilities and full fees still need verification; buyer availability does not establish seller eligibility. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://docs.whop.com/) — checked 2026-09-08

<a id="xai"></a>

## xAI (Grok API)

xAI's Grok models via an OpenAI-compatible REST API, with an llms.txt and self-serve console keys.

[Website](https://x.ai) · [Source record](../data/providers/xai.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="xai-access"></a>

[Docs](https://docs.x.ai) · [API reference](https://docs.x.ai/developers/rest-api-reference/inference)

—

### Service pricing

—

### Task results

—

### Sources

—

<a id="xquik"></a>

## Xquik

Hosted X data and account automation service with a REST API, official MCP server, OpenAPI, SDKs, HMAC webhooks, and OAuth 2.1.

[Website](https://xquik.com) · [Source record](../data/candidates/xquik.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="xquik-access"></a>

[Docs](https://docs.xquik.com) · [API reference](https://docs.xquik.com/api-reference/overview) · [SDK](https://docs.xquik.com/sdks) · [MCP entry](https://docs.xquik.com/mcp/overview)

—

### Service pricing

[Official pricing](https://xquik.com/pricing)

### Task results

—

### Notes

- The official Streamable HTTP MCP endpoint is https://xquik.com/mcp and supports API key or OAuth authentication.

### Sources

—

<a id="zai"></a>

## Z.ai (GLM)

GLM models via Z.ai's OpenAI-compatible international API, with llms.txt, published pricing, and self-serve keys.

[Website](https://z.ai) · [Source record](../data/providers/zai.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="zai-access"></a>

[Docs](https://docs.z.ai) · [API reference](https://docs.z.ai/api-reference)

—

### Service pricing

[Official pricing](https://docs.z.ai/guides/overview/pricing)

### Task results

—

### Sources

—

<a id="zapier"></a>

## Zapier

Automation platform bridging 7000+ apps, with llms.txt and an official MCP endpoint that gives agents access to those integrations.

[Website](https://zapier.com) · [Source record](../data/providers/zapier.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="zapier-access"></a>

[Docs](https://docs.zapier.com) · [CLI](https://github.com/zapier/zapier-platform) · [MCP entry](https://zapier.com/mcp) · [MCP setup](https://docs.zapier.com/mcp/get-started/quickstart)

—

### Service pricing

[Official pricing](https://zapier.com/pricing)

### Task results

—

### Notes

- MCP setup documentation checked on 2026-09-09: https://docs.zapier.com/mcp/get-started/quickstart. The server or product entry remains separately recorded in mcp_official.

### Sources

—

<a id="qunar-flights"></a>

## 去哪儿机票合作

去哪儿官方机票及分销合作渠道线索；个人自助机票搜索 API 或 MCP 尚未确认。

[Website](https://www.qunar.com/site/zh/Cooperate_4.shtml) · [Source record](../data/candidates/qunar-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="qunar-flights-access"></a>

—

### Service pricing

—

### Task results

—

### Sources

- [official_site](https://www.qunar.com/site/zh/Cooperate_4.shtml) — checked 2026-09-07

<a id="tongcheng-flights"></a>

## 同程机票合作

同程官方机票与出行平台合作线索；普通个人自助搜索 API 的准入、费用和能力尚未确认。

[Website](https://www.ly.com/public/about17u/contactus) · [Source record](../data/candidates/tongcheng-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="tongcheng-flights-access"></a>

—

### Service pricing

—

### Task results

—

### Sources

- [official_site](https://www.ly.com/public/about17u/contactus) — checked 2026-09-07
- [official_site](https://flights.ly.com/open/home) — checked 2026-09-07

<a id="ctrip-flights"></a>

## 携程机票合作

携程的分销与供应商合作线索；尚未确认面向普通个人的旅客机票搜索 API。

[Website](https://pages.ctrip.com/public/dlhz.htm) · [Source record](../data/candidates/ctrip-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="ctrip-flights-access"></a>

—

### Service pricing

—

### Task results

—

### Sources

- [official_site](https://pages.ctrip.com/public/dlhz.htm) — checked 2026-09-07
- [official_site](https://developer.ctrip.com/) — checked 2026-09-07

<a id="feishu"></a>

## 飞书 Feishu

China-region Feishu workspace and Base APIs; separate account/tenant from international Lark.

[Website](https://www.feishu.cn/) · [Source record](../data/candidates/feishu.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="feishu-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [base-api (API)](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/create) | [Docs](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/create.md) | self serve | Requires a platform app, authorized identity and Base scopes/resource permissions. Ordinary-person onboarding from a fresh account is not tested. |
| [official-cli (CLI)](https://github.com/larksuite/cli) | [Docs](https://github.com/larksuite/cli) | self serve | Official CLI covers Base and supports individuals. Account signup, app creation and permission setup still need separate verification. |
| [official-mcp (MCP)](https://github.com/larksuite/lark-openapi-mcp) | [Docs](https://github.com/larksuite/lark-openapi-mcp) | self serve | Local official MCP package uses platform app credentials; identity and tenant domains must match. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/create.md) — checked 2026-09-08
- [official_repo](https://github.com/larksuite/cli) — checked 2026-09-08
- [official_repo](https://github.com/larksuite/lark-openapi-mcp) — checked 2026-09-08
- [official_site](https://www.feishu.cn/service?tab=free) — checked 2026-09-08

<a id="fliggy-domestic-flights"></a>

## 飞猪国内机票开放平台

面向机票商家的政策与订单接口，需要企业、代理商身份、店铺和聚石塔；不等同于旅客搜索接口。

[Website](https://open.alitrip.com/businessDetail.htm?tagId=85) · [Source record](../data/candidates/fliggy-domestic-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="fliggy-domestic-flights-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [merchant-api (API)](https://open.alitrip.com/businessDetail.htm?tagId=85) | — | restricted | Requires: company, store, industry_license; 商家店铺须绑定支付宝并使用聚石塔；不能将政策和订单接口记成消费者搜索能力。其他个人入口未知。 |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://open.alitrip.com/businessDetail.htm?tagId=85) — checked 2026-09-07
- [official_docs](https://open.alitrip.com/docs/doc.htm?articleId=121782&docType=1&treeId=111) — checked 2026-09-07
