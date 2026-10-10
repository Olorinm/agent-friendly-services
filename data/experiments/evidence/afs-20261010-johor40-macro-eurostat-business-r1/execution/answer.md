Dataset `prc_hicp_aind` works, but it's marked discontinued, replaced by `prc_hicp_ainr`. Let me query the current dataset to confirm/compare.
Both datasets parsed. Let me check `prompt.txt` and write the extraction script.
已完成。数据经本轮指定服务 Eurostat Statistics API 实际取得。

**结果（全项目 HICP 年度平均涨幅，NSA，%）**

| 国家 | 2023 | 2024 | 回落 |
|---|---|---|---|
| 德国 | 6.0 | 2.5 | **3.5 个百分点** |
| 法国 | 5.7 | 2.3 | **3.4 个百分点** |

**交付文件**（当前工作目录）
- `hicp_de_fr_annual_avg_change_2023_2024.csv` — 长表，含国家、年份、指标、单位，并附回落行
- `SOURCES.md` — 来源与追溯说明
- `extract_hicp.py`、`raw/` — 解析脚本与原始响应

**来源**
- 现行数据集 `prc_hicp_ainr`（HICP 年度数据，ECOICOP ver.2，2025=100），指标 `RCH_A_AVG`，全项目 `coicop18=TOTAL`，`geo=DE/FR`：
  https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_ainr?format=JSON&lang=EN&coicop18=TOTAL&geo=DE&geo=FR&sinceTimePeriod=2022&untilTimePeriod=2024
- 查询日期：2026-10-10（UTC）

**修订/口径说明**：前身数据集 `prc_hicp_aind`（ECOICOP ver.1，`coicop=CP00`，2015=100，已停用）取值完全相同（德 6.0/2.5、法 5.7/2.3），无修订差异；差异仅在分类版本与指数基准年，基准年变更只影响指数点位、不影响同比涨幅。本 CSV 采用现行 `prc_hicp_ainr`。

来源署名 Eurostat；本表为对 Eurostat 公开数据的重新整理。