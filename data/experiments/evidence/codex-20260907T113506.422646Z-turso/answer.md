已完成。按 [Turso 官方 API](https://docs.turso.tech/api-reference/introduction) 创建了独立远程数据库 `[SERVICE_SECRET]`，数据已保存。

写入进程 **45788** 提交并退出后，全新进程 **45799** 使用只读连接读回：

| id | title | done |
|---|---|---|
| 1 | Buy milk | false |
| 2 | Read book | true |
| 3 | Walk dog | true |

未完成项仅 **id=1**；**总数 3，完成数 2**，标题全部保持不变。

证据已保存：

- [完整报告、请求和 SQL 索引](evidence/README.md)
- [写入真实响应](evidence/09-write.response.json)
- [新进程读取真实响应](evidence/10-read-new-process.response.json)
- [进程退出及独立启动证据](evidence/process-separation.json)
- [凭据隔离及响应哈希检查](evidence/audit.json)

账户实际为零元套餐，超额付费关闭；免费额度包括 **100 库、5GB、每月 5 亿行读／1000 万行写**。[官方定价](https://turso.tech/pricing)

数据库未设置固定删除期限，但免费库**闲置 10 天会归档**。[官方限制](https://docs.turso.tech/api-reference/groups/unarchive) 本次写入／只读令牌分别于北京时间 **2026-09-08 19:39:16／19:39:18** 到期。真实凭据仅保存在当前目录的私有文件中，未进入证据或答案。