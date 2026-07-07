<!-- GENERATED FILE — do not edit. Run `npm run generate`. Source of truth: data/ -->

# Agent-Friendly Services

An evidence-backed directory of **service entry points for AI agents**: where the docs are, how to authenticate, what is machine-readable — and how fresh every fact is.

![Providers](https://img.shields.io/badge/providers-25-2563eb)
[![Link health](https://img.shields.io/badge/link_health-173_ok%2C_0_broken-10b981)](./generated/link-health.json)
[![Last update](https://img.shields.io/github/last-commit/Olorinm/agent-friendly-services?label=last%20update&color=8b5cf6)](https://github.com/Olorinm/agent-friendly-services/commits/main)
[![Data: CC BY 4.0](https://img.shields.io/badge/data-CC_BY_4.0-64748b)](./LICENSE-DATA)

**25 providers · 8 categories · 268 entry links (machine-probed weekly) · 158 capability facts, each with evidence and a date.** No scores, no tiers, no editorial ranking.

## Use It In 30 Seconds

### 🤖 You are an agent

The dataset is one JSON file — fetch it and go:

```bash
curl -s https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/providers.json
```

Recipes:

```bash
# Entry points for one provider (docs, API reference, MCP, pricing, status page…)
curl -s https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/providers.json | jq '.providers[] | select(.id == "stripe") | .entrypoints'

# Providers with an official MCP server AND a working sandbox
curl -s https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/providers.json | jq '[.providers[] | select(.entrypoints.mcp_official and .checks.sandbox_or_test_mode.status == "supported") | .id]'

# Every official MCP server in the index
curl -s https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/providers.json | jq '.providers[] | {id, mcp: .entrypoints.mcp_official} | select(.mcp)'
```

[`llms.txt`](./llms.txt) is the map of this repo; [`AGENTS.md`](./AGENTS.md) is the contribution manual. An MCP server exposing this index is on the roadmap — until then, the JSON **is** the API.

### 🧑‍💻 You are a human

Browse the [service matrix](#service-matrix) below, see [how to read it](#how-to-read-this), or open [`matrix.csv`](./generated/matrix.csv) in a spreadsheet. Want to help? Every `unknown` in [Help Wanted](#help-wanted-) is a 15-minute contribution.

### 🏢 You run one of these services

Your entry may be incomplete — that is fixable in one small PR: set `submitted_by: vendor` and use documentation (not marketing pages) as evidence. Disagree with a status? Open an issue with official evidence — facts change when evidence changes. Promotional PRs are declined; see [contributing](./docs/contributing.md).

## How To Read This

- **URL = fact.** Most questions ("is there an OpenAPI spec?") are answered with the link itself. Links are probed weekly ([`generated/link-health.json`](./generated/link-health.json)).
- **Checks** record behavior a URL can't express (self-serve signup, scoped tokens, idempotency…). `supported`/`partial` always carry an official evidence link and a verification date.
- **A missing link means "no known URL"**, not "confirmed absent". `unknown` means "checked, no reliable evidence found yet". Nobody guesses.
- Symbols: ✓ supported/available · ◐ partial · ✗ not supported · n/a not applicable · — unknown

## Service Matrix

### AI Models

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Anthropic](#anthropic) | — | ✓ | — | ✓ | — | ✓ | 2026-07-07 |
| [Gemini API](#gemini-api) | — | — | — | — | — | ✓ | 2026-07-07 |
| [Groq](#groq) | — | ✓ | — | — | — | ✓ | 2026-07-07 |
| [Hugging Face](#hugging-face) | ✓ | — | — | ✓ | — | ✓ | 2026-07-07 |
| [OpenAI](#openai) | — | — | ✓ | — | — | ✓ | 2026-07-07 |
| [Replicate](#replicate) | — | ✓ | — | ✓ | — | ✓ | 2026-07-07 |
| [Together AI](#together-ai) | — | ✓ | — | — | — | ✓ | 2026-07-07 |

### Code Execution

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Browserbase](#browserbase) | ✓ | ✓ | — | — | n/a | ✓ | 2026-07-07 |
| [E2B](#e2b) | ✓ | ✓ | — | — | n/a | ✓ | 2026-07-07 |
| [Modal](#modal) | — | ✓ | — | ✓ | ✓ | ✓ | 2026-07-07 |

### Developer Tools

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [GitHub](#github) | ✓ | — | ✓ | ✓ | — | ✓ | 2026-07-07 |

### Cloud / Hosting

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Cloudflare](#cloudflare) | ✓ | ✓ | ✓ | ✓ | ◐ | ✓ | 2026-07-07 |
| [Vercel](#vercel) | ✓ | ✓ | — | ✓ | ✓ | ✓ | 2026-07-07 |

### Databases

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [MongoDB Atlas](#mongodb-atlas) | ✓ | ✓ | ✓ | ✓ | — | ✓ | 2026-07-07 |
| [Neon](#neon) | ✓ | ✓ | — | ✓ | ✓ | ✓ | 2026-07-07 |
| [Pinecone](#pinecone) | ✓ | ✓ | — | — | — | ✓ | 2026-07-07 |
| [Supabase](#supabase) | ✓ | ✓ | — | ✓ | ◐ | ✓ | 2026-07-07 |

### Web Search / Data

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Apify](#apify) | ✓ | ✓ | — | ✓ | — | ✓ | 2026-07-07 |
| [Brave Search API](#brave-search) | — | — | — | — | — | ✓ | 2026-07-07 |
| [Exa](#exa) | ✓ | ✓ | — | — | — | ✓ | 2026-07-07 |
| [Firecrawl](#firecrawl) | ✓ | ✓ | — | — | — | ✓ | 2026-07-07 |
| [Perplexity API](#perplexity) | ✓ | ✓ | — | — | — | ✓ | 2026-07-07 |
| [Tavily](#tavily) | ✓ | ✓ | — | — | — | ✓ | 2026-07-07 |

### Payments / Billing

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Stripe](#stripe) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 2026-07-07 |

### Communication

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Resend](#resend) | ✓ | — | — | — | ✓ | ✓ | 2026-07-07 |

## Providers

### Anthropic <a id="anthropic"></a>

> Claude model APIs with agent-focused documentation, llms.txt, and the company behind the MCP standard itself.

**Category:** AI Models · `llms.txt` `CLI` `Agent Docs` `Self-serve`

**Links:** [Documentation](https://docs.anthropic.com) · [API Reference](https://docs.anthropic.com/en/api) · [llms.txt](https://docs.anthropic.com/llms.txt) · [Changelog](https://docs.anthropic.com/en/release-notes/api) · [Status Page](https://status.anthropic.com) · [Pricing](https://www.anthropic.com/pricing) · [Signup](https://console.anthropic.com) · [API Keys](https://docs.anthropic.com/en/api/getting-started) · [CLI](https://docs.anthropic.com/en/docs/claude-code) · [SDKs](https://docs.anthropic.com/en/api/client-sdks) · [Agent Docs](https://docs.anthropic.com/en/docs/agents-and-tools) · [Rate Limits](https://docs.anthropic.com/en/api/rate-limits) · [Errors](https://docs.anthropic.com/en/api/errors)

- **Supported:** [Self-serve signup](https://console.anthropic.com) · [Self-serve API keys](https://docs.anthropic.com/en/api/getting-started) · [Self-serve upgrade](https://www.anthropic.com/pricing) · [Usage dashboard](https://docs.anthropic.com/en/api/rate-limits) · [Versioning policy](https://docs.anthropic.com/en/api/versioning)
- **Partial:** [Scoped tokens](https://docs.anthropic.com/en/api/rate-limits) — Keys are scoped per workspace (limits and separation per workspace); no per-permission scoping.
- **Unknown (help wanted):** `oauth_support`, `token_revocation`, `sandbox_or_test_mode`, `free_tier_or_trial`, `idempotency`, `automation_permitted`

> Anthropic authored the MCP standard; no first-party MCP server exposing the Anthropic API was found at review time (mcp_official intentionally absent).
> Claude Code is listed as cli — it is an agent CLI rather than an API-management CLI.

### Apify <a id="apify"></a>

> Web scraping and automation platform with thousands of ready-made actors, a versioned API, llms.txt, and an official MCP server.

**Category:** Web Search / Data · `Official MCP` `llms.txt` `CLI` `Self-serve`

**Links:** [Documentation](https://docs.apify.com) · [API Reference](https://docs.apify.com/api/v2) · [llms.txt](https://docs.apify.com/llms.txt) · [Changelog](https://apify.com/change-log) · [Status Page](https://status.apify.com) · [Pricing](https://apify.com/pricing) · [Signup](https://console.apify.com/sign-up) · [API Keys](https://docs.apify.com/platform/integrations/api) · [CLI](https://docs.apify.com/cli) · [SDKs](https://docs.apify.com/sdk) · [Official MCP](https://docs.apify.com/platform/integrations/mcp) · [Webhooks](https://docs.apify.com/platform/integrations/webhooks)

- **Supported:** [Self-serve signup](https://console.apify.com/sign-up) · [Self-serve API keys](https://docs.apify.com/platform/integrations/api) · [Free tier / trial](https://apify.com/pricing) · [Self-serve upgrade](https://apify.com/pricing) · [Versioning policy](https://docs.apify.com/api/v2)
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `sandbox_or_test_mode`, `usage_dashboard`, `idempotency`, `automation_permitted`

> mcp.apify.com hosts the official remote MCP server; the docs page above explains setup.

### Brave Search API <a id="brave-search"></a>

> Independent web search index with a developer API, self-serve registration, and a free plan.

**Category:** Web Search / Data · **Scope:** Brave Search API (Data for Search / Data for AI plans); the consumer search engine is not assessed. · `Self-serve`

**Links:** [Documentation](https://api-dashboard.search.brave.com/app/documentation) · [Pricing](https://brave.com/search/api/) · [Signup](https://api-dashboard.search.brave.com/register)

- **Supported:** [Self-serve signup](https://api-dashboard.search.brave.com/register) · [Self-serve API keys](https://api-dashboard.search.brave.com/app/documentation) · [Free tier / trial](https://brave.com/search/api/) · [Self-serve upgrade](https://brave.com/search/api/)
- **N/A:** Idempotency — Read-only search API; requests are inherently repeatable.
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `sandbox_or_test_mode`, `usage_dashboard`, `versioning_policy`, `automation_permitted`

> Detailed API docs live inside the dashboard domain but are publicly readable without login (verified at review time).

### Browserbase <a id="browserbase"></a>

> Headless browser infrastructure for AI agents and automation, with session APIs and an official MCP server.

**Category:** Code Execution · `Official MCP` `llms.txt` `Self-serve`

**Links:** [Documentation](https://docs.browserbase.com) · [API Reference](https://docs.browserbase.com/reference) · [llms.txt](https://docs.browserbase.com/llms.txt) · [Status Page](https://status.browserbase.com) · [Pricing](https://www.browserbase.com/pricing) · [Signup](https://www.browserbase.com/sign-up) · [API Keys](https://docs.browserbase.com/introduction) · [SDKs](https://docs.browserbase.com/reference) · [Official MCP](https://github.com/browserbase/mcp-server-browserbase)

- **Supported:** [Self-serve signup](https://www.browserbase.com/sign-up) · [Self-serve API keys](https://docs.browserbase.com/introduction) · [Free tier / trial](https://www.browserbase.com/pricing) · [Self-serve upgrade](https://www.browserbase.com/pricing) · [Automation permitted](https://www.browserbase.com)
- **N/A:** Sandbox / test mode — The product itself is an ephemeral, isolated browser session — every run is a sandbox.
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `usage_dashboard`, `idempotency`, `versioning_policy`

> Stagehand (the company's agent framework) is a separate open-source project and not assessed here.

### Cloudflare <a id="cloudflare"></a>

> Edge network, Workers serverless platform, storage, and AI services with agent-focused docs and official MCP servers.

**Category:** Cloud / Hosting · **Scope:** Developer platform (Workers, R2, D1, AI) and core API. Enterprise network products not assessed. · `Official MCP` `llms.txt` `OpenAPI` `CLI` `Agent Docs` `Self-serve`

**Links:** [Documentation](https://developers.cloudflare.com) · [API Reference](https://developers.cloudflare.com/api/) · [OpenAPI](https://github.com/cloudflare/api-schemas) · [llms.txt](https://developers.cloudflare.com/llms.txt) · [Changelog](https://developers.cloudflare.com/changelog/) · [Status Page](https://www.cloudflarestatus.com) · [Pricing](https://www.cloudflare.com/plans/) · [Signup](https://dash.cloudflare.com/sign-up) · [API Keys](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) · [CLI](https://developers.cloudflare.com/workers/wrangler/) · [SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/) · [Official MCP](https://github.com/cloudflare/mcp-server-cloudflare) · [Agent Docs](https://developers.cloudflare.com/agents/)

- **Supported:** [Self-serve signup](https://dash.cloudflare.com/sign-up) · [Self-serve API keys](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) · [Scoped tokens](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) · [Token revocation](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) · [Free tier / trial](https://www.cloudflare.com/plans/) · [Self-serve upgrade](https://www.cloudflare.com/plans/) · [Versioning policy](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/)
- **Partial:** [Sandbox / test mode](https://developers.cloudflare.com/workers/wrangler/) — No global sandbox; wrangler local dev and the Workers free plan serve as a test environment.
- **Unknown (help wanted):** `oauth_support`, `usage_dashboard`, `idempotency`, `automation_permitted`

### E2B <a id="e2b"></a>

> Isolated cloud sandboxes for running AI-generated code, with llms.txt, an official MCP server, and self-serve keys.

**Category:** Code Execution · `Official MCP` `llms.txt` `Self-serve`

**Links:** [Documentation](https://e2b.dev/docs) · [llms.txt](https://e2b.dev/llms.txt) · [Status Page](https://status.e2b.dev) · [Pricing](https://e2b.dev/pricing) · [Signup](https://e2b.dev/dashboard) · [API Keys](https://e2b.dev/docs/api-key) · [SDKs](https://e2b.dev/docs/sdk-reference) · [Official MCP](https://github.com/e2b-dev/mcp-server)

- **Supported:** [Self-serve signup](https://e2b.dev/dashboard) · [Self-serve API keys](https://e2b.dev/docs/api-key) · [Free tier / trial](https://e2b.dev/pricing) · [Self-serve upgrade](https://e2b.dev/pricing) · [Automation permitted](https://e2b.dev/docs)
- **N/A:** Sandbox / test mode — The product itself is an isolated, ephemeral sandbox per session.
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `usage_dashboard`, `idempotency`, `versioning_policy`

### Exa <a id="exa"></a>

> Search API built for AI — semantic web search, content retrieval, and research endpoints with an official MCP server.

**Category:** Web Search / Data · `Official MCP` `llms.txt` `Self-serve`

**Links:** [Documentation](https://docs.exa.ai) · [API Reference](https://docs.exa.ai/reference/getting-started) · [llms.txt](https://docs.exa.ai/llms.txt) · [Changelog](https://docs.exa.ai/changelog) · [Pricing](https://exa.ai/pricing) · [Signup](https://dashboard.exa.ai) · [API Keys](https://docs.exa.ai/reference/getting-started) · [SDKs](https://docs.exa.ai/sdks/typescript-sdk-specification) · [Official MCP](https://github.com/exa-labs/exa-mcp-server) · [Rate Limits](https://docs.exa.ai/reference/rate-limits)

- **Supported:** [Self-serve signup](https://dashboard.exa.ai) · [Self-serve API keys](https://docs.exa.ai/reference/getting-started) · [Free tier / trial](https://exa.ai/pricing) · [Self-serve upgrade](https://exa.ai/pricing)
- **N/A:** Idempotency — Read-only search/retrieval API; requests are inherently repeatable.
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `sandbox_or_test_mode`, `usage_dashboard`, `versioning_policy`, `automation_permitted`

### Firecrawl <a id="firecrawl"></a>

> Web scraping and crawling API that turns websites into LLM-ready markdown, with an official MCP server.

**Category:** Web Search / Data · `Official MCP` `llms.txt` `Self-serve`

**Links:** [Documentation](https://docs.firecrawl.dev) · [API Reference](https://docs.firecrawl.dev/api-reference/introduction) · [llms.txt](https://docs.firecrawl.dev/llms.txt) · [Pricing](https://www.firecrawl.dev/pricing) · [Signup](https://www.firecrawl.dev/signin/signup) · [API Keys](https://docs.firecrawl.dev/introduction) · [SDKs](https://docs.firecrawl.dev/sdks/overview) · [Official MCP](https://docs.firecrawl.dev/mcp-server) · [Rate Limits](https://docs.firecrawl.dev/rate-limits)

- **Supported:** [Self-serve signup](https://www.firecrawl.dev/pricing) · [Self-serve API keys](https://docs.firecrawl.dev/introduction) · [Free tier / trial](https://www.firecrawl.dev/pricing) · [Self-serve upgrade](https://www.firecrawl.dev/pricing)
- **N/A:** Idempotency — Scrape/crawl jobs are re-runnable reads; no state mutation to protect.
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `sandbox_or_test_mode`, `usage_dashboard`, `versioning_policy`, `automation_permitted`

### Gemini API <a id="gemini-api"></a>

> Google's Gemini model APIs via AI Studio, with generous free tier and documented API versioning.

**Category:** AI Models · **Scope:** Gemini API via Google AI Studio (ai.google.dev); Vertex AI is not assessed. · `Agent Docs` `Self-serve`

**Links:** [Documentation](https://ai.google.dev/gemini-api/docs) · [API Reference](https://ai.google.dev/api) · [Changelog](https://ai.google.dev/gemini-api/docs/changelog) · [Pricing](https://ai.google.dev/gemini-api/docs/pricing) · [Signup](https://aistudio.google.com) · [API Keys](https://ai.google.dev/gemini-api/docs/api-key) · [SDKs](https://ai.google.dev/gemini-api/docs/libraries) · [Agent Docs](https://ai.google.dev/gemini-api/docs/function-calling) · [Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits) · [Errors](https://ai.google.dev/gemini-api/docs/troubleshooting)

- **Supported:** [Self-serve signup](https://aistudio.google.com) · [Self-serve API keys](https://ai.google.dev/gemini-api/docs/api-key) · [Free tier / trial](https://ai.google.dev/gemini-api/docs/pricing) · [Self-serve upgrade](https://ai.google.dev/gemini-api/docs/pricing) · [Versioning policy](https://ai.google.dev/gemini-api/docs/api-versions)
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `sandbox_or_test_mode`, `usage_dashboard`, `idempotency`, `automation_permitted`

### GitHub <a id="github"></a>

> Code hosting, collaboration, and automation with REST and GraphQL APIs, an official CLI, and an official MCP server.

**Category:** Developer Tools · **Scope:** Core platform (repos, issues, PRs, REST/GraphQL APIs). Actions/Packages/Copilot not assessed separately. · `Official MCP` `OpenAPI` `CLI` `Self-serve`

**Links:** [Documentation](https://docs.github.com) · [API Reference](https://docs.github.com/rest) · [OpenAPI](https://github.com/github/rest-api-description) · [GraphQL](https://docs.github.com/graphql) · [Changelog](https://github.blog/changelog/) · [Status Page](https://www.githubstatus.com) · [Pricing](https://github.com/pricing) · [Signup](https://github.com/signup) · [API Keys](https://docs.github.com/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) · [CLI](https://cli.github.com) · [SDKs](https://github.com/octokit) · [Official MCP](https://github.com/github/github-mcp-server) · [Webhooks](https://docs.github.com/webhooks) · [Rate Limits](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api)

- **Supported:** [Self-serve signup](https://github.com/signup) · [Self-serve API keys](https://docs.github.com/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) · [OAuth](https://docs.github.com/apps/oauth-apps) · [Scoped tokens](https://docs.github.com/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) · [Token revocation](https://docs.github.com/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) · [Free tier / trial](https://github.com/pricing) · [Self-serve upgrade](https://github.com/pricing) · [Usage dashboard](https://docs.github.com/billing) · [Versioning policy](https://docs.github.com/rest/about-the-rest-api/api-versions) · [Automation permitted](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
- **Unknown (help wanted):** `sandbox_or_test_mode`, `idempotency`

> Multi-product platform; this entry covers the core developer platform only (see scope).

### Groq <a id="groq"></a>

> Ultra-low-latency LLM inference with an OpenAI-compatible API, llms.txt, and self-serve keys with a free tier.

**Category:** AI Models · `llms.txt` `Self-serve`

**Links:** [Documentation](https://console.groq.com/docs) · [API Reference](https://console.groq.com/docs/api-reference) · [llms.txt](https://console.groq.com/llms.txt) · [Changelog](https://console.groq.com/docs/changelog) · [Status Page](https://groqstatus.com) · [Pricing](https://groq.com/pricing) · [Signup](https://console.groq.com) · [API Keys](https://console.groq.com/docs/quickstart) · [SDKs](https://console.groq.com/docs/libraries) · [Rate Limits](https://console.groq.com/docs/rate-limits) · [Errors](https://console.groq.com/docs/errors)

- **Supported:** [Self-serve signup](https://console.groq.com) · [Self-serve API keys](https://console.groq.com/docs/quickstart) · [Free tier / trial](https://groq.com/pricing) · [Self-serve upgrade](https://groq.com/pricing)
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `sandbox_or_test_mode`, `usage_dashboard`, `idempotency`, `versioning_policy`, `automation_permitted`

### Hugging Face <a id="hugging-face"></a>

> Model hub and inference platform with fine-grained tokens, OAuth, an official MCP server, and a full Hub API.

**Category:** AI Models · **Scope:** Hub + Hub API + Inference Providers; self-hosted libraries are not assessed. · `Official MCP` `CLI` `Self-serve`

**Links:** [Documentation](https://huggingface.co/docs) · [API Reference](https://huggingface.co/docs/hub/api) · [Status Page](https://status.huggingface.co) · [Pricing](https://huggingface.co/pricing) · [Signup](https://huggingface.co/join) · [API Keys](https://huggingface.co/docs/hub/security-tokens) · [CLI](https://huggingface.co/docs/huggingface_hub/guides/cli) · [SDKs](https://huggingface.co/docs/huggingface_hub) · [Official MCP](https://huggingface.co/mcp) · [Rate Limits](https://huggingface.co/docs/hub/rate-limits)

- **Supported:** [Self-serve signup](https://huggingface.co/join) · [Self-serve API keys](https://huggingface.co/docs/hub/security-tokens) · [OAuth](https://huggingface.co/docs/hub/oauth) · [Scoped tokens](https://huggingface.co/docs/hub/security-tokens) · [Token revocation](https://huggingface.co/docs/hub/security-tokens) · [Free tier / trial](https://huggingface.co/pricing) · [Self-serve upgrade](https://huggingface.co/pricing)
- **Unknown (help wanted):** `sandbox_or_test_mode`, `usage_dashboard`, `idempotency`, `versioning_policy`, `automation_permitted`

### Modal <a id="modal"></a>

> Serverless compute for Python with first-class Sandboxes for agent code execution, llms.txt, and an official CLI.

**Category:** Code Execution · `llms.txt` `CLI` `Agent Docs` `Sandbox` `Self-serve`

**Links:** [Documentation](https://modal.com/docs) · [API Reference](https://modal.com/docs/reference) · [llms.txt](https://modal.com/llms.txt) · [Changelog](https://modal.com/docs/reference/changelog) · [Status Page](https://status.modal.com) · [Pricing](https://modal.com/pricing) · [Signup](https://modal.com/signup) · [API Keys](https://modal.com/docs/reference/cli) · [CLI](https://modal.com/docs/reference/cli) · [Agent Docs](https://modal.com/docs/guide/sandbox)

- **Supported:** [Self-serve signup](https://modal.com/signup) · [Self-serve API keys](https://modal.com/docs/reference/cli) · [Sandbox / test mode](https://modal.com/docs/guide/sandbox) · [Free tier / trial](https://modal.com/pricing) · [Self-serve upgrade](https://modal.com/pricing) · [Automation permitted](https://modal.com/docs/guide/sandbox)
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `usage_dashboard`, `idempotency`, `versioning_policy`

### MongoDB Atlas <a id="mongodb-atlas"></a>

> Managed MongoDB with a versioned Admin API, published OpenAPI spec, llms.txt, official CLI and MCP server.

**Category:** Databases · **Scope:** Atlas managed cloud + Atlas Administration API; self-hosted MongoDB is not assessed. · `Official MCP` `llms.txt` `OpenAPI` `CLI` `Self-serve`

**Links:** [Documentation](https://www.mongodb.com/docs/atlas/) · [API Reference](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/) · [OpenAPI](https://github.com/mongodb/openapi) · [llms.txt](https://www.mongodb.com/docs/llms.txt) · [Changelog](https://www.mongodb.com/docs/atlas/release-notes/) · [Status Page](https://status.cloud.mongodb.com) · [Pricing](https://www.mongodb.com/pricing) · [Signup](https://www.mongodb.com/cloud/atlas/register) · [API Keys](https://www.mongodb.com/docs/atlas/configure-api-access/) · [CLI](https://www.mongodb.com/docs/atlas/cli/) · [SDKs](https://www.mongodb.com/docs/drivers/) · [Official MCP](https://github.com/mongodb-js/mongodb-mcp-server)

- **Supported:** [Self-serve signup](https://www.mongodb.com/cloud/atlas/register) · [Self-serve API keys](https://www.mongodb.com/docs/atlas/configure-api-access/) · [OAuth](https://www.mongodb.com/docs/atlas/configure-api-access/) · [Scoped tokens](https://www.mongodb.com/docs/atlas/configure-api-access/) · [Token revocation](https://www.mongodb.com/docs/atlas/configure-api-access/) · [Free tier / trial](https://www.mongodb.com/pricing) · [Self-serve upgrade](https://www.mongodb.com/pricing) · [Versioning policy](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/)
- **Unknown (help wanted):** `sandbox_or_test_mode`, `usage_dashboard`, `idempotency`, `automation_permitted`

### Neon <a id="neon"></a>

> Serverless Postgres with instant branching, a full management API, official MCP server, and agent-oriented docs.

**Category:** Databases · `Official MCP` `llms.txt` `CLI` `Agent Docs` `Sandbox` `Self-serve`

**Links:** [Documentation](https://neon.com/docs) · [API Reference](https://api-docs.neon.tech) · [llms.txt](https://neon.com/llms.txt) · [Changelog](https://neon.com/docs/changelog) · [Status Page](https://neonstatus.com) · [Pricing](https://neon.com/pricing) · [Signup](https://console.neon.tech/signup) · [API Keys](https://neon.com/docs/manage/api-keys) · [CLI](https://neon.com/docs/reference/neon-cli) · [Official MCP](https://github.com/neondatabase/mcp-server-neon) · [Agent Docs](https://neon.com/docs/ai/ai-intro)

- **Supported:** [Self-serve signup](https://console.neon.tech/signup) · [Self-serve API keys](https://neon.com/docs/manage/api-keys) · [OAuth](https://neon.com/docs/guides/oauth-integration) · [Token revocation](https://neon.com/docs/manage/api-keys) · [Sandbox / test mode](https://neon.com/docs/introduction/branching) · [Free tier / trial](https://neon.com/pricing) · [Self-serve upgrade](https://neon.com/pricing) · [Usage dashboard](https://neon.com/docs/introduction/monitor-usage)
- **Partial:** [Scoped tokens](https://neon.com/docs/manage/api-keys) — Organization- and project-scoped API keys; no per-permission scoping.
- **Unknown (help wanted):** `idempotency`, `versioning_policy`, `automation_permitted`

### OpenAI <a id="openai"></a>

> GPT model APIs with an official OpenAPI spec, agents guides, and a large SDK ecosystem.

**Category:** AI Models · `OpenAPI` `Agent Docs` `Self-serve`

**Links:** [Documentation](https://platform.openai.com/docs) · [API Reference](https://platform.openai.com/docs/api-reference) · [OpenAPI](https://github.com/openai/openai-openapi) · [Changelog](https://platform.openai.com/docs/changelog) · [Status Page](https://status.openai.com) · [Pricing](https://platform.openai.com/docs/pricing) · [Signup](https://platform.openai.com/signup) · [API Keys](https://platform.openai.com/docs/quickstart) · [SDKs](https://platform.openai.com/docs/libraries) · [Agent Docs](https://platform.openai.com/docs/guides/agents) · [Rate Limits](https://platform.openai.com/docs/guides/rate-limits) · [Errors](https://platform.openai.com/docs/guides/error-codes)

- **Supported:** [Self-serve signup](https://platform.openai.com/signup) · [Self-serve API keys](https://platform.openai.com/docs/quickstart) · [Self-serve upgrade](https://platform.openai.com/docs/pricing) · [Versioning policy](https://platform.openai.com/docs/deprecations)
- **Partial:** [Scoped tokens](https://platform.openai.com/docs/quickstart) — Project-scoped API keys separate projects; permission granularity is limited.
- **Unknown (help wanted):** `oauth_support`, `token_revocation`, `sandbox_or_test_mode`, `free_tier_or_trial`, `usage_dashboard`, `idempotency`, `automation_permitted`

### Perplexity API <a id="perplexity"></a>

> Sonar API for web-grounded answers and search, with llms.txt, an official MCP server, and documented usage tiers.

**Category:** Web Search / Data · **Scope:** Sonar API platform (docs.perplexity.ai); the consumer Perplexity app is not assessed. · `Official MCP` `llms.txt` `Self-serve`

**Links:** [Documentation](https://docs.perplexity.ai) · [llms.txt](https://docs.perplexity.ai/llms.txt) · [Changelog](https://docs.perplexity.ai/changelog) · [Status Page](https://status.perplexity.com) · [Pricing](https://docs.perplexity.ai/getting-started/pricing) · [API Keys](https://docs.perplexity.ai/getting-started/quickstart) · [Official MCP](https://github.com/ppl-ai/modelcontextprotocol) · [Rate Limits](https://docs.perplexity.ai/guides/rate-limits)

- **Supported:** [Self-serve signup](https://docs.perplexity.ai/getting-started/quickstart) · [Self-serve API keys](https://docs.perplexity.ai/getting-started/quickstart) · [Self-serve upgrade](https://docs.perplexity.ai/getting-started/pricing)
- **Partial:** [Free tier / trial](https://docs.perplexity.ai/getting-started/pricing) — No standalone free tier; Perplexity Pro subscribers receive monthly API credits.
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `sandbox_or_test_mode`, `usage_dashboard`, `idempotency`, `versioning_policy`, `automation_permitted`

### Pinecone <a id="pinecone"></a>

> Managed vector database for search and RAG, with llms.txt, an official MCP server, and self-serve keys.

**Category:** Databases · `Official MCP` `llms.txt` `Self-serve`

**Links:** [Documentation](https://docs.pinecone.io) · [API Reference](https://docs.pinecone.io/reference/api/introduction) · [llms.txt](https://docs.pinecone.io/llms.txt) · [Changelog](https://docs.pinecone.io/release-notes) · [Status Page](https://status.pinecone.io) · [Pricing](https://www.pinecone.io/pricing/) · [Signup](https://app.pinecone.io) · [API Keys](https://docs.pinecone.io/guides/projects/manage-api-keys) · [Official MCP](https://docs.pinecone.io/guides/operations/mcp-server)

- **Supported:** [Self-serve signup](https://app.pinecone.io) · [Self-serve API keys](https://docs.pinecone.io/guides/projects/manage-api-keys) · [Token revocation](https://docs.pinecone.io/guides/projects/manage-api-keys) · [Free tier / trial](https://www.pinecone.io/pricing/) · [Self-serve upgrade](https://www.pinecone.io/pricing/) · [Versioning policy](https://docs.pinecone.io/reference/api/versioning)
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `sandbox_or_test_mode`, `usage_dashboard`, `idempotency`, `automation_permitted`

### Replicate <a id="replicate"></a>

> Run and fine-tune open-source models via a simple predictions API, with llms.txt, webhooks, and an official CLI.

**Category:** AI Models · `llms.txt` `CLI` `Self-serve`

**Links:** [Documentation](https://replicate.com/docs) · [API Reference](https://replicate.com/docs/reference/http) · [llms.txt](https://replicate.com/llms.txt) · [Changelog](https://replicate.com/changelog) · [Status Page](https://replicatestatus.com) · [Pricing](https://replicate.com/pricing) · [Signup](https://replicate.com/signin) · [API Keys](https://replicate.com/docs/reference/http) · [CLI](https://github.com/replicate/cli) · [SDKs](https://replicate.com/docs/reference/client-libraries) · [Webhooks](https://replicate.com/docs/topics/webhooks)

- **Supported:** [Self-serve signup](https://replicate.com/signin) · [Self-serve API keys](https://replicate.com/docs/reference/http) · [Self-serve upgrade](https://replicate.com/pricing)
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `sandbox_or_test_mode`, `free_tier_or_trial`, `usage_dashboard`, `idempotency`, `versioning_policy`, `automation_permitted`

### Resend <a id="resend"></a>

> Email API for developers with test mode, scoped API keys, idempotency support, and an official MCP server.

**Category:** Communication · `Official MCP` `Sandbox` `Self-serve` `Idempotent API`

**Links:** [Documentation](https://resend.com/docs) · [API Reference](https://resend.com/docs/api-reference/introduction) · [Changelog](https://resend.com/changelog) · [Pricing](https://resend.com/pricing) · [Signup](https://resend.com/signup) · [API Keys](https://resend.com/docs/dashboard/api-keys/introduction) · [SDKs](https://resend.com/docs/sdks) · [Official MCP](https://github.com/resend/mcp-send-email) · [Webhooks](https://resend.com/docs/dashboard/webhooks/introduction) · [Errors](https://resend.com/docs/api-reference/errors)

- **Supported:** [Self-serve signup](https://resend.com/signup) · [Self-serve API keys](https://resend.com/docs/dashboard/api-keys/introduction) · [Scoped tokens](https://resend.com/docs/dashboard/api-keys/introduction) · [Token revocation](https://resend.com/docs/dashboard/api-keys/introduction) · [Sandbox / test mode](https://resend.com/docs/dashboard/emails/send-test-emails) · [Free tier / trial](https://resend.com/pricing) · [Self-serve upgrade](https://resend.com/pricing) · [Idempotency](https://resend.com/docs/api-reference/introduction)
- **Unknown (help wanted):** `oauth_support`, `usage_dashboard`, `versioning_policy`, `automation_permitted`

### Stripe <a id="stripe"></a>

> Payments, billing, subscriptions, and financial infrastructure with a famously complete API surface.

**Category:** Payments / Billing · `Official MCP` `llms.txt` `OpenAPI` `CLI` `Agent Docs` `Sandbox` `Self-serve` `Idempotent API`

**Links:** [Documentation](https://docs.stripe.com) · [API Reference](https://docs.stripe.com/api) · [OpenAPI](https://github.com/stripe/openapi) · [llms.txt](https://docs.stripe.com/llms.txt) · [Changelog](https://docs.stripe.com/changelog) · [Status Page](https://status.stripe.com) · [Pricing](https://stripe.com/pricing) · [Signup](https://dashboard.stripe.com/register) · [API Keys](https://docs.stripe.com/keys) · [CLI](https://docs.stripe.com/stripe-cli) · [SDKs](https://docs.stripe.com/sdks) · [Official MCP](https://docs.stripe.com/mcp) · [Agent Docs](https://docs.stripe.com/agents) · [Webhooks](https://docs.stripe.com/webhooks) · [Rate Limits](https://docs.stripe.com/rate-limits) · [Errors](https://docs.stripe.com/api/errors)

- **Supported:** [Self-serve signup](https://dashboard.stripe.com/register) · [Self-serve API keys](https://docs.stripe.com/keys) · [OAuth](https://docs.stripe.com/connect/oauth-reference) · [Scoped tokens](https://docs.stripe.com/keys) · [Token revocation](https://docs.stripe.com/keys) · [Sandbox / test mode](https://docs.stripe.com/testing) · [Free tier / trial](https://docs.stripe.com/testing) · [Self-serve upgrade](https://stripe.com/pricing) · [Usage dashboard](https://docs.stripe.com/dashboard/basics) · [Idempotency](https://docs.stripe.com/api/idempotent_requests) · [Versioning policy](https://docs.stripe.com/api/versioning)
- **Unknown (help wanted):** `automation_permitted`

> Agent tooling (MCP, agent toolkit) evolves quickly; re-check quarterly.

### Supabase <a id="supabase"></a>

> Postgres platform with auth, storage, edge functions, a management API, official MCP server, and LLM-ready docs.

**Category:** Databases · `Official MCP` `llms.txt` `CLI` `Agent Docs` `Self-serve`

**Links:** [Documentation](https://supabase.com/docs) · [API Reference](https://supabase.com/docs/reference/api/introduction) · [llms.txt](https://supabase.com/llms.txt) · [Changelog](https://supabase.com/changelog) · [Status Page](https://status.supabase.com) · [Pricing](https://supabase.com/pricing) · [Signup](https://supabase.com/dashboard/sign-up) · [API Keys](https://supabase.com/docs/guides/api/api-keys) · [CLI](https://supabase.com/docs/guides/cli) · [SDKs](https://supabase.com/docs/reference) · [Official MCP](https://supabase.com/docs/guides/getting-started/mcp) · [Agent Docs](https://supabase.com/docs/guides/getting-started/ai-prompts) · [Webhooks](https://supabase.com/docs/guides/database/webhooks)

- **Supported:** [Self-serve signup](https://supabase.com/dashboard/sign-up) · [Self-serve API keys](https://supabase.com/docs/guides/api/api-keys) · [OAuth](https://supabase.com/docs/guides/integrations/build-a-supabase-integration) · [Token revocation](https://supabase.com/docs/guides/api/api-keys) · [Free tier / trial](https://supabase.com/pricing) · [Self-serve upgrade](https://supabase.com/pricing)
- **Partial:** [Scoped tokens](https://supabase.com/docs/guides/api/api-keys) — Publishable/secret key split and JWT roles; management-API tokens are account-wide.
- **Partial:** [Sandbox / test mode](https://supabase.com/docs/guides/cli) — Full local development stack via CLI; hosted branching is a paid feature.
- **Unknown (help wanted):** `usage_dashboard`, `idempotency`, `versioning_policy`, `automation_permitted`

### Tavily <a id="tavily"></a>

> Search and extraction API built for AI agents, with llms.txt, an official MCP server, and a free tier.

**Category:** Web Search / Data · `Official MCP` `llms.txt` `Self-serve`

**Links:** [Documentation](https://docs.tavily.com) · [API Reference](https://docs.tavily.com/documentation/api-reference/introduction) · [llms.txt](https://docs.tavily.com/llms.txt) · [Status Page](https://status.tavily.com) · [Pricing](https://www.tavily.com/pricing) · [Signup](https://app.tavily.com) · [API Keys](https://docs.tavily.com/documentation/quickstart) · [SDKs](https://docs.tavily.com/sdk) · [Official MCP](https://docs.tavily.com/documentation/mcp) · [Rate Limits](https://docs.tavily.com/documentation/rate-limits)

- **Supported:** [Self-serve signup](https://app.tavily.com) · [Self-serve API keys](https://docs.tavily.com/documentation/quickstart) · [Free tier / trial](https://www.tavily.com/pricing) · [Self-serve upgrade](https://www.tavily.com/pricing)
- **N/A:** Idempotency — Read-only search/extract API; requests are inherently repeatable.
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `sandbox_or_test_mode`, `usage_dashboard`, `versioning_policy`, `automation_permitted`

### Together AI <a id="together-ai"></a>

> Inference and fine-tuning platform for open-source models with an OpenAI-compatible API and llms.txt.

**Category:** AI Models · `llms.txt` `Self-serve`

**Links:** [Documentation](https://docs.together.ai) · [API Reference](https://docs.together.ai/reference/chat-completions) · [llms.txt](https://docs.together.ai/llms.txt) · [Status Page](https://status.together.ai) · [Pricing](https://www.together.ai/pricing) · [Signup](https://api.together.ai) · [API Keys](https://docs.together.ai/docs/quickstart) · [Rate Limits](https://docs.together.ai/docs/rate-limits) · [Errors](https://docs.together.ai/docs/error-codes)

- **Supported:** [Self-serve signup](https://api.together.ai) · [Self-serve API keys](https://docs.together.ai/docs/quickstart) · [Self-serve upgrade](https://www.together.ai/pricing)
- **Unknown (help wanted):** `oauth_support`, `scoped_tokens`, `token_revocation`, `sandbox_or_test_mode`, `free_tier_or_trial`, `usage_dashboard`, `idempotency`, `versioning_policy`, `automation_permitted`

### Vercel <a id="vercel"></a>

> Frontend cloud for deploying web apps, with a REST API, CLI, official MCP server, and AI SDK ecosystem.

**Category:** Cloud / Hosting · `Official MCP` `llms.txt` `CLI` `Agent Docs` `Sandbox` `Self-serve`

**Links:** [Documentation](https://vercel.com/docs) · [API Reference](https://vercel.com/docs/rest-api) · [llms.txt](https://vercel.com/llms.txt) · [Changelog](https://vercel.com/changelog) · [Status Page](https://www.vercel-status.com) · [Pricing](https://vercel.com/pricing) · [Signup](https://vercel.com/signup) · [API Keys](https://vercel.com/guides/how-do-i-use-a-vercel-api-access-token) · [CLI](https://vercel.com/docs/cli) · [SDKs](https://vercel.com/docs/rest-api/sdk) · [Official MCP](https://vercel.com/docs/mcp/vercel-mcp) · [Agent Docs](https://vercel.com/docs/agents) · [Webhooks](https://vercel.com/docs/webhooks) · [Rate Limits](https://vercel.com/docs/limits) · [Errors](https://vercel.com/docs/errors)

- **Supported:** [Self-serve signup](https://vercel.com/signup) · [Self-serve API keys](https://vercel.com/guides/how-do-i-use-a-vercel-api-access-token) · [OAuth](https://vercel.com/docs/integrations) · [Token revocation](https://vercel.com/guides/how-do-i-use-a-vercel-api-access-token) · [Sandbox / test mode](https://vercel.com/docs/deployments/environments) · [Free tier / trial](https://vercel.com/pricing) · [Self-serve upgrade](https://vercel.com/pricing) · [Usage dashboard](https://vercel.com/docs/pricing/understanding-my-invoice)
- **Partial:** [Scoped tokens](https://vercel.com/guides/how-do-i-use-a-vercel-api-access-token) — Tokens are scoped to account or team, not to fine-grained permissions.
- **Partial:** [Versioning policy](https://vercel.com/docs/rest-api) — Endpoints are individually versioned (v6, v13, ...); no single published deprecation policy found.
- **Unknown (help wanted):** `idempotency`, `automation_permitted`


## Help Wanted 🌱

The fastest way to contribute is to resolve an `unknown`: find official evidence, add the URL, open a PR. **142 unknowns are open right now.**

- `llms_txt` link unknown for: [brave-search](#brave-search), [gemini-api](#gemini-api), [github](#github), [hugging-face](#hugging-face), [openai](#openai), [resend](#resend)
- `openapi` link unknown for: [anthropic](#anthropic), [apify](#apify), [brave-search](#brave-search), [browserbase](#browserbase), [e2b](#e2b), [exa](#exa), [firecrawl](#firecrawl), [gemini-api](#gemini-api), [groq](#groq), [hugging-face](#hugging-face), [modal](#modal), [neon](#neon), [perplexity](#perplexity), [pinecone](#pinecone), [replicate](#replicate), [resend](#resend), [supabase](#supabase), [tavily](#tavily), [together-ai](#together-ai), [vercel](#vercel)
- `mcp_official` link unknown for: [anthropic](#anthropic), [brave-search](#brave-search), [gemini-api](#gemini-api), [groq](#groq), [modal](#modal), [openai](#openai), [replicate](#replicate), [together-ai](#together-ai)
- `agent_docs` link unknown for: [apify](#apify), [brave-search](#brave-search), [browserbase](#browserbase), [e2b](#e2b), [exa](#exa), [firecrawl](#firecrawl), [github](#github), [groq](#groq), [hugging-face](#hugging-face), [mongodb-atlas](#mongodb-atlas), [perplexity](#perplexity), [pinecone](#pinecone), [replicate](#replicate), [resend](#resend), [tavily](#tavily), [together-ai](#together-ai)

## Contributing

One fact = one contribution: report a broken link (2 min, [issue form](../../issues/new/choose)) · resolve an `unknown` (15 min) · add a provider (1–2 h, [inclusion rules](./docs/methodology.md#inclusion-rules)). CI validates everything mechanical with readable errors; humans only review evidence quality. Full guide: [`docs/contributing.md`](./docs/contributing.md).

Have a coding agent? Point it at a checkout of this repo and paste:

```text
Read AGENTS.md, then resolve one "unknown" check from the Help Wanted section of
README.md: find official evidence, update the provider YAML (or leave it unknown
if evidence is genuinely missing), run `npm run validate`, and open a small PR.
```

## Methodology

Facts only, evidence required, `unknown` is honest, freshness is tracked per check, links are probed weekly. Full write-up: [`docs/methodology.md`](./docs/methodology.md).

Related projects: [Fern Agent Score](https://buildwithfern.com/agent-score) and the [Agent-Friendly Docs Spec](https://github.com/fern-api/agent-score) (docs-site readiness scoring — we deliberately don't duplicate it), [Cloudflare Agent Readiness](https://blog.cloudflare.com/agent-readiness/), the [official MCP Registry](https://registry.modelcontextprotocol.io/) (authoritative MCP source we sync against), [llms.txt hub](https://llmstxthub.com/).

## License

Code: [MIT](./LICENSE) · Data (`data/`, `generated/`): [CC BY 4.0](./LICENSE-DATA)
