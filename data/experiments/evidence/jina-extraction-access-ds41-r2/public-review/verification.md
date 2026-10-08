Publication excerpt. Original independent evidence SHA256: 9b1d83496fbc0155e418f7d1ab259eb104adcea503edf5ee7268767e92339ebd. Original material is retained privately; controller additions are labelled.

# 网络可达性核验（验收方复核摘要）

核验对象：本次执行指定的 Jina Reader 入口 `https://r.jina.ai/` 是否可达。
来源：执行记录 `execution/artifacts/result.md` 与 `execution/answer.md` 中的实测；验收环境复核，现象一致。无账号、密钥或资源标识。

## 执行记录中的实测（UTC 2026-10-08 13:09–13:12）

- `GET https://r.jina.ai/https://example.com/`（45s/60s/30s 多次）：连接超时 curl(28)，HTTP 000，无响应正文。
- 强制 IPv6 / HTTP:80 / 指定 IP + SNI 直连：立即失败或 `Connection reset by peer`。
- DoH（1.1.1.1 / cloudflare-dns.com / dns.google）：超时/重置。
- DNS `r.jina.ai` 解析到非 Jina/Cloudflare 地址（IPv4 `31.13.94.37` 等、IPv6 `2a03:2880:f107:83:face:b00c:0:25de`）。
- 对照域名 `example.com`、`github.com`、`registry.npmjs.org`、`pypi.org`、`www.cloudflare.com`：HTTP 200。

## 验收环境复核（同轮封锁）

- `https://example.com/` → HTTP 200；`https://github.com/` 等对照域可达。
- `https://r.jina.ai/`、`https://jina.ai/` → 连接超时 / HTTP 000。
- 再次解析 `r.jina.ai`：返回反复变化的无关地址（如 `103.246.246.144`、`103.228.130.61`、`103.214.168.106`、`198.44.185.131`、`31.13.94.37`），非 Jina 真实地址，属 DNS 黑洞/污染特征。
- 同期题面涉及的另外两个服务域名 `api.firecrawl.dev`（HTTP 200）、`mcp.exa.ai`（HTTP 405，可达）解析到真实地址。

## 结论

指定服务入口 `r.jina.ai` / `jina.ai` 在测试网络内被域名级 DNS 污染与出网阻断，而对照域名与其他提取服务域名可达。该阻断与执行者的调用方式无关，属执行/测试环境网络限制，导致无法通过指定入口取得正文。

总控限定：可直接核对的事实是本轮DNS解析结果变化、请求超时/重置及对照域可达。未取得网络策略日志或权威DNS对照，因此不能据此精确确定拦截机制；验收中“DNS污染/出网阻断”为原因解释。保留环境无效结论，不据此判断其他地区的服务能力。未继续派发Jina业务题。
