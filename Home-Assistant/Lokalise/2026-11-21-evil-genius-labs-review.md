# Home Assistant – Evil Genius Labs: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `evil_genius_labs`

## Underlag och verifiering

Samtliga fem aktuella strängar jämfördes med `homeassistant/components/evil_genius_labs/strings.json` och Lokalise API. `svlang`, `hunspell-sv` och `l10n-lint` användes som stöd för den komponentegna beskrivningen.

L10n-lint gav inga fel och hunspell gav inga relevanta stavningsträffar. Svlang markerade “Evil” och “Labs” som ovanliga ord; de är delar av produktnamnet Evil Genius Labs och ska inte ändras.

## Radvis resultat

| Fullständig nyckel | Engelska | Svenska | Resultat |
| --- | --- | --- | --- |
| `component::evil_genius_labs::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Behåll. Delad referens. |
| `component::evil_genius_labs::config::error::timeout` | Timeout while establishing a connection | Tidsgränsen överskreds när anslutningen upprättades. | Behåll. Delad referens. |
| `component::evil_genius_labs::config::error::unknown` | Unexpected error | Oväntat fel | Behåll. Delad referens. |
| `component::evil_genius_labs::config::step::user::data::host` | Host | Värd | Behåll. Delad referens. |
| `component::evil_genius_labs::config::step::user::data_description::host` | The hostname or IP address of your Evil Genius Labs device. | Värdnamn eller IP-adress för din Evil Genius Labs-enhet. | Behåll. Produktnamn och terminologi är korrekta. |

Inga ändringar behövde sparas i Lokalise.