公开证据节选；独立核验原文件 SHA256：92787ae19b0080873ec14f7a836c5ba34df02cd39645b73463e2547c3d8cc163。原始材料私有保存，以下编辑不改验收结论。

# 验收核验摘要（公开，已脱敏）

来源：本次执行记录 execution/ 下原始工具记录与采集副本；本文件仅摘录必要业务字段，已删除项目标识、主机名与全部密钥。

## 1. 同一远程 Neon Claimable Postgres 库

- 写入程序 execution/artifacts/write_todos.js 与独立读取程序 execution/artifacts/read_todos.js 均使用同一私有 `credentials.json` 中的 `database_url` 建立 `pg` 连接；该文件在两次调用之间未变。
- 通过 claimable API `GET /v1/projects/{id}/credentials` 实际返回：同一 `project_id`、同一 `branch_id`、`expires_at: 2026-10-11T12:36:21.796Z`、`has_database_url: true`（资源标识已脱敏）。
- 写入前 execution/artifacts/db_check.js 实际输出 `non-system tables: []`，确认复用库为空。

## 2. 写入进程（独立 Node 进程，运行后结束）

实际输出：
```
inserted 3 rows
updated id=2 rows affected: 1
state after write: [{"id":1,"title":"Buy milk","done":false},{"id":2,"title":"Read book","done":true},{"id":3,"title":"Walk dog","done":true}]
```

## 3. 全新进程重连读取（另一次独立 shell 调用 / 另一 Node 进程）

实际输出（同 execution/artifacts/read_result.txt）：
```
ALL (by id): [{"id":1,"title":"Buy milk","done":false},{"id":2,"title":"Read book","done":true},{"id":3,"title":"Walk dog","done":true}]
OPEN (done=false, by id): [{"id":1,"title":"Buy milk","done":false}]
COUNTS: {"total":3,"completed":2}
```

## 4. 到期 / 额度

- 官方文档 https://neon.com/docs/reference/claimable-neon（2026-10-08 本次获取）：未认领项目 72 小时到期、100 MB 存储 / 1 GB 传输上限、认领码 15 分钟有效。
- 本次 API 返回 `expires_at` 与创建时间相差 72 小时，与上述一致；执行者答复明确说明到期，未声称永久。
