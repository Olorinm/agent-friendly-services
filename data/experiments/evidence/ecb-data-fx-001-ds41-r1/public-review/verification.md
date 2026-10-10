公开证据节选：总控从独立验收记录选取必要内容；原始核验文件 SHA256：012554dcc7fc722cb19ef3b5d6bb1ccddbebfbddcc1f2a3cb915141411e72bfc。任务完成结论不变。

# ECB Data API 当次汇率观测（摘录）

来源：执行 env 内单次未认证 curl 请求（2026-10-08）：
`curl -s --max-time 60 "https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2026-08-01&endPeriod=2026-08-31&format=csvdata"`

响应为 ECB SDMX CSV（KEY=EXR.D.USD.EUR.SP00.A，CURRENCY=USD，CURRENCY_DENOM=EUR，
TITLE="US dollar/Euro ECB reference exchange rate"）。与本次任务相关行（TIME_PERIOD,OBS_VALUE）：

- 2026-08-13, 1.1534
- 2026-08-14, 1.1567
- 2026-08-17, 1.1593

08-15（周六）、08-16（周日）无观测；下一发布日为 08-17（周一）。
即 1 EUR = 1.1567 USD（08-14）/ 1.1593 USD（08-17），USD→EUR 应除以该值。
