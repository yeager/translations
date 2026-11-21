# Home Assistant – IQVIA: svensk radgranskning

Datum: 2026-11-21  
Komponent: `iqvia`  
Omfattning: 4/4 aktuella källsträngar

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Bedömning |
| --- | --- | --- | --- | --- |
| `component::iqvia::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Oförändrad | Korrekt; Lokalise returnerar upplöst text för den gemensamma källreferensen. |
| `component::iqvia::config::error::invalid_zip_code` | ZIP code is invalid | Ogiltigt postnummer | Oförändrad | Korrekt svensk formulering. |
| `component::iqvia::config::step::user::data::zip_code` | ZIP code | Postnummer | Oförändrad | Lämplig svensk UI-term. |
| `component::iqvia::config::step::user::description` | Fill out your U.S. or Canadian ZIP code. | Fyll i ditt amerikanska eller kanadensiska postnummer. | Oförändrad | Korrekt och tydlig. |

## Verifiering

- Aktuell källa och svenska värden hämtades via Lokalise API.
- `l10n-lint`: inga problem.
- `hunspell-sv` och `svlang`: inga anmärkningar.
- Inga platshållare, pluralformer eller formateringsmarkörer förekommer.
- Ingen ändring skickades, eftersom de sparade översättningarna redan är korrekta.
