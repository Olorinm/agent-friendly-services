Now I'll create the `Expenses` table with the four required fields.
Table created. Now adding the six expense records.
Records added. Now building the page with the detail grid and live summary tables.
Now let me verify the computed summaries.
Rounding the money formulas to the cent to avoid floating-point noise.
Now removing the default placeholder table.
账本已在线建好（Grist，私人文档，未共享/邀请/转账）。

- 私人链接：https://docs.getgrist.com/[SERVICE_SECRET] （页面 `共享支出账本`）
- 结构：`支出明细`（日期/用途/付款人/人民币金额，六笔完整录入）＋两个自动汇总表 `各人汇总`、`结算`，均由 Grist 汇总表和公式实时计算。
- 当前结算：总支出 ¥2400.00，每人应分摊 ¥1200.00；林青已付 ¥2095.60（净 +¥895.60），周舟已付 ¥304.40（净 -¥895.60）→ **周舟补给林青 ¥895.60**。
- 继续记账：在 `共享支出账本` 页的 `支出明细` 表直接增行或改金额，汇总与结算自动更新，无需脚本或 Agent。

交付说明存于 `DELIVERY.md`。