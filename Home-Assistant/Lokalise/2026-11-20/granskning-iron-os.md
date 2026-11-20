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
| `component::iron_os::entity::number::sleep_temperature::name` | `Sleep temperature` | `Temperatur i viloläge` | Ändrad från felaktig hybridkonstruktion till idiomatisk svensk reglageetikett; sparad och återläst i Lokalise (ID 572443017). |
| `component::iron_os::entity::number::sleep_timeout::name` | `Sleep timeout` | `Tidsgräns för viloläge` | Ändrad från svensk–engelsk blandform till komplett svensk reglageetikett; sparad och återläst i Lokalise (ID 572443018). |
| `component::iron_os::entity::number::temp_increment_long::name` | `Long-press temperature step` | `Temperatursteg vid långtryckning` | Ändrad från felaktig särskrivning till korrekt svensk sammansättning; sparad och återläst i Lokalise (ID 572443019). |
| `component::iron_os::entity::number::temp_increment_short::name` | `Short-press temperature step` | `Temperatursteg vid korttryckning` | Ändrad från felaktig särskrivning till korrekt svensk sammansättning; sparad och återläst i Lokalise (ID 572443020). |
| `component::iron_os::entity::number::voltage_div::name` | `Voltage divider` | `Spänningsdelare` | Granskad i Lokalise (ID 572443021); korrekt svensk teknisk term. |
| `component::iron_os::entity::select::animation_speed::name` | `Animation speed` | `Animationshastighet` | Granskad i Lokalise (ID 580407937); korrekt svensk sammansättning. |
| `component::iron_os::entity::select::autostart_mode::name` | `Start-up behavior` | `Uppstartsbeteende` | Granskad i Lokalise (ID 580407942); korrekt svensk sammansättning. |
| `component::iron_os::entity::select::animation_speed::state::fast` | `[%key:component::iron_os::common::fast%]` | Oförändrad | Granskad i Lokalise (ID 580407938); korrekt referens till den verifierade gemensamma hastighetstermen `Snabb`. |
| `component::iron_os::entity::select::animation_speed::state::medium` | `[%key:common::state::medium%]` | Oförändrad | Granskad i Lokalise (ID 580407939); korrekt Core-referens till medelhastighet. |
| `component::iron_os::entity::select::animation_speed::state::off` | `[%key:common::state::off%]` | Oförändrad | Granskad i Lokalise (ID 580407940); korrekt Core-referens till avstängt läge. |
| `component::iron_os::entity::select::animation_speed::state::slow` | `[%key:component::iron_os::common::slow%]` | Oförändrad | Granskad i Lokalise (ID 580407941); korrekt referens till den verifierade gemensamma hastighetstermen `Långsam`. |
| `component::iron_os::entity::select::autostart_mode::state::sleeping` | `Sleeping mode` | `Viloläge` | Ändrad från det oidiomatiska `Sovläge` till etablerad Home Assistant-term; sparad och återläst i Lokalise (ID 580407945). |
| `component::iron_os::entity::select::autostart_mode::state::disabled` | `[%key:common::state::disabled%]` | Oförändrad | Granskad i Lokalise (ID 580407943); korrekt Core-referens till inaktiverat läge. |
| `component::iron_os::entity::select::autostart_mode::state::idle` | `Idle mode` | `Inaktivt läge` | Granskad i Lokalise (ID 580407944); korrekt och tydligt för ett startläge. |
| `component::iron_os::entity::select::autostart_mode::state::soldering` | `Soldering mode` | `Lödningsläge` | Granskad i Lokalise (ID 580407946); korrekt svensk sammansättning. |
| `component::iron_os::entity::select::desc_scroll_speed::name` | `Scrolling speed` | `Skrollhastighet` | Granskad i Lokalise (ID 580407947); korrekt etablerad sammansättning, även belagd i terminologibanken. |
| `component::iron_os::entity::select::desc_scroll_speed::state::fast` | `[%key:component::iron_os::common::fast%]` | Oförändrad | Granskad i Lokalise (ID 580407948); korrekt referens till den verifierade hastighetstermen `Snabb`. |
| `component::iron_os::entity::select::desc_scroll_speed::state::slow` | `[%key:component::iron_os::common::slow%]` | Oförändrad | Granskad i Lokalise (ID 580407949); korrekt referens till den verifierade hastighetstermen `Långsam`. |
| `component::iron_os::entity::select::locking_mode::name` | `Button locking mode` | `Läge för knapplåsning` | Granskad i Lokalise (ID 580407950); korrekt svensk reglageetikett. |
| `component::iron_os::entity::select::locking_mode::state::boost_only` | `Boost only` | `Endast boost` | Granskad i Lokalise (ID 580407951); kort och tydlig valetikett i låskontext. |
| `component::iron_os::entity::select::locking_mode::state::full_locking` | `Full locking` | `Fullständig låsning` | Ändrad från den oidiomatiska direktöversättningen `Full låsning`; sparad och återläst i Lokalise (ID 580407952). |
| `component::iron_os::entity::select::locking_mode::state::off` | `[%key:common::state::off%]` | Oförändrad | Granskad i Lokalise (ID 580407953); korrekt Core-referens till avstängt läge. |
| `component::iron_os::entity::select::logo_duration::name` | `Boot logo duration` | `Uppstartslogotypens visningstid` | Granskad i Lokalise (ID 580407954); exakt och idiomatisk svensk inställningsetikett. |
| `component::iron_os::entity::select::logo_duration::state::loop` | `Loop` | `Loop` | Granskad i Lokalise (ID 580407955); etablerad kort term för upprepad visning. |
| `component::iron_os::entity::select::logo_duration::state::off` | `[%key:common::state::off%]` | Oförändrad | Granskad i Lokalise (ID 580407956); korrekt Core-referens till avstängt läge. |
| `component::iron_os::entity::select::logo_duration::state::seconds_1` | `1 second` | `1 sekund` | Granskad i Lokalise (ID 580407957); korrekt singularform. |
| `component::iron_os::entity::select::logo_duration::state::seconds_2` | `2 seconds` | `2 sekunder` | Granskad i Lokalise (ID 580407958); korrekt pluralform. |
| `component::iron_os::entity::select::logo_duration::state::seconds_3` | `3 seconds` | `3 sekunder` | Granskad i Lokalise (ID 580407959); korrekt pluralform. |
| `component::iron_os::entity::select::logo_duration::state::seconds_4` | `4 seconds` | `4 sekunder` | Granskad i Lokalise (ID 580407960); korrekt pluralform. |
| `component::iron_os::entity::select::logo_duration::state::seconds_5` | `5 seconds` | `5 sekunder` | Granskad i Lokalise (ID 580407961); korrekt pluralform. |
| `component::iron_os::entity::select::min_dc_voltage_cells::name` | `Power source` | `Strömkälla` | Granskad i Lokalise (ID 580407962); korrekt svensk teknisk term. |
| `component::iron_os::entity::select::min_dc_voltage_cells::state::battery_3s` | `3S (3 cells)` | `3S (3 celler)` | Granskad i Lokalise (ID 580407963); korrekt batteribeteckning och pluralform. |
| `component::iron_os::entity::select::min_dc_voltage_cells::state::battery_4s` | `4S (4 cells)` | `4S (4 celler)` | Granskad i Lokalise (ID 580407964); korrekt batteribeteckning och pluralform. |
| `component::iron_os::entity::select::min_dc_voltage_cells::state::battery_5s` | `5S (5 cells)` | `5S (5 celler)` | Granskad i Lokalise (ID 580407965); korrekt batteribeteckning och pluralform. |
| `component::iron_os::entity::select::min_dc_voltage_cells::state::battery_6s` | `6S (6 cells)` | `6S (6 celler)` | Granskad i Lokalise (ID 580407966); korrekt batteribeteckning och pluralform. |
| `component::iron_os::entity::select::min_dc_voltage_cells::state::no_battery` | `External power supply (DC)` | `Extern strömförsörjning (DC)` | Granskad i Lokalise (ID 580407967); korrekt svensk teknisk term och enhet. |
| `component::iron_os::entity::select::orientation_mode::name` | `Display orientation mode` | `Läge för skärmorientering` | Granskad i Lokalise (ID 580407968); korrekt svensk reglageetikett. |
| `component::iron_os::entity::select::orientation_mode::state::auto` | `[%key:common::state::auto%]` | Oförändrad | Granskad i Lokalise (ID 580407969); korrekt Core-referens för automatiskt läge. |
| `component::iron_os::entity::select::orientation_mode::state::left_handed` | `Left-handed` | `Vänsterhänt` | Granskad i Lokalise (ID 580407970); korrekt svensk användarinställning. |
| `component::iron_os::entity::select::orientation_mode::state::right_handed` | `Right-handed` | `Högerhänt` | Granskad i Lokalise (ID 580407971); korrekt svensk användarinställning. |
| `component::iron_os::entity::select::temp_unit::name` | `Temperature display unit` | `Enhet för temperaturvisning` | Granskad i Lokalise (ID 580407972); korrekt och tydlig svensk etikett. |
| `component::iron_os::entity::select::temp_unit::state::celsius` | `Celsius (°C)` | `Celsius (°C)` | Granskad i Lokalise (ID 580407973); namn och enhet är korrekta. |
| `component::iron_os::entity::select::temp_unit::state::fahrenheit` | `Fahrenheit (°F)` | `Fahrenheit (°F)` | Granskad i Lokalise (ID 580407974); namn och enhet är korrekta. |
| `component::iron_os::entity::select::tip_type::name` | `Soldering tip type` | `Typ av lödspets` | Granskad i Lokalise (ID 616289598); korrekt svensk fackterm. |
| `component::iron_os::entity::select::tip_type::state::auto` | `Auto sense` | `Automatisk avkänning` | Granskad i Lokalise (ID 616289599); korrekt funktionsterm. |
| `component::iron_os::entity::select::tip_type::state::pine_short` | `Pinecil short tip` | `Pinecil kort lödspets` | Kompletterad med facktermen `lödspets`; sparad och återläst i Lokalise (ID 616289600). |
| `component::iron_os::entity::select::tip_type::state::pts200` | `PTS200 short tip` | `PTS200 kort lödspets` | Kompletterad med facktermen `lödspets`; sparad och återläst i Lokalise (ID 616289601). |
| `component::iron_os::entity::select::tip_type::state::ts100_long` | `TS100 long/Hakko T12 tip` | `TS100 lång lödspets/Hakko T12-lödspets` | Kompletterad med tydliga facktermer för båda spetsalternativen; sparad och återläst i Lokalise (ID 616289602). |
| `component::iron_os::entity::select::usb_pd_mode::name` | `Power Delivery 3.1 EPR` | `Power Delivery 3.1 EPR` | Granskad i Lokalise (ID 592275690); standardnamn och förkortning ska behållas. |
| `component::iron_os::entity::select::usb_pd_mode::state::off` | `[%key:common::state::off%]` | Oförändrad | Granskad i Lokalise (ID 592275691); korrekt Core-referens. |
| `component::iron_os::entity::select::usb_pd_mode::state::on` | `[%key:common::state::on%]` | Oförändrad | Granskad i Lokalise (ID 592275692); korrekt Core-referens. |
| `component::iron_os::entity::sensor::estimated_power::name` | `Estimated power` | `Beräknad effekt` | Granskad i Lokalise (ID 511674996); korrekt svensk teknisk term. |
| `component::iron_os::entity::sensor::hall_sensor::name` | `Hall effect strength` | `Halleffektstyrka` | Granskad i Lokalise (ID 511674997); korrekt svensk sammansättning. |
| `component::iron_os::entity::sensor::handle_temperature::name` | `Handle temperature` | `Handtagets temperatur` | Granskad i Lokalise (ID 511674998); korrekt svensk sensorbenämning. |
| `component::iron_os::entity::sensor::live_temperature::name` | `Tip temperature` | `Spetstemperatur` | Granskad i Lokalise (ID 511674999); korrekt svensk sammansättning i lödningskontext. |
| `component::iron_os::entity::sensor::max_tip_temp_ability::name` | `Max tip temperature` | `Maximal spetstemperatur` | Ändrad från förkortningen `Max` till komplett svensk sensorbenämning; sparad och återläst i Lokalise (ID 511675000). |
| `component::iron_os::entity::sensor::movement_time::name` | `Last movement time` | `Tidpunkt för senaste rörelse` | Ändrad från ofullständiga `Senaste rörelse` så att tidsaspekten uttrycks; sparad och återläst i Lokalise (ID 511675001). |
| `component::iron_os::entity::sensor::operating_mode::name` | `Operating mode` | `Driftläge` | Granskad i Lokalise (ID 511675002); etablerad svensk teknisk term. |
| `component::iron_os::entity::sensor::operating_mode::state::boost` | `Boost` | `Boost` | Granskad i Lokalise (ID 511675003); etablerat lägesnamn i denna lödningskontext. |
| `component::iron_os::entity::sensor::operating_mode::state::cjc_calibration` | `CJC calibration` | `CJC-kalibrering` | Granskad i Lokalise (ID 616289603); teknisk förkortning bevarad med korrekt svensk sammansättning. |
| `component::iron_os::entity::sensor::operating_mode::state::debug` | `Debug` | `Debug` | Granskad i Lokalise (ID 511675004); etablerat tekniskt lägesnamn. |
| `component::iron_os::entity::sensor::operating_mode::state::hibernating` | `Hibernating` | `Viloläge` | Granskad i Lokalise (ID 616289604); korrekt etablerad term. |
| `component::iron_os::entity::sensor::operating_mode::state::idle` | `[%key:common::state::idle%]` | Oförändrad | Granskad i Lokalise (ID 511675005); korrekt Core-referens. |
| `component::iron_os::entity::sensor::operating_mode::state::initialisation_done` | `Initialisation done` | `Initialisering genomförd` | Granskad i Lokalise (ID 616289605); korrekt svensk statusfras. |
| `component::iron_os::entity::sensor::operating_mode::state::settings` | `Settings` | `Inställningar` | Granskad i Lokalise (ID 511675006); korrekt lägesnamn. |
| `component::iron_os::entity::sensor::operating_mode::state::sleeping` | `Sleeping` | `Sover` | Granskad i Lokalise (ID 511675007); korrekt pågående statusform. |
| `component::iron_os::entity::sensor::operating_mode::state::soldering` | `Soldering` | `Löder` | Granskad i Lokalise (ID 511675008); korrekt pågående statusform. |
| `component::iron_os::entity::sensor::operating_mode::state::soldering_profile` | `Soldering profile` | `Lödningsprofil` | Granskad i Lokalise (ID 616289606); korrekt svensk sammansättning. |
| `component::iron_os::entity::sensor::operating_mode::state::startup_logo` | `Booting` | `Startar` | Granskad i Lokalise (ID 616289607); korrekt pågående statusform. |
| `component::iron_os::entity::sensor::operating_mode::state::startup_warnings` | `Startup warnings` | `Varningar vid uppstart` | Granskad i Lokalise (ID 616289608); korrekt och idiomatisk svensk statusfras. |
| `component::iron_os::entity::sensor::operating_mode::state::temperature_adjust` | `Temperature adjust` | `Temperaturjustering` | Granskad i Lokalise (ID 616289609); korrekt svensk teknisk sammansättning. |
| `component::iron_os::entity::sensor::operating_mode::state::thermal_runaway` | `Thermal runaway` | `Termisk rusning` | Granskad i Lokalise (ID 616289610); korrekt svensk teknisk säkerhetsterm. |
| `component::iron_os::entity::sensor::operating_mode::state::usb_pd_debug` | `USB PD debug` | `USB PD-felsökning` | Granskad i Lokalise (ID 616289611); standardförkortning bevarad och korrekt svensk sammansättning. |
| `component::iron_os::entity::sensor::power_pwm_level::name` | `Power level` | `Effektnivå` | Granskad i Lokalise (ID 511675009); korrekt svensk teknisk term i UI-kontexten. |

## Pågående täckning

Endast ovanstående rad är kontrollerad hittills. Inga ännu osparade förslag räknas som ändringar.
