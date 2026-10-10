公开证据节选；独立核验原文件 SHA256：58e538697cfc75507cd6ed9549aa10d288e962ca4d735f49010592881289aaa1。原始材料私有保存，以下编辑不改验收结论。

# 核验摘要（从当次真实响应摘录）

来源：`execution/artifacts/response.json`、`execution/artifacts/headers.txt`（本次执行采集副本）。

- 服务/入口：`https://api.open-meteo.com/v1/forecast`（Open-Meteo 非商业免费公共 Forecast API，无需账号/Key）。
- 请求参数：latitude=51.5074, longitude=-0.1278, hourly=temperature_2m,precipitation, timezone=Europe/London, start_date/end_date=2026-10-10；无 API key。
- HTTP 回执：`HTTP/1.1 200 OK`，`Date: Thu, 08 Oct 2026 14:54:33 GMT`（即当地 15:54，Europe/London UTC+1）。
- 响应元数据：返回网格点 51.5115, -0.1308，elevation 16.0，utc_offset_seconds=3600，timezone=Europe/London，timezone_abbreviation=GMT+1；units: temperature_2m=°C，precipitation=mm。
- 相关小时值（当地时标）：
  - 09:00 temperature_2m=11.3；10:00 precipitation=0.00
  - 10:00 temperature_2m=12.0；11:00 precipitation=0.00
  - 11:00 temperature_2m=13.3；12:00 precipitation=0.00
- 结论：三个区间 09:00–10:00 / 10:00–11:00 / 11:00–12:00 起始整点气温为 11.3/12.0/13.3 °C，整小时累计降水均为 0.0 mm；数据无缺失，无其他天气服务调用。


Weather data by [Open-Meteo](https://open-meteo.com/) — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Changes: selected fields, local-time conversion and table presentation for this task; no service endorsement.

本轮只检验指定服务预报查询与忠实交付，不验证未来真实天气是否命中，也不以两家数值相同为标准。两家可能共享上游预报。当前/未来气温均按服务提供的模型或预报值理解，不视为气象站实测观测。原始调用、回执与全部冻结字段/时区资料私有保留；公开只展示任务相关小表与核验摘要。单轮、同一出口IP，不是普遍可靠性或预测准确率排名。

独立总控业务前只读回执manifest SHA256：84844d3b6a0cfcd5c232b5487f5fae3fe7fb47214c4a79540c33f86930701def。每服务另1次公共GET作为核验辅助开销；后续预报更新不能推翻较早真实查询，最终答案按执行时响应独立核对。独立验收预算40次模型请求/300秒，被测预算25次/600秒，双方一致。
