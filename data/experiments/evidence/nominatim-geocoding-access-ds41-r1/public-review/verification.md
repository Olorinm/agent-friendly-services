公开证据节选；独立核验原文件 SHA256：e7b441a368075fd77c1585624568fabed377f93dfa0a631405f7c3fa0dba870f。原始材料私有保存，以下编辑不改验收结论。

# 指定入口网络失败核验摘要（摘自原始运行日志，已脱敏）

任务：geocoding-access-001/v1；指定入口：https://nominatim.openstreetmap.org/search

## 执行者对本入口的调用尝试与结果
- python urllib（geocode.py）：`OSError: [Errno 101] Network is unreachable`
- curl -4 入口 `?q=Eiffel+Tower,+Paris,+France`：`curl: (28) Connection timed out after 25000 milliseconds`，HTTP 000
- curl 入口 `/status`：连接超时（约 20s 无响应）
- curl `http://nominatim.openstreetmap.org/search?q=test`：HTTP 000
- webfetch 入口同一查询 URL：`Request timed out`
- curl 入口 `?q=test` 重试 3 次：均为 HTTP 000

## 同一容器内的 DNS 与连通性对照
- `getent hosts nominatim.openstreetmap.org` → `2a03:2880:f10d:183:face:b00c:0:25de`（Facebook 段）
- 随后 `getent ahostsv4` → `174.36.196.242`，再查为 `69.63.184.142`
- `getaddrinfo` 连续返回 `31.13.84.2` / `128.242.245.212` / `162.125.80.6`（轮换，且与 OSM 无关）
- 可达对照：example.com HTTP 200；api.github.com HTTP 200；nominatim.org HTTP 200；operations.osmfoundation.org HTTP 200
- 同批被阻断：www.openstreetmap.org HTTP 000；www.google.com HTTP 000

## 交付物状态
- 工作目录未产生 `result.json`，无 `cache/` 目录；`last_request.json` 仅记录一次尝试时间 `2026-10-08T15:17:00Z`
- 会话在开始后约 290 秒被终止：`exit_code=-15`，`timed_out=true`
- `answer.md` 仅剩一句未完成片段，无地点、坐标、来源或配置位置说明

公开地点数据来源：[Photon / komoot](https://photon.komoot.io/) 与 [OpenStreetMap contributors](https://www.openstreetmap.org/copyright)，按 [ODbL](https://opendatacommons.org/licenses/odbl/) 许可标注来源。变动：选取任务相关字段，中文说明和坐标距离计算；不代表服务方背书。Nominatim无成功响应，因此其记录没有可发布的服务地点数据。

总控复核限制：独立验收同时记录执行者约9次入口尝试，超过本轮4次上限；不能把所有诊断尝试称为合规。网络错误是本次真实查询未能发生的直接阻碍，实际根因未定位到具体DNS配置、出口设备或服务方。后续仅做DNS查询（未再查地理编码API）时，宿主机与该容器均出现异常轮换地址，不能据此断言只有容器配置有问题。失败原始用量不完整，模型费保持未知并保留上限预留。没有继续派发本服务的业务题；不作为服务失败或准确性样本。
