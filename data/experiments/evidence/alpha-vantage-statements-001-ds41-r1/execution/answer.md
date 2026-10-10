Alpha Vantage 数据已取到。为核对 GAAP 数字与原始财报出处，我再用 SEC EDGAR（原始财报官方库）交叉验证。
交叉验证一致。现将结果整理成表格并附原始 10-K 出处。
已完成。数据取自指定服务 Alpha Vantage REST API（`INCOME_STATEMENT`、`CASH_FLOW`），并用 SEC EDGAR XBRL 逐项核验一致。

**Apple vs Microsoft 2025 财年对比**（单位：十亿美元，GAAP）

| 指标 | Apple (AAPL) | Microsoft (MSFT) |
|---|---|---|
| 财年结束日 | 2025-09-27（AV 标签 2025-09-30） | 2025-06-30 |
| 营收 | 416.161 | 281.724 |
| 净利润 | 112.010 | 101.832 |
| 经营现金流 | 111.482 | 136.162 |

**原始财报出处（各公司 10-K）**
1. Apple Inc., Form 10-K, FY ended 2025-09-27 — SEC accession `0000320193-25-000079`（filed 2025-10-31）: https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm
2. Microsoft Corp., Form 10-K, FY ended 2025-06-30 — SEC accession `0000950170-25-100235`（filed 2025-07-30）: https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm

完整结果与核验说明见 `result.md`。注意两家财年口径不同（9 月 vs 6 月），跨公司比较需留意期间错位。