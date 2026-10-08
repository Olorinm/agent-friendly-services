公开证据节选；独立核验原文件 SHA256：7bb50a7997d62267dcda4d4f6963aa6e284524ecd322c078a1557f4e486ccc1b。原始材料私有保存，以下编辑不改验收结论。

# Alpha Vantage 接入核验摘要（脱敏）

来源：本次执行记录中实际工具调用的命令与响应（原始会话/日志为私有材料）。
时间：2026-10-08。入口：GET https://www.alphavantage.co/query ，认证参数 apikey（值已删除）。

## 实际数据响应核验范围

验收者已检查 3 次真实返回：GLOBAL_QUOTE IBM/MSFT 与 TIME_SERIES_DAILY IBM，均有业务数据及交易日期。公开证据仅保留调用类型、日期和结论；完整行情、交易量与历史序列留在私有原件。

## 保存的连接配置（键值，Key 已删除）

/home/node/service-tools/service-config.json：
- service = Alpha Vantage
- endpoint = https://www.alphavantage.co/query, method = GET
- auth.type = api_key_query_param, auth.param = apikey, auth.plan = free, auth.limits = 25 requests/day total
- verified.status = ok, functions_tested = [GLOBAL_QUOTE, TIME_SERIES_DAILY], last_trading_day_returned = 2026-10-07
- 复用脚本 execution/artifacts/av_query.py 从该配置读取 endpoint/api_key 并附带 User-Agent 调用

## 免费依据

Alpha Vantage 官方 Premium 页（https://www.alphavantage.co/premium/）：多数端点免费，标准免费额度 25 requests/day；超出或需 premium 函数才订阅。本次 3 次均调用免费端点（GLOBAL_QUOTE、TIME_SERIES_DAILY compact），在额度内。
