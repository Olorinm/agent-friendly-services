The first result matches cleanly. Let me confirm the full record via a free single lookup (DOI) for accurate author order and journal metadata.
已找到并核对，结果写入 `answer.md`。

**文献条目**
- 题名：Deep learning
- 作者（原序）：Yann LeCun、Yoshua Bengio、Geoffrey E. Hinton
- 年份：2015
- 期刊：Nature
- DOI：[10.1038/nature14539](https://doi.org/10.1038/nature14539)

匹配依据：OpenAlex 中 `publication_year:2015 + title.search:"deep learning" + raw_author_name.search:Bengio` 返回 6 条，仅此条同时满足 Nature 与题名完全一致，作者中 Yoshua Bengio 姓 Bengio。检索来源为指定服务 `https://api.openalex.org/works`（列表查询 + DOI 单条核对，原始响应存于本目录 `resp1.json`/`resp2.json`）。仅取公开书目元数据，未下载或概括全文。