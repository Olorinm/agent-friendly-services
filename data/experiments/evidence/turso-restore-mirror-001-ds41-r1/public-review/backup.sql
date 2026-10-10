-- Turso/libSQL logical backup
-- source db: [SERVICE_SECRET]
-- source db_id: [SERVICE_SECRET]
-- exported_at_utc: 2026-10-08T16:59:54.974983Z
-- dialect: SQLite / libSQL
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE lists (id INTEGER NOT NULL PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE todos (id INTEGER NOT NULL PRIMARY KEY, list_id INTEGER NOT NULL REFERENCES lists(id) ON UPDATE NO ACTION ON DELETE NO ACTION, title TEXT NOT NULL, done BOOLEAN NOT NULL DEFAULT false, note TEXT);
INSERT INTO "lists" ("id","name") VALUES (1,'生活');
INSERT INTO "lists" ("id","name") VALUES (2,'学习');
INSERT INTO "todos" ("id","list_id","title","done","note") VALUES (101,1,'买牛奶',0,NULL);
INSERT INTO "todos" ("id","list_id","title","done","note") VALUES (102,1,'预约自行车保养',0,'周六上午');
INSERT INTO "todos" ("id","list_id","title","done","note") VALUES (103,2,'Read "Designing Data-Intensive Applications"',1,'');
INSERT INTO "todos" ("id","list_id","title","done","note") VALUES (104,2,'复习 SQL 事务',0,'先读笔记，再做练习');
INSERT INTO "todos" ("id","list_id","title","done","note") VALUES (105,1,'给绿植浇水',1,NULL);
COMMIT;
