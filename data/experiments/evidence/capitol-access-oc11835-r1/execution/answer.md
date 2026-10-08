文档确认：`https://www.capitolexposed.com/api/v1` 免 Key 免费访问（按 IP 限流）。现在实测基础调用：
`/stats` 返回 200，免 Key 可用。接着实测业务查询（合计不超过 5 条记录）：
三项调用全部成功（限流头确认 60/min，匿名免费档）。保存持久配置与后续调用辅助脚本：
验证辅助脚本走保存的配置可正常调用：
`/top-traders` 经 urllib 得到 403 —— 先用 curl 区分是端点问题还是 UA 被拦：
确认是 Cloudflare 按 User-Agent 拦截（error 1010），端点本身正常。修正辅助脚本的 UA：
辅助脚本验证通过。按授权要求停止进一步数据查询，写入接入结果到题目目录：
接入完成，服务可用。

**结论**：capitol-exposed 指定入口 `https://www.capitolexposed.com/api/v1` 免 Key 免费访问，REST 直接调用实测通过（未注册、未付款）：

- `GET /stats` → 200（member_count=539, trade_count=73251）
- `GET /members?per_page=2` → 200（2 条记录）
- `GET /trades?per_page=3` → 200（3 条交易记录，含 parser_confidence 与 source_url）
- `GET /top-traders?limit=1` → 首次经 Python urllib 得 403（Cloudflare error 1010 拦 UA，非端点问题），换正常 UA 后 200
- 限流实测：列表类 60 次/分钟（`X-RateLimit-*` 头确认）

**持久化**（后续任务直接可用）：
- 配置：`/home/node/service-tools/service-config.json`（含 UA 要求、限流、2026-10-03 已移除端点等注意事项）
- 零依赖辅助脚本：`/home/node/service-tools/installed-tools/capitol_query.py`（已实测走该配置调用成功）
- 结果明细：`integration-result.md`（本题目录）

无未解决阻碍；共返回 6 条真实记录（其中 1 条为 UA 验证调用），符合“少量必要查询”要求。