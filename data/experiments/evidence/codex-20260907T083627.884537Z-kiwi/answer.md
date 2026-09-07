已实际通过 [Kiwi.com 指定服务](https://mcp.kiwi.com) 查询成功，无需账号或密钥。以下均为 **1名成人、单程、经济舱、直飞**，时间为机场当地时间。

| 各航段机场 | 航司／航班号 | 当地起飞时间 | 当地抵达时间 | 搜索报价 |
|---|---|---|---|---|
| 米兰贝加莫 BGY → 埃因霍温 EIN | Ryanair **FR3460** | 2026-09-25 06:40 | 2026-09-25 08:20 | **62 EUR** |
| 米兰利纳特 LIN → 阿姆斯特丹史基浦 AMS | easyJet **U25405** | 2026-09-25 06:55 | 2026-09-25 08:50 | **68 EUR** |
| 米兰马尔彭萨 MXP → 阿姆斯特丹史基浦 AMS | easyJet **U23851** | 2026-09-25 06:10 | 2026-09-25 08:05 | **75 EUR** |

查询时间：2026-09-07 08:37 UTC。报价为查询时返回的单人总价。

请求通过 `POST https://mcp.kiwi.com`，调用 JSON-RPC `tools/call` → `search-flight`。核对证据：

- BGY→EIN：[请求参数]([WORKSPACE]/evidence/bgy-ein-request.json) · [真实响应]([WORKSPACE]/evidence/bgy-ein-response.txt)
- LIN→AMS：[请求参数]([WORKSPACE]/evidence/lin-ams-request.json) · [真实响应]([WORKSPACE]/evidence/lin-ams-response.txt)
- MXP→AMS：[请求参数]([WORKSPACE]/evidence/mxp-ams-request.json) · [真实响应]([WORKSPACE]/evidence/mxp-ams-response.txt)
- [证据说明与核对位置]([WORKSPACE]/evidence/README.md)