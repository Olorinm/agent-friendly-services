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

<details>
<summary>任务、配置、样本与接入方式</summary>

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Alibaba Qwen (Model Studio)](https://www.alibabacloud.com/en/product/modelstudio) · [资料](./generated/providers.md#qwen) | Qwen model family via Alibaba Cloud Model Studio's OpenAI-compatible API, with an official open-source coding CLI agent (qwen-code). | [Docs](https://www.alibabacloud.com/help/en/model-studio/)<br>[API](https://www.alibabacloud.com/help/en/model-studio/models)<br>[CLI](https://github.com/QwenLM/qwen-code) | 待实测 |
| [Anthropic](https://www.anthropic.com) · [资料](./generated/providers.md#anthropic) | Claude model APIs with agent-focused documentation, llms.txt, and the company behind the MCP standard itself. | [Docs](https://docs.anthropic.com)<br>[API](https://docs.anthropic.com/en/api)<br>[CLI](https://docs.anthropic.com/en/docs/claude-code) | 待实测 |
| [Cartesia](https://cartesia.ai) · [资料](./generated/providers.md#cartesia) | Low-latency voice models (Sonic TTS, Ink STT) with a documented API, official MCP server, llms.txt, and a free tier. | [Docs](https://docs.cartesia.ai)<br>[API](https://docs.cartesia.ai/api-reference)<br>[MCP](https://github.com/cartesia-ai/cartesia-mcp) | 待实测 |
| [Cerebras Inference](https://cloud.cerebras.ai) · [资料](./generated/providers.md#cerebras) | Wafer-scale inference for open models at very high tokens/sec, OpenAI-compatible API, llms.txt, and a standing free tier. | [Docs](https://inference-docs.cerebras.ai)<br>[API](https://inference-docs.cerebras.ai/api-reference/chat-completions) | 待实测 |
| [Cohere](https://cohere.com) · [资料](./generated/providers.md#cohere) | Enterprise LLM platform (command, embed, rerank) with llms.txt, documented API versioning, free trial keys, and error/rate-limit docs. | [Docs](https://docs.cohere.com)<br>[API](https://docs.cohere.com/reference/about) | 待实测 |
| [Deepgram](https://deepgram.com) · [资料](./generated/providers.md#deepgram) | Speech-to-text and voice AI API with a public OpenAPI spec, llms.txt, scoped API keys, and $200 free credit without a card. | [Docs](https://developers.deepgram.com/docs)<br>[API](https://developers.deepgram.com/reference) | 待实测 |
| [DeepSeek](https://www.deepseek.com) · [资料](./generated/providers.md#deepseek) | OpenAI-compatible LLM API (DeepSeek-V3/R1) with transparent per-token pricing, a detailed changelog, and self-serve keys. | [Docs](https://api-docs.deepseek.com) | 待实测 |
| [ElevenLabs](https://elevenlabs.io) · [资料](./generated/providers.md#elevenlabs) | Voice AI (TTS, STT, agents) with a public OpenAPI spec, llms.txt, an official MCP server, and a free tier. | [Docs](https://elevenlabs.io/docs)<br>[API](https://elevenlabs.io/docs/api-reference/introduction)<br>[MCP](https://github.com/elevenlabs/elevenlabs-mcp) | 待实测 |
| [fal.ai](https://fal.ai) · [资料](./generated/providers.md#fal) | Generative media platform (image, video, audio models) with queue/streaming APIs, an official CLI/serving framework, llms.txt, and self-serve keys. | [Docs](https://fal.ai/docs)<br>[API](https://fal.ai/docs/model-apis)<br>[CLI](https://github.com/fal-ai/fal) | 待实测 |
| [Fireworks AI](https://fireworks.ai) · [资料](./generated/providers.md#fireworks) | Fast open-model inference and fine-tuning with an OpenAI-compatible API, official firectl CLI, llms.txt, and published pricing. | [Docs](https://docs.fireworks.ai)<br>[API](https://docs.fireworks.ai/api-reference/introduction)<br>[CLI](https://docs.fireworks.ai/tools-sdks/firectl/firectl) | 待实测 |
| [Gemini API](https://ai.google.dev) · [资料](./generated/providers.md#gemini-api) | Google's Gemini model APIs via AI Studio, with generous free tier and documented API versioning. | [Docs](https://ai.google.dev/gemini-api/docs)<br>[API](https://ai.google.dev/api)<br>[CLI](https://github.com/google-gemini/gemini-cli) | 待实测 |
| [Groq](https://groq.com) · [资料](./generated/providers.md#groq) | Ultra-low-latency LLM inference with an OpenAI-compatible API, llms.txt, and self-serve keys with a free tier. | [Docs](https://console.groq.com/docs)<br>[API](https://console.groq.com/docs/api-reference) | 待实测 |
| [Hugging Face](https://huggingface.co) · [资料](./generated/providers.md#hugging-face) | Model hub and inference platform with fine-grained tokens, OAuth, an official MCP server, and a full Hub API. | [Docs](https://huggingface.co/docs)<br>[API](https://huggingface.co/docs/hub/api)<br>[MCP](https://huggingface.co/mcp)<br>[CLI](https://huggingface.co/docs/huggingface_hub/guides/cli) | 待实测 |
| [Luma AI (Dream Machine)](https://lumalabs.ai) · [资料](./generated/providers.md#luma) | Dream Machine video and image generation via the Luma API, with llms.txt and published API pricing. | [Docs](https://docs.lumalabs.ai)<br>[API](https://docs.lumalabs.ai/reference) | 待实测 |
| [MiniMax](https://platform.minimax.io) · [资料](./generated/providers.md#minimax) | MiniMax text, speech, video and music models via the international platform API, with an official MCP server. | [Docs](https://platform.minimax.io/docs)<br>[API](https://platform.minimax.io/docs/api-reference)<br>[MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | 待实测 |
| [Mistral AI](https://mistral.ai) · [资料](./generated/providers.md#mistral) | European LLM provider (La Plateforme) with llms.txt, an open OpenAPI-based docs repo, a free experiment tier, and self-serve keys. | [Docs](https://docs.mistral.ai)<br>[API](https://docs.mistral.ai/api) | 待实测 |
| [Moonshot AI (Kimi)](https://platform.kimi.ai) · [资料](./generated/providers.md#moonshot) | Kimi models (K2 line) via an OpenAI-compatible API on the international Kimi platform, with an official terminal CLI agent (kimi-cli). | [Docs](https://platform.kimi.ai/docs)<br>[API](https://platform.kimi.ai/docs/api/chat)<br>[CLI](https://github.com/MoonshotAI/kimi-cli) | 待实测 |
| [OpenAI](https://openai.com) · [资料](./generated/providers.md#openai) | GPT model APIs with an official OpenAPI spec, agents guides, and a large SDK ecosystem. | [Docs](https://developers.openai.com/api/docs)<br>[API](https://platform.openai.com/docs/api-reference) | 待实测 |
| [OpenRouter](https://openrouter.ai) · [资料](./generated/providers.md#openrouter) | Unified OpenAI-compatible API over hundreds of models from many labs, with one key, per-model pricing, automatic fallbacks, and an llms.txt. | [Docs](https://openrouter.ai/docs)<br>[API](https://openrouter.ai/docs/api-reference/overview) | 待实测 |
| [Replicate](https://replicate.com) · [资料](./generated/providers.md#replicate) | Run and fine-tune open-source models via a simple predictions API, with llms.txt, webhooks, and an official CLI. | [Docs](https://replicate.com/docs)<br>[API](https://replicate.com/docs/reference/http)<br>[CLI](https://github.com/replicate/cli) | 待实测 |
| [Together AI](https://www.together.ai) · [资料](./generated/providers.md#together-ai) | Inference and fine-tuning platform for open-source models with an OpenAI-compatible API and llms.txt. | [Docs](https://docs.together.ai)<br>[API](https://docs.together.ai/reference/chat-completions) | 待实测 |
| [xAI (Grok API)](https://x.ai) · [资料](./generated/providers.md#xai) | xAI's Grok models via an OpenAI-compatible REST API, with an llms.txt and self-serve console keys. | [Docs](https://docs.x.ai)<br>[API](https://docs.x.ai/developers/rest-api-reference/inference) | 待实测 |
| [Z.ai (GLM)](https://z.ai) · [资料](./generated/providers.md#zai) | GLM models via Z.ai's OpenAI-compatible international API, with llms.txt, published pricing, and self-serve keys. | [Docs](https://docs.z.ai)<br>[API](https://docs.z.ai/api-reference) | 待实测 |

</details>

<a id="services-agent-tooling"></a>

### Agent Tooling (5)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Composio](./generated/providers.md#composio) | 待实测 | — | — | — |
| [Mem0](./generated/providers.md#mem0) | 待实测 | — | — | — |
| [n8n](./generated/providers.md#n8n) | 待实测 | — | — | — |
| [Vapi](./generated/providers.md#vapi) | 待实测 | — | — | — |
| [Zapier](./generated/providers.md#zapier) | 待实测 | — | — | — |

<details>
<summary>任务、配置、样本与接入方式</summary>

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Composio](https://composio.dev) · [资料](./generated/providers.md#composio) | Tool and integration layer for AI agents (hundreds of app connectors with managed auth), with llms.txt and a hosted MCP directory. | [Docs](https://docs.composio.dev)<br>[MCP](https://mcp.composio.dev) | 待实测 |
| [Mem0](https://mem0.ai) · [资料](./generated/providers.md#mem0) | Memory layer for AI agents (hosted platform + open-source), with REST API, llms.txt, and the official OpenMemory MCP server. | [Docs](https://docs.mem0.ai)<br>[API](https://docs.mem0.ai/api-reference)<br>[MCP](https://docs.mem0.ai/openmemory/overview) | 待实测 |
| [n8n](https://n8n.io) · [资料](./generated/providers.md#n8n) | Workflow automation platform with native AI/agent nodes, a public REST API, official hosted MCP server, CLI, and llms.txt; fair-code and self-hostable. | [Docs](https://docs.n8n.io)<br>[API](https://docs.n8n.io/api/)<br>[MCP](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)<br>[CLI](https://docs.n8n.io/hosting/cli-commands/) | 待实测 |
| [Vapi](https://vapi.ai) · [资料](./generated/providers.md#vapi) | Voice-agent orchestration API (calls, turn-taking, tool use over phone/web) with an official MCP server and an llms.txt that opens with instructions for AI agents. | [Docs](https://docs.vapi.ai)<br>[API](https://docs.vapi.ai/api-reference)<br>[MCP](https://github.com/VapiAI/mcp-server) | 待实测 |
| [Zapier](https://zapier.com) · [资料](./generated/providers.md#zapier) | Automation platform bridging 7000+ apps, with llms.txt and an official MCP endpoint that gives agents access to those integrations. | [Docs](https://docs.zapier.com)<br>[MCP](https://zapier.com/mcp)<br>[CLI](https://github.com/zapier/zapier-platform) | 待实测 |

</details>

<a id="services-code-execution"></a>

### Code Execution (4)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Browserbase](./generated/providers.md#browserbase) | 待实测 | — | — | — |
| [E2B](./generated/providers.md#e2b) | 待实测 | — | — | — |
| [Modal](./generated/providers.md#modal) | 待实测 | — | — | — |
| [Steel](./generated/providers.md#steel) | 待实测 | — | — | — |

<details>
<summary>任务、配置、样本与接入方式</summary>

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Browserbase](https://www.browserbase.com) · [资料](./generated/providers.md#browserbase) | Headless browser infrastructure for AI agents and automation, with session APIs and an official MCP server. | [Docs](https://docs.browserbase.com)<br>[API](https://docs.browserbase.com/reference)<br>[MCP](https://github.com/browserbase/mcp-server-browserbase) | 待实测 |
| [E2B](https://e2b.dev) · [资料](./generated/providers.md#e2b) | Isolated cloud sandboxes for running AI-generated code, with llms.txt, an official MCP server, and self-serve keys. | [Docs](https://e2b.dev/docs)<br>[MCP](https://github.com/e2b-dev/mcp-server)<br>[CLI](https://e2b.dev/docs/cli) | 待实测 |
| [Modal](https://modal.com) · [资料](./generated/providers.md#modal) | Serverless compute for Python with first-class Sandboxes for agent code execution, llms.txt, and an official CLI. | [Docs](https://modal.com/docs)<br>[API](https://modal.com/docs/reference)<br>[CLI](https://modal.com/docs/reference/cli) | 待实测 |
| [Steel](https://steel.dev) · [资料](./generated/providers.md#steel) | Cloud browser API for AI agents (sessions, CDP, anti-bot) — open-source and self-hostable, with llms.txt and a free tier. | [Docs](https://docs.steel.dev)<br>[API](https://docs.steel.dev/api-reference) | 待实测 |

</details>

<a id="services-developer-tools"></a>

### Developer Tools (4)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Atlassian (Jira & Confluence)](./generated/providers.md#atlassian) | 待实测 | — | — | — |
| [GitHub](./generated/providers.md#github) | [历史实测](./generated/agent-runs.md#github) | — | — | — |
| [GitLab](./generated/providers.md#gitlab) | 待实测 | — | — | — |
| [Postman](./generated/providers.md#postman) | 待实测 | — | — | — |

<details>
<summary>任务、配置、样本与接入方式</summary>

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Atlassian (Jira & Confluence)](https://www.atlassian.com) · [资料](./generated/providers.md#atlassian) | Jira, Confluence and the Atlassian Cloud platform — REST APIs, an official remote MCP server (OAuth 2.1), and the acli CLI. | [Docs](https://developer.atlassian.com)<br>[API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)<br>[MCP](https://github.com/atlassian/atlassian-mcp-server)<br>[CLI](https://developer.atlassian.com/cloud/acli/) | 待实测 |
| [GitHub](https://github.com) · [资料](./generated/providers.md#github) | Code hosting, collaboration, and automation with REST and GraphQL APIs, an official CLI, and an official MCP server. | [Docs](https://docs.github.com)<br>[API](https://docs.github.com/rest)<br>[MCP](https://github.com/github/github-mcp-server)<br>[CLI](https://cli.github.com) | [历史实测](./generated/agent-runs.md#github) |
| [GitLab](https://gitlab.com) · [资料](./generated/providers.md#gitlab) | DevOps platform with REST and GraphQL APIs, scoped tokens, llms.txt, and an official CLI. | [Docs](https://docs.gitlab.com)<br>[API](https://docs.gitlab.com/api/rest/)<br>[MCP](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server)<br>[CLI](https://gitlab.com/gitlab-org/cli) | 待实测 |
| [Postman](https://www.postman.com) · [资料](./generated/providers.md#postman) | API development platform with a public Postman API, llms.txt, official CLI, and self-serve keys. | [Docs](https://learning.postman.com)<br>[API](https://learning.postman.com/docs/developer/postman-api/intro-api/)<br>[MCP](https://github.com/postmanlabs/postman-mcp-server)<br>[CLI](https://learning.postman.com/docs/postman-cli/postman-cli-overview/) | 待实测 |

</details>

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

<details>
<summary>任务、配置、样本与接入方式</summary>

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Cloudflare](https://www.cloudflare.com) · [资料](./generated/providers.md#cloudflare) | Edge network, Workers serverless platform, storage, and AI services with agent-focused docs and official MCP servers. | [CLI](https://developers.cloudflare.com/d1/get-started/) | 待实测 |
| [Fly.io](https://fly.io) · [资料](./generated/providers.md#fly-io) | Run full-stack apps and machines close to users, with a spec'd Machines API, scoped macaroon tokens, and official MCP docs. | [Docs](https://fly.io/docs)<br>[API](https://fly.io/docs/machines/api/)<br>[MCP](https://fly.io/docs/mcp/)<br>[CLI](https://fly.io/docs/flyctl/) | 待实测 |
| [Netlify](https://www.netlify.com) · [资料](./generated/providers.md#netlify) | Web platform for deploying sites and functions, with an OpenAPI-specified API, llms.txt, official CLI and MCP server. | [Docs](https://docs.netlify.com)<br>[API](https://open-api.netlify.com)<br>[MCP](https://docs.netlify.com/welcome/build-with-ai/netlify-mcp-server/)<br>[CLI](https://docs.netlify.com/cli/get-started/) | 待实测 |
| [Railway](https://railway.com) · [资料](./generated/providers.md#railway) | App/database hosting with a public GraphQL API, official CLI, llms.txt, and usage-based pricing. | [Docs](https://docs.railway.com)<br>[API](https://docs.railway.com/reference/public-api)<br>[CLI](https://github.com/railwayapp/cli) | 待实测 |
| [Render](https://render.com) · [资料](./generated/providers.md#render) | Cloud hosting for web services, static sites and databases with a REST API, official CLI, official MCP server, and llms.txt. | [Docs](https://render.com/docs)<br>[API](https://api-docs.render.com/reference/introduction)<br>[MCP](https://github.com/render-oss/render-mcp-server)<br>[CLI](https://github.com/render-oss/cli) | 待实测 |
| [Vercel](https://vercel.com) · [资料](./generated/providers.md#vercel) | Frontend cloud for deploying web apps, with a REST API, CLI, official MCP server, and AI SDK ecosystem. | [Docs](https://vercel.com/docs)<br>[API](https://vercel.com/docs/rest-api)<br>[MCP](https://vercel.com/docs/mcp/vercel-mcp)<br>[CLI](https://vercel.com/docs/cli) | 待实测 |

</details>

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
<summary>任务、配置、样本与接入方式</summary>

**[database-todos-001 v1](./generated/evaluations.md#comparison-1420586eae17)**

gpt-6-astra / xhigh · codex-cli 0.153.4 · 600s · legacy · 预供凭据

- 为我的个人待办应用准备一个独立的远程数据库，验证新增、修改和重新连接后读取待办事项

- Turso / platform-api: 完成 / 失败 / 环境无效 = 1 / 0 / 0; [2026-09-07](./data/experiments/evaluations/codex-20260907T113506.422646Z-turso.json)

**[database-todos-001 v1](./generated/evaluations.md#comparison-fdecec09a4b6)**

gpt-6-astra / xhigh · codex-cli 0.153.4 · 600s · legacy · 未供凭据

- 为我的个人待办应用准备一个独立的远程数据库，验证新增、修改和重新连接后读取待办事项

- Neon / ephemeral-api: 完成 / 失败 / 环境无效 = 1 / 0 / 0; [2026-09-07](./data/experiments/evaluations/codex-20260907T112258.549053Z-neon.json)

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Aiven](https://aiven.io/) · [资料](./data/candidates/aiven.yaml) | Managed databases including free hosted PostgreSQL. Account signup and provisioning remain untested; free lifecycle limits need checking before production use. | [CLI](https://aiven.io/docs/tools/cli) | 待实测 |
| [Cloudflare](https://www.cloudflare.com) · [资料](./generated/providers.md#cloudflare) | Edge network, Workers serverless platform, storage, and AI services with agent-focused docs and official MCP servers. | [CLI](https://developers.cloudflare.com/d1/get-started/) | 待实测 |
| [Neon](https://neon.com) · [资料](./generated/providers.md#neon) | Serverless Postgres with instant branching, a full management API, official MCP server, and agent-oriented docs. | [API](https://neon.new/) | [1 完成](./generated/evaluations.md) |
| [PlanetScale](https://planetscale.com/) · [资料](./data/candidates/planetscale.yaml) | PostgreSQL single-node plans start at USD 5/month. No free writable database allowance verified; not provisioned in this no-payment round. Public pricing SQL is read-only and does not meet the task. | [CLI](https://planetscale.com/docs/cli) | 待实测 |
| [Supabase](https://supabase.com) · [资料](./generated/providers.md#supabase) | Postgres platform with auth, storage, edge functions, a management API, official MCP server, and LLM-ready docs. | [API](https://supabase.com/docs/guides/api) | 待实测 |
| [Turso](https://turso.tech/) · [资料](./data/candidates/turso.yaml) | Free cloud account: 100 databases, 5 GB, 500 million reads/month and 10 million writes/month. Signup/login required; local engine alone does not satisfy remote storage. | [CLI](https://docs.turso.tech/cli/introduction)<br>[API](https://docs.turso.tech/api-reference/introduction) | [1 完成](./generated/evaluations.md) |

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

<details>
<summary>任务、配置、样本与接入方式</summary>

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Chroma](https://www.trychroma.com) · [资料](./generated/providers.md#chroma) | Open-source embedding database with a hosted Chroma Cloud, official CLI, official MCP server, and llms.txt. | [Docs](https://docs.trychroma.com)<br>[API](https://docs.trychroma.com/docs/overview/introduction)<br>[MCP](https://github.com/chroma-core/chroma-mcp)<br>[CLI](https://docs.trychroma.com/docs/cli/install) | 待实测 |
| [MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-database) · [资料](./generated/providers.md#mongodb-atlas) | Managed MongoDB with a versioned Admin API, published OpenAPI spec, llms.txt, official CLI and MCP server. | [Docs](https://www.mongodb.com/docs/atlas/)<br>[API](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/)<br>[MCP](https://github.com/mongodb-js/mongodb-mcp-server)<br>[CLI](https://www.mongodb.com/docs/atlas/cli/) | 待实测 |
| [Pinecone](https://www.pinecone.io) · [资料](./generated/providers.md#pinecone) | Managed vector database for search and RAG, with llms.txt, an official MCP server, and self-serve keys. | [Docs](https://docs.pinecone.io)<br>[API](https://docs.pinecone.io/reference/api/introduction)<br>[MCP](https://docs.pinecone.io/guides/operations/mcp-server)<br>[CLI](https://github.com/pinecone-io/cli) | 待实测 |
| [Qdrant](https://qdrant.tech) · [资料](./generated/providers.md#qdrant) | Open-source vector database with a managed cloud, llms.txt, an official MCP server, and a free cluster tier. | [Docs](https://qdrant.tech/documentation)<br>[API](https://api.qdrant.tech)<br>[MCP](https://github.com/qdrant/mcp-server-qdrant) | 待实测 |
| [Redis (Redis Cloud)](https://redis.io) · [资料](./generated/providers.md#redis) | In-memory data platform for caching, vector search and real-time apps; Redis Cloud has a REST management API, official MCP server, redis-cli, and llms.txt. | [Docs](https://redis.io/docs/latest)<br>[API](https://redis.io/docs/latest/operate/rc/api/)<br>[MCP](https://github.com/redis/mcp-redis)<br>[CLI](https://redis.io/docs/latest/develop/tools/cli/) | 待实测 |
| [Upstash](https://upstash.com) · [资料](./generated/providers.md#upstash) | Serverless Redis, Kafka-successor queues, and vector storage with REST APIs, llms.txt, an official MCP server, and a free tier. | [Docs](https://upstash.com/docs)<br>[API](https://upstash.com/docs/devops/developer-api/introduction)<br>[MCP](https://github.com/upstash/mcp-server)<br>[CLI](https://github.com/upstash/cli) | 待实测 |
| [Weaviate](https://weaviate.io) · [资料](./generated/providers.md#weaviate) | Open-source vector database with REST/GraphQL/gRPC APIs, Weaviate Cloud free sandboxes, an official CLI, MCP server, and llms.txt. | [Docs](https://docs.weaviate.io)<br>[API](https://docs.weaviate.io/weaviate/api/rest)<br>[MCP](https://github.com/weaviate/mcp-server-weaviate)<br>[CLI](https://github.com/weaviate/weaviate-cli) | 待实测 |

</details>

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
<summary>任务、配置、样本与接入方式</summary>

**[web-search-001 v1](./generated/evaluations.md#comparison-9dbe771526ac)**

gpt-6-astra / xhigh · codex-cli 0.153.4 · 600s · legacy · 预供凭据

- 我准备把 Python 应用升级到 3.13，查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并给出官方依据

- Exa / search-api: 完成 / 失败 / 环境无效 = 0 / 1 / 0; [2026-09-07](./data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json)

**[web-search-001 v1](./generated/evaluations.md#comparison-b5f21fc39ab4)**

gpt-6-astra / xhigh · codex-cli 0.153.4 · 600s · legacy · 未供凭据

- 我准备把 Python 应用升级到 3.13，查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并给出官方依据

- Firecrawl / public-search-api: 完成 / 失败 / 环境无效 = 1 / 0 / 0; [2026-09-07](./data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json)

**[web-search-001 v1](./generated/evaluations.md#comparison-87ab787b88b3)**

gpt-6-astra / xhigh · codex-cli 0.153.4 · 600s · legacy · 未供凭据

- 我准备把 Python 应用升级到 3.13，查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并给出官方依据

- Exa / public-mcp: 完成 / 失败 / 环境无效 = 1 / 0 / 0; [2026-09-07](./data/experiments/evaluations/codex-20260907T112257.401366Z-exa.json)

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Brave Search API](https://brave.com/search/api/) · [资料](./generated/providers.md#brave-search) | Independent web search index with a developer API, self-serve registration, and a free plan. | [API](https://brave.com/search/api/) | 待实测 |
| [Exa](https://exa.ai) · [资料](./generated/providers.md#exa) | Search API built for AI — semantic web search, content retrieval, and research endpoints with an official MCP server. | [MCP](https://mcp.exa.ai/mcp)<br>[API](https://exa.ai/docs/reference/search) | [1 完成 / 1 未完成](./generated/evaluations.md) |
| [Firecrawl](https://www.firecrawl.dev) · [资料](./generated/providers.md#firecrawl) | Web scraping and crawling API that turns websites into LLM-ready markdown, with an official MCP server. | [API: account-search-api](https://docs.firecrawl.dev/features/search) | [1 完成](./generated/evaluations.md) |
| [SerpApi](https://serpapi.com) · [资料](./generated/providers.md#serpapi) | Real-time JSON API for Google and other search engines' results, with an official MCP server, llms.txt, and a free monthly quota. | [API: google-flights-api](https://serpapi.com/google-flights-api)<br>[MCP](https://github.com/serpapi/serpapi-mcp)<br>[API: web-search-api](https://serpapi.com/search-api) | 待实测 |
| [Serper](https://serper.dev/) · [资料](./data/candidates/serper.yaml) | Google results API with signup trial queries; actual account flow and authentication remain untested. | [API](https://serper.dev/) | 待实测 |
| [Tavily](https://www.tavily.com) · [资料](./generated/providers.md#tavily) | Search and extraction API built for AI agents, with llms.txt, an official MCP server, and a free tier. | [API](https://docs.tavily.com/documentation/quickstart) | 待实测 |

</details>

<a id="services-web-search-data-other"></a>

#### 其他服务

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Apify](./generated/providers.md#apify) | 待实测 | — | — | — |
| [Jina AI](./generated/providers.md#jina) | 待实测 | — | — | — |
| [Perplexity API](./generated/providers.md#perplexity) | 待实测 | — | — | — |
| [Xquik](./data/candidates/xquik.yaml) | [历史首次调用检查](./data/experiments/published/xquik/2026-07-15-dry-fire-rep3.md) | — | — | — |

<details>
<summary>任务、配置、样本与接入方式</summary>

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Apify](https://apify.com) · [资料](./generated/providers.md#apify) | Web scraping and automation platform with thousands of ready-made actors, a versioned API, llms.txt, and an official MCP server. | [Docs](https://docs.apify.com)<br>[API](https://docs.apify.com/api/v2)<br>[MCP](https://docs.apify.com/platform/integrations/mcp)<br>[CLI](https://docs.apify.com/cli) | 待实测 |
| [Jina AI](https://jina.ai) · [资料](./generated/providers.md#jina) | Search-foundation APIs (Reader for URL-to-markdown, embeddings, reranker, deep search) with an official remote MCP server, an agent-targeted llms.txt, and a keyless trial path. | [API](https://docs.jina.ai)<br>[MCP](https://github.com/jina-ai/MCP) | 待实测 |
| [Perplexity API](https://www.perplexity.ai) · [资料](./generated/providers.md#perplexity) | Sonar API for web-grounded answers and search, with llms.txt, an official MCP server, and documented usage tiers. | [Docs](https://docs.perplexity.ai)<br>[MCP](https://github.com/ppl-ai/modelcontextprotocol) | 待实测 |
| [Xquik](https://xquik.com) · [资料](./data/candidates/xquik.yaml) | Hosted X data and account automation service with a REST API, official MCP server, OpenAPI, SDKs, HMAC webhooks, and OAuth 2.1. | [Docs](https://docs.xquik.com)<br>[API](https://docs.xquik.com/api-reference/overview)<br>[MCP](https://docs.xquik.com/mcp/overview) | [历史首次调用检查](./data/experiments/published/xquik/2026-07-15-dry-fire-rep3.md) |

</details>

<a id="services-payments-billing"></a>

### Payments / Billing (4)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Lemon Squeezy](./generated/providers.md#lemonsqueezy) | 待实测 | — | — | — |
| [paas.build](./data/candidates/paas-build.yaml) | [历史首次调用检查](./data/experiments/published/paas-build/2026-07-15-dry-fire-rep3.md) | — | — | — |
| [Paddle](./generated/providers.md#paddle) | 待实测 | — | — | — |
| [Stripe](./generated/providers.md#stripe) | 待实测 | — | — | — |

<details>
<summary>任务、配置、样本与接入方式</summary>

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Lemon Squeezy](https://www.lemonsqueezy.com) · [资料](./generated/providers.md#lemonsqueezy) | Merchant-of-record payments for digital products/SaaS with a JSON:API REST API, documented test mode, and self-serve keys. | [Docs](https://docs.lemonsqueezy.com)<br>[API](https://docs.lemonsqueezy.com/api) | 待实测 |
| [paas.build](https://paas.build) · [资料](./data/candidates/paas-build.yaml) | Agent-native payment facilitator (the AI-builder product of UniPaaS, FCA-authorised No. 929994) — opens a real merchant account via progressive KYB and creates checkouts through MCP or REST. | [Docs](https://paas.build/agents)<br>[MCP](https://github.com/UNIPaaS/paas-build-mcp) | [历史首次调用检查](./data/experiments/published/paas-build/2026-07-15-dry-fire-rep3.md) |
| [Paddle](https://www.paddle.com) · [资料](./generated/providers.md#paddle) | Merchant-of-record billing platform with a versioned API, full sandbox, llms.txt, and webhooks. | [Docs](https://developer.paddle.com)<br>[API](https://developer.paddle.com/api-reference/overview)<br>[MCP](https://github.com/PaddleHQ/paddle-mcp-server) | 待实测 |
| [Stripe](https://stripe.com) · [资料](./generated/providers.md#stripe) | Payments, billing, subscriptions, and financial infrastructure with a famously complete API surface. | [Docs](https://docs.stripe.com)<br>[API](https://docs.stripe.com/api)<br>[MCP](https://docs.stripe.com/mcp)<br>[CLI](https://docs.stripe.com/stripe-cli) | 待实测 |

</details>

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

<details>
<summary>任务、配置、样本与接入方式</summary>

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Discord](https://discord.com) · [资料](./generated/providers.md#discord) | Chat platform with a versioned bot/OAuth2 API, official OpenAPI spec (preview), webhooks, and documented rate limits. | [Docs](https://discord.com/developers/docs/intro)<br>[API](https://discord.com/developers/docs/reference) | 待实测 |
| [Lark](https://www.larksuite.com) · [资料](./generated/providers.md#lark) | Collaboration suite (messaging, docs, calendar) with an open platform, llms.txt, an official CLI with 200+ commands and agent skills, and an official OpenAPI MCP server. | [API](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create)<br>[CLI](https://github.com/larksuite/cli)<br>[MCP](https://github.com/larksuite/lark-openapi-mcp) | 待实测 |
| [Resend](https://resend.com) · [资料](./generated/providers.md#resend) | Email API for developers with test mode, scoped API keys, idempotency support, and an official MCP server. | [Docs](https://resend.com/docs)<br>[API](https://resend.com/docs/api-reference/introduction)<br>[MCP](https://github.com/resend/mcp-send-email) | 待实测 |
| [Slack](https://slack.com) · [资料](./generated/providers.md#slack) | Workspace messaging platform with a mature Web API, granular OAuth scopes, an OpenAPI spec, and llms.txt. | [Docs](https://api.slack.com)<br>[API](https://api.slack.com/methods)<br>[CLI](https://docs.slack.dev/tools/slack-cli) | 待实测 |
| [Telegram Bot API](https://telegram.org) · [资料](./generated/providers.md#telegram) | Free bot platform with instant token issuance via BotFather, webhooks, a documented test environment, and a detailed changelog. | [Docs](https://core.telegram.org/bots)<br>[API](https://core.telegram.org/bots/api) | 待实测 |
| [Twilio](https://www.twilio.com) · [资料](./generated/providers.md#twilio) | Programmable messaging and voice APIs with test credentials, an OpenAPI spec, llms.txt, and an official CLI. | [Docs](https://www.twilio.com/docs)<br>[API](https://www.twilio.com/docs/usage/api)<br>[MCP](https://github.com/twilio-labs/mcp)<br>[CLI](https://www.twilio.com/docs/twilio-cli) | 待实测 |

</details>

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
<summary>任务、配置、样本与接入方式</summary>

**[collaborative-tables-001 v2](./generated/evaluations.md#comparison-6203194a76cd)**

gpt-6-astra / xhigh · codex-cli 0.153.4 · 600s · natural · 预供凭据

- 帮我把这份读书会会议记录里的待办整理成在线任务表，给我链接，再告诉我还有哪些没完成、各自什么时候到期。

- Grist / rest-api: 完成 / 失败 / 环境无效 = 1 / 0 / 0; [2026-09-08](./data/experiments/evaluations/codex-20260908T035504.472694Z-grist.json)
- Notion / rest-api: 完成 / 失败 / 环境无效 = 1 / 0 / 0; [2026-09-08](./data/experiments/evaluations/codex-20260908T035504.906378Z-notion.json)

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Airtable](https://www.airtable.com) · [资料](./generated/providers.md#airtable) | Spreadsheet-database hybrid with a REST API, scoped personal access tokens, OAuth, webhooks, and documented rate limits. | [API](https://airtable.com/developers/web/api/introduction) | 待实测 |
| [Baserow Cloud](https://baserow.io/) · [资料](./data/candidates/baserow.yaml) | Hosted collaborative tables; free workspace and scoped row-access tokens. Schema management uses a different credential. | [API](https://baserow.io/docs/apis/rest-api)<br>[MCP](https://baserow.io/user-docs/mcp-server) | 待实测 |
| [Coda / Superhuman Docs](https://coda.io/) · [资料](./data/candidates/coda.yaml) | Docs and tables with a free REST API; current API page is branded Superhuman Docs. | [API](https://coda.io/developers/apis/v1)<br>[MCP](https://coda.io/apis/mcp) | 待实测 |
| [Google Sheets](https://workspace.google.com/products/sheets/) · [资料](./data/candidates/google-sheets.yaml) | Online spreadsheets with a no-additional-cost API; Cloud project and OAuth setup are still prerequisites. | [API](https://developers.google.com/workspace/sheets/api/guides/concepts) | 待实测 |
| [Grist](https://www.getgrist.com/) · [资料](./data/candidates/grist.yaml) | Hosted relational spreadsheets with a free personal site, REST API and official MCP. | [API](https://support.getgrist.com/api/)<br>[MCP](https://docs.getgrist.com/api/mcp)<br>[SDK: python-sdk](https://pypi.org/project/grist-api/)<br>[SDK: javascript-sdk](https://www.npmjs.com/package/grist-api) | [2 完成](./generated/evaluations.md) |
| [Lark](https://www.larksuite.com) · [资料](./generated/providers.md#lark) | Collaboration suite (messaging, docs, calendar) with an open platform, llms.txt, an official CLI with 200+ commands and agent skills, and an official OpenAPI MCP server. | [API](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create)<br>[CLI](https://github.com/larksuite/cli)<br>[MCP](https://github.com/larksuite/lark-openapi-mcp) | 待实测 |
| [Notion](https://www.notion.com) · [资料](./generated/providers.md#notion) | Connected workspace with a versioned REST API, capability-scoped integrations, llms.txt, and an official MCP server. | [API](https://developers.notion.com/reference/intro)<br>[SDK](https://github.com/makenotion/notion-sdk-js)<br>[CLI](https://developers.notion.com/cli/get-started/overview)<br>[MCP](https://mcp.notion.com/mcp) | [2 完成](./generated/evaluations.md) |
| [飞书 Feishu](https://www.feishu.cn/) · [资料](./data/candidates/feishu.yaml) | China-region Feishu workspace and Base APIs; separate account/tenant from international Lark. | [API](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/create)<br>[CLI](https://github.com/larksuite/cli)<br>[MCP](https://github.com/larksuite/lark-openapi-mcp) | 待实测 |

</details>

<a id="services-productivity-storage-other"></a>

#### 其他服务

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Dropbox](./generated/providers.md#dropbox) | 待实测 | — | — | — |
| [Linear](./generated/providers.md#linear) | 待实测 | — | — | — |

<details>
<summary>任务、配置、样本与接入方式</summary>

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Dropbox](https://www.dropbox.com) · [资料](./generated/providers.md#dropbox) | File storage and sync with a scoped-OAuth HTTP API, self-serve app creation, and webhooks. | [Docs](https://www.dropbox.com/developers/documentation)<br>[API](https://www.dropbox.com/developers/documentation/http/documentation)<br>[CLI](https://github.com/dropbox/dbxcli) | 待实测 |
| [Linear](https://linear.app) · [资料](./generated/providers.md#linear) | Issue tracking and product planning with a GraphQL API, llms.txt, an official MCP server, and webhooks. | [Docs](https://linear.app/developers)<br>[MCP](https://linear.app/docs/mcp) | 待实测 |

</details>

<a id="services-observability-security"></a>

### Observability / Security (3)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Datadog](./generated/providers.md#datadog) | 待实测 | — | — | — |
| [Grafana (Grafana Cloud)](./generated/providers.md#grafana) | 待实测 | — | — | — |
| [Sentry](./generated/providers.md#sentry) | 待实测 | — | — | — |

<details>
<summary>任务、配置、样本与接入方式</summary>

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Datadog](https://www.datadoghq.com) · [资料](./generated/providers.md#datadog) | Observability platform with a full REST API, llms.txt, documented OAuth for integrations, rate limits, and webhooks. | [Docs](https://docs.datadoghq.com)<br>[API](https://docs.datadoghq.com/api/latest/)<br>[MCP](https://docs.datadoghq.com/bits_ai/mcp_server)<br>[CLI](https://github.com/DataDog/datadog-ci) | 待实测 |
| [Grafana (Grafana Cloud)](https://grafana.com) · [资料](./generated/providers.md#grafana) | Observability platform (dashboards, metrics, logs, traces) with a documented HTTP API, official MCP server, llms.txt, and a standing free cloud tier. | [Docs](https://grafana.com/docs)<br>[API](https://grafana.com/docs/grafana/latest/developers/http_api/)<br>[MCP](https://github.com/grafana/mcp-grafana) | 待实测 |
| [Sentry](https://sentry.io) · [资料](./generated/providers.md#sentry) | Error monitoring and performance tracing with llms.txt, an official MCP server, scoped auth tokens, and a full API. | [Docs](https://docs.sentry.io)<br>[API](https://docs.sentry.io/api/)<br>[MCP](https://docs.sentry.io/product/sentry-mcp/)<br>[CLI](https://docs.sentry.io/cli/) | 待实测 |

</details>

<a id="services-commerce-marketing"></a>

### Commerce / Marketing (1)

| 服务 | 完成率 | Token 用量 | 模型费用 | 服务费用 |
| --- | ---: | ---: | ---: | ---: |
| [Shopify](./generated/providers.md#shopify) | 待实测 | — | — | — |

<details>
<summary>任务、配置、样本与接入方式</summary>

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [Shopify](https://www.shopify.com) · [资料](./generated/providers.md#shopify) | Commerce platform with versioned GraphQL APIs, llms.txt, official MCP docs, access-scoped tokens, free development stores, and a CLI. | [Docs](https://shopify.dev/docs)<br>[API](https://shopify.dev/docs/api)<br>[MCP](https://shopify.dev/docs/apps/build/storefront-mcp)<br>[CLI](https://shopify.dev/docs/api/shopify-cli) | 待实测 |

</details>

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
<summary>任务、配置、样本与接入方式</summary>

**[flights-search-001 v1](./generated/evaluations.md#comparison-c77feef961a0)**

gpt-6-astra / xhigh · codex-cli 0.153.4 · 600s · legacy · 未供凭据

- 找到9月25日米兰飞往荷兰的机票

- Kiwi.com / search-mcp: 完成 / 失败 / 环境无效 = 1 / 0 / 0; [2026-09-07](./data/experiments/evaluations/codex-20260907T092329.724439Z-kiwi.json)

**[flights-search-001 v1](./generated/evaluations.md#comparison-45effe165cf4)**

gpt-6-astra / xhigh · codex-cli 0.153.4 · 600s · legacy · 未供凭据

- 找到9月25日米兰飞往荷兰的机票

- Ignav Flights / public-playground: 完成 / 失败 / 环境无效 = 1 / 0 / 0; [2026-09-07](./data/experiments/evaluations/codex-20260907T083644.877057Z-ignav.json)

| 服务 | 用途 | 接入方式 | 实测状态 |
| --- | --- | --- | --- |
| [AirGateway Platform API](https://airgateway.com/) · [资料](./data/candidates/airgateway.yaml) | Air distribution API with sandbox keys, production certification and an agency application. | [API](https://support.airgateway.com/en-US/kb/article/4/introduction-to-airgateway-platform-api) | 待实测 |
| [Amadeus Flight APIs](https://developers.amadeus.com/) · [资料](./data/candidates/amadeus-flights.yaml) | Historical Self-Service flight API and the current Enterprise portal; individual onboarding must be re-established. | [API: former-self-service](https://developers.amadeus.com/blog/comparing-open-source-flight-data-sources)<br>[API: enterprise-api](https://developers.amadeus.com/) | 待实测 |
| [apiheya Air Scraper](https://rapidapi.com/apiheya/api/sky-scrapper/pricing) · [资料](./data/candidates/apiheya-air-scraper.yaml) | An apiheya flight-data product distributed through RapidAPI; distinct from the official Skyscanner partner API. | [API](https://rapidapi.com/apiheya/api/sky-scrapper/playground/apiendpoint_6856e0a6-2804-43cd-9cc0-bb377022981e) | 待实测 |
| [Aviasales via Travelpayouts](https://www.aviasales.com/) · [资料](./data/candidates/aviasales.yaml) | Travelpayouts-distributed live flight search and a separately accessible historical price-data API. | [API: live-search-api](https://support.travelpayouts.com/hc/en-us/articles/210995808-How-to-get-access-to-the-Aviasales-Search-API)<br>[API: cached-data-api](https://support.travelpayouts.com/hc/en-us/articles/203956163-Aviasales-Data-API) | 待实测 |
| [Bright Data SERP API](https://brightdata.com/) · [资料](./data/candidates/bright-data-serp.yaml) | SERP API with a documented Google Flights request; structured fare extraction and onboarding need verification. | [API](https://docs.brightdata.com/api-reference/serp/google-flights/currency) | 待实测 |
| [Duffel Flights API](https://duffel.com/) · [资料](./data/candidates/duffel-flights.yaml) | Flight API whose self-serve test environment must be distinguished from live account activation. | [API: test-api](https://duffel.com/docs/api/overview/test-mode)<br>[API: live-api](https://duffel.com/guides/getting-started) | 待实测 |
| [Expedia XAP Flight Listings](https://developers.expediagroup.com/xap-apis/api/start-guide/getting-started) · [资料](./data/candidates/expedia-xap-flights.yaml) | Travel Redirect/XAP flight listings product whose new API applications are currently paused. | [API](https://developers.expediagroup.com/xap-apis/api/shopping-apis/flight-listings) | 待实测 |
| [Flight MCP](https://flight-mcp.com/) · [资料](./data/candidates/flight-mcp.yaml) | Authenticated flight lookup and a separate, restricted public cache exposed through REST and MCP. | [MCP: public-cache-mcp](https://flight-mcp.com/docs) | 待实测 |
| [FlightAPI.io Flight Price API](https://www.flightapi.io/) · [资料](./data/candidates/flightapi-io.yaml) | Flight-price search for one-way, round-trip and multi-city itineraries, with credit-based usage. | [API](https://www.flightapi.io/documentation/) | 待实测 |
| [Ignav Flights](https://ignav.com/) · [资料](./data/candidates/ignav.yaml) | Flight search and purchase-link API with email signup and an official MCP; individual eligibility remains untested. | [WEB](https://ignav.com/playground)<br>[API](https://ignav.com/docs)<br>[MCP](https://ignav.com/docs/mcp) | [1 完成](./generated/evaluations.md) |
| [KAYAK Affiliate API](https://affiliates.kayak.com/) · [资料](./data/candidates/kayak-affiliate.yaml) | Affiliate flight APIs with a business application and an optional requested sandbox. | [API](https://developers.kayak.com/) | 待实测 |
| [Kiwi.com](https://www.kiwi.com/) · [资料](./data/candidates/kiwi.yaml) | Flight search through a publicized MCP path and the separately gated Tequila partnership API. | [MCP](https://mcp.kiwi.com)<br>[API](https://media.kiwi.com/articles-and-interviews/better-for-business-kiwi-com-takes-a-new-approach-to-partnerships/) | [2 完成 / 1 环境无效](./generated/evaluations.md) |
| [LetsFG Personal Flight Search](https://letsfg.co/) · [资料](./data/candidates/letsfg.yaml) | Personal flight search through MCP, CLI and SDKs, with a human payment-method authorization step. | [MCP](https://letsfg.co/for-agents)<br>[SDK](https://github.com/letsfg/letsfg) | 待实测 |
| [Lufthansa Partner Fare API](https://developer.lufthansa.com/page) · [资料](./data/candidates/lufthansa-partner.yaml) | Lufthansa fare methods are partner-scoped; the developer portal currently pauses new Open API registrations. | [API: open-api-registration](https://developer.lufthansa.com/page)<br>[API: partner-offers-api](https://developer.lufthansa.com/docs/read/api_partner/offers) | 待实测 |
| [Sabre Air APIs](https://developer.sabre.com/) · [资料](./data/candidates/sabre-air.yaml) | Air API workflows with assigned credentials, plus a separately researched Agentic API/MCP lead. | [API](https://github.com/SabreDevStudio/SabreAPIsWorkflows/blob/master/SabreAPIsTestSuites/README.md)<br>[MCP](https://developer.sabre.com/) | 待实测 |
| [Scrapingdog Google Flights API](https://www.scrapingdog.com/) · [资料](./data/candidates/scrapingdog-flights.yaml) | Google Flights extraction endpoint charged in platform credits rather than one credit per flight search. | [API](https://www.scrapingdog.com/documentation/google-flights-api/) | 待实测 |
| [SearchApi Google Flights](https://www.searchapi.io/) · [资料](./data/candidates/searchapi.yaml) | Google Flights extraction API and a hosted MCP integration supporting token or browser authorization. | [API](https://www.searchapi.io/docs/google-flights-api)<br>[MCP](https://www.searchapi.io/mcp) | 待实测 |
| [SerpApi](https://serpapi.com) · [资料](./generated/providers.md#serpapi) | Real-time JSON API for Google and other search engines' results, with an official MCP server, llms.txt, and a free monthly quota. | [API: google-flights-api](https://serpapi.com/google-flights-api)<br>[MCP](https://github.com/serpapi/serpapi-mcp)<br>[API: web-search-api](https://serpapi.com/search-api) | 待实测 |
| [Skootle Google Flights Scraper](https://apify.com/skootle/google-flights-scraper) · [资料](./data/candidates/skootle-google-flights.yaml) | A Skootle-published flight-scraping Actor hosted on Apify, billed by startup and output records. | [API](https://apify.com/skootle/google-flights-scraper) | 待实测 |
| [Skyscanner Travel APIs](https://www.skyscanner.net/) · [资料](./data/candidates/skyscanner.yaml) | Partner flight APIs and an official MCP, with independently documented business-access paths. | [API](https://developers.skyscanner.net/docs/getting-started/authentication)<br>[MCP](https://developers.skyscanner.net/docs/mcp-server) | 待实测 |
| [Travelport TripServices](https://developer.travelport.com/) · [资料](./data/candidates/travelport-tripservices.yaml) | Travel distribution API requiring trial requests and provider-provisioned production credentials. | [API](https://developer.travelport.com/docs/getting-started) | 待实测 |
| [Trip.com Flight Distribution](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html) · [资料](./data/candidates/trip-com-flights.yaml) | Trip.com supplier fare-maintenance API lead; a consumer flight-search access path is not yet established. | [API](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html) | 待实测 |
| [去哪儿机票合作](https://www.qunar.com/site/zh/Cooperate_4.shtml) · [资料](./data/candidates/qunar-flights.yaml) | 去哪儿官方机票及分销合作渠道线索；个人自助机票搜索 API 或 MCP 尚未确认。 | — | 待实测 |
| [同程机票合作](https://www.ly.com/public/about17u/contactus) · [资料](./data/candidates/tongcheng-flights.yaml) | 同程官方机票与出行平台合作线索；普通个人自助搜索 API 的准入、费用和能力尚未确认。 | — | 待实测 |
| [携程机票合作](https://pages.ctrip.com/public/dlhz.htm) · [资料](./data/candidates/ctrip-flights.yaml) | 携程的分销与供应商合作线索；尚未确认面向普通个人的旅客机票搜索 API。 | — | 待实测 |
| [飞猪国内机票开放平台](https://open.alitrip.com/businessDetail.htm?tagId=85) · [资料](./data/candidates/fliggy-domestic-flights.yaml) | 面向机票商家的政策与订单接口，需要企业、代理商身份、店铺和聚石塔；不等同于旅客搜索接口。 | [API](https://open.alitrip.com/businessDetail.htm?tagId=85) | 待实测 |

</details>

## 一起补全这份资料

如果你知道我们漏掉的服务、有想测的真实任务，或发现资料已经过时，欢迎提 Issue 或 PR。提供一条线索、纠正一个事实，都能帮上忙。

[核心理念](./AGENTS.md) · [收录标准](./docs/catalog-standard.zh-CN.md) · [任务设计](./data/experiments/tasks/AGENTS.md) · [执行与验收](./data/experiments/AGENTS.md) · [参与贡献](./docs/contributing.md) · [机票阶段结论](./docs/flights.zh-CN.md)

代码：[MIT](./LICENSE) · 数据：[CC BY 4.0](./LICENSE-DATA)。
