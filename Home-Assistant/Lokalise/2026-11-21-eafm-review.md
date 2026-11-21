# Home Assistant – EAFM: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `eafm`

## Underlag och verktyg

Alla fem strängar i aktuell `homeassistant/components/eafm/strings.json` jämfördes med Lokalise API. `svlang`, `hunspell-sv` och `l10n-lint` kördes på den föreslagna ändringen. Samtliga gav ett godkänt resultat.

## Radvis resultat

| Fullständig nyckel | Engelska | Befintlig svenska | Resultat |
| --- | --- | --- | --- |
| `component::eafm::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Behåll. Delad referens. |
| `component::eafm::config::abort::no_stations` | No flood monitoring stations found. | Inga övervakningsstationer för översvämningar hittades. | Behåll. |
| `component::eafm::config::step::user::data::station` | Station | Station | Behåll. |
| `component::eafm::config::step::user::description` | Select the station you want to monitor | Välj den station du vill övervaka | Behåll. |
| `component::eafm::config::step::user::title` | Track a flood monitoring station | Spåra en station för övervakning av översvämningar | Sparad som **Följ en övervakningsstation för översvämningar**. Den följer komponentens egen term i feltexten och fungerar bättre som UI-rubrik. |

## Verifiering

Den ändrade måltexten skickades till Lokalise och lästes tillbaka via API. Komponenten saknar platshållare och pluralformer som påverkas av ändringen.