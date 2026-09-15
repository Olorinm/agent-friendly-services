任务明确：接入 ECB 数据服务（data-api.ecb.europa.eu），验证能通过指定 REST API 查询数据，并保存配置。先看环境和官方文档。
文档确认：入口为 `https://data-api.ecb.europa.eu/service/`，数据查询路径 `/service/data/{dataflow}/{seriesKey}`，公开读取无需认证。现在实际调用验证。
两次调用均返回 HTTP 200。第二条的 curl 23 错误可能只是 `head` 提前截断管道，确认一下 XML 文件是否完整写入，并再测一个其他数据集和带过滤条件的查询。
CSV 查询、通配符+多序列+dataonly 都正常。XML 文件没写出来（可能 /tmp/opencode 不存在），换个位置重试并测试数据流发现接口。
XML 查询成功（2009 年 5 月 4 条观测值）。之前 /tmp/opencode 写入失败是因为该目录属 root 无写权限。ICP 调用遇到 HTTP2 帧错误，换 HTTP/1.1 重试确认。
ICP 404 是我猜测的序列键不存在（服务正确返回了结构化错误），换成真实 HICP 键重试，并查看 XML 结构。
HICP 通胀数据也正常返回。快速核对 XML 日期过滤是否生效，然后把连接配置保存到持久目录。
奇怪：有 4 个 Series 且没匹配到 TIME_PERIOD。直接查看 XML 内容确认。
验证全部通过：日期过滤生效（仅返回 2009-05，值 1.365045），XML 中 `grep -c` 的 4 是 `generic:SeriesKey` 重复匹配所致，实际只有 1 个序列。现在保存持久化连接配置。
校验 JSON 配置有效性：
接入完成，服务可用。

**接入结果**
- 服务：ECB Data Portal REST API（SDMX 2.1），入口 `https://data-api.ecb.europa.eu/service/`，公开免费读取，**无需注册、无需 API Key**，因此未创建任何账号。
- 实测调用（均 HTTP 200）：
  - `EXR/D.USD.EUR.SP00.A`（美元/欧元参考汇率，CSV）：最新值 2026-09-14 = 1.1551
  - `EXR/M.USD.EUR.SP00.A`（XML，`startPeriod/endPeriod=2009-05`）：日期过滤生效，仅返回 2009-05 = 1.365045
  - `EXR/D.GBP+JPY.EUR.SP00.A`（通配多序列 + `detail=dataonly`）：GBP 0.85598、JPY 178.52
  - `ICP/M.U2.N.000000.4.ANR`（欧元区 HICP 通胀，CSV）：2025-12 年率 1.9%
  - 不存在的序列键正确返回结构化 404 JSON 错误，便于排查
- 无外部依赖：系统 curl 即可，未额外安装库。

**保存的配置**
- 持久配置：`/home/node/service-tools/service-config.json`（含 base_url、数据查询路径、常用参数 format/startPeriod/lastNObservations/detail、序列键语法、已验证调用清单、HTTP/2 偶发帧错误时降级 `--http1.1` 的提示）。JSON 校验通过。

**无阻碍**：未遇到验证码、限流或权限问题，全程只读，未付款、未写远端数据。