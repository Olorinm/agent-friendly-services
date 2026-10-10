Docs confirmed: anonymous, no auth, `/v1/query` (POST) + `/v1/vulns/{id}` (GET). Now writing a small client with cache + rate spacing.
Query returned records. Now exercising the record path via `GET /v1/vulns/{id}`:
Both endpoints verified. Now saving the reusable connection config.
Verifying cache behavior (repeat request served locally, no new network call):
已接通 OSV 公共 REST API 并完成真实查询。

## 查询结果（可识别公告）
查询：`POST /v1/query`，包 `minimist` (npm) 版本 `1.2.0`
- **GHSA-vh95-rmgr-6w4m** — Prototype Pollution in minimist，别名 CVE-2020-7598，severity MODERATE
- **GHSA-xvch-5gv4-984h** — Prototype Pollution，别名 CVE-2021-44906，severity CRITICAL

包名均为 `minimist` / ecosystem `npm` / purl `pkg:npm/minimist`；来源字段指向 GitHub Advisory Database（`github.com/github/advisory-database/.../GHSA-vh95-rmgr-6w4m.json`），references 含 NVD CVE 页面。

记录路径复核：`GET /v1/vulns/GHSA-vh95-rmgr-6w4m` 200，返回 id、aliases、published/modified 均正常。

## 接入步骤
1. 读官方 quickstart/api 文档，确认匿名入口与两个路径。
2. 无需注册/密钥：直接调用 `https://api.osv.dev/v1/query`（POST JSON）和 `/v1/vulns/{id}`（GET）。
3. 写轻量客户端 `osv_client.py`（仅 Python 标准库 urllib），带 User-Agent 标识、单线程、≥2s 间隔、磁盘缓存。
4. 实测查询 + 记录拉取，缓存重复请求（复跑返回 `source: cache`，不再联网）。

## 本地配置与产物
- 通用连接配置：`/home/node/service-tools/service-config.json`（基址、端点、客户端标识、限流/缓存纪律；无秘密）
- 查询脚本：`osv_client.py`；原始响应：`query_minimist_1.2.0.json`、`record_GHSA-vh95-rmgr-6w4m.json`；缓存：`cache/`
- 未安装外部依赖（仅标准库），故 `installed-tools` 为空。

## 已有账号来源 / 人工要求 / 阻碍
- **账号来源：无**。OSV 官方为匿名公共入口，本轮未提供也未需要任何账号、邮箱、付款或企业资质；无注册步骤，未创建账号。
- **人工或特殊申请：无**。
- **实际阻碍：无**。两次实时请求均 200，未出现 403/429/连接失败；官方文档说明当前无限流，客户端额外按本轮规则做了节流与缓存。