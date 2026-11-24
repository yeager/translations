# Home Assistant Core – historisk avstämning 16561–16680

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 86 direkta källtexter matchar HA Core-källan; 18 referensanvändningar med 12 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 16 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 16561 | 873763036 | `component::opensensemap::issues::deprecated_air_quality_in_use::title` | The openSenseMap air quality entity is deprecated | Entiteten för luftkvalitet i openSenseMap är utfasad | Shared reference target checked |
| 16562 | 873763035 | `component::opensensemap::issues::deprecated_air_quality_in_use::description` | The openSenseMap air quality entity (`{entity_id}`) is deprecated. The particulate matter measurements it provided are now available as individual sensor entities.<br><br>It is still used in the following automations or scripts:<br>{items}<br><br>Update them to use the sensor entities, then disable the air quality entity to have it removed after the next restart. | Entiteten för luftkvalitet i openSenseMap (`{entity_id}`) är utfasad. De mätningar av partiklar som den tillhandahöll finns nu tillgängliga som enskilda sensorentiteter.<br><br>Den används fortfarande i följande automatiseringar eller skript:<br>{items}<br><br>Uppdatera dem så att de använder sensorentiteterna och inaktivera sedan luftkvalitetsentiteten för att den ska kunna tas bort efter nästa omstart. | Core-literal match |
| 16563 | 873763034 | `component::opensensemap::issues::deprecated_air_quality::title` | The openSenseMap air quality entity is deprecated | Entiteten för luftkvalitet i openSenseMap är utfasad | Core-literal match |
| 16564 | 873763033 | `component::opensensemap::issues::deprecated_air_quality::description` | The openSenseMap air quality entity (`{entity_id}`) is deprecated. The particulate matter measurements it provided are now available as individual sensor entities.<br><br>Update your dashboards and templates to use those sensor entities, then disable the air quality entity to have it removed after the next restart. | Luftkvalitetsenheten i openSenseMap (`{entity_id}`) är utfasad. De mätvärden för partiklar som den tidigare tillhandahöll finns nu tillgängliga som enskilda sensorenheter.<br><br>Uppdatera dina instrumentpaneler och mallar så att de använder dessa sensorenheter, och inaktivera sedan luftkvalitetsenheten för att ta bort den efter nästa omstart. | Core-literal match |
| 16565 | 873743947 | `component::modern_forms::exceptions::invalid_response::message` | Invalid response from the Modern Forms device | Ogiltigt svar från Modern Forms-enheten | Core-literal match |
| 16566 | 873743946 | `component::modern_forms::exceptions::communication_error::message` | Error communicating with the Modern Forms device | Fel vid kommunikation med Modern Forms-enheten | Core-literal match |
| 16567 | 873737315 | `component::whirlpool::entity::button::oven_stop_upper::name` | Upper oven stop | Övre ugnsstopp | Core-literal match |
| 16568 | 873737314 | `component::whirlpool::entity::button::oven_stop_lower::name` | Lower oven stop | Nedre ugnsstopp | Core-literal match |
| 16569 | 873737313 | `component::whirlpool::entity::button::oven_stop::name` | Stop | Stopp | Core-literal match |
| 16570 | 873736807 | `component::reolink::exceptions::webhook_no_url::message` | Error registering URL for webhook {event_id}: Home Assistant URL is not available | Fel vid registrering av URL för webhook {event_id}: Home Assistant-URL:en är inte tillgänglig | Core-literal match |
| 16571 | 873020618 | `component::nasweb::exceptions::config_entry_error_serial_mismatch::message` | Connected to different NASweb device (serial number mismatch). | Ansluten till en annan NASweb-enhet (serienumret stämmer inte överens). | Core-literal match |
| 16572 | 873014480 | `component::hue::config::step::init::data::id` | Hue bridge | Hue-brygga | Core-literal match |
| 16573 | 873014255 | `component::islamic_prayer_times::config::step::user::data::name` | Name | Namn | Source-path follow-up open |
| 16574 | 873014254 | `component::islamic_prayer_times::config::step::user::data::location` | Location | Plats | Shared reference target checked |
| 16575 | 873013929 | `component::lacrosse_view::config::step::location::data::location` | Location | Plats | Shared reference target checked |
| 16576 | 873013624 | `component::melnor::config::step::pick_device::data::address` | Device | Enhet | Shared reference target checked |
| 16577 | 873013305 | `component::meteoclimatic::config::step::user::data_description::station_code` | Looks like ESCAT4300000043206B | Ser ut som ESCAT4300000043206B | Core-literal match |
| 16578 | 873013304 | `component::meteoclimatic::config::step::user::data::station_code` | Station code | Stationskod | Core-literal match |
| 16579 | 873013271 | `component::motionblinds_ble::config::step::confirm::data::blind_type` | Blind type | Rullgardinstyp | Core-literal match |
| 16580 | 873012951 | `component::blink::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference target checked |
| 16581 | 873012950 | `component::blink::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 16582 | 873000341 | `component::lookin::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 16583 | 873000340 | `component::gogogate2::config::step::user::data::device` | Device | Enhet | Shared reference target checked |
| 16584 | 873000339 | `component::flux_led::config::step::pick_device::data::device` | Device | Enhet | Shared reference target checked |
| 16585 | 873000334 | `component::tuya::config::step::scan::data::QR` | QR code | QR-kod | Core-literal match |
| 16586 | 873000332 | `component::israel_rail::exceptions::request_timeout::message` | Timeout connecting to the Israel Rail API for {config_title}: {error} | Timeout vid anslutning till Israel Rail API för {config_title}: {error} | Core-literal match |
| 16587 | 873000328 | `component::vesync::exceptions::server_error::message` | Server error occurred while connecting to VeSync | Ett serverfel uppstod vid anslutningen till VeSync | Core-literal match |
| 16588 | 873000327 | `component::vesync::exceptions::invalid_auth::message` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 16589 | 873000326 | `component::vesync::exceptions::api_response_error::message` | Invalid response from the VeSync API | Ogiltigt svar från VeSync API | Core-literal match |
| 16590 | 873000324 | `component::plaato::options::step::user::data::scan_interval` | Update interval (minutes) | Uppdateringsintervall (minuter) | Source-path follow-up open |
| 16591 | 873000320 | `component::snooz::config::step::user::data::name` | Name | Namn | Source-path follow-up open |
| 16592 | 872996051 | `component::homematicip_cloud::entity::sensor::window_state::state::tilted` | Tilted | Lutad | Core-literal match |
| 16593 | 872996050 | `component::homematicip_cloud::entity::sensor::window_state::state::open` | Open | Öppen | Shared reference target checked |
| 16594 | 872996049 | `component::homematicip_cloud::entity::sensor::window_state::state::closed` | Closed | Stängd | Shared reference target checked |
| 16595 | 872996048 | `component::homematicip_cloud::entity::sensor::window_state::name` | Window state | Fönstertillstånd | Core-literal match |
| 16596 | 872976121 | `component::yoto::exceptions::config_update_failed::message` | Failed to update Yoto player settings. | Det gick inte att uppdatera inställningarna för Yoto-spelaren. | Core-literal match |
| 16597 | 872976120 | `component::yoto::entity::time::night_mode_start::name` | Night mode start | Nattläge start | Core-literal match |
| 16598 | 872976119 | `component::yoto::entity::time::day_mode_start::name` | Day mode start | Dagläge start | Core-literal match |
| 16599 | 872975402 | `component::template::selector::sensor_device_class::options::uptime` | Uptime | Upptid | Source-path follow-up open |
| 16600 | 872975401 | `component::template::selector::number_device_class::options::volatile_organic_compounds_parts` | Volatile organic compounds parts | Delar av flyktiga organiska föreningar (VOC) | Source-path follow-up open |
| 16601 | 872975400 | `component::template::selector::number_device_class::options::monetary` | Monetary balance | Monetärt saldo | Source-path follow-up open |
| 16602 | 872975399 | `component::template::selector::number_device_class::options::energy_distance` | Energy per distance | Energi per sträcka | Source-path follow-up open |
| 16603 | 872975398 | `component::template::selector::number_device_class::options::duration` | Duration | Varaktighet | Source-path follow-up open |
| 16604 | 872975397 | `component::template::selector::number_device_class::options::data_size` | Data size | Datastorlek | Source-path follow-up open |
| 16605 | 872970587 | `component::miele::entity::sensor::program_id::state::rinse_and_hold` | Rinse and hold | Skölj och håll | Core-literal match |
| 16606 | 872970074 | `component::knx::options::step::communication_settings::sections::telegram_store_section::name` | Telegram store settings | Inställningar för Telegram-lagring | Core-literal match |
| 16607 | 872970073 | `component::knx::options::step::communication_settings::sections::telegram_store_section::data_description::telegram_db_retention_days` | Number of days to keep telegram history. Older telegrams are automatically deleted nightly at 3 AM. Set to `0` to delete all telegram history on every nightly run. | Antal dagar som telegramhistoriken ska sparas. Äldre telegram raderas automatiskt varje natt kl. 03.00. Ställ in värdet på `0` för att radera hela telegramhistoriken varje natt. | Core-literal match |
| 16608 | 872970072 | `component::knx::options::step::communication_settings::sections::telegram_store_section::data_description::telegram_db_load_hours` | Number of hours of telegram history to load when the group monitor is opened. | Antal timmar telegramhistorik som ska läsas in när gruppövervakaren öppnas. | Core-literal match |
| 16609 | 872970071 | `component::knx::options::step::communication_settings::sections::telegram_store_section::data::telegram_db_retention_days` | Retention period | Lagringstid | Core-literal match |
| 16610 | 872970070 | `component::knx::options::step::communication_settings::sections::telegram_store_section::data::telegram_db_load_hours` | Group monitor history | Gruppövervakningshistorik | Core-literal match |
| 16611 | 872970069 | `component::knx::issues::telegram_storage_error::title` | KNX telegram storage error | Fel vid lagring av KNX-telegram | Core-literal match |
| 16612 | 872970068 | `component::knx::issues::telegram_storage_error::description` | The configured KNX telegram storage backend failed to initialize. As a result, KNX telegrams are currently not being stored. Check the logs for details on the error and ensure your database is accessible. | Det gick inte att initialisera det konfigurerade lagringssystemet för KNX-telegram. Detta innebär att KNX-telegram för närvarande inte lagras. Kontrollera loggfilerna för mer information om felet och se till att databasen är tillgänglig. | Core-literal match |
| 16613 | 872542683 | `component::blebox::entity::sensor::reverse_reactive_energy_n::name` | Reverse reactive energy {index} | Omvänd reaktiv energi {index} | Core-literal match |
| 16614 | 872542682 | `component::blebox::entity::sensor::reverse_reactive_energy::name` | Reverse reactive energy | Omvänd reaktiv energi | Core-literal match |
| 16615 | 872542681 | `component::blebox::entity::sensor::forward_reactive_energy_n::name` | Forward reactive energy {index} | Framåtriktad reaktiv energi {index} | Core-literal match |
| 16616 | 872542680 | `component::blebox::entity::sensor::forward_reactive_energy::name` | Forward reactive energy | Framåtriktad reaktiv energi | Core-literal match |
| 16617 | 872542557 | `component::blebox::config::step::reauth_confirm::title` | Reauthenticate your BleBox device | Återautentisera din BleBox-enhet | Core-literal match |
| 16618 | 872542556 | `component::blebox::config::step::reauth_confirm::description` | Enter credentials for the BleBox device at {address}. | Ange inloggningsuppgifter för BleBox-enheten på {address}. | Core-literal match |
| 16619 | 872542555 | `component::blebox::config::step::reauth_confirm::data_description::username` | The username for your BleBox device. | Användarnamnet för din BleBox-enhet. | Shared reference target checked |
| 16620 | 872542554 | `component::blebox::config::step::reauth_confirm::data_description::password` | The password for your BleBox device. | Lösenordet för din BleBox-enhet. | Shared reference target checked |
| 16621 | 872542553 | `component::blebox::config::step::reauth_confirm::data::username` | Username | Användarnamn | Shared reference target checked |
| 16622 | 872542552 | `component::blebox::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 16623 | 872542551 | `component::blebox::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 16624 | 872542550 | `component::blebox::config::abort::unsupported_device_version` | BleBox device has outdated firmware. Please upgrade it first. | BleBox-enheten har föråldrad firmware. Uppgradera den först. | Shared reference target checked |
| 16625 | 872542549 | `component::blebox::config::abort::unsupported_device_response` | The BleBox device returned an unrecognized response. | BleBox-enheten returnerade ett okänt svar. | Core-literal match |
| 16626 | 872542548 | `component::blebox::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 16627 | 872542547 | `component::blebox::config::abort::authorization_required` | The BleBox device requires authentication. | BleBox-enheten kräver autentisering. | Core-literal match |
| 16628 | 872345631 | `component::hypontech::config::step::user::data_description::oem` | The brand that sold the equipment | Det varumärke som sålde utrustningen | Core-literal match |
| 16629 | 872345630 | `component::hypontech::config::step::user::data::oem` | Manufacturer | Tillverkare | Core-literal match |
| 16630 | 872343616 | `component::opendisplay::exceptions::setup_connection_error::message` | Failed to connect to OpenDisplay device. | Det gick inte att ansluta till OpenDisplay-enheten. | Core-literal match |
| 16631 | 872091299 | `component::melcloud_home::entity::sensor::tank_water_temperature::name` | Tank water temperature | Tankens vattentemperatur | Core-literal match |
| 16632 | 872091298 | `component::melcloud_home::entity::sensor::room_temperature_zone_2::name` | Zone 2 room temperature | Rumstemperatur i zon 2 | Core-literal match |
| 16633 | 872091297 | `component::melcloud_home::entity::sensor::room_temperature_zone_1::name` | Zone 1 room temperature | Rumstemperatur i zon 1 | Core-literal match |
| 16634 | 872091296 | `component::melcloud_home::entity::sensor::room_temperature::name` | Room temperature | Rumstemperatur | Core-literal match |
| 16635 | 871988640 | `component::litterrobot::entity::sensor::scoops_saved_count::unit_of_measurement` | scoops | skopor | Core-literal match |
| 16636 | 871988639 | `component::litterrobot::entity::sensor::scoops_saved_count::name` | Scoops saved | Sparade skopor | Core-literal match |
| 16637 | 871988638 | `component::litterrobot::entity::sensor::next_filter_replacement::name` | Next filter replacement | Nästa filterbyte | Core-literal match |
| 16638 | 871988637 | `component::litterrobot::entity::button::change_filter::name` | Change filter | Byt filter | Core-literal match |
| 16639 | 871988636 | `component::litterrobot::entity::binary_sensor::online::name` | Online | Online | Core-literal match |
| 16640 | 871988635 | `component::litterrobot::entity::binary_sensor::laser_dirty::name` | Laser dirty | Lasern är smutsig | Core-literal match |
| 16641 | 871988634 | `component::litterrobot::entity::binary_sensor::drawer_removed::name` | Drawer removed | Lådan har tagits bort | Core-literal match |
| 16642 | 871988633 | `component::litterrobot::entity::binary_sensor::bonnet_removed::name` | Bonnet removed | Huven är borttagen | Core-literal match |
| 16643 | 871988468 | `component::blebox::entity::sensor::voltage_n::name` | Voltage {index} | Spänning {index} | Core-literal match |
| 16644 | 871988467 | `component::blebox::entity::sensor::voltage::name` | Voltage | Spänning | Source-path follow-up open |
| 16645 | 871988466 | `component::blebox::entity::sensor::temperature_n::name` | Temperature {index} | Temperatur {index} | Core-literal match |
| 16646 | 871988465 | `component::blebox::entity::sensor::temperature::name` | Temperature | Temperatur | Source-path follow-up open |
| 16647 | 871988464 | `component::blebox::entity::sensor::reverse_active_energy_n::name` | Reverse active energy {index} | Omvänd aktiv energi {index} | Core-literal match |
| 16648 | 871988463 | `component::blebox::entity::sensor::reverse_active_energy::name` | Reverse active energy | Omvänd aktiv energi | Core-literal match |
| 16649 | 871988462 | `component::blebox::entity::sensor::reactive_power_n::name` | Reactive power {index} | Reaktiv effekt {index} | Core-literal match |
| 16650 | 871988461 | `component::blebox::entity::sensor::reactive_power::name` | Reactive power | Reaktiv effekt | Source-path follow-up open |
| 16651 | 871988460 | `component::blebox::entity::sensor::power_consumption::name` | Energy last hour | Energi senaste timmen | Core-literal match |
| 16652 | 871988459 | `component::blebox::entity::sensor::open_status::name` | Open status | Öppningsstatus | Core-literal match |
| 16653 | 871988458 | `component::blebox::entity::sensor::frequency_n::name` | Frequency {index} | Frekvens {index} | Core-literal match |
| 16654 | 871988457 | `component::blebox::entity::sensor::frequency::name` | Frequency | Frekvens | Source-path follow-up open |
| 16655 | 871988456 | `component::blebox::entity::sensor::forward_active_energy_n::name` | Forward active energy {index} | Framåtriktad aktiv energi {index} | Core-literal match |
| 16656 | 871988455 | `component::blebox::entity::sensor::forward_active_energy::name` | Forward active energy | Framåtriktad aktiv energi | Core-literal match |
| 16657 | 871988454 | `component::blebox::entity::sensor::current_n::name` | Current {index} | Ström {index} | Core-literal match |
| 16658 | 871988453 | `component::blebox::entity::sensor::current::name` | Current | Ström | Source-path follow-up open |
| 16659 | 871988452 | `component::blebox::entity::sensor::apparent_power_n::name` | Apparent power {index} | Skenbar effekt {index} | Core-literal match |
| 16660 | 871988451 | `component::blebox::entity::sensor::apparent_power::name` | Apparent power | Skenbar effekt | Source-path follow-up open |
| 16661 | 871988450 | `component::blebox::entity::sensor::active_power_n::name` | Active power {index} | Aktiv effekt {index} | Core-literal match |
| 16662 | 871988449 | `component::blebox::entity::sensor::active_power::name` | Active power | Aktiv effekt | Core-literal match |
| 16663 | 871988448 | `component::blebox::entity::light::channel::name` | Channel {index} | Kanal {index} | Core-literal match |
| 16664 | 871988447 | `component::blebox::config::step::user::data_description::username` | The username for your BleBox device. | Användarnamnet för din BleBox-enhet. | Core-literal match |
| 16665 | 871988446 | `component::blebox::config::step::user::data_description::port` | The port of your BleBox device. | Porten på din BleBox-enhet. | Core-literal match |
| 16666 | 871988445 | `component::blebox::config::step::user::data_description::password` | The password for your BleBox device. | Lösenordet för din BleBox-enhet. | Core-literal match |
| 16667 | 871988444 | `component::blebox::config::step::user::data_description::host` | The IP address of your BleBox device. | IP-adressen till din BleBox-enhet. | Core-literal match |
| 16668 | 871822148 | `component::melcloud_home::entity::binary_sensor::standby::name` | Standby | Viloläge | Core-literal match |
| 16669 | 871822147 | `component::melcloud_home::entity::binary_sensor::forced_hot_water::name` | Forced hot water | Forcerat varmvatten | Core-literal match |
| 16670 | 871822146 | `component::melcloud_home::entity::binary_sensor::error::name` | Error | Fel | Core-literal match |
| 16671 | 871626799 | `component::blebox::entity::sensor::co2_level::state::unhealthy` | Unhealthy | Ohälsosam | Core-literal match |
| 16672 | 871626798 | `component::blebox::entity::sensor::co2_level::state::poor` | Poor | Dålig | Core-literal match |
| 16673 | 871626797 | `component::blebox::entity::sensor::co2_level::state::medium` | Medium | Måttlig | Core-literal match |
| 16674 | 871626796 | `component::blebox::entity::sensor::co2_level::state::hazardous` | Hazardous | Farlig | Core-literal match |
| 16675 | 871626795 | `component::blebox::entity::sensor::co2_level::state::good` | Good | Bra | Core-literal match |
| 16676 | 871626794 | `component::blebox::entity::sensor::co2_level::state::excellent` | Excellent | Utmärkt | Core-literal match |
| 16677 | 871626793 | `component::blebox::entity::sensor::co2_level::state::acceptable` | Acceptable | Acceptabel | Core-literal match |
| 16678 | 871626792 | `component::blebox::entity::sensor::co2_level::name` | Carbon dioxide level | Koldioxidnivå | Core-literal match |
| 16679 | 871626734 | `component::reolink::exceptions::uid_mismatch::message` | UID {uid} of Reolink camera "{name}" did not match the stored configuration UID {conf_uid}, please check the connection details | UID-numret {uid} för Reolink-kameran ”{name}” stämde inte överens med det sparade konfigurations-UID-numret {conf_uid}. Kontrollera anslutningsuppgifterna. | Core-literal match |
| 16680 | 871578740 | `component::vistapool::entity::binary_sensor::redox_pump::name` | Redox pump | Redoxpump | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 873014255 | `component::islamic_prayer_times::config::step::user::data::name` | Name |
| 873000324 | `component::plaato::options::step::user::data::scan_interval` | Update interval (minutes) |
| 873000320 | `component::snooz::config::step::user::data::name` | Name |
| 872975402 | `component::template::selector::sensor_device_class::options::uptime` | Uptime |
| 872975401 | `component::template::selector::number_device_class::options::volatile_organic_compounds_parts` | Volatile organic compounds parts |
| 872975400 | `component::template::selector::number_device_class::options::monetary` | Monetary balance |
| 872975399 | `component::template::selector::number_device_class::options::energy_distance` | Energy per distance |
| 872975398 | `component::template::selector::number_device_class::options::duration` | Duration |
| 872975397 | `component::template::selector::number_device_class::options::data_size` | Data size |
| 872542548 | `component::blebox::config::abort::reauth_successful` | Re-authentication was successful |
| 871988467 | `component::blebox::entity::sensor::voltage::name` | Voltage |
| 871988465 | `component::blebox::entity::sensor::temperature::name` | Temperature |
| 871988461 | `component::blebox::entity::sensor::reactive_power::name` | Reactive power |
| 871988457 | `component::blebox::entity::sensor::frequency::name` | Frequency |
| 871988453 | `component::blebox::entity::sensor::current::name` | Current |
| 871988451 | `component::blebox::entity::sensor::apparent_power::name` | Apparent power |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
