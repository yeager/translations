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
| `component::iron_os::entity::button::settings_reset::name` | `Restore default settings` | `Återställ standardinställningar` | Granskad i Lokalise (ID 584039639); korrekt åtgärdsterm. |
| `component::iron_os::entity::button::settings_save::name` | `Save settings` | `Spara inställningar` | Granskad i Lokalise (ID 584039640); korrekt åtgärdsterm. |
| `component::iron_os::entity::number::accel_sensitivity::name` | `Motion sensitivity` | `Rörelsekänslighet` | Granskad i Lokalise (ID 572443004); korrekt reglageterm. |
| `component::iron_os::entity::number::boost_temp::name` | `Boost temperature` | `Boosttemperatur` | Ändrad från uppmaningsform till saklig reglageetikett; sparad och återläst i Lokalise (ID 572443005). |
| `component::iron_os::entity::number::calibration_offset::name` | `Calibration offset` | `Kalibreringsförskjutning` | Ändrad från direktengelsk konstruktion till svensk fackterm; sparad och återläst i Lokalise (ID 572443006). |
| `component::iron_os::entity::number::display_brightness::name` | `Display brightness` | `Skärmens ljusstyrka` | Granskad i Lokalise (ID 572443007); korrekt och idiomatisk etikett. |
| `component::iron_os::entity::number::hall_effect_sleep_time::name` | `Hall sensor sleep timeout` | `Tidsgräns för Hallsensorns viloläge` | Ändrad från blandad svensk–engelsk text till komplett svensk facketikett; sparad och återläst i Lokalise (ID 616289597). |
| `component::iron_os::entity::number::hall_sensitivity::name` | `Hall effect sensitivity` | `Halleffektkänslighet` | Ändrad från särskriven text med felaktig versalisering till korrekt svensk sammansättning; sparad och återläst i Lokalise (ID 572443008). |
| `component::iron_os::entity::number::keep_awake_pulse_delay::name` | `Keep-awake pulse delay` | `Fördröjning för vakenhållningspuls` | Ändrad från en ofullständig ord-för-ord-konstruktion till svensk reglageetikett; sparad och återläst i Lokalise (ID 572443009). |
| `component::iron_os::entity::number::keep_awake_pulse_duration::name` | `Keep-awake pulse duration` | `Varaktighet för vakenhållningspuls` | Ändrad från en ofullständig ord-för-ord-konstruktion till svensk reglageetikett; sparad och återläst i Lokalise (ID 572443010). |
| `component::iron_os::entity::number::keep_awake_pulse_power::name` | `Keep-awake pulse intensity` | `Intensitet för vakenhållningspuls` | Ändrad från en ofullständig ord-för-ord-konstruktion till svensk reglageetikett; sparad och återläst i Lokalise (ID 572443011). |
| `component::iron_os::entity::number::min_voltage_per_cell::name` | `Min. voltage per cell` | `Minsta spänning per cell` | Förkortningen expanderad till tydlig svensk reglageetikett; sparad och återläst i Lokalise (ID 572443012). |
| `component::iron_os::entity::number::pd_timeout::name` | `Power Delivery timeout` | `Tidsgräns för Power Delivery` | Ändrad från hybridterm till konsekvent svensk reglageetikett; sparad och återläst i Lokalise (ID 572443013). |
| `component::iron_os::entity::number::power_limit::name` | `Power limit` | `Effektgräns` | Granskad i Lokalise (ID 572443014); korrekt svensk teknisk sammansättning. |
| `component::iron_os::entity::number::qc_max_voltage::name` | `Quick Charge voltage` | `Quick Charge-spänning` | Granskad i Lokalise (ID 572443015); produktnamnet bevaras och svensk sammansättning är korrekt. |
| `component::iron_os::entity::number::setpoint_temperature::name` | `Setpoint temperature` | `Börvärde för temperatur` | Granskad i Lokalise (ID 512732275); tydlig och korrekt svensk reglageetikett. |
| `component::iron_os::entity::number::shutdown_timeout::name` | `Shutdown timeout` | `Tidsgräns för avstängning` | Ändrad från svensk–engelsk blandform till komplett svensk reglageetikett; sparad och återläst i Lokalise (ID 572443016). |

## Pågående täckning

Endast ovanstående rad är kontrollerad hittills. Inga ännu osparade förslag räknas som ändringar.
