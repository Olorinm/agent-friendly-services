Now let me test connectivity to the specified endpoint with a real, small read-only query. Requests are single-threaded with ≥2s spacing per protocol.
Connectivity confirmed (HTTP 200, JSON-stat 2.0). Now verifying alternate formats and a financial dataset via the same endpoint.
Docs confirm the STATISTICS endpoint only accepts `format=JSON` (my `format=CSV` → 400 is expected). Now a clean financial-dataset query with real values, then inspect dimension codes.
Clean financial query confirmed: euro-area long-term interest rate = **3.60263%** (2026-08). Now writing the reusable script and the shared connection config.
Both queries verified. Now saving the shared connection config for later tasks.
已接通，指定方式可正常查询数据。

**结果**
- 入口 `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{datasetCode}`，HTTP 200，返回 JSON-stat 2.0，免账号/Key、免费。
- 实测有效数据：欧元区长端利率 `irt_lt_mcby_m`（geo=EA, lastTimePeriod=1）= **3.60263**（2026-08）；欧盟 HICP 通胀 `prc_hicp_manr` = 2.5/2.4/2.3（2025-10~12）。
- 关键约束（官方文档+实测）：该 STATISTICS 端点的 `format` **只接受 `JSON`**；`format=CSV` 返回 400 `Invalid value for 'wsOutputFormat' parameter`。CSV/SDMX 属于另一组 SDMX 端点，本轮不使用。

**交付物**
- 查询脚本：`eurostat_query.py`（当前工作目录，支持 `--dataset/--filter/--last/--since/--until/--rows`，含 403/413/400 处理）
- 连接配置：`/home/node/service-tools/service-config.json`（端点、参数、UA `agent-friendly-services/20261010`、单线程≥2s、缓存与错误处理，供后续任务复用）
- 原始响应证据：`response_*.json`（含一次 400 示例 `response_hicp.csv`）

**说明**：无需注册，未创建任何账号。未遇到限流/验证码；所有请求单线程且间隔≥2秒，未轮换 IP/身份。