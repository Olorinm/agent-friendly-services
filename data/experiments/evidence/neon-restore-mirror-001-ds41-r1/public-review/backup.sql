-- Logical backup of personal todo application
-- Source database: neondb@project [SERVICE_SECRET] (PostgreSQL 17.11)
-- Dumped at: 2026-10-08T17:00:12Z (UTC)
-- Format: plain SQL (schema + data), restorable with psql or any compat. engine
-- Content: CREATE TABLE for lists, todos + all rows.
--       Empty string is stored as '' and NULL is stored as NULL; distinction preserved.

BEGIN;

-- ---------- table: public.lists ----------
CREATE TABLE public."lists" (
  "id" integer NOT NULL,
  "name" text NOT NULL,
  PRIMARY KEY ("id")
);

INSERT INTO public."lists" ("id", "name") VALUES (1, '生活');
INSERT INTO public."lists" ("id", "name") VALUES (2, '学习');

-- ---------- table: public.todos ----------
CREATE TABLE public."todos" (
  "id" integer NOT NULL,
  "list_id" integer NOT NULL,
  "title" text NOT NULL,
  "done" boolean DEFAULT false NOT NULL,
  "note" text,
  PRIMARY KEY ("id")
);

INSERT INTO public."todos" ("id", "list_id", "title", "done", "note") VALUES (101, 1, '买牛奶', false, NULL);
INSERT INTO public."todos" ("id", "list_id", "title", "done", "note") VALUES (102, 1, '预约自行车保养', false, '周六上午');
INSERT INTO public."todos" ("id", "list_id", "title", "done", "note") VALUES (103, 2, 'Read "Designing Data-Intensive Applications"', true, '');
INSERT INTO public."todos" ("id", "list_id", "title", "done", "note") VALUES (104, 2, '复习 SQL 事务', false, '先读笔记，再做练习');
INSERT INTO public."todos" ("id", "list_id", "title", "done", "note") VALUES (105, 1, '给绿植浇水', true, NULL);

ALTER TABLE public."todos" ADD CONSTRAINT "todos_list_id_fkey" FOREIGN KEY ("list_id") REFERENCES public."lists" ("id");

COMMIT;
