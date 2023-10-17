DROP DATABASE IF EXISTS recipe_web;

CREATE DATABASE recipe_web CHARACTER SET utf8 COLLATE utf8_general_ci;

USE recipe_web;

DROP TABLE IF EXISTS User;
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    password VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci,
    photo VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci
);

INSERT INTO User (username, password)
VALUES
    ('user', '123')