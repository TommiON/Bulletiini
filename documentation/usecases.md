# Käyttötapaukset

Sovelluksen avainkäsitteitä ovat Viestit (Message), joista muodostuu Keskusteluketjuja (Thread), jotka voivat kuulua yhteen tai useampaan Aiheeseen (Topic). Lisäksi sovelluksessa on tietysti Käyttäjiä (tietokannassa Account), joista osa voi olla ylläpito-oikeuksin varustettuja.

Alla on lueteltu sovelluksen käyttötapaukset ja niitä tukevat SQL-kyselyt.

## Käyttäjähallinta

* Käyttäjä voi luoda itselleen käyttäjätunnuksen. Uusilla käyttäjätunnuksilla ei ole ylläpitäjän oikeuksia.

```INSERT INTO account(username, password, is_admin, joined) VALUES (?, ? , false, current_timestamp())```

* Ylläpito-oikeuksin varustettu käyttäjä voi antaa tai ottaa pois toisen käyttäjän ylläpito-oikeudet.

```UPDATE account SET is_admin=? WHERE id=?```

* Ylläpito-oikeuksin varustettu käyttäjä voi poistaa toisen käyttäjätunnuksen. _ei vielä toteutettu_

```DELETE FROM account WHERE id=?```

* Lista kaikista rekisteröityneistä käyttäjistä.

```SELECT * FROM account```

* Yksittäisen käyttäjän tarkemmat tiedot.

```SELECT * FROM account WHERE id=?```

## Keskusteluketjut

* Lista kaikista keskusteluketjuista.

```SELECT * FROM thread```

* Yksittäisen keskusteluketjun tarkemmat tiedot.

```SELECT * FROM thread WHERE id=?```

* Uuden keskusteluketjun luominen. Tämä käyttötapaus ei ilmene koskaan yksinään, vaan yhdessä viestin luomisen kanssa.

```INSERT INTO thread(id, title, time_of_opening) VALUES(?, ?, current_timestamp())```

## Viestit

* Viestilistasta voi avata yksittäisen viestin, jolloin pääsee näkemään sen varsinaisen sisällön. Jos käyttäjä avaa oman viestinsä, tässä näkymässä pääsee myös muokkaamaan viestiä tai poistamaan sen.

```SELECT * FROM message WHERE id=?

--
* Käyttäjä voi aloittaa uuden keskusteluketjun ja kirjoittaa sen ensimmäisen viestin. Uutta keskusteluketjua aloitettaessa viestille voi valita yhden tai useamman aiheen valmiista listasta. Aiheet ovat eräänlaisia leimoja/tageja, jotka kuvaavat keskustelun aihetta. Aihe on aina kokonaisen keskusteluketjun ominaisuus ja kattaa siis kaikki kyseisen ketjun viestit. Keskusteluketjulla voi olla samanaikaisesti useita aiheita. _Aiheiden valitsemistoiminnallisuus vielä kesken_
* Ylläpito-oikeuksien varustettu käyttäjä voi lisätä, poistaa ja muokata aiheita. Tavallisille käyttäjille ne ovat kuitenkin vain read-only -lista, jonka sisältöö ei voi vaikuttaa.
* Keskusteluketjuja voi selata aikajärjestyksessä tai suodattaa niitä aiheiden mukaan. _Aihepiirien mukaan suodattaminen vielä kesken_
* Yksittäisen keskusteluketjun voi avata, jolloin sen kaikki viestit näytetään aikajärjestyksessä. Keskusteluketjunäkymä näyttää viesteistä otsikon, lähettäjän ja lähetysajan. Tässä näkymässä pääsee myös kirjoittamaan uuden viestin kyseiseen ketjuun. Keskusteluketjuun vastaukseksi kirjoitetut viestit näytetään aikajärjestyksessä. Sovellus ei siis tarjoa toiminnallisuutta haarautuviin vastauspuihin. Lista näyttää kirjautuneen käyttäjän viestin kohdalla myös linkit kyseisen viestin muokkaamiseen ja poistamiseen.

* Normaalioikeuksin varustetulla käyttäjällä on täydet CRUD-oikeudet itse kirjoittamiinsa viesteihin, mutta vain lukuoikeudet kaikkeen muuhun. Käyttäjä voi siis muokata viestinsä otsikkoa ja sisältöä sen jälkeen kun se on lähetetty ja myös poistaa koko viestin. Jos käyttäjä poistaa itse kirjoittamansa viestin, joka on ollut keskusteluketjun avausviesti, koko ketju ja kaikki sen viestit poistetaan.
* Ylläpito-oikeuksin varustetulla käyttäjällä on täydet CRUD-oikeudet kaikkeen dataan, myös muiden käyttäjien käyttäjätietoihin. _Viestien muokkaus- ja poistoauktorisointi ylläpitokäyttäjälle vielä kesken_
* Sovellus tarjoaa myös erillisen tilastonäkymän, jossa voi tarkastella erilaisia tilastoja: aktiivisimmat viestien kirjoittajat, suosituimmat aiheet, viestin ja käyttäjien kokonaismäärä jne.
