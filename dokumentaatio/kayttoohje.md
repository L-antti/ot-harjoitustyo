# Käyttöohje

Lataa sovelluksen viimeisin [versio](https://github.com/L-antti/ot-harjoitustyo/releases) valitsemalla ensin Asset ja sitten Source Code.

## Sovelluksen käynnistäminen

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Pelin aloitus

Peli alkaa painamalla välilyöntiä.

![](dokumentaatio/kuvat/aloitusruutu.png)

## Pelin pelaaminen

Tähtäystä säädetään nuolinäppäimillä oikealle ja vasemmalle. Ylösnuolella laukaistaan uusi papu. Jonossa näkyvät seuraavaksi tulevat ammukset. 
Pisteitä saa 10 per poistettu papu. 

![](dokumentaatio/kuvat/pelitila.png)

## Pelin päättyminen

Peli päättyy kun kriittinen raja ylitetään. Tällöin on mahdollista lisätä nimensä High Score listalle.

![](dokumentaatio/kuvat/nimiruutu.png)
