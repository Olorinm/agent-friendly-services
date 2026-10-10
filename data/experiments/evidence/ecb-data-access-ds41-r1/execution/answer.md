The API responds. Let me inspect the returned data and validate the documented access patterns.
Everything works (JSON, CSV, metadata). Now saving the persistent connection config and a verification result.
接通成功，无需账号/Key。

**验证结果**（指定入口 `https://data-api.ecb.europa.eu/service/`，2026-10-08，均 HTTP 200）：
- JSON：`/data/EXR/M.USD.EUR.SP00.A?lastNObservations=2&format=jsondata` → 返回最新美元/欧元汇率 `1.1513`
- CSV：`/data/EXR/D.USD.EUR.SP00.A?startPeriod=2024-01-01&endPeriod=2024-01-05&format=csvdata` → 4 行
- 元数据：`/datastructure/ECB/ECB_EXR1?references=children` → XML

**配置已存**：`/home/node/service-tools/service-config.json`（base_url、端点、格式、常用查询参数、限流说明）。验证记录：`verification-result.md`（本题工作目录）。

无阻碍。