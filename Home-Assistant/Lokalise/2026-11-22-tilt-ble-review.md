# Home Assistant Core – Tilt BLE

Datum: 2026-11-22

Alla sju Tilt BLE-strängar är granskade rad för rad mot källtexten och
återlästa från Lokalise API. Ingen ändring behövdes.

| Nyckel | Svenska |
| --- | --- |
| `component::tilt_ble::config::abort::already_configured` | Enheten är redan konfigurerad |
| `component::tilt_ble::config::abort::already_in_progress` | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. |
| `component::tilt_ble::config::abort::no_devices_found` | Inga enheter hittades i nätverket |
| `component::tilt_ble::config::flow_title` | {name} |
| `component::tilt_ble::config::step::bluetooth_confirm::description` | Vill du konfigurera {name}? |
| `component::tilt_ble::config::step::user::data::address` | Enhet |
| `component::tilt_ble::config::step::user::description` | Välj en enhet att konfigurera |

Platshållaren `{name}` är bevarad i båda berörda rader. Inga pluralformer
eller referenser förekommer. Hunspell och svlang ger endast förväntade
platshållarträffar. Lokalise API:s verifieringsflagga är inte skrivbar med
aktuell behörighet; granskningsspåret finns här.
