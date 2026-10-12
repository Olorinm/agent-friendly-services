Now I understand the API. Let me test connectivity with a small, real macro-financial query (single data point), using the required client identifier.
Connectivity confirmed (HTTP 200, real GDP value). Now let me write a reusable client and save the config.
Now a real macro-financial query (euro exchange rate) to confirm the financial use case:
Both queries succeeded. Now saving the reusable connection config to the designated persistent location.
已接好，可用。

**结论**：Eurostat Statistics API（指定入口 `.../statistics/1.0/data/`）连通，匿名免 Key，已用指定方式完成真实查询。

**实测（均 HTTP 200）**
- `nama_10_gdp time=2023 geo=EU27_2020 na_item=B1GQ unit=CP_MEUR` → EU27 2023 GDP = 17,294,868.6 百万欧元
- `ert_bil_eur_m currency=USD lastTimePeriod=3` → EUR/USD 月均 2026-09 = 1.1513

**已保存配置**
- 通用连接配置：`/home/node/service-tools/service-config.json`
- 复用脚本：`eurostat_client.py`（内置 2s 最小间隔+本地缓存）
- 结果摘要：`result.md`，原始响应 `test_gdp.json`、`cache/`

**无阻碍**：无需注册/凭据；遵守单线程、≥2s 间隔、只读小范围查询与来源署名。