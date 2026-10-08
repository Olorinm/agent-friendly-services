Publication excerpt. Original independent evidence SHA256: 897bc24e4cea6e19f9241082c3e72d5d7c9c50bbe81dda24769565af335db96d. Original material is retained privately; controller additions are labelled.

# Firecrawl 调用与 2027 表核验摘要（脱敏）

本文件由验收者从执行记录中摘录必要业务字段，删除账号与密钥。原始会话/工具日志不公开。

## 指定服务调用（Firecrawl 匿名 Public Scrape API）

- 请求：`POST https://api.firecrawl.dev/v2/scrape`，`Content-Type: application/json`，无 `Authorization`/API Key 头。
- 请求体：`{"url":"https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/","formats":["markdown","html"]}`
- 响应：HTTP 200；`success=true`；`data.metadata` = {title: "Federal Holidays", statusCode: 200, sourceURL: "https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/"}。
- 免费规则来源（官方文档）：https://docs.firecrawl.dev/features/scrape —— “No API key needed to get started — add one for higher rate limits”。本次即以无 Key 匿名方式取得 200，无账户/支付信息。

## 响应中提取的 “2027 Holiday Schedule” 表（markdown 原文）

| Date | Holiday |
| --- | --- |
| Friday, January 01 | New Year’s Day |
| Monday, January 18 | Birthday of Martin Luther King, Jr. |
| Monday, February 15 * | Washington’s Birthday |
| Monday, May 31 | Memorial Day |
| Friday, June 18 ** | Juneteenth National Independence Day |
| Monday, July 05 ** | Independence Day |
| Monday, September 06 | Labor Day |
| Monday, October 11 | Columbus Day |
| Thursday, November 11 | Veterans Day |
| Thursday, November 25 | Thanksgiving Day |
| Friday, December 24 ** | Christmas Day |

（脚注 `*`/`**` 为页面原始标记，交付 CSV 已去除。）

Scope: one public HTML table and CSV delivery; this does not demonstrate arbitrary dynamic, authenticated or anti-bot page coverage.

Controller cache observation from actual response metadata: cacheState=hit; cachedAt=2026-10-08T10:02:18.822Z; creditsUsed=1. The request did not set maxAge, so this is a cached response and not proof of a fresh origin fetch. The target rows nevertheless matched the separately frozen official table.

Explicit free-price basis: https://docs.firecrawl.dev/rate-limits , Keyless section, states free usage with separate per-IP daily request and credit ceilings; this run used that anonymous Scrape route.
