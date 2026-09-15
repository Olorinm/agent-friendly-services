<!-- GENERATED — npm run generate; source: data/experiments/evaluations/ -->
# 任务实测结果

每行只说明该服务入口在该任务和运行配置下的观察。Token用量为输入总数（含缓存）加输出，缓存不重复相加。模型费用根据保存的LiteLLM价格表自动估算，估价日期不冒充运行日期；服务费用单独记录，unknown不等于0。点击结果可查看冻结的任务、独立复核与选取的证据；原始日志仍在本地。免费账号的注册准备若发生在计时前，说明保存在 environment.preparation_note；表中 token 与耗时不包含这部分准备。历史记录保留，不把不同任务、配置或日期直接平均成服务排名。

按当前分类和接入／业务阶段分组，再展示同一任务版本和冻结内容的运行。展示归属来自 task-classifications.yaml；历史任务、结果和用量不改写。同组仍需核对接入前提与模型等配置，不能仅按耗时排序判断优劣。

输入方式 legacy 是带明确测试要求的初期试跑，Agent 的开销包含证据保存与整理；natural 只提供用户任务、资料及运行环境，使用自动会话日志与外部远端复核。不同方式分别记录；单次测量都不代表典型开销，跨版本差异也可能来自业务要求、执行路径和缓存变化。

<a id="web-search-data-financial-data-disclosures"></a>

## 搜索与数据获取 / 金融数据 / 交易披露（web-search-data/financial-data/disclosures）

### financial-disclosures-004 / v1

帮我核对这条待查说法：“Ed Case 本人在 2026 年 8 月 18 日主动买入了恰好 8,000 美元的苹果股票。”请逐项判断交易归属、日期、金额和交易性质，写出有依据的更正，并附原始申报出处。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| capitol-exposed / data-api-keyless | financial-disclosures-004 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-004-900s-c10-r1.json) | 2026-09-15T13:30:44.951470+00:00 | 1.18.29 / glm-5.3-flash / high | 225048 / 204800 / 5872 | 193.388154s | 0 | unknown |
| capitol-exposed / data-api-keyless | financial-disclosures-004 (v1) | none | natural | [invalid_run](../data/experiments/evaluations/capitol-disclosures-004-r1.json) | 2026-09-15T12:38:23.929828+00:00 | 1.18.29 / glm-5.3-flash / high | 250971 / 232064 / 5116 | — | 0 | 0 |
| bargo-congress / congress-api-keyless | financial-disclosures-004 (v1) | none | natural | [not_completed](../data/experiments/evaluations/bargo-disclosures-004-r1.json) | 2026-09-15T12:38:21.712373+00:00 | 1.18.29 / glm-5.3-flash / high | unknown | 590.066135s | 0 | unknown |

### financial-disclosures-003 / v1

比较 Richard W. Allen 和 Ed Case 在 2026 年 8 月提交的股票披露：从交易发生到正式提交分别隔了多久？列出每笔的日期和天数，再按申报人汇总笔数、最短和最长间隔，并附原始申报出处。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| capitol-exposed / data-api-keyless | financial-disclosures-003 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-003-900s-c10-r1.json) | 2026-09-15T13:28:27.702197+00:00 | 1.18.29 / glm-5.3-flash / high | 202230 / 185088 / 4276 | 128.978342s | 0 | 0 |
| capitol-exposed / data-api-keyless | financial-disclosures-003 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-003-r1.json) | 2026-09-15T12:26:19.469293+00:00 | 1.18.29 / glm-5.3-flash / high | 260342 / 242048 / 5776 | 207.284676s | 0 | 0 |
| bargo-congress / congress-api-keyless | financial-disclosures-003 (v1) | none | natural | [completed](../data/experiments/evaluations/bargo-disclosures-003-r1.json) | 2026-09-15T12:26:17.426614+00:00 | 1.18.29 / glm-5.3-flash / high | 564454 / 530304 / 13956 | 400.656225s | 0 | 0 |

### financial-disclosures-002 / v1

我的关注名单里有 Richard W. Allen、Donald Sternoff Beyer Jr、Rob Bresnahan 和 Ed Case。查一下他们 2026 年 8 月提交的披露中有哪些苹果股票买卖，列出明细；没有匹配记录的人也请说明，并附原始申报出处。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| capitol-exposed / data-api-keyless | financial-disclosures-002 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-002-900s-c10-r1.json) | 2026-09-15T13:21:48.603813+00:00 | 1.18.29 / glm-5.3-flash / high | 302171 / 273152 / 7480 | 393.147793s | 0 | 0 |
| capitol-exposed / data-api-keyless | financial-disclosures-002 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-002-r1.json) | 2026-09-15T12:09:04.533341+00:00 | 1.18.29 / glm-5.3-flash / high | 1103414 / 1052672 / 13130 | 516.740228s | 0 | 0 |
| bargo-congress / congress-api-keyless | financial-disclosures-002 (v1) | none | natural | [not_completed](../data/experiments/evaluations/bargo-disclosures-002-r1.json) | 2026-09-15T12:09:02.396160+00:00 | 1.18.29 / glm-5.3-flash / high | unknown | 590.067368s | 0 | 0 |

### financial-disclosures-001 / v1

帮我整理 Richard W. Allen 在 2026 年 8 月向美国众议院提交的股票买卖披露，列出股票、买卖方向、交易日期、提交日期和金额区间，并附原始申报出处。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| capitol-exposed / data-api-keyless | financial-disclosures-001 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-001-900s-c10-r1.json) | 2026-09-15T13:17:49.887185+00:00 | 1.18.29 / glm-5.3-flash / high | 158452 / 134272 / 4661 | 233.011992s | 0 | 0 |
| capitol-exposed / data-api-keyless | financial-disclosures-001 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-001-r1.json) | 2026-09-15T11:52:43.643345+00:00 | 1.18.29 / glm-5.3-flash / high | 284404 / 216384 / 6563 | 262.354235s | 0 | 0 |
| bargo-congress / congress-api-keyless | financial-disclosures-001 (v1) | none | natural | [not_completed](../data/experiments/evaluations/bargo-disclosures-001-r1.json) | 2026-09-15T11:52:41.065341+00:00 | 1.18.29 / glm-5.3-flash / high | unknown | 590.067227s | 0 | 0 |
| capitol-exposed / data-api-keyless | financial-disclosures-001 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-business.json) | 2026-09-15T09:20:49.994872+00:00 | 1.18.29 / glm-5.3-flash / high | 316639 / 248576 / 5213 | 220.999401s | 0 | unknown |
| bargo-congress / congress-api-keyless | financial-disclosures-001 (v1) | none | natural | [completed](../data/experiments/evaluations/bargo-business.json) | 2026-09-15T09:15:16.890334+00:00 | 1.18.29 / glm-5.3-flash / high | 738160 / 702208 / 13547 | 525.761527s | 0 | 0 |

<a id="web-search-data-financial-data"></a>

## 搜索与数据获取 / 金融数据（web-search-data/financial-data） · 接入测试

### financial-access-001 / v1

帮我把这个金融数据服务接好，确认能用指定方式查询数据，并保存后续调用需要的配置；如果接不通，说明卡在哪里。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| capitol-exposed / data-api-keyless | financial-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-access.json) | 2026-09-15T09:14:32.838922+00:00 | 1.18.29 / glm-5.3-flash / high | 189737 / 172864 / 2746 | 138.671707s | 0 | 0 |
| bargo-congress / congress-api-keyless | financial-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/bargo-access.json) | 2026-09-15T09:07:26.717325+00:00 | 1.18.29 / glm-5.3-flash / high | 92193 / 73920 / 3609 | 157.266045s | 0 | 0 |
| tracefour / data-api-keyless | financial-access-001 (v1) | none | natural | [not_completed](../data/experiments/evaluations/tracefour-access.json) | 2026-09-15T09:07:26.569219+00:00 | 1.18.29 / glm-5.3-flash / high | 103555 / 86272 / 3755 | 153.41522s | 0 | 0 |
| frankfurter / data-api | financial-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/frankfurter-access.json) | 2026-09-15T07:06:04.074344+00:00 | 1.18.29 / glm-5.3-flash / high | 84240 / 72512 / 2596 | 115.282949s | 0 | 0 |
| ecb-data / data-api | financial-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/ecb-access.json) | 2026-09-15T07:06:04.069023+00:00 | 1.18.29 / glm-5.3-flash / high | 216483 / 199488 / 5383 | 216.897575s | 0 | 0 |

<a id="web-search-data-financial-data-fx"></a>

## 搜索与数据获取 / 金融数据 / 汇率数据（web-search-data/financial-data/fx）

### financial-fx-001 / v1

把这三笔美元支出按发生当日的欧洲央行参考汇率折算成欧元，列出每笔金额和合计，并给出汇率出处。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| ecb-data / data-api | financial-fx-001 (v1) | none | natural | [completed](../data/experiments/evaluations/ecb-business.json) | 2026-09-15T07:15:18.031345+00:00 | 1.18.29 / glm-5.3-flash / high | 60837 / 56064 / 1994 | 81.215126s | 0 | 0 |
| frankfurter / data-api | financial-fx-001 (v1) | none | natural | [completed](../data/experiments/evaluations/frankfurter-business.json) | 2026-09-15T07:11:48.392690+00:00 | 1.18.29 / glm-5.3-flash / high | 51862 / 42880 / 2384 | 88.202808s | 0 | 0 |

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

## 支付与计费 / 收款（payments-billing/accept-payments）

### payment-acceptance-001 / v1

我要卖一份电子书《城市散步指南》，标价12美元，一次性付款。先在测试环境做好收款页面，把顾客能打开的链接给我。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| paddle / sandbox-api | payment-acceptance-001 (v1) | provided: PADDLE_SANDBOX_API_KEY | natural | [not_completed](../data/experiments/evaluations/codex-20260909T032011.000426Z-paddle.json) | 2026-09-09T03:20:11.012572+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 450919 / 391040 / 4297 | 178.002s | 0 | 0 |
| paas-build / rest-api | payment-acceptance-001 (v1) | provided: PAAS_SANDBOX_ACCESS_TOKEN, PAAS_SANDBOX_VENDOR_ID | natural | [invalid_run](../data/experiments/evaluations/codex-20260908T113239.160717Z-paas-build.json) | 2026-09-08T11:32:39.178384+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 790729 / 699520 / 7753 | 408.184s | 0 | 0 |

<a id="productivity-storage-collaborative-tables"></a>

## 办公协作 / 协作表格（productivity-storage/collaborative-tables）

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

## 搜索与数据获取 / 网页搜索（web-search-data/web-search）

### web-search-001 / v1

我准备把 Python 应用升级到 3.13，查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并给出官方依据

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| exa / search-api | web-search-001 (v1) | provided: EXA_API_KEY | legacy | [not_completed](../data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json) | 2026-09-07T11:29:52.610600+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | unknown | 602.017s | 0 | 0 |
| firecrawl / public-search-api | web-search-001 (v1) | none | legacy | [completed](../data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json) | 2026-09-07T11:29:51.792723+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 338090 / 295552 / 8728 | 362.944s | 0 | 0 |
| exa / public-mcp | web-search-001 (v1) | none | legacy | [completed](../data/experiments/evaluations/codex-20260907T112257.401366Z-exa.json) | 2026-09-07T11:22:57.413717+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 917915 / 847104 / 13629 | 522.486s | 0 | 0 |

<a id="travel-flights"></a>

## 旅行 / 机票（travel/flights）

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

<a id="comparison-cbad562eed82"></a>

### financial-disclosures-001 v1, financial-disclosures-002 v1, financial-disclosures-003 v1, financial-disclosures-004 v1

**capitol-exposed / data-api-keyless** — 4 完成 / 0 未完成 / 0 环境无效。

1.18.29 / glm-5.3-flash / high · 900s · natural · none · 独立验收（本轮无其他服务答案可参考）

准备：15-minute budget comparison following the 600-second round. Same task v1, model GLM-5.3-Flash/high, role instructions, service/route, references and price snapshot; execution and grading each 900 seconds, batch ceiling ten concurrent model sessions, with one active session per existing runtime (four available runtimes). Reuses the independently passed access setup and generic installed dependencies in the same containers with fresh task workspaces/sessions; no fresh signup. Collector fix preserves receipts before artifact collection and omits links without following them. Prior 600-second records remain separate. Shared-IP service quotas are checked before dispatch. Dispatch amendment: user deferred Bargo before execution because its daily quota was exhausted. Only CapitolExposed execution/grading ran (two runtimes, actual peak two); no other service answer was available. Controller archived prior task files before reuse; shared temporary-directory cleanup was added before execution 003 and grading 002.

- [capitol-disclosures-004-900s-c10-r1](../data/experiments/evaluations/capitol-disclosures-004-900s-c10-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 官方免费规则及当次免 Key 只读请求支持服务费用为零；模型费用另行估算。; https://www.capitolexposed.com/api-docs
- [capitol-disclosures-003-900s-c10-r1](../data/experiments/evaluations/capitol-disclosures-003-900s-c10-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 官方免费规则及当次免 Key 只读请求支持服务费用为零；模型费用另行估算。; https://www.capitolexposed.com/api-docs
- [capitol-disclosures-002-900s-c10-r1](../data/experiments/evaluations/capitol-disclosures-002-900s-c10-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 官方免费规则及当次免 Key 只读请求支持服务费用为零；模型费用另行估算。; https://www.capitolexposed.com/api-docs
- [capitol-disclosures-001-900s-c10-r1](../data/experiments/evaluations/capitol-disclosures-001-900s-c10-r1.json)：模型费用 $0.0100；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 官方免费规则及当次免 Key 只读请求支持服务费用为零；模型费用另行估算。; https://www.capitolexposed.com/api-docs

<a id="comparison-864872ad88ab"></a>

### financial-disclosures-001 v1, financial-disclosures-002 v1, financial-disclosures-003 v1, financial-disclosures-004 v1

**bargo-congress / congress-api-keyless** — 1 完成 / 3 未完成 / 0 环境无效。

1.18.29 / glm-5.3-flash / high · 600s · natural · none · 独立验收可参考同期 2 家服务的答案

准备：Continues the independently passed 2026-09-15 keyless access setup in the same service/route container. Reuses service configuration and installed dependencies only; new workspace/session per task. Controller prepared tasks and official references. Cloud execution and grading GLM-5.3-Flash/high, 600 seconds each; at most two active sessions across batch. Round 1 of this four-task comparison; no fresh signup claimed.

- [bargo-disclosures-004-r1](../data/experiments/evaluations/bargo-disclosures-004-r1.json)：模型费用 —；Per-request usage capture is incomplete. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；confirmed_free: 官方免费规则与本次四次免 Key 只读响应支持 confirmed_free；统一计价脚本计算为零。原验收金额字段留空，原件保留；这不是实付账单。; https://www.bargo.ai/free-apis/congress
- [bargo-disclosures-003-r1](../data/experiments/evaluations/bargo-disclosures-003-r1.json)：模型费用 $0.03；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 官方文档明示读端点免 Key 免费（rate-limited，FREE · NO CARD）；本次执行仅 2 次免 Key 读请求、22 行，验收复核另用 2 次请求，均在 Keyless 限额内；执行环境未提供账户、Key 或支付方式，无注册、无付款。; https://www.bargo.ai/free-apis/congress; https://www.bargo.ai/free-apis/terms
- [bargo-disclosures-002-r1](../data/experiments/evaluations/bargo-disclosures-002-r1.json)：模型费用 —；Per-request usage capture is incomplete. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；confirmed_free: 官方文档声明读端点免 Key 免费（rate-limited），无账户/卡片要求；免 Key 限额 30 请求/100 行每天每 IP。; https://www.bargo.ai/free-apis/congress
- [bargo-disclosures-001-r1](../data/experiments/evaluations/bargo-disclosures-001-r1.json)：模型费用 —；Per-request usage capture is incomplete. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；confirmed_free: 服务侧费用为 0（免 Key 免费档内使用）；模型用量与模型费用不在本字段范围。; https://www.bargo.ai/free-apis/congress; grading/artifacts/evidence/verification-summary.md

<a id="comparison-bd611da6270b"></a>

### financial-access-001 v1

**bargo-congress / congress-api-keyless** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.29 / glm-5.3-flash / high · 600s · natural · none

准备：Account-free public API; no account, key or call code pre-provisioned. Dedicated service/route container; fresh session per task, retaining only service configuration and installed dependencies. Controller researched candidates and froze independent references; cloud execution and grading use GLM-5.3-Flash/high.

- [bargo-access](../data/experiments/evaluations/bargo-access.json)：模型费用 $0.0068；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 免费规则：官方文档明示读端点免 Key、FREE · NO CARD，keyless 30 请求/100 行每天/IP。本次适用观察：执行全部 9 次业务请求及验收复测均使用 keyless 读端点并返回 200，响应头 X-RateLimit-Limit=30、X-RateLimit-Rows-Limit=100 与该规则一致，未注册账号、未提供或绑定任何支付方式，无付费回执。依据：工具记录 0005（官方页）与 0009/0010/0014（响应头），验收复测见 evidence/live-verification.md。; https://www.bargo.ai/free-apis/congress; https://www.bargo.ai/free-apis/terms; reference.json free_rule: Keyless 30 requests and 100 rows/day/IP

**capitol-exposed / data-api-keyless** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.29 / glm-5.3-flash / high · 600s · natural · none

准备：Account-free public API; no account, key or call code pre-provisioned. Dedicated service/route container; fresh session per task, retaining only service configuration and installed dependencies. Controller researched candidates and froze independent references; cloud execution and grading use GLM-5.3-Flash/high.

- [capitol-access](../data/experiments/evaluations/capitol-access.json)：模型费用 $0.0091；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 本轮仅使用免 Key GET 读取端点（/stats、/members、/search、/members/{slug}/trades），未用 API Key、未触发付费 AI 或批量导出产品，适用文档化免费层，服务费用为 0。; https://www.capitolexposed.com/api-docs（执行中抓取：Free-tier requests require no authentication, rate-limited by IP）; reference.json free_rule：免 Key member/trade 列表端点 60 次/分/IP，免费读取并要求署名

**ecb-data / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.29 / glm-5.3-flash / high · 600s · natural · none

准备：Account-free public API; no account, key or call code pre-provisioned. Dedicated service/route container; fresh session per task, retaining only service configuration and installed dependencies. Controller researched candidates and froze independent references; cloud execution and grading use GLM-5.3-Flash/high.

- [ecb-access](../data/experiments/evaluations/ecb-access.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 免费结论依据 ECB 官方免费使用规则与本次实际无凭据只读请求，而非执行者自述或仅因成功响应；未发生任何服务端计费。; https://www.ecb.europa.eu/services/using-our-site/disclaimer/html/index.en.html; execution/artifacts/ENVIRONMENT.md; grading/artifacts/evidence/ecb-independent-check.md

**frankfurter / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.29 / glm-5.3-flash / high · 600s · natural · none

准备：Account-free public API; no account, key or call code pre-provisioned. Dedicated service/route container; fresh session per task, retaining only service configuration and installed dependencies. Controller researched candidates and froze independent references; cloud execution and grading use GLM-5.3-Flash/high.

- [frankfurter-access](../data/experiments/evaluations/frankfurter-access.json)：模型费用 $0.0052；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 服务端无计费回执；本次调用确认免费，无实付金额，故金额字段保留 null。模型费用由运行器与统一计价脚本处理，不在此填写。; https://frankfurter.dev/; grading/artifacts/evidence/independent-check.md

**tracefour / data-api-keyless** — 0 完成 / 1 未完成 / 0 环境无效。

1.18.29 / glm-5.3-flash / high · 600s · natural · none

准备：Account-free public API; no account, key or call code pre-provisioned. Dedicated service/route container; fresh session per task, retaining only service configuration and installed dependencies. Controller researched candidates and froze independent references; cloud execution and grading use GLM-5.3-Flash/high.

- [tracefour-access](../data/experiments/evaluations/tracefour-access.json)：模型费用 $0.0071；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 规则：指定入口为免 Key 免费读取，限 60 次/小时/IP。本次适用性：全程仅约 9 次免 Key 只读 GET，远低于限额；所有请求在 Cloudflare 边缘即被 403 质询拒绝，服务未实际处理任何请求；未提供也未创建任何账户、Key 或支付方式，无付款回执。故本次服务侧费用为 0。模型 token 与模型费用由运行器统一核算，不在此列。; reference.json（本题冻结参考 free_rule：Keyless reads 60 requests/hour/IP; compilation CC BY 4.0 with attribution）; execution/artifacts/probe-results.txt; grading/artifacts/evidence/independent-verification.md

<a id="comparison-d86a11990066"></a>

### financial-fx-001 v1

**ecb-data / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.29 / glm-5.3-flash / high · 600s · natural · none

准备：Account-free public API; no account, key or call code pre-provisioned. Dedicated service/route container; fresh session per task, retaining only service configuration and installed dependencies. Controller researched candidates and froze independent references; cloud execution and grading use GLM-5.3-Flash/high.

- [ecb-business](../data/experiments/evaluations/ecb-business.json)：模型费用 $0.0034；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 规则：ECB 版权政策允许免费使用其网站直接获取的信息（需注明来源），且 Data Portal SDMX REST API 为公开 web 服务，无需注册、Key 或付款（站点注册仅用于门户个性化功能）；适用：本次仅无鉴权 GET 且 HTTP 200，环境未提供账户或支付方式，验收环境独立重放同样成功。无账单回执，实付为 0。; https://www.ecb.europa.eu/services/disclaimer/html/index.en.html; https://data.ecb.europa.eu/help/api/overview; https://data.ecb.europa.eu/help/api/data-examples; review-packet/tools/0005.json

**frankfurter / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.29 / glm-5.3-flash / high · 600s · natural · none

准备：Account-free public API; no account, key or call code pre-provisioned. Dedicated service/route container; fresh session per task, retaining only service configuration and installed dependencies. Controller researched candidates and froze independent references; cloud execution and grading use GLM-5.3-Flash/high.

- [frankfurter-business](../data/experiments/evaluations/frankfurter-business.json)：模型费用 $0.0038；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 服务本身免费：官方声明无 Key、无配额，本次仅匿名 GET 读取，无任何付费路径; https://frankfurter.dev/ （官方文档："Free, open-source exchange rates API ... No API key required"；FAQ：commercial use free、no quotas，仅防滥用限流）

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
