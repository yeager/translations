# RuuviTag BLE: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga 16 strängar i komponenten
`ruuvitag_ble` har lästs från Lokalise. Mallvariabeln `{name}` är bevarad
exakt i både flödestiteln och bekräftelsefrågan.

## Rättning sparad i Lokalise

| Fullständig nyckel | Tidigare text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `component::ruuvitag_ble::entity::sensor::acceleration_total::name` | Total acceleration | Totalacceleration | Svensk sammansättning för det sammanlagda accelerationsvärdet. |

Ändringen sparades och lästes tillbaka via Lokalise API. Den finns i det
validerade HA-minnet i `swedish-tm`.

## Kontrollerade utan ändring

| Fullständig nyckel | Aktuell svensk text |
| --- | --- |
| `component::ruuvitag_ble::config::abort::already_configured` | Enheten är redan konfigurerad |
| `component::ruuvitag_ble::config::abort::already_in_progress` | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. |
| `component::ruuvitag_ble::config::abort::no_devices_found` | Inga enheter hittades i nätverket |
| `component::ruuvitag_ble::config::abort::not_supported` | Enheten stöds inte |
| `component::ruuvitag_ble::config::flow_title` | {name} |
| `component::ruuvitag_ble::config::step::bluetooth_confirm::description` | Vill du konfigurera {name}? |
| `component::ruuvitag_ble::config::step::user::data::address` | Enhet |
| `component::ruuvitag_ble::config::step::user::description` | Välj en enhet att konfigurera |
| `component::ruuvitag_ble::entity::sensor::acceleration_x::name` | X-acceleration |
| `component::ruuvitag_ble::entity::sensor::acceleration_y::name` | Y-acceleration |
| `component::ruuvitag_ble::entity::sensor::acceleration_z::name` | Z-acceleration |
| `component::ruuvitag_ble::entity::sensor::movement_counter::name` | Rörelseräknare |
| `component::ruuvitag_ble::entity::sensor::nox_index::name` | NOx-index |
| `component::ruuvitag_ble::entity::sensor::voc_index::name` | VOC-index |
| `component::ruuvitag_ble::entity::sensor::iaqs::name` | Poäng för inomhusluftkvalitet |

## Verifiering

- Lokalise API: alla 16 svenska översättningar hämtades direkt vid denna
  granskning.
- Termfamiljen är konsekvent: `Totalacceleration`, `X-acceleration`,
  `Y-acceleration` och `Z-acceleration`.
- Kemiska och tekniska beteckningar (`NOx`, `VOC`, `BLE`) är medvetet
  oförändrade.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
