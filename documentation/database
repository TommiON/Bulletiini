# Tietokannan kuvaus


## Taulujen SQL-lauseet

```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	username VARCHAR(30) NOT NULL, 
	password VARCHAR(30) NOT NULL, 
	is_admin BOOLEAN NOT NULL, 
	joined DATETIME, 
	PRIMARY KEY (id), 
	CHECK (is_admin IN (0, 1))
)
```
