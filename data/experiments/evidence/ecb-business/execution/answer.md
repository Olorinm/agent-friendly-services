配置已就绪。现在调用 ECB API 查询指定日期区间的美元/欧元参考汇率：
三笔日期中 8-15（周六）无发布，回退至 8-14。用 Python 精确计算并写入结果文件：
三笔美元支出按 ECB 参考汇率折算结果如下（逐笔四舍五入到欧分）：

| 日期 | 金额 (USD) | 适用汇率日 | USD/EUR 参考汇率 | 金额 (EUR) |
|---|---|---|---|---|
| 2026-08-14 | 80.00 | 2026-08-14 | 1.1567 | 69.16 |
| 2026-08-15 | 125.00 | 2026-08-14（周六无发布，回退最近发布日） | 1.1567 | 108.07 |
| 2026-08-17 | 39.90 | 2026-08-17 | 1.1593 | 34.42 |
| **合计** | 244.90 | | | **211.65 EUR** |

**汇率出处**：欧洲央行数据门户 REST API（`ecb-data` 指定服务），数据流 `EXR/D.USD.EUR.SP00.A`（US dollar/Euro ECB reference exchange rate，每日 2.15 pm C.E.T. 发布），实际调用：
`https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2026-08-10&endPeriod=2026-08-18&format=csvdata`（HTTP 200，逐日原始观测值，无插补）。

计算脚本与原始响应已存于本题目录：`convert.py`、`rates.csv`、`result.txt`。