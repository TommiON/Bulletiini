# Käyttöohje

## Verkkosovellus

Bulletiini on verkkosovellus eikä sellaisenaan vaadi asentamista. Sovellus löytyy [Herokusta](https://bulletiini.herokuapp.com/). Sovellukseen pääsee kirjautumaan testitunnuksella "testi" ja salasanalla "testi", jolla saa käyttöönsä ylläpitäjän oikeudet. Osa toiminallisuudesta (viestien lukeminen, käyttäjälista) on saatavilla myös ilman kirjautumista.

## Paikallinen asentaminen

Sovelluksen voi myös asentaa omaan käyttöön esim. localhost-palvelimella toimivaksi:

* [Asenna Python](https://www.python.org/downloads/) jos se ei ole jo asennettu.
* Luo sovellukselle hakemisto haluamaasi paikkaan ja lataa Bulletiini-repositorion sisältö sinne.
* Mene äsken luomaasi sovelluksen juurihakemistoon ja asenna tarvittavat riippuvuudet (ennen kaikkea Flask-kirjasto) komennolla ``pip install -r requirements.txt``.
* Käynnistä sovellus application-hakemistosta löytyvällä skriptillä komennolla ``python run.py``.

## Sovelluksen perustoiminnot

Sovelluksen perustoiminnot löytyvät yläpalkista:

![](bulletin_ui.png)

* _Bulletiini_ palauttaa kaikista näkymistä takaisin etusivulle, jossa näytetään 10 tuoreinta viestiä.
* _Luo käyttäjätunnus_ -kohdasta pääsee luomaan käyttäjätunnuksen. Luodulle käyttäjätunnukselle annetaan perustasoiset oikeudet, ja vain ylläpito-oikeuksin varustetut käyttäjät voivat tehdä muista käyttäjistä ylläpitäjiä.
* _Keskustelut_ -välilehti näyttää kaikki Bulletiinin keskusteluketjut. Yksittäistä ketjunnimeä klikkaamalla saa näkyville kyseisen ketjun viestit ja viestin otsikkoa klikkaamalla edelleen kyseisen viestin tarkempaan näkymään. Keskusteluketjulistauksen ylälaidan _Aloita uusi keskusteluketju_-kohdasta voi aloittaa uuden keskusteluketjun, yksittäisen keskusteluketjunäkymän ylälaidan _Vastaa tähän keskusteluketjuun_-kohdasta puolestaan voi lisätä uuden viestin olemassaolevaan ketjuun. Käyttäjä voi muokata ja poistaa omia viestejään, mutta ainoastaan lukea muiden viestejä (poikkeuksena ylläpitäjät, joilla pääsy kaikkeen). Muokkaus- ja poistotoiminnot on saavutettavissa sekä viestiketjun että yksittäisen viestin näkymästä. Lisäksi _Keskustelut_-sivun ylälaidassa on foorumille määriteltyjen aihepiirien nimet, joita klikkaamalla näkymään suodatetaan vain ne ketjut, joiden aihepiireihin kyseinen aihe on merkitty.
* _Aihepiirit_ -välilehdeltä tavallinen käyttäjä näkee sovelluksen tarjoamat aiheet. Ylläpitokäyttäjä pääsee myös lisäämään ja poistamaan niitä.
* _Käyttäjät_-välilehdeltä näkee sovellukseen rekisteröityneet käyttäjät. Käyttäjänimeä klikkaamalla saa tarkemmat tiedot kyseisestä käyttäjästä. Ylläpito-oikeuksin varustetulle käyttäjälle on sekä käyttäjälistassa että yksittäisen käyttäjän näkymässä tarjolla toiminnot käyttoikeuksien muuttamiseen sekä käyttäjätilin poistamiseen.
* _Tilastot_-välilehti tarjoaa tilastotietoa Bulletiinista.
