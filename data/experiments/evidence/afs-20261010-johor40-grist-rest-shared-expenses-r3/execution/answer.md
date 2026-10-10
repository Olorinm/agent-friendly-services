Now let me check the current document state and write an API helper.
Auth works. Now creating the ledger tables with formula-driven summary.
Let me verify the document's page structure so the link lands on a usable view.
Pages were auto-created per table. Let me confirm the page URLs resolve.
完成。已在指定的 Grist 文档中建好在线账本（REST 入口，仅本工作区/本空文档）。

**私人表格链接**（私有，需登录该 Grist 账号访问；未公开分享）
- 账目页（记账）: https://docs.getgrist.com/doc/[SERVICE_SECRET]/p/2
- 结算页（自动汇总）: https://docs.getgrist.com/doc/[SERVICE_SECRET]/p/3
- 文档根: https://docs.getgrist.com/doc/[SERVICE_SECRET]

**当前结算数**（按最初六笔）
- 总支出 ¥2400.00，每人应分摊 ¥1200.00
- 林青已付 ¥2095.60；周舟已付 ¥304.40
- 周舟需补付给林青 **¥895.60**

**继续记账**：在「账目」页按 日期/用途/付款人/金额 追加或修改行即可，「结算」页的已付、应分摊、净额和“谁补给谁”会由公式自动更新。

表结构：`Expenses`（日期、用途、付款人、金额）与 `Settlement`（成员、已付、应分摊、净额、结算说明），汇总全部为公式列，无需再运行脚本或调用 Agent。未做任何转账、邀请或通知。