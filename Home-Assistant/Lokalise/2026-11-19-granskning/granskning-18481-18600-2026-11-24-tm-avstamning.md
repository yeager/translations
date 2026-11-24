# Home Assistant Core – historisk avstämning 18481–18600

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 92 direkta källtexter matchar HA Core-källan; 19 referensanvändningar med 13 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 9 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 18481 | 852816763 | `component::backup::entity::event::automatic_backup_event::state_attributes::failed_reason::state::unknown_error` | Unknown error | Okänt fel | Core-literal match |
| 18482 | 852816762 | `component::backup::entity::event::automatic_backup_event::state_attributes::failed_reason::state::password_incorrect` | Password incorrect | Felaktigt lösenord | Core-literal match |
| 18483 | 852816761 | `component::backup::entity::event::automatic_backup_event::state_attributes::failed_reason::state::multiple_errors` | Multiple errors | Flera fel | Core-literal match |
| 18484 | 852816760 | `component::backup::entity::event::automatic_backup_event::state_attributes::failed_reason::state::invalid_backup_filename` | Invalid backup filename | Ogiltigt filnamn för säkerhetskopian | Core-literal match |
| 18485 | 852816759 | `component::backup::entity::event::automatic_backup_event::state_attributes::failed_reason::state::decrypt_on_download_not_supported` | Decrypt on download not supported | Dekryptering vid nedladdning stöds inte | Core-literal match |
| 18486 | 852816758 | `component::backup::entity::event::automatic_backup_event::state_attributes::failed_reason::state::backup_reader_writer_error` | Backup reader/writer error | Fel vid läsning/skrivning för säkerhetskopia | Core-literal match |
| 18487 | 852816757 | `component::backup::entity::event::automatic_backup_event::state_attributes::failed_reason::state::backup_not_found` | Backup not found | Säkerhetskopian hittades inte | Core-literal match |
| 18488 | 852816756 | `component::backup::entity::event::automatic_backup_event::state_attributes::failed_reason::state::backup_manager_error` | Backup manager error | Fel i säkerhetskopieringshanteraren | Core-literal match |
| 18489 | 852816755 | `component::backup::entity::event::automatic_backup_event::state_attributes::failed_reason::state::backup_agent_unreachable` | Backup agent unreachable | Säkerhetskopieringsagenten är inte tillgänglig | Core-literal match |
| 18490 | 852816754 | `component::backup::entity::event::automatic_backup_event::state_attributes::failed_reason::state::backup_agent_error` | Backup agent error | Fel på säkerhetskopieringsagent | Core-literal match |
| 18491 | 852786647 | `component::motioneye::options::step::init::sections::more_options::name` | More options | Fler alternativ | Core-literal match |
| 18492 | 852786646 | `component::motioneye::options::step::init::sections::more_options::data::stream_url_template` | Stream URL template | Mall för webbadress för ström | Core-literal match |
| 18493 | 852770376 | `component::hassio::exceptions::supervisor_not_connected::message` | Not connected with the supervisor / system too busy | Inte ansluten till Supervisor / systemet är för upptaget | Core-literal match |
| 18494 | 852595210 | `component::plex::config::step::website_auth::description` | Something went wrong connecting to Plex. Please try again. | Det uppstod ett fel vid anslutningen till Plex. Försök igen. | Core-literal match |
| 18495 | 852595209 | `component::plex::config::step::user::menu_options::website_auth` | Link Plex account (recommended) | Koppla ett Plex-konto (rekommenderas) | Core-literal match |
| 18496 | 852595208 | `component::plex::config::step::user::menu_options::manual_setup` | Enter manually | Ange manuellt | Core-literal match |
| 18497 | 852595207 | `component::plex::config::step::select_server::data::server_id` | Server | Server | Core-literal match |
| 18498 | 852485657 | `component::hassio::issues::legacy_homeassistant_folder::title` | Legacy "homeassistant" folder used in partial backup/restore | Föråldrad "homeassistant"-mapp som används vid partiell säkerhetskopiering/återställning | Source-path follow-up open |
| 18499 | 852485656 | `component::hassio::issues::legacy_homeassistant_folder::fix_flow::step::confirm::title` | Legacy "homeassistant" folder used in partial backup/restore | Föråldrad "homeassistant"-mapp som används vid partiell säkerhetskopiering/återställning | Source-path follow-up open |
| 18500 | 852485655 | `component::hassio::issues::legacy_homeassistant_folder::fix_flow::step::confirm::description` | An automation or script called the `hassio.backup_partial` or `hassio.restore_partial` action with `"homeassistant"` listed in `folders`. This is a legacy alias for the `homeassistant: true` option and will stop being accepted in a future release.<br><br>Update the affected automations and scripts to set `homeassistant: true` and remove `"homeassistant"` from the `folders` list. When this is done, select **Submit** to mark this issue as resolved. | En automatisering eller ett skript kallade åtgärden `hassio.backup_partial` eller `hassio.restore_partial` med `"homeassistant"` listad i `folders`. Detta är ett äldre alias för alternativet `homeassistant: true` och kommer inte längre att accepteras i en framtida version. Uppdatera de berörda automatiseringarna och skripten så att `homeassistant: true` anges och `"homeassistant"` tas bort från listan `folders`. När detta är gjort, välj **Bekräfta** för att markera detta problem som löst. | Source-path follow-up open |
| 18501 | 852456270 | `component::ouman_eh_800::entity::sensor::valve_position::name` | Valve position | Ventilposition | Core-literal match |
| 18502 | 852456269 | `component::ouman_eh_800::entity::sensor::supply_water_temperature_setpoint::name` | Supply water temperature setpoint | Börvärde för framledningsvattentemperatur | Core-literal match |
| 18503 | 852456268 | `component::ouman_eh_800::entity::sensor::supply_water_temperature::name` | Supply water temperature | Framledningsvattentemperatur | Core-literal match |
| 18504 | 852456267 | `component::ouman_eh_800::entity::sensor::room_temperature_setpoint::name` | Room temperature setpoint | Börvärde för rumstemperatur | Core-literal match |
| 18505 | 852456266 | `component::ouman_eh_800::entity::sensor::room_temperature::name` | Room temperature | Rumstemperatur | Core-literal match |
| 18506 | 852456265 | `component::ouman_eh_800::entity::sensor::room_sensor_potentiometer::name` | Room sensor potentiometer | Potentiometer för rumsgivare | Core-literal match |
| 18507 | 852456264 | `component::ouman_eh_800::entity::sensor::outside_temperature::name` | Outside temperature | Utetemperatur | Core-literal match |
| 18508 | 852456263 | `component::ouman_eh_800::entity::sensor::fine_adjustment_effect::name` | Fine adjustment effect | Effekten av finjustering | Core-literal match |
| 18509 | 852456262 | `component::ouman_eh_800::entity::sensor::delayed_room_temperature::name` | Delayed room temperature | Fördröjd rumstemperatur | Core-literal match |
| 18510 | 852456261 | `component::ouman_eh_800::entity::sensor::delayed_outdoor_temperature_effect::name` | Delayed outdoor temperature effect | Fördröjd effekt av utomhustemperatur | Core-literal match |
| 18511 | 852456260 | `component::ouman_eh_800::entity::sensor::curve_supply_water_temperature::name` | Curve supply water temperature | Kurva framledningsvattentemperatur | Core-literal match |
| 18512 | 852456259 | `component::ouman_eh_800::device::heating_circuit_with_name::name` | Heating circuit {circuit_number} {circuit_name} | Värmekrets {circuit_number} {circuit_name} | Core-literal match |
| 18513 | 852456258 | `component::ouman_eh_800::device::heating_circuit::name` | Heating circuit {circuit_number} | Värmekrets {circuit_number} | Core-literal match |
| 18514 | 852456257 | `component::ouman_eh_800::config::step::user::data_description::username` | Username for the Ouman EH-800 web interface | Användarnamn för Ouman EH-800:s webbgränssnitt | Core-literal match |
| 18515 | 852456256 | `component::ouman_eh_800::config::step::user::data_description::url` | The URL of the Ouman EH-800 web interface | URL till Ouman EH-800:s webbgränssnitt | Core-literal match |
| 18516 | 852456255 | `component::ouman_eh_800::config::step::user::data_description::password` | Password for the Ouman EH-800 web interface | Lösenord för Ouman EH-800 webbgränssnitt | Core-literal match |
| 18517 | 852456254 | `component::ouman_eh_800::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 18518 | 852456253 | `component::ouman_eh_800::config::step::user::data::url` | URL | URL | Shared reference target checked |
| 18519 | 852456252 | `component::ouman_eh_800::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 18520 | 852456251 | `component::ouman_eh_800::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 18521 | 852456250 | `component::ouman_eh_800::config::error::invalid_url` | Invalid URL | Ogiltig URL | Core-literal match |
| 18522 | 852456249 | `component::ouman_eh_800::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 18523 | 852456248 | `component::ouman_eh_800::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18524 | 852456247 | `component::ouman_eh_800::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 18525 | 852099747 | `component::nest::services::set_fan_timer::name` | Set fan timer | Ställ in fläkttimer | Core-literal match |
| 18526 | 852099746 | `component::nest::services::set_fan_timer::fields::duration::name` | Duration | Varaktighet | Core-literal match |
| 18527 | 852099745 | `component::nest::services::set_fan_timer::fields::duration::description` | The duration the fan should run for. | Den tid som fläkten ska vara igång. | Core-literal match |
| 18528 | 852099744 | `component::nest::services::set_fan_timer::description` | Sets the fan to run for a specific duration. | Ställer in fläkten så att den går under en viss tid. | Core-literal match |
| 18529 | 851927246 | `component::xthings_cloud::config::step::user::title` | Xthings Cloud Login | Xthings Cloud-inloggning | Core-literal match |
| 18530 | 851927245 | `component::xthings_cloud::config::step::user::description` | Please enter your Xthings Cloud account credentials. | Ange inloggningsuppgifterna för ditt Xthings Cloud-konto. | Core-literal match |
| 18531 | 851927244 | `component::xthings_cloud::config::step::user::data_description::password` | Your Xthings Cloud account password. | Lösenordet till ditt Xthings Cloud-konto. | Core-literal match |
| 18532 | 851927243 | `component::xthings_cloud::config::step::user::data_description::email` | The email address used to register your Xthings Cloud account. | Den e-postadress som användes vid registreringen av ditt Xthings Cloud-konto. | Core-literal match |
| 18533 | 851927242 | `component::xthings_cloud::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 18534 | 851927241 | `component::xthings_cloud::config::step::user::data::email` | Email | E-post | Shared reference target checked |
| 18535 | 851927240 | `component::xthings_cloud::config::error::user_not_logged_in` | Session expired, please log in again. | Sessionen har gått ut, vänligen logga in igen. | Core-literal match |
| 18536 | 851927239 | `component::xthings_cloud::config::error::user_not_activated` | This account has not been activated. | Det här kontot har inte aktiverats. | Core-literal match |
| 18537 | 851927238 | `component::xthings_cloud::config::error::user_disabled` | This account has been disabled. | Det här kontot har inaktiverats. | Core-literal match |
| 18538 | 851927237 | `component::xthings_cloud::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 18539 | 851927236 | `component::xthings_cloud::config::error::token_invalid` | Invalid token, please log in again. | Ogiltig token, vänligen logga in igen. | Core-literal match |
| 18540 | 851927235 | `component::xthings_cloud::config::error::token_expired` | Token expired, please log in again. | Token har gått ut, vänligen logga in igen. | Core-literal match |
| 18541 | 851927234 | `component::xthings_cloud::config::error::password_wrong` | Incorrect password. | Felaktigt lösenord. | Core-literal match |
| 18542 | 851927233 | `component::xthings_cloud::config::error::password_empty` | Password cannot be empty. | Lösenordet får inte vara tomt. | Core-literal match |
| 18543 | 851927232 | `component::xthings_cloud::config::error::email_not_found` | Email does not exist. | E-postadressen finns inte. | Core-literal match |
| 18544 | 851927231 | `component::xthings_cloud::config::error::email_invalid` | Invalid email format. | Ogiltigt e-postformat. | Core-literal match |
| 18545 | 851927230 | `component::xthings_cloud::config::error::email_empty` | Email cannot be empty. | E-mail får inte vara tom. | Core-literal match |
| 18546 | 851927229 | `component::xthings_cloud::config::error::device_offline` | Device is offline. | Enhet är offline. | Core-literal match |
| 18547 | 851927228 | `component::xthings_cloud::config::error::device_not_found` | Device not found. | Enhet hittades inte. | Core-literal match |
| 18548 | 851927227 | `component::xthings_cloud::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18549 | 851927226 | `component::xthings_cloud::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 18550 | 851911672 | `component::mqtt::options::step::options::data_description::discovery_qos` | The quality of service for discovery subscriptions to your MQTT broker. | Kvaliteten på tjänsten för discovery-prenumerationer till din MQTT-broker. | Core-literal match |
| 18551 | 851911671 | `component::mqtt::options::step::options::data::discovery_qos` | Discovery QoS | QoS för upptäckt | Core-literal match |
| 18552 | 851887747 | `component::tuya::entity::sensor::outside_temperature::name` | Outside temperature | Utetemperatur | Core-literal match |
| 18553 | 851887746 | `component::tuya::entity::sensor::heat_exchanger_temperature::name` | Heat exchanger temperature | Värmeväxlartemperatur | Core-literal match |
| 18554 | 851887745 | `component::tuya::entity::sensor::flow_temperature::name` | Flow temperature | Flödestemperatur | Core-literal match |
| 18555 | 851887744 | `component::tuya::entity::sensor::compressor_strength::name` | Compressor strength | Kompressorstyrka | Core-literal match |
| 18556 | 851887743 | `component::tuya::entity::sensor::coil_temperature::name` | Coil temperature | Spoltemperatur | Core-literal match |
| 18557 | 851849339 | `component::tuya::entity::binary_sensor::temp_error::name` | Temperature error | Temperaturfel | Core-literal match |
| 18558 | 851849338 | `component::tuya::entity::binary_sensor::motor_fault::name` | Motor fault | Motorfel | Core-literal match |
| 18559 | 851849337 | `component::tuya::entity::binary_sensor::low_temp::name` | Low temperature | Låg temperatur | Core-literal match |
| 18560 | 851849336 | `component::tuya::entity::binary_sensor::low_humidity::name` | Low humidity | Låg luftfuktighet | Core-literal match |
| 18561 | 851849335 | `component::tuya::entity::binary_sensor::high_temp::name` | High temperature | Hög temperatur | Core-literal match |
| 18562 | 851849334 | `component::tuya::entity::binary_sensor::filter_cleaning::name` | Filter cleaning | Filterrengöring | Core-literal match |
| 18563 | 851849333 | `component::tuya::entity::binary_sensor::coil_freeze::name` | Coil freeze/defrost | Spole frysning/avfrostning | Core-literal match |
| 18564 | 851095130 | `component::vicare::entity::sensor::target_temperature::name` | Target temperature | Måltemperatur | Core-literal match |
| 18565 | 851094765 | `component::watts::services::activate_timer_mode::name` | Activate timer mode | Aktivera timerläge | Core-literal match |
| 18566 | 851094764 | `component::watts::services::activate_timer_mode::fields::temperature::name` | Temperature | Temperatur | Core-literal match |
| 18567 | 851094763 | `component::watts::services::activate_timer_mode::fields::temperature::description` | Target temperature while the timer is active. | Måltemperatur medan timern är aktiv. | Core-literal match |
| 18568 | 851094762 | `component::watts::services::activate_timer_mode::fields::duration::name` | Duration | Varaktighet | Core-literal match |
| 18569 | 851094761 | `component::watts::services::activate_timer_mode::fields::duration::description` | Duration of the timer. | Timerns varaktighet. | Core-literal match |
| 18570 | 851094760 | `component::watts::services::activate_timer_mode::description` | Activates timer mode on the thermostat for a specified temperature and duration. | Aktiverar timerläge på termostaten för en angiven temperatur och varaktighet. | Core-literal match |
| 18571 | 851094759 | `component::watts::exceptions::timer_temperature_out_of_range::message` | Timer temperature {temperature} is out of range ({min_temp}-{max_temp}) | Timertemperaturen {temperature} ligger utanför intervallet ({min_temp}-{max_temp}) | Core-literal match |
| 18572 | 851094758 | `component::watts::exceptions::activate_timer_mode_error::message` | An error occurred while activating timer mode | Ett fel inträffade när timerläget aktiverades | Core-literal match |
| 18573 | 851052398 | `component::avea::issues::deprecated_yaml_import_issue_no_bulbs::title` | Avea YAML configuration import failed | Import av Avea YAML-konfiguration misslyckades | Source-path follow-up open |
| 18574 | 851052397 | `component::avea::issues::deprecated_yaml_import_issue_no_bulbs::description` | Configuring {integration_title} using YAML is deprecated and will be removed in a future release. While importing your YAML configuration, Home Assistant could not discover any Avea bulbs. Make sure the bulbs are powered on, nearby, and reachable over Bluetooth, then restart Home Assistant. If you no longer use the YAML configuration, remove the `{domain}` entry from your `configuration.yaml` file. | Konfigurering av {integration_title} med hjälp av YAML är föråldrad och kommer att tas bort i en framtida version. När du importerade din YAML-konfiguration kunde Home Assistant inte upptäcka några Avea-lampor. Kontrollera att lamporna är påslagna, i närheten och nåbara via Bluetooth och starta sedan om Home Assistant. Om du inte längre använder YAML-konfigurationen, ta bort posten `{domain}` från din `configuration.yaml`-fil. | Source-path follow-up open |
| 18575 | 851052396 | `component::avea::issues::deprecated_yaml::title` | The {integration_title} YAML configuration is being removed | YAML-konfigurationen för {integration_title} tas bort | Source-path follow-up open |
| 18576 | 851052395 | `component::avea::issues::deprecated_yaml::description` | Configuring {integration_title} using YAML is being removed.<br><br>Your existing YAML configuration has been imported into the UI automatically.<br><br>Remove the `{domain}` configuration from your configuration.yaml file and restart Home Assistant to fix this issue. | Konfigurering av {integration_title} med hjälp av YAML tas bort.<br><br>Din befintliga YAML-konfiguration har importerats automatiskt till användargränssnittet.<br><br>Ta bort konfigurationen `{domain}` från filen configuration.yaml och starta om Home Assistant för att åtgärda problemet. | Source-path follow-up open |
| 18577 | 851052394 | `component::avea::config::step::user::description` | Choose a device to set up | Välj en enhet att konfigurera | Shared reference target checked |
| 18578 | 851052393 | `component::avea::config::step::user::data::address` | Device | Enhet | Shared reference target checked |
| 18579 | 851052392 | `component::avea::config::step::bluetooth_confirm::description` | Do you want to set up {name}? | Vill du konfigurera {name}? | Shared reference target checked |
| 18580 | 851052391 | `component::avea::config::flow_title` | {name} | {name} | Core-literal match |
| 18581 | 851052390 | `component::avea::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 18582 | 851052389 | `component::avea::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18583 | 851052388 | `component::avea::config::abort::no_devices_found` | No devices found on the network | Inga enheter hittades i nätverket | Shared reference target checked |
| 18584 | 851052387 | `component::avea::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 18585 | 851052386 | `component::avea::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 18586 | 851006539 | `component::eurotronic_cometblue::entity::number::offset::name` | Setpoint offset | Börvärdesförskjutning | Core-literal match |
| 18587 | 851006538 | `component::eurotronic_cometblue::entity::number::eco_setpoint::name` | Eco setpoint | Eco-börvärde | Core-literal match |
| 18588 | 851006537 | `component::eurotronic_cometblue::entity::number::comfort_setpoint::name` | Comfort setpoint | Komfortbörvärde | Core-literal match |
| 18589 | 850933831 | `component::kiosker::entity::switch::disable_screensaver::name` | Disable screensaver | Inaktivera skärmsläckare | Core-literal match |
| 18590 | 850933585 | `component::indevolt::exceptions::write_error::message` | Cannot update value for {name} | Det går inte att uppdatera värdet för {name} | Core-literal match |
| 18591 | 850775882 | `component::tuya::entity::number::irrigation_duration::name` | Irrigation duration | Bevattningslängd | Core-literal match |
| 18592 | 850742318 | `component::airnow::options::step::init::data_description::radius` | The radius in miles around your location to search for reporting stations. | Radien i engelska mil runt din plats för att söka efter rapporteringsstationer. | Source-path follow-up open |
| 18593 | 850741828 | `component::watts::exceptions::set_preset_mode_error::message` | An error occurred while setting the preset mode | Ett fel inträffade vid inställning av förinställt läge | Core-literal match |
| 18594 | 850741827 | `component::watts::entity::climate::thermostat::state_attributes::preset_mode::state::timer` | Timer | Timer | Core-literal match |
| 18595 | 850741826 | `component::watts::entity::climate::thermostat::state_attributes::preset_mode::state::defrost` | Defrost | Avfrostning | Core-literal match |
| 18596 | 850740765 | `component::centriconnect::entity::sensor::tank_size::name` | Tank size | Tankstorlek | Core-literal match |
| 18597 | 850740764 | `component::centriconnect::entity::sensor::tank_remaining_volume::name` | Tank remaining volume | Återstående tankvolym | Core-literal match |
| 18598 | 850740763 | `component::centriconnect::entity::sensor::tank_level::name` | Tank level | Tanknivå | Core-literal match |
| 18599 | 850740762 | `component::centriconnect::entity::sensor::solar_voltage::name` | Solar voltage | Solspänning | Core-literal match |
| 18600 | 850740761 | `component::centriconnect::entity::sensor::solar_level::name` | Solar level | Solnivå | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 852485657 | `component::hassio::issues::legacy_homeassistant_folder::title` | Legacy "homeassistant" folder used in partial backup/restore |
| 852485656 | `component::hassio::issues::legacy_homeassistant_folder::fix_flow::step::confirm::title` | Legacy "homeassistant" folder used in partial backup/restore |
| 852485655 | `component::hassio::issues::legacy_homeassistant_folder::fix_flow::step::confirm::description` | An automation or script called the `hassio.backup_partial` or `hassio.restore_partial` action with `"homeassistant"` listed in `folders`. This is a legacy alias for the `homeassistant: true` option and will stop being accepted in a future release.

Update the affected automations and scripts to set `homeassistant: true` and remove `"homeassistant"` from the `folders` list. When this is done, select **Submit** to mark this issue as resolved. |
| 851052398 | `component::avea::issues::deprecated_yaml_import_issue_no_bulbs::title` | Avea YAML configuration import failed |
| 851052397 | `component::avea::issues::deprecated_yaml_import_issue_no_bulbs::description` | Configuring {integration_title} using YAML is deprecated and will be removed in a future release. While importing your YAML configuration, Home Assistant could not discover any Avea bulbs. Make sure the bulbs are powered on, nearby, and reachable over Bluetooth, then restart Home Assistant. If you no longer use the YAML configuration, remove the `{domain}` entry from your `configuration.yaml` file. |
| 851052396 | `component::avea::issues::deprecated_yaml::title` | The {integration_title} YAML configuration is being removed |
| 851052395 | `component::avea::issues::deprecated_yaml::description` | Configuring {integration_title} using YAML is being removed.

Your existing YAML configuration has been imported into the UI automatically.

Remove the `{domain}` configuration from your configuration.yaml file and restart Home Assistant to fix this issue. |
| 851052387 | `component::avea::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |
| 850742318 | `component::airnow::options::step::init::data_description::radius` | The radius in miles around your location to search for reporting stations. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
