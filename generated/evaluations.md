<!-- GENERATED — npm run generate; source: data/experiments/evaluations/ -->
# 任务实测结果

每行只说明该服务入口在该任务和运行配置下的观察。Token用量为输入总数（含缓存）加输出，缓存不重复相加。模型费用根据保存的LiteLLM价格表自动估算，估价日期不冒充运行日期；服务费用单独记录，unknown不等于0。点击结果可查看冻结的任务、独立复核与选取的证据；原始日志仍在本地。免费账号的注册准备若发生在计时前，说明保存在 environment.preparation_note；表中 token 与耗时不包含这部分准备。历史记录保留，不把不同任务、配置或日期直接平均成服务排名。

按任务所属大类 / 子类分组，再展示同一任务版本和冻结内容的运行。分类标题来自当前任务表，仅用于导航；历史任务、结果和用量不改写。同组仍需核对接入前提与模型等配置，不能仅按耗时排序判断优劣。

输入方式 legacy 是带明确测试要求的初期试跑，Agent 的开销包含证据保存与整理；natural 只提供用户任务、资料及运行环境，使用自动会话日志与外部远端复核。不同方式分别记录；单次测量都不代表典型开销，跨版本差异也可能来自业务要求、执行路径和缓存变化。

<a id="communication-mailboxes"></a>

## 通信 / 邮箱（communication/mailboxes）

### mailboxes-code-001 / v1

找出收件箱里 AFS Demo 最新一封登录邮件的验证码，告诉我对应邮件的主题和时间。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| guerrilla-mail / mail-api | mailboxes-code-001 (v1) | provided: COOKIE_HEADER, MAILBOX_ADDRESS, SESSION_TOKEN | natural | [not_completed](../data/experiments/evaluations/codex-20260909T103849.955516Z-guerrilla-mail.json) | 2026-09-09T10:38:49.977481+00:00 | codex-cli 0.153.4 / gpt-6-astra / medium | 84645 / 66432 / 678 | 43.589s | 0 | 0 |
| mail-tm / mail-api | mailboxes-code-001 (v1) | provided: MAILBOX_ADDRESS, MAILBOX_TOKEN | natural | [completed](../data/experiments/evaluations/codex-20260909T103356.699996Z-mail-tm.json) | 2026-09-09T10:33:56.712589+00:00 | codex-cli 0.153.4 / gpt-6-astra / medium | 75009 / 65920 / 486 | 44.287s | 0 | 0 |

### mailboxes-create-001 / v1

为这次自动化测试准备一个临时收件邮箱，给我地址，并保存后续读取收件箱需要的访问信息。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| guerrilla-mail / mail-api | mailboxes-create-001 (v1) | none | natural | [completed](../data/experiments/evaluations/codex-20260909T102405.681663Z-guerrilla-mail.json) | 2026-09-09T10:24:05.693712+00:00 | codex-cli 0.153.4 / gpt-6-astra / medium | 112605 / 91392 / 1107 | 55.401s | 0 | 0 |
| mail-tm / mail-api | mailboxes-create-001 (v1) | none | natural | [completed](../data/experiments/evaluations/codex-20260909T102400.674330Z-mail-tm.json) | 2026-09-09T10:24:00.688296+00:00 | codex-cli 0.153.4 / gpt-6-astra / medium | 60460 / 46208 / 1064 | 56.859s | 0 | 0 |

<a id="payments-billing-accept-payments"></a>

## 支付与账单 / 收款（payments-billing/accept-payments）

### payment-acceptance-001 / v1

我要卖一份电子书《城市散步指南》，标价12美元，一次性付款。先在测试环境做好收款页面，把顾客能打开的链接给我。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| paddle / sandbox-api | payment-acceptance-001 (v1) | provided: PADDLE_SANDBOX_API_KEY | natural | [not_completed](../data/experiments/evaluations/codex-20260909T032011.000426Z-paddle.json) | 2026-09-09T03:20:11.012572+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 450919 / 391040 / 4297 | 178.002s | 0 | 0 |
| paas-build / rest-api | payment-acceptance-001 (v1) | provided: PAAS_SANDBOX_ACCESS_TOKEN, PAAS_SANDBOX_VENDOR_ID | natural | [invalid_run](../data/experiments/evaluations/codex-20260908T113239.160717Z-paas-build.json) | 2026-09-08T11:32:39.178384+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 790729 / 699520 / 7753 | 408.184s | 0 | 0 |

<a id="productivity-storage-collaborative-tables"></a>

## 协作办公与存储 / 在线任务表（productivity-storage/collaborative-tables）

### collaborative-tables-001 / v2

帮我把这份读书会会议记录里的待办整理成在线任务表，给我链接，再告诉我还有哪些没完成、各自什么时候到期。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| notion / rest-api | collaborative-tables-001 (v2) | provided: NOTION_API_TOKEN, NOTION_PARENT_PAGE_ID | natural | [completed](../data/experiments/evaluations/codex-20260908T035504.906378Z-notion.json) | 2026-09-08T03:55:05.045850+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 211718 / 173440 / 3779 | 183.384s | 0 | 0 |
| grist / rest-api | collaborative-tables-001 (v2) | provided: GRIST_API_KEY, GRIST_WORKSPACE_ID | natural | [completed](../data/experiments/evaluations/codex-20260908T035504.472694Z-grist.json) | 2026-09-08T03:55:04.657181+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 536770 / 489088 / 3983 | 219.634s | 0 | 0 |

### collaborative-tables-001 / v1

把一次读书会筹备会的行动项整理成在线任务表，更新进展，然后告诉我还剩什么没完成

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| notion / rest-api | collaborative-tables-001 (v1) | provided: NOTION_API_TOKEN, NOTION_PARENT_PAGE_ID | legacy | [completed](../data/experiments/evaluations/codex-20260908T032850.330773Z-notion.json) | 2026-09-08T03:28:50.359616+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 471247 / 425344 / 12291 | 463.678s | 0 | 0 |
| grist / rest-api | collaborative-tables-001 (v1) | provided: GRIST_API_KEY, GRIST_WORKSPACE_ID | legacy | [completed](../data/experiments/evaluations/codex-20260908T032113.556233Z-grist.json) | 2026-09-08T03:21:13.580494+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 769817 / 708608 / 11455 | 478.476s | 0 | 0 |

<a id="databases-hosted-relational"></a>

## 数据库 / 托管关系型数据库（databases/hosted-relational）

### database-todos-001 / v1

为我的个人待办应用准备一个独立的远程数据库，验证新增、修改和重新连接后读取待办事项

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| turso / platform-api | database-todos-001 (v1) | provided: TURSO_API_TOKEN, TURSO_ORGANIZATION | legacy | [completed](../data/experiments/evaluations/codex-20260907T113506.422646Z-turso.json) | 2026-09-07T11:35:06.452325+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 755366 / 687616 / 12234 | 457.78s | 0 | 0 |
| neon / ephemeral-api | database-todos-001 (v1) | none | legacy | [completed](../data/experiments/evaluations/codex-20260907T112258.549053Z-neon.json) | 2026-09-07T11:22:58.558715+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 452623 / 402560 / 12790 | 456.342s | 0 | 0 |

<a id="web-search-data-web-search"></a>

## 网页搜索与数据 / 网页搜索（web-search-data/web-search）

### web-search-001 / v1

我准备把 Python 应用升级到 3.13，查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并给出官方依据

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| exa / search-api | web-search-001 (v1) | provided: EXA_API_KEY | legacy | [not_completed](../data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json) | 2026-09-07T11:29:52.610600+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | unknown | 602.017s | 0 | 0 |
| firecrawl / public-search-api | web-search-001 (v1) | none | legacy | [completed](../data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json) | 2026-09-07T11:29:51.792723+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 338090 / 295552 / 8728 | 362.944s | 0 | 0 |
| exa / public-mcp | web-search-001 (v1) | none | legacy | [completed](../data/experiments/evaluations/codex-20260907T112257.401366Z-exa.json) | 2026-09-07T11:22:57.413717+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 917915 / 847104 / 13629 | 522.486s | 0 | 0 |

<a id="travel-flights"></a>

## 旅行 / 航空机票（travel/flights）

### flights-search-001 / v1

找到9月25日米兰飞往荷兰的机票

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| kiwi / search-mcp | flights-search-001 (v1) | none | legacy | [completed](../data/experiments/evaluations/codex-20260907T092329.724439Z-kiwi.json) | 2026-09-07T09:23:29.733240+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 204087 / 163968 / 5464 | 212.222s | 0 | 0 |
| kiwi / search-mcp | flights-search-001 (v1) | none | legacy | [invalid_run](../data/experiments/evaluations/codex-20260907T091621.435575Z-kiwi.json) | 2026-09-07T09:16:21.457471+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | unknown | 1s | 0 | 0 |

### flights-search-001 / v1

找到9月25日米兰飞往荷兰的机票

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| ignav / public-playground | flights-search-001 (v1) | none | legacy | [completed](../data/experiments/evaluations/codex-20260907T083644.877057Z-ignav.json) | 2026-09-07T08:36:44.885519+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 207427 / 157696 / 5517 | 204.375s | 0 | 0 |
| kiwi / search-mcp | flights-search-001 (v1) | none | legacy | [completed](../data/experiments/evaluations/codex-20260907T083627.884537Z-kiwi.json) | 2026-09-07T08:36:27.894085+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 184152 / 129408 / 3754 | 156.912s | 0 | 0 |

## 汇总条件与费用依据

<a id="comparison-8624e51d6979"></a>

### mailboxes-code-001 v1

**mail-tm / mail-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / medium · 600s · natural · provided: MAILBOX_ADDRESS, MAILBOX_TOKEN

准备：Dedicated temporary mailbox supplied with three synthetic emails sent from a user-authorized Gmail account. Delivery and reference timestamps checked before this run. Prior provisioning and fixture preparation are excluded from this task usage; no personal inbox access or calling scripts supplied.

- [codex-20260909T103356.699996Z-mail-tm](../data/experiments/evaluations/codex-20260909T103356.699996Z-mail-tm.json)：模型费用 $0.18；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Free public receive API for the dedicated temporary mailbox; no paid feature used. Gmail fixture sending occurred in preparation and is excluded from the measured service task.; https://docs.mail.tm/; response-excerpt.json

**guerrilla-mail / mail-api** — 0 完成 / 1 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / medium · 600s · natural · provided: COOKIE_HEADER, MAILBOX_ADDRESS, SESSION_TOKEN

准备：Dedicated temporary mailbox supplied with three synthetic emails sent from a user-authorized Gmail account. Delivery and reference timestamps checked before this run. Prior provisioning and fixture preparation are excluded from this task usage; no personal inbox access or calling scripts supplied.

- [codex-20260909T103849.955516Z-guerrilla-mail](../data/experiments/evaluations/codex-20260909T103849.955516Z-guerrilla-mail.json)：模型费用 $0.28；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Public default temporary mailbox API; no payment credentials, custom domain or subscription were used. Fixture sending was preparation and is excluded from this measured task.; https://www.guerrillamail.com/GuerrillaMailAPI.html; external-check.json

<a id="comparison-1149cab0b0f0"></a>

### payment-acceptance-001 v1

**paddle / sandbox-api** — 0 完成 / 1 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · natural · provided: PADDLE_SANDBOX_API_KEY

准备：A separate sandbox account was registered and email-verified by the evaluator using synthetic test business/address details. No KYC or production activation occurred. A sandbox API key expires after seven days and grants read/write access only to products, prices, transactions, checkout domains and client-side tokens. A preflight API read confirmed an empty product catalog. No product, price, transaction, checkout page or solution code was prepared. A dedicated empty local Chromium browser is supplied over CDP to avoid macOS sandbox browser-launch failures; the executing Codex still uses workspace-write sandboxing. Registration, browser startup and evaluator work are outside measured execution metrics. This configuration differs from earlier browser-less trials.

- [codex-20260909T032011.000426Z-paddle](../data/experiments/evaluations/codex-20260909T032011.000426Z-paddle.json)：模型费用 $1.20；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Sandbox-only API requests, with no completed payment, no paid subscription or live account activation. Official docs specify no real money in sandbox and pricing has no monthly fees. The $12 product price is not a service cost.; https://developer.paddle.com/sdks/sandbox/; https://www.paddle.com/pricing

<a id="comparison-bc10c53a81ca"></a>

### payment-acceptance-001 v1

**paas-build / rest-api** — 0 完成 / 0 未完成 / 1 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · natural · provided: PAAS_SANDBOX_ACCESS_TOKEN, PAAS_SANDBOX_VENDOR_ID

准备：A new sandbox-only merchant was provisioned by the evaluator through the official API with notifications disabled. Sandbox token identity was checked before execution. No product, price, checkout, production merchant or solution code was prepared. Signup identity stays private; preparation time and evaluator tokens are outside execution metrics.

- [codex-20260908T113239.160717Z-paas-build](../data/experiments/evaluations/codex-20260908T113239.160717Z-paas-build.json)：模型费用 $2.00；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Official instructions state that the sandbox is free to play with. Only sandbox checkout creation and reads occurred; no payment was submitted. The $12 product price is not a service charge.; https://paas.build/SKILL.md

<a id="comparison-6203194a76cd"></a>

### collaborative-tables-001 v2

**grist / rest-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · natural · provided: GRIST_API_KEY, GRIST_WORKSPACE_ID

准备：Existing dedicated free test account; API credential and a newly created empty workspace prepared before timing. No business schema, records or adapter supplied. Setup and external verification excluded from measured tokens/time. No payment enabled.

- [codex-20260908T035504.472694Z-grist](../data/experiments/evaluations/codex-20260908T035504.472694Z-grist.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

**notion / rest-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · natural · provided: NOTION_API_TOKEN, NOTION_PARENT_PAGE_ID

准备：Existing dedicated free test account; API credential and a newly created empty private parent page prepared before timing. No business schema, records or adapter supplied. Setup and external verification excluded from measured tokens/time. No payment enabled.

- [codex-20260908T035504.906378Z-notion](../data/experiments/evaluations/codex-20260908T035504.906378Z-notion.json)：模型费用 $0.75；Actual recorded usage × saved LiteLLM standard API rates; estimate at the snapshot date, not an account charge. Excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

<a id="comparison-1420586eae17"></a>

### database-todos-001 v1

**turso / platform-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · provided: TURSO_API_TOKEN, TURSO_ORGANIZATION

准备：Outer Agent registered a new dedicated Free organization using Google sign-in, selected a username and created an organization API token; no card/payment, no existing database. Signup and token creation outside measured time/tokens. Executor receives only this organization and token, and must provision its own test database.

- [codex-20260907T113506.422646Z-turso](../data/experiments/evaluations/codex-20260907T113506.422646Z-turso.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

<a id="comparison-9dbe771526ac"></a>

### web-search-001 v1

**exa / search-api** — 0 完成 / 1 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · provided: EXA_API_KEY

准备：Free account prepared by the outer Agent using browser Google sign-in and onboarding; no card or payment. Signup work is outside measured session tokens/time; only EXA_API_KEY provided, no adapter or research context.

- [codex-20260907T112952.581354Z-exa](../data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json)：模型费用 —；Token usage was not reported. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

<a id="comparison-b5f21fc39ab4"></a>

### web-search-001 v1

**firecrawl / public-search-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：No service account or resource prepared before the measured session.

- [codex-20260907T112951.715536Z-firecrawl](../data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

<a id="comparison-fdecec09a4b6"></a>

### database-todos-001 v1

**neon / ephemeral-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：No service credentials provided.

- [codex-20260907T112258.549053Z-neon](../data/experiments/evaluations/codex-20260907T112258.549053Z-neon.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

<a id="comparison-87ab787b88b3"></a>

### web-search-001 v1

**exa / public-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：No service credentials provided.

- [codex-20260907T112257.401366Z-exa](../data/experiments/evaluations/codex-20260907T112257.401366Z-exa.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

<a id="comparison-c77feef961a0"></a>

### flights-search-001 v1

**kiwi / search-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：unknown

- [codex-20260907T092329.724439Z-kiwi](../data/experiments/evaluations/codex-20260907T092329.724439Z-kiwi.json)：模型费用 $0.84；Actual recorded usage × saved LiteLLM standard API rates; estimate at the snapshot date, not an account charge. Excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

<a id="comparison-45effe165cf4"></a>

### flights-search-001 v1

**ignav / public-playground** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：unknown

- [codex-20260907T083644.877057Z-ignav](../data/experiments/evaluations/codex-20260907T083644.877057Z-ignav.json)：模型费用 $0.93；Actual recorded usage × saved LiteLLM standard API rates; estimate at the snapshot date, not an account charge. Excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。
