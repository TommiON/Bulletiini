# Bulletiini
Helsingin yliopiston Tietokantaprojekti-kurssin harjoitustyö.

# Sovelluksen tarkoitus

Sovellus tarjoaa toiminnallisuuden yksinkertaiselle keskustelufoorumille.

### Keskeiset käsitteet

Avainkäsitteitä ovat Viestit (Message), joista muodostuu Keskusteluketjuja (Thread) ja jotka voivat kuulua yhteen tai useampaan Aiheeseen (Topic). Lisäksi sovelluksessa on tietysti Käyttäjiä (User), joista osa voi olla ylläpito-oikeuksin varustettuja.

### Käyttötapauksia

* Käyttäjä voi aloittaa uuden keskusteluketjun ja kirjoittaa sen ensimmäisen viestin. Uutta keskusteluketjua aloitettaessa viestille voi valita yhden tai useamman aiheen valmiista listasta. Aiheet ovat eräänlaisia leimoja/tageja, jotka kuvaavat keskustelun aihetta. Aihe on aina kokonaisen keskusteluketjun ominaisuus ja kattaa siis kaikki kyseisen ketjun viestit. Keskusteluketjulla voi olla samanaikaisesti useita aiheita.
* Ylläpito-oikeuksien varustettu käyttäjä voi lisätä, poistaa ja muokata aiheita. Tavallisille käyttäjille ne ovat kuitenkin vain read-only -lista, jonka sisältöö ei voi vaikuttaa.
* Keskusteluketjuja voi selata aikajärjestyksessä tai suodattaa niitä aiheiden mukaan.
* Yksittäisen keskusteluketjun voi avata, jolloin sen kaikki viestit näytetään aikajärjestyksessä. Keskusteluketjunäkymä näyttää viesteistä otsikon, lähettäjän ja lähetysajan. Tässä näkymässä pääsee myös kirjoittamaan uuden viestin kyseiseen ketjuun. Keskusteluketjuun vastaukseksi kirjoitetut viestit näytetään aikajärjestyksessä. Sovellus ei siis tarjoa toiminnallisuutta haarautuviin vastauspuihin.
* Viestilistasta voi puolestaan avata yksittäisen viestin, jolloin pääsee näkemään sen varsinaisen sisällön. Jos käyttäjä avaa oman viestinsä, tässä näkymässä pääsee myös muokkaamaan viestiä tai poistamaan sen.
* Normaalioikeuksin varustetulla käyttäjällä on täydet CRUD-oikeudet itse kirjoittamiinsa viesteihin, mutta vain lukuoikeudet kaikkeen muuhun. Käyttäjä voi siis muokata viestinsä otsikkoa ja sisältöä sen jälkeen kun se on lähetetty ja myös poistaa koko viestin. Jos käyttäjä poistaa itse kirjoittamansa viestin, joka on ollut keskusteluketjun avausviesti, koko ketju ja kaikki sen viestit poistetaan.
* Ylläpito-oikeuksin varustetulla käyttäjällä on täydet CRUD-oikeudet kaikkeen dataan, myös muiden käyttäjien käyttäjätietoihin.
* Sovellus tarjoaa myös erillisen tilastonäkymän, jossa voi tarkastella erilaisia tilastoja: aktiivisimmat viestien kirjoittajat, suosituimmat aiheet, viestin ja käyttäjien kokonaismäärä jne.

_(Täydentyy ja tarkentuu projektin edetessä.)_

# Tietokantakaavio

![T](documentation/Tietokantakaavio.png)

# Heroku-sovelluksen osoite

Sovelluksen tämänhetkinen työversio löytyy [Herokusta](https://bulletiini.herokuapp.com/). Sovellukseen pääsee kirjautumaan testitunnuksella "testi" ja salasanalla "testi". Osa toiminallisuudesta (viestien lukeminen, käyttäjälista) on saatavilla myös ilman kirjautumista.
