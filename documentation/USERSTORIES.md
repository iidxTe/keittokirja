# User stories


#### As a user I want to register with a name and a password

INSERT INTO account (date_created, date_modified, name, password, role_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)

---

#### As a user I want to login into the application

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.password AS account_password, account.role_id AS account_role_id 
FROM account 
WHERE account.name = ? AND account.password = ?

---

#### As a user I want to add recipes

INSERT INTO recipe (date_created, date_modified, header, category, description, directions, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)

---

As a user I want to change/update recipes:

UPDATE recipe SET date_modified=CURRENT_TIMESTAMP, header=?, category=?, description=?, directions=? WHERE recipe.id = ?

---

#### As a user I want to delete recipes

DELETE FROM recipe WHERE recipe.id = ?

---

#### As a user I want to see the recipes I have added

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.password AS account_password, account.role_id AS account_role_id 
FROM account 
WHERE account.id = ?

---

#### As a user I want to browse the recipes by their category (ei vielä totetutettu)

---

#### As a user I want to search the recipes by an ingredient (ei vielä totetutettu)

---

#### As a user I want to log out of the application

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.password AS account_password, account.role_id AS account_role_id 
FROM account 
WHERE account.id = ?

