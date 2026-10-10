公开证据节选：总控从独立验收记录选取必要内容；原始核验文件 SHA256：4c7f716f35162ed4e29e8917000c7b036e9f054a5c3bcc2316663e09a19ce4e7。任务完成结论不变。

# 核验摘要：Frankfurter 接入

## 1. 本次真实数据查询（指定入口 https://api.frankfurter.dev/v2/）

执行记录中的实测响应（HTTP 200，无鉴权头、无 Key）：

- `GET /v2/rate/EUR/USD` → `{"date":"2026-10-08","base":"EUR","quote":"USD","rate":1.1221}`
- `GET /v2/rates?base=USD&quotes=CNY,JPY,GBP` → `[{"date":"2026-10-08","base":"USD","quote":"CNY","rate":6.7002},{"date":"2026-10-08","base":"USD","quote":"GBP","rate":0.75518},{"date":"2026-10-08","base":"USD","quote":"JPY","rate":158.25}]`
- `GET /v2/rates?base=EUR&quotes=USD&from=2026-10-01&to=2026-10-08` → 8 条日频记录，首尾 `2026-10-01=1.1327`、`2026-10-08=1.1221`
- `GET /v2/coverage?base=EUR&quotes=USD` → `{"start_date":"1999-01-01","end_date":"2026-10-08"}`

独立复核（验收环境直接请求）：`GET /v2/rate/EUR/USD` 返回同一结果 `rate=1.1221`、`date=2026-10-08`，HTTP 200。

## 2. 保存的配置

`/home/node/service-tools/service-config.json`（持久目录），写入成功且通过 `python3 -m json.tool` 校验；内容含 `base_url`、9 个端点、查询参数（base/quotes/from/to/date/providers/group/expand）、示例与本次实测记录；`auth.type="none"`。retained-files 记录为 `service-config.json`。

## 免费依据

Frankfurter 官方文档 https://frankfurter.dev/ 说明其公共 API 免费、无需 Key，仍受防滥用速率限制。本次匿名调用符合该入口条件。
