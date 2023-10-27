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

INSERT INTO recipes (name, path)
VALUES
    ('carne_asada', '../static/image/recipes/recipe1.png'),
    ('greek_rib', '../static/image/recipes/recipe2.png'),
    ('vegetable_soup', '../static/image/recipes/recipe3.png'),
    ('banana_pancake', '../static/image/recipes/recipe4.png'),
    ('carne_asada', '../static/image/recipes/recipe5.png'),
    ('carne_asada', '../static/image/recipes/recipe6.png');
