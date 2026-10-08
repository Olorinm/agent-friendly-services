Now I'll create the tables in the specified document.
Tables created. Now add the six expense records and the settlement row.
Formula error on `Expenses.Amount` — cross-table aggregation needs `.all`. Let me fix the `Total` formula.
Let me run a diagnostic on the formula engine.
Found it: this doc's RecordSets need generator iteration. Let me update all formulas.
Now let me round the net value and check the document's pages so the user can keep entering data.
Let me check the API spec for table modify/delete and record endpoints before restructuring for UI usability.
Pages were auto-created for each table, so no restructure needed. Let me verify the final server-computed values.