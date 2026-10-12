两条公告记录已通过指定 API 查得（响应头 `x-ratelimit-remaining` 充足，未触发限流）。结论如下。

## 逐条核对（PyPI / Django，当前 5.2.6）

**CVE-2025-57833**（GHSA-6w2r-r2m5-xq5w）
- 5.2 分支受影响范围：`>= 5.2a1, < 5.2.6`，最早修复版本 `5.2.6`
- 当前 5.2.6 **不在受影响范围内**（5.2.6 正是该分支修复版），此条已处理

**CVE-2025-59681**（GHSA-hpr9-3m2g-3j9p）
- 5.2 分支受影响范围：`>= 5.2, < 5.2.7`，最早修复版本 `5.2.7`
- 当前 5.2.6 **仍在受影响范围内**，此条未处理

## 汇总

- 5.2.x 分支各自最早修复版：CVE-2025-57833 → **5.2.6**；CVE-2025-59681 → **5.2.7**
- 仅处理这两条，至少需升级到 **Django 5.2.7**

## 依据链接（均来自本次 API 记录的引用）

- 公告页：https://github.com/advisories/GHSA-6w2r-r2m5-xq5w ，https://github.com/advisories/GHSA-hpr9-3m2g-3j9p
- 维护者发布记录：https://www.djangoproject.com/weblog/2025/sep/03/security-releases （57833）、https://www.djangoproject.com/weblog/2025/oct/01/security-releases （59681）

原始响应存于当前目录 `resp_57833.json`、`resp_59681.json`（含响应头）。未安装/升级/修改项目。