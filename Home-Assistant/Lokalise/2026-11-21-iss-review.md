# Home Assistant – ISS: svensk radgranskning

Datum: 2026-11-21  
Komponent: `iss`  
Omfattning: 3/3 aktuella källsträngar

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Bedömning |
| --- | --- | --- | --- | --- |
| `component::iss::config::abort::latitude_longitude_not_defined` | Latitude and longitude are not defined in Home Assistant. | Latitud och longitud är inte angivna i Home Assistant. | Oförändrad | Tydlig och korrekt. |
| `component::iss::config::step::user::description` | Do you want to configure International Space Station (ISS)? | Vill du konfigurera den internationella rymdstationen (ISS)? | Oförändrad | Korrekt etablerad svensk benämning; förkortningen bevaras. |
| `component::iss::options::step::init::data::show_on_map` | Show on map | Visa på karta | Oförändrad | Korrekt och konsekvent UI-formulering. |

## Verifiering

- Aktuell källa och svenska värden hämtades via Lokalise API.
- `l10n-lint`: inga problem.
- `hunspell-sv`: inga stavningsanmärkningar.
- `svlang`: 10,0/10; markeringen av ”Home Assistant” är ett förväntat produktnamn, inte ett fel.
- Inga platshållare, pluralformer, referenser eller formateringsmarkörer förekommer.
- Ingen ändring skickades för komponenten, eftersom samtliga sparade översättningar redan är korrekta.
