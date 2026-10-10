官方文档已确认。现在实测一次基础查询（CSV 格式），带署名 User-Agent。
核心数据接口可用。再验证一个宏观指标数据集和元数据接口。
EXR、ICP 两个宏观数据集均返回 200。再确认元数据接口与 SDMX-JSON 内容协商。
requests 未安装（用标准库即可）。元数据接口 XML 返回 200。现在编写可复用查询脚本并保存配置。
脚本与配置就绪。现在端到端验证脚本（含缓存复用）。
已接通，可用指定方式查询。

**服务**：ECB Data Portal 官方 SDMX API，入口 `https://data-api.ecb.europa.eu/service/`，免账号/Key。

**实测结果（均为 HTTP 200，真实响应）**
- 数据接口 CSV：`data/EXR/M.USD.EUR.SP00.A?format=csvdata&lastNObservations=3` — 美元/欧元汇率
- 宏观指标：`data/ICP/M.U2.N.000000.4.ANR?format=csvdata` — 欧元区 HICP 年通胀（2025-12 = 1.9%）
- 内容协商：`Accept: application/json` 返回 SDMX-JSON（1.0.0-wd）
- 元数据：`dataflow/ECB?detail=allstubs` 返回 SDMX 结构 XML，共 105 个 dataflow
- 缓存复用已确认（二次请求命中本地缓存）
- 注：metadata 接口 406 表明仅支持 XML，不支持 JSON；`-wd/-cts` 是 ECB 支持的 SDMX-JSON 版本标识。

**交付物**
- 通用连接配置：`/home/node/service-tools/service-config.json`（base_url、端点、格式、参数、限流、署名、已验证查询）
- 查询脚本：`ecb_query.py`（标准库实现，无额外依赖；含 2 秒限流、本地缓存、`agent-friendly-services/20261010` User-Agent），原始响应存 `responses/`、缓存存 `cache/`

**用法**
```
python3 ecb_query.py data EXR/M.USD.EUR.SP00.A --format csvdata --lastNObservations 3
python3 ecb_query.py metadata dataflow/ECB --out responses/dataflows.xml
```

**合规**：单线程、请求间隔 ≥2 秒、重复请求走缓存；署名与修改说明已写入配置。无阻碍，未使用账号、付费或邮箱。数据版权归 European Central Bank (ECB Data Portal)。