<!-- GENERATED FILE — do not edit. Run `npm run generate`. Source of truth: data/ -->

# Agent-Friendly Services

English | [简体中文](./README.zh-CN.md)

Where AI agents plug into 76 popular services: docs, APIs, official MCP servers, llms.txt, CLIs. Every link machine-probed weekly; every capability fact backed by official evidence and a date ([methodology](./docs/methodology.md)) — plus **[measured agent runs](./generated/agent-runs.md)**: real agents completing real tasks against the live service, independently verified, transcripts included. 🏆 marks the best measured result in a category — held until someone measures better.

![Providers](https://img.shields.io/badge/providers-76-2563eb)
[![Agent-verified](https://img.shields.io/badge/agent--verified-1-10b981)](./generated/agent-runs.md)
[![Link health](https://img.shields.io/badge/link_health-731_ok%2C_0_broken-10b981)](./generated/link-health.json)
[![Last update](https://img.shields.io/github/last-commit/Olorinm/agent-friendly-services?label=last%20update&color=8b5cf6)](https://github.com/Olorinm/agent-friendly-services/commits/main)
[![Data: CC BY 4.0](https://img.shields.io/badge/data-CC_BY_4.0-64748b)](./LICENSE-DATA)

**🤖 Agents** — add the MCP server, or fetch the whole dataset as one JSON file:

```bash
# MCP server — tools: search_providers, get_provider, list_categories, get_stats
claude mcp add agent-friendly-services -- npx -y github:Olorinm/agent-friendly-services

# Or skip the server: the same data as one JSON file
curl -s https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/providers.json
```

Other MCP clients: command `npx`, args `["-y", "github:Olorinm/agent-friendly-services"]` ([details](./mcp/)). Repo map: [`llms.txt`](./llms.txt) · contribution manual: [`AGENTS.md`](./AGENTS.md).

**🧑‍💻 Humans** — browse below: each name links to the docs, the trailing links are what officially exists (a missing link means "no known URL", not "confirmed absent"). Full fact sheets with evidence and dates: [provider details](./generated/providers.md#providers) · measured runs & route comparison: [agent runs](./generated/agent-runs.md) · spreadsheet: [`matrix.csv`](./generated/matrix.csv).

**🏢 Vendors** — fix your own entry in one PR with documentation (not marketing) as evidence; promotional PRs are declined ([rules](./docs/contributing.md)).

<details open>
<summary><b>Capability matrix</b> — all 76 providers at a glance (✓ supported · ◐ partial · ✗ unsupported · — unknown · Agent: verified routes, h=http c=cli m=mcp)</summary>

**AI Models**

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Anthropic](./generated/providers.md#anthropic) | — | ✓ | — | ✓ | — | ✓ | — | 2026-07-07 |
| [Cartesia](./generated/providers.md#cartesia) | ✓ | ✓ | — | — | — | ✓ | — | 2026-07-08 |
| [Cerebras Inference](./generated/providers.md#cerebras) | — | ✓ | — | — | — | ✓ | — | 2026-07-08 |
| [Cohere](./generated/providers.md#cohere) | — | ✓ | — | — | ◐ | ✓ | — | 2026-07-07 |
| [Deepgram](./generated/providers.md#deepgram) | — | ✓ | ✓ | — | — | ✓ | — | 2026-07-07 |
| [DeepSeek](./generated/providers.md#deepseek) | — | — | — | — | — | ✓ | — | 2026-07-07 |
| [ElevenLabs](./generated/providers.md#elevenlabs) | ✓ | ✓ | ✓ | — | — | ✓ | — | 2026-07-07 |
| [fal.ai](./generated/providers.md#fal) | — | ✓ | — | ✓ | — | ✓ | — | 2026-07-08 |
| [Fireworks AI](./generated/providers.md#fireworks) | — | ✓ | — | ✓ | — | ✓ | — | 2026-07-08 |
| [Gemini API](./generated/providers.md#gemini-api) | — | — | — | ✓ | — | ✓ | — | 2026-07-07 |
| [Groq](./generated/providers.md#groq) | — | ✓ | — | — | — | ✓ | — | 2026-07-07 |
| [Hugging Face](./generated/providers.md#hugging-face) | ✓ | — | — | ✓ | — | ✓ | — | 2026-07-07 |
| [Luma AI (Dream Machine)](./generated/providers.md#luma) | — | ✓ | — | — | — | ✓ | — | 2026-07-08 |
| [MiniMax](./generated/providers.md#minimax) | ✓ | — | — | — | — | ✓ | — | 2026-07-08 |
| [Mistral AI](./generated/providers.md#mistral) | — | ✓ | ✓ | — | — | ✓ | — | 2026-07-07 |
| [Moonshot AI (Kimi)](./generated/providers.md#moonshot) | — | — | — | ✓ | — | ✓ | — | 2026-07-08 |
| [OpenAI](./generated/providers.md#openai) | — | — | ✓ | — | — | ✓ | — | 2026-07-07 |
| [OpenRouter](./generated/providers.md#openrouter) | — | ✓ | — | — | — | ✓ | — | 2026-07-08 |
| [Alibaba Qwen (Model Studio)](./generated/providers.md#qwen) | — | — | — | ✓ | — | ✓ | — | 2026-07-08 |
| [Replicate](./generated/providers.md#replicate) | — | ✓ | — | ✓ | — | ✓ | — | 2026-07-07 |
| [Together AI](./generated/providers.md#together-ai) | — | ✓ | — | — | — | ✓ | — | 2026-07-07 |
| [xAI (Grok API)](./generated/providers.md#xai) | — | ✓ | — | — | — | — | — | 2026-07-08 |
| [Z.ai (GLM)](./generated/providers.md#zai) | — | ✓ | — | — | — | ✓ | — | 2026-07-08 |

**Agent Tooling**

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Composio](./generated/providers.md#composio) | ✓ | ✓ | — | — | — | — | — | 2026-07-07 |
| [Mem0](./generated/providers.md#mem0) | ✓ | ✓ | — | — | ✓ | ✓ | — | 2026-07-08 |
| [n8n](./generated/providers.md#n8n) | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 2026-07-08 |
| [Vapi](./generated/providers.md#vapi) | ✓ | ✓ | — | — | — | ✓ | — | 2026-07-08 |
| [Zapier](./generated/providers.md#zapier) | ✓ | ✓ | — | ✓ | — | ✓ | — | 2026-07-07 |

**Code Execution**

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Browserbase](./generated/providers.md#browserbase) | ✓ | ✓ | — | — | n/a | ✓ | — | 2026-07-07 |
| [E2B](./generated/providers.md#e2b) | ✓ | ✓ | — | ✓ | n/a | ✓ | — | 2026-07-07 |
| [Modal](./generated/providers.md#modal) | — | ✓ | — | ✓ | ✓ | ✓ | — | 2026-07-07 |
| [Steel](./generated/providers.md#steel) | — | ✓ | — | — | ✓ | ✓ | — | 2026-07-08 |

**Developer Tools**

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Atlassian (Jira & Confluence)](./generated/providers.md#atlassian) | ✓ | — | — | ✓ | ◐ | ✓ | — | 2026-07-08 |
| [GitHub](./generated/providers.md#github) | ✓ | ✓ | ✓ | ✓ | — | ✓ | [✓ h·c·m](./generated/agent-runs.md#github) | 2026-07-07 |
| [GitLab](./generated/providers.md#gitlab) | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 2026-07-07 |
| [Postman](./generated/providers.md#postman) | ✓ | ✓ | — | ✓ | — | ✓ | — | 2026-07-07 |

**Cloud / Hosting**

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Cloudflare](./generated/providers.md#cloudflare) | ✓ | ✓ | ✓ | ✓ | ◐ | ✓ | — | 2026-07-07 |
| [Fly.io](./generated/providers.md#fly-io) | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 2026-07-07 |
| [Netlify](./generated/providers.md#netlify) | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 2026-07-07 |
| [Railway](./generated/providers.md#railway) | — | ✓ | — | ✓ | — | ✓ | — | 2026-07-08 |
| [Render](./generated/providers.md#render) | ✓ | ✓ | — | ✓ | — | ✓ | — | 2026-07-08 |
| [Vercel](./generated/providers.md#vercel) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 2026-07-07 |

**Databases**

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Chroma](./generated/providers.md#chroma) | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 2026-07-08 |
| [MongoDB Atlas](./generated/providers.md#mongodb-atlas) | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 2026-07-07 |
| [Neon](./generated/providers.md#neon) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 2026-07-07 |
| [Pinecone](./generated/providers.md#pinecone) | ✓ | ✓ | — | ✓ | — | ✓ | — | 2026-07-07 |
| [Qdrant](./generated/providers.md#qdrant) | ✓ | ✓ | — | — | — | ✓ | — | 2026-07-07 |
| [Redis (Redis Cloud)](./generated/providers.md#redis) | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 2026-07-08 |
| [Supabase](./generated/providers.md#supabase) | ✓ | ✓ | ✓ | ✓ | ◐ | ✓ | — | 2026-07-07 |
| [Upstash](./generated/providers.md#upstash) | ✓ | ✓ | — | ✓ | — | ✓ | — | 2026-07-07 |
| [Weaviate](./generated/providers.md#weaviate) | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 2026-07-08 |

**Web Search / Data**

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Apify](./generated/providers.md#apify) | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 2026-07-07 |
| [Brave Search API](./generated/providers.md#brave-search) | ✓ | — | — | — | — | ✓ | — | 2026-07-07 |
| [Exa](./generated/providers.md#exa) | ✓ | ✓ | — | — | — | ✓ | — | 2026-07-07 |
| [Firecrawl](./generated/providers.md#firecrawl) | ✓ | ✓ | — | — | — | ✓ | — | 2026-07-07 |
| [Jina AI](./generated/providers.md#jina) | ✓ | ✓ | — | — | — | ✓ | — | 2026-07-08 |
| [Perplexity API](./generated/providers.md#perplexity) | ✓ | ✓ | — | — | — | ✓ | — | 2026-07-07 |
| [SerpApi](./generated/providers.md#serpapi) | ✓ | ✓ | — | — | — | ✓ | — | 2026-07-08 |
| [Tavily](./generated/providers.md#tavily) | ✓ | ✓ | — | — | — | ✓ | — | 2026-07-07 |

**Payments / Billing**

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Lemon Squeezy](./generated/providers.md#lemonsqueezy) | — | — | — | — | ✓ | ✓ | — | 2026-07-08 |
| [Paddle](./generated/providers.md#paddle) | ✓ | ✓ | — | — | ✓ | ◐ | — | 2026-07-07 |
| [Stripe](./generated/providers.md#stripe) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 2026-07-07 |

**Communication**

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Discord](./generated/providers.md#discord) | — | — | ✓ | — | — | ✓ | — | 2026-07-07 |
| [Lark](./generated/providers.md#lark) | ✓ | ✓ | — | ✓ | — | ✓ | — | 2026-07-07 |
| [Resend](./generated/providers.md#resend) | ✓ | ✓ | — | — | ✓ | ✓ | — | 2026-07-07 |
| [Slack](./generated/providers.md#slack) | — | ✓ | ✓ | ✓ | — | ✓ | — | 2026-07-07 |
| [Telegram Bot API](./generated/providers.md#telegram) | — | — | — | — | ✓ | ◐ | — | 2026-07-07 |
| [Twilio](./generated/providers.md#twilio) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 2026-07-07 |

**Productivity / Storage**

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Airtable](./generated/providers.md#airtable) | — | — | — | — | — | ✓ | — | 2026-07-07 |
| [Dropbox](./generated/providers.md#dropbox) | — | ✓ | — | ✓ | — | ✓ | — | 2026-07-07 |
| [Linear](./generated/providers.md#linear) | ✓ | ✓ | — | — | — | ✓ | — | 2026-07-07 |
| [Notion](./generated/providers.md#notion) | ✓ | ✓ | — | — | — | ✓ | — | 2026-07-07 |

**Observability / Security**

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Datadog](./generated/providers.md#datadog) | ✓ | ✓ | — | ✓ | — | ✓ | — | 2026-07-07 |
| [Grafana (Grafana Cloud)](./generated/providers.md#grafana) | ✓ | ✓ | — | — | ✓ | ✓ | — | 2026-07-08 |
| [Sentry](./generated/providers.md#sentry) | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 2026-07-07 |

**Commerce / Marketing**

| Provider | MCP | llms.txt | OpenAPI | CLI | Sandbox | Self-serve | Agent | Checked |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Shopify](./generated/providers.md#shopify) | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 2026-07-07 |

</details>

---

[AI Models](#ai-models) · [Agent Tooling](#agent-tooling) · [Code Execution](#code-execution) · [Developer Tools](#developer-tools) · [Cloud / Hosting](#cloud--hosting) · [Databases](#databases) · [Web Search / Data](#web-search--data) · [Payments / Billing](#payments--billing) · [Communication](#communication) · [Productivity / Storage](#productivity--storage) · [Observability / Security](#observability--security) · [Commerce / Marketing](#commerce--marketing)

## AI Models

- **[Anthropic](https://docs.anthropic.com)** — Claude model APIs with agent-focused documentation, llms.txt, and the company behind the MCP standard itself. [API](https://docs.anthropic.com/en/api) · [llms.txt](https://docs.anthropic.com/llms.txt) · [CLI](https://docs.anthropic.com/en/docs/claude-code) · [all facts →](./generated/providers.md#anthropic)
- **[Cartesia](https://docs.cartesia.ai)** — Low-latency voice models (Sonic TTS, Ink STT) with a documented API, official MCP server, llms.txt, and a free tier. [API](https://docs.cartesia.ai/api-reference) · [MCP](https://github.com/cartesia-ai/cartesia-mcp) · [llms.txt](https://docs.cartesia.ai/llms.txt) · [all facts →](./generated/providers.md#cartesia)
- **[Cerebras Inference](https://inference-docs.cerebras.ai)** — Wafer-scale inference for open models at very high tokens/sec, OpenAI-compatible API, llms.txt, and a standing free tier. [API](https://inference-docs.cerebras.ai/api-reference/chat-completions) · [llms.txt](https://inference-docs.cerebras.ai/llms.txt) · [all facts →](./generated/providers.md#cerebras)
- **[Cohere](https://docs.cohere.com)** — Enterprise LLM platform (command, embed, rerank) with llms.txt, documented API versioning, free trial keys, and error/rate-limit docs. [API](https://docs.cohere.com/reference/about) · [llms.txt](https://docs.cohere.com/llms.txt) · [all facts →](./generated/providers.md#cohere)
- **[Deepgram](https://developers.deepgram.com/docs)** — Speech-to-text and voice AI API with a public OpenAPI spec, llms.txt, scoped API keys, and $200 free credit without a card. [API](https://developers.deepgram.com/reference) · [llms.txt](https://developers.deepgram.com/llms.txt) · [OpenAPI](https://github.com/deepgram/deepgram-api-specs) · [all facts →](./generated/providers.md#deepgram)
- **[DeepSeek](https://api-docs.deepseek.com)** — OpenAI-compatible LLM API (DeepSeek-V3/R1) with transparent per-token pricing, a detailed changelog, and self-serve keys. [all facts →](./generated/providers.md#deepseek)
- **[ElevenLabs](https://elevenlabs.io/docs)** — Voice AI (TTS, STT, agents) with a public OpenAPI spec, llms.txt, an official MCP server, and a free tier. [API](https://elevenlabs.io/docs/api-reference/introduction) · [MCP](https://github.com/elevenlabs/elevenlabs-mcp) · [llms.txt](https://elevenlabs.io/docs/llms.txt) · [OpenAPI](https://api.elevenlabs.io/openapi.json) · [all facts →](./generated/providers.md#elevenlabs)
- **[fal.ai](https://fal.ai/docs)** — Generative media platform (image, video, audio models) with queue/streaming APIs, an official CLI/serving framework, llms.txt, and self-serve keys. [API](https://fal.ai/docs/model-apis) · [llms.txt](https://fal.ai/llms.txt) · [CLI](https://github.com/fal-ai/fal) · [all facts →](./generated/providers.md#fal)
- **[Fireworks AI](https://docs.fireworks.ai)** — Fast open-model inference and fine-tuning with an OpenAI-compatible API, official firectl CLI, llms.txt, and published pricing. [API](https://docs.fireworks.ai/api-reference/introduction) · [llms.txt](https://docs.fireworks.ai/llms.txt) · [CLI](https://docs.fireworks.ai/tools-sdks/firectl/firectl) · [all facts →](./generated/providers.md#fireworks)
- **[Gemini API](https://ai.google.dev/gemini-api/docs)** — Google's Gemini model APIs via AI Studio, with generous free tier and documented API versioning. [API](https://ai.google.dev/api) · [CLI](https://github.com/google-gemini/gemini-cli) · [all facts →](./generated/providers.md#gemini-api)
- **[Groq](https://console.groq.com/docs)** — Ultra-low-latency LLM inference with an OpenAI-compatible API, llms.txt, and self-serve keys with a free tier. [API](https://console.groq.com/docs/api-reference) · [llms.txt](https://console.groq.com/llms.txt) · [all facts →](./generated/providers.md#groq)
- **[Hugging Face](https://huggingface.co/docs)** — Model hub and inference platform with fine-grained tokens, OAuth, an official MCP server, and a full Hub API. [API](https://huggingface.co/docs/hub/api) · [MCP](https://huggingface.co/mcp) · [CLI](https://huggingface.co/docs/huggingface_hub/guides/cli) · [all facts →](./generated/providers.md#hugging-face)
- **[Luma AI (Dream Machine)](https://docs.lumalabs.ai)** — Dream Machine video and image generation via the Luma API, with llms.txt and published API pricing. [API](https://docs.lumalabs.ai/reference) · [llms.txt](https://docs.lumalabs.ai/llms.txt) · [all facts →](./generated/providers.md#luma)
- **[MiniMax](https://platform.minimax.io/docs)** — MiniMax text, speech, video and music models via the international platform API, with an official MCP server. [API](https://platform.minimax.io/docs/api-reference) · [MCP](https://github.com/MiniMax-AI/MiniMax-MCP) · [all facts →](./generated/providers.md#minimax)
- **[Mistral AI](https://docs.mistral.ai)** — European LLM provider (La Plateforme) with llms.txt, an open OpenAPI-based docs repo, a free experiment tier, and self-serve keys. [API](https://docs.mistral.ai/api) · [llms.txt](https://docs.mistral.ai/llms.txt) · [OpenAPI](https://github.com/mistralai/platform-docs-public) · [all facts →](./generated/providers.md#mistral)
- **[Moonshot AI (Kimi)](https://platform.kimi.ai/docs)** — Kimi models (K2 line) via an OpenAI-compatible API on the international Kimi platform, with an official terminal CLI agent (kimi-cli). [API](https://platform.kimi.ai/docs/api/chat) · [CLI](https://github.com/MoonshotAI/kimi-cli) · [all facts →](./generated/providers.md#moonshot)
- **[OpenAI](https://platform.openai.com/docs)** — GPT model APIs with an official OpenAPI spec, agents guides, and a large SDK ecosystem. [API](https://platform.openai.com/docs/api-reference) · [OpenAPI](https://github.com/openai/openai-openapi) · [all facts →](./generated/providers.md#openai)
- **[OpenRouter](https://openrouter.ai/docs)** — Unified OpenAI-compatible API over hundreds of models from many labs, with one key, per-model pricing, automatic fallbacks, and an llms.txt. [API](https://openrouter.ai/docs/api-reference/overview) · [llms.txt](https://openrouter.ai/docs/llms.txt) · [all facts →](./generated/providers.md#openrouter)
- **[Alibaba Qwen (Model Studio)](https://www.alibabacloud.com/help/en/model-studio/)** — Qwen model family via Alibaba Cloud Model Studio's OpenAI-compatible API, with an official open-source coding CLI agent (qwen-code). [API](https://www.alibabacloud.com/help/en/model-studio/models) · [CLI](https://github.com/QwenLM/qwen-code) · [all facts →](./generated/providers.md#qwen)
- **[Replicate](https://replicate.com/docs)** — Run and fine-tune open-source models via a simple predictions API, with llms.txt, webhooks, and an official CLI. [API](https://replicate.com/docs/reference/http) · [llms.txt](https://replicate.com/llms.txt) · [CLI](https://github.com/replicate/cli) · [all facts →](./generated/providers.md#replicate)
- **[Together AI](https://docs.together.ai)** — Inference and fine-tuning platform for open-source models with an OpenAI-compatible API and llms.txt. [API](https://docs.together.ai/reference/chat-completions) · [llms.txt](https://docs.together.ai/llms.txt) · [all facts →](./generated/providers.md#together-ai)
- **[xAI (Grok API)](https://docs.x.ai)** — xAI's Grok models via an OpenAI-compatible REST API, with an llms.txt and self-serve console keys. [API](https://docs.x.ai/developers/rest-api-reference/inference) · [llms.txt](https://docs.x.ai/llms.txt) · [all facts →](./generated/providers.md#xai)
- **[Z.ai (GLM)](https://docs.z.ai)** — GLM models via Z.ai's OpenAI-compatible international API, with llms.txt, published pricing, and self-serve keys. [API](https://docs.z.ai/api-reference) · [llms.txt](https://docs.z.ai/llms.txt) · [all facts →](./generated/providers.md#zai)

## Agent Tooling

- **[Composio](https://docs.composio.dev)** — Tool and integration layer for AI agents (hundreds of app connectors with managed auth), with llms.txt and a hosted MCP directory. [MCP](https://mcp.composio.dev) · [llms.txt](https://docs.composio.dev/llms.txt) · [all facts →](./generated/providers.md#composio)
- **[Mem0](https://docs.mem0.ai)** — Memory layer for AI agents (hosted platform + open-source), with REST API, llms.txt, and the official OpenMemory MCP server. [API](https://docs.mem0.ai/api-reference) · [MCP](https://docs.mem0.ai/openmemory/overview) · [llms.txt](https://docs.mem0.ai/llms.txt) · [all facts →](./generated/providers.md#mem0)
- **[n8n](https://docs.n8n.io)** — Workflow automation platform with native AI/agent nodes, a public REST API, official hosted MCP server, CLI, and llms.txt; fair-code and self-hostable. [API](https://docs.n8n.io/api/) · [MCP](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) · [llms.txt](https://docs.n8n.io/llms.txt) · [CLI](https://docs.n8n.io/hosting/cli-commands/) · [all facts →](./generated/providers.md#n8n)
- **[Vapi](https://docs.vapi.ai)** — Voice-agent orchestration API (calls, turn-taking, tool use over phone/web) with an official MCP server and an llms.txt that opens with instructions for AI agents. [API](https://docs.vapi.ai/api-reference) · [MCP](https://github.com/VapiAI/mcp-server) · [llms.txt](https://docs.vapi.ai/llms.txt) · [all facts →](./generated/providers.md#vapi)
- **[Zapier](https://docs.zapier.com)** — Automation platform bridging 7000+ apps, with llms.txt and an official MCP endpoint that gives agents access to those integrations. [MCP](https://zapier.com/mcp) · [llms.txt](https://docs.zapier.com/llms.txt) · [CLI](https://github.com/zapier/zapier-platform) · [all facts →](./generated/providers.md#zapier)

## Code Execution

- **[Browserbase](https://docs.browserbase.com)** — Headless browser infrastructure for AI agents and automation, with session APIs and an official MCP server. [API](https://docs.browserbase.com/reference) · [MCP](https://github.com/browserbase/mcp-server-browserbase) · [llms.txt](https://docs.browserbase.com/llms.txt) · [all facts →](./generated/providers.md#browserbase)
- **[E2B](https://e2b.dev/docs)** — Isolated cloud sandboxes for running AI-generated code, with llms.txt, an official MCP server, and self-serve keys. [MCP](https://github.com/e2b-dev/mcp-server) · [llms.txt](https://e2b.dev/llms.txt) · [CLI](https://e2b.dev/docs/cli) · [all facts →](./generated/providers.md#e2b)
- **[Modal](https://modal.com/docs)** — Serverless compute for Python with first-class Sandboxes for agent code execution, llms.txt, and an official CLI. [API](https://modal.com/docs/reference) · [llms.txt](https://modal.com/llms.txt) · [CLI](https://modal.com/docs/reference/cli) · [all facts →](./generated/providers.md#modal)
- **[Steel](https://docs.steel.dev)** — Cloud browser API for AI agents (sessions, CDP, anti-bot) — open-source and self-hostable, with llms.txt and a free tier. [API](https://docs.steel.dev/api-reference) · [llms.txt](https://docs.steel.dev/llms.txt) · [all facts →](./generated/providers.md#steel)

## Developer Tools

- **[Atlassian (Jira & Confluence)](https://developer.atlassian.com)** — Jira, Confluence and the Atlassian Cloud platform — REST APIs, an official remote MCP server (OAuth 2.1), and the acli CLI. [API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/) · [MCP](https://github.com/atlassian/atlassian-mcp-server) · [CLI](https://developer.atlassian.com/cloud/acli/) · [all facts →](./generated/providers.md#atlassian)
- **[GitHub](https://docs.github.com)** 🏆 — Code hosting, collaboration, and automation with REST and GraphQL APIs, an official CLI, and an official MCP server. [API](https://docs.github.com/rest) · [MCP](https://github.com/github/github-mcp-server) · [llms.txt](https://docs.github.com/llms.txt) · [OpenAPI](https://github.com/github/rest-api-description) · [CLI](https://cli.github.com) · [all facts →](./generated/providers.md#github) · **[🤖✓ agent-verified](./generated/agent-runs.md#github)**
- **[GitLab](https://docs.gitlab.com)** — DevOps platform with REST and GraphQL APIs, scoped tokens, llms.txt, and an official CLI. [API](https://docs.gitlab.com/api/rest/) · [MCP](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server) · [llms.txt](https://docs.gitlab.com/llms.txt) · [OpenAPI](https://docs.gitlab.com/api/openapi/openapi_interactive) · [CLI](https://gitlab.com/gitlab-org/cli) · [all facts →](./generated/providers.md#gitlab)
- **[Postman](https://learning.postman.com)** — API development platform with a public Postman API, llms.txt, official CLI, and self-serve keys. [API](https://learning.postman.com/docs/developer/postman-api/intro-api/) · [MCP](https://github.com/postmanlabs/postman-mcp-server) · [llms.txt](https://learning.postman.com/llms.txt) · [CLI](https://learning.postman.com/docs/postman-cli/postman-cli-overview/) · [all facts →](./generated/providers.md#postman)

## Cloud / Hosting

- **[Cloudflare](https://developers.cloudflare.com)** — Edge network, Workers serverless platform, storage, and AI services with agent-focused docs and official MCP servers. [API](https://developers.cloudflare.com/api/) · [MCP](https://github.com/cloudflare/mcp-server-cloudflare) · [llms.txt](https://developers.cloudflare.com/llms.txt) · [OpenAPI](https://github.com/cloudflare/api-schemas) · [CLI](https://developers.cloudflare.com/workers/wrangler/) · [all facts →](./generated/providers.md#cloudflare)
- **[Fly.io](https://fly.io/docs)** — Run full-stack apps and machines close to users, with a spec'd Machines API, scoped macaroon tokens, and official MCP docs. [API](https://fly.io/docs/machines/api/) · [MCP](https://fly.io/docs/mcp/) · [llms.txt](https://fly.io/llms.txt) · [OpenAPI](https://docs.machines.dev) · [CLI](https://fly.io/docs/flyctl/) · [all facts →](./generated/providers.md#fly-io)
- **[Netlify](https://docs.netlify.com)** — Web platform for deploying sites and functions, with an OpenAPI-specified API, llms.txt, official CLI and MCP server. [API](https://open-api.netlify.com) · [MCP](https://docs.netlify.com/welcome/build-with-ai/netlify-mcp-server/) · [llms.txt](https://docs.netlify.com/llms.txt) · [OpenAPI](https://github.com/netlify/open-api) · [CLI](https://docs.netlify.com/cli/get-started/) · [all facts →](./generated/providers.md#netlify)
- **[Railway](https://docs.railway.com)** — App/database hosting with a public GraphQL API, official CLI, llms.txt, and usage-based pricing. [API](https://docs.railway.com/reference/public-api) · [llms.txt](https://docs.railway.com/llms.txt) · [CLI](https://github.com/railwayapp/cli) · [all facts →](./generated/providers.md#railway)
- **[Render](https://render.com/docs)** — Cloud hosting for web services, static sites and databases with a REST API, official CLI, official MCP server, and llms.txt. [API](https://api-docs.render.com/reference/introduction) · [MCP](https://github.com/render-oss/render-mcp-server) · [llms.txt](https://render.com/docs/llms.txt) · [CLI](https://github.com/render-oss/cli) · [all facts →](./generated/providers.md#render)
- **[Vercel](https://vercel.com/docs)** — Frontend cloud for deploying web apps, with a REST API, CLI, official MCP server, and AI SDK ecosystem. [API](https://vercel.com/docs/rest-api) · [MCP](https://vercel.com/docs/mcp/vercel-mcp) · [llms.txt](https://vercel.com/llms.txt) · [OpenAPI](https://openapi.vercel.sh) · [CLI](https://vercel.com/docs/cli) · [all facts →](./generated/providers.md#vercel)

## Databases

- **[Chroma](https://docs.trychroma.com)** — Open-source embedding database with a hosted Chroma Cloud, official CLI, official MCP server, and llms.txt. [API](https://docs.trychroma.com/docs/overview/introduction) · [MCP](https://github.com/chroma-core/chroma-mcp) · [llms.txt](https://docs.trychroma.com/llms.txt) · [CLI](https://docs.trychroma.com/docs/cli/install) · [all facts →](./generated/providers.md#chroma)
- **[MongoDB Atlas](https://www.mongodb.com/docs/atlas/)** — Managed MongoDB with a versioned Admin API, published OpenAPI spec, llms.txt, official CLI and MCP server. [API](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/) · [MCP](https://github.com/mongodb-js/mongodb-mcp-server) · [llms.txt](https://www.mongodb.com/docs/llms.txt) · [OpenAPI](https://github.com/mongodb/openapi) · [CLI](https://www.mongodb.com/docs/atlas/cli/) · [all facts →](./generated/providers.md#mongodb-atlas)
- **[Neon](https://neon.com/docs)** — Serverless Postgres with instant branching, a full management API, official MCP server, and agent-oriented docs. [API](https://api-docs.neon.tech) · [MCP](https://github.com/neondatabase/mcp-server-neon) · [llms.txt](https://neon.com/llms.txt) · [OpenAPI](https://neon.tech/api_spec/release/v2.json) · [CLI](https://neon.com/docs/reference/neon-cli) · [all facts →](./generated/providers.md#neon)
- **[Pinecone](https://docs.pinecone.io)** — Managed vector database for search and RAG, with llms.txt, an official MCP server, and self-serve keys. [API](https://docs.pinecone.io/reference/api/introduction) · [MCP](https://docs.pinecone.io/guides/operations/mcp-server) · [llms.txt](https://docs.pinecone.io/llms.txt) · [CLI](https://github.com/pinecone-io/cli) · [all facts →](./generated/providers.md#pinecone)
- **[Qdrant](https://qdrant.tech/documentation)** — Open-source vector database with a managed cloud, llms.txt, an official MCP server, and a free cluster tier. [API](https://api.qdrant.tech) · [MCP](https://github.com/qdrant/mcp-server-qdrant) · [llms.txt](https://qdrant.tech/llms.txt) · [all facts →](./generated/providers.md#qdrant)
- **[Redis (Redis Cloud)](https://redis.io/docs/latest)** — In-memory data platform for caching, vector search and real-time apps; Redis Cloud has a REST management API, official MCP server, redis-cli, and llms.txt. [API](https://redis.io/docs/latest/operate/rc/api/) · [MCP](https://github.com/redis/mcp-redis) · [llms.txt](https://redis.io/llms.txt) · [CLI](https://redis.io/docs/latest/develop/tools/cli/) · [all facts →](./generated/providers.md#redis)
- **[Supabase](https://supabase.com/docs)** — Postgres platform with auth, storage, edge functions, a management API, official MCP server, and LLM-ready docs. [API](https://supabase.com/docs/reference/api/introduction) · [MCP](https://supabase.com/docs/guides/getting-started/mcp) · [llms.txt](https://supabase.com/llms.txt) · [OpenAPI](https://api.supabase.com/api/v1-json) · [CLI](https://supabase.com/docs/guides/cli) · [all facts →](./generated/providers.md#supabase)
- **[Upstash](https://upstash.com/docs)** — Serverless Redis, Kafka-successor queues, and vector storage with REST APIs, llms.txt, an official MCP server, and a free tier. [API](https://upstash.com/docs/devops/developer-api/introduction) · [MCP](https://github.com/upstash/mcp-server) · [llms.txt](https://upstash.com/docs/llms.txt) · [CLI](https://github.com/upstash/cli) · [all facts →](./generated/providers.md#upstash)
- **[Weaviate](https://docs.weaviate.io)** — Open-source vector database with REST/GraphQL/gRPC APIs, Weaviate Cloud free sandboxes, an official CLI, MCP server, and llms.txt. [API](https://docs.weaviate.io/weaviate/api/rest) · [MCP](https://github.com/weaviate/mcp-server-weaviate) · [llms.txt](https://docs.weaviate.io/llms.txt) · [CLI](https://github.com/weaviate/weaviate-cli) · [all facts →](./generated/providers.md#weaviate)

## Web Search / Data

- **[Apify](https://docs.apify.com)** — Web scraping and automation platform with thousands of ready-made actors, a versioned API, llms.txt, and an official MCP server. [API](https://docs.apify.com/api/v2) · [MCP](https://docs.apify.com/platform/integrations/mcp) · [llms.txt](https://docs.apify.com/llms.txt) · [OpenAPI](https://docs.apify.com/api/openapi.json) · [CLI](https://docs.apify.com/cli) · [all facts →](./generated/providers.md#apify)
- **[Brave Search API](https://api-dashboard.search.brave.com/app/documentation)** — Independent web search index with a developer API, self-serve registration, and a free plan. [MCP](https://github.com/brave/brave-search-mcp-server) · [all facts →](./generated/providers.md#brave-search)
- **[Exa](https://docs.exa.ai)** — Search API built for AI — semantic web search, content retrieval, and research endpoints with an official MCP server. [API](https://docs.exa.ai/reference/getting-started) · [MCP](https://github.com/exa-labs/exa-mcp-server) · [llms.txt](https://docs.exa.ai/llms.txt) · [all facts →](./generated/providers.md#exa)
- **[Firecrawl](https://docs.firecrawl.dev)** — Web scraping and crawling API that turns websites into LLM-ready markdown, with an official MCP server. [API](https://docs.firecrawl.dev/api-reference/introduction) · [MCP](https://docs.firecrawl.dev/mcp-server) · [llms.txt](https://docs.firecrawl.dev/llms.txt) · [all facts →](./generated/providers.md#firecrawl)
- **[Jina AI](https://docs.jina.ai)** — Search-foundation APIs (Reader for URL-to-markdown, embeddings, reranker, deep search) with an official remote MCP server, an agent-targeted llms.txt, and a keyless trial path. [API](https://docs.jina.ai) · [MCP](https://github.com/jina-ai/MCP) · [llms.txt](https://docs.jina.ai/llms.txt) · [all facts →](./generated/providers.md#jina)
- **[Perplexity API](https://docs.perplexity.ai)** — Sonar API for web-grounded answers and search, with llms.txt, an official MCP server, and documented usage tiers. [MCP](https://github.com/ppl-ai/modelcontextprotocol) · [llms.txt](https://docs.perplexity.ai/llms.txt) · [all facts →](./generated/providers.md#perplexity)
- **[SerpApi](https://serpapi.com/search-api)** — Real-time JSON API for Google and other search engines' results, with an official MCP server, llms.txt, and a free monthly quota. [API](https://serpapi.com/search-api) · [MCP](https://github.com/serpapi/serpapi-mcp) · [llms.txt](https://serpapi.com/llms.txt) · [all facts →](./generated/providers.md#serpapi)
- **[Tavily](https://docs.tavily.com)** — Search and extraction API built for AI agents, with llms.txt, an official MCP server, and a free tier. [API](https://docs.tavily.com/documentation/api-reference/introduction) · [MCP](https://docs.tavily.com/documentation/mcp) · [llms.txt](https://docs.tavily.com/llms.txt) · [all facts →](./generated/providers.md#tavily)

## Payments / Billing

- **[Lemon Squeezy](https://docs.lemonsqueezy.com)** — Merchant-of-record payments for digital products/SaaS with a JSON:API REST API, documented test mode, and self-serve keys. [API](https://docs.lemonsqueezy.com/api) · [all facts →](./generated/providers.md#lemonsqueezy)
- **[Paddle](https://developer.paddle.com)** — Merchant-of-record billing platform with a versioned API, full sandbox, llms.txt, and webhooks. [API](https://developer.paddle.com/api-reference/overview) · [MCP](https://github.com/PaddleHQ/paddle-mcp-server) · [llms.txt](https://developer.paddle.com/llms.txt) · [all facts →](./generated/providers.md#paddle)
- **[Stripe](https://docs.stripe.com)** — Payments, billing, subscriptions, and financial infrastructure with a famously complete API surface. [API](https://docs.stripe.com/api) · [MCP](https://docs.stripe.com/mcp) · [llms.txt](https://docs.stripe.com/llms.txt) · [OpenAPI](https://github.com/stripe/openapi) · [CLI](https://docs.stripe.com/stripe-cli) · [all facts →](./generated/providers.md#stripe)

## Communication

- **[Discord](https://discord.com/developers/docs/intro)** — Chat platform with a versioned bot/OAuth2 API, official OpenAPI spec (preview), webhooks, and documented rate limits. [API](https://discord.com/developers/docs/reference) · [OpenAPI](https://github.com/discord/discord-api-spec) · [all facts →](./generated/providers.md#discord)
- **[Lark](https://open.larksuite.com/document/home/index)** — Collaboration suite (messaging, docs, calendar) with an open platform, llms.txt, an official CLI with 200+ commands and agent skills, and an official OpenAPI MCP server. [API](https://open.larksuite.com/document/server-docs/getting-started/server-api-list) · [MCP](https://github.com/larksuite/lark-openapi-mcp) · [llms.txt](https://open.larksuite.com/llms.txt) · [CLI](https://github.com/larksuite/cli) · [all facts →](./generated/providers.md#lark)
- **[Resend](https://resend.com/docs)** — Email API for developers with test mode, scoped API keys, idempotency support, and an official MCP server. [API](https://resend.com/docs/api-reference/introduction) · [MCP](https://github.com/resend/mcp-send-email) · [llms.txt](https://resend.com/llms.txt) · [all facts →](./generated/providers.md#resend)
- **[Slack](https://api.slack.com)** — Workspace messaging platform with a mature Web API, granular OAuth scopes, an OpenAPI spec, and llms.txt. [API](https://api.slack.com/methods) · [llms.txt](https://docs.slack.dev/llms.txt) · [OpenAPI](https://github.com/slackapi/slack-api-specs) · [CLI](https://docs.slack.dev/tools/slack-cli) · [all facts →](./generated/providers.md#slack)
- **[Telegram Bot API](https://core.telegram.org/bots)** — Free bot platform with instant token issuance via BotFather, webhooks, a documented test environment, and a detailed changelog. [API](https://core.telegram.org/bots/api) · [all facts →](./generated/providers.md#telegram)
- **[Twilio](https://www.twilio.com/docs)** — Programmable messaging and voice APIs with test credentials, an OpenAPI spec, llms.txt, and an official CLI. [API](https://www.twilio.com/docs/usage/api) · [MCP](https://github.com/twilio-labs/mcp) · [llms.txt](https://www.twilio.com/docs/llms.txt) · [OpenAPI](https://github.com/twilio/twilio-oai) · [CLI](https://www.twilio.com/docs/twilio-cli) · [all facts →](./generated/providers.md#twilio)

## Productivity / Storage

- **[Airtable](https://airtable.com/developers)** — Spreadsheet-database hybrid with a REST API, scoped personal access tokens, OAuth, webhooks, and documented rate limits. [API](https://airtable.com/developers/web/api/introduction) · [all facts →](./generated/providers.md#airtable)
- **[Dropbox](https://www.dropbox.com/developers/documentation)** — File storage and sync with a scoped-OAuth HTTP API, self-serve app creation, and webhooks. [API](https://www.dropbox.com/developers/documentation/http/documentation) · [llms.txt](https://www.dropbox.com/llms.txt) · [CLI](https://github.com/dropbox/dbxcli) · [all facts →](./generated/providers.md#dropbox)
- **[Linear](https://linear.app/developers)** — Issue tracking and product planning with a GraphQL API, llms.txt, an official MCP server, and webhooks. [GraphQL](https://linear.app/developers/graphql) · [MCP](https://linear.app/docs/mcp) · [llms.txt](https://linear.app/llms.txt) · [all facts →](./generated/providers.md#linear)
- **[Notion](https://developers.notion.com)** — Connected workspace with a versioned REST API, capability-scoped integrations, llms.txt, and an official MCP server. [API](https://developers.notion.com/reference/intro) · [MCP](https://developers.notion.com/docs/mcp) · [llms.txt](https://developers.notion.com/llms.txt) · [all facts →](./generated/providers.md#notion)

## Observability / Security

- **[Datadog](https://docs.datadoghq.com)** — Observability platform with a full REST API, llms.txt, documented OAuth for integrations, rate limits, and webhooks. [API](https://docs.datadoghq.com/api/latest/) · [MCP](https://docs.datadoghq.com/bits_ai/mcp_server) · [llms.txt](https://docs.datadoghq.com/llms.txt) · [CLI](https://github.com/DataDog/datadog-ci) · [all facts →](./generated/providers.md#datadog)
- **[Grafana (Grafana Cloud)](https://grafana.com/docs)** — Observability platform (dashboards, metrics, logs, traces) with a documented HTTP API, official MCP server, llms.txt, and a standing free cloud tier. [API](https://grafana.com/docs/grafana/latest/developers/http_api/) · [MCP](https://github.com/grafana/mcp-grafana) · [llms.txt](https://grafana.com/llms.txt) · [all facts →](./generated/providers.md#grafana)
- **[Sentry](https://docs.sentry.io)** — Error monitoring and performance tracing with llms.txt, an official MCP server, scoped auth tokens, and a full API. [API](https://docs.sentry.io/api/) · [MCP](https://docs.sentry.io/product/sentry-mcp/) · [llms.txt](https://docs.sentry.io/llms.txt) · [OpenAPI](https://github.com/getsentry/sentry-api-schema) · [CLI](https://docs.sentry.io/cli/) · [all facts →](./generated/providers.md#sentry)

## Commerce / Marketing

- **[Shopify](https://shopify.dev/docs)** — Commerce platform with versioned GraphQL APIs, llms.txt, official MCP docs, access-scoped tokens, free development stores, and a CLI. [API](https://shopify.dev/docs/api) · [MCP](https://shopify.dev/docs/apps/build/storefront-mcp) · [llms.txt](https://www.shopify.com/llms.txt) · [CLI](https://shopify.dev/docs/api/shopify-cli) · [all facts →](./generated/providers.md#shopify)

## Contributing

One fact = one contribution: report a broken link (2 min, [issue form](../../issues/new/choose)) · resolve one of the **497 open `unknown`s** (15 min) · add a provider (1–2 h, [inclusion rules](./docs/methodology.md#inclusion-rules)). CI validates everything mechanical; humans only review evidence quality. Full guide: [`docs/contributing.md`](./docs/contributing.md).

Have a coding agent? Point it at a checkout and paste:

```text
Read AGENTS.md, then resolve one "unknown" check: find official evidence, update
the provider YAML (or leave it unknown if evidence is genuinely missing), run
npm run validate, and open a small PR.
```

## Related

[Fern Agent Score](https://buildwithfern.com/agent-score) (docs-site readiness scoring — we deliberately don't duplicate it) · [Cloudflare Agent Readiness](https://blog.cloudflare.com/agent-readiness/) · [official MCP Registry](https://registry.modelcontextprotocol.io/) · [llms.txt hub](https://llmstxthub.com/)

## License

Code: [MIT](./LICENSE) · Data (`data/`, `generated/`): [CC BY 4.0](./LICENSE-DATA)
