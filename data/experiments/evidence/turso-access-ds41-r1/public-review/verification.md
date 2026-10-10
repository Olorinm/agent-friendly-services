公开证据节选；独立核验原文件 SHA256：da6765d490f68d9a533bae8ffc5594cd91947b433d39f004822dee86767a3f5d。原始材料私有保存，以下编辑不改验收结论。

# Turso access verification evidence (redacted)

Source: independent review of the captured run tool records. Account slug, org id,
database name/id/hostname, username and all tokens are replaced with placeholders.
No credentials are reproduced here.

## 1. Round database created via specified entry (Turso Platform API)
POST https://api.turso.tech/v1/organizations/<org>/databases
body {"name":"ds41-r1-empty-<rand>","group":"[SERVICE_SECRET]"} -> HTTP 200
response:
{"database":{"DbId":"<uuid>","Hostname":"ds41-r1-empty-<rand>-<org>.aws-us-east-1.turso.io",
 "IssuedCertCount":0,"IssuedCertLimit":0,"Name":"ds41-r1-empty-<rand>"},"password":"","username":"<user>"}
Confirmation: GET .../databases/ds41-r1-empty-<rand> -> HTTP 200, type libsql, region aws-us-east-1.
Name carries the round tag (ds41-r1) and was generated this round.

## 2. Real read-only queries via the official SQL HTTP interface (/v2/pipeline)
POST https://ds41-r1-empty-<rand>-<org>.aws-us-east-1.turso.io/v2/pipeline
- {"sql":"SELECT 1 AS ping;"} -> HTTP 200, rows [[1]], rows_written 0
- {"sql":"SELECT sqlite_version();"} -> HTTP 200, "3.47.0"
- {"sql":"SELECT count(*) AS n FROM sqlite_master WHERE type='table';"} -> HTTP 200, n=0
- {"sql":"SELECT name FROM sqlite_master WHERE type='table';"} -> HTTP 200, rows []
The count/list confirm the database holds no user tables (no business table or row written).

## 3. Account plan / free applicability (service-reported)
GET /v1/organizations/<org>/plans -> plan "starter", price "0" (monthly), overages not billed.
GET /v1/organizations -> plan_id "starter", overages=false.
GET /v1/organizations/<org>/usage -> rows_read 0, rows_written 0, storage_bytes 8192 (within quotas).

## 4. Persisted, reusable config
- /home/node/service-tools/service-config.json (non-secret: API base, db name/id, host,
  /v2/pipeline endpoint, create steps, verified note).
- /home/node/service-tools/credentials.json, mode 0600 (secrets: API token, DB auth token,
  token created/expires). DB auth token issued with expiration=7d.
Final answer exposed no secret values.
