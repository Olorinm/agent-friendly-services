# bargo-congress 接入验收摘要（financial-access-001/v1，run r1）

## 核对内容
- 指定入口为 `https://www.bargo.ai/free-apis/congress/v1`（REST 直连）。执行记录中共 2 次业务请求，均打到该入口：
  1. `GET /health` → HTTP 200，`status: ok`（服务存活与数据新鲜度）。
  2. `GET /trades?limit=5` → HTTP 200，`content-type: application/json`，JSON 顶层 `count=5`，返回 5 条真实 STOCK Act 披露记录，字段完整（member/ticker/type/amount_range/transaction_date/disclosure_date/est_price/perf_pct/filing_portal 等，filing_portal 指向众议院书记官官方披露系统）。原始响应体已从当次会话完整记录逐字核对，与执行者交付摘要一致；原始数据行不入公开材料。
- 配置保存：`/home/node/service-tools/service-config.json`（ENVIRONMENT.md 指定持久目录）写入成功，JSON 解析通过，含 base_url、全部端点、免 Key 限额、署名/再分发条款与验证状态（`verification.status: connected`）；运行器 retained-files 清单确认该文件保留，可供新会话复用。
- 授权合规：未注册、未付款、未写远端；仅 2 次请求、`limit=5`（≤5 条），响应头 `x-ratelimit-remaining: 28`（限 30）与用量吻合，未绕过配额。
- 执行时长约 2 分钟（上限 900 秒）；工具采集完整，源文件哈希已验证。

## 结论
接入成功：真实数据查询 + 可复用配置均达成，无阻碍。

## 来源
- 服务与免费规则：https://www.bargo.ai/free-apis/congress （"FREE · NO CARD"，读端点免 Key、限速 30 请求/100 行每天/IP）及 https://www.bargo.ai/free-apis/terms
- 免 Key 费率适用性：本次 2 次请求均无 Key、均成功，响应限额头与官方规则一致；无任何账户或支付行为。
