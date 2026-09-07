<!-- GENERATED — npm run generate; source: data/experiments/evaluations/ -->
# 任务实测结果

每行只说明该服务入口在该任务和运行配置下的观察。Agent消耗只记录token，不换算货币；缓存输入已含在输入总数中。服务调用费用单独记录，unknown不等于0。点击结果可查看冻结的任务、独立复核与选取的证据；原始日志仍在本地。历史记录保留，不把不同任务、配置或日期直接平均成服务排名。

| 服务 / 入口 | 任务 / 版本 | 结果与证据 | 测试起始时间（含时区） | Harness / 模型 / 思考等级 | 输入 / 其中缓存 / 输出token | 耗时 | 服务调用费用（USD） | 执行中人工介入 |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| kiwi / search-mcp | flights-search-001 (v1) | [completed](../data/experiments/evaluations/codex-20260907T092329.724439Z-kiwi.json) | 2026-09-07T09:23:29.733240+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 204087 / 163968 / 5464 | 212.222s | 0 | 0 |
| kiwi / search-mcp | flights-search-001 (v1) | [invalid_run](../data/experiments/evaluations/codex-20260907T091621.435575Z-kiwi.json) | 2026-09-07T09:16:21.457471+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | unknown | 1s | 0 | 0 |
| ignav / public-playground | flights-search-001 (v1) | [completed](../data/experiments/evaluations/codex-20260907T083644.877057Z-ignav.json) | 2026-09-07T08:36:44.885519+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 207427 / 157696 / 5517 | 204.375s | 0 | 0 |
| kiwi / search-mcp | flights-search-001 (v1) | [completed](../data/experiments/evaluations/codex-20260907T083627.884537Z-kiwi.json) | 2026-09-07T08:36:27.894085+00:00 | codex-cli 0.153.4 / gpt-6-astra / xhigh | 184152 / 129408 / 3754 | 156.912s | 0 | 0 |
