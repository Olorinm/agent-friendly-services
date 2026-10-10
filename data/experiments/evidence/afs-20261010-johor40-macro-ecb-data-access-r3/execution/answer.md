Docs reviewed. Now testing the specified entry with a basic query (respecting 2s spacing and client identifier).
HTTP 200, real data returned. Now confirming the default (non-CSV) format works too.
Both response formats work. Let me verify the metadata (dataflow) endpoint too, then build reusable tooling.
Dataflow metadata works too (the 406 was only from an unsupported `Accept: application/json`). Now creating the reusable client and persistent config.
All checks pass. Persisting the reusable client alongside the config.
已接通，查询验证通过。

**结果**
- 指定入口 `https://data-api.ecb.europa.eu/service/`：匿名可用，无需账号/Key/付费。
- 实测 HTTP 200：
  - 数据（CSV）：`/service/data/EXR/M.USD.EUR.SP00.A?format=csvdata&lastNObservations=3` → 返回 2026-07~09 月均 USD/EUR 汇率。
  - 数据（默认 SDMX-ML 2.1）：同路径无 `format` → `application/vnd.sdmx.genericdata+xml;version=2.1`。
  - 元数据：`/service/dataflow/ECB/EXR` → SDMX 结构 XML。
  - 日期区间查询：`EXR/D.USD.EUR.SP00.A?startPeriod=2026-09-01&endPeriod=2026-09-10` → 正常返回。
- 无阻碍；仅 `Accept: ...+json` 会返回 406（ECB 只提供 XML/CSV，非故障）。

**保存的配置（后续调用）**
- `service-config.json`：base_url、免认证说明、端点模板、查询参数、格式、限流策略（单线程/≥2s/遇 403·429 停止）、署名、已验证记录。
- `ecb_query.py`：标准库客户端，支持 `flow/key`、`--start/--end/--last/--first/--updated-after/--detail/--format/--meta`，自动 UA、≥2s 节流、相同请求走缓存。
  例：`python3 ecb_query.py EXR/M.USD.EUR.SP00.A --format csvdata --last 3`

**持久位置**
- `/home/node/service-tools/service-config.json`
- `/home/node/service-tools/ecb_query.py`
- 本题证据与缓存：工作目录 `out/`、`cache/`（无外部依赖，未用 installed-tools）。

**署名要求**：引用时标注来源 European Central Bank, ECB Data Portal，并说明是否有修改。