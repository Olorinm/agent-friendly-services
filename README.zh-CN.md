<!-- 生成文件 — 修改 scripts/generate.ts，再运行 npm run generate。 -->

# Agent-Friendly Services

[English](./README.md) | 简体中文

**哪些服务能让 AI Agent 真正把事办成？我们让 Agent 用真实任务去试，记录通过率、费用和接入门槛。**

**195** 个服务 · **35** 个已实测 · **187** 次有效试跑 · 最近一次 2026-10-10

**通过率**：该子类所有任务（含接入任务）中通过独立验收的试跑比例，括号内为通过数 / 有效试跑数。**平均费用**：每次试跑的模型费用（按 LiteLLM 价表估算）加有记录的服务费，取平均。**免注册**：✅ 不用事先注册即可使用 · ❌ 需要事先准备账号或密钥。环境故障导致的无效试跑不计入。点子类标题旁的 → 查看各任务明细。

[旅行](#results-travel) · [数据库](#results-databases) · [搜索与网页抓取](#results-search-scraping) · [地图与地理](#results-maps-geo) · [天气与日历](#results-weather-calendar) · [金融数据](#results-financial-data) · [学术与知识](#results-scholarly) · [办公与协作](#results-productivity-storage) · [开发工具](#results-developer-tools) · [支付与计费](#results-payments-billing) · [通信](#results-communication)

<a id="results-travel"></a>

## 旅行

### 机票 [→](./generated/directory.zh-CN.md#services-travel-flights)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [Kiwi.com](./generated/services.md#kiwi) | **100%**（2/2） | $0.85 | [MCP](https://mcp.kiwi.com) | ✅ |
| [Ignav Flights](./generated/services.md#ignav) | **100%**（1/1） | $0.93 | [网页](https://ignav.com/playground) | ✅ |

<a id="results-databases"></a>

## 数据库

### 托管关系型数据库 [→](./generated/directory.zh-CN.md#services-databases-hosted-relational)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [Turso](./generated/services.md#turso) | **92%**（11/12） | $0.02 | [API](https://api.turso.tech/v1/) | ❌ |
| [Neon](./generated/services.md#neon) | **88%**（7/8） | $0.01 | [API](https://claimable.neon.tech/v1/agent/identity) | ✅ |

<a id="results-search-scraping"></a>

## 搜索与网页抓取

### 网页搜索 [→](./generated/directory.zh-CN.md#services-search-scraping-web-search)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [Exa](./generated/services.md#exa) | **100%**（5/5） | $0.01 | [MCP](https://mcp.exa.ai/mcp) | ✅ |
| [Firecrawl](./generated/services.md#firecrawl) | **100%**（3/3） | $0.01 | [API](https://api.firecrawl.dev/v2/search) | ✅ |
| [Exa](./generated/services.md#exa) | **0%**（0/1） | — | [API](https://exa.ai/docs/reference/search) | ❌ |

### 网页内容提取 [→](./generated/directory.zh-CN.md#services-search-scraping-web-extraction)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [Jina AI](./generated/services.md#jina) | **100%**（7/7） | $0.0071 | [API](https://r.jina.ai/) | ✅ |
| [Firecrawl](./generated/services.md#firecrawl) | **83%**（10/12） | $0.01 | [API](https://api.firecrawl.dev/v2/scrape) | ✅ |
| [Exa](./generated/services.md#exa) | **80%**（4/5） | $0.02 | [MCP](https://mcp.exa.ai/mcp) | ✅ |

<a id="results-maps-geo"></a>

## 地图与地理

### 地理编码 [→](./generated/directory.zh-CN.md#services-maps-geo-geocoding)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [Nominatim Public API](./generated/services.md#nominatim) | **100%**（2/2） | $0.0094 | [API](https://nominatim.openstreetmap.org/search) | ✅ |
| [Photon Public Demo API](./generated/services.md#photon) | **100%**（2/2） | $0.01 | [API](https://photon.komoot.io/api/) | ✅ |

### 路线规划 [→](./generated/directory.zh-CN.md#services-maps-geo-route-planning)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [OSRM Public Demo API](./generated/services.md#osrm) | **100%**（2/2） | $0.0093 | [API](https://router.project-osrm.org/route/v1/driving) | ✅ |
| [Valhalla Public Demo API](./generated/services.md#valhalla) | **100%**（2/2） | $0.01 | [API](https://valhalla1.openstreetmap.de/route) | ✅ |

<a id="results-weather-calendar"></a>

## 天气与日历

### 天气数据 [→](./generated/directory.zh-CN.md#services-weather-calendar-weather-data)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [MET Norway Locationforecast](./generated/services.md#met-norway) | **100%**（2/2） | $0.0085 | [API](https://api.met.no/weatherapi/locationforecast/2.0/compact) | ✅ |
| [Open-Meteo](./generated/services.md#open-meteo) | **100%**（2/2） | $0.0097 | [API](https://api.open-meteo.com/v1/forecast) | ✅ |

### 公共节假日 [→](./generated/directory.zh-CN.md#services-weather-calendar-public-holidays)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [OpenHolidays API](./generated/services.md#openholidays) | **100%**（8/8） | $0.0096 | [API](https://openholidaysapi.org/PublicHolidays) | ✅ |
| [Nager.Date](./generated/services.md#nager-date) | **100%**（8/8） | $0.01 | [API](https://nagerholidays.com/api/v4/Holidays) | ✅ |

<a id="results-financial-data"></a>

## 金融数据

### 汇率数据 [→](./generated/directory.zh-CN.md#services-financial-data-fx)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [ECB Data Portal API](./generated/services.md#ecb-data) | **100%**（7/7） | $0.01 | [API](https://data-api.ecb.europa.eu/service/) | ✅ |
| [Frankfurter](./generated/services.md#frankfurter) | **100%**（4/4） | $0.0056 | [API](https://api.frankfurter.dev/v2/) | ✅ |

### 资产行情 [→](./generated/directory.zh-CN.md#services-financial-data-prices)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [Alpha Vantage](./generated/services.md#alpha-vantage) | **80%**（4/5） | $0.01 | [API](https://www.alphavantage.co/query) | ❌ |
| [Alpha Vantage](./generated/services.md#alpha-vantage) | **75%**（3/4） | $0.02 | [MCP](https://mcp.alphavantage.co/mcp) | ❌ |

### 公司财务数据 [→](./generated/directory.zh-CN.md#services-financial-data-statements)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [Alpha Vantage](./generated/services.md#alpha-vantage) | **100%**（4/4） | $0.01 | [API](https://www.alphavantage.co/query) | ❌ |
| [SEC EDGAR Data APIs](./generated/services.md#sec-edgar) | **100%**（2/2） | $0.0092 | [API](https://data.sec.gov/) | ✅ |
| [Alpha Vantage](./generated/services.md#alpha-vantage) | **100%**（2/2） | $0.03 | [MCP](https://mcp.alphavantage.co/mcp) | ❌ |

### 交易披露 [→](./generated/directory.zh-CN.md#services-financial-data-disclosures)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [CapitolExposed](./generated/services.md#capitol-exposed) | **90%**（9/10） | $0.02 | [API](https://www.capitolexposed.com/api/v1) | ✅ |
| [Bargo Congress Trades API](./generated/services.md#bargo-congress) | **55%**（6/11） | $0.02 | [API](https://www.bargo.ai/free-apis/congress/v1) | ✅ |
| [Tracefour](./generated/services.md#tracefour) | **0%**（0/1） | $0.0071 | [API](https://tracefour.com/v1) | ✅ |

### 宏观经济指标 [→](./generated/directory.zh-CN.md#services-financial-data-macro)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [ECB Data Portal API](./generated/services.md#ecb-data) | **100%**（8/8） | $0.02 | [API](https://data-api.ecb.europa.eu/service/) | ✅ |
| [Eurostat Data API](./generated/services.md#eurostat) | **100%**（6/6） | $0.02 | [API](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/) | ✅ |

<a id="results-scholarly"></a>

## 学术与知识

### 学术文献检索 [→](./generated/directory.zh-CN.md#services-scholarly-scholarly-search)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [Crossref](./generated/services.md#crossref) | **100%**（2/2） | $0.0097 | [API](https://api.crossref.org/works) | ✅ |
| [OpenAlex](./generated/services.md#openalex) | **100%**（2/2） | $0.0099 | [API](https://api.openalex.org/works) | ✅ |

<a id="results-productivity-storage"></a>

## 办公与协作

### 协作表格 [→](./generated/directory.zh-CN.md#services-productivity-storage-collaborative-tables)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [Grist](./generated/services.md#grist) | **100%**（7/7） | $0.03 | [MCP](https://docs.getgrist.com/api/mcp) | ❌ |
| [Notion](./generated/services.md#notion) | **100%**（2/2） | $0.75 | [API](https://developers.notion.com/reference/intro) | ❌ |
| [Grist](./generated/services.md#grist) | **78%**（7/9） | $0.03 | [API](https://docs.getgrist.com/api) | ❌ |

<a id="results-developer-tools"></a>

## 开发工具

### 依赖漏洞公告 [→](./generated/directory.zh-CN.md#services-developer-tools-dependency-advisories)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [GitHub](./generated/services.md#github) | **100%**（8/8） | $0.01 | [API](https://api.github.com/advisories) | ✅ |
| [OSV.dev](./generated/services.md#osv) | **100%**（8/8） | $0.01 | [API](https://api.osv.dev/v1/query) | ✅ |

### 二维码图片 [→](./generated/directory.zh-CN.md#services-developer-tools-qr-codes)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [goQR QR Code API](./generated/services.md#goqr) | **100%**（2/2） | $0.0068 | [API](https://api.qrserver.com/v1/create-qr-code/) | ✅ |
| [QuickChart](./generated/services.md#quickchart) | **100%**（2/2） | $0.0083 | [API](https://quickchart.io/qr) | ✅ |

<a id="results-payments-billing"></a>

## 支付与计费

### 收款 [→](./generated/directory.zh-CN.md#services-payments-billing-accept-payments)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [Paddle](./generated/services.md#paddle) | **0%**（0/1） | $1.20 | [API](https://developer.paddle.com/sdks/sandbox/) | ❌ |
| [paas.build](./generated/services.md#paas-build) | 环境无效 | — | [API](https://paas.build/openapi.json) | ❌ |

<a id="results-communication"></a>

## 通信

### 邮箱 [→](./generated/directory.zh-CN.md#services-communication-mailboxes)

| 服务&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 通过率&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 平均费用&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 方式&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;免注册&nbsp;&nbsp; |
| :--- | ---: | ---: | :--- | :---: |
| [Mail.tm](./generated/services.md#mail-tm) | **100%**（3/3） | $0.14 | [API](https://api.mail.tm) | ✅ |
| [Guerrilla Mail](./generated/services.md#guerrilla-mail) | **50%**（1/2） | $0.32 | [API](https://www.guerrillamail.com/GuerrillaMailAPI.html) | ✅ |
| [AgentMail](./generated/services.md#agentmail) | **0%**（0/1） | $0.03 | [API](https://api.agentmail.to/v0/) | ✅ |

## 怎么测的

每次试跑都是全新会话和隔离容器，被测 Agent 只拿到用户任务和服务入口，看不到答案或其他服务的结果；另起一个会话按事先冻结的标准验收。用量取自运行器抓包，证据带哈希，可复查、可复跑。样本还少，结果是观察，不是长期可靠性的证明。 [方法](./AGENTS.md)

## 最新发现

- **网页抽取（GOV.UK 假日表）：Jina 3/3，Firecrawl 1/3。** Firecrawl 每次都成功取回页面且 HTML 正确，但其 Markdown 中年份标注位于表格之后，Agent 两次据此取到了错误年份的表。 [证据](./data/experiments/evaluations/afs-20261010-johor40-web-extraction-firecrawl-uk-holidays-r3.json)
- **测试地点会改变结论。** Jina Reader 在国内服务器上因 DNS 污染无法访问，记为环境无效；换到海外服务器后接入与两项抽取任务全部完成。 [证据](./data/experiments/evaluations/jina-extraction-access-ds41-r2.json)
- **Grist 共享账本：MCP 3/3，REST 2/3。** REST 的失败一次中，服务端表格与公式已全部正确，但 Agent 在请求上限内没写出最终答复——服务能做到，交付没完成。 [证据](./data/experiments/evaluations/afs-20261010-johor40-grist-rest-shared-expenses-r1.json)

## 完整目录

所有收录的服务（包括还没测的），以及每个任务的原文、配置和逐次结果：

- [旅行](./generated/directory.zh-CN.md#services-travel) — 27 个服务，已实测 2
- [数据库](./generated/directory.zh-CN.md#services-databases) — 13 个服务，已实测 2
- [搜索与网页抓取](./generated/directory.zh-CN.md#services-search-scraping) — 12 个服务，已实测 3
- [地图与地理](./generated/directory.zh-CN.md#services-maps-geo) — 7 个服务，已实测 4
- [天气与日历](./generated/directory.zh-CN.md#services-weather-calendar) — 4 个服务，已实测 4
- [金融数据](./generated/directory.zh-CN.md#services-financial-data) — 34 个服务，已实测 8
- [学术与知识](./generated/directory.zh-CN.md#services-scholarly) — 3 个服务，已实测 2
- [办公与协作](./generated/directory.zh-CN.md#services-productivity-storage) — 13 个服务，已实测 3
- [AI 服务](./generated/directory.zh-CN.md#services-ai-models) — 25 个服务，已实测 0
- [Agent 基础设施与自动化](./generated/directory.zh-CN.md#services-agent-tooling) — 5 个服务，已实测 0
- [开发工具](./generated/directory.zh-CN.md#services-developer-tools) — 10 个服务，已实测 4
- [云计算与托管](./generated/directory.zh-CN.md#services-cloud-hosting) — 11 个服务，已实测 0
- [支付与计费](./generated/directory.zh-CN.md#services-payments-billing) — 19 个服务，已实测 1
- [通信](./generated/directory.zh-CN.md#services-communication) — 23 个服务，已实测 3
- [电商](./generated/directory.zh-CN.md#services-commerce-marketing) — 1 个服务，已实测 0

想测某个服务或任务？欢迎[提 Issue](https://github.com/Olorinm/agent-friendly-services/issues)。

## 给 Agent 的入口

[查询指引](./llms.txt) · [服务 JSON](./generated/catalog.json) · [实测 JSON](./generated/evaluations.json) · [MCP 配置](./mcp/README.md)

## 方法与贡献

[核心理念](./AGENTS.md) · [收录标准](./docs/catalog-standard.zh-CN.md) · [机票阶段结论](./docs/flights.zh-CN.md) · [任务设计](./data/experiments/tasks/AGENTS.md) · [执行与验收](./data/experiments/AGENTS.md) · [全部实测与证据](./generated/evaluations.md) · [参与贡献](./docs/contributing.md)

代码：[MIT](./LICENSE) · 数据：[CC BY 4.0](./LICENSE-DATA)
