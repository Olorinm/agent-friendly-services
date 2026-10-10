公开证据节选；独立核验原文件 SHA256：878bb8f9e08176b0ed73a9f2e8a18da2bdbb5db9ba29b695c1093ffb0864e551。原始材料私有保存，以下编辑不改验收结论。

# 核验摘要：weather-access-001/v1（open-meteo）

## 真实请求（本次唯一一次天气 API 读取）
- 指定入口请求 URL（来自 execution/artifacts/run1.stderr [REQUEST] 行）：
  `https://api.open-meteo.com/v1/forecast?latitude=39.9042&longitude=116.4074&current=temperature_2m,...&daily=...&timezone=auto&temperature_unit=celsius&wind_speed_unit=kmh&precipitation_unit=mm&timeformat=iso8601`
- 响应头 Date: Thu, 08 Oct 2026 14:51:44 GMT；缓存头均为 None（无 Cache-Control/Expires）。
- 第二次同参数运行仅命中本地缓存（execution/artifacts/run2.stderr: `[CACHE HIT] ... default TTL 600s`），未新增网络读取。

## 响应业务字段（execution/artifacts/last_response.json，与 run2.json / cache 逐字节一致）
- 地点：请求 39.9042,116.4074（北京，CN）；返回 latitude=39.89455, longitude=116.35983
- 时区：Asia/Shanghai (GMT+8)
- 观测时间：2026-10-08T22:45（interval 900 s）
- 数值与单位：气温 20.1 °C，体感 21.0 °C，相对湿度 66 %，降水 0.00 mm，天气码 0，风速 1.0 km/h，风向 211°
- 逐日：最高/最低温 °C、降水 mm、降水概率 %，覆盖 2026-10-08 至 2026-10-14

## 与答复一致性
- execution/answer.md 所报地点、观测时间（22:45）、当前数值与逐日表格与上述响应逐项一致，并标注单位。

## 复用配置
- 持久配置写入 `/home/node/service-tools/service-config.json`（base_url、无鉴权、默认单位/时区、User-Agent、非商业许可、缓存/限流设置）；retained-files.json 列为保留文件。内容不含任何密钥。

## 免费规则
- 官方定价页 https://open-meteo.com/en/pricing 明确：Free / Open-Access 列为非商业用途、无需 API key、限 10,000 次/日；客户付费域为 customer-api.open-meteo.com。
- 本次以非商业研究身份、无 key 成功请求 1 次，远低于日限，未付费。


Weather data by [Open-Meteo](https://open-meteo.com/) — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Changes: selected fields, local-time conversion and table presentation for this task; no service endorsement.

本轮只检验指定服务预报查询与忠实交付，不验证未来真实天气是否命中，也不以两家数值相同为标准。两家可能共享上游预报。当前/未来气温均按服务提供的模型或预报值理解，不视为气象站实测观测。原始调用、回执与全部冻结字段/时区资料私有保留；公开只展示任务相关小表与核验摘要。单轮、同一出口IP，不是普遍可靠性或预测准确率排名。
