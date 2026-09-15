数据来源：[CapitolExposed](https://www.capitolexposed.com/)。本页仅展示核验摘要。

文档已获取。免费层无需 Key，按 IP 限流。根路径 404 属正常（需具体资源路径）。现在实际调用验证。
`/stats` 调用成功（HTTP 200）。再验证几个核心查询端点。
核心端点都可用。检查限流响应头并验证 trades 查询。
/tmp/opencode 归 root 不可写；改用本题工作目录存放临时文件。
全部验证通过。保存持久化配置。
**接入完成，服务可用。**

- **指定方式**：REST 直连 `https://www.capitolexposed.com/api/v1`，免 Key 公开入口（按 IP 限流），无需注册（本轮授权也不允许注册）。
- **实测验证（全部 HTTP 200）**：
  - `/stats` — 返回 532 名议员、36,992 笔交易等站点统计
  - `/members?chamber=senate&party=D` — 过滤查询正常（共 89 条）
  - `/search?q=Pelosi NVIDIA` — 命中众议院 Clerk 原始 PTR 文件并给出出处链接
  - `/members/nancy-pelosi/trades` — 返回真实 STOCK Act 申报明细（含金额区间、owner、原始 PDF 出处）
- **限流**：实测响应头 `x-ratelimit-limit: 60`（列表类 60 次/分）；搜索 30/分、批量导出 5/小时；429 时遵循 `Retry-After`。
- **配置已保存**：`/home/node/service-tools/service-config.json`（含 base URL、全部已验证端点、参数、限流与署名要求），后续任务可直接复用。探测响应存于本题目录 `api-probe-trades.json`。
- **未做/受阻项**：无。API Key 属付费升级项且本轮未提供，免 Key 入口已够用；未注册、未写远端。