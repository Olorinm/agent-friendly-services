# Real-task definitions

For the current workflow use [task design](./AGENTS.md), [execution and review](../AGENTS.md), and the [flight task table](./travel-flights.md). The milestone format below is retained for historical experiments; it is not a prerequisite for new tasks.

Current Markdown task tables separate the user request, raw inputs, resources
and independent completion checks. Their navigation and setup/business phase
are maintained in [task-classifications.yaml](../task-classifications.yaml).
Count distinct business task IDs within each terminal classification; setup
tasks, task versions and historical milestone ladders do not add business tasks.
For current coverage use the latest defined version of each ID. For example,
`mailboxes-create-001/v1` retains its historical business mapping, but its latest
`v2` is a setup task and does not fill a current business-task slot.

Public need sources and design limitations may be kept beside the task table,
or in `data/research/<category>/<subcategory>.yaml` under the
[research guidance](../../../docs/contributing.md#research-user-needs). When
reusing a research file, cite its revision and scenario IDs. A research scenario
is not a runnable test. A task design is not a tested result: confirm the stated
account, input, authorization and verification prerequisites before dispatch,
then freeze the same materials and settings for each applicable service.
Sources establish that a need exists; they do not establish its market frequency.

## Dispatch prerequisites

New tables are task designs, not verified service results or permission to run.
Before dispatch the controller must confirm candidate eligibility, usable input
materials, account provenance, resource scope and an independent verification
method. Complete setup separately; a pre-existing account is not agent-created
access. Synthetic materials are identified as such. Actual filenames, hashes,
dates and resource identities are frozen before a comparison starts, with the
same inputs for each applicable service in that task and round.

The terminal classification defines the candidate pool. Retain every candidate
in its service/task preparation matrix, including documented feature limitations,
unknown support and account or environment blockers. Qualification determines
how to prepare and interpret a pair; it must not silently remove difficult
candidates. A documented limitation is not an observed failed trial, and an
unrun pair has no empirical completion rate. Incorrect category assignments
should be corrected with evidence rather than stretched to fit a task.

Prefer synthetic raw inputs for records, messages, documents and media when
they satisfy the task's stated conditions. Disclose their origin and freeze the
same bytes for each comparison. Actual service responses, inventory, quotes,
delivery and persisted state must be obtained from the real service. Changing
human recordings to synthetic speech changes the task conditions; see the
[synthetic speech-recognition v2 designs](ai-speech-recognition-synthetic-v2.md),
which retain the original v1 definitions and independent listening prerequisites.

For services that need registration, the controller uses a dedicated authorized
mailbox and reuses a legitimate test account for that service. Keep registration
mail access and account management keys with the controller; provide workers
only the service credentials and test resources needed for their assigned task.
Reset or recreate those resources between repetitions, respecting service limits.
An existing credential file is not proof that an account or resource is still
usable; confirm expiry, authentication and the authorized resource before dispatch.
Record this preparation as a provided-account condition, separately from access
trials, with its actual cost evidence or unknowns.

The pipeline uses the trial configuration's `environment` text for the actual
`ENVIRONMENT.md`. Include the table's resource and authorization conditions in
that configuration and inspect the frozen execution packet; listing them in a
table alone does not make them available to the executor. Attachments must use
the actual `materials/` paths declared in the input.

Only the request, raw input and authorized environment reach the executor.
Recording scripts, reference transcripts, expected answers, other services'
results and service-call solution programs stay outside its packet. Keep every
completion requirement visible in the request or input. A task-specific missing
asset, account or verification channel remains a preparation blocker.

Independent review checks real service responses and artifacts against the
visible requirements, following the shared evidence, compliance and
cross-check rules in [task design](AGENTS.md). Media content needs content
inspection, not just a valid file signature. Record service operations and user
delivery separately; classify environment failures separately from service
limitations. Use fresh sessions and reset business resources between repetitions.

Use only explicitly authorized accounts, sandboxes, recipients and service
credits; do not automatically buy subscriptions, bind payment methods, send to
real contacts or place travel/store orders. Model and service charges must retain
their evidence and unknowns. Runtime protection limits are separate from user
requirements. See [resource guards and repeats](resource-guards-and-repeats.md)
for comparison preparation, and [execution and review](../AGENTS.md) for the
pipeline handoff. Do not send these repository instructions to the executor.

## Current business task tables

This is navigation to task definitions, including designs awaiting preparation;
it is not a list of verified services or completed experiments. Current phase
and classification remain defined in the mapping file.

| 分类 | 任务表 |
| --- | --- |
| AI 服务 | [模型接入：让个人应用完成三种工作](./ai-model-access-business.md) · [语音合成：可听的文章、配音和公共导览](./ai-speech-synthesis-business.md) · [语音识别：系统合成音频 v2](./ai-speech-recognition-synthetic-v2.md) · [语音识别：原有人声设计 v1](./ai-speech-recognition-business.md) · [图像生成：活动海报、商品插图与教学图](./ai-image-generation-business.md) · [视频生成：商品镜头、教学动作与背景片段](./ai-video-generation-business.md) |
| Agent 基础设施与自动化 | [记忆服务：跨会话偏好、更正与遗忘](./agent-memory-business.md) · [工具集成：日历、表格和邮箱的真实工作](./agent-tool-integrations-business.md) · [流程自动化：表单去重、逾期待办与日报](./agent-workflow-automation-business.md) |
| 开发工具 | [依赖漏洞公告：核对已有告警与修复版本](./dependency-advisories.md) · [开发工具：业务任务补齐（2026-10-12）](./coverage-comm-developer.md) · [静态二维码：任务表](./qr-codes.md) |
| 云计算与托管 | [代码沙箱：支出分析、图片整理与表格清洗](./cloud-code-sandboxes-business.md) · [云端浏览器：页面查询、文件导出与表单草稿](./cloud-browser-environments-business.md) · [应用托管：活动页面、小工具与更新发布](./cloud-app-hosting-business.md) |
| 数据库 | [数据库 / 托管关系型数据库：待办数据任务 v2](./databases-v2.md) · [数据库：个人应用的逻辑备份与恢复（独立准备源库）](./database-restore-v2.md) · [数据库：不留下半批数据的书目导入](./database-atomic-import.md) · [向量数据库：笔记检索、范围筛选与资料更新](./database-vector-business.md) · [文档数据库：嵌套商品、订单汇总与单字段更正](./database-document-business.md) · [云计算与托管：应用配置读取](./cloud-hosting.md) · [键值数据库：多设备退出与缓存刷新](./database-key-value-business.md) |
| 搜索与网页抓取 | [网页搜索：Python 升级查询 v2](./web-search-v2.md) · [网页搜索：参观准备与公共服务办理信息](./coverage-data-web-search.md) · [网页内容提取：任务表](./web-extraction.md) · [网页内容提取：英国地区假日日历](./web-extraction-uk.md) · [PDF 表格提取：任务表](./web-extraction-pdf.md) |
| 地图与地理 | [地理编码：给旅行地图标记场馆](./geocoding.md) · [地理编码：同名地点与旅行照片归档](./coverage-data-geocoding.md) · [驾车路线规划：任务表](./route-planning.md) · [路线规划：固定停靠顺序与避收费对照](./coverage-data-route-planning.md) |
| 天气与日历 | [既有天气与机票任务：未来日期冻结版本](./coverage-data-rolling-revisions.md) · [天气数据：选择活动时段与历史行李准备](./coverage-data-weather.md) · [公共节假日数据：按地区整理个人日程](./public-holidays.md) · [公共假日：跨地区安排与连休选择](./coverage-data-public-holidays.md) |
| 金融数据 | [金融数据：需求与任务表](./financial-data.md) · [汇率数据：费用偏差与旅行预算波动](./coverage-data-fx.md) · [资产行情：合成持仓估值与拆股解释](./coverage-data-prices.md) · [公司财务数据：季度现金流与资产负债阅读](./coverage-data-statements.md) · [宏观数据：可复用的跨国通胀对照表](./financial-macro.md) · [宏观数据：名义与实际工资、数据修订](./coverage-data-macro.md) · [综合金融数据平台：跨数据集个人资料整理](./coverage-data-platforms.md) |
| 学术与知识 | [学术文献检索：从阅读笔记找回引用](./scholarly-search.md) · [学术检索：主题入门阅读与引用清理](./coverage-data-scholarly.md) |
| 支付与计费 | [支付与账单 / 收款：任务表](./payment-acceptance.md) |
| 通信 | [邮箱：需求与任务表](./mailboxes.md) · [通信：业务任务补齐（2026-10-12）](./coverage-comm-communication.md) |
| 办公与协作 | [协作办公 / 在线任务表：任务 v4](./collaborative-tables-v4.md) · [协作办公 / 在线任务表：任务表](./collaborative-tables.md) · [协作表格：会自动更新的共同支出账本](./collaborative-tables-shared-expenses.md) · [开发工具：仓库问题整理](./developer-tools.md) · [办公协作：业务任务补齐（2026-10-12）](./coverage-comm-productivity.md) |
| 电商 | [电商：业务任务定义（2026-10-12）](./coverage-comm-commerce.md) |
| 旅行 | [既有天气与机票任务：未来日期冻结版本](./coverage-data-rolling-revisions.md) · [机票：行李总价与周末目的地选择](./coverage-data-flights.md) · [酒店：基础房价、可取消条件与无障碍房型](./coverage-data-hotels.md) |

## Historical milestone ladders

The historical `code-execution.yaml` and `observability-security.yaml` filenames remain stable after their services move into cloud hosting and developer tools. The legacy runner retains their original task selection; new comparisons use explicit task tables.

One file per original category, holding that category's **milestone ladder**. Milestones
pin the real-task scenarios so runs are comparable within a category and the
verdict never depends on the agent's mid-run judgment about what "the task"
means. See `docs/agent-verification.md` for the method.

Top-level fields:

- `provisioning` — the minimum a human must supply before any real run. This
  list is itself a published friction fact.
- `milestones` — the ladder, in climbing order (see below).
- `reset_commands` — per-provider commands the runner executes **before every
  rep** to wipe `afs-*` artifacts, so no rep can imitate visible prior work.
- `cleanup` — how created state is removed. Test modes / free tiers are
  mandatory where they exist.
- `provider_overrides` — provider pins that apply to every milestone (e.g.
  "data plane only").

Each milestone:

- `id` — `core` (the category's basic realistic task; all badges and the route
  comparison pin to it), `lifecycle` (set up → use → evolve → tear down →
  verifiable receipt), `billing` (machine-readable usage/billing reality).
- `scenario` — the realistic user request given to the agent, with `{{NONCE}}`
  replaced per run by the runner (a unique string, so independent verification
  can match exactly).
- `verification` — how the runner independently confirms success. `method:
  state` = fetch the created state itself; `re-execute` = run the runner's own
  pinned query. `expect: nonce` = output must contain the run's nonce;
  `expect: success` = the command must succeed with a non-empty numeric
  response.
- `verify_commands` — per-provider command templates the runner executes for
  that confirmation (placeholders: `{{NONCE}}`, `{{CURLRC}}`,
  `{{provision.*}}` from the local `<id>.provision.yaml`). Public on purpose:
  they define what counts as a pass. Added per provider as it gets its first
  provisioned run — a milestone without a `verify_commands` entry for a
  provider refuses to run. Secret-bearing values (e.g. a Redis URI with a
  password) live only in `verify_commands`/`reset_commands` placeholders like
  `{{provision.uri}}` — never in `scenario`, which goes into the agent's
  prompt.
- `provider_overrides` — pinned targets where the category scenario is
  ambiguous for a specific provider (key-value stores, class-naming rules,
  index-level lifecycles …).

Tasks are route-agnostic: the same scenario, nonce and verification run over
every access route (HTTP baseline / official CLI / official MCP — see
`docs/agent-verification.md`). Route provisioning (curl config file, CLI env
vars, MCP config) is harness environment, not task data.

Ladder semantics: `--ladder` climbs milestones in order and stops at the first
one without a majority pass across reps; `--milestone=<id>` runs one rung.

Task definitions are data: challenge them by PR like any other fact here.
