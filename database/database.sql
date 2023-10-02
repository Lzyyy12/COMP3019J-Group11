CREATE DATABASE Manage CHARACTER SET utf8 COLLATE utf8_general_ci;

USE Manage;

DROP TABLE IF EXISTS User;
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    password VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    photo BLOB NOT NULL
);

DROP TABLE IF EXISTS Recipe;
CREATE TABLE Recipe (
    recipe_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    recipe_name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    category VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    description TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

DROP TABLE IF EXISTS Picture;
CREATE TABLE Picture (
    picture_id INT AUTO_INCREMENT PRIMARY KEY,
    recipe_id INT NOT NULL,
    picture BLOB NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id)
);

DROP TABLE IF EXISTS Ingredient;
CREATE TABLE Ingredient (
    ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
    ingredient_name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
);

DROP TABLE IF EXISTS Ing_Rcp;
CREATE TABLE Ing_Rcp (
    ingredient_id INT NOT NULL,
    recipe_id INT NOT NULL,
    amount VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id),
    FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id)
);

DROP TABLE IF EXISTS User_Rcp;
CREATE TABLE User_Rcp (
    user_id INT NOT NULL,
    recipe_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (recipe_id) REFERENCES Recipe(recipe_id)
);