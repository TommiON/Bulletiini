# Käyttötapaukset

Sovelluksen avainkäsitteitä ovat Viestit (Message), joista muodostuu Keskusteluketjuja (Thread), jotka voivat kuulua yhteen tai useampaan Aiheeseen (Topic). Lisäksi sovelluksessa on tietysti Käyttäjiä (tietokannassa Account), joista osa voi olla ylläpito-oikeuksin varustettuja.

Alla on lueteltu sovelluksen käyttötapaukset ja niitä tukevat SQL-kyselyt. _(Aihepiireihin (Topic) liittyvä toiminnallisuus on vielä kesken..)

## Käyttäjähallinta

* Käyttäjä voi luoda itselleen käyttäjätunnuksen. Uusilla käyttäjätunnuksilla ei ole ylläpitäjän oikeuksia.

```INSERT INTO account(username, password, is_admin, joined) VALUES (?, ? , false, current_timestamp())```

* Ylläpito-oikeuksin varustettu käyttäjä voi antaa tai ottaa pois toisen käyttäjän ylläpito-oikeudet.

```UPDATE account SET is_admin=? WHERE id=?```

* Ylläpito-oikeuksin varustettu käyttäjä voi poistaa minkä tahansa käyttäjätunnuksen.

```DELETE FROM account WHERE id=?```

* Lista kaikista rekisteröityneistä käyttäjistä.

```SELECT * FROM account```

* Yksittäisen käyttäjän tarkemmat tiedot.

```SELECT * FROM account WHERE id=?```

## Keskusteluketjut

* Lista kaikista keskusteluketjuista.

```SELECT * FROM thread```

* Yksittäisen keskusteluketjun tarkemmat tiedot. Keskusteluketjuun vastaukseksi kirjoitetut viestit näytetään aikajärjestyksessä. Sovellus ei siis tarjoa toiminnallisuutta haarautuviin vastauspuihin. Lista näyttää kirjautuneen käyttäjän viestin kohdalla myös linkit kyseisen viestin muokkaamiseen ja poistamiseen. Keskusteluketjunäkymä näyttää viesteistä otsikon, lähettäjän ja lähetysajan. Tässä näkymässä pääsee myös kirjoittamaan uuden viestin kyseiseen ketjuun.

```SELECT * FROM thread WHERE id=?```

* Uuden keskusteluketjun luominen. Tämä käyttötapaus ei ilmene koskaan yksinään, vaan yhdessä viestin luomisen kanssa. Uutta keskusteluketjua aloitettaessa viestille voi valita yhden tai useamman aiheen valmiista listasta. Aiheet ovat eräänlaisia leimoja/tageja, jotka kuvaavat keskustelun aihetta. Aihe on aina kokonaisen keskusteluketjun ominaisuus ja kattaa siis kaikki kyseisen ketjun viestit. Keskusteluketjulla voi olla samanaikaisesti useita aiheita. _Aiheiden valitsemistoiminnallisuus vielä kesken_

```INSERT INTO thread(id, title, time_of_opening) VALUES(?, ?, current_timestamp())```

* Keskusteluketjuja voi suodattaa näkyviin aiheiden mukaan. _Aihepiirien mukaan suodattaminen vielä kesken_

* Keskusteluketjun poistaminen. Tämä toiminto ei aktivoidu suoraan käyttäjän toimenpiteestä, vaan epäsuorasti sen seurauksena, kun ketjun viimeinen viesti poistetaan.

```DELETE FROM thread WHERE id=?```

## Viestit

* Lista kaikista viesteistä. (Toimintoa ei tällä hetkellä käytetä sovelluksessa tällaisenaan mihinkään, mutta se on kuitenkin aiemman kehityksen tuloksena olemassa eikä poistettu.)

```SELECT * FROM message```

* Viestilistasta voi avata yksittäisen viestin, jolloin pääsee näkemään sen varsinaisen sisällön. Jos käyttäjä avaa oman viestinsä, tässä näkymässä pääsee myös muokkaamaan viestiä tai poistamaan sen.

```SELECT * FROM message WHERE id=?```

* Kun keskusteluketju on olemassa, siihen voi kirjoittaa uuden viestin.

```ÌNSERT INTO message(title, content, time_of_sending, author_id, thread_id) VALUES (?, ?, current_timestamp(), ?, ?)```

* Viestin kirjoittanut käyttäjä tai admin-käyttäjä voi muokata viestin otsikkoa ja/tai sisältöä.

```ÙPDATE message SET title=?, content=? WHERE id=?```

* Viestin kirjoittanut käyttäjä tai admin-käyttäjä voi poistaa viestin.

```DELETE FROM message WHERE id=?```

## Aihepiirit

* Kaikki käyttäjät voivat katsella listaa mahdollisista aihepiireistä.

```SELECT * from topic```

* Ylläpito-oikeuksien varustettu käyttäjä voi lisätä aiheita.

```ÌNSERT INTO topic(name) VALUES(?)```

* Ylläpito-oikeuksien varustettu käyttäjä voi poistaa aiheita.

```DELETE FROM topic WHERE id=?```

## Tilastoja ja yhteenvetokyselyjä

Seuraavat käyttötapaukset eivät ole suoraan seurausta käyttäjän toimista, vaan tuottavat automaattisesti tietoa sovelluksen eri näkymiin.

* Viestien kokonaismäärän näyttäminen etusivulla ja tilastosivulla.

```SELECT COUNT(message.id) FROM message```

* Uusimpien x:n viestin (nykytoteutuksessa 10:n) näyttäminen sovelluksen etusivulla.

```SELECT * FROM message ORDER BY id DESC LIMIT 10```

* Käyttäjien määrä.

```SELECT COUNT(account.id) FROM account```

* Ainakin yhden viestin julkaisseiden käyttäjien määrä.

```SELECT COUNT(DISTINCT message.author_id) FROM message```

* Keksusteluketjujen määrä.

```SELECT COUNT(thread.id) FROM MESSAGE```


