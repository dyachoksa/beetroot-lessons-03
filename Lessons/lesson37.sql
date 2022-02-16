-- Language: SQL
-- Variations:
-- DDL - Data Definition Language
--     CREATE TABLE, CREATE INDEX, CREATE DATABASE ...
-- DML - Data Manipulation Language
--     INSERT, UPDATE or DELETE
-- DQL - Data Query Language
--     SELECT

-- contacts table:
-- id  |  name        |  email                  |  address              |  notes  |
-- ----------------------------------------------
-- 1   |  Kirk James  | kirk.james@example.com  |  9012 Walnut Hill Ln  |  "Mobile: `(139)-249-2194`

DROP TABLE IF EXISTS contacts;

CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    notes TEXT DEFAULT '- no notes -',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_contacts_email ON contacts (email);
CREATE INDEX idx_contacts_created_at ON contacts (created_at);

INSERT INTO contacts (name, email, address, notes)
VALUES
    ('Kirk James', 'kirk.james@example.com', '9012 Walnut Hill Ln', 'Mobile: `(139)-249-2194`\n\n'),
    ('Brittany Oliver', 'brittany.oliver@example.com', '3760 Lovers Ln', NULL);

SELECT * FROM contacts;
SELECT name, email, created_at FROM contacts;
SELECT * FROM contacts WHERE email = 'kirk.james@example.com';
SELECT id FROM contacts WHERE email = 'kirk.james@example.com';
SELECT name FROM contacts WHERE id = 1;
SELECT * FROM contacts WHERE email LIKE 'brit%' AND created_at < '2022-02-16 18:49:42';
SELECT * FROM contacts WHERE email LIKE '%kirk%' OR name LIKE '%kirk%';