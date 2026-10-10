公开证据节选；独立核验原文件 SHA256：1202a10db8abcb79b76740a66d5b7afa1f7a0a4bb192fd364fbad7a132a477d4。原始材料私有保存，以下编辑不改验收结论。

# 持久配置核验摘要（脱敏）

来源：本次执行工具记录（write 到 `/home/node/service-tools/service-config.json`，随后 JSON 校验通过），以及运行器采集的 `execution/retained-files.json`。

运行器 retained-files.json 记录保留文件：`["service-config.json"]`，表明该文件位于持久目录 `/home/node/service-tools/` 并被采集为跨会话保留项。

写入的配置内容（无任何密钥/口令，`auth: none`）：

```json
{
  "service": "met-norway",
  "product": "locationforecast-2.0-compact",
  "base_url": "https://api.met.no/weatherapi/locationforecast/2.0/compact",
  "method": "GET",
  "auth": "none",
  "user_agent": "agent-friendly-services/20261008 (+https://github.com/Olorinm/agent-friendly-services)",
  "required_headers": { "Accept-Encoding": "gzip, deflate" },
  "query_params": {
    "lat": "latitude, max 4 decimals",
    "lon": "longitude, max 4 decimals",
    "altitude": "optional, meters"
  },
  "caching": {
    "reuse_until_header": "Expires",
    "conditional_header": "If-Modified-Since",
    "conditional_value_source": "Last-Modified",
    "rule": "do not HEAD+GET; reuse response while valid"
  },
  "license": "CC BY 4.0 - attribution to Norwegian Meteorological Institute (MET Norway)",
  "docs": "https://docs.api.met.no/doc/GettingStarted.html"
}
```

不含 API Key、Cookie、账号或支付信息，可被新会话直接复用。

# MET Norway 免费规则与本次适用性核验

## 免费规则来源（官方）
- 官方 Licensing and Data Policy：https://docs.api.met.no/doc/License.html
  > "Unless specified otherwise, all data and products are licensed under the Norwegian Licence for Open Government Data (NLOD) 2.0 and Creative Commons 4.0 BY International licences."
  即数据以 NLOD 2.0 / CC BY 4.0 开放许可发布，无需购买。
- 官方 Terms of Service：https://docs.api.met.no/doc/TermsOfService.html
  > "All open data require attribution as specified in the CC BY 4.0 license"
  条款只要求 User-Agent 标识、缓存与署名，未列出任何收费、订阅或账号/密钥要求。

## 本次适用性观察
- 本次对指定入口 `https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.9139&lon=10.7522` 的请求为无 Key / 无账号 / 无支付方式的普通 GET。
- 响应 `execution/artifacts/forecast.headers.txt`：`HTTP/2 200`、`content-type: application/json`、`access-control-allow-origin: *`，返回真实预报数据。
- 全程无注册、无授权、无计费步骤；配置 `auth: none`。

结论：该服务为公开开放数据接口，本次使用落在免费范围内。


Weather data by [Norwegian Meteorological Institute (MET Norway)](https://www.met.no/en) — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Changes: selected fields, local-time conversion and table presentation for this task; no service endorsement.

本轮只检验指定服务预报查询与忠实交付，不验证未来真实天气是否命中，也不以两家数值相同为标准。两家可能共享上游预报。当前/未来气温均按服务提供的模型或预报值理解，不视为气象站实测观测。原始调用、回执与全部冻结字段/时区资料私有保留；公开只展示任务相关小表与核验摘要。单轮、同一出口IP，不是普遍可靠性或预测准确率排名。
