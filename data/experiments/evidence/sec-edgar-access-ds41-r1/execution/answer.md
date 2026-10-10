Both SEC endpoints work. Now let me verify the remaining core endpoints and then save the config.
All core endpoints work. Saving persistent connection config and a reusable client.
已接通。指定服务是 SEC EDGAR（`https://data.sec.gov`，REST），仅需声明 User-Agent（client_name + contact），无需 Key、无需注册。

已实测通过的查询（真实响应）：
- `submissions/CIK0000320193.json` → 200，Apple Inc.，ticker `AAPL`
- `api/xbrl/companyconcept/.../us-gaap/Revenues.json` → 200，含 11 期营收数据
- `api/xbrl/companyfacts/CIK0000320193.json` → 200，taxonomy `dei`+`us-gaap`
- `api/xbrl/frames/us-gaap/Revenues/USD/CY2023.json` → 200，2678 家公司

注意点：响应为 gzip，需解压；遵守 ≤10 请求/秒限流。

已保存配置：
- 持久连接配置：`/home/node/service-tools/service-config.json`（含 base_url、默认头、四类端点、限流说明；User-Agent 属连接必要信息，存于该私有位置，未打印）
- 可复用客户端脚本：`[WORKSPACE]/sec_edgar_client.py`（`python3 sec_edgar_client.py 320193` 已跑通）

未完成/说明：`ENVIRONMENT.md` 提到 Alpha Vantage 免费 Key，但 `credentials.json` 中并不存在该 Key（仅有 SEC 的 client_name/contact）；本轮指定入口为 `data.sec.gov`，故按 SEC 完成接入，未使用也未创建其他账号。