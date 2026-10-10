<!-- GENERATED — npm run generate; source: data/experiments/evaluations/ -->
# 任务实测结果

每行只说明该服务入口在该任务和运行配置下的观察。完成率衡量 Agent 在本轮环境及约束下是否交付完整任务，不等于服务可用率；未完成须结合已验证能力、用户交付缺口与具体阻碍阅读。主持复核补充说明来自 result-notes.json，独立于原始验收，不改变历史状态或统计。Token用量为输入总数（含缓存）加输出，缓存不重复相加。模型费用根据保存的LiteLLM价格表自动估算，估价日期不冒充运行日期；服务费用单独记录，unknown不等于0。点击结果可查看冻结的任务、独立复核与选取的证据；原始日志仍在本地。免费账号的注册准备若发生在计时前，说明保存在 environment.preparation_note；表中 token 与耗时不包含这部分准备。历史记录保留，不把不同任务、配置或日期直接平均成服务排名。

按当前分类和接入／业务阶段分组，再展示同一任务版本和冻结内容的运行。展示归属来自 task-classifications.yaml；历史任务、结果和用量不改写。汇总要求准备说明完全相同，包下载源、请求上限等条件改变后分别统计；说明不同或缺失时不推定等价，因此措辞差异也可能拆分汇总。同组仍需核对接入前提与模型等配置，不能仅按耗时排序判断优劣。

输入方式 legacy 是带明确测试要求的初期试跑，Agent 的开销包含证据保存与整理；natural 只提供用户任务、资料及运行环境，使用自动会话日志与外部远端复核。不同方式分别记录；单次测量都不代表典型开销，跨版本差异也可能来自业务要求、执行路径和缓存变化。

<a id="databases-hosted-relational"></a>

## 数据库 / 托管关系型数据库（databases/hosted-relational）

### database-atomic-import-001 / v1

我的个人书目目录要按文件批量导入，遇到重复编号不能留下半批数据。请做一个可复用的导入器，用数据库的整批原子操作或事务保护，在提供的两个独立测试表中分别实际验证错误样本整批拒绝、更正样本全部保存，原有书目不变。交付导入器、简短用法和两次结果，凭据单独保存。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| neon / claimable-api | database-atomic-import-001 (v1) | Preprovided existing authorized parent identity; executor creates one fresh empty logical database | natural | [completed](../data/experiments/evaluations/neon-atomic-import-001-ds41-r1.json) | 2026-10-08T21:46:10.206848+00:00 | 1.18.35 / deepseek-flash / high | 135931 / 126336 / 6373 | 41.536756s | 0 | 0 |
| turso / platform-api | database-atomic-import-001 (v1) | Preprovided existing authorized parent identity; executor creates one fresh empty logical database | natural | [completed](../data/experiments/evaluations/turso-atomic-import-001-ds41-r1.json) | 2026-10-08T21:46:08.207709+00:00 | 1.18.35 / deepseek-flash / high | 318702 / 303104 / 9179 | 64.04082s | 0 | 0 |

### database-restore-001 / v1

帮我给个人待办应用做一次备份恢复演练：把源库导出成可下载留存的逻辑备份，在同一服务中新建一个独立空数据库，用这份备份实际恢复，保持源库不变。恢复结束后重新连接新库核对，交付备份、简短恢复方法、新库位置、各表行数和核对结果，并说明新库的免费或到期限制。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| neon / claimable-api | database-restore-001 (v1) | none initially; generated anonymous Claimable project credentials | natural | [completed](../data/experiments/evaluations/neon-restore-mirror-001-ds41-r1.json) | 2026-10-08T16:59:27.290152+00:00 | 1.18.35 / deepseek-flash / high | 465395 / 445824 / 14007 | 89.827118s | unknown | 0 |
| turso / platform-api | database-restore-001 (v1) | existing authorized Turso management account | natural | [not_completed](../data/experiments/evaluations/turso-restore-mirror-001-ds41-r1.json) | 2026-10-08T16:59:25.563534+00:00 | 1.18.35 / deepseek-flash / high | unknown | 85.787553s | 0 | 0 |

**主持复核补充说明（原判定不变）：**

- [turso-restore-mirror-001-ds41-r1](../data/experiments/evaluations/turso-restore-mirror-001-ds41-r1.json)：主持复核补充，原独立验收判定不变：真实备份、新库恢复、完整结构与记录、重新连接及源库未变均已独立验证。未完成是因为25次模型请求耗尽后，没有交付备份位置、恢复方法、目标位置及结果和期限说明，不是恢复失败或服务拒绝。约86秒即耗尽请求数，600秒时间预算仍有剩余。

### database-todos-001 / v2

为我的个人待办应用准备一个独立的远程数据库，用附件数据验证新增和修改后的保存情况。写入程序退出后，用一个全新的程序重新连接同一数据库读取；给我按 id 排列的全部待办、未完成待办，以及总数和完成数，并说明数据库的免费或到期限制。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| neon / claimable-api | database-todos-001 (v2) | none initially; executor obtains anonymous scoped test credentials | natural | [completed](../data/experiments/evaluations/neon-todos-001v2-ds41-r1.json) | 2026-10-08T12:40:43.320755+00:00 | 1.18.35 / deepseek-flash / high | 268481 / 253824 / 6356 | 256.353056s | 0 | 0 |
| turso / platform-api | database-todos-001 (v2) | pre-existing Turso management account | natural | [completed](../data/experiments/evaluations/turso-todos-001v2-ds41-r1.json) | 2026-10-08T12:40:41.768769+00:00 | 1.18.35 / deepseek-flash / high | 269458 / 251008 / 7176 | 81.907304s | 0 | 0 |

### database-todos-001 / v1

为我的个人待办应用准备一个独立的远程数据库，验证新增、修改和重新连接后读取待办事项

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| turso / platform-api | database-todos-001 (v1) | provided: TURSO_API_TOKEN, TURSO_ORGANIZATION | legacy | [completed](../data/experiments/evaluations/codex-20260907T113506.422646Z-turso.json) | 2026-09-07T11:35:06.452325+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 755366 / 687616 / 12234 | 457.78s | 0 | 0 |
| neon / ephemeral-api | database-todos-001 (v1) | none | legacy | [completed](../data/experiments/evaluations/codex-20260907T112258.549053Z-neon.json) | 2026-09-07T11:22:58.558715+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 452623 / 402560 / 12790 | 456.342s | 0 | 0 |

<a id="databases-hosted-relational"></a>

## 数据库 / 托管关系型数据库（databases/hosted-relational） · 接入测试

### database-access-001 / v1

帮我通过指定方式接通这个数据库服务，准备一个本轮专用的空远程测试数据库，做一次不写入业务数据的查询确认可用，并保存后续连接配置；说明接入步骤、人工门槛和免费或到期限制。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| turso / platform-api | database-access-001 (v1) | Preprovided existing authorized parent identity; executor creates one fresh empty logical database | natural | [completed](../data/experiments/evaluations/turso-atomic-access-ds41-r1.json) | 2026-10-08T21:36:57.665696+00:00 | 1.18.35 / deepseek-flash / high | 224623 / 211328 / 7991 | 50.403294s | 0 | 0 |
| neon / claimable-api | database-access-001 (v1) | Preprovided existing authorized parent identity; executor creates one fresh empty logical database | natural | [completed](../data/experiments/evaluations/neon-atomic-access-ds41-r1.json) | 2026-10-08T21:36:57.665333+00:00 | 1.18.35 / deepseek-flash / high | 161771 / 149632 / 5465 | 40.8719s | unknown | 0 |
| turso / platform-api | database-access-001 (v1) | existing authorized Turso management account | natural | [completed](../data/experiments/evaluations/turso-restore-mirror-access-ds41-r1.json) | 2026-10-08T16:39:23.940242+00:00 | 1.18.35 / deepseek-flash / high | 431148 / 412928 / 10242 | 79.603005s | 0 | 0 |
| neon / claimable-api | database-access-001 (v1) | none initially; generated anonymous Claimable project credentials | natural | [completed](../data/experiments/evaluations/neon-restore-mirror-access-ds41-r1.json) | 2026-10-08T16:39:23.940055+00:00 | 1.18.35 / deepseek-flash / high | 234599 / 219264 / 5665 | 51.414486s | 0 | 0 |
| neon / claimable-api | database-access-001 (v1) | none initially; generated anonymous Claimable project credentials | natural | [not_completed](../data/experiments/evaluations/neon-restore-access-ds41-r1.json) | 2026-10-08T16:27:54.812617+00:00 | 1.18.35 / deepseek-flash / high | unknown | 290.065099s | 0 | 0 |
| turso / platform-api | database-access-001 (v1) | existing authorized Turso management account | natural | [completed](../data/experiments/evaluations/turso-restore-access-ds41-r1.json) | 2026-10-08T16:27:54.812377+00:00 | 1.18.35 / deepseek-flash / high | 312145 / 296448 / 11557 | 83.658056s | 0 | 0 |
| neon / claimable-api | database-access-001 (v1) | none initially; executor obtains anonymous scoped test credentials | natural | [completed](../data/experiments/evaluations/neon-access-ds41-r1.json) | 2026-10-08T12:36:09.493852+00:00 | 1.18.35 / deepseek-flash / high | 261313 / 247040 / 5486 | 197.823139s | 0 | 0 |
| turso / platform-api | database-access-001 (v1) | pre-existing Turso management account | natural | [completed](../data/experiments/evaluations/turso-access-ds41-r1.json) | 2026-10-08T12:36:09.493565+00:00 | 1.18.35 / deepseek-flash / high | 234818 / 221056 / 7475 | 68.505025s | 0 | 0 |

**主持复核补充说明（原判定不变）：**

- [neon-restore-access-ds41-r1](../data/experiments/evaluations/neon-restore-access-ds41-r1.json)：主持复核补充，原独立验收判定不变：匿名身份和项目已创建，但数据库凭据获取、真实只读SQL查询及可复用配置保存均未完成，不能归为只缺最终答复。原300秒批次超时；后来镜像环境的成功属于另一批条件，不能补写本次结果，也不能把旧次未完成解释为Neon不支持数据库访问。

<a id="productivity-storage-collaborative-tables"></a>

## 办公与协作 / 协作表格（productivity-storage/collaborative-tables）

### collaborative-tables-shared-expenses-001 / v1

我和室友按一人一半分摊共同支出。请把材料里的 10 月账目做成在线账本，保留每笔日期、用途、付款人和人民币金额，并在表里显示各自已付、应分摊金额，以及谁还需补给谁多少钱。以后追加账目或修正金额时，汇总要自动更新，不用再找 Agent 或运行本地脚本。给我私人表格链接、当前结算数和一句话说明在哪里继续记账；不要实际转账、邀请或通知任何人。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| grist / hosted-mcp | collaborative-tables-shared-expenses-001 (v1) | provided: existing Grist Personal account; new empty parent workspace prepared by controller | natural | [completed](../data/experiments/evaluations/grist-mcp-shared-expenses-001-ds41-r1.json) | 2026-10-08T20:47:10.577404+00:00 | 1.18.35 / deepseek-flash / high | 754675 / 721280 / 14319 | 86.478336s | 0 | 0 |
| grist / rest-api | collaborative-tables-shared-expenses-001 (v1) | provided: existing Grist Personal account; new empty parent workspace prepared by controller | natural | [not_completed](../data/experiments/evaluations/grist-rest-shared-expenses-001-ds41-r1.json) | 2026-10-08T20:44:03.248139+00:00 | 1.18.35 / deepseek-flash / high | unknown | 177.21403s | 0 | 0 |

**主持复核补充说明（原判定不变）：**

- [grist-rest-shared-expenses-001-ds41-r1](../data/experiments/evaluations/grist-rest-shared-expenses-001-ds41-r1.json)：主持复核补充，原独立验收判定不变：在线账本及新增、修改后的自动重算均经独立验证。未完成是因为25次模型请求耗尽，没有向用户交付私人链接、结算金额和继续记账说明。服务端结果正确，但完整用户交付缺失；约177秒结束，未耗尽600秒时间预算。

### collaborative-tables-001 / v4

把附件里的读书会会议待办整理成在线任务表，包含负责人、截止日期和完成状态。给我链接，并列出未完成事项、负责人和截止日期。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| grist / hosted-mcp | collaborative-tables-001 (v4) | provided: existing Grist Personal account; new empty parent workspace prepared by controller | natural | [completed](../data/experiments/evaluations/grist-mcp-tables-001v4-ds41-r1.json) | 2026-10-08T13:49:55.441225+00:00 | 1.18.35 / deepseek-flash / high | 194402 / 180864 / 6168 | 50.849686s | 0 | 0 |
| grist / rest-api | collaborative-tables-001 (v4) | provided: existing Grist Personal account; new empty parent workspace prepared by controller | natural | [completed](../data/experiments/evaluations/grist-rest-tables-001v4-ds41-r1.json) | 2026-10-08T13:48:16.280786+00:00 | 1.18.35 / deepseek-flash / high | 439512 / 413056 / 8661 | 83.200902s | 0 | 0 |

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

<a id="web-search-data-web-extraction"></a>

## 搜索与数据获取 / 网页内容提取（web-search-data/web-extraction）

### web-extraction-scanned-table-001 / v1

我在把一份旧扫描手册整理成可检索的表格。请从材料指定的 TTB Table No. 4 中，把 Proof 从 1.0 到 2.0 的这一小段转成 CSV，保留两种 gallons per pound 数值，给我文件和官方来源链接。只抄录原表，不做计税或其他业务计算。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| exa / public-mcp | web-extraction-scanned-table-001 (v1) | none; anonymous public extraction routes, no account/email/token/payment supplied | natural | [not_completed](../data/experiments/evaluations/exa-pdf-scanned-table-001-ds41-r1.json) | 2026-10-08T20:14:50.718553+00:00 | 1.18.35 / deepseek-flash / high | 709413 / 682112 / 36074 | 192.427232s | 0 | 0 |
| firecrawl / public-scrape-api | web-extraction-scanned-table-001 (v1) | none; anonymous public extraction routes, no account/email/token/payment supplied | natural | [completed](../data/experiments/evaluations/firecrawl-pdf-scanned-table-001-ds41-r1.json) | 2026-10-08T20:14:49.046726+00:00 | 1.18.35 / deepseek-flash / high | 359102 / 337152 / 6593 | 57.05532s | unknown | 0 |

### web-extraction-pdf-hikes-001 / v1

我在整理锡安国家公园的徒步候选清单。请从附件指定的官方 PDF 中，把 Hiking Guide 表里 EASY 一组的全部步道做成 CSV，保留英文名称、往返距离、平均用时和海拔变化，按原表顺序排列，给我文件和来源链接。只整理这份指南，不判断目前是否开放或适合安全出行。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| exa / public-mcp | web-extraction-pdf-hikes-001 (v1) | none; anonymous public extraction routes, no account/email/token/payment supplied | natural | [completed](../data/experiments/evaluations/exa-pdf-hikes-001-ds41-r1.json) | 2026-10-08T18:54:42.102239+00:00 | 1.18.35 / deepseek-flash / high | 245616 / 227072 / 13246 | 72.610281s | 0 | 0 |
| firecrawl / public-scrape-api | web-extraction-pdf-hikes-001 (v1) | none; anonymous public extraction routes, no account/email/token/payment supplied | natural | [completed](../data/experiments/evaluations/firecrawl-pdf-hikes-001-ds41-r1.json) | 2026-10-08T18:54:40.401656+00:00 | 1.18.35 / deepseek-flash / high | 311181 / 285952 / 6369 | 44.747639s | 0 | 0 |

### web-extraction-holidays-001 / v1

我想把官方假日表用于个人日历整理。请从附件给定的网页提取 2027 年假日安排，做成按日期排序的 CSV 文件，包含表中全部假日的日期、星期和英文名称；按网页列出的日期记录，并给我文件和来源链接。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| exa / public-mcp | web-extraction-holidays-001 (v1) | none | natural | [completed](../data/experiments/evaluations/exa-extraction-holidays-001-ds41-r1.json) | 2026-10-08T13:16:48.131642+00:00 | 1.18.35 / deepseek-flash / high | 307477 / 290048 / 5337 | 38.131958s | 0 | 0 |
| firecrawl / public-scrape-api | web-extraction-holidays-001 (v1) | none | natural | [completed](../data/experiments/evaluations/firecrawl-extraction-holidays-001-ds41-r1.json) | 2026-10-08T13:16:46.370512+00:00 | 1.18.35 / deepseek-flash / high | 260900 / 237312 / 3282 | 28.302448s | 0 | 0 |

<a id="productivity-storage-qr-codes"></a>

## 办公与协作 / 二维码图片（productivity-storage/qr-codes）

### qr-codes-travel-link-001 / v1

帮我把材料里的国家公园旅行指南链接做成一张静态二维码 PNG，放进我打印的旅行资料。按材料里的尺寸和配色制作，扫码直接得到完整原链接，并把图片文件交给我。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| goqr / public-qr-api | qr-codes-travel-link-001 (v1) | none; public static QR APIs, no account/key/email/payment supplied | natural | [completed](../data/experiments/evaluations/goqr-qr-travel-link-001-ds41-r1.json) | 2026-10-08T19:47:45.550068+00:00 | 1.18.35 / deepseek-flash / high | 57077 / 45440 / 1781 | 15.063508s | 0 | 0 |
| quickchart / public-qr-api | qr-codes-travel-link-001 (v1) | none; public static QR APIs, no account/key/email/payment supplied | natural | [completed](../data/experiments/evaluations/quickchart-qr-travel-link-001-ds41-r1.json) | 2026-10-08T19:47:43.811739+00:00 | 1.18.35 / deepseek-flash / high | 142552 / 130176 / 3258 | 29.713184s | 0 | 0 |

<a id="productivity-storage-qr-codes"></a>

## 办公与协作 / 二维码图片（productivity-storage/qr-codes） · 接入测试

### qr-codes-access-001 / v1

帮我接通这个二维码服务，通过指定入口生成一张测试二维码并保存图片，确认我能开始使用；留下后续调用需要的通用配置，并说明接入步骤和实际门槛。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| goqr / public-qr-api | qr-codes-access-001 (v1) | none; public static QR APIs, no account/key/email/payment supplied | natural | [completed](../data/experiments/evaluations/goqr-qr-access-ds41-r1.json) | 2026-10-08T19:42:40.980388+00:00 | 1.18.35 / deepseek-flash / high | 110859 / 99328 / 3081 | 58.588541s | unknown | 0 |
| quickchart / public-qr-api | qr-codes-access-001 (v1) | none; public static QR APIs, no account/key/email/payment supplied | natural | [completed](../data/experiments/evaluations/quickchart-qr-access-ds41-r1.json) | 2026-10-08T19:42:40.980149+00:00 | 1.18.35 / deepseek-flash / high | 124001 / 112128 / 3327 | 58.362095s | 0 | 0 |

<a id="web-search-data-route-planning"></a>

## 搜索与数据获取 / 路线规划（web-search-data/route-planning）

### route-planning-bridge-001 / v1

我在整理旅行地图，想保存从附件南侧点到北侧点、开车穿过金门大桥的路线。请给出总里程、服务估算的驾驶时间、主要道路和行驶方向，交付一份可留存到地图中的路线文件，并注明来源。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| valhalla / public-route-api | route-planning-bridge-001 (v1) | none; anonymous FOSSGIS public demos, no account/token/email/payment supplied | natural | [completed](../data/experiments/evaluations/valhalla-routing-bridge-001-ds41-r1.json) | 2026-10-08T19:20:57.252254+00:00 | 1.18.35 / deepseek-flash / high | 178879 / 157440 / 3233 | 24.691011s | unknown | 0 |
| osrm / public-route-api | route-planning-bridge-001 (v1) | none; anonymous FOSSGIS public demos, no account/token/email/payment supplied | natural | [completed](../data/experiments/evaluations/osrm-routing-bridge-001-ds41-r1.json) | 2026-10-08T19:20:18.636362+00:00 | 1.18.35 / deepseek-flash / high | 160961 / 141184 / 5374 | 33.370304s | unknown | 0 |

<a id="web-search-data-route-planning"></a>

## 搜索与数据获取 / 路线规划（web-search-data/route-planning） · 接入测试

### route-planning-access-001 / v1

帮我接通这个路线规划服务，通过指定入口查询附件两个点之间的一段小汽车路线，告诉我服务给出的距离和估算驾驶时间，确认可以用；保存后续调用所需配置，并说明接入步骤和实际门槛。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| valhalla / public-route-api | route-planning-access-001 (v1) | none; anonymous FOSSGIS public demos, no account/token/email/payment supplied | natural | [completed](../data/experiments/evaluations/valhalla-routing-access-ds41-r1.json) | 2026-10-08T19:17:01.066382+00:00 | 1.18.35 / deepseek-flash / high | 276819 / 255360 / 4440 | 30.104117s | unknown | 0 |
| osrm / public-route-api | route-planning-access-001 (v1) | none; anonymous FOSSGIS public demos, no account/token/email/payment supplied | natural | [completed](../data/experiments/evaluations/osrm-routing-access-ds41-r1.json) | 2026-10-08T19:15:51.908424+00:00 | 1.18.35 / deepseek-flash / high | 55580 / 47488 / 2272 | 16.986749s | unknown | 0 |

<a id="web-search-data-web-extraction"></a>

## 搜索与数据获取 / 网页内容提取（web-search-data/web-extraction） · 接入测试

### web-extraction-access-001 / v1

帮我接通这个网页内容提取服务，通过指定方式读取附件里的示例网页，给我页面标题和一句内容概述，确认能用；保存后续调用所需配置，并说明接入步骤和遇到的门槛。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| exa / public-mcp | web-extraction-access-001 (v1) | none; anonymous public extraction routes, no account/email/token/payment supplied | natural | [completed](../data/experiments/evaluations/exa-pdf-access-ds41-r1.json) | 2026-10-08T18:47:05.275433+00:00 | 1.18.35 / deepseek-flash / high | 161115 / 146048 / 4641 | 33.987788s | 0 | 0 |
| firecrawl / public-scrape-api | web-extraction-access-001 (v1) | none; anonymous public extraction routes, no account/email/token/payment supplied | natural | [completed](../data/experiments/evaluations/firecrawl-pdf-access-ds41-r1.json) | 2026-10-08T18:47:05.275071+00:00 | 1.18.35 / deepseek-flash / high | 183635 / 161408 / 3163 | 23.34858s | 0 | 0 |
| jina / reader-api | web-extraction-access-001 (v1) | none | natural | [invalid_run](../data/experiments/evaluations/jina-extraction-access-ds41-r2.json) | 2026-10-08T13:09:26.421153+00:00 | 1.18.35 / deepseek-flash / high | 110620 / 102400 / 5106 | 202.576397s | unknown | 0 |
| exa / public-mcp | web-extraction-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/exa-extraction-access-ds41-r1.json) | 2026-10-08T13:02:53.059860+00:00 | 1.18.35 / deepseek-flash / high | 161201 / 151680 / 3629 | 30.026639s | 0 | 0 |
| jina / reader-api | web-extraction-access-001 (v1) | none | natural | [invalid_run](../data/experiments/evaluations/jina-access-ds41-r1.json) | 2026-10-08T13:02:53.059652+00:00 | 1.18.35 / deepseek-flash / high | unknown | 89.179861s | unknown | 0 |
| firecrawl / public-scrape-api | web-extraction-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/firecrawl-access-ds41-r1.json) | 2026-10-08T13:02:53.059342+00:00 | 1.18.35 / deepseek-flash / high | 105719 / 84736 / 2019 | 22.199907s | 0 | 0 |

<a id="developer-tools-dependency-advisories"></a>

## 开发工具 / 依赖漏洞公告（developer-tools/dependency-advisories）

### dependency-advisories-check-001 / v1

我在整理项目的两条依赖安全告警。请用指定服务逐条核对当前版本是否仍在公告的受影响版本范围内，给出 5.2.x 分支中各自最早的修复版本；告诉我仅处理这两条至少需要升级到哪个版本，并附上可核对的依据链接。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| github / public-advisories-api | dependency-advisories-check-001 (v1) | none; anonymous public advisory API, no account/email/token/payment supplied | natural | [completed](../data/experiments/evaluations/github-advisories-django-001-ds41-r1.json) | 2026-10-08T18:23:46.008530+00:00 | 1.18.35 / deepseek-flash / high | 72242 / 62336 / 3531 | 22.98942s | 0 | 0 |
| osv / public-api | dependency-advisories-check-001 (v1) | none; anonymous public advisory API, no account/email/token/payment supplied | natural | [completed](../data/experiments/evaluations/osv-advisories-django-001-ds41-r1.json) | 2026-10-08T18:23:44.313467+00:00 | 1.18.35 / deepseek-flash / high | 193502 / 166272 / 7536 | 167.099132s | 0 | 0 |

<a id="developer-tools-dependency-advisories"></a>

## 开发工具 / 依赖漏洞公告（developer-tools/dependency-advisories） · 接入测试

### dependency-advisories-access-001 / v1

帮我接通这个依赖漏洞公告服务，通过指定方式做一次真实查询，确认能取得可识别的公告记录，并保存后续查询需要的本地配置；说明接入步骤和实际阻碍。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| github / public-advisories-api | dependency-advisories-access-001 (v1) | none; anonymous public advisory API, no account/email/token/payment supplied | natural | [completed](../data/experiments/evaluations/github-advisories-access-ds41-r1.json) | 2026-10-08T18:20:21.466259+00:00 | 1.18.35 / deepseek-flash / high | 180078 / 166528 / 5675 | 36.125993s | unknown | 0 |
| osv / public-api | dependency-advisories-access-001 (v1) | none; anonymous public advisory API, no account/email/token/payment supplied | natural | [completed](../data/experiments/evaluations/osv-advisories-access-ds41-r1.json) | 2026-10-08T18:20:21.466021+00:00 | 1.18.35 / deepseek-flash / high | 172161 / 159232 / 6358 | 42.586955s | unknown | 0 |

<a id="communication-mailboxes"></a>

## 通信 / 邮箱（communication/mailboxes） · 接入测试

### mailboxes-create-001 / v2

为这次自动化测试准备一个临时收件邮箱，给我地址，并保存后续读取收件箱需要的访问信息。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| mail-tm / mail-api | mailboxes-create-001 (v2) | none initially; one fresh anonymous mailbox and necessary identity created inside measured execution | natural | [completed](../data/experiments/evaluations/mail-tm-mailbox-create-v2-ds41-r1.json) | 2026-10-08T17:53:30.353516+00:00 | 1.18.35 / deepseek-flash / high | 113186 / 103936 / 3032 | 28.614918s | 0 | 0 |
| agentmail / mail-api | mailboxes-create-001 (v2) | none initially; one fresh anonymous mailbox and necessary identity created inside measured execution | natural | [not_completed](../data/experiments/evaluations/agentmail-mailbox-create-v2-ds41-r1.json) | 2026-10-08T17:53:30.353217+00:00 | 1.18.35 / deepseek-flash / high | 766511 / 733568 / 16873 | 137.407982s | unknown | 0 |

**主持复核补充说明（原判定不变）：**

- [agentmail-mailbox-create-v2-ds41-r1](../data/experiments/evaluations/agentmail-mailbox-create-v2-ds41-r1.json)：主持复核补充，原独立验收判定不变：本轮没有创建邮箱、读取收件箱或取得可复用凭据。测试服务器及容器访问API均收到CloudFront 403，说明该访问路径当时受阻，具体原因未确定，不能据此推断服务整体不可用。另有执行偏离：请求超过12次上限，4次注册POST与答复所称一次不符。

<a id="web-search-data-public-holidays"></a>

## 搜索与数据获取 / 公共节假日（web-search-data/public-holidays）

### public-holidays-berlin-001 / v1

我在整理明年在柏林的个人日程。请通过指定服务查出 2027 年适用于德国柏林州的全部公共节假日，按日期列出日期和节日名称，给出总数并注明查询来源。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| openholidays / public-holidays-api | public-holidays-berlin-001 (v1) | none; anonymous publicAPI, no account/email/key/payment supplied | natural | [completed](../data/experiments/evaluations/openholidays-holidays-berlin-001-ds41-r1.json) | 2026-10-08T17:28:57.472194+00:00 | 1.18.35 / deepseek-flash / high | 171236 / 151680 / 3112 | 30.480165s | 0 | 0 |
| nager-date / community-api-v4 | public-holidays-berlin-001 (v1) | none; anonymous publicAPI, no account/email/key/payment supplied | natural | [completed](../data/experiments/evaluations/nager-date-holidays-berlin-001-ds41-r1.json) | 2026-10-08T17:28:55.765485+00:00 | 1.18.35 / deepseek-flash / high | 153596 / 142208 / 5195 | 41.507746s | 0 | 0 |

<a id="web-search-data-public-holidays"></a>

## 搜索与数据获取 / 公共节假日（web-search-data/public-holidays） · 接入测试

### public-holidays-access-001 / v1

帮我接通这个公共节假日查询服务，通过指定方式做一次真实的小范围假日查询，确认能查到日期和名称，并保存后续查询所需配置；说明接入步骤和实际阻碍。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| openholidays / public-holidays-api | public-holidays-access-001 (v1) | none; anonymous publicAPI, no account/email/key/payment supplied | natural | [completed](../data/experiments/evaluations/openholidays-holidays-access-ds41-r1.json) | 2026-10-08T17:26:34.723079+00:00 | 1.18.35 / deepseek-flash / high | 140980 / 129280 / 3990 | 29.527567s | 0 | 0 |
| nager-date / community-api-v4 | public-holidays-access-001 (v1) | none; anonymous publicAPI, no account/email/key/payment supplied | natural | [completed](../data/experiments/evaluations/nager-date-holidays-access-ds41-r1.json) | 2026-10-08T17:26:34.722814+00:00 | 1.18.35 / deepseek-flash / high | 60939 / 51840 / 2840 | 17.740838s | 0 | 0 |

<a id="web-search-data-scholarly-search"></a>

## 搜索与数据获取 / 学术文献检索（web-search-data/scholarly-search）

### scholarly-reference-001 / v1

请用指定服务根据附件中的阅读笔记找到那篇论文，为我的笔记补齐文献条目：原文题名、全部作者（保持原顺序）、发表年份、期刊名和可点击的 DOI 链接；用中文简单说明为什么匹配这些线索，并注明检索来源。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| openalex / public-rest-api | scholarly-reference-001 (v1) | none; currentofficialkeylesspublicroute, no account/email/payment supplied; lowvolumebibliographicmetadata only | natural | [completed](../data/experiments/evaluations/openalex-scholarly-reference-001-ds41-r1.json) | 2026-10-08T16:00:56.871697+00:00 | 1.18.35 / deepseek-flash / high | 100732 / 89984 / 3765 | 34.478856s | 0 | 0 |
| crossref / public-rest-api | scholarly-reference-001 (v1) | none; currentofficialkeylesspublicroute, no account/email/payment supplied; lowvolumebibliographicmetadata only | natural | [completed](../data/experiments/evaluations/crossref-scholarly-reference-001-ds41-r1.json) | 2026-10-08T16:00:55.130066+00:00 | 1.18.35 / deepseek-flash / high | 70253 / 60928 / 2661 | 28.382116s | 0 | 0 |

<a id="web-search-data-scholarly-search"></a>

## 搜索与数据获取 / 学术文献检索（web-search-data/scholarly-search） · 接入测试

### scholarly-access-001 / v1

帮我接通这个学术文献检索服务，通过指定方式做一次真实文献查询，确认能查到可识别的论文记录，并保存后续查询需要的本地配置；说明接入步骤和实际阻碍。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| crossref / public-rest-api | scholarly-access-001 (v1) | none; currentofficialkeylesspublicroute, no account/email/payment supplied; lowvolumebibliographicmetadata only | natural | [completed](../data/experiments/evaluations/crossref-scholarly-access-ds41-r1.json) | 2026-10-08T15:55:05.176032+00:00 | 1.18.35 / deepseek-flash / high | 215612 / 197376 / 5275 | 59.090171s | 0 | 0 |
| openalex / public-rest-api | scholarly-access-001 (v1) | none; currentofficialkeylesspublicroute, no account/email/payment supplied; lowvolumebibliographicmetadata only | natural | [completed](../data/experiments/evaluations/openalex-scholarly-access-ds41-r1.json) | 2026-10-08T15:55:05.175832+00:00 | 1.18.35 / deepseek-flash / high | 162189 / 150912 / 6032 | 43.797491s | 0 | 0 |

<a id="web-search-data-financial-data-prices"></a>

## 搜索与数据获取 / 金融数据 / 资产行情（web-search-data/financial-data/prices）

### financial-prices-001 / v1

帮我画出苹果公司 2026 年 8 月的每日收盘价走势，使用不复权价格，并附上 CSV 和数据来源。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| alpha-vantage / hosted-mcp | financial-prices-001 (v1) | controller-registered ordinary free API key; same existing account for REST and MCP | natural | [completed](../data/experiments/evaluations/alpha-mcp-prices-mirror-001-ds41-r1.json) | 2026-10-08T15:36:50.209167+00:00 | 1.18.35 / deepseek-flash / high | 207881 / 195456 / 7051 | 62.297901s | 0 | 0 |
| alpha-vantage / data-api | financial-prices-001 (v1) | controller-registered ordinary free API key; same existing account for REST and MCP | natural | [completed](../data/experiments/evaluations/alpha-rest-prices-mirror-001-ds41-r1.json) | 2026-10-08T15:35:30.920720+00:00 | 1.18.35 / deepseek-flash / high | 430683 / 405632 / 7379 | 69.943454s | unknown | 0 |
| alpha-vantage / hosted-mcp | financial-prices-001 (v1) | controller-registered ordinary free API key; same existing account for REST and MCP | natural | [not_completed](../data/experiments/evaluations/alpha-mcp-prices-001-ds41-r1.json) | 2026-10-08T14:22:41.046437+00:00 | 1.18.35 / deepseek-flash / high | unknown | 590.065117s | unknown | 0 |
| alpha-vantage / data-api | financial-prices-001 (v1) | controller-registered ordinary free API key; same existing account for REST and MCP | natural | [not_completed](../data/experiments/evaluations/alpha-rest-prices-001-ds41-r1.json) | 2026-10-08T14:12:41.161084+00:00 | 1.18.35 / deepseek-flash / high | unknown | 590.065048s | unknown | 0 |

**主持复核补充说明（原判定不变）：**

- [alpha-mcp-prices-001-ds41-r1](../data/experiments/evaluations/alpha-mcp-prices-001-ds41-r1.json)：主持复核补充，原独立验收判定不变：官方MCP已返回正确的21个交易日数据，约36秒完成取数；但CSV、走势图和最终答复均未交付。其后依赖安装消耗了剩余时间预算。本轮验证了该入口取数，未完成完整用户任务；不应将其概括为MCP或服务不可用。
- [alpha-rest-prices-001-ds41-r1](../data/experiments/evaluations/alpha-rest-prices-001-ds41-r1.json)：主持复核补充，原独立验收判定不变：指定服务取数及CSV已完成；用户要求的走势图和最终答复未交付。执行约590秒后超时，主要耗在缓慢的matplotlib下载与等待。原题不限定作图库，因此本次记录为执行策略与预算内交付失败，不代表Alpha Vantage无法提供行情。

<a id="web-search-data-financial-data"></a>

## 搜索与数据获取 / 金融数据（web-search-data/financial-data） · 接入测试

### financial-access-001 / v1

帮我把这个金融数据服务接好，确认能用指定方式查询数据，并保存后续调用需要的配置；如果接不通，说明卡在哪里。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| alpha-vantage / hosted-mcp | financial-access-001 (v1) | controller-registered ordinary free API key; same existing account for REST and MCP | natural | [completed](../data/experiments/evaluations/alpha-mcp-prices-mirror-access-ds41-r1.json) | 2026-10-08T15:29:43.509122+00:00 | 1.18.35 / deepseek-flash / high | 552500 / 525184 / 12067 | 184.674383s | unknown | 0 |
| alpha-vantage / data-api | financial-access-001 (v1) | controller-registered ordinary free API key; same existing account for REST and MCP | natural | [completed](../data/experiments/evaluations/alpha-rest-prices-mirror-access-ds41-r1.json) | 2026-10-08T15:28:08.583876+00:00 | 1.18.35 / deepseek-flash / high | 184198 / 168704 / 4121 | 32.632337s | 0 | 0 |
| alpha-vantage / hosted-mcp | financial-access-001 (v1) | controller-registered ordinary free API key; same existing account for REST and MCP | natural | [completed](../data/experiments/evaluations/alpha-mcp-prices-access-ds41-r1.json) | 2026-10-08T14:09:26.927480+00:00 | 1.18.35 / deepseek-flash / high | 565383 / 536448 / 11092 | 118.680959s | 0 | 0 |
| alpha-vantage / data-api | financial-access-001 (v1) | controller-registered ordinary free API key; same existing account for REST and MCP | natural | [completed](../data/experiments/evaluations/alpha-rest-prices-access-ds41-r1.json) | 2026-10-08T14:07:21.955843+00:00 | 1.18.35 / deepseek-flash / high | 105161 / 95616 / 4568 | 33.809312s | 0 | 0 |
| sec-edgar / data-api | financial-access-001 (v1) | none; contact identity only | natural | [completed](../data/experiments/evaluations/sec-edgar-access-ds41-r1.json) | 2026-10-08T12:14:13.175775+00:00 | 1.18.35 / deepseek-flash / high | 105820 / 97152 / 5675 | 40.119431s | 0 | 0 |
| alpha-vantage / data-api | financial-access-001 (v1) | controller-registered ordinary free API key | natural | [completed](../data/experiments/evaluations/alpha-vantage-access-ds41-r1.json) | 2026-10-08T12:14:13.175298+00:00 | 1.18.35 / deepseek-flash / high | 81815 / 74112 / 2516 | 24.074587s | 0 | 0 |
| frankfurter / data-api | financial-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/frankfurter-access-ds41-r1.json) | 2026-10-08T11:49:06.202214+00:00 | 1.18.35 / deepseek-flash / high | 110298 / 97024 / 2973 | 38.641535s | 0 | 0 |
| ecb-data / data-api | financial-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/ecb-data-access-ds41-r1.json) | 2026-10-08T11:49:06.201856+00:00 | 1.18.35 / deepseek-flash / high | 120041 / 106624 / 3254 | 29.506871s | unknown | 0 |
| capitol-exposed / data-api-keyless | financial-access-001 (v1) | none | natural | [not_completed](../data/experiments/evaluations/capitol-access-oc11835-r1.json) | 2026-10-08T07:24:16.929807+00:00 | 1.18.35 / glm-5.3-flash / high | 295856 / 269184 / 4643 | 169.698703s | 0 | unknown |
| bargo-congress / congress-api-keyless | financial-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/bargo-access-oc11835-r1.json) | 2026-10-08T07:24:13.769678+00:00 | 1.18.35 / glm-5.3-flash / high | 94365 / 74816 / 3151 | 121.069769s | 0 | 0 |
| capitol-exposed / data-api-keyless | financial-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-access.json) | 2026-09-15T09:14:32.838922+00:00 | 1.18.29 / glm-5.3-flash / high | 189737 / 172864 / 2746 | 138.671707s | 0 | 0 |
| bargo-congress / congress-api-keyless | financial-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/bargo-access.json) | 2026-09-15T09:07:26.717325+00:00 | 1.18.29 / glm-5.3-flash / high | 92193 / 73920 / 3609 | 157.266045s | 0 | 0 |
| tracefour / data-api-keyless | financial-access-001 (v1) | none | natural | [not_completed](../data/experiments/evaluations/tracefour-access.json) | 2026-09-15T09:07:26.569219+00:00 | 1.18.29 / glm-5.3-flash / high | 103555 / 86272 / 3755 | 153.41522s | 0 | 0 |
| frankfurter / data-api | financial-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/frankfurter-access.json) | 2026-09-15T07:06:04.074344+00:00 | 1.18.29 / glm-5.3-flash / high | 84240 / 72512 / 2596 | 115.282949s | 0 | 0 |
| ecb-data / data-api | financial-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/ecb-access.json) | 2026-09-15T07:06:04.069023+00:00 | 1.18.29 / glm-5.3-flash / high | 216483 / 199488 / 5383 | 216.897575s | 0 | 0 |

**主持复核补充说明（原判定不变）：**

- [capitol-access-oc11835-r1](../data/experiments/evaluations/capitol-access-oc11835-r1.json)：主持复核补充，原独立验收判定不变：接入功能已验证，真实数据查询及配置复用成功。未完成源于超出本轮接入阶段最多返回5条记录的测试约束：累计返回7条，且交付统计不完整。这不是服务只支持5条，也不是其免费额度耗尽。

<a id="web-search-data-geocoding"></a>

## 搜索与数据获取 / 地理编码（web-search-data/geocoding）

### geocoding-venue-001 / v1

我想在旅行地图上标记大英博物馆。请用指定服务把附件中的场馆地址转成可用坐标，用中文给出匹配地点名称、明确标注纬度和经度的 WGS84 十进制度坐标、服务实际返回的地址信息和数据来源，并说明这是场馆、入口还是更粗略的定位。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| photon / public-search-api | geocoding-venue-001 (v1) | none; official low-volume public route selected deliberately for one public-venue research task | natural | [completed](../data/experiments/evaluations/photon-geocoding-venue-001-ds41-r1.json) | 2026-10-08T15:24:18.918504+00:00 | 1.18.35 / deepseek-flash / high | 95519 / 86400 / 4760 | 69.526803s | 0 | 0 |

<a id="web-search-data-geocoding"></a>

## 搜索与数据获取 / 地理编码（web-search-data/geocoding） · 接入测试

### geocoding-access-001 / v1

帮我接通这个地理编码服务，通过指定方式做一次真实地点查询，确认能把地点或地址转成坐标，并保存后续查询需要的本地配置；说明接入步骤和实际阻碍。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| nominatim / public-search-api | geocoding-access-001 (v1) | none; official low-volume public route selected deliberately for one public-venue research task | natural | [invalid_run](../data/experiments/evaluations/nominatim-geocoding-access-ds41-r1.json) | 2026-10-08T15:16:36.665691+00:00 | 1.18.35 / deepseek-flash / high | unknown | 290.065141s | 0 | 0 |
| photon / public-search-api | geocoding-access-001 (v1) | none; official low-volume public route selected deliberately for one public-venue research task | natural | [completed](../data/experiments/evaluations/photon-geocoding-access-ds41-r1.json) | 2026-10-08T15:16:36.665425+00:00 | 1.18.35 / deepseek-flash / high | 248700 / 229248 / 4848 | 75.763506s | 0 | 0 |

<a id="web-search-data-weather-data"></a>

## 搜索与数据获取 / 天气数据（web-search-data/weather-data）

### weather-outing-001 / v1

我 10 月 10 日上午要去伦敦市中心散步，请用中文把当地时间 09:00–12:00 三个小时的预报气温和降水量整理成小表，标明单位、数据来源和查询时间（注明时区），并简要指出哪些时段预计有降水。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| met-norway / locationforecast-api | weather-outing-001 (v1) | none; official public read-only free noncommercial route | natural | [completed](../data/experiments/evaluations/met-norway-weather-outing-001-ds41-r1.json) | 2026-10-08T14:54:24.335797+00:00 | 1.18.35 / deepseek-flash / high | 111073 / 100096 / 4091 | 29.366903s | 0 | 0 |
| open-meteo / forecast-api | weather-outing-001 (v1) | none; official public read-only free noncommercial route | natural | [completed](../data/experiments/evaluations/open-meteo-weather-outing-001-ds41-r1.json) | 2026-10-08T14:54:22.604013+00:00 | 1.18.35 / deepseek-flash / high | 34038 / 26496 / 1464 | 13.786233s | 0 | 0 |

<a id="web-search-data-weather-data"></a>

## 搜索与数据获取 / 天气数据（web-search-data/weather-data） · 接入测试

### weather-access-001 / v1

帮我接通这个天气服务，通过指定方式做一次真实天气查询，确认能用，并保存后续查询需要的本地配置；说明完成的接入步骤和实际阻碍。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| met-norway / locationforecast-api | weather-access-001 (v1) | none; official public read-only free noncommercial route | natural | [completed](../data/experiments/evaluations/met-norway-weather-access-ds41-r1.json) | 2026-10-08T14:51:19.491028+00:00 | 1.18.35 / deepseek-flash / high | 109720 / 95360 / 2778 | 31.329883s | 0 | 0 |
| open-meteo / forecast-api | weather-access-001 (v1) | none; official public read-only free noncommercial route | natural | [completed](../data/experiments/evaluations/open-meteo-weather-access-ds41-r1.json) | 2026-10-08T14:51:19.490808+00:00 | 1.18.35 / deepseek-flash / high | 231327 / 213504 / 7130 | 44.047586s | 0 | 0 |

<a id="web-search-data-web-search"></a>

## 搜索与数据获取 / 网页搜索（web-search-data/web-search）

### web-search-001 / v2

我准备把 Python 应用升级到 3.13，请用中文简要查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并附上支持这些结论的官方页面链接。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| firecrawl / public-search-api | web-search-001 (v2) | none; documented anonymous public route | natural | [completed](../data/experiments/evaluations/firecrawl-search-001v2-ds41-r1.json) | 2026-10-08T14:38:35.814758+00:00 | 1.18.35 / deepseek-flash / high | 239035 / 200960 / 6207 | 58.998363s | 0 | 0 |
| exa / public-mcp | web-search-001 (v2) | none; documented anonymous public route | natural | [completed](../data/experiments/evaluations/exa-search-001v2-ds41-r1.json) | 2026-10-08T14:38:34.155742+00:00 | 1.18.35 / deepseek-flash / high | 177830 / 163968 / 5584 | 85.419932s | 0 | 0 |

### web-search-001 / v1

我准备把 Python 应用升级到 3.13，查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并给出官方依据

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| exa / public-mcp | web-search-001 (v1) | none | natural | [completed](../data/experiments/evaluations/exa-search-001-ds41-r1.json) | 2026-10-08T12:03:57.797870+00:00 | 1.18.35 / deepseek-flash / high | 222107 / 198784 / 8504 | 110.567806s | unknown | 0 |
| exa / search-api | web-search-001 (v1) | provided: EXA_API_KEY | legacy | [not_completed](../data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json) | 2026-09-07T11:29:52.610600+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | unknown | 602.017s | 0 | 0 |
| firecrawl / public-search-api | web-search-001 (v1) | none | legacy | [completed](../data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json) | 2026-09-07T11:29:51.792723+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 338090 / 295552 / 8728 | 362.944s | 0 | 0 |
| exa / public-mcp | web-search-001 (v1) | none | legacy | [completed](../data/experiments/evaluations/codex-20260907T112257.401366Z-exa.json) | 2026-09-07T11:22:57.413717+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 917915 / 847104 / 13629 | 522.486s | 0 | 0 |

<a id="web-search-data-web-search"></a>

## 搜索与数据获取 / 网页搜索（web-search-data/web-search） · 接入测试

### web-search-access-001 / v1

帮我接通这个搜索服务，通过指定方式做一次简单的真实网页搜索，确认能用，并保存后续搜索需要的本地配置；说明完成了哪些接入步骤，遇到阻碍也请说明。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| firecrawl / public-search-api | web-search-access-001 (v1) | none; documented anonymous public route | natural | [completed](../data/experiments/evaluations/firecrawl-searchv2-access-ds41-r1.json) | 2026-10-08T14:35:05.604890+00:00 | 1.18.35 / deepseek-flash / high | 104329 / 87040 / 2087 | 21.400023s | 0 | 0 |
| exa / public-mcp | web-search-access-001 (v1) | none; documented anonymous public route | natural | [completed](../data/experiments/evaluations/exa-searchv2-access-ds41-r1.json) | 2026-10-08T14:35:05.604712+00:00 | 1.18.35 / deepseek-flash / high | 288909 / 270976 / 5640 | 41.914642s | 0 | 0 |
| exa / public-mcp | web-search-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/exa-access-ds41-r1.json) | 2026-10-08T12:01:59.543536+00:00 | 1.18.35 / deepseek-flash / high | 199173 / 183680 / 5236 | 38.345252s | 0 | 0 |

<a id="productivity-storage-collaborative-tables"></a>

## 办公与协作 / 协作表格（productivity-storage/collaborative-tables） · 接入测试

### collaborative-tables-access-001 / v1

帮我通过指定方式接通这个在线表格服务，新建一个本轮专用的空测试空间，读取它确认可用，并保存后续创建任务表所需的配置；给我空间链接，说明接入步骤、人工门槛和免费限制。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| grist / hosted-mcp | collaborative-tables-access-001 (v1) | provided: existing Grist Personal account; new empty parent workspace prepared by controller | natural | [completed](../data/experiments/evaluations/grist-mcp-access-ds41-r1.json) | 2026-10-08T13:45:37.768748+00:00 | 1.18.35 / deepseek-flash / high | 350908 / 324352 / 6743 | 61.963463s | 0 | 1 |
| grist / rest-api | collaborative-tables-access-001 (v1) | provided: existing Grist Personal account; new empty parent workspace prepared by controller | natural | [completed](../data/experiments/evaluations/grist-rest-access-ds41-r1.json) | 2026-10-08T13:42:01.154679+00:00 | 1.18.35 / deepseek-flash / high | 106882 / 91904 / 4125 | 34.159175s | 0 | 0 |

<a id="web-search-data-financial-data-statements"></a>

## 搜索与数据获取 / 金融数据 / 公司财务数据（web-search-data/financial-data/statements）

### financial-statements-001 / v1

比较苹果和微软 2025 财年的营收、净利润和经营现金流，做成表格并附原始财报出处。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| alpha-vantage / data-api | financial-statements-001 (v1) | controller-registered ordinary free API key | natural | [completed](../data/experiments/evaluations/alpha-vantage-statements-001-ds41-r1.json) | 2026-10-08T12:25:33.613786+00:00 | 1.18.35 / deepseek-flash / high | 179589 / 168192 / 9052 | 77.721987s | 0 | 1 |
| sec-edgar / data-api | financial-statements-001 (v1) | none; contact identity only | natural | [completed](../data/experiments/evaluations/sec-edgar-statements-001-ds41-r1.json) | 2026-10-08T12:25:31.794208+00:00 | 1.18.35 / deepseek-flash / high | 92106 / 82560 / 4177 | 34.919235s | 0 | 0 |

<a id="web-search-data-financial-data-fx"></a>

## 搜索与数据获取 / 金融数据 / 汇率数据（web-search-data/financial-data/fx）

### financial-fx-001 / v1

把这三笔美元支出按发生当日的欧洲央行参考汇率折算成欧元，列出每笔金额和合计，并给出汇率出处。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| frankfurter / data-api | financial-fx-001 (v1) | none | natural | [completed](../data/experiments/evaluations/frankfurter-fx-001-ds41-r1.json) | 2026-10-08T11:50:53.149145+00:00 | 1.18.35 / deepseek-flash / high | 50178 / 40448 / 1659 | 22.572511s | 0 | 0 |
| ecb-data / data-api | financial-fx-001 (v1) | none | natural | [completed](../data/experiments/evaluations/ecb-data-fx-001-ds41-r1.json) | 2026-10-08T11:50:51.065816+00:00 | 1.18.35 / deepseek-flash / high | 56374 / 47488 / 1952 | 16.839879s | 0 | 0 |
| ecb-data / data-api | financial-fx-001 (v1) | none | natural | [completed](../data/experiments/evaluations/ecb-business.json) | 2026-09-15T07:15:18.031345+00:00 | 1.18.29 / glm-5.3-flash / high | 60837 / 56064 / 1994 | 81.215126s | 0 | 0 |
| frankfurter / data-api | financial-fx-001 (v1) | none | natural | [completed](../data/experiments/evaluations/frankfurter-business.json) | 2026-09-15T07:11:48.392690+00:00 | 1.18.29 / glm-5.3-flash / high | 51862 / 42880 / 2384 | 88.202808s | 0 | 0 |

<a id="web-search-data-financial-data-disclosures"></a>

## 搜索与数据获取 / 金融数据 / 交易披露（web-search-data/financial-data/disclosures）

### financial-disclosures-004 / v1

帮我核对这条待查说法：“Ed Case 本人在 2026 年 8 月 18 日主动买入了恰好 8,000 美元的苹果股票。”请逐项判断交易归属、日期、金额和交易性质，写出有依据的更正，并附原始申报出处。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| bargo-congress / congress-api-keyless | financial-disclosures-004 (v1) | none | natural | [not_completed](../data/experiments/evaluations/bargo-disclosures-004-oc11835-r1.json) | 2026-10-08T08:15:11.057749+00:00 | 1.18.35 / glm-5.3-flash / high | unknown | 890.066711s | 0 | unknown |
| capitol-exposed / data-api-keyless | financial-disclosures-004 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-004-900s-c10-r1.json) | 2026-09-15T13:30:44.951470+00:00 | 1.18.29 / glm-5.3-flash / high | 225048 / 204800 / 5872 | 193.388154s | 0 | unknown |
| capitol-exposed / data-api-keyless | financial-disclosures-004 (v1) | none | natural | [invalid_run](../data/experiments/evaluations/capitol-disclosures-004-r1.json) | 2026-09-15T12:38:23.929828+00:00 | 1.18.29 / glm-5.3-flash / high | 250971 / 232064 / 5116 | — | 0 | 0 |
| bargo-congress / congress-api-keyless | financial-disclosures-004 (v1) | none | natural | [not_completed](../data/experiments/evaluations/bargo-disclosures-004-r1.json) | 2026-09-15T12:38:21.712373+00:00 | 1.18.29 / glm-5.3-flash / high | unknown | 590.066135s | 0 | unknown |

### financial-disclosures-003 / v1

比较 Richard W. Allen 和 Ed Case 在 2026 年 8 月提交的股票披露：从交易发生到正式提交分别隔了多久？列出每笔的日期和天数，再按申报人汇总笔数、最短和最长间隔，并附原始申报出处。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| bargo-congress / congress-api-keyless | financial-disclosures-003 (v1) | none | natural | [completed](../data/experiments/evaluations/bargo-disclosures-003-oc11835-r1.json) | 2026-10-08T08:08:36.531431+00:00 | 1.18.35 / glm-5.3-flash / high | 593481 / 566528 / 10262 | 385.232457s | 0 | 0 |
| capitol-exposed / data-api-keyless | financial-disclosures-003 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-003-900s-c10-r1.json) | 2026-09-15T13:28:27.702197+00:00 | 1.18.29 / glm-5.3-flash / high | 202230 / 185088 / 4276 | 128.978342s | 0 | 0 |
| capitol-exposed / data-api-keyless | financial-disclosures-003 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-003-r1.json) | 2026-09-15T12:26:19.469293+00:00 | 1.18.29 / glm-5.3-flash / high | 260342 / 242048 / 5776 | 207.284676s | 0 | 0 |
| bargo-congress / congress-api-keyless | financial-disclosures-003 (v1) | none | natural | [completed](../data/experiments/evaluations/bargo-disclosures-003-r1.json) | 2026-09-15T12:26:17.426614+00:00 | 1.18.29 / glm-5.3-flash / high | 564454 / 530304 / 13956 | 400.656225s | 0 | 0 |

### financial-disclosures-002 / v1

我的关注名单里有 Richard W. Allen、Donald Sternoff Beyer Jr、Rob Bresnahan 和 Ed Case。查一下他们 2026 年 8 月提交的披露中有哪些苹果股票买卖，列出明细；没有匹配记录的人也请说明，并附原始申报出处。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| bargo-congress / congress-api-keyless | financial-disclosures-002 (v1) | none | natural | [not_completed](../data/experiments/evaluations/bargo-disclosures-002-oc11835-r1.json) | 2026-10-08T07:53:37.799002+00:00 | 1.18.35 / glm-5.3-flash / high | unknown | 890.067592s | 0 | 0 |
| capitol-exposed / data-api-keyless | financial-disclosures-002 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-002-900s-c10-r1.json) | 2026-09-15T13:21:48.603813+00:00 | 1.18.29 / glm-5.3-flash / high | 302171 / 273152 / 7480 | 393.147793s | 0 | 0 |
| capitol-exposed / data-api-keyless | financial-disclosures-002 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-002-r1.json) | 2026-09-15T12:09:04.533341+00:00 | 1.18.29 / glm-5.3-flash / high | 1103414 / 1052672 / 13130 | 516.740228s | 0 | 0 |
| bargo-congress / congress-api-keyless | financial-disclosures-002 (v1) | none | natural | [not_completed](../data/experiments/evaluations/bargo-disclosures-002-r1.json) | 2026-09-15T12:09:02.396160+00:00 | 1.18.29 / glm-5.3-flash / high | unknown | 590.067368s | 0 | 0 |

### financial-disclosures-001 / v1

帮我整理 Richard W. Allen 在 2026 年 8 月向美国众议院提交的股票买卖披露，列出股票、买卖方向、交易日期、提交日期和金额区间，并附原始申报出处。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| bargo-congress / congress-api-keyless | financial-disclosures-001 (v1) | none | natural | [completed](../data/experiments/evaluations/bargo-disclosures-001-oc11835-r1.json) | 2026-10-08T07:44:31.757729+00:00 | 1.18.35 / glm-5.3-flash / high | 762755 / 731776 / 15607 | 538.45171s | 0 | 0 |
| capitol-exposed / data-api-keyless | financial-disclosures-001 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-001-900s-c10-r1.json) | 2026-09-15T13:17:49.887185+00:00 | 1.18.29 / glm-5.3-flash / high | 158452 / 134272 / 4661 | 233.011992s | 0 | 0 |
| capitol-exposed / data-api-keyless | financial-disclosures-001 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-disclosures-001-r1.json) | 2026-09-15T11:52:43.643345+00:00 | 1.18.29 / glm-5.3-flash / high | 284404 / 216384 / 6563 | 262.354235s | 0 | 0 |
| bargo-congress / congress-api-keyless | financial-disclosures-001 (v1) | none | natural | [not_completed](../data/experiments/evaluations/bargo-disclosures-001-r1.json) | 2026-09-15T11:52:41.065341+00:00 | 1.18.29 / glm-5.3-flash / high | unknown | 590.067227s | 0 | 0 |
| capitol-exposed / data-api-keyless | financial-disclosures-001 (v1) | none | natural | [completed](../data/experiments/evaluations/capitol-business.json) | 2026-09-15T09:20:49.994872+00:00 | 1.18.29 / glm-5.3-flash / high | 316639 / 248576 / 5213 | 220.999401s | 0 | unknown |
| bargo-congress / congress-api-keyless | financial-disclosures-001 (v1) | none | natural | [completed](../data/experiments/evaluations/bargo-business.json) | 2026-09-15T09:15:16.890334+00:00 | 1.18.29 / glm-5.3-flash / high | 738160 / 702208 / 13547 | 525.761527s | 0 | 0 |

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

<a id="comparison-eb4cee33eee8"></a>

### database-atomic-import-001 v1

**neon / claimable-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · Preprovided existing authorized parent identity; executor creates one fresh empty logical database · 独立验收可参考同期 2 份同题答案

准备：Fresh independently passed access resources; controller then creates two matching synthetic initial tables in each new database. Same fields/constraints/baseline andtwoCSVfiles; no executor importer/code supplied. Current injected runner file hashes verified before each dispatch and saved inreceipt. Samebaseimage/TUNApip; Neon retains its own access-installedpsycopg2-binary2.9.13 underinstalled-tools, Turso no installedclient. Broad management/parentURL removed, old access verification data archived root-only; Neon SQL role stilltechnicallyprojectwide, only newtables authorized. RetentionauditSHA256 6889f9c6c62e5cf961116b1ce826490cfa88c62612305871c45d6de2468b449f. Identicalexec25requests600s/grade40requests300s/32000output/2GiB1CPU256pids;2providerstreams, service40operation/first403429stop rulesare instructions;modelrequest/timeceilings enforced. ExistingTursostarteraccount vs existingNeonClaimableparent/preprovidedidentity, sharedquota/lifetime, no newregistration. Rootseed+readonlybefore/after12readoperationsmax/provider are externalunmeteredpreparation/verification; executors allstopped before afterreads. Independentexactsynthetictruth, frozenpeeroutputs notverdicts, gradersnocredentials/noSQL/noimporterrerun. Grader mustbindactualsource/invocations/nativeerror/atomicpath plusunchangedschema/terminalrows, notterminalonly. One rejected andonecorrectedbatch perprovider, nosingle-protocol/engine-superiority orACID/crash/concurrency/performanceclaim.

- [neon-atomic-import-001-ds41-r1](../data/experiments/evaluations/neon-atomic-import-001-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 被测业务费用为 Neon 数据库侧；本次运行在总控预建的 Claimable 免费项目内的小逻辑库上只读元数据、向两张测试表插入少量记录，无付款或绑卡。模型/运行器费用不由本字段计。; execution/artifacts/ENVIRONMENT.md

  结论与限制：同一交付的 importer.py 经指定 Neon 服务实际运行两次：错误样本在单事务内被数据库以重复主键拒绝（UniqueViolation/23505），整批回滚、无已提交新增记录，reject_case 仅剩原有 100/已有书目；更正样本 3 行全部提交到 accept_case，原有 100 不变。总控独立前后读回显示两表终态、结构与主键约束与预期一致，两表互不覆盖，全程仅 INSERT/SELECT，无 UPDATE/DELETE/DDL 或提交后补偿。导入器、用法、结果交付齐全，凭据与代码分离，答案不含密钥。仅就观察到的两个小样本与其事务路径作结论。

**turso / platform-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · Preprovided existing authorized parent identity; executor creates one fresh empty logical database · 独立验收可参考同期 2 份同题答案

准备：Fresh independently passed access resources; controller then creates two matching synthetic initial tables in each new database. Same fields/constraints/baseline andtwoCSVfiles; no executor importer/code supplied. Current injected runner file hashes verified before each dispatch and saved inreceipt. Samebaseimage/TUNApip; Neon retains its own access-installedpsycopg2-binary2.9.13 underinstalled-tools, Turso no installedclient. Broad management/parentURL removed, old access verification data archived root-only; Neon SQL role stilltechnicallyprojectwide, only newtables authorized. RetentionauditSHA256 6889f9c6c62e5cf961116b1ce826490cfa88c62612305871c45d6de2468b449f. Identicalexec25requests600s/grade40requests300s/32000output/2GiB1CPU256pids;2providerstreams, service40operation/first403429stop rulesare instructions;modelrequest/timeceilings enforced. ExistingTursostarteraccount vs existingNeonClaimableparent/preprovidedidentity, sharedquota/lifetime, no newregistration. Rootseed+readonlybefore/after12readoperationsmax/provider are externalunmeteredpreparation/verification; executors allstopped before afterreads. Independentexactsynthetictruth, frozenpeeroutputs notverdicts, gradersnocredentials/noSQL/noimporterrerun. Grader mustbindactualsource/invocations/nativeerror/atomicpath plusunchangedschema/terminalrows, notterminalonly. One rejected andonecorrectedbatch perprovider, nosingle-protocol/engine-superiority orACID/crash/concurrency/performanceclaim.

- [turso-atomic-import-001-ds41-r1](../data/experiments/evaluations/turso-atomic-import-001-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 无账单回执；依据平台账户快照与本次实际用量判定，未按量估算。; controller-verification/resource-limits.json

  结论与限制：在指定 Turso/libSQL 新库上，用同一交付导入器真实运行两个样本：错误文件由数据库以重复主键拒绝（SQLITE_CONSTRAINT: UNIQUE constraint failed: reject_case.book_id）并在未提交事务内整批回滚，reject_case 终态仅剩原有 100/已有书目；更正文件 3 行全部提交到 accept_case，原有 100 不变，两表互不覆盖。执行路径为单个 db.transaction("write") + COMMIT/ROLLBACK，全部命令仅 SELECT/INSERT，无 UPDATE/DELETE/DDL/补偿删改；结构与约束前后一致。交付导入器、用法与两次结果与实际执行相符，凭据与源码分离且答复无密钥。错误样本重复键拒绝为预期结果，服务本身可用。

<a id="comparison-7a86e94d64f8"></a>

### database-access-001 v1

**neon / claimable-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · Preprovided existing authorized parent identity; executor creates one fresh empty logical database

准备：Fresh containers, current injected runner source hashes, same image/OpenCode1.18.35 DeepSeekFlash/high, TUNA pip index and empty cache. Existing Turso personal starter management account and existing authorized Neon Claimable parent credentials provided; no registration measured. Agent creates and queries one new empty logical database; earlier user/test databases untouched. New Neondatabase shares existing parent100MB/1GB and2026-10-11T12:36:21.796Zexpiry; no new parent/identity. New cohort not pooled with anonymous-parent-creation access. Executor25modelrequests/300s andgrader40/300s,20serviceoperations instructed,first403/429stop,2parallelproviderstreams. Controller entitlement preflight and runtime preparation are external setup, costs not separately measured. Injected file hashes in private preparation and runtime receipts.

- [neon-atomic-access-ds41-r1](../data/experiments/evaluations/neon-atomic-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: 无付费回执或账单；父项目与免费额度由总控预先提供，本次未捕获 Neon 的计价规则或用量计费证据。执行答复依据环境说明称免费，但材料未提供可独立核验的免费规则来源，故保留 unknown。已观察的限额为项目到期 2026-10-11T12:36:21.796Z、100MB 存储/1GB 传输/72h 由项目内全部逻辑库共享。

  结论与限制：已在总控预提供的 Neon 父项目内，用授权管理连接真实新建单一逻辑空库 [SERVICE_SECRET]，并通过标准 Postgres 驱动完成一次只读连通查询（返回新库与 [SERVICE_SECRET]，用户表数=0），未建业务表、未写业务行；配置保存到指定持久目录且答复只给路径、未泄露凭据；账号来源、接入步骤、人工门槛与到期/限额如实说明。费用无回执或可核计价规则，保留 unknown。

**turso / platform-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · Preprovided existing authorized parent identity; executor creates one fresh empty logical database

准备：Fresh containers, current injected runner source hashes, same image/OpenCode1.18.35 DeepSeekFlash/high, TUNA pip index and empty cache. Existing Turso personal starter management account and existing authorized Neon Claimable parent credentials provided; no registration measured. Agent creates and queries one new empty logical database; earlier user/test databases untouched. New Neondatabase shares existing parent100MB/1GB and2026-10-11T12:36:21.796Zexpiry; no new parent/identity. New cohort not pooled with anonymous-parent-creation access. Executor25modelrequests/300s andgrader40/300s,20serviceoperations instructed,first403/429stop,2parallelproviderstreams. Controller entitlement preflight and runtime preparation are external setup, costs not separately measured. Injected file hashes in private preparation and runtime receipts.

- [turso-atomic-access-ds41-r1](../data/experiments/evaluations/turso-atomic-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Turso 账户处于 Free/免费计划，$0/月且 overages=false，支付方式状态未单独核实；本轮仅新增 1 个空库并使用 1 次只读查询，用量远低于 Free 额度（100 库/5GB），未产生计费或超限。token 无到期、库无计划删除。; https://turso.tech/pricing (Free plan $0/month, 100 databases, 5GB storage; fetched 2026-10-08); frozen-execution/ENVIRONMENT.md (controller snapshot: starter plan price 0, overages=false, 1 existing DB, storage 36864 bytes, no blocked reads/writes)

  结论与限制：本轮通过指定入口 Turso Platform API v1 接入已提供的 Turso 账号（非本轮注册），新建恰好一个空库 [SERVICE_SECRET]（HTTP 200，返回服务生成的 DbId/Host），并用官方 SQL HTTP /v2/pipeline 执行一次真实只读查询 SELECT 1/current_timestamp，HTTP 200、ok=1、rows_written=0。连接配置与库标识已写入指定持久目录 /home/node/service-tools/（credentials.json、service-config.json，权限 600），答复只给配置路径、未泄露凭据；未创建业务表/写业务数据、未访问既有库；预算管理请求 4 次 + SQL 提交 1 次（≤20）、新库 1 个（≤1），无 403/429。账号来源、人工门槛与免费/到期限制均已如实说明。费用为 Turso Free 计划 $0 且账户 overages=false，本次用量在免费额度内。

<a id="comparison-cb6f4b024594"></a>

### collaborative-tables-shared-expenses-001 v1

**grist / hosted-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · provided: existing Grist Personal account; new empty parent workspace prepared by controller

准备：Shared-expenses formula followup on same previously verified Grist REST/MCP runtimes and existing Personal account. Two new empty parent workspaces and empty documents prepared/read-verified by controller; no business schema/data/formulas/helper supplied, preparation overhead unmetered. Prior task resource pointers removed and archived root-only; generic retained auth/route setup only, no installed dependencies. Adapter archives previous home/workspace/tmp before new session. Retention audit SHA256 0c63da5f9d52d12497339feb10a14b81143a3fb34a15ed70ad232dea5afdc928. Same image/OpenCode1.18.35/DeepSeekV4.1Flash high,2GiB/1CPU/pids256; execution25modelrequests/600s, grading40/300s,32000outputcap. Maximum40 caller-visible service operations per route; stop at first403/429/402/paywall or2consecutive connection failures. These service stop rules are instructions, model request limit is enforced by proxy. REST then MCP serial on shared quota; remaining monthly quota unknown. After both executions collected, controller independently snapshots each document, then applies pre-frozen1append+1amountcorrection only to source ledger columns when mapping safely established; never formulas/schema/summary. Initial/append/correction snapshots and independent arithmetic reference supplied to separate graders without credentials or peer verdicts. Controller verification writes and reads are separate overhead, not part of executor cost. No peer-results group for same-provider routes. Final test state retained per input. Single synthetic two-person50/50 ledger per route, same Grist engine; not multiuser-concurrency/accounting-advice/general reliability or protocol ranking.

- [grist-mcp-shared-expenses-001-ds41-r1](../data/experiments/evaluations/grist-mcp-shared-expenses-001-ds41-r1.json)：模型费用 $0.03；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Grist 免费 Personal 计划，本次仅用免费额度，未付费、未绑卡、未开启超额。; https://support.getgrist.com/limits/; https://support.getgrist.com/limits/; public-review/verification.json — unchanged actual personalFree entitlement from frozen controller initial read; remaining month quota unknown

  结论与限制：执行者通过指定入口（Grist 官方托管 MCP）在本轮专属新文档建立了真实在线账本：独立初态回执确认六笔明细逐条与输入一致，服务端自动汇总（总支出2400.00、林青已付2095.60、周舟已付304.40、各应分摊1200.00、周舟需补给林青895.60）与初次答复及独立基准一致，答复给出私人链接并说明在“支出明细”表继续记账。执行者停止后，总控仅追加一笔、再修正一笔金额，服务端汇总分别自动重算为 2442.40/874.40 与 2422.40/864.40，公式与结构未变，证明汇总由明细持续计算。资源在免费 Personal 额度内，未新建文档、未分享/邀请/通知/支付/转账。

**grist / rest-api** — 0 完成 / 1 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · provided: existing Grist Personal account; new empty parent workspace prepared by controller

准备：Shared-expenses formula followup on same previously verified Grist REST/MCP runtimes and existing Personal account. Two new empty parent workspaces and empty documents prepared/read-verified by controller; no business schema/data/formulas/helper supplied, preparation overhead unmetered. Prior task resource pointers removed and archived root-only; generic retained auth/route setup only, no installed dependencies. Adapter archives previous home/workspace/tmp before new session. Retention audit SHA256 0c63da5f9d52d12497339feb10a14b81143a3fb34a15ed70ad232dea5afdc928. Same image/OpenCode1.18.35/DeepSeekV4.1Flash high,2GiB/1CPU/pids256; execution25modelrequests/600s, grading40/300s,32000outputcap. Maximum40 caller-visible service operations per route; stop at first403/429/402/paywall or2consecutive connection failures. These service stop rules are instructions, model request limit is enforced by proxy. REST then MCP serial on shared quota; remaining monthly quota unknown. After both executions collected, controller independently snapshots each document, then applies pre-frozen1append+1amountcorrection only to source ledger columns when mapping safely established; never formulas/schema/summary. Initial/append/correction snapshots and independent arithmetic reference supplied to separate graders without credentials or peer verdicts. Controller verification writes and reads are separate overhead, not part of executor cost. No peer-results group for same-provider routes. Final test state retained per input. Single synthetic two-person50/50 ledger per route, same Grist engine; not multiuser-concurrency/accounting-advice/general reliability or protocol ranking.

- [grist-rest-shared-expenses-001-ds41-r1](../data/experiments/evaluations/grist-rest-shared-expenses-001-ds41-r1.json)：模型费用 —；Per-request usage capture is incomplete. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；confirmed_free: 仅使用授权 Grist Personal 免费账户；无付款回执。; controller-verification/initial.json; frozen-execution/ENVIRONMENT.md; https://support.getgrist.com/limits/; public-review/verification.json — unchanged actual personalFree entitlement from frozen controller initial read; remaining month quota unknown

  结论与限制：服务侧账本本身正确且可自动更新：执行者经指定 Grist REST 入口在总控提供的本轮空文档中建立了 Expenses/Settlement 两表并录入六笔明细，独立远端读回初态汇总（总支出 2400.00、每人应分摊 1200.00、林青已付 2095.60、周舟已付 304.40、周舟补给林青 895.60）与输入及冻结参考一致；总控在文档中追加一笔、修正一笔金额后，服务端汇总分别自动变为 2442.40/1221.20/2095.60/346.80/874.40 与 2422.40/1211.20/2075.60/346.80/864.40，与参考一致且公式未变。但执行者没有向用户交付要求的答复：最终产物 execution/answer.md 只有 8 行过程叙述，不含私人账本链接、不含各自已付/应分摊/补差方向与金额、也不含继续记账位置说明；执行回执 exit_code=1，会话最后事件为运行器返回的模型请求预算耗尽（403，25/25 次用尽），执行在“准备核对最终值”前中止。按冻结标准，真实在线账本与完整用户答复分别判定，本次服务计算正确但完整用户交付缺失。

<a id="comparison-c49d8e01e18c"></a>

### web-extraction-scanned-table-001 v1

**firecrawl / public-scrape-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; anonymous public extraction routes, no account/email/token/payment supplied · 独立验收可参考同期 2 份同题答案

准备：New scanned/mixed PDF business follow-up after independently completed anonymous PDF access on the same two owned runtimes. Prior native-PDF runs and original access remain immutable; no new access sample. Exact same image,2GiB/1CPU/pids256,pipTUNA, execution25requests/600s, grading40/300s,32000outputtokens/request. Retained config byte-identical to prior audited generic setup; no installed dependencies or query material in retained paths. Owned runtimes resumed with only baseline sleep/inspection processes; adapter archives previous home/workspace/tmp before each fresh session. Retention audit SHA256 0ba61770d71e418cc9550b8c11e3d497cb89ae822a969cb5fe1f4faf77493213. Source PDF, page render, and visually transcribed numeric reference frozen by independent task-design role before queries; controller independently checked all selected values before dispatch. Text-only DeepSeek grader uses that frozen readable reference and actual candidate evidence; no claim that it visually read source images. Controller/reference preparation overhead unmetered. Maximum2 extraction calls per service (including retries), first403/429/402 stop,2consecutive connection failures stop; anonymous remaining quotas unknown. Same original URL and user request; no pre-cropped PDF or answer/helper delivered to executors. Business peers sealed before separate grading with no peer verdicts. Single small scanned-table sample, not general OCR reliability or regulatory advice.

- [firecrawl-pdf-scanned-table-001-ds41-r1](../data/experiments/evaluations/firecrawl-pdf-scanned-table-001-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: Controller conservatively preserves unknown: original grader labeled confirmed_free but explicitly left service_cost_usd null and said the amount was unknown. Original independent assessment/hash retained; this publication does not infer zero.; https://docs.firecrawl.dev/rate-limits

  结论与限制：指定匿名入口 https://api.firecrawl.dev/v2/scrape 对原 TTB Table_4.pdf 实际返回目标表正文（HTTP 200, success=true, sourceURL 为原 URL, numPages 2/totalPages 21），执行者据此生成 UTF-8 CSV，11 行、三列列名符合 input.md，Proof 1.0–2.0 升序含两端，33 个数值与冻结独立参考逐值一致并保留原表精度；答复给出文件位置与官方来源链接。仅用 1 次抽取调用（限 2 次），未直连下载/本地解析/他源补齐。

**exa / public-mcp** — 0 完成 / 1 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; anonymous public extraction routes, no account/email/token/payment supplied · 独立验收可参考同期 2 份同题答案

准备：New scanned/mixed PDF business follow-up after independently completed anonymous PDF access on the same two owned runtimes. Prior native-PDF runs and original access remain immutable; no new access sample. Exact same image,2GiB/1CPU/pids256,pipTUNA, execution25requests/600s, grading40/300s,32000outputtokens/request. Retained config byte-identical to prior audited generic setup; no installed dependencies or query material in retained paths. Owned runtimes resumed with only baseline sleep/inspection processes; adapter archives previous home/workspace/tmp before each fresh session. Retention audit SHA256 0ba61770d71e418cc9550b8c11e3d497cb89ae822a969cb5fe1f4faf77493213. Source PDF, page render, and visually transcribed numeric reference frozen by independent task-design role before queries; controller independently checked all selected values before dispatch. Text-only DeepSeek grader uses that frozen readable reference and actual candidate evidence; no claim that it visually read source images. Controller/reference preparation overhead unmetered. Maximum2 extraction calls per service (including retries), first403/429/402 stop,2consecutive connection failures stop; anonymous remaining quotas unknown. Same original URL and user request; no pre-cropped PDF or answer/helper delivered to executors. Business peers sealed before separate grading with no peer verdicts. Single small scanned-table sample, not general OCR reliability or regulatory advice.

- [exa-pdf-scanned-table-001-ds41-r1](../data/experiments/evaluations/exa-pdf-scanned-table-001-ds41-r1.json)：模型费用 $0.06；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 匿名免费规则来自冻结官方文档；本次调用确为 keyless 匿名且在免费限流范围内，未观察到计费字段。匿名额度余量未知，但不影响本次免费适用结论。金额按 0 计。; https://exa.ai/docs/reference/exa-mcp

  结论与限制：用户委托的 11 行 CSV 未交付：指定服务 web_fetch_exa 对原 URL 两次返回同一 12017 字符劣质 OCR 正文（sha256 f29f0df5…），不含物理第2页/印刷532 左半表 Proof 1.0–2.0（Proof 标签最小 96.0，数值范围 0.03175–190.9，无 0.0005–0.003 区间值），因此未产生目标表文字；交付 CSV 仅表头，最终答复 execution/answer.md 仅为过程叙述、无文件位置与官方来源。另有执行违规：首次 MCP initialize 返回 HTTP 403（Cloudflare 1010 browser_signature_banned），ENVIRONMENT.md 要求首次 403 即停止，执行者却循环探测 User-Agent 并改 UA 为 Chrome 后继续初始化与提取，故两次提取发生在强制停止之后，只能记录“换 UA 重试返回了文本”，不能支撑合规的服务比较结论。该 403 属该入口对默认客户端的路由/环境条件，本次失败由“服务返回内容不含目标段”与“执行者违反停止规则”共同导致，不据此断言服务普遍不支持 OCR/PDF，也不归为环境失效。模型请求 25/25 耗尽、exit_code=1，时间约 3 分 13 秒（未超 600 秒）；提取调用 2 次（≤2，单一 URL）合规。

<a id="comparison-0f505e0eb8fb"></a>

### qr-codes-travel-link-001 v1

**goqr / public-qr-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; public static QR APIs, no account/key/email/payment supplied · 独立验收可参考同期 2 份同题答案

准备：Same frozen task/model/budget. Two public static QR APIs with no account and no target destination visit. Up to2services concurrent, eachstage4generationcalls includingretry,>=2sec, first403/429stop. Service request limits are instructions, model/output/time caps enforced. Same baseimage2GiB/1CPU/pids256,pipTUNA/emptycache; no preinstalled executorclient. Exec25requests/access300s/business600s;grader40/300s;32000outputtokens/request. Access genericconfig/installeddependencies audited and kept, oldtaskimages/queries archived and ownedexecutor restarted before fresh businesssession. Separate graders have read-only offline ZXing3.1.1/Pillow12.3.0/NumPy2.3.5 and neutralfixture-verified generic image inspector; no decoder/helper/reference supplied to executors. Controller directly views exact hashed collectedPNG before grading and supplies factual visual observations; DeepSeek grader has no declared image input and independently verifies decoded bytes/pixels/provenance using offline tools. Controller visual inspection is disclosed separate overhead, not a claimed model-vision benchmark. Reference is original input bytes, no canonicalbitmap. Businesspeers sealedbeforegrading with no peerverdicts. Fourmodulemargin is only observation, not required; no DPI/mask/ECC/PNGmode restriction or realprinter/phone assurance. Officialfee/terms snapshots grader-only; goQRToS body missing, QuickChart retention7vs30days conflict explicit; no complete legal-reviewclaim. Rawtranscripts private; reviewedminimalfacts and requestedpublicURLimage may be published. Official source manifest SHA256 898dcf4ba868d3259742f29892fc95bf83f06c05b9b19767e8611412d4996ecf. Retention audit SHA256 5aa551a6989858d3f5ddaebc8740f3372738ba2132b963b11b3b3476d8a59322.

- [goqr-qr-travel-link-001-ds41-r1](../data/experiments/evaluations/goqr-qr-travel-link-001-ds41-r1.json)：模型费用 $0.0059；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: goQR.me 官方主页明确声明其创建的二维码完全免费（含商业与印刷用途），并鼓励推荐/捐赠以维持这项免费服务；本次使用其公开静态接口 api.qrserver.com 匿名调用，无账号/Key/邮箱/支付，HTTP 200 取回图片，未见任何付费、订阅或额度耗尽。免费规则适用于本次运行。; official-route-sources/goqr-home.html

  结论与限制：本次执行通过指定服务 goQR.me / QR Server（https://api.qrserver.com/v1/create-qr-code/）在业务阶段发出一次匿名 GET，HTTP 200 直接取回 1190 字节图片并保存为 PNG；采集的交付物 execution/artifacts/zion-travel-guide-qr.png（sha256 bc3ac0cc…4960a，1190 字节）与响应一致，独立离线工具确认其为 600×600、格式 PNG、全不透明、全灰度、含黑白像素，且解码出唯一 QR，raw bytes 逐字等于冻结输入 URL；总控对同一 sha 图片的可见观察记为白底黑码、仅一个二维码、无文字/logo。所有可见要求均有证据满足，答复给出真实文件位置。

**quickchart / public-qr-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; public static QR APIs, no account/key/email/payment supplied · 独立验收可参考同期 2 份同题答案

准备：Same frozen task/model/budget. Two public static QR APIs with no account and no target destination visit. Up to2services concurrent, eachstage4generationcalls includingretry,>=2sec, first403/429stop. Service request limits are instructions, model/output/time caps enforced. Same baseimage2GiB/1CPU/pids256,pipTUNA/emptycache; no preinstalled executorclient. Exec25requests/access300s/business600s;grader40/300s;32000outputtokens/request. Access genericconfig/installeddependencies audited and kept, oldtaskimages/queries archived and ownedexecutor restarted before fresh businesssession. Separate graders have read-only offline ZXing3.1.1/Pillow12.3.0/NumPy2.3.5 and neutralfixture-verified generic image inspector; no decoder/helper/reference supplied to executors. Controller directly views exact hashed collectedPNG before grading and supplies factual visual observations; DeepSeek grader has no declared image input and independently verifies decoded bytes/pixels/provenance using offline tools. Controller visual inspection is disclosed separate overhead, not a claimed model-vision benchmark. Reference is original input bytes, no canonicalbitmap. Businesspeers sealedbeforegrading with no peerverdicts. Fourmodulemargin is only observation, not required; no DPI/mask/ECC/PNGmode restriction or realprinter/phone assurance. Officialfee/terms snapshots grader-only; goQRToS body missing, QuickChart retention7vs30days conflict explicit; no complete legal-reviewclaim. Rawtranscripts private; reviewedminimalfacts and requestedpublicURLimage may be published. Official source manifest SHA256 898dcf4ba868d3259742f29892fc95bf83f06c05b9b19767e8611412d4996ecf. Retention audit SHA256 5aa551a6989858d3f5ddaebc8740f3372738ba2132b963b11b3b3476d8a59322.

- [quickchart-qr-travel-link-001-ds41-r1](../data/experiments/evaluations/quickchart-qr-travel-link-001-ds41-r1.json)：模型费用 $0.0084；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 指定公开静态入口无计费凭据，本次用量在文档所述免费社区配额内，无付费或超额；无真实账单回执，金额为 0（免费规则适用）。; official-route-sources/quickchart-qr-overview.html: "We render QR codes and chart images free of charge."; official-route-sources/quickchart-qr-pricing.html: Community $0/month，1,000 QR codes per month，60 QR codes per minute rate limit

  结论与限制：QuickChart 公开静态 QR API 实际生成并交付了可离线解码的 PNG：POST https://quickchart.io/qr 返回 HTTP 200 / image/png / 5044 字节，采集副本 zion_qr.png 与该回执字节一致（sha256 ba1ede…3546）。独立离线 ZXing 解码 raw bytes_hex 与可见原始 URL 逐字相同，尺寸 600×600、不透明、灰度、黑码白底，仅一个二维码，无文字/logo；答复指出真实文件位置。

<a id="comparison-1c64f31025f0"></a>

### qr-codes-access-001 v1

**goqr / public-qr-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; public static QR APIs, no account/key/email/payment supplied

准备：Same frozen task/model/budget. Two public static QR APIs with no account and no target destination visit. Up to2services concurrent, eachstage4generationcalls includingretry,>=2sec, first403/429stop. Service request limits are instructions, model/output/time caps enforced. Same baseimage2GiB/1CPU/pids256,pipTUNA/emptycache; no preinstalled executorclient. Exec25requests/access300s/business600s;grader40/300s;32000outputtokens/request. Access genericconfig/installeddependencies audited and kept, oldtaskimages/queries archived and ownedexecutor restarted before fresh businesssession. Separate graders have read-only offline ZXing3.1.1/Pillow12.3.0/NumPy2.3.5 and neutralfixture-verified generic image inspector; no decoder/helper/reference supplied to executors. Controller directly views exact hashed collectedPNG before grading and supplies factual visual observations; DeepSeek grader has no declared image input and independently verifies decoded bytes/pixels/provenance using offline tools. Controller visual inspection is disclosed separate overhead, not a claimed model-vision benchmark. Reference is original input bytes, no canonicalbitmap. Businesspeers sealedbeforegrading with no peerverdicts. Fourmodulemargin is only observation, not required; no DPI/mask/ECC/PNGmode restriction or realprinter/phone assurance. Officialfee/terms snapshots grader-only; goQRToS body missing, QuickChart retention7vs30days conflict explicit; no complete legal-reviewclaim. Rawtranscripts private; reviewedminimalfacts and requestedpublicURLimage may be published. Official source manifest SHA256 898dcf4ba868d3259742f29892fc95bf83f06c05b9b19767e8611412d4996ecf.

- [goqr-qr-access-ds41-r1](../data/experiments/evaluations/goqr-qr-access-ds41-r1.json)：模型费用 $0.0078；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: 无计费回执。goqr.me 官网首页称 goQR.me 生成的二维码免费（含商业用途），但冻结的官方来源中 API 专用 ToS 正文缺失、剩余匿名额度未定，无法确认该免费规则对 api.qrserver.com 的本次适用性，故保留 unknown；成功响应与未列费率不作为免费依据。; official-route-sources/goqr-home.html; official-route-sources/goqr-api-terms.html

  结论与限制：指定入口 api.qrserver.com 的一次匿名 GET 生成请求返回 HTTP 200 image/png，响应体 474 字节被保存为 test-qr.png；与视觉回执同 sha256 的该文件经独立离线工具确认为 PNG 300x300，唯一二维码解码 bytes_hex 与测试网址完全一致；持久目录保留可复用的通用端点为 none 的配置；未发生人工介入或秘密泄露。

**quickchart / public-qr-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; public static QR APIs, no account/key/email/payment supplied

准备：Same frozen task/model/budget. Two public static QR APIs with no account and no target destination visit. Up to2services concurrent, eachstage4generationcalls includingretry,>=2sec, first403/429stop. Service request limits are instructions, model/output/time caps enforced. Same baseimage2GiB/1CPU/pids256,pipTUNA/emptycache; no preinstalled executorclient. Exec25requests/access300s/business600s;grader40/300s;32000outputtokens/request. Access genericconfig/installeddependencies audited and kept, oldtaskimages/queries archived and ownedexecutor restarted before fresh businesssession. Separate graders have read-only offline ZXing3.1.1/Pillow12.3.0/NumPy2.3.5 and neutralfixture-verified generic image inspector; no decoder/helper/reference supplied to executors. Controller directly views exact hashed collectedPNG before grading and supplies factual visual observations; DeepSeek grader has no declared image input and independently verifies decoded bytes/pixels/provenance using offline tools. Controller visual inspection is disclosed separate overhead, not a claimed model-vision benchmark. Reference is original input bytes, no canonicalbitmap. Businesspeers sealedbeforegrading with no peerverdicts. Fourmodulemargin is only observation, not required; no DPI/mask/ECC/PNGmode restriction or realprinter/phone assurance. Officialfee/terms snapshots grader-only; goQRToS body missing, QuickChart retention7vs30days conflict explicit; no complete legal-reviewclaim. Rawtranscripts private; reviewedminimalfacts and requestedpublicURLimage may be published. Official source manifest SHA256 898dcf4ba868d3259742f29892fc95bf83f06c05b9b19767e8611412d4996ecf.

- [quickchart-qr-access-ds41-r1](../data/experiments/evaluations/quickchart-qr-access-ds41-r1.json)：模型费用 $0.0082；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: No payment receipt exists; classified by the service's published free rule plus this run's observed applicability.; https://quickchart.io/pricing/qr/; https://quickchart.io/qr-code-api/; execution/artifacts/qr-example.png

  结论与限制：QuickChart's designated anonymous static endpoint (GET https://quickchart.io/qr) was actually called with the frozen User-Agent; it returned HTTP 200 image/png which was saved as qr-example.png in the task workspace. Offline ZXing/Pillow inspection of the retained file confirms a valid PNG (300x300, opaque, black-on-white) whose QR raw bytes decode exactly to the input URL https://example.com/. General reusable config was retained at /home/node/service-tools/service-config.json (no secrets, no test URL) and the answer truthfully discloses that the service needs no account/key/email/payment, self-service, no human steps, and the static-QR free scope. No barrier, no leaked secret, within request limits (1 generation request).

<a id="comparison-f0300fd67f1a"></a>

### route-planning-bridge-001 v1

**osrm / public-route-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; anonymous FOSSGIS public demos, no account/token/email/payment supplied · 独立验收可参考同期 2 份同题答案

准备：Same frozen task/model/budget, public OSRM vs Valhalla engines hosted by FOSSGIS using OSM; not independent providers or map truth. All candidate executions serial; 4routecalls per service per stage,>=2s,stop first403/429 or two consecutive connection failures. Service limits are instructions; model/output/time caps enforced. Explicit truthful UA/project URL and Valhalla X-Client-Id. No account/key/paid fallback/prewritten client. Same image2GiB/1CPU/pids256,pipTUNA/emptycache. Access then audited generic configuration/installed dependencies retained; restart owned executor before fresh businesshome/session/workspace. Exec25requests/access300s/business600s;grading40/300s;output32000/request. Independent roads/reference and official operator rules frozen before candidate queries and grader-only; business peers sealed before separate grading without peer verdicts. No grader candidateAPI calls. Official summary allows low-volume noncommercial use; full linked German policy was blocked and not read, no blanket complete terms-review claim. AttributionOSM/FOSSGIS andfix-maplink accompany public facts. Official source manifest SHA256 c316e7244f96b20dc106f32047f9a055d1684b6c52a4fc0699e8d4e28dd80a05. Retention audit SHA256 83fc21262ffafb4959ab6f50b7c6161fb4da0beb7e96adb54d87ddff0b11d200.

- [osrm-routing-bridge-001-ds41-r1](../data/experiments/evaluations/osrm-routing-bridge-001-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: Controller source review could not confirm an explicit hosted-demo zero-fee rule in the frozen official sources. Donation-funded, public, no-registration use and open-source/map licences do not establish price. Original independent confirmed_free assessment is preserved privately with its hash and unchanged task verdict/reason/checks; publication conservatively retains unknown rather than inferring zero. No additional model review or service query.; official-route-sources/operator-services.source; official-route-sources/osrm-demo.source; execution/artifacts/out/osrm_route_raw.json (response to the single anonymous request)

  结论与限制：本次执行真实调用冻结的 FOSSGIS OSRM 公共驾驶入口 router.project-osrm.org/route/v1/driving，按 A(南)→B(北)、小汽车模式取得路线（HTTP 200，code=Ok）。交付的 GeoJSON/GPX 与原始响应几何一致、可解析且连续有序；独立测起点距 A 0.62 m、终点距 B 0.00 m，对官方道路参考中心线 densify 最大偏差约 6.2 m（<50 m 走廊），纬度单调北增，路名 Golden Gate Bridge(US 101; CA 1)，无其他桥/渡轮/步行/停靠/绕回。距离 2.234 km、估算 2.3 min 与响应 2234 m/138.8 s 一致并标注估算，来源与 OSM/FOSSGIS 署名齐全。指定入口为免费公共演示服务，本次匿名请求无凭据、无付费。

**valhalla / public-route-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; anonymous FOSSGIS public demos, no account/token/email/payment supplied · 独立验收可参考同期 2 份同题答案

准备：Same frozen task/model/budget, public OSRM vs Valhalla engines hosted by FOSSGIS using OSM; not independent providers or map truth. All candidate executions serial; 4routecalls per service per stage,>=2s,stop first403/429 or two consecutive connection failures. Service limits are instructions; model/output/time caps enforced. Explicit truthful UA/project URL and Valhalla X-Client-Id. No account/key/paid fallback/prewritten client. Same image2GiB/1CPU/pids256,pipTUNA/emptycache. Access then audited generic configuration/installed dependencies retained; restart owned executor before fresh businesshome/session/workspace. Exec25requests/access300s/business600s;grading40/300s;output32000/request. Independent roads/reference and official operator rules frozen before candidate queries and grader-only; business peers sealed before separate grading without peer verdicts. No grader candidateAPI calls. Official summary allows low-volume noncommercial use; full linked German policy was blocked and not read, no blanket complete terms-review claim. AttributionOSM/FOSSGIS andfix-maplink accompany public facts. Official source manifest SHA256 c316e7244f96b20dc106f32047f9a055d1684b6c52a4fc0699e8d4e28dd80a05. Retention audit SHA256 83fc21262ffafb4959ab6f50b7c6161fb4da0beb7e96adb54d87ddff0b11d200.

- [valhalla-routing-bridge-001-ds41-r1](../data/experiments/evaluations/valhalla-routing-bridge-001-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: 官方文档仅说明 FOSSGIS 公共演示服务器面向公众开放、无需注册并遵循 fair-usage/速率限制，未给出明确免费或无计费条款；完整德文运营方 Nutzungsbedingungen 未读取，依据不足，保留 unknown，不因本次成功响应或未付款认定免费。; official-route-sources/valhalla-demo.source; official-route-sources/operator-services.source; official-route-sources/operator-about.source

  结论与限制：指定 FOSSGIS 托管 Valhalla 入口以 auto 模式对 A→B 取得真实路线（HTTP 200，本次 1 次请求）。交付 GeoJSON LineString 由该响应 polyline6 形状独立解码所得，起终点距给定点分别 0.62 m、0.0 m（<50 m），与冻结官方道路参考中心线加密双向比对最大偏差约 6.2 m（<50 m），南→北、无渡轮/其他桥；距离 2.24 km、估时约 1.3 分钟与响应一致，道路名/方向与来源署名准确。

<a id="comparison-6d420b99e4b1"></a>

### route-planning-access-001 v1

**osrm / public-route-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; anonymous FOSSGIS public demos, no account/token/email/payment supplied

准备：Same frozen task/model/budget, public OSRM vs Valhalla engines hosted by FOSSGIS using OSM; not independent providers or map truth. All candidate executions serial; 4routecalls per service per stage,>=2s,stop first403/429 or two consecutive connection failures. Service limits are instructions; model/output/time caps enforced. Explicit truthful UA/project URL and Valhalla X-Client-Id. No account/key/paid fallback/prewritten client. Same image2GiB/1CPU/pids256,pipTUNA/emptycache. Access then audited generic configuration/installed dependencies retained; restart owned executor before fresh businesshome/session/workspace. Exec25requests/access300s/business600s;grading40/300s;output32000/request. Independent roads/reference and official operator rules frozen before candidate queries and grader-only; business peers sealed before separate grading without peer verdicts. No grader candidateAPI calls. Official summary allows low-volume noncommercial use; full linked German policy was blocked and not read, no blanket complete terms-review claim. AttributionOSM/FOSSGIS andfix-maplink accompany public facts. Official source manifest SHA256 c316e7244f96b20dc106f32047f9a055d1684b6c52a4fc0699e8d4e28dd80a05.

- [osrm-routing-access-ds41-r1](../data/experiments/evaluations/osrm-routing-access-ds41-r1.json)：模型费用 $0.0054；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: Controller source review could not confirm an explicit hosted-demo zero-fee rule in the frozen official sources. Donation-funded, public, no-registration use and open-source/map licences do not establish price. Original independent confirmed_free assessment is preserved privately with its hash and unchanged task verdict/reason/checks; publication conservatively retains unknown rather than inferring zero. No additional model review or service query.; official-route-sources/operator-services.source; official-route-sources/operator-about.source

  结论与限制：执行者通过冻结指定的 FOSSGIS 公共 OSRM 入口对给定起终点完成一次真实普通小汽车路线查询：HTTP 200、code Ok，坐标按 经度,纬度 顺序、profile=driving，请求带规定 User-Agent，仅 1 次路由请求（预算内，未触发 403/429）。答复距离 3850 米、估算时间 381.1 秒，与采集响应 routes[0] 完全一致且单位明确。通用（非秘密）配置写入持久目录 /home/node/service-tools/service-config.json 并被保留。接入步骤与实际门槛如实说明：无需注册/Key/授权，无人工介入，无秘密泄露，并给出 OSM 署名。

**valhalla / public-route-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; anonymous FOSSGIS public demos, no account/token/email/payment supplied

准备：Same frozen task/model/budget, public OSRM vs Valhalla engines hosted by FOSSGIS using OSM; not independent providers or map truth. All candidate executions serial; 4routecalls per service per stage,>=2s,stop first403/429 or two consecutive connection failures. Service limits are instructions; model/output/time caps enforced. Explicit truthful UA/project URL and Valhalla X-Client-Id. No account/key/paid fallback/prewritten client. Same image2GiB/1CPU/pids256,pipTUNA/emptycache. Access then audited generic configuration/installed dependencies retained; restart owned executor before fresh businesshome/session/workspace. Exec25requests/access300s/business600s;grading40/300s;output32000/request. Independent roads/reference and official operator rules frozen before candidate queries and grader-only; business peers sealed before separate grading without peer verdicts. No grader candidateAPI calls. Official summary allows low-volume noncommercial use; full linked German policy was blocked and not read, no blanket complete terms-review claim. AttributionOSM/FOSSGIS andfix-maplink accompany public facts. Official source manifest SHA256 c316e7244f96b20dc106f32047f9a055d1684b6c52a4fc0699e8d4e28dd80a05.

- [valhalla-routing-access-ds41-r1](../data/experiments/evaluations/valhalla-routing-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: Controller source review could not confirm an explicit hosted-demo zero-fee rule in the frozen official sources. Donation-funded, public, no-registration use and open-source/map licences do not establish price. Original independent confirmed_free assessment is preserved privately with its hash and unchanged task verdict/reason/checks; publication conservatively retains unknown rather than inferring zero. No additional model review or service query.; official-route-sources/operator-services.source; official-route-sources/valhalla-demo.source

  结论与限制：指定入口 FOSSGIS Valhalla 公共路线 API 实际返回有效小汽车路线：POST https://valhalla1.openstreetmap.de/route 得 HTTP 200、trip.status 0，按给定起点→终点坐标与 costing=auto 取得 4.579 km / 404.622 s；答复与响应逐值相符且单位明确；非秘密通用配置已保存到持久目录 /home/node/service-tools/service-config.json；零账号自助接入、无人工介入或额外申请，门槛如实说明；预算内完成（1 次路由请求、约 30 秒）。免费公共演示规则有官方来源支持。

<a id="comparison-bde1a47b7eaa"></a>

### web-extraction-access-001 v1

**exa / public-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; anonymous public extraction routes, no account/email/token/payment supplied

准备：Same frozen task, model and budget. Firecrawl anonymous REST scrape versus Exa anonymous hosted MCP content fetch; a specific PDF and route trial, not a general service or interface ranking. No account/key/paid fallback. Fresh access before business; retain only audited generic config and genuinely installed dependencies. Restart each owned execution container after access to remove orphan processes while retaining file hashes, then fresh home/session/workspace. Same image,2GiB/1CPU/pids256,pipTUNA and initial empty cache. Execution25requests/access300s/business600s,grading40/300s,32000outputtokens/request. Candidate API6/stage and at least1s spacing are instructions; model/time caps enforced. Anonymous remaining quota unknown; do not apply keyed account allowance or price. Independent source PDF/reference and official anonymous route/cost documents frozen before candidate executions, supplied only to graders; business peers sealed before separate grading, no peer verdicts. Format, truncation and caching features differ by route; disclose actual behavior, no artificial common freshness claim.

- [exa-pdf-access-ds41-r1](../data/experiments/evaluations/exa-pdf-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 官方文档 Authentication 表明确列出 Keyless 模式为 free rate-limited usage without sign-in or API key，无逐次计费回执；本次为匿名 keyless 调用。; official-route-sources/exa-mcp.md; review-packet/tools/0006.json; review-packet/tools/0010.json

  结论与限制：执行者通过指定官方匿名 hosted MCP 入口 https://mcp.exa.ai/mcp，用 web_fetch_exa 真实提取 https://example.com/ 正文，标题与概述与返回值及独立参考一致；非秘密复用配置已写入持久目录，接入步骤、keyless 免注册与门槛说明属实。未使用需 Key 的 REST /contents、未直读源站、未注册账号，1 次提取调用在 6 次预算内。

**firecrawl / public-scrape-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; anonymous public extraction routes, no account/email/token/payment supplied

准备：Same frozen task, model and budget. Firecrawl anonymous REST scrape versus Exa anonymous hosted MCP content fetch; a specific PDF and route trial, not a general service or interface ranking. No account/key/paid fallback. Fresh access before business; retain only audited generic config and genuinely installed dependencies. Restart each owned execution container after access to remove orphan processes while retaining file hashes, then fresh home/session/workspace. Same image,2GiB/1CPU/pids256,pipTUNA and initial empty cache. Execution25requests/access300s/business600s,grading40/300s,32000outputtokens/request. Candidate API6/stage and at least1s spacing are instructions; model/time caps enforced. Anonymous remaining quota unknown; do not apply keyed account allowance or price. Independent source PDF/reference and official anonymous route/cost documents frozen before candidate executions, supplied only to graders; business peers sealed before separate grading, no peer verdicts. Format, truncation and caching features differ by route; disclose actual behavior, no artificial common freshness claim.

- [firecrawl-pdf-access-ds41-r1](../data/experiments/evaluations/firecrawl-pdf-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 匿名无 Key 属官方 keyless 免费档；本次调用符合其条件，未产生实付费用。匿名每日配额数值/余量未知，按回执 creditsUsed=1 记录但不计费。; official-route-sources/firecrawl-rate-limits.md; official-route-sources/firecrawl-billing.md; grading/artifacts/evidence/free-rule.md

  结论与限制：执行者通过指定官方匿名入口 POST https://api.firecrawl.dev/v2/scrape（无 Authorization、无 API key）真实取得 https://example.com/ 正文：HTTP 200、success:true、metadata.title=Example Domain、statusCode=200，返回 markdown 首段与参考页面正文逐字一致；据此给出的标题与一句概述与返回正文相符。必要配置已写入指定持久目录 /home/node/service-tools/service-config.json 并为合法 JSON、无秘密，答复仅给出路径。账号来源、接入步骤与门槛（无注册/无人工/无额外申请；匿名配额余量未知、默认缓存）如实说明。仅 1 次提取调用、未换服务或身份、未付费，符合预算。匿名无 Key 属官方文档明示的免费档且本次调用符合其条件。

<a id="comparison-644e634b8512"></a>

### dependency-advisories-check-001 v1

**github / public-advisories-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; anonymous public advisory API, no account/email/token/payment supplied · 独立验收可参考同期 2 份同题答案

准备：Same frozen task, model and budget; two anonymous provider streams. Fresh access before business; only generic configuration and genuinely installed dependencies may be retained after controller audit, no old query helper/cache/answer. Same image 2GiB/1CPU/pids256, pipTUNA/emptycache. Exec25 model requests (access300s/business600s), grade40/300s, output32000. Candidate API limit6/stage and ≥1s spacing are instructions, assessed against actual traces; model/time caps enforced. One GitHub anonymous rate_limit preflight returned core60/60 before prepare; actual API headers govern quota. Independent maintainer source snapshot before candidate queries; business peer outputs frozen together before separate graders. Shared OSV/GHSA upstream is disclosed: compare metadata task delivery and access, not independent vulnerability discovery, exhaustive coverage, deploy exploitability or universal safe upgrades. No account or mutable service resource created. Retention audit SHA256 7b1887aa539fb9c744c89b63df042874d9756ca439422714010d852a9d0057e5.

- [github-advisories-django-001-ds41-r1](../data/experiments/evaluations/github-advisories-django-001-ds41-r1.json)：模型费用 $0.0076；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 指定 GitHub global-advisories 为匿名免费公共 API；本次 2 次 GET 均 HTTP 200，未用凭据、未付款，core 限流 60/小时。; frozen-execution/ENVIRONMENT.md; https://docs.github.com/en/rest/security-advisories/global-advisories

  结论与限制：执行者用指定 GitHub global-advisories 匿名 API 对 CVE-2025-57833、CVE-2025-59681 各发起 1 次 cve_id 查询，均 HTTP 200 并采集原始记录。逐条核对 PyPI Django 5.2.6：CVE-2025-57833 的 5.2 分支范围为 >=5.2a1,<5.2.6，5.2.6 不匹配（已修复，首个修复版 5.2.6）；CVE-2025-59681 的 5.2 分支范围为 >=5.2,<5.2.7，5.2.6 仍匹配（首个修复版 5.2.7）；仅这两条的最低升级版本 5.2.7。结论与事前冻结的 djangoproject.com 公告及 5.2.6/5.2.7 发布说明一致，来源链接可追溯，仅读范围无安装或修改。

**osv / public-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; anonymous public advisory API, no account/email/token/payment supplied · 独立验收可参考同期 2 份同题答案

准备：Same frozen task, model and budget; two anonymous provider streams. Fresh access before business; only generic configuration and genuinely installed dependencies may be retained after controller audit, no old query helper/cache/answer. Same image 2GiB/1CPU/pids256, pipTUNA/emptycache. Exec25 model requests (access300s/business600s), grade40/300s, output32000. Candidate API limit6/stage and ≥1s spacing are instructions, assessed against actual traces; model/time caps enforced. One GitHub anonymous rate_limit preflight returned core60/60 before prepare; actual API headers govern quota. Independent maintainer source snapshot before candidate queries; business peer outputs frozen together before separate graders. Shared OSV/GHSA upstream is disclosed: compare metadata task delivery and access, not independent vulnerability discovery, exhaustive coverage, deploy exploitability or universal safe upgrades. No account or mutable service resource created. Retention audit SHA256 7b1887aa539fb9c744c89b63df042874d9756ca439422714010d852a9d0057e5.

- [osv-advisories-django-001-ds41-r1](../data/experiments/evaluations/osv-advisories-django-001-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 被测服务为 OSV 公共公告 API。任务冻结材料将本轮指定服务描述为免费公开公告服务（task.json resources），ENVIRONMENT.md 载明“OSV公开服务当前免费”。本次全部候选查询均为匿名、无 Key/Token/鉴权头，且未发生任何付费流程，费用为 0。; frozen-execution/ENVIRONMENT.md; task.json

  结论与限制：本次执行真实查询指定 OSV 公共 API（匿名 POST https://api.osv.dev/v1/query）并按 CVE 别名定位两条记录；答复逐条正确判断 PyPI Django 5.2.6 的匹配情况与 5.2.x 修复边界，与采集到的 API 原始响应及事前冻结的 Django 维护者公告一致，且未越权。

<a id="comparison-7a5fd0fd8e1a"></a>

### dependency-advisories-access-001 v1

**github / public-advisories-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; anonymous public advisory API, no account/email/token/payment supplied

准备：Same frozen task, model and budget; two anonymous provider streams. Fresh access before business; only generic configuration and genuinely installed dependencies may be retained after controller audit, no old query helper/cache/answer. Same image 2GiB/1CPU/pids256, pipTUNA/emptycache. Exec25 model requests (access300s/business600s), grade40/300s, output32000. Candidate API limit6/stage and ≥1s spacing are instructions, assessed against actual traces; model/time caps enforced. One GitHub anonymous rate_limit preflight returned core60/60 before prepare; actual API headers govern quota. Independent maintainer source snapshot before candidate queries; business peer outputs frozen together before separate graders. Shared OSV/GHSA upstream is disclosed: compare metadata task delivery and access, not independent vulnerability discovery, exhaustive coverage, deploy exploitability or universal safe upgrades. No account or mutable service resource created.

- [github-advisories-access-ds41-r1](../data/experiments/evaluations/github-advisories-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: Anonymous GitHub global-advisories API; no payment, billing or fee was observed in the run. Only rate-limit (60/hour) and HTTP 200 headers were captured, and no official free-rule/pricing source was retained, so a free conclusion cannot be evidenced and cost is left unknown. This is the service fee only; model/token cost is out of scope.

  结论与限制：Executor used the assigned anonymous route https://api.github.com/advisories with the required Accept, X-GitHub-Api-Version: 2026-03-10 and project User-Agent headers; captured HTTP 200 responses contain identifiable advisories (GHSA-q7m5-3jmv-vm48/praisonai, GHSA-77xj-x4rm-935c/datamodel-code-generator, GHSA-xpx6-x8c2-mw5w/praisonai) matching answer.md. A non-secret reusable config was written to the authorized persistent path /home/node/service-tools/service-config.json and recorded as retained. No account, token or human step was required; only the anonymous shared 60/hour rate-limit barrier is reported. No scope violations observed. Service fee: anonymous GitHub API showed no billing and only rate-limit headers, no official free-rule/pricing source was captured, so cost kept unknown.

**osv / public-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; anonymous public advisory API, no account/email/token/payment supplied

准备：Same frozen task, model and budget; two anonymous provider streams. Fresh access before business; only generic configuration and genuinely installed dependencies may be retained after controller audit, no old query helper/cache/answer. Same image 2GiB/1CPU/pids256, pipTUNA/emptycache. Exec25 model requests (access300s/business600s), grade40/300s, output32000. Candidate API limit6/stage and ≥1s spacing are instructions, assessed against actual traces; model/time caps enforced. One GitHub anonymous rate_limit preflight returned core60/60 before prepare; actual API headers govern quota. Independent maintainer source snapshot before candidate queries; business peer outputs frozen together before separate graders. Shared OSV/GHSA upstream is disclosed: compare metadata task delivery and access, not independent vulnerability discovery, exhaustive coverage, deploy exploitability or universal safe upgrades. No account or mutable service resource created.

- [osv-advisories-access-ds41-r1](../data/experiments/evaluations/osv-advisories-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: No billing receipt or usage-based charge applies to this anonymous endpoint. Official OSV documentation describes the API as anonymous with currently no rate limits but publishes no explicit free/pricing rule, and per rubric rate-limit absence or an unlisted price does not by itself establish free service. The frozen ENVIRONMENT.md notes the public service is currently free and no account/payment mechanism was used, but no official free rule with applicability evidence could be confirmed, so the cost is left unknown.; https://google.github.io/osv.dev/faq/; https://google.github.io/osv.dev/api/; execution/answer.md

  结论与限制：OSV public API was reached at the assigned route POST https://api.osv.dev/v1/query and a self-selected real query returned HTTP 200 with an identifiable advisory (GHSA-462w-v97r-4m45, aliases CVE-2019-10906/PYSEC-2019-217) for package jinja2 (PyPI, pkg:pypi/jinja2); the same-API record path GET /v1/vulns/{id} returned the full record. A reusable non-secret config was written to the authorized persistent location /home/node/service-tools/service-config.json and retained. Answer matches the captured responses. Access was fully anonymous with no account/key/registration and no human or application barrier; only 3 candidate API requests (limit 6) were made, no installs/scans/repo changes/payments/messages.

<a id="comparison-183e17ccb640"></a>

### mailboxes-create-001 v2

**mail-tm / mail-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none initially; one fresh anonymous mailbox and necessary identity created inside measured execution

准备：Fresh isolated runtime, no supplied account, human email, mailbox, key, answer, or service client. Same v2 task permits minimal anonymous upstream identity for one free mailbox; old v1/harness/results unchanged. Two provider executions can run concurrently; each creates its own mailbox. External controller independently reuses only saved authentication in GET requests after execution; these reads are additional verification overhead. Execution output and controller evidence are frozen before separate credential-free grading. No peer packet for these access runs; own identity/creation/GET evidence supports each verdict. This covers provisioning and authenticated listing only, not real email delivery, sending, website acceptance, long-term retention or account recovery. Executor25requests/300s, grader40/300s, output32000; same image2GiB/1CPU/pids256 and pipTUNA/emptycache. No paid service subscription or human mailbox attached.

- [mail-tm-mailbox-create-v2-ds41-r1](../data/experiments/evaluations/mail-tm-mailbox-create-v2-ds41-r1.json)：模型费用 $0.0070；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 服务本身按官方规则免费，本次未产生服务费用；金额记为 0。; https://docs.mail.tm/; https://mail.tm/

  结论与限制：本轮在 mail.tm 官方 API 匿名新建了一个专用收件邮箱（maxxspace.com 域，2026-10-08T17:53:45Z 创建），并以 Bearer 令牌成功读取收件箱列表（/messages，HTTP 200，totalItems=0，空列表有效）；访问信息已保存为本执行用户 600 权限的私有文件，总控用保存状态独立只读核验同一邮箱成功（identity_matches_saved_mailbox=true，messages 为空），地址/状态/文件位置与证据一致且答复未泄露秘密。四项交付要求均满足。

**agentmail / mail-api** — 0 完成 / 1 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none initially; one fresh anonymous mailbox and necessary identity created inside measured execution

准备：Fresh isolated runtime, no supplied account, human email, mailbox, key, answer, or service client. Same v2 task permits minimal anonymous upstream identity for one free mailbox; old v1/harness/results unchanged. Two provider executions can run concurrently; each creates its own mailbox. External controller independently reuses only saved authentication in GET requests after execution; these reads are additional verification overhead. Execution output and controller evidence are frozen before separate credential-free grading. No peer packet for these access runs; own identity/creation/GET evidence supports each verdict. This covers provisioning and authenticated listing only, not real email delivery, sending, website acceptance, long-term retention or account recovery. Executor25requests/300s, grader40/300s, output32000; same image2GiB/1CPU/pids256 and pipTUNA/emptycache. No paid service subscription or human mailbox attached.

- [agentmail-mailbox-create-v2-ds41-r1](../data/experiments/evaluations/agentmail-mailbox-create-v2-ds41-r1.json)：模型费用 $0.03；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: 没有任何 AgentMail API 调用成功（全部在边缘 403），无计费回执或成功用量；未取得 Free 邮箱，官方免费规则未被本次实际适用，故费用保留 unknown。

  结论与限制：未达到交付：没有创建任何邮箱、没有真实收件箱读取、也没有可复用的访问状态。执行者按匿名 receive-only 路径向 https://api.agentmail.to/v0/agent/sign-up 发起创建，但对 api.agentmail.to 的全部请求（含无认证根路径与 /v0/inboxes）都被 CloudFront 边缘以 403 Request blocked 拦截，应用层未返回 api_key/inbox；保存的 credentials.json 为空 {}。总控独立诊断从 host 与执行容器同样得到 CloudFront 403，且未做独立复用（independent_reuse=not_performed）。该阻碍属网络/接入障碍（环境侧），执行者已如实说明，非服务能力或资质问题；因基础执行环境与工具（shell/curl/python/node、常规联网及同服务 docs/console）均正常，未记为 invalid_run。另有执行行为问题：对指定 API 主机的候选请求超过 12 次上限（总控核为 17 次以上），且答复称 sign-up“唯一一次”与实际 4 次 POST 不符。

<a id="comparison-39d86ae45d95"></a>

### public-holidays-berlin-001 v1

**nager-date / community-api-v4** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; anonymous publicAPI, no account/email/key/payment supplied · 独立验收可参考同期 2 份同题答案

准备：Freshanonymousaccess thenbusiness with separate sessions/workspaces. Samefrozen task,model,effort,25executionrequests (300saccess/600sbusiness),40gradingrequests/300s,32000outputtokens/request. Samebaseimage2GiB/1CPU/pids256;2providerstreams;all4runtimes preconfigureTUNApipindex,emptycache,noadditionalpackages. ≤6APIrequests/stage,1atatime,≥2sstartspacing,truthfulUA. CurrentNagerCommunityv4 fornoncommercial/private/nonprofit vsOpenHolidayspublicAPI/ODbL,termsdifferences disclosed. No lookupcode/queryanswer/reference supplied; independentofficialBerlinHTML/referencefrozenbeforecalls;peerresultssealedbeforegrading. Completecandidateholidaytables/answersretainedprivately;publiconlyminimalverification/hashfacts,notaholidayportal. ActualAPI docs/schema discovery and dependency setupcountinrun. OneBerlin/yearlookup,notglobalcoverage/futureaccuracy/uptime/closureorlegalentitlementranking. Retentionapproved: genericconfig/dependenciesonly; controlleraudit SHA256 e6dc61b41dc164298bdb2616d2075a07e6e3db348167c1f4a25a71deffc2d030.

- [nager-date-holidays-berlin-001-ds41-r1](../data/experiments/evaluations/nager-date-holidays-berlin-001-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Nager.Date Community v4 托管 Web API 无 Key、无计费入口。官方条款允许 private/non-profit 项目使用，商业用途需 active sponsorship（本次为非商业低量服务研究）。实际匿名无 Key 请求 HTTP 200，未使用支付或订阅，NuGet/Docker 离线包的 license key 不适用于本次使用的托管 Community API。; https://nagerholidays.com/legal/termsofservice; https://nagerholidays.com/api

  结论与限制：指定服务 Nager.Date Community v4 被真实调用：采集的工具记录显示 GET https://nagerholidays.com/api/v4/Holidays/DE/2027 返回 HTTP 200，正文为德国 2027 年 19 条公共假日条目。执行者按 nationalHoliday=true 或 subdivisionCodes 含 DE-BE 且类型 Public 过滤，得到 10 条，与事前冻结的柏林官方独立参考（reference.json）在日期与节日身份上完全一致，计数 10=10，按日期升序、无重复、无越界他州节日、周末节日保留实际日期。来源可追溯，服务在官方条款允许的非商业范围内无 Key 免费使用。

**openholidays / public-holidays-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; anonymous publicAPI, no account/email/key/payment supplied · 独立验收可参考同期 2 份同题答案

准备：Freshanonymousaccess thenbusiness with separate sessions/workspaces. Samefrozen task,model,effort,25executionrequests (300saccess/600sbusiness),40gradingrequests/300s,32000outputtokens/request. Samebaseimage2GiB/1CPU/pids256;2providerstreams;all4runtimes preconfigureTUNApipindex,emptycache,noadditionalpackages. ≤6APIrequests/stage,1atatime,≥2sstartspacing,truthfulUA. CurrentNagerCommunityv4 fornoncommercial/private/nonprofit vsOpenHolidayspublicAPI/ODbL,termsdifferences disclosed. No lookupcode/queryanswer/reference supplied; independentofficialBerlinHTML/referencefrozenbeforecalls;peerresultssealedbeforegrading. Completecandidateholidaytables/answersretainedprivately;publiconlyminimalverification/hashfacts,notaholidayportal. ActualAPI docs/schema discovery and dependency setupcountinrun. OneBerlin/yearlookup,notglobalcoverage/futureaccuracy/uptime/closureorlegalentitlementranking. Retentionapproved: genericconfig/dependenciesonly; controlleraudit SHA256 e6dc61b41dc164298bdb2616d2075a07e6e3db348167c1f4a25a71deffc2d030.

- [openholidays-holidays-berlin-001-ds41-r1](../data/experiments/evaluations/openholidays-holidays-berlin-001-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 无计费回执；按官方免费规则确认本次服务费用为免费，非按执行者自称未付款。; https://www.openholidaysapi.org/en/faq/

  结论与限制：本次执行使用指定服务 OpenHolidays API 的真实匿名只读请求（HTTP 200），限定 countryIsoCode=DE、subdivisionCode=DE-BE 与 2027-01-01~2027-12-31，返回 10 条 type=Public 公共节假日；日期与节日身份与冻结的柏林官方独立参考 10/10 对应，无他州独有节日、学校假期或普通星期日，周末保留实际日期，升序无重复，总数 10，来源可追溯。指定服务费用依官方 FAQ 免费规则确认为免费。

<a id="comparison-0ce2de00d325"></a>

### public-holidays-access-001 v1

**nager-date / community-api-v4** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; anonymous publicAPI, no account/email/key/payment supplied

准备：Freshanonymousaccess thenbusiness with separate sessions/workspaces. Samefrozen task,model,effort,25executionrequests (300saccess/600sbusiness),40gradingrequests/300s,32000outputtokens/request. Samebaseimage2GiB/1CPU/pids256;2providerstreams;all4runtimes preconfigureTUNApipindex,emptycache,noadditionalpackages. ≤6APIrequests/stage,1atatime,≥2sstartspacing,truthfulUA. CurrentNagerCommunityv4 fornoncommercial/private/nonprofit vsOpenHolidayspublicAPI/ODbL,termsdifferences disclosed. No lookupcode/queryanswer/reference supplied; independentofficialBerlinHTML/referencefrozenbeforecalls;peerresultssealedbeforegrading. Completecandidateholidaytables/answersretainedprivately;publiconlyminimalverification/hashfacts,notaholidayportal. ActualAPI docs/schema discovery and dependency setupcountinrun. OneBerlin/yearlookup,notglobalcoverage/futureaccuracy/uptime/closureorlegalentitlementranking.

- [nager-date-holidays-access-ds41-r1](../data/experiments/evaluations/nager-date-holidays-access-ds41-r1.json)：模型费用 $0.0064；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 托管 Community v4 Web API 未列入需 license key 的产品（license key 仅针对离线 NuGet/Docker），Terms 允许 private/non-profit 使用；本次为匿名非商业低量调用。无服务商回执，费用按官方免费规则确认为 0。; https://nagerholidays.com/integration/getstarted; https://nagerholidays.com/legal/termsofservice

  结论与限制：指定服务 Nager.Date Community v4 的真实假日查询已完成：匿名 GET https://nagerholidays.com/api/v4/Holidays/AT/2026 返回 HTTP 200 与 20 条 AT 2026 假日，答复中的范围与示例（2026-01-01 New Year's Day、2026-12-25 Christmas Day）与采集响应一致；必要配置写入指定持久目录 /home/node/service-tools/service-config.json 且无秘密；答复说明了匿名无账号、无人工介入与无额外申请。未换服务或离线库，API 调用 1 次。

**openholidays / public-holidays-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; anonymous publicAPI, no account/email/key/payment supplied

准备：Freshanonymousaccess thenbusiness with separate sessions/workspaces. Samefrozen task,model,effort,25executionrequests (300saccess/600sbusiness),40gradingrequests/300s,32000outputtokens/request. Samebaseimage2GiB/1CPU/pids256;2providerstreams;all4runtimes preconfigureTUNApipindex,emptycache,noadditionalpackages. ≤6APIrequests/stage,1atatime,≥2sstartspacing,truthfulUA. CurrentNagerCommunityv4 fornoncommercial/private/nonprofit vsOpenHolidayspublicAPI/ODbL,termsdifferences disclosed. No lookupcode/queryanswer/reference supplied; independentofficialBerlinHTML/referencefrozenbeforecalls;peerresultssealedbeforegrading. Completecandidateholidaytables/answersretainedprivately;publiconlyminimalverification/hashfacts,notaholidayportal. ActualAPI docs/schema discovery and dependency setupcountinrun. OneBerlin/yearlookup,notglobalcoverage/futureaccuracy/uptime/closureorlegalentitlementranking.

- [openholidays-holidays-access-ds41-r1](../data/experiments/evaluations/openholidays-holidays-access-ds41-r1.json)：模型费用 $0.0091；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 官方 FAQ 明确 OpenHolidays API 为开放数据、免费使用且允许商业项目；本次为其覆盖的非商业低量匿名使用，无任何计费回执。; https://www.openholidaysapi.org/en/faq/

  结论与限制：指定 openholidays 的 PublicHolidays 入口被真实调用并返回可识别假日（DE 2025-01-01 New Year's Day 等），最终答复与响应一致；复用配置已写入 ENVIRONMENT.md 指定的持久位置且无秘密；账号来源（匿名公共路线，无注册/人工介入/额外申请）与调用约束如实说明；模型/harness 与测评配置一致。

<a id="comparison-bfa31194c37d"></a>

### database-restore-001 v1

**neon / claimable-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none initially; generated anonymous Claimable project credentials · 独立验收可参考同期 2 份同题答案

准备：Same independentlyfrozen synthetic2table logicalstate, controllerseeded onlyeachnewpassedaccesssource and verifiedcomplete rows/catalog beforedispatch. No fixture/reference/seedcode senttoexecutor. Sourceidentity/permissions/quota verified; controllerwrites notexecutionachievement. BothallowofficialAPI/SDK/CLI/standardSQLclients, actualusedinterfacesmustbedisclosed,notAPI-onlyprotocolrank. TursoexistingaccountwithreadonlysourceSQLtoken+broadermanagement vsNeonnewanonymousClaimableowner; sourcewritepermissionnottechnicallyeliminated, behavioralboundary+independentbefore/afterreadback. BothsameTUNApipsetting fromaccess; Neonkeepsitsownmeasuredaccessinstalledpsycopg2-binary2.9.13venv;Tursohasnoretainedclient. Controllerarchivedconfigsandremovedonlystaleempty-sourceclaims; explicitretentionauditSHA256 779f9d7b6c30269f63ca7295b9e2b44e3a1b70efecee750c0e709635fef3d2f1. NewcohortseparatefromoriginaldefaultPyPIaccess; earlierfailedrecordpreserved. Same2GiB/1CPU/pids256baseimage;2providerstreamsmax;OpenCode1.18.35DeepSeekFlash/high,exec25requests/600s,grade40/300s,32000outputtokens. Sourcesnootherwriter;≤1target,≤40serviceoperations,≤10MBbackup. Independentcontrollerreadonlyverificationbeforegrading; no livegradercredentials. Onesmallsame-enginebackup,notcrossengine/large/concurrent/PITR/productionDRproof.

- [neon-restore-mirror-001-ds41-r1](../data/experiments/evaluations/neon-restore-mirror-001-ds41-r1.json)：模型费用 $0.03；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: 运行在未 claim 的 Neon claimable 匿名临时项目内，未付费、未绑卡、未申请 claim，项目共享 100MB 存储/1GB 传输、到期 2026-10-11T16:39:36.935Z。无账单单据、无按量计费回执，官方 claimable 文档仅列 72h 期限与 100MB/1GB 上限而未列费率，故无法确证为零费用，费用保留未知。; https://neon.com/docs/reference/claimable-neon; controller-verification/resource-limits.json

  结论与限制：指定 Neon claimable 服务上完成了真实逻辑备份恢复演练。源库 neondb 导出为自包含纯 SQL 备份（1697B，含两表结构、主键、外键、NOT NULL、默认值及全部记录，NULL 与空串区分保留）；在本次同一项目/分支内新建了与源库不同名的独立逻辑库（控制器确认其不在执行前库列表中，且恢复前 public 无业务表），并用该备份文件实际执行恢复；执行者与控制器独立读回均显示目标库结构精确等于源库、行内容与冻结 fixture 逐行一致（lists=2, todos=5），源库结构与记录未变。交付含备份、恢复方法、目标位置、行数与核对结果及期限说明。费用方面无回执与费率依据，按未知处理。

<a id="comparison-3961c742b40e"></a>

### database-restore-001 v1

**turso / platform-api** — 0 完成 / 1 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · existing authorized Turso management account · 独立验收可参考同期 2 份同题答案

准备：Same independentlyfrozen synthetic2table logicalstate, controllerseeded onlyeachnewpassedaccesssource and verifiedcomplete rows/catalog beforedispatch. No fixture/reference/seedcode senttoexecutor. Sourceidentity/permissions/quota verified; controllerwrites notexecutionachievement. BothallowofficialAPI/SDK/CLI/standardSQLclients, actualusedinterfacesmustbedisclosed,notAPI-onlyprotocolrank. TursoexistingaccountwithreadonlysourceSQLtoken+broadermanagement vsNeonnewanonymousClaimableowner; sourcewritepermissionnottechnicallyeliminated, behavioralboundary+independentbefore/afterreadback. BothsameTUNApipsetting fromaccess; Neonkeepsitsownmeasuredaccessinstalledpsycopg2-binary2.9.13venv;Tursohasnoretainedclient. Controllerarchivedconfigsandremovedonlystaleempty-sourceclaims; explicitretentionauditSHA256 779f9d7b6c30269f63ca7295b9e2b44e3a1b70efecee750c0e709635fef3d2f1. NewcohortseparatefromoriginaldefaultPyPIaccess; earlierfailedrecordpreserved. Same2GiB/1CPU/pids256baseimage;2providerstreamsmax;OpenCode1.18.35DeepSeekFlash/high,exec25requests/600s,grade40/300s,32000outputtokens. Sourcesnootherwriter;≤1target,≤40serviceoperations,≤10MBbackup. Independentcontrollerreadonlyverificationbeforegrading; no livegradercredentials. Onesmallsame-enginebackup,notcrossengine/large/concurrent/PITR/productionDRproof.

- [turso-restore-mirror-001-ds41-r1](../data/experiments/evaluations/turso-restore-mirror-001-ds41-r1.json)：模型费用 —；Per-request usage capture is incomplete. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；confirmed_free: 仅免费 starter 计划内的少量操作，本次无计费金额；该免费额度不代表永久免费。; controller-verification/resource-limits.json

  结论与限制：备份导出、在指定服务经 Platform API 新建独立空目标、用该备份实际恢复、恢复后结构与全部记录等价、源库未变、重连读回均已由执行记录与控制器独立核对确认；但本次执行在写出最终答复前因模型请求预算耗尽（403 Model request budget exhausted，回执 exit_code=1）终止，执行者最终答复 execution/answer.md 只有 8 行过程旁白，未交付备份路径、简短恢复方法、新库位置、各表行数与核对结果、免费/期限说明，工作目录亦无该说明文件，缺少必要业务交付，故未完成。属执行预算/交付缺口，非服务或运行环境失效。

<a id="comparison-b5f2b1f41c23"></a>

### scholarly-reference-001 v1

**crossref / public-rest-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; currentofficialkeylesspublicroute, no account/email/payment supplied; lowvolumebibliographicmetadata only · 独立验收可参考同期 2 份同题答案

准备：Fresh anonymous access thenbusinesssessions, commonfrozenreadingnote/task/model/effort/generictools/time/requestlimits. SamebaseimageOpenCode1.18.35,DeepSeekFlash/high. Execution25requests/300saccessor600sbusiness;grading40requests/300s,32000outputtokens/request. Eachcontainer2GiB/1CPU,pids256; two providerstreams mayoverlap on16CPU/31.34GiBhost. Eachstage≤3APIrequests,oneatime,≥5secondsbetweenstarts; cacheidenticalqueries, truthfulprojectUA. No prewrittenservicecode or targetanswer. StandardCrossrefpublicpool(noemail) versusOpenAlexanonymousallowance(noKey), conditionsnotidenticalanddisclosed. BothmayuseCrossrefupstream; independentpublisherHTML/referencefrozenbeforequeries,neverhandedtoexecutor. ReturnedDOI/publisherlinkfollowup allowed equally. Gradersuseactualcapturedcalls, noextracandidateAPIqueries. OnefamousEnglishpaperlookup, nottopicsearch/fulltext/citationquality/generalcoverageranking. Controllerarchived originalaccessconfig and removedoldtaskcachepath frombothconfigs pluspriorOpenAlexusageheaders; no newscript/query/data added. Thisisdisclosedexternalcleanup,notunassistedconfigurationreuse. Retentionaudit SHA256 fa597023514b81c739918ae218dc62c1d7459e8818aa0913d1228c9f245c26d2.

- [crossref-scholarly-reference-001-ds41-r1](../data/experiments/evaluations/crossref-scholarly-reference-001-ds41-r1.json)：模型费用 $0.0064；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 免费规则来自 Crossref 官方 REST API 文档与冻结环境说明；本次仅匿名公共元数据查询，无计费回执。; https://www.crossref.org/documentation/retrieve-metadata/rest-api/; frozen-execution/ENVIRONMENT.md

  结论与限制：执行者通过指定服务 CrossRef REST API（https://api.crossref.org/works）真实查询并命中唯一同时满足全部线索的论文。检索响应与 DOI 单条核对响应均为 HTTP 200，且交付的必要书目信息（题名 Deep learning、作者顺序 LeCun/Bengio/Hinton、年份 2015、期刊 Nature、DOI https://doi.org/10.1038/nature14539）与事前冻结的出版社官方参考（Nature 文章页 citation 元数据）完全一致，作者无遗漏或错序，DOI 指向同一作品。中文匹配说明有本次响应数据依据并注明了检索来源与请求路径。

**openalex / public-rest-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; currentofficialkeylesspublicroute, no account/email/payment supplied; lowvolumebibliographicmetadata only · 独立验收可参考同期 2 份同题答案

准备：Fresh anonymous access thenbusinesssessions, commonfrozenreadingnote/task/model/effort/generictools/time/requestlimits. SamebaseimageOpenCode1.18.35,DeepSeekFlash/high. Execution25requests/300saccessor600sbusiness;grading40requests/300s,32000outputtokens/request. Eachcontainer2GiB/1CPU,pids256; two providerstreams mayoverlap on16CPU/31.34GiBhost. Eachstage≤3APIrequests,oneatime,≥5secondsbetweenstarts; cacheidenticalqueries, truthfulprojectUA. No prewrittenservicecode or targetanswer. StandardCrossrefpublicpool(noemail) versusOpenAlexanonymousallowance(noKey), conditionsnotidenticalanddisclosed. BothmayuseCrossrefupstream; independentpublisherHTML/referencefrozenbeforequeries,neverhandedtoexecutor. ReturnedDOI/publisherlinkfollowup allowed equally. Gradersuseactualcapturedcalls, noextracandidateAPIqueries. OnefamousEnglishpaperlookup, nottopicsearch/fulltext/citationquality/generalcoverageranking. Controllerarchived originalaccessconfig and removedoldtaskcachepath frombothconfigs pluspriorOpenAlexusageheaders; no newscript/query/data added. Thisisdisclosedexternalcleanup,notunassistedconfigurationreuse. Retentionaudit SHA256 fa597023514b81c739918ae218dc62c1d7459e8818aa0913d1228c9f245c26d2.

- [openalex-scholarly-reference-001-ds41-r1](../data/experiments/evaluations/openalex-scholarly-reference-001-ds41-r1.json)：模型费用 $0.0083；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 本轮无账号、无 Key、无支付方式，仅用 OpenAlex 匿名路径。响应头 x-ratelimit-limit-usd=0.1、remaining-usd 由 0.098 降至 0.0979（始终为正），逐次 x-ratelimit-cost-usd 合计约 $0.0011，全部消耗于匿名每日免费额度内，未产生实付费用。; execution/artifacts/headers1.txt; execution/artifacts/headers2.txt; https://help.openalex.org/access/example-costs/; https://help.openalex.org/access/pricing/

  结论与限制：执行者通过指定服务 OpenAlex 公共 API 真实检索（列表+过滤查询 resp1，按 DOI 单条核对 resp2，均 HTTP 200，响应头为 OpenAlex 限流头），取得唯一同时满足 2015、Nature、题名 Deep learning、作者含 Bengio 的正式记录；交付的题名、三位作者原序、年份、期刊与 DOI 链接均与冻结的出版社独立参考一致，作者无遗漏错序，DOI 指向同一论文，中文匹配说明与检索来源齐备。

<a id="comparison-e571efbd864f"></a>

### scholarly-access-001 v1

**crossref / public-rest-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; currentofficialkeylesspublicroute, no account/email/payment supplied; lowvolumebibliographicmetadata only

准备：Fresh anonymous access thenbusinesssessions, commonfrozenreadingnote/task/model/effort/generictools/time/requestlimits. SamebaseimageOpenCode1.18.35,DeepSeekFlash/high. Execution25requests/300saccessor600sbusiness;grading40requests/300s,32000outputtokens/request. Eachcontainer2GiB/1CPU,pids256; two providerstreams mayoverlap on16CPU/31.34GiBhost. Eachstage≤3APIrequests,oneatime,≥5secondsbetweenstarts; cacheidenticalqueries, truthfulprojectUA. No prewrittenservicecode or targetanswer. StandardCrossrefpublicpool(noemail) versusOpenAlexanonymousallowance(noKey), conditionsnotidenticalanddisclosed. BothmayuseCrossrefupstream; independentpublisherHTML/referencefrozenbeforequeries,neverhandedtoexecutor. ReturnedDOI/publisherlinkfollowup allowed equally. Gradersuseactualcapturedcalls, noextracandidateAPIqueries. OnefamousEnglishpaperlookup, nottopicsearch/fulltext/citationquality/generalcoverageranking.

- [crossref-scholarly-access-ds41-r1](../data/experiments/evaluations/crossref-scholarly-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 本次为公共免费路径，无现金费用；未使用需付费的 Metadata Plus。; https://www.crossref.org/documentation/retrieve-metadata/rest-api/ （官方文档：'All this metadata is openly shared with the global scholarly community through our free APIs'）; execution/artifacts/cache/headers.txt / headers3.txt （x-api-pool: public-array / public-single，匿名公共池）

  结论与限制：通过指定入口 https://api.crossref.org/works 完成真实文献查询，三次 HTTP 200 响应返回可识别记录（DOI 10.1038/sdata.2016.18，Scientific Data，2016），并以单条 DOI 接口复核；答复与采集响应一致；通用连接配置已写入指定持久位置 /home/node/service-tools/service-config.json，有效 JSON 且无秘密。全程匿名公共池、无注册/Key/付款、未加 mailto 或 polite/付费池，使用规定 UA，请求间隔≥5s、共 3 次，在时限内结束。

**openalex / public-rest-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; currentofficialkeylesspublicroute, no account/email/payment supplied; lowvolumebibliographicmetadata only

准备：Fresh anonymous access thenbusinesssessions, commonfrozenreadingnote/task/model/effort/generictools/time/requestlimits. SamebaseimageOpenCode1.18.35,DeepSeekFlash/high. Execution25requests/300saccessor600sbusiness;grading40requests/300s,32000outputtokens/request. Eachcontainer2GiB/1CPU,pids256; two providerstreams mayoverlap on16CPU/31.34GiBhost. Eachstage≤3APIrequests,oneatime,≥5secondsbetweenstarts; cacheidenticalqueries, truthfulprojectUA. No prewrittenservicecode or targetanswer. StandardCrossrefpublicpool(noemail) versusOpenAlexanonymousallowance(noKey), conditionsnotidenticalanddisclosed. BothmayuseCrossrefupstream; independentpublisherHTML/referencefrozenbeforequeries,neverhandedtoexecutor. ReturnedDOI/publisherlinkfollowup allowed equally. Gradersuseactualcapturedcalls, noextracandidateAPIqueries. OnefamousEnglishpaperlookup, nottopicsearch/fulltext/citationquality/generalcoverageranking.

- [openalex-scholarly-access-ds41-r1](../data/experiments/evaluations/openalex-scholarly-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 匿名无 Key 使用 OpenAlex 属免费层；未提供或使用任何账号、Key 或支付方式，未产生现金费用。本次消耗为免费额度：1 次搜索 $0.001（10 credits）+ 1 次单条 lookup $0（免费）。; https://help.openalex.org/access/pricing/; https://help.openalex.org/access/example-costs/; grading/artifacts/evidence/openalex_run_evidence.md

  结论与限制：执行者按指定入口 https://api.openalex.org/works 以匿名无 Key 方式完成 2 次真实 API 调用：1 次全文搜索（HTTP 200，返回 3 条含 OpenAlex ID/DOI 的可识别文献）与 1 次单条 lookup（免费），答复中的题名、标识与响应头数据与捕获响应一致。可复用配置写入持久目录 /home/node/service-tools/service-config.json（匿名、无 api_key），位置已在答复中报告并被 retained-files.json 记录。全程无需注册/付费/人工介入，符合免注册入口不强行注册的要求；未发现阻碍。

<a id="comparison-965a5e31dfe6"></a>

### financial-prices-001 v1

**alpha-vantage / hosted-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · controller-registered ordinary free API key; same existing account for REST and MCP

准备：Existing ordinary free account and key, two fresh route-specific runtimes, no prewritten service calls or prior answers. Serial REST then MCP execution; same frozen task/model/effort/time limits. Access300s/business600s/grading300s;25execution/40grading modelrequests,32000outputtokens/request. Free account25/day planned as shared by both routes based on official forwarding implementation, not live billing-counter proof;13knownprior calls, per-route access1/business3 financial request caps. Original prices/CSV/chart remain private; public measurements omit reconstructable market data. Explicit new environment: defaultpipindex https://pypi.tuna.tsinghua.edu.cn/simple set in /etc/pip.conf for all4newcontainers; same baseimage and initially emptycache, no additionalpreinstalledlibrary or service/plotcode. Additionalresourcechanges versus priorbatch: providerfinancialrequestcaps reduced from3access/5business to1access/3business due sharedquota; independentgradingmodelcap40 instead25,executioncap25 unchanged. PreviousoriginalPyPIfailedruns retained, newcohortneverpooledwithold norusedascontrolledcausalevidence. Same-provider route comparison, one sample each; no peer-results snapshot, no general protocol ranking. Independent reference is Nasdaq official close with calendar/issuer corroboration, never another candidate answer. Actual /etc/pip.conf SHA256 d4bcb0da1ab0fea5b2203d6b00cd570cb7f8bf357af86763a7d44d108a3709c5. Effectivepipconfig verified undertheworkers sterileenvironment asuid1000; no task-data prefetch. Beforebusiness, each newaccess usedonefinancialcall, total15knowncalls; actualremainingunknown. Controller archivedandremoved accessverificationmetadata from genericconfig, without addinginstructions/code/data; originalaccessconfig+artifacts+grades retained. Retentionaudit SHA256 96d995e4faa94f590851ee2345ff56af8587ff23da4abf9593eb079d888d3bd3.

- [alpha-mcp-prices-mirror-001-ds41-r1](../data/experiments/evaluations/alpha-mcp-prices-mirror-001-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Alpha Vantage 官方 premium 页面声明多数端点可免费使用、标准免费额度为 25 请求/日；ENVIRONMENT.md 指明本轮使用预置的普通免费账号。本轮业务阶段仅 1 次 TIME_SERIES_DAILY 数据请求，未使用 premium 端点/参数，未付款，故本次服务费用为 0。; https://www.alphavantage.co/premium/; execution/artifacts/ENVIRONMENT.md

  结论与限制：指定服务 Alpha Vantage 官方 MCP（https://mcp.alphavantage.co/mcp）经 JSON-RPC tools/call 调用 TIME_SERIES_DAILY(symbol=AAPL, outputsize=compact, datatype=json) 获取不复权日线，产出可打开的走势图、CSV 与可识别来源。CSV 21 行日期与冻结参考的 21 个常规交易日完全一致，无周末/重复/缺失；21 个收盘价逐行与参考序列在 USD 0.01 精度下完全一致；图表与 CSV 数值一致；未使用 REST、其他服务或模型记忆。业务阶段仅 1 次金融数据请求，位于免费额度内。

**alpha-vantage / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · controller-registered ordinary free API key; same existing account for REST and MCP

准备：Existing ordinary free account and key, two fresh route-specific runtimes, no prewritten service calls or prior answers. Serial REST then MCP execution; same frozen task/model/effort/time limits. Access300s/business600s/grading300s;25execution/40grading modelrequests,32000outputtokens/request. Free account25/day planned as shared by both routes based on official forwarding implementation, not live billing-counter proof;13knownprior calls, per-route access1/business3 financial request caps. Original prices/CSV/chart remain private; public measurements omit reconstructable market data. Explicit new environment: defaultpipindex https://pypi.tuna.tsinghua.edu.cn/simple set in /etc/pip.conf for all4newcontainers; same baseimage and initially emptycache, no additionalpreinstalledlibrary or service/plotcode. Additionalresourcechanges versus priorbatch: providerfinancialrequestcaps reduced from3access/5business to1access/3business due sharedquota; independentgradingmodelcap40 instead25,executioncap25 unchanged. PreviousoriginalPyPIfailedruns retained, newcohortneverpooledwithold norusedascontrolledcausalevidence. Same-provider route comparison, one sample each; no peer-results snapshot, no general protocol ranking. Independent reference is Nasdaq official close with calendar/issuer corroboration, never another candidate answer. Actual /etc/pip.conf SHA256 d4bcb0da1ab0fea5b2203d6b00cd570cb7f8bf357af86763a7d44d108a3709c5. Effectivepipconfig verified undertheworkers sterileenvironment asuid1000; no task-data prefetch. Beforebusiness, each newaccess usedonefinancialcall, total15knowncalls; actualremainingunknown. Controller archivedandremoved accessverificationmetadata from genericconfig, without addinginstructions/code/data; originalaccessconfig+artifacts+grades retained. Retentionaudit SHA256 96d995e4faa94f590851ee2345ff56af8587ff23da4abf9593eb079d888d3bd3.

- [alpha-rest-prices-mirror-001-ds41-r1](../data/experiments/evaluations/alpha-rest-prices-mirror-001-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: 独立验收的结构化kind写confirmed_free，但说明同时写“金额留未知”，数值字段为null。总控在公开录入时保守保留unknown，未按零计；原验收与其免费规则来源及哈希私有保留。任务完成结论与全部检查布尔值不变。; https://www.alphavantage.co/documentation/; grading/artifacts/evidence/summary.md

  结论与限制：执行者用指定入口 Alpha Vantage REST 的 TIME_SERIES_DAILY（AAPL, outputsize=compact，不复权原始日线）发起 1 次业务请求，产出可打开的 PNG 走势图与 CSV。独立核对：CSV 含 2026-08 全部 21 个常规交易日，无重复、缺失、周末/休市日脏数据；21/21 收盘价与冻结参考在 USD 0.01 精度上完全一致；图表为有效非空 PNG 且由同一 CSV 生成；来源与不复权口径可识别；未用 MCP、未调用付费端点、未泄漏 Key。

<a id="comparison-29077cd73ecd"></a>

### financial-access-001 v1

**alpha-vantage / hosted-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · controller-registered ordinary free API key; same existing account for REST and MCP

准备：Existing ordinary free account and key, two fresh route-specific runtimes, no prewritten service calls or prior answers. Serial REST then MCP execution; same frozen task/model/effort/time limits. Access300s/business600s/grading300s;25execution/40grading modelrequests,32000outputtokens/request. Free account25/day planned as shared by both routes based on official forwarding implementation, not live billing-counter proof;13knownprior calls, per-route access1/business3 financial request caps. Original prices/CSV/chart remain private; public measurements omit reconstructable market data. Explicit new environment: defaultpipindex https://pypi.tuna.tsinghua.edu.cn/simple set in /etc/pip.conf for all4newcontainers; same baseimage and initially emptycache, no additionalpreinstalledlibrary or service/plotcode. Additionalresourcechanges versus priorbatch: providerfinancialrequestcaps reduced from3access/5business to1access/3business due sharedquota; independentgradingmodelcap40 instead25,executioncap25 unchanged. PreviousoriginalPyPIfailedruns retained, newcohortneverpooledwithold norusedascontrolledcausalevidence. Same-provider route comparison, one sample each; no peer-results snapshot, no general protocol ranking. Independent reference is Nasdaq official close with calendar/issuer corroboration, never another candidate answer. Actual /etc/pip.conf SHA256 d4bcb0da1ab0fea5b2203d6b00cd570cb7f8bf357af86763a7d44d108a3709c5. Effectivepipconfig verified undertheworkers sterileenvironment asuid1000; no task-data prefetch.

- [alpha-mcp-prices-mirror-access-ds41-r1](../data/experiments/evaluations/alpha-mcp-prices-mirror-access-ds41-r1.json)：模型费用 $0.03；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: 本次使用总控事前提供的 Alpha Vantage 免费账号，仅调用核心行情端点 GLOBAL_QUOTE 一次，执行者未付款。但未采集到服务商计费回执，官方文档页仅提示可获取 free API key，未列出费率/免费定价规则文本，无法独立确认该调用在计费上免费，故保留 unknown，不按零计。

  结论与限制：指定入口 https://mcp.alphavantage.co/mcp (streamable-http) 接通：initialize 返回 serverInfo alphavantage-mcp-server 1.0.0，tools/list 返回 133 个工具；使用本轮提供的 API key（credentials.json 的 api_key）经 URL 查询参数 ?apikey= 认证，成功调用一次 GLOBAL_QUOTE(symbol=IBM) 并取得真实行情（200，最新交易日 2026-10-07，price [market value retained privately]）。可复用连接配置已写入持久位置 /home/node/service-tools/service-config.json（执行回执 retained-files.json 确认保留），密钥只留 credentials.json、配置内用占位符、答复未含密钥。账号为总控事前提供的普通免费账号，本次非自主注册；全过程无人工介入。仅调用 1 次金融数据请求（接入额度 1/1），未用 REST 或他服务代替，未付费、未调用付费端点。

**alpha-vantage / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · controller-registered ordinary free API key; same existing account for REST and MCP

准备：Existing ordinary free account and key, two fresh route-specific runtimes, no prewritten service calls or prior answers. Serial REST then MCP execution; same frozen task/model/effort/time limits. Access300s/business600s/grading300s;25execution/40grading modelrequests,32000outputtokens/request. Free account25/day planned as shared by both routes based on official forwarding implementation, not live billing-counter proof;13knownprior calls, per-route access1/business3 financial request caps. Original prices/CSV/chart remain private; public measurements omit reconstructable market data. Explicit new environment: defaultpipindex https://pypi.tuna.tsinghua.edu.cn/simple set in /etc/pip.conf for all4newcontainers; same baseimage and initially emptycache, no additionalpreinstalledlibrary or service/plotcode. Additionalresourcechanges versus priorbatch: providerfinancialrequestcaps reduced from3access/5business to1access/3business due sharedquota; independentgradingmodelcap40 instead25,executioncap25 unchanged. PreviousoriginalPyPIfailedruns retained, newcohortneverpooledwithold norusedascontrolledcausalevidence. Same-provider route comparison, one sample each; no peer-results snapshot, no general protocol ranking. Independent reference is Nasdaq official close with calendar/issuer corroboration, never another candidate answer. Actual /etc/pip.conf SHA256 d4bcb0da1ab0fea5b2203d6b00cd570cb7f8bf357af86763a7d44d108a3709c5. Effectivepipconfig verified undertheworkers sterileenvironment asuid1000; no task-data prefetch.

- [alpha-rest-prices-mirror-access-ds41-r1](../data/experiments/evaluations/alpha-rest-prices-mirror-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Alpha Vantage 官方文档区分 free 与 premium API key，并指引领取免费 API key；本次使用的 GLOBAL_QUOTE 未标 Premium（行情端点的 realtime 部分才需 premium），调用无任何计费回执。; https://www.alphavantage.co/documentation/

  结论与限制：经指定 REST 入口 https://www.alphavantage.co/query 完成一次真实金融数据查询（function=GLOBAL_QUOTE&symbol=IBM，HTTP 200，返回有效报价），并把可复用连接配置写入持久目录且未泄露密钥。使用本轮提供的既有免费账号，未自主注册、未用 MCP、未触碰付费端点或付款；无阻碍。

<a id="comparison-c820e750045c"></a>

### geocoding-venue-001 v1

**photon / public-search-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; official low-volume public route selected deliberately for one public-venue research task

准备：Fresh access then business sessions. Same frozen venue task,model/effort/generic tools/limits. Execution25modelrequests,access300s/business600s;grading40requests/300s;32000outputtokens/request. Two provider runtimes may overlap on shared16CPU/31.34GiB host,each2GiB/1CPU;one serial stream per APIhost,4calls/phase max and15s spacing,cache same query. Truthful projectUA supplied, no targetanswer or callscript. Generic setup inspected between sessions; all business data cleared. Graders use actual captured execution request/response and independent official venue reference; no extra candidate APIcalls. Both services shareOSM, so agreement is not independent geographic truth. One publicvenue,place-level mapmarking only, no entrance navigation or general geocoding accuracy claim. PublicOSMF policy explicitly linked/explained; not a generic arbitrary-query platform or recurring bulk geocoder.

- [photon-geocoding-venue-001-ds41-r1](../data/experiments/evaluations/photon-geocoding-venue-001-ds41-r1.json)：模型费用 $0.0090；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 未提供付费账号/Key，也无付费入口；本次对指定入口的查询未附任何认证或支付信息。; https://photon.komoot.io/ (official Terms of Use); execution/artifacts/ENVIRONMENT.md

  结论与限制：本次真实调用冻结指定服务 Photon（https://photon.komoot.io/api/）并命中伦敦大英博物馆场馆对象（R 177044, tourism=museum），答复给出的 WGS84 纬度 51.5193118 / 经度 -0.1267051 与响应一致、轴序正确，距冻结官方场馆点约 20.7 m（≤200 m），并完整披露返回地址、来源与场馆级粒度，未把街道对象冒充场馆。

<a id="comparison-d21a9019050d"></a>

### geocoding-access-001 v1

**nominatim / public-search-api** — 0 完成 / 0 未完成 / 1 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; official low-volume public route selected deliberately for one public-venue research task

准备：Fresh access then business sessions. Same frozen venue task,model/effort/generic tools/limits. Execution25modelrequests,access300s/business600s;grading40requests/300s;32000outputtokens/request. Two provider runtimes may overlap on shared16CPU/31.34GiB host,each2GiB/1CPU;one serial stream per APIhost,4calls/phase max and15s spacing,cache same query. Truthful projectUA supplied, no targetanswer or callscript. Generic setup inspected between sessions; all business data cleared. Graders use actual captured execution request/response and independent official venue reference; no extra candidate APIcalls. Both services shareOSM, so agreement is not independent geographic truth. One publicvenue,place-level mapmarking only, no entrance navigation or general geocoding accuracy claim. PublicOSMF policy explicitly linked/explained; not a generic arbitrary-query platform or recurring bulk geocoder.

- [nominatim-geocoding-access-ds41-r1](../data/experiments/evaluations/nominatim-geocoding-access-ds41-r1.json)：模型费用 —；Per-request usage capture is incomplete. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；confirmed_free: 公共 OSM Nominatim 为捐赠运行的免费公开服务，无账号/Key/付费机制；本次无计费回执。本次因环境网络失败未发出成功请求，故无实际用量金额。; https://operations.osmfoundation.org/policies/nominatim/

  结论与限制：执行环境无法连通指定入口 https://nominatim.openstreetmap.org/search：DNS 把 nominatim.openstreetmap.org 解析为与 OSM 无关的轮换 IP（含 Facebook 段 2a03:2880:...:face:b00c...、31.13.84.2 等），urllib/curl/webfetch 对该入口的连接一律超时或 Network unreachable；同一容器内 example.com、api.github.com、nominatim.org、operations.osmfoundation.org 均 HTTP 200，而 www.openstreetmap.org、www.google.com 同为 HTTP 000，指向容器级 DNS/出口限制。工作目录未产生 result.json 或 cache，last_request.json 仅记录一次尝试；会话在约 290 秒时被超时终止（exit_code=-15, timed_out=true），answer.md 仅剩未完成片段。核心阻碍属于执行环境网络（DNS/出口）而非服务能力、接入门槛或执行者行为，故记 invalid_run；未做接入补测。

<a id="comparison-3bcbfb46bd35"></a>

### geocoding-access-001 v1

**photon / public-search-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; official low-volume public route selected deliberately for one public-venue research task

准备：Fresh access then business sessions. Same frozen venue task,model/effort/generic tools/limits. Execution25modelrequests,access300s/business600s;grading40requests/300s;32000outputtokens/request. Two provider runtimes may overlap on shared16CPU/31.34GiB host,each2GiB/1CPU;one serial stream per APIhost,4calls/phase max and15s spacing,cache same query. Truthful projectUA supplied, no targetanswer or callscript. Generic setup inspected between sessions; all business data cleared. Graders use actual captured execution request/response and independent official venue reference; no extra candidate APIcalls. Both services shareOSM, so agreement is not independent geographic truth. One publicvenue,place-level mapmarking only, no entrance navigation or general geocoding accuracy claim. PublicOSMF policy explicitly linked/explained; not a generic arbitrary-query platform or recurring bulk geocoder.

- [photon-geocoding-access-ds41-r1](../data/experiments/evaluations/photon-geocoding-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: komoot 托管的官方公开 Photon demo，免注册、无 Key、无支付、无计费入口。; https://photon.komoot.io/; https://github.com/komoot/photon

  结论与限制：执行者对指定服务 photon（komoot 官方托管 demo）经指定入口 https://photon.komoot.io/api/ 完成 1 次真实正向地理编码查询，返回可识别公开地点 Eiffel Tower (Paris, FR) 与有效且标注正确的经纬度，来自 OpenStreetMap；答复与原始响应一致，持久配置已保存并报告路径且不含秘密，接入步骤与阻碍如实说明。免注册路径未强行注册，未付费，未换服务。

<a id="comparison-728ca7b6aa38"></a>

### weather-outing-001 v1

**met-norway / locationforecast-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; official public read-only free noncommercial route · 独立验收可参考同期 2 份同题答案

准备：Fresh access then business sessions. Same frozen weather task,model/effort/generic tools and budgets for both routes. Execution25modelrequests,access300s/business600s;independent grading40modelrequests/300s after prior search grader exhausted25, no service execution budget increase.32000outputtokens/request. Two providers can run concurrently on shared16CPU/31.34GiB host;eachruntime2GiB/1CPU. ProjectUser-Agent/contact preprovided, no account/key or answer supplied.10weatherdatareads/phase maximum subject to officialcache/rate limits. Controller method/source snapshots and two private before-business publicGETreceipts are separate overhead and grader-only. Each actual query-time forecast is its own evidence; no cross-provider numerical truth, commonupstream possible, no forecastskill/reliabilityranking. Generic setup retention inspected, no business data carried over.

- [met-norway-weather-outing-001-ds41-r1](../data/experiments/evaluations/met-norway-weather-outing-001-ds41-r1.json)：模型费用 $0.0088；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 开放许可的免费公共天气 API，本次单次 GET 无付费凭据与回执，计服务费为 0。; https://docs.api.met.no/doc/License.html; https://docs.api.met.no/doc/TermsOfService.html

  结论与限制：指定服务 MET Norway Locationforecast 2.0 compact 实际被调用，独立解压执行者保存的真实响应并按用户时区重新提取，得到当地 09:00–10:00 / 10:00–11:00 / 11:00–12:00 三个整点区间：气温 10.6 / 11.8 / 13.0 °C（区间起始整点 instant.air_temperature），整小时累计降水 0.0 / 0.0 / 0.0 mm（同一时刻 next_1_hours.precipitation_amount），与交付表一致；单位、时区、来源署名、查询时间与降水说明均可核对，无缺失或均摊。

**open-meteo / forecast-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; official public read-only free noncommercial route · 独立验收可参考同期 2 份同题答案

准备：Fresh access then business sessions. Same frozen weather task,model/effort/generic tools and budgets for both routes. Execution25modelrequests,access300s/business600s;independent grading40modelrequests/300s after prior search grader exhausted25, no service execution budget increase.32000outputtokens/request. Two providers can run concurrently on shared16CPU/31.34GiB host;eachruntime2GiB/1CPU. ProjectUser-Agent/contact preprovided, no account/key or answer supplied.10weatherdatareads/phase maximum subject to officialcache/rate limits. Controller method/source snapshots and two private before-business publicGETreceipts are separate overhead and grader-only. Each actual query-time forecast is its own evidence; no cross-provider numerical truth, commonupstream possible, no forecastskill/reliabilityranking. Generic setup retention inspected, no business data carried over.

- [open-meteo-weather-outing-001-ds41-r1](../data/experiments/evaluations/open-meteo-weather-outing-001-ds41-r1.json)：模型费用 $0.0042；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Open-Meteo 非商业免费公共 Forecast API：官方文档标注 Usage licence 分 Non-Commercial/Commercial，apikey 仅商业用途需要；ENVIRONMENT.md 冻结本轮为非商业研究、使用已确认免费的只读公共资源且未提供账号/Key。本次以无 key 公共请求访问 /v1/forecast 得到 HTTP 200，未付款、未绑定支付方式。; execution/artifacts/ENVIRONMENT.md; execution/artifacts/headers.txt; reference-sources/open-meteo-forecast-docs-20261008.html

  结论与限制：本次执行通过指定服务 Open-Meteo Forecast API 入口 https://api.open-meteo.com/v1/forecast 真实取得 2026-10-10 伦敦市中心坐标 51.5074,-0.1278 的小时预报（HTTP 200，查询时间 2026-10-08 14:54 UTC / 当地 15:54 Europe/London UTC+1）。交付的中文小表对 09:00–10:00、10:00–11:00、11:00–12:00 三个当地整点小时区间，按区间起始整点取近地面气温 11.3/12.0/13.3 °C，按该小时累计总降水取 0.0/0.0/0.0 mm，与当次响应逐值一致，时区、单位、温度时点与降水区间均正确，来源、署名与含时区查询时间齐备，降水说明与数据相符，无缺失/填造。

<a id="comparison-7e7df525d550"></a>

### weather-access-001 v1

**met-norway / locationforecast-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; official public read-only free noncommercial route

准备：Fresh access then business sessions. Same frozen weather task,model/effort/generic tools and budgets for both routes. Execution25modelrequests,access300s/business600s;independent grading40modelrequests/300s after prior search grader exhausted25, no service execution budget increase.32000outputtokens/request. Two providers can run concurrently on shared16CPU/31.34GiB host;eachruntime2GiB/1CPU. ProjectUser-Agent/contact preprovided, no account/key or answer supplied.10weatherdatareads/phase maximum subject to officialcache/rate limits. Controller method/source snapshots and two private before-business publicGETreceipts are separate overhead and grader-only. Each actual query-time forecast is its own evidence; no cross-provider numerical truth, commonupstream possible, no forecastskill/reliabilityranking. Generic setup retention inspected, no business data carried over.

- [met-norway-weather-access-ds41-r1](../data/experiments/evaluations/met-norway-weather-access-ds41-r1.json)：模型费用 $0.0082；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 服务为公开开放数据接口，本次使用落在免费范围内；无费用回执，故 service_cost_usd 保持 null。; https://docs.api.met.no/doc/License.html; https://docs.api.met.no/doc/TermsOfService.html

  结论与限制：执行者通过指定入口 MET Norway Locationforecast 2.0 compact 对公开地点 Oslo (59.9139N, 10.7522E) 完成了一次真实、无 Key 的天气查询，HTTP 200 返回 84 个时次数据；答案中的地点、时间、数值与单位（7.0 °C、81.8 %、6.5 m/s、9.0°、1003.3 hPa、updated_at 2026-10-08T14:29:23Z 等）与采集到的 forecast.json 逐项一致。通用连接配置已写入持久目录 /home/node/service-tools/service-config.json（auth: none，无秘密），运行器 retained-files 记录其被保留，可跨会话复用。入口免注册，执行者未强行注册，无人工介入或额外申请；客户端标识、四位坐标、gzip 与缓存/署名要求均符合服务条款。仅 1 次天气 API 读取，未 HEAD+GET，未换服务。

**open-meteo / forecast-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; official public read-only free noncommercial route

准备：Fresh access then business sessions. Same frozen weather task,model/effort/generic tools and budgets for both routes. Execution25modelrequests,access300s/business600s;independent grading40modelrequests/300s after prior search grader exhausted25, no service execution budget increase.32000outputtokens/request. Two providers can run concurrently on shared16CPU/31.34GiB host;eachruntime2GiB/1CPU. ProjectUser-Agent/contact preprovided, no account/key or answer supplied.10weatherdatareads/phase maximum subject to officialcache/rate limits. Controller method/source snapshots and two private before-business publicGETreceipts are separate overhead and grader-only. Each actual query-time forecast is its own evidence; no cross-provider numerical truth, commonupstream possible, no forecastskill/reliabilityranking. Generic setup retention inspected, no business data carried over.

- [open-meteo-weather-access-ds41-r1](../data/experiments/evaluations/open-meteo-weather-access-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 服务侧无计费回执；免费规则来自官方定价页与本轮环境授权，本次查询完全落在免费非商业额度内。; https://open-meteo.com/en/pricing; frozen-execution/ENVIRONMENT.md

  结论与限制：通过指定入口 https://api.open-meteo.com/v1/forecast 完成一次真实天气查询，响应含可识别地点、有效观测时间、数值与单位，答复与响应一致；免注册无鉴权，接入配置已写入持久目录且不含秘密；无人工介入或额外申请，服务为官方非商业免费公共 Forecast API，未付费。

<a id="comparison-f351c20d0bf2"></a>

### web-search-001 v2

**exa / public-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; documented anonymous public route · 独立验收可参考同期 2 份同题答案

准备：Fresh access and business sessions. Same new v2 business request, model/effort/limits and generic tools; no prewritten calls, answer URLs or reference given to executor. Exa anonymous hosted MCP vs Firecrawl anonymous REST search; specific route comparison, one sample, not interface ranking. Two providers may execute concurrently on shared server/network (16 logical CPUs,31.34GiB RAM); per-runtime2GiB/1CPU. Anonymous IP quota remainder unknown; no paid fallback. Business600s/access300s/grading300s,25modelrequests/role,32000outputtokens/request. Priorv1 unchanged and excluded from v2 averages. Generic setup retention inspected before business. Independent source snapshots and peer execution answers frozen before isolated grading; peer grades never shared.

- [exa-search-001v2-ds41-r1](../data/experiments/evaluations/exa-search-001v2-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 未产生计费回执；使用 exa keyless 匿名免费限流额度，无 API key/OAuth/付费。; https://exa.ai/docs/reference/exa-mcp

  结论与限制：执行者通过本轮指定的 exa 官方匿名远程 MCP（入口 https://mcp.exa.ai/mcp，keyless 无鉴权）实际调用 web_search_exa / web_fetch_exa 发现并读取 python.org 官方来源，用中文正确回答了三个问题（自由线程默认未启用、需用 free-threaded 构建/--disable-gil 启用、C 扩展需专门构建并显式声明否则回退启用 GIL），并给出可追溯到 exa 搜索结果的官方页面链接。三个结论均有官方文档支持，无版本混淆，未使用其他搜索引擎或模型记忆替代来源发现。

**firecrawl / public-search-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; documented anonymous public route · 独立验收可参考同期 2 份同题答案

准备：Fresh access and business sessions. Same new v2 business request, model/effort/limits and generic tools; no prewritten calls, answer URLs or reference given to executor. Exa anonymous hosted MCP vs Firecrawl anonymous REST search; specific route comparison, one sample, not interface ranking. Two providers may execute concurrently on shared server/network (16 logical CPUs,31.34GiB RAM); per-runtime2GiB/1CPU. Anonymous IP quota remainder unknown; no paid fallback. Business600s/access300s/grading300s,25modelrequests/role,32000outputtokens/request. Priorv1 unchanged and excluded from v2 averages. Generic setup retention inspected before business. Independent source snapshots and peer execution answers frozen before isolated grading; peer grades never shared.

- [firecrawl-search-001v2-ds41-r1](../data/experiments/evaluations/firecrawl-search-001v2-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 匿名 Search API，本次无回执金额、无账号与支付方式；结论为免费，而非按量估算。; execution/artifacts/ENVIRONMENT.md; https://docs.firecrawl.dev/features/search; execution/artifacts/result1.json

  结论与限制：本次执行真实调用了指定服务 firecrawl 的匿名 Search API（https://api.firecrawl.dev/v2/search，4 次 POST 均 HTTP 200、success=true、creditsUsed=2），检索域限定 python.org/docs.python.org，并用返回结果直接读取官方页面。execution/answer.md 与 execution/artifacts/answer.md 用中文分别回答了默认状态（3.13 实验性，未默认启用，需 python3.13t 单独可执行文件）、启用方式（Windows/macOS 可选组件或源码 --disable-gil，运行时 PYTHON_GIL 或 -X gil，识别方法）与 C 扩展兼容性限制（须专门构建、须用 Py_mod_gil/PyUnstable_Module_SetGIL 声明、不支持 Limited C API/stable ABI、借用引用与无锁宏风险等），三个结论均可在所读 3.13 官方页面中逐条核对，版本为 3.13 无混淆，官方链接与结论对应且可追溯到本次搜索结果或返回页面的官方内链。环境有效、exit_code=0、未超时。

<a id="comparison-5244b7150d7c"></a>

### web-search-access-001 v1

**exa / public-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; documented anonymous public route

准备：Fresh access and business sessions. Same new v2 business request, model/effort/limits and generic tools; no prewritten calls, answer URLs or reference given to executor. Exa anonymous hosted MCP vs Firecrawl anonymous REST search; specific route comparison, one sample, not interface ranking. Two providers may execute concurrently on shared server/network (16 logical CPUs,31.34GiB RAM); per-runtime2GiB/1CPU. Anonymous IP quota remainder unknown; no paid fallback. Business600s/access300s/grading300s,25modelrequests/role,32000outputtokens/request. Priorv1 unchanged and excluded from v2 averages. Generic setup retention inspected before business. Independent source snapshots and peer execution answers frozen before isolated grading; peer grades never shared.

- [exa-searchv2-access-ds41-r1](../data/experiments/evaluations/exa-searchv2-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 本次仅使用 Exa 官方匿名 keyless 入口，未注册、未付费、未使用 API key。; https://exa.ai/docs/reference/exa-mcp; execution/artifacts/search-result.raw.json

  结论与限制：执行者按官方指定入口 https://mcp.exa.ai/mcp 以 keyless 方式完成 MCP 接入：initialize 握手 200（exa-search-server 3.2.1，协议 2025-06-18），tools/list 列出 web_search_exa/web_fetch_exa，并以 web_search_exa 做了一次真实搜索，返回含标题与有效 URL 的结果（Python 3.13.0 (final) released \| Python Insider，https://blog.python.org/2024/10/python-3130-final-released/，已独立复核可访问）。连接配置写入持久目录 /home/node/service-tools/service-config.json 且不含秘密，答复与响应一致并如实说明免注册、自助步骤与一处 403 阻碍。无人类介入，服务按官方 keyless 免费限流规则使用。

**firecrawl / public-search-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; documented anonymous public route

准备：Fresh access and business sessions. Same new v2 business request, model/effort/limits and generic tools; no prewritten calls, answer URLs or reference given to executor. Exa anonymous hosted MCP vs Firecrawl anonymous REST search; specific route comparison, one sample, not interface ranking. Two providers may execute concurrently on shared server/network (16 logical CPUs,31.34GiB RAM); per-runtime2GiB/1CPU. Anonymous IP quota remainder unknown; no paid fallback. Business600s/access300s/grading300s,25modelrequests/role,32000outputtokens/request. Priorv1 unchanged and excluded from v2 averages. Generic setup retention inspected before business. Independent source snapshots and peer execution answers frozen before isolated grading; peer grades never shared.

- [firecrawl-searchv2-access-ds41-r1](../data/experiments/evaluations/firecrawl-searchv2-access-ds41-r1.json)：模型费用 $0.0082；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 无账单回执；本次为官方匿名免费入口，未使用付费额度。金额缺失不按零，service_cost_usd 留空由脚本处理。; frozen-execution/ENVIRONMENT.md：指定服务 firecrawl，仅用官方匿名免费入口，通过 https://api.firecrawl.dev/v2/search 完成搜索；匿名免费额度受每 IP 每日请求数与 credits 双上限约束，未提供账号/密钥/支付方式; https://docs.firecrawl.dev/features/search：无需 API key 即可开始使用（No API key needed to get started）

  结论与限制：执行者用指定服务 firecrawl 的官方匿名 REST 入口 POST https://api.firecrawl.dev/v2/search 完成了真实网页搜索：查询 `how to bake sourdough bread` 返回 success:true、creditsUsed:2，含标题与有效 URL 的结果，答复与实际响应一致。可复用连接配置已写入指定持久目录 /home/node/service-tools/service-config.json（纯匿名、无秘密）。全程无注册、无人工介入或额外申请，符合授权范围。

<a id="comparison-892c10c8ee63"></a>

### collaborative-tables-001 v4

**grist / hosted-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · provided: existing Grist Personal account; new empty parent workspace prepared by controller

准备：Same existing Personal account and API key, two distinct newly created empty parent workspaces, fresh route-specific containers. Account registration and controller parent provisioning precede measured access; executor must create and read its own empty document. Serial REST then MCP execution avoids shared-account quota interference. No prewritten calls or business data. OpenCode 1.18.35 / DeepSeek V4.1 Flash high; 25 requests per role, 32000 output-token cap per request, access300s/business600s/grading300s. One sample per route, no cross-service or general protocol ranking. No peer snapshot: same-provider routes use separate independent grading. Controller GET-only remote verification is separate overhead; backend API counts behind MCP are unknown.

- [grist-mcp-tables-001v4-ds41-r1](../data/experiments/evaluations/grist-mcp-tables-001v4-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Grist Free(Personal) 计划不产生费用；独立回执中账户 product_name=personalFree、stripePlanId 为空、inGoodStanding=true，本次仅 5 次 MCP 调用，远低于 Free 3000 次/月额度上限。未取得剩余额度，但账户处于免费、无付费订阅状态。 Publication review supplements the same fee conclusion with actual non-identifying plan fields from unchanged controller GET bytes; it is not inferred solely from the Personal name or a free-only instruction.; https://support.getgrist.com/limits/#api-limits; controller-verification/entitlement.json; public-review/verification.json — actual controller GET metadata product.name=personalFree; remaining monthly usage unknown

  结论与限制：Grist hosted-MCP 执行在预留空文档内新建 Tasks 表并写入 3 行；总控在执行结束后独立只读 API 取回文档/表/字段/全部记录，远端恰好三项且与输入一致，答复链接指向该文档，未完成清单正确。资源、请求与免费额度约束均满足。

**grist / rest-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · provided: existing Grist Personal account; new empty parent workspace prepared by controller

准备：Same existing Personal account and API key, two distinct newly created empty parent workspaces, fresh route-specific containers. Account registration and controller parent provisioning precede measured access; executor must create and read its own empty document. Serial REST then MCP execution avoids shared-account quota interference. No prewritten calls or business data. OpenCode 1.18.35 / DeepSeek V4.1 Flash high; 25 requests per role, 32000 output-token cap per request, access300s/business600s/grading300s. One sample per route, no cross-service or general protocol ranking. No peer snapshot: same-provider routes use separate independent grading. Controller GET-only remote verification is separate overhead; backend API counts behind MCP are unknown.

- [grist-rest-tables-001v4-ds41-r1](../data/experiments/evaluations/grist-rest-tables-001v4-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 无付款回执。账号套餐为 personalFree（免费档），免费档包含 REST API 且仅受每月 3,000 次共享调用额度限制，无按次费用；本轮执行约 13 次业务调用 + 总控 7 次只读读取，远低于额度。故确认免费，金额为 $0，无实付/估算支出。 Publication review supplements the same fee conclusion with actual non-identifying plan fields from unchanged controller GET bytes; it is not inferred solely from the Personal name or a free-only instruction.; https://support.getgrist.com/limits/; grading/artifacts/evidence/free-plan-usage.md; public-review/verification.json — actual controller GET metadata product.name=personalFree; remaining monthly usage unknown

  结论与限制：本轮唯一执行入口为 Grist REST API，任务在总控预建并授权的工作区/文档内完成。总控在执行结束后（13:49:48 > 13:49:39）以只读 GET 独立重读，冻结回执完整（controller-verification/manifest.json，complete=true），Tasks 表恰有 3 条记录，字段、内容、日期、完成状态与期望一致；答复链接指向承载该表的文档（urlId [SERVICE_SECRET]），未完成清单为确认场地/林青/2026-09-15 与 制作海报/陈禾/2026-09-20，与远端一致。资源约束满足：1 个业务表、3 行、约 13 次业务调用（<40）、工作区仅 1 个文档，无分享/邀请/通知/付费。账号/密钥/空工作区由总控预建并授权（非本轮自主注册，已提供账号），执行阶段无人工介入。服务费用按 Grist Free(personalFree) 免费档确认免费（见 evidence/free-plan-usage.md）。

<a id="comparison-5bcdeb33cbc4"></a>

### collaborative-tables-access-001 v1

**grist / hosted-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · provided: existing Grist Personal account; new empty parent workspace prepared by controller

准备：Same existing Personal account and API key, two distinct newly created empty parent workspaces, fresh route-specific containers. Account registration and controller parent provisioning precede measured access; executor must create and read its own empty document. Serial REST then MCP execution avoids shared-account quota interference. No prewritten calls or business data. OpenCode 1.18.35 / DeepSeek V4.1 Flash high; 25 requests per role, 32000 output-token cap per request, access300s/business600s/grading300s. One sample per route, no cross-service or general protocol ranking. No peer snapshot: same-provider routes use separate independent grading. Controller GET-only remote verification is separate overhead; backend API counts behind MCP are unknown.

- [grist-mcp-access-ds41-r1](../data/experiments/evaluations/grist-mcp-access-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 使用预提供的 Grist Personal 免费账号，仅在免费权限内新建一个空文档并做 MCP 读取，未购买/绑卡/开超额；无服务账单回执。controller-verification/manifest.json 记录 free-plan applicability 依据账号/准备证据确定且未从 HTTP 成功推断计费。故判为 confirmed_free，未产生需上报金额。 Publication review supplements the same fee conclusion with actual non-identifying plan fields from unchanged controller GET bytes; it is not inferred solely from the Personal name or a free-only instruction.; https://support.getgrist.com/limits/; frozen-execution/ENVIRONMENT.md; controller-verification/manifest.json; public-review/verification.json — actual controller GET metadata product.name=personalFree; remaining monthly usage unknown

  结论与限制：执行者通过指定官方托管 MCP https://docs.getgrist.com/api/mcp（initialize 2025-06-18 -> notifications/initialized -> tools/call）在授权工作区 [SERVICE_SECRET] 内新建唯一空文档 [SERVICE_SECRET]（id [SERVICE_SECRET]），并用 grist_get_doc_info 重新读取到 id/name/workspace 一致的同一远端资源；独立 controller 读取（read_after_execution）确认该工作区仅此一个文档、仅含默认占位表 Table1（A/B/C）、0 条记录。连接配置保存在持久目录 /home/node/service-tools/service-config.json（无密钥，密钥仍在 credentials.json），答复只给配置位置并给出链接。账号为预提供的既有 Personal 免费账号，非本轮注册；免费限制与官方 limits 页面一致，剩余额度如实记为未知。未发现越权、预建业务数据、泄露凭据或改用 REST 代做的情况。

**grist / rest-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · provided: existing Grist Personal account; new empty parent workspace prepared by controller

准备：Same existing Personal account and API key, two distinct newly created empty parent workspaces, fresh route-specific containers. Account registration and controller parent provisioning precede measured access; executor must create and read its own empty document. Serial REST then MCP execution avoids shared-account quota interference. No prewritten calls or business data. OpenCode 1.18.35 / DeepSeek V4.1 Flash high; 25 requests per role, 32000 output-token cap per request, access300s/business600s/grading300s. One sample per route, no cross-service or general protocol ranking. No peer snapshot: same-provider routes use separate independent grading. Controller GET-only remote verification is separate overhead; backend API counts behind MCP are unknown.

- [grist-rest-access-ds41-r1](../data/experiments/evaluations/grist-rest-access-ds41-r1.json)：模型费用 $0.0100；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 无付款回执，按免费计划字段与官方免费规则判定为免费；本轮实际剩余额度未知。 Publication review supplements the same fee conclusion with actual non-identifying plan fields from unchanged controller GET bytes; it is not inferred solely from the Personal name or a free-only instruction.; [official_doc] https://support.getgrist.com/limits/ — Free plans 限 3,000 API calls/month shared；免费计划各项限额; [api_response] grading/artifacts/evidence/service-plan.txt — 账号 API 响应显示 product.name=personalFree、stripePlanId=null、未绑卡; public-review/verification.json — actual controller GET metadata product.name=personalFree; remaining monthly usage unknown

  结论与限制：执行者通过指定入口 Grist REST API（https://docs.getgrist.com/api）在授权工作区 [SERVICE_SECRET] 内新建了唯一空文档 [SERVICE_SECRET]（docId [SERVICE_SECRET]），并重新 GET 回读该同一远端资源确认可访问；独立采集的 controller-verification 读回与答复中的链接/标识一致，容器内无业务字段或记录（仅默认空白占位表 Table1，0 行）。非秘密配置已写入指定持久目录，密钥仅留私有文件，答复不含密钥；账号来源（总控预先提供、非自主注册）、自助步骤、人工门槛与免费限制如实说明，未列出的剩余额度记为未知。

<a id="comparison-032f75889210"></a>

### web-extraction-holidays-001 v1

**exa / public-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none · 独立验收可参考同期 2 份同题答案

准备：Passed independent access; fresh session/workspace keeps only connection configuration and dependencies. Same frozen task, DeepSeek Flash/high, OpenCode1.18.35, execution600s/grading300s and25 modelrequests/role for all services. Anonymous routes and provider cache/format defaults differ and must be reported. Reference values withheld from execution. Jina access retry recovered from controller interruption, not a service failure.

- [exa-extraction-holidays-001-ds41-r1](../data/experiments/evaluations/exa-extraction-holidays-001-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Exa 匿名 MCP 免 Key 限流额度内使用，无付费；$10 free credits/付费 API 未启用。; https://exa.ai/docs/get-started/exa-mcp; grading/artifacts/evidence/exa-mcp-2027-fetch.md

  结论与限制：目标 2027 Holiday Schedule 表由指定 Exa 匿名 MCP 的 web_fetch_exa 真实取得（keyless，无 Key），返回文本含逐行日期与假日；交付 CSV 为 UTF-8、列 date,weekday,holiday，11 行与官方表中公布值逐项一致、日期升序、无脚注/重复/其他年份，答复给出文件位置与官方来源链接。

**firecrawl / public-scrape-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none · 独立验收可参考同期 2 份同题答案

准备：Passed independent access; fresh session/workspace keeps only connection configuration and dependencies. Same frozen task, DeepSeek Flash/high, OpenCode1.18.35, execution600s/grading300s and25 modelrequests/role for all services. Anonymous routes and provider cache/format defaults differ and must be reported. Reference values withheld from execution. Jina access retry recovered from controller interruption, not a service failure.

- [firecrawl-extraction-holidays-001-ds41-r1](../data/experiments/evaluations/firecrawl-extraction-holidays-001-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 本次仅有匿名免费调用，无付费回执或账户扣费，服务费用确认为 0；未观察到人工介入。 Controller source check adds the explicit free keyless rule; HTTP200/no-key alone is not the price proof.; https://docs.firecrawl.dev/features/scrape; grading/artifacts/evidence/firecrawl-request-and-2027-table.md; https://docs.firecrawl.dev/rate-limits

  结论与限制：指定服务 Firecrawl 匿名 Public Scrape API 真实取得官方 OPM 页面（HTTP 200，sourceURL 为该页），从响应内的“2027 Holiday Schedule”表提取全部 11 个假日，生成可解析的 UTF-8 CSV（列 date,weekday,holiday，日期升序，脚注标记去除），与独立参考逐行一致；答复给出文件位置与官方来源链接。

<a id="comparison-4582424b2cd6"></a>

### web-extraction-access-001 v1

**jina / reader-api** — 0 完成 / 0 未完成 / 1 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none

准备：Fresh runtime, no account, prewritten calling scripts or previous results. OpenCode 1.18.35 / DeepSeek V4.1 Flash high; 25 model requests per role, 32000 output tokens/request, execution and grading 300s. New budget conditions retained separately from older runs. Original attempt was interrupted by a controller naming collision in another service; retained as an invalid/interrupt record separately. This is a fresh runtime with no inherited configuration or results.

- [jina-extraction-access-ds41-r2](../data/experiments/evaluations/jina-extraction-access-ds41-r2.json)：模型费用 $0.0092；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: 未产生任何成功的服务调用或计费回执；执行者未付款不等于免费，且本次无法读取官方文档核实免费规则，故保留 unknown。

  结论与限制：指定服务入口 https://r.jina.ai/ 在测试网络内被域名级 DNS 污染与出网阻断（r.jina.ai、jina.ai 解析为无关/轮换地址并连接超时），而对照域名 example.com、github.com 等均返回 200，同期题面涉及的 firecrawl、exa 域名也可达，故无法通过指定入口取得 https://example.com/ 正文与标题。失败原因属执行环境网络限制而非服务能力、凭据或执行行为；执行者仅用指定入口、未切换其他服务、未绕过直读，并如实保存配置与阻碍。因环境无法访问指定服务，本次无法对 Jina Reader 的可接入性做有效评测，故记 invalid_run。

<a id="comparison-2f500bd738e2"></a>

### database-todos-001 v2

**neon / claimable-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none initially; executor obtains anonymous scoped test credentials · 独立验收可参考同期 2 份同题答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v2 task, model, effort, tools and 25-request budget for both services. Reference values and peer results withheld from executors. Newly issued and preprovided secrets are removed from independent grading copies and peer snapshots; original raw evidence remains controller-private. Execution 600s; independent grading 300s.

- [neon-todos-001v2-ds41-r1](../data/experiments/evaluations/neon-todos-001v2-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Neon Claimable 匿名未认领项目无需 Neon 账号、Key 或支付方式，也无自动超额计费；本次全程仅用匿名身份，未提供或绑定任何账号/付款，未 claim 到付费组织。除 72 小时到期与 100MB/1GB 上限外无计费项。无账单回执，故不按金额记账。; https://neon.com/docs/reference/claimable-neon（官方文档，2026-10-08 本次获取）; frozen-execution/ENVIRONMENT.md（本轮指定免费 Claimable 入口与额度范围）

  结论与限制：指定的 Neon Claimable 远程 Postgres 库内实际新建三条并更新 id=2；写进程结束后另起全新 Node 进程重连同一库读回，列表、未完成项与计数均与独立参考一致，并按官方文档如实说明 72 小时到期与免费额度；答复未泄露凭据。

<a id="comparison-785fde9d2ce4"></a>

### database-todos-001 v2

**turso / platform-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · pre-existing Turso management account · 独立验收可参考同期 2 份同题答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v2 task, model, effort, tools and 25-request budget for both services. Reference values and peer results withheld from executors. Newly issued and preprovided secrets are removed from independent grading copies and peer snapshots; original raw evidence remains controller-private. Execution 600s; independent grading 300s.

- [turso-todos-001v2-ds41-r1](../data/experiments/evaluations/turso-todos-001v2-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Turso 账号处于 starter 免费套餐，无需付费即可完成；本次用量远低于免费额度。; grading/artifacts/evidence/turso_free_plan_evidence.md; execution/artifacts/result.json

  结论与限制：使用接入阶段交付的指定 Turso libSQL 空库，独立写入程序建表并插入三条合成待办、把 id=2 改为 done=true 后退出；随后另一全新进程重连同一端点读回，结果与 reference.json 期望完全一致（id 升序、仅 id=1 未完成、总数 3、完成 2，标题不变）。答复正确披露 starter 免费套餐与 Token 7 天到期/10 天无活动归档限制，未泄露凭据、未建第二库、未启用付费。全部验收项通过。

<a id="comparison-85831928a49a"></a>

### financial-statements-001 v1

**alpha-vantage / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · controller-registered ordinary free API key · 独立验收可参考同期 2 份同题答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v1 task, model, effort, tools and 25-request budget for both services. Reference values and peer results withheld from executors. Registered secrets are removed from independent grading copies and peer snapshots; original raw evidence remains controller-private. Execution 600s; independent grading 300s.

- [alpha-vantage-statements-001-ds41-r1](../data/experiments/evaluations/alpha-vantage-statements-001-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 本次使用总控预先注册的 Alpha Vantage 普通免费 Key，仅调用免费端点；无付费回执。; execution/artifacts/ENVIRONMENT.md; https://www.alphavantage.co/support/; grading/artifacts/evidence/verification.md

  结论与限制：指定服务 Alpha Vantage 的 INCOME_STATEMENT、CASH_FLOW 返回了 AAPL FY2025 与 MSFT FY2025 的营收/净利润/经营现金流；六项数值与独立参考（reference.json）及采集的 SEC XBRL 原件逐项一致。答复提供了两公司三指标的十亿美元比较表、财年结束日、币种/单位、GAAP 口径与可定位的 10-K 出处，满足全部成功条件。

<a id="comparison-01f9c83debc7"></a>

### financial-statements-001 v1

**sec-edgar / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; contact identity only · 独立验收可参考同期 2 份同题答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v1 task, model, effort, tools and 25-request budget for both services. Reference values and peer results withheld from executors. Registered secrets are removed from independent grading copies and peer snapshots; original raw evidence remains controller-private. Execution 600s; independent grading 300s.

- [sec-edgar-statements-001-ds41-r1](../data/experiments/evaluations/sec-edgar-statements-001-ds41-r1.json)：模型费用 $0.0084；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: SEC EDGAR is a free public government disclosure service; no per-query charge applies and no account/receipt exists. service_cost_usd left null because there is no billed amount to report.; https://www.sec.gov/search-filings/edgar-application-programming-interfaces; frozen-execution/ENVIRONMENT.md

  结论与限制：Executor queried the designated service SEC EDGAR (data.sec.gov) XBRL APIs for both companies' FY2025 10-K and produced the required comparison table with fiscal-year ends, USD billions and traceable 10-K provenance. Grader re-read the collected raw SEC responses and re-fetched Apple NetIncomeLoss live; all six metrics, both fiscal-year ends, units and sources match the independent reference.

<a id="comparison-33be83cbd5a7"></a>

### financial-access-001 v1

**sec-edgar / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; contact identity only

准备：Fresh runtime, no prewritten calling scripts or previous results. Controller provisioned a contact identity for SEC and a newly registered ordinary free Alpha Vantage key using the authorized mailbox; registration time/token overhead is not part of these model sessions and is not claimed as executor self-registration. OpenCode 1.18.35 / DeepSeek V4.1 Flash high; 25 model requests per role, 32000 output tokens/request, execution and grading 300s. New budget conditions retained separately from older runs.

- [sec-edgar-access-ds41-r1](../data/experiments/evaluations/sec-edgar-access-ds41-r1.json)：模型费用 $0.0100；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 无计费回执；SEC EDGAR 为免费公开数据服务，本次未产生服务费用。; https://www.sec.gov/about/webmaster-frequently-asked-questions — SEC 官方 FAQ: 'All Government-created content on sec.gov and EDGAR public filing content are free to access and reuse.'; https://www.sec.gov/search-filings/edgar-application-programming-interfaces — SEC EDGAR API 官方页: 'These APIs do not require any authentication or API keys to access.'

  结论与限制：指定服务 SEC EDGAR（https://data.sec.gov REST API）已实际接通：用提供的 client_name/contact 作为 User-Agent，无需 Key/注册即可调用；submissions、companyconcept、companyfacts、frames 四类端点均返回 HTTP 200 真实数据（如 Apple Inc./AAPL、11 期 Revenues）。可复用连接配置已写入持久目录 /home/node/service-tools/service-config.json 并读回校验通过。未发现失败或替代服务行为；Alpha Vantage 材料与凭据不一致已如实说明，非本次指定入口。

<a id="comparison-db274edc24f6"></a>

### web-search-001 v1

**exa / public-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none · 独立验收可参考同期 2 份同题答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v1 task, model, effort, generic tools and 25-request budget for both services. Interfaces differ by declared route: Exa anonymous remote MCP and Tavily anonymous REST API; this compares these specific routes, not identical interfaces. Reference values and peer results withheld from executors. Execution 600s; independent grading 300s.

- [exa-search-001-ds41-r1](../data/experiments/evaluations/exa-search-001-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: Exa 采用官方匿名 keyless MCP 入口，无账号、无 API Key、未绑定支付；未采集任何服务端计费回执，也未取得官方免费规则的当次证据，执行者未付款不构成免费证明，故保留 unknown。

  结论与限制：本次执行真实调用了指定服务 Exa 官方匿名远程 MCP（https://mcp.exa.ai/mcp，keyless），真实搜索响应中出现多个不同的官方 python.org 页面（如 /3/howto/free-threading-python.html、/3/howto/free-threading-extensions.html、/3/whatsnew/3.13.html），三个问题（默认不启用、如何启用、C 扩展兼容性）的结论均能在当次获取内容中找到依据，其中 Q1 的原文直接来自响应内的 What's New in Python 3.13。核验发现的差异属于模型的引用/版本处理：最终答复把官方依据改写成 /3.13/ 形式（并列入从未获取的 PEP 703），这些 URL 字符串未出现在搜索响应中，也未捕获重定向或版本对应证据，仅用 curl 确认 /3.13/ 页面返回 200；当次实际抓取的 howto 页面为 /3/（标题 3.14.6/3.14.7），whatsnew/3.13 文档以 /3/ 形式返回。按独立参考允许等价官方来源与 3.13 文档版本漂移的判定，任务要求的真实发现与结论依据成立，故记完成；引用版本口径差异见 checks/evidence。

<a id="comparison-8c4b61fb41be"></a>

### financial-fx-001 v1

**ecb-data / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none · 独立验收可参考同期 2 份同题答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v1 task, model, effort, tools and 25-request budget for both services. Reference values and peer results withheld from executors. Execution 600s; independent grading 300s.

- [ecb-data-fx-001-ds41-r1](../data/experiments/evaluations/ecb-data-fx-001-ds41-r1.json)：模型费用 $0.0053；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: ECB 官方站声明其网站信息可免费使用/免费获取；本次执行未提供账户、Key 或支付方式，对 ECB Data Portal API 单次未认证 GET 成功，无计费、订阅或超出免费范围的操作。; https://www.ecb.europa.eu/services/disclaimer/html/index.en.html; public-review/free-rule.md; public-review/verification.md

  结论与限制：本次执行通过指定 ECB Data Portal REST API（未认证、免费）取得 USD/EUR 参考汇率，正确完成非发布日回退、币种方向与逐笔舍入；三笔欧元金额与合计 211.65 EUR 与独立参考逐一核对一致，并给出可核对的序列键、请求 URL 与官方文档出处。

**frankfurter / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none · 独立验收可参考同期 2 份同题答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v1 task, model, effort, tools and 25-request budget for both services. Reference values and peer results withheld from executors. Execution 600s; independent grading 300s.

- [frankfurter-fx-001-ds41-r1](../data/experiments/evaluations/frankfurter-fx-001-ds41-r1.json)：模型费用 $0.0052；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Frankfurter 公网 API 免 Key、无账户、无付费层级；本次执行及验收复核均经公开入口取得数据，未使用 Key 或产生费用。; https://frankfurter.dev/ 官方文档：Free, open-source exchange rates API; No API key required; grading/artifacts/evidence/frankfurter-fx-001-verification.md 记录的本次无 Key 公开调用

  结论与限制：本次执行在指定服务 Frankfurter API v2 的 ECB 提供方路由上按发生日获取 ECB 参考汇率，非发布日（2026-08-15 周六）正确回退到 2026-08-14，币种方向为 EUR/USD 且按乘算关系使用，三笔欧元金额 69.16/108.07/34.42 与合计 211.65 经独立重算及独立 ECB 参考（1.1567/1.1593）核对一致，出处可核对，免费入口无 Key。

<a id="comparison-8a11046c9744"></a>

### financial-access-001 v1

**ecb-data / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none

准备：Fresh runtime, no account, prewritten calling scripts or previous results. OpenCode 1.18.35 / DeepSeek V4.1 Flash high; 25 model requests per role, 32000 output tokens/request, execution and grading 300s. New budget conditions retained separately from older runs.

- [ecb-data-access-ds41-r1](../data/experiments/evaluations/ecb-data-access-ds41-r1.json)：模型费用 $0.0086；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: Controller publication review: the original access grader cited the task environment and unauthenticated HTTP 200 responses, which do not independently prove a free-price rule. Preserve unknown for this access record; task-completion verdict and measured usage are unchanged. The later business run has its own separately verified fee evidence.

  结论与限制：执行者通过指定入口 data-api.ecb.europa.eu/service 的 SDMX 2.1 REST API 完成了真实数据查询（JSON/CSV/元数据均 HTTP 200），无需账号或 Key，未强行注册；并把可复用连接配置写入持久目录 /home/node/service-tools/service-config.json。验收方在验收环境独立复现同一查询，均 HTTP 200 且数据一致。

**frankfurter / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none

准备：Fresh runtime, no account, prewritten calling scripts or previous results. OpenCode 1.18.35 / DeepSeek V4.1 Flash high; 25 model requests per role, 32000 output tokens/request, execution and grading 300s. New budget conditions retained separately from older runs.

- [frankfurter-access-ds41-r1](../data/experiments/evaluations/frankfurter-access-ds41-r1.json)：模型费用 $0.0081；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Frankfurter 公共 API 官方文档声明免费、开源、无需 API Key、无配额且可用于商业用途；OpenAPI 无 security 方案、license 为 MIT。本次仅匿名调用公开入口并取得 200 数据，无任何账号、Key 或付费。; https://frankfurter.dev/; https://api.frankfurter.dev/v2/openapi.json

  结论与限制：指定入口 https://api.frankfurter.dev/v2/ 为免 Key 公开 REST API；执行者实际完成多项真实数据查询（含 GET /v2/rate/EUR/USD 返回 2026-10-08 rate=1.1221、多币种 /rates、历史区间、coverage、providers 与单 provider 查询），并将连接配置写入指定持久目录 /home/node/service-tools/service-config.json（JSON 校验通过）。无需注册/认证，未使用其他聚合服务，未付费或写远端。验收环境独立重放 /v2/rate/EUR/USD 得到相同结果。

<a id="comparison-1d87fed8bbbd"></a>

### financial-disclosures-001 v1, financial-disclosures-002 v1, financial-disclosures-003 v1, financial-disclosures-004 v1

**bargo-congress / congress-api-keyless** — 2 完成 / 2 未完成 / 0 环境无效。

1.18.35 / glm-5.3-flash / high · 900s · natural · none

准备：OpenCode 1.18.35 rerun on 2026-10-08 after independently graded fresh keyless REST access in this batch. GLM-5.3-Flash/high; execution and grading each 900 seconds; batch ceiling 10 with four exclusive runtimes. Original task v1, inputs, roles, historical official reference and LiteLLM price snapshot retained; service data remains live and dates differ from prior trials. Only connection configuration and generic installed packages persist. No service key, account or payment supplied; quota shared by IP. One planned trial per task; no automatic repeat-until-success. This is not an isolated causal test of the OpenCode version.

- [bargo-disclosures-004-oc11835-r1](../data/experiments/evaluations/bargo-disclosures-004-oc11835-r1.json)：模型费用 —；Per-request usage capture is incomplete. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；confirmed_free: 官方文档明示读端点免 Key 且免费（仅限速，页面标注 FREE · NO CARD）；本次全部服务调用为免 Key GET，HTTP 200，响应头 x-ratelimit-limit:30 / rows-limit:100（keyless 档），未注册、未付款。适用条件已核对。; https://www.bargo.ai/free-apis/congress

  结论与限制：独立验收判定本题未完成：执行触及预算上限，虽已取得相关业务数据并完成部分核对，但未交付四项说法的逐项判断、有依据的成文更正和完整原始申报出处。属本次 Agent 在预算内未完成，未判为服务能力不支持；本次执行 Token 与模型费因最后请求未完整采集而保持未知。 公开版由总控删减交易明细；原独立验收判断未改，原始验收 SHA256：6e3e4bb1a7c76306e9388aa9dfd2d6ba8cd4a458125ab1c98af0e98d4a9d6fa0 本轮未向验收者提供其他服务的同题答案；每题仅一次尝试，使用线上服务与历史冻结参考，不能把相对历史成绩的变化单独归因于 OpenCode 升级。
- [bargo-disclosures-003-oc11835-r1](../data/experiments/evaluations/bargo-disclosures-003-oc11835-r1.json)：模型费用 $0.03；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 服务费用为 0 美元（文档化免 Key 免费读端点，本次调用满足其条件）。模型 token 与模型费用由运行器与统一计价脚本另行核算，不在此填写。; https://www.bargo.ai/free-apis/congress; grading/artifacts/evidence/verify-summary.md

  结论与限制：独立验收确认本题全部用户要求满足：指定服务提供的两名成员数据完整，逐笔滞后天数与汇总统计正确，按官方提交日期筛选并附可核对的原始申报出处。 公开版由总控删减交易明细；原独立验收判断未改，原始验收 SHA256：7094c74600279184468166e7ab9edc49c7d4395db4808cf8ce6a85ab4fba5ad9 本轮未向验收者提供其他服务的同题答案；每题仅一次尝试，使用线上服务与历史冻结参考，不能把相对历史成绩的变化单独归因于 OpenCode 升级。
- [bargo-disclosures-002-oc11835-r1](../data/experiments/evaluations/bargo-disclosures-002-oc11835-r1.json)：模型费用 —；Per-request usage capture is incomplete. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard）。服务费用 $0；confirmed_free: 服务费用为 0；依据官方免费规则与本次免 Key 用量观察，非执行者自述。; https://www.bargo.ai/free-apis/congress

  结论与限制：独立验收判定本题未完成：运行触及预算上限，交付未完整列出所需交易日期、金额区间、数据服务与具体申报出处，也未完成四名成员的结果汇总。属本次 Agent 在预算内未完成，未判为服务能力不支持；本次执行用量与模型费因最后请求未完整采集而保持未知。 公开版由总控删减交易明细；原独立验收判断未改，原始验收 SHA256：a363a37b97c0f1ff220ec0754252691a834a12bfbfe76a78ccb2e851462c1ee7 本轮未向验收者提供其他服务的同题答案；每题仅一次尝试，使用线上服务与历史冻结参考，不能把相对历史成绩的变化单独归因于 OpenCode 升级。
- [bargo-disclosures-001-oc11835-r1](../data/experiments/evaluations/bargo-disclosures-001-oc11835-r1.json)：模型费用 $0.03；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 服务侧未发生任何付费；该 confirmed_free 仅指 bargo-congress 数据服务，不含模型费用（由运行器与统一计价脚本处理）。; https://www.bargo.ai/free-apis/congress

  结论与限制：独立验收确认本题全部用户要求满足：指定服务真实返回的数据集合完整，按官方提交日期筛选，股票类型、日期、方向、金额区间与原始申报出处均已核对。 公开版由总控删减交易明细；原独立验收判断未改，原始验收 SHA256：65c7377734999adf9ed98a0e2991df0cec14e8bc587af0dbfb0a5187c3dd03a1 本轮未向验收者提供其他服务的同题答案；每题仅一次尝试，使用线上服务与历史冻结参考，不能把相对历史成绩的变化单独归因于 OpenCode 升级。

<a id="comparison-a3477334d9b4"></a>

### financial-access-001 v1

**bargo-congress / congress-api-keyless** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / glm-5.3-flash / high · 900s · natural · none

准备：Fresh service runtime after OpenCode 1.18.35 upgrade. No service account or key supplied; keyless REST only. New service access is measured before business tasks. Controller preflight used one shared-IP Bargo request. Model and grading each use GLM-5.3-Flash/high with 900-second budgets; exact image digest and resource limits retained privately. Only generic package dependencies and connection configuration may persist; prior answers and task scripts are archived.

- [bargo-access-oc11835-r1](../data/experiments/evaluations/bargo-access-oc11835-r1.json)：模型费用 $0.0068；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 服务侧免费：免 Key 读端点在规则限额内使用，本次 2 次请求远低于配额，实付 0。模型 Token 与模型费用由运行器与统一计价脚本处理，不在此填写。; https://www.bargo.ai/free-apis/congress; https://www.bargo.ai/free-apis/terms

  结论与限制：按指定方式（REST 直连 https://www.bargo.ai/free-apis/congress/v1）完成免 Key 接入：GET /trades?limit=5 返回 HTTP 200 与 5 条真实 STOCK Act 披露记录（原始响应体逐字核对，count=5，字段完整，非仅文档或健康检查）；必要连接配置已写入持久目录 /home/node/service-tools/service-config.json 并通过 JSON 校验，retained-files 清单确认保留，可供新会话复用；全程未注册、未付款，仅 2 次请求、limit=5，符合免 Key 限额与授权范围，无阻碍。

**capitol-exposed / data-api-keyless** — 0 完成 / 1 未完成 / 0 环境无效。

1.18.35 / glm-5.3-flash / high · 900s · natural · none

准备：Fresh service runtime after OpenCode 1.18.35 upgrade. No service account or key supplied; keyless REST only. New service access is measured before business tasks. Controller preflight used one shared-IP Bargo request. Model and grading each use GLM-5.3-Flash/high with 900-second budgets; exact image digest and resource limits retained privately. Only generic package dependencies and connection configuration may persist; prior answers and task scripts are archived.

- [capitol-access-oc11835-r1](../data/experiments/evaluations/capitol-access-oc11835-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 免费规则来自官方文档与独立参考：免 Key 匿名读免费，列表端点 60 请求/分钟/IP，要求署名；更高限额与 AI 产品为付费且本次未使用。本次全部调用落在免费匿名档，无付费回执，未发生费用。; https://www.capitolexposed.com/api-docs; reference.json free_rule

  结论与限制：接入本身成立：经指定入口 REST 直接 HTTP 调用，/trades、/members、/top-traders 均返回 200 真实数据，service-config.json 与辅助脚本保存到 /home/node/service-tools 并经实调用验证，全程免 Key、未注册未付款。但违反冻结环境的接入资源约束「接入只做必要的少量真实数据查询，最多返回 5 条记录」：本次对指定入口共 7 次请求，5 次成功取数实际返回 7 条记录（trades 3 + members 2 + top-traders 1×2 次，第 5、7 次为重复返回；/stats 为聚合不计条），执行者自报 6 条亦超限；交付调用表漏记 2 次调用（第二次 403 归因复测与辅助脚本验证调用）。偏离属执行行为（超授权查询规模且交付统计不完整），非服务能力、接入门槛或环境问题；据冻结要求不能放宽，故判 not_completed。

<a id="comparison-60de41521941"></a>

### financial-disclosures-001 v1, financial-disclosures-002 v1, financial-disclosures-003 v1, financial-disclosures-004 v1

**capitol-exposed / data-api-keyless** — 4 完成 / 0 未完成 / 0 环境无效。

1.18.29 / glm-5.3-flash / high · 900s · natural · none · 独立验收（本轮无其他服务答案可参考）

准备：15-minute budget comparison following the 600-second round. Same task v1, model GLM-5.3-Flash/high, role instructions, service/route, references and price snapshot; execution and grading each 900 seconds, batch ceiling ten concurrent model sessions, with one active session per existing runtime (four available runtimes). Reuses the independently passed access setup and generic installed dependencies in the same containers with fresh task workspaces/sessions; no fresh signup. Collector fix preserves receipts before artifact collection and omits links without following them. Prior 600-second records remain separate. Shared-IP service quotas are checked before dispatch. Dispatch amendment: user deferred Bargo before execution because its daily quota was exhausted. Only CapitolExposed execution/grading ran (two runtimes, actual peak two); no other service answer was available. Controller archived prior task files before reuse; shared temporary-directory cleanup was added before execution 003 and grading 002.

- [capitol-disclosures-004-900s-c10-r1](../data/experiments/evaluations/capitol-disclosures-004-900s-c10-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 官方免费规则及当次免 Key 只读请求支持服务费用为零；模型费用另行估算。; https://www.capitolexposed.com/api-docs

  结论与限制：独立验收确认：指定服务真实查询与原始申报支持对合成说法的逐项核对；归属、日期、金额口径及交易性质均按冻结参考正确区分，给出有依据的更正和出处。 原始交易行及逐行答案私有保留。
- [capitol-disclosures-003-900s-c10-r1](../data/experiments/evaluations/capitol-disclosures-003-900s-c10-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 官方免费规则及当次免 Key 只读请求支持服务费用为零；模型费用另行估算。; https://www.capitolexposed.com/api-docs

  结论与限制：独立验收确认：披露滞后比较的匹配集合、逐笔日期和自然日间隔、按人汇总与冻结官方参考一致；指定服务真实查询、原件核对及出处支持交付。 原始交易行及逐行答案私有保留。
- [capitol-disclosures-002-900s-c10-r1](../data/experiments/evaluations/capitol-disclosures-002-900s-c10-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 官方免费规则及当次免 Key 只读请求支持服务费用为零；模型费用另行估算。; https://www.capitolexposed.com/api-docs

  结论与限制：独立验收确认：关注名单的匹配明细与无匹配说明符合冻结官方参考；服务查询、原始申报核对、金额区间、家庭成员范围及出处齐全，并说明了服务覆盖限制，不从披露推断持仓。 原始交易行及逐行答案私有保留。
- [capitol-disclosures-001-900s-c10-r1](../data/experiments/evaluations/capitol-disclosures-001-900s-c10-r1.json)：模型费用 $0.0100；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 官方免费规则及当次免 Key 只读请求支持服务费用为零；模型费用另行估算。; https://www.capitolexposed.com/api-docs

  结论与限制：独立验收确认：个人月度明细由指定服务真实查询取得，匹配集合、所需字段、金额区间和家庭成员归属与冻结官方参考一致，原始申报出处及服务署名齐全。 原始交易行及逐行答案私有保留。

<a id="comparison-f170f4b6c34f"></a>

### financial-access-001 v1

**tracefour / data-api-keyless** — 0 完成 / 1 未完成 / 0 环境无效。

1.18.29 / glm-5.3-flash / high · 600s · natural · none

准备：Account-free public API; no account, key or call code pre-provisioned. Dedicated service/route container; fresh session per task, retaining only service configuration and installed dependencies. Controller researched candidates and froze independent references; cloud execution and grading use GLM-5.3-Flash/high.

- [tracefour-access](../data/experiments/evaluations/tracefour-access.json)：模型费用 $0.0071；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 规则：指定入口为免 Key 免费读取，限 60 次/小时/IP。本次适用性：全程仅约 9 次免 Key 只读 GET，远低于限额；所有请求在 Cloudflare 边缘即被 403 质询拒绝，服务未实际处理任何请求；未提供也未创建任何账户、Key 或支付方式，无付款回执。故本次服务侧费用为 0。模型 token 与模型费用由运行器统一核算，不在此列。; reference.json（本题冻结参考 free_rule：Keyless reads 60 requests/hour/IP; compilation CC BY 4.0 with attribution）; execution/artifacts/probe-results.txt; grading/artifacts/evidence/independent-verification.md

  结论与限制：本轮通过指定 REST 方式接入 Tracefour 未完成：文档页和实际尝试的 URL 从本轮云端环境返回 Cloudflare 403 challenge，没有取得真实金融数据；已保存含阻碍说明的配置，无人工介入。独立验收复现了 /v1 和 /api-docs 的 403。执行者未成功读取文档，也未调用后来研究确认的 /v1/congress 等数据路由，因此这些观察不能证明全部数据端点、MCP 或其他网络环境都不可用；本轮没有执行交易披露业务题。

<a id="comparison-e42af771b245"></a>

### mailboxes-code-001 v1

**mail-tm / mail-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / medium · 600s · natural · provided: MAILBOX_ADDRESS, MAILBOX_TOKEN

准备：Dedicated temporary mailbox supplied with three synthetic emails sent from a user-authorized Gmail account. Delivery and reference timestamps checked before this run. Prior provisioning and fixture preparation are excluded from this task usage; no personal inbox access or calling scripts supplied.

- [codex-20260909T103356.699996Z-mail-tm](../data/experiments/evaluations/codex-20260909T103356.699996Z-mail-tm.json)：模型费用 $0.18；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Free public receive API for the dedicated temporary mailbox; no paid feature used. Gmail fixture sending occurred in preparation and is excluded from the measured service task.; https://docs.mail.tm/; response-excerpt.json

  结论与限制：Read the delivered test messages through Mail.tm and selected the newer login email, excluding the older login and later unrelated notice. Returned the correct synthetic code, original subject and equivalent timestamp.

**guerrilla-mail / mail-api** — 0 完成 / 1 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / medium · 600s · natural · provided: COOKIE_HEADER, MAILBOX_ADDRESS, SESSION_TOKEN

准备：Dedicated temporary mailbox supplied with three synthetic emails sent from a user-authorized Gmail account. Delivery and reference timestamps checked before this run. Prior provisioning and fixture preparation are excluded from this task usage; no personal inbox access or calling scripts supplied.

- [codex-20260909T103849.955516Z-guerrilla-mail](../data/experiments/evaluations/codex-20260909T103849.955516Z-guerrilla-mail.json)：模型费用 $0.28；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Public default temporary mailbox API; no payment credentials, custom domain or subscription were used. Fixture sending was preparation and is excluded from this measured task.; https://www.guerrillamail.com/GuerrillaMailAPI.html; external-check.json

  结论与限制：The Agent correctly extracted the latest login code and its received timestamp, but could not return the original subject. Both full-message and list APIs returned an empty subject despite the Gmail sent message having AFS Demo login 2. Reported honestly as no subject; no code-selection failure or fabricated title. The task requires all three fields, so this trial is not fully completed.

<a id="comparison-3a57cb066008"></a>

### payment-acceptance-001 v1

**paddle / sandbox-api** — 0 完成 / 1 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · natural · provided: PADDLE_SANDBOX_API_KEY

准备：A separate sandbox account was registered and email-verified by the evaluator using synthetic test business/address details. No KYC or production activation occurred. A sandbox API key expires after seven days and grants read/write access only to products, prices, transactions, checkout domains and client-side tokens. A preflight API read confirmed an empty product catalog. No product, price, transaction, checkout page or solution code was prepared. A dedicated empty local Chromium browser is supplied over CDP to avoid macOS sandbox browser-launch failures; the executing Codex still uses workspace-write sandboxing. Registration, browser startup and evaluator work are outside measured execution metrics. This configuration differs from earlier browser-less trials.

- [codex-20260909T032011.000426Z-paddle](../data/experiments/evaluations/codex-20260909T032011.000426Z-paddle.json)：模型费用 $1.20；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Sandbox-only API requests, with no completed payment, no paid subscription or live account activation. Official docs specify no real money in sandbox and pricing has no monthly fees. The $12 product price is not a service cost.; https://developer.paddle.com/sdks/sandbox/; https://www.paddle.com/pricing

  结论与限制：The default newly registered Paddle sandbox account rejected creation of the ebook product with product_tax_category_not_approved for ebooks. No product, transaction or customer checkout link was created. This is an account/category access barrier for this scenario, not evidence that Paddle cannot serve any product or approved account. The dedicated browser connected successfully but had no dashboard login, as disclosed. Independent authenticated dashboard inspection shows eBook Not Requested, SaaS Approved, and a notice that category approval must be requested in the live account; no live application was made.

<a id="comparison-b073a7f72e8c"></a>

### payment-acceptance-001 v1

**paas-build / rest-api** — 0 完成 / 0 未完成 / 1 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · natural · provided: PAAS_SANDBOX_ACCESS_TOKEN, PAAS_SANDBOX_VENDOR_ID

准备：A new sandbox-only merchant was provisioned by the evaluator through the official API with notifications disabled. Sandbox token identity was checked before execution. No product, price, checkout, production merchant or solution code was prepared. Signup identity stays private; preparation time and evaluator tokens are outside execution metrics.

- [codex-20260908T113239.160717Z-paas-build](../data/experiments/evaluations/codex-20260908T113239.160717Z-paas-build.json)：模型费用 $2.00；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Official instructions state that the sandbox is free to play with. Only sandbox checkout creation and reads occurred; no payment was submitted. The $12 product price is not a service charge.; https://paas.build/SKILL.md

  结论与限制：The executor created a real sandbox checkout, but macOS sandbox permissions prevented Chromium from launching. Exclude this trial from service completion-rate comparisons. Independent post-run browser inspection also showed only the checkout shell, without the product, amount or payment form; this is a separate observed usability issue requiring a fresh run after environment repair.

<a id="comparison-8cc2ab7b2dcd"></a>

### collaborative-tables-001 v2

**notion / rest-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · natural · provided: NOTION_API_TOKEN, NOTION_PARENT_PAGE_ID

准备：Existing dedicated free test account; API credential and a newly created empty private parent page prepared before timing. No business schema, records or adapter supplied. Setup and external verification excluded from measured tokens/time. No payment enabled.

- [codex-20260908T035504.906378Z-notion](../data/experiments/evaluations/codex-20260908T035504.906378Z-notion.json)：模型费用 $0.75；Actual recorded usage × saved LiteLLM standard API rates; estimate at the snapshot date, not an account charge. Excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：Natural v2 created a real online table with three correct final actions and returned the matching link and two outstanding tasks. Independent remote read after executor exit matched all user facts. 7 business API requests observed in executed code and CLI outputs, within 40. Setup and external review excluded; one observation, not a typical-cost estimate or service ranking.

<a id="comparison-ab4e4c0d9054"></a>

### collaborative-tables-001 v2

**grist / rest-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · natural · provided: GRIST_API_KEY, GRIST_WORKSPACE_ID

准备：Existing dedicated free test account; API credential and a newly created empty workspace prepared before timing. No business schema, records or adapter supplied. Setup and external verification excluded from measured tokens/time. No payment enabled.

- [codex-20260908T035504.472694Z-grist](../data/experiments/evaluations/codex-20260908T035504.472694Z-grist.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：Natural v2 created a real online table with three correct final actions and returned the matching link and two outstanding tasks. Independent remote read after executor exit matched all user facts. 11 business API requests observed in executed code and CLI outputs, within 40. Setup and external review excluded; one observation, not a typical-cost estimate or service ranking.

<a id="comparison-07edbec76825"></a>

### database-todos-001 v1

**turso / platform-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · provided: TURSO_API_TOKEN, TURSO_ORGANIZATION

准备：Outer Agent registered a new dedicated Free organization using Google sign-in, selected a username and created an organization API token; no card/payment, no existing database. Signup and token creation outside measured time/tokens. Executor receives only this organization and token, and must provision its own test database.

- [codex-20260907T113506.422646Z-turso](../data/experiments/evaluations/codex-20260907T113506.422646Z-turso.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：Independent writer/reader processes and outer reviewer remote re-read confirm persisted todos. Dedicated free organization and API token were prepared before timing; database/group and SQL tokens were created during execution. No payment; overages remain off. Free archival and token expiry limit long-term use.

<a id="comparison-53b484528301"></a>

### web-search-001 v1

**exa / search-api** — 0 完成 / 1 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · provided: EXA_API_KEY

准备：Free account prepared by the outer Agent using browser Google sign-in and onboarding; no card or payment. Signup work is outside measured session tokens/time; only EXA_API_KEY provided, no adapter or research context.

- [codex-20260907T112952.581354Z-exa](../data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json)：模型费用 —；Token usage was not reported. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：The authenticated Exa API returned real search results, but the executor spent its 10-search allowance on source discovery/evidence work and reached the 600-second wall-clock limit without a final answer. This is a task-budget failure, not API unavailability. CLI emitted no turn.completed usage event before interruption: tokens remain unknown, not zero. Free account was prepared outside measured time; no payment.

<a id="comparison-3f655dc71038"></a>

### web-search-001 v1

**firecrawl / public-search-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：No service account or resource prepared before the measured session.

- [codex-20260907T112951.715536Z-firecrawl](../data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：Anonymous Firecrawl search and direct reads of returned official sources support all three answers. Two cited pages were discovered through links inside result descriptions, not separate ranked hits; this satisfies frozen v1 response-URL criterion. No account or payment; a single-run token difference does not establish overall provider superiority.

<a id="comparison-b514e81afd38"></a>

### database-todos-001 v1

**neon / ephemeral-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：No service credentials provided.

- [codex-20260907T112258.549053Z-neon](../data/experiments/evaluations/codex-20260907T112258.549053Z-neon.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：Independent remote re-read confirms the three synthetic todos and update; separate writer/reader processes and count response satisfy v1. No signup or payment; ephemeral database expires 2026-09-10T11:23:56.173Z. This establishes short-term persistence only.

<a id="comparison-521dd3fb476a"></a>

### flights-search-001 v1

**kiwi / search-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：unknown

- [codex-20260907T092329.724439Z-kiwi](../data/experiments/evaluations/codex-20260907T092329.724439Z-kiwi.json)：模型费用 $0.84；Actual recorded usage × saved LiteLLM standard API rates; estimate at the snapshot date, not an account charge. Excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：独立核对当次请求、完整服务SSE响应和最终答案，3个方案均满足 flights-search-001 v1：BGY→EIN FR3460 62 EUR、LIN→AMS U25405 68 EUR、MXP→AMS U23851 75 EUR，均为2026-09-25出发、1名成人单程经济舱。单次运行212.222秒内完成，执行中人工介入0。初次GET 406后MCP POST成功，无未解决执行阻碍；仅证明本次基础搜索完成，Agent与服务逐次实付费用未报告，保留未知。 2026-09-07费用口径修订：本字段统计本次调用服务的新增实付。实际使用无账户、无凭据的公开入口，且没有付款，因此将原先因缺账单填写的未知修正为0；原始复核说明保留，不涉及机票报价。

<a id="comparison-77a51e093709"></a>

### flights-search-001 v1

**ignav / public-playground** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：unknown

- [codex-20260907T083644.877057Z-ignav](../data/experiments/evaluations/codex-20260907T083644.877057Z-ignav.json)：模型费用 $0.93；Actual recorded usage × saved LiteLLM standard API rates; estimate at the snapshot date, not an account charge. Excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：基础找票任务完成：3个提交方案与当次服务响应及任务参数相符。单次同机试跑，不代表其他入口或长期成功率。
