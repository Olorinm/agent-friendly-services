核对完成（指定服务：OSV 公共 REST API）。

| CVE | 5.2.x 受影响范围 | 5.2.x 最早修复 | 当前 5.2.6 |
|---|---|---|---|
| CVE-2025-57833 | 5.2 ≤ v < 5.2.6 | 5.2.6 | 不受影响（已在修复版本） |
| CVE-2025-59681 | 5.2 ≤ v < 5.2.7 | 5.2.7 | 仍受影响 |

仅处理这两条：升级到 **5.2.7**。

依据（OSV 记录及其内引用）：
- https://api.osv.dev/v1/vulns/CVE-2025-57833
- https://api.osv.dev/v1/vulns/CVE-2025-59681
- 维护者公告 https://www.djangoproject.com/weblog/2025/sep/03/security-releases/ 、 https://www.djangoproject.com/weblog/2025/oct/01/security-releases/

补充：对 Django 5.2.6 的按包/版本查询未返回 CVE-2025-57833、返回了 CVE-2025-59681，与记录 ranges 一致。未安装或修改项目；结果存于 `answer.md`，原始响应在 `cache/`。