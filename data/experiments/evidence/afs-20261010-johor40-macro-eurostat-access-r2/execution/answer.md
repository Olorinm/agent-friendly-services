Docs confirmed. Endpoint format: `.../statistics/1.0/data/{datasetCode}?format=JSON&lang=EN&{filters}`. Now testing a small read-only query.
First query succeeded (HTTP 200, JSON-stat 2.0). Now one more probe with multiple filter values, then I'll save config.
Multi-value filters work. Now saving the reusable connection config and a query script.
已接通并验证可用。Eurostat Statistics API 为免费匿名入口，无需注册或 Key。

**实测（指定入口 `.../statistics/1.0/data/`，User-Agent 按授权标识）**
- `nama_10_gdp` 单值查询 → HTTP 200，JSON-stat 2.0，EU27_2020 2023 年 GDP = 17,294,868.6（百万欧元当期价）
- 多值过滤 `geo=DE&geo=FR&lastTimePeriod=2` → HTTP 200，返回 2×2 个值，证明多值/时间参数可用

**已保存的后续调用配置**
- `/home/node/service-tools/service-config.json` — 端点、GET 方法、请求模板与参数、请求头、限流/异步/署名约束、验证记录
- 当前目录 `eurostat_query.py` — 复用脚本（读取配置、2 秒限流、按 URL 哈希缓存），`cache/` 存原始响应

调用方式：`{endpoint}{datasetCode}?format=JSON&lang=EN&维度=值&...`（如 `.../data/nama_10_gdp?format=JSON&lang=EN&geo=DE&time=2023`）。

未遇到阻碍；无需注册或其他申请。注意遵守 2 秒请求间隔、结果署名 Eurostat 及派生数据修改说明。