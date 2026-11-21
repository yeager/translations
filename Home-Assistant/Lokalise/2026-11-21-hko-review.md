# Home Assistant – HKO: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `hko`

## Underlag och verifiering

Alla fem aktuella strängar jämfördes med `homeassistant/components/hko/strings.json` och Lokalise API. `svlang`, `hunspell-sv` och `l10n-lint` kördes på den komponentegna beskrivningen och gav inga anmärkningar.

## Radvis resultat

| Fullständig nyckel | Engelska | Svenska | Resultat |
| --- | --- | --- | --- |
| `component::hko::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Behåll. Delad referens. |
| `component::hko::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Behåll. Delad referens. |
| `component::hko::config::error::unknown` | Unexpected error | Oväntat fel | Behåll. Delad referens. |
| `component::hko::config::step::user::data::location` | Location | Plats | Behåll. Delad referens. |
| `component::hko::config::step::user::description` | Please select a location to use for weather forecasting. | Välj en plats att använda för väderprognoser. | Behåll. Kort, korrekt och idiomatisk formulering. |

Inga ändringar behövde sparas i Lokalise.