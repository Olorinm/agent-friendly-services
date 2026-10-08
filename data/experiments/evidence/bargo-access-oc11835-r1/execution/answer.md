文档已确认：这是 Bargo 的美国国会股票交易 API，免 Key 只读入口，限额 30 请求/100 行每天。现在开始接入验证，先做健康检查。
健康检查通过。现在做一次最小真实数据查询（≤5 条记录）。
查询成功，返回 5 条真实记录，限额头正常（30 请求/100 行每天，已用 2 请求）。现在保存持久化连接配置和验证结果。
接入完成，服务可用。

**结果**：bargo-congress 通过指定入口 `https://www.bargo.ai/free-apis/congress/v1`（免 Key REST）接入成功——

- `GET /health` → 200，`status: ok`，共 50,416 条披露交易，最新披露 2026-10-02
- `GET /trades?limit=5` → 200，返回 5 条真实 STOCK Act 记录（member/ticker/交易与披露日期/估价/perf_pct/filing_portal 完整），限额头确认免 Key 配额 30 请求/100 行每天（仅消耗 2 请求）
- 配置已存 `/home/node/service-tools/service-config.json`（端点、限额、署名条款、验证状态），验证详情在本目录 `result.md`

**无阻碍**：读端点免 Key 即可用，未注册、未付款；配额与后续任务共享，后续查询建议保持最小化（免费数据仅覆盖最近 3 个月）。