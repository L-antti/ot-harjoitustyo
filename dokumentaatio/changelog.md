## Viikko 3
* Pelaaja voi tähdätä liikuttaa laukaisijaa ja ampua papuja.
* Lisätty Launcher-luokka laukaisijaa sekä Bean-luokka ammuttavia papuja varten
* Testattu Launcherin toimintaa


## Viikko 4
* Pelaaja voi ampua papuja, jotka poksahtavat kolmen ryhmissä.
* Laskuriin kertyy pisteitä poksautetuista pavuista.
* Jaettu koodia gameloop, game_area ja settings osioihin
* Testattu Bean-luokan toimintaa

## Viikko 5
* Pelaaja saa nyt pisteitä myös suuremmista kuin kolmen pavun ryhmistä
* Pelialueen yläreunaan tulee uusi rivi papuja, jos tulee kolme hutia putkeen
* Game over -ilmoitus, jos papvut ylittvät kriittisen rajan
* Koodi on jaettu kokonaan uusiin luokkiin: GameUI, GameArea, GameController, GameLogic, GameState
* Testattu hieman GameArea, GameState, GameLogic ja GameUI luokkien toimintaa

## Viikko 6
* Pelaajan pisteet päivitetään pelin päätyttyä High Score tiedostoon.
* Lisätty HighscoreManager luokka.
* Koodia refaktoroitu lisää. Sovelluslogiikka eriytetty käyttöliittymästä ja pelinohjauksesta.
* Lisää testejä GameLogic ja GameController luokille.
