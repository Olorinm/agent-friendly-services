# ecb-data 独立复测（验收环境，2026-09-15）

## 独立调用同一指定入口（与执行环境独立）

```
$ curl -sS --http1.1 "https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?lastNObservations=2&format=csvdata"
KEY,FREQ,CURRENCY,CURRENCY_DENOM,EXR_TYPE,EXR_SUFFIX,TIME_PERIOD,OBS_VALUE,...
EXR.D.USD.EUR.SP00.A,D,USD,EUR,SP00,A,2026-09-11,1.1592,A,...
EXR.D.USD.EUR.SP00.A,D,USD,EUR,SP00,A,2026-09-14,1.1551,A,...
[HTTP 200]
```

- 无凭据、无 Key 直接返回 HTTP 200 与真实观测值，证实该服务公开只读、无需注册。
- 与执行会话采信值一致（执行记录 0005 同端点：2026-09-10=1.1616、2026-09-11=1.1592、2026-09-14=1.1551），数据并非模型记忆或其他来源。

## 执行会话的真实查询证据（摘录业务字段）

- 0005：GET /service/data/EXR/D.USD.EUR.SP00.A?lastNObservations=3&format=csvdata → HTTP 200，3 条日汇率观测。
- 0008：GET /service/data/EXR/D.GBP+JPY.EUR.SP00.A?lastNObservations=1&format=csvdata&detail=dataonly → HTTP 200，GBP 0.85598 / JPY 178.52（2026-09-14）。
- 0009/0014：GET /service/data/EXR/M.USD.EUR.SP00.A?startPeriod=2009-05-01&endPeriod=2009-05-31 → HTTP 200，SDMX Generic XML，Header Sender id="ECB"、结构 ECB_EXR1、Prepared 2026-09-15T09:06:40+02:00，仅含 2009-05 一条观测（值 1.365045），日期过滤生效。
- 0012：GET /service/data/ICP/M.U2.N.000000.4.ANR?lastNObservations=2&format=csvdata → HTTP 200，HICP 年率 2025-11=2.1、2025-12=1.9。

## 配置持久化证据

- 执行会话将 /home/node/service-tools/service-config.json（2195 字节，含 base_url、查询路径、常用参数、序列键语法、已验证调用、--http1.1 降级提示）写入持久目录；首次 JSON 校验失败后修正引号错误，python3 -m json.tool 校验输出 "JSON OK"（工具 0016→0020）。
- 运行回执 retained-files.json 列含 "service-config.json"，隔离说明含 "retained service-tools"，配置可供后续会话复用。

## 免费规则（核实于 2026-09-15）

- 来源：ECB 官方 Disclaimer & Copyright，https://www.ecb.europa.eu/services/using-our-site/disclaimer/html/index.en.html
- 原文（Copyright 节）："users of this website may make free use of the information obtained directly from it"（条件为注明来源、准确转载等）。
- 适用性：本次及执行会话全部请求均为对 ECB 网站公开数据的只读 GET 检索，未注册、未登录、未付费；运行环境亦未提供任何账户、Key 或支付方式。属上述免费使用规则范围。
