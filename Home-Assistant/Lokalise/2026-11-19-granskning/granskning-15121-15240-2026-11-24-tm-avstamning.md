# Home Assistant Core – historisk avstämning 15121–15240

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 100 direkta källtexter matchar HA Core-källan; 15 referensanvändningar med 10 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 5 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 15121 | 889701858 | `component::gree::entity::climate::climate::state_attributes::swing_mode::state::fixed_upper` | Fixed upper | Fast övre | Core-literal match |
| 15122 | 889701857 | `component::gree::entity::climate::climate::state_attributes::swing_mode::state::fixed_middle` | Fixed middle | Fast mitten | Core-literal match |
| 15123 | 889701856 | `component::gree::entity::climate::climate::state_attributes::swing_mode::state::fixed_lower_middle` | Fixed lower middle | Fast nedre mitten | Core-literal match |
| 15124 | 889701855 | `component::gree::entity::climate::climate::state_attributes::swing_mode::state::fixed_lower` | Fixed lower | Fast nedre | Core-literal match |
| 15125 | 889701854 | `component::gree::entity::climate::climate::state_attributes::swing_mode::state::default` | Default | Standard | Core-literal match |
| 15126 | 889701853 | `component::gree::entity::climate::climate::state_attributes::swing_horizontal_mode::state::right_center` | Right center | Höger mitten | Core-literal match |
| 15127 | 889701852 | `component::gree::entity::climate::climate::state_attributes::swing_horizontal_mode::state::right` | Right | Höger | Core-literal match |
| 15128 | 889701851 | `component::gree::entity::climate::climate::state_attributes::swing_horizontal_mode::state::left_center` | Left center | Vänster mitten | Core-literal match |
| 15129 | 889701850 | `component::gree::entity::climate::climate::state_attributes::swing_horizontal_mode::state::left` | Left | Vänster | Core-literal match |
| 15130 | 889701849 | `component::gree::entity::climate::climate::state_attributes::swing_horizontal_mode::state::full_swing` | Full swing | Full sving | Core-literal match |
| 15131 | 889701848 | `component::gree::entity::climate::climate::state_attributes::swing_horizontal_mode::state::default` | Default | Standard | Core-literal match |
| 15132 | 889701847 | `component::gree::entity::climate::climate::state_attributes::swing_horizontal_mode::state::center` | Center | Mitten | Core-literal match |
| 15133 | 889700960 | `component::steam_online::config_subentries::friend::step::user::title` | Friend online status | Väns online-status | Core-literal match |
| 15134 | 889700959 | `component::steam_online::config_subentries::friend::step::user::description` | Track the online status of a Steam friend. | Spåra en Steam-väns onlinestatus. | Core-literal match |
| 15135 | 889700958 | `component::steam_online::config_subentries::friend::step::user::data_description::account` | Select a friend from your friend list to track their online status. | Välj en vän från din vänlista för att spåra deras onlinestatus. | Core-literal match |
| 15136 | 889700957 | `component::steam_online::config_subentries::friend::step::user::data::account` | Friend | Vän | Core-literal match |
| 15137 | 889700956 | `component::steam_online::config_subentries::friend::initiate_flow::user` | Add friend | Lägg till vän | Core-literal match |
| 15138 | 889700955 | `component::steam_online::config_subentries::friend::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 15139 | 889700954 | `component::steam_online::config_subentries::friend::error::timeout_connect` | Timeout while establishing a connection | Tidsgränsen överskreds när anslutningen upprättades. | Shared reference target checked |
| 15140 | 889700953 | `component::steam_online::config_subentries::friend::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15141 | 889700952 | `component::steam_online::config_subentries::friend::entry_type` | Friend | Vän | Core-literal match |
| 15142 | 889700951 | `component::steam_online::config_subentries::friend::abort::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 15143 | 889700950 | `component::steam_online::config_subentries::friend::abort::timeout_connect` | Timeout while establishing a connection | Tidsgränsen överskreds när anslutningen upprättades. | Shared reference target checked |
| 15144 | 889700949 | `component::steam_online::config_subentries::friend::abort::no_more_friends` | All friends from your friend list have already been added. | Alla vänner från din vänlista har redan lagts till. | Core-literal match |
| 15145 | 889700948 | `component::steam_online::config_subentries::friend::abort::friendlist_private` | Your friend list appears to be private or inaccessible.<br><br>To add friend accounts open Steam and go to [**{name} > Profile > Edit Profile > Privacy Settings**]({privacy_settings_url}) and set **Friends List** to **Public**.<br><br>Once your friends are added, you can switch it back to your preferred privacy setting. | Din vänlista verkar vara privat eller oåtkomlig.<br><br>För att lägga till vänkonton, öppna Steam och gå till [**{name} > Profil > Redigera profil > Sekretessinställningar**]({privacy_settings_url}) och ställ in **Vänlista** till **Offentlig**.<br><br>När dina vänner har lagts till kan du återställa till de sekretessinställningar som du önskar. | Core-literal match |
| 15146 | 889700947 | `component::steam_online::config_subentries::friend::abort::config_entry_not_loaded` | Cannot add friend accounts when the main account is disabled or not loaded. | Det går inte att lägga till vänkonton när huvudkontot är inaktiverat eller inte har laddats in. | Core-literal match |
| 15147 | 889700946 | `component::steam_online::config_subentries::friend::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15148 | 889700945 | `component::steam_online::config_subentries::friend::abort::already_configured_as_entry` | This account is already configured as a service and cannot be added as a friend. | Det här kontot är redan konfigurerat som en tjänst och kan inte läggas till som en vän. | Core-literal match |
| 15149 | 889700944 | `component::steam_online::config_subentries::friend::abort::already_configured` | Already configured as a friend in this or another account. | Du är redan registrerad som vän på det här eller ett annat konto. | Core-literal match |
| 15150 | 889700943 | `component::steam_online::config::abort::already_configured_as_subentry` | This Steam account is already configured as a sub-entry. | Det här Steam-kontot är redan konfigurerat som en underpost. | Core-literal match |
| 15151 | 889611937 | `component::weatherflow::entity::sensor::lightning_strike_last_epoch::name` | Lightning last strike | Senaste blixtnedslag | Core-literal match |
| 15152 | 889611936 | `component::weatherflow::entity::sensor::lightning_strike_last_energy::name` | Lightning last energy | Energi vid senaste blixtnedslag | Core-literal match |
| 15153 | 889611935 | `component::weatherflow::entity::sensor::lightning_strike_last_distance::name` | Lightning last distance | Avstånd till senaste blixtnedslag | Core-literal match |
| 15154 | 889360105 | `component::environment_canada::options::step::init::data_description::radar_fps` | Frame rate of the radar animation | Bildfrekvens för radaranimationen | Source-path follow-up open |
| 15155 | 889360104 | `component::environment_canada::options::step::init::data_description::radar_duration` | How far back the radar animation goes, in minutes (0 for the full available history) | Hur långt tillbaka i tiden radaranimationen sträcker sig, i minuter (0 för hela den tillgängliga historiken) | Source-path follow-up open |
| 15156 | 889360103 | `component::environment_canada::options::step::init::data::radar_fps` | Loop frame rate | Loop-bildfrekvens | Source-path follow-up open |
| 15157 | 889360102 | `component::environment_canada::options::step::init::data::radar_duration` | Loop duration | Looplängd | Source-path follow-up open |
| 15158 | 889358652 | `component::melcloud_home::exceptions::temperature_min_exceeds_max::message` | The minimum temperature must be lower than the maximum temperature. | Den lägsta temperaturen måste vara lägre än den högsta temperaturen. | Core-literal match |
| 15159 | 889358651 | `component::melcloud_home::exceptions::temperature_max_below_min::message` | The maximum temperature must be higher than the minimum temperature. | Den högsta temperaturen måste vara högre än den lägsta temperaturen. | Core-literal match |
| 15160 | 889358650 | `component::melcloud_home::entity::number::overheat_protection_min_temp::name` | Overheat protection minimum temperature | Överhettningsskydd lägsta temperatur | Core-literal match |
| 15161 | 889358649 | `component::melcloud_home::entity::number::overheat_protection_max_temp::name` | Overheat protection maximum temperature | Överhettningsskydd högsta temperatur | Core-literal match |
| 15162 | 889358648 | `component::melcloud_home::entity::number::frost_protection_min_temp::name` | Frost protection minimum temperature | Frostskydd lägsta temperatur | Core-literal match |
| 15163 | 889358647 | `component::melcloud_home::entity::number::frost_protection_max_temp::name` | Frost protection maximum temperature | Frostskydd högsta temperatur | Core-literal match |
| 15164 | 889058194 | `component::zwave_js::services::set_user::fields::credential_type::name` | Credential type | Typ av autentisering | Core-literal match |
| 15165 | 889058193 | `component::zwave_js::services::set_user::fields::credential_type::description` | The type of credential (pin_code or password). | Typ av autentiseringsuppgift (PIN-kod eller lösenord). | Core-literal match |
| 15166 | 889058192 | `component::zwave_js::services::set_user::fields::credential_slot::name` | Credential slot | Plats för autentiseringsuppgift | Core-literal match |
| 15167 | 889058191 | `component::zwave_js::services::set_user::fields::credential_slot::description` | Credential slot index. If not specified, the first available slot is used. | Index för autentiseringsuppgift. Om inget anges används den första tillgängliga platsen. | Core-literal match |
| 15168 | 889058190 | `component::zwave_js::services::set_user::fields::credential_data::name` | Credential data | Autentiseringsuppgift | Core-literal match |
| 15169 | 889058189 | `component::zwave_js::services::set_user::fields::credential_data::description` | The credential data (e.g. PIN digits or password string). | Autentiseringsuppgift (t.ex. PIN-siffror eller lösenordssträng). | Core-literal match |
| 15170 | 889058188 | `component::zwave_js::exceptions::credential_required::message` | This device requires a credential when adding a user. | Den här enheten kräver inloggningsuppgifter när en användare läggs till. | Core-literal match |
| 15171 | 889014433 | `component::velux::entity::number::open_position_limitation::name` | Open position limit | Gräns för öppen position | Core-literal match |
| 15172 | 889014432 | `component::velux::entity::number::closed_position_limitation::name` | Closed position limit | Gräns för stängd position | Core-literal match |
| 15173 | 888988534 | `component::subaru::entity::sensor::vehicle_state::state::ignition_on` | Ignition on | Tändning på | Core-literal match |
| 15174 | 888988533 | `component::subaru::entity::sensor::vehicle_state::state::ignition_off` | Ignition off | Tändning av | Core-literal match |
| 15175 | 888988532 | `component::subaru::entity::sensor::vehicle_state::state::ignition_acc` | Accessory power | Tillbehörsström | Core-literal match |
| 15176 | 888988531 | `component::subaru::entity::sensor::vehicle_state::state::engine_on_remote_start` | Engine on (remote start) | Motorn är igång (fjärrstart) | Core-literal match |
| 15177 | 888988530 | `component::subaru::entity::sensor::vehicle_state::name` | Vehicle state | Fordonets tillstånd | Core-literal match |
| 15178 | 888988529 | `component::subaru::entity::sensor::recommended_tire_pressure_rear::name` | Recommended tire pressure rear | Rekommenderat däcktryck bak | Core-literal match |
| 15179 | 888988528 | `component::subaru::entity::sensor::recommended_tire_pressure_front::name` | Recommended tire pressure front | Rekommenderat däcktryck fram | Core-literal match |
| 15180 | 888974621 | `component::fronius::entity::binary_sensor::battery_standby::name` | Battery standby | Batteri standby | Core-literal match |
| 15181 | 888974620 | `component::fronius::entity::binary_sensor::backup_mode::name` | Backup mode | Läge för säkerhetskopiering | Core-literal match |
| 15182 | 888925804 | `component::melcloud_home::config::step::reconfigure::description` | Re-enter your credentials to reconfigure your MELCloud Home account. | Ange dina inloggningsuppgifter på nytt för att konfigurera om ditt MELCloud Home-konto. | Core-literal match |
| 15183 | 888925803 | `component::melcloud_home::config::step::reconfigure::data_description::password` | Password for your MELCloud Home account. | Lösenord för ditt MELCloud Home-konto. | Shared reference target checked |
| 15184 | 888925802 | `component::melcloud_home::config::step::reconfigure::data_description::email` | Email address for your MELCloud Home account. | E-postadress för ditt MELCloud Home-konto. | Shared reference target checked |
| 15185 | 888925801 | `component::melcloud_home::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 15186 | 888925800 | `component::melcloud_home::config::step::reconfigure::data::email` | Email | E-post | Shared reference target checked |
| 15187 | 888925799 | `component::melcloud_home::config::abort::reconfigure_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 15188 | 888925632 | `component::liebherr::exceptions::invalid_api_key::message` | Invalid API key | Ogiltig API-nyckel | Core-literal match |
| 15189 | 888925631 | `component::liebherr::exceptions::device_timeout_error::message` | Timeout communicating with device {device_id} | Timeout för kommunikation med enheten {device_id} | Core-literal match |
| 15190 | 888925630 | `component::liebherr::exceptions::device_connection_error::message` | Failed to connect to device {device_id} | Det gick inte att ansluta till enheten {device_id} | Core-literal match |
| 15191 | 888925629 | `component::liebherr::exceptions::device_communication_error::message` | Error communicating with device {device_id} | Fel vid kommunikation med enheten {device_id} | Core-literal match |
| 15192 | 888925628 | `component::liebherr::exceptions::cannot_connect::message` | Failed to connect to the Liebherr API | Det gick inte att ansluta till Liebherr API | Core-literal match |
| 15193 | 888925627 | `component::liebherr::exceptions::auth_expired::message` | API key is no longer valid | API-nyckeln är inte längre giltig | Core-literal match |
| 15194 | 888762660 | `component::aqualogic::issues::deprecated_yaml_import_issue_cannot_connect::title` | The {integration_title} YAML configuration is being removed | YAML-konfigurationen för {integration_title} tas bort | Core-literal match |
| 15195 | 888762659 | `component::aqualogic::issues::deprecated_yaml_import_issue_cannot_connect::description` | Configuring {integration_title} via YAML is deprecated and will be removed in a future release. While importing your YAML configuration, the AquaLogic device could not be reached or did not respond as an AquaLogic panel. Please ensure the device is accessible and restart Home Assistant to retry, or remove the {domain} key from your configuration and set up the integration via the UI. | Konfiguration av {integration_title} via YAML är föråldrad och kommer att tas bort i en framtida version. När YAML-konfigurationen importerades kunde AquaLogic-enheten inte nås eller svarade inte som en AquaLogic-panel. Kontrollera att enheten kan nås och starta om Home Assistant för att försöka igen. Du kan också ta bort nyckeln {domain} från konfigurationen och konfigurera integrationen via användargränssnittet. | Core-literal match |
| 15196 | 888762658 | `component::aqualogic::config::step::user::data_description::port` | TCP port used to connect to the AquaLogic controller | TCP-port som används för att ansluta till AquaLogic-styrenheten | Core-literal match |
| 15197 | 888762657 | `component::aqualogic::config::step::user::data_description::host` | Hostname or IP address of your AquaLogic controller | Värdnamn eller IP-adress för din AquaLogic-styrenhet | Core-literal match |
| 15198 | 888762656 | `component::aqualogic::config::step::user::data::port` | Port | Port | Shared reference target checked |
| 15199 | 888762655 | `component::aqualogic::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 15200 | 888762654 | `component::aqualogic::config::error::invalid_device` | The device at the given address is not an AquaLogic panel | Enheten på den angivna adressen är inte en AquaLogic-panel | Core-literal match |
| 15201 | 888762653 | `component::aqualogic::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15202 | 888762652 | `component::aqualogic::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15203 | 888762651 | `component::aqualogic::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 15204 | 888762650 | `component::onedrive::exceptions::no_files_match_pattern::message` | No files match the following patterns: {patterns} | Inga filer matchar följande mönster: {patterns} | Core-literal match |
| 15205 | 888762532 | `component::liebherr::exceptions::open_auto_door_error::message` | An error occurred while opening the door | Ett fel uppstod när dörren öppnades | Core-literal match |
| 15206 | 888762531 | `component::liebherr::exceptions::close_auto_door_error::message` | An error occurred while closing the door | Ett fel uppstod när dörren stängdes | Core-literal match |
| 15207 | 888762530 | `component::liebherr::entity::cover::auto_door_top_zone::name` | Top zone AutoDoor | Övre zon AutoDoor | Core-literal match |
| 15208 | 888762529 | `component::liebherr::entity::cover::auto_door_middle_zone::name` | Middle zone AutoDoor | Mellanzon AutoDoor | Core-literal match |
| 15209 | 888762528 | `component::liebherr::entity::cover::auto_door_bottom_zone::name` | Bottom zone AutoDoor | Bottenzon AutoDoor | Core-literal match |
| 15210 | 888762527 | `component::liebherr::entity::cover::auto_door::name` | AutoDoor | AutoDoor | Core-literal match |
| 15211 | 888762369 | `component::tessie::entity::text::navigation_destination::name` | Navigation destination | Navigeringsdestination | Core-literal match |
| 15212 | 888761879 | `component::dsmr::config::step::user::data_description::port` | Select a serial device, or enter a network address such as socket://host:port | Välj en seriell enhet eller ange en nätverksadress, till exempel socket://host:port | Core-literal match |
| 15213 | 888761878 | `component::dsmr::config::step::user::data::port` | Select device | Välj enhet | Core-literal match |
| 15214 | 888761877 | `component::dsmr::config::step::user::data::dsmr_version` | Select DSMR version | Välj DSMR-version | Core-literal match |
| 15215 | 888761609 | `component::lg_thinq::entity::climate::climate_air_conditioner::state_attributes::fan_mode::state::slow_low` | Super low | Superlåg | Core-literal match |
| 15216 | 888761608 | `component::lg_thinq::entity::climate::climate_air_conditioner::state_attributes::fan_mode::state::mid_high` | Medium high | Medelhög | Core-literal match |
| 15217 | 888761607 | `component::lg_thinq::entity::climate::climate_air_conditioner::state_attributes::fan_mode::state::low_mid` | Low medium | Låg medel | Core-literal match |
| 15218 | 888761606 | `component::lg_thinq::entity::climate::climate_air_conditioner::state_attributes::fan_mode::state::breeze` | Light breeze | Lätt bris | Core-literal match |
| 15219 | 888761596 | `component::html5::issues::deprecated_event_bus::title` | Detected use of deprecated event {event} | Upptäckt användning av föråldrad händelse {event} | Core-literal match |
| 15220 | 888761595 | `component::html5::issues::deprecated_event_bus::description` | Detected **{listeners}** listener(s) for the event `{event}`.<br><br>The HTML5 Push Notifications integration firing events on the event bus is deprecated and this functionality will be removed in a future release.<br><br>Please update your automations and scripts to use the event entities instead.<br><br>## Example automation:<br><br>{example_yaml} | Upptäckte **{listeners}** lyssnare för händelse `{event}`.<br><br>HTML5 Push Notifications-integrationen som utlöser händelser på händelsebussen är föråldrad och den här funktionen kommer att tas bort i en framtida version.<br><br>Uppdatera dina automatiseringar och skript för att använda händelseentiteterna istället.<br><br>## Exempel på automatisering:<br><br>{example_yaml} | Core-literal match |
| 15221 | 888761587 | `component::surepetcare::exceptions::invalid_pet_name::message` | Unknown Sure Petcare pet: {pet_name} | Okänt Sure Petcare-husdjur: {pet_name} | Core-literal match |
| 15222 | 888761586 | `component::surepetcare::exceptions::invalid_flap_id::message` | Unknown Sure Petcare flap ID: {flap_id} | Okänt Sure Petcare luck-ID: {flap_id} | Core-literal match |
| 15223 | 888761585 | `component::geniushub::exceptions::invalid_zone::message` | Unknown Genius Hub zone: {entity_id} | Okänd Genius Hub-zon: {entity_id} | Core-literal match |
| 15224 | 888761584 | `component::geniushub::exceptions::invalid_entity_id::message` | Unknown Genius Hub entity: {entity_id} | Okänd Genius Hub-entitet: {entity_id} | Core-literal match |
| 15225 | 888748679 | `component::wmspro::services::set_cover_position_and_tilt::name` | Set cover position and tilt | Ställ in skyddets position och lutning | Core-literal match |
| 15226 | 888748678 | `component::wmspro::services::set_cover_position_and_tilt::fields::tilt_position::name` | Tilt position | Lutningsposition | Core-literal match |
| 15227 | 888748677 | `component::wmspro::services::set_cover_position_and_tilt::fields::tilt_position::description` | Target tilt position. | Målposition för lutning. | Core-literal match |
| 15228 | 888748676 | `component::wmspro::services::set_cover_position_and_tilt::fields::position::name` | Position | Position | Core-literal match |
| 15229 | 888748675 | `component::wmspro::services::set_cover_position_and_tilt::fields::position::description` | Target vertical position. 0 means closed, 100 means fully open. | Vertikalt målläge. 0 betyder stängt, 100 betyder helt öppet. | Core-literal match |
| 15230 | 888748674 | `component::wmspro::services::set_cover_position_and_tilt::description` | Moves the cover and tilt to the target position simultaneously, preventing cancellation of individual movements. | Flyttar skyddet och ställer in lutningen samtidigt till de angivna mållägena, så att de enskilda rörelserna inte avbryter varandra. | Core-literal match |
| 15231 | 888747892 | `component::portainer::entity::update::container_image_update::name` | Image update available | Avbildningsuppdatering tillgänglig | Core-literal match |
| 15232 | 888718724 | `component::upnp::entity::sensor::upload_speed_no_rollover_handling::name` | Upload speed (no rollover handling) | Uppladdningshastighet (utan rollover-hantering) | Core-literal match |
| 15233 | 888718723 | `component::upnp::entity::sensor::packet_upload_speed_no_rollover_handling::name` | Packet upload speed (no rollover handling) | Uppladdningshastighet för paket (utan rollover-hantering) | Core-literal match |
| 15234 | 888718722 | `component::upnp::entity::sensor::packet_download_speed_no_rollover_handling::name` | Packet download speed (no rollover handling) | Nedladdningshastighet för paket (utan rollover-hantering) | Core-literal match |
| 15235 | 888718721 | `component::upnp::entity::sensor::download_speed_no_rollover_handling::name` | Download speed (no rollover handling) | Nedladdningshastighet (utan rollover-hantering) | Core-literal match |
| 15236 | 888691555 | `component::melcloud_home::entity::sensor::energy_consumed::name` | Energy consumed (monthly) | Förbrukad energi (månadsvis) | Core-literal match |
| 15237 | 888633946 | `component::google_health::config::abort::api_not_enabled` | The Google Health API is not enabled for your Google Cloud project. Enable it in the [Google Cloud Console]({url}), wait a few minutes for the change to propagate, then try again. | Google Health API är inte aktiverat för ditt Google Cloud-projekt. Aktivera det i [Google Cloud Console]({url}), vänta några minuter tills ändringen har trätt i kraft och försök sedan igen. | Core-literal match |
| 15238 | 888596808 | `component::luci::issues::yaml_import_invalid_auth::title` | YAML configuration import failed: invalid authentication | Import av YAML-konfiguration misslyckades: ogiltig autentisering | Core-literal match |
| 15239 | 888596807 | `component::luci::issues::yaml_import_invalid_auth::description` | The YAML configuration for OpenWrt (luci) at `{host}` could not be imported because the credentials are invalid.<br><br>Please update your `configuration.yaml` with valid credentials and restart Home Assistant. | YAML-konfigurationen för OpenWrt (luci) på `{host}` kunde inte importeras eftersom inloggningsuppgifterna är ogiltiga.<br><br>Uppdatera din `configuration.yaml` med giltiga inloggningsuppgifter och starta om Home Assistant. | Core-literal match |
| 15240 | 888596806 | `component::luci::issues::yaml_import_cannot_connect::title` | YAML configuration import failed: cannot connect | Import av YAML-konfigurationen misslyckades: går inte att ansluta | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 889360105 | `component::environment_canada::options::step::init::data_description::radar_fps` | Frame rate of the radar animation |
| 889360104 | `component::environment_canada::options::step::init::data_description::radar_duration` | How far back the radar animation goes, in minutes (0 for the full available history) |
| 889360103 | `component::environment_canada::options::step::init::data::radar_fps` | Loop frame rate |
| 889360102 | `component::environment_canada::options::step::init::data::radar_duration` | Loop duration |
| 888925799 | `component::melcloud_home::config::abort::reconfigure_successful` | Re-authentication was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
