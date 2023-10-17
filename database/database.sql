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

INSERT INTO User (username, password, photo)
VALUES
    ('user1', 'password1', 'photo1'),
    ('user2', 'password2', 'photo2'),
    ('user3', 'password3', 'photo3'),
    ('user4', 'password4', 'photo4'),
    ('user5', 'password5', 'photo5');

INSERT INTO Recipe (user_id, recipe_name, category, description)
VALUES
    (1, 'Chinese Pork Dumpling', 'Eastern', 'These tasty steamed pork dumplings make a perfect appetizer for a party or you can serve them as a main dish.'),
    (2, 'Chinese Spring Roll', 'Eastern', 'Spring rolls are fried Chinese pastries. Spring rolls are usually eaten during the Spring Festival in China, hence the name. Best served at once, hot and crispy, with sweet and sour sauce for dipping.'),
    (3, 'Tamagoyaki - Japanese Rolled Omelette', 'Eastern', 'Tamagoyaki is a classic Japanese omelette, slightly sweet and seasoned with soy sauce, mirin, and dashi stock.'),
    (4, 'Chinese Fried Noodles', 'Eastern', 'These fried noodles are a quick, easy, and delicious recipe that all will enjoy. Try adding cooked, cubed pork or chicken. Bean sprouts, water chestnuts, sliced almonds, or any of your favorite vegetables can also be added to this versatile recipe.'),
    (5, 'British Pancake', 'Western', 'Perfect pancakes are easier to make than you think. This pancake recipe produces thick, fluffy, and all-around delicious pancakes with just a few ingredients that are probably already in your kitchen and it is so much better than the boxed stuff.'),
    (1, 'Bazlama - Turkish Flat Bread', 'Turkish', 'Bazlama is a simple and delicious village bread that I learned to prepare after moving to Turkey. Normally it is cooked in an outdoor oven but it works just as well on the stove top. It is best served warm.');

INSERT INTO Picture (recipe_id, picture)
VALUES
    (1, 'dumpling_pic'),
    (2, 'spring_roll_pic'),
    (3, 'omelette_pic'),
    (4, 'noodle_pic'),
    (5, 'pancake_pic'),
    (6, 'bazlama_pic');

INSERT INTO Ingredient (ingredient_name)
VALUES
    ('Egg'),
    ('White Sugar'),
    ('Sweet Wine'),
    ('Soy Sauce'),
    ('Vegetable Oil');

INSERT INTO Ing_Rcp (ingredient_id, recipe_id, amount)
VALUES
    (1, 3, '4'),
    (2, 3, '1 tablespoon'),
    (3, 3, '1 teaspoon'),
    (4, 3, '1/2 teaspoon'),
    (5, 3, '1/2 tablespoon');

INSERT INTO User_Rcp (user_id, recipe_id)
VALUES
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 4);