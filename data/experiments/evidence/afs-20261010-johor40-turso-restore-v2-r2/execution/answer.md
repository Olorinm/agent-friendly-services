演练完成。成果在题目目录：

- **备份**：`source-backup.sql`（可留存逻辑备份，含两表结构与全部记录，含 NULL/空串区分）
- **恢复方法**：执行备份内 `CREATE TABLE` 后按 `lists→todos` 顺序 `INSERT`；`restore.py` 可经 `/v2/pipeline` 重现
- **新库**：`[SERVICE_SECRET]`（db_id `[SERVICE_SECRET]`，组 `[SERVICE_SECRET]`，区 `[SERVICE_SECRET]`）
- **行数**：lists 2 / todos 5（源库同）
- **核对**：结构、外键、逐行数据完全一致；`id=103` note 为空串、`101/105` 为 NULL，区别保留；源库全程只读未变
- **限制**：Starter `$0`、无超额，账户共享 100 库/5GB/500m 读行/10m 写行月额度；源读 token 6h 到期，新库自动到期官方未明确

详见 `delivery.md`，核对原始响应在 `target-verify.json`。共 7 次服务操作，未超上限。