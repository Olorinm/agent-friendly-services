Now let me fetch the page via the specified Jina Reader service.
I have the 2027 table. Now let me generate the CSV via a parser script to avoid transcription errors.
完成。已通过指定服务 Jina Reader (`https://r.jina.ai/`) 抓取 OPM 官方页面（1 次请求，HTTP 200），从“2027 Holiday Schedule”表提取全部 11 条假日，脚注标记（`*`/`**`）已去除，按日期排序输出。

交付文件：`[WORKSPACE]/opm_2027_holidays.csv`（UTF-8，列 `date,weekday,holiday`）

| date | weekday | holiday |
|---|---|---|
| 2027-01-01 | Friday | New Year’s Day |
| 2027-01-18 | Monday | Birthday of Martin Luther King, Jr. |
| 2027-02-15 | Monday | Washington’s Birthday |
| 2027-05-31 | Monday | Memorial Day |
| 2027-06-18 | Friday | Juneteenth National Independence Day |
| 2027-07-05 | Monday | Independence Day |
| 2027-09-06 | Monday | Labor Day |
| 2027-10-11 | Monday | Columbus Day |
| 2027-11-11 | Thursday | Veterans Day |
| 2027-11-25 | Thursday | Thanksgiving Day |
| 2027-12-24 | Friday | Christmas Day |

来源：https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/ （2027 Holiday Schedule 表）
原始抓取内容存于同目录 `opm_2027_raw.txt`，解析脚本 `extract_2027.py`。日期均按表中公布值记录（如 Independence Day 记为 2027-07-05），未换算为节日日历日。