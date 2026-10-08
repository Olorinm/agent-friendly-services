Now the real query. I'll create a small cached helper (tool) and run one search.
Search returned real records. Let me verify one record with a free single lookup (waiting ≥5s).
已接通 OpenAlex 并完成真实查询。

## 接入步骤
1. 读官方认证文档：匿名无 Key 可做基本查询，无需注册。
2. 检查环境：`curl`/`python3`/`node` 可用；持久目录 `/home/node/service-tools`、`/home/node/installed-tools` 已建。
3. 写入通用配置 `/home/node/service-tools/service-config.json`（base URL、入口、匿名身份、UA、限速/退避、缓存路径）。
4. 写可复用查询助手 `/home/node/installed-tools/openalex_query.sh`（固定 UA、按 URL 的 sha256 缓存、命中即复用）。
5. 发真实请求（每请求间隔 ≥5s，固定 UA `agent-friendly-services/20261008`），共 2 次：1 次搜索（$0.001）+ 1 次单条 lookup（免费）。

## 实际查到的记录
搜索 `attention is all you need`（`https://api.openalex.org/works?search=...`）返回，例如：
- **Attention Is All You Need** — OpenAlex `W2626778328`，DOI `https://doi.org/10.65215/2q58a426`，2025，被引 26807（lookup 确认存在，类型 posted-content/acceptedVersion）。注意：该条目是仓储/预印本条目，并非经典 NeurIPS 版本，OpenAlex 索引中同题多版本需按 DOI 区分。
- **Attention Is All You Need In Speech Separation** — DOI `https://doi.org/10.1109/icassp39728.2021.9413901`（IEEE ICASSP）。
- **Channel Attention Is All You Need for Video Frame Interpolation** — DOI `https://doi.org/10.1609/aaai.v34i07.6693`（AAAI）。

响应头实测匿名额度：`limit-usd=0.1`、`remaining-usd=0.099`、`remaining=990`、`reset=29061s`（UTC 午夜）。

## 本地保存
- 可复用配置：`/home/node/service-tools/service-config.json`（无秘密，匿名，无 Key）
- 查询助手：`/home/node/installed-tools/openalex_query.sh`
- 本题响应（仅本题目录）：`results/query1_attention.json`、`results/lookup_W2626778328.json`、缓存 `cache/`

## 人工介入/阻碍
- 无需注册或付费，本轮无账号、Key、邮箱可用，故不注册；匿名额度为共享，剩余范围未知，撞限额即停。
- 未发现阻碍，接入即可用；未启用 rerank/内容下载，未购买全文。