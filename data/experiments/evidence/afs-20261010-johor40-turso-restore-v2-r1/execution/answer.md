I'll start by reading the task materials.
Source read complete. Now building the logical backup.
Backup ready. Now creating the empty target database via the Platform API.
Target created and its access token stored privately. Verifying the target is empty before restore.
Target confirmed empty. Restoring the backup into it.
Restore succeeded. Now reconnecting to the target to verify schema, rows, and constraints.
Target matches the backup exactly (including NULL vs `''`). Now confirming the source is unchanged.
All checks pass. Writing the delivery report and a restore helper.
演练完成。交付如下：

**备份（本地留存，可下载）** — `backup/`
- `backup.sql`（DDL+数据，标准 SQLite/libSQL 语法）sha256 `38695c35…a16203`
- `backup.json`（结构化）sha256 `db41010d…c976c`；`manifest.json`
- 含建表 DDL、全部记录；PK/FK/NOT NULL/DEFAULT 保留；`note` 的 `''` 与 `NULL` 分别保留。

**恢复方法** — `sqlite3 target.db < backup/backup.sql`，或本次实际用的 Turso `/v2/pipeline` 逐条恢复；可复现脚本 `tools/restore_target.py`，说明见 `backup/restore.sh`。

**新库位置** — `[SERVICE_SECRET]`，db_id `[SERVICE_SECRET]`，host `[SERVICE_SECRET]`，group `[SERVICE_SECRET]`。建库时业务表数=0（已核对为空白）。

**行数与核对** — lists 源 2/备份 2/新库 2；todos 源 5/备份 5/新库 5。重连新库核对：建表语句与源库逐字一致；记录逐字段一致，`typeof(note)` 确认 NULL 与 `''` 区别保留；`PRAGMA foreign_key_check` 无违规、`integrity_check`=ok。源库重读后 schema、2+5 行数据与完整性均未变。

**免费/到期限制** — Starter 计划 $0、`overages=false`，未绑卡/未超额；额度 100 库/5GB/500m 读行/10m 写行每月，本 cohort 最多 7 新库、账户总计 8。目标库单库自动到期时间总控未明确（未知项）；源读 token 6h 到期，目标 token 按 `never` 签发。凭据仅存 `/home/node/service-tools/`，未输出。完整报告：`DELIVERY.md`。