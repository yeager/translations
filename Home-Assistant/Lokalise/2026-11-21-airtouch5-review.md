# Home Assistant – AirTouch 5: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `airtouch5`

## Underlag och verifiering

Alla sju aktuella strängar kontrollerades mot `homeassistant/components/airtouch5/strings.json` och Lokalise API. `l10n-lint` godkände de komponentegna strängarna mot engelsk referens. Svlang markerade “Auto” som ovanligt; det är en del av det produktstyrda lägesnamnet “Intelligent Auto”.

## Radvis resultat

| Fullständig nyckel | Engelska | Svenska | Resultat |
| --- | --- | --- | --- |
| `component::airtouch5::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Behåll. Delad referens. |
| `component::airtouch5::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Behåll. Delad referens. |
| `component::airtouch5::config::error::unknown` | Unexpected error | Oväntat fel | Behåll. Delad referens. |
| `component::airtouch5::config::step::user::data::host` | Host | Värd | Behåll. Delad referens. |
| `component::airtouch5::entity::climate::airtouch5::state_attributes::fan_mode::state::intelligent_auto` | Intelligent Auto | Intelligent Auto | Behåll. Produktstyrt lägesnamn. |
| `component::airtouch5::entity::climate::airtouch5::state_attributes::fan_mode::state::turbo` | Turbo | Turbo | Behåll. Etablerat lägesnamn. |
| `component::airtouch5::entity::cover::damper::name` | Damper | Spjäll | Behåll. Korrekt HVAC-term. |

Inga ändringar behövde sparas i Lokalise.