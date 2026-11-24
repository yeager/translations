# Home Assistant Core – historisk avstämning 14401–14520

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 46 direkta källtexter matchar HA Core-källan; 12 referensanvändningar med 11 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 62 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 14401 | 896674289 | `component::knx::config_panel::entities::create::yaml::yaml_error` | There are YAML errors and it cannot be parsed. Switching to the visual editor may cause pending changes to be lost. | Det finns YAML-fel och det kan inte tolkas. Om du byter till den visuella redigeraren kan det leda till att väntande ändringar går förlorade. | Core-literal match |
| 14402 | 896674288 | `component::knx::config_panel::entities::create::yaml::mode_hint` | This is an internal representation of the entity configuration and may change in future Home Assistant versions. YAML mode is intended for debugging, and for sharing or copying configurations — prefer the visual editor for everyday use. | Detta är en intern representation av entitetens konfiguration och kan komma att ändras i framtida versioner av Home Assistant. YAML-läget är avsett för felsökning samt för att dela eller kopiera konfigurationer – använd helst den visuella redigeraren för daglig användning. | Core-literal match |
| 14403 | 896674287 | `component::knx::config_panel::dpt_reference::title` | DPT reference | DPT-referens | Core-literal match |
| 14404 | 896674286 | `component::knx::config_panel::dpt_reference::description` | Browse supported KNX datapoint types | Bläddra bland de KNX-datapunkttyper som stöds | Core-literal match |
| 14405 | 896674285 | `component::knx::config_panel::dialogs::send::write_button` | Write | Skriv | Core-literal match |
| 14406 | 896674284 | `component::knx::config_panel::dialogs::send::title` | Send KNX telegram | Skicka KNX-telegram | Core-literal match |
| 14407 | 896674283 | `component::knx::config_panel::dialogs::send::response::label` | Response | Svar | Core-literal match |
| 14408 | 896674282 | `component::knx::config_panel::dialogs::send::response::description` | Send as GroupValueResponse telegram. | Skicka som GroupValueResponse-telegram. | Core-literal match |
| 14409 | 896674281 | `component::knx::config_panel::dialogs::send::read_button` | Read | Läs | Core-literal match |
| 14410 | 896674280 | `component::knx::config_panel::dialogs::send::description` | You can use the hotkey `s` to spawn this dialog from anywhere in the KNX config panel. | Du kan använda snabbtangenten `s` för att öppna den här dialogrutan var som helst i KNX-konfigurationspanelen. | Core-literal match |
| 14411 | 896674279 | `component::knx::config_panel::dialogs::send::data::label` | Data | Data | Core-literal match |
| 14412 | 896674278 | `component::knx::config_panel::dialogs::send::data::description` | The data to send in the telegram. The format depends on the selected datapoint type. | Data som ska skickas i telegrammet. Formatet beror på vald datapunktstyp. | Core-literal match |
| 14413 | 896674277 | `component::knx::config_panel::dashboard::send::title` | Send KNX telegram | Skicka KNX-telegram | Shared reference target checked |
| 14414 | 896674276 | `component::knx::config_panel::dashboard::send::description` | Send an arbitrary telegram to the KNX bus. | Skicka ett godtyckligt telegram till KNX-bussen. | Core-literal match |
| 14415 | 896640994 | `component::mikrotik::entity::button::shutdown::name` | Shutdown | Stäng av | Core-literal match |
| 14416 | 896289838 | `component::edifier_infrared::entity::button::line::name` | Line | Linjeingång | Core-literal match |
| 14417 | 895881179 | `component::midea_lan::selector::login_mode::options::preset` | Preset cloud credentials | Förinställda inloggningsuppgifter för moln | Source-path follow-up open |
| 14418 | 895881178 | `component::midea_lan::selector::login_mode::options::account` | Your account credentials | Dina inloggningsuppgifter | Source-path follow-up open |
| 14419 | 895881177 | `component::midea_lan::exceptions::unsupported_hvac_mode::message` | HVAC mode {hvac_mode} is not supported by this device. | HVAC-läge {hvac_mode} stöds inte av den här enheten. | Source-path follow-up open |
| 14420 | 895881176 | `component::midea_lan::entity::climate::climate_zone2::name` | Zone 2 thermostat | Zon 2 termostat | Source-path follow-up open |
| 14421 | 895881175 | `component::midea_lan::entity::climate::climate_zone1::name` | Zone 1 thermostat | Zon 1 termostat | Source-path follow-up open |
| 14422 | 895881174 | `component::midea_lan::config::step::user::title` | Set up Midea LAN | Konfigurera Midea LAN | Source-path follow-up open |
| 14423 | 895881173 | `component::midea_lan::config::step::user::menu_options::search` | Search automatically | Sök automatiskt | Source-path follow-up open |
| 14424 | 895881172 | `component::midea_lan::config::step::user::menu_options::manually` | Configure manually | Konfigurera manuellt | Source-path follow-up open |
| 14425 | 895881171 | `component::midea_lan::config::step::user::menu_options::list` | List all appliances only | Lista endast alla apparater | Source-path follow-up open |
| 14426 | 895881170 | `component::midea_lan::config::step::search::title` | Search devices | Sök enheter | Source-path follow-up open |
| 14427 | 895881169 | `component::midea_lan::config::step::search::data_description::ip_address` | Enter 'auto' to scan your network, or enter a specific IP address | Ange "auto" för att skanna ditt nätverk, eller ange en specifik IP-adress | Source-path follow-up open |
| 14428 | 895881168 | `component::midea_lan::config::step::search::data::ip_address` | IP address | IP-adress | Source-path follow-up open |
| 14429 | 895881167 | `component::midea_lan::config::step::manually::title` | Configure manually | Konfigurera manuellt | Source-path follow-up open |
| 14430 | 895881166 | `component::midea_lan::config::step::manually::data_description::type` | The type of your Midea appliance | Typen av din Midea-apparat | Source-path follow-up open |
| 14431 | 895881165 | `component::midea_lan::config::step::manually::data_description::token` | The token of your Midea appliance (hexadecimal string) | Token för din Midea-apparat (hexadecimal sträng) | Source-path follow-up open |
| 14432 | 895881164 | `component::midea_lan::config::step::manually::data_description::subtype` | The subtype of your Midea appliance | Subtypen för din Midea-apparat | Source-path follow-up open |
| 14433 | 895881163 | `component::midea_lan::config::step::manually::data_description::protocol` | The protocol used by your Midea appliance | Protokollet som används av din Midea-apparat | Source-path follow-up open |
| 14434 | 895881162 | `component::midea_lan::config::step::manually::data_description::port` | The local port used by your Midea appliance | Den lokala porten som används av din Midea-apparat | Source-path follow-up open |
| 14435 | 895881161 | `component::midea_lan::config::step::manually::data_description::model` | The model of your Midea appliance | Modellen på din Midea-apparat | Source-path follow-up open |
| 14436 | 895881160 | `component::midea_lan::config::step::manually::data_description::key` | The key of your Midea appliance (hexadecimal string) | Nyckeln till din Midea-apparat (hexadecimal sträng) | Source-path follow-up open |
| 14437 | 895881159 | `component::midea_lan::config::step::manually::data_description::ip_address` | The local IP address of your Midea appliance | Den lokala IP-adressen för din Midea-apparat | Source-path follow-up open |
| 14438 | 895881158 | `component::midea_lan::config::step::manually::data_description::device_id` | The device ID of your Midea appliance | Enhets-ID:t för din Midea-apparat | Source-path follow-up open |
| 14439 | 895881157 | `component::midea_lan::config::step::manually::data::type` | Type | Typ | Source-path follow-up open |
| 14440 | 895881156 | `component::midea_lan::config::step::manually::data::token` | Token | Token | Source-path follow-up open |
| 14441 | 895881155 | `component::midea_lan::config::step::manually::data::subtype` | Subtype | Subtyp | Source-path follow-up open |
| 14442 | 895881154 | `component::midea_lan::config::step::manually::data::protocol` | Protocol | Protokoll | Source-path follow-up open |
| 14443 | 895881153 | `component::midea_lan::config::step::manually::data::port` | Port | Port | Source-path follow-up open |
| 14444 | 895881152 | `component::midea_lan::config::step::manually::data::model` | Model | Modell | Source-path follow-up open |
| 14445 | 895881151 | `component::midea_lan::config::step::manually::data::key` | Key | Nyckel | Source-path follow-up open |
| 14446 | 895881150 | `component::midea_lan::config::step::manually::data::ip_address` | IP address | IP-adress | Source-path follow-up open |
| 14447 | 895881149 | `component::midea_lan::config::step::manually::data::device_id` | Device ID | Enhets-ID | Source-path follow-up open |
| 14448 | 895881148 | `component::midea_lan::config::step::login_credentials::title` | Cloud login | Molninloggning | Source-path follow-up open |
| 14449 | 895881147 | `component::midea_lan::config::step::login_credentials::data_description::server` | The Midea cloud server for your region | Mideas molnserver för din region | Source-path follow-up open |
| 14450 | 895881146 | `component::midea_lan::config::step::login_credentials::data_description::password` | Your Midea cloud account password | Lösenord för ditt Midea-molnkonto | Source-path follow-up open |
| 14451 | 895881145 | `component::midea_lan::config::step::login_credentials::data_description::account` | Your Midea cloud account username or email address | Användarnamn eller e-postadress för ditt Midea-molnkonto | Source-path follow-up open |
| 14452 | 895881144 | `component::midea_lan::config::step::login_credentials::data::server` | Server | Server | Source-path follow-up open |
| 14453 | 895881143 | `component::midea_lan::config::step::login_credentials::data::password` | Password | Lösenord | Source-path follow-up open |
| 14454 | 895881142 | `component::midea_lan::config::step::login_credentials::data::account` | Account | Konto | Source-path follow-up open |
| 14455 | 895881141 | `component::midea_lan::config::step::list::title` | Discovered appliances | Upptäckta apparater | Source-path follow-up open |
| 14456 | 895881140 | `component::midea_lan::config::step::list::description` | {table} | {table} | Source-path follow-up open |
| 14457 | 895881139 | `component::midea_lan::config::step::auto::title` | Select a discovered device | Välj en upptäckt enhet | Source-path follow-up open |
| 14458 | 895881138 | `component::midea_lan::config::step::auto::data_description::device` | Select the discovered device to configure | Välj den upptäckta enheten att konfigurera | Source-path follow-up open |
| 14459 | 895881137 | `component::midea_lan::config::step::auto::data::device` | Device | Enhet | Source-path follow-up open |
| 14460 | 895881136 | `component::midea_lan::config::step::auth_method::title` | Authentication | Autentisering | Source-path follow-up open |
| 14461 | 895881135 | `component::midea_lan::config::step::auth_method::description` | Choose how you want to authenticate. | Välj hur du vill autentisera dig. | Source-path follow-up open |
| 14462 | 895881134 | `component::midea_lan::config::step::auth_method::data_description::login_mode` | How to authenticate with the Midea cloud | Hur man autentiserar med Midea-molnet | Source-path follow-up open |
| 14463 | 895881133 | `component::midea_lan::config::step::auth_method::data::login_mode` | Login mode | Inloggningsläge | Source-path follow-up open |
| 14464 | 895881132 | `component::midea_lan::config::error::type_mismatch` | The type does not match the discovered device | Typen matchar inte den upptäckta enheten | Source-path follow-up open |
| 14465 | 895881131 | `component::midea_lan::config::error::token_unavailable` | Could not get a valid token and key from the cloud | Det gick inte att hämta ett giltig token och nyckel från molnet | Source-path follow-up open |
| 14466 | 895881130 | `component::midea_lan::config::error::protocol_mismatch` | The protocol does not match the discovered device | Protokollet matchar inte den upptäckta enheten | Source-path follow-up open |
| 14467 | 895881129 | `component::midea_lan::config::error::preset_login_failed` | Could not log in with the preset account | Det gick inte att logga in med det förinställda kontot | Source-path follow-up open |
| 14468 | 895881128 | `component::midea_lan::config::error::no_devices` | No devices found | Inga enheter hittades | Source-path follow-up open |
| 14469 | 895881127 | `component::midea_lan::config::error::login_failed` | Could not log in to the selected cloud server | Det gick inte att logga in på den valda molnservern | Source-path follow-up open |
| 14470 | 895881126 | `component::midea_lan::config::error::ip_address_mismatch` | The IP address does not match the discovered device | IP-adressen matchar inte den upptäckta enheten | Source-path follow-up open |
| 14471 | 895881125 | `component::midea_lan::config::error::invalid_token` | Token and key must be valid hexadecimal strings | Token och nyckel måste vara giltiga hexadecimala strängar | Source-path follow-up open |
| 14472 | 895881124 | `component::midea_lan::config::error::invalid_device_ip` | Could not find a supported device at this IP address | Det gick inte att hitta en enhet som stöds på den här IP-adressen | Source-path follow-up open |
| 14473 | 895881123 | `component::midea_lan::config::error::invalid_device_id_for_ip` | The device ID does not match the selected IP address | Enhets-ID:t matchar inte den valda IP-adressen | Source-path follow-up open |
| 14474 | 895881122 | `component::midea_lan::config::error::device_auth_failed` | Could not connect with the provided configuration | Det gick inte att ansluta med den angivna konfigurationen | Source-path follow-up open |
| 14475 | 895881121 | `component::midea_lan::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Source-path follow-up open |
| 14476 | 895653199 | `component::google_health::entity::sensor::sleep_to_fall_asleep::name` | Time to fall asleep | Tid till sovande | Core-literal match |
| 14477 | 895653198 | `component::google_health::entity::sensor::sleep_in_bed::name` | Time in bed | Tid i säng | Core-literal match |
| 14478 | 895653197 | `component::google_health::entity::sensor::sleep_awake::name` | Time awake | Tid vaken | Core-literal match |
| 14479 | 895653196 | `component::google_health::entity::sensor::sleep_asleep::name` | Time asleep | Tid sovande | Core-literal match |
| 14480 | 895653195 | `component::google_health::entity::sensor::sleep_after_wakeup::name` | Time after waking up | Tid efter uppvak | Core-literal match |
| 14481 | 895598752 | `component::portainer::entity::sensor::container_health_state::state::unhealthy` | Unhealthy | Ohälsosam | Core-literal match |
| 14482 | 895598751 | `component::portainer::entity::sensor::container_health_state::state::starting` | Starting | Startar | Core-literal match |
| 14483 | 895598750 | `component::portainer::entity::sensor::container_health_state::state::healthy` | Healthy | Hälsosam | Core-literal match |
| 14484 | 895598749 | `component::portainer::entity::sensor::container_health_state::name` | Health | Hälsa | Core-literal match |
| 14485 | 895570665 | `component::yardian::entity::binary_sensor::freeze_prevent_enabled::name` | Freeze prevent enabled | Frostskydd aktiverat | Core-literal match |
| 14486 | 895228381 | `component::smlight::exceptions::invalid_auth::message` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 14487 | 895228380 | `component::schlage::entity::select::auto_lock_time::state:::600` | 10 minutes | 10 minuter | Core-literal match |
| 14488 | 895228379 | `component::schlage::entity::select::auto_lock_time::state:::360` | 6 minutes | 6 minuter | Core-literal match |
| 14489 | 895218046 | `component::roborock::entity::select::cleaning_mode::state::smart_mode` | Smart | Smart | Core-literal match |
| 14490 | 895218045 | `component::roborock::entity::select::cleaning_mode::state::custom` | Custom | Anpassad | Core-literal match |
| 14491 | 895154319 | `component::imou::entity::sensor::use_time::name` | Usage duration | Användningstid | Core-literal match |
| 14492 | 895154318 | `component::imou::entity::sensor::use_electricity::name` | Energy consumption | Energiförbrukning | Core-literal match |
| 14493 | 895154317 | `component::imou::entity::sensor::switch_cnt::name` | Cycles today | Cykler idag | Core-literal match |
| 14494 | 895154316 | `component::imou::entity::sensor::storage_used::name` | Storage used | Använt lagringsutrymme | Core-literal match |
| 14495 | 895154315 | `component::imou::entity::sensor::status::state::upgrading` | Upgrading | Uppgraderar | Core-literal match |
| 14496 | 895154314 | `component::imou::entity::sensor::status::state::sleep` | Standby | Viloläge | Shared reference target checked |
| 14497 | 895154313 | `component::imou::entity::sensor::status::state::online` | Connected | Ansluten | Shared reference target checked |
| 14498 | 895154312 | `component::imou::entity::sensor::status::state::offline` | Disconnected | Frånkopplad | Shared reference target checked |
| 14499 | 895154311 | `component::imou::entity::sensor::status::name` | Status | Status | Core-literal match |
| 14500 | 895098666 | `component::google_health::config::abort::wrong_account` | Wrong account: Please authenticate with the right account. | Fel konto: autentisera med det rätta kontot. | Core-literal match |
| 14501 | 895098665 | `component::google_health::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 14502 | 894891160 | `component::overkiz::config::abort::reconfigure_wrong_account` | You can only reconfigure this entry with the same Overkiz account and hub | Du kan bara omkonfigurera den här posten med samma Overkiz-konto och hubb. | Core-literal match |
| 14503 | 894891159 | `component::overkiz::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 14504 | 894809069 | `component::gardena_bluetooth::entity::sensor::water_temperature::name` | Water temperature | Vattentemperatur | Core-literal match |
| 14505 | 894809068 | `component::gardena_bluetooth::entity::sensor::tank_pressure::name` | Tank pressure | Tanktryck | Core-literal match |
| 14506 | 894734065 | `component::shelly::config::step::user_manual::data_description::verify_ssl` | Verify SSL/TLS certificate when connecting on HTTPS (port 443, Gen2+). | Verifiera SSL/TLS-certifikatet vid anslutning via HTTPS (port 443, Gen2+). | Core-literal match |
| 14507 | 894734064 | `component::shelly::config::step::user_manual::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 14508 | 894734063 | `component::shelly::config::step::reconfigure::data_description::verify_ssl` | Verify SSL/TLS certificate when connecting on HTTPS (port 443, Gen2+). | Verifiera SSL/TLS-certifikatet vid anslutning via HTTPS (port 443, Gen2+). | Shared reference target checked |
| 14509 | 894734062 | `component::shelly::config::step::reconfigure::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 14510 | 894713762 | `component::wattwaechter::config::step::reconfigure::title` | Reconfigure WattWächter | Konfigurera om WattWächter Plus | Core-literal match |
| 14511 | 894713761 | `component::wattwaechter::config::step::reconfigure::data_description::token` | The API token for your WattWächter device. | API-token för din WattWächter Plus-enhet. | Shared reference target checked |
| 14512 | 894713760 | `component::wattwaechter::config::step::reconfigure::data_description::host` | The hostname or IP address of your WattWächter device. | Värdnamnet eller IP-adressen för din WattWächter Plus-enhet. | Shared reference target checked |
| 14513 | 894713759 | `component::wattwaechter::config::step::reconfigure::data::token` | API token | API-token | Shared reference target checked |
| 14514 | 894713758 | `component::wattwaechter::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 14515 | 894713757 | `component::wattwaechter::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 14516 | 894700257 | `component::duco::entity::sensor::supply_air_temperature::name` | Supply air temperature | Tilluftstemperatur | Core-literal match |
| 14517 | 894700256 | `component::duco::entity::sensor::outdoor_air_temperature::name` | Outdoor air temperature | Utomhustemperatur | Core-literal match |
| 14518 | 894700255 | `component::duco::entity::sensor::extract_air_temperature::name` | Extract air temperature | Frånluftstemperatur | Core-literal match |
| 14519 | 894700254 | `component::duco::entity::sensor::exhaust_air_temperature::name` | Exhaust air temperature | Frånluftstemperatur | Core-literal match |
| 14520 | 894678347 | `component::portainer::entity::sensor::container_state::state::removing` | Removing | Tar bort | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 895881179 | `component::midea_lan::selector::login_mode::options::preset` | Preset cloud credentials |
| 895881178 | `component::midea_lan::selector::login_mode::options::account` | Your account credentials |
| 895881177 | `component::midea_lan::exceptions::unsupported_hvac_mode::message` | HVAC mode {hvac_mode} is not supported by this device. |
| 895881176 | `component::midea_lan::entity::climate::climate_zone2::name` | Zone 2 thermostat |
| 895881175 | `component::midea_lan::entity::climate::climate_zone1::name` | Zone 1 thermostat |
| 895881174 | `component::midea_lan::config::step::user::title` | Set up Midea LAN |
| 895881173 | `component::midea_lan::config::step::user::menu_options::search` | Search automatically |
| 895881172 | `component::midea_lan::config::step::user::menu_options::manually` | Configure manually |
| 895881171 | `component::midea_lan::config::step::user::menu_options::list` | List all appliances only |
| 895881170 | `component::midea_lan::config::step::search::title` | Search devices |
| 895881169 | `component::midea_lan::config::step::search::data_description::ip_address` | Enter 'auto' to scan your network, or enter a specific IP address |
| 895881168 | `component::midea_lan::config::step::search::data::ip_address` | IP address |
| 895881167 | `component::midea_lan::config::step::manually::title` | Configure manually |
| 895881166 | `component::midea_lan::config::step::manually::data_description::type` | The type of your Midea appliance |
| 895881165 | `component::midea_lan::config::step::manually::data_description::token` | The token of your Midea appliance (hexadecimal string) |
| 895881164 | `component::midea_lan::config::step::manually::data_description::subtype` | The subtype of your Midea appliance |
| 895881163 | `component::midea_lan::config::step::manually::data_description::protocol` | The protocol used by your Midea appliance |
| 895881162 | `component::midea_lan::config::step::manually::data_description::port` | The local port used by your Midea appliance |
| 895881161 | `component::midea_lan::config::step::manually::data_description::model` | The model of your Midea appliance |
| 895881160 | `component::midea_lan::config::step::manually::data_description::key` | The key of your Midea appliance (hexadecimal string) |
| 895881159 | `component::midea_lan::config::step::manually::data_description::ip_address` | The local IP address of your Midea appliance |
| 895881158 | `component::midea_lan::config::step::manually::data_description::device_id` | The device ID of your Midea appliance |
| 895881157 | `component::midea_lan::config::step::manually::data::type` | Type |
| 895881156 | `component::midea_lan::config::step::manually::data::token` | Token |
| 895881155 | `component::midea_lan::config::step::manually::data::subtype` | Subtype |
| 895881154 | `component::midea_lan::config::step::manually::data::protocol` | Protocol |
| 895881153 | `component::midea_lan::config::step::manually::data::port` | Port |
| 895881152 | `component::midea_lan::config::step::manually::data::model` | Model |
| 895881151 | `component::midea_lan::config::step::manually::data::key` | Key |
| 895881150 | `component::midea_lan::config::step::manually::data::ip_address` | IP address |
| 895881149 | `component::midea_lan::config::step::manually::data::device_id` | Device ID |
| 895881148 | `component::midea_lan::config::step::login_credentials::title` | Cloud login |
| 895881147 | `component::midea_lan::config::step::login_credentials::data_description::server` | The Midea cloud server for your region |
| 895881146 | `component::midea_lan::config::step::login_credentials::data_description::password` | Your Midea cloud account password |
| 895881145 | `component::midea_lan::config::step::login_credentials::data_description::account` | Your Midea cloud account username or email address |
| 895881144 | `component::midea_lan::config::step::login_credentials::data::server` | Server |
| 895881143 | `component::midea_lan::config::step::login_credentials::data::password` | Password |
| 895881142 | `component::midea_lan::config::step::login_credentials::data::account` | Account |
| 895881141 | `component::midea_lan::config::step::list::title` | Discovered appliances |
| 895881140 | `component::midea_lan::config::step::list::description` | {table} |
| 895881139 | `component::midea_lan::config::step::auto::title` | Select a discovered device |
| 895881138 | `component::midea_lan::config::step::auto::data_description::device` | Select the discovered device to configure |
| 895881137 | `component::midea_lan::config::step::auto::data::device` | Device |
| 895881136 | `component::midea_lan::config::step::auth_method::title` | Authentication |
| 895881135 | `component::midea_lan::config::step::auth_method::description` | Choose how you want to authenticate. |
| 895881134 | `component::midea_lan::config::step::auth_method::data_description::login_mode` | How to authenticate with the Midea cloud |
| 895881133 | `component::midea_lan::config::step::auth_method::data::login_mode` | Login mode |
| 895881132 | `component::midea_lan::config::error::type_mismatch` | The type does not match the discovered device |
| 895881131 | `component::midea_lan::config::error::token_unavailable` | Could not get a valid token and key from the cloud |
| 895881130 | `component::midea_lan::config::error::protocol_mismatch` | The protocol does not match the discovered device |
| 895881129 | `component::midea_lan::config::error::preset_login_failed` | Could not log in with the preset account |
| 895881128 | `component::midea_lan::config::error::no_devices` | No devices found |
| 895881127 | `component::midea_lan::config::error::login_failed` | Could not log in to the selected cloud server |
| 895881126 | `component::midea_lan::config::error::ip_address_mismatch` | The IP address does not match the discovered device |
| 895881125 | `component::midea_lan::config::error::invalid_token` | Token and key must be valid hexadecimal strings |
| 895881124 | `component::midea_lan::config::error::invalid_device_ip` | Could not find a supported device at this IP address |
| 895881123 | `component::midea_lan::config::error::invalid_device_id_for_ip` | The device ID does not match the selected IP address |
| 895881122 | `component::midea_lan::config::error::device_auth_failed` | Could not connect with the provided configuration |
| 895881121 | `component::midea_lan::config::abort::already_configured` | Device is already configured |
| 895098665 | `component::google_health::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 894891159 | `component::overkiz::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 894713757 | `component::wattwaechter::config::abort::reconfigure_successful` | Reconfiguration was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
