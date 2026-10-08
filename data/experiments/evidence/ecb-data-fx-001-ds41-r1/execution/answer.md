按欧洲央行参考汇率逐笔折算：

| 支出日 | 原始金额 | 适用汇率 (1 EUR = USD) | 折算欧元 |
|---|---|---|---|
| 2026-08-14 (五) | 80.00 USD | 1.1567 | 69.16 EUR |
| 2026-08-15 (六, 未发布) | 125.00 USD | 1.1567（顺延用 08-14） | 108.07 EUR |
| 2026-08-17 (一) | 39.90 USD | 1.1593 | 34.42 EUR |
| **合计** | **244.90 USD** | — | **211.65 EUR** |

汇率出处：欧洲央行官方数据门户 REST API，序列键 `EXR/D.USD.EUR.SP00.A`（US dollar/Euro ECB reference exchange rate，每日 14:15 CET 发布）。
接口：`https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2026-08-01&endPeriod=2026-08-31&format=csvdata`
文档：https://data.ecb.europa.eu/help/api/data-examples

说明：08-15 为周六未发布汇率，按题目规则取此前最近发布日 08-14 的 1.1567；每笔四舍五入到欧分后加总。计算脚本与原始数据留存于本题目目录（`convert.py`、API 响应 `/tmp/opencode/ecb_usd.csv`）。