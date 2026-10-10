Query succeeded (HTTP 200, rate limit 60/hr, remaining 59). Now building a reusable, cache-aware query script and saving config.
已接通并完成真实查询。

**结果（来源：GitHub Advisory Database，CC BY 4.0）**
- 公告：`GHSA-pwhx-cvv3-qj5c` / `CVE-2026-108259`，high / reviewed
- 关联包：`npm / @tinacms/cli`，范围 `<= 2.7.0`，修复 `3.0.0`
- 来源代码：https://github.com/tinacms/tinacms ；公告：https://github.com/advisories/GHSA-pwhx-cvv3-qj5c
- 同批另得：`GHSA-x34j-47hf-4xg7`（critical，`npm / tinacms`、`@tinacms/app`）

**接入步骤**：GET `https://api.github.com/advisories`，头 `Accept: application/vnd.github+json`、`X-GitHub-Api-Version: 2026-03-10`、指定 User-Agent；匿名无 Authorization，读取 `X-RateLimit-*` 限流、单线程 ≥2s、相同请求走缓存。

**配置与文件**
- 通用连接配置（持久）：`/home/node/service-tools/service-config.json`
- 可复用脚本：`query_advisories.py`（缓存感知+节流）；原始响应/头缓存：`cache/`；说明：`result.md`

**实际阻碍**：无。匿名公共只读入口，无需注册/授权/邮箱/付款，也就无自助注册或人工申请步骤。唯一约束为匿名共享出口 60 次/小时；两次查询后 remaining=58，版本头被接受（`x-github-api-version-selected: 2026-03-10`），未触发 403/429。