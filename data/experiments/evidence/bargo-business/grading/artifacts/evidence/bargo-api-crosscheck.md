# 公开核验摘要（依据独立验收整理）

数据服务：[Bargo](https://www.bargo.ai/free-apis/congress)。本摘要不包含原始交易行或可重建该表的逐项数值；完整答案、响应与验收记录私有保留。

## 独立验收结论

`financial-disclosures-001/v1` 的原始独立验收结论为 `completed`。验收者核对了真实指定服务请求、官方年度索引与原始 PTR，确认要求的股票、方向、交易日期、提交日期、美元区间及记录集完整性符合冻结参考；具体出处与服务署名齐全。

业务数据由 Bargo 免 Key REST 查询取得，官方文件用于核对。提交日采用官方索引口径，未与交易日或通知日混用。执行者完成了官方检索与原始文件核对；PDF 解析依赖的安装、排查和读取耗时属于 Agent 任务过程。

[对应官方 PTR](https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035260.pdf) 的下载副本 SHA-256 为 `6fc31ac8feb1040b81469cc510002cbce91df4ae9b582c8ebb45921dd8b4db12`，与事前冻结原始件相同。哈希仅标识材料，逐项核对实际由独立验收者执行。

## 总控补充质量说明

原答案在额外叙述中将 SP 解释为“本人和配偶”账户，这个解释不准确。众议院[官方字段说明](https://ethics.house.gov/wp-content/uploads/2023/12/CY-2017-Instruction-Guide-for-Financial-Disclosure-Statements-and-PTRs_0_0.pdf)将 SP 定义为配偶；本人及共同持有不能据此推定。该说明由总控在验收后另行核对，不能冒充原独立验收已发现的问题。保留原始 `completed` 结论及全部检查布尔值，同时披露这项答案质量缺陷；不声称整份答复无误，也不改写冻结任务。

## 资源与结论边界

[官方文档](https://www.bargo.ai/free-apis/congress)及当次限额回执支持此次免费、免 Key、只读使用；未注册、未付费、未进行交易。依据[Bargo 条款](https://www.bargo.ai/free-apis/terms)，公开副本只提供核验摘要与署名，原始数据不重分发。

这是单个服务入口、单个冻结样本的一次执行和一次独立验收；不代表参众两院全覆盖、MCP 路径、长期稳定性或总体排名。总耗时包含 Agent 查文档、尝试、安装工具和核对，不能当作 API 延迟。
