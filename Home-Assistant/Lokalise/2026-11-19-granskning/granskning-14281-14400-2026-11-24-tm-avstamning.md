# Home Assistant Core – historisk avstämning 14281–14400

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 97 direkta källtexter matchar HA Core-källan; 21 referensanvändningar med 17 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 2 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 14281 | 898758015 | `component::midea::config::step::login_credentials::data_description::password` | Your Midea cloud account password | Lösenord för ditt Midea-molnkonto | Core-literal match |
| 14282 | 898758014 | `component::midea::config::step::login_credentials::data_description::account` | Your Midea cloud account username or email address | Användarnamn eller e-postadress för ditt Midea-molnkonto | Core-literal match |
| 14283 | 898758013 | `component::midea::config::step::login_credentials::data::server` | Server | Server | Core-literal match |
| 14284 | 898758012 | `component::midea::config::step::login_credentials::data::password` | Password | Lösenord | Shared reference target checked |
| 14285 | 898758011 | `component::midea::config::step::login_credentials::data::account` | Account | Konto | Core-literal match |
| 14286 | 898758010 | `component::midea::config::step::list::title` | Discovered appliances | Upptäckta apparater | Core-literal match |
| 14287 | 898758009 | `component::midea::config::step::list::description` | {table} | {table} | Core-literal match |
| 14288 | 898758008 | `component::midea::config::step::auto::title` | Select a discovered device | Välj en upptäckt enhet | Core-literal match |
| 14289 | 898758007 | `component::midea::config::step::auto::data_description::device` | Select the discovered device to configure | Välj den upptäckta enheten att konfigurera | Core-literal match |
| 14290 | 898758006 | `component::midea::config::step::auto::data::device` | Device | Enhet | Shared reference target checked |
| 14291 | 898758005 | `component::midea::config::step::auth_method::title` | Authentication | Autentisering | Core-literal match |
| 14292 | 898758004 | `component::midea::config::step::auth_method::description` | Choose how you want to authenticate. | Välj hur du vill autentisera dig. | Core-literal match |
| 14293 | 898758003 | `component::midea::config::step::auth_method::data_description::login_mode` | How to authenticate with the Midea cloud | Hur man autentiserar med Midea-molnet | Core-literal match |
| 14294 | 898758002 | `component::midea::config::step::auth_method::data::login_mode` | Login mode | Inloggningsläge | Core-literal match |
| 14295 | 898758001 | `component::midea::config::error::type_mismatch` | The type does not match the discovered device | Typen matchar inte den upptäckta enheten | Core-literal match |
| 14296 | 898758000 | `component::midea::config::error::token_unavailable` | Could not get a valid token and key from the cloud | Det gick inte att hämta ett giltig token och nyckel från molnet | Core-literal match |
| 14297 | 898757999 | `component::midea::config::error::protocol_mismatch` | The protocol does not match the discovered device | Protokollet matchar inte den upptäckta enheten | Core-literal match |
| 14298 | 898757998 | `component::midea::config::error::preset_login_failed` | Could not log in with the preset account | Det gick inte att logga in med det förinställda kontot | Core-literal match |
| 14299 | 898757997 | `component::midea::config::error::no_devices` | No devices found | Inga enheter hittades | Core-literal match |
| 14300 | 898757996 | `component::midea::config::error::login_failed` | Could not log in to the selected cloud server | Det gick inte att logga in på den valda molnservern | Core-literal match |
| 14301 | 898757995 | `component::midea::config::error::ip_address_mismatch` | The IP address does not match the discovered device | IP-adressen matchar inte den upptäckta enheten | Core-literal match |
| 14302 | 898757994 | `component::midea::config::error::invalid_token` | Token and key must be valid hexadecimal strings | Token och nyckel måste vara giltiga hexadecimala strängar | Core-literal match |
| 14303 | 898757993 | `component::midea::config::error::invalid_device_ip` | Could not find a supported device at this IP address | Det gick inte att hitta en enhet som stöds på den här IP-adressen | Core-literal match |
| 14304 | 898757992 | `component::midea::config::error::invalid_device_id_for_ip` | The device ID does not match the selected IP address | Enhets-ID:t matchar inte den valda IP-adressen | Core-literal match |
| 14305 | 898757991 | `component::midea::config::error::device_auth_failed` | Could not connect with the provided configuration | Det gick inte att ansluta med den angivna konfigurationen | Core-literal match |
| 14306 | 898757990 | `component::midea::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 14307 | 898726892 | `component::lg_infrared::selector::hvac_modes::options::heat` | Heat | Värme | Core-literal match |
| 14308 | 898726891 | `component::lg_infrared::selector::hvac_modes::options::fan_only` | Fan only | Endast fläkt | Core-literal match |
| 14309 | 898726890 | `component::lg_infrared::selector::hvac_modes::options::dry` | Dry | Avfuktning | Core-literal match |
| 14310 | 898726889 | `component::lg_infrared::selector::hvac_modes::options::cool` | Cool | Kyla | Core-literal match |
| 14311 | 898726888 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::fan_mode::state::quiet` | Quiet | Tyst | Core-literal match |
| 14312 | 898726887 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::fan_mode::state::medium_low` | Medium low | Medellåg | Core-literal match |
| 14313 | 898726886 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::fan_mode::state::medium_high` | Medium high | Medelhög | Core-literal match |
| 14314 | 898726885 | `component::lg_infrared::config::step::user::menu_options::tv` | TV | TV | Shared reference target checked |
| 14315 | 898726884 | `component::lg_infrared::config::step::user::menu_options::ac` | Air conditioner | Luftkonditionering | Core-literal match |
| 14316 | 898726883 | `component::lg_infrared::config::step::tv::title` | Set up LG TV | Ställ in LG TV | Core-literal match |
| 14317 | 898726882 | `component::lg_infrared::config::step::tv::description` | Select at least one infrared emitter or receiver to use with your LG TV. | Välj minst en infraröd sändare eller mottagare att använda med din LG TV. | Core-literal match |
| 14318 | 898726881 | `component::lg_infrared::config::step::tv::data_description::infrared_receiver_entity_id` | The infrared receiver entity to use for receiving signals. | Mottagarentiteten som ska användas för att ta emot infraröda signaler. | Shared reference target checked |
| 14319 | 898726880 | `component::lg_infrared::config::step::tv::data_description::infrared_entity_id` | The infrared emitter entity to use for sending commands. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Shared reference target checked |
| 14320 | 898726879 | `component::lg_infrared::config::step::tv::data::infrared_receiver_entity_id` | Infrared receiver | Infraröd mottagare | Shared reference target checked |
| 14321 | 898726878 | `component::lg_infrared::config::step::tv::data::infrared_entity_id` | Infrared emitter | Infraröd sändare | Shared reference target checked |
| 14322 | 898726877 | `component::lg_infrared::config::step::ac::title` | Set up LG AC | Ställ in LG AC | Core-literal match |
| 14323 | 898726876 | `component::lg_infrared::config::step::ac::description` | Select an infrared emitter and the modes your LG AC supports. | Välj en infraröd sändare och de lägen som din LG AC stöder. | Core-literal match |
| 14324 | 898726875 | `component::lg_infrared::config::step::ac::data_description::infrared_receiver_entity_id` | Optional — allows the integration to update state when the physical remote is used. | Valfritt — tillåter integrationen att uppdatera tillstånd när den fysiska fjärrkontrollen används. | Core-literal match |
| 14325 | 898726874 | `component::lg_infrared::config::step::ac::data_description::infrared_entity_id` | The infrared emitter entity to use for sending commands. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Shared reference target checked |
| 14326 | 898726873 | `component::lg_infrared::config::step::ac::data_description::hvac_modes` | Select the operating modes your AC unit supports. Heat is not available on all models. | Välj de driftlägen som luftkonditioneringen stöder. Värme är inte tillgängligt på alla modeller. | Core-literal match |
| 14327 | 898726872 | `component::lg_infrared::config::step::ac::data::infrared_receiver_entity_id` | Infrared receiver | Infraröd mottagare | Shared reference target checked |
| 14328 | 898726871 | `component::lg_infrared::config::step::ac::data::infrared_entity_id` | Infrared emitter | Infraröd sändare | Shared reference target checked |
| 14329 | 898726870 | `component::lg_infrared::config::step::ac::data::hvac_modes` | Supported modes | Lägen som stöds | Core-literal match |
| 14330 | 898726869 | `component::lg_infrared::config::error::no_hvac_modes` | Select at least one supported mode. | Välj minst ett av de lägen som stöds. | Core-literal match |
| 14331 | 898544038 | `component::ouman_eh_800::config::step::reconfigure::data_description::username` | Username for the Ouman EH-800 web interface | Användarnamn för Ouman EH-800:s webbgränssnitt | Shared reference target checked |
| 14332 | 898544037 | `component::ouman_eh_800::config::step::reconfigure::data_description::url` | The URL of the Ouman EH-800 web interface | URL till Ouman EH-800:s webbgränssnitt | Shared reference target checked |
| 14333 | 898544036 | `component::ouman_eh_800::config::step::reconfigure::data_description::password` | Password for the Ouman EH-800 web interface | Lösenord för Ouman EH-800 webbgränssnitt | Shared reference target checked |
| 14334 | 898544035 | `component::ouman_eh_800::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference target checked |
| 14335 | 898544034 | `component::ouman_eh_800::config::step::reconfigure::data::url` | URL | URL | Shared reference target checked |
| 14336 | 898544033 | `component::ouman_eh_800::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 14337 | 898544032 | `component::ouman_eh_800::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 14338 | 898180455 | `component::izone::exceptions::unable_to_connect::message` | Unable to connect to controller {uid} | Det går inte att ansluta till kontrollern {uid} | Core-literal match |
| 14339 | 898180454 | `component::izone::exceptions::command_rejected::message` | Controller {uid} rejected command: {error} | Kontrollern {uid} avvisade kommandot: {error} | Core-literal match |
| 14340 | 897994669 | `component::mikrotik::entity::button::backup::name` | Backup | Backup | Core-literal match |
| 14341 | 897669617 | `component::event::entity_component::button::state_attributes::multi_press_count::name` | Multi-press count | Multi-tryck antal | Core-literal match |
| 14342 | 897669616 | `component::event::entity_component::button::state_attributes::event_type::state::press_start` | Press start | Tryck start | Core-literal match |
| 14343 | 897669615 | `component::event::entity_component::button::state_attributes::event_type::state::press_end` | Press end | Tryck slut | Core-literal match |
| 14344 | 897669614 | `component::event::entity_component::button::state_attributes::event_type::state::multi_press_ongoing` | Multi-press ongoing | Multi-tryck pågående | Core-literal match |
| 14345 | 897669613 | `component::event::entity_component::button::state_attributes::event_type::state::multi_press_end` | Multi-press end | Multi-tryck slut | Core-literal match |
| 14346 | 897669612 | `component::event::entity_component::button::state_attributes::event_type::state::long_press_start` | Long press start | Långt tryck start | Core-literal match |
| 14347 | 897669611 | `component::event::entity_component::button::state_attributes::event_type::state::long_press_end` | Long press end | Långt tryck slut | Core-literal match |
| 14348 | 897619213 | `component::mikrotik::options::step::device_tracker::data_description::force_dhcp` | Force scanning using DHCP. This will use the DHCP leases to track devices. | Tvinga skanning via DHCP. Detta innebär att enheterna spåras med hjälp av DHCP-leasingavtalen. | Core-literal match |
| 14349 | 897619212 | `component::mikrotik::options::step::device_tracker::data_description::detection_time` | The time interval in seconds to consider a device as home after it was last seen. | Tidsintervallet i sekunder för att en enhet ska betraktas som hemma efter att den senast sågs. | Core-literal match |
| 14350 | 897619211 | `component::mikrotik::options::step::device_tracker::data_description::arp_ping` | Enable ARP ping for device tracking. This will send an ARP request to the device to check if it is online. | Aktivera ARP-ping för enhetsspårning. Detta skickar en ARP-begäran till enheten för att kontrollera om den är online. | Core-literal match |
| 14351 | 897619210 | `component::mikrotik::config::step::user::data_description::verify_ssl` | Verify SSL certificate of your Mikrotik router. | Verifiera SSL-certifikatet för din Mikrotik-router. | Core-literal match |
| 14352 | 897619209 | `component::mikrotik::config::step::user::data_description::username` | The username for your Mikrotik router. | Användarnamnet för din Mikrotik-router. | Core-literal match |
| 14353 | 897619208 | `component::mikrotik::config::step::user::data_description::port` | The port of your Mikrotik router. | Porten på din MikroTik-router. | Core-literal match |
| 14354 | 897619207 | `component::mikrotik::config::step::user::data_description::password` | The password for your Mikrotik router. | Lösenordet till din MikroTik-router. | Core-literal match |
| 14355 | 897619206 | `component::mikrotik::config::step::user::data_description::name` | The name of your Mikrotik router. | Namnet på din Mikrotik-router. | Core-literal match |
| 14356 | 897619205 | `component::mikrotik::config::step::user::data_description::host` | The hostname or IP address of your Mikrotik router. | Värdnamnet eller IP-adressen för din Mikrotik-router. | Core-literal match |
| 14357 | 897619204 | `component::mikrotik::config::step::reauth_confirm::data_description::password` | The password for your Mikrotik device. | Lösenordet för din Mikrotik-enhet. | Core-literal match |
| 14358 | 897503482 | `component::moon::conditions::is_waxing::name` | Moon is waxing | Månen tilltar | Core-literal match |
| 14359 | 897503481 | `component::moon::conditions::is_waxing::description` | Tests if the moon is waxing. | Testar om månen tilltar. | Core-literal match |
| 14360 | 897503480 | `component::moon::conditions::is_waning::name` | Moon is waning | Månen avtar | Core-literal match |
| 14361 | 897503479 | `component::moon::conditions::is_waning::description` | Tests if the moon is waning. | Testar om månen avtar. | Core-literal match |
| 14362 | 897503478 | `component::moon::conditions::is_phase::name` | Moon phase | Månfas | Core-literal match |
| 14363 | 897503477 | `component::moon::conditions::is_phase::fields::phase::name` | Phase | Fas | Core-literal match |
| 14364 | 897503476 | `component::moon::conditions::is_phase::fields::phase::description` | The moon phase to test for. | Den månfas som ska testas. | Core-literal match |
| 14365 | 897503475 | `component::moon::conditions::is_phase::description` | Tests if the moon is in a specific phase. | Testar om månen är i en specifik fas. | Core-literal match |
| 14366 | 897455101 | `component::nintendo_parental_controls::services::update_pin_code::name` | Update PIN code | Uppdatera PIN-kod | Core-literal match |
| 14367 | 897455100 | `component::nintendo_parental_controls::services::update_pin_code::fields::pin::name` | PIN | PIN | Core-literal match |
| 14368 | 897455099 | `component::nintendo_parental_controls::services::update_pin_code::fields::pin::description` | The new PIN code. Enter a 4 to 8-digit PIN between 0000 and 99999999. | Den nya PIN-koden. Ange en PIN-kod med 4 till 8 siffror mellan 0000 och 99999999. | Core-literal match |
| 14369 | 897455098 | `component::nintendo_parental_controls::services::update_pin_code::fields::device_id::name` | Device | Enhet | Core-literal match |
| 14370 | 897455097 | `component::nintendo_parental_controls::services::update_pin_code::fields::device_id::example` | 1234567890abcdef | 1234567890abcdef | Source-path follow-up open |
| 14371 | 897455096 | `component::nintendo_parental_controls::services::update_pin_code::fields::device_id::description` | The ID of the device to update the PIN code for. | ID:t för den enhet som PIN-koden ska uppdateras på. | Core-literal match |
| 14372 | 897455095 | `component::nintendo_parental_controls::services::update_pin_code::description` | Updates the PIN code for the selected Nintendo Switch. | Uppdaterar PIN-koden för den valda Nintendo Switch. | Core-literal match |
| 14373 | 897455094 | `component::nintendo_parental_controls::exceptions::invalid_pin_length::message` | The PIN code must be a 4 to 8-digit number between 0000 and 99999999. | PIN-koden måste vara ett 4- till 8-siffrigt nummer mellan 0000 och 99999999. | Core-literal match |
| 14374 | 897161297 | `component::hassio::issues::unhealthy_os_filesystem_check_error::title` | Unhealthy system - OS partition filesystem check failed | Ohälsosamt system - Kontroll av OS-partitionens filsystem misslyckades | Core-literal match |
| 14375 | 897161296 | `component::hassio::issues::unhealthy_os_filesystem_check_error::description` | System is currently unhealthy because a filesystem integrity check failed on an operating system partition. This can be caused by unexpected power loss or failing storage. For troubleshooting information, select Learn more. | Systemet är för närvarande ohälsosamt eftersom en integritetskontroll av filsystemet misslyckades på ett av operativsystemets partitioner. Detta kan orsakas av oväntade strömavbrott eller ett fel på lagringsenheten. För felsökningsinformation, välj Läs mer. | Core-literal match |
| 14376 | 897161295 | `component::hassio::issues::unhealthy_data_filesystem_check_error::title` | Unhealthy system - Data partition filesystem check failed | Ohälsosamt system - Kontroll av datapartitionens filsystem misslyckades | Core-literal match |
| 14377 | 897161294 | `component::hassio::issues::unhealthy_data_filesystem_check_error::description` | System is currently unhealthy because a filesystem integrity check failed on the data partition. This can be caused by unexpected power loss or failing storage and may affect configuration, apps, or backups. For troubleshooting information, select Learn more. | Systemet är för närvarande ohälsosamt eftersom en integritetskontroll av filsystemet misslyckades på datapartitionen. Detta kan orsakas av oväntade strömavbrott eller ett fel på lagringsenheten och kan påverka konfigurationen, appar eller säkerhetskopior. För felsökningsinformation, välj Läs mer. | Core-literal match |
| 14378 | 896962415 | `component::wiim::exceptions::unsupported_media_type::message` | Unsupported media type: {media_type} | Medietyp stöds inte: {media_type} | Core-literal match |
| 14379 | 896962414 | `component::wiim::exceptions::media_sources_unsupported::message` | Media sources are not supported on this device. | Mediekällor stöds inte på den här enheten. | Core-literal match |
| 14380 | 896962413 | `component::wiim::exceptions::invalid_track_id::message` | Invalid media ID: {media_id}. Expected a valid track index. | Ogiltigt medie-ID: {media_id}. Ett giltigt spårindex förväntas. | Core-literal match |
| 14381 | 896962412 | `component::wiim::exceptions::invalid_preset_id::message` | Invalid preset ID: {media_id} | Ogiltigt förinställnings-ID: {media_id} | Core-literal match |
| 14382 | 896962411 | `component::wiim::exceptions::invalid_browse_path::message` | Invalid browse path: {media_content_id} | Ogiltig sökväg: {media_content_id} | Core-literal match |
| 14383 | 896962410 | `component::wiim::exceptions::http_api_request_failed::message` | HTTP API request failed for {host} | HTTP API-begäran misslyckades för {host} | Core-literal match |
| 14384 | 896962409 | `component::wiim::exceptions::direct_url_playback_unsupported::message` | Direct URL playback is not supported on this device. | Direktuppspelning från URL stöds inte på den här enheten. | Core-literal match |
| 14385 | 896962408 | `component::wiim::exceptions::device_setup_failed::message` | Device setup failed for {host} | Enhetskonfigurationen misslyckades för {host} | Core-literal match |
| 14386 | 896962407 | `component::wiim::exceptions::command_failed::message` | {command} failed for {entity_id} | {command} misslyckades för {entity_id} | Core-literal match |
| 14387 | 896676930 | `component::nextdns::config_subentries::profile::step::user::title` | Add NextDNS profile | Lägg till NextDNS-profil | Core-literal match |
| 14388 | 896676929 | `component::nextdns::config_subentries::profile::step::user::description` | Select the NextDNS profile you want to add. | Välj den NextDNS-profil som du vill lägga till. | Core-literal match |
| 14389 | 896676928 | `component::nextdns::config_subentries::profile::step::user::data_description::profile_id` | The NextDNS configuration profile you want to integrate | Den NextDNS-konfigurationsprofil som du vill integrera | Shared reference target checked |
| 14390 | 896676927 | `component::nextdns::config_subentries::profile::step::user::data::profile_id` | Profile | Profil | Shared reference target checked |
| 14391 | 896676926 | `component::nextdns::config_subentries::profile::initiate_flow::user` | Add profile | Lägg till profil | Core-literal match |
| 14392 | 896676925 | `component::nextdns::config_subentries::profile::entry_type` | NextDNS profile | NextDNS-profil | Core-literal match |
| 14393 | 896676924 | `component::nextdns::config_subentries::profile::abort::entry_not_loaded` | The NextDNS configuration entry is not loaded. Please ensure it is set up correctly before adding a profile. | NextDNS-konfigurationsposten har inte laddats. Se till att den är korrekt konfigurerad innan du lägger till en profil. | Core-literal match |
| 14394 | 896676923 | `component::nextdns::config_subentries::profile::abort::already_configured` | This NextDNS profile is already configured. | Denna NextDNS-profil är redan konfigurerad. | Core-literal match |
| 14395 | 896676922 | `component::nextdns::config_subentries::profile::abort::all_profiles_configured` | All NextDNS profiles are already configured. | Alla NextDNS-profiler är redan konfigurerade. | Shared reference target checked |
| 14396 | 896676921 | `component::nextdns::config::step::profiles::data_description::profile_id` | The NextDNS configuration profile you want to integrate | Den NextDNS-konfigurationsprofil som du vill integrera | Core-literal match |
| 14397 | 896676920 | `component::nextdns::config::step::profiles::data::profile_id` | Profile | Profil | Core-literal match |
| 14398 | 896676919 | `component::nextdns::config::abort::all_profiles_configured` | All NextDNS profiles are already configured. | Alla NextDNS-profiler är redan konfigurerade. | Core-literal match |
| 14399 | 896674291 | `component::knx::config_panel::expose::create::yaml::yaml_error` | There are YAML errors and it cannot be parsed. Switching to the visual editor may cause pending changes to be lost. | Det finns YAML-fel och det kan inte tolkas. Om du byter till den visuella redigeraren kan det leda till att väntande ändringar går förlorade. | Shared reference target checked |
| 14400 | 896674290 | `component::knx::config_panel::expose::create::yaml::mode_hint` | This is an internal representation of the expose configuration and may change in future Home Assistant versions. YAML mode is intended for debugging, and for sharing or copying configurations — prefer the visual editor for everyday use. | Detta är en intern representation av Expose-konfigurationen och kan komma att ändras i framtida versioner av Home Assistant. YAML-läget är avsett för felsökning samt för att dela eller kopiera konfigurationer – använd helst den visuella redigeraren för daglig användning. | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 898544032 | `component::ouman_eh_800::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 897455097 | `component::nintendo_parental_controls::services::update_pin_code::fields::device_id::example` | 1234567890abcdef |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
