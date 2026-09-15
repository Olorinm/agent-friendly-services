# 公开核验摘要

数据服务：[Bargo](https://www.bargo.ai/free-apis/congress)。总控依据本次独立验收整理；原始交易行、答案、原件、日志及交叉材料私有保留。

`financial-disclosures-003/v1`，独立结论为 `completed`。指定服务提供业务数据，执行者检索两人的年度 PTR 并核对本题提交月份。逐笔交易日、提交日及自然日差，按人的笔数、最短与最长间隔均符合冻结官方参考；日期口径、普通股和家庭成员范围正确，原始出处与 Bargo 署名齐全。

独立验收复核了当次执行响应，并另行通过同一免费 API 核对；官方 PDF 采集副本与冻结原件哈希一致。依据包括[年度索引](https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2026FD.zip)、[Allen PTR](https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035260.pdf)、[Case PTR](https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035275.pdf)。

执行约 401 秒，无超时。执行与验收的 API 复核共享当日免 Key 配额，均有当次回执支持；服务费用确认为零，模型执行和验收用量分别计量。依[Bargo 条款](https://www.bargo.ai/free-apis/terms)，公开副本不重分发原始记录。

本次成功不抹去前两题超时，也不证明所有任务或未来重复运行都能完成；它说明在这个冻结任务与预算下完成了交付。
