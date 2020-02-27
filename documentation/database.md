# Tietokannan kuvaus

## Tietokantakaavio

![](Tietokantakaavio.png)

## Huomioita tietokannassa

Sovellus käyttää Herokussa PostgreSQL-tietokantaa, mutta paikallisesti sovellusta on kehitetty SQLite:n varassa. Tästä seurasi 

Kahdessa tietokannan taulussa (Account ja Message) on täysi CRUD-toiminnallisuus.

Kaikki tietokannan entiteetit ovat kolmannessa normaalimuodossa.

## Taulujen CREATE TABLE -lauseet

Käyttäjä (User-entiteetin nimi tietokantatauluna on Account):
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


Aihepiiri:
```
CREATE TABLE topic (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	PRIMARY KEY (id)
)
```


Keskusteluketju:
```
CREATE TABLE thread (
	id INTEGER NOT NULL, 
	title VARCHAR(50) NOT NULL, 
	time_of_opening DATETIME, 
	author_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(author_id) REFERENCES account (id)
)
```


Viesti:
```
CREATE TABLE message (
	id INTEGER NOT NULL, 
	title VARCHAR(50) NOT NULL, 
	content VARCHAR(5000), 
	time_of_sending DATETIME, 
	author_id INTEGER NOT NULL, 
	thread_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(author_id) REFERENCES account (id), 
	FOREIGN KEY(thread_id) REFERENCES thread (id)
)
```


Keskusteluketjun ja aihepiirin liitostaulu:
```
CREATE TABLE "Thread_topic" (
	thread_id INTEGER NOT NULL, 
	topic_id INTEGER NOT NULL, 
	PRIMARY KEY (thread_id, topic_id), 
	FOREIGN KEY(thread_id) REFERENCES thread (id), 
	FOREIGN KEY(topic_id) REFERENCES topic (id)
)
```

