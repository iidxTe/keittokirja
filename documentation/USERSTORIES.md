# User stories


#### As a user I want to register with a name and a password

INSERT INTO account (date_created, date_modified, name, password) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)

---

#### As a user I want to login into the application

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.password AS account_password 
FROM account 
WHERE account.name = ? AND account.password = ?

---

#### As a user I want to see my own info

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.password AS account_password 
FROM account 
WHERE account.id = ?

SELECT COUNT( * ) FROM Recipe WHERE account_id = ?

---

#### As a user I want to change my name and/or password

UPDATE account SET date_modified=CURRENT_TIMESTAMP, name=?, password=? WHERE account.id = ?

---

#### As a user I want to delete my profile

DELETE FROM account WHERE account.id = ?

---

#### As a user I want to add recipes

INSERT INTO recipe (date_created, date_modified, header, category, description, directions, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)

---

#### As a user I want to update a recipe:

UPDATE recipe SET date_modified=CURRENT_TIMESTAMP, directions=? WHERE recipe.id = ?

---

#### As a user I want to delete recipes

DELETE FROM recipe_ingredient WHERE recipe_ingredient.id = ?

DELETE FROM recipe WHERE recipe.id = ?

---

#### As a user I want to see the recipes I have added

SELECT recipe.id AS recipe_id, recipe.date_created AS recipe_date_created, recipe.date_modified AS recipe_date_modified, recipe.header AS recipe_header, recipe.category AS recipe_category, recipe.description AS recipe_description, recipe.directions AS recipe_directions, recipe.account_id AS recipe_account_id 
FROM recipe 
WHERE recipe.account_id = ?

---

#### As a user I want to see statistics

SELECT Account.name, COUNT(Recipe.account_id) FROM Account LEFT JOIN Recipe ON Account.id = Recipe.account_id GROUP BY Account.id, Recipe.account_id

SELECT Ingredient.name, COUNT(Recipe_Ingredient.ingredient_id) FROM Ingredient LEFT JOIN Recipe_Ingredient ON Ingredient.id = Recipe_Ingredient.ingredient_id GROUP BY Ingredient.id, Recipe_Ingredient.ingredient_id

---

#### As a user I want to log out of the application

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.password AS account_password 
FROM account 
WHERE account.id = ?


