公开证据节选；独立核验原文件 SHA256：a4ec38502fbb8d6f0383a835d005cf3147ff4afaed727e893b400e235ae63b71。原始材料私有保存，以下编辑不改验收结论。

# 核验摘要 — Alpha Vantage 本次执行

任务：financial-statements-001 / v1；target_run_id：alpha-vantage-statements-001-ds41-r1。

## 指定服务取数（执行采集副本 execution/artifacts/）
Alpha Vantage REST API `INCOME_STATEMENT`、`CASH_FLOW` 的 `annualReports` 全年值：

| 公司 | 财年结束（AV fiscalDateEnding） | 营收 (USD) | 净利润 (USD) | 经营现金流 (USD) |
|---|---|---|---|---|
| Apple (AAPL) | 2025-09-30（实际期末 2025-09-27） | 416,161,000,000 | 112,010,000,000 | 111,482,000,000 |
| Microsoft (MSFT) | 2025-06-30 | 281,724,000,000 | 101,832,000,000 | 136,162,000,000 |

对应十亿美元：AAPL 416.161 / 112.010 / 111.482；MSFT 281.724 / 101.832 / 136.162。

## 与 SEC 原件交叉核对（执行采集副本 execution/artifacts/sec_*.json）
- Apple 10-K accession 0000320193-25-000079（filed 2025-10-31），期间 2024-09-29 → 2025-09-27：
  营收 416,161,000,000；净利润 112,010,000,000；经营现金流 111,482,000,000。
- Microsoft 10-K accession 0000950170-25-100235（filed 2025-07-30），期间 2024-07-01 → 2025-06-30：
  营收 281,724,000,000；净利润 101,832,000,000；经营现金流 136,162,000,000。

六项数值与独立参考（reference.json）完全一致，且为各公司 2025 财年全年合并 GAAP 口径。

## 接入与免费额度
Alpha Vantage 普通免费 Key 由总控预先注册（见 execution/artifacts/ENVIRONMENT.md），本次仅调用免费端点 INCOME_STATEMENT、CASH_FLOW 共 4 次，未使用付费/实时参数，低于 25 次/日免费额度。
官方免费规则：https://www.alphavantage.co/support/ （“free stock API service ... 25 API requests per day”）。


总控前提说明：此轮使用事前注册的普通免费账户；注册未计入本次执行耗时。独立验收将这一前置账号提供计为1次介入，接入验收则按会话内介入口径计0；原始数值保留，两者不能解释为全程自主注册。全夜已知Alpha数据请求合计7次（接入3、业务4），另有一次不含有效数据参数的入口检查，服务未提供额度账单。
