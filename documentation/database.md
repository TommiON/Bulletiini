# Tietokannan kuvaus

## Tietokantakaavio

![](Tietokantakaavio.png)

## Huomioita tietokannasta

Tietokannassa on neljä varsinaista tietokohdetta (Käyttäjä, Viesti, Keskusteluketju ja Aihepiiri) ja lisäksi Keskusteluketjun ja Aihepiirin monesta moneen -yhteyttä hoitava liitostaulu. Kahdessa tietokannan taulussa (Käyttäjä ja Viesti) on täysi CRUD-toiminnallisuus. Kaikki tietokannan entiteetit ovat kolmannessa normaalimuodossa.

Sovellus käyttää Herokussa PostgreSQL-tietokantaa, mutta paikallisesti sovellusta on kehitetty SQLite:n varassa. Tästä seurasi kehityksen kuluessa lukuisia ongelmia, koska näemmä PostgreSQL suhtautuu huomattavasti tiukemmin tietokannan integriteettiin (esim. viittaukset ei-minnekään) kuin SQLite. Näin ollen paikallisessa kehityksessä toimivaksi kuvitellut seikat osoittautuivatkin usein "tuotantoympäristössä" toimimattomiksi ja seurasi työlästä buginmetsästystä. Todennäköisesti parempi lähestymistapa olisi ollut käyttää PostgreSQL:aa kehityksessä myös paikallisesti.

SQLite/PostgreSQL-ristiinvedon ja ajanpuutteen vuoksi sovellukseen myös jäi yksi epätyydyttävästi toimiva ominaisuus, josta lisää [puutedokumentissa](puutteet.md).

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

