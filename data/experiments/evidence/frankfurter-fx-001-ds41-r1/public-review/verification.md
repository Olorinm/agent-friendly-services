公开证据节选：总控从独立验收记录选取必要内容；原始核验文件 SHA256：e64c08ade4c03d293ffa61d7020166b282217a38ec3ef187696946823df604c1。任务完成结论不变。

# Frankfurter FX-001 验收核验摘要（公开证据）

## 本次执行使用的服务与调用
- 指定服务入口：https://api.frankfurter.dev/v2/ （Frankfurter API v2）
- 执行者调用的 ECB 提供方路由（业务字段）：
  - `GET /v2/providers/ecb/rate/usd/eur?date=2026-08-14` → `{"date":"2026-08-14","base":"USD","quote":"EUR","rate":0.86453}`
  - `GET /v2/providers/ecb/rate/usd/eur?date=2026-08-17` → `{"date":"2026-08-17","base":"USD","quote":"EUR","rate":0.86259}`
  - 2026-08-15（周六）该路由返回 2026-08-14 的值（0.86453），无 08-15 发布日。

## 验收环境独立复核（2026-10-08）
- 重新请求同一 ECB 提供方路由，得到与本次执行一致的 `0.86453`（08-14）与 `0.86259`（08-17）；全程未使用账号或 API Key。

## 独立重算（逐笔 ROUND_HALF_UP 到欧分后加总）
- 2026-08-14：80.00 × 0.86453 = 69.1624 → 69.16 EUR
- 2026-08-15：125.00 × 0.86453 = 108.0663 → 108.07 EUR（回退用 08-14）
- 2026-08-17：39.90 × 0.86259 = 34.4173 → 34.42 EUR
- 合计：211.65 EUR
- 与独立参考 ECB 口径（USD per EUR 1.1567 / 1.1593）逐笔结果一致。

## 免费规则观察
- 官方文档 https://frankfurter.dev/ 明示：`Free, open-source exchange rates API ... No API key required`，公网 API 位于 api.frankfurter.dev。
- 本次实际调用均为无 Key、无账户的公开入口，返回正常数据，未产生付费。
