已通过 [Ignav Playground](https://ignav.com/playground) 实际查询，找到以下符合条件的方案，均为 **1 名成人、单程、经济舱、直飞**：

| 航班 | 航段 | 当地起飞时间 | 当地抵达时间 | 搜索报价 |
|---|---|---|---|---|
| easyJet U2 3851 | 米兰马尔彭萨 MXP → 阿姆斯特丹 AMS | 2026-09-25 06:10 | 2026-09-25 08:05 | **58 EUR** |
| easyJet U2 3859 | MXP → AMS | 2026-09-25 17:50 | 2026-09-25 19:45 | **64 EUR** |
| easyJet U2 7814 | MXP → AMS | 2026-09-25 09:40 | 2026-09-25 11:40 | **70 EUR** |

两地当日均为 UTC+2。查询时间为 **2026-09-07 16:38 北京时间**，服务返回 HTTP 200。

核对证据：

- [查询请求：方法、URL、非敏感参数]([WORKSPACE]/evidence/fares-MXP-AMS-request.json)
- [真实服务响应（已脱敏）]([WORKSPACE]/evidence/fares-MXP-AMS-response.json)：上述方案对应 `itineraries[0]` 至 `[2]`
- [调用链、时间与核对说明]([WORKSPACE]/evidence/README.md)