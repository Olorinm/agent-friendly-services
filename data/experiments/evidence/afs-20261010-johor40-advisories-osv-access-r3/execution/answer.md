接入完成，两条官方路径均已实测可用。

**结果**：OSV 公共 REST API 匿名接通用。选定的真实查询 `{"package":{"name":"lodash","ecosystem":"npm"},"version":"4.17.20"}` 经 `POST /v1/query` 返回 5 条可识别公告，如 `GHSA-29mw-wpgm-hmr9`（别名 CVE-2020-28500，影响 `npm:lodash` `>=4.0.0,fixed 4.17.21`）。记录路径 `GET /v1/vulns/{id}` 亦正常。跟随引用核对到 lodash 官方仓库修复提交（HTTP 200）。

**接入步骤**：无认证直连；携客户端标识 `agent-friendly-services/20261010`；编写最小客户端 `osv_query.py`（单线程、间隔≥2s、同请求走缓存）；保存通用配置 `/home/node/service-tools/service-config.json`。

**阻碍/自助要求**：无。匿名入口，无注册、无凭据、无付费、未触发 403/429。

交付物：`answer.md`、`osv_query.py`、`query-lodash.json`、`raw-query-lodash.json`、`raw-vuln-GHSA-29mw-wpgm-hmr9.json`、`cache/`；持久配置 `/home/node/service-tools/service-config.json`（无秘密）。