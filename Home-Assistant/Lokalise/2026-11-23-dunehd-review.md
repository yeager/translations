# Home Assistant Core – Dune HD

Datum: 2026-11-23

Hela komponenten (sju aktuella strängar) lästes från Lokalise API och
jämfördes med källtexten. Alla var korrekta och behövde ingen ändring.

| Nyckel | Svenska | Resultat |
| --- | --- | --- |
| `component::dunehd::config::abort::already_configured` | Enheten är redan konfigurerad | Korrekt. |
| `component::dunehd::config::error::already_configured` | Enheten är redan konfigurerad | Korrekt. |
| `component::dunehd::config::error::cannot_connect` | Det gick inte att ansluta | Korrekt. |
| `component::dunehd::config::error::invalid_host` | Ogiltigt värdnamn eller IP-adress | Korrekt. |
| `component::dunehd::config::step::user::data::host` | Värd | Korrekt i nätverkskontext. |
| `component::dunehd::config::step::user::description` | Se till att din spelare är påslagen. | Korrekt. |
| `component::dunehd::config::step::user::data_description::host` | Värdnamnet eller IP-adressen för din Dune HD-enhet. | Korrekt. |

Inga platshållare, pluralformer eller referenser förekommer. Hunspell har
endast produktnamnet `Dune` som okänt ord. svlang fann inga skrivregelfel eller
anglifieringar; den enda V2-varningen är en felträff på ett UI-fragment.
Manifestet är API-återläst och tillagt i det validerade Home Assistant-TMX-minnet.
