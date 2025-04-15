# Ohjelmistotekniikka, harjoitustyö

## BEAN SHOOTER
Ammu papuja ja kerää pisteitä!

## Dokumentaatio
* [Vaatimusmäärittely](https://github.com/L-antti/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/L-antti/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
* [Changelog](https://github.com/L-antti/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
* [Arkkitehtuuri](https://github.com/L-antti/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

### Asentaminen

1. **Kloonaa repositorio**:
   ```bash
   git clone git@github.com:L-antti/ot-harjoitustyo.git
   cd ot-harjoitustyo
   ```
2. **Asenna riippuvuudet**:
   ```bash
   poetry install
   ```
3. **Käynnistä sovellus**:
   ```bash
   poetry run invoke start
   ```

   
### Komentorivitoiminnot

* **Käynnistää sovelluksen**:
   ```bash
   poetry run invoke start
   ```
* **Suorittaa pytestit**:
  ```bash
   poetry run invoke test
   ```
* **Luo testikattavuus raportin _htmlcov_-hakemistoon**:
   ```bash
   poetry run invoke coverage-report
   ```
* **Suorittaa Pylint tarkistukset**:
   ```bash
   poetry run invoke lint
