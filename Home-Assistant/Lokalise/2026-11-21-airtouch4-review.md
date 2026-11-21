# Home Assistant – AirTouch 4: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `airtouch4`

## Underlag och verktyg

Alla sex aktuella strängar jämfördes med `homeassistant/components/airtouch4/strings.json` och Lokalise API. Den ändrade rubriken validerades med `svlang`, `hunspell-sv` och `l10n-lint`. Svlang markerade endast produktnamnet AirTouch som ovanligt; det ska bevaras.

## Radvis resultat

| Fullständig nyckel | Engelska | Befintlig svenska | Resultat |
| --- | --- | --- | --- |
| `component::airtouch4::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Behåll. Delad referens. |
| `component::airtouch4::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Behåll. Delad referens. |
| `component::airtouch4::config::error::no_units` | Could not find any AirTouch 4 Groups. | Det gick inte att hitta några AirTouch 4-grupper. | Behåll. |
| `component::airtouch4::config::step::user::data::host` | Host | Värd | Behåll. Delad referens. |
| `component::airtouch4::config::step::user::data_description::host` | The hostname or IP address of your AirTouch controller. | Värdnamnet eller IP-adressen för din AirTouch-kontroller. | Behåll. |
| `component::airtouch4::config::step::user::title` | Set up your AirTouch 4 connection details. | Ställ in dina AirTouch 4-anslutningsdetaljer. | Sparad som **Ställ in anslutningsuppgifterna för AirTouch 4.** Idiomatisk svensk UI-term och tydligare ägande. |

## Verifiering

Ändringen är skickad till Lokalise och läst tillbaka via API. Inga platshållare, referenser eller pluralformer påverkades.