公开证据节选；独立核验原文件 SHA256：c505f80fbd75454465815df5bbc370421b88f8a60d4b80223c8f82aeb755093e。原始材料私有保存，以下编辑不改验收结论。

# SEC EDGAR 接入验收核验摘要

本文件为验收方从本次运行采集记录中整理的脱敏业务证据，非执行者交付物。

## 1. 指定服务与调用方式
- 指定入口：`https://data.sec.gov`（SEC EDGAR REST API）。
- 认证方式：仅需声明性 `User-Agent`（client_name + contact），无需 API Key、无需注册。
  - 官方说明（SEC EDGAR API 页）："These APIs do not require any authentication or API keys to access."
    https://www.sec.gov/search-filings/edgar-application-programming-interfaces

## 2. 本次真实查询观察（均直连 data.sec.gov）
- `GET /submissions/CIK0000320193.json` → HTTP 200；Apple Inc.，ticker AAPL，fiscalYearEnd 0926。
- `GET /api/xbrl/companyconcept/CIK0000320193/us-gaap/Revenues.json` → HTTP 200；`us-gaap Revenues USD`，11 期；最新一期 end 2018-09-29 val 62,900,000,000。
- `GET /api/xbrl/companyfacts/CIK0000320193.json` → HTTP 200；taxonomies `dei`+`us-gaap`。
- `GET /api/xbrl/frames/us-gaap/Revenues/USD/CY2023.json` → HTTP 200；返回 2678 家公司。
- 响应为 gzip，需解压；限流 ≤10 请求/秒。

## 3. 已保存的持久连接配置
- `/home/node/service-tools/service-config.json` 写入成功（1631 字节），内容为可复用配置：
  `base_url`、`auth`(user-agent-header)、`default_headers`、`submissions`/`companyconcept`/`companyfacts`/`frames` 四类端点、`cik_format`、`rate_limit`、gzip 编码说明、`verified_at_utc`。
- 读回校验：`config ok: SEC EDGAR (data.sec.gov) | ua set: True`。
- 可复用客户端脚本：`execution/artifacts/sec_edgar_client.py`；`python3 sec_edgar_client.py 320193` 输出 `Apple Inc. ['AAPL'] CIK 0000320193`。

## 4. 服务费用（免费规则）
- 官方规则（SEC FAQ）："All Government-created content on sec.gov and EDGAR public filing content are free to access and reuse."
  https://www.sec.gov/about/webmaster-frequently-asked-questions
- 本次适用观察：上述查询仅使用声明性 User-Agent，未使用 API Key、账户、支付方式或付费端点，未产生任何账单/回执。

## 5. 材料一致性说明
- `ENVIRONMENT.md` 提及 Alpha Vantage 免费 Key，但环境提供的 `credentials.json` 仅含 SEC 的 client_name/contact，无 Alpha Vantage Key；本轮指定入口为 data.sec.gov，执行者未凭空索取或注册其他账号。
