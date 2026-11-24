# Home Assistant Core – historisk avstämning 16441–16560

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 85 direkta källtexter matchar HA Core-källan; 31 referensanvändningar med 24 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 4 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 16441 | 874647735 | `component::tractive::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 16442 | 874647734 | `component::tractive::config::step::reauth_confirm::data::email` | Email | E-post | Shared reference target checked |
| 16443 | 874616336 | `component::iskra::config::step::user::data::protocol` | Protocol | Protokoll | Core-literal match |
| 16444 | 874615979 | `component::modem_callerid::config::step::user::data::device` | Device | Enhet | Shared reference target checked |
| 16445 | 874615857 | `component::sia::config::step::add_account::title` | Add another account to the current port | Lägg till ytterligare ett konto till den aktuella porten | Core-literal match |
| 16446 | 874615856 | `component::sia::config::step::add_account::data::zones` | Number of zones for the account | Antal zoner för kontot | Shared reference target checked |
| 16447 | 874615855 | `component::sia::config::step::add_account::data::ping_interval` | Ping interval (min) | Pingintervall (min) | Shared reference target checked |
| 16448 | 874615854 | `component::sia::config::step::add_account::data::encryption_key` | Encryption key | Krypteringsnyckel | Shared reference target checked |
| 16449 | 874615853 | `component::sia::config::step::add_account::data::additional_account` | Additional accounts | Ytterligare konton | Shared reference target checked |
| 16450 | 874615852 | `component::sia::config::step::add_account::data::account` | Account ID | Konto-ID | Shared reference target checked |
| 16451 | 874615851 | `component::airvisual::config::step::user::data::type` | Integration type | Integrationstyp | Core-literal match |
| 16452 | 874615448 | `component::local_calendar::config::step::import_ics_file::description` | You can import events in iCal format (.ics file). | Du kan importera händelser i iCal-format (.ics-fil). | Core-literal match |
| 16453 | 874615447 | `component::local_calendar::config::step::import_ics_file::data::ics_file` | ICS file | ICS-fil | Core-literal match |
| 16454 | 874615378 | `component::honeywell::config::step::reauth_confirm::data::username` | Username | Användarnamn | Shared reference target checked |
| 16455 | 874615297 | `component::hlk_sw16::config::step::user::data::port` | Port | Port | Shared reference target checked |
| 16456 | 874615228 | `component::here_travel_time::config::step::origin_entity::title` | Choose origin | Välj startpunkt | Shared reference target checked |
| 16457 | 874615227 | `component::here_travel_time::config::step::origin_entity::data::origin_entity_id` | Origin using an entity | Utgångspunkt från en entitet | Core-literal match |
| 16458 | 874615226 | `component::here_travel_time::config::step::destination_entity::title` | Choose destination | Välj destination | Shared reference target checked |
| 16459 | 874615225 | `component::here_travel_time::config::step::destination_entity::data::destination_entity_id` | Destination using an entity | Destination från en entitet | Core-literal match |
| 16460 | 874283458 | `component::unifi_access::config::flow_title` | {name} ({ip_address}) | {name} ({ip_address}) | Core-literal match |
| 16461 | 874137744 | `component::aquacell::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 16462 | 874137743 | `component::aquacell::config::step::reauth_confirm::description` | The password for {email} is no longer valid. Enter your current softener mobile app password to reconnect. | Lösenordet för {email} är inte längre giltigt. Ange ditt nuvarande lösenord för mobilappen för att ansluta igen. | Core-literal match |
| 16463 | 874137742 | `component::aquacell::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 16464 | 874137741 | `component::aquacell::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 16465 | 874135969 | `component::mitsubishi_comfort::exceptions::set_temperature_failed::message` | {device_name} did not accept the requested temperature | {device_name} accepterade inte den begärda temperaturen | Core-literal match |
| 16466 | 874135968 | `component::mitsubishi_comfort::exceptions::set_swing_mode_failed::message` | {device_name} did not accept the requested swing mode | {device_name} accepterade inte det begärda svingläget | Core-literal match |
| 16467 | 874135967 | `component::mitsubishi_comfort::exceptions::set_hvac_mode_failed::message` | {device_name} did not accept the requested HVAC mode | {device_name} accepterade inte det begärda HVAC-läget | Core-literal match |
| 16468 | 874135966 | `component::mitsubishi_comfort::exceptions::set_fan_mode_failed::message` | {device_name} did not accept the requested fan mode | {device_name} accepterade inte det begärda fläktläget | Core-literal match |
| 16469 | 874135878 | `component::fluss::config::step::reauth_confirm::description` | The Fluss+ API key is no longer valid. Get your API key from the profile page of the Fluss+ app, or generate a new one, and enter it below. | Fluss+ API-nyckeln är inte längre giltig. Hämta din API-nyckel från profilsidan i Fluss+-appen, eller generera en ny, och ange den här. | Core-literal match |
| 16470 | 874135877 | `component::fluss::config::step::reauth_confirm::data_description::api_key` | The API key found in the profile page of the Fluss+ app. | API-nyckeln som finns på profilsidan i appen Fluss+. | Core-literal match |
| 16471 | 874135876 | `component::fluss::config::step::reauth_confirm::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 16472 | 874135875 | `component::fluss::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 16473 | 874135156 | `component::data_grand_lyon::config_subentries::velov_station::step::user::data_description::station_id` | Search by station name, address or city, or enter a station ID directly. | Sök efter stationsnamn, adress eller stad, eller ange ett stations-ID direkt. | Core-literal match |
| 16474 | 874135155 | `component::data_grand_lyon::config_subentries::velov_station::error::invalid_station_id` | Station ID must be a number. | Stations-ID måste vara ett nummer. | Core-literal match |
| 16475 | 874135154 | `component::data_grand_lyon::config_subentries::velov_station::abort::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 16476 | 874135153 | `component::data_grand_lyon::config_subentries::velov_station::abort::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 16477 | 874135152 | `component::data_grand_lyon::config_subentries::velov_station::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16478 | 874134663 | `component::green_planet_energy::services::get_cheapest_duration::name` | Get cheapest time window | Hitta det billigaste tidsfönstret | Core-literal match |
| 16479 | 874134662 | `component::green_planet_energy::services::get_cheapest_duration::fields::time_range::name` | Time range | Tidsintervall | Core-literal match |
| 16480 | 874134661 | `component::green_planet_energy::services::get_cheapest_duration::fields::time_range::description` | Time range to search within. | Tidsintervall att söka inom. | Core-literal match |
| 16481 | 874134660 | `component::green_planet_energy::services::get_cheapest_duration::fields::duration::name` | Duration | Varaktighet | Core-literal match |
| 16482 | 874134659 | `component::green_planet_energy::services::get_cheapest_duration::fields::duration::description` | Duration in hours for which to find the cheapest time window. | Tidsperiod i timmar för vilken det billigaste tidsfönstret ska hittas. | Core-literal match |
| 16483 | 874134658 | `component::green_planet_energy::services::get_cheapest_duration::description` | Retrieves electricity price data and finds the cheapest consecutive time window for a given duration. | Hämtar elprisdata och hittar det billigaste tidsfönstret i följd för en given period. | Core-literal match |
| 16484 | 874134657 | `component::green_planet_energy::exceptions::no_data_available::message` | No price data available for the requested duration and time range | Det finns inga prisuppgifter tillgängliga för den begärda tidsperioden och det angivna tidsintervallet | Core-literal match |
| 16485 | 874134656 | `component::green_planet_energy::exceptions::no_config_entry::message` | No matching integration instance was found | Ingen matchande integrationsinstans hittades | Core-literal match |
| 16486 | 874134655 | `component::green_planet_energy::exceptions::config_entry_not_loaded::message` | This integration instance is not currently loaded | Denna integrationsinstans är för närvarande inte laddad | Core-literal match |
| 16487 | 874134617 | `component::lutron_caseta::device_automation::trigger_type::multi_tap` | "{subtype}" multi-tapped | "{subtype}" – multitryck | Core-literal match |
| 16488 | 874134616 | `component::lutron_caseta::device_automation::trigger_type::long_press` | "{subtype}" long pressed | "{subtype}" – långt tryck | Core-literal match |
| 16489 | 873836288 | `component::smtp::exceptions::send_mail_connection_error::message` | Failed to send email message due to a connection error. | Det gick inte att skicka e-postmeddelandet på grund av ett anslutningsfel. | Core-literal match |
| 16490 | 873836287 | `component::smtp::exceptions::connection_error::message` | Failed to connect to SMTP server. | Det gick inte att ansluta till SMTP-servern. | Core-literal match |
| 16491 | 873836286 | `component::smtp::exceptions::authentication_error::message` | Failed to authenticate with SMTP server. Please verify your credentials. | Det gick inte att autentisera sig hos SMTP-servern. Kontrollera dina inloggningsuppgifter. | Core-literal match |
| 16492 | 873826406 | `component::overkiz::entity::water_heater::overkiz::state::performance` | Boost | Boost | Core-literal match |
| 16493 | 873826405 | `component::overkiz::entity::water_heater::overkiz::state::manual` | Manual | Manuell | Shared reference target checked |
| 16494 | 873826404 | `component::overkiz::entity::water_heater::overkiz::state::auto` | Auto | Auto | Shared reference target checked |
| 16495 | 873825942 | `component::blebox::config::step::confirm_discovery::title` | BleBox device discovered | BleBox-enhet upptäckt | Core-literal match |
| 16496 | 873825941 | `component::blebox::config::step::confirm_discovery::description` | Do you want to add the BleBox device **{name}** at `{host}` to Home Assistant? | Vill du lägga till BleBox-enheten **{name}** på `{host}` i Home Assistant? | Core-literal match |
| 16497 | 873825940 | `component::blebox::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16498 | 873819713 | `component::icloud::exceptions::unsupported_media_type::message` | Unsupported media type | Medietyp stöds inte | Core-literal match |
| 16499 | 873819712 | `component::icloud::exceptions::unknown_media_item::message` | Unknown media item | Okänt medieobjekt | Core-literal match |
| 16500 | 873819711 | `component::icloud::exceptions::photo_not_found::message` | Photo not found | Foto hittades inte | Core-literal match |
| 16501 | 873819710 | `component::icloud::exceptions::invalid_view_type::message` | Invalid album view type | Ogiltig albumvisningstyp | Core-literal match |
| 16502 | 873819709 | `component::icloud::exceptions::invalid_media_source::message` | Invalid media source | Ogiltig mediekälla | Core-literal match |
| 16503 | 873819708 | `component::icloud::exceptions::incomplete_media_source_identifier::message` | Incomplete media source identifier | Ofullständig identifierare för mediekälla | Core-literal match |
| 16504 | 873819707 | `component::icloud::exceptions::config_entry_not_loaded::message` | Config entry not loaded | Konfigurationsposten laddades inte | Core-literal match |
| 16505 | 873819706 | `component::icloud::exceptions::config_entry_not_found::message` | Config entry not found for account: {entry} | Konfigurationsposten hittades inte för konto: {entry} | Core-literal match |
| 16506 | 873819705 | `component::icloud::exceptions::album_type_not_specified::message` | Album type not specified | Albumtyp har inte specificerats | Core-literal match |
| 16507 | 873819704 | `component::icloud::exceptions::album_not_found::message` | Album not found | Album hittades inte | Core-literal match |
| 16508 | 873819703 | `component::icloud::exceptions::account_not_initialized::message` | Account not initialized: {entry} | Kontot har inte initialiserats: {entry} | Core-literal match |
| 16509 | 873818473 | `component::unifi_direct::issues::yaml_import_cannot_connect::title` | YAML configuration import failed: cannot connect | Importen av YAML-konfigurationen misslyckades: det går inte att ansluta | Core-literal match |
| 16510 | 873818472 | `component::unifi_direct::issues::yaml_import_cannot_connect::description` | The YAML configuration for UniFi AP at `{host}` could not be imported because the connection failed.<br><br>Please check that `{host}` is reachable, update your `configuration.yaml` if needed, and restart Home Assistant. | YAML-konfigurationen för UniFi AP på `{host}` kunde inte importeras eftersom anslutningen misslyckades.<br><br>Kontrollera att `{host}` går att nå, uppdatera `configuration.yaml` vid behov och starta om Home Assistant. | Core-literal match |
| 16511 | 873818471 | `component::unifi_direct::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 16512 | 873818470 | `component::unifi_direct::config::step::user::data::port` | Port | Port | Shared reference target checked |
| 16513 | 873818469 | `component::unifi_direct::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 16514 | 873818468 | `component::unifi_direct::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 16515 | 873818467 | `component::unifi_direct::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16516 | 873818466 | `component::unifi_direct::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 16517 | 873807135 | `component::greencell::entity::sensor::voltage_l3::name` | Voltage phase L3 | Spänning, fas L3 | Core-literal match |
| 16518 | 873807134 | `component::greencell::entity::sensor::voltage_l2::name` | Voltage phase L2 | Spänning, fas L2 | Core-literal match |
| 16519 | 873807133 | `component::greencell::entity::sensor::voltage_l1::name` | Voltage phase L1 | Spänning, fas L1 | Core-literal match |
| 16520 | 873807132 | `component::greencell::entity::sensor::status::state::waiting_for_car` | Waiting for car | Väntar på bil | Core-literal match |
| 16521 | 873807131 | `component::greencell::entity::sensor::status::state::idle` | Idle | Inaktiv | Shared reference target checked |
| 16522 | 873807130 | `component::greencell::entity::sensor::status::state::finished` | Finished | Färdig | Core-literal match |
| 16523 | 873807129 | `component::greencell::entity::sensor::status::state::error_evse` | EVSE error | EVSE-fel | Core-literal match |
| 16524 | 873807128 | `component::greencell::entity::sensor::status::state::error_car` | Car error | Bilfel | Core-literal match |
| 16525 | 873807127 | `component::greencell::entity::sensor::status::state::connected` | Connected | Ansluten | Shared reference target checked |
| 16526 | 873807126 | `component::greencell::entity::sensor::status::state::charging` | Charging | Laddar | Shared reference target checked |
| 16527 | 873807125 | `component::greencell::entity::sensor::status::name` | Status | Status | Core-literal match |
| 16528 | 873807124 | `component::greencell::entity::sensor::power::name` | Power | På/Av | Source-path follow-up open |
| 16529 | 873807123 | `component::greencell::entity::sensor::current_l3::name` | Current phase L3 | Ström, fas L3 | Core-literal match |
| 16530 | 873807122 | `component::greencell::entity::sensor::current_l2::name` | Current phase L2 | Ström, fas L2 | Core-literal match |
| 16531 | 873807121 | `component::greencell::entity::sensor::current_l1::name` | Current phase L1 | Ström, fas L1 | Core-literal match |
| 16532 | 873807120 | `component::greencell::config::step::user::title` | Set up your Greencell HabuDen EVSE | Konfigurera din Greencell HabuDen EVSE | Core-literal match |
| 16533 | 873807119 | `component::greencell::config::step::user::description` | The integration will try to discover your EVSE devices over MQTT. | Integrationen kommer att försöka upptäcka dina EVSE-enheter via MQTT. | Core-literal match |
| 16534 | 873807118 | `component::greencell::config::step::select::title` | Select your device | Välj din enhet | Core-literal match |
| 16535 | 873807117 | `component::greencell::config::step::select::description` | Multiple Greencell devices were found (total: {count}). Please choose which one you want to configure. | Flera Greencell-enheter hittades (totalt: {count}). Välj vilken du vill konfigurera. | Core-literal match |
| 16536 | 873807116 | `component::greencell::config::step::select::data_description::serial_number` | Select the device you want to add to Home Assistant | Välj den enhet som du vill lägga till i Home Assistant | Core-literal match |
| 16537 | 873807115 | `component::greencell::config::step::select::data::serial_number` | Device serial number | Enhetens serienummer | Core-literal match |
| 16538 | 873807114 | `component::greencell::config::step::confirm::title` | Greencell device discovered | Greencell-enhet upptäckt | Core-literal match |
| 16539 | 873807113 | `component::greencell::config::step::confirm::description` | A Greencell device with serial number {serial} was discovered. Do you want to add it? | En Greencell-enhet med serienummer {serial} har hittats. Vill du lägga till den? | Core-literal match |
| 16540 | 873807112 | `component::greencell::config::abort::no_discovery_data` | No discovery data received. Ensure the device is online and broadcasting. | Inga upptäcktsdata har mottagits. Kontrollera att enheten är uppkopplad och sänder. | Core-literal match |
| 16541 | 873807111 | `component::greencell::config::abort::mqtt_subscription_failed` | Failed to subscribe to the MQTT topic for discovery. | Det gick inte att prenumerera på MQTT-ämnet för upptäckt. | Core-literal match |
| 16542 | 873807110 | `component::greencell::config::abort::mqtt_not_connected` | MQTT is not connected. Ensure the MQTT broker is running and configured. | MQTT är inte anslutet. Se till att MQTT-brokern körs och är konfigurerad. | Core-literal match |
| 16543 | 873807109 | `component::greencell::config::abort::mqtt_not_configured` | MQTT is not configured. Please configure MQTT first. | MQTT är inte konfigurerat. Konfigurera MQTT först. | Core-literal match |
| 16544 | 873807108 | `component::greencell::config::abort::invalid_discovery_data` | The received discovery data is invalid. | De mottagna upptäcktsuppgifterna är ogiltiga. | Core-literal match |
| 16545 | 873807107 | `component::greencell::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 16546 | 873807106 | `component::greencell::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 16547 | 873800410 | `component::yoto::entity::binary_sensor::headphones::name` | Headphones | Hörlurar | Core-literal match |
| 16548 | 873800409 | `component::yoto::entity::binary_sensor::bluetooth_audio::name` | Bluetooth audio | Bluetooth-ljud | Core-literal match |
| 16549 | 873793430 | `component::broadlink::exceptions::connect_failed::message` | Failed to connect to the device at {host}: {error} | Det gick inte att ansluta till enheten på {host}: {error} | Core-literal match |
| 16550 | 873788008 | `component::msteams::issues::integration_removed::title` | Microsoft Teams integration has been removed | Microsoft Teams-integrationen har tagits bort | Core-literal match |
| 16551 | 873788007 | `component::msteams::issues::integration_removed::description` | The Microsoft Teams integration has been removed from Home Assistant.<br><br>The [Office 365 Connectors]({url}) used by this integration to send messages to Microsoft Teams have been discontinued by Microsoft and are no longer supported.<br><br>To resolve this issue, remove the Microsoft Teams integration configuration from your `configuration.yaml` file and restart Home Assistant.<br><br>Once the configuration has been removed and Home Assistant has restarted, this issue will no longer be shown. | Microsoft Teams-integrationen har tagits bort från Home Assistant.<br><br>De [Office 365-anslutningar]({url}) som denna integration använde för att skicka meddelanden till Microsoft Teams har avvecklats av Microsoft och stöds inte längre.<br><br>För att lösa problemet tar du bort konfigurationen för Microsoft Teams-integrationen från din `configuration.yaml`-fil och starta om Home Assistant.<br><br>När konfigurationen har tagits bort och Home Assistant har startats om kommer detta problem inte längre att visas. | Core-literal match |
| 16552 | 873786805 | `component::yoto::entity::sensor::day_mode::state::night` | Night | Natt | Core-literal match |
| 16553 | 873786804 | `component::yoto::entity::sensor::day_mode::state::day` | Day | Dag | Core-literal match |
| 16554 | 873786803 | `component::yoto::entity::sensor::day_mode::name` | Day mode | Dagläge | Core-literal match |
| 16555 | 873786802 | `component::yoto::entity::sensor::card_insertion_state::state::streaming` | Streaming | Streaming | Core-literal match |
| 16556 | 873786801 | `component::yoto::entity::sensor::card_insertion_state::state::remote` | Remote | Fjärr | Core-literal match |
| 16557 | 873786800 | `component::yoto::entity::sensor::card_insertion_state::state::physical` | Physical card | Fysiskt kort | Core-literal match |
| 16558 | 873786799 | `component::yoto::entity::sensor::card_insertion_state::state::none` | None | Ingen | Core-literal match |
| 16559 | 873786798 | `component::yoto::entity::sensor::card_insertion_state::name` | Content source | Innehållskälla | Core-literal match |
| 16560 | 873763488 | `component::verisure::config::error::mfa_rate_limited` | Too many login attempts. Wait before trying again. | För många inloggningsförsök. Vänta innan du försöker igen. | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 874137741 | `component::aquacell::config::abort::reauth_successful` | Re-authentication was successful |
| 874135875 | `component::fluss::config::abort::reauth_successful` | Re-authentication was successful |
| 873807124 | `component::greencell::entity::sensor::power::name` | Power |
| 873807107 | `component::greencell::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
