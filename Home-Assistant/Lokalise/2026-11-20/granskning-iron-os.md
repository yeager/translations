# Home Assistant Core – IronOS

Datum: 2026-11-20. Komponenten granskas rad för rad mot aktuell Core-källa och motsvarande Lokalise-rad. Referenser ska bevaras som referenser och direkta enheter kontrolleras för term, kontext och format.

| Fullständig nyckel | Engelsk källa | Svensk text | Status och motivering |
| --- | --- | --- | --- |
| `component::iron_os::common::fast` | `Fast` | `Snabb` | Granskad i Lokalise (ID 580407935); korrekt i hastighetskontext. |
| `component::iron_os::common::slow` | `Slow` | `Långsam` | Granskad i Lokalise (ID 580407936); korrekt i hastighetskontext. |
| `component::iron_os::config::abort::already_configured` | `[%key:common::config_flow::abort::already_configured_device%]` | Oförändrad | Granskad i Lokalise (ID 511674991); korrekt Core-referens. |
| `component::iron_os::config::abort::cannot_connect` | `[%key:common::config_flow::error::cannot_connect%]` | Oförändrad | Granskad i Lokalise (ID 641222254); korrekt Core-referens. |
| `component::iron_os::config::abort::no_devices_found` | `[%key:common::config_flow::abort::no_devices_found%]` | Oförändrad | Granskad i Lokalise (ID 511674992); korrekt Core-referens. |
| `component::iron_os::config::abort::unknown` | `[%key:common::config_flow::error::unknown%]` | Oförändrad | Granskad i Lokalise (ID 641222255); korrekt Core-referens. |
| `component::iron_os::config::step::bluetooth_confirm::description` | `Do you want to set up {name}?` + Bluetooth-anvisning | Oförändrad | Granskad i Lokalise (ID 511674993); `{name}`, två radbrytningar och Markdown-kursivering är bevarade. |
| `component::iron_os::config::step::user::data::address` | `[%key:common::config_flow::data::device%]` | Oförändrad | Granskad i Lokalise (ID 511674994); korrekt Core-referens. |
| `component::iron_os::config::step::user::data_description::address` | Bluetooth-anvisning | Oförändrad | Granskad i Lokalise (ID 570330581); idiomatisk och komplett. |
| `component::iron_os::config::step::user::description` | `[%key:component::bluetooth::config::step::user::description%]` | Oförändrad | Granskad i Lokalise (ID 511674995); korrekt Core-referens. |
| `component::iron_os::config::error::cannot_connect` | `[%key:common::config_flow::error::cannot_connect%]` | Oförändrad | Granskad i Lokalise (ID 641222256); korrekt Core-referens. |
| `component::iron_os::config::error::unknown` | `[%key:common::config_flow::error::unknown%]` | Oförändrad | Granskad i Lokalise (ID 641222257); korrekt Core-referens. |
| `component::iron_os::entity::binary_sensor::tip_connected::name` | `Soldering tip` | `Lödspets` | Granskad i Lokalise (ID 575468261); korrekt fackterm. |

## Pågående täckning

Endast ovanstående rad är kontrollerad hittills. Inga ännu osparade förslag räknas som ändringar.
