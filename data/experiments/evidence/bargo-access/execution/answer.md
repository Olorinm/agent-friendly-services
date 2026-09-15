数据来源：[Bargo Congress Trades API](https://www.bargo.ai/free-apis/congress)。本页仅展示核验摘要。

文档确认：该服务读端点免 Key（限流 keyless 30 请求/100 行每天），REST 调用正确。现在实际验证各端点：
curl 在此容器崩溃（段错误），改用 Python 调用：
服务连通正常。继续验证数据端点（trades / 单ticker / members）：
全部端点验证通过。保存持久配置并留档验证脚本：
接入完成，服务可用。

**接入结果（bargo-congress，美国国会 STOCK Act 股票交易数据）**
- 指定方式：REST API 直接 HTTP 调用，`https://www.bargo.ai/free-apis/congress/v1`，读端点免 Key（未提供账号，未注册，符合授权范围）
- 实测通过 5 个端点（均 HTTP 200）：`/health`、`/stats`、`/trades`、`/trades/NVDA`、`/members`，返回真实披露数据（50,279 笔交易，最新披露 2026-09-14，与官方页一致）

**需要注意的环境问题**
- 本容器 curl 存在段错误（SIGSEGV），调用请用 Python urllib/requests 或 Node fetch（已写入配置）

**已保存配置**
- `/home/node/service-tools/service-config.json`：base URL、端点、响应字段、限额（keyless 30 请求/100 行每天，含 X-RateLimit 头）、3 个月数据窗口、署名与不得再分发条款、MCP 需 Key 说明
- 验证脚本：`[WORKSPACE]/verify-access.py`（5/5 PASS，当日剩余配额 22 请求/89 行）
- 无额外依赖需安装（Python 标准库即可），`installed-tools/` 已建好备用