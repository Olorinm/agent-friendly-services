已接通并完成一次真实查询。

**结果**（`GET /advisories?per_page=3&sort=published&direction=desc`，HTTP 200，服务端确认 `x-github-api-version-selected: 2026-03-10`）：

| GHSA 标识 | CVE | 严重度 | 关联包 (生态) |
|---|---|---|---|
| GHSA-m687-p538-r5hp | — | high | code.vikunja.io/api (go) |
| GHSA-fmmf-xq98-g327 | — | medium | code.vikunja.io/api (go) |
| GHSA-pjr3-86v4-5p7w | — | medium | code.vikunja.io/api (go) |

来源 `https://github.com/go-vikunja/vikunja`；详情查询另确认 GHSA-m687-p538-r5hp 受影响范围 `>= 2.2.0, <= 2.6.0`、CWE-942。

**配置与产物**
- 通用连接配置：`/home/node/service-tools/service-config.json`（匿名模式、请求头、限流/缓存策略、CC BY 4.0 署名）
- 查询脚本：`./query_advisories.py`（读配置，单线程、间隔≥2s、缓存去重）
- 原始响应/响应头缓存：`./cache/`；完整答复与步骤：`./answer.md`

**接入步骤**：无需注册，直接带三个官方头（`Accept: application/vnd.github+json`、`X-GitHub-Api-Version: 2026-03-10`、真实 User-Agent）GET 公共入口即可。

**阻碍/边界**：无注册或人工审核，无 403/429/连接失败。匿名配额 60/小时（响应头为准），执行中 used 6→9、remaining 51；无秘密需保存，本轮无账号来源。