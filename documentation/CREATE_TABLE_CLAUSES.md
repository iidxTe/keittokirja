CREATE TABLE ingredient (
	id INTEGER NOT NULL, 
	name VARCHAR(200) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
)

CREATE TABLE recipe (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	header VARCHAR(200) NOT NULL, 
	category VARCHAR(100) NOT NULL, 
	description VARCHAR(1000), 
	directions VARCHAR(10000) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)

CREATE TABLE recipe_ingredient (
	id INTEGER NOT NULL, 
	amount FLOAT, 
	unit VARCHAR(200), 
	recipe_id INTEGER NOT NULL, 
	ingredient_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(recipe_id) REFERENCES recipe (id), 
	FOREIGN KEY(ingredient_id) REFERENCES ingredient (id)
)

