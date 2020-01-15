# Bulletiini
Helsingin yliopiston Tietokantaprojekti-kurssin harjoitustyö. Sovellus tarjoaa toiminnallisuuden yksinkertaiselle keskustelufoorumille.

Avainkäsitteitä ovat Viestit (Message), joista muodostuu Keskusteluketjuja (Thread) ja jotka voivat kuulua yhteen tai useampaan Aiheeseen (Topic). Lisäksi sovelluksessa on tietysti Käyttäjiä (User), joista osa voi olla ylläpito-oikeuksin varustettuja.

Perustoiminnallisuuden hahmottelua:

•	Uusia Viestejä voi luoda kahdella tavalla: 1) aloittaa uuden Keskusteluketjun (Thread), jonka ensimmäiseksi viestiksi uusi viesti tulee, tai 2) kirjoittaa viestin vastaukseksi olemassa olevaan keskusteluketjuun.
•	Keskusteluketjuun vastaukseksi kirjoitetut viestit näytetään aikajärjestyksessä. Sovellus ei siis tarjoa toiminnallisuutta haarautuviin vastauspuihin.
•	Keskusteluketjujen lisäksi viestejä voi jaotella Aiheiden (Topic) mukaan. Nämä ovat eräänlaisia leimoja/tageja, jotka kuvaavat keskustelun aihetta. Käyttäjä ei voi itse luoda aiheita, vaan sovellus tarjoaa listan valmiita aiheita. Aihe on aina kokonaisen keskusteluketjun ominaisuus, ja aiheieima kattaa siis kaikki kyseisen ketjun viestit. Keskusteluketjulla voi olla samanaikaisesti useita aiheita.
•	Normaalioikeuksin varustetulla käyttäjällä on täydet CRUD-oikeudet itse kirjoittamiinsa viesteihin, mutta vain lukuoikeudet kaikkeen muuhun. Jos käyttäjä poistaa itse kirjoittamansa viestin, joka on ollut keskusteluketjun avausviesti, koko ketju ja kaikki sen viestit poistetaan.
•	Ylläpito-oikeuksin varustetulla käyttäjällä on täydet CRUD-oikeudet kaikkeen dataan, myös Aiheiden lisäämiseen/poistamiseen ja muiden käyttäjien käyttäjätietoihin.
