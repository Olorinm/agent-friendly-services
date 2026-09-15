服务费用（ecb-data / ECB Data Portal REST API）免费依据，验收者于 2026-09-15 查证：

规则来源：
1) ECB 官方免责与版权页 https://www.ecb.europa.eu/services/disclaimer/html/index.en.html：
   "users of this website may make free use of the information obtained directly from it"
   （条件：准确转载并注明 ECB 为来源；商业转载须告知可免费获取）。
2) API 官方文档 https://data.ecb.europa.eu/help/api/overview 与 /help/api/data-examples：
   SDMX 2.1 RESTful web service 公开提供统计数据的程序化访问；示例均为无鉴权 curl/wget 直接调用；
   站点注册仅用于保存收藏、个性化看板、订阅邮件通知等门户功能，不涉及数据 API 访问或付费。

本次适用观察：
- 执行回执与工具记录显示本次仅使用无鉴权 GET（无 Key、无 Authorization 头、无付款渠道，环境也未提供账户），
  请求返回 HTTP 200 与完整数据（review-packet/tools/0005.json，采集自执行真实会话）。
- 验收环境以相同无鉴权调用独立重放成功（见 evidence/independent-replay.txt），确认无需注册或 Key 即可读取。

结论：本次读取使用的公开免费入口，实付金额为 0。
