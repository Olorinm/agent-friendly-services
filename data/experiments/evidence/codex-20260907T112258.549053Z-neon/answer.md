已完成，耗时约 420 秒。通过 [neon.new](https://neon.new/) 的免账号入口创建独立远程数据库，未使用已有项目。

写入进程 **28718** 退出后，新进程 **28719** 建立新 TLS 连接，读回结果：

| id | title | done |
|---|---|---|
| 1 | Buy milk | false |
| 2 | Read book | true |
| 3 | Walk dog | true |

未完成项仅 **id=1**；总数 **3**，完成数 **2**，标题未变。

资源有效期 **72 小时**，实际到期时间为 **北京时间 2026-09-10 19:23:56**。凭据仅保存在工作目录私有文件中，权限为 `0600`。

证据文件：

- [完整索引、方案来源、请求与 SQL](evidence/README.md)
- [创建数据库的脱敏真实响应](evidence/02-create-database.json)
- [写入及更新的原始响应](evidence/10-write-response-body.json)
- [新进程读取的原始响应](evidence/11-read-response-body.json)
- [进程退出与独立启动证据](evidence/12-process-separation.json)

TLS、Neon 请求 ID、文件哈希和凭据脱敏核验均已保存至 `evidence/`。