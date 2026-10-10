核对完成（Django 5.2.6，PyPI），来源为指定服务 GitHub Global Advisories 匿名 REST API：

| CVE | GHSA | 5.2.x 受影响范围 | 5.2.x 最早修复 | 5.2.6 是否受影响 |
|---|---|---|---|---|
| CVE-2025-57833 | GHSA-6w2r-r2m5-xq5w | `>= 5.2a1, < 5.2.6` | 5.2.6 | 否 |
| CVE-2025-59681 | GHSA-hpr9-3m2g-3j9p | `>= 5.2, < 5.2.7` | 5.2.7 | 是 |

仅处理这两条至少需升级到 **5.2.7**（5.2.6 已覆盖前者，但落在后者 `>= 5.2, < 5.2.7` 内）。

依据链接（服务返回的 html_url 及维护者发布记录）：
- https://github.com/advisories/GHSA-6w2r-r2m5-xq5w ｜ https://www.djangoproject.com/weblog/2025/sep/03/security-releases
- https://github.com/advisories/GHSA-hpr9-3m2g-3j9p ｜ https://www.djangoproject.com/weblog/2025/oct/01/security-releases

明细与原始响应见 `result.md`、`cve-2025-*.json`。未安装或修改项目。