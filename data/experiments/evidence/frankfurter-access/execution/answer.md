Frankfurter 是免 Key 的公开汇率 API，指定入口为 `https://api.frankfurter.dev/v2/`。现在实测核心查询接口：
最新汇率、单对汇率、历史日期均返回 200。再验证时间序列与货币列表：
`group=day` 无效（文档只支持 week/month），`format` 参数不存在（NDJSON 只靠 Accept 头）。修正后复测：
全部接口验证通过。保存连接配置到持久目录：
已接通，可用指定方式正常查询。

**结论**
- 服务 frankfurter 通过指定 REST 入口 `https://api.frankfurter.dev/v2/` 实测可用：最新汇率（USD→EUR/GBP/JPY/CNY）、单对 `rate/eur/usd`（1.1573）、历史（1999-01-04）、时序 + 周降采样、NDJSON 流、货币列表均返回 200；无效货币 404、未知参数/无效 group 422，错误处理正常。
- 无注册/Key 要求，未创建账号，未付费；全程仅公开读取。

**踩坑点（已写入配置）**
- `group` 仅支持 `week`/`month`，无 `day`；NDJSON 只靠 `Accept: application/x-ndjson`，没有 `format` 参数；无转换端点，需自行乘算汇率。

**产物**
- 持久配置：`/home/node/service-tools/service-config.json`（端点清单、参数约定、错误码、验证结果，JSON 已校验）
- 验证记录：`[WORKSPACE]/results/access-verification.md`

无阻塞项，后续任务可直接用该配置调用。