# 候选收录标准 v1

目标：帮助普通个人找到能让 Agent 完成任务的服务，逐步回答哪个更省钱、省事、可靠。当前标准覆盖**发现与收录**；公开资料不能替代接入验证和真实任务测试。

本文是当前候选字段的填写参考，随研究迭代。[维护说明](./contributing.md)包含用户需求研究的做法；服务功能表不替代需求证据。

普通个人默认没有公司、旅行社资质、商家店铺、对外运营的网站、用户流量或供应商合同。国籍、居住地、手机号、支付方式、服务器地区和票价销售市场必须在实际测试时指定，不能从一个地区的成功外推全球。

## 1. 记录什么对象

一份 YAML 对应一个明确的服务产品，文件名等于稳定 `id`。同一个服务的多种入口写在 `catalog.routes`。第三方发布者在市场上销售的独立产品可以单列，例如 Skootle 的 Actor；Apify 是托管平台，不是该机票产品的发布者。

分类从 [categories.yaml](../data/categories.yaml) 选择：`travel/flights`、`travel/hotels`。`category` 保留一个主要大类以兼容旧索引；`catalog.classifications` 可以有多个大类/子类路径。例如 SerpApi 主类仍为 `web-search-data`，同时归入 `travel/flights`。尚未划分子类的旧服务不强行归类。

能力表示用户任务的结果：机票搜索、重新核价、返回购买链接、出票。搜索到报价不等于重新核价成功，返回购买链接不等于出票。能力词典随子类维护，不按接口名或 CRUD 动作建立能力。

## 2. 第一条记录可以很小

以下为格式示例，`example.com` 是占位地址，不能作为真实候选提交：

```yaml
id: example-flights
name: Example Flights
category: travel
homepage: https://example.com/
summary: Example flight service awaiting access-route research.
submitted_by: community
catalog:
  version: 1
  classifications: [travel/flights]
  sources:
    discovery:
      url: https://example.com/partners
      checked_on: "2026-09-07"
      kind: official_site
  routes: []
```

最低要求是产品身份、分类和一手来源。没有 API 文档、拿不到密钥、需要商务审核，都可以收录。`routes: []` 表示尚未确认具体入口，不表示没有 API。已有旧格式记录继续兼容；新增调查优先使用本标准。

## 3. 每条入口分别查什么

| 字段 | 含义与填写规则 |
| --- | --- |
| `id` | 服务内稳定且唯一，例如 `search-mcp`、`tequila-api` |
| `interface` | `api / sdk / cli / mcp / web / mobile`；只记录找到的入口，缺项为未知 |
| `entry_url`、`docs` | Agent 从哪里开始：安装说明、产品 API 文档或协议地址。文档不是独立的接口类型 |
| `maintainer` | 相对于本条服务产品的维护方：`official / third_party / unknown`。Skootle 官方产品仍是 Google Flights 的第三方数据入口 |
| `upstream` | 已确认的上游标识，例如 `google-flights`；不确定就省略。共享上游不能算成独立票源 |
| `via` | 本服务内依赖的另一条入口编号；只表达依赖，不自动继承能力、权限、费用或实测结果 |
| `availability` | `self_serve / application / invite_only / paused / retired / unknown`，描述该入口公开的开放方式 |
| `personal_access` | `documented / restricted / unknown`。注册按钮或 API 文档不足以推断个人符合资格；限制必须注明条件 |
| `auth` | `none / api_key / oauth / platform_credentials / unknown`；多种方式可以拆路径或在备注中说明 |
| `data_kind` | `live / cached / sandbox / mixed / unknown`。`live` 是来源声称可查当前报价，不保证每次请求强制刷新 |
| `capabilities` | 能力 ID → `documented / unsupported / unknown`；本字段没有“实测通过”取值 |
| `requirements` | 每项为 `required / not_required / unknown`；包括公司、店铺、网站、流量、资质、合同、邀请、审核、邮箱/手机/实名、支付方式、预付、平台账户 |
| `human_steps` | 来源明确需要人的步骤及阶段：`signup / credentials / activation / task`。省略表示未收集，不表示无需人工 |
| `costs` | 公开免费额度、用量费用、最低支出；数值、单位、计费分母/周期、范围与证据。货币使用 `unit: money` 与 ISO 币种 |

SDK 是编程库，CLI 是终端程序，MCP 是 Agent 工具协议，API 是程序调用的服务接口。它们常共享底层服务，但包装、认证、安装与工具覆盖可能不同。**先分别登记已知入口；测试时先选适用路径，不把每个服务机械地跑四遍。** 有无指导通过起始文档及实验的起始信息记录，无须再复制一套服务分类。

确定的值使用以下形状：

```yaml
availability:
  value: invite_only
  evidence: [partnership-policy]
  notes: New partnerships require invitation; this does not describe the MCP route.
```

`evidence` 引用本服务 `catalog.sources` 中的来源。来源都有公开 URL、实际查阅日期、类型和必要限制。不同事实可以引用同一来源；重新查阅时只更新对应来源日期，不给全文件刷新“验证时间”。

`unknown` 可无证据，也可保留矛盾来源并说明。确定值必须有来源；`unsupported` 还需明确否定的说明，不能用搜索无结果代替。解析失败、HTTP 401/403、MCP 无法作为网页读取，都不是功能不可用的结论。

`5 credits / flight request` 不等于 5 美元；`250 searches / month` 不等于 250 次任意任务。只在来源明确时填 0。免费额度、绑卡和预付分别记录；尚未测量的人工时间、等待时间与 Agent 成本不填 0。

## 4. 公开资料检索流程

1. **确定边界**：大类、子类、个人画像、用户期望结果；机票首轮找票价搜索，不把只有航班状态的 API 算进去。
2. **分方向检索**：平台/联盟、航司与分销系统、数据提取商、API 市场、官方与社区 Agent 工具；同时使用中英文。目录和论坛作线索，结论回到一手资料。
3. **保留依据**：在对应记录中保存来源、日期、关键取舍和缺口。检索过程按复查需要留存，不要求逐次查询另交报告；保留的日志必须如实记录。
4. **去重入池**：匹配产品身份、已有 ID、发布者、平台和上游。不因同属一家公司就合并不同产品，不因多了一个 MCP 就算另一家服务。
5. **逐入口补事实**：从官方文档/仓库/公告、注册页、价格页核查。市场产品使用具体发布者页面。宣传只能登记为来源声明，不能作为质量证据。
6. **校验展示**：运行校验与生成，再复核证据含义。首轮覆盖各检索方向后即可发布带缺口的候选集，不宣称穷尽市场。

[机票阶段结果](./flights.zh-CN.md)汇总首轮发现和覆盖限制，逐产品事实直接维护在候选资料中。

## 5. 文档、接入和任务结果分别成立

| 证据层次 | 能说明什么 | 不能推出什么 |
| --- | --- | --- |
| 公开资料 | 供应方公布的能力、步骤、价格和限制 | 个人已获权限、价格正确 |
| 链接探测 / M1 | 链接响应或请求/auth 形状有依据 | 实时搜索权限、任务完成 |
| 实际接入 | 指定个人、地区和账户的注册、授权、激活情况 | 任意任务都能完成 |
| 真实任务 | 指定入口、输入、环境和预算下的结果 | 全球最低价、永久可用、其他入口有效 |

当前生成记录明确标为 `evidence_level: public_sources_only`、`route_tests: not_recorded`。旧服务所在目录、徽章、M1 或其他任务的成功，不会自动变成新增入口的成功。原有实验保留，但还没有映射到本标准的入口 ID。

后续测试至少绑定：服务 ID、入口 ID 与工具版本、任务 ID 与版本、起始文档、模型/工具/服务器地区、用户地区与销售市场、时间、重复次数与预算。分别记录接入阻碍、数据权限、任务结果、响应与独立核验、服务实付、Agent token（输入/其中缓存/输出）、人工操作与等待时间。接入受阻仍形成结果，任务部分记“未开展”。

公平测试固定旅客、完整日期、机场范围、币种、销售市场、行李、转机与自转机限制；实时报价在相近时间窗执行并记录时间。缓存和沙箱不参加实时报价比较；比较的是统一条件下观察到的可用报价，不宣称全网最低。接入成本与已接入后的任务成本分别报告。此版不实现付费接入、出票或总分榜。

## 6. 仓库使用

- `data/candidates/`：包括未知、受限、暂停及未实测候选；不要求先拿密钥。
- `data/providers/`：保留旧索引；同一 ID 不跨目录重复，已有服务新调查写入 `catalog`。
- `schema/provider.schema.json`、`schema/catalog.schema.json`：字段约束；额外校验分类、能力归属、来源引用、真实日期、重复入口、依赖环与金额单位。
- `generated/catalog.json`、`generated/catalog.md`：生成的跨目录发现数据与入口清单；旧 `providers.json` 不混入新入口声明。
- MCP `search_services` / `get_service`：按大类、子类、入口、能力、个人门槛查询。入口条件必须在同一条路径成立；旧 MCP 工具维持原用途。

```sh
npm run validate
npm test
AFS_OUTPUT_DIR=/private/tmp/afs-preview npm run generate
AFS_DATA_DIR=/private/tmp/afs-preview/generated node mcp/server.mjs
```

沙箱若阻止 `tsx` CLI 创建 IPC，可用 `node --import tsx scripts/validate.ts`、`AFS_OUTPUT_DIR=/private/tmp/afs-preview node --import tsx scripts/generate.ts` 执行相同脚本。预览生成不会修改工作区的 README 与 `generated/`；这些视图通常由源资料生成。

机票需求与场景保存在 `data/research/travel/flights.yaml`；当前进度与下一步见[机票阶段结果](./flights.zh-CN.md)。
