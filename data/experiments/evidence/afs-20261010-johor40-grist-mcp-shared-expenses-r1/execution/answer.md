I have the tool schemas. Let me inspect the target document first.
Now I understand the recommended approach. Let me build the document: a detail table plus a summary table driven by formulas.
Now let me verify the final state and test that the summary auto-updates on insert/edit (then revert the test change).
Auto-update verified (add + edit recalculated the summary; test record removed, back to the original six). Let me capture the final doc info and write a short delivery note.
已建好在线账本（Grist，私人文档，未共享/邀请/通知任何人，未发生转账）。

**私人表格链接**：https://docs.getgrist.com/9BAEULLj4nBS/[SERVICE_SECRET]-blank

**当前结算（最初 6 笔，合计 ¥2400.00，每人应承担 ¥1200.00）**

| 人员 | 已付 | 应分摊 | 差额 |
|---|---|---|---|
| 林青 | ¥2095.60 | ¥1200.00 | +¥895.60 |
| 周舟 | ¥304.40 | ¥1200.00 | −¥895.60 |

**结论：周舟需补给林青 ¥895.60**（仅显示，未实际转账）。

**在哪里继续记账**：打开文档默认页「共享支出账本」，在「逐笔明细」表底部新增一行（日期/用途/付款人/金额）或改金额即可，「结算汇总」用公式自动重算，无需脚本或 Agent。

明细保留 6 笔；我另用临时记录验证过“新增/改金额自动更新”后已删除还原。私有交付记录见 `delivery.md`。