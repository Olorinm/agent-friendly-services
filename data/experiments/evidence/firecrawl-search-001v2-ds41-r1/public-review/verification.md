公开证据节选；独立核验原文件 SHA256：273cda821979b1c306a7aac3036397e39974511ccd94551c3a47386880555252。原始材料私有保存，以下编辑不改验收结论。

# firecrawl 匿名搜索来源链核验摘要（脱敏）

被测执行仅通过指定入口 `https://api.firecrawl.dev/v2/search` 发现来源，未使用其他搜索引擎或模型记忆替代。以下为本次真实调用的业务事实摘录，无凭据、无账号信息。

## 匿名调用与免费入口
- 4 次搜索均为匿名 POST：请求只带 `Content-Type: application/json`，无 `Authorization` / API key / 支付方式。
- 4 次响应均 `HTTP 200`、`"success": true`、`"creditsUsed": 2`，`data.web` 分别返回 8/8/8/10 条。
- 冻结输入 `ENVIRONMENT.md` 声明：本轮只使用官方免费匿名入口，未提供账号/Key/支付；本执行仅匿名调用，无账号绑定与付费超额。

## 搜索谓词与关键返回（source 相对 execution/artifacts/）
- search1.json（includeDomains: python.org, docs.python.org）→ result1.json：返回 `https://docs.python.org/3.13/howto/free-threading-python.html`（position 2）。
- search2.json（includeDomains: docs.python.org）→ result2.json：返回 free-threading-extensions、`/3/whatsnew/3.13.html` 等。
- search3.json（includeDomains: docs.python.org）→ result3.json：返回 free-threading-extensions（position 1）、`/3/whatsnew/3.13.html` 等。
- search4.json（includeDomains: docs.python.org）→ result4.json：返回 whatsnew 3.13、zh-cn/3.13/free-threading-extensions 等。

## 答案所引官方链接的追溯
- `docs.python.org/3.13/howto/free-threading-python.html`：直接出现在 result1。
- `docs.python.org/3.13/whatsnew/3.13.html`：搜索返回 `/3/whatsnew/3.13.html`（canonical 等价），执行又直接读取 3.13 版页面。
- `docs.python.org/3.13/howto/free-threading-extensions.html`：搜索返回 `/3/` 与 zh-cn/3.13 版（canonical 等价），执行直接读取 3.13 版页面。
- `peps.python.org/pep-0703/`：由所读 3.13 whatsnew 页面内链指向。

（`review-packet/`、`peer-results/`、`tool-records.json` 及原始会话/模型用量文件均为私有材料，未列为公开证据。）


本轮按相同web-search-001/v2任务比较，旧v1不合并统计。接入和业务均为匿名公开入口，额度余量未知，同一服务器出口IP；持久化配置经检查未含业务答案。执行原始返回与三份事前独立官方参考均私有保留；来源链由独立验收核对，没有额外最低页面数要求。单次试跑只说明这次任务，不是普遍可靠性排名。

本次初始独立验收在25次模型请求上限退出，未形成assessment。改用新独立会话、50次请求上限和原300秒时间重新验收；执行及其冻结输入、原始输出、比较快照均未改动或重跑，第二验收未读取第一验收草稿。第一验收的用量不完整，其费用未知；第二次估计费用和两次原始哈希均留底，总验收费不将未知当零。
