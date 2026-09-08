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

Browse the full collection below, grouped by primary category. Links show recorded access routes; task counts apply only to their recorded tasks and conditions. Legacy checks are labeled separately.

[AI Models](#services-ai-models) · [Agent Tooling](#services-agent-tooling) · [Code Execution](#services-code-execution) · [Developer Tools](#services-developer-tools) · [Cloud / Hosting](#services-cloud-hosting) · [Databases](#services-databases) · [Web Search / Data](#services-web-search-data) · [Payments / Billing](#services-payments-billing) · [Communication](#services-communication) · [Productivity / Storage](#services-productivity-storage) · [Observability / Security](#services-observability-security) · [Commerce / Marketing](#services-commerce-marketing) · [Travel](#services-travel)

<a id="services-ai-models"></a>

### AI Models (23)

- **[Alibaba Qwen (Model Studio)](https://www.alibabacloud.com/en/product/modelstudio)** — Qwen model family via Alibaba Cloud Model Studio's OpenAI-compatible API, with an official open-source coding CLI agent (qwen-code). [Docs](https://www.alibabacloud.com/help/en/model-studio/) · [API](https://www.alibabacloud.com/help/en/model-studio/models) · [CLI](https://github.com/QwenLM/qwen-code) · [Details](./generated/providers.md#qwen) · Not yet task-tested
- **[Anthropic](https://www.anthropic.com)** — Claude model APIs with agent-focused documentation, llms.txt, and the company behind the MCP standard itself. [Docs](https://docs.anthropic.com) · [API](https://docs.anthropic.com/en/api) · [CLI](https://docs.anthropic.com/en/docs/claude-code) · [Details](./generated/providers.md#anthropic) · Not yet task-tested
- **[Cartesia](https://cartesia.ai)** — Low-latency voice models (Sonic TTS, Ink STT) with a documented API, official MCP server, llms.txt, and a free tier. [Docs](https://docs.cartesia.ai) · [API](https://docs.cartesia.ai/api-reference) · [MCP](https://github.com/cartesia-ai/cartesia-mcp) · [Details](./generated/providers.md#cartesia) · Not yet task-tested
- **[Cerebras Inference](https://cloud.cerebras.ai)** — Wafer-scale inference for open models at very high tokens/sec, OpenAI-compatible API, llms.txt, and a standing free tier. [Docs](https://inference-docs.cerebras.ai) · [API](https://inference-docs.cerebras.ai/api-reference/chat-completions) · [Details](./generated/providers.md#cerebras) · Not yet task-tested
- **[Cohere](https://cohere.com)** — Enterprise LLM platform (command, embed, rerank) with llms.txt, documented API versioning, free trial keys, and error/rate-limit docs. [Docs](https://docs.cohere.com) · [API](https://docs.cohere.com/reference/about) · [Details](./generated/providers.md#cohere) · Not yet task-tested
- **[Deepgram](https://deepgram.com)** — Speech-to-text and voice AI API with a public OpenAPI spec, llms.txt, scoped API keys, and $200 free credit without a card. [Docs](https://developers.deepgram.com/docs) · [API](https://developers.deepgram.com/reference) · [Details](./generated/providers.md#deepgram) · Not yet task-tested
- **[DeepSeek](https://www.deepseek.com)** — OpenAI-compatible LLM API (DeepSeek-V3/R1) with transparent per-token pricing, a detailed changelog, and self-serve keys. [Docs](https://api-docs.deepseek.com) · [Details](./generated/providers.md#deepseek) · Not yet task-tested
- **[ElevenLabs](https://elevenlabs.io)** — Voice AI (TTS, STT, agents) with a public OpenAPI spec, llms.txt, an official MCP server, and a free tier. [Docs](https://elevenlabs.io/docs) · [API](https://elevenlabs.io/docs/api-reference/introduction) · [MCP](https://github.com/elevenlabs/elevenlabs-mcp) · [Details](./generated/providers.md#elevenlabs) · Not yet task-tested
- **[fal.ai](https://fal.ai)** — Generative media platform (image, video, audio models) with queue/streaming APIs, an official CLI/serving framework, llms.txt, and self-serve keys. [Docs](https://fal.ai/docs) · [API](https://fal.ai/docs/model-apis) · [CLI](https://github.com/fal-ai/fal) · [Details](./generated/providers.md#fal) · Not yet task-tested
- **[Fireworks AI](https://fireworks.ai)** — Fast open-model inference and fine-tuning with an OpenAI-compatible API, official firectl CLI, llms.txt, and published pricing. [Docs](https://docs.fireworks.ai) · [API](https://docs.fireworks.ai/api-reference/introduction) · [CLI](https://docs.fireworks.ai/tools-sdks/firectl/firectl) · [Details](./generated/providers.md#fireworks) · Not yet task-tested
- **[Gemini API](https://ai.google.dev)** — Google's Gemini model APIs via AI Studio, with generous free tier and documented API versioning. [Docs](https://ai.google.dev/gemini-api/docs) · [API](https://ai.google.dev/api) · [CLI](https://github.com/google-gemini/gemini-cli) · [Details](./generated/providers.md#gemini-api) · Not yet task-tested
- **[Groq](https://groq.com)** — Ultra-low-latency LLM inference with an OpenAI-compatible API, llms.txt, and self-serve keys with a free tier. [Docs](https://console.groq.com/docs) · [API](https://console.groq.com/docs/api-reference) · [Details](./generated/providers.md#groq) · Not yet task-tested
- **[Hugging Face](https://huggingface.co)** — Model hub and inference platform with fine-grained tokens, OAuth, an official MCP server, and a full Hub API. [Docs](https://huggingface.co/docs) · [API](https://huggingface.co/docs/hub/api) · [MCP](https://huggingface.co/mcp) · [CLI](https://huggingface.co/docs/huggingface_hub/guides/cli) · [Details](./generated/providers.md#hugging-face) · Not yet task-tested
- **[Luma AI (Dream Machine)](https://lumalabs.ai)** — Dream Machine video and image generation via the Luma API, with llms.txt and published API pricing. [Docs](https://docs.lumalabs.ai) · [API](https://docs.lumalabs.ai/reference) · [Details](./generated/providers.md#luma) · Not yet task-tested
- **[MiniMax](https://platform.minimax.io)** — MiniMax text, speech, video and music models via the international platform API, with an official MCP server. [Docs](https://platform.minimax.io/docs) · [API](https://platform.minimax.io/docs/api-reference) · [MCP](https://github.com/MiniMax-AI/MiniMax-MCP) · [Details](./generated/providers.md#minimax) · Not yet task-tested
- **[Mistral AI](https://mistral.ai)** — European LLM provider (La Plateforme) with llms.txt, an open OpenAPI-based docs repo, a free experiment tier, and self-serve keys. [Docs](https://docs.mistral.ai) · [API](https://docs.mistral.ai/api) · [Details](./generated/providers.md#mistral) · Not yet task-tested
- **[Moonshot AI (Kimi)](https://platform.kimi.ai)** — Kimi models (K2 line) via an OpenAI-compatible API on the international Kimi platform, with an official terminal CLI agent (kimi-cli). [Docs](https://platform.kimi.ai/docs) · [API](https://platform.kimi.ai/docs/api/chat) · [CLI](https://github.com/MoonshotAI/kimi-cli) · [Details](./generated/providers.md#moonshot) · Not yet task-tested
- **[OpenAI](https://openai.com)** — GPT model APIs with an official OpenAPI spec, agents guides, and a large SDK ecosystem. [Docs](https://developers.openai.com/api/docs) · [API](https://platform.openai.com/docs/api-reference) · [Details](./generated/providers.md#openai) · Not yet task-tested
- **[OpenRouter](https://openrouter.ai)** — Unified OpenAI-compatible API over hundreds of models from many labs, with one key, per-model pricing, automatic fallbacks, and an llms.txt. [Docs](https://openrouter.ai/docs) · [API](https://openrouter.ai/docs/api-reference/overview) · [Details](./generated/providers.md#openrouter) · Not yet task-tested
- **[Replicate](https://replicate.com)** — Run and fine-tune open-source models via a simple predictions API, with llms.txt, webhooks, and an official CLI. [Docs](https://replicate.com/docs) · [API](https://replicate.com/docs/reference/http) · [CLI](https://github.com/replicate/cli) · [Details](./generated/providers.md#replicate) · Not yet task-tested
- **[Together AI](https://www.together.ai)** — Inference and fine-tuning platform for open-source models with an OpenAI-compatible API and llms.txt. [Docs](https://docs.together.ai) · [API](https://docs.together.ai/reference/chat-completions) · [Details](./generated/providers.md#together-ai) · Not yet task-tested
- **[xAI (Grok API)](https://x.ai)** — xAI's Grok models via an OpenAI-compatible REST API, with an llms.txt and self-serve console keys. [Docs](https://docs.x.ai) · [API](https://docs.x.ai/developers/rest-api-reference/inference) · [Details](./generated/providers.md#xai) · Not yet task-tested
- **[Z.ai (GLM)](https://z.ai)** — GLM models via Z.ai's OpenAI-compatible international API, with llms.txt, published pricing, and self-serve keys. [Docs](https://docs.z.ai) · [API](https://docs.z.ai/api-reference) · [Details](./generated/providers.md#zai) · Not yet task-tested

<a id="services-agent-tooling"></a>

### Agent Tooling (5)

- **[Composio](https://composio.dev)** — Tool and integration layer for AI agents (hundreds of app connectors with managed auth), with llms.txt and a hosted MCP directory. [Docs](https://docs.composio.dev) · [MCP](https://mcp.composio.dev) · [Details](./generated/providers.md#composio) · Not yet task-tested
- **[Mem0](https://mem0.ai)** — Memory layer for AI agents (hosted platform + open-source), with REST API, llms.txt, and the official OpenMemory MCP server. [Docs](https://docs.mem0.ai) · [API](https://docs.mem0.ai/api-reference) · [MCP](https://docs.mem0.ai/openmemory/overview) · [Details](./generated/providers.md#mem0) · Not yet task-tested
- **[n8n](https://n8n.io)** — Workflow automation platform with native AI/agent nodes, a public REST API, official hosted MCP server, CLI, and llms.txt; fair-code and self-hostable. [Docs](https://docs.n8n.io) · [API](https://docs.n8n.io/api/) · [MCP](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) · [CLI](https://docs.n8n.io/hosting/cli-commands/) · [Details](./generated/providers.md#n8n) · Not yet task-tested
- **[Vapi](https://vapi.ai)** — Voice-agent orchestration API (calls, turn-taking, tool use over phone/web) with an official MCP server and an llms.txt that opens with instructions for AI agents. [Docs](https://docs.vapi.ai) · [API](https://docs.vapi.ai/api-reference) · [MCP](https://github.com/VapiAI/mcp-server) · [Details](./generated/providers.md#vapi) · Not yet task-tested
- **[Zapier](https://zapier.com)** — Automation platform bridging 7000+ apps, with llms.txt and an official MCP endpoint that gives agents access to those integrations. [Docs](https://docs.zapier.com) · [MCP](https://zapier.com/mcp) · [CLI](https://github.com/zapier/zapier-platform) · [Details](./generated/providers.md#zapier) · Not yet task-tested

<a id="services-code-execution"></a>

### Code Execution (4)

- **[Browserbase](https://www.browserbase.com)** — Headless browser infrastructure for AI agents and automation, with session APIs and an official MCP server. [Docs](https://docs.browserbase.com) · [API](https://docs.browserbase.com/reference) · [MCP](https://github.com/browserbase/mcp-server-browserbase) · [Details](./generated/providers.md#browserbase) · Not yet task-tested
- **[E2B](https://e2b.dev)** — Isolated cloud sandboxes for running AI-generated code, with llms.txt, an official MCP server, and self-serve keys. [Docs](https://e2b.dev/docs) · [MCP](https://github.com/e2b-dev/mcp-server) · [CLI](https://e2b.dev/docs/cli) · [Details](./generated/providers.md#e2b) · Not yet task-tested
- **[Modal](https://modal.com)** — Serverless compute for Python with first-class Sandboxes for agent code execution, llms.txt, and an official CLI. [Docs](https://modal.com/docs) · [API](https://modal.com/docs/reference) · [CLI](https://modal.com/docs/reference/cli) · [Details](./generated/providers.md#modal) · Not yet task-tested
- **[Steel](https://steel.dev)** — Cloud browser API for AI agents (sessions, CDP, anti-bot) — open-source and self-hostable, with llms.txt and a free tier. [Docs](https://docs.steel.dev) · [API](https://docs.steel.dev/api-reference) · [Details](./generated/providers.md#steel) · Not yet task-tested

<a id="services-developer-tools"></a>

### Developer Tools (4)

- **[Atlassian (Jira & Confluence)](https://www.atlassian.com)** — Jira, Confluence and the Atlassian Cloud platform — REST APIs, an official remote MCP server (OAuth 2.1), and the acli CLI. [Docs](https://developer.atlassian.com) · [API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/) · [MCP](https://github.com/atlassian/atlassian-mcp-server) · [CLI](https://developer.atlassian.com/cloud/acli/) · [Details](./generated/providers.md#atlassian) · Not yet task-tested
- **[GitHub](https://github.com)** — Code hosting, collaboration, and automation with REST and GraphQL APIs, an official CLI, and an official MCP server. [Docs](https://docs.github.com) · [API](https://docs.github.com/rest) · [MCP](https://github.com/github/github-mcp-server) · [CLI](https://cli.github.com) · [Details](./generated/providers.md#github) · [Legacy trials](./generated/agent-runs.md#github)
- **[GitLab](https://gitlab.com)** — DevOps platform with REST and GraphQL APIs, scoped tokens, llms.txt, and an official CLI. [Docs](https://docs.gitlab.com) · [API](https://docs.gitlab.com/api/rest/) · [MCP](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server) · [CLI](https://gitlab.com/gitlab-org/cli) · [Details](./generated/providers.md#gitlab) · Not yet task-tested
- **[Postman](https://www.postman.com)** — API development platform with a public Postman API, llms.txt, official CLI, and self-serve keys. [Docs](https://learning.postman.com) · [API](https://learning.postman.com/docs/developer/postman-api/intro-api/) · [MCP](https://github.com/postmanlabs/postman-mcp-server) · [CLI](https://learning.postman.com/docs/postman-cli/postman-cli-overview/) · [Details](./generated/providers.md#postman) · Not yet task-tested

<a id="services-cloud-hosting"></a>

### Cloud / Hosting (6)

- **[Cloudflare](https://www.cloudflare.com)** — Edge network, Workers serverless platform, storage, and AI services with agent-focused docs and official MCP servers. [CLI](https://developers.cloudflare.com/d1/get-started/) · [Details](./generated/providers.md#cloudflare) · Not yet task-tested
- **[Fly.io](https://fly.io)** — Run full-stack apps and machines close to users, with a spec'd Machines API, scoped macaroon tokens, and official MCP docs. [Docs](https://fly.io/docs) · [API](https://fly.io/docs/machines/api/) · [MCP](https://fly.io/docs/mcp/) · [CLI](https://fly.io/docs/flyctl/) · [Details](./generated/providers.md#fly-io) · Not yet task-tested
- **[Netlify](https://www.netlify.com)** — Web platform for deploying sites and functions, with an OpenAPI-specified API, llms.txt, official CLI and MCP server. [Docs](https://docs.netlify.com) · [API](https://open-api.netlify.com) · [MCP](https://docs.netlify.com/welcome/build-with-ai/netlify-mcp-server/) · [CLI](https://docs.netlify.com/cli/get-started/) · [Details](./generated/providers.md#netlify) · Not yet task-tested
- **[Railway](https://railway.com)** — App/database hosting with a public GraphQL API, official CLI, llms.txt, and usage-based pricing. [Docs](https://docs.railway.com) · [API](https://docs.railway.com/reference/public-api) · [CLI](https://github.com/railwayapp/cli) · [Details](./generated/providers.md#railway) · Not yet task-tested
- **[Render](https://render.com)** — Cloud hosting for web services, static sites and databases with a REST API, official CLI, official MCP server, and llms.txt. [Docs](https://render.com/docs) · [API](https://api-docs.render.com/reference/introduction) · [MCP](https://github.com/render-oss/render-mcp-server) · [CLI](https://github.com/render-oss/cli) · [Details](./generated/providers.md#render) · Not yet task-tested
- **[Vercel](https://vercel.com)** — Frontend cloud for deploying web apps, with a REST API, CLI, official MCP server, and AI SDK ecosystem. [Docs](https://vercel.com/docs) · [API](https://vercel.com/docs/rest-api) · [MCP](https://vercel.com/docs/mcp/vercel-mcp) · [CLI](https://vercel.com/docs/cli) · [Details](./generated/providers.md#vercel) · Not yet task-tested

<a id="services-databases"></a>

### Databases (12)

- **[Aiven](https://aiven.io/)** — Managed databases including free hosted PostgreSQL. Account signup and provisioning remain untested; free lifecycle limits need checking before production use. [CLI](https://aiven.io/docs/tools/cli) · [Details](./data/candidates/aiven.yaml) · Not yet task-tested
- **[Chroma](https://www.trychroma.com)** — Open-source embedding database with a hosted Chroma Cloud, official CLI, official MCP server, and llms.txt. [Docs](https://docs.trychroma.com) · [API](https://docs.trychroma.com/docs/overview/introduction) · [MCP](https://github.com/chroma-core/chroma-mcp) · [CLI](https://docs.trychroma.com/docs/cli/install) · [Details](./generated/providers.md#chroma) · Not yet task-tested
- **[MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-database)** — Managed MongoDB with a versioned Admin API, published OpenAPI spec, llms.txt, official CLI and MCP server. [Docs](https://www.mongodb.com/docs/atlas/) · [API](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/) · [MCP](https://github.com/mongodb-js/mongodb-mcp-server) · [CLI](https://www.mongodb.com/docs/atlas/cli/) · [Details](./generated/providers.md#mongodb-atlas) · Not yet task-tested
- **[Neon](https://neon.com)** — Serverless Postgres with instant branching, a full management API, official MCP server, and agent-oriented docs. [API](https://neon.new/) · [Details](./generated/providers.md#neon) · [1 completed](./generated/evaluations.md)
- **[Pinecone](https://www.pinecone.io)** — Managed vector database for search and RAG, with llms.txt, an official MCP server, and self-serve keys. [Docs](https://docs.pinecone.io) · [API](https://docs.pinecone.io/reference/api/introduction) · [MCP](https://docs.pinecone.io/guides/operations/mcp-server) · [CLI](https://github.com/pinecone-io/cli) · [Details](./generated/providers.md#pinecone) · Not yet task-tested
- **[PlanetScale](https://planetscale.com/)** — PostgreSQL single-node plans start at USD 5/month. No free writable database allowance verified; not provisioned in this no-payment round. Public pricing SQL is read-only and does not meet the task. [CLI](https://planetscale.com/docs/cli) · [Details](./data/candidates/planetscale.yaml) · Not yet task-tested
- **[Qdrant](https://qdrant.tech)** — Open-source vector database with a managed cloud, llms.txt, an official MCP server, and a free cluster tier. [Docs](https://qdrant.tech/documentation) · [API](https://api.qdrant.tech) · [MCP](https://github.com/qdrant/mcp-server-qdrant) · [Details](./generated/providers.md#qdrant) · Not yet task-tested
- **[Redis (Redis Cloud)](https://redis.io)** — In-memory data platform for caching, vector search and real-time apps; Redis Cloud has a REST management API, official MCP server, redis-cli, and llms.txt. [Docs](https://redis.io/docs/latest) · [API](https://redis.io/docs/latest/operate/rc/api/) · [MCP](https://github.com/redis/mcp-redis) · [CLI](https://redis.io/docs/latest/develop/tools/cli/) · [Details](./generated/providers.md#redis) · Not yet task-tested
- **[Supabase](https://supabase.com)** — Postgres platform with auth, storage, edge functions, a management API, official MCP server, and LLM-ready docs. [API](https://supabase.com/docs/guides/api) · [Details](./generated/providers.md#supabase) · Not yet task-tested
- **[Turso](https://turso.tech/)** — Free cloud account: 100 databases, 5 GB, 500 million reads/month and 10 million writes/month. Signup/login required; local engine alone does not satisfy remote storage. [CLI](https://docs.turso.tech/cli/introduction) · [API](https://docs.turso.tech/api-reference/introduction) · [Details](./data/candidates/turso.yaml) · [1 completed](./generated/evaluations.md)
- **[Upstash](https://upstash.com)** — Serverless Redis, Kafka-successor queues, and vector storage with REST APIs, llms.txt, an official MCP server, and a free tier. [Docs](https://upstash.com/docs) · [API](https://upstash.com/docs/devops/developer-api/introduction) · [MCP](https://github.com/upstash/mcp-server) · [CLI](https://github.com/upstash/cli) · [Details](./generated/providers.md#upstash) · Not yet task-tested
- **[Weaviate](https://weaviate.io)** — Open-source vector database with REST/GraphQL/gRPC APIs, Weaviate Cloud free sandboxes, an official CLI, MCP server, and llms.txt. [Docs](https://docs.weaviate.io) · [API](https://docs.weaviate.io/weaviate/api/rest) · [MCP](https://github.com/weaviate/mcp-server-weaviate) · [CLI](https://github.com/weaviate/weaviate-cli) · [Details](./generated/providers.md#weaviate) · Not yet task-tested

<a id="services-web-search-data"></a>

### Web Search / Data (10)

- **[Apify](https://apify.com)** — Web scraping and automation platform with thousands of ready-made actors, a versioned API, llms.txt, and an official MCP server. [Docs](https://docs.apify.com) · [API](https://docs.apify.com/api/v2) · [MCP](https://docs.apify.com/platform/integrations/mcp) · [CLI](https://docs.apify.com/cli) · [Details](./generated/providers.md#apify) · Not yet task-tested
- **[Brave Search API](https://brave.com/search/api/)** — Independent web search index with a developer API, self-serve registration, and a free plan. [API](https://brave.com/search/api/) · [Details](./generated/providers.md#brave-search) · Not yet task-tested
- **[Exa](https://exa.ai)** — Search API built for AI — semantic web search, content retrieval, and research endpoints with an official MCP server. [MCP](https://mcp.exa.ai/mcp) · [API](https://exa.ai/docs/reference/search) · [Details](./generated/providers.md#exa) · [1 completed / 1 not completed](./generated/evaluations.md)
- **[Firecrawl](https://www.firecrawl.dev)** — Web scraping and crawling API that turns websites into LLM-ready markdown, with an official MCP server. [API: account-search-api](https://docs.firecrawl.dev/features/search) · [Details](./generated/providers.md#firecrawl) · [1 completed](./generated/evaluations.md)
- **[Jina AI](https://jina.ai)** — Search-foundation APIs (Reader for URL-to-markdown, embeddings, reranker, deep search) with an official remote MCP server, an agent-targeted llms.txt, and a keyless trial path. [API](https://docs.jina.ai) · [MCP](https://github.com/jina-ai/MCP) · [Details](./generated/providers.md#jina) · Not yet task-tested
- **[Perplexity API](https://www.perplexity.ai)** — Sonar API for web-grounded answers and search, with llms.txt, an official MCP server, and documented usage tiers. [Docs](https://docs.perplexity.ai) · [MCP](https://github.com/ppl-ai/modelcontextprotocol) · [Details](./generated/providers.md#perplexity) · Not yet task-tested
- **[SerpApi](https://serpapi.com)** — Real-time JSON API for Google and other search engines' results, with an official MCP server, llms.txt, and a free monthly quota. [API: google-flights-api](https://serpapi.com/google-flights-api) · [MCP](https://github.com/serpapi/serpapi-mcp) · [API: web-search-api](https://serpapi.com/search-api) · [Details](./generated/providers.md#serpapi) · Not yet task-tested
- **[Serper](https://serper.dev/)** — Google results API with signup trial queries; actual account flow and authentication remain untested. [API](https://serper.dev/) · [Details](./data/candidates/serper.yaml) · Not yet task-tested
- **[Tavily](https://www.tavily.com)** — Search and extraction API built for AI agents, with llms.txt, an official MCP server, and a free tier. [API](https://docs.tavily.com/documentation/quickstart) · [Details](./generated/providers.md#tavily) · Not yet task-tested
- **[Xquik](https://xquik.com)** — Hosted X data and account automation service with a REST API, official MCP server, OpenAPI, SDKs, HMAC webhooks, and OAuth 2.1. [Docs](https://docs.xquik.com) · [API](https://docs.xquik.com/api-reference/overview) · [MCP](https://docs.xquik.com/mcp/overview) · [Details](./data/candidates/xquik.yaml) · [Legacy first-call check](./data/experiments/published/xquik/2026-07-15-dry-fire-rep3.md)

<a id="services-payments-billing"></a>

### Payments / Billing (4)

- **[Lemon Squeezy](https://www.lemonsqueezy.com)** — Merchant-of-record payments for digital products/SaaS with a JSON:API REST API, documented test mode, and self-serve keys. [Docs](https://docs.lemonsqueezy.com) · [API](https://docs.lemonsqueezy.com/api) · [Details](./generated/providers.md#lemonsqueezy) · Not yet task-tested
- **[paas.build](https://paas.build)** — Agent-native payment facilitator (the AI-builder product of UniPaaS, FCA-authorised No. 929994) — opens a real merchant account via progressive KYB and creates checkouts through MCP or REST. [Docs](https://paas.build/agents) · [MCP](https://github.com/UNIPaaS/paas-build-mcp) · [Details](./data/candidates/paas-build.yaml) · [Legacy first-call check](./data/experiments/published/paas-build/2026-07-15-dry-fire-rep3.md)
- **[Paddle](https://www.paddle.com)** — Merchant-of-record billing platform with a versioned API, full sandbox, llms.txt, and webhooks. [Docs](https://developer.paddle.com) · [API](https://developer.paddle.com/api-reference/overview) · [MCP](https://github.com/PaddleHQ/paddle-mcp-server) · [Details](./generated/providers.md#paddle) · Not yet task-tested
- **[Stripe](https://stripe.com)** — Payments, billing, subscriptions, and financial infrastructure with a famously complete API surface. [Docs](https://docs.stripe.com) · [API](https://docs.stripe.com/api) · [MCP](https://docs.stripe.com/mcp) · [CLI](https://docs.stripe.com/stripe-cli) · [Details](./generated/providers.md#stripe) · Not yet task-tested

<a id="services-communication"></a>

### Communication (6)

- **[Discord](https://discord.com)** — Chat platform with a versioned bot/OAuth2 API, official OpenAPI spec (preview), webhooks, and documented rate limits. [Docs](https://discord.com/developers/docs/intro) · [API](https://discord.com/developers/docs/reference) · [Details](./generated/providers.md#discord) · Not yet task-tested
- **[Lark](https://www.larksuite.com)** — Collaboration suite (messaging, docs, calendar) with an open platform, llms.txt, an official CLI with 200+ commands and agent skills, and an official OpenAPI MCP server. [API](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create) · [CLI](https://github.com/larksuite/cli) · [MCP](https://github.com/larksuite/lark-openapi-mcp) · [Details](./generated/providers.md#lark) · Not yet task-tested
- **[Resend](https://resend.com)** — Email API for developers with test mode, scoped API keys, idempotency support, and an official MCP server. [Docs](https://resend.com/docs) · [API](https://resend.com/docs/api-reference/introduction) · [MCP](https://github.com/resend/mcp-send-email) · [Details](./generated/providers.md#resend) · Not yet task-tested
- **[Slack](https://slack.com)** — Workspace messaging platform with a mature Web API, granular OAuth scopes, an OpenAPI spec, and llms.txt. [Docs](https://api.slack.com) · [API](https://api.slack.com/methods) · [CLI](https://docs.slack.dev/tools/slack-cli) · [Details](./generated/providers.md#slack) · Not yet task-tested
- **[Telegram Bot API](https://telegram.org)** — Free bot platform with instant token issuance via BotFather, webhooks, a documented test environment, and a detailed changelog. [Docs](https://core.telegram.org/bots) · [API](https://core.telegram.org/bots/api) · [Details](./generated/providers.md#telegram) · Not yet task-tested
- **[Twilio](https://www.twilio.com)** — Programmable messaging and voice APIs with test credentials, an OpenAPI spec, llms.txt, and an official CLI. [Docs](https://www.twilio.com/docs) · [API](https://www.twilio.com/docs/usage/api) · [MCP](https://github.com/twilio-labs/mcp) · [CLI](https://www.twilio.com/docs/twilio-cli) · [Details](./generated/providers.md#twilio) · Not yet task-tested

<a id="services-productivity-storage"></a>

### Productivity / Storage (9)

- **[Airtable](https://www.airtable.com)** — Spreadsheet-database hybrid with a REST API, scoped personal access tokens, OAuth, webhooks, and documented rate limits. [API](https://airtable.com/developers/web/api/introduction) · [Details](./generated/providers.md#airtable) · Not yet task-tested
- **[Baserow Cloud](https://baserow.io/)** — Hosted collaborative tables; free workspace and scoped row-access tokens. Schema management uses a different credential. [API](https://baserow.io/docs/apis/rest-api) · [MCP](https://baserow.io/user-docs/mcp-server) · [Details](./data/candidates/baserow.yaml) · Not yet task-tested
- **[Coda / Superhuman Docs](https://coda.io/)** — Docs and tables with a free REST API; current API page is branded Superhuman Docs. [API](https://coda.io/developers/apis/v1) · [MCP](https://coda.io/apis/mcp) · [Details](./data/candidates/coda.yaml) · Not yet task-tested
- **[Dropbox](https://www.dropbox.com)** — File storage and sync with a scoped-OAuth HTTP API, self-serve app creation, and webhooks. [Docs](https://www.dropbox.com/developers/documentation) · [API](https://www.dropbox.com/developers/documentation/http/documentation) · [CLI](https://github.com/dropbox/dbxcli) · [Details](./generated/providers.md#dropbox) · Not yet task-tested
- **[Google Sheets](https://workspace.google.com/products/sheets/)** — Online spreadsheets with a no-additional-cost API; Cloud project and OAuth setup are still prerequisites. [API](https://developers.google.com/workspace/sheets/api/guides/concepts) · [Details](./data/candidates/google-sheets.yaml) · Not yet task-tested
- **[Grist](https://www.getgrist.com/)** — Hosted relational spreadsheets with a free personal site, REST API and official MCP. [API](https://support.getgrist.com/api/) · [MCP](https://docs.getgrist.com/api/mcp) · [SDK: python-sdk](https://pypi.org/project/grist-api/) · [SDK: javascript-sdk](https://www.npmjs.com/package/grist-api) · [Details](./data/candidates/grist.yaml) · [2 completed](./generated/evaluations.md)
- **[Linear](https://linear.app)** — Issue tracking and product planning with a GraphQL API, llms.txt, an official MCP server, and webhooks. [Docs](https://linear.app/developers) · [MCP](https://linear.app/docs/mcp) · [Details](./generated/providers.md#linear) · Not yet task-tested
- **[Notion](https://www.notion.com)** — Connected workspace with a versioned REST API, capability-scoped integrations, llms.txt, and an official MCP server. [API](https://developers.notion.com/reference/intro) · [SDK](https://github.com/makenotion/notion-sdk-js) · [CLI](https://developers.notion.com/cli/get-started/overview) · [MCP](https://mcp.notion.com/mcp) · [Details](./generated/providers.md#notion) · [2 completed](./generated/evaluations.md)
- **[飞书 Feishu](https://www.feishu.cn/)** — China-region Feishu workspace and Base APIs; separate account/tenant from international Lark. [API](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/create) · [CLI](https://github.com/larksuite/cli) · [MCP](https://github.com/larksuite/lark-openapi-mcp) · [Details](./data/candidates/feishu.yaml) · Not yet task-tested

<a id="services-observability-security"></a>

### Observability / Security (3)

- **[Datadog](https://www.datadoghq.com)** — Observability platform with a full REST API, llms.txt, documented OAuth for integrations, rate limits, and webhooks. [Docs](https://docs.datadoghq.com) · [API](https://docs.datadoghq.com/api/latest/) · [MCP](https://docs.datadoghq.com/bits_ai/mcp_server) · [CLI](https://github.com/DataDog/datadog-ci) · [Details](./generated/providers.md#datadog) · Not yet task-tested
- **[Grafana (Grafana Cloud)](https://grafana.com)** — Observability platform (dashboards, metrics, logs, traces) with a documented HTTP API, official MCP server, llms.txt, and a standing free cloud tier. [Docs](https://grafana.com/docs) · [API](https://grafana.com/docs/grafana/latest/developers/http_api/) · [MCP](https://github.com/grafana/mcp-grafana) · [Details](./generated/providers.md#grafana) · Not yet task-tested
- **[Sentry](https://sentry.io)** — Error monitoring and performance tracing with llms.txt, an official MCP server, scoped auth tokens, and a full API. [Docs](https://docs.sentry.io) · [API](https://docs.sentry.io/api/) · [MCP](https://docs.sentry.io/product/sentry-mcp/) · [CLI](https://docs.sentry.io/cli/) · [Details](./generated/providers.md#sentry) · Not yet task-tested

<a id="services-commerce-marketing"></a>

### Commerce / Marketing (1)

- **[Shopify](https://www.shopify.com)** — Commerce platform with versioned GraphQL APIs, llms.txt, official MCP docs, access-scoped tokens, free development stores, and a CLI. [Docs](https://shopify.dev/docs) · [API](https://shopify.dev/docs/api) · [MCP](https://shopify.dev/docs/apps/build/storefront-mcp) · [CLI](https://shopify.dev/docs/api/shopify-cli) · [Details](./generated/providers.md#shopify) · Not yet task-tested

<a id="services-travel"></a>

### Travel (25)

- **[AirGateway Platform API](https://airgateway.com/)** — Air distribution API with sandbox keys, production certification and an agency application. [API](https://support.airgateway.com/en-US/kb/article/4/introduction-to-airgateway-platform-api) · [Details](./data/candidates/airgateway.yaml) · Not yet task-tested
- **[Amadeus Flight APIs](https://developers.amadeus.com/)** — Historical Self-Service flight API and the current Enterprise portal; individual onboarding must be re-established. [API: former-self-service](https://developers.amadeus.com/blog/comparing-open-source-flight-data-sources) · [API: enterprise-api](https://developers.amadeus.com/) · [Details](./data/candidates/amadeus-flights.yaml) · Not yet task-tested
- **[apiheya Air Scraper](https://rapidapi.com/apiheya/api/sky-scrapper/pricing)** — An apiheya flight-data product distributed through RapidAPI; distinct from the official Skyscanner partner API. [API](https://rapidapi.com/apiheya/api/sky-scrapper/playground/apiendpoint_6856e0a6-2804-43cd-9cc0-bb377022981e) · [Details](./data/candidates/apiheya-air-scraper.yaml) · Not yet task-tested
- **[Aviasales via Travelpayouts](https://www.aviasales.com/)** — Travelpayouts-distributed live flight search and a separately accessible historical price-data API. [API: live-search-api](https://support.travelpayouts.com/hc/en-us/articles/210995808-How-to-get-access-to-the-Aviasales-Search-API) · [API: cached-data-api](https://support.travelpayouts.com/hc/en-us/articles/203956163-Aviasales-Data-API) · [Details](./data/candidates/aviasales.yaml) · Not yet task-tested
- **[Bright Data SERP API](https://brightdata.com/)** — SERP API with a documented Google Flights request; structured fare extraction and onboarding need verification. [API](https://docs.brightdata.com/api-reference/serp/google-flights/currency) · [Details](./data/candidates/bright-data-serp.yaml) · Not yet task-tested
- **[Duffel Flights API](https://duffel.com/)** — Flight API whose self-serve test environment must be distinguished from live account activation. [API: test-api](https://duffel.com/docs/api/overview/test-mode) · [API: live-api](https://duffel.com/guides/getting-started) · [Details](./data/candidates/duffel-flights.yaml) · Not yet task-tested
- **[Expedia XAP Flight Listings](https://developers.expediagroup.com/xap-apis/api/start-guide/getting-started)** — Travel Redirect/XAP flight listings product whose new API applications are currently paused. [API](https://developers.expediagroup.com/xap-apis/api/shopping-apis/flight-listings) · [Details](./data/candidates/expedia-xap-flights.yaml) · Not yet task-tested
- **[Flight MCP](https://flight-mcp.com/)** — Authenticated flight lookup and a separate, restricted public cache exposed through REST and MCP. [MCP: public-cache-mcp](https://flight-mcp.com/docs) · [Details](./data/candidates/flight-mcp.yaml) · Not yet task-tested
- **[FlightAPI.io Flight Price API](https://www.flightapi.io/)** — Flight-price search for one-way, round-trip and multi-city itineraries, with credit-based usage. [API](https://www.flightapi.io/documentation/) · [Details](./data/candidates/flightapi-io.yaml) · Not yet task-tested
- **[Ignav Flights](https://ignav.com/)** — Flight search and purchase-link API with email signup and an official MCP; individual eligibility remains untested. [WEB](https://ignav.com/playground) · [API](https://ignav.com/docs) · [MCP](https://ignav.com/docs/mcp) · [Details](./data/candidates/ignav.yaml) · [1 completed](./generated/evaluations.md)
- **[KAYAK Affiliate API](https://affiliates.kayak.com/)** — Affiliate flight APIs with a business application and an optional requested sandbox. [API](https://developers.kayak.com/) · [Details](./data/candidates/kayak-affiliate.yaml) · Not yet task-tested
- **[Kiwi.com](https://www.kiwi.com/)** — Flight search through a publicized MCP path and the separately gated Tequila partnership API. [MCP](https://mcp.kiwi.com) · [API](https://media.kiwi.com/articles-and-interviews/better-for-business-kiwi-com-takes-a-new-approach-to-partnerships/) · [Details](./data/candidates/kiwi.yaml) · [2 completed / 1 invalid environment](./generated/evaluations.md)
- **[LetsFG Personal Flight Search](https://letsfg.co/)** — Personal flight search through MCP, CLI and SDKs, with a human payment-method authorization step. [MCP](https://letsfg.co/for-agents) · [SDK](https://github.com/letsfg/letsfg) · [Details](./data/candidates/letsfg.yaml) · Not yet task-tested
- **[Lufthansa Partner Fare API](https://developer.lufthansa.com/page)** — Lufthansa fare methods are partner-scoped; the developer portal currently pauses new Open API registrations. [API: open-api-registration](https://developer.lufthansa.com/page) · [API: partner-offers-api](https://developer.lufthansa.com/docs/read/api_partner/offers) · [Details](./data/candidates/lufthansa-partner.yaml) · Not yet task-tested
- **[Sabre Air APIs](https://developer.sabre.com/)** — Air API workflows with assigned credentials, plus a separately researched Agentic API/MCP lead. [API](https://github.com/SabreDevStudio/SabreAPIsWorkflows/blob/master/SabreAPIsTestSuites/README.md) · [MCP](https://developer.sabre.com/) · [Details](./data/candidates/sabre-air.yaml) · Not yet task-tested
- **[Scrapingdog Google Flights API](https://www.scrapingdog.com/)** — Google Flights extraction endpoint charged in platform credits rather than one credit per flight search. [API](https://www.scrapingdog.com/documentation/google-flights-api/) · [Details](./data/candidates/scrapingdog-flights.yaml) · Not yet task-tested
- **[SearchApi Google Flights](https://www.searchapi.io/)** — Google Flights extraction API and a hosted MCP integration supporting token or browser authorization. [API](https://www.searchapi.io/docs/google-flights-api) · [MCP](https://www.searchapi.io/mcp) · [Details](./data/candidates/searchapi.yaml) · Not yet task-tested
- **[Skootle Google Flights Scraper](https://apify.com/skootle/google-flights-scraper)** — A Skootle-published flight-scraping Actor hosted on Apify, billed by startup and output records. [API](https://apify.com/skootle/google-flights-scraper) · [Details](./data/candidates/skootle-google-flights.yaml) · Not yet task-tested
- **[Skyscanner Travel APIs](https://www.skyscanner.net/)** — Partner flight APIs and an official MCP, with independently documented business-access paths. [API](https://developers.skyscanner.net/docs/getting-started/authentication) · [MCP](https://developers.skyscanner.net/docs/mcp-server) · [Details](./data/candidates/skyscanner.yaml) · Not yet task-tested
- **[Travelport TripServices](https://developer.travelport.com/)** — Travel distribution API requiring trial requests and provider-provisioned production credentials. [API](https://developer.travelport.com/docs/getting-started) · [Details](./data/candidates/travelport-tripservices.yaml) · Not yet task-tested
- **[Trip.com Flight Distribution](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html)** — Trip.com supplier fare-maintenance API lead; a consumer flight-search access path is not yet established. [API](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html) · [Details](./data/candidates/trip-com-flights.yaml) · Not yet task-tested
- **[去哪儿机票合作](https://www.qunar.com/site/zh/Cooperate_4.shtml)** — 去哪儿官方机票及分销合作渠道线索；个人自助机票搜索 API 或 MCP 尚未确认。  · [Details](./data/candidates/qunar-flights.yaml) · Not yet task-tested
- **[同程机票合作](https://www.ly.com/public/about17u/contactus)** — 同程官方机票与出行平台合作线索；普通个人自助搜索 API 的准入、费用和能力尚未确认。  · [Details](./data/candidates/tongcheng-flights.yaml) · Not yet task-tested
- **[携程机票合作](https://pages.ctrip.com/public/dlhz.htm)** — 携程的分销与供应商合作线索；尚未确认面向普通个人的旅客机票搜索 API。  · [Details](./data/candidates/ctrip-flights.yaml) · Not yet task-tested
- **[飞猪国内机票开放平台](https://open.alitrip.com/businessDetail.htm?tagId=85)** — 面向机票商家的政策与订单接口，需要企业、代理商身份、店铺和聚石塔；不等同于旅客搜索接口。 [API](https://open.alitrip.com/businessDetail.htm?tagId=85) · [Details](./data/candidates/fliggy-domestic-flights.yaml) · Not yet task-tested

## Help us fill the gaps

Know a service we missed, have a task you would like tested, or found something that has changed? Issues and PRs are welcome. A useful lead or a correction is a contribution too.

[Principles](./AGENTS.md) · [Inclusion standards](./docs/catalog-standard.zh-CN.md) · [Task design](./data/experiments/tasks/AGENTS.md) · [Execution and review](./data/experiments/AGENTS.md) · [Contributing](./docs/contributing.md) · [Flight findings](./docs/flights.zh-CN.md)

Code: [MIT](./LICENSE) · Data: [CC BY 4.0](./LICENSE-DATA).
