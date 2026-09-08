# 执行、验收与结果回填

目的：把候选表和任务表变成可核对的实际结果，让用户知道哪个入口能完成任务、需要多少开销。复用已有候选和任务；只有资料不足或需求变化时才继续研究，不重复制造中间报告。

准备/验收Agent可以读仓库。被测Agent必须是独立新会话，只获得冻结的题目、指定入口和统一资源，不能收到研究材料、历史答案、提前写好的服务适配代码或本文件。

## 两个 Agent 的边界

| 角色 | 会话与职责 | 能看到的内容 |
| --- | --- | --- |
| 评测 Agent | 当前主持会话可以兼任准备与验收；执行结束后独立读服务状态，写 assessment.json | 仓库原则、任务表、验收规则、真实结果和本地日志 |
| 被测 Agent | 每个服务/任务启动独立 Codex CLI 新会话，实际调用服务和交付用户结果 | 简短委托、原始材料、服务入口及本轮工具/凭据/资源范围 |

`codex-service-trial.py` 只启动被测 Agent 和采集日志；`record-trial.py` 只录入外部评测 Agent 写好的结论，不是第三个 Agent，也不自动启动盲评会话。评测 Agent 已参与准备，不能声称它不知任务设计或历史结果。两者会话/工作目录分开，当前仍同机运行，不是 VM 或完整文件读取隔离。

验收在被测会话结束后进行，独立读取真实远端结果，不采信被测 Agent 的自评脚本。记录器拒收被测工作目录内的 assessment 文件，但这只是录入检查，不能替代对评测者身份和证据的实际核对。评测规则、参考答案不随任务交给被测会话。

## 从已有分类接手

1. 读根目录理念、对应候选与任务表。选定服务ID、入口ID、任务ID与版本。新需求按`tasks/AGENTS.md`出题；确定完成条件后再运行。任务日期过期时先更新题目与版本，不让执行Agent自行改变题目。
2. `npm run pricing:update`获取本轮模型的LiteLLM价表快照（新增模型可在命令后加`-- 模型名`）；`npm run validate`、`npm run generate`检查数据并自动估算模型费用、更新目录。生成本身不联网，使用`data/pricing/litellm.json`中冻结的价格；主动刷新价格会更新展示中的估算，快照日期不等于历史运行日期。入口来自`generated/catalog.json`，任务来自Markdown任务表。按同一批次固定harness、模型、思考等级、预算、工具和凭据条件；不同设置的结果分别记录。
3. 启动独立执行。例如以下是运行命令，不是提供给被测Agent的解法：

   ```sh
   python3 scripts/codex-service-trial.py kiwi --route search-mcp \
     --task-file data/experiments/tasks/travel-flights.md --task flights-search-001 \
     --model gpt-6-astra --reasoning-effort xhigh --seconds 600
   ```

   服务与任务参数可以换成表里的其他记录；`--prepare-only`只生成并保存prompt和配置。脚本沿用本机Codex登录，要求全局AGENTS为空，关闭被测会话的项目指令/技能/插件/记忆注入。默认提供终端与联网检索、不提供服务凭据；也支持准备者在已授权范围内先注册免费账号，再用 `--credentials-file` 传入仅属于指定服务的私有 JSON 凭据，必须用 `--preparation-note` 公开说明准备步骤及其未计入执行 token/耗时。两种前提分别记录；不能让执行 Agent 搜索本机既有凭据。需要本轮未提供的账号、验证码、凭据或付款就记录阻碍。它是同机新目录隔离，非虚拟机；环境不满足时修复环境或记为运行阻碍，不将其归因于服务。

   **在Codex内编排时，启动脚本应通过宿主机终端或获准提升权限的shell执行。** macOS沙箱里嵌套启动Codex可能在初始化app-server前报`Operation not permitted`；这是启动环境问题。在允许权限提升的环境且已有启动授权时，可以只对该启动命令申请宿主执行；当前环境禁止权限参数时不要传入该参数。被测Codex仍保留脚本设置的`workspace-write`沙箱，不改为全盘访问。未获授权则记录阻碍，不绕过审批。环境无效的尝试保留记录，修复后用全新会话重跑，不计作供应商失败。
   自然任务用 `--prompt-style natural`：prompt 只含简短委托及附件位置，原始材料写入 `input.md`，环境与授权范围写入 `ENVIRONMENT.md`。预计输出不重复拼接，完成/失败标准留给外部复核；必要交付要求须已在委托或材料中写清。自动保存的 CLI 日志和独立远端读取承担留证，不让执行者额外整理测试报告。修改任务要求时升级版本，不能将自然任务结果与历史强指导任务混为同一题。

   新自然输入可先用 `--prepare-only` 查看。原始附件在运行前备份到结果目录的 `context-files/`，文件 hash 随 run.json 保存；不能仅按 prompt 字符数比较信息量，Agent 阅读附件也会消耗 token。旧任务表可能仍含测试要求，逐题整理并升级版本后再选择 natural；legacy 保留用于旧方式。

4. 等进程结束，保留它输出的结果目录。运行器保留本地 Codex session（不使用 `--ephemeral`），退出后按本次 thread ID 找到原始文件，复制为仅本机可读的 `session.raw.jsonl`；该文件与其他原始日志均留在 gitignored 结果目录，禁止作为公开证据。自动提取 `request-usage.json`，只保留逐次 token 计数、采集状态和源文件 hash，不保留会话内容、路径或请求/会话 ID。优先使用 `token_usage_record`，兼容 `token_count`；去重后必须与 CLI 最终用量一致才标记 `complete`。超时缺少最终汇总、明细缺失、截断或计数不一致均标记 `incomplete`，保留观察值但不当作完整费用。录入器从原始 session 重新提取，不接受评测者手填请求用量。外部Agent读`run.json`中的冻结任务、`answer.md`、`events.jsonl`和`workspace/evidence/`。核对调用确实来自指定服务、请求参数与任务一致、答案由真实响应支持；不要执行或采信被测Agent写的校验器来替代复核。
5. 在结果目录内、`workspace/`之外写`assessment.json`。按原先完成标准逐项核对，完整填好以下字段（示意中的空值必须据证据填写，不是默认判定）：

   ```json
   {
     "status": null,
     "reason": "",
     "reviewer": "external preparing Agent / session identifier if available",
     "checks": [
       {"criterion": "任务的某条完成条件", "passed": false, "evidence": "请求/响应/答案的具体位置及核对结果"}
     ],
     "evidence": [
       {"path": "workspace/evidence/实际文件名", "note": "此文件支持什么判断"}
     ],
     "service_cost_usd": null,
     "service_cost": {
       "kind": "unknown",
       "sources": [],
       "note": "写明费用依据或未知原因"
     },
     "human_interventions": null
   }
   ```

   `status`为`completed`、`not_completed`或`invalid_run`。成功必须满足全部完成条件；缺凭据、无结果、任务超时等写清原因。环境故障用`invalid_run`。遇到无法证实的答案，不猜为成功。选取足够核对结论的请求、真实响应、答案或失败证据；先确认脱敏，原始完整日志保留本地。对动态查询核对当次证据，不固定未来价格答案。

   `service_cost_usd`记录本次被测服务调用费用，不含机票等业务商品价格。`service_cost.kind`为`reported`（回执/账单金额）、`confirmed_free`（确认免费）、`estimated`（用量×单价）或`unknown`；已知金额须在`sources`提供脱敏证据路径或公开计费来源，并在`note`写明依据。记录器不自动抓取各家账单，外部评测 Agent 负责采集与核验；回执没写费用不代表免费。旧记录的新增实付金额原样保留，不补造新来源。

   估算服务费用时提供`items`，例如`[{"quantity": 10, "unit": "request", "usd_per_unit": 0.002}]`，顶层金额可为null，由记录器计算为0.02；若填写了金额，必须与计算结果一致。复杂套餐、阶梯或最低消费需先据真实账单/规则确定本次适用的计费项，不能只按一次请求的标价猜算。信用额度不是实付金额，只有确认本次落在免费范围才标`confirmed_free`。

   模型费用不由评测 Agent 手填：`npm run generate`从真实`usage`和LiteLLM快照自动得到`model_cost`，公开在生成的结果JSON与目录。新运行优先对每次请求按其输入长度选择LiteLLM价格档位，再逐次相加；完整明细须与整轮用量核对一致。按标准API价格估算普通输入、缓存读取/写入和输出，推理token若已含在输出中不重复加。缺价格、缺用量或无法判断上下文计价档位时记未知；不能用累计会话输入冒充单次请求上下文。服务费用估算单独标明。`human_interventions`来自实际观察，不知道填null；模型、用量、耗时和配置只来自运行器记录。

6. 回填结果并更新展示：

   ```sh
   python3 scripts/record-trial.py <结果目录> --review <结果目录>/assessment.json
   npm run validate
   npm run generate
   ```

   检查`generated/evaluations.md`出现新行、`generated/catalog.json`的对应服务/入口出现该次`task_runs`，其他入口不继承成功。MCP的`search_services`和`get_service`从同一目录读取这些结果；本机检查时设置`AFS_DATA_DIR`指向当前`generated/`。

## 留下什么

- 候选表、任务表、[结果表](../../generated/evaluations.md)是主交付。`data/experiments/evaluations/`保存精简结果源，`evidence/`保留选取的证据；原始`results/`日志仍gitignored。
- 首页显示完成率、Token用量、模型费用、服务费用；后面三项取有效试跑均值（成功与失败都包含），未知值不按0填，也不跳过未知样本制造偏低均值。当前汇总按服务/入口最新已测协议取样，任务冻结内容、重复次数及配置一致才合表；旧记录仍可查。
- 记录harness版本、模型、思考等级、实际起止时间/时区、任务版本与hash、接入条件和验收依据。历史观察保留；新运行追加，修订旧结论要解释原因，不静默覆盖。
- 公开副本不保留本机用户名、目录路径或Codex会话ID。记录工具替换已知路径和会话标识，原始文件仍留在本地；发生脱敏时同时保留原文件hash与公开副本hash，并说明原因。Agent仍需检查密钥、Cookie、私人消息等内容，不能把自动替换当作完整隐私审查。
- 录入工作区与公开发布是不同操作。当前流程不自动提交/推送，不联系服务商；外部发布沿用维护者的授权范围。
- 脚本负责重复动作，Agent负责研究与证据判断。格式可以调整，限制来自真实任务与公平性要求；调整工具后做相应验证。

旧的`npm run agent-verify`、`published/`及milestone文档属于历史Claude实验链路，不用于本次流程。

## 免费账户测试的私有输入

凭据文件格式为 `{ "SERVICE_API_KEY": "实际值" }`，置于仓库外并设为 `0600`。脚本只把明确传入的字段复制到新目录的 `.private/credentials.json`；不继承本机其他服务登录，不把密钥放入 prompt、命令参数或公开元数据。指定 Key 对应免费账户/额度，由准备者先核对，不启用付费超额。准备注册不等于执行期间的人类介入；两部分分开描述。

本地结果目录的 `private-secrets.json` 是脱敏用字符串数组，也可由复核者补入本次生成的数据库密码、连接 URL、claim URL 或账号标识。此文件不能作为公开证据。记录器将这些确切值及编码形式从公开副本中替换，仍须人工审查未列出的敏感项。源文件 hash 和脱敏副本 hash 同时保留。只选最少的请求/响应证据，不公开完整网页、邮箱、控制台或原始会话。
