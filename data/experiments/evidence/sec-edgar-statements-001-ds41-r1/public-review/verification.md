公开证据节选；独立核验原文件 SHA256：6f3295baf07f6fe9dca811ac71fded58544f010333920336cc2a869a6261607f。原始材料私有保存，以下编辑不改验收结论。

# Independent verification — SEC EDGAR FY2025 comparison

- Task: financial-statements-001/v1 (Apple AAPL vs Microsoft MSFT, FY2025 revenue / net income / operating cash flow, USD billions, original report provenance).
- Assigned service / entry: SEC EDGAR XBRL APIs, https://data.sec.gov/.
- Grader check: values re-read from the collected raw SEC responses under `execution/artifacts/raw/`; Apple `NetIncomeLoss` additionally re-fetched live from `data.sec.gov` and agreed.

## Six indicators (from SEC 10-K XBRL, USD)

| Company | Metric | us-gaap tag | Period (start..end) | Value (USD) | Accession |
|---|---|---|---|---|---|
| Apple Inc. | Revenue | RevenueFromContractWithCustomerExcludingAssessedTax | 2024-09-29..2025-09-27 | 416,161,000,000 | 0000320193-25-000079 |
| Apple Inc. | Net income | NetIncomeLoss | 2024-09-29..2025-09-27 | 112,010,000,000 | 0000320193-25-000079 |
| Apple Inc. | Operating cash flow | NetCashProvidedByUsedInOperatingActivities | 2024-09-29..2025-09-27 | 111,482,000,000 | 0000320193-25-000079 |
| Microsoft Corp. | Revenue | RevenueFromContractWithCustomerExcludingAssessedTax | 2024-07-01..2025-06-30 | 281,724,000,000 | 0000950170-25-100235 |
| Microsoft Corp. | Net income | NetIncomeLoss | 2024-07-01..2025-06-30 | 101,832,000,000 | 0000950170-25-100235 |
| Microsoft Corp. | Operating cash flow | NetCashProvidedByUsedInOperatingActivities | 2024-07-01..2025-06-30 | 136,162,000,000 | 0000950170-25-100235 |

All six figures are 10-K FY annual periods (duration 363–364 days), not natural-year, quarterly, TTM or adjusted values.

Fiscal-year ends (from SEC submissions metadata): Apple 2025-09-27 (10-K filed 2025-10-31, primary `aapl-20250927.htm`); Microsoft 2025-06-30 (10-K filed 2025-07-30, primary `msft-20250630.htm`).

## Original-report provenance

- Apple: https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm
- Microsoft: https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm

## Free-of-charge rule

SEC EDGAR developer page (https://www.sec.gov/search-filings/edgar-application-programming-interfaces) states the data APIs "do not require any authentication or API keys to access." This run used only the free `data.sec.gov` endpoints (`companyconcept`, `submissions`) with a descriptive User-Agent, no key, no registration, no payment and no paid endpoint.
