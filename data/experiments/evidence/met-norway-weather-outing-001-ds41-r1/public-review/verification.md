公开证据节选；独立核验原文件 SHA256：22177eb8d5104e893178c14496bf8a3c2e402160d121f79fc20cc261a7f611ac。原始材料私有保存，以下编辑不改验收结论。

```json
{
  "derived_from": [
    "execution/artifacts/forecast.json (gzip, sha256 233c651e3cda7b50cb9d6e9cc76c481cc0969174795dba3826b4a96a4ade7cce)",
    "execution/artifacts/response_headers.txt"
  ],
  "provider": "MET Norway Locationforecast 2.0 compact",
  "service_url": "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5074&lon=-0.1278",
  "updated_at": "2026-10-08T13:16:55Z",
  "units": {
    "air_pressure_at_sea_level": "hPa",
    "air_temperature": "celsius",
    "cloud_area_fraction": "%",
    "precipitation_amount": "mm",
    "relative_humidity": "%",
    "wind_from_direction": "degrees",
    "wind_speed": "m/s"
  },
  "returned_point": [
    -0.1278,
    51.5074,
    8
  ],
  "intervals": [
    {
      "local_start_BST": "2026-10-10T09:00:00+01:00",
      "utc_start": "2026-10-10T08:00:00Z",
      "air_temperature_c": 10.6,
      "precip_next_1h_mm": 0.0,
      "symbol": "partlycloudy_day"
    },
    {
      "local_start_BST": "2026-10-10T10:00:00+01:00",
      "utc_start": "2026-10-10T09:00:00Z",
      "air_temperature_c": 11.8,
      "precip_next_1h_mm": 0.0,
      "symbol": "clearsky_day"
    },
    {
      "local_start_BST": "2026-10-10T11:00:00+01:00",
      "utc_start": "2026-10-10T10:00:00Z",
      "air_temperature_c": 13.0,
      "precip_next_1h_mm": 0.0,
      "symbol": "fair_day"
    }
  ]
}
```


Weather data by [Norwegian Meteorological Institute (MET Norway)](https://www.met.no/en) — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Changes: selected fields, local-time conversion and table presentation for this task; no service endorsement.

本轮只检验指定服务预报查询与忠实交付，不验证未来真实天气是否命中，也不以两家数值相同为标准。两家可能共享上游预报。当前/未来气温均按服务提供的模型或预报值理解，不视为气象站实测观测。原始调用、回执与全部冻结字段/时区资料私有保留；公开只展示任务相关小表与核验摘要。单轮、同一出口IP，不是普遍可靠性或预测准确率排名。

独立总控业务前只读回执manifest SHA256：84844d3b6a0cfcd5c232b5487f5fae3fe7fb47214c4a79540c33f86930701def。每服务另1次公共GET作为核验辅助开销；后续预报更新不能推翻较早真实查询，最终答案按执行时响应独立核对。独立验收预算40次模型请求/300秒，被测预算25次/600秒，双方一致。
