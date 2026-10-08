公开证据节选；独立核验原文件 SHA256：c3110144e7ca99aeb4da3f2c1557fea520184a980878f8c2c2a126c346a4116a。原始材料私有保存，以下编辑不改验收结论。

# Photon 接入验收 — 最小业务证据摘要（脱敏）

本文件为独立验收摘要，供引用被私有化的工具记录；不含密钥、Cookie、账号或原始会话内容。

## 真实请求与响应（唯一一次 Photon API 调用）
- 入口：`https://photon.komoot.io/api/`（指定入口）
- 方法/参数：`GET /api/?q=Eiffel%20Tower&limit=3&lang=en`
- User-Agent（执行者从首请求即使用）：`agent-friendly-services/20261008 (+https://github.com/Olorinm/agent-friendly-services)`
- 无账号、无 Key、无支付信息、无代理/UA 轮换
- 结果：HTTP 200，约 9.9s；`Content-Type: application/json`；`Cache-Control: max-age=3600`
- 首个匹配：Eiffel Tower, Paris, Île-de-France, France（postcode 75007, FR; osm_type=W, osm_id=5013364）
- 坐标（GeoJSON `coordinates` 顺序为 [经度, 纬度]）：longitude 2.2945006, latitude 48.8582599
- 来源：OpenStreetMap；许可 https://www.openstreetmap.org/copyright

原始业务文件见 `execution/artifacts/photon_query_eiffel.json` 与 `execution/artifacts/headers_basic.txt`。

## 持久配置观察
- 路径：`/home/node/service-tools/service-config.json`（ENVIRONMENT.md 指定的持久目录；`execution/retained-files.json` 记为保留文件）
- 内容仅通用连接/身份/缓存规则：service/provider/官方文档 URL、endpoints、auth=none、identity.userAgent、请求规则（单线程、15s 间隔、4 次/阶段）、缓存策略、GeoJSON 坐标顺序、OSM 署名、policyNote、noSecrets=true
- 未包含任何账号、Key、Cookie 或私人信息；执行环境写入后经 `python3 -m json.tool` 校验为合法 JSON

## 免费规则来源
官方 Photon 站点及 komoot/photon README 允许合理请求量的项目使用，过量可能限流，未承诺可用性；本次使用免账号、无Key的公开demo路径。来源：https://photon.komoot.io/ 、https://github.com/komoot/photon 。

公开地点数据来源：[Photon / komoot](https://photon.komoot.io/) 与 [OpenStreetMap contributors](https://www.openstreetmap.org/copyright)，按 [ODbL](https://opendatacommons.org/licenses/odbl/) 许可标注来源。变动：选取任务相关字段，中文说明和坐标距离计算；不代表服务方背书。Nominatim无成功响应，因此其记录没有可发布的服务地点数据。

总控实际检查后，仅允许通用连接配置从接入带入下一题，没有继承接入地点、坐标或业务脚本。每阶段最多4次请求和15秒间隔是本次测试约束，不是Photon承诺的数值配额。
