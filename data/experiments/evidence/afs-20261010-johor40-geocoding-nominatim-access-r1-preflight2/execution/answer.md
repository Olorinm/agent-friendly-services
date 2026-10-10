已接通 Nominatim 公共 Search API 并完成真实地点查询。

## 查询结果（真实响应）
查询 `Johor Bahru, Malaysia`：
- **匹配地点**：Johor Bahru, Johor, 80730, Malaysia
- **纬度 (latitude)**：`1.4581986`
- **经度 (longitude)**：`103.7649059`
- **OSM 对象**：node/254237831（place=city）
- **获取时间**：2026-10-10T10:33:45Z
- **请求 URL**：`https://nominatim.openstreetmap.org/search?q=Johor+Bahru%2C+Malaysia&format=jsonv2&addressdetails=1&limit=1`
- **来源**：OpenStreetMap / Nominatim — © OpenStreetMap contributors，https://www.openstreetmap.org/copyright

地点→坐标转换确认成功（返回标准 lat/lon 字段）。

## 本地配置与产物
- **通用连接配置**（持久）：`/home/node/service-tools/service-config.json`（base_url、format、UA、缓存路径、限流、来源署名）
- **原始响应缓存**（持久，按完整 URL 键）：`/home/node/service-tools/geocoding-cache/responses.json`
- **查询/缓存脚本**（本题目录）：`/workspace/...-preflight2-execution/geocode_query.py`
- 无秘密/凭据文件：该入口匿名，无需账号。

## 接入步骤（全部自助完成，无需人工介入）
1. 确认公共入口授权范围，未注册、未付费（匿名公共实例）。
2. 复用指定真实 UA：`agent-friendly-services/20261010 (+https://github.com/Olorinm/agent-friendly-services)`。
3. 用 Python 标准库（urllib）编写脚本，无需额外依赖。
4. 请求前先查缓存文件；按完整请求 URL 缓存原始响应+获取时间，相同 URL 只读缓存。
5. 单线程、相邻请求起始间隔 ≥20s，执行查询并解析 lat/lon。

## 实际阻碍
- 首次查询 `Sultan Ibrahim Building, Johor Bahru, Malaysia` 返回 **No match**（该具体建筑未被 OSM 收录），非服务故障。第二次换用可解析的公开地点后成功（本阶段共 2 次尝试，上限 4 次；无 403/429）。
- 公共实例有严格使用政策：须保留 OSM 署名、不得批量抓取、不得封装为通用查询平台；本次为低量只读研究。免费范围内无支付/资质要求，无需额外申请。

未完成部分：无（一次真实地点查询 + 坐标转换 + 本地配置保存均已达成）。