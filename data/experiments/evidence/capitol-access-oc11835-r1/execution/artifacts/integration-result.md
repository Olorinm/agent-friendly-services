# capitol-exposed 接入结果

日期：2026-10-08（UTC）

## 结论

接入成功。指定入口 `https://www.capitolexposed.com/api/v1` 免 Key 免费可用，REST/HTTP 直接调用已实测通过，连接配置已保存供后续任务使用。无未解决阻碍。

## 实测记录（全部真实响应，非文档示例）

| # | 调用 | 结果 |
|---|------|------|
| 1 | `GET /api/v1/stats`（curl） | 200，返回站点统计：member_count=539，trade_count=73251，alert_count=160，last_updated=2026-10-08 07:01 UTC |
| 2 | `GET /api/v1/members?per_page=2`（curl） | 200，返回 2 条成员记录，meta.total=1146 |
| 3 | `GET /api/v1/trades?per_page=3`（curl） | 200，返回 3 条 STOCK Act 交易记录（含 member_name、ticker/asset、transaction_date、amount 区间、source_url、parser_confidence） |
| 4 | `GET /api/v1/top-traders?limit=1`（urllib，默认 UA） | 403（Cloudflare error 1010，UA 被拦） |
| 5 | `GET /api/v1/top-traders?limit=1`（curl / 自定义 UA） | 200，返回 1 条记录（原始成员信息和数值仅私有留底） |

说明：第 4 次调用用于验证 403 归因，随后确认是 Cloudflare 拒绝 `python-urllib` 默认 UA（error 1010），与端点无关；换正常 UA 即恢复。数据返回量：members 2 + trades 3 + top-traders 1 = 6 条（其中 1 条为 UA 验证调用返回）；此后未再发起数据查询。

## 限流与配额（响应头实测）

- 列表类（/members、/trades 等）：60 次/分钟；实测响应头 `X-RateLimit-Limit: 60`。
- 搜索/合同线索：30 次/分钟；批量导出：每路由 5 次/60 分钟（免费窗口：trades 30 天、lobbying/votes 90 天、bills 仅当前国会）。
- 免费档无需认证，按 IP 限流；本轮未注册、未付款，符合授权范围。

## 使用的坑位与注意事项（来自官方文档，已写入配置）

- 响应为统一信封 `{api_version, status, data, meta, citation}`，snake_case。
- 2026-10-03 移除项：`min_score`/`min_conflict` 参数（传 400）、`/investigations`、`/members/{slug}/fara`、`/hearing-correlations`（410）、`type=cross_reference`（400）——不要调用。
- `parser_confidence<=0.7`、`parser_version` 含 "vision" 或 `source=senate_ocr` 的行是机器读取，使用前需核对原始申报文件。
- 署名要求："Public Records — Attribution Requested"，引用需注明 CapitolExposed 及各记录 source_url。

## 持久化位置

- 连接配置：`/home/node/service-tools/service-config.json`（base_url、认证方式、限流、UA 要求、已验证调用、API 注意事项）
- 后续调用辅助脚本（Python 标准库，零依赖）：`/home/node/service-tools/installed-tools/capitol_query.py`
  - 用法：`python3 capitol_query.py /trades "ticker=AAPL&per_page=5"`
  - 已实测通过该脚本走保存配置成功调用 `/top-traders?limit=1`
