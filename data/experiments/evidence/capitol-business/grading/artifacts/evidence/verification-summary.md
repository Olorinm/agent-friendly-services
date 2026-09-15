数据来源：[CapitolExposed](https://www.capitolexposed.com/)。

# 公开核验摘要 — financial-disclosures-001/v1

本摘要依据独立验收整理，省略原始交易行及其数值；完整响应、逐行答案和原始验收仍私有保留。

- **独立结论：completed。** 验收者对指定服务采集的全部记录按任务要求的提交月份重筛，与执行前冻结的众议院索引和 PTR 逐项比较，数量与记录集一致，无遗漏、重复或多余项。
- 核对了普通股范围、标的、买卖方向、交易日期、官方提交日期和美元金额区间；区分了通知日期，未把区间当精确成交金额。配偶标记解释正确。
- 真实工具记录支持指定服务的免 Key HTTP 调用。业务查询取得三页成员交易记录；另有一次默认 User-Agent 请求被 403 拒绝，执行者改用 curl 后完成。原始 PDF 用于核对，没有替代指定服务的业务数据。
- 执行者取得的原始 PDF 与事前冻结副本 SHA-256 一致：`6fc31ac8feb1040b81469cc510002cbce91df4ae9b582c8ebb45921dd8b4db12`。[官方原件](https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035260.pdf)。
- 免费依据：[官方 API 文档](https://www.capitolexposed.com/api-docs)与[服务条款](https://www.capitolexposed.com/terms)。本轮使用免 Key 只读入口及其免费限额，没有付费 AI、导出或账户升级操作；服务费用由独立验收确认免费。

这是一次固定任务、模型、环境和预算下的结果，不代表所有成员、时间范围、入口或后续运行的表现。
