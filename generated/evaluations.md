<!-- GENERATED — npm run generate; source: data/experiments/evaluations/ -->
# 任务实测结果

每行只说明该服务入口在该任务和运行配置下的观察。Agent消耗只记录token，不换算货币；缓存输入已含在输入总数中。服务调用费用单独记录，unknown不等于0。点击结果可查看冻结的任务、独立复核与选取的证据；原始日志仍在本地。免费账号的注册准备若发生在计时前，说明保存在 environment.preparation_note；表中 token 与耗时不包含这部分准备。历史记录保留，不把不同任务、配置或日期直接平均成服务排名。

| 服务 / 入口 | 任务 / 版本 | 预供服务凭据 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| notion / rest-api | collaborative-tables-001 (v1) | provided: NOTION_API_TOKEN, NOTION_PARENT_PAGE_ID | [completed](../data/experiments/evaluations/codex-20260908T032850.330773Z-notion.json) | 2026-09-08T03:28:50.359616+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 471247 / 425344 / 12291 | 463.678s | 0 | 0 |
| grist / rest-api | collaborative-tables-001 (v1) | provided: GRIST_API_KEY, GRIST_WORKSPACE_ID | [completed](../data/experiments/evaluations/codex-20260908T032113.556233Z-grist.json) | 2026-09-08T03:21:13.580494+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 769817 / 708608 / 11455 | 478.476s | 0 | 0 |
| turso / platform-api | database-todos-001 (v1) | provided: TURSO_API_TOKEN, TURSO_ORGANIZATION | [completed](../data/experiments/evaluations/codex-20260907T113506.422646Z-turso.json) | 2026-09-07T11:35:06.452325+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 755366 / 687616 / 12234 | 457.78s | 0 | 0 |
| exa / search-api | web-search-001 (v1) | provided: EXA_API_KEY | [not_completed](../data/experiments/evaluations/codex-20260907T112952.581354Z-exa.json) | 2026-09-07T11:29:52.610600+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | unknown | 602.017s | 0 | 0 |
| firecrawl / public-search-api | web-search-001 (v1) | none | [completed](../data/experiments/evaluations/codex-20260907T112951.715536Z-firecrawl.json) | 2026-09-07T11:29:51.792723+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 338090 / 295552 / 8728 | 362.944s | 0 | 0 |
| neon / ephemeral-api | database-todos-001 (v1) | none | [completed](../data/experiments/evaluations/codex-20260907T112258.549053Z-neon.json) | 2026-09-07T11:22:58.558715+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 452623 / 402560 / 12790 | 456.342s | 0 | 0 |
| exa / public-mcp | web-search-001 (v1) | none | [completed](../data/experiments/evaluations/codex-20260907T112257.401366Z-exa.json) | 2026-09-07T11:22:57.413717+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 917915 / 847104 / 13629 | 522.486s | 0 | 0 |
| kiwi / search-mcp | flights-search-001 (v1) | none | [completed](../data/experiments/evaluations/codex-20260907T092329.724439Z-kiwi.json) | 2026-09-07T09:23:29.733240+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 204087 / 163968 / 5464 | 212.222s | 0 | 0 |
| kiwi / search-mcp | flights-search-001 (v1) | none | [invalid_run](../data/experiments/evaluations/codex-20260907T091621.435575Z-kiwi.json) | 2026-09-07T09:16:21.457471+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | unknown | 1s | 0 | 0 |
| ignav / public-playground | flights-search-001 (v1) | none | [completed](../data/experiments/evaluations/codex-20260907T083644.877057Z-ignav.json) | 2026-09-07T08:36:44.885519+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 207427 / 157696 / 5517 | 204.375s | 0 | 0 |
| kiwi / search-mcp | flights-search-001 (v1) | none | [completed](../data/experiments/evaluations/codex-20260907T083627.884537Z-kiwi.json) | 2026-09-07T08:36:27.894085+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 184152 / 129408 / 3754 | 156.912s | 0 | 0 |
