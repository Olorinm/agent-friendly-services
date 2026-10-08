已完成一次 Open-Meteo 预报查询（入口 `https://api.open-meteo.com/v1/forecast`，免费非商业 Forecast API）。

## 伦敦市中心 2026-10-10 上午预报（09:00–12:00）

坐标：纬度 51.5074、经度 -0.1278（服务实际返回网格点 51.5115, -0.1308，海拔 16 m）｜时区 Europe/London（查询时为 GMT+1/BST）

| 时段（当地） | 气温（°C，区间起始整点近地面 2 m） | 降水量（mm，该整小时累计总降水） |
|---|---|---|
| 09:00–10:00 | 11.3 | 0.0 |
| 10:00–11:00 | 12.0 | 0.0 |
| 11:00–12:00 | 13.3 | 0.0 |

- **来源**：Open-Meteo Forecast API（`hourly=temperature_2m,precipitation`）；数据署名：Weather data by Open-Meteo.com (CC BY 4.0)。
- **查询时间**：2026-10-08 14:54 UTC，即当地 2026-10-08 15:54（Europe/London，UTC+1）。
- **降水提示**：三个时段预报累计降水均为 0.0 mm，**09:00–12:00 无降水，适合散步**。数据无缺失，未将缺失视为零。

原始响应已保存在当前目录 `response.json`（HTTP 头见 `headers.txt`）。