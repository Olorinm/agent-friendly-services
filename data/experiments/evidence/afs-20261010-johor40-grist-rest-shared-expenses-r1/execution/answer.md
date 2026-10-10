I'll start by reading the credentials and service config, and checking the workspace.
Doc and workspace confirmed. Now I'll create the tables with records and formulas. First, let me compute date epochs.
Now I'll create the ledger tables via the REST API.
widgetOptions must be JSON strings, not objects. Fixing.
Records weren't inserted and table ids became `Table2`/`Table3`. Let me add records separately.
Formulas error since they reference `账目` while the table id is `Table2`. I'll rename tables to Chinese ids via the apply action.
The apply endpoint takes a raw array. Let me fix the payload and retry.
The REST rename is `PATCH /tables` with `fields.tableId`. Let me use that.
ASCII ids accepted (Chinese table ids aren't). Now I'll point the Settlement formulas at the renamed `Expenses` table.
Summary computes correctly. Now I'll remove the default empty placeholder table.