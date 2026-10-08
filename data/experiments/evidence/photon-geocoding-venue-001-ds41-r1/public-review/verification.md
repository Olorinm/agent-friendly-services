公开证据节选；独立核验原文件 SHA256：b4b18e55bc9dd17de576daa0f0eb00c8a47c0d60806c4a9f0b0a06ed53a3d7db。原始材料私有保存，以下编辑不改验收结论。

# 独立核验摘要（geocoding-venue-001 / photon）

## 1. 真实指定服务查询
- 入口：https://photon.komoot.io/api/（冻结 ENVIRONMENT.md 指定）。
- 采集证据 cache/q_british_museum_headers.txt：HTTP/1.1 200，Server: nginx，Date 2026-10-08 15:24:32，Cache-Control: max-age=3600。
- 请求带真实标识 User-Agent: agent-friendly-services/20261008 (+https://github.com/Olorinm/agent-friendly-services)。

## 2. 身份语义（场馆本身）
响应 cache/q_british_museum.json 首条 Feature：
- name=British Museum；osm_type=R；osm_id=177044；osm_key=tourism；osm_value=museum；
- street=Great Russell Street；locality=St Giles；district=Bloomsbury；city=London；state=England；country=United Kingdom；postcode=WC1B 3DG；countrycode=GB。
- geometry.coordinates=[-0.1267051, 51.5193118]（GeoJSON：经度, 纬度）。
-> 为 tourism=museum 的场馆对象，非街道/邮编/城市中心。

## 3. 坐标与 200m 容差
- 答复坐标：纬度 51.5193118 / 经度 -0.1267051（与响应一致，轴序正确）。
- 冻结官方场馆点（reference.json / reference-sources）：51.519413319978, -0.12695659999997。
- Haversine（R=6371008.8）：d ≈ 20.7 m ≤ 200 m。

## 4. 输入地址 vs 返回地址
- 输入地址（附件）：Great Russell Street, London WC1B 3DG, United Kingdom。
- 返回地址（场馆查询）：Great Russell Street, St Giles, Bloomsbury, London, England, United Kingdom, WC1B 3DG。
- 以输入地址原文查询时返回 highway=tertiary、type=street 的街道段（cache/q_address.json），属街道级，未冒充场馆；答复已如实分开说明。

## 5. 免费规则依据
官方 https://photon.komoot.io/ 允许合理量项目使用，过量可能限流且无可用性保证；本次使用无认证、无支付的公开demo入口。只依据官方适用规则和实际免认证查询，不以不付费指令单独推定免费。

公开地点数据来源：[Photon / komoot](https://photon.komoot.io/) 与 [OpenStreetMap contributors](https://www.openstreetmap.org/copyright)，按 [ODbL](https://opendatacommons.org/licenses/odbl/) 许可标注来源。变动：选取任务相关字段，中文说明和坐标距离计算；不代表服务方背书。Nominatim无成功响应，因此其记录没有可发布的服务地点数据。

总控实际检查后，仅允许通用连接配置从接入带入下一题，没有继承接入地点、坐标或业务脚本。每阶段最多4次请求和15秒间隔是本次测试约束，不是Photon承诺的数值配额。

重要表述限制：执行者答复中的“常见官方点位”51.5194,-0.1270来自其自行写入的近似点，未提供官方来源；23米不是本轮独立核验值。验收使用事前冻结的独立官方场馆点，得到约20.7米。答案所称重心及点落在场馆轮廓内，也不能只由返回bbox严格证明；可确认的是匹配到场馆对象、返回点位于官方位置200米内，适用于行程概览，不是精确入口导航。原答复保留以供核对。实际调用顺序为先场馆名称、后地址，答案的叙述顺序不代表真实调用顺序。

独立参考来源是大英博物馆官方visit页面的搜索索引提取（原站直接请求403，索引标记约5个月前抓取且无精确抓取时间），不是成功下载的原始HTML；只用于稳定场馆位置，不推断当日开放安排。200米是执行前已向用户题目公开的用途容差，不是官方精度标准。只有Photon完成业务，Nominatim因接入环境无效暂缓，因此无同题跨服务结果快照，也不能给两者排准确性名次。
