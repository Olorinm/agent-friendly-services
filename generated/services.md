<!-- GENERATED — edit source records; run npm run generate. -->
# Service profiles

Token and costs are means per valid trial, including successes and failures; invalid runs are excluded. Model costs use saved LiteLLM prices; ~ marks estimated service charges. — means no data. Setup costs are separate from business task costs. Access and pricing are source claims; a listed route does not establish task support. Compare only matching tasks and conditions.

<a id="adyen"></a>

## Adyen

Payment processing with hosted Pay by Link checkout; test merchant accounts and live onboarding have separate requirements.

**Classification:** Payments / Billing / Payment Acceptance

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

<a id="agentmail"></a>

## AgentMail

Dedicated agent inboxes with sending, receiving, threads and API, SDK, CLI and MCP access.

**Classification:** Communication / Mailboxes

[Website](https://www.agentmail.to/) · [Source record](../data/candidates/agentmail.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="agentmail-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [mail-api (API)](https://docs.agentmail.to/quickstart) | [Docs](https://docs.agentmail.to/quickstart) | — | Agent signup accepts an owner email and sends an OTP. Verification unlocks full permissions; existing owner accounts cannot use first-time signup. Signup can rotate an existing unverified key, so inspect account state before retrying. Published Free plan: 3 inboxes and 3,000 emails/month, no card required; not observed account entitlement. |
| [mail-sdk (SDK)](https://docs.agentmail.to/quickstart) | [Docs](https://docs.agentmail.to/quickstart) | — | Separate route; shares the service account and plan limits. No task result inherited from other routes. |
| [mail-cli (CLI)](https://docs.agentmail.to/quickstart) | [Docs](https://docs.agentmail.to/quickstart) | — | Separate route; shares the service account and plan limits. No task result inherited from other routes. |
| [mail-mcp (MCP)](https://mcp.agentmail.to/mcp) | [Docs](https://docs.agentmail.to/agent-onboarding) | — | Separate route; shares the service account and plan limits. No task result inherited from other routes. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://docs.agentmail.to/quickstart) — checked 2026-09-09
- [official_docs](https://www.agentmail.to/pricing) — checked 2026-09-09
- [official_docs](https://docs.agentmail.to/agent-onboarding) — checked 2026-09-09

<a id="agentservices"></a>

## AgentServices

Market data, web search and extraction, and model access through REST, MCP and a JavaScript SDK; selected free tools, x402 payments on REST, and a documented OAuth/prepaid-credit MCP path.

**Classification:** Search & Data Access / Web Search; Search & Data Access / Web Content Extraction; AI Services / Model Access; Search & Data Access / Financial Data / Asset Prices

[Website](https://agentservices.to/) · [Source record](../data/candidates/agentservices.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="agentservices-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [rest-api (API)](https://api.agentservices.to/) | [Docs](https://github.com/vbkotecha/agentservices-api/blob/main/docs/buyer-quickstart.md) | self serve / documented | Buyer guide names api.agentservices.to as the API host; agentservices.to serves the inspected documentation. The free-price example is distinct from a paid data result. An HTTP 402 challenge would establish quoted terms only, not delivery or settlement. Paid prices remain unresolved. |
| [official-mcp (MCP)](https://agentservices.to/mcp) | [Docs](https://github.com/vbkotecha/agentservices-api/blob/main/README.md#using-as-mcp-server-claude-desktop-cursor-etc) | self serve / documented | Protocol configuration is documented, not executed here. MCP discovery, a free tool call and fulfillment of a paid tool are separate checks; neither MCP support nor a registry listing establishes hosted-service terms or read-only behavior for every tool. |
| [javascript-sdk (SDK)](https://github.com/vbkotecha/agentservices-api/tree/main/sdk) | [Docs](https://github.com/vbkotecha/agentservices-api/blob/main/sdk/README.md) | self serve / documented | Package installation and execution were not tested. SDK price examples are indicative, and a payment challenge surfaced by the client is not a successful paid result. |

### Service pricing

—

### Task results

—

### Notes

- One service identity covers its REST, MCP and SDK routes, including the older AIServices name. The README attributes free crypto prices to CoinGecko and OpenAPI attributes chat completions to OpenRouter; these routes are not independent underlying data or model sources.
- A written version/deprecation policy and hosted-service automation terms remain unknown; version labels and protocol endpoints do not establish either policy.
- Data retrieval and x402 settlement are separate actions. The current platform also documents trading and persistent-memory writes; no service-wide read-only or idempotency conclusion is made.

### Sources

- [publisher_listing](https://github.com/Olorinm/agent-friendly-services/pull/4) — checked 2026-09-15
- [official_docs](https://github.com/vbkotecha/agentservices-api/blob/a9a5fd8aa7ecb9910e4a291b4718aa659ea41fbe/docs/buyer-quickstart.md) — checked 2026-09-15
- [official_docs](https://github.com/vbkotecha/agentservices-api/blob/a9a5fd8aa7ecb9910e4a291b4718aa659ea41fbe/README.md) — checked 2026-09-15
- [official_docs](https://agentservices.to/openapi.json) — checked 2026-09-15
- [official_docs](https://agentservices.to/.well-known/x402) — checked 2026-09-15
- [official_docs](https://github.com/vbkotecha/agentservices-api/blob/a9a5fd8aa7ecb9910e4a291b4718aa659ea41fbe/sdk/README.md) — checked 2026-09-15
- [official_repo](https://github.com/vbkotecha/agentservices-api/blob/a9a5fd8aa7ecb9910e4a291b4718aa659ea41fbe/sdk/index.js) — checked 2026-09-15

<a id="airgateway"></a>

## AirGateway Platform API

Air distribution API with sandbox keys, production certification and an agency application.

**Classification:** Travel / Flights

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

**Classification:** Workplace Collaboration / Collaborative Tables

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

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Databases / Hosted Relational Databases

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

**Classification:** AI Services / Model Access

[Website](https://www.alibabacloud.com/en/product/modelstudio) · [Source record](../data/providers/qwen.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="qwen-access"></a>

[Docs](https://www.alibabacloud.com/help/en/model-studio/) · [API reference](https://www.alibabacloud.com/help/en/model-studio/models) · [CLI](https://github.com/QwenLM/qwen-code)

—

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://www.alibabacloud.com/help/en/model-studio/get-api-key) — checked 2026-07-08

<a id="alipay"></a>

## Alipay

Online merchant payment integrations for websites and apps through Alipay APIs and SDKs.

**Classification:** Payments / Billing / Payment Acceptance

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

<a id="alpaca-market-data"></a>

## Alpaca Market Data

Read-only equities, options and crypto market data, separate from trading operations; Basic access is included with paper accounts.

**Classification:** Search & Data Access / Financial Data / Asset Prices

[Website](https://alpaca.markets/) · [Source record](../data/candidates/alpaca-market-data.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="alpaca-market-data-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://docs.alpaca.markets/us/docs/about-market-data-api) | [Docs](https://docs.alpaca.markets/us/docs/about-market-data-api) | self serve / documented | Basic is free with limited real-time feeds; historical coverage and latest-15-minute restrictions are separate. Use market-data endpoints only. Paper-account signup and identity requirements have not been measured. |
| [crypto-api-keyless (API)](https://docs.alpaca.markets/us/docs/about-market-data-api) | [Docs](https://docs.alpaca.markets/us/docs/about-market-data-api) | self serve / documented | Official documentation exempts historical crypto endpoints from authentication. Does not imply equity-data access or trading permission. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://docs.alpaca.markets/us/docs/about-market-data-api) — checked 2026-09-09

<a id="alpha-vantage"></a>

## Alpha Vantage

Stock prices, company financials, FX, crypto and economic indicators. Free keys have a daily quota; premium endpoints are separate.

**Classification:** Search & Data Access / Financial Data / Exchange Rates; Search & Data Access / Financial Data / Asset Prices; Search & Data Access / Financial Data / Company Financials; Search & Data Access / Financial Data / Transaction Disclosures; Search & Data Access / Financial Data / Economic Indicators

[Website](https://www.alphavantage.co/) · [Source record](../data/candidates/alpha-vantage.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="alpha-vantage-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://www.alphavantage.co/documentation/) | [Docs](https://www.alphavantage.co/documentation/) | self serve / documented | Free key: 25 requests/day, excluding premium endpoints. Unadjusted daily compact output (latest 100 observations) is available to free keys; full history and intraday are premium. This may cover the current short historical task, subject to access and source precision. Real-time quotes and adjusted data require separate entitlement checks. |

### Service pricing

- data-api: 25 requests / day (free_allowance; Free API key allowance; excludes premium endpoints.)

### Task results

—

### Notes

- Official support links https://mcp.alphavantage.co/ as the MCP setup surface; detailed setup could not be extracted in this pass.

### Sources

- [official_docs](https://www.alphavantage.co/documentation/) — checked 2026-09-15
- [official_site](https://www.alphavantage.co/support/) — checked 2026-09-15
- [official_docs](https://www.alphavantage.co/support/) — checked 2026-09-09

<a id="amadeus-flights"></a>

## Amadeus Flight APIs

Historical Self-Service flight API and the current Enterprise portal; individual onboarding must be re-established.

**Classification:** Travel / Flights

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

**Classification:** AI Services / Model Access

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

- [official_docs](https://docs.anthropic.com/en/api/getting-started) — checked 2026-07-07

<a id="apify"></a>

## Apify

Web scraping and automation platform with thousands of ready-made actors, a versioned API, llms.txt, and an official MCP server.

**Classification:** Search & Data Access / Web Content Extraction

[Website](https://apify.com) · [Source record](../data/providers/apify.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="apify-access"></a>

[Docs](https://docs.apify.com) · [API reference](https://docs.apify.com/api/v2) · [CLI](https://docs.apify.com/cli) · [SDK](https://docs.apify.com/sdk) · [MCP entry](https://docs.apify.com/platform/integrations/mcp)

—

### Service pricing

[Official pricing](https://apify.com/pricing)

### Task results

—

### Notes

- Extraction scope is supported by the Apify-maintained Website Content Crawler, which takes start URLs and returns page content. This platform record does not inherit every third-party Actor capability; route, Actor version and access must be selected before a task.
- mcp.apify.com hosts the official remote MCP server; the docs page above explains setup.

### Sources

- [official_docs](https://docs.apify.com/platform/integrations/api) — checked 2026-07-07
- [publisher_listing](https://apify.com/apify/website-content-crawler) — checked 2026-09-15

<a id="apiheya-air-scraper"></a>

## apiheya Air Scraper

An apiheya flight-data product distributed through RapidAPI; distinct from the official Skyscanner partner API.

**Classification:** Travel / Flights

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

**Classification:** Developer Tools / Code Hosting & Review; Workplace Collaboration / Project & Task Management; Workplace Collaboration / Document Collaboration

[Website](https://www.atlassian.com) · [Source record](../data/providers/atlassian.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="atlassian-access"></a>

[Docs](https://developer.atlassian.com) · [API reference](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/) · [CLI](https://developer.atlassian.com/cloud/acli/) · [MCP entry](https://github.com/atlassian/atlassian-mcp-server)

—

### Service pricing

[Official pricing](https://www.atlassian.com/software/jira/pricing)

### Task results

—

### Notes

- Legacy suite record: Bitbucket supports repository work, Jira supports issue/project work, and Confluence supports document collaboration. These are product-specific scopes, not capabilities shared by one route.

### Sources

- [official_docs](https://developer.atlassian.com/cloud/) — checked 2026-09-15

<a id="aviasales"></a>

## Aviasales via Travelpayouts

Travelpayouts-distributed live flight search and a separately accessible historical price-data API.

**Classification:** Travel / Flights

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

<a id="bargo-congress"></a>

## Bargo Congress Trades API

Read-only US congressional trade disclosures through a free REST API and keyed MCP; this entry covers only the Congress product.

**Classification:** Search & Data Access / Financial Data / Transaction Disclosures

[Website](https://www.bargo.ai/free-apis/congress) · [Source record](../data/candidates/bargo-congress.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="bargo-congress-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [congress-api-keyless (API)](https://www.bargo.ai/free-apis/congress/v1) | [Docs](https://www.bargo.ai/free-apis/congress) | self serve / documented | Rolling three-month coverage. Preserve transaction and disclosure dates; the Free API Terms require attribution and restrict raw-data redistribution. |
| [congress-api-keyed (API)](https://www.bargo.ai/free-apis/congress/v1) | [Docs](https://www.bargo.ai/free-apis/congress) | self serve / documented | Requires: platform_account; Free keys are issued through Google sign-in. REST accepts Bearer or X-Api-Key authentication; regenerating a key invalidates the old one. Signup and key acquisition have not been measured. The published quota covers the same key across Bargo Free APIs, not a separate allowance per route. |
| [congress-mcp (MCP)](https://www.bargo.ai/free-apis/congress/mcp) | [Docs](https://www.bargo.ai/free-apis/congress) | self serve / documented | Requires: platform_account; Uses the free key obtained through Google sign-in. Bearer authentication is documented; no separate MCP data or quota allowance is claimed. Verify tool coverage per task. |

### Service pricing

- congress-api-keyless: 30 requests / day (free_allowance; Keyless quota shared per IP.)

- congress-api-keyless: 100 rows / day (free_allowance; Rolling three-month Congress dataset; redistribution restrictions apply.)

- congress-api-keyed: 100 requests / day (free_allowance; Free-key allowance across Bargo Free APIs, including REST and MCP.)

- congress-api-keyed: 1000 rows / day (free_allowance; Same free-key allowance; Congress data is limited to a rolling three-month window.)

- congress-mcp: 100 requests / day (free_allowance; Free-key allowance across Bargo Free APIs, including REST and MCP.)

- congress-mcp: 1000 rows / day (free_allowance; Same free-key allowance; Congress data is limited to a rolling three-month window.)

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
| --- | --- | --- | --- | --- |
| API (congress-api-keyless) | [No account or key supplied](../data/experiments/evaluations/bargo-business.json) | [95.8k](../data/experiments/evaluations/bargo-access.json) | 157.266045s | 0 |
| API (congress-api-keyed) | — | — | — | — |
| MCP | — | — | — | — |

#### Set up this financial-data service, confirm that it can query data through the specified interface, and save the configuration needed for later use. If access is blocked, explain where.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API (congress-api-keyless) | [1](./evaluations.md#comparison-bd611da6270b) | [100%](./evaluations.md#comparison-bd611da6270b) | 95.8k | $0.0068 | $0 |
| API (congress-api-keyed) | — | — | — | — | — |
| MCP | — | — | — | — | — |

<details>
<summary>Task, conditions and evidence</summary>

The service, required interface, and any supplied account or signup information are specified in the environment. Use account-free access directly when available. For signup, use only the identity information supplied for this trial. Retain the necessary connection configuration for later tasks.

**Completion:** Complete the required signup, authentication and configuration for the specified interface, and query real financial data. Necessary configuration works in a fresh session. Do not force registration for account-free routes. Documentation, a health check or a configuration file alone does not establish data access.

1.18.29 · glm-5.3-flash / high · 600s · 2026-09-15 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-bd611da6270b)

[Task definition](./tasks.en.md#financial-access-001-v1)

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| financial-access-001 v1 | API (congress-api-keyless) | [completed](../data/experiments/evaluations/bargo-access.json) | 2026-09-15 |

</details>

### Task results

#### Summarize the stock purchases and sales Richard W. Allen filed with the U.S. House in August 2026. Include the stock, direction, transaction date, filing date, amount range and original filing source.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API (congress-api-keyless) | [1](./evaluations.md#comparison-ee257df56f0f) | [100%](./evaluations.md#comparison-ee257df56f0f) | 751.7k | $0.03 | $0 |
| API (congress-api-keyed) | — | — | — | — | — |
| MCP | — | — | — | — | — |

<details>
<summary>Task, conditions and evidence</summary>

Filer: Richard W. Allen, Georgia district 12 (GA12). Select Periodic Transaction Reports by official filing date from 2026-08-01 through 2026-08-31, publicly available as of 2026-09-15. Include reported family-member transactions and retain USD amount ranges. Common stock only, excluding options, funds, bonds and other assets. Filing in August does not mean trading in August. This is for private reading; no data export is needed.

**Completion:** Match all applicable records in the independently frozen official index and PTR, without duplicates or unsupported additions. Real queries to the specified service support the disclosures; original filings may supplement date and provenance verification. Use the official index filing date, distinct from trade, notification and service ingestion/publication dates. Do not present midpoints, estimated prices or family-member trades as exact personal trades by the member. Identify the specific original filing rather than only the portal.

1.18.29 · glm-5.3-flash / high · 600s · 2026-09-15 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-ee257df56f0f)

[Task definition](./tasks.en.md#financial-disclosures-001-v1)

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| financial-disclosures-001 v1 | API (congress-api-keyless) | [completed](../data/experiments/evaluations/bargo-business.json) | 2026-09-15 |

</details>

### Notes

- Originally submitted by the vendor in https://github.com/Olorinm/agent-friendly-services/pull/6; incorporated during the broader financial-data discovery pass. This record covers the Congress product, not Bargo's separate market-intelligence platform; no task result is implied.
- The OpenAPI date filters select transaction dates, not disclosure dates; filing_portal points to the source filing portal and does not establish a direct link to each original filing. Preserve these distinctions when selecting a task or checking provenance.
- Free API Terms allow personal applications, agents and analysis with visible Bargo attribution. Raw records may not be redistributed, including partial exports; derivative work must not expose or reconstruct them. Evidence publication must respect this restriction.

### Sources

- [official_docs](https://www.bargo.ai/free-apis/congress) — checked 2026-09-15
- [official_docs](https://www.bargo.ai/free-apis/congress/openapi.json) — checked 2026-09-15
- [official_site](https://www.bargo.ai/free-apis/dash) — checked 2026-09-15
- [official_site](https://www.bargo.ai/free-apis/terms) — checked 2026-09-15

<a id="baserow"></a>

## Baserow Cloud

Hosted collaborative tables; free workspace and scoped row-access tokens. Schema management uses a different credential.

**Classification:** Workplace Collaboration / Collaborative Tables

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

<a id="bloomberg-data-license"></a>

## Bloomberg Data License

Enterprise pricing, fundamentals, reference and other financial datasets delivered through REST, SFTP or cloud.

**Classification:** Search & Data Access / Financial Data / Asset Prices

[Website](https://professional.bloomberg.com/products/data/data-license/) · [Source record](../data/candidates/bloomberg-data-license.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="bloomberg-data-license-access"></a>

—

### Service pricing

—

### Task results

—

### Notes

- Pricing is explicit in the recorded Data License scope. Fundamentals alone are insufficient here to confirm statement fields; no route or personal license is established.
- Existing-client data portal and demo request are documented. Personal self-service API signup and a free execution allowance have not been established.

### Sources

- [official_site](https://professional.bloomberg.com/products/data/data-license/) — checked 2026-09-09

<a id="brave-search"></a>

## Brave Search API

Independent web search index with a developer API, self-serve registration, and a free plan.

**Classification:** Search & Data Access / Web Search

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

**Classification:** Travel / Flights

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

**Classification:** Cloud Computing & Hosting / Browser Environments

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

- [official_docs](https://docs.browserbase.com/introduction) — checked 2026-07-07

<a id="capitol-trades"></a>

## Capitol Trades

Public congressional trading website by 2iQ; no self-serve API is established in this record.

**Classification:** Search & Data Access / Financial Data / Transaction Disclosures

[Website](https://www.capitoltrades.com/) · [Source record](../data/candidates/capitol-trades.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="capitol-trades-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [trades-website (WEB)](https://www.capitoltrades.com/trades) | — | self serve / documented | Official indexed pages describe free public access. Direct page fetch returned 403 during this review; browser usability, automation terms and any personal API access remain unverified. |

### Service pricing

—

### Task results

—

### Sources

- [official_site](https://www.capitoltrades.com/about-us) — checked 2026-09-15
- [official_site](https://www.capitoltrades.com/index) — checked 2026-09-15

<a id="capitol-exposed"></a>

## CapitolExposed

Congressional disclosures and related public records, with a keyless read API and separate paid features.

**Classification:** Search & Data Access / Financial Data / Transaction Disclosures

[Website](https://www.capitolexposed.com/) · [Source record](../data/candidates/capitol-exposed.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="capitol-exposed-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api-keyless (API)](https://www.capitolexposed.com/api/v1) | [Docs](https://www.capitolexposed.com/api-docs) | self serve / documented | Keyless requests are limited by IP. Terms require attribution; raw-data resale and competing services have additional restrictions. Use the records API, not its separately metered AI research product. |

### Service pricing

- data-api-keyless: 60 requests / minute (free_allowance; Free member/trade list endpoints; separate limits apply to search, exports and AI tools.)

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
| --- | --- | --- | --- | --- |
| API | [No account or key supplied](../data/experiments/evaluations/capitol-business.json) | [192.5k](../data/experiments/evaluations/capitol-access.json) | 138.671707s | 0 |

#### Set up this financial-data service, confirm that it can query data through the specified interface, and save the configuration needed for later use. If access is blocked, explain where.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-bd611da6270b) | [100%](./evaluations.md#comparison-bd611da6270b) | 192.5k | $0.0091 | $0 |

<details>
<summary>Task, conditions and evidence</summary>

The service, required interface, and any supplied account or signup information are specified in the environment. Use account-free access directly when available. For signup, use only the identity information supplied for this trial. Retain the necessary connection configuration for later tasks.

**Completion:** Complete the required signup, authentication and configuration for the specified interface, and query real financial data. Necessary configuration works in a fresh session. Do not force registration for account-free routes. Documentation, a health check or a configuration file alone does not establish data access.

1.18.29 · glm-5.3-flash / high · 600s · 2026-09-15 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-bd611da6270b)

[Task definition](./tasks.en.md#financial-access-001-v1)

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| financial-access-001 v1 | API | [completed](../data/experiments/evaluations/capitol-access.json) | 2026-09-15 |

</details>

### Task results

#### Summarize the stock purchases and sales Richard W. Allen filed with the U.S. House in August 2026. Include the stock, direction, transaction date, filing date, amount range and original filing source.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-ee257df56f0f) | [100%](./evaluations.md#comparison-ee257df56f0f) | 321.9k | $0.02 | $0 |

<details>
<summary>Task, conditions and evidence</summary>

Filer: Richard W. Allen, Georgia district 12 (GA12). Select Periodic Transaction Reports by official filing date from 2026-08-01 through 2026-08-31, publicly available as of 2026-09-15. Include reported family-member transactions and retain USD amount ranges. Common stock only, excluding options, funds, bonds and other assets. Filing in August does not mean trading in August. This is for private reading; no data export is needed.

**Completion:** Match all applicable records in the independently frozen official index and PTR, without duplicates or unsupported additions. Real queries to the specified service support the disclosures; original filings may supplement date and provenance verification. Use the official index filing date, distinct from trade, notification and service ingestion/publication dates. Do not present midpoints, estimated prices or family-member trades as exact personal trades by the member. Identify the specific original filing rather than only the portal.

1.18.29 · glm-5.3-flash / high · 600s · 2026-09-15 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-ee257df56f0f)

[Task definition](./tasks.en.md#financial-disclosures-001-v1)

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| financial-disclosures-001 v1 | API | [completed](../data/experiments/evaluations/capitol-business.json) | 2026-09-15 |

</details>

### Sources

- [official_docs](https://www.capitolexposed.com/api-docs) — checked 2026-09-15
- [official_site](https://www.capitolexposed.com/terms) — checked 2026-09-15

<a id="cartesia"></a>

## Cartesia

Low-latency voice models (Sonic TTS, Ink STT) with a documented API, official MCP server, llms.txt, and a free tier.

**Classification:** AI Services / Speech Synthesis; AI Services / Speech Recognition; Communication / Voice Agents

[Website](https://cartesia.ai) · [Source record](../data/providers/cartesia.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="cartesia-access"></a>

[Docs](https://docs.cartesia.ai) · [API reference](https://docs.cartesia.ai/api-reference) · [MCP entry](https://github.com/cartesia-ai/cartesia-mcp)

—

### Service pricing

[Official pricing](https://www.cartesia.ai/pricing)

### Task results

—

### Notes

- Sonic speech synthesis, Ink transcription and Managed Agents are distinct products/features; model-specific route coverage remains unrecorded.

### Sources

- [official_docs](https://docs.cartesia.ai/get-started/overview) — checked 2026-09-15

<a id="cerebras"></a>

## Cerebras Inference

Wafer-scale inference for open models at very high tokens/sec, OpenAI-compatible API, llms.txt, and a standing free tier.

**Classification:** AI Services / Model Access

[Website](https://cloud.cerebras.ai) · [Source record](../data/providers/cerebras.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="cerebras-access"></a>

[Docs](https://inference-docs.cerebras.ai) · [API reference](https://inference-docs.cerebras.ai/api-reference/chat-completions)

—

### Service pricing

[Official pricing](https://www.cerebras.ai/pricing)

### Task results

—

### Sources

- [official_docs](https://inference-docs.cerebras.ai/introduction) — checked 2026-07-08

<a id="checkout-com"></a>

## Checkout.com

Payment Links API for hosted checkout, with separate sandbox and production API hosts.

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Databases / Vector Databases

[Website](https://www.trychroma.com) · [Source record](../data/providers/chroma.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="chroma-access"></a>

[Docs](https://docs.trychroma.com) · [API reference](https://docs.trychroma.com/docs/overview/introduction) · [CLI](https://docs.trychroma.com/docs/cli/install) · [MCP entry](https://github.com/chroma-core/chroma-mcp)

—

### Service pricing

[Official pricing](https://www.trychroma.com/pricing)

### Task results

—

### Notes

- Chroma stores embeddings and searches vectors. The record covers Cloud and open-source deployment; their access requirements are separate. Document payload storage is not evidence of a general document database.

### Sources

- [official_docs](https://docs.trychroma.com/docs/overview/introduction) — checked 2026-09-15

<a id="cloudflare"></a>

## Cloudflare

Edge network, Workers serverless platform, storage, and AI services with agent-focused docs and official MCP servers.

**Classification:** Cloud Computing & Hosting / Application Hosting; Databases / Hosted Relational Databases; Databases / Key-value Databases

[Website](https://www.cloudflare.com) · [Source record](../data/providers/cloudflare.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="cloudflare-access"></a>

[Docs](https://developers.cloudflare.com) · [API reference](https://developers.cloudflare.com/api/) · [CLI](https://developers.cloudflare.com/workers/wrangler/) · [SDK](https://developers.cloudflare.com/fundamentals/api/reference/sdks/) · [MCP entry](https://github.com/cloudflare/mcp-server-cloudflare)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [d1-cli (CLI)](https://developers.cloudflare.com/d1/get-started/) | [Docs](https://developers.cloudflare.com/d1/get-started/) | self serve / documented | D1 Workers Free: 5 million reads/day, 100,000 writes/day, 5 GB total storage. Account authorization required; Wrangler local mode is not a remote database test. Existing paid projects are excluded. |
| [kv-api (API)](https://api.cloudflare.com/client/v4/) | [Docs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/get/) | self serve | Documented remote Workers KV key-value read API. Requires account and namespace identifiers and credentials with permission for the requested operation. No task success is claimed. |
| [kv-sdk (SDK)](https://developers.cloudflare.com/api/typescript/resources/kv/subresources/namespaces/subresources/values/methods/get/) | [Docs](https://developers.cloudflare.com/api/typescript/resources/kv/subresources/namespaces/subresources/values/methods/get/) | self serve | Official cloudflare TypeScript client exposes remote KV namespace and value methods. Local package installation is distinct from obtaining credentials and remote resource access. |
| [kv-cli (CLI)](https://developers.cloudflare.com/kv/reference/kv-commands/) | [Docs](https://developers.cloudflare.com/kv/reference/kv-commands/) | self serve | Wrangler provides native KV namespace, key-list and key-read commands. Remote storage must be selected for comparison with cloud API/SDK/MCP; local simulation is not equivalent. |
| [api-mcp (MCP)](https://mcp.cloudflare.com/mcp) | [Docs](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/) | self serve | Official remote API MCP exposes search and execute tools for Cloudflare API operations, including KV. Record the actual exposed tools and native MCP calls separately from raw HTTP. An existing Wrangler OAuth login is not assumed to authorize this endpoint. |

### Service pricing

[Official pricing](https://www.cloudflare.com/plans/)

- d1-cli: 5 GB / account (free_allowance; D1 total storage on Workers Free; separate daily row quotas.)

### Task results

—

### Sources

- [official_docs](https://developers.cloudflare.com/d1/get-started/) — checked 2026-09-07
- [official_docs](https://developers.cloudflare.com/d1/platform/pricing/) — checked 2026-09-07
- [official_docs](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/get/) — checked 2026-09-10
- [official_docs](https://developers.cloudflare.com/api/typescript/resources/kv/subresources/namespaces/subresources/values/methods/get/) — checked 2026-09-10
- [official_docs](https://developers.cloudflare.com/kv/reference/kv-commands/) — checked 2026-09-10
- [official_docs](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/) — checked 2026-09-10
- [official_docs](https://developers.cloudflare.com/kv/) — checked 2026-09-15

<a id="coda"></a>

## Coda / Superhuman Docs

Docs and tables with a free REST API; current API page is branded Superhuman Docs.

**Classification:** Workplace Collaboration / Collaborative Tables; Workplace Collaboration / Document Collaboration

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

### Notes

- Document and messaging membership does not transfer collaborative-table trial results to those tasks.

### Sources

- [official_docs](https://coda.io/developers/apis/v1) — checked 2026-09-08
- [official_docs](https://help.coda.io/hc/en-us/articles/44722661982989-Connect-to-the-Coda-MCP) — checked 2026-09-08
- [official_docs](https://coda.io/developers/apis/v1) — checked 2026-09-15

<a id="cog-depot"></a>

## Cog Depot

Hosted marketplace for agents to discover counterparties, negotiate capability exchanges and obtain direct contact details after paying platform fees.

**Classification:** Agent Infrastructure & Automation

[Website](https://cogdepot.com/) · [Source record](../data/candidates/cog-depot.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="cog-depot-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [marketplace-api (API)](https://api.cogdepot.com) | [Docs](https://cogdepot.com/docs) | self serve | Complete email, Google or GitHub web signup and transfer the issued key to the agent.; Registration alone does not establish readiness to trade. Negotiation needs enough credits for its fee hold; x402-funded accounts receive no welcome grant merely for paying. |
| [marketplace-a2a (API)](https://api.cogdepot.com/a2a) | [Docs](https://cogdepot.com/docs/machine-discovery) | — | Official docs describe A2A v1.0 over JSON-RPC and the Agent Card at /.well-known/agent-card.json. Authentication details and protocol conformance were not independently verified; no task result is implied. |
| [marketplace-mcp-local (MCP)](https://github.com/cogdepot/mcp-server) | [Docs](https://github.com/cogdepot/mcp-server#install) | self serve | Local stdio wrapper published as @cogdepot/mcp-server, started with npx. A preview has no search or pagination; the full feed is charged. Uses the same service credits; no local installation or task was tested. |
| [marketplace-mcp-remote (MCP)](https://mcp.cogdepot.com) | [Docs](https://github.com/cogdepot/mcp-server#remote-hosted-oauth) | self serve | Sign in and authorize the hosted MCP connector.; Hosted OAuth documents action-scoped access, unlike the original PR's account-key-only description. This does not establish scopes for static API keys or imply tested authorization behavior. |

### Service pricing

- marketplace-api: 20000 credits / eligible account (free_allowance; Web signup receives the grant immediately; API signup starts at zero and must verify domain control, once per domain and account. Granted credits are not cash or measured savings.)

- marketplace-api: 1 credits / billable listing request (usage; Published metering for posting a listing, a feed page or an individual listing read; pricing explicitly values one credit at USD 0.0005.)

- marketplace-api: 200 credits / posted listing (usage; Posting fee in addition to the metered request. Unfunded accounts have a lifetime limit of three listings regardless of granted balance.)

- marketplace-api: 2000 credits / party per sealed deal (usage; The opener reserves this platform fee when a thread opens; capture occurs at seal, when the poster also pays. The underlying service purchase is separate.)

- marketplace-api: 0.5 USD / smallest listed x402 credit pack (minimum_spend; Published equivalent for 1000 credits paid in USDC on Base; insufficient by itself for the 2000-credit deal fee. Not a required signup payment or observed expenditure.)

### Task results

—

### Notes

- Originally submitted by the vendor in https://github.com/Olorinm/agent-friendly-services/pull/7; reviewed on 2026-09-15 at head f97e8ef286f3feeba7e83ef086fbd5b354213cb2. The July submission's absent-MCP claim is superseded by current official documentation.
- The terms exclude users located in, or nationals/residents of, Cuba, Iran, North Korea, Syria and Russia and named restricted parties. Their B2B description does not establish a company-registration requirement or ordinary-person eligibility; those remain unknown.
- Escrow covers platform fees only. Counterparties exchange work and payment directly after introduction; Cog Depot does not hold the purchase price or guarantee delivery. Crypto funding of platform credits must not be described as settlement of the underlying deal.

### Sources

- [official_docs](https://cogdepot.com/docs) — checked 2026-09-15
- [official_docs](https://cogdepot.com/docs/machine-discovery) — checked 2026-09-15
- [official_repo](https://github.com/cogdepot/mcp-server) — checked 2026-09-15
- [official_docs](https://cogdepot.com/docs/full-flow) — checked 2026-09-15
- [official_site](https://cogdepot.com/auth/signup) — checked 2026-09-15
- [official_docs](https://cogdepot.com/pricing) — checked 2026-09-15
- [official_docs](https://cogdepot.com/terms) — checked 2026-09-15

<a id="cohere"></a>

## Cohere

Enterprise LLM platform (command, embed, rerank) with llms.txt, documented API versioning, free trial keys, and error/rate-limit docs.

**Classification:** AI Services / Model Access

[Website](https://cohere.com) · [Source record](../data/providers/cohere.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="cohere-access"></a>

[Docs](https://docs.cohere.com) · [API reference](https://docs.cohere.com/reference/about)

—

### Service pricing

[Official pricing](https://cohere.com/pricing)

### Task results

—

### Sources

- [official_docs](https://docs.cohere.com/docs/rate-limits) — checked 2026-07-07

<a id="coingecko"></a>

## CoinGecko

Crypto prices and market data with a free Demo API plan and official keyless or authenticated MCP servers.

**Classification:** Search & Data Access / Financial Data / Asset Prices

[Website](https://www.coingecko.com/) · [Source record](../data/candidates/coingecko.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="coingecko-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://docs.coingecko.com/docs/setting-up-your-api-key) | [Docs](https://docs.coingecko.com/docs/setting-up-your-api-key) | self serve / documented | Demo and paid API plans have different history and quotas. Keyless MCP has shared limits and a smaller tool set. Asset IDs and quote currency must match the task. |
| [keyless-mcp (MCP)](https://mcp.api.coingecko.com/mcp) | [Docs](https://docs.coingecko.com/ai-integration/mcp-server) | self serve / documented | Free, shared rate limits, limited tool set; account and key not required. |
| [keyed-mcp (MCP)](https://mcp.pro-api.coingecko.com/mcp) | [Docs](https://docs.coingecko.com/ai-integration/mcp-server) | self serve / documented | Account entitlement and tool set differ from keyless MCP; confirm free Demo compatibility before a paid-server call. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://docs.coingecko.com/docs/setting-up-your-api-key) — checked 2026-09-09
- [official_docs](https://docs.coingecko.com/) — checked 2026-09-09
- [official_docs](https://docs.coingecko.com/ai-integration/mcp-server) — checked 2026-09-09
- [official_docs](https://docs.coingecko.com/reference/simple-price) — checked 2026-09-15

<a id="coinmarketcap"></a>

## CoinMarketCap

Crypto market data with selected keyless endpoints and a free authenticated Basic plan.

**Classification:** Search & Data Access / Financial Data / Asset Prices

[Website](https://coinmarketcap.com/) · [Source record](../data/candidates/coinmarketcap.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="coinmarketcap-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://coinmarketcap.com/api/) | — | self serve / documented | Basic advertises 15,000 monthly call credits and 50 requests/minute. History depth and endpoint availability depend on plan; keyless access is limited to selected endpoints. |

### Service pricing

- data-api: 15000 credits / month (free_allowance; Authenticated Basic plan; selected endpoints and history only.)

### Task results

—

### Sources

- [official_site](https://coinmarketcap.com/api/) — checked 2026-09-09

<a id="composio"></a>

## Composio

Tool and integration layer for AI agents (hundreds of app connectors with managed auth), with llms.txt and a hosted MCP directory.

**Classification:** Agent Infrastructure & Automation / Tool Connections

[Website](https://composio.dev) · [Source record](../data/providers/composio.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="composio-access"></a>

[Docs](https://docs.composio.dev) · [MCP entry](https://mcp.composio.dev) · [MCP setup](https://docs.composio.dev/docs/composio-connect)

—

### Service pricing

[Official pricing](https://composio.dev/pricing)

### Task results

—

### Notes

- Managed app authentication and callable tool actions establish tool connections; an integration listing does not certify every connected application task.
- MCP setup documentation checked on 2026-09-09: https://docs.composio.dev/docs/composio-connect. The server or product entry remains separately recorded in mcp_official.

### Sources

- [official_docs](https://docs.composio.dev/docs) — checked 2026-09-15

<a id="congress-stock-tracker"></a>

## Congress Stock Tracker

Licensed congressional transaction datasets with source links and amendment history; pricing is negotiated.

**Classification:** Search & Data Access / Financial Data / Transaction Disclosures

[Website](https://www.congressstock.com/) · [Source record](../data/candidates/congress-stock-tracker.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="congress-stock-tracker-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [licensed-api (API)](https://www.congressstock.com/congress-trading-api) | [Docs](https://www.congressstock.com/congress-trading-api) | application | Request a dataset licence and access terms.; Contact-based pricing; no self-serve free tier. An evaluation extract or discounted academic/non-commercial access requires a request and is not an issued API entitlement. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://www.congressstock.com/congress-trading-api) — checked 2026-09-15

<a id="creem"></a>

## Creem

Digital-product checkout and billing APIs with separate test mode and reviewed merchant accounts.

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Developer Tools / Monitoring & Troubleshooting

[Website](https://www.datadoghq.com) · [Source record](../data/providers/datadog.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="datadog-access"></a>

[Docs](https://docs.datadoghq.com) · [API reference](https://docs.datadoghq.com/api/latest/) · [CLI](https://github.com/DataDog/datadog-ci) · [MCP entry](https://docs.datadoghq.com/bits_ai/mcp_server)

—

### Service pricing

[Official pricing](https://www.datadoghq.com/pricing)

### Task results

—

### Sources

- [official_docs](https://docs.datadoghq.com/account_management/api-app-keys) — checked 2026-07-07

<a id="deepgram"></a>

## Deepgram

Speech-to-text and voice AI API with a public OpenAPI spec, llms.txt, scoped API keys, and $200 free credit without a card.

**Classification:** AI Services / Speech Recognition; AI Services / Speech Synthesis; Communication / Voice Agents

[Website](https://deepgram.com) · [Source record](../data/providers/deepgram.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="deepgram-access"></a>

[Docs](https://developers.deepgram.com/docs) · [API reference](https://developers.deepgram.com/reference) · [SDK](https://developers.deepgram.com/docs/deepgram-sdks)

—

### Service pricing

[Official pricing](https://deepgram.com/pricing)

### Task results

—

### Notes

- Transcription, speech synthesis and the Voice Agent API have separate model/route coverage.

### Sources

- [official_docs](https://developers.deepgram.com/home) — checked 2026-09-15

<a id="deepseek"></a>

## DeepSeek

OpenAI-compatible LLM API (DeepSeek-V3/R1) with transparent per-token pricing, a detailed changelog, and self-serve keys.

**Classification:** AI Services / Model Access

[Website](https://www.deepseek.com) · [Source record](../data/providers/deepseek.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="deepseek-access"></a>

[Docs](https://api-docs.deepseek.com)

—

### Service pricing

[Official pricing](https://api-docs.deepseek.com/quick_start/pricing)

### Task results

—

### Sources

- [official_docs](https://api-docs.deepseek.com/quick_start/pricing) — checked 2026-07-07

<a id="discord"></a>

## Discord

Chat platform with a versioned bot/OAuth2 API, official OpenAPI spec (preview), webhooks, and documented rate limits.

**Classification:** Communication / Messaging

[Website](https://discord.com) · [Source record](../data/providers/discord.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="discord-access"></a>

[Docs](https://discord.com/developers/docs/intro) · [API reference](https://discord.com/developers/docs/reference)

—

### Service pricing

—

### Task results

—

### Notes

- Scope is authorized bot/application messaging, not unrestricted access to personal messages.
- The official OpenAPI spec is published by Discord but marked public preview / subject to change.

### Sources

- [official_docs](https://docs.discord.com/developers/intro) — checked 2026-09-15

<a id="dodo-payments"></a>

## Dodo Payments

Merchant-of-record checkout for one-time and subscription sales, with test mode, APIs, CLI and MCP documentation.

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Workplace Collaboration / File Sharing

[Website](https://www.dropbox.com) · [Source record](../data/providers/dropbox.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="dropbox-access"></a>

[Docs](https://www.dropbox.com/developers/documentation) · [API reference](https://www.dropbox.com/developers/documentation/http/documentation) · [CLI](https://github.com/dropbox/dbxcli)

—

### Service pricing

[Official pricing](https://www.dropbox.com/plans)

### Task results

—

### Notes

- Dropbox file/folder access and shared links; document editing is not established by file storage alone.

### Sources

- [official_docs](https://www.dropbox.com/developers/documentation) — checked 2026-09-15

<a id="duffel-flights"></a>

## Duffel Flights API

Flight API whose self-serve test environment must be distinguished from live account activation.

**Classification:** Travel / Flights

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

**Classification:** Cloud Computing & Hosting / Code Sandboxes

[Website](https://e2b.dev) · [Source record](../data/providers/e2b.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="e2b-access"></a>

[Docs](https://e2b.dev/docs) · [CLI](https://e2b.dev/docs/cli) · [SDK](https://e2b.dev/docs/sdk-reference) · [MCP entry](https://github.com/e2b-dev/mcp-server)

—

### Service pricing

[Official pricing](https://e2b.dev/pricing)

### Task results

—

### Sources

- [official_docs](https://e2b.dev/docs/api-key) — checked 2026-07-07

<a id="ecb-data"></a>

## ECB Data Portal API

European Central Bank statistical data, including historical reference exchange rates, through SDMX REST.

**Classification:** Search & Data Access / Financial Data / Exchange Rates; Search & Data Access / Financial Data / Economic Indicators

[Website](https://data.ecb.europa.eu/) · [Source record](../data/candidates/ecb-data.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="ecb-data-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://data-api.ecb.europa.eu/service/) | [Docs](https://data.ecb.europa.eu/help/api/data-examples) | self serve / documented | Series dimensions, quote direction, observation frequency and date range must be selected correctly. Reference rates are not executable conversion prices. Reference-rate information is freely published under the ECB reuse policy; fees for a run still require observation of the actual route. The documentation page was temporarily unreadable during the latest research pass. |

### Service pricing

—

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
| --- | --- | --- | --- | --- |
| API | [No account or key supplied](../data/experiments/evaluations/ecb-business.json) | [221.9k](../data/experiments/evaluations/ecb-access.json) | 216.897575s | 0 |

#### Set up this financial-data service, confirm that it can query data through the specified interface, and save the configuration needed for later use. If access is blocked, explain where.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-bd611da6270b) | [100%](./evaluations.md#comparison-bd611da6270b) | 221.9k | $0.01 | $0 |

<details>
<summary>Task, conditions and evidence</summary>

The service, required interface, and any supplied account or signup information are specified in the environment. Use account-free access directly when available. For signup, use only the identity information supplied for this trial. Retain the necessary connection configuration for later tasks.

**Completion:** Complete the required signup, authentication and configuration for the specified interface, and query real financial data. Necessary configuration works in a fresh session. Do not force registration for account-free routes. Documentation, a health check or a configuration file alone does not establish data access.

1.18.29 · glm-5.3-flash / high · 600s · 2026-09-15 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-bd611da6270b)

[Task definition](./tasks.en.md#financial-access-001-v1)

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| financial-access-001 v1 | API | [completed](../data/experiments/evaluations/ecb-access.json) | 2026-09-15 |

</details>

### Task results

#### Convert these three USD expenses into EUR using the European Central Bank reference rate for each expense date. List each converted amount and the total, and cite the exchange-rate source.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-d86a11990066) | [100%](./evaluations.md#comparison-d86a11990066) | 62.8k | $0.0034 | $0 |

<details>
<summary>Task, conditions and evidence</summary>

Synthetic expenses: August 14, 2026: USD 80.00; August 15, 2026: USD 125.00; August 17, 2026: USD 39.90. If no rate was published on the expense date, use the most recent earlier publication date. Round each converted amount to euro cents, then sum. Exclude fees.

**Completion:** Use the corresponding ECB USD/EUR reference observations. Select the preceding published rate on non-publication dates. Quote direction, multiplication or division, individual cent rounding and the total match the independent reference. Core rates come from the specified service.

1.18.29 · glm-5.3-flash / high · 600s · 2026-09-15 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-d86a11990066)

[Task definition](./tasks.en.md#financial-fx-001-v1)

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| financial-fx-001 v1 | API | [completed](../data/experiments/evaluations/ecb-business.json) | 2026-09-15 |

</details>

### Sources

- [official_docs](https://data.ecb.europa.eu/help/api/data-examples) — checked 2026-09-09
- [official_site](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) — checked 2026-09-15
- [official_site](https://www.ecb.europa.eu/services/using-our-site/disclaimer/html/index.en.html) — checked 2026-09-15
- [official_docs](https://data.ecb.europa.eu/help/api/schemas) — checked 2026-09-15
- [official_docs](https://www.ecb.europa.eu/stats/accessing-our-data/html/index.en.html) — checked 2026-09-15

<a id="elevenlabs"></a>

## ElevenLabs

Voice AI (TTS, STT, agents) with a public OpenAPI spec, llms.txt, an official MCP server, and a free tier.

**Classification:** AI Services / Speech Synthesis; AI Services / Speech Recognition; Communication / Voice Agents

[Website](https://elevenlabs.io) · [Source record](../data/providers/elevenlabs.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="elevenlabs-access"></a>

[Docs](https://elevenlabs.io/docs) · [API reference](https://elevenlabs.io/docs/api-reference/introduction) · [MCP entry](https://github.com/elevenlabs/elevenlabs-mcp)

—

### Service pricing

[Official pricing](https://elevenlabs.io/pricing)

### Task results

—

### Notes

- Speech synthesis, transcription and conversational agents are documented separately. Other creative products need product-specific route research.

### Sources

- [official_docs](https://elevenlabs.io/docs/overview/intro) — checked 2026-09-15

<a id="eodhd"></a>

## EODHD

Historical market prices, fundamentals, economic datasets and congressional trades, with dataset-specific plan entitlements.

**Classification:** Search & Data Access / Financial Data / Asset Prices; Search & Data Access / Financial Data / Company Financials; Search & Data Access / Financial Data / Economic Indicators; Search & Data Access / Financial Data / Transaction Disclosures

[Website](https://eodhd.com/) · [Source record](../data/candidates/eodhd.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="eodhd-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://eodhd.com/financial-apis/) | [Docs](https://eodhd.com/financial-apis/) | self serve / documented | Free registration advertises 20 API calls/day without a card; some data types are excluded. Check dataset and market coverage before choosing a trial. Congressional Trades is documented for the All-in-one plan; the generic 20-call free allowance does not establish access to this dataset. |

### Service pricing

- data-api: 20 requests / day (free_allowance; Free plan; some data types are excluded.)

### Task results

—

### Sources

- [official_docs](https://eodhd.com/financial-apis/) — checked 2026-09-09
- [official_site](https://eodhd.com/pricing) — checked 2026-09-15
- [official_docs](https://eodhd.com/financial-apis/congressional-trades-api) — checked 2026-09-15
- [official_announcement](https://eodhd.com/financial-apis-blog/introducing-the-congressional-trades-api) — checked 2026-09-15

<a id="exa"></a>

## Exa

Search API built for AI — semantic web search, content retrieval, and research endpoints with an official MCP server.

**Classification:** Search & Data Access / Web Content Extraction; Search & Data Access / Web Search

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

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
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
- [official_docs](https://exa.ai/docs/get-started/exa-mcp) — checked 2026-09-15

<a id="expedia-xap-flights"></a>

## Expedia XAP Flight Listings

Travel Redirect/XAP flight listings product whose new API applications are currently paused.

**Classification:** Travel / Flights

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

<a id="factset-data"></a>

## FactSet Data APIs

Financial-data API catalog; retained as an institutional candidate while product-specific access is researched.

**Classification:** Search & Data Access / Financial Data

[Website](https://www.factset.com/) · [Source record](../data/candidates/factset-data.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="factset-data-access"></a>

—

### Service pricing

—

### Task results

—

### Notes

- Institutional API marketplace; select a concrete dataset/product and source before assigning a narrower class.
- Developer portal is discoverable, but the exact dataset, individual eligibility, credentials and price remain unconfirmed. No claim of free self-service access.

### Sources

- [official_docs](https://developer.factset.com/) — checked 2026-09-09

<a id="fal"></a>

## fal.ai

Generative media platform (image, video, audio models) with queue/streaming APIs, an official CLI/serving framework, llms.txt, and self-serve keys.

**Classification:** AI Services / Model Access; AI Services / Image Generation; AI Services / Video Generation

[Website](https://fal.ai) · [Source record](../data/providers/fal.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="fal-access"></a>

[Docs](https://fal.ai/docs) · [API reference](https://fal.ai/docs/model-apis) · [CLI](https://github.com/fal-ai/fal)

—

### Service pricing

[Official pricing](https://fal.ai/pricing)

### Task results

—

### Notes

- Model APIs expose identifiable media models for image and video generation. A model listing is not proof of every model/route entitlement.

### Sources

- [official_docs](https://fal.ai/docs/documentation/model-apis/overview) — checked 2026-09-15

<a id="fastmail"></a>

## Fastmail

Persistent email with JMAP API tokens, OAuth and standard mail protocols.

**Classification:** Communication / Mailboxes

[Website](https://www.fastmail.com/) · [Source record](../data/candidates/fastmail.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="fastmail-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [mail-api (API)](https://www.fastmail.com/dev/) | [Docs](https://www.fastmail.com/dev/) | — | JMAP tokens can be generated for an existing account. Subscription/trial API eligibility is not yet verified; do not assume permanent free access. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://www.fastmail.com/dev/) — checked 2026-09-09

<a id="fastspring"></a>

## FastSpring

Checkout and subscription platform with API, JavaScript checkout libraries and order webhooks.

**Classification:** Payments / Billing / Payment Acceptance

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

<a id="financial-datasets"></a>

## Financial Datasets

US company financial statements, historical prices, filings and insider trades, with API and an officially listed MCP integration.

**Classification:** Search & Data Access / Financial Data / Asset Prices; Search & Data Access / Financial Data / Company Financials; Search & Data Access / Financial Data / Transaction Disclosures

[Website](https://financialdatasets.ai/) · [Source record](../data/candidates/financial-datasets.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="financial-datasets-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://docs.financialdatasets.ai/quickstart) | [Docs](https://docs.financialdatasets.ai/quickstart) | self serve / documented | Create an account and key. A free execution allowance has not been established; do not start metered requests without confirming available free credit. |

### Service pricing

—

### Task results

—

### Notes

- Official index lists https://docs.financialdatasets.ai/mcp-server.md; the setup page was not retrievable in this pass.

### Sources

- [official_docs](https://docs.financialdatasets.ai/quickstart) — checked 2026-09-15
- [official_docs](https://docs.financialdatasets.ai/llms.txt) — checked 2026-09-09

<a id="fmp"></a>

## Financial Modeling Prep (FMP)

Stock prices, financial statements, FX, crypto and congressional disclosures through a keyed API and official MCP.

**Classification:** Search & Data Access / Financial Data / Asset Prices; Search & Data Access / Financial Data / Company Financials; Search & Data Access / Financial Data / Exchange Rates; Search & Data Access / Financial Data / Transaction Disclosures

[Website](https://financialmodelingprep.com/) · [Source record](../data/candidates/fmp.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="fmp-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://site.financialmodelingprep.com/developer/docs) | [Docs](https://site.financialmodelingprep.com/developer/docs) | self serve / documented | Basic is free with 250 calls/day and end-of-day/profile/reference features. Annual fundamentals are listed under paid Starter; a free key does not establish access to the fiscal-year comparison task. Displaying or redistributing FMP data requires a separate licensing agreement according to its pricing page. The House Trades endpoint is documented, but Congress-specific free-plan entitlement is not confirmed. |
| [data-mcp (MCP)](https://financialmodelingprep.com/mcp) | [Docs](https://site.financialmodelingprep.com/developer/docs/mcp-server) | self serve / documented | Uses the existing API key and plan limits; key must be injected privately, never stored in the URL in public results. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://site.financialmodelingprep.com/developer/docs) — checked 2026-09-09
- [official_docs](https://site.financialmodelingprep.com/developer/docs/pricing) — checked 2026-09-15
- [official_docs](https://site.financialmodelingprep.com/developer/docs/mcp-server) — checked 2026-09-09
- [official_docs](https://site.financialmodelingprep.com/developer/docs/stable/house-trading) — checked 2026-09-15

<a id="finnhub"></a>

## Finnhub

Stock quotes, historical candles and fundamentals; stock candles are documented as premium.

**Classification:** Search & Data Access / Financial Data / Asset Prices

[Website](https://finnhub.io/) · [Source record](../data/candidates/finnhub.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="finnhub-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://finnhub.io/docs/api/quote) | [Docs](https://finnhub.io/docs/api/quote) | self serve | Dashboard API key required. Stock candles require premium access; a working free quote endpoint would not establish free historical-data access. |

### Service pricing

—

### Task results

—

### Notes

- Company fundamentals are mentioned in discovery, but the recorded quote reference does not establish financial-statement fields. Statement classification awaits a specific source.

### Sources

- [official_docs](https://finnhub.io/docs/api/quote) — checked 2026-09-09

<a id="firecrawl"></a>

## Firecrawl

Web scraping and crawling API that turns websites into LLM-ready markdown, with an official MCP server.

**Classification:** Search & Data Access / Web Content Extraction; Search & Data Access / Web Search

[Website](https://www.firecrawl.dev) · [Source record](../data/providers/firecrawl.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="firecrawl-access"></a>

[Docs](https://docs.firecrawl.dev) · [API reference](https://docs.firecrawl.dev/api-reference/introduction) · [SDK](https://docs.firecrawl.dev/sdks/overview) · [MCP entry](https://docs.firecrawl.dev/mcp-server)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [public-search-api (API)](https://docs.firecrawl.dev/features/search) | [Docs](https://docs.firecrawl.dev/features/search) | self serve / documented | Current search docs explicitly permit starting without a key. Anonymous quota is unquantified; account free credits cannot be assumed for this route. |
| [account-search-api (API)](https://docs.firecrawl.dev/features/search) | [Docs](https://docs.firecrawl.dev/features/search) | self serve / documented | Search: 2 credits per 10 results; extra scraping can consume credits. |
| [public-scrape-api (API)](https://api.firecrawl.dev/v2/scrape) | [Docs](https://docs.firecrawl.dev/features/scrape) | — | Specified-URL scraping. Docs allow starting without a key; anonymous limits and paid-account costs are separate and no extraction task has been run. |

### Service pricing

[Official pricing](https://www.firecrawl.dev/pricing)

- account-search-api: 1000 credits / month (free_allowance; Account Free plan; separate from anonymous access.)

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
| --- | --- | --- | --- | --- |
| API (public-search-api) | [No account or key supplied](../data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json) | — | — | — |
| API (account-search-api) | — | — | — | — |
| API (public-scrape-api) | — | — | — | — |

### Task results

#### I am upgrading a Python app to 3.13. Find out whether free threading is enabled by default, how to enable it, and what compatibility limits apply to existing C extensions, with official sources

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API (public-search-api) | [1](./evaluations.md#comparison-b5f21fc39ab4) | [100%](./evaluations.md#comparison-b5f21fc39ab4) | 346.8k | — | $0 |
| API (account-search-api) | — | — | — | — | — |
| API (public-scrape-api) | — | — | — | — | — |

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
- [official_docs](https://docs.firecrawl.dev/features/scrape) — checked 2026-09-15

<a id="fireworks"></a>

## Fireworks AI

Fast open-model inference and fine-tuning with an OpenAI-compatible API, official firectl CLI, llms.txt, and published pricing.

**Classification:** AI Services / Model Access

[Website](https://fireworks.ai) · [Source record](../data/providers/fireworks.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="fireworks-access"></a>

[Docs](https://docs.fireworks.ai) · [API reference](https://docs.fireworks.ai/api-reference/introduction) · [CLI](https://docs.fireworks.ai/tools-sdks/firectl/firectl)

—

### Service pricing

[Official pricing](https://fireworks.ai/pricing)

### Task results

—

### Sources

- [official_docs](https://docs.fireworks.ai/getting-started/introduction) — checked 2026-07-08

<a id="flight-mcp"></a>

## Flight MCP

Authenticated flight lookup and a separate, restricted public cache exposed through REST and MCP.

**Classification:** Travel / Flights

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

**Classification:** Travel / Flights

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

**Classification:** Cloud Computing & Hosting / Application Hosting

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

- [official_docs](https://fly.io/docs/security/tokens/) — checked 2026-07-07

<a id="frankfurter"></a>

## Frankfurter

Public exchange-rate API and official MCP using central-bank reference data, with no API key.

**Classification:** Search & Data Access / Financial Data / Exchange Rates

[Website](https://frankfurter.dev/) · [Source record](../data/candidates/frankfurter.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="frankfurter-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://api.frankfurter.dev/v2/) | [Docs](https://frankfurter.dev/) | self serve / documented | The hosted public API is free with no key or daily/monthly quota; abuse rate limits apply. Default v2 rates blend sources; filter by ECB when the task requires ECB reference data. Reference rates are not executable bank/card quotes. |
| [rates-mcp (MCP)](https://frankfurter.dev/mcp/) | [Docs](https://frankfurter.dev/mcp/) | self serve / documented | Official hosted/local MCP setup guide; uses reference rates, not a payment or currency-trading service. |

### Service pricing

- data-api: 0 USD / public API request (usage; Hosted public API under its documented fair-use rate limiting; underlying provider terms still apply.)

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
| --- | --- | --- | --- | --- |
| API | [No account or key supplied](../data/experiments/evaluations/frankfurter-business.json) | [86.8k](../data/experiments/evaluations/frankfurter-access.json) | 115.282949s | 0 |
| MCP | — | — | — | — |

#### Set up this financial-data service, confirm that it can query data through the specified interface, and save the configuration needed for later use. If access is blocked, explain where.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-bd611da6270b) | [100%](./evaluations.md#comparison-bd611da6270b) | 86.8k | $0.0052 | $0 |
| MCP | — | — | — | — | — |

<details>
<summary>Task, conditions and evidence</summary>

The service, required interface, and any supplied account or signup information are specified in the environment. Use account-free access directly when available. For signup, use only the identity information supplied for this trial. Retain the necessary connection configuration for later tasks.

**Completion:** Complete the required signup, authentication and configuration for the specified interface, and query real financial data. Necessary configuration works in a fresh session. Do not force registration for account-free routes. Documentation, a health check or a configuration file alone does not establish data access.

1.18.29 · glm-5.3-flash / high · 600s · 2026-09-15 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-bd611da6270b)

[Task definition](./tasks.en.md#financial-access-001-v1)

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| financial-access-001 v1 | API | [completed](../data/experiments/evaluations/frankfurter-access.json) | 2026-09-15 |

</details>

### Task results

#### Convert these three USD expenses into EUR using the European Central Bank reference rate for each expense date. List each converted amount and the total, and cite the exchange-rate source.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-d86a11990066) | [100%](./evaluations.md#comparison-d86a11990066) | 54.2k | $0.0038 | $0 |
| MCP | — | — | — | — | — |

<details>
<summary>Task, conditions and evidence</summary>

Synthetic expenses: August 14, 2026: USD 80.00; August 15, 2026: USD 125.00; August 17, 2026: USD 39.90. If no rate was published on the expense date, use the most recent earlier publication date. Round each converted amount to euro cents, then sum. Exclude fees.

**Completion:** Use the corresponding ECB USD/EUR reference observations. Select the preceding published rate on non-publication dates. Quote direction, multiplication or division, individual cent rounding and the total match the independent reference. Core rates come from the specified service.

1.18.29 · glm-5.3-flash / high · 600s · 2026-09-15 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-d86a11990066)

[Task definition](./tasks.en.md#financial-fx-001-v1)

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| financial-fx-001 v1 | API | [completed](../data/experiments/evaluations/frankfurter-business.json) | 2026-09-15 |

</details>

### Sources

- [official_docs](https://frankfurter.dev/) — checked 2026-09-15
- [official_docs](https://frankfurter.dev/mcp/) — checked 2026-09-09

<a id="fred"></a>

## FRED / ALFRED

Economic time series and historical vintages from the Federal Reserve Bank of St. Louis.

**Classification:** Search & Data Access / Financial Data / Economic Indicators

[Website](https://fred.stlouisfed.org/) · [Source record](../data/candidates/fred.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="fred-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://fred.stlouisfed.org/docs/api/fred/) | [Docs](https://fred.stlouisfed.org/docs/api/fred/) | self serve / documented | A registered account can request an API key. Series units, seasonal adjustment, source and vintage matter; not a stock-price provider. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://fred.stlouisfed.org/docs/api/fred/) — checked 2026-09-15
- [official_docs](https://fred.stlouisfed.org/docs/api/api_key.html) — checked 2026-09-09

<a id="gemini-api"></a>

## Gemini API

Google's Gemini model APIs via AI Studio, with generous free tier and documented API versioning.

**Classification:** AI Services / Model Access

[Website](https://ai.google.dev) · [Source record](../data/providers/gemini-api.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="gemini-api-access"></a>

[Docs](https://ai.google.dev/gemini-api/docs) · [API reference](https://ai.google.dev/api) · [CLI](https://github.com/google-gemini/gemini-cli) · [SDK](https://ai.google.dev/gemini-api/docs/libraries)

—

### Service pricing

[Official pricing](https://ai.google.dev/gemini-api/docs/pricing)

### Task results

—

### Sources

- [official_docs](https://ai.google.dev/gemini-api/docs/api-key) — checked 2026-07-07

<a id="github"></a>

## GitHub

Code hosting, collaboration, and automation with REST and GraphQL APIs, an official CLI, and an official MCP server.

**Classification:** Developer Tools / Code Hosting & Review; Workplace Collaboration / Project & Task Management

[Website](https://github.com) · [Source record](../data/providers/github.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="github-access"></a>

[Docs](https://docs.github.com) · [API reference](https://docs.github.com/rest) · [CLI](https://cli.github.com) · [SDK](https://github.com/octokit) · [MCP entry](https://github.com/github/github-mcp-server)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [rest-api (API)](https://api.github.com/) | [Docs](https://docs.github.com/en/rest/quickstart) | self serve / documented | Authenticated REST access; existing account setup and token permissions must be recorded separately from the task. |

### Service pricing

[Official pricing](https://github.com/pricing)

### Task results

—

### Notes

- Multi-product platform; this entry covers the core developer platform only (see scope).

### Sources

- [official_docs](https://docs.github.com/en/rest/quickstart) — checked 2026-09-10
- [official_docs](https://docs.github.com/en/rest) — checked 2026-09-15

<a id="gitlab"></a>

## GitLab

DevOps platform with REST and GraphQL APIs, scoped tokens, llms.txt, and an official CLI.

**Classification:** Developer Tools / Code Hosting & Review; Workplace Collaboration / Project & Task Management

[Website](https://gitlab.com) · [Source record](../data/providers/gitlab.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="gitlab-access"></a>

[Docs](https://docs.gitlab.com) · [API reference](https://docs.gitlab.com/api/rest/) · [CLI](https://gitlab.com/gitlab-org/cli) · [MCP entry](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server)

—

### Service pricing

[Official pricing](https://about.gitlab.com/pricing/)

### Task results

—

### Notes

- Repository/merge-request work and issue/epic tracking are separate supported scopes. SaaS and self-managed access must be distinguished.

### Sources

- [official_docs](https://docs.gitlab.com/user/) — checked 2026-09-15

<a id="gmail"></a>

## Gmail

Persistent Google mailboxes accessible through the Gmail API after account and OAuth setup.

**Classification:** Communication / Mailboxes

[Website](https://mail.google.com/) · [Source record](../data/candidates/gmail.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="gmail-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [mail-api (API)](https://developers.google.com/workspace/gmail/api/guides) | [Docs](https://developers.google.com/workspace/gmail/api/guides) | — | Existing mailbox, API project and scoped OAuth consent are separate preparation steps. Gmail API access is not a public API for creating consumer Google accounts. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://developers.google.com/workspace/gmail/api/guides) — checked 2026-09-09

<a id="google-sheets"></a>

## Google Sheets

Online spreadsheets with a no-additional-cost API; Cloud project and OAuth setup are still prerequisites.

**Classification:** Workplace Collaboration / Collaborative Tables

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

**Classification:** Developer Tools / Monitoring & Troubleshooting

[Website](https://grafana.com) · [Source record](../data/providers/grafana.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="grafana-access"></a>

[Docs](https://grafana.com/docs) · [API reference](https://grafana.com/docs/grafana/latest/developers/http_api/) · [MCP entry](https://github.com/grafana/mcp-grafana)

—

### Service pricing

[Official pricing](https://grafana.com/pricing)

### Task results

—

### Sources

- [official_docs](https://grafana.com/docs/grafana/latest/administration/service-accounts/) — checked 2026-07-08

<a id="grist"></a>

## Grist

Hosted relational spreadsheets with a free personal site, REST API and official MCP.

**Classification:** Workplace Collaboration / Collaborative Tables

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

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
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

**Classification:** AI Services / Model Access

[Website](https://groq.com) · [Source record](../data/providers/groq.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="groq-access"></a>

[Docs](https://console.groq.com/docs) · [API reference](https://console.groq.com/docs/api-reference) · [SDK](https://console.groq.com/docs/libraries)

—

### Service pricing

[Official pricing](https://groq.com/pricing)

### Task results

—

### Sources

- [official_docs](https://console.groq.com/docs/quickstart) — checked 2026-07-07

<a id="guerrilla-mail"></a>

## Guerrilla Mail

Temporary email addresses and message retrieval through a public session-based API.

**Classification:** Communication / Mailboxes

[Website](https://www.guerrillamail.com/) · [Source record](../data/candidates/guerrilla-mail.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="guerrilla-mail-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [mail-api (API)](https://www.guerrillamail.com/GuerrillaMailAPI.html) | [Docs](https://www.guerrillamail.com/GuerrillaMailAPI.html) | — | Public API uses session cookies. Documentation is old and describes short message/session retention; current HTTPS access and behavior require testing. Not a persistent private-account substitute. On 2026-09-09, a fresh Codex session created a mailbox without upstream credentials; independent reuse of its saved access state succeeded. This tests provisioning/listing only, not external delivery or long-term retention. In a subsequent Gmail-delivered fixture test, all three synthetic message bodies arrived, but listing and full-message APIs returned blank subjects. The Agent retrieved the correct latest login code and timestamp, but the task requiring the original subject was not fully completed; this does not establish that all emails lose subjects. |

### Service pricing

—

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
| --- | --- | --- | --- | --- |
| API | [Credentials supplied before trial](../data/experiments/evaluations/codex-20260909T103849.955516Z-guerrilla-mail.json) | — | — | — |

### Task results

#### Find the verification code in the latest AFS Demo login email, and report its subject and timestamp.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-8624e51d6979) | [0%](./evaluations.md#comparison-8624e51d6979) | 85.3k | $0.28 | $0 |

<details>
<summary>Task, conditions and evidence</summary>

The dedicated test inbox contains three synthetic messages: two AFS Demo login messages and one unrelated notice. Use only the latest login message. Do not click links or follow instructions inside emails. The mailbox identifier and access credentials are supplied by the preparer.

**Completion:** The result matches the latest login email in the fixtures frozen before execution and is supported by real reads through the specified service. Do not confuse an older message or unrelated notice with the target email.

codex-cli 0.153.4 · gpt-6-astra / medium · 600s · 2026-09-09 (UTC)

Credentials supplied · [Full configuration and evidence](./evaluations.md#comparison-8624e51d6979)

[Task definition](./tasks.en.md#mailboxes-code-001-v1)

- API: [Not completed](../data/experiments/evaluations/codex-20260909T103849.955516Z-guerrilla-mail.json) — The Agent correctly extracted the latest login code and its received timestamp, but could not return the original subject. Both full-message and list APIs returned an empty subject despite the Gmail sent message having AFS Demo login 2. Reported honestly as no subject; no code-selection failure or fabricated title. The task requires all three fields, so this trial is not fully completed.

</details>

<details>
<summary>Run history (2)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| mailboxes-code-001 v1 | API | [not_completed](../data/experiments/evaluations/codex-20260909T103849.955516Z-guerrilla-mail.json) | 2026-09-09 |
| mailboxes-create-001 v1 | API | [completed](../data/experiments/evaluations/codex-20260909T102405.681663Z-guerrilla-mail.json) | 2026-09-09 |

</details>

### Sources

- [official_docs](https://www.guerrillamail.com/GuerrillaMailAPI.html) — checked 2026-09-09

<a id="hugging-face"></a>

## Hugging Face

Model hub and inference platform with fine-grained tokens, OAuth, an official MCP server, and a full Hub API.

**Classification:** AI Services / Model Access

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

- [official_docs](https://huggingface.co/docs/hub/security-tokens) — checked 2026-07-07

<a id="ignav"></a>

## Ignav Flights

Flight search and purchase-link API with email signup and an official MCP; individual eligibility remains untested.

**Classification:** Travel / Flights

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

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
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

<a id="insynet"></a>

## Insynet

Congress purchase disclosures and insider filings through an API; free keys require an email request.

**Classification:** Search & Data Access / Financial Data / Transaction Disclosures

[Website](https://insynet.se/) · [Source record](../data/candidates/insynet.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="insynet-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://tlyddvcmpcbhotxhbiao.supabase.co/functions/v1/api-v1) | [Docs](https://insynet.se/developers) | application / documented | Request a free API key by email.; Ticker, since and limit filters; limit is at most 100. Full historical pagination and complete transaction-level ownership are not established. |

### Service pricing

- data-api: 100 requests / day (free_allowance; Free-key tier covers all five endpoints with data delayed at least 24 hours after ingestion.)

### Task results

—

### Sources

- [official_docs](https://insynet.se/developers) — checked 2026-09-15

<a id="jina"></a>

## Jina AI

Search-foundation APIs (Reader for URL-to-markdown, embeddings, reranker, deep search) with an official remote MCP server, an agent-targeted llms.txt, and a keyless trial path.

**Classification:** Search & Data Access / Web Content Extraction

[Website](https://jina.ai) · [Source record](../data/providers/jina.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="jina-access"></a>

[Docs](https://docs.jina.ai) · [MCP entry](https://github.com/jina-ai/MCP)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [reader-api (API)](https://r.jina.ai/) | [Docs](https://jina.ai/reader/) | — | Reader converts a supplied URL to text. Keyless basic usage is documented; keyed rate limits and billing are separate. No broader search or embedding capability is inferred from this route. |

### Service pricing

—

### Task results

—

### Sources

- [official_site](https://jina.ai/api-dashboard) — checked 2026-07-08
- [official_docs](https://jina.ai/reader/) — checked 2026-09-15

<a id="joinquant-data"></a>

## JoinQuant JQData

Chinese-market data candidate. The official documentation returned a non-Mainland-China region restriction during research.

**Classification:** Search & Data Access / Financial Data

[Website](https://www.joinquant.com/) · [Source record](../data/candidates/joinquant-data.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="joinquant-data-access"></a>

—

### Service pricing

—

### Task results

—

### Notes

- Chinese-market data remains discoverable. The recorded documentation was region-restricted; supported datasets and reporting fields need direct evidence before narrowing.
- The documentation access restriction was observed through the research browser, not a local API trial. API availability, personal onboarding, transport and free trial remain unverified.

### Sources

- [official_docs](https://www.joinquant.com/help/api/help?name=JQData) — checked 2026-09-09

<a id="kayak-affiliate"></a>

## KAYAK Affiliate API

Affiliate flight APIs with a business application and an optional requested sandbox.

**Classification:** Travel / Flights

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

**Classification:** Travel / Flights

[Website](https://www.kiwi.com/) · [Source record](../data/candidates/kiwi.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="kiwi-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [search-mcp (MCP)](https://mcp.kiwi.com) | [Docs](https://www.kiwi.com/en/pages/mcp/) | self serve | — |
| [tequila-api (API)](https://media.kiwi.com/articles-and-interviews/better-for-business-kiwi-com-takes-a-new-approach-to-partnerships/) | — | invite only | Requires: invitation; Keep invitation-only Tequila separate from the search MCP. Current endpoints and task coverage need further research. |

### Service pricing

—

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
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

**Classification:** Workplace Collaboration / Collaborative Tables; Communication / Messaging; Workplace Collaboration / Document Collaboration

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

### Notes

- International larksuite.com service. Do not transfer Feishu China results to this identity.
- Document and messaging membership does not transfer collaborative-table trial results to those tasks.

### Sources

- [official_docs](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create.md) — checked 2026-09-08
- [official_repo](https://github.com/larksuite/cli) — checked 2026-09-08
- [official_repo](https://github.com/larksuite/lark-openapi-mcp) — checked 2026-09-08
- [official_site](https://www.larksuite.com/en_us/plans) — checked 2026-09-08
- [official_site](https://www.larksuite.com/en_us/paid/collaboration) — checked 2026-09-15

<a id="lemonsqueezy"></a>

## Lemon Squeezy

Merchant-of-record payments for digital products/SaaS with a JSON:API REST API, documented test mode, and self-serve keys.

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Travel / Flights

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

### Notes

- Documentation conflict: current site describes zero-amount Revolut/card setup; repository README described Stripe and older token lifetimes. Recheck current auth discovery before any onboarding. Developer API is a separate paid offering.

### Sources

- [official_docs](https://letsfg.co/for-agents) — checked 2026-09-07
- [official_repo](https://github.com/letsfg/letsfg) — checked 2026-09-07

<a id="linear"></a>

## Linear

Issue tracking and product planning with a GraphQL API, llms.txt, an official MCP server, and webhooks.

**Classification:** Workplace Collaboration / Project & Task Management

[Website](https://linear.app) · [Source record](../data/providers/linear.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="linear-access"></a>

[Docs](https://linear.app/developers) · [MCP entry](https://linear.app/docs/mcp)

—

### Service pricing

[Official pricing](https://linear.app/pricing)

### Task results

—

### Notes

- Issue and project workflows through the Linear developer platform.

### Sources

- [official_docs](https://linear.app/developers) — checked 2026-09-15

<a id="lseg-data"></a>

## LSEG Data Platform

Financial-data platform and Python library with licensed desktop and cloud access paths.

**Classification:** Search & Data Access / Financial Data

[Website](https://www.lseg.com/en/data-analytics) · [Source record](../data/candidates/lseg-data.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="lseg-data-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (SDK)](https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/quick-start) | [Docs](https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/quick-start) | application / restricted | Requires: platform_account; Obtain licensed cloud credentials through an account manager, or provide an existing entitled desktop login.; Cloud credentials require an account manager; desktop access needs a valid Workspace/Eikon login and App Key. Individual admission and trial approval are not established. |

### Service pricing

—

### Task results

—

### Notes

- Licensed data library spans separately entitled datasets; a library quickstart alone does not identify which product this candidate can supply.

### Sources

- [official_docs](https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/quick-start) — checked 2026-09-09

<a id="lufthansa-partner"></a>

## Lufthansa Partner Fare API

Lufthansa fare methods are partner-scoped; the developer portal currently pauses new Open API registrations.

**Classification:** Travel / Flights

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

**Classification:** AI Services / Image Generation; AI Services / Video Generation

[Website](https://lumalabs.ai) · [Source record](../data/providers/luma.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="luma-access"></a>

[Docs](https://docs.lumalabs.ai) · [API reference](https://docs.lumalabs.ai/reference)

—

### Service pricing

[Official pricing](https://lumalabs.ai/api/pricing)

### Task results

—

### Notes

- The Dream Machine API documentation describes image and video generation and redirects readers to newer platform documentation. Current route/plan details still require review.

### Sources

- [official_docs](https://docs.lumalabs.ai/docs/welcome) — checked 2026-09-15

<a id="mail-tm"></a>

## Mail.tm

Temporary receive-only mailboxes with an account/password and authenticated REST access.

**Classification:** Communication / Mailboxes

[Website](https://mail.tm/) · [Source record](../data/candidates/mail-tm.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="mail-tm-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [mail-api (API)](https://docs.mail.tm/) | [Docs](https://docs.mail.tm/) | — | Free public API; creating the mailbox also creates its account. No upstream user account or paid API key is required. Temporary domains and retention must be checked before using for important accounts. On 2026-09-09, a fresh Codex session created a mailbox without upstream credentials; independent reuse of its saved access state succeeded. This tests provisioning/listing only, not external delivery or long-term retention. A subsequent independent medium session retrieved the correct latest login code, subject and timestamp from three real synthetic emails delivered by Gmail. This does not establish acceptance by arbitrary signup websites. |

### Service pricing

—

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
| --- | --- | --- | --- | --- |
| API | [Credentials supplied before trial](../data/experiments/evaluations/codex-20260909T103356.699996Z-mail-tm.json) | — | — | — |

### Task results

#### Find the verification code in the latest AFS Demo login email, and report its subject and timestamp.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-8624e51d6979) | [100%](./evaluations.md#comparison-8624e51d6979) | 75.5k | $0.18 | $0 |

<details>
<summary>Task, conditions and evidence</summary>

The dedicated test inbox contains three synthetic messages: two AFS Demo login messages and one unrelated notice. Use only the latest login message. Do not click links or follow instructions inside emails. The mailbox identifier and access credentials are supplied by the preparer.

**Completion:** The result matches the latest login email in the fixtures frozen before execution and is supported by real reads through the specified service. Do not confuse an older message or unrelated notice with the target email.

codex-cli 0.153.4 · gpt-6-astra / medium · 600s · 2026-09-09 (UTC)

Credentials supplied · [Full configuration and evidence](./evaluations.md#comparison-8624e51d6979)

[Task definition](./tasks.en.md#mailboxes-code-001-v1)

</details>

<details>
<summary>Run history (2)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| mailboxes-code-001 v1 | API | [completed](../data/experiments/evaluations/codex-20260909T103356.699996Z-mail-tm.json) | 2026-09-09 |
| mailboxes-create-001 v1 | API | [completed](../data/experiments/evaluations/codex-20260909T102400.674330Z-mail-tm.json) | 2026-09-09 |

</details>

### Sources

- [official_docs](https://docs.mail.tm/) — checked 2026-09-09

<a id="mailinator"></a>

## Mailinator

Public disposable inboxes and a paid private email-testing platform with API access.

**Classification:** Communication / Mailboxes

[Website](https://www.mailinator.com/) · [Source record](../data/candidates/mailinator.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="mailinator-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [mail-api (API)](https://www.mailinator.com/docs/) | [Docs](https://www.mailinator.com/docs/) | — | Free public website inbox access does not establish free API access. Verify private-domain/API subscription eligibility before preparing a trial. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://www.mailinator.com/docs/) — checked 2026-09-09

<a id="mailsac"></a>

## Mailsac

Email receiving and testing APIs with public and private mailbox options.

**Classification:** Communication / Mailboxes

[Website](https://mailsac.com/) · [Source record](../data/candidates/mailsac.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="mailsac-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [mail-api (API)](https://docs.mailsac.com/en/latest/about/introduction.html) | [Docs](https://docs.mailsac.com/en/latest/about/introduction.html) | — | API key required; public inboxes are publicly viewable. Private addresses and retention depend on the plan; no real registration secrets should be placed in a public inbox. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://docs.mailsac.com/en/latest/about/introduction.html) — checked 2026-09-09

<a id="mailsink"></a>

## MailSink

Temporary inbox API and MCP with message, verification-code and verification-link retrieval.

**Classification:** Communication / Mailboxes

[Website](https://mailsink.dev/) · [Source record](../data/candidates/mailsink.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="mailsink-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [mail-api (API)](https://mailsink.dev/docs/) | [Docs](https://mailsink.dev/docs/) | — | Homepage advertises anonymous mode, but current quickstart says GitHub login and Bearer token are required for all API requests. Preserve this conflict until observed; do not assume anonymous access. |
| [mail-mcp (MCP)](https://mailsink.dev/docs/) | [Docs](https://mailsink.dev/docs/) | — | Official @mailsink/mcp setup requires MAILSINK_API_KEY. Anonymous-mode conflict remains unresolved. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://mailsink.dev/docs/) — checked 2026-09-09
- [official_docs](https://mailsink.dev/) — checked 2026-09-09

<a id="mailslurp"></a>

## MailSlurp

Programmable mailboxes for email automation and testing, including message waiting and agent integrations.

**Classification:** Communication / Mailboxes

[Website](https://www.mailslurp.com/) · [Source record](../data/candidates/mailslurp.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="mailslurp-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [mail-api (API)](https://www.mailslurp.com/guides/getting-started/) | [Docs](https://www.mailslurp.com/guides/getting-started/) | — | A service account and API key are required. Free plan has caps and sandbox-only sending; receiving real email and sending externally have different entitlements. |
| [mail-mcp (MCP)](https://www.mailslurp.com/docs/agents/) | [Docs](https://www.mailslurp.com/docs/agents/) | — | Agent-scoped access requires account setup; task usage has not been measured. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://www.mailslurp.com/guides/getting-started/) — checked 2026-09-09
- [official_docs](https://app.mailslurp.com/pricing/) — checked 2026-09-09
- [official_docs](https://www.mailslurp.com/docs/agents/) — checked 2026-09-09

<a id="massive"></a>

## Massive (formerly Polygon.io)

Market-data APIs with stock history and separate data products. Stocks Basic is listed at USD 0/month.

**Classification:** Search & Data Access / Financial Data / Asset Prices

[Website](https://massive.com/) · [Source record](../data/candidates/massive.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="massive-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://massive.com/docs/rest/quickstart) | [Docs](https://massive.com/docs/rest/quickstart) | self serve / documented | Stocks Basic: USD 0/month for individual use, 5 calls/minute, two years of historical end-of-day data. A free stock plan does not establish free fundamentals or permission to redistribute data. Confirm unadjusted daily aggregate settings and actual access in the trial. |

### Service pricing

- data-api: 0 USD / month on Stocks Basic (usage; Individual Stocks Basic plan only; no other datasets, subscriptions or paid entitlements inferred.)

### Task results

—

### Sources

- [official_docs](https://massive.com/docs/rest/quickstart) — checked 2026-09-09
- [official_site](https://massive.com/pricing) — checked 2026-09-15

<a id="mem0"></a>

## Mem0

Memory layer for AI agents (hosted platform + open-source), with REST API, llms.txt, and the official OpenMemory MCP server.

**Classification:** Agent Infrastructure & Automation / Agent Memory

[Website](https://mem0.ai) · [Source record](../data/providers/mem0.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="mem0-access"></a>

[Docs](https://docs.mem0.ai) · [API reference](https://docs.mem0.ai/api-reference) · [MCP entry](https://docs.mem0.ai/openmemory/overview)

—

### Service pricing

[Official pricing](https://mem0.ai/pricing)

### Task results

—

### Notes

- Persistent memory across sessions, with save/search operations. Hosted platform and self-hosted library are separate access scopes.

### Sources

- [official_docs](https://docs.mem0.ai/introduction) — checked 2026-09-15

<a id="minimax"></a>

## MiniMax

MiniMax text, speech, video and music models via the international platform API, with an official MCP server.

**Classification:** AI Services / Model Access

[Website](https://platform.minimax.io) · [Source record](../data/providers/minimax.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="minimax-access"></a>

[Docs](https://platform.minimax.io/docs) · [API reference](https://platform.minimax.io/docs/api-reference) · [MCP entry](https://github.com/MiniMax-AI/MiniMax-MCP)

—

### Service pricing

—

### Task results

—

### Sources

- [official_site](https://platform.minimax.io/user-center/basic-information/interface-key) — checked 2026-07-08

<a id="mistral"></a>

## Mistral AI

European LLM provider (La Plateforme) with llms.txt, an open OpenAPI-based docs repo, a free experiment tier, and self-serve keys.

**Classification:** AI Services / Model Access

[Website](https://mistral.ai) · [Source record](../data/providers/mistral.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="mistral-access"></a>

[Docs](https://docs.mistral.ai) · [API reference](https://docs.mistral.ai/api) · [SDK](https://docs.mistral.ai/getting-started/clients)

—

### Service pricing

[Official pricing](https://mistral.ai/pricing)

### Task results

—

### Sources

- [official_docs](https://docs.mistral.ai/getting-started/quickstart) — checked 2026-07-07

<a id="modal"></a>

## Modal

Serverless compute for Python with first-class Sandboxes for agent code execution, llms.txt, and an official CLI.

**Classification:** Cloud Computing & Hosting / Code Sandboxes

[Website](https://modal.com) · [Source record](../data/providers/modal.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="modal-access"></a>

[Docs](https://modal.com/docs) · [API reference](https://modal.com/docs/reference) · [CLI](https://modal.com/docs/reference/cli)

—

### Service pricing

[Official pricing](https://modal.com/pricing)

### Task results

—

### Sources

- [official_docs](https://modal.com/docs/reference/cli) — checked 2026-07-07

<a id="mollie"></a>

## Mollie

Payment links and payment APIs with isolated test mode and a simulated checkout screen.

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Databases / Document Databases

[Website](https://www.mongodb.com/products/platform/atlas-database) · [Source record](../data/providers/mongodb-atlas.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="mongodb-atlas-access"></a>

[Docs](https://www.mongodb.com/docs/atlas/) · [API reference](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/) · [CLI](https://www.mongodb.com/docs/atlas/cli/) · [SDK](https://www.mongodb.com/docs/drivers/) · [MCP entry](https://github.com/mongodb-js/mongodb-mcp-server)

—

### Service pricing

[Official pricing](https://www.mongodb.com/pricing)

### Task results

—

### Notes

- Managed document collections and queries. Atlas administration API is not automatically a document data-access route; vector-search coverage is not asserted here.

### Sources

- [official_docs](https://www.mongodb.com/docs/atlas/) — checked 2026-09-15

<a id="moonshot"></a>

## Moonshot AI (Kimi)

Kimi models (K2 line) via an OpenAI-compatible API on the international Kimi platform, with an official terminal CLI agent (kimi-cli).

**Classification:** AI Services / Model Access

[Website](https://platform.kimi.ai) · [Source record](../data/providers/moonshot.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="moonshot-access"></a>

[Docs](https://platform.kimi.ai/docs) · [API reference](https://platform.kimi.ai/docs/api/chat) · [CLI](https://github.com/MoonshotAI/kimi-cli)

—

### Service pricing

—

### Task results

—

### Sources

- [official_site](https://platform.kimi.ai/console/api-keys) — checked 2026-07-08

<a id="n8n"></a>

## n8n

Workflow automation platform with native AI/agent nodes, a public REST API, official hosted MCP server, CLI, and llms.txt; fair-code and self-hostable.

**Classification:** Agent Infrastructure & Automation / Workflow Automation

[Website](https://n8n.io) · [Source record](../data/providers/n8n.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="n8n-access"></a>

[Docs](https://docs.n8n.io) · [API reference](https://docs.n8n.io/api/) · [CLI](https://docs.n8n.io/hosting/cli-commands/) · [MCP entry](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)

—

### Service pricing

[Official pricing](https://n8n.io/pricing)

### Task results

—

### Notes

- Executes workflows with cloud and self-hosted options. Workflow templates alone do not establish any downstream business capability.

### Sources

- [official_docs](https://docs.n8n.io/) — checked 2026-09-15

<a id="nasdaq-data-link"></a>

## Nasdaq Data Link

Marketplace for financial and economic datasets with free and separately subscribed products.

**Classification:** Search & Data Access / Financial Data

[Website](https://data.nasdaq.com/) · [Source record](../data/candidates/nasdaq-data-link.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="nasdaq-data-link-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://docs.data.nasdaq.com/docs/getting-started) | [Docs](https://docs.data.nasdaq.com/docs/getting-started) | documented | Choose a specific dataset before comparison. Most datasets are premium. The legacy documentation announces retirement on 2026-08-31; its replacement link was not readable in this research pass. |

### Service pricing

—

### Task results

—

### Notes

- Dataset marketplace retained at the parent. Select a concrete dataset and verify its current documentation and availability before assigning child categories.

### Sources

- [official_docs](https://docs.data.nasdaq.com/docs/getting-started) — checked 2026-09-09

<a id="neon"></a>

## Neon

Serverless Postgres with instant branching, a full management API, official MCP server, and agent-oriented docs.

**Classification:** Databases / Hosted Relational Databases

[Website](https://neon.com) · [Source record](../data/providers/neon.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="neon-access"></a>

[Docs](https://neon.com/docs) · [API reference](https://api-docs.neon.tech) · [CLI](https://neon.com/docs/reference/neon-cli) · [MCP entry](https://github.com/neondatabase/mcp-server-neon)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [ephemeral-api (API)](https://neon.new/) | — | documented | No-account, 72-hour ephemeral hosted Postgres. Tests can establish short-term persistence only; this is not a permanent free production database. Connection strings and claim URLs are private credentials. |

### Service pricing

[Official pricing](https://neon.com/pricing)

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
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

**Classification:** Cloud Computing & Hosting / Application Hosting

[Website](https://www.netlify.com) · [Source record](../data/providers/netlify.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="netlify-access"></a>

[Docs](https://docs.netlify.com) · [API reference](https://open-api.netlify.com) · [CLI](https://docs.netlify.com/cli/get-started/) · [MCP entry](https://docs.netlify.com/welcome/build-with-ai/netlify-mcp-server/)

—

### Service pricing

[Official pricing](https://www.netlify.com/pricing/)

### Task results

—

### Sources

- [official_docs](https://docs.netlify.com/api/get-started/) — checked 2026-07-07

<a id="notion"></a>

## Notion

Connected workspace with a versioned REST API, capability-scoped integrations, llms.txt, and an official MCP server.

**Classification:** Workplace Collaboration / Collaborative Tables; Workplace Collaboration / Document Collaboration

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

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
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

### Notes

- Document and messaging membership does not transfer collaborative-table trial results to those tasks.

### Sources

- [official_docs](https://developers.notion.com/reference/intro) — checked 2026-09-08
- [official_docs](https://developers.notion.com/guides/get-started/authorization) — checked 2026-09-08
- [official_docs](https://developers.notion.com/guides/get-started/personal-access-tokens) — checked 2026-09-08
- [official_site](https://www.notion.com/pricing) — checked 2026-09-08
- [official_repo](https://github.com/makenotion/notion-sdk-js) — checked 2026-09-08
- [official_docs](https://developers.notion.com/cli/get-started/overview) — checked 2026-09-08
- [official_docs](https://developers.notion.com/guides/mcp/get-started-with-mcp) — checked 2026-09-08
- [official_docs](https://developers.notion.com/guides/data-apis/working-with-page-content) — checked 2026-09-15

<a id="open-exchange-rates"></a>

## Open Exchange Rates

Currency reference rates via a keyed API with a free signup plan; base-currency and historical access depend on the plan.

**Classification:** Search & Data Access / Financial Data / Exchange Rates

[Website](https://openexchangerates.org/) · [Source record](../data/candidates/open-exchange-rates.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="open-exchange-rates-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://docs.openexchangerates.org/reference/api-introduction) | [Docs](https://docs.openexchangerates.org/reference/api-introduction) | self serve / documented | A free signup route is published. Confirm whether the chosen historical date and currency base are included; rates are indicative rather than executable bank/card quotes. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://docs.openexchangerates.org/reference/api-introduction) — checked 2026-09-09
- [official_site](https://openexchangerates.org/signup/free) — checked 2026-09-09

<a id="openai"></a>

## OpenAI

GPT model APIs with an official OpenAPI spec, agents guides, and a large SDK ecosystem.

**Classification:** AI Services / Model Access

[Website](https://openai.com) · [Source record](../data/providers/openai.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="openai-access"></a>

[Docs](https://developers.openai.com/api/docs) · [API reference](https://platform.openai.com/docs/api-reference) · [SDK](https://platform.openai.com/docs/libraries)

—

### Service pricing

[Official pricing](https://platform.openai.com/docs/pricing)

### Task results

—

### Sources

- [official_docs](https://platform.openai.com/docs/quickstart) — checked 2026-07-07

<a id="openrouter"></a>

## OpenRouter

Unified OpenAI-compatible API over hundreds of models from many labs, with one key, per-model pricing, automatic fallbacks, and an llms.txt.

**Classification:** AI Services / Model Access

[Website](https://openrouter.ai) · [Source record](../data/providers/openrouter.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="openrouter-access"></a>

[Docs](https://openrouter.ai/docs) · [API reference](https://openrouter.ai/docs/api-reference/overview)

—

### Service pricing

[Official pricing](https://openrouter.ai/models)

### Task results

—

### Sources

- [official_docs](https://openrouter.ai/docs/quickstart) — checked 2026-07-08

<a id="outlook-mail"></a>

## Outlook Mail

Persistent Microsoft mailboxes with mail retrieval and management through Microsoft Graph.

**Classification:** Communication / Mailboxes

[Website](https://outlook.live.com/) · [Source record](../data/candidates/outlook-mail.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="outlook-mail-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [mail-api (API)](https://learn.microsoft.com/en-us/graph/outlook-mail-concept-overview) | [Docs](https://learn.microsoft.com/en-us/graph/outlook-mail-concept-overview) | — | Personal versus organizational accounts and delegated permissions differ. Requires mailbox ownership and app authorization; Graph mail access does not create consumer Microsoft accounts. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://learn.microsoft.com/en-us/graph/outlook-mail-concept-overview) — checked 2026-09-09

<a id="paas-build"></a>

## paas.build

Agent-native payment facilitator (the AI-builder product of UniPaaS, FCA-authorised No. 929994) — opens a real merchant account via progressive KYB and creates checkouts through MCP or REST.

**Classification:** Payments / Billing / Payment Acceptance

[Website](https://paas.build) · [Source record](../data/candidates/paas-build.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="paas-build-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [rest-api (API)](https://paas.build/openapi.json) | [Docs](https://paas.build/SKILL.md) | restricted | PayFac powered by UniPaaS; merchant retains tax responsibilities. Official materials limit onboarding to UK/EU/US merchants. Sandbox and production tokens differ. A 2026-09-08 sandbox-only account and token were prepared successfully. A fresh Codex trial created a remote checkout but hit a browser launch permission failure, so it is invalid for completion-rate comparison. Independent browser review showed only the checkout shell; customer usability remains unverified. |
| [official-mcp (MCP)](https://paas.build/mcp) | [Docs](https://paas.build/agents) | — | Discovery verified four tools on 2026-09-08. Default onboarding can provision both environments and send notifications; explicitly prepare sandbox-only access. Protocol discovery is not task completion. |

### Service pricing

[Official pricing](https://paas.build/pricing)

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
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

**Classification:** Payments / Billing / Payment Acceptance

[Website](https://www.paddle.com) · [Source record](../data/providers/paddle.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="paddle-access"></a>

[Docs](https://developer.paddle.com) · [API reference](https://developer.paddle.com/api-reference/overview) · [MCP entry](https://github.com/PaddleHQ/paddle-mcp-server)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [sandbox-api (API)](https://developer.paddle.com/sdks/sandbox/) | [Docs](https://developer.paddle.com/sdks/sandbox/) | self serve | Requires: platform_account; Register the separate sandbox account and obtain its API key.; Create a separate sandbox account with sandbox credentials. Sandbox does not require the domain and checkout approvals needed for live sales. Merchant-of-record responsibilities and live account review differ from payment processing alone. On 2026-09-09, sandbox email verification completed and a seven-day API key was created with scoped permissions. An authenticated sandbox products read returned HTTP 200 with an empty catalog. No KYC, production activation or payment was performed. Account setup alone is not a completed checkout task. The first ebook checkout task was not completed: POST /products rejected ebooks with product_tax_category_not_approved. The authenticated sandbox dashboard showed eBook Not Requested and SaaS Approved, with a notice that category approval must be requested in a live account. No live application was made. This result concerns the default account and ebook scenario, not approved categories or all Paddle checkouts. |

### Service pricing

[Official pricing](https://www.paddle.com/pricing)

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
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

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Search & Data Access / Web Search

[Website](https://www.perplexity.ai) · [Source record](../data/providers/perplexity.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="perplexity-access"></a>

[Docs](https://docs.perplexity.ai) · [MCP entry](https://github.com/ppl-ai/modelcontextprotocol)

—

### Service pricing

[Official pricing](https://docs.perplexity.ai/getting-started/pricing)

### Task results

—

### Notes

- Search API and source-grounded answers support web discovery. General URL extraction is not inferred from citations or snippets; newer model-router products require separate route review.

### Sources

- [official_docs](https://docs.perplexity.ai/docs/getting-started/overview) — checked 2026-09-15

<a id="pinecone"></a>

## Pinecone

Managed vector database for search and RAG, with llms.txt, an official MCP server, and self-serve keys.

**Classification:** Databases / Vector Databases

[Website](https://www.pinecone.io) · [Source record](../data/providers/pinecone.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="pinecone-access"></a>

[Docs](https://docs.pinecone.io) · [API reference](https://docs.pinecone.io/reference/api/introduction) · [CLI](https://github.com/pinecone-io/cli) · [MCP entry](https://docs.pinecone.io/guides/operations/mcp-server)

—

### Service pricing

[Official pricing](https://www.pinecone.io/pricing/)

### Task results

—

### Notes

- Persistent vector indexes and semantic retrieval; a separate managed memory product is not inferred from an example memory use case.

### Sources

- [official_docs](https://docs.pinecone.io/guides/get-started/overview) — checked 2026-09-15

<a id="pingxx"></a>

## Ping++

Unified payment integration across payment channels, with API keys, a web SDK and simulated test transactions.

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Databases / Hosted Relational Databases

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

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Developer Tools / API Development & Testing

[Website](https://www.postman.com) · [Source record](../data/providers/postman.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="postman-access"></a>

[Docs](https://learning.postman.com) · [API reference](https://learning.postman.com/docs/developer/postman-api/intro-api/) · [CLI](https://learning.postman.com/docs/postman-cli/postman-cli-overview/) · [MCP entry](https://github.com/postmanlabs/postman-mcp-server)

—

### Service pricing

[Official pricing](https://www.postman.com/pricing/)

### Task results

—

### Notes

- Reusable request collections and API testing. Having an API does not classify an arbitrary service as API development.

### Sources

- [official_docs](https://learning.postman.com/docs/getting-started/overview/) — checked 2026-09-15

<a id="qdrant"></a>

## Qdrant

Open-source vector database with a managed cloud, llms.txt, an official MCP server, and a free cluster tier.

**Classification:** Databases / Vector Databases

[Website](https://qdrant.tech) · [Source record](../data/providers/qdrant.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="qdrant-access"></a>

[Docs](https://qdrant.tech/documentation) · [API reference](https://api.qdrant.tech) · [SDK](https://qdrant.tech/documentation/interfaces) · [MCP entry](https://github.com/qdrant/mcp-server-qdrant)

—

### Service pricing

[Official pricing](https://qdrant.tech/pricing)

### Task results

—

### Notes

- Vector collections and similarity retrieval, with managed and self-hosted deployments distinguished at access time.

### Sources

- [official_docs](https://qdrant.tech/documentation/overview/) — checked 2026-09-15

<a id="quiver-quantitative"></a>

## Quiver Quantitative

Congressional and insider transactions, institutional activity and other alternative financial datasets.

**Classification:** Search & Data Access / Financial Data / Transaction Disclosures

[Website](https://www.quiverquant.com/) · [Source record](../data/candidates/quiver-quantitative.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="quiver-quantitative-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://www.quiverquant.com/api-setup/) | [Docs](https://www.quiverquant.com/api-setup/) | self serve / documented | API access is advertised from USD 30/month. Free website signup does not establish free API access; no free execution allowance confirmed. |
| [data-mcp (MCP)](https://mcp.quiverquant.com/) | [Docs](https://api.quiverquant.com/mcp-server/) | self serve / documented | Uses a Quiver API key and plan entitlement; MCP is not an additional free allowance. Required dataset tier must be checked. |

### Service pricing

- data-api: 30 USD / month (minimum_spend; Advertised API starting price; exact dataset entitlement not established.)

### Task results

—

### Sources

- [official_docs](https://www.quiverquant.com/api-setup/) — checked 2026-09-15
- [official_site](https://api.quiverquant.com/) — checked 2026-09-15
- [official_docs](https://api.quiverquant.com/mcp-server/) — checked 2026-09-15

<a id="railway"></a>

## Railway

App/database hosting with a public GraphQL API, official CLI, llms.txt, and usage-based pricing.

**Classification:** Cloud Computing & Hosting / Application Hosting

[Website](https://railway.com) · [Source record](../data/providers/railway.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="railway-access"></a>

[Docs](https://docs.railway.com) · [API reference](https://docs.railway.com/reference/public-api) · [CLI](https://github.com/railwayapp/cli)

—

### Service pricing

[Official pricing](https://railway.com/pricing)

### Task results

—

### Sources

- [official_docs](https://docs.railway.com/reference/public-api) — checked 2026-07-08

<a id="razorpay"></a>

## Razorpay

Payment Links API for collecting specified amounts through hosted checkout, including a documented test mode.

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Databases / Key-value Databases; Databases / Vector Databases; Databases / Document Databases

[Website](https://redis.io) · [Source record](../data/providers/redis.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="redis-access"></a>

[Docs](https://redis.io/docs/latest) · [API reference](https://redis.io/docs/latest/operate/rc/api/) · [CLI](https://redis.io/docs/latest/develop/tools/cli/) · [MCP entry](https://github.com/redis/mcp-redis)

—

### Service pricing

[Official pricing](https://redis.io/pricing)

### Task results

—

### Notes

- Redis key/value operations, vector search and queryable JSON are documented features. Cloud and open-source versions/entitlements are not interchangeable.

### Sources

- [official_docs](https://redis.io/docs/latest/) — checked 2026-09-15

<a id="render"></a>

## Render

Cloud hosting for web services, static sites and databases with a REST API, official CLI, official MCP server, and llms.txt.

**Classification:** Cloud Computing & Hosting / Application Hosting

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

- [official_docs](https://render.com/docs/api) — checked 2026-07-08

<a id="replicate"></a>

## Replicate

Run and fine-tune open-source models via a simple predictions API, with llms.txt, webhooks, and an official CLI.

**Classification:** AI Services / Model Access

[Website](https://replicate.com) · [Source record](../data/providers/replicate.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="replicate-access"></a>

[Docs](https://replicate.com/docs) · [API reference](https://replicate.com/docs/reference/http) · [CLI](https://github.com/replicate/cli) · [SDK](https://replicate.com/docs/reference/client-libraries)

—

### Service pricing

[Official pricing](https://replicate.com/pricing)

### Task results

—

### Sources

- [official_docs](https://replicate.com/docs/reference/http) — checked 2026-07-07

<a id="resend"></a>

## Resend

Email API for developers with test mode, scoped API keys, idempotency support, and an official MCP server.

**Classification:** Communication / Email Delivery

[Website](https://resend.com) · [Source record](../data/providers/resend.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="resend-access"></a>

[Docs](https://resend.com/docs) · [API reference](https://resend.com/docs/api-reference/introduction) · [SDK](https://resend.com/docs/sdks) · [MCP entry](https://github.com/resend/mcp-send-email)

—

### Service pricing

[Official pricing](https://resend.com/pricing)

### Task results

—

### Notes

- Application email delivery. A persistent user mailbox is not inferred from receiving webhooks.

### Sources

- [official_docs](https://resend.com/docs/introduction) — checked 2026-09-15

<a id="sabre-air"></a>

## Sabre Air APIs

Air API workflows with assigned credentials, plus a separately researched Agentic API/MCP lead.

**Classification:** Travel / Flights

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

**Classification:** Travel / Flights

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

**Classification:** Travel / Flights

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

<a id="sec-edgar"></a>

## SEC EDGAR Data APIs

Official public company filings and XBRL financial facts; data.sec.gov reading APIs require no account or key.

**Classification:** Search & Data Access / Financial Data / Company Financials

[Website](https://www.sec.gov/) · [Source record](../data/candidates/sec-edgar.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="sec-edgar-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | [Docs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | self serve / documented | Reading APIs are separate from filer submission APIs. Automated-access policy applies. Facts need fiscal-period, unit and amendment interpretation; CORS is not supported. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) — checked 2026-09-15

<a id="sentry"></a>

## Sentry

Error monitoring and performance tracing with llms.txt, an official MCP server, scoped auth tokens, and a full API.

**Classification:** Developer Tools / Monitoring & Troubleshooting

[Website](https://sentry.io) · [Source record](../data/providers/sentry.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="sentry-access"></a>

[Docs](https://docs.sentry.io) · [API reference](https://docs.sentry.io/api/) · [CLI](https://docs.sentry.io/cli/) · [SDK](https://docs.sentry.io/platforms/) · [MCP entry](https://docs.sentry.io/product/sentry-mcp/)

—

### Service pricing

[Official pricing](https://sentry.io/pricing/)

### Task results

—

### Sources

- [official_docs](https://docs.sentry.io/api/auth/) — checked 2026-07-07

<a id="serpapi"></a>

## SerpApi

Real-time JSON API for Google and other search engines' results, with an official MCP server, llms.txt, and a free monthly quota.

**Classification:** Travel / Flights; Search & Data Access / Web Search

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

**Classification:** Search & Data Access / Web Search

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

**Classification:** E-commerce

[Website](https://www.shopify.com) · [Source record](../data/providers/shopify.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="shopify-access"></a>

[Docs](https://shopify.dev/docs) · [API reference](https://shopify.dev/docs/api) · [CLI](https://shopify.dev/docs/api/shopify-cli) · [MCP entry](https://shopify.dev/docs/apps/build/storefront-mcp)

—

### Service pricing

[Official pricing](https://www.shopify.com/pricing)

### Task results

—

### Notes

- Admin and Storefront surfaces support store products, inventory, carts and orders. This broad category already describes the product; finer commerce branches await wider candidate research.

### Sources

- [official_docs](https://shopify.dev/docs/api) — checked 2026-09-15

<a id="simfin"></a>

## SimFin

Company fundamentals and price data with API and CSV access advertised across free and paid plans.

**Classification:** Search & Data Access / Financial Data / Asset Prices; Search & Data Access / Financial Data / Company Financials

[Website](https://www.simfin.com/) · [Source record](../data/candidates/simfin.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="simfin-access"></a>

—

### Service pricing

—

### Task results

—

### Notes

- Free account exists, but API versus bulk-CSV permissions and history differ. Exact API setup documentation and execution allowance still need verification.

### Sources

- [official_site](https://www.simfin.com/en/prices/) — checked 2026-09-09

<a id="skootle-google-flights"></a>

## Skootle Google Flights Scraper

A Skootle-published flight-scraping Actor hosted on Apify, billed by startup and output records.

**Classification:** Travel / Flights

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

**Classification:** Travel / Flights

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

**Classification:** Communication / Messaging

[Website](https://slack.com) · [Source record](../data/providers/slack.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="slack-access"></a>

[Docs](https://api.slack.com) · [API reference](https://api.slack.com/methods) · [CLI](https://docs.slack.dev/tools/slack-cli) · [SDK](https://tools.slack.dev)

—

### Service pricing

[Official pricing](https://slack.com/pricing)

### Task results

—

### Notes

- Conversation/channel messaging through authorized Slack apps; permissions determine accessible conversations.

### Sources

- [official_docs](https://docs.slack.dev/) — checked 2026-09-15

<a id="square"></a>

## Square

Hosted payment links and payment APIs with a free developer sandbox; merchant availability depends on country.

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Cloud Computing & Hosting / Browser Environments

[Website](https://steel.dev) · [Source record](../data/providers/steel.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="steel-access"></a>

[Docs](https://docs.steel.dev) · [API reference](https://docs.steel.dev/api-reference)

—

### Service pricing

[Official pricing](https://steel.dev/pricing)

### Task results

—

### Sources

- [official_docs](https://docs.steel.dev/overview/intro-to-steel) — checked 2026-07-08

<a id="stripe"></a>

## Stripe

Payments, billing, subscriptions, and financial infrastructure with a famously complete API surface.

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Databases / Hosted Relational Databases

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

**Classification:** Search & Data Access / Web Content Extraction; Search & Data Access / Web Search

[Website](https://www.tavily.com) · [Source record](../data/providers/tavily.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="tavily-access"></a>

[Docs](https://docs.tavily.com) · [API reference](https://docs.tavily.com/documentation/api-reference/introduction) · [SDK](https://docs.tavily.com/sdk) · [MCP entry](https://docs.tavily.com/documentation/mcp)

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [search-api (API)](https://docs.tavily.com/documentation/quickstart) | [Docs](https://docs.tavily.com/documentation/quickstart) | self serve / documented | Basic search costs 1 credit; advanced search 2. Paid overage setting is separate. |
| [extract-api (API)](https://api.tavily.com/extract) | [Docs](https://docs.tavily.com/documentation/api-reference/endpoint/extract) | — | Extract accepts one or more URLs. Search pricing and search trials do not establish extraction cost or success. |

### Service pricing

[Official pricing](https://www.tavily.com/pricing)

- search-api: 1000 credits / month (free_allowance; Free account allowance, not requests.)

### Task results

—

### Sources

- [official_docs](https://docs.tavily.com/documentation/quickstart) — checked 2026-09-07
- [official_docs](https://docs.tavily.com/documentation/api-credits) — checked 2026-09-07
- [official_docs](https://docs.tavily.com/documentation/api-reference/endpoint/extract) — checked 2026-09-15

<a id="telegram"></a>

## Telegram Bot API

Free bot platform with instant token issuance via BotFather, webhooks, a documented test environment, and a detailed changelog.

**Classification:** Communication / Messaging

[Website](https://telegram.org) · [Source record](../data/providers/telegram.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="telegram-access"></a>

[Docs](https://core.telegram.org/bots) · [API reference](https://core.telegram.org/bots/api)

—

### Service pricing

—

### Task results

—

### Notes

- Scope is Telegram Bot API messaging, not user-account automation or arbitrary private-chat access.

### Sources

- [official_docs](https://core.telegram.org/bots/api) — checked 2026-09-15

<a id="temp-mail"></a>

## Temp Mail

Disposable email receiving service with a developer API for automated email workflows.

**Classification:** Communication / Mailboxes

[Website](https://temp-mail.org/) · [Source record](../data/candidates/temp-mail.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="temp-mail-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [mail-api (API)](https://temp-mail.org/en/api/) | [Docs](https://temp-mail.org/en/api/) | — | Free web inboxes do not establish free developer API access. API credentials, pricing and retention require preparation checks. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://temp-mail.org/en/api/) — checked 2026-09-09

<a id="tiingo"></a>

## Tiingo

Market data covering end-of-day prices and other feeds, with an account-issued authentication token.

**Classification:** Search & Data Access / Financial Data / Asset Prices; Search & Data Access / Financial Data / Exchange Rates

[Website](https://www.tiingo.com/) · [Source record](../data/candidates/tiingo.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="tiingo-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://www.tiingo.com/documentation/general/overview) | [Docs](https://www.tiingo.com/documentation/general/overview) | self serve | Token is assigned after account creation. Request and bandwidth limits apply; current free allowance and target-feed entitlement are not yet established. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://www.tiingo.com/documentation/general/overview) — checked 2026-09-09
- [official_docs](https://www.tiingo.com/documentation/forex) — checked 2026-09-15

<a id="together-ai"></a>

## Together AI

Inference and fine-tuning platform for open-source models with an OpenAI-compatible API and llms.txt.

**Classification:** AI Services / Model Access

[Website](https://www.together.ai) · [Source record](../data/providers/together-ai.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="together-ai-access"></a>

[Docs](https://docs.together.ai) · [API reference](https://docs.together.ai/reference/chat-completions)

—

### Service pricing

[Official pricing](https://www.together.ai/pricing)

### Task results

—

### Sources

- [official_docs](https://docs.together.ai/docs/quickstart) — checked 2026-07-07

<a id="tracefour"></a>

## Tracefour

Public trading disclosures through keyless REST and MCP, with attribution and original-filing links.

**Classification:** Search & Data Access / Financial Data / Transaction Disclosures

[Website](https://tracefour.com/) · [Source record](../data/candidates/tracefour.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="tracefour-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api-keyless (API)](https://tracefour.com/v1) | [Docs](https://tracefour.com/api-docs) | self serve / documented | CC BY 4.0 compilation; link to the attribution page supplied with each response. Congress coverage is not established as complete for both chambers. |
| [data-mcp (MCP)](https://tracefour.com/v1/mcp) | [Docs](https://tracefour.com/api-docs/mcp) | self serve / documented | Streamable HTTP; anonymous calls share the documented per-IP allowance. Optional free key increases the allowance to 600/hour; key acquisition not tested. |

### Service pricing

- data-api-keyless: 60 requests / hour (free_allowance; Anonymous read allowance per IP.)

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
| --- | --- | --- | --- | --- |
| API | [No account or key supplied](../data/experiments/evaluations/tracefour-access.json) | [107.3k](../data/experiments/evaluations/tracefour-access.json) | 153.41522s | 0 |
| MCP | — | — | — | — |

#### Set up this financial-data service, confirm that it can query data through the specified interface, and save the configuration needed for later use. If access is blocked, explain where.

| Route | Trials | Resolution rate | Tokens | Model cost | Service cost |
| --- | --- | --- | --- | --- | --- |
| API | [1](./evaluations.md#comparison-bd611da6270b) | [0%](./evaluations.md#comparison-bd611da6270b) | 107.3k | $0.0071 | $0 |
| MCP | — | — | — | — | — |

<details>
<summary>Task, conditions and evidence</summary>

The service, required interface, and any supplied account or signup information are specified in the environment. Use account-free access directly when available. For signup, use only the identity information supplied for this trial. Retain the necessary connection configuration for later tasks.

**Completion:** Complete the required signup, authentication and configuration for the specified interface, and query real financial data. Necessary configuration works in a fresh session. Do not force registration for account-free routes. Documentation, a health check or a configuration file alone does not establish data access.

1.18.29 · glm-5.3-flash / high · 600s · 2026-09-15 (UTC)

No account or key supplied · [Full configuration and evidence](./evaluations.md#comparison-bd611da6270b)

[Task definition](./tasks.en.md#financial-access-001-v1)

- API: [Not completed](../data/experiments/evaluations/tracefour-access.json) — 本轮通过指定 REST 方式接入 Tracefour 未完成：文档页和实际尝试的 URL 从本轮云端环境返回 Cloudflare 403 challenge，没有取得真实金融数据；已保存含阻碍说明的配置，无人工介入。独立验收复现了 /v1 和 /api-docs 的 403。执行者未成功读取文档，也未调用后来研究确认的 /v1/congress 等数据路由，因此这些观察不能证明全部数据端点、MCP 或其他网络环境都不可用；本轮没有执行交易披露业务题。

</details>

<details>
<summary>Run history (1)</summary>

| Task | Route | Result | Date (UTC) |
| --- | --- | --- | --- |
| financial-access-001 v1 | API | [not_completed](../data/experiments/evaluations/tracefour-access.json) | 2026-09-15 |

</details>

### Task results

—

### Sources

- [official_docs](https://tracefour.com/api-docs) — checked 2026-09-15
- [official_docs](https://tracefour.com/api-docs/congress-trading-api) — checked 2026-09-15
- [official_docs](https://tracefour.com/api-docs/mcp) — checked 2026-09-15

<a id="travelport-tripservices"></a>

## Travelport TripServices

Travel distribution API requiring trial requests and provider-provisioned production credentials.

**Classification:** Travel / Flights

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

**Classification:** Travel / Flights

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

**Classification:** Databases / Hosted Relational Databases

[Website](https://turso.tech/) · [Source record](../data/candidates/turso.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="turso-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [cloud-cli (CLI)](https://docs.turso.tech/cli/introduction) | [Docs](https://docs.turso.tech/cli/introduction) | self serve / documented | Free cloud account: 100 databases, 5 GB, 500 million reads/month and 10 million writes/month. Signup/login required; local engine alone does not satisfy remote storage. |
| [platform-api (API)](https://docs.turso.tech/api-reference/introduction) | [Docs](https://docs.turso.tech/api-reference/introduction) | self serve | Management API; SQL connectivity uses separate database credentials created during execution. Provision only within a dedicated free test organization; no precreated database. |

### Service pricing

- cloud-cli: 5 GB / account (free_allowance; Free cloud storage; account quota also limits reads, writes and number of databases.)

### Setup observations

| Route | Starting resources | Latest setup tokens | Latest setup time | Latest setup human involvement |
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

<a id="tushare"></a>

## Tushare Pro

Chinese-market prices and financial statements through a token-based HTTP API and Python SDK.

**Classification:** Search & Data Access / Financial Data / Asset Prices; Search & Data Access / Financial Data / Company Financials

[Website](https://tushare.pro/) · [Source record](../data/candidates/tushare.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="tushare-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://tushare.pro/document/1?doc_id=40) | [Docs](https://tushare.pro/document/1?doc_id=40) | self serve / documented | Daily unadjusted prices start at 120 points; financial statements start at 2,000. Points are an access threshold, not per-call spending. Some datasets need separate permissions. The HTTP example uses an unencrypted endpoint; verify a secure credential path before testing. |
| [python-sdk (SDK)](https://tushare.pro/document/1?doc_id=40) | [Docs](https://tushare.pro/document/1?doc_id=40) | self serve / documented | Python SDK shares token and point thresholds with HTTP access; verify transport security before supplying credentials. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://tushare.pro/document/1?doc_id=40) — checked 2026-09-09
- [official_docs](https://tushare.pro/document/1?doc_id=290) — checked 2026-09-09
- [official_docs](https://tushare.pro/document/1?doc_id=108) — checked 2026-09-09

<a id="twelve-data"></a>

## Twelve Data

Global stock, FX and crypto time series with API, Python SDK and CLI access.

**Classification:** Search & Data Access / Financial Data / Asset Prices; Search & Data Access / Financial Data / Exchange Rates

[Website](https://twelvedata.com/) · [Source record](../data/candidates/twelve-data.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="twelve-data-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://twelvedata.com/docs/introduction/quickstart) | [Docs](https://twelvedata.com/docs/introduction/quickstart) | self serve / documented | Basic advertises 800 API credits/day. Credits are not necessarily requests. Market coverage, fundamentals and display rights depend on plan. |
| [python-sdk (SDK)](https://twelvedata.com/docs/introduction/quickstart) | [Docs](https://twelvedata.com/docs/introduction/quickstart) | self serve / documented | Official Python TDClient example; same account entitlement as REST. |
| [data-cli (CLI)](https://github.com/twelvedata/twelvedata-cli) | [Docs](https://github.com/twelvedata/twelvedata-cli) | self serve / documented | Official CLI repository; installation and command coverage not yet tested. |

### Service pricing

- data-api: 800 credits / day (free_allowance; Basic plan; endpoint credit weights and market entitlements vary.)

- python-sdk: 800 credits / day (free_allowance; Basic plan; endpoint credit weights and market entitlements vary.)

- data-cli: 800 credits / day (free_allowance; Basic plan; endpoint credit weights and market entitlements vary.)

### Task results

—

### Sources

- [official_docs](https://twelvedata.com/docs/introduction/quickstart) — checked 2026-09-09
- [official_site](https://twelvedata.com/pricing) — checked 2026-09-15
- [official_docs](https://twelvedata.com/docs/introduction/quickstart) — checked 2026-09-09
- [official_repo](https://github.com/twelvedata/twelvedata-cli) — checked 2026-09-09

<a id="twilio"></a>

## Twilio

Programmable messaging and voice APIs with test credentials, an OpenAPI spec, llms.txt, and an official CLI.

**Classification:** Communication / SMS Delivery; Communication / Voice Calls

[Website](https://www.twilio.com) · [Source record](../data/providers/twilio.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="twilio-access"></a>

[Docs](https://www.twilio.com/docs) · [API reference](https://www.twilio.com/docs/usage/api) · [CLI](https://www.twilio.com/docs/twilio-cli) · [SDK](https://www.twilio.com/docs/libraries) · [MCP entry](https://github.com/twilio-labs/mcp)

—

### Service pricing

[Official pricing](https://www.twilio.com/en-us/pricing)

### Task results

—

### Notes

- Messaging/SMS and Voice are separate products. SendGrid email is not automatically included in this Twilio record.

### Sources

- [official_docs](https://www.twilio.com/docs) — checked 2026-09-15

<a id="us-house-disclosures"></a>

## U.S. House Financial Disclosures

Original House financial disclosure filings and searchable annual indexes, published by the Clerk.

**Classification:** Search & Data Access / Financial Data / Transaction Disclosures

[Website](https://disclosures-clerk.house.gov/FinancialDisclosure) · [Source record](../data/candidates/us-house-disclosures.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="us-house-disclosures-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [filing-website (WEB)](https://disclosures-clerk.house.gov/FinancialDisclosure) | — | self serve / documented | Website/file access, not a documented public financial-data API. Annual ZIP contains filing indexes; transaction rows require the linked PDFs. Source used for independent references; not yet measured as a service. |

### Service pricing

—

### Task results

—

### Sources

- [official_site](https://disclosures-clerk.house.gov/FinancialDisclosure/ViewReport) — checked 2026-09-15
- [official_site](https://disclosures-clerk.house.gov/FinancialDisclosure/ViewSearch) — checked 2026-09-15

<a id="upstash"></a>

## Upstash

Serverless Redis, Kafka-successor queues, and vector storage with REST APIs, llms.txt, an official MCP server, and a free tier.

**Classification:** Databases / Key-value Databases; Databases / Vector Databases

[Website](https://upstash.com) · [Source record](../data/providers/upstash.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="upstash-access"></a>

[Docs](https://upstash.com/docs) · [API reference](https://upstash.com/docs/devops/developer-api/introduction) · [CLI](https://github.com/upstash/cli) · [MCP entry](https://github.com/upstash/mcp-server)

—

### Service pricing

[Official pricing](https://upstash.com/pricing)

### Task results

—

### Notes

- Legacy multi-product record: Redis maps to key-value and Vector to vector databases. QStash is a message queue, not user chat; separate new products are not inferred to share these routes.

### Sources

- [official_docs](https://upstash.com/docs/introduction) — checked 2026-09-15

<a id="vapi"></a>

## Vapi

Voice-agent orchestration API (calls, turn-taking, tool use over phone/web) with an official MCP server and an llms.txt that opens with instructions for AI agents.

**Classification:** Communication / Voice Agents; Communication / Voice Calls

[Website](https://vapi.ai) · [Source record](../data/providers/vapi.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="vapi-access"></a>

[Docs](https://docs.vapi.ai) · [API reference](https://docs.vapi.ai/api-reference) · [MCP entry](https://github.com/VapiAI/mcp-server)

—

### Service pricing

[Official pricing](https://vapi.ai/pricing)

### Task results

—

### Notes

- Voice-agent orchestration with phone and web sessions. Underlying STT/TTS providers do not establish a standalone Vapi speech-model API.

### Sources

- [official_docs](https://docs.vapi.ai/quickstart/introduction) — checked 2026-09-15

<a id="vercel"></a>

## Vercel

Frontend cloud for deploying web apps, with a REST API, CLI, official MCP server, and AI SDK ecosystem.

**Classification:** Cloud Computing & Hosting / Application Hosting

[Website](https://vercel.com) · [Source record](../data/providers/vercel.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="vercel-access"></a>

[Docs](https://vercel.com/docs) · [API reference](https://vercel.com/docs/rest-api) · [CLI](https://vercel.com/docs/cli) · [SDK](https://vercel.com/docs/rest-api/sdk) · [MCP entry](https://vercel.com/docs/mcp/vercel-mcp)

—

### Service pricing

[Official pricing](https://vercel.com/pricing)

### Task results

—

### Sources

- [official_docs](https://vercel.com/docs/integrations) — checked 2026-07-07

<a id="weaviate"></a>

## Weaviate

Open-source vector database with REST/GraphQL/gRPC APIs, Weaviate Cloud free sandboxes, an official CLI, MCP server, and llms.txt.

**Classification:** Databases / Vector Databases

[Website](https://weaviate.io) · [Source record](../data/providers/weaviate.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="weaviate-access"></a>

[Docs](https://docs.weaviate.io) · [API reference](https://docs.weaviate.io/weaviate/api/rest) · [CLI](https://github.com/weaviate/weaviate-cli) · [MCP entry](https://github.com/weaviate/mcp-server-weaviate)

—

### Service pricing

[Official pricing](https://weaviate.io/pricing)

### Task results

—

### Notes

- This record covers the vector database and its Cloud deployment. Engram is a separate named product; its memory capabilities are not transferred to this record.

### Sources

- [official_docs](https://docs.weaviate.io/weaviate) — checked 2026-09-15

<a id="wechat-pay"></a>

## WeChat Pay

Merchant payment APIs including Native QR checkout; merchant credentials and channel-specific setup are required.

**Classification:** Payments / Billing / Payment Acceptance

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

**Classification:** Payments / Billing / Payment Acceptance

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

<a id="world-bank-data"></a>

## World Bank Indicators API

Country-level economic and development indicators through the public Indicators API.

**Classification:** Search & Data Access / Financial Data / Economic Indicators

[Website](https://data.worldbank.org/) · [Source record](../data/candidates/world-bank-data.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="world-bank-data-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [data-api (API)](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) | [Docs](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) | self serve / documented | Annual country indicators have publication lags and revisions. Confirm each series and year; do not substitute annual GDP or inflation for monthly US indicators. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) — checked 2026-09-09

<a id="xai"></a>

## xAI (Grok API)

xAI's Grok models via an OpenAI-compatible REST API, with an llms.txt and self-serve console keys.

**Classification:** AI Services / Model Access

[Website](https://x.ai) · [Source record](../data/providers/xai.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="xai-access"></a>

[Docs](https://docs.x.ai) · [API reference](https://docs.x.ai/developers/rest-api-reference/inference)

—

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://docs.x.ai/overview) — checked 2026-07-08

<a id="xiurouter"></a>

## XiuRouter

Hosted model gateway with documented OpenAI, Anthropic and Gemini API protocols, scoped keys and request-level usage records.

**Classification:** AI Services / Model Access

[Website](https://router.xiu.ai/) · [Source record](../data/candidates/xiurouter.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="xiurouter-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [model-api (API)](https://router-api.xiu.ai) | [Docs](https://docs.xiu.ai/en/router/quickstart/) | — | Requires: platform_account; Documents Chat Completions, Responses, Messages and Gemini GenerateContent. The exact model, account group and protocol must match; ordinary text support does not establish tool compatibility. Responses storage, previous_response_id and background mode are outside the documented scope; Gemini Interactions, Files and fine-tuning are also excluded. Keys can restrict models, quota, expiration and IP access. No signup, authentication or model request was performed for this review. |
| [vercel-ai-sdk (SDK)](https://docs.xiu.ai/router/integrations/vercel-ai-sdk/) | [Docs](https://docs.xiu.ai/router/integrations/vercel-ai-sdk/) | — | The supplier guide installs ai and @ai-sdk/openai-compatible and configures a server-side client for the Chat Completions API. This is a third-party client path, not a XiuRouter-owned SDK or an independent service. Text, streaming and tool behavior remain untested. |

### Service pricing

—

### Task results

—

### Notes

- Vendor contribution by XiuAI / XiuLab Inc., reviewed from PR #10 at head d7395f6decec10bfbdb1cdf8cac453dc2a88da7c: https://github.com/Olorinm/agent-friendly-services/pull/10 (checked September 15, 2026). This record contains public-source claims only; it does not establish successful access or task completion.
- Usage and pricing sources describe variable charges by model, group, context length, processing mode, token/cache usage and hosted tools. A reference discount is not a guaranteed saving or an actual charge. Free allowance, sandbox availability and minimum spend remain unknown; no zero-cost claim is made.
- The current usage documentation says the benefit group is closed to new selection and will cease after September 30, 2026. Existing keys require migration to another available group; a public model listing does not grant account access. This notice concerns one group, not retirement of XiuRouter.
- The privacy source says conversation content is not stored or used for training by XiuRouter, while usage and performance records are retained long term. Model developers apply their own retention and training policies; this statement does not establish end-to-end zero retention.
- The OpenCode integration guide documents using XiuRouter as a Chat Completions model provider; that client configuration has not been tested here.

### Sources

- [official_docs](https://docs.xiu.ai/en/router/quickstart/index.md) — checked 2026-09-15
- [official_docs](https://docs.xiu.ai/en/router/api-compatibility/index.md) — checked 2026-09-15
- [official_docs](https://docs.xiu.ai/en/router/models-pricing-usage/index.md) — checked 2026-09-15
- [official_site](https://router.xiu.ai/en/pricing) — checked 2026-09-15
- [official_site](https://router.xiu.ai/en/data-privacy) — checked 2026-09-15
- [official_docs](https://docs.xiu.ai/router/integrations/vercel-ai-sdk/) — checked 2026-09-15
- [official_docs](https://docs.xiu.ai/router/integrations/opencode/) — checked 2026-09-15

<a id="xquik"></a>

## Xquik

Hosted X data and account automation service with a REST API, official MCP server, OpenAPI, SDKs, HMAC webhooks, and OAuth 2.1.

**Classification:** Search & Data Access

[Website](https://xquik.com) · [Source record](../data/candidates/xquik.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="xquik-access"></a>

[Docs](https://docs.xquik.com) · [API reference](https://docs.xquik.com/api-reference/overview) · [SDK](https://docs.xquik.com/sdks) · [MCP entry](https://docs.xquik.com/mcp/overview)

—

### Service pricing

[Official pricing](https://xquik.com/pricing)

### Task results

—

### Notes

- X-specific post/profile data and account automation. It does not meet broad public-web search or arbitrary-URL extraction criteria. Retained at data access until social-data category coverage is researched.
- The official Streamable HTTP MCP endpoint is https://xquik.com/mcp and supports API key or OAuth authentication.

### Sources

- [official_docs](https://docs.xquik.com/api-reference/overview) — checked 2026-09-15

<a id="zai"></a>

## Z.ai (GLM)

GLM models via Z.ai's OpenAI-compatible international API, with llms.txt, published pricing, and self-serve keys.

**Classification:** AI Services / Model Access

[Website](https://z.ai) · [Source record](../data/providers/zai.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="zai-access"></a>

[Docs](https://docs.z.ai) · [API reference](https://docs.z.ai/api-reference)

—

### Service pricing

[Official pricing](https://docs.z.ai/guides/overview/pricing)

### Task results

—

### Sources

- [official_docs](https://docs.z.ai/guides/overview/quick-start) — checked 2026-07-08

<a id="zapier"></a>

## Zapier

Automation platform bridging 7000+ apps, with llms.txt and an official MCP endpoint that gives agents access to those integrations.

**Classification:** Agent Infrastructure & Automation / Tool Connections; Agent Infrastructure & Automation / Workflow Automation

[Website](https://zapier.com) · [Source record](../data/providers/zapier.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="zapier-access"></a>

[Docs](https://docs.zapier.com) · [CLI](https://github.com/zapier/zapier-platform) · [MCP entry](https://zapier.com/mcp) · [MCP setup](https://docs.zapier.com/mcp/get-started/quickstart)

—

### Service pricing

[Official pricing](https://zapier.com/pricing)

### Task results

—

### Notes

- Application integrations provide actions/triggers and power executable workflows. Connector availability does not prove a downstream task passes.
- MCP setup documentation checked on 2026-09-09: https://docs.zapier.com/mcp/get-started/quickstart. The server or product entry remains separately recorded in mcp_official.

### Sources

- [official_docs](https://docs.zapier.com/integrations) — checked 2026-09-15

<a id="zoho-mail"></a>

## Zoho Mail

Persistent personal and organizational mailboxes with scoped OAuth mail APIs.

**Classification:** Communication / Mailboxes

[Website](https://www.zoho.com/mail/) · [Source record](../data/candidates/zoho-mail.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="zoho-mail-access"></a>

| Route | Docs | Personal access | Requirements and human steps |
| --- | --- | --- | --- |
| [mail-api (API)](https://www.zoho.com/mail/help/api/getting-started-with-api.html) | [Docs](https://www.zoho.com/mail/help/api/getting-started-with-api.html) | — | Account, OAuth client/scopes and data-center endpoint must be prepared. Free mailbox availability does not establish the API permissions required by a task. |

### Service pricing

—

### Task results

—

### Sources

- [official_docs](https://www.zoho.com/mail/help/api/getting-started-with-api.html) — checked 2026-09-09

<a id="qunar-flights"></a>

## 去哪儿机票合作

去哪儿官方机票及分销合作渠道线索；个人自助机票搜索 API 或 MCP 尚未确认。

**Classification:** Travel / Flights

[Website](https://www.qunar.com/site/zh/Cooperate_4.shtml) · [Source record](../data/candidates/qunar-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="qunar-flights-access"></a>

—

### Service pricing

—

### Task results

—

### Notes

- 商务联系入口不证明禁止个人；酒店供应商 API 不作为机票搜索证据，routes 暂为空。

### Sources

- [official_site](https://www.qunar.com/site/zh/Cooperate_4.shtml) — checked 2026-09-07

<a id="tongcheng-flights"></a>

## 同程机票合作

同程官方机票与出行平台合作线索；普通个人自助搜索 API 的准入、费用和能力尚未确认。

**Classification:** Travel / Flights

[Website](https://www.ly.com/public/about17u/contactus) · [Source record](../data/candidates/tongcheng-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="tongcheng-flights-access"></a>

—

### Service pricing

—

### Task results

—

### Notes

- 开放平台页面动态内容无法提取；这不是停服或没有 API 的证据，routes 暂为空。

### Sources

- [official_site](https://www.ly.com/public/about17u/contactus) — checked 2026-09-07
- [official_site](https://flights.ly.com/open/home) — checked 2026-09-07

<a id="ctrip-flights"></a>

## 携程机票合作

携程的分销与供应商合作线索；尚未确认面向普通个人的旅客机票搜索 API。

**Classification:** Travel / Flights

[Website](https://pages.ctrip.com/public/dlhz.htm) · [Source record](../data/candidates/ctrip-flights.yaml) · [Back to directory](../README.md#all-services)

### Documentation and access <a id="ctrip-flights-access"></a>

—

### Service pricing

—

### Task results

—

### Notes

- 仅发现合作入口，未把开发者主页登记成已知可调用 API。公开资料不足不等于没有 API。

### Sources

- [official_site](https://pages.ctrip.com/public/dlhz.htm) — checked 2026-09-07
- [official_site](https://developer.ctrip.com/) — checked 2026-09-07

<a id="feishu"></a>

## 飞书 Feishu

China-region Feishu workspace and Base APIs; separate account/tenant from international Lark.

**Classification:** Workplace Collaboration / Collaborative Tables

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

### Notes

- China Feishu service. Do not reuse international Lark onboarding or test results.

### Sources

- [official_docs](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/create.md) — checked 2026-09-08
- [official_repo](https://github.com/larksuite/cli) — checked 2026-09-08
- [official_repo](https://github.com/larksuite/lark-openapi-mcp) — checked 2026-09-08
- [official_site](https://www.feishu.cn/service?tab=free) — checked 2026-09-08

<a id="fliggy-domestic-flights"></a>

## 飞猪国内机票开放平台

面向机票商家的政策与订单接口，需要企业、代理商身份、店铺和聚石塔；不等同于旅客搜索接口。

**Classification:** Travel / Flights

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
