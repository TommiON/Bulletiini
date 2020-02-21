# Käyttöohje

_(Täydentyy...)_

## Verkkosovellus

Bulletiini on verkkosovellus eikä sellaisenaan vaadi asentamista. Sovellus löytyy [Herokusta](https://bulletiini.herokuapp.com/). Sovellukseen pääsee kirjautumaan testitunnuksella "testi" ja salasanalla "testi", jolla saa käyttöönsä ylläpitäjän oikeudet. Osa toiminallisuudesta (viestien lukeminen, käyttäjälista) on saatavilla myös ilman kirjautumista.

## Asentaminen

Sovelluksen voi myös asentaa omaan käyttöön esim. localhost-palvelimella toimivaksi:

* [Asenna Python](https://www.python.org/downloads/) jos se ei ole jo asennettu.
* Luo sovellukselle hakemisto haluamaasi paikkaan ja lataa Bulletiini-repositorion sisältö sinne.
* Mene äsken luomaasi sovelluksen juurihakemistoon ja asenna tarvittavat riippuvuudet (ennen kaikkea Flask-kirjasto) komennolla ``pip install -r requirements.txt``.
* Käynnistä sovellus application-hakemistosta löytyvällä skriptillä komennolla ``python run.py``.

## Sovelluksen perustoiminnot

Sovelluksen perustoiminnot löytyvät yläpalkista:

![](bulletin_ui.png)

* _Bulletiini_ palauttaa kaikista näkymistä takaisin etusivulle, jossa näytetään 10 tuoreinta viestiä.
* _Luo käyttäjätunnus_ -kohdasta pääsee luomaan käyttäjätunnuksen. Luodulle käyttäjätunnukselle annetaan perustasoiset oikeudet.
* _Keskustelut_ -välilehti näyttää kaikki Bulletiinin keskusteluketjut. Yksittäistä ketjunnimeä klikkaamalla saa näkyville kyseisen ketjun viestit. Käyttäjä voi muokata ja poistaa omia viestejään.
* _Aihepiirit_ -välilehdeltä tavallinen käyttäjä näkee sovelluksen tarjoamat aiheet ja ylläpitokäyttäjä pääsee myös lisäämään ja poistamaan niitä.
* _Käyttäjät_-välilehdeltä näkee sovellukseen rekisteröityneet käyttäjät. Käyttäjänimeä klikkaamalla saa tarkemmat tiedot kyseisestä käyttäjästä.
* _Tilastot_-välilehti tarjoaa tilastotietoa Bulletiinista.

_täydentyy..._

