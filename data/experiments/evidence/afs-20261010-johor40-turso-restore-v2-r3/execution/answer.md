演练完成。源库全程只读未改动，已在同一服务新建独立空库并实际恢复、重连核对。

**备份（可下载留存）**
- `backup/[SERVICE_SECRET]_20261010.sql`（逻辑备份：建表 DDL + 全部数据 INSERT，兼容 SQLite/libSQL）
- SHA-256：`4606f94ec460a9991f7e21f46b65e74b75e2e01de4041360e11c4c89ed4400cb`
- 恢复方法：`sqlite3 new.db < 该文件`，或在 `/v2/pipeline` 中按序执行；恢复说明见 `backup/README_restore.md`

**新库位置**
- 名称 `[SERVICE_SECRET]`，org `[SERVICE_SECRET]`，group `[SERVICE_SECRET]`（[SERVICE_SECRET]）
- db_id `[SERVICE_SECRET]`，恢复前业务表数实测为 0

**行数与核对**

| 表 | 源库 | 新库 |
|---|---|---|
| lists | 2 | 2 |
| todos | 5 | 5 |

- 结构 `target == source`（主键/外键/NOT NULL/DEFAULT 0 一致）
- 数据逐行一致；`note` 空串（id=103 `''`）与缺值（id=101/105 `NULL`）均正确保留
- `PRAGMA foreign_key_check` 源/目标均无违规；恢复后源库快照与恢复前一致（未变更）
- 另将备份导入本地 SQLite 复核，行数一致，证明可脱离原服务恢复

**免费/到期限制**：Starter 计划 $0、overages 关闭；账户月度额度 100 库 / 5GB / 500m 读行 / 10m 写行，本 cohort 最多新增 7 库、账户总计 8 库。该库明确到期时间本轮未给定（账户库自动到期未知），免费库长期闲置可能被暂停/归档。本轮新库与备份均保留待总控清理；目标库 token 仅存于 `work/target_token.txt`（未输出）。