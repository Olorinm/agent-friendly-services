# 独立复测记录（验收环境，2026-09-15）

命令（无任何 Key/账号/认证头）：

```
curl -sS "https://api.frankfurter.dev/v2/rates?base=usd&quotes=eur,gbp"
```

实际响应（HTTP 200）：

```json
[{"date":"2026-09-15","base":"USD","quote":"EUR","rate":0.86406},{"date":"2026-09-15","base":"USD","quote":"GBP","rate":0.74009}]
```

- 与执行采集到的响应（数值、日期、格式）一致，确认服务真实可用且为免 Key 公开读取入口。
- 官方文档 https://frankfurter.dev/ 明示 "Free ... No API key required"；本次及执行中的实际请求均未带凭据即成功，落在该免费规则内。
