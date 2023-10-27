DROP DATABASE IF EXISTS recipe_web;

CREATE DATABASE recipe_web CHARACTER SET utf8 COLLATE utf8_general_ci;

USE recipe_web;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    password VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci,
    photo VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci );

INSERT INTO users (name, password)
VALUES
    ('123456', '123456');

CREATE TABLE recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    path VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci
);

INSERT INTO recipes (name, path, type)
VALUES
    ('noodle', '../static/image/recipes/recipe1.png', eastern),
    ('skewers', '../static/image/recipes/recipe2.png', eastern),
    ('beef_brisket_with_tomatop', '../static/image/recipes/recipe3.png', western),
    ('pizza', '../static/image/recipes/recipe4.png', western),
    ('dessert', '../static/image/recipes/recipe5.png', western),
    ('macaron', '../static/image/recipes/recipe6.png', western);
