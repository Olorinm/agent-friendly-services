接入完成，真实查询成功。

**地点与结果**（MET Norway Locationforecast 2.0 compact，Oslo 59.9139N, 10.7522E，`Content-Type: application/json`，HTTP 200）
- 预报时间 2026-10-08T14:00:00Z，气温 7.0 °C；相对湿度 81.8 %；风速 6.5 m/s，风向 9.0°；海平面气压 1003.3 hPa；降水时段符号 rain
- 后续 15:00Z：7.2 °C；16:00Z：7.3 °C
- 预报更新时间 `updated_at` 2026-10-08T14:29:23Z；响应 `Expires` 2026-10-08T15:18:22Z

**接入步骤（我自行完成）**
1. 阅读官方 Getting Started / TermsOfService / Locationforecast 文档。
2. 无需注册或 Key，直接用指定入口 GET：`https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.9139&lon=10.7522`。
3. 按 ToS 要求带真实可联系 User-Agent，坐标截断至 4 位小数，接受 gzip。
4. 捕获响应头与 JSON，解析当前时次数值与单位。
5. 将通用连接/客户端标识配置写入持久目录 `/home/node/service-tools/service-config.json`（含入口、方法、User-Agent、缓存规则、署名要求）。本轮仅 1 次天气 API 读取，未 HEAD+GET。

**实际阻碍**：无。入口开放、无账号/付费/验证码。仅需注意两项合规约束：User-Agent 必须真实可联系，坐标限 4 位小数；后续查询应复用 `Expires` 前缓存并用 `Last-Modified` 做 `If-Modified-Since` 条件请求。

**后续查询**：直接读取上述配置即可复用，无需注册；数据使用需按 CC BY 4.0 署名挪威气象研究所。