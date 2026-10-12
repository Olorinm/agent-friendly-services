Data retrieved. Germany 2023=6.0, 2024=2.5; France 2023=5.7, 2024=2.3. Now building the CSV deliverables.
完成。数据经指定 ECB Data Portal 官方 API（`https://data-api.ecb.europa.eu/service/`）实际查询取得。

**结果（全项目 HICP 年度平均变化率，%，未季调/未工作日调整）**

| 国家 | 2023 | 2024 | 2024 较 2023 回落 |
|---|---|---|---|
| 德国 | 6.0 | 2.5 | **3.5 个百分点** |
| 法国 | 5.7 | 2.3 | **3.4 个百分点** |

**交付文件**
- `hicp_de_fr_annual_average_2023_2024.csv` — 长表，含 country/country_code/year/indicator/unit/value/drop_vs_prev_year_pp/source/source_url/series_key/query_date
- `data/ecb_icp_raw_DEFR_2022-2024.csv` — API 原始返回（留档）

**数据来源（查询日期 2026-10-10）**
- API 调用：`https://data-api.ecb.europa.eu/service/data/ICP/A.DE+FR.N.000000.4.AVR?format=csvdata&startPeriod=2022&endPeriod=2024`
- 数据集：ICP（"Indices of Consumer Prices"，即 HICP），门户 https://data.ecb.europa.eu/data/datasets/ICP
- 系列键：`ICP.A.<DE|FR>.N.000000.4.AVR`
  - 维度含义：`A`=年频；`DE`/`FR`=国家；`N`=Neither seasonally nor working day adjusted；`000000`=Overall index（全项目）；`4`=Eurostat 为编制机构；`AVR`=Annual average rate of change（年度平均变化率，全年平均指数相对上年平均）
- 单位：PCCH（percent change，%）；`OBS_STATUS=A`（正常值），`OBS_CONF=F`（非机密）

**修订/口径说明**：所用 `AVR` 系列即题目要求的“全年平均指数相对上年平均指数的涨幅”，非 12 月同比、非各月同比简单平均。查询时无中断标志（`BREAKS` 为空），编制方为 Eurostat。HICP 年度平均率日后可能随指数修订而更新，本表采用查询当日现行公布值。原始数据署名为 European Central Bank / Eurostat。