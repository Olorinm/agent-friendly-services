I've read the task and environment. Let me set up a todo list and verify the provided workspace via the Grist REST API.
Workspace [PRIVATE_WORKSPACE_ID] confirmed empty (`docs: []`), access `owners`. Now creating the dedicated empty container (document).
Container created (`[PRIVATE_DOC_ID]`). Now reading back its metadata to confirm the same remote resource.
Readback confirms the same remote resource (doc `[PRIVATE_DOC_ID]` in workspace `[PRIVATE_WORKSPACE_ID]`). Now saving the connection config to the persistent service-tools location (secrets stay in the existing private credentials file).
已通过指定 REST 入口完成接入。

**容器链接**
- 文档（本轮空容器，后续任务表建于此）：[PRIVATE_DOC_URL]
- 所属父工作区：`docs-218066` / workspace id `[PRIVATE_WORKSPACE_ID]`，名称同为 `[SERVICE_SECRET]`
- 读取回传确认同一远端资源：doc id `[PRIVATE_DOC_ID]`、urlId `[PRIVATE_DOC_URL_ID]`，`workspace.id=[PRIVATE_WORKSPACE_ID]`，`access=owners`。创建时工作区 `docs:[]`，文档仅含 Grist 新建空文档自带的默认空表 `Table1`（无字段/记录，未预建任何业务内容）。

**接入步骤（全部自助完成，共 4 次服务操作）**
1. 读取私有凭据 `/home/node/service-tools/credentials.json` 中的 API key / workspace id。
2. `GET /api/workspaces/[PRIVATE_WORKSPACE_ID]` 校验授权，确认父工作区为空。
3. `POST /api/workspaces/[PRIVATE_WORKSPACE_ID]/docs` body `{"name":"[SERVICE_SECRET]"}` → 返回 doc id。
4. `GET /api/docs/{id}` 与 `/tables` 真实回读，确认元数据一致。
5. 保存连接配置（未安装任何依赖，REST 调用用 Python 标准库 urllib，无需 MCP/第三方客户端）。

**配置位置**
- 通用连接配置：`/home/node/service-tools/service-config.json`（含 base URL、org/workspace/container 标识与文档链接，模式 600）。
- 密钥仍只在私有文件 `/home/node/service-tools/credentials.json`，配置文件仅引用其路径，未复制秘密。

**人工门槛**
- 账号与 API key 由总控提供，非我注册；本轮无需注册、验证码、支付或绑卡，未遇任何人工阻碍。
- 分享/邀请被限制（免费版工作区可分享数=0），本轮也未授权分享，故均未操作。

**已知免费限制（从账号读回）**
- 套餐 `personalFree`，`paid=false`，`inGoodStanding=true`；组织级 API 额度 3000 次/月（REST 与 MCP 共用，剩余量未提供，记未知）。
- 单文档上限：5000 行、约 10 MB 数据、附件 1 GB；每文档分享 2、每工作区分享 0。
- 快照窗口 30 天，超限宽限 14 天，Assistant 调用 100 次。

未做：未录入任何会议/账本/示例字段，未访问其他工作区或旧文档，未付款或分享。