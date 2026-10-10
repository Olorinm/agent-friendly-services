Tables and formulas work. Now let me remove the hardcoded key from my scratch scripts (credentials must stay only in credentials.json) and do a final state check.
已在指定 Grist 文档中建好账本（同一文档内 3 张表，均按人民币元、精确到分）：

- **明细 Expenses**：字段 `日期 / 用途 / 付款人 / 金额(元)`，另含公式列 `个人分摊(元)=金额/2`，已录入 6 笔。
- **汇总 Summary**：林青、周舟各一行，`已付`、`应分摊`、`净垫付` 均为公式，由明细实时计算。
- **结算 Settlement**：`总支出` 与 `结算说明` 为公式。

**私人表格链接**：https://docs.getgrist.com/doc/[SERVICE_SECRET]

**当前结算（按最初六笔）**
- 总支出 ¥2400.00，各应分摊 ¥1200.00
- 林青已付 ¥2095.60（净垫付 +895.60）
- 周舟已付 ¥304.40（净垫付 −895.60）
- **周舟需补付林青 ¥895.60**

**继续记账**：在文档「Expenses」页面直接新增一行（日期/用途/付款人/金额），或修改已有金额，Summary 与 Settlement 的已付、应分摊和补差方向金额就会自动刷新，无需运行脚本或找 Agent。

说明：仅做了上述录入与公式配置；未发起任何转账、邀请或通知，未邀请第三人，也未使用超出本轮的付费能力。运行脚本在题目目录 `grist_setup.py` / `grist_records.py` / `grist_verify.py`，密钥仅保存在 `/home/node/service-tools/credentials.json`。