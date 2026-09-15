<!-- GENERATED FILE — do not edit. -->
# Service discovery catalog

Access, requirements and published costs below are **public-source claims**. Source URLs and per-fact dates are in each linked YAML and [catalog.json](./catalog.json). Separately reviewed task observations appear in the last column and the [results table](./evaluations.md); they do not certify other routes or tasks. Missing routes/fields mean unknown. See the [collection standard](../docs/catalog-standard.zh-CN.md).

Each row is an access route, not an independent data supplier. Services without an established route remain discoverable. No cost/quality ranking is implied.


<a id="ai-models"></a>

## AI Services

Services for accessing models and generating or processing content; compare access providers using a shared model or content services using a specific user task.

**Includes:** Provides model inference or generated/processed content.

**Boundary:** A directory of models or agent connectors alone is insufficient.

[Model Access](#ai-models-model-access) · [Speech Synthesis](#ai-models-speech-synthesis) · [Speech Recognition](#ai-models-speech-recognition) · [Image Generation](#ai-models-image-generation) · [Video Generation](#ai-models-video-generation)

<a id="ai-models-model-access"></a>

## AI Services / Model Access

Access a model through its provider or an inference/router service. Compare only a shared model version and matched request settings; this is not a model-quality leaderboard.

**Includes:** Accepts inference requests for identifiable models.

**Boundary:** Merely listing models or returning search snippets is insufficient; compare the same model and settings.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [AgentServices](../data/candidates/agentservices.yaml) | web-search-data/web-search, web-search-data/web-extraction, ai-models/model-access, web-search-data/financial-data/prices | [rest-api (api)](https://api.agentservices.to/) | unknown | self_serve | documented | Requirements incomplete; Buyer guide names api.agentservices.to as the API host; agentservices.to serves the inspected documentation. The free-price example is distinct from a paid data result. An HTTP 402 challenge would establish quoted terms only, not delivery or settlement. Paid prices remain unresolved. | not recorded |
| [AgentServices](../data/candidates/agentservices.yaml) | web-search-data/web-search, web-search-data/web-extraction, ai-models/model-access, web-search-data/financial-data/prices | [official-mcp (mcp)](https://agentservices.to/mcp) | unknown | self_serve | documented | Requirements incomplete; Protocol configuration is documented, not executed here. MCP discovery, a free tool call and fulfillment of a paid tool are separate checks; neither MCP support nor a registry listing establishes hosted-service terms or read-only behavior for every tool. | not recorded |
| [AgentServices](../data/candidates/agentservices.yaml) | web-search-data/web-search, web-search-data/web-extraction, ai-models/model-access, web-search-data/financial-data/prices | [javascript-sdk (sdk)](https://github.com/vbkotecha/agentservices-api/tree/main/sdk) | unknown | self_serve | documented | Requirements incomplete; Package installation and execution were not tested. SDK price examples are indicative, and a payment challenge surfaced by the client is not a successful paid result. | not recorded |
| [Anthropic](../data/providers/anthropic.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Cerebras Inference](../data/providers/cerebras.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Cohere](../data/providers/cohere.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [DeepSeek](../data/providers/deepseek.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [fal.ai](../data/providers/fal.yaml) | ai-models/model-access, ai-models/image-generation, ai-models/video-generation | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Fireworks AI](../data/providers/fireworks.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Gemini API](../data/providers/gemini-api.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Groq](../data/providers/groq.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Hugging Face](../data/providers/hugging-face.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [MiniMax](../data/providers/minimax.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Mistral AI](../data/providers/mistral.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Moonshot AI (Kimi)](../data/providers/moonshot.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [OpenAI](../data/providers/openai.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [OpenRouter](../data/providers/openrouter.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Alibaba Qwen (Model Studio)](../data/providers/qwen.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Replicate](../data/providers/replicate.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Together AI](../data/providers/together-ai.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [xAI (Grok API)](../data/providers/xai.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [XiuRouter](../data/candidates/xiurouter.yaml) | ai-models/model-access | [model-api (api)](https://router-api.xiu.ai) | unknown | unknown | unknown | Requires: platform_account; Documents Chat Completions, Responses, Messages and Gemini GenerateContent. The exact model, account group and protocol must match; ordinary text support does not establish tool compatibility. Responses storage, previous_response_id and background mode are outside the documented scope; Gemini Interactions, Files and fine-tuning are also excluded. Keys can restrict models, quota, expiration and IP access. No signup, authentication or model request was performed for this review. | not recorded |
| [XiuRouter](../data/candidates/xiurouter.yaml) | ai-models/model-access | [vercel-ai-sdk (sdk)](https://docs.xiu.ai/router/integrations/vercel-ai-sdk/) | unknown | unknown | unknown | Requirements incomplete; The supplier guide installs ai and @ai-sdk/openai-compatible and configures a server-side client for the Chat Completions API. This is a third-party client path, not a XiuRouter-owned SDK or an independent service. Text, streaming and tool behavior remain untested. | not recorded |
| [Z.ai (GLM)](../data/providers/zai.yaml) | ai-models/model-access | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="ai-models-speech-synthesis"></a>

## AI Services / Speech Synthesis

Generate spoken audio from supplied text.

**Includes:** Returns playable speech corresponding to supplied text.

**Boundary:** Transcription and voice-call orchestration alone are separate.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Cartesia](../data/providers/cartesia.yaml) | ai-models/speech-synthesis, ai-models/speech-recognition, communication/voice-agents | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Deepgram](../data/providers/deepgram.yaml) | ai-models/speech-recognition, ai-models/speech-synthesis, communication/voice-agents | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [ElevenLabs](../data/providers/elevenlabs.yaml) | ai-models/speech-synthesis, ai-models/speech-recognition, communication/voice-agents | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="ai-models-speech-recognition"></a>

## AI Services / Speech Recognition

Transcribe supplied recordings or live speech.

**Includes:** Returns text derived from supplied speech.

**Boundary:** Audio generation and call transport alone do not qualify.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Cartesia](../data/providers/cartesia.yaml) | ai-models/speech-synthesis, ai-models/speech-recognition, communication/voice-agents | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Deepgram](../data/providers/deepgram.yaml) | ai-models/speech-recognition, ai-models/speech-synthesis, communication/voice-agents | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [ElevenLabs](../data/providers/elevenlabs.yaml) | ai-models/speech-synthesis, ai-models/speech-recognition, communication/voice-agents | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="ai-models-image-generation"></a>

## AI Services / Image Generation

Generate or transform images from a prompt or reference.

**Includes:** Delivers a generated or edited image.

**Boundary:** Image search, hosting and vector retrieval alone do not qualify.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [fal.ai](../data/providers/fal.yaml) | ai-models/model-access, ai-models/image-generation, ai-models/video-generation | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Luma AI (Dream Machine)](../data/providers/luma.yaml) | ai-models/image-generation, ai-models/video-generation | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="ai-models-video-generation"></a>

## AI Services / Video Generation

Generate video from a prompt or reference media.

**Includes:** Delivers generated video frames as a clip.

**Boundary:** Video storage, transcription and playback alone do not qualify.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [fal.ai](../data/providers/fal.yaml) | ai-models/model-access, ai-models/image-generation, ai-models/video-generation | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Luma AI (Dream Machine)](../data/providers/luma.yaml) | ai-models/image-generation, ai-models/video-generation | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="agent-tooling"></a>

## Agent Infrastructure & Automation

Agent memory, tool connections, workflow execution and discovery infrastructure.

**Includes:** Provides reusable infrastructure for building or operating agents and cross-service automation.

**Boundary:** A service exposing an MCP endpoint alone does not belong here.

[Agent Memory](#agent-tooling-memory) · [Tool Connections](#agent-tooling-tool-integrations) · [Workflow Automation](#agent-tooling-workflow-automation)

| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Cog Depot](../data/candidates/cog-depot.yaml) | agent-tooling | [marketplace-api (api)](https://api.cogdepot.com) | unknown | self_serve | unknown | Requirements incomplete; 20000 credits / eligible account (free_allowance; Web signup receives the grant immediately; API signup starts at zero and must verify domain control, once per domain and account. Granted credits are not cash or measured savings.); 1 credits / billable listing request (usage; Published metering for posting a listing, a feed page or an individual listing read; pricing explicitly values one credit at USD 0.0005.); 200 credits / posted listing (usage; Posting fee in addition to the metered request. Unfunded accounts have a lifetime limit of three listings regardless of granted balance.); 2000 credits / party per sealed deal (usage; The opener reserves this platform fee when a thread opens; capture occurs at seal, when the poster also pays. The underlying service purchase is separate.); 0.5 USD / smallest listed x402 credit pack (minimum_spend; Published equivalent for 1000 credits paid in USDC on Base; insufficient by itself for the 2000-credit deal fee. Not a required signup payment or observed expenditure.); Human: Complete email, Google or GitHub web signup and transfer the issued key to the agent.; Registration alone does not establish readiness to trade. Negotiation needs enough credits for its fee hold; x402-funded accounts receive no welcome grant merely for paying. | not recorded |
| [Cog Depot](../data/candidates/cog-depot.yaml) | agent-tooling | [marketplace-a2a (api)](https://api.cogdepot.com/a2a) | unknown | unknown | unknown | Requirements incomplete; Official docs describe A2A v1.0 over JSON-RPC and the Agent Card at /.well-known/agent-card.json. Authentication details and protocol conformance were not independently verified; no task result is implied. | not recorded |
| [Cog Depot](../data/candidates/cog-depot.yaml) | agent-tooling | [marketplace-mcp-local (mcp)](https://github.com/cogdepot/mcp-server) | unknown | self_serve | unknown | Requirements incomplete; Local stdio wrapper published as @cogdepot/mcp-server, started with npx. A preview has no search or pagination; the full feed is charged. Uses the same service credits; no local installation or task was tested. | not recorded |
| [Cog Depot](../data/candidates/cog-depot.yaml) | agent-tooling | [marketplace-mcp-remote (mcp)](https://mcp.cogdepot.com) | unknown | self_serve | unknown | Requirements incomplete; Human: Sign in and authorize the hosted MCP connector.; Hosted OAuth documents action-scoped access, unlike the original PR's account-key-only description. This does not establish scopes for static API keys or imply tested authorization behavior. | not recorded |

<a id="agent-tooling-memory"></a>

## Agent Infrastructure & Automation / Agent Memory

Retain and retrieve agent context across interactions.

**Includes:** Provides persistent memory management and retrieval for an agent.

**Boundary:** Raw vector storage alone does not establish a managed memory service.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Mem0](../data/providers/mem0.yaml) | agent-tooling/memory | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="agent-tooling-tool-integrations"></a>

## Agent Infrastructure & Automation / Tool Connections

Connect an agent to actions in external applications.

**Includes:** Provides callable application actions and connection/authentication management.

**Boundary:** A static directory or one product with its own MCP server is insufficient.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Composio](../data/providers/composio.yaml) | agent-tooling/tool-integrations | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Zapier](../data/providers/zapier.yaml) | agent-tooling/tool-integrations, agent-tooling/workflow-automation | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="agent-tooling-workflow-automation"></a>

## Agent Infrastructure & Automation / Workflow Automation

Run repeatable sequences across tools or services.

**Includes:** Defines and executes workflows with triggers or ordered steps.

**Boundary:** A single connector or a library of templates without execution is insufficient.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [n8n](../data/providers/n8n.yaml) | agent-tooling/workflow-automation | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Zapier](../data/providers/zapier.yaml) | agent-tooling/tool-integrations, agent-tooling/workflow-automation | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="developer-tools"></a>

## Developer Tools

Code hosting, API development, testing, monitoring and troubleshooting.

**Includes:** Supports software development, repository collaboration, API development or operational diagnosis.

**Boundary:** Hosting runtime and application storage are classified separately.

[Monitoring & Troubleshooting](#developer-tools-monitoring) · [Code Hosting & Review](#developer-tools-code-hosting) · [API Development & Testing](#developer-tools-api-development)

<a id="developer-tools-monitoring"></a>

## Developer Tools / Monitoring & Troubleshooting

Collect and retrieve application errors, logs and performance evidence to diagnose problems.

**Includes:** Collects or retrieves operational errors, logs or performance evidence.

**Boundary:** A status page alone does not establish an application monitoring service.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Datadog](../data/providers/datadog.yaml) | developer-tools/monitoring | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Grafana (Grafana Cloud)](../data/providers/grafana.yaml) | developer-tools/monitoring | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Sentry](../data/providers/sentry.yaml) | developer-tools/monitoring | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="developer-tools-code-hosting"></a>

## Developer Tools / Code Hosting & Review

Host versioned code and collaborate on changes.

**Includes:** Provides repositories and a contribution/review workflow.

**Boundary:** Issue tracking alone belongs under project management.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Atlassian (Jira & Confluence)](../data/providers/atlassian.yaml) | developer-tools/code-hosting, productivity-storage/project-management, productivity-storage/document-collaboration | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [GitHub](../data/providers/github.yaml) | developer-tools/code-hosting, productivity-storage/project-management | [rest-api (api)](https://api.github.com/) | unknown | self_serve | documented | Requirements incomplete; Authenticated REST access; existing account setup and token permissions must be recorded separately from the task. | not recorded |
| [GitLab](../data/providers/gitlab.yaml) | developer-tools/code-hosting, productivity-storage/project-management | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="developer-tools-api-development"></a>

## Developer Tools / API Development & Testing

Build, organize and test API interactions.

**Includes:** Provides reusable API requests, collections or test execution.

**Boundary:** Merely offering a public API does not qualify.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Postman](../data/providers/postman.yaml) | developer-tools/api-development | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="cloud-hosting"></a>

## Cloud Computing & Hosting

Cloud runtime environments and hosting for code, browsers and applications.

**Includes:** Provides an environment for running code, browser sessions or deployed applications.

**Boundary:** A storage-only service belongs under databases; remote browser execution is not web search.

[Code Sandboxes](#cloud-hosting-code-sandboxes) · [Browser Environments](#cloud-hosting-browser-environments) · [Application Hosting](#cloud-hosting-app-hosting)

<a id="cloud-hosting-code-sandboxes"></a>

## Cloud Computing & Hosting / Code Sandboxes

Run code and process files in an isolated temporary environment.

**Includes:** Runs supplied code in an isolated execution environment.

**Boundary:** A model returning code without executing it is insufficient.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [E2B](../data/providers/e2b.yaml) | cloud-hosting/code-sandboxes | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Modal](../data/providers/modal.yaml) | cloud-hosting/code-sandboxes | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="cloud-hosting-browser-environments"></a>

## Cloud Computing & Hosting / Browser Environments

Create a remote browser session and execute browser operations.

**Includes:** Provides a controllable browser session.

**Boundary:** Fetching page text without browser control belongs under web extraction.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Browserbase](../data/providers/browserbase.yaml) | cloud-hosting/browser-environments | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Steel](../data/providers/steel.yaml) | cloud-hosting/browser-environments | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="cloud-hosting-app-hosting"></a>

## Cloud Computing & Hosting / Application Hosting

Deploy a website or application and keep it available at a public endpoint.

**Includes:** Deploys an application to an address reachable by its intended users.

**Boundary:** Temporary code execution without a deployed application is insufficient.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [d1-cli (cli)](https://developers.cloudflare.com/d1/get-started/) | unknown | self_serve | documented | Requirements incomplete; 5 GB / account (free_allowance; D1 total storage on Workers Free; separate daily row quotas.); D1 Workers Free: 5 million reads/day, 100,000 writes/day, 5 GB total storage. Account authorization required; Wrangler local mode is not a remote database test. Existing paid projects are excluded. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [kv-api (api)](https://api.cloudflare.com/client/v4/) | unknown | self_serve | unknown | Requirements incomplete; Documented remote Workers KV key-value read API. Requires account and namespace identifiers and credentials with permission for the requested operation. No task success is claimed. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [kv-sdk (sdk)](https://developers.cloudflare.com/api/typescript/resources/kv/subresources/namespaces/subresources/values/methods/get/) | unknown | self_serve | unknown | Requirements incomplete; Official cloudflare TypeScript client exposes remote KV namespace and value methods. Local package installation is distinct from obtaining credentials and remote resource access. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [kv-cli (cli)](https://developers.cloudflare.com/kv/reference/kv-commands/) | unknown | self_serve | unknown | Requirements incomplete; Wrangler provides native KV namespace, key-list and key-read commands. Remote storage must be selected for comparison with cloud API/SDK/MCP; local simulation is not equivalent. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [api-mcp (mcp)](https://mcp.cloudflare.com/mcp) | unknown | self_serve | unknown | Requirements incomplete; Official remote API MCP exposes search and execute tools for Cloudflare API operations, including KV. Record the actual exposed tools and native MCP calls separately from raw HTTP. An existing Wrangler OAuth login is not assumed to authorize this endpoint. | not recorded |
| [Fly.io](../data/providers/fly-io.yaml) | cloud-hosting/app-hosting | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Netlify](../data/providers/netlify.yaml) | cloud-hosting/app-hosting | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Railway](../data/providers/railway.yaml) | cloud-hosting/app-hosting | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Render](../data/providers/render.yaml) | cloud-hosting/app-hosting | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Vercel](../data/providers/vercel.yaml) | cloud-hosting/app-hosting | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="databases"></a>

## Databases

Databases, vector stores, data platforms.

**Includes:** Stores and retrieves application data through a database model.

**Boundary:** User-facing work tables belong under workplace collaboration; third-party datasets belong under data access.

[Hosted Relational Databases](#databases-hosted-relational) · [Vector Databases](#databases-vector) · [Document Databases](#databases-document) · [Key-value Databases](#databases-key-value)

<a id="databases-hosted-relational"></a>

## Databases / Hosted Relational Databases

Remote SQL storage for personal applications, including temporary development databases.

**Includes:** Offers hosted SQL tables and relational queries.

**Boundary:** Local-only database files, document-only stores and collaborative work tables are separate.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Aiven](../data/candidates/aiven.yaml) | databases/hosted-relational | [postgres-cli (cli)](https://aiven.io/docs/tools/cli) | unknown | self_serve | documented | Requirements incomplete; Managed databases including free hosted PostgreSQL. Account signup and provisioning remain untested; free lifecycle limits need checking before production use. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [d1-cli (cli)](https://developers.cloudflare.com/d1/get-started/) | unknown | self_serve | documented | Requirements incomplete; 5 GB / account (free_allowance; D1 total storage on Workers Free; separate daily row quotas.); D1 Workers Free: 5 million reads/day, 100,000 writes/day, 5 GB total storage. Account authorization required; Wrangler local mode is not a remote database test. Existing paid projects are excluded. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [kv-api (api)](https://api.cloudflare.com/client/v4/) | unknown | self_serve | unknown | Requirements incomplete; Documented remote Workers KV key-value read API. Requires account and namespace identifiers and credentials with permission for the requested operation. No task success is claimed. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [kv-sdk (sdk)](https://developers.cloudflare.com/api/typescript/resources/kv/subresources/namespaces/subresources/values/methods/get/) | unknown | self_serve | unknown | Requirements incomplete; Official cloudflare TypeScript client exposes remote KV namespace and value methods. Local package installation is distinct from obtaining credentials and remote resource access. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [kv-cli (cli)](https://developers.cloudflare.com/kv/reference/kv-commands/) | unknown | self_serve | unknown | Requirements incomplete; Wrangler provides native KV namespace, key-list and key-read commands. Remote storage must be selected for comparison with cloud API/SDK/MCP; local simulation is not equivalent. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [api-mcp (mcp)](https://mcp.cloudflare.com/mcp) | unknown | self_serve | unknown | Requirements incomplete; Official remote API MCP exposes search and execute tools for Cloudflare API operations, including KV. Record the actual exposed tools and native MCP calls separately from raw HTTP. An existing Wrangler OAuth login is not assumed to authorize this endpoint. | not recorded |
| [Neon](../data/providers/neon.yaml) | databases/hosted-relational | [ephemeral-api (api)](https://neon.new/) | unknown | unknown | documented | Requirements incomplete; No-account, 72-hour ephemeral hosted Postgres. Tests can establish short-term persistence only; this is not a permanent free production database. Connection strings and claim URLs are private credentials. | [database-todos-001: completed (2026-09-07)](../data/experiments/evaluations/codex-20260907T112258.549053Z-neon.json) |
| [PlanetScale](../data/candidates/planetscale.yaml) | databases/hosted-relational | [database-cli (cli)](https://planetscale.com/docs/cli) | unknown | self_serve | documented | Requirements incomplete; 5 USD / month (minimum_spend; Postgres single-node starting plan; configuration, region and other resources may cost more.); PostgreSQL single-node plans start at USD 5/month. No free writable database allowance verified; not provisioned in this no-payment round. Public pricing SQL is read-only and does not meet the task. | not recorded |
| [Supabase](../data/providers/supabase.yaml) | databases/hosted-relational | [data-api (api)](https://supabase.com/docs/guides/api) | unknown | self_serve | documented | Requirements incomplete; 500 MB / project (free_allowance; Free plan database size; up to two active projects, pauses after one inactive week.); Existing project required; Free plan: two active projects, 500 MB database per project; pauses after one week inactivity. Management provisioning is separate from the data REST API. | not recorded |
| [Turso](../data/candidates/turso.yaml) | databases/hosted-relational | [cloud-cli (cli)](https://docs.turso.tech/cli/introduction) | unknown | self_serve | documented | Requirements incomplete; 5 GB / account (free_allowance; Free cloud storage; account quota also limits reads, writes and number of databases.); Free cloud account: 100 databases, 5 GB, 500 million reads/month and 10 million writes/month. Signup/login required; local engine alone does not satisfy remote storage. | not recorded |
| [Turso](../data/candidates/turso.yaml) | databases/hosted-relational | [platform-api (api)](https://docs.turso.tech/api-reference/introduction) | unknown | self_serve | unknown | Requirements incomplete; Management API; SQL connectivity uses separate database credentials created during execution. Provision only within a dedicated free test organization; no precreated database. | [database-todos-001: completed (2026-09-07)](../data/experiments/evaluations/codex-20260907T113506.422646Z-turso.json) |

<a id="databases-vector"></a>

## Databases / Vector Databases

Store and query data by vector similarity.

**Includes:** Persists indexed vectors and supports similarity queries.

**Boundary:** An embedding model alone does not store or search application data.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Chroma](../data/providers/chroma.yaml) | databases/vector | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Pinecone](../data/providers/pinecone.yaml) | databases/vector | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Qdrant](../data/providers/qdrant.yaml) | databases/vector | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Redis (Redis Cloud)](../data/providers/redis.yaml) | databases/key-value, databases/vector, databases/document | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Upstash](../data/providers/upstash.yaml) | databases/key-value, databases/vector | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Weaviate](../data/providers/weaviate.yaml) | databases/vector | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="databases-document"></a>

## Databases / Document Databases

Store and query structured application documents.

**Includes:** Provides persistent document collections with field-based queries.

**Boundary:** A file drive or metadata attached to vectors alone is insufficient.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [MongoDB Atlas](../data/providers/mongodb-atlas.yaml) | databases/document | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Redis (Redis Cloud)](../data/providers/redis.yaml) | databases/key-value, databases/vector, databases/document | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="databases-key-value"></a>

## Databases / Key-value Databases

Store and retrieve application values by key.

**Includes:** Offers addressable keys and values across calls.

**Boundary:** A local cache or temporary execution variable alone does not qualify.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [d1-cli (cli)](https://developers.cloudflare.com/d1/get-started/) | unknown | self_serve | documented | Requirements incomplete; 5 GB / account (free_allowance; D1 total storage on Workers Free; separate daily row quotas.); D1 Workers Free: 5 million reads/day, 100,000 writes/day, 5 GB total storage. Account authorization required; Wrangler local mode is not a remote database test. Existing paid projects are excluded. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [kv-api (api)](https://api.cloudflare.com/client/v4/) | unknown | self_serve | unknown | Requirements incomplete; Documented remote Workers KV key-value read API. Requires account and namespace identifiers and credentials with permission for the requested operation. No task success is claimed. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [kv-sdk (sdk)](https://developers.cloudflare.com/api/typescript/resources/kv/subresources/namespaces/subresources/values/methods/get/) | unknown | self_serve | unknown | Requirements incomplete; Official cloudflare TypeScript client exposes remote KV namespace and value methods. Local package installation is distinct from obtaining credentials and remote resource access. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [kv-cli (cli)](https://developers.cloudflare.com/kv/reference/kv-commands/) | unknown | self_serve | unknown | Requirements incomplete; Wrangler provides native KV namespace, key-list and key-read commands. Remote storage must be selected for comparison with cloud API/SDK/MCP; local simulation is not equivalent. | not recorded |
| [Cloudflare](../data/providers/cloudflare.yaml) | cloud-hosting/app-hosting, databases/hosted-relational, databases/key-value | [api-mcp (mcp)](https://mcp.cloudflare.com/mcp) | unknown | self_serve | unknown | Requirements incomplete; Official remote API MCP exposes search and execute tools for Cloudflare API operations, including KV. Record the actual exposed tools and native MCP calls separately from raw HTTP. An existing Wrangler OAuth login is not assumed to authorize this endpoint. | not recorded |
| [Redis (Redis Cloud)](../data/providers/redis.yaml) | databases/key-value, databases/vector, databases/document | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Upstash](../data/providers/upstash.yaml) | databases/key-value, databases/vector | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="web-search-data"></a>

## Search & Data Access

Search APIs, crawling and scraping, data providers.

**Includes:** Discovers external information or supplies usable source content or datasets.

**Boundary:** Storage of user-supplied application data is a database; a general model API alone is not a data source.

[Web Search](#web-search-data-web-search) · [Web Content Extraction](#web-search-data-web-extraction) · [Financial Data](#web-search-data-financial-data)

| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Xquik](../data/candidates/xquik.yaml) | web-search-data | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="web-search-data-web-search"></a>

## Search & Data Access / Web Search

Discover relevant public web pages from a query; answers may include source citations.

**Includes:** Accepts a topic or query and returns relevant web sources.

**Boundary:** Fetching a supplied URL alone is extraction; source snippets do not establish full-page retrieval.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [AgentServices](../data/candidates/agentservices.yaml) | web-search-data/web-search, web-search-data/web-extraction, ai-models/model-access, web-search-data/financial-data/prices | [rest-api (api)](https://api.agentservices.to/) | unknown | self_serve | documented | Requirements incomplete; Buyer guide names api.agentservices.to as the API host; agentservices.to serves the inspected documentation. The free-price example is distinct from a paid data result. An HTTP 402 challenge would establish quoted terms only, not delivery or settlement. Paid prices remain unresolved. | not recorded |
| [AgentServices](../data/candidates/agentservices.yaml) | web-search-data/web-search, web-search-data/web-extraction, ai-models/model-access, web-search-data/financial-data/prices | [official-mcp (mcp)](https://agentservices.to/mcp) | unknown | self_serve | documented | Requirements incomplete; Protocol configuration is documented, not executed here. MCP discovery, a free tool call and fulfillment of a paid tool are separate checks; neither MCP support nor a registry listing establishes hosted-service terms or read-only behavior for every tool. | not recorded |
| [AgentServices](../data/candidates/agentservices.yaml) | web-search-data/web-search, web-search-data/web-extraction, ai-models/model-access, web-search-data/financial-data/prices | [javascript-sdk (sdk)](https://github.com/vbkotecha/agentservices-api/tree/main/sdk) | unknown | self_serve | documented | Requirements incomplete; Package installation and execution were not tested. SDK price examples are indicative, and a payment challenge surfaced by the client is not a successful paid result. | not recorded |
| [Brave Search API](../data/providers/brave-search.yaml) | web-search-data/web-search | [search-api (api)](https://brave.com/search/api/) | unknown | self_serve | documented | Requires: payment_method; Free-plan card verification is required. No card supplied in this pilot; onboarding restriction does not establish poor search quality. | not recorded |
| [Exa](../data/providers/exa.yaml) | web-search-data/web-extraction, web-search-data/web-search | [public-mcp (mcp)](https://mcp.exa.ai/mcp) | unknown | self_serve | documented | Requirements incomplete; Public search MCP has a casual-use free plan; own key lifts limits. Additional agent_run tool requires authentication and separate usage charges; it is excluded from this pilot. API signup credits are not a quota guarantee for anonymous MCP. | [web-search-001: completed (2026-09-07)](../data/experiments/evaluations/codex-20260907T112257.401366Z-exa.json) |
| [Exa](../data/providers/exa.yaml) | web-search-data/web-extraction, web-search-data/web-search | [search-api (api)](https://exa.ai/docs/reference/search) | unknown | self_serve | documented | Requirements incomplete; 20 USD / one_time (free_allowance; Published signup credits; some may require onboarding. Actual account award should be checked.); 10 USD / month (free_allowance; Free account monthly allowance, not anonymous MCP quota.); Free account signup advertised at USD 20 initial credits plus USD 10/month; onboarding may be needed for part of initial credits. No payment method required. Anonymous MCP quota is separate. | [web-search-001: not_completed (2026-09-07)](../data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json) |
| [Firecrawl](../data/providers/firecrawl.yaml) | web-search-data/web-extraction, web-search-data/web-search | [public-search-api (api)](https://docs.firecrawl.dev/features/search) | unknown | self_serve | documented | Requirements incomplete; Current search docs explicitly permit starting without a key. Anonymous quota is unquantified; account free credits cannot be assumed for this route. | [web-search-001: completed (2026-09-07)](../data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json) |
| [Firecrawl](../data/providers/firecrawl.yaml) | web-search-data/web-extraction, web-search-data/web-search | [account-search-api (api)](https://docs.firecrawl.dev/features/search) | unknown | self_serve | documented | Requirements incomplete; 1000 credits / month (free_allowance; Account Free plan; separate from anonymous access.); Search: 2 credits per 10 results; extra scraping can consume credits. | not recorded |
| [Firecrawl](../data/providers/firecrawl.yaml) | web-search-data/web-extraction, web-search-data/web-search | [public-scrape-api (api)](https://api.firecrawl.dev/v2/scrape) | unknown | unknown | unknown | Requirements incomplete; Specified-URL scraping. Docs allow starting without a key; anonymous limits and paid-account costs are separate and no extraction task has been run. | not recorded |
| [Perplexity API](../data/providers/perplexity.yaml) | web-search-data/web-search | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [SerpApi](../data/providers/serpapi.yaml) | travel/flights, web-search-data/web-search | [google-flights-api (api)](https://serpapi.com/google-flights-api) | unknown | self_serve | unknown | Requirements incomplete; 250 searches / month (free_allowance; Platform search allowance; flight-endpoint entitlement and shared usage untested.); A third-party Google Flights data service. Not a Google-operated API. | not recorded |
| [SerpApi](../data/providers/serpapi.yaml) | travel/flights, web-search-data/web-search | [official-mcp (mcp)](https://github.com/serpapi/serpapi-mcp) | unknown | unknown | unknown | Requirements incomplete; Official to SerpApi. Flight tool coverage and access gates are unconfirmed; do not inherit API-route results. | not recorded |
| [SerpApi](../data/providers/serpapi.yaml) | travel/flights, web-search-data/web-search | [web-search-api (api)](https://serpapi.com/search-api) | unknown | self_serve | unknown | Requirements incomplete; Separate from Google Flights API. Existing flight evaluations do not establish web search performance. | not recorded |
| [Serper](../data/candidates/serper.yaml) | web-search-data/web-search | [search-api (api)](https://serper.dev/) | unknown | self_serve | documented | Requirements incomplete; 2500 queries / one_time (free_allowance; Advertised initial free queries, no monthly renewal claimed.); Google results API with signup trial queries; actual account flow and authentication remain untested. | not recorded |
| [Tavily](../data/providers/tavily.yaml) | web-search-data/web-extraction, web-search-data/web-search | [search-api (api)](https://docs.tavily.com/documentation/quickstart) | unknown | self_serve | documented | Requirements incomplete; 1000 credits / month (free_allowance; Free account allowance, not requests.); Basic search costs 1 credit; advanced search 2. Paid overage setting is separate. | not recorded |
| [Tavily](../data/providers/tavily.yaml) | web-search-data/web-extraction, web-search-data/web-search | [extract-api (api)](https://api.tavily.com/extract) | unknown | unknown | unknown | Requirements incomplete; Extract accepts one or more URLs. Search pricing and search trials do not establish extraction cost or success. | not recorded |

<a id="web-search-data-web-extraction"></a>

## Search & Data Access / Web Content Extraction

Retrieve specified web pages or sites as usable text or structured data.

**Includes:** Accepts identified web URLs or a specified site and returns its content as usable text or structured data.

**Boundary:** Query-only result lists/snippets are web search; browser control is a runtime, not extraction itself.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [AgentServices](../data/candidates/agentservices.yaml) | web-search-data/web-search, web-search-data/web-extraction, ai-models/model-access, web-search-data/financial-data/prices | [rest-api (api)](https://api.agentservices.to/) | unknown | self_serve | documented | Requirements incomplete; Buyer guide names api.agentservices.to as the API host; agentservices.to serves the inspected documentation. The free-price example is distinct from a paid data result. An HTTP 402 challenge would establish quoted terms only, not delivery or settlement. Paid prices remain unresolved. | not recorded |
| [AgentServices](../data/candidates/agentservices.yaml) | web-search-data/web-search, web-search-data/web-extraction, ai-models/model-access, web-search-data/financial-data/prices | [official-mcp (mcp)](https://agentservices.to/mcp) | unknown | self_serve | documented | Requirements incomplete; Protocol configuration is documented, not executed here. MCP discovery, a free tool call and fulfillment of a paid tool are separate checks; neither MCP support nor a registry listing establishes hosted-service terms or read-only behavior for every tool. | not recorded |
| [AgentServices](../data/candidates/agentservices.yaml) | web-search-data/web-search, web-search-data/web-extraction, ai-models/model-access, web-search-data/financial-data/prices | [javascript-sdk (sdk)](https://github.com/vbkotecha/agentservices-api/tree/main/sdk) | unknown | self_serve | documented | Requirements incomplete; Package installation and execution were not tested. SDK price examples are indicative, and a payment challenge surfaced by the client is not a successful paid result. | not recorded |
| [Apify](../data/providers/apify.yaml) | web-search-data/web-extraction | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Exa](../data/providers/exa.yaml) | web-search-data/web-extraction, web-search-data/web-search | [public-mcp (mcp)](https://mcp.exa.ai/mcp) | unknown | self_serve | documented | Requirements incomplete; Public search MCP has a casual-use free plan; own key lifts limits. Additional agent_run tool requires authentication and separate usage charges; it is excluded from this pilot. API signup credits are not a quota guarantee for anonymous MCP. | not recorded |
| [Exa](../data/providers/exa.yaml) | web-search-data/web-extraction, web-search-data/web-search | [search-api (api)](https://exa.ai/docs/reference/search) | unknown | self_serve | documented | Requirements incomplete; 20 USD / one_time (free_allowance; Published signup credits; some may require onboarding. Actual account award should be checked.); 10 USD / month (free_allowance; Free account monthly allowance, not anonymous MCP quota.); Free account signup advertised at USD 20 initial credits plus USD 10/month; onboarding may be needed for part of initial credits. No payment method required. Anonymous MCP quota is separate. | not recorded |
| [Firecrawl](../data/providers/firecrawl.yaml) | web-search-data/web-extraction, web-search-data/web-search | [public-search-api (api)](https://docs.firecrawl.dev/features/search) | unknown | self_serve | documented | Requirements incomplete; Current search docs explicitly permit starting without a key. Anonymous quota is unquantified; account free credits cannot be assumed for this route. | not recorded |
| [Firecrawl](../data/providers/firecrawl.yaml) | web-search-data/web-extraction, web-search-data/web-search | [account-search-api (api)](https://docs.firecrawl.dev/features/search) | unknown | self_serve | documented | Requirements incomplete; 1000 credits / month (free_allowance; Account Free plan; separate from anonymous access.); Search: 2 credits per 10 results; extra scraping can consume credits. | not recorded |
| [Firecrawl](../data/providers/firecrawl.yaml) | web-search-data/web-extraction, web-search-data/web-search | [public-scrape-api (api)](https://api.firecrawl.dev/v2/scrape) | unknown | unknown | unknown | Requirements incomplete; Specified-URL scraping. Docs allow starting without a key; anonymous limits and paid-account costs are separate and no extraction task has been run. | not recorded |
| [Jina AI](../data/providers/jina.yaml) | web-search-data/web-extraction | [reader-api (api)](https://r.jina.ai/) | unknown | unknown | unknown | Requirements incomplete; Reader converts a supplied URL to text. Keyless basic usage is documented; keyed rate limits and billing are separate. No broader search or embedding capability is inferred from this route. | not recorded |
| [Tavily](../data/providers/tavily.yaml) | web-search-data/web-extraction, web-search-data/web-search | [search-api (api)](https://docs.tavily.com/documentation/quickstart) | unknown | self_serve | documented | Requirements incomplete; 1000 credits / month (free_allowance; Free account allowance, not requests.); Basic search costs 1 credit; advanced search 2. Paid overage setting is separate. | not recorded |
| [Tavily](../data/providers/tavily.yaml) | web-search-data/web-extraction, web-search-data/web-search | [extract-api (api)](https://api.tavily.com/extract) | unknown | unknown | unknown | Requirements incomplete; Extract accepts one or more URLs. Search pricing and search trials do not establish extraction cost or success. | not recorded |

<a id="web-search-data-financial-data"></a>

## Search & Data Access / Financial Data

Access identifiable financial or economic datasets; select a data type, then match coverage and task conditions.

**Includes:** Supplies financial/economic observations or original filings; unresolved dataset scope can remain at this parent with an explanation.

**Boundary:** News, trading execution or a generic search API alone does not establish a financial dataset service.

[Exchange Rates](#web-search-data-financial-data-fx) · [Asset Prices](#web-search-data-financial-data-prices) · [Company Financials](#web-search-data-financial-data-statements) · [Transaction Disclosures](#web-search-data-financial-data-disclosures) · [Economic Indicators](#web-search-data-financial-data-macro)

| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [FactSet Data APIs](../data/candidates/factset-data.yaml) | web-search-data/financial-data | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [JoinQuant JQData](../data/candidates/joinquant-data.yaml) | web-search-data/financial-data | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [LSEG Data Platform](../data/candidates/lseg-data.yaml) | web-search-data/financial-data | [data-api (sdk)](https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/quick-start) | unknown | application | restricted | Requires: platform_account; Human: Obtain licensed cloud credentials through an account manager, or provide an existing entitled desktop login.; Cloud credentials require an account manager; desktop access needs a valid Workspace/Eikon login and App Key. Individual admission and trial approval are not established. | not recorded |
| [Nasdaq Data Link](../data/candidates/nasdaq-data-link.yaml) | web-search-data/financial-data | [data-api (api)](https://docs.data.nasdaq.com/docs/getting-started) | unknown | unknown | documented | Requirements incomplete; Choose a specific dataset before comparison. Most datasets are premium. The legacy documentation announces retirement on 2026-08-31; its replacement link was not readable in this research pass. | not recorded |

<a id="web-search-data-financial-data-fx"></a>

## Search & Data Access / Financial Data / Exchange Rates

Retrieve currency-pair exchange rates.

**Includes:** Rates identify the currency pair, direction and observation date.

**Boundary:** A payment conversion fee or asset valuation alone is insufficient; reference rates do not imply executable exchange quotes.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Alpha Vantage](../data/candidates/alpha-vantage.yaml) | web-search-data/financial-data/fx, web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/disclosures, web-search-data/financial-data/macro | [data-api (api)](https://www.alphavantage.co/documentation/) | unknown | self_serve | documented | Requirements incomplete; 25 requests / day (free_allowance; Free API key allowance; excludes premium endpoints.); Free key: 25 requests/day, excluding premium endpoints. Unadjusted daily compact output (latest 100 observations) is available to free keys; full history and intraday are premium. This may cover the current short historical task, subject to access and source precision. Real-time quotes and adjusted data require separate entitlement checks. | not recorded |
| [ECB Data Portal API](../data/candidates/ecb-data.yaml) | web-search-data/financial-data/fx, web-search-data/financial-data/macro | [data-api (api)](https://data-api.ecb.europa.eu/service/) | unknown | self_serve | documented | Requirements incomplete; Series dimensions, quote direction, observation frequency and date range must be selected correctly. Reference rates are not executable conversion prices. Reference-rate information is freely published under the ECB reuse policy; fees for a run still require observation of the actual route. The documentation page was temporarily unreadable during the latest research pass. | [financial-fx-001: completed (2026-09-15)](../data/experiments/evaluations/ecb-business.json) |
| [Financial Modeling Prep (FMP)](../data/candidates/fmp.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/fx, web-search-data/financial-data/disclosures | [data-api (api)](https://site.financialmodelingprep.com/developer/docs) | unknown | self_serve | documented | Requirements incomplete; Basic is free with 250 calls/day and end-of-day/profile/reference features. Annual fundamentals are listed under paid Starter; a free key does not establish access to the fiscal-year comparison task. Displaying or redistributing FMP data requires a separate licensing agreement according to its pricing page. The House Trades endpoint is documented, but Congress-specific free-plan entitlement is not confirmed. | not recorded |
| [Financial Modeling Prep (FMP)](../data/candidates/fmp.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/fx, web-search-data/financial-data/disclosures | [data-mcp (mcp)](https://financialmodelingprep.com/mcp) | unknown | self_serve | documented | Requirements incomplete; Uses the existing API key and plan limits; key must be injected privately, never stored in the URL in public results. | not recorded |
| [Frankfurter](../data/candidates/frankfurter.yaml) | web-search-data/financial-data/fx | [data-api (api)](https://api.frankfurter.dev/v2/) | unknown | self_serve | documented | Requirements incomplete; 0 USD / public API request (usage; Hosted public API under its documented fair-use rate limiting; underlying provider terms still apply.); The hosted public API is free with no key or daily/monthly quota; abuse rate limits apply. Default v2 rates blend sources; filter by ECB when the task requires ECB reference data. Reference rates are not executable bank/card quotes. | [financial-fx-001: completed (2026-09-15)](../data/experiments/evaluations/frankfurter-business.json) |
| [Frankfurter](../data/candidates/frankfurter.yaml) | web-search-data/financial-data/fx | [rates-mcp (mcp)](https://frankfurter.dev/mcp/) | unknown | self_serve | documented | Requirements incomplete; Official hosted/local MCP setup guide; uses reference rates, not a payment or currency-trading service. | not recorded |
| [Open Exchange Rates](../data/candidates/open-exchange-rates.yaml) | web-search-data/financial-data/fx | [data-api (api)](https://docs.openexchangerates.org/reference/api-introduction) | unknown | self_serve | documented | Requirements incomplete; A free signup route is published. Confirm whether the chosen historical date and currency base are included; rates are indicative rather than executable bank/card quotes. | not recorded |
| [Tiingo](../data/candidates/tiingo.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/fx | [data-api (api)](https://www.tiingo.com/documentation/general/overview) | unknown | self_serve | unknown | Requirements incomplete; Token is assigned after account creation. Request and bandwidth limits apply; current free allowance and target-feed entitlement are not yet established. | not recorded |
| [Twelve Data](../data/candidates/twelve-data.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/fx | [data-api (api)](https://twelvedata.com/docs/introduction/quickstart) | unknown | self_serve | documented | Requirements incomplete; 800 credits / day (free_allowance; Basic plan; endpoint credit weights and market entitlements vary.); Basic advertises 800 API credits/day. Credits are not necessarily requests. Market coverage, fundamentals and display rights depend on plan. | not recorded |
| [Twelve Data](../data/candidates/twelve-data.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/fx | [python-sdk (sdk)](https://twelvedata.com/docs/introduction/quickstart) | unknown | self_serve | documented | Requirements incomplete; 800 credits / day (free_allowance; Basic plan; endpoint credit weights and market entitlements vary.); Official Python TDClient example; same account entitlement as REST. | not recorded |
| [Twelve Data](../data/candidates/twelve-data.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/fx | [data-cli (cli)](https://github.com/twelvedata/twelvedata-cli) | unknown | self_serve | documented | Requirements incomplete; 800 credits / day (free_allowance; Basic plan; endpoint credit weights and market entitlements vary.); Official CLI repository; installation and command coverage not yet tested. | not recorded |

<a id="web-search-data-financial-data-prices"></a>

## Search & Data Access / Financial Data / Asset Prices

Retrieve asset price snapshots or historical series.

**Includes:** Provides prices for identifiable assets and observation times.

**Boundary:** Valuations inside transaction disclosures or news articles alone are insufficient; assets, adjustments and entitlements must match.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [AgentServices](../data/candidates/agentservices.yaml) | web-search-data/web-search, web-search-data/web-extraction, ai-models/model-access, web-search-data/financial-data/prices | [rest-api (api)](https://api.agentservices.to/) | unknown | self_serve | documented | Requirements incomplete; Buyer guide names api.agentservices.to as the API host; agentservices.to serves the inspected documentation. The free-price example is distinct from a paid data result. An HTTP 402 challenge would establish quoted terms only, not delivery or settlement. Paid prices remain unresolved. | not recorded |
| [AgentServices](../data/candidates/agentservices.yaml) | web-search-data/web-search, web-search-data/web-extraction, ai-models/model-access, web-search-data/financial-data/prices | [official-mcp (mcp)](https://agentservices.to/mcp) | unknown | self_serve | documented | Requirements incomplete; Protocol configuration is documented, not executed here. MCP discovery, a free tool call and fulfillment of a paid tool are separate checks; neither MCP support nor a registry listing establishes hosted-service terms or read-only behavior for every tool. | not recorded |
| [AgentServices](../data/candidates/agentservices.yaml) | web-search-data/web-search, web-search-data/web-extraction, ai-models/model-access, web-search-data/financial-data/prices | [javascript-sdk (sdk)](https://github.com/vbkotecha/agentservices-api/tree/main/sdk) | unknown | self_serve | documented | Requirements incomplete; Package installation and execution were not tested. SDK price examples are indicative, and a payment challenge surfaced by the client is not a successful paid result. | not recorded |
| [Alpaca Market Data](../data/candidates/alpaca-market-data.yaml) | web-search-data/financial-data/prices | [data-api (api)](https://docs.alpaca.markets/us/docs/about-market-data-api) | unknown | self_serve | documented | Requirements incomplete; Basic is free with limited real-time feeds; historical coverage and latest-15-minute restrictions are separate. Use market-data endpoints only. Paper-account signup and identity requirements have not been measured. | not recorded |
| [Alpaca Market Data](../data/candidates/alpaca-market-data.yaml) | web-search-data/financial-data/prices | [crypto-api-keyless (api)](https://docs.alpaca.markets/us/docs/about-market-data-api) | unknown | self_serve | documented | Requirements incomplete; Official documentation exempts historical crypto endpoints from authentication. Does not imply equity-data access or trading permission. | not recorded |
| [Alpha Vantage](../data/candidates/alpha-vantage.yaml) | web-search-data/financial-data/fx, web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/disclosures, web-search-data/financial-data/macro | [data-api (api)](https://www.alphavantage.co/documentation/) | unknown | self_serve | documented | Requirements incomplete; 25 requests / day (free_allowance; Free API key allowance; excludes premium endpoints.); Free key: 25 requests/day, excluding premium endpoints. Unadjusted daily compact output (latest 100 observations) is available to free keys; full history and intraday are premium. This may cover the current short historical task, subject to access and source precision. Real-time quotes and adjusted data require separate entitlement checks. | not recorded |
| [Bloomberg Data License](../data/candidates/bloomberg-data-license.yaml) | web-search-data/financial-data/prices | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [CoinGecko](../data/candidates/coingecko.yaml) | web-search-data/financial-data/prices | [data-api (api)](https://docs.coingecko.com/docs/setting-up-your-api-key) | unknown | self_serve | documented | Requirements incomplete; Demo and paid API plans have different history and quotas. Keyless MCP has shared limits and a smaller tool set. Asset IDs and quote currency must match the task. | not recorded |
| [CoinGecko](../data/candidates/coingecko.yaml) | web-search-data/financial-data/prices | [keyless-mcp (mcp)](https://mcp.api.coingecko.com/mcp) | unknown | self_serve | documented | Requirements incomplete; Free, shared rate limits, limited tool set; account and key not required. | not recorded |
| [CoinGecko](../data/candidates/coingecko.yaml) | web-search-data/financial-data/prices | [keyed-mcp (mcp)](https://mcp.pro-api.coingecko.com/mcp) | unknown | self_serve | documented | Requirements incomplete; Account entitlement and tool set differ from keyless MCP; confirm free Demo compatibility before a paid-server call. | not recorded |
| [CoinMarketCap](../data/candidates/coinmarketcap.yaml) | web-search-data/financial-data/prices | [data-api (api)](https://coinmarketcap.com/api/) | unknown | self_serve | documented | Requirements incomplete; 15000 credits / month (free_allowance; Authenticated Basic plan; selected endpoints and history only.); Basic advertises 15,000 monthly call credits and 50 requests/minute. History depth and endpoint availability depend on plan; keyless access is limited to selected endpoints. | not recorded |
| [EODHD](../data/candidates/eodhd.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/macro, web-search-data/financial-data/disclosures | [data-api (api)](https://eodhd.com/financial-apis/) | unknown | self_serve | documented | Requirements incomplete; 20 requests / day (free_allowance; Free plan; some data types are excluded.); Free registration advertises 20 API calls/day without a card; some data types are excluded. Check dataset and market coverage before choosing a trial. Congressional Trades is documented for the All-in-one plan; the generic 20-call free allowance does not establish access to this dataset. | not recorded |
| [Financial Datasets](../data/candidates/financial-datasets.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/disclosures | [data-api (api)](https://docs.financialdatasets.ai/quickstart) | unknown | self_serve | documented | Requirements incomplete; Create an account and key. A free execution allowance has not been established; do not start metered requests without confirming available free credit. | not recorded |
| [Finnhub](../data/candidates/finnhub.yaml) | web-search-data/financial-data/prices | [data-api (api)](https://finnhub.io/docs/api/quote) | unknown | self_serve | unknown | Requirements incomplete; Dashboard API key required. Stock candles require premium access; a working free quote endpoint would not establish free historical-data access. | not recorded |
| [Financial Modeling Prep (FMP)](../data/candidates/fmp.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/fx, web-search-data/financial-data/disclosures | [data-api (api)](https://site.financialmodelingprep.com/developer/docs) | unknown | self_serve | documented | Requirements incomplete; Basic is free with 250 calls/day and end-of-day/profile/reference features. Annual fundamentals are listed under paid Starter; a free key does not establish access to the fiscal-year comparison task. Displaying or redistributing FMP data requires a separate licensing agreement according to its pricing page. The House Trades endpoint is documented, but Congress-specific free-plan entitlement is not confirmed. | not recorded |
| [Financial Modeling Prep (FMP)](../data/candidates/fmp.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/fx, web-search-data/financial-data/disclosures | [data-mcp (mcp)](https://financialmodelingprep.com/mcp) | unknown | self_serve | documented | Requirements incomplete; Uses the existing API key and plan limits; key must be injected privately, never stored in the URL in public results. | not recorded |
| [Massive (formerly Polygon.io)](../data/candidates/massive.yaml) | web-search-data/financial-data/prices | [data-api (api)](https://massive.com/docs/rest/quickstart) | unknown | self_serve | documented | Requirements incomplete; 0 USD / month on Stocks Basic (usage; Individual Stocks Basic plan only; no other datasets, subscriptions or paid entitlements inferred.); Stocks Basic: USD 0/month for individual use, 5 calls/minute, two years of historical end-of-day data. A free stock plan does not establish free fundamentals or permission to redistribute data. Confirm unadjusted daily aggregate settings and actual access in the trial. | not recorded |
| [SimFin](../data/candidates/simfin.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Tiingo](../data/candidates/tiingo.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/fx | [data-api (api)](https://www.tiingo.com/documentation/general/overview) | unknown | self_serve | unknown | Requirements incomplete; Token is assigned after account creation. Request and bandwidth limits apply; current free allowance and target-feed entitlement are not yet established. | not recorded |
| [Tushare Pro](../data/candidates/tushare.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements | [data-api (api)](https://tushare.pro/document/1?doc_id=40) | unknown | self_serve | documented | Requirements incomplete; Daily unadjusted prices start at 120 points; financial statements start at 2,000. Points are an access threshold, not per-call spending. Some datasets need separate permissions. The HTTP example uses an unencrypted endpoint; verify a secure credential path before testing. | not recorded |
| [Tushare Pro](../data/candidates/tushare.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements | [python-sdk (sdk)](https://tushare.pro/document/1?doc_id=40) | unknown | self_serve | documented | Requirements incomplete; Python SDK shares token and point thresholds with HTTP access; verify transport security before supplying credentials. | not recorded |
| [Twelve Data](../data/candidates/twelve-data.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/fx | [data-api (api)](https://twelvedata.com/docs/introduction/quickstart) | unknown | self_serve | documented | Requirements incomplete; 800 credits / day (free_allowance; Basic plan; endpoint credit weights and market entitlements vary.); Basic advertises 800 API credits/day. Credits are not necessarily requests. Market coverage, fundamentals and display rights depend on plan. | not recorded |
| [Twelve Data](../data/candidates/twelve-data.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/fx | [python-sdk (sdk)](https://twelvedata.com/docs/introduction/quickstart) | unknown | self_serve | documented | Requirements incomplete; 800 credits / day (free_allowance; Basic plan; endpoint credit weights and market entitlements vary.); Official Python TDClient example; same account entitlement as REST. | not recorded |
| [Twelve Data](../data/candidates/twelve-data.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/fx | [data-cli (cli)](https://github.com/twelvedata/twelvedata-cli) | unknown | self_serve | documented | Requirements incomplete; 800 credits / day (free_allowance; Basic plan; endpoint credit weights and market entitlements vary.); Official CLI repository; installation and command coverage not yet tested. | not recorded |

<a id="web-search-data-financial-data-statements"></a>

## Search & Data Access / Financial Data / Company Financials

Retrieve company financial statements or reported financial facts.

**Includes:** Financial values identify the company, reporting period and units, or link to the original statement.

**Boundary:** Company profiles, market prices or valuation ratios alone are insufficient.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Alpha Vantage](../data/candidates/alpha-vantage.yaml) | web-search-data/financial-data/fx, web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/disclosures, web-search-data/financial-data/macro | [data-api (api)](https://www.alphavantage.co/documentation/) | unknown | self_serve | documented | Requirements incomplete; 25 requests / day (free_allowance; Free API key allowance; excludes premium endpoints.); Free key: 25 requests/day, excluding premium endpoints. Unadjusted daily compact output (latest 100 observations) is available to free keys; full history and intraday are premium. This may cover the current short historical task, subject to access and source precision. Real-time quotes and adjusted data require separate entitlement checks. | not recorded |
| [EODHD](../data/candidates/eodhd.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/macro, web-search-data/financial-data/disclosures | [data-api (api)](https://eodhd.com/financial-apis/) | unknown | self_serve | documented | Requirements incomplete; 20 requests / day (free_allowance; Free plan; some data types are excluded.); Free registration advertises 20 API calls/day without a card; some data types are excluded. Check dataset and market coverage before choosing a trial. Congressional Trades is documented for the All-in-one plan; the generic 20-call free allowance does not establish access to this dataset. | not recorded |
| [Financial Datasets](../data/candidates/financial-datasets.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/disclosures | [data-api (api)](https://docs.financialdatasets.ai/quickstart) | unknown | self_serve | documented | Requirements incomplete; Create an account and key. A free execution allowance has not been established; do not start metered requests without confirming available free credit. | not recorded |
| [Financial Modeling Prep (FMP)](../data/candidates/fmp.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/fx, web-search-data/financial-data/disclosures | [data-api (api)](https://site.financialmodelingprep.com/developer/docs) | unknown | self_serve | documented | Requirements incomplete; Basic is free with 250 calls/day and end-of-day/profile/reference features. Annual fundamentals are listed under paid Starter; a free key does not establish access to the fiscal-year comparison task. Displaying or redistributing FMP data requires a separate licensing agreement according to its pricing page. The House Trades endpoint is documented, but Congress-specific free-plan entitlement is not confirmed. | not recorded |
| [Financial Modeling Prep (FMP)](../data/candidates/fmp.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/fx, web-search-data/financial-data/disclosures | [data-mcp (mcp)](https://financialmodelingprep.com/mcp) | unknown | self_serve | documented | Requirements incomplete; Uses the existing API key and plan limits; key must be injected privately, never stored in the URL in public results. | not recorded |
| [SEC EDGAR Data APIs](../data/candidates/sec-edgar.yaml) | web-search-data/financial-data/statements | [data-api (api)](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | unknown | self_serve | documented | Requirements incomplete; Reading APIs are separate from filer submission APIs. Automated-access policy applies. Facts need fiscal-period, unit and amendment interpretation; CORS is not supported. | not recorded |
| [SimFin](../data/candidates/simfin.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Tushare Pro](../data/candidates/tushare.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements | [data-api (api)](https://tushare.pro/document/1?doc_id=40) | unknown | self_serve | documented | Requirements incomplete; Daily unadjusted prices start at 120 points; financial statements start at 2,000. Points are an access threshold, not per-call spending. Some datasets need separate permissions. The HTTP example uses an unencrypted endpoint; verify a secure credential path before testing. | not recorded |
| [Tushare Pro](../data/candidates/tushare.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements | [python-sdk (sdk)](https://tushare.pro/document/1?doc_id=40) | unknown | self_serve | documented | Requirements incomplete; Python SDK shares token and point thresholds with HTTP access; verify transport security before supplying credentials. | not recorded |

<a id="web-search-data-financial-data-disclosures"></a>

## Search & Data Access / Financial Data / Transaction Disclosures

Retrieve publicly reported transactions.

**Includes:** Records identify the reporting party and distinguish disclosure from transaction timing where available.

**Boundary:** Company annual reports alone are not transaction disclosures; congressional and insider filings are different populations.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Alpha Vantage](../data/candidates/alpha-vantage.yaml) | web-search-data/financial-data/fx, web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/disclosures, web-search-data/financial-data/macro | [data-api (api)](https://www.alphavantage.co/documentation/) | unknown | self_serve | documented | Requirements incomplete; 25 requests / day (free_allowance; Free API key allowance; excludes premium endpoints.); Free key: 25 requests/day, excluding premium endpoints. Unadjusted daily compact output (latest 100 observations) is available to free keys; full history and intraday are premium. This may cover the current short historical task, subject to access and source precision. Real-time quotes and adjusted data require separate entitlement checks. | not recorded |
| [Bargo Congress Trades API](../data/candidates/bargo-congress.yaml) | web-search-data/financial-data/disclosures | [congress-api-keyless (api)](https://www.bargo.ai/free-apis/congress/v1) | unknown | self_serve | documented | Requirements incomplete; 30 requests / day (free_allowance; Keyless quota shared per IP.); 100 rows / day (free_allowance; Rolling three-month Congress dataset; redistribution restrictions apply.); Rolling three-month coverage. Preserve transaction and disclosure dates; the Free API Terms require attribution and restrict raw-data redistribution. | [financial-disclosures-001: completed (2026-09-15)](../data/experiments/evaluations/bargo-business.json) |
| [Bargo Congress Trades API](../data/candidates/bargo-congress.yaml) | web-search-data/financial-data/disclosures | [congress-api-keyed (api)](https://www.bargo.ai/free-apis/congress/v1) | unknown | self_serve | documented | Requires: platform_account; 100 requests / day (free_allowance; Free-key allowance across Bargo Free APIs, including REST and MCP.); 1000 rows / day (free_allowance; Same free-key allowance; Congress data is limited to a rolling three-month window.); Free keys are issued through Google sign-in. REST accepts Bearer or X-Api-Key authentication; regenerating a key invalidates the old one. Signup and key acquisition have not been measured. The published quota covers the same key across Bargo Free APIs, not a separate allowance per route. | not recorded |
| [Bargo Congress Trades API](../data/candidates/bargo-congress.yaml) | web-search-data/financial-data/disclosures | [congress-mcp (mcp)](https://www.bargo.ai/free-apis/congress/mcp) | unknown | self_serve | documented | Requires: platform_account; 100 requests / day (free_allowance; Free-key allowance across Bargo Free APIs, including REST and MCP.); 1000 rows / day (free_allowance; Same free-key allowance; Congress data is limited to a rolling three-month window.); Uses the free key obtained through Google sign-in. Bearer authentication is documented; no separate MCP data or quota allowance is claimed. Verify tool coverage per task. | not recorded |
| [CapitolExposed](../data/candidates/capitol-exposed.yaml) | web-search-data/financial-data/disclosures | [data-api-keyless (api)](https://www.capitolexposed.com/api/v1) | unknown | self_serve | documented | Requirements incomplete; 60 requests / minute (free_allowance; Free member/trade list endpoints; separate limits apply to search, exports and AI tools.); Keyless requests are limited by IP. Terms require attribution; raw-data resale and competing services have additional restrictions. Use the records API, not its separately metered AI research product. | [financial-disclosures-001: completed (2026-09-15)](../data/experiments/evaluations/capitol-business.json) |
| [Capitol Trades](../data/candidates/capitol-trades.yaml) | web-search-data/financial-data/disclosures | [trades-website (web)](https://www.capitoltrades.com/trades) | unknown | self_serve | documented | Requirements incomplete; Official indexed pages describe free public access. Direct page fetch returned 403 during this review; browser usability, automation terms and any personal API access remain unverified. | not recorded |
| [Congress Stock Tracker](../data/candidates/congress-stock-tracker.yaml) | web-search-data/financial-data/disclosures | [licensed-api (api)](https://www.congressstock.com/congress-trading-api) | unknown | application | unknown | Requirements incomplete; Human: Request a dataset licence and access terms.; Contact-based pricing; no self-serve free tier. An evaluation extract or discounted academic/non-commercial access requires a request and is not an issued API entitlement. | not recorded |
| [EODHD](../data/candidates/eodhd.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/macro, web-search-data/financial-data/disclosures | [data-api (api)](https://eodhd.com/financial-apis/) | unknown | self_serve | documented | Requirements incomplete; 20 requests / day (free_allowance; Free plan; some data types are excluded.); Free registration advertises 20 API calls/day without a card; some data types are excluded. Check dataset and market coverage before choosing a trial. Congressional Trades is documented for the All-in-one plan; the generic 20-call free allowance does not establish access to this dataset. | not recorded |
| [Financial Datasets](../data/candidates/financial-datasets.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/disclosures | [data-api (api)](https://docs.financialdatasets.ai/quickstart) | unknown | self_serve | documented | Requirements incomplete; Create an account and key. A free execution allowance has not been established; do not start metered requests without confirming available free credit. | not recorded |
| [Financial Modeling Prep (FMP)](../data/candidates/fmp.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/fx, web-search-data/financial-data/disclosures | [data-api (api)](https://site.financialmodelingprep.com/developer/docs) | unknown | self_serve | documented | Requirements incomplete; Basic is free with 250 calls/day and end-of-day/profile/reference features. Annual fundamentals are listed under paid Starter; a free key does not establish access to the fiscal-year comparison task. Displaying or redistributing FMP data requires a separate licensing agreement according to its pricing page. The House Trades endpoint is documented, but Congress-specific free-plan entitlement is not confirmed. | not recorded |
| [Financial Modeling Prep (FMP)](../data/candidates/fmp.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/fx, web-search-data/financial-data/disclosures | [data-mcp (mcp)](https://financialmodelingprep.com/mcp) | unknown | self_serve | documented | Requirements incomplete; Uses the existing API key and plan limits; key must be injected privately, never stored in the URL in public results. | not recorded |
| [Insynet](../data/candidates/insynet.yaml) | web-search-data/financial-data/disclosures | [data-api (api)](https://tlyddvcmpcbhotxhbiao.supabase.co/functions/v1/api-v1) | unknown | application | documented | Requirements incomplete; 100 requests / day (free_allowance; Free-key tier covers all five endpoints with data delayed at least 24 hours after ingestion.); Human: Request a free API key by email.; Ticker, since and limit filters; limit is at most 100. Full historical pagination and complete transaction-level ownership are not established. | not recorded |
| [Quiver Quantitative](../data/candidates/quiver-quantitative.yaml) | web-search-data/financial-data/disclosures | [data-api (api)](https://www.quiverquant.com/api-setup/) | unknown | self_serve | documented | Requirements incomplete; 30 USD / month (minimum_spend; Advertised API starting price; exact dataset entitlement not established.); API access is advertised from USD 30/month. Free website signup does not establish free API access; no free execution allowance confirmed. | not recorded |
| [Quiver Quantitative](../data/candidates/quiver-quantitative.yaml) | web-search-data/financial-data/disclosures | [data-mcp (mcp)](https://mcp.quiverquant.com/) | unknown | self_serve | documented | Requirements incomplete; Uses a Quiver API key and plan entitlement; MCP is not an additional free allowance. Required dataset tier must be checked. | not recorded |
| [Tracefour](../data/candidates/tracefour.yaml) | web-search-data/financial-data/disclosures | [data-api-keyless (api)](https://tracefour.com/v1) | unknown | self_serve | documented | Requirements incomplete; 60 requests / hour (free_allowance; Anonymous read allowance per IP.); CC BY 4.0 compilation; link to the attribution page supplied with each response. Congress coverage is not established as complete for both chambers. | not recorded |
| [Tracefour](../data/candidates/tracefour.yaml) | web-search-data/financial-data/disclosures | [data-mcp (mcp)](https://tracefour.com/v1/mcp) | unknown | self_serve | documented | Requirements incomplete; Streamable HTTP; anonymous calls share the documented per-IP allowance. Optional free key increases the allowance to 600/hour; key acquisition not tested. | not recorded |
| [U.S. House Financial Disclosures](../data/candidates/us-house-disclosures.yaml) | web-search-data/financial-data/disclosures | [filing-website (web)](https://disclosures-clerk.house.gov/FinancialDisclosure) | unknown | self_serve | documented | Requirements incomplete; Website/file access, not a documented public financial-data API. Annual ZIP contains filing indexes; transaction rows require the linked PDFs. Source used for independent references; not yet measured as a service. | not recorded |

<a id="web-search-data-financial-data-macro"></a>

## Search & Data Access / Financial Data / Economic Indicators

Retrieve named economic indicator series.

**Includes:** Observations identify the series, periods and units.

**Boundary:** Market asset prices alone are not macro indicators; frequency, seasonality and revisions must match.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Alpha Vantage](../data/candidates/alpha-vantage.yaml) | web-search-data/financial-data/fx, web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/disclosures, web-search-data/financial-data/macro | [data-api (api)](https://www.alphavantage.co/documentation/) | unknown | self_serve | documented | Requirements incomplete; 25 requests / day (free_allowance; Free API key allowance; excludes premium endpoints.); Free key: 25 requests/day, excluding premium endpoints. Unadjusted daily compact output (latest 100 observations) is available to free keys; full history and intraday are premium. This may cover the current short historical task, subject to access and source precision. Real-time quotes and adjusted data require separate entitlement checks. | not recorded |
| [ECB Data Portal API](../data/candidates/ecb-data.yaml) | web-search-data/financial-data/fx, web-search-data/financial-data/macro | [data-api (api)](https://data-api.ecb.europa.eu/service/) | unknown | self_serve | documented | Requirements incomplete; Series dimensions, quote direction, observation frequency and date range must be selected correctly. Reference rates are not executable conversion prices. Reference-rate information is freely published under the ECB reuse policy; fees for a run still require observation of the actual route. The documentation page was temporarily unreadable during the latest research pass. | not recorded |
| [EODHD](../data/candidates/eodhd.yaml) | web-search-data/financial-data/prices, web-search-data/financial-data/statements, web-search-data/financial-data/macro, web-search-data/financial-data/disclosures | [data-api (api)](https://eodhd.com/financial-apis/) | unknown | self_serve | documented | Requirements incomplete; 20 requests / day (free_allowance; Free plan; some data types are excluded.); Free registration advertises 20 API calls/day without a card; some data types are excluded. Check dataset and market coverage before choosing a trial. Congressional Trades is documented for the All-in-one plan; the generic 20-call free allowance does not establish access to this dataset. | not recorded |
| [FRED / ALFRED](../data/candidates/fred.yaml) | web-search-data/financial-data/macro | [data-api (api)](https://fred.stlouisfed.org/docs/api/fred/) | unknown | self_serve | documented | Requirements incomplete; A registered account can request an API key. Series units, seasonal adjustment, source and vintage matter; not a stock-price provider. | not recorded |
| [World Bank Indicators API](../data/candidates/world-bank-data.yaml) | web-search-data/financial-data/macro | [data-api (api)](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) | unknown | self_serve | documented | Requirements incomplete; Annual country indicators have publication lags and revisions. Confirm each series and year; do not substitute annual GDP or inflation for monthly US indicators. | not recorded |

<a id="payments-billing"></a>

## Payments / Billing

Payments, billing, subscription infrastructure.

**Includes:** Provides payment collection or billing infrastructure.

**Boundary:** Retrieving financial data or accepting payment for its own API does not qualify.

[Payment Acceptance](#payments-billing-accept-payments)

<a id="payments-billing-accept-payments"></a>

## Payments / Billing / Payment Acceptance

Accept customer payments for products or services; alternatives depend on merchant eligibility, geography and the task.

**Includes:** Enables a merchant to collect customer payments for a product or service.

**Boundary:** A payment link directory or paid API consumption alone is insufficient; merchant eligibility remains separate.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Adyen](../data/candidates/adyen.yaml) | payments-billing/accept-payments | [payment-links-api (api)](https://docs.adyen.com/api-explorer/Checkout/latest/post/paymentLinks) | mixed | unknown | unknown | Requirements incomplete; Requires merchantAccount and API credentials. Test cards and test accounts are documented; test account admission and individual eligibility have not been verified. Live setup needs approval and merchant terms. Pay by Link is described as supplementary to an online store checkout. | not recorded |
| [Airwallex](../data/candidates/airwallex.yaml) | payments-billing/accept-payments | [payment-links-api (api)](https://www.airwallex.com/docs/api/payments/payment_links/api) | mixed | unknown | unknown | Requirements incomplete; API requires an access token and merchant configuration. Sandbox examples are documented, but individual account eligibility, activation and full fees are not established here. Payment success is reported separately from link creation. | not recorded |
| [Alipay](../data/candidates/alipay.yaml) | payments-billing/accept-payments | [web-app-api (api)](https://open.alipay.com/module/webApp) | unknown | application | unknown | Requires: approval; Application setup, signing keys and review are documented for launch. Merchant qualification, supported currencies and a task-compatible sandbox still need verification. Web/app integration is not proof of a standalone shareable checkout link. | not recorded |
| [Checkout.com](../data/candidates/checkout-com.yaml) | payments-billing/accept-payments | [payment-links-api (api)](https://api-reference.checkout.com/tag/Payment-Links/) | mixed | unknown | unknown | Requirements incomplete; API secret key and account-specific host required. Sandbox endpoints are documented; obtaining an account, individual merchant admission and negotiated fees remain unverified. | not recorded |
| [Creem](../data/candidates/creem.yaml) | payments-billing/accept-payments | [sandbox-api (api)](https://docs.creem.io/getting-started/test-mode) | sandbox | self_serve | unknown | Requires: platform_account; Human: Use dashboard Test Mode and obtain a test API key.; Test mode has separate API keys, products and test-api.creem.io. Production account review includes the product website and individual or business identity; do not infer automatic approval from sandbox access. | not recorded |
| [Dodo Payments](../data/candidates/dodo-payments.yaml) | payments-billing/accept-payments | [sandbox-api (api)](https://docs.dodopayments.com/introduction) | sandbox | unknown | unknown | Requires: platform_account; Use test API keys and simulated payments. Individual accounts are documented, but live payments and payouts require product review, identity verification and bank verification. Accepted ID countries apply; sandbox access does not certify live eligibility. | not recorded |
| [Dodo Payments](../data/candidates/dodo-payments.yaml) | payments-billing/accept-payments | [official-cli (cli)](https://github.com/dodopayments/dodopayments-cli) | unknown | unknown | unknown | Requirements incomplete; Official CLI for payments and billing resources. Authentication and environment must be prepared; this route has not been task-tested. | not recorded |
| [Dodo Payments](../data/candidates/dodo-payments.yaml) | payments-billing/accept-payments | [live-api (api)](https://docs.dodopayments.com/introduction) | live | application | documented | Requires: approval, identity_verification; Individual account type is documented, subject to product, identity and bank review plus accepted-country restrictions. Live payments and payouts require approval. No live account was created or approved in this research. | not recorded |
| [Dodo Payments](../data/candidates/dodo-payments.yaml) | payments-billing/accept-payments | [payments-mcp (mcp)](https://mcp.dodopayments.com/sse) | mixed | unknown | unknown | Requirements incomplete; Transactional MCP. Initial OAuth setup asks for the merchant API key and test/live environment; explicitly select test. This is separate from the documentation-only Knowledge MCP and has not been task-tested. | not recorded |
| [FastSpring](../data/candidates/fastspring.yaml) | payments-billing/accept-payments | [official-api (api)](https://developer.fastspring.com/) | unknown | unknown | unknown | Requirements incomplete; Official docs establish API, checkout and subscription integration options. Individual admission, store activation, sandbox prerequisites and applicable fees have not been checked in this discovery pass. | not recorded |
| [Lemon Squeezy](../data/providers/lemonsqueezy.yaml) | payments-billing/accept-payments | [sandbox-api (api)](https://docs.lemonsqueezy.com/guides/developer-guide/taking-payments) | sandbox | unknown | unknown | Requires: platform_account; Use test-mode products and API keys; test resources do not automatically become live products. Store activation and live merchant eligibility must be checked separately. Merchant-of-record checkout applies to digital products/SaaS. | not recorded |
| [Mollie](../data/candidates/mollie.yaml) | payments-billing/accept-payments | [sandbox-api (api)](https://docs.mollie.com/reference/create-payment-link) | sandbox | unknown | unknown | Requires: platform_account; Uses a Test API key (or testmode with supported tokens). Test checkout is a simulator, not the live payment page. Account admission and live payment-method activation remain prerequisites to check separately. | not recorded |
| [paas.build](../data/candidates/paas-build.yaml) | payments-billing/accept-payments | [rest-api (api)](https://paas.build/openapi.json) | mixed | unknown | restricted | Requirements incomplete; PayFac powered by UniPaaS; merchant retains tax responsibilities. Official materials limit onboarding to UK/EU/US merchants. Sandbox and production tokens differ. A 2026-09-08 sandbox-only account and token were prepared successfully. A fresh Codex trial created a remote checkout but hit a browser launch permission failure, so it is invalid for completion-rate comparison. Independent browser review showed only the checkout shell; customer usability remains unverified. | [payment-acceptance-001: invalid_run (2026-09-08)](../data/experiments/evaluations/codex-20260908T113239.160717Z-paas-build.json) |
| [paas.build](../data/candidates/paas-build.yaml) | payments-billing/accept-payments | [official-mcp (mcp)](https://paas.build/mcp) | mixed | unknown | unknown | Requirements incomplete; Discovery verified four tools on 2026-09-08. Default onboarding can provision both environments and send notifications; explicitly prepare sandbox-only access. Protocol discovery is not task completion. | not recorded |
| [Paddle](../data/providers/paddle.yaml) | payments-billing/accept-payments | [sandbox-api (api)](https://developer.paddle.com/sdks/sandbox/) | sandbox | self_serve | unknown | Requires: platform_account; Human: Register the separate sandbox account and obtain its API key.; Create a separate sandbox account with sandbox credentials. Sandbox does not require the domain and checkout approvals needed for live sales. Merchant-of-record responsibilities and live account review differ from payment processing alone. On 2026-09-09, sandbox email verification completed and a seven-day API key was created with scoped permissions. An authenticated sandbox products read returned HTTP 200 with an empty catalog. No KYC, production activation or payment was performed. Account setup alone is not a completed checkout task. The first ebook checkout task was not completed: POST /products rejected ebooks with product_tax_category_not_approved. The authenticated sandbox dashboard showed eBook Not Requested and SaaS Approved, with a notice that category approval must be requested in a live account. No live application was made. This result concerns the default account and ebook scenario, not approved categories or all Paddle checkouts. | [payment-acceptance-001: not_completed (2026-09-09)](../data/experiments/evaluations/codex-20260909T032011.000426Z-paddle.json) |
| [PayPal](../data/candidates/paypal.yaml) | payments-billing/accept-payments | [sandbox-api (api)](https://developer.paypal.com/api/rest) | sandbox | self_serve | unknown | Requires: platform_account; Human: Create a developer account and obtain sandbox app client credentials.; Developer dashboard supplies sandbox buyer and seller accounts and app credentials. Going live requires a Business account; merchant country and personal eligibility need separate checks. | not recorded |
| [Ping++](../data/candidates/pingxx.yaml) | payments-billing/accept-payments | [sandbox-api (api)](https://www.pingxx.com/api/%E8%AE%A4%E8%AF%81.html) | sandbox | unknown | unknown | Requires: platform_account; Dashboard provides separate test/live API keys; test transactions are documented as simulated and without actual transaction fees. Channel-specific merchant permissions may still be needed for live use. Current individual admission and channel fees need verification. | not recorded |
| [Ping++](../data/candidates/pingxx.yaml) | payments-billing/accept-payments | [web-sdk (sdk)](https://www.pingxx.com/docs/client/web.html) | unknown | unknown | unknown | Requirements incomplete; Web SDK consumes server-created Charge credentials and invokes the selected payment channel. This is not a separate merchant account or a waiver of channel admission. | not recorded |
| [Polar](../data/candidates/polar.yaml) | payments-billing/accept-payments | [sandbox-api (api)](https://polar.sh/docs/integrate/sandbox) | sandbox | self_serve | unknown | Requires: platform_account; Human: Create a sandbox account and organization, then issue sandbox credentials.; Create a separate sandbox account and organization; production credentials cannot be reused. Sandbox customer email delivery is restricted. Live payouts depend on Polar's supported seller countries and Stripe Connect Express, not the Stripe Payments country list. | not recorded |
| [Razorpay](../data/candidates/razorpay.yaml) | payments-billing/accept-payments | [payment-links-api (api)](https://razorpay.com/docs/api/payments/payment-links/create-standard/) | mixed | unknown | unknown | Requirements incomplete; Documentation limits test-mode creation to 30 payment links per business before contacting support. API-key access, merchant geography, KYC and production eligibility need preparation checks; a documented test endpoint does not establish individual admission. | not recorded |
| [Square](../data/candidates/square.yaml) | payments-billing/accept-payments | [sandbox-api (api)](https://developer.squareup.com/reference/square/checkout-api/CreatePaymentLink) | sandbox | self_serve | unknown | Requires: platform_account; 0 USD / sandbox API call (usage; Documented free sandbox API calls; not live processing or model usage.); Human: Create an application and select its sandbox seller account and access token.; Requires a Square account, application and sandbox seller location. Sandbox is free; live merchant eligibility is separate. Hosted checkout behavior must be checked before treating a sandbox link as a usable customer page. | not recorded |
| [Stripe](../data/providers/stripe.yaml) | payments-billing/accept-payments | [sandbox-api (api)](https://docs.stripe.com/payment-links/create) | sandbox | unknown | unknown | Requires: platform_account; Use isolated sandbox resources and test API keys. One-time and recurring product prices are documented. Live account activation, merchant country eligibility and tax responsibilities require separate checks. | not recorded |
| [WeChat Pay](../data/candidates/wechat-pay.yaml) | payments-billing/accept-payments | [native-api (api)](https://pay.wechatpay.cn/doc/v3/merchant/4012791877) | unknown | unknown | unknown | Requirements incomplete; Native checkout is a QR payment flow, not a browser-hosted card checkout. Merchant admission, individual eligibility and an applicable free sandbox remain unknown in this discovery pass; do not simulate success by using a live small-value payment. | not recorded |
| [Whop](../data/candidates/whop.yaml) | payments-billing/accept-payments | [official-api (api)](https://docs.whop.com/) | unknown | unknown | unknown | Requirements incomplete; Docs describe dashboard API keys and checkout integration. Merchant eligibility, sandbox coverage, service responsibilities and full fees still need verification; buyer availability does not establish seller eligibility. | not recorded |

<a id="communication"></a>

## Communication

Email, SMS, chat, notifications.

**Includes:** Enables email, messaging or live voice communication.

**Boundary:** Text-to-speech alone is an AI content service, not communication delivery.

[Mailboxes](#communication-mailboxes) · [Email Delivery](#communication-email-delivery) · [Messaging](#communication-messaging) · [SMS Delivery](#communication-sms) · [Voice Calls](#communication-voice-calls) · [Voice Agents](#communication-voice-agents)

<a id="communication-mailboxes"></a>

## Communication / Mailboxes

Mailboxes for receiving and managing email; temporary and persistent accounts have different retention and access conditions.

**Includes:** Provides a mailbox with later access to received email.

**Boundary:** Sending email alone and single callback notifications are insufficient; retention and mailbox ownership must match.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [AgentMail](../data/candidates/agentmail.yaml) | communication/mailboxes | [mail-api (api)](https://docs.agentmail.to/quickstart) | unknown | unknown | unknown | Requirements incomplete; Agent signup accepts an owner email and sends an OTP. Verification unlocks full permissions; existing owner accounts cannot use first-time signup. Signup can rotate an existing unverified key, so inspect account state before retrying. Published Free plan: 3 inboxes and 3,000 emails/month, no card required; not observed account entitlement. | not recorded |
| [AgentMail](../data/candidates/agentmail.yaml) | communication/mailboxes | [mail-sdk (sdk)](https://docs.agentmail.to/quickstart) | unknown | unknown | unknown | Requirements incomplete; Separate route; shares the service account and plan limits. No task result inherited from other routes. | not recorded |
| [AgentMail](../data/candidates/agentmail.yaml) | communication/mailboxes | [mail-cli (cli)](https://docs.agentmail.to/quickstart) | unknown | unknown | unknown | Requirements incomplete; Separate route; shares the service account and plan limits. No task result inherited from other routes. | not recorded |
| [AgentMail](../data/candidates/agentmail.yaml) | communication/mailboxes | [mail-mcp (mcp)](https://mcp.agentmail.to/mcp) | unknown | unknown | unknown | Requirements incomplete; Separate route; shares the service account and plan limits. No task result inherited from other routes. | not recorded |
| [Fastmail](../data/candidates/fastmail.yaml) | communication/mailboxes | [mail-api (api)](https://www.fastmail.com/dev/) | unknown | unknown | unknown | Requirements incomplete; JMAP tokens can be generated for an existing account. Subscription/trial API eligibility is not yet verified; do not assume permanent free access. | not recorded |
| [Gmail](../data/candidates/gmail.yaml) | communication/mailboxes | [mail-api (api)](https://developers.google.com/workspace/gmail/api/guides) | unknown | unknown | unknown | Requirements incomplete; Existing mailbox, API project and scoped OAuth consent are separate preparation steps. Gmail API access is not a public API for creating consumer Google accounts. | not recorded |
| [Guerrilla Mail](../data/candidates/guerrilla-mail.yaml) | communication/mailboxes | [mail-api (api)](https://www.guerrillamail.com/GuerrillaMailAPI.html) | unknown | unknown | unknown | Requirements incomplete; Public API uses session cookies. Documentation is old and describes short message/session retention; current HTTPS access and behavior require testing. Not a persistent private-account substitute. On 2026-09-09, a fresh Codex session created a mailbox without upstream credentials; independent reuse of its saved access state succeeded. This tests provisioning/listing only, not external delivery or long-term retention. In a subsequent Gmail-delivered fixture test, all three synthetic message bodies arrived, but listing and full-message APIs returned blank subjects. The Agent retrieved the correct latest login code and timestamp, but the task requiring the original subject was not fully completed; this does not establish that all emails lose subjects. | [mailboxes-create-001: completed (2026-09-09)](../data/experiments/evaluations/codex-20260909T102405.681663Z-guerrilla-mail.json); [mailboxes-code-001: not_completed (2026-09-09)](../data/experiments/evaluations/codex-20260909T103849.955516Z-guerrilla-mail.json) |
| [Mail.tm](../data/candidates/mail-tm.yaml) | communication/mailboxes | [mail-api (api)](https://docs.mail.tm/) | unknown | unknown | unknown | Requirements incomplete; Free public API; creating the mailbox also creates its account. No upstream user account or paid API key is required. Temporary domains and retention must be checked before using for important accounts. On 2026-09-09, a fresh Codex session created a mailbox without upstream credentials; independent reuse of its saved access state succeeded. This tests provisioning/listing only, not external delivery or long-term retention. A subsequent independent medium session retrieved the correct latest login code, subject and timestamp from three real synthetic emails delivered by Gmail. This does not establish acceptance by arbitrary signup websites. | [mailboxes-create-001: completed (2026-09-09)](../data/experiments/evaluations/codex-20260909T102400.674330Z-mail-tm.json); [mailboxes-code-001: completed (2026-09-09)](../data/experiments/evaluations/codex-20260909T103356.699996Z-mail-tm.json) |
| [Mailinator](../data/candidates/mailinator.yaml) | communication/mailboxes | [mail-api (api)](https://www.mailinator.com/docs/) | unknown | unknown | unknown | Requirements incomplete; Free public website inbox access does not establish free API access. Verify private-domain/API subscription eligibility before preparing a trial. | not recorded |
| [Mailsac](../data/candidates/mailsac.yaml) | communication/mailboxes | [mail-api (api)](https://docs.mailsac.com/en/latest/about/introduction.html) | unknown | unknown | unknown | Requirements incomplete; API key required; public inboxes are publicly viewable. Private addresses and retention depend on the plan; no real registration secrets should be placed in a public inbox. | not recorded |
| [MailSink](../data/candidates/mailsink.yaml) | communication/mailboxes | [mail-api (api)](https://mailsink.dev/docs/) | unknown | unknown | unknown | Requirements incomplete; Homepage advertises anonymous mode, but current quickstart says GitHub login and Bearer token are required for all API requests. Preserve this conflict until observed; do not assume anonymous access. | not recorded |
| [MailSink](../data/candidates/mailsink.yaml) | communication/mailboxes | [mail-mcp (mcp)](https://mailsink.dev/docs/) | unknown | unknown | unknown | Requirements incomplete; Official @mailsink/mcp setup requires MAILSINK_API_KEY. Anonymous-mode conflict remains unresolved. | not recorded |
| [MailSlurp](../data/candidates/mailslurp.yaml) | communication/mailboxes | [mail-api (api)](https://www.mailslurp.com/guides/getting-started/) | unknown | unknown | unknown | Requirements incomplete; A service account and API key are required. Free plan has caps and sandbox-only sending; receiving real email and sending externally have different entitlements. | not recorded |
| [MailSlurp](../data/candidates/mailslurp.yaml) | communication/mailboxes | [mail-mcp (mcp)](https://www.mailslurp.com/docs/agents/) | unknown | unknown | unknown | Requirements incomplete; Agent-scoped access requires account setup; task usage has not been measured. | not recorded |
| [Outlook Mail](../data/candidates/outlook-mail.yaml) | communication/mailboxes | [mail-api (api)](https://learn.microsoft.com/en-us/graph/outlook-mail-concept-overview) | unknown | unknown | unknown | Requirements incomplete; Personal versus organizational accounts and delegated permissions differ. Requires mailbox ownership and app authorization; Graph mail access does not create consumer Microsoft accounts. | not recorded |
| [Temp Mail](../data/candidates/temp-mail.yaml) | communication/mailboxes | [mail-api (api)](https://temp-mail.org/en/api/) | unknown | unknown | unknown | Requirements incomplete; Free web inboxes do not establish free developer API access. API credentials, pricing and retention require preparation checks. | not recorded |
| [Zoho Mail](../data/candidates/zoho-mail.yaml) | communication/mailboxes | [mail-api (api)](https://www.zoho.com/mail/help/api/getting-started-with-api.html) | unknown | unknown | unknown | Requirements incomplete; Account, OAuth client/scopes and data-center endpoint must be prepared. Free mailbox availability does not establish the API permissions required by a task. | not recorded |

<a id="communication-email-delivery"></a>

## Communication / Email Delivery

Send application email to recipients.

**Includes:** Provides programmatic email delivery and delivery outcomes.

**Boundary:** Mailbox provisioning and incoming-email reading alone do not qualify.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Resend](../data/providers/resend.yaml) | communication/email-delivery | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="communication-messaging"></a>

## Communication / Messaging

Read and send messages in conversations or channels.

**Includes:** Exposes conversation/channel messaging operations.

**Boundary:** SMS transport and passive social-data retrieval are separate.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Discord](../data/providers/discord.yaml) | communication/messaging | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Lark](../data/providers/lark.yaml) | productivity-storage/collaborative-tables, communication/messaging, productivity-storage/document-collaboration | [base-api (api)](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create) | unknown | self_serve | unknown | Requirements incomplete; 2000 rows / table (free_allowance; Starter Base table limit; access still depends on tenant/app scopes.); Requires a platform app, authorized identity and Base scopes/resource permissions. Ordinary-person onboarding from a fresh account is not tested. | not recorded |
| [Lark](../data/providers/lark.yaml) | productivity-storage/collaborative-tables, communication/messaging, productivity-storage/document-collaboration | [official-cli (cli)](https://github.com/larksuite/cli) | unknown | self_serve | unknown | Requirements incomplete; Official CLI covers Base and supports individuals. Account signup, app creation and permission setup still need separate verification. | not recorded |
| [Lark](../data/providers/lark.yaml) | productivity-storage/collaborative-tables, communication/messaging, productivity-storage/document-collaboration | [official-mcp (mcp)](https://github.com/larksuite/lark-openapi-mcp) | unknown | self_serve | unknown | Requirements incomplete; Local official MCP package uses platform app credentials; identity and tenant domains must match. | not recorded |
| [Slack](../data/providers/slack.yaml) | communication/messaging | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Telegram Bot API](../data/providers/telegram.yaml) | communication/messaging | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="communication-sms"></a>

## Communication / SMS Delivery

Send and receive carrier text messages.

**Includes:** Provides delivery to phone-number recipients over SMS.

**Boundary:** In-app chat messages and number verification alone are insufficient.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Twilio](../data/providers/twilio.yaml) | communication/sms, communication/voice-calls | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="communication-voice-calls"></a>

## Communication / Voice Calls

Establish and handle live voice calls.

**Includes:** Provides live calling or a voice agent that can participate in calls.

**Boundary:** Speech synthesis/transcription alone does not establish calling.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Twilio](../data/providers/twilio.yaml) | communication/sms, communication/voice-calls | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Vapi](../data/providers/vapi.yaml) | communication/voice-agents, communication/voice-calls | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="communication-voice-agents"></a>

## Communication / Voice Agents

Operate conversational agents over live voice.

**Includes:** Orchestrates listening, response generation and speech in an interactive session.

**Boundary:** A standalone speech model or telephony transport alone is insufficient.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Cartesia](../data/providers/cartesia.yaml) | ai-models/speech-synthesis, ai-models/speech-recognition, communication/voice-agents | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Deepgram](../data/providers/deepgram.yaml) | ai-models/speech-recognition, ai-models/speech-synthesis, communication/voice-agents | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [ElevenLabs](../data/providers/elevenlabs.yaml) | ai-models/speech-synthesis, ai-models/speech-recognition, communication/voice-agents | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Vapi](../data/providers/vapi.yaml) | communication/voice-agents, communication/voice-calls | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="productivity-storage"></a>

## Workplace Collaboration

Documents, collaborative tables, project management and file sharing; application object storage belongs under cloud services.

**Includes:** Organizes shared work, documents, tasks or files for people.

**Boundary:** Application database and object-storage APIs alone are not office collaboration.

[Collaborative Tables](#productivity-storage-collaborative-tables) · [Project & Task Management](#productivity-storage-project-management) · [Document Collaboration](#productivity-storage-document-collaboration) · [File Sharing](#productivity-storage-file-sharing)

<a id="productivity-storage-collaborative-tables"></a>

## Workplace Collaboration / Collaborative Tables

User-facing online tables for organizing and following up shared work.

**Includes:** Provides user-facing shared tables with structured records.

**Boundary:** A backend database without collaborative work-table features is insufficient.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Airtable](../data/providers/airtable.yaml) | productivity-storage/collaborative-tables | [web-api (api)](https://airtable.com/developers/web/api/introduction) | unknown | self_serve | documented | Requirements incomplete; 1000 API calls / workspace/month (free_allowance; Free plan; includes metadata/schema calls, 5 requests/second/base.); 1000 records / base (free_allowance; Free plan storage limit across all tables in a base.); Human: Create a personal access token with required scopes and selected test resources.; PAT scopes plus selected workspace/base access required. Base creation is documented on all plans; do not infer paid-only access from outdated posts. | not recorded |
| [Baserow Cloud](../data/candidates/baserow.yaml) | productivity-storage/collaborative-tables | [database-api (api)](https://baserow.io/docs/apis/rest-api) | unknown | self_serve | documented | Requirements incomplete; 3000 rows / workspace (free_allowance; Cloud Free plan. 2 GB storage. JWT/schema access and database row tokens are distinct.); Human: Generate a database token and select permitted tables and operations.; Database token can read/create/update/delete rows in permitted tables; creating the table/schema requires a short-lived JWT. A precreated table changes the test setup. | not recorded |
| [Baserow Cloud](../data/candidates/baserow.yaml) | productivity-storage/collaborative-tables | [native-mcp (mcp)](https://baserow.io/user-docs/mcp-server) | unknown | unknown | unknown | Requirements incomplete; Human: Create a workspace MCP endpoint in account settings and securely store its private URL.; Workspace admin creates a unique secret-bearing endpoint URL; the URL is itself a credential and must not be published. Documented tools read schema/list tables and create/update/delete rows, but do not list table creation. Cloud plan availability is not yet verified; do not assume this route can provision task 001 from an empty container. | not recorded |
| [Coda / Superhuman Docs](../data/candidates/coda.yaml) | productivity-storage/collaborative-tables, productivity-storage/document-collaboration | [rest-api (api)](https://coda.io/developers/apis/v1) | unknown | self_serve | unknown | Requirements incomplete; API available in free and paid workspaces. Creating docs requires a Doc Maker role; row writes may be asynchronous. Table/schema creation support must be verified for the task. | not recorded |
| [Coda / Superhuman Docs](../data/candidates/coda.yaml) | productivity-storage/collaborative-tables, productivity-storage/document-collaboration | [hosted-mcp (mcp)](https://coda.io/apis/mcp) | unknown | self_serve | unknown | Requirements incomplete; Official hosted MCP; connector setup needs authorization. | not recorded |
| [飞书 Feishu](../data/candidates/feishu.yaml) | productivity-storage/collaborative-tables | [base-api (api)](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/create) | unknown | self_serve | unknown | Requirements incomplete; Requires a platform app, authorized identity and Base scopes/resource permissions. Ordinary-person onboarding from a fresh account is not tested. | not recorded |
| [飞书 Feishu](../data/candidates/feishu.yaml) | productivity-storage/collaborative-tables | [official-cli (cli)](https://github.com/larksuite/cli) | unknown | self_serve | unknown | Requirements incomplete; Official CLI covers Base and supports individuals. Account signup, app creation and permission setup still need separate verification. | not recorded |
| [飞书 Feishu](../data/candidates/feishu.yaml) | productivity-storage/collaborative-tables | [official-mcp (mcp)](https://github.com/larksuite/lark-openapi-mcp) | unknown | self_serve | unknown | Requirements incomplete; Local official MCP package uses platform app credentials; identity and tenant domains must match. | not recorded |
| [Google Sheets](../data/candidates/google-sheets.yaml) | productivity-storage/collaborative-tables | [sheets-api (api)](https://developers.google.com/workspace/sheets/api/guides/concepts) | unknown | self_serve | unknown | Requirements incomplete; 0 USD / standard API usage (usage; Sheets API standard use has no additional cost; per-minute quotas apply.); Human: Configure a Cloud project and OAuth consent/client, then authorize selected account access.; Quickstart requires a Google account, Cloud project, enabled Sheets API and OAuth client/consent setup. Service accounts are another route, not assumed preconfigured. | not recorded |
| [Grist](../data/candidates/grist.yaml) | productivity-storage/collaborative-tables | [rest-api (api)](https://support.getgrist.com/api/) | unknown | self_serve | documented | Requirements incomplete; 5000 records / document (free_allowance; Hosted Free plan; API quota must also be checked for the selected site.); Human: Sign in and generate an API key in account settings.; Account API key grants the user’s existing access. Use a separate free test account; personal site is freely available. | [collaborative-tables-001: completed (2026-09-08)](../data/experiments/evaluations/codex-20260908T032113.556233Z-grist.json); [collaborative-tables-001: completed (2026-09-08)](../data/experiments/evaluations/codex-20260908T035504.472694Z-grist.json) |
| [Grist](../data/candidates/grist.yaml) | productivity-storage/collaborative-tables | [hosted-mcp (mcp)](https://docs.getgrist.com/api/mcp) | unknown | self_serve | documented | Requirements incomplete; Hosted server accepts API keys or interactive OAuth; available on all plans. Calls share the API pool. | not recorded |
| [Grist](../data/candidates/grist.yaml) | productivity-storage/collaborative-tables | [python-sdk (sdk)](https://pypi.org/project/grist-api/) | unknown | unknown | unknown | Requirements incomplete; Official Python client linked by Grist REST API guide; SDK installation does not remove account permission requirements. | not recorded |
| [Grist](../data/candidates/grist.yaml) | productivity-storage/collaborative-tables | [javascript-sdk (sdk)](https://www.npmjs.com/package/grist-api) | unknown | unknown | unknown | Requirements incomplete; Official JavaScript/TypeScript client linked by Grist REST API guide; npm page fetch returned 403 during public research, not a service failure. | not recorded |
| [Lark](../data/providers/lark.yaml) | productivity-storage/collaborative-tables, communication/messaging, productivity-storage/document-collaboration | [base-api (api)](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create) | unknown | self_serve | unknown | Requirements incomplete; 2000 rows / table (free_allowance; Starter Base table limit; access still depends on tenant/app scopes.); Requires a platform app, authorized identity and Base scopes/resource permissions. Ordinary-person onboarding from a fresh account is not tested. | not recorded |
| [Lark](../data/providers/lark.yaml) | productivity-storage/collaborative-tables, communication/messaging, productivity-storage/document-collaboration | [official-cli (cli)](https://github.com/larksuite/cli) | unknown | self_serve | unknown | Requirements incomplete; Official CLI covers Base and supports individuals. Account signup, app creation and permission setup still need separate verification. | not recorded |
| [Lark](../data/providers/lark.yaml) | productivity-storage/collaborative-tables, communication/messaging, productivity-storage/document-collaboration | [official-mcp (mcp)](https://github.com/larksuite/lark-openapi-mcp) | unknown | self_serve | unknown | Requirements incomplete; Local official MCP package uses platform app credentials; identity and tenant domains must match. | not recorded |
| [Notion](../data/providers/notion.yaml) | productivity-storage/collaborative-tables, productivity-storage/document-collaboration | [rest-api (api)](https://developers.notion.com/reference/intro) | unknown | self_serve | documented | Requirements incomplete; 0 USD / month (free_allowance; Free workspace subscription; API limits and resource permissions still apply.); Human: Create internal connection and grant only the test page, or create a PAT in a dedicated test workspace.; Internal connection requires workspace owner creation and explicit page sharing; PAT acts with creator permissions in the selected workspace. Free-plan PAT creation is restricted to workspace owners; being a free member alone is insufficient. | [collaborative-tables-001: completed (2026-09-08)](../data/experiments/evaluations/codex-20260908T032850.330773Z-notion.json); [collaborative-tables-001: completed (2026-09-08)](../data/experiments/evaluations/codex-20260908T035504.906378Z-notion.json) |
| [Notion](../data/providers/notion.yaml) | productivity-storage/collaborative-tables, productivity-storage/document-collaboration | [javascript-sdk (sdk)](https://github.com/makenotion/notion-sdk-js) | unknown | self_serve | unknown | Requirements incomplete; Official client library over the REST API; credentials and resource grants remain necessary. | not recorded |
| [Notion](../data/providers/notion.yaml) | productivity-storage/collaborative-tables, productivity-storage/document-collaboration | [official-cli (cli)](https://developers.notion.com/cli/get-started/overview) | unknown | self_serve | unknown | Requirements incomplete; Official CLI discovered in current docs; measure separately from raw REST. | not recorded |
| [Notion](../data/providers/notion.yaml) | productivity-storage/collaborative-tables, productivity-storage/document-collaboration | [hosted-mcp (mcp)](https://mcp.notion.com/mcp) | unknown | self_serve | unknown | Requirements incomplete; Official hosted MCP requires interactive OAuth. Token-based open-source server is no longer actively maintained. | not recorded |

<a id="productivity-storage-project-management"></a>

## Workplace Collaboration / Project & Task Management

Track work items, ownership and progress.

**Includes:** Provides durable tasks/issues and their status in a shared work context.

**Boundary:** Code storage and free-form documents alone are insufficient.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Atlassian (Jira & Confluence)](../data/providers/atlassian.yaml) | developer-tools/code-hosting, productivity-storage/project-management, productivity-storage/document-collaboration | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [GitHub](../data/providers/github.yaml) | developer-tools/code-hosting, productivity-storage/project-management | [rest-api (api)](https://api.github.com/) | unknown | self_serve | documented | Requirements incomplete; Authenticated REST access; existing account setup and token permissions must be recorded separately from the task. | not recorded |
| [GitLab](../data/providers/gitlab.yaml) | developer-tools/code-hosting, productivity-storage/project-management | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Linear](../data/providers/linear.yaml) | productivity-storage/project-management | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="productivity-storage-document-collaboration"></a>

## Workplace Collaboration / Document Collaboration

Create, edit and share working documents.

**Includes:** Provides collaborative document content and access.

**Boundary:** Files stored without document editing are file sharing; JSON document storage is a database.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Atlassian (Jira & Confluence)](../data/providers/atlassian.yaml) | developer-tools/code-hosting, productivity-storage/project-management, productivity-storage/document-collaboration | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Coda / Superhuman Docs](../data/candidates/coda.yaml) | productivity-storage/collaborative-tables, productivity-storage/document-collaboration | [rest-api (api)](https://coda.io/developers/apis/v1) | unknown | self_serve | unknown | Requirements incomplete; API available in free and paid workspaces. Creating docs requires a Doc Maker role; row writes may be asynchronous. Table/schema creation support must be verified for the task. | not recorded |
| [Coda / Superhuman Docs](../data/candidates/coda.yaml) | productivity-storage/collaborative-tables, productivity-storage/document-collaboration | [hosted-mcp (mcp)](https://coda.io/apis/mcp) | unknown | self_serve | unknown | Requirements incomplete; Official hosted MCP; connector setup needs authorization. | not recorded |
| [Lark](../data/providers/lark.yaml) | productivity-storage/collaborative-tables, communication/messaging, productivity-storage/document-collaboration | [base-api (api)](https://open.larksuite.com/document/server-docs/docs/bitable-v1/app/create) | unknown | self_serve | unknown | Requirements incomplete; 2000 rows / table (free_allowance; Starter Base table limit; access still depends on tenant/app scopes.); Requires a platform app, authorized identity and Base scopes/resource permissions. Ordinary-person onboarding from a fresh account is not tested. | not recorded |
| [Lark](../data/providers/lark.yaml) | productivity-storage/collaborative-tables, communication/messaging, productivity-storage/document-collaboration | [official-cli (cli)](https://github.com/larksuite/cli) | unknown | self_serve | unknown | Requirements incomplete; Official CLI covers Base and supports individuals. Account signup, app creation and permission setup still need separate verification. | not recorded |
| [Lark](../data/providers/lark.yaml) | productivity-storage/collaborative-tables, communication/messaging, productivity-storage/document-collaboration | [official-mcp (mcp)](https://github.com/larksuite/lark-openapi-mcp) | unknown | self_serve | unknown | Requirements incomplete; Local official MCP package uses platform app credentials; identity and tenant domains must match. | not recorded |
| [Notion](../data/providers/notion.yaml) | productivity-storage/collaborative-tables, productivity-storage/document-collaboration | [rest-api (api)](https://developers.notion.com/reference/intro) | unknown | self_serve | documented | Requirements incomplete; 0 USD / month (free_allowance; Free workspace subscription; API limits and resource permissions still apply.); Human: Create internal connection and grant only the test page, or create a PAT in a dedicated test workspace.; Internal connection requires workspace owner creation and explicit page sharing; PAT acts with creator permissions in the selected workspace. Free-plan PAT creation is restricted to workspace owners; being a free member alone is insufficient. | not recorded |
| [Notion](../data/providers/notion.yaml) | productivity-storage/collaborative-tables, productivity-storage/document-collaboration | [javascript-sdk (sdk)](https://github.com/makenotion/notion-sdk-js) | unknown | self_serve | unknown | Requirements incomplete; Official client library over the REST API; credentials and resource grants remain necessary. | not recorded |
| [Notion](../data/providers/notion.yaml) | productivity-storage/collaborative-tables, productivity-storage/document-collaboration | [official-cli (cli)](https://developers.notion.com/cli/get-started/overview) | unknown | self_serve | unknown | Requirements incomplete; Official CLI discovered in current docs; measure separately from raw REST. | not recorded |
| [Notion](../data/providers/notion.yaml) | productivity-storage/collaborative-tables, productivity-storage/document-collaboration | [hosted-mcp (mcp)](https://mcp.notion.com/mcp) | unknown | self_serve | unknown | Requirements incomplete; Official hosted MCP requires interactive OAuth. Token-based open-source server is no longer actively maintained. | not recorded |

<a id="productivity-storage-file-sharing"></a>

## Workplace Collaboration / File Sharing

Store, organize and share user files.

**Includes:** Provides user file/folder storage and sharing controls.

**Boundary:** Object storage used only as an application backend is separate.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Dropbox](../data/providers/dropbox.yaml) | productivity-storage/file-sharing | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="commerce-marketing"></a>

## E-commerce

Services for building and operating online stores.

**Includes:** Operates an online store, including products, inventory, carts or orders.

**Boundary:** Payment processing alone belongs under payments; no store subcategory is asserted from one provider.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Shopify](../data/providers/shopify.yaml) | commerce-marketing | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |

<a id="travel"></a>

## Travel

Services for planning and purchasing travel as an individual.

**Includes:** Finds or arranges travel inventory for individual travelers.

**Boundary:** Generic map, weather or payment services alone do not qualify.

[Flights](#travel-flights)

<a id="travel-flights"></a>

## Travel / Flights

Flight offers, fare comparison, purchase links and ticketing.

**Includes:** Returns flight offers or supports their purchase or ticketing.

**Boundary:** Airport information, schedules or status without offers are insufficient; ticket issuance is separately documented.



| Service | Classification | Route | Data kind | Availability | Personal access | Requirements, published costs and limits | Observed tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [AirGateway Platform API](../data/candidates/airgateway.yaml) | travel/flights | [agency-api (api)](https://support.airgateway.com/en-US/kb/article/4/introduction-to-airgateway-platform-api) | unknown | application | restricted | Requires: company, industry_license, approval; This does not prove the absence of other individual-facing AirGateway products. | not recorded |
| [Amadeus Flight APIs](../data/candidates/amadeus-flights.yaml) | travel/flights | [former-self-service (api)](https://developers.amadeus.com/blog/comparing-open-source-flight-data-sources) | unknown | retired | unknown | Requirements incomplete; Retain this historical access path. Stale tutorials do not establish current self-service signup. | not recorded |
| [Amadeus Flight APIs](../data/candidates/amadeus-flights.yaml) | travel/flights | [enterprise-api (api)](https://developers.amadeus.com/) | unknown | unknown | unknown | Requirements incomplete; Current portal lead; personal eligibility, application requirements, costs and current flight endpoints remain unknown. | not recorded |
| [apiheya Air Scraper](../data/candidates/apiheya-air-scraper.yaml) | travel/flights | [rapidapi-product (api)](https://rapidapi.com/apiheya/api/sky-scrapper/playground/apiendpoint_6856e0a6-2804-43cd-9cc0-bb377022981e) | unknown | unknown | unknown | Requires: platform_account; 20 requests / month (free_allowance; Listed Basic plan; card requirements and included flight endpoints unverified.); Publisher is apiheya; RapidAPI is the marketplace. Upstream identity is not established by a product slug. | not recorded |
| [Aviasales via Travelpayouts](../data/candidates/aviasales.yaml) | travel/flights | [live-search-api (api)](https://support.travelpayouts.com/hc/en-us/articles/210995808-How-to-get-access-to-the-Aviasales-Search-API) | live | application | restricted | Requires: platform_account, approval, traffic | not recorded |
| [Aviasales via Travelpayouts](../data/candidates/aviasales.yaml) | travel/flights | [cached-data-api (api)](https://support.travelpayouts.com/hc/en-us/articles/203956163-Aviasales-Data-API) | cached | self_serve | unknown | Requires: platform_account; Historical user-search cache for price trends and inspiration. Each method has its own time window; no fresh search is triggered. | not recorded |
| [Bright Data SERP API](../data/candidates/bright-data-serp.yaml) | travel/flights | [google-flights-serp (api)](https://docs.brightdata.com/api-reference/serp/google-flights/currency) | unknown | unknown | unknown | Requirements incomplete; Requires a SERP zone. Do not apply other Bright Data products’ payment requirements to this route. | not recorded |
| [携程机票合作](../data/candidates/ctrip-flights.yaml) | travel/flights | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Duffel Flights API](../data/candidates/duffel-flights.yaml) | travel/flights | [test-api (api)](https://duffel.com/docs/api/overview/test-mode) | sandbox | self_serve | unknown | Requirements incomplete; Duffel Airways test prices and schedules are fictitious. Test-token success cannot establish live fare access. | not recorded |
| [Duffel Flights API](../data/candidates/duffel-flights.yaml) | travel/flights | [live-api (api)](https://duffel.com/guides/getting-started) | unknown | unknown | unknown | Requires: email_verification, identity_verification; Human: Verify email and submit individual or business details; Live permissions, market coverage and pricing must be checked using a real eligible account. | not recorded |
| [Expedia XAP Flight Listings](../data/candidates/expedia-xap-flights.yaml) | travel/flights | [flight-listings-api (api)](https://developers.expediagroup.com/xap-apis/api/shopping-apis/flight-listings) | unknown | paused | restricted | Requirements incomplete | not recorded |
| [飞猪国内机票开放平台](../data/candidates/fliggy-domestic-flights.yaml) | travel/flights | [merchant-api (api)](https://open.alitrip.com/businessDetail.htm?tagId=85) | unknown | unknown | restricted | Requires: company, store, industry_license; 商家店铺须绑定支付宝并使用聚石塔；不能将政策和订单接口记成消费者搜索能力。其他个人入口未知。 | not recorded |
| [Flight MCP](../data/candidates/flight-mcp.yaml) | travel/flights | [authenticated-api (api)](https://flight-mcp.com/docs) | mixed | self_serve | unknown | Requirements incomplete; 300 new_fetches / month (free_allowance; Authenticated free plan; cache hits do not consume this allowance.) | not recorded |
| [Flight MCP](../data/candidates/flight-mcp.yaml) | travel/flights | [authenticated-mcp (mcp)](https://flight-mcp.com/docs) | mixed | self_serve | unknown | Requirements incomplete; 300 new_fetches / month (free_allowance; Authenticated free plan; cache hits do not consume this allowance.) | not recorded |
| [Flight MCP](../data/candidates/flight-mcp.yaml) | travel/flights | [public-cache-api (api)](https://flight-mcp.com/docs) | cached | self_serve | unknown | Requirements incomplete; Only 10 specified directed routes, one adult, economy, USD, en-US and US point of sale; per-date weekly cache refresh over 180 days. Does not trigger fresh queries for arbitrary routes. | not recorded |
| [Flight MCP](../data/candidates/flight-mcp.yaml) | travel/flights | [public-cache-mcp (mcp)](https://flight-mcp.com/docs) | cached | self_serve | unknown | Requirements incomplete; Only 10 specified directed routes, one adult, economy, USD, en-US and US point of sale; per-date weekly cache refresh over 180 days. Does not trigger fresh queries for arbitrary routes. | not recorded |
| [FlightAPI.io Flight Price API](../data/candidates/flightapi-io.yaml) | travel/flights | [price-api (api)](https://www.flightapi.io/documentation/) | unknown | self_serve | unknown | Requirements incomplete; 2 credits / request (usage; One-way or round-trip flight-price query.); 5 credits / request (usage; Multi-city flight-price query.); Trial quota units, card requirements and new-account endpoint access still need verification. | not recorded |
| [Ignav Flights](../data/candidates/ignav.yaml) | travel/flights | [public-playground (web)](https://ignav.com/playground) | unknown | self_serve | unknown | Requirements incomplete; Public trial UI; limits and selectable markets may differ from the customer API. Experimental observations remain separate from catalog claims. | [flights-search-001: completed (2026-09-07)](../data/experiments/evaluations/codex-20260907T083644.877057Z-ignav.json) |
| [Ignav Flights](../data/candidates/ignav.yaml) | travel/flights | [flights-api (api)](https://ignav.com/docs) | unknown | self_serve | unknown | Requires: email_verification; 1000 requests / one_time (free_allowance; One-time account allowance, not monthly.); 2 USD / 1000 successful requests (usage; Successful HTTP 200 responses; search and booking-link retrieval are separate calls.); Human: Verify signup email | not recorded |
| [Ignav Flights](../data/candidates/ignav.yaml) | travel/flights | [official-mcp (mcp)](https://ignav.com/docs/mcp) | unknown | unknown | unknown | Requirements incomplete; Uses Ignav credentials. The API route records published account pricing; MCP tool billing and coverage need confirmation. | not recorded |
| [KAYAK Affiliate API](../data/candidates/kayak-affiliate.yaml) | travel/flights | [affiliate-api (api)](https://developers.kayak.com/) | unknown | application | unknown | Requires: company, website, approval; Human: Submit business application for review | not recorded |
| [Kiwi.com](../data/candidates/kiwi.yaml) | travel/flights | [search-mcp (mcp)](https://mcp.kiwi.com) | unknown | self_serve | unknown | Requirements incomplete | [flights-search-001: completed (2026-09-07)](../data/experiments/evaluations/codex-20260907T083627.884537Z-kiwi.json); [flights-search-001: invalid_run (2026-09-07)](../data/experiments/evaluations/codex-20260907T091621.435575Z-kiwi.json); [flights-search-001: completed (2026-09-07)](../data/experiments/evaluations/codex-20260907T092329.724439Z-kiwi.json) |
| [Kiwi.com](../data/candidates/kiwi.yaml) | travel/flights | [tequila-api (api)](https://media.kiwi.com/articles-and-interviews/better-for-business-kiwi-com-takes-a-new-approach-to-partnerships/) | unknown | invite_only | unknown | Requires: invitation; Keep invitation-only Tequila separate from the search MCP. Current endpoints and task coverage need further research. | not recorded |
| [LetsFG Personal Flight Search](../data/candidates/letsfg.yaml) | travel/flights | [personal-mcp (mcp)](https://letsfg.co/for-agents) | unknown | unknown | documented | Requires: payment_method; 0 USD / search (usage; Personal flight-search claim only; excludes booking, payment authorization and the separate Developer API.); Human: Complete browser consent and connect a payment method | not recorded |
| [LetsFG Personal Flight Search](../data/candidates/letsfg.yaml) | travel/flights | [personal-cli (cli)](https://github.com/letsfg/letsfg) | unknown | unknown | unknown | Requirements incomplete; Official repository advertises this interface (Python/JS for SDK). Installation version, current auth compatibility and route-specific gates remain unverified due to documentation drift. | not recorded |
| [LetsFG Personal Flight Search](../data/candidates/letsfg.yaml) | travel/flights | [personal-sdk (sdk)](https://github.com/letsfg/letsfg) | unknown | unknown | unknown | Requirements incomplete; Official repository advertises this interface (Python/JS for SDK). Installation version, current auth compatibility and route-specific gates remain unverified due to documentation drift. | not recorded |
| [Lufthansa Partner Fare API](../data/candidates/lufthansa-partner.yaml) | travel/flights | [open-api-registration (api)](https://developer.lufthansa.com/page) | unknown | paused | unknown | Requirements incomplete; Public schedule and status APIs are not evidence of consumer fare-search capability. | not recorded |
| [Lufthansa Partner Fare API](../data/candidates/lufthansa-partner.yaml) | travel/flights | [partner-offers-api (api)](https://developer.lufthansa.com/docs/read/api_partner/offers) | unknown | unknown | unknown | Requirements incomplete; Public schedule/status APIs do not establish fare-search access. A readable registration form does not override the pause notice. | not recorded |
| [去哪儿机票合作](../data/candidates/qunar-flights.yaml) | travel/flights | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Sabre Air APIs](../data/candidates/sabre-air.yaml) | travel/flights | [air-workflow-api (api)](https://github.com/SabreDevStudio/SabreAPIsWorkflows/blob/master/SabreAPIsTestSuites/README.md) | unknown | application | unknown | Requirements incomplete; Human: Contact sales to obtain EPR, IPCC and password; This older workflow is evidence for its own credential path only. | not recorded |
| [Sabre Air APIs](../data/candidates/sabre-air.yaml) | travel/flights | [agentic-mcp-lead (mcp)](https://developer.sabre.com/) | unknown | unknown | unknown | Requirements incomplete; Current developer homepage advertises Agentic API/MCP. Exact product, tools and onboarding need research; do not copy legacy workflow gates onto it. | not recorded |
| [Scrapingdog Google Flights API](../data/candidates/scrapingdog-flights.yaml) | travel/flights | [flights-api (api)](https://www.scrapingdog.com/documentation/google-flights-api/) | unknown | self_serve | unknown | Requirements incomplete; 5 credits / flight request (usage; Do not equate platform free credits to the same number of flight searches.) | not recorded |
| [SearchApi Google Flights](../data/candidates/searchapi.yaml) | travel/flights | [google-flights-api (api)](https://www.searchapi.io/docs/google-flights-api) | unknown | self_serve | unknown | Requirements incomplete; 100 requests / trial (free_allowance; Product-page trial; whether shared across engines requires account verification.) | not recorded |
| [SearchApi Google Flights](../data/candidates/searchapi.yaml) | travel/flights | [hosted-mcp (mcp)](https://www.searchapi.io/mcp) | unknown | unknown | unknown | Requirements incomplete; Human: Authorize in browser when choosing OAuth; Supports browser OAuth or a separate MCP token. Which tools expose the flight task remains untested. | not recorded |
| [SerpApi](../data/providers/serpapi.yaml) | travel/flights, web-search-data/web-search | [google-flights-api (api)](https://serpapi.com/google-flights-api) | unknown | self_serve | unknown | Requirements incomplete; 250 searches / month (free_allowance; Platform search allowance; flight-endpoint entitlement and shared usage untested.); A third-party Google Flights data service. Not a Google-operated API. | not recorded |
| [SerpApi](../data/providers/serpapi.yaml) | travel/flights, web-search-data/web-search | [official-mcp (mcp)](https://github.com/serpapi/serpapi-mcp) | unknown | unknown | unknown | Requirements incomplete; Official to SerpApi. Flight tool coverage and access gates are unconfirmed; do not inherit API-route results. | not recorded |
| [SerpApi](../data/providers/serpapi.yaml) | travel/flights, web-search-data/web-search | [web-search-api (api)](https://serpapi.com/search-api) | unknown | self_serve | unknown | Requirements incomplete; Separate from Google Flights API. Existing flight evaluations do not establish web search performance. | not recorded |
| [Skootle Google Flights Scraper](../data/candidates/skootle-google-flights.yaml) | travel/flights | [apify-actor-api (api)](https://apify.com/skootle/google-flights-scraper) | unknown | unknown | unknown | Requires: platform_account; Publisher is Skootle; Apify is the host. Not operated by Google or Apify. Record-based fees, actor version and actual trial eligibility need verification. | not recorded |
| [Skyscanner Travel APIs](../data/candidates/skyscanner.yaml) | travel/flights | [partner-api (api)](https://developers.skyscanner.net/docs/getting-started/authentication) | unknown | application | unknown | Requires: approval; Partnership review; personal-use acceptance, fees and waiting time are unknown. | not recorded |
| [Skyscanner Travel APIs](../data/candidates/skyscanner.yaml) | travel/flights | [partner-mcp (mcp)](https://developers.skyscanner.net/docs/mcp-server) | unknown | application | unknown | Requires: approval; Human: Contact account manager or partnership team; Case-by-case access; an official MCP does not establish personal self-service access. | not recorded |
| [同程机票合作](../data/candidates/tongcheng-flights.yaml) | travel/flights | unknown | unknown | unknown | unknown | No route established; see source record | not recorded |
| [Travelport TripServices](../data/candidates/travelport-tripservices.yaml) | travel/flights | [tripservices-api (api)](https://developer.travelport.com/docs/getting-started) | unknown | application | unknown | Requires: approval; Human: Request trial access; contact sales for customer onboarding; Production/pre-production credentials and PCC/point-of-sale context are provisioned. Personal access and trial data realism remain unknown. | not recorded |
| [Trip.com Flight Distribution](../data/candidates/trip-com-flights.yaml) | travel/flights | [supplier-fare-maintenance (api)](https://tradeplatformmanual.trip.com/international-shared-platform-api-guide-20260701/international-shared-platform-api-guide.html) | unknown | unknown | unknown | Requirements incomplete; Supplier fare and rule maintenance with existing distribution permissions/support. Not evidence of consumer itinerary search; no flights.search capability is assigned. | not recorded |
