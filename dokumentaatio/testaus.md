# Testikattavuus

Sovellusta on testattu sekä yksikkötesteillä että manuaalisesti pelaamalla.

Yksikkötesteillä on testattu pelilogiikkaa ja papujen liikkeitä pelikentällä. Lisäksi GameLogic-luokkaa on testattu eristämällä sen riippuvuudet. Esimerkiksi GameArea-luokan sijasta testeissä käytetään DummyGameArea-luokkaa, joka simuloi tarvittavaa käytöstä ilman grafiikkaa.

Käyttöliittymä perustuu Pygameen, joten sitä on testattu manuaalisesti eri tilanteissa.

Yksikkötestauksen haaraumakattavuus on 75%. Testauksen ulkopuolelle on jätetty käyttöliittymä sekä index.py.
 
![](dokumentaatio/kuvat/coverage.png)
