已接通 OSV 官方公共 REST API 并完成真实只读查询。

**真实结果（可识别公告）**
- 查询：`POST /v1/query` → `{"version":"2.4.1","package":{"name":"jinja2","ecosystem":"PyPI"}}`
- 命中：`GHSA-462w-v97r-4m45`（别名 `CVE-2019-10906`, `PYSEC-2019-217`）
- 关联包：`PyPI / jinja2`（受影响 0 → 修复 2.10.1）
- 来源：NVD `CVE-2019-10906`；GitHub Advisory `GHSA-462w-v97r-4m45`
- 已用 `GET /v1/vulns/GHSA-462w-v97r-4m45` 二次核对一致；重复请求命中本地缓存。

**接入步骤**：读官方 quickstart → 写持久配置 → 用脚本调用指定端点（真实 UA、≥2s 间隔、缓存）→ 实测并把响应存本地。

**保存位置**
- 持久配置：`/home/node/service-tools/service-config.json`（匿名入口，无凭据）
- 查询脚本/缓存/响应/答案：当前工作目录 `osv_query.py`、`cache/`、`vuln_record_GHSA-462w-v97r-4m45.out`、`RESULT.md`

**实际阻碍**：无账号/注册/资质要求（匿名公共入口直接可用）；未遇验证码或 403/429；仅自设礼貌限流 ≥2s，未触服务端限制。本服务只用 Python 标准库，故 `installed-tools` 无需依赖。