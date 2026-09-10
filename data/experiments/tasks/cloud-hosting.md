# 云计算与托管：应用配置读取

分类：云计算与托管（cloud-hosting）；本轮不新增子类。先比较 Cloudflare 同一任务的 API、SDK、CLI、MCP 入口；KV 读取不代表应用部署已经完成，也不合入 D1 数据库成绩。

需求依据：[Workers KV 的适用工作负载](https://developers.cloudflare.com/kv/concepts/how-kv-works/)包括应用配置；本轮“查看维护模式”的委托由用户选定。官方使用说明支持该工作流，不作为独立市场频率证据。

## 任务

| ID | 版本 | 用户任务 | 用户任务（英文） | 预计输入 | 预计输出 | 完成标准 | 未完成标准 | 运行资源 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cloudflare-access-001 | v1 | 帮我接通 Cloudflare，确认能够通过指定方式访问测试 KV 空间，保留后续使用需要的本地配置。 | Set up the specified way of accessing Cloudflare, confirm that the test KV namespace is accessible, and retain the local configuration needed for subsequent use. | 账号与测试 KV 空间标识、官方入口、允许使用的账号或凭据及其来源在 ENVIRONMENT.md。只读验证空间身份或键列表即可，不读取配置值。秘密保存在本地私有配置中，答复只说明是否可用和配置位置。 | 指定方式真实调用成功、正确 KV 空间身份、后续可使用的本地配置位置；受阻时说明原因。 | 真实响应证明指定方式可访问正确远端 KV 空间；本地配置可复用且不泄露凭据；验收分别记录已有账号来源、自助完成步骤、人工介入及特殊申请，不将预先取得的账号或资源算作本轮自助创建。 | 只安装或只保存配置，没有成功调用；误用本地模拟数据或其他空间；改走其他方式；配置不可复用；实际运行未完成。缺少授权资源或执行环境故障单列原因。 | 仅通过 ENVIRONMENT.md 指定的入口接入本轮测试空间；安装与配置限本轮隔离环境。只读验证，不创建或修改云资源，不访问其他空间、不付费。没有授权身份或凭据时报告阻碍，不读取本机既有登录。 | 已定义；远端空间及账号来源确认后执行。 |
| cloudflare-kv-config-001 | v1 | 帮我读一下测试应用的当前配置，列出配置内容，并告诉我维护模式开着吗。 | Read the test application's current configuration, list its settings, and tell me whether maintenance mode is enabled. | 配置保存在测试 KV 空间的 app:config 键中，是 JSON 对象；maintenance_mode 表示维护模式。账号和空间标识在 ENVIRONMENT.md。只读，不更改任何内容。 | app:config 的全部配置字段和值，以及维护模式开启或关闭的明确结论。 | 指定方式真实读取正确远端空间的 app:config；输出与冻结并独立重读的 JSON 语义一致，字段和值完整；维护模式结论正确；没有修改远端数据。 | 只列出键名却没读取值；漏字段或改值；错误判断维护模式；使用本地模拟、文档示例或其他空间；改走其他入口；预算内未完成。材料未就绪、数据漂移或环境故障单列无效。 | 仅通过指定入口读取本轮远端测试 KV 空间；CLI 也必须访问云端数据。可复用接入阶段的安装认证配置，不继承接入会话、调用脚本或参考答案。不创建、修改或删除资源。 | 已定义；合成配置实际写入、稳定读回后执行。 |

## 入口与独立验收

2026-09-10 核对的官方入口：

| 方式 | 官方资料 | 这轮核对范围 |
| --- | --- | --- |
| API | [KV 读取接口](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/get/) | 原始 HTTP 请求读取远端键值。 |
| SDK | [Cloudflare TypeScript SDK 的 KV 读取](https://developers.cloudflare.com/api/typescript/resources/kv/subresources/namespaces/subresources/values/methods/get/) | 官方 cloudflare 包的 KV 方法。 |
| CLI | [Wrangler KV 命令](https://developers.cloudflare.com/kv/reference/kv-commands/) | 原生 KV 命令，访问远端空间，不能把本地模拟结果当成云端结果。 |
| MCP | [Cloudflare API MCP](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/) | 官方远程服务覆盖 Cloudflare API，支持 OAuth 或 API token；使用 search/execute 工具，由服务端执行接口调用。必须记录实际可用工具及响应，文档覆盖不等于本轮已接通。 |

总控在专用 KV 空间投递一个小型合成 JSON 对象：maintenance_mode 为布尔值，另有数个普通配置字段。实际值和空间状态冻结在验收包中，执行者只看到键名与字段含义。独立读回确认就绪后，再供四种入口读取同一份不变数据。KV 有最终一致性，准备写入后应确认读取稳定；执行期间不改动该键，若前后独立重读不同则调查材料漂移。

验收不要求 JSON 排版或字段顺序相同；要求字段和值正确、结论有真实读取依据。服务费用只能从实际请求计数、额度或回执判断，HTTP 成功不等于免费。接入与业务用量分别记录；环境、版本、模型、预算、入口和原生 MCP 工具定义由本批清单冻结，不与不同方式混合平均。
