已按要求实际接入并测试，但**服务不可达，未能取得标题与概述**。

**`GET https://r.jina.ai/https://example.com/`（官方免 Key 方式）** 在本容器内多次尝试均超时；DNS 将 `r.jina.ai` 污染为 Meta 的 IP（`31.13.94.37` 等），直连被 reset。对照 `example.com`/`github.com`/`pypi.org` 均返回 200，说明是本机出网白名单/DNS 屏蔽，而非调用方式或权限问题。未注册、未付款、未绕过入口。

- 配置已存：`/home/node/service-tools/service-config.json`（免 Key，无秘密，记录入口/调用方式/可达性）
- 详细结果与实测记录：`[WORKSPACE]/result.md`
- 接入步骤：直接请求 `https://r.jina.ai/<完整URL>`，`Accept: text/plain` 取 Markdown，受官方匿名限流。
- 门槛/阻碍：需上游在防火墙/DNS 放行 `r.jina.ai`（及 `jina.ai`），或提供可用代理；当前无代理、无 Key。