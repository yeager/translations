# SensorPro: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga åtta strängar i komponenten
`sensorpro` har lästs från Lokalise. Inga ändringar behövdes.

| Fullständig nyckel | Aktuell svensk text |
| --- | --- |
| `component::sensorpro::config::abort::already_configured` | Enheten är redan konfigurerad |
| `component::sensorpro::config::abort::already_in_progress` | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. |
| `component::sensorpro::config::abort::no_devices_found` | Inga enheter hittades i nätverket |
| `component::sensorpro::config::abort::not_supported` | Enheten stöds inte |
| `component::sensorpro::config::flow_title` | {name} |
| `component::sensorpro::config::step::bluetooth_confirm::description` | Vill du konfigurera {name}? |
| `component::sensorpro::config::step::user::data::address` | Enhet |
| `component::sensorpro::config::step::user::description` | Välj en enhet att konfigurera |

## Verifiering

- Lokalise API: alla åtta svenska översättningar hämtades direkt vid
  granskningen.
- Mallvariabeln `{name}` förekommer två gånger och är bevarad exakt.
- Formuleringarna följer samma konfigurationsflödesterminologi som Core i
  övrigt: `konfigurera`, `enhet` och `stöds inte`.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
