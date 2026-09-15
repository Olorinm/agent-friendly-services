# 独立验收核验摘录（financial-fx-001/v1）

## 1. 星期与回退（验收环境独立计算）
2026-08-14=Friday；2026-08-15=Saturday；2026-08-16=Sunday；2026-08-17=Monday。
2026-08-15（周六）无 ECB 发布，答案按规则取前一发布日 2026-08-14。

## 2. 指定服务当次汇率（执行时采集，execution/artifacts/rates_raw.json）
GET https://api.frankfurter.dev/v2/rates?from=2026-08-13&to=2026-08-17&base=USD&quotes=EUR&providers=ecb
→ 2026-08-14 rate 0.86453；2026-08-17 rate 0.86259（8-15/8-16 无行）。
另一次调用带 expand=providers，响应含 {"key":"ECB","date":"2026-08-14","rate":0.86453}，确认发布方 ECB。

## 3. 验收环境直连复核（本次验收时重新请求）
- date=2026-08-14 → 0.86453，providers=[{key:"ECB",date:"2026-08-14"}]
- date=2026-08-17 → 0.86259，providers=[{key:"ECB",date:"2026-08-17"}]
- date=2026-08-15 → 返回 2026-08-14 行 0.86453（服务端同样按最近前发布日回退）
与执行时采集数值一致。

## 4. 与独立参考（reference.json，ECB 官方 eurofxref-hist-90d.xml）交叉核对
ECB USD per EUR：2026-08-14=1.1567；2026-08-17=1.1593。
1/1.1567=0.86453；1/1.1593=0.86259 → 与服务返回的 USD→EUR 汇率互为倒数，方向与数值一致。

## 5. 独立重算（Decimal, ROUND_HALF_UP）
- 80.00 × 0.86453 = 69.1624 → 69.16 EUR
- 125.00 × 0.86453 = 108.06625 → 108.07 EUR（汇率日 2026-08-14）
- 39.90 × 0.86259 = 34.417341 → 34.42 EUR
合计 69.16+108.07+34.42 = 211.65 EUR，与 reference.json 期望（69.16/108.07/34.42，合计 211.65）完全一致。

## 6. 免费规则来源
官方文档 https://frankfurter.dev/："Free, open-source exchange rates API ... No API key required"；FAQ："Is the API free for commercial use? Yes, absolutely"；"There are no quotas. Requests are rate-limited to prevent abuse, but there are no monthly or daily caps."
本次观察：执行与复核均仅匿名 GET 读取 api.frankfurter.dev，HTTP 200，无注册、无 Key、无支付。
