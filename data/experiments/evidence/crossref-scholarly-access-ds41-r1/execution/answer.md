Docs read. Now I'll write the persistent config and run one real query through the specified endpoint.
Query succeeded with identifiable DOI records. Now a second, title-targeted query to surface the canonical paper (respecting the 5s minimum interval).
Canonical record found. Third and final request: verify the DOI directly via the specified single-record endpoint.
已接通并完成真实查询。

## 结果（可识别文献记录）
- 题名: **The FAIR Guiding Principles for scientific data management and stewardship**
- 标识: **DOI 10.1038/sdata.2016.18**；链接 https://doi.org/10.1038/sdata.2016.18
- 来源: Crossref REST API（`https://api.crossref.org/works` 与 `/works/10.1038/sdata.2016.18`）
- 其他元数据: Sci Data, 2016-03-15, Springer Nature, ISSN 2052-4463, 第一作者 Wilkinson，被引 15533（响应中 `is-referenced-by-count`）
- 另一次 list 查询也返回多条带 DOI 的记录（如 10.3233/ds-210047、10.1038/s41431-018-0160-0），来源同上。

## 接入步骤
1. 读官方文档 `https://www.crossref.org/documentation/retrieve-metadata/rest-api/`：确认无需注册/Key，公共 REST 池限速 1 req/s、并发 1。
2. 按本轮授权从第一请求即用 UA `agent-friendly-services/20261008 (+https://github.com/Olorinm/agent-friendly-services)`，**未加 mailto**、未用 polite/MetadataPlus。
3. 用 `curl -G` 调 `/works`，参数 `query.bibliographic`、`query.author`、`filter=type:journal-article,...`、`rows=3`、`select=DOI,title,author,container-title,issued,URL,type` 控制返回量。
4. 共 3 次请求，起始间隔 ≥5s，全部 HTTP 200；第 3 次用 `/works/{doi}` 复核单条记录。
5. 结果/响应缓存于题目目录 `cache/`（query1.json、query2.json、doi_verify.json、headers*.txt）。

## 本地配置（后续查询用）
`/home/node/service-tools/service-config.json` — 含 base URL、两个入口、匿名认证说明、UA、限速（官方 1/s，本轮 5s、每阶段 ≤3 请求、并发 1、退避/终止规则）、默认 rows/select、缓存目录与策略、元数据权利提示。无可放入私有文件的秘密（匿名、无 Key）。

## 已有账号来源 / 自助与人工介入
- 本轮未提供账号、Key、邮箱或支付方式，也**不需要**：Crossref 公共路径匿名可用，因此未注册、未付费、未发邮件。
- 自助即可完成全部调用；无人工审批或额外申请需要。
- 若未来需要更高配额/更快响应，只能由用户自行申请 Crossref **Metadata Plus**（付费）或按官方要求加入 polite 池（提供 mailto）——本轮明确禁止，故未启用。

## 实际阻碍
- 无阻断性阻碍：无验证码、无 429、无 DNS/连接错误。
- 响应头确认公共池限制：`x-rate-limit-limit: 1`、`x-rate-limit-interval: 1s`、`x-concurrency-limit: 1`、`x-api-pool: public-array`；本轮 5s 间隔更保守，因此单次查询耗时受等待约束。
- 检索质量：`query.bibliographic` 优先返回他人推荐/复现记录，需叠加 `query.author=Wilkinson` 与年份过滤才能稳定命中原论文（已据此定位）。
- 权利边界：多数书目元数据可复用，但摘要/全文可能受第三方权利限制，本轮只读元数据、未下载全文。