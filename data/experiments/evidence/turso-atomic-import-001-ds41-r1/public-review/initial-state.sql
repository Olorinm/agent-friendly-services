CREATE TABLE reject_case (book_id INTEGER PRIMARY KEY NOT NULL, title TEXT NOT NULL);
INSERT INTO reject_case(book_id,title) VALUES (100,'已有书目');
CREATE TABLE accept_case (book_id INTEGER PRIMARY KEY NOT NULL, title TEXT NOT NULL);
INSERT INTO accept_case(book_id,title) VALUES (100,'已有书目');
