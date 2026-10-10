Data retrieved and consistent. Now building deliverables.
已完成，数据经 ECB Data Portal 官方 API 实际取得（HICP 数据流，`AVR` 年度平均变化率，`000000` 全项目，`N` 未季调/未工作日调整，`4D0` Eurostat）。

**回落幅度（2024 vs 2023，百分点）**
- 德国：6.0% → 2.5%，回落 **3.5 个百分点**
- 法国：5.7% → 2.3%，回落 **3.4 个百分点**

**交付文件**（当前工作目录）
- `de_fr_hicp_annual_avg_2023_2024.csv` — 长表：国家/年份/指标/口径/单位/数值/序列键/来源/查询日
- `de_fr_hicp_annual_avg_summary.csv` — 汇总：`change_pp` 列
- `SOURCES.md` — 来源与口径说明；`fetch_hicp.py` — 可复现查询脚本；原始响应在 `cache/`

**可追溯来源**
- 入口：`https://data-api.ecb.europa.eu/service/`，序列 `HICP.A.DE.N.000000.4D0.AVR` 与 `HICP.A.FR.N.000000.4D0.AVR`（`startPeriod=2023&endPeriod=2024`）；文档 https://data.ecb.europa.eu/help/api/data-examples ；查询日期 **2026-10-10**。
- 口径：HICP 全项目年度平均变化率（全年平均指数对上年平均指数的涨幅，单位 `PCCH`/%，保留一位小数），非本国 CPI、非 12 月同比、非各月同比均值。所取记录无 `BREAKS`/`PRE_BREAK_VALUE` 修订标记；但 HICP 数据仍可能例行修订，来源署名为 (c) European Central Bank, ECB Data Portal / Eurostat，数值未作修改。