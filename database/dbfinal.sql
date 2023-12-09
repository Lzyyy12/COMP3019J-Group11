DROP DATABASE IF EXISTS recipe_web;

CREATE DATABASE recipe_web CHARACTER SET utf8 COLLATE utf8_general_ci;

USE recipe_web;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    password VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci,
    photo VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci,
    type INT);

DROP TABLE IF EXISTS recipes;
CREATE TABLE recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    user_id INT NOT NULL,
    path VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci, 
    type VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci,
    description VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS ingredient;
CREATE TABLE ingredient(
    id INT AUTO_INCREMENT PRIMARY KEY,
    recipe_id INT NOT NULL,
    name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    amount VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci,
    FOREIGN KEY (recipe_id) REFERENCES recipes(id)
);

DROP TABLE IF EXISTS favorites;
CREATE TABLE favorites(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    recipe_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (recipe_id) REFERENCES recipes(id)
);

INSERT INTO users (name, password, type)
VALUES
    ('123456', '123456', '1');

INSERT INTO recipes (name, user_id, path, type)
VALUES
    ('noodle', '1', '../static/image/recipes/recipe1.png', 'eastern'),
    ('skewers', '1', '../static/image/recipes/recipe2.png', 'eastern'),
    ('beef_brisket_with_tomatop', '1', '../static/image/recipes/recipe3.png', 'western'),
    ('pizza', '1', '../static/image/recipes/recipe4.png', 'western'),
    ('dessert', '1', '../static/image/recipes/recipe5.png', 'western'),
    ('macaron', '1', '../static/image/recipes/recipe6.png', 'western');

INSERT INTO ingredient (recipe_id, name, amount)
VALUES
    ('1', 'meat', '50g'),
    ('1', 'flower', '50g'),
    ('1', 'egg', '2'),
    ('2', 'vegetable', '200g'),
    ('2', 'egg', '1');