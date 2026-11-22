# Sanix: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga tio strängar i komponenten `sanix`
har lästs från Lokalise.

## Rättning sparad i Lokalise

| Fullständig nyckel | Tidigare text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `component::sanix::entity::sensor::service_date::name` | Servicedata | Servicedatum | Källan avser datum för service, inte serviceinformation. |

Ändringen sparades via Lokalise API och lästes tillbaka ordagrant. Den finns i
det validerade HA-minnet (`swedish-tm`, commit `fb4d4ea`).

## Kontrollerade utan ändring

| Fullständig nyckel | Aktuell svensk text eller kontroll |
| --- | --- |
| `component::sanix::config::abort::already_configured` | Enheten är redan konfigurerad |
| `component::sanix::config::error::invalid_auth` | Ogiltig autentisering |
| `component::sanix::config::error::unknown` | Oväntat fel |
| `component::sanix::config::step::user::data::serial_number` | Serienummer |
| `component::sanix::config::step::user::data::token` | Åtkomsttoken |
| `component::sanix::config::step::user::description` | Länktext, produktnamnet `Sanix Dashboard` och `{dashboard_url}` är korrekta. |
| `component::sanix::entity::sensor::device_no::name` | Enhetens nummer |
| `component::sanix::entity::sensor::fill_perc::name` | Fylld |
| `component::sanix::entity::sensor::ssid::name` | SSID |

`Fylld` är korrekt som kort tillståndsetikett för den engelska etiketten
`Filled`; källtexten anger inte ett mått som skulle motivera `fyllnadsgrad`.

## Verifiering

- Lokalise API: alla tio svenska översättningar hämtades direkt vid denna
  granskning; rättningen lästes tillbaka efter skrivning.
- `svlang check`: 10,0/10 för `Servicedatum`.
- `hunspell-sv`: inga stavningsavvikelser för `Servicedatum`.
- HA-TMX-validatorn: `valid: 3320 entries` efter uppdateringen.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
