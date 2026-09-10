# 独立测试环境

一批测试中，每个**服务 × 调用方式**使用一个容器。第一项接入任务负责必要的安装、认证和基础调用；后续业务任务留在同一容器，保留安装与登录状态，逐题启动新 Agent 会话。全部结束后归档、销毁容器，不为每道题重建环境。

```sh
docker --context <context> build -t afs-trial-base:local scripts/sandbox
python3 scripts/sandbox/trial-container.py --context <context> create afs-example-cli --run-id access --input <access-input>
# 执行器在返回的 workspace 中启动接入会话；结束后采集该会话日志。
python3 scripts/sandbox/trial-container.py --context <context> next-task afs-example-cli --run-id task-001 --input <task-input> --session-record <access-session-record> --output <new-private-access-archive>
# 执行器在返回的新 workspace 中启动全新业务会话。更多题重复 next-task。
python3 scripts/sandbox/trial-container.py --context <context> export afs-example-cli --output <new-private-final-archive>
# 单独确认最后一次执行器日志已归档，再销毁。
python3 scripts/sandbox/trial-container.py --context <context> destroy afs-example-cli
```

`create` 把首题复制到 `/workspace/tasks/<run-id>`。`next-task` 先导出上一题工作目录与已采集会话，再移除上一题目录、放入新题，返回相同容器 ID 和新工作目录。导出目标必须是新目录，运行 ID 不重复；旧式无生命周期记录的容器不能自动切题。安装目录统一用 `/home/node/service-tools`，必要登录与 MCP 配置保存在环境说明指定的持久位置，不放在会被清理的题目目录。

MCP 配置若需重启执行器或换会话才能加载，由总控在原容器完成，仍计入当前接入任务；记录相关会话并累计接入用量，实际工具调用通过后才进入业务题。

总控负责停止上次执行及其遗留进程、采集日志、核对持久目录只保留工具和必要配置，随后切题并启动新会话。执行器适配负责按会话 ID 采集、归档并清理可被下一题读取的历史会话和临时解题文件；本脚本不管理 Agent 数据库，复制日志也不等于证明模型输入已完整留底。无法确认隔离时不得继续派题。同一容器内任务串行；并发发生在不同服务或调用方式之间。写入型任务还需按冻结要求恢复远端测试数据，换工作目录不能重置服务端状态。

输入只放执行角色 `AGENTS.md`、任务材料和必要资源，不放仓库整体指令、其他任务答案或验收材料。文件复制进容器，不挂载个人目录或 Docker socket。容器使用普通用户、资源上限和独立可写层；新工作目录本身不是对容器内其余文件的访问隔离。

执行器必须实际连接到容器，命令与文件工具都在那里运行，不能仅在 prompt 中要求使用容器。基础镜像可以缓存通用工具及固定版本 Agent；服务专用工具在接入任务安装并计量，认证在运行时提供。记录镜像 ID、执行器版本、会话 ID 和实际 cwd。跨批次重新测试接入、切换调用方式，或环境已损坏时另建容器并记录原因。

`export` 导出工作目录和容器配置，不自动采集各执行器 session，也不备份整个安装目录。归档可能含凭据，保持私有，公开副本另行脱敏。删除容器不撤销服务端账号或资源。
