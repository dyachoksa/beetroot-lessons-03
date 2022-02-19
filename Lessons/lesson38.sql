-- users: id, name, email, password
-- profile: bio, profile_image
-- posts: id, title, content, published_at
-- tags: id, name

-- user can have only one profile (one-to-one relation)
-- user can have several posts (one-to-many)
-- post can have several tags as well as tag can be assigned to several posts (many-to-many)

PRAGMA foreign_keys;
PRAGMA foreign_keys = ON;

-- DDL
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT DEFAULT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS profiles;
CREATE TABLE IF NOT EXISTS profiles (
    user_id INTEGER PRIMARY KEY, -- or NOT NULL UNIQUE
    bio TEXT NOT NULL,
    profile_image TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS posts;
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users (id) ON DELETE RESTRICT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    published_at DATETIME,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX 'idx_post_author' ON posts(user_id);
CREATE INDEX 'idx_post_published_date' ON posts (published_at DESC);

DROP TABLE IF EXISTS tags;
CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS post_tags;
CREATE TABLE IF NOT EXISTS post_tags (
    post_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,

    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags (id) ON DELETE CASCADE
);

CREATE INDEX 'idx_post_tags_post' ON post_tags (post_id);
CREATE INDEX 'idx_post_tags_tag' ON post_tags (tag_id);

-- DML
-- users
INSERT INTO users (name, email, password)
VALUES ('Alice Simmons', 'alice.simmons@example.com', NULL),
       ('Guy Bowman', 'guy.bowman@example.com', 'bullseye');

-- profiles
INSERT INTO profiles (user_id, bio, profile_image)
VALUES (2, 'My birthday is 10/2/1979', 'https://randomuser.me/api/portraits/men/24.jpg');

INSERT INTO profiles (user_id, bio, profile_image)
VALUES (100, 'Some bio', 'profile pic url');

-- tags
INSERT INTO tags (name) VALUES ('python'), ('web'), ('travel');

-- posts
INSERT INTO posts (user_id, title, content, published_at)
VALUES (1, 'Alice Post 1', 'Post content #1', NULL),
       (1, 'Alice Post 2', 'Post content #2', CURRENT_TIMESTAMP),
       (2, 'Guy Post 1', 'Post content #3', '2022-02-18 10:16:02');

-- post tags
INSERT INTO post_tags (post_id, tag_id)
VALUES (1, 1), (2, 1), (2, 3), (3, 2);

DELETE FROM users WHERE id = 2;

DELETE FROM tags WHERE id = 3;

-- DQL
SELECT * FROM users ORDER BY name DESC;

SELECT
    u.id AS "user_id",
    u.name AS "user_name",
    p.bio AS "user_bio",
    p.profile_image AS "user_image"
FROM users AS u
    LEFT JOIN profiles p on u.id = p.user_id
ORDER BY u.name;

SELECT
    p.id AS "post_id",
    p.title AS "post_title",
    u.name AS "author_name"
FROM posts AS p
    INNER JOIN users AS u ON p.user_id = u.id
WHERE p.published_at IS NOT NULL
ORDER BY p.published_at DESC;

SELECT
    t.name
FROM tags AS t
    INNER JOIN post_tags AS pt ON t.id = pt.tag_id
    INNER JOIN posts AS p ON pt.post_id = p.id
WHERE p.title = 'Alice Post 2';
