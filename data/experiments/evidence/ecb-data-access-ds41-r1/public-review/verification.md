公开证据节选：总控从独立验收记录选取必要内容；原始核验文件 SHA256：68e052d07e922d18d1ed460f7e7ee1642a0c1b7e0cf7ffbdf86e731fe8862d0f。任务完成结论不变。

# 独立核验摘要（验收环境）

验收方于验收环境独立复现指定入口，不依赖执行者脚本。

## 独立请求与结果（2026-10-08）

1. `GET https://data-api.ecb.europa.eu/service/data/EXR/M.USD.EUR.SP00.A?lastNObservations=2&format=jsondata`
   - 无任何认证头（无 Key/Cookie）
   - HTTP 200 | 3223 bytes
   - 解析：series key `0:0:0:0:0`，dimensions `[FREQ, CURRENCY, CURRENCY_DENOM, EXR_TYPE, EXR_SUFFIX]`，最近两条观测 `1.1593095238095241`、`1.1513227272727276`。与执行记录一致。
2. `GET https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2024-01-01&endPeriod=2024-01-05&format=csvdata`
   - HTTP 200；返回 4 行真实日度观测：2024-01-02=1.0956、01-03=1.0919、01-04=1.0953、01-05=1.0921（TITLE=US dollar/Euro ECB reference exchange rate）。

## 结论

指定入口为真实 ECB SDMX 2.1 REST API，免 Key 可查询真实金融数据，复现成功。
