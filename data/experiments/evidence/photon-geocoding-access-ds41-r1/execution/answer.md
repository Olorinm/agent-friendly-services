Query succeeded. Now saving the persistent config and local result artifacts.
已接通 Photon，并完成 1 次真实查询。

**结果**
- 查询：`GET https://photon.komoot.io/api/?q=Eiffel%20Tower&limit=3&lang=en`（HTTP 200，约 9.9s）
- 匹配：Eiffel Tower, Paris, Île-de-France, France (75007, FR)
- **经度 2.2945006 / 纬度 48.8582599**
- 来源：OpenStreetMap（osm_type=W, osm_id=5013364）；许可 https://www.openstreetmap.org/copyright
- 返回为 GeoJSON，坐标为 `[经度, 纬度]`。

**接入步骤**
1. 读官方文档 `photon.komoot.io` 与 api-v1.md，确认 `/api` 参数与 GeoJSON 格式。
2. 免注册直接用真实 UA `agent-friendly-services/20261008 (+https://github.com/Olorinm/agent-friendly-services)` 调用。
3. 发起 1 次查询 → 解析 coordinates。
4. 通用连接/身份/缓存规则写入持久配置。

**本地配置（后续查询用）**
- 持久：`/home/node/service-tools/service-config.json`（仅连接/身份/缓存规则，含 15s 间隔、单线程、4 次/阶段、缓存策略、OSM 署名）
- 本题目录：`photon_query_eiffel.json`（原始响应）、`headers_basic.txt`、`photon_result.md`

**实际阻碍**
- 无：免注册、无 Key、无依赖需安装（用自带 curl/Python）；未遇验证码/资质/拒绝。
- 唯一限制是公共 demo 的公平使用（不承诺可用性、超量会限流/封禁），本轮已按限速执行，无人工或额外申请环节。