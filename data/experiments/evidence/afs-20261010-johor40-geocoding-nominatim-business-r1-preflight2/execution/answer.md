已完成查询（Nominatim 公共 Search API，单线程、间隔≥20s）。

## 结果

- **匹配地点名称**：British Museum（大英博物馆）
- **WGS84 十进制度坐标**：**纬度 51.5193118，经度 -0.1267051**
- **数据来源**：OpenStreetMap contributors，经 Nominatim 公共 Search API 返回；OSM 对象 `relation/177044`，`place_id` 290933544；许可 Data © OpenStreetMap contributors, ODbL 1.0（https://www.openstreetmap.org/copyright）
- **定位类型**：**场馆本身**。返回对象类别 `category=tourism`、`type=museum`、`addresstype=tourism`、`place_rank=30`，是博物馆的多边形（multipolygon）关系，坐标为场馆轮廓中心；**不是入口，也不是街道/邮编/城市中心**（输入中的街道、邮编未冒充场馆）。

**服务实际返回的字段**（原文）：
- `display_name`: `British Museum, Great Russell Street, St Giles, Bloomsbury, London Borough of Camden, Greater London, England, WC1B 3DG, United Kingdom`
- `address`: road=Great Russell Street；neighbourhood=St Giles；suburb=Bloomsbury；city_district=London Borough of Camden；city=Greater London；state=England；postcode=WC1B 3DG；country=United Kingdom；country_code=gb
- `boundingbox`: [51.5180651, 51.5205596, -0.1288843, -0.1248691]

**输入地址与服务返回地址的区分**：输入为 `The British Museum; Great Russell Street, London WC1B 3DG, United Kingdom`。服务返回的 `display_name`/`address` 与输入的路名和邮编一致（Great Russell Street、WC1B 3DG），但结构性字段（neighbourhood/suburb/city_district 等）由服务补全，非输入提供。

**过程中的事实**：直接用完整输入地址查询 `The British Museum, Great Russell Street, London WC1B 3DG, United Kingdom` 返回 `[]`（无结果，1 次尝试）；改用 `British Museum, Great Russell Street, London` 命中场馆（1 次尝试）。共 2 次请求，未触发限流。原始响应与获取时间已缓存于 `/home/node/service-tools/geocoding-cache/responses.json`；查询脚本 `geocode_query.py` 在当前工作目录。

定位精度满足要求（场馆中心，远优于 200 米门限）。