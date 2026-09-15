# Frankfurter 接入验证记录 (2026-09-15)

指定方式: REST API 直接 HTTP 调用, 入口 https://api.frankfurter.dev/v2/ (免 Key, 无注册步骤, 故未创建账号)

| 测试 | 结果 |
|---|---|
| GET /v2/rates?base=usd&quotes=eur,gbp,jpy,cny | 200, 2026-09-15: EUR 0.86406, GBP 0.74009, JPY 154.33, CNY 6.7074 |
| GET /v2/rate/eur/usd | 200, 1.1573 |
| GET /v2/rates?date=1999-01-04&base=eur | 200, USD 1.1759, GBP 0.70834 |
| GET /v2/rates?from=2026-08-01&to=2026-08-10&group=week | 200, 周降采样 2 行 |
| GET /v2/rates (Accept: application/x-ndjson) | 200, 逐行 JSON 流 |
| GET /v2/currencies | 200, 205 币种 |
| GET /v2/currency/xyz | 404 not found (错误处理正常) |
| group=day / format=ndjson | 422 (确认仅 week/month, 无 format 参数) |

配置已持久化: /home/node/service-tools/service-config.json (含端点清单、参数约定、错误码、验证结果)
结论: 接通, 可用指定方式查询最新/历史/时序汇率。
