Database verified, write and fresh-read both succeeded. Let me record non-secret config and the result artifact.
已完成。使用接入阶段新建的独立空库 `[SERVICE_SECRET]`（远程 libSQL，aws-us-east-1），业务表 `todos` 写入 3 条并把 id=2 改为 `done=true`；写入程序退出后由全新程序重连读取，结果一致。

**按 id 排列的全部待办**
| id | title | done |
|----|-------|------|
| 1 | Buy milk | false |
| 2 | Read book | **true**（已修改） |
| 3 | Walk dog | true |

**未完成待办**：`[{id:1, title:"Buy milk"}]`
**总数**：3　**完成数**：2　**未完成**：1

产物（均在本工作目录）：
- `write_todos.py` / `read_todos.py` — 两个独立程序，各自用官方 SQL HTTP 接口（`/v2/pipeline`）连接
- `result.json` — 本次读取结果
- 私有凭据 `/home/node/service-tools/credentials.json`（含 token、URL、密码，未在答复中输出）；非秘密配置 `/home/node/service-tools/service-config.json`

**免费与到期限制**（账号套餐 `starter`，`overages=false`，即不会自动超额计费）：
- 免费额度（每月）：读 5 亿行、写 1000 万行、同步 3 GB、存储 5 GB、数据库 100 个、节点 3 个、group 1 个；价格为 0。
- 超限：未启用 overages，达到上限会被限制/阻断请求，不会产生费用。
- 到期：本次签发的数据库 Token 为 **full-access，7 天有效，2026-10-15 12:37 UTC 到期**，到期后需重新签发；数据库本身只要账号存在即保留。
- 归档：免费套餐数据库若 **10 天无活动会被自动归档**（可通过 API `POST .../groups/{group}/unarchive` 恢复），归档不删除数据。

未做：未新建其它库、未访问既有用户库、未开启付费或超额。