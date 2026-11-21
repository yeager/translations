# Home Assistant – LG Soundbar: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `lg_soundbar`

## Underlag och verktyg

Samtliga fem strängar jämfördes mot aktuell `homeassistant/components/lg_soundbar/strings.json` och Lokalise API. `svlang`, `hunspell-sv` och `l10n-lint` godkände den ändrade feltexten.

## Radvis resultat

| Fullständig nyckel | Engelska | Befintlig svenska | Resultat |
| --- | --- | --- | --- |
| `component::lg_soundbar::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Behåll. Delad referens. |
| `component::lg_soundbar::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Behåll. Delad referens. |
| `component::lg_soundbar::config::error::no_data` | Device did not return any data required to an entry. | Enheten skickade inte nödvändig data. | Sparad som **Enheten returnerade inte de data som krävs för att lägga till den.** Återger både att data saknas och att den krävs i konfigurationsflödet. |
| `component::lg_soundbar::config::step::user::data::host` | Host | Värd | Behåll. Delad referens. |
| `component::lg_soundbar::config::step::user::data_description::host` | The hostname or IP address of your LG Soundbar. | Värdnamnet eller IP-adressen för din LG Soundbar. | Behåll. Produktnamnet bevarat. |

## Verifiering

Den ändrade svenska texten skickades till Lokalise och lästes tillbaka via API. Komponenten har inga platshållare eller pluralformer som påverkades.