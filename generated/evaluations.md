<!-- GENERATED — npm run generate; source: data/experiments/evaluations/ -->
# 任务实测结果

每行只说明该服务入口在该任务和运行配置下的观察。Token用量为输入总数（含缓存）加输出，缓存不重复相加。模型费用根据保存的LiteLLM价格表自动估算，估价日期不冒充运行日期；服务费用单独记录，unknown不等于0。点击结果可查看冻结的任务、独立复核与选取的证据；原始日志仍在本地。免费账号的注册准备若发生在计时前，说明保存在 environment.preparation_note；表中 token 与耗时不包含这部分准备。历史记录保留，不把不同任务、配置或日期直接平均成服务排名。

按当前分类和接入／业务阶段分组，再展示同一任务版本和冻结内容的运行。展示归属来自 task-classifications.yaml；历史任务、结果和用量不改写。同组仍需核对接入前提与模型等配置，不能仅按耗时排序判断优劣。

输入方式 legacy 是带明确测试要求的初期试跑，Agent 的开销包含证据保存与整理；natural 只提供用户任务、资料及运行环境，使用自动会话日志与外部远端复核。不同方式分别记录；单次测量都不代表典型开销，跨版本差异也可能来自业务要求、执行路径和缓存变化。

<a id="web-search-data-financial-data-statements"></a>

## 搜索与数据获取 / 金融数据 / 公司财务数据（web-search-data/financial-data/statements）

### financial-statements-001 / v1

比较苹果和微软 2025 财年的营收、净利润和经营现金流，做成表格并附原始财报出处。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| alpha-vantage / data-api | financial-statements-001 (v1) | controller-registered ordinary free API key | natural | [completed](../data/experiments/evaluations/alpha-vantage-statements-001-ds41-r1.json) | 2026-10-08T12:25:33.613786+00:00 | 1.18.35 / deepseek-flash / high | 179589 / 168192 / 9052 | 77.721987s | 0 | 1 |
| sec-edgar / data-api | financial-statements-001 (v1) | none; contact identity only | natural | [completed](../data/experiments/evaluations/sec-edgar-statements-001-ds41-r1.json) | 2026-10-08T12:25:31.794208+00:00 | 1.18.35 / deepseek-flash / high | 92106 / 82560 / 4177 | 34.919235s | 0 | 0 |

<a id="web-search-data-financial-data"></a>

## 搜索与数据获取 / 金融数据（web-search-data/financial-data） · 接入测试

### financial-access-001 / v1

帮我把这个金融数据服务接好，确认能用指定方式查询数据，并保存后续调用需要的配置；如果接不通，说明卡在哪里。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
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

<a id="web-search-data-web-search"></a>

## 搜索与数据获取 / 网页搜索（web-search-data/web-search）

### web-search-001 / v1

我准备把 Python 应用升级到 3.13，查清楚自由线程是否默认启用、如何启用，以及现有 C 扩展有什么兼容性限制，并给出官方依据

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 输入方式 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| tavily / keyless-search-api | web-search-001 (v1) | none | natural | [completed](../data/experiments/evaluations/tavily-search-001-ds41-r1.json) | 2026-10-08T12:04:00.194813+00:00 | 1.18.35 / deepseek-flash / high | 519740 / 478848 / 7454 | 89.797556s | 0 | 0 |
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
| exa / public-mcp | web-search-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/exa-access-ds41-r1.json) | 2026-10-08T12:01:59.543536+00:00 | 1.18.35 / deepseek-flash / high | 199173 / 183680 / 5236 | 38.345252s | 0 | 0 |
| tavily / keyless-search-api | web-search-access-001 (v1) | none | natural | [completed](../data/experiments/evaluations/tavily-access-ds41-r1.json) | 2026-10-08T12:01:59.416003+00:00 | 1.18.35 / deepseek-flash / high | 89861 / 80512 / 2329 | 27.012414s | 0 | 0 |

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

<a id="comparison-6ea769563771"></a>

### financial-statements-001 v1

**alpha-vantage / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · controller-registered ordinary free API key · 独立验收可参考同期 2 家服务的答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v1 task, model, effort, tools and 25-request budget for both services. Reference values and peer results withheld from executors. Registered secrets are removed from independent grading copies and peer snapshots; original raw evidence remains controller-private. Execution 600s; independent grading 300s.

- [alpha-vantage-statements-001-ds41-r1](../data/experiments/evaluations/alpha-vantage-statements-001-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 本次使用总控预先注册的 Alpha Vantage 普通免费 Key，仅调用免费端点；无付费回执。; execution/artifacts/ENVIRONMENT.md; https://www.alphavantage.co/support/; grading/artifacts/evidence/verification.md

  结论与限制：指定服务 Alpha Vantage 的 INCOME_STATEMENT、CASH_FLOW 返回了 AAPL FY2025 与 MSFT FY2025 的营收/净利润/经营现金流；六项数值与独立参考（reference.json）及采集的 SEC XBRL 原件逐项一致。答复提供了两公司三指标的十亿美元比较表、财年结束日、币种/单位、GAAP 口径与可定位的 10-K 出处，满足全部成功条件。

<a id="comparison-8f6f28f05196"></a>

### financial-statements-001 v1

**sec-edgar / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none; contact identity only · 独立验收可参考同期 2 家服务的答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v1 task, model, effort, tools and 25-request budget for both services. Reference values and peer results withheld from executors. Registered secrets are removed from independent grading copies and peer snapshots; original raw evidence remains controller-private. Execution 600s; independent grading 300s.

- [sec-edgar-statements-001-ds41-r1](../data/experiments/evaluations/sec-edgar-statements-001-ds41-r1.json)：模型费用 $0.0084；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: SEC EDGAR is a free public government disclosure service; no per-query charge applies and no account/receipt exists. service_cost_usd left null because there is no billed amount to report.; https://www.sec.gov/search-filings/edgar-application-programming-interfaces; frozen-execution/ENVIRONMENT.md

  结论与限制：Executor queried the designated service SEC EDGAR (data.sec.gov) XBRL APIs for both companies' FY2025 10-K and produced the required comparison table with fiscal-year ends, USD billions and traceable 10-K provenance. Grader re-read the collected raw SEC responses and re-fetched Apple NetIncomeLoss live; all six metrics, both fiscal-year ends, units and sources match the independent reference.

<a id="comparison-04dea4e239e0"></a>

### financial-access-001 v1

**sec-edgar / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none; contact identity only

准备：Fresh runtime, no prewritten calling scripts or previous results. Controller provisioned a contact identity for SEC and a newly registered ordinary free Alpha Vantage key using the authorized mailbox; registration time/token overhead is not part of these model sessions and is not claimed as executor self-registration. OpenCode 1.18.35 / DeepSeek V4.1 Flash high; 25 model requests per role, 32000 output tokens/request, execution and grading 300s. New budget conditions retained separately from older runs.

- [sec-edgar-access-ds41-r1](../data/experiments/evaluations/sec-edgar-access-ds41-r1.json)：模型费用 $0.0100；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 无计费回执；SEC EDGAR 为免费公开数据服务，本次未产生服务费用。; https://www.sec.gov/about/webmaster-frequently-asked-questions — SEC 官方 FAQ: 'All Government-created content on sec.gov and EDGAR public filing content are free to access and reuse.'; https://www.sec.gov/search-filings/edgar-application-programming-interfaces — SEC EDGAR API 官方页: 'These APIs do not require any authentication or API keys to access.'

  结论与限制：指定服务 SEC EDGAR（https://data.sec.gov REST API）已实际接通：用提供的 client_name/contact 作为 User-Agent，无需 Key/注册即可调用；submissions、companyconcept、companyfacts、frames 四类端点均返回 HTTP 200 真实数据（如 Apple Inc./AAPL、11 期 Revenues）。可复用连接配置已写入持久目录 /home/node/service-tools/service-config.json 并读回校验通过。未发现失败或替代服务行为；Alpha Vantage 材料与凭据不一致已如实说明，非本次指定入口。

<a id="comparison-d1ad42ce8a0d"></a>

### financial-access-001 v1

**alpha-vantage / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · controller-registered ordinary free API key

准备：Fresh runtime, no prewritten calling scripts or previous results. Controller provisioned a contact identity for SEC and a newly registered ordinary free Alpha Vantage key using the authorized mailbox; registration time/token overhead is not part of these model sessions and is not claimed as executor self-registration. OpenCode 1.18.35 / DeepSeek V4.1 Flash high; 25 model requests per role, 32000 output tokens/request, execution and grading 300s. New budget conditions retained separately from older runs.

- [alpha-vantage-access-ds41-r1](../data/experiments/evaluations/alpha-vantage-access-ds41-r1.json)：模型费用 $0.0058；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Alpha Vantage 免费层，无回执亦无扣费。执行仅使用普通免费 Key 调用免费端点。; https://www.alphavantage.co/premium/

  结论与限制：执行者使用本轮提供的免费 API Key，通过指定入口 https://www.alphavantage.co/query 以 GET+apikey 方式完成 3 次真实数据查询（GLOBAL_QUOTE IBM/MSFT、TIME_SERIES_DAILY IBM，均返回 2026-10-07 行情），并把可复用连接配置写入指定持久目录 /home/node/service-tools/service-config.json；答复未输出 Key。接入无阻碍，全部要求有采集证据支持。

<a id="comparison-b8056c1607c9"></a>

### web-search-001 v1

**exa / public-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none · 独立验收可参考同期 2 家服务的答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v1 task, model, effort, generic tools and 25-request budget for both services. Interfaces differ by declared route: Exa anonymous remote MCP and Tavily anonymous REST API; this compares these specific routes, not identical interfaces. Reference values and peer results withheld from executors. Execution 600s; independent grading 300s.

- [exa-search-001-ds41-r1](../data/experiments/evaluations/exa-search-001-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 —；unknown: Exa 采用官方匿名 keyless MCP 入口，无账号、无 API Key、未绑定支付；未采集任何服务端计费回执，也未取得官方免费规则的当次证据，执行者未付款不构成免费证明，故保留 unknown。

  结论与限制：本次执行真实调用了指定服务 Exa 官方匿名远程 MCP（https://mcp.exa.ai/mcp，keyless），真实搜索响应中出现多个不同的官方 python.org 页面（如 /3/howto/free-threading-python.html、/3/howto/free-threading-extensions.html、/3/whatsnew/3.13.html），三个问题（默认不启用、如何启用、C 扩展兼容性）的结论均能在当次获取内容中找到依据，其中 Q1 的原文直接来自响应内的 What's New in Python 3.13。核验发现的差异属于模型的引用/版本处理：最终答复把官方依据改写成 /3.13/ 形式（并列入从未获取的 PEP 703），这些 URL 字符串未出现在搜索响应中，也未捕获重定向或版本对应证据，仅用 curl 确认 /3.13/ 页面返回 200；当次实际抓取的 howto 页面为 /3/（标题 3.14.6/3.14.7），whatsnew/3.13 文档以 /3/ 形式返回。按独立参考允许等价官方来源与 3.13 文档版本漂移的判定，任务要求的真实发现与结论依据成立，故记完成；引用版本口径差异见 checks/evidence。

**tavily / keyless-search-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none · 独立验收可参考同期 2 家服务的答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v1 task, model, effort, generic tools and 25-request budget for both services. Interfaces differ by declared route: Exa anonymous remote MCP and Tavily anonymous REST API; this compares these specific routes, not identical interfaces. Reference values and peer results withheld from executors. Execution 600s; independent grading 300s.

- [tavily-search-001-ds41-r1](../data/experiments/evaluations/tavily-search-001-ds41-r1.json)：模型费用 $0.02；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Tavily 官方 keyless 文档明确 /search 与 /extract 免账号、免 Key、免费且按限流使用；本次两个端点均以 X-Tavily-Access-Mode: keyless 且无 Authorization 调用并返回 HTTP 200，未使用付费 research/crawl/proxy 端点，无实付费用。; https://docs.tavily.com/documentation/keyless; execution/artifacts/s_whatsnew.json; grading/artifacts/evidence/tavily-keyless-free.md

  结论与限制：本次执行通过 Tavily 官方 keyless Search API 真实检索，搜索响应中出现了多个 python.org 官方页面；再用 Tavily Extract 读取 Python 3.13 官方文档。中文简答正确覆盖三个问题：默认状态（实验性、默认不启用、需单独 free-threaded 可执行文件/构建）、启用方式（源码 --disable-gil、官方 Windows/macOS 安装器可选 free-threaded 二进制、运行时 PYTHON_GIL / -X gil，且运行时开关仅作用于 free-threaded 构建）、C 扩展兼容性（需专门构建并显式声明支持，否则导入时告警并回退 GIL），各结论均能与其保存的官方页面内容对应，无版本混淆，证据可核对。

<a id="comparison-7aef90c6de38"></a>

### web-search-access-001 v1

**exa / public-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none

准备：Fresh runtime, no account, prewritten calling scripts or previous results. OpenCode 1.18.35 / DeepSeek V4.1 Flash high; 25 model requests per role, 32000 output tokens/request, execution and grading 300s. New budget conditions retained separately from older runs.

- [exa-access-ds41-r1](../data/experiments/evaluations/exa-access-ds41-r1.json)：模型费用 $0.01；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Exa 匿名远程 MCP 为免 Key 免费层，本轮全程未提供账号、Key 或支付方式，亦未触发任何计费；免费层适用且带限流。; https://exa.ai/docs/reference/exa-mcp (官方文档: 'No API key is required to get started'); 本次工具响应中的免额度提示: "You've hit Exa's free MCP rate limit. To continue using without limits, create your own Exa API key."

  结论与限制：执行者按 ENVIRONMENT.md 指定的 Exa 官方匿名远程 MCP（https://mcp.exa.ai/mcp）完成 keyless 接入，实测 web_search_exa 返回真实网页结果（查询 'history of the Python programming language'，含标题与有效 URL），并将连接配置写入指定持久目录 /home/node/service-tools/service-config.json；答复与响应一致，无账号/Key/秘密，无人工介入。

**tavily / keyless-search-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 300s · natural · none

准备：Fresh runtime, no account, prewritten calling scripts or previous results. OpenCode 1.18.35 / DeepSeek V4.1 Flash high; 25 model requests per role, 32000 output tokens/request, execution and grading 300s. New budget conditions retained separately from older runs.

- [tavily-access-ds41-r1](../data/experiments/evaluations/tavily-access-ds41-r1.json)：模型费用 $0.0061；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 仅使用 Tavily 官方 keyless 模式，未付款、未绑定支付、未使用付费端点。; https://docs.tavily.com/documentation/keyless

  结论与限制：通过指定入口 Tavily 官方 keyless Search API 完成一次真实网页搜索，HTTP 200 返回含标题与有效 URL 的结果，答复与响应一致；连接配置已写入指定持久目录且无秘密泄露；免注册入口未强行注册，未使用付费端点。独立复测同入口同样返回真实结果。

<a id="comparison-6c4685dc77de"></a>

### financial-fx-001 v1

**ecb-data / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none · 独立验收可参考同期 2 家服务的答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v1 task, model, effort, tools and 25-request budget for both services. Reference values and peer results withheld from executors. Execution 600s; independent grading 300s.

- [ecb-data-fx-001-ds41-r1](../data/experiments/evaluations/ecb-data-fx-001-ds41-r1.json)：模型费用 $0.0053；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: ECB 官方站声明其网站信息可免费使用/免费获取；本次执行未提供账户、Key 或支付方式，对 ECB Data Portal API 单次未认证 GET 成功，无计费、订阅或超出免费范围的操作。; https://www.ecb.europa.eu/services/disclaimer/html/index.en.html; public-review/free-rule.md; public-review/verification.md

  结论与限制：本次执行通过指定 ECB Data Portal REST API（未认证、免费）取得 USD/EUR 参考汇率，正确完成非发布日回退、币种方向与逐笔舍入；三笔欧元金额与合计 211.65 EUR 与独立参考逐一核对一致，并给出可核对的序列键、请求 URL 与官方文档出处。

**frankfurter / data-api** — 1 完成 / 0 未完成 / 0 环境无效。

1.18.35 / deepseek-flash / high · 600s · natural · none · 独立验收可参考同期 2 家服务的答案

准备：Reuses independently passed access from this batch with fresh session and cleaned workspace. Same frozen v1 task, model, effort, tools and 25-request budget for both services. Reference values and peer results withheld from executors. Execution 600s; independent grading 300s.

- [frankfurter-fx-001-ds41-r1](../data/experiments/evaluations/frankfurter-fx-001-ds41-r1.json)：模型费用 $0.0052；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Frankfurter 公网 API 免 Key、无账户、无付费层级；本次执行及验收复核均经公开入口取得数据，未使用 Key 或产生费用。; https://frankfurter.dev/ 官方文档：Free, open-source exchange rates API; No API key required; grading/artifacts/evidence/frankfurter-fx-001-verification.md 记录的本次无 Key 公开调用

  结论与限制：本次执行在指定服务 Frankfurter API v2 的 ECB 提供方路由上按发生日获取 ECB 参考汇率，非发布日（2026-08-15 周六）正确回退到 2026-08-14，币种方向为 EUR/USD 且按乘算关系使用，三笔欧元金额 69.16/108.07/34.42 与合计 211.65 经独立重算及独立 ECB 参考（1.1567/1.1593）核对一致，出处可核对，免费入口无 Key。

<a id="comparison-d5ebeb408e55"></a>

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

<a id="comparison-fb6dcb23321f"></a>

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

<a id="comparison-90e1d23f0407"></a>

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

<a id="comparison-cbad562eed82"></a>

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

<a id="comparison-bd611da6270b"></a>

### financial-access-001 v1

**tracefour / data-api-keyless** — 0 完成 / 1 未完成 / 0 环境无效。

1.18.29 / glm-5.3-flash / high · 600s · natural · none

准备：Account-free public API; no account, key or call code pre-provisioned. Dedicated service/route container; fresh session per task, retaining only service configuration and installed dependencies. Controller researched candidates and froze independent references; cloud execution and grading use GLM-5.3-Flash/high.

- [tracefour-access](../data/experiments/evaluations/tracefour-access.json)：模型费用 $0.0071；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/328a5f5d6024c673c4d5e37bad8dab17ab8e79ee/model_prices_and_context_window.json)（2026-09-09T10:51:49.718Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: 规则：指定入口为免 Key 免费读取，限 60 次/小时/IP。本次适用性：全程仅约 9 次免 Key 只读 GET，远低于限额；所有请求在 Cloudflare 边缘即被 403 质询拒绝，服务未实际处理任何请求；未提供也未创建任何账户、Key 或支付方式，无付款回执。故本次服务侧费用为 0。模型 token 与模型费用由运行器统一核算，不在此列。; reference.json（本题冻结参考 free_rule：Keyless reads 60 requests/hour/IP; compilation CC BY 4.0 with attribution）; execution/artifacts/probe-results.txt; grading/artifacts/evidence/independent-verification.md

  结论与限制：本轮通过指定 REST 方式接入 Tracefour 未完成：文档页和实际尝试的 URL 从本轮云端环境返回 Cloudflare 403 challenge，没有取得真实金融数据；已保存含阻碍说明的配置，无人工介入。独立验收复现了 /v1 和 /api-docs 的 403。执行者未成功读取文档，也未调用后来研究确认的 /v1/congress 等数据路由，因此这些观察不能证明全部数据端点、MCP 或其他网络环境都不可用；本轮没有执行交易披露业务题。

<a id="comparison-8624e51d6979"></a>

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

<a id="comparison-1149cab0b0f0"></a>

### payment-acceptance-001 v1

**paddle / sandbox-api** — 0 完成 / 1 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · natural · provided: PADDLE_SANDBOX_API_KEY

准备：A separate sandbox account was registered and email-verified by the evaluator using synthetic test business/address details. No KYC or production activation occurred. A sandbox API key expires after seven days and grants read/write access only to products, prices, transactions, checkout domains and client-side tokens. A preflight API read confirmed an empty product catalog. No product, price, transaction, checkout page or solution code was prepared. A dedicated empty local Chromium browser is supplied over CDP to avoid macOS sandbox browser-launch failures; the executing Codex still uses workspace-write sandboxing. Registration, browser startup and evaluator work are outside measured execution metrics. This configuration differs from earlier browser-less trials.

- [codex-20260909T032011.000426Z-paddle](../data/experiments/evaluations/codex-20260909T032011.000426Z-paddle.json)：模型费用 $1.20；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Sandbox-only API requests, with no completed payment, no paid subscription or live account activation. Official docs specify no real money in sandbox and pricing has no monthly fees. The $12 product price is not a service cost.; https://developer.paddle.com/sdks/sandbox/; https://www.paddle.com/pricing

  结论与限制：The default newly registered Paddle sandbox account rejected creation of the ebook product with product_tax_category_not_approved for ebooks. No product, transaction or customer checkout link was created. This is an account/category access barrier for this scenario, not evidence that Paddle cannot serve any product or approved account. The dedicated browser connected successfully but had no dashboard login, as disclosed. Independent authenticated dashboard inspection shows eBook Not Requested, SaaS Approved, and a notice that category approval must be requested in the live account; no live application was made.

<a id="comparison-bc10c53a81ca"></a>

### payment-acceptance-001 v1

**paas-build / rest-api** — 0 完成 / 0 未完成 / 1 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · natural · provided: PAAS_SANDBOX_ACCESS_TOKEN, PAAS_SANDBOX_VENDOR_ID

准备：A new sandbox-only merchant was provisioned by the evaluator through the official API with notifications disabled. Sandbox token identity was checked before execution. No product, price, checkout, production merchant or solution code was prepared. Signup identity stays private; preparation time and evaluator tokens are outside execution metrics.

- [codex-20260908T113239.160717Z-paas-build](../data/experiments/evaluations/codex-20260908T113239.160717Z-paas-build.json)：模型费用 $2.00；Each recorded request × saved LiteLLM standard API rates for its input length, then summed. Estimate, not an account charge; excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard; context tier selected per request）。服务费用 $0；confirmed_free: Official instructions state that the sandbox is free to play with. Only sandbox checkout creation and reads occurred; no payment was submitted. The $12 product price is not a service charge.; https://paas.build/SKILL.md

  结论与限制：The executor created a real sandbox checkout, but macOS sandbox permissions prevented Chromium from launching. Exclude this trial from service completion-rate comparisons. Independent post-run browser inspection also showed only the checkout shell, without the product, amount or payment form; this is a separate observed usability issue requiring a fresh run after environment repair.

<a id="comparison-6203194a76cd"></a>

### collaborative-tables-001 v2

**grist / rest-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · natural · provided: GRIST_API_KEY, GRIST_WORKSPACE_ID

准备：Existing dedicated free test account; API credential and a newly created empty workspace prepared before timing. No business schema, records or adapter supplied. Setup and external verification excluded from measured tokens/time. No payment enabled.

- [codex-20260908T035504.472694Z-grist](../data/experiments/evaluations/codex-20260908T035504.472694Z-grist.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：Natural v2 created a real online table with three correct final actions and returned the matching link and two outstanding tasks. Independent remote read after executor exit matched all user facts. 11 business API requests observed in executed code and CLI outputs, within 40. Setup and external review excluded; one observation, not a typical-cost estimate or service ranking.

**notion / rest-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · natural · provided: NOTION_API_TOKEN, NOTION_PARENT_PAGE_ID

准备：Existing dedicated free test account; API credential and a newly created empty private parent page prepared before timing. No business schema, records or adapter supplied. Setup and external verification excluded from measured tokens/time. No payment enabled.

- [codex-20260908T035504.906378Z-notion](../data/experiments/evaluations/codex-20260908T035504.906378Z-notion.json)：模型费用 $0.75；Actual recorded usage × saved LiteLLM standard API rates; estimate at the snapshot date, not an account charge. Excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：Natural v2 created a real online table with three correct final actions and returned the matching link and two outstanding tasks. Independent remote read after executor exit matched all user facts. 7 business API requests observed in executed code and CLI outputs, within 40. Setup and external review excluded; one observation, not a typical-cost estimate or service ranking.

<a id="comparison-1420586eae17"></a>

### database-todos-001 v1

**turso / platform-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · provided: TURSO_API_TOKEN, TURSO_ORGANIZATION

准备：Outer Agent registered a new dedicated Free organization using Google sign-in, selected a username and created an organization API token; no card/payment, no existing database. Signup and token creation outside measured time/tokens. Executor receives only this organization and token, and must provision its own test database.

- [codex-20260907T113506.422646Z-turso](../data/experiments/evaluations/codex-20260907T113506.422646Z-turso.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：Independent writer/reader processes and outer reviewer remote re-read confirm persisted todos. Dedicated free organization and API token were prepared before timing; database/group and SQL tokens were created during execution. No payment; overages remain off. Free archival and token expiry limit long-term use.

<a id="comparison-9dbe771526ac"></a>

### web-search-001 v1

**exa / search-api** — 0 完成 / 1 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · provided: EXA_API_KEY

准备：Free account prepared by the outer Agent using browser Google sign-in and onboarding; no card or payment. Signup work is outside measured session tokens/time; only EXA_API_KEY provided, no adapter or research context.

- [codex-20260907T112952.581354Z-exa](../data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json)：模型费用 —；Token usage was not reported. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：The authenticated Exa API returned real search results, but the executor spent its 10-search allowance on source discovery/evidence work and reached the 600-second wall-clock limit without a final answer. This is a task-budget failure, not API unavailability. CLI emitted no turn.completed usage event before interruption: tokens remain unknown, not zero. Free account was prepared outside measured time; no payment.

<a id="comparison-b5f21fc39ab4"></a>

### web-search-001 v1

**firecrawl / public-search-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：No service account or resource prepared before the measured session.

- [codex-20260907T112951.715536Z-firecrawl](../data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：Anonymous Firecrawl search and direct reads of returned official sources support all three answers. Two cited pages were discovered through links inside result descriptions, not separate ranked hits; this satisfies frozen v1 response-URL criterion. No account or payment; a single-run token difference does not establish overall provider superiority.

<a id="comparison-fdecec09a4b6"></a>

### database-todos-001 v1

**neon / ephemeral-api** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：No service credentials provided.

- [codex-20260907T112258.549053Z-neon](../data/experiments/evaluations/codex-20260907T112258.549053Z-neon.json)：模型费用 —；Context-dependent pricing requires per-request usage; session totals cannot establish the applicable tier. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：Independent remote re-read confirms the three synthetic todos and update; separate writer/reader processes and count response satisfy v1. No signup or payment; ephemeral database expires 2026-09-10T11:23:56.173Z. This establishes short-term persistence only.

<a id="comparison-c77feef961a0"></a>

### flights-search-001 v1

**kiwi / search-mcp** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：unknown

- [codex-20260907T092329.724439Z-kiwi](../data/experiments/evaluations/codex-20260907T092329.724439Z-kiwi.json)：模型费用 $0.84；Actual recorded usage × saved LiteLLM standard API rates; estimate at the snapshot date, not an account charge. Excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：独立核对当次请求、完整服务SSE响应和最终答案，3个方案均满足 flights-search-001 v1：BGY→EIN FR3460 62 EUR、LIN→AMS U25405 68 EUR、MXP→AMS U23851 75 EUR，均为2026-09-25出发、1名成人单程经济舱。单次运行212.222秒内完成，执行中人工介入0。初次GET 406后MCP POST成功，无未解决执行阻碍；仅证明本次基础搜索完成，Agent与服务逐次实付费用未报告，保留未知。 2026-09-07费用口径修订：本字段统计本次调用服务的新增实付。实际使用无账户、无凭据的公开入口，且没有付款，因此将原先因缺账单填写的未知修正为0；原始复核说明保留，不涉及机票报价。

<a id="comparison-45effe165cf4"></a>

### flights-search-001 v1

**ignav / public-playground** — 1 完成 / 0 未完成 / 0 环境无效。

codex-cli 0.153.4 / gpt-6-astra / xhigh · 600s · legacy · none

准备：unknown

- [codex-20260907T083644.877057Z-ignav](../data/experiments/evaluations/codex-20260907T083644.877057Z-ignav.json)：模型费用 $0.93；Actual recorded usage × saved LiteLLM standard API rates; estimate at the snapshot date, not an account charge. Excludes non-token tool fees. [LiteLLM价格快照](https://raw.githubusercontent.com/BerriAI/litellm/0e26edfdb95c8288a610cba4746af2bc1f2fe312/model_prices_and_context_window.json)（2026-10-08T10:40:18.309Z，standard）。服务费用 $0；旧记录新增实付金额；沿用原复核，不补造回执或估算依据。

  结论与限制：基础找票任务完成：3个提交方案与当次服务响应及任务参数相符。单次同机试跑，不代表其他入口或长期成功率。
