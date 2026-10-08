已接通并验证。

- 服务：Alpha Vantage，入口 `https://www.alphavantage.co/query`（GET，`apikey` 查询参数）。
- 实测通过：`GLOBAL_QUOTE`（IBM、MSFT）与 `TIME_SERIES_DAILY`（IBM）均返回 2026-10-07 行情，共 3 次请求，在免费额度内。
- 配置已存：`/home/node/service-tools/service-config.json`（含 endpoint、认证方式、已测函数；Key 只存放于此私有目录，未输出）。
- 复用脚本：`[WORKSPACE]/av_query.py`，用法 `python3 av_query.py GLOBAL_QUOTE symbol=IBM`。

注意：免费 Key 限 25 次/日，只能用免费端点。无阻碍。