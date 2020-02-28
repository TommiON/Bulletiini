# Puutteet ja kehityskohteet

Ajanpuutteen vuoksi sovellukseen jäi ainakin yksi merkittävä bugi, joka kylläkään ei estä sovellusta toimimasta, mutta toimii eri tavalla kuin alunperin oli tarkoitus:

* Jos Aihepiiriä on käytetty Keskusteluketjuissa ja kaikki Aihepiiriä käsittelevät Keskusteluketjut poistetaan, myös Aihepiiri poistuu. Alunperin tarkoituksena oli, että Aihepiiri jää jäljelle ja sitä voi käyttää tulevissa Ketjuissa. Bugi liittyy ilmeisesti SQLAlchemyn "Cascading" -toiminnallisuuteen ja koskeaa ainoastaan Herokua/PostgreSQL:aa. Paikallisessa SQLite-versiossa tätä käytöstä ei esiinny.

Lisäksi jäi toteuttamatta muutamia melko ilmeisiä toimintoja ja osa-alueita:

* Haarautuvat viestiketjut: viesteihin voisi vastata niin, että ne muodostavat hierarkkisia viestipuita.
* Käytettävyydessä ja ulkoasussa  puutteita ja hiomattomuuksia, esim. etusivulla näkyvät keskusteluketjujen id:t eivätkä nimet, ja kirjautumisen jälkeen palaudutaan aina etusivulle eikä siihen kohtaan josta kirjautumispyyntö laukaistiin, jne.
* Salasanat tallennetaan salaamattomana, ei ollut aikaa tehdä oikeaoppista, hässättyä toteutusta.
