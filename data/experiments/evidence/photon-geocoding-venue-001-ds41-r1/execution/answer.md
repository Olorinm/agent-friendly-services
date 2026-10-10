已用指定服务 Photon（komoot 公开 demo）完成查询。

**匹配地点名称**：British Museum（大英博物馆）

**WGS84 十进制度坐标**（EPSG:4326）
- 纬度：**51.5193118**
- 经度：**-0.1267051**

**服务实际返回的地址信息**
`name=British Museum｜street=Great Russell Street｜locality=St Giles｜district=Bloomsbury｜city=London｜state=England｜country=United Kingdom｜postcode=WC1B 3DG｜countrycode=GB`；OSM 对象 `R 177044`，`tourism=museum`，`type=house`。返回坐标为 `[-0.1267051, 51.5193118]`（经度, 纬度）。

**定位粒度**：这是**场馆本身**（OSM 关系 R 177044 的代表点/重心，落在场馆范围内），**不是入口级**——服务未返回单独入口节点。校验：距场馆 bbox 中心约 12 m，距常见官方点位约 23 m，满足 200 m 场馆级要求，可用于行程标记。

**数据来源**：Photon（https://photon.komoot.io/ ），底层数据 **OpenStreetMap**，许可 https://www.openstreetmap.org/copyright 。

说明：输入地址原文查询只返回 *Great Russell Street 街道段*（街道级，不能代表场馆），故最终采用按场馆名称查询结果。原始响应已存 `cache/`，答案存 `answer.md`。