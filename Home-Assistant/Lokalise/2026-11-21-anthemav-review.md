# Home Assistant – Anthem AV: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `anthemav`

## Underlag och verifiering

Samtliga fem aktuella strängar jämfördes mot `homeassistant/components/anthemav/strings.json` och Lokalise API. Fyra är delade referenser och deras upplösta engelska och svenska måltexter kontrollerades. `hunspell-sv`, `svlang` och `l10n-lint` användes som stöd.

Hunspell och l10n-lint gav inga innehållsfel. Svlang markerade “Se till att enheten är påslagen” som möjlig V2-avvikelse; det är en falsk positiv för en korrekt imperativ sats.

## Radvis resultat

| Fullständig nyckel | Engelska | Svenska | Resultat |
| --- | --- | --- | --- |
| `component::anthemav::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Behåll. Delad referens. |
| `component::anthemav::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Behåll. Delad referens. |
| `component::anthemav::config::error::cannot_receive_deviceinfo` | Failed to retrieve MAC address. Make sure the device is turned on | Det gick inte att hämta MAC-adress. Se till att enheten är påslagen | Behåll. Korrekt och idiomatisk svensk feltext. |
| `component::anthemav::config::step::user::data::host` | Host | Värd | Behåll. Delad referens. |
| `component::anthemav::config::step::user::data::port` | Port | Port | Behåll. Delad referens. |

Inga ändringar behövde sparas i Lokalise.