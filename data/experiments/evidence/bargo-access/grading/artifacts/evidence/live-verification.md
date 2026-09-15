数据来源：[Bargo Congress Trades API](https://www.bargo.ai/free-apis/congress)。本页仅展示核验摘要。

# 独立核验摘要（financial-access-001/v1，2026-09-15）

## 核验内容
- 指定入口 `https://www.bargo.ai/free-apis/congress/v1` 本次独立复测（验收环境，keyless GET）：
  - `/health` → HTTP 200，`status: ok`，trades 总量与最新披露日期与执行记录一致。
  - `/trades?limit=1` → HTTP 200，返回 1 行真实披露数据；响应头 `X-RateLimit-Remaining: 21`、`X-RateLimit-Rows-Remaining: 88`。
- 配额连续性：执行者最后一次自验记录剩余 22 请求/89 行（execution/answer.md 及工具记录）；本次同日同窗口独立调用恰消耗 1 请求/1 行后为 21/88，逐项吻合。说明采集记录与在线服务状态对应，属对真实服务的真实调用，非仅文档或离线材料。
- 配置留存：执行工具记录显示成功写入 `/home/node/service-tools/service-config.json`（含 base_url、端点、响应字段、keyless 限额、调用注意事项）；`execution/retained-files.json` 列明该文件随持久目录保留。该文件属执行环境持久目录，验收环境不直接挂载，依据为写入回执与留存清单。

## 结论依据
- 全部业务调用均为指定 bargo-congress REST 端点的直接 HTTP GET，未使用替代服务或模型记忆。
- 接入门槛：官方文档确认读端点免 Key（keyless 30 请求/100 行每天/IP）；本轮未提供账号/Key，也无注册、付款或人工步骤。
- 免费依据：官方页标注 FREE · NO CARD，读端点 keyless 限流可用；本轮所有调用均为 keyless 读端点且返回 200，未见付费或超额。

## 来源
- 官方文档：https://www.bargo.ai/free-apis/congress
- 服务条款：https://www.bargo.ai/free-apis/terms
- 免 Key 规则（独立参考）：keyless 30 请求/100 行每天/IP

## 完整性与署名
- 执行答复 execution/answer.md sha256: aa3f020639c9f2c1794b7866357628ecf1c012a6102ae967c9c4d3960857fe26
- 工具记录源 events.jsonl sha256: b110b12bd2a5be5d44e2f1452152a9eaccc53bba226b85e48fd32cfee506c7d2
- 数据归属：Bargo 免费 U.S. Congress Stock Trades API（STOCK Act 披露）；本摘要不复制原始数据行，仅描述核验过程与状态。
