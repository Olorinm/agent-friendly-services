I have the docs. Now let me set up the config and a small client.
Query succeeded. Now let me add a conservative default TTL (server sent no cache headers) and verify cache reuse without a second network call.
接入完成，真实查询成功。

## 接入步骤（全部自助完成，无需账号）
1. 阅读官方文档 https://open-meteo.com/en/docs，确认入口 `https://api.open-meteo.com/v1/forecast` 属非商业免费公共 Forecast API，**无需注册、无需 API Key、无支付方式**。
2. 在持久目录写入通用连接/客户端标识配置：`/home/node/service-tools/service-config.json`（base_url、无鉴权、默认单位/时区、User-Agent、署名与非商业许可、缓存与请求上限）。不含任何秘密（本服务本就无密钥）。
3. 在本题工作目录编写轻量客户端 `openmeteo_client.py`，读取上述配置，带 `User-Agent: agent-friendly-services/20261008 (+https://github.com/Olorinm/agent-friendly-services)` 发起请求，并把响应与响应头按 URL 缓存到 `./cache`，有效期内容直接复用、不发新请求、不加 cache-busting 参数。
4. 执行一次真实查询并校验：再用同参数运行命中缓存（`[CACHE HIT] ... default TTL 600s`），与首次响应逐字节一致，未产生第二次网络读取。本会话天气 API 读取共 **1 次**（上限 10）。

## 查询结果（公开地点：北京，39.9042, 116.4074）
观测/预报时区 `Asia/Shanghai (GMT+8)`，数据源 Open-Meteo。

当前（2026-10-08T22:45，15 分钟时段）：
- 气温 20.1 °C，体感 21.0 °C，相对湿度 66 %
- 降水 0.00 mm，天气码 0（晴）
- 风速 1.0 km/h，风向 211°

逐日（单位见括号）：
| 日期 | 最高/最低温(°C) | 降水(mm) | 降水概率(%) | 天气码 |
|---|---|---|---|---|
| 2026-10-08 | 26.0 / 13.0 | 0.00 | 0 | 0 |
| 2026-10-09 | 26.3 / 14.4 | 0.00 | 0 | 3 |
| 2026-10-10 | 27.5 / 15.8 | 0.00 | 0 | 3 |
| 2026-10-11 | 26.0 / 15.9 | 0.00 | 0 | 3 |
| 2026-10-12 | 23.9 / 17.6 | 2.00 | 31 | 53 |
| 2026-10-13 | 19.8 / 14.6 | 0.00 | 6 | 1 |
| 2026-10-14 | 20.9 / 10.0 | 0.00 | 0 | 3 |

## 产物位置
- 持久配置：`/home/node/service-tools/service-config.json`
- 本次客户端/响应/缓存：`[WORKSPACE]/openmeteo_client.py`、`last_response.json`、`last_response.meta.json`、`cache/`

## 实际阻碍
- 无鉴权阻碍：无需注册、无额度密钥、无人工介入或额外申请。
- 唯一注意点：`/v1/forecast` 响应未返回 `Cache-Control`/`Expires`（见 `last_response.meta.json`），无官方显式有效期。为遵守“有效响应复用、不重复请求”，客户端在无缓存头时采用保守默认 TTL 600 秒；如服务后续给出缓存头会自动优先采用。观测时间随请求实时变化，缓存仅用于短时去重。

数据署名：Weather data by Open-Meteo.com（CC BY 4.0，非商业用途）。