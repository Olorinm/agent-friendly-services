The access phase already created a project. Let me verify credentials freshness and set up a Postgres client.
Fresh process confirmed persistence. Now let me verify project status/quota via the API for the expiry details.
已完成。远程库为接入阶段新建的独立空库（项目 `[SERVICE_SECRET]`，验证时非系统表为空）。写入进程先插 3 条、再把 id=2 改为 done（1 行受影响）后退出；随后全新进程重连读取。

**按 id 排列的全部待办**
| id | title | done |
|----|-------|------|
| 1 | Buy milk | false |
| 2 | Read book | true |
| 3 | Walk dog | true |

**未完成待办（done=false）**：id=1 Buy milk

**总数 3，完成数 2，未完成 1**

**免费 / 到期限制（Neon Claimable 未认领项目）**
- 这是匿名「可认领」免费项目，无需绑卡、无付费：72 小时未认领即到期删除，到期时间 **2026-10-11T12:36:21Z**（北京时间 10-11 20:36）。
- 额度上限：100 MB 存储、1 GB 传输；到期后数据不可恢复。
- 可生成认领码把项目转入你自己的 Neon 账号；认领码本身 15 分钟内有效（可重发），认领后由你的账号套餐决定长期保留与额度。
- 资料位置：连接配置/项目标识 `service-config.json`，私密凭据在 `/home/node/service-tools/credentials.json`（未在答复中输出任何秘密）。

本轮业务脚本与结果（`write_todos.js`、`read_todos.js`、`db_check.js`、`read_result.txt`）均只保存在本题工作目录。