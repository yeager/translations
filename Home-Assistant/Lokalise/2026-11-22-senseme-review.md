# SenseME: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga tio strängar i komponenten
`senseme` har lästs från Lokalise. Inga ändringar behövdes.

| Fullständig nyckel | Aktuell svensk text |
| --- | --- |
| `component::senseme::config::abort::already_configured` | Enheten är redan konfigurerad |
| `component::senseme::config::error::cannot_connect` | Det gick inte att ansluta |
| `component::senseme::config::error::invalid_host` | Ogiltigt värdnamn eller IP-adress |
| `component::senseme::config::flow_title` | {name} - {model} ({host}) |
| `component::senseme::config::step::discovery_confirm::description` | Vill du konfigurera {name} - {model} ({host})? |
| `component::senseme::config::step::manual::data::host` | Värd |
| `component::senseme::config::step::manual::description` | Ange en IP-adress. |
| `component::senseme::config::step::user::data::device` | Enhet |
| `component::senseme::config::step::user::description` | Välj en enhet, eller välj "IP-adress" för att manuellt ange en IP-adress. |
| `component::senseme::config::abort::cannot_connect` | Det gick inte att ansluta |

## Verifiering

- Lokalise API: alla tio svenska översättningar hämtades direkt vid
  granskningen.
- `{name}`, `{model}` och `{host}` förekommer både i flödestiteln och i
  bekräftelsefrågan och är bevarade exakt.
- Den citerade UI-etiketten `IP-adress` och den svenska sammansättningen
  `värdnamn` är konsekventa med Home Assistants terminologi.
- De två separata anslutningsfelen har identisk käll- och måltext och har
  kontrollerats på båda nycklarna.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
