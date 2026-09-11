# 执行、验收与结果回填

目的：把有来源的候选和真实用户任务变成可核对的结果，比较服务的可用性、接入门槛和开销。Pipeline 使用统一任务与结果，不绑定领域、服务、模型或执行器；具体运行环境负责启动会话和采集真实记录。

## 角色与边界

总控协调[发现服务](../candidates/AGENTS.md)、[任务设计](tasks/AGENTS.md)、[执行](../../scripts/roles/execution/AGENTS.md)和[独立验收](../../scripts/roles/grading/AGENTS.md)。角色的具体原则各维护一份。总控负责交接、资源授权、异常判断、复核与结果录入，各角色不负责启动自己。

一次执行对应一个独立验收会话。执行者只获得该次任务、材料、环境和执行角色指令；验收者只获得该次冻结要求、必要参考、执行记录及交付物，不混用其他运行的答案。历史记录保留实际验收方式，不改称独立盲评。

## 第一个任务：接入服务

每个服务先测试“接入服务”：按需注册、验证、授权、获取凭据或安装配置，通过指定 API、CLI、SDK 或 MCP 完成一次基础调用，确认可以开始使用。业务要求和授权资源在执行前明确；具体操作由执行 Agent 查官方资料决定，不提供预写服务调用代码。账号注册成功不等于接入完成。

- 无需注册时直接调用，并记录无需账号。已有账号时说明由谁、何时提供，不能声称本轮完成了自助注册。
- 接入结果与接入门槛分别记录。结果说明完成或受阻；门槛说明 Agent 自助、实际人工介入、特殊申请或资质要求及具体原因。这些条件可以同时存在，例如需人工提交企业申请。
- Token、费用、耗时与人工步骤由这项任务单独留底，不藏在业务测试前。未测量的历史准备保持未知，不补填零。
- 需要人工身份核验或特殊申请时保留实际进度与阻碍。后续依赖该账号的任务尚未执行，不能批量记为业务能力失败。
- 安装 MCP 后若执行器必须重启或换会话才能加载工具，由总控在同一容器内完成；仍属于同一次接入任务，关联全部会话并累计用量、耗时与人工步骤。配置文件写成不等于接入成功，必须有指定方式的实际调用证据。
- 同一账号可在授权范围内供后续任务使用；更换接入方式时仍需验证该方式的安装、认证和实际调用。已完成的注册不重复计费，也不冒充再次注册。

## 环境生命周期

一批测试按服务 × 调用方式创建容器，接入任务完成安装、认证和基础调用，后续业务任务在原容器中运行，不逐题重建或重复复制依赖。每次运行使用独立题目目录和全新会话，安装与认证保留，接入开销不重复计入每道业务题。

总控按顺序停止执行、归档产物与该会话日志、清理上题目录及其他临时解题文件，再启动下一题。执行器适配须处理自身历史会话留存，避免下一题读到旧答案；验收在另一个环境中进行。同一容器不并发执行多题，写入型任务的远端数据按冻结要求单独恢复。无法确认清理或环境损坏时暂停该路线，重建必须记录原因，不能把新环境冒充复用。具体环境操作见 [容器工具](../../scripts/sandbox/README.md)。

## 材料与资源交接

任务生成器从候选和任务表生成简短 prompt、`input.md`、`ENVIRONMENT.md` 和独立验收材料。脚本负责生成合成数据、工作目录和必要文件；真实账号、Key、授权或远端资源通过实际操作取得，不能以生成了文件代替已取得资源。

接入任务产出的凭据只交给明确依赖它的任务，以本地私有文件或运行环境支持的安全方式传递。后续会话可获得必要的账号、资源标识与登录配置，不继承上轮对话、解题脚本或评分内容。身份资料、验证邮箱等外部输入必须来自本轮授权，不能搜索本机其他账号；合成测试内容不能冒充真实身份或资质。

需要远端测试材料时，生成之后还要投递或创建并确认就绪。例如验证码题的三封合成邮件必须实际送达本轮邮箱，不能只在本地写出三段文本。准备未就绪属于材料或环境问题，不算被测服务业务任务失败。

## 从任务到结果

1. **确定批次。** 选择服务、入口、任务 ID 与版本、重复次数、执行器、模型、思考等级、工具、预算和并发条件。服务、任务和次数均来自批次输入，不写死在调度代码。只对条件一致的记录合并统计。
2. **冻结输入。** 为每次运行保存原始委托、附件、执行角色指令、授权资源、预算及哈希；评分要求与参考答案另存。材料变更升级版本，不能在执行中修改题目来适应某个服务。
3. **启动与留底。** 运行器以独立新会话执行该次委托，返回可查询的运行标识，采集实际状态、起止时间、配置、工具过程、答案、逐请求用量与整轮汇总。确认日志保留能力并持续归档模型实际输入；不能仅凭复制了 AGENTS.md 就宣称它实际生效。同机新目录不等于 OS 文件系统隔离。
4. **逐次验收。** 执行结束后生成该次验收任务。独立 Agent 核对冻结要求和真实服务证据，需要时自行构造授权范围内的核验请求；不能运行执行者的自评脚本代替验证，也不补做业务任务。输出 `assessment.json`，正常流程直接交脚本校验、录入，不固定再加一层 Agent 验收。发现异常时退回补充依据或记录未知；修正保留原始结论。
5. **录入与生成。** 运行记录和验收结论合成统一结果源，校验后生成结果表、目录、服务详情和机器入口。数值由记录计算，Agent 不手填 Token、模型费用或另写一份榜单。原始记录留本地，仅发布最少的脱敏证据。

总控应核对执行会话的实际工具列表，能禁用委派工具时禁用，不能只靠角色文本假设执行者不会调用子 Agent；出现越界调用时保留记录并交独立验收，不能直接纳入合格样本。

运行器应提供启动、状态查询、结果采集和停止能力；状态不明时先查实际会话，不能盲目重发。预算是可核对的执行限制，不能只在 prompt 写一个数字便视为已实现超时控制。不同任务可并发，但共享机器、网络和服务限流条件必须记录。

通用调度由 `scripts/pipeline.py` 实现；其命令适配协议已通过本地固定样本验证，实际执行器的远端隔离、完整日志、停止能力还须分别接入验证。不能把固定样本通过说成真实服务测评通过。

## 验收与费用

`assessment.json` 沿用现有结果录入字段：`status`、`reason`、`reviewer`、`checks`、`evidence`、`service_cost_usd`、`service_cost`、`human_interventions`。字段可以随需求迭代，判定必须能追溯到冻结任务和证据。

- `completed`：全部用户要求有证据满足；`not_completed`：实际执行未完成；`invalid_run`：运行环境或测试材料失效。说明原因来自服务、接入门槛、执行行为、材料还是环境，证据不足不能猜成功。
- 服务费用优先依据回执、账单和真实用量；确认免费标 `confirmed_free`，按用量和单价估算标 `estimated`，实际报告金额标 `reported`，缺依据标 `unknown`。来源与说明随结果保留，返回成功不能证明免费。
- 模型费用按冻结 LiteLLM 价表从逐请求输入、缓存读取/写入和输出计算，并与整轮用量核对。按单次请求的输入长度判断计价档位，不能拿累计输入代替。缓存输入若已包含在输入总数中不重复加；推理 Token 若已含在输出中不重复加。
- 用量不完整、计数不一致、缺价格或计价条件不明时保留未知及原因，不填零。标准 API 价估算不是订阅套餐的实际扣费。
- 接入任务、业务执行、独立验收的用量分别记录。每次有效试跑均值包含成功和失败，排除环境无效；缺项不能跳过后制造完整的低均值。

## 现有结果入口

`data/experiments/evaluations/` 保存结果源，`data/experiments/evidence/` 保存必要证据；`data/experiments/results/` 保存本地原始运行记录。执行器输出先转换为统一记录，再交给现有录入与生成工具；不能把某个执行器专有的日志格式直接冒充兼容。

```sh
python3 scripts/record-trial.py <结果目录> --review <结果目录>/assessment.json
npm run validate
npm run generate
```

`record-trial.py` 是统一录入入口：读取 `run.json` 与独立 `assessment.json`，所有服务费用经过 `service_cost.py`。历史 Codex 日志沿用原始提取；新执行器通过 `adapter-v1` 数值记录核对逐请求用量、总量与原始来源哈希。该核对不能代替对具体执行器转换代码的验证。新 pipeline 冻结价格表，页面按该次快照重算模型费；历史无快照记录保留原有计价行为。生成器从同一份结果源更新 `generated/evaluations.md`、目录、服务详情和 MCP 数据。价格快照通过 `npm run pricing:update` 更新；更新快照会影响费用估算，快照日期不冒充测试日期。

发布前检查私人信息、密钥、Cookie、用户目录和会话标识。凭据仅存私有位置，完整原始会话不进入公开证据；自动脱敏不能代替对公开副本的检查。历史观察保留，新运行追加；角色说明、脚本和输出格式服务于可核对的结论，不追求文档数量。

## 通用 pipeline 的使用

后续执行和验收优先使用服务器运行器。已实测的接入是 [OpenCode SSH 运行器](../../scripts/runners/opencode/README.md)，使用 GLM-5.3-Flash / high；通用 pipeline 仍通过适配协议支持其他执行器。服务器地址、SSH 身份、密钥、容器映射和本批资源配置由私有配置传入，不写进代码、角色指令或公开结果。运行器提供镜像构建、容器准备、派发、采集和停止命令；更换机器只需调整外部配置。具体服务方式与并发规模仍以实际验证为准。

各角色可以在不同机器工作，通过文件交接。候选与任务仍由对应 Agent 调研生成；pipeline 从已确定的候选、任务表开始，不用脚本替代需求研究。`prepare` 复用现有任务生成函数，分别冻结执行、验收材料和价表；`run` 自动推进执行、采集和独立验收；`record` 通过同一个校验入口录入、生成页面。

```sh
python3 scripts/pipeline.py prepare data/experiments/results/<run-id> --config <private-config.json>
python3 scripts/pipeline.py run data/experiments/results/<run-id>
python3 scripts/pipeline.py status data/experiments/results/<run-id>
python3 scripts/pipeline.py stop data/experiments/results/<run-id>
python3 scripts/pipeline.py record data/experiments/results/<run-id> --generate
```

`advance` 只推进一步，供外部调度器调用；`run` 循环推进到验收完成、停止或异常。状态和原始记录私有保存，发布前检查所选证据。不推送 Git，也不把测试夹具写入真实榜单。启动响应丢失时保留 `*_starting`，先按运行 ID 核对实际会话，不能重新发题；错误与超时不冒充完成。当前不会自动修复不确定状态或安排第二个验收者。

配置为 JSON，包含以下字段：

| 字段 | 内容 |
| --- | --- |
| `service`、`route` | 现有目录中的服务和接入路径 ID |
| `task_file`、`task` | 仓库任务表路径及任务 ID |
| `phase` | `access` 或 `business` |
| `environment_id` | 本批次服务 × 方式的持久容器标识 |
| `environment` | 明确的可用工具、指定方式、授权、凭据位置、预算及资源边界；直接生成 ENVIRONMENT.md |
| `depends_on` | 业务任务依赖的上一运行绝对目录；必须已验收通过，服务、方式和环境标识一致 |
| `attachments`、`reference` | 可选：原始附件目录、私有验收参考 JSON 文件的绝对路径；分开传递 |
| `preparation_note` | 已提供账号等准备条件，不能冒充 Agent 注册成果 |
| `execution`、`grading` | 各自的模型、思考等级、执行器版本、运行环境、预算和适配命令 |

每个角色的配置形如：

```json
{
  "model": "实际模型 ID",
  "reasoning_effort": "high",
  "harness": {"name": "实际执行器", "version": "固定版本", "mode": "noninteractive"},
  "runtime": "该角色的运行环境标识",
  "seconds": 600,
  "commands": {
    "start": ["/absolute/path/adapter", "start", "{request}"],
    "status": ["/absolute/path/adapter", "status", "{request}"],
    "collect": ["/absolute/path/adapter", "collect", "{request}"],
    "stop": ["/absolute/path/adapter", "stop", "{request}"]
  }
}
```

命令是 argv 数组，不经 shell 拼接。执行和验收使用不同 runtime，实际回执必须对应不同会话和工作目录。`runtime` 相同只能说明声明一致，实际容器复用、历史清理与远端数据恢复必须由适配器落实并留证。新题目目录不能访问其他题答案；不能把整个 pipeline 记录目录开放给执行者。

### 执行器适配协议

每个命令读取 `{request}` 指向的 JSON，stdout 返回一个 JSON 对象，诊断写 stderr。请求包含 `run_id`、`role`、`model`、`reasoning_effort`、`harness`、`seconds`、`runtime`、`input`、`output`、`fresh_session: true`；启动后增加 `handle`。路径属于总控机器，远端适配器负责传送到实际环境、执行及取回。

- `start`：新建会话并返回 `{"handle":"可查询运行标识"}`；适配器用 run_id + role 保证不重复启动。
- `status`：返回 `{"status":"running"}`、`completed` 或 `failed`，必须查询真实运行状态。
- `stop`：终止对应会话及遗留进程；远端场景不能只结束本地 SSH。没有 handle 的不确定启动也要能按 run_id 核对并停止。
- `collect`：将该次记录导出到 output，返回 `{"collected":true}`，必须可重复采集；不运行题目、不自评。

执行 output 包含 `answer.md`（失败可缺）、`events.jsonl`、原始用量来源、`usage.json`、必要业务证据和 `receipt.json`；验收 output 包含 `assessment.json`、原始来源、`usage.json`、`receipt.json`。验收能读取本次执行材料，但不可补做业务。公开证据路径相对运行根目录，例如 `execution/evidence/response.json`。

`receipt.json` 记录实际 `session_id`、`workspace`、`model`、`reasoning_effort`、`harness`、`runtime`、`started_at`、`ended_at`、`exit_code`、`timed_out`、`isolation`、`input_verified`。`input_verified` 必须基于实际模型输入或执行器明确加载记录，不能因为文件存在就填 true。需要重载 MCP 的接入任务由适配器关联所有相关会话、累计用量并保持完整证据，不漏掉初始化阶段。

`usage.json` 使用下列结构。计数来自执行器原始记录，`totals` 是独立读取的运行总量，不能用逐请求求和伪造一次核对。输入包含缓存部分，输出包含推理部分：

```json
{
  "schema_version": 1,
  "complete": true,
  "model": "与实际回执相同的模型 ID",
  "sources": [{"path": "runtime.raw.jsonl", "sha256": "原始文件的 SHA256"}],
  "requests": [{"id": "运行内唯一请求标识", "usage": {
    "input_tokens": 100, "cached_input_tokens": 60,
    "cache_write_input_tokens": 0, "output_tokens": 20, "reasoning_output_tokens": 10
  }}],
  "totals": {"input_tokens": 100, "cached_input_tokens": 60,
    "cache_write_input_tokens": 0, "output_tokens": 20, "reasoning_output_tokens": 10}
}
```

来源路径相对 output。缓存写入数必须显式提供，不能把缺失当零。缺字段、来源不符或计数不一致时，模型费用保持未知；不能采信 Agent 答复中的 Token 或金额。多模型请求不能合并成一个模型计价，适配器须单独分账，当前单模型入口不支持时明确标记用量不完整。价表由 pipeline 事前冻结，执行与验收分别计价。小于展示精度的正金额显示 `<$0.0001`，底层保留数值。
