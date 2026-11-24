# Home Assistant Core – historisk avstämning 19321–19440

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120 nycklar avstämda: 119 översättningsbara och 1 strukturposter utan engelsk källtext. 92 direkta källtexter matchar HA Core-källan; 21 referensanvändningar med 18 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 6 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Inga äldre radvisa språkförslag för dessa 120 nycklar.
- 119 översättningsbara poster synkades retroaktivt till HA Core TM. En nyckel har tom engelsk källtext och motsvarar `data: {}` i källan; de är dokumenterade som strukturposter och har inte lagts i TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 19321 | 840176292 | `component::wled::entity::switch::freeze::name` | Freeze | Frys | Core-literal match |
| 19322 | 840149489 | `component::shelly::entity::binary_sensor::tilt::name` | Tilt | Lutning | Core-literal match |
| 19323 | 840149488 | `component::shelly::entity::binary_sensor::rotation::name` | Rotation | Rotation | Core-literal match |
| 19324 | 839958684 | `component::victron_gx::config::step::reconfigure::data_description::username` | Username for the MQTT server, default is empty. Not needed by Victron devices. This is only needed if you route your MQTT messages through a non-Victron server and it does require a username. | Användarnamn för MQTT-servern, standardvärdet är tomt. Behövs inte för Victron-enheter. Detta behövs bara om du dirigerar dina MQTT-meddelanden via en server som inte är från Victron och som kräver ett användarnamn. | Shared reference target checked |
| 19325 | 839958683 | `component::victron_gx::config::step::reconfigure::data_description::ssl` | Indicates whether to use SSL to connect to the Victron device. Normally it is disabled. | Anger om SSL ska användas för att ansluta till Victron-enheten. Normalt är det inaktiverat. | Shared reference target checked |
| 19326 | 839958682 | `component::victron_gx::config::step::reconfigure::data_description::port` | The MQTT port on the host. Normally it is 1883. | MQTT-porten på värden. Normalt är den 1883. | Shared reference target checked |
| 19327 | 839958681 | `component::victron_gx::config::step::reconfigure::data_description::password` | Password for the Victron device, default is empty. This is not your VRM password. | Lösenord för Victron-enheten, standardinställningen är tom. Detta är inte ditt VRM-lösenord. | Shared reference target checked |
| 19328 | 839958680 | `component::victron_gx::config::step::reconfigure::data_description::host` | Hostname or IP address of Victron device, usually mDNS name like 'venus.local' | Värdnamn eller IP-adress för Victron-enhet, vanligtvis mDNS-namn likt 'venus.local' | Shared reference target checked |
| 19329 | 839958679 | `component::victron_gx::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference target checked |
| 19330 | 839958678 | `component::victron_gx::config::step::reconfigure::data::ssl` | Uses an SSL certificate | Använder ett SSL-certifikat | Shared reference target checked |
| 19331 | 839958677 | `component::victron_gx::config::step::reconfigure::data::port` | Port | Port | Shared reference target checked |
| 19332 | 839958676 | `component::victron_gx::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 19333 | 839958675 | `component::victron_gx::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 19334 | 839958674 | `component::victron_gx::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 19335 | 839958673 | `component::victron_gx::config::abort::different_device` | The device at this address is different from the originally configured device. | Enheten på den här adressen är inte samma som den ursprungligen konfigurerade enheten. | Core-literal match |
| 19336 | 839958669 | `component::switchbot_cloud::entity::sensor::lock_state::state::unlocking` | Unlocking | Låser upp | Core-literal match |
| 19337 | 839958668 | `component::switchbot_cloud::entity::sensor::lock_state::state::unlocked` | Unlocked | Olåst | Shared reference target checked |
| 19338 | 839958667 | `component::switchbot_cloud::entity::sensor::lock_state::state::locking` | Locking | Låser | Core-literal match |
| 19339 | 839958666 | `component::switchbot_cloud::entity::sensor::lock_state::state::locked` | Locked | Låst | Shared reference target checked |
| 19340 | 839958665 | `component::switchbot_cloud::entity::sensor::lock_state::state::latch_bolt_locked` | Latch bolt locked | Låsregeln är låst | Core-literal match |
| 19341 | 839958664 | `component::switchbot_cloud::entity::sensor::lock_state::state::jammed` | Jammed | Fastnat | Core-literal match |
| 19342 | 839958663 | `component::switchbot_cloud::entity::sensor::lock_state::state::half_locked` | Half locked | Halvlåst | Core-literal match |
| 19343 | 839958662 | `component::switchbot_cloud::entity::sensor::lock_state::name` | Lock state | Låsläge | Core-literal match |
| 19344 | 839957622 | `component::victron_gx::exceptions::cannot_connect::message` | Cannot connect to the GX device at {host}. | Det går inte att ansluta till GX-enheten på {host}. | Core-literal match |
| 19345 | 839957621 | `component::victron_gx::exceptions::authentication_failed::message` | Authentication failed for {host}. | Autentiseringen misslyckades för {host}. | Core-literal match |
| 19346 | 839955133 | `component::fumis::config::step::reconfigure::description` | Reconfigure your Fumis pellet stove connection. | Konfigurera om anslutningen till din Fumis pelletskamin. | Core-literal match |
| 19347 | 839955132 | `component::fumis::config::step::reconfigure::data_description::pin` | You can find the PIN code on the label of the Fumis WiRCU Wi-Fi module connected to your stove. | PIN-koden finns på etiketten på den Fumis WiRCU Wi-Fi-modul som är ansluten till din kamin. | Shared reference target checked |
| 19348 | 839955131 | `component::fumis::config::step::reconfigure::data::pin` | PIN code | PIN-kod | Shared reference target checked |
| 19349 | 839955130 | `component::fumis::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 19350 | 839794629 | `component::technove::config::abort::unique_id_mismatch` | MAC address does not match the configured device. Expected to connect to device with MAC: `{expected_mac}`, but connected to device with MAC: `{actual_mac}`. <br><br>Please ensure you reconfigure against the same device. | MAC-adressen stämmer inte överens med den konfigurerade enheten. Förväntades ansluta till enhet med MAC: `{expected_mac}`, men anslöt till enhet med MAC: `{actual_mac}`. <br><br>Se till att du konfigurerar om mot samma enhet. | Core-literal match |
| 19351 | 839794628 | `component::technove::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 19352 | 839766482 | `component::knx::config_panel::common::monitor_x_group_addresses` | Monitor {count} group addresses | Övervaka {count} gruppadresser | Core-literal match |
| 19353 | 839766481 | `component::knx::config_panel::common::exposes_count` | Exposes: {count} | Exponerar: {count} | Core-literal match |
| 19354 | 839758715 | `component::github::config_subentries::repository::step::user::data_description::repository` | The repository to track | Respository att följa | Core-literal match |
| 19355 | 839758714 | `component::github::config_subentries::repository::step::user::data::repository` | Repository | Repository | Core-literal match |
| 19356 | 839758713 | `component::github::config_subentries::repository::initiate_flow::user` | Add repository | Lägg till respository | Core-literal match |
| 19357 | 839758712 | `component::github::config_subentries::repository::entry_type` | Repository | Repository | Shared reference target checked |
| 19358 | 839758711 | `component::github::config_subentries::repository::abort::already_configured` | Repository is already configured | Repository är redan konfigurerat | Core-literal match |
| 19360 | 839021702 | `component::indevolt::entity::sensor::discharge_limit::name` | Discharge limit | Urladdningsgräns | Shared reference target checked |
| 19361 | 838786722 | `component::unifi::entity::switch::wlan_control::name` | Enabled | Aktiverad | Core-literal match |
| 19362 | 838786721 | `component::unifi::entity::switch::poe_port_control::name` | {port_name} PoE | {port_name} PoE | Core-literal match |
| 19363 | 838786720 | `component::unifi::entity::switch::block_client::name` | Blocked | Blockerad | Core-literal match |
| 19364 | 838786719 | `component::unifi::entity::sensor::wlan_clients::name` | Clients | Klienter | Core-literal match |
| 19365 | 838786718 | `component::unifi::entity::sensor::wan_latency::name` | {target} {wan} latency | {target} {wan} latens | Core-literal match |
| 19366 | 838786717 | `component::unifi::entity::sensor::smartpower_ac_power_consumption::name` | AC power consumption | AC-strömförbrukning | Core-literal match |
| 19367 | 838786716 | `component::unifi::entity::sensor::smartpower_ac_power_budget::name` | AC power budget | AC-strömbudget | Core-literal match |
| 19368 | 838786715 | `component::unifi::entity::sensor::port_poe_power::name` | {port_name} PoE power | {port_name} PoE-ström | Core-literal match |
| 19369 | 838786714 | `component::unifi::entity::sensor::port_bandwidth_tx::name` | {port_name} TX | {port_name} TX | Core-literal match |
| 19370 | 838786713 | `component::unifi::entity::sensor::port_bandwidth_rx::name` | {port_name} RX | {port_name} RX | Core-literal match |
| 19371 | 838786712 | `component::unifi::entity::sensor::outlet_power::name` | {outlet_name} outlet power | {outlet_name} uttagseffekt | Core-literal match |
| 19372 | 838786711 | `component::unifi::entity::sensor::device_uptime::name` | Uptime | Upptid | Source-path follow-up open |
| 19373 | 838786710 | `component::unifi::entity::sensor::device_uplink_mac::name` | Uplink MAC | Upplänk MAC | Core-literal match |
| 19374 | 838786709 | `component::unifi::entity::sensor::device_sub_temperature::name` | {name} temperature | {name} temperatur | Core-literal match |
| 19375 | 838786708 | `component::unifi::entity::sensor::device_state::name` | State | Tillstånd | Core-literal match |
| 19376 | 838786707 | `component::unifi::entity::sensor::device_memory_utilization::name` | Memory utilization | Minnesanvändning | Core-literal match |
| 19377 | 838786706 | `component::unifi::entity::sensor::device_cpu_utilization::name` | CPU utilization | CPU-användning | Core-literal match |
| 19378 | 838786705 | `component::unifi::entity::sensor::device_clients::name` | Clients | Klienter | Core-literal match |
| 19379 | 838786704 | `component::unifi::entity::sensor::client_uptime::name` | Uptime | Upptid | Source-path follow-up open |
| 19380 | 838786703 | `component::unifi::entity::sensor::client_bandwidth_tx::name` | TX | TX | Core-literal match |
| 19381 | 838786702 | `component::unifi::entity::sensor::client_bandwidth_rx::name` | RX | RX | Core-literal match |
| 19382 | 838786701 | `component::unifi::entity::image::wlan_qr_code::name` | QR code | QR-kod | Core-literal match |
| 19383 | 838786700 | `component::unifi::entity::button::wlan_regenerate_password::name` | Regenerate password | Återskapa lösenord | Core-literal match |
| 19384 | 838786699 | `component::unifi::entity::button::port_power_cycle::name` | {port_name} power cycle | {port_name} strömcykla | Core-literal match |
| 19385 | 838567987 | `component::firefly_iii::common::verify_ssl_description` | Verify the SSL certificate of the Firefly III instance | Kontrollera SSL-certifikatet för Firefly III-instansen | Core-literal match |
| 19386 | 838567986 | `component::firefly_iii::common::api_key_description` | The access token for authenticating with Firefly III | Åtkomsttoken för autentisering med Firefly III | Core-literal match |
| 19387 | 838567985 | `component::firefly_iii::common::api_key` | Access token | Åtkomsttoken | Core-literal match |
| 19388 | 838563496 | `component::frontier_silicon::exceptions::connection_error::message` | Failed to execute {command}: could not connect to device | Det gick inte att köra {command}: det gick inte att ansluta till enheten | Core-literal match |
| 19389 | 838563495 | `component::frontier_silicon::exceptions::api_error::message` | Failed to execute {command}: {message} | Det gick inte att köra {command}: {message} | Core-literal match |
| 19390 | 838523563 | `component::nobo_hub::selector::override_type::options::now` | Now | Nu | Core-literal match |
| 19391 | 838523562 | `component::nobo_hub::selector::override_type::options::constant` | Constant | Konstant | Core-literal match |
| 19392 | 838035046 | `component::transmission::exceptions::version_error::message` | You are running {transmission_version} of Transmission. Minimum required version is {min_version}. Please upgrade Transmission and then restart Home Assistant. | Du använder version {transmission_version} av Transmission. Minsta krävda version är {min_version}. Uppgradera Transmission och starta sedan om Home Assistant. | Core-literal match |
| 19393 | 838035045 | `component::transmission::config::error::transmission_version` | Minimum required version is 4.0.0. Please upgrade Transmission and then retry. | Minimikravet är version 4.0.0. Uppgradera Transmission och försök igen. | Core-literal match |
| 19394 | 838034906 | `component::portainer::entity::sensor::volume_size::name` | Volume size | Volymstorlek | Core-literal match |
| 19395 | 838034905 | `component::portainer::entity::sensor::volume_driver::name` | Volume driver | Volymdrivrutin | Core-literal match |
| 19396 | 838034846 | `component::portainer::entity::button::recreate_container::name` | Recreate container | Återskapa containern | Core-literal match |
| 19397 | 838026954 | `component::iaqualink::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 19398 | 838026953 | `component::iaqualink::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 19399 | 838026703 | `component::fumis::entity::sensor::wifi_signal_strength::name` | Wi-Fi signal strength | Wi-Fi-signalstyrka | Core-literal match |
| 19400 | 838026702 | `component::fumis::entity::sensor::wifi_rssi::name` | Wi-Fi RSSI | Wi-Fi-RSSI | Core-literal match |
| 19401 | 838026701 | `component::fumis::entity::sensor::uptime::name` | Uptime | Upptid | Core-literal match |
| 19402 | 838026700 | `component::fumis::entity::sensor::time_to_service::name` | Time to service | Tid till service | Core-literal match |
| 19403 | 838026699 | `component::fumis::entity::sensor::stove_status::state::off` | Off | Av | Shared reference target checked |
| 19404 | 838026698 | `component::fumis::entity::sensor::stove_status::state::ignition` | Ignition | Tändning | Core-literal match |
| 19405 | 838026697 | `component::fumis::entity::sensor::stove_status::state::heating_up` | Heating up | Värmer upp | Core-literal match |
| 19406 | 838026696 | `component::fumis::entity::sensor::stove_status::state::eco` | Eco | Eco | Core-literal match |
| 19407 | 838026695 | `component::fumis::entity::sensor::stove_status::state::cooling` | Cooling | Kyler | Core-literal match |
| 19408 | 838026694 | `component::fumis::entity::sensor::stove_status::state::burning` | Burning | Brinner | Core-literal match |
| 19409 | 838026693 | `component::fumis::entity::sensor::stove_status::name` | Stove status | Spisstatus | Core-literal match |
| 19410 | 838026692 | `component::fumis::entity::sensor::pressure::name` | Combustion chamber pressure | Tryck i förbränningskammaren | Core-literal match |
| 19411 | 838026691 | `component::fumis::entity::sensor::power_output::name` | Power output | Effekt ut | Core-literal match |
| 19412 | 838026690 | `component::fumis::entity::sensor::overheatings::name` | Overheatings | Överhettningar | Core-literal match |
| 19413 | 838026689 | `component::fumis::entity::sensor::module_temperature::name` | WiRCU module | WiRCU-modul | Core-literal match |
| 19414 | 838026688 | `component::fumis::entity::sensor::misfires::name` | Misfires | Misständningar | Core-literal match |
| 19415 | 838026687 | `component::fumis::entity::sensor::igniter_starts::name` | Igniter starts | Tändaren startar | Core-literal match |
| 19416 | 838026686 | `component::fumis::entity::sensor::heating_time::name` | Burning time | Brinntid | Core-literal match |
| 19417 | 838026685 | `component::fumis::entity::sensor::fuel_used::name` | Fuel consumed | Förbrukat bränsle | Core-literal match |
| 19418 | 838026684 | `component::fumis::entity::sensor::fuel_quantity::name` | Fuel level | Bränslenivå | Core-literal match |
| 19419 | 838026683 | `component::fumis::entity::sensor::fan_2_speed::name` | Fan 2 speed | Fläkt 2-hastighet | Core-literal match |
| 19420 | 838026682 | `component::fumis::entity::sensor::fan_1_speed::name` | Fan 1 speed | Fläkt 1-hastighet | Core-literal match |
| 19421 | 838026681 | `component::fumis::entity::sensor::detailed_stove_status::state::wood_start` | Wood start | Vedstart | Core-literal match |
| 19422 | 838026680 | `component::fumis::entity::sensor::detailed_stove_status::state::wood_combustion` | Wood combustion | Vedförbränning | Core-literal match |
| 19423 | 838026679 | `component::fumis::entity::sensor::detailed_stove_status::state::wood_burning_off` | Off (wood burning) | Av (vedeldning) | Core-literal match |
| 19424 | 838026678 | `component::fumis::entity::sensor::detailed_stove_status::state::pre_heating` | Pre-heating | Förvärmning | Core-literal match |
| 19425 | 838026677 | `component::fumis::entity::sensor::detailed_stove_status::state::pre_combustion` | Pre-combustion | Förförbränning | Core-literal match |
| 19426 | 838026676 | `component::fumis::entity::sensor::detailed_stove_status::state::off` | Off | Av | Shared reference target checked |
| 19427 | 838026675 | `component::fumis::entity::sensor::detailed_stove_status::state::ignition` | Ignition | Tändning | Core-literal match |
| 19428 | 838026674 | `component::fumis::entity::sensor::detailed_stove_status::state::hybrid_start` | Hybrid start | Hybridstart | Core-literal match |
| 19429 | 838026673 | `component::fumis::entity::sensor::detailed_stove_status::state::hybrid_init` | Hybrid init | Hybrid-init | Core-literal match |
| 19430 | 838026672 | `component::fumis::entity::sensor::detailed_stove_status::state::eco` | Eco | Eco | Core-literal match |
| 19431 | 838026671 | `component::fumis::entity::sensor::detailed_stove_status::state::cooling` | Cooling | Kyler | Core-literal match |
| 19432 | 838026670 | `component::fumis::entity::sensor::detailed_stove_status::state::combustion` | Combustion | Förbränning | Core-literal match |
| 19433 | 838026669 | `component::fumis::entity::sensor::detailed_stove_status::state::cold_start_off` | Off (cold start) | Av (kallstart) | Core-literal match |
| 19434 | 838026668 | `component::fumis::entity::sensor::detailed_stove_status::state::cold_start` | Cold start | Kallstart | Core-literal match |
| 19435 | 838026667 | `component::fumis::entity::sensor::detailed_stove_status::name` | Detailed stove status | Detaljerad status för kaminen | Core-literal match |
| 19436 | 838026666 | `component::fumis::entity::sensor::combustion_chamber_temperature::name` | Combustion chamber | Förbränningskammare | Core-literal match |
| 19437 | 838026446 | `component::fumis::config::step::dhcp_confirm::description` | A Fumis WiRCU Wi-Fi module was discovered on your network. Enter the PIN code from the label on the module to set up your pellet stove. | En Fumis WiRCU Wi-Fi-modul har upptäckts i ditt nätverk. Ange PIN-koden som står på etiketten på modulen för att konfigurera din pelletskamin. | Core-literal match |
| 19438 | 838026445 | `component::fumis::config::step::dhcp_confirm::data_description::pin` | You can find the PIN code on the label of the Fumis WiRCU Wi-Fi module connected to your stove. | PIN-koden finns på etiketten på den Fumis WiRCU Wi-Fi-modul som är ansluten till din kamin. | Shared reference target checked |
| 19439 | 838026444 | `component::fumis::config::step::dhcp_confirm::data::pin` | PIN code | PIN-kod | Shared reference target checked |
| 19440 | 837969252 | `component::nobo_hub::options::step::init::data_description::override_type` | Select "Now" to end the override on the next week profile change, or "Constant" to keep it until manually cleared. | Välj "Nu" för att avsluta åsidosättningen vid nästa veckas profiländring, eller "Konstant" för att behålla den tills den rensas manuellt. | Core-literal match |

## Inte översättningsbara strukturposter

| Lokalise-nyckel-ID | Nyckel | Orsak |
|---:|---|---|
| 839758710 | `component::github::config::step` | Tom engelsk källtext; motsvarande `data: {}` i HA Core |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 839958674 | `component::victron_gx::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 839955130 | `component::fumis::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 839794628 | `component::technove::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 838786711 | `component::unifi::entity::sensor::device_uptime::name` | Uptime |
| 838786704 | `component::unifi::entity::sensor::client_uptime::name` | Uptime |
| 838026954 | `component::iaqualink::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
