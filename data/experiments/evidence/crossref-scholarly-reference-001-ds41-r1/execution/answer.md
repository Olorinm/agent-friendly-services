CLUE MATCHED. 第一条请求即命中，再用 DOI 端点核对完整书目。
已完成。通过指定服务 CrossRef REST API（`https://api.crossref.org/works`）检索并核对，命中唯一同时满足全部线索的论文。

**文献条目**
- 原文题名：Deep learning
- 全部作者（原顺序）：Yann LeCun; Yoshua Bengio; Geoffrey Hinton
- 发表年份：2015
- 期刊名：Nature
- DOI 链接：https://doi.org/10.1038/nature14539

**匹配理由（中文）**
以 `deep learning` + 作者 `Bengio` + 出版年 2015 检索，返回结果中唯一同时满足「2015 年、期刊 Nature、作者姓 Bengio、题名含 deep learning」四条线索的记录是 DOI `10.1038/nature14539`。其他候选或年份/期刊不符，或仅为会议论文/特刊社论。再请求 `works/10.1038/nature14539` 核对 DOI 记录，确认作者共 3 人且顺序为 LeCun、Bengio、Hinton。

**检索来源**
- 服务：CrossRef REST API，入口 `https://api.crossref.org/works`
- 检索：`?query.bibliographic=deep learning&query.author=Bengio&filter=from-pub-date:2015-01-01,until-pub-date:2015-12-31`
- 核对：`/works/10.1038/nature14539`
- 原始响应与完整说明：本工作目录 `resp_r1.json`、`resp_r2.json`、`answer.md`

补充（非必需）：卷 521，期 7553，页 436–444，出版日期 2015-05-27。共使用 2 次 API 请求，遵守 5 秒间隔与匿名公共路径限制。