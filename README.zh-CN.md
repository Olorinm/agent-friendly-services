<!-- 生成文件 — 修改 scripts/generate.ts，再运行 npm run generate。 -->

# Agent-Friendly Services

[English](./README.md) | 简体中文

**帮你找到能让 Agent 完成任务的服务，并用实测比较哪个更可靠、更省事、更有性价比。**

让 Agent 帮忙找机票、准备数据库或整理会议待办，往往还得先选服务、读文档、申请账号，再试试到底能不能用。我们把这些选择收集起来，用真实任务逐步验证，让你和你的 Agent 少走一些重复的弯路。我们关注普通个人能用上的服务，注册、权限和付费门槛也会一并记录。

## 看看有哪些服务

按下面的分类，可以找到候选服务、我们设计的任务，以及已经留下的实测结果。

| 大类 / 子类 | 候选服务 | 任务定义 | 实测记录 | 有运行记录的服务 |
| --- | ---: | --- | ---: | --- |
| 数据库 / 托管关系型数据库 | [6](./generated/catalog.md#databases-hosted-relational) | [任务](./data/experiments/tasks/databases.md) | [2](./generated/evaluations.md#databases-hosted-relational) | Neon, Turso |
| 协作办公与存储 / 在线任务表 | [8](./generated/catalog.md#productivity-storage-collaborative-tables) | [任务](./data/experiments/tasks/collaborative-tables.md) | [4](./generated/evaluations.md#productivity-storage-collaborative-tables) | Grist, Notion |
| 旅行 / 航空机票 | [26](./generated/catalog.md#travel-flights) | [任务](./data/experiments/tasks/travel-flights.md) | [4](./generated/evaluations.md#travel-flights) | Ignav Flights, Kiwi.com |
| 网页搜索与数据 / 网页搜索 | [6](./generated/catalog.md#web-search-data-web-search) | [任务](./data/experiments/tasks/web-search.md) | [3](./generated/evaluations.md#web-search-data-web-search) | Exa, Firecrawl |

[全部候选与接入方式](./generated/catalog.md) · [全部实测与证据](./generated/evaluations.md) · [旧版服务索引（76）](./generated/providers.md)

点开实测记录，可以看到 Agent 实际做成了什么、需要哪些准备，以及用了多少 token、时间和服务费用。每次运行也保留任务、模型、日期与证据，方便你判断结果是否适用于自己的情况。

资料还在持续积累。未测的服务、遇到的接入门槛都会保留，运行次数也包含历史版本和未成功的尝试。一次成功能提供参考；要推荐谁更值得用，还需要更多可比的结果。

## 也可以交给你的 Agent 来查

把下面的查询指引交给你的 Agent，让它结合你的任务寻找候选、核对接入条件，再根据已有证据说明推荐理由。

[查询指引](./llms.txt) · [服务 JSON](./generated/catalog.json) · [实测 JSON](./generated/evaluations.json) · [MCP 配置](./mcp/README.md)

通过 `search_services` 按分类和接入方式检索，再用 `get_service` 查看个人准入条件、费用与实测依据。不安装 MCP 也可直接读取：

```sh
curl -s https://raw.githubusercontent.com/Olorinm/agent-friendly-services/main/generated/catalog.json
```

## 一起补全这份资料

如果你知道我们漏掉的服务、有想测的真实任务，或发现资料已经过时，欢迎提 Issue 或 PR。提供一条线索、纠正一个事实，都能帮上忙。

[核心理念](./AGENTS.md) · [收录标准](./docs/catalog-standard.zh-CN.md) · [任务设计](./data/experiments/tasks/AGENTS.md) · [执行与验收](./data/experiments/AGENTS.md) · [参与贡献](./docs/contributing.md) · [机票阶段结论](./docs/flights.zh-CN.md)

代码：[MIT](./LICENSE) · 数据：[CC BY 4.0](./LICENSE-DATA)。
