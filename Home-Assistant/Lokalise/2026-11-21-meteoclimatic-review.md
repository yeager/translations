# Home Assistant – Meteoclimatic: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `meteoclimatic`

## Underlag och verifiering

Alla fem aktuella strängar jämfördes med `homeassistant/components/meteoclimatic/strings.json` och Lokalise API. `l10n-lint` godkände de komponentegna etiketterna mot engelsk referens. Svlang och hunspell markerade stationskoden och sammansättningen “stationskod”; de är giltiga tekniska respektive svenska facktermer.

## Radvis resultat

| Fullständig nyckel | Engelska | Svenska | Resultat |
| --- | --- | --- | --- |
| `component::meteoclimatic::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Behåll. Delad referens. |
| `component::meteoclimatic::config::abort::unknown` | Unexpected error | Oväntat fel | Behåll. Delad referens. |
| `component::meteoclimatic::config::error::not_found` | No devices found on the network | Inga enheter hittades i nätverket | Behåll. Delad referens. |
| `component::meteoclimatic::config::step::user::data::station_code` | Station code | Stationskod | Behåll. |
| `component::meteoclimatic::config::step::user::data_description::station_code` | Looks like ESCAT4300000043206B | Ser ut som ESCAT4300000043206B | Behåll. Det tekniska exempelvärdet är oförändrat. |

Inga ändringar behövde sparas i Lokalise.