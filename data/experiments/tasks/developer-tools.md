# 开发工具：仓库问题整理

分类：开发工具（developer-tools）；本轮不新增子类。先比较 GitHub 同一任务的 API、SDK、CLI、MCP 入口，不据此排列不同开发工具服务的优劣。

需求依据：[GitHub 的问题筛选工作流](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests)支持按状态和标签整理待处理问题；本轮具体委托由用户选定。这说明需求与可实现的工作流存在，不代表已经证明市场频率。

## 任务

| ID | 版本 | 用户任务 | 用户任务（英文） | 预计输入 | 预计输出 | 完成标准 | 未完成标准 | 运行资源 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| github-access-001 | v1 | 帮我接通 GitHub，确认能够通过指定方式访问测试仓库，保留后续使用需要的本地配置。 | Set up the specified way of accessing GitHub, confirm that the test repository is accessible, and retain the local configuration needed for subsequent use. | 仅访问本轮测试仓库；仓库标识、官方入口、允许使用的账号或凭据及其来源在 ENVIRONMENT.md。只读验证仓库身份即可，不整理 issue。秘密保存在本地私有配置中，答复只说明是否可用和配置位置。 | 指定方式真实调用成功、正确仓库身份、可供后续使用的本地配置位置；受阻时说明具体原因。 | 真实响应证明指定方式能够访问正确仓库；所需本地配置可复用且不泄露凭据；验收分别记录已有账号来源、自助完成步骤、人工介入和特殊申请，不将已有账号算作本轮注册。 | 只安装或只保存配置，没有成功调用；访问错误仓库；用其他方式替代指定方式；配置不可复用；实际运行未完成。缺少授权资源或执行环境故障单列原因。 | 按 ENVIRONMENT.md 指定的 API、SDK、CLI 或 MCP 入口接入，安装与配置限本轮隔离环境。只读测试仓库，不写入仓库、不发送通知、不注册其他服务、不付费。没有提供身份或凭据时报告接入阻碍，不读取本机既有登录。 | 已定义；资源及账号来源确认后执行。 |
| github-open-bugs-001 | v1 | 帮我列出测试仓库里所有尚未关闭、带 bug 标签的 issue，给出标题和链接。 | List all open issues labeled bug in the test repository, including each title and link. | 测试仓库标识在 ENVIRONMENT.md；只需 issue，不包括 pull request，不修改任何内容。列表顺序不限。 | 符合条件的全部 issue 标题及网页链接。 | 与本轮冻结并独立重读的仓库状态一致；所有 open 且带 bug 标签的 issue 均列出，标题和链接正确，无已关闭项、无其他标签项、无 pull request 或重复项；真实调用通过指定方式完成。 | 漏项、多项、错误标题或链接、只返回教程或示例、未实际读取指定仓库、改走其他入口、预算内未完成；材料变化或环境故障单列无效，不猜测成功。 | 仅通过指定入口读取测试仓库。可复用接入阶段交付的安装与认证配置，不继承接入会话、调用脚本、答案或验收资料。禁止写入仓库。 | 已定义；冻结合成仓库状态后执行。 |

## 入口与独立验收

2026-09-10 核对的官方入口：

| 方式 | 官方资料 | 这轮核对范围 |
| --- | --- | --- |
| API | [REST issues](https://docs.github.com/en/rest/issues/issues#list-repository-issues) | 原始 HTTP 请求；该接口可能混入 PR，结果按用户要求验收。 |
| SDK | [Octokit JavaScript SDK](https://github.com/octokit/octokit.js) | 官方 SDK 的仓库及 issue 方法；不是另写 HTTP 包装冒充 SDK。 |
| CLI | [GitHub CLI issue list](https://cli.github.com/manual/gh_issue_list) | 使用 issue 业务命令；本轮不以 gh api 通用 HTTP 转发代表业务 CLI。 |
| MCP | [GitHub 官方 MCP](https://github.com/github/github-mcp-server) | 官方服务提供仓库及 issue 查询工具；由 harness 原生接入并留下实际工具调用，手写 JSON-RPC 不替代这一路。 |

总控在专用仓库准备合成 issue，包含符合条件项、已关闭 bug 和未关闭的其他标签项；可放置同标签 PR 以核对对象类型。记录实际创建后的 ID、标题、URL、状态、标签和对象类型，冻结为独立验收参考。执行材料只给仓库标识与用户要求，不给预期条目数、答案或筛选代码。四种方式读取同一份不变数据；执行前后独立重读，若数据变动则判断影响后重跑，不把漂移算作服务失败。

接入与业务任务分别留用量、耗时和人工步骤。每次业务执行是新会话，实际模型、预算、工具定义、依赖版本、安装状态由本批运行清单冻结。中英委托是等价展示，执行语言由本批统一指定，不混用两种 prompt 合并统计。
