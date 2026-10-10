Docs confirmed. Now running the first real query (single request, capturing headers + body).
Query succeeded (HTTP 200). Let me inspect the records.
Records are identifiable. Now saving the persistent config and a reusable query script.
Now verifying the reusable script end-to-end with a second real call (get by GHSA id).
已接通并完成真实查询，取得可识别公告记录。

**接入步骤**：匿名调用 `GET https://api.github.com/advisories`，带上规定请求头（`Accept: application/vnd.github+json`、`X-GitHub-Api-Version: 2026-03-10`、指定 User-Agent），单线程且间隔 ≥2s，按 `X-RateLimit-*` 退避。无需注册/令牌。

**真实查询结果**（npm, per_page=3）：
1. `GHSA-pwhx-cvv3-qj5c` / CVE-2026-108259（high）— 包 `@tinacms/cli` <=2.7.0；来源 https://github.com/advisories/GHSA-pwhx-cvv3-qj5c
2. `GHSA-x34j-47hf-4xg7` / CVE-2026-108261（critical）— 包 `tinacms`, `@tinacms/app`；来源 https://github.com/advisories/GHSA-x34j-47hf-4xg7
3. `GHSA-c42q-qvc3-j6vg` / CVE-2026-108260（high）— 包 `@tinacms/web-components`；来源 https://github.com/advisories/GHSA-c42q-qvc3-j6vg

单条详情 `GET /advisories/GHSA-pwhx-cvv3-qj5c` 亦返回 200，验证通过。

**本地配置**：`/home/node/service-tools/service-config.json`（匿名、无秘密）。查询脚本 `queries/query_advisories.py`，原始响应 `cache/list_npm.json`、`results/`，摘要 `answer.md`。

**账号/人工要求**：使用匿名公共入口，无账号、无令牌、无邮箱、无付款方式，未注册任何账号，无人工或特殊申请。

**阻碍**：无阻塞。匿名核心配额 60 次/小时（实测首查后 remaining=57），超限返回 403/429 需退避；数据为 CC BY 4.0，需保留署名与来源链接。