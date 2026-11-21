# Home Assistant – GeoJSON Events: svensk radgranskning

Datum: 2026-11-21  
Komponent: `geo_json_events`  
Omfattning: 4/4 aktuella källsträngar

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Bedömning |
| --- | --- | --- | --- | --- |
| `component::geo_json_events::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Oförändrad | Korrekt. Lokal källreferens är upplöst av Lokalise. |
| `component::geo_json_events::config::step::user::data::location` | Location | Plats | Oförändrad | Korrekt. Lokal källreferens är upplöst av Lokalise. |
| `component::geo_json_events::config::step::user::data::url` | URL | URL | Oförändrad | Korrekt. Lokal källreferens är upplöst av Lokalise. |
| `component::geo_json_events::config::step::user::title` | Fill in your GeoJSON feed details. | Fyll i uppgifter om ditt GeoJSON-flöde. | Oförändrad | Naturlig och tydlig formulering. |

## Verifiering

- Aktuell källa och svenska värden hämtades via Lokalise API.
- `l10n-lint`: inga problem.
- `hunspell-sv`: inga stavningsanmärkningar.
- `svlang`: 10,0/10; GeoJSON är en avsiktlig teknisk beteckning.
- Inga platshållare, pluralformer eller formateringsmarkörer förekommer.
- Ingen ändring skickades, eftersom de sparade översättningarna redan är korrekta.
