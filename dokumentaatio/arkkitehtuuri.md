# Arkkitehtuurikuvaus
## Rakenne

Sovelluksen arkkitehtuuri jakautuu viiteen kerrokseen 

* Käyttöliittymäkerros (UI): Tämä kerros on vastuussa pelin visuaalisista näkymistä ja käyttäjän syötteistä. Se toimii rajapintana pelaajan ja pelin muiden osien välillä. Renderer piirtää pelin elementit, ja GameOverView käsittelee pelin loppunäkymän.

* Ohjainkerros (Controller): Tämä kerros ohjaa pelin logiikkaa ja tapahtumien käsittelyä. Se reagoi pelaajan syötteisiin ja päivittää pelin tilan (esim. peli päättyy, peli käynnissä). Se sisältää myös pelisilmukan ja pelin pääsilmukan (GameLoop) ajamisen, sekä pelaajan syötteen lukemisen pelitilanteessa(EventHandler) ja pelin päätyttyä (GameOverController).

* Pelilogiikkakerros (Mechanics): Tämä kerros hoitaa pelin säännöt ja mekaniikan, kuten papujen tarkistaminen, liikkuminen ja rivin lisääminen. Se käyttää GameArea-luokkaa hallitsemaan pelialuetta ja GameLogic-luokkaa, joka sisältää pelin logiikan ja tilanmuutokset.

* Pelihahmokerros (Sprites): Tässä kerroksessa käsitellään pelin objekteja, kuten papuja ja laukaisijaa. Se huolehtii papujen liikkumisesta ja niiden vuorovaikutuksesta pelialueen kanssa.

* Tietovarastokerros (Repository): Tämä kerros on vastuussa tietojen tallentamisesta, kuten parhaista pisteistä.

* Lisäksi löytyy yhteiset tiedot ja asetukset, jotka vaikuttavat muihin kerroksiin. Näitä ovat esimerkiksi GameState (pelin tila), Clock (aikakellon hallinta) ja Settings (pelin asetukset, kuten nopeus ja värit).
  
```mermaid
graph LR
    A[UI]
    B[Controller]
    C[Mechanics]
    D[Repository]
    E[Sprites]

    A --> B
    B --> C
    B --> D
    B --> E
    C --> E
    A --> D
    A --> E

```

```mermaid
graph LR
    subgraph UI
        Renderer
        GameOverView
    end

    subgraph Controller
        EventHandler
        GameLoop
        GameOverController
    end

    subgraph Mechanics
        GameArea
        GameLogic
    end

    subgraph Sprites
        Bean
        Launcher
    end

    subgraph Repository
        HighscoreManager
    end

    GameState[GameState]
    Clock[Clock]
    Settings[Settings]

    GameLogic --> Settings
    Launcher --> Settings
    Bean --> Settings

    GameLoop --> GameState
    GameLoop --> GameLogic
    GameLoop --> Renderer
    GameLoop --> EventHandler

    GameLoop --> Clock

    GameOverView --> HighscoreManager
    GameOverView --> Settings

    Renderer --> GameLoop
    GameOverView -->GameOverController

    %% Controller -> Mechanics
    EventHandler --> GameLogic
    GameOverController --> GameState
    GameOverController --> GameLogic
    GameOverController --> GameOverView

    GameOverController --> HighscoreManager

    EventHandler -->Launcher

    EventHandler --> GameState

    GameLogic --> GameArea
    GameLogic --> Bean
    GameArea --> Bean
    GameLogic --> GameState
    GameLogic --> Launcher

    GameState -->GameLoop

    Renderer --> Bean

    Launcher --> Bean
    GameLogic --> Launcher



```

## Käyttöliittymä
Sovelluksessa on viisi erilaista näkymää:

* Alkunäkymä, jossa kerrotaan pelin säännöt ja siirrytään pelaamaan painamalla välilyöntiä.

* Pelinäkymä, jossa pelaaja voi ampua papuja ja nähdä nykyisen pistemäärän.

* Game over -näkymä, joka ilmoittaa pelin päättymisestä. Se piirretään hetkellisesti pelinäkymän päälle.

* Nimen syöttönäkymä, jossa pelaaja voi syöttää nimensä tulosta varten.
* Highscore-näkymä, jossa näytetään kymmenen parasta tulosta.

Käyttöliittymä saa pelitilanteen tilatiedot (GameState) ohjainkerrokselta, jolloin se piirtää kulloisenkin näkymän tämän tilan perusteella ilman, että ohjainkerros määrittelee suoraan mitä piirretään. Käyttöliittymä on pyritty erottamaan pelilogiikasta, ja se toimii puhtaasti tiedon esittäjänä.
Käyttöliittymä on edelleen jaettu omiin osakomponentteihinsa: esimerkiksi pelin päättymisestä vastaava näkymä on erillisessä luokassa. Pelinäkymän piirtämisestä vastaava luokka on tiiviisti yhteydessä pelihahmokerroksen Bean-luokkaan, koska se käsittelee papujen piirtämistä ruudulle.
Lisäksi käyttöliittymä hyödyntää pygame-kirjaston renderöintiominaisuuksia suoraan, kuten display.flip() ja fonttipiirtoa.

## Tietojen tallentaminen
Kymmenen parasta tulosta tallennetaan nimen ja pistemäärän kanssa highscores.json tiedostoon.

## Päätoiminnallisuudet
Päätöiminnallisuudet esitettynä sekvenssikaavioina

### Pelin aloitus

Pelin alussa pelaaja siirtyy alkunäkymästä pelitilaan painamalla välilyöntiä. Tällöin alustetaan pelilogiikka ja luodaan pelikentälle ensimmäiset pavut. Renderer piirtää alkuasetelman ruudulle, mukaan lukien pavut, pisteet ja laukaisija.

```mermaid
sequenceDiagram
    autonumber
    participant Player
    participant GameLoop
    participant EventHandler
    participant Renderer
    participant GameArea
    participant GameLogic
    participant Bean
    participant Pygame

    Note over GameLoop,Player: Peli on valikossa (in_menu = True)

    Player->>Pygame: painaa SPACE
    GameLoop->>EventHandler: process_events()
    EventHandler->>EventHandler: in_menu = False
    EventHandler-->>GameLoop: return True (exit_menu)
    GameLoop->>Pygame: event.clear()

    Note over GameLoop: Seuraava pelisilmukan kierros alkaa

    GameLoop->>EventHandler: process_events()
    alt in_menu == False
        GameLoop->>GameLogic: update_game_state()
        GameLoop->>Renderer: render_game_view()
    end

    Note over main.py: GameArea luodaan jo ennen loop.run() -kutsua

    main.py->>GameArea: GameArea()
    GameArea->>GameArea: _create_beans(rows=5, cols=SCREEN_WIDTH//40)
    loop for each row & col
        GameArea->>Bean: new Bean(color, position)
        GameArea->>GameArea.beans: add(bean)
    end

    Renderer->>Renderer: _draw_game_area()
    Renderer->>Renderer: _draw_score(GameLogic.score = 0)
    Renderer->>Renderer: _draw_beans(GameArea.beans)
    Renderer->>Renderer: _draw_launcher(Launcher)
    Renderer->>GameArea: get_next_bean_color()
    Renderer->>Renderer: _draw_next_bean(color)
    Renderer->>GameArea: bean_queue
    Renderer->>Renderer: _draw_bean_queue()
    Renderer->>Pygame: display.flip()



```

### Pelaaminen

Pelaaminen tapahtuu jatkuvassa silmukassa, jossa käsitellään syötteitä, päivitetään pelilogiikkaa ja piirretään näkymä. Pelaaja voi kääntää laukaisijaa ja ampua papuja. Papu liikkuu ja törmää muihin papuihin, minkä jälkeen päivitetään kiinnittyneet naapurit, tarkastellaan pisteiden saamista tai uuden rivin lisäämistä epäonnistuneiden laukausten perusteella.

```mermaid
sequenceDiagram
    autonumber
    participant Player
    participant GameLoop
    participant EventHandler
    participant Launcher
    participant GameLogic
    participant Bean
    participant GameArea
    participant Renderer
    participant Pygame

    Note over GameLoop: Peli on käynnissä (in_menu == False)

    loop joka pelisilmukan kierros
        GameLoop->>EventHandler: process_events()

        alt ← tai → näppäin painettu
            EventHandler->>Launcher: rotate(delta)
        end

        alt ↑ painettu ja state == IDLE
            EventHandler->>GameLogic: launch_next_bean(Launcher)
            GameLogic->>GameArea: get_next_bean()
            GameLogic->>Bean: new Bean(color, LAUNCHER_POSITION)
            Launcher->>Launcher: get_launch_velocity()
            Bean->>Bean: set velocity
            GameLogic->>GameLogic: transition_state(MOVING)
        end

        GameLoop->>GameLogic: update_game_state()

        alt state == MOVING
            GameLogic->>Bean: move()
            Bean->>Bean: update position and bounce off walls
            Bean->>GameArea: has_collided(beans)
            alt collision == True
                GameArea->>GameArea: attach_bean(bean)
                Bean->>Bean: stop()
                GameLogic->>GameLogic: transition_state(EVALUATING)
            end
        end

        alt state == EVALUATING
            GameLogic->>GameLogic: get_connected_same_color(bean)
            GameLogic->>Bean: access neighbours
            alt same color group >= 3
                GameArea->>GameArea.beans: remove(group)
                GameLogic->>GameLogic: increase score
                GameLogic->>GameLogic: transition_state(IDLE, reset_failed_shots=True)
            else same color neighbour exists
                GameLogic->>GameLogic: transition_state(IDLE, reset_failed_shots=True)
            else
                GameLogic->>GameLogic: failed_shots += 1
                alt failed_shots >= 3
                    GameLogic->>GameLogic: transition_state(ADDING_ROW, reset_failed_shots=True)
                    GameArea->>GameArea: add_new_row()
                    GameArea->>GameArea: _create_beans(rows=1, cols=SCREEN_WIDTH // 40, offset_adjustment=40)
                    GameArea->>GameArea: _shift_beans_down(y_offset=40)
                    GameArea->>GameArea: _update_neighbours_for_new_beans(new_beans)
                    GameLogic->>GameLogic: transition_state(GameState.IDLE, reset_failed_shots=True)
                else
                    GameLogic->>GameLogic: transition_state(IDLE)
                end
            end
        end
        
        GameLoop->>GameLogic: check_game_over()
        GameLogic->>GameLoop: game_over = False

        GameLoop->>Renderer: render_game_view()
    end


```


### Pelin päättyminen

Peli päättyy, jos joku papu saavuttaa kentän alareunan. Tällöin näytetään pelinlopetusnäkymä ja pelaajalta pyydetään nimi tulostaulukkoa varten. Jos nimi annetaan, se tallennetaan, ja näytetään parhaat tulokset. Lopuksi peli odottaa pelaajan syötettä uuden pelin aloittamiseksi.
```mermaid
sequenceDiagram
    autonumber
    participant GameLoop
    participant GameLogic
    participant GameOverController
    participant GameOverView
    participant HighscoreManager
    participant Player
    participant Pygame

    GameLoop->>GameLogic: check_game_over()
    GameLogic->>GameLoop: game_over = True
    alt peli ohi
        GameLoop->>GameOverController: handle_game_over()
        
        GameOverController->>GameOverView: show_game_over_screen()
        GameOverView->>Pygame: display.flip() + delay

        loop nimi syöttö
            GameOverController->>GameOverView: draw_name_input(name)
            GameOverView->>Pygame: display.flip()
            Player->>Pygame: näppäin painettu
            GameOverController->>Pygame: event.get()
            alt Enter painettu
                GameOverController-->>GameOverController: syöttö päättyy
            else
                GameOverController-->>GameOverController: päivitä name
            end
        end

        alt nimi ei tyhjä
            GameOverController->>HighscoreManager: add_score(name, score)
            HighscoreManager->>HighscoreManager: sort, truncate, save_scores()
        end

        GameOverController->>GameOverView: show_highscores_screen()
        GameOverView->>HighscoreManager: get_scores()
        GameOverView->>Pygame: display.flip()

        GameOverController->>GameOverController: _wait_for_any_key()
        Player->>Pygame: painaa mitä tahansa
        GameOverController->>GameLogic: reset_game()
    end

```
