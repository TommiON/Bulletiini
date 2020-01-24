# Bulletiini
Helsingin yliopiston Tietokantaprojekti-kurssin harjoitustyö.

### Toimivuus- ja bugitilanne 24.1.2020

Sovelluksessa on Herokuun liittyvä bugi, joka ei tällä aikataululla ehtinyt ratketa: GET-pyynnön osoitteeseen _/users_ pitäisi tuottaa lista rekisteröityneistä käyttäjistä, ja tämä toimii ongelmitta paikallisesti, mutta jostakin syystä Herokussa ei. Sen sijaan GET-pyynnöt osoitteeseen _/users/<user_id>_ toimivat myös Herokussa ja tuottavat siis detaljinäkymän yksittäisestä käyttäjästä. Selvittely jatkuu...

### Sovelluksen tarkoitus

Sovellus tarjoaa toiminnallisuuden yksinkertaiselle keskustelufoorumille. Tarkempaa tietoa [käyttötapaus- ja käsitedokumentissa](documentation/usecases.md).

### Tietokantakaavio

![](documentation/Tietokantakaavio.png)

### Heroku-sovelluksen osoite

Sovelluksen tämänhetkinen työversio löytyy [Herokusta](https://bulletiini.herokuapp.com/). Sovellukseen pääsee kirjautumaan testitunnuksella "testi" ja salasanalla "testi". Tämänhetkisessä versiossa kaikki (vähäinen) toiminnallisuus näkyy kuitenkin myös kirjautumattomalle käyttäjälle.
