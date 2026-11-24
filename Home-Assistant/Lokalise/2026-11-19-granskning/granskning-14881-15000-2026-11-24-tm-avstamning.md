# Home Assistant Core – historisk avstämning 14881–15000

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 92 direkta källtexter matchar HA Core-källan; 24 referensanvändningar med 19 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 4 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 14881 | 891436773 | `component::led_infrared::entity::light::light::state_attributes::effect::state::light_green` | Color: Light green | Färg: Ljusgrön | Core-literal match |
| 14882 | 891436772 | `component::led_infrared::entity::light::light::state_attributes::effect::state::green` | Color: Green | Färg: Grön | Core-literal match |
| 14883 | 891436771 | `component::led_infrared::entity::light::light::state_attributes::effect::state::flash` | Flash | Blinka | Core-literal match |
| 14884 | 891436770 | `component::led_infrared::entity::light::light::state_attributes::effect::state::fade` | Fade | Tona | Core-literal match |
| 14885 | 891436769 | `component::led_infrared::entity::light::light::state_attributes::effect::state::dark_cyan` | Color: Dark cyan | Färg: Mörk cyan | Core-literal match |
| 14886 | 891436768 | `component::led_infrared::entity::light::light::state_attributes::effect::state::cyan` | Color: Cyan | Färg: Cyan | Core-literal match |
| 14887 | 891436767 | `component::led_infrared::entity::light::light::state_attributes::effect::state::blue` | Color: Blue | Färg: Blå | Core-literal match |
| 14888 | 891436766 | `component::led_infrared::config::step::user::title` | Set up LED Infrared device | Konfigurera LED infraröd enhet | Core-literal match |
| 14889 | 891436765 | `component::led_infrared::config::step::user::description` | Select the device type and at least one infrared emitter or receiver. You can identify the correct device based on the remote control used. Please refer to the [documentation]({docs_url}). | Välj enhetstyp och minst en infraröd sändare eller mottagare. Du kan identifiera rätt enhet baserat på fjärrkontrollen som används. Se [dokumentationen]({docs_url}). | Core-literal match |
| 14890 | 891436764 | `component::led_infrared::config::step::user::data_description::infrared_entity_id` | The infrared emitter entity to use for sending commands. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Shared reference target checked |
| 14891 | 891436763 | `component::led_infrared::config::step::user::data_description::device_type` | The type of remote control used for the LED light bulb, lamp, or controller. | Den typ av fjärrkontroll som används för LED lampan, lampan eller styrenheten. | Core-literal match |
| 14892 | 891436762 | `component::led_infrared::config::step::user::data::infrared_entity_id` | Infrared emitter | Infraröd sändare | Shared reference target checked |
| 14893 | 891436761 | `component::led_infrared::config::step::user::data::device_type` | Device type | Enhetstyp | Shared reference target checked |
| 14894 | 891436760 | `component::led_infrared::config::error::missing_infrared_entity` | Select an infrared emitter or receiver. | Välj en infraröd sändare eller mottagare. | Shared reference target checked |
| 14895 | 891436759 | `component::led_infrared::config::abort::no_infrared_entities` | No infrared entities found. Please set up an infrared device first. | Inga infraröda entiteter hittades. Konfigurera först en infraröd enhet. | Shared reference target checked |
| 14896 | 891436758 | `component::led_infrared::config::abort::already_configured` | This device has already been configured with this infrared entity. | Den här enheten har redan konfigurerats med denna infraröda enhet. | Core-literal match |
| 14897 | 891399928 | `component::whirlpool::entity::light::oven_light_upper::name` | Upper oven light | Övre ugnslampa | Core-literal match |
| 14898 | 891399927 | `component::whirlpool::entity::light::oven_light_lower::name` | Lower oven light | Nedre ugnslampa | Core-literal match |
| 14899 | 891399926 | `component::whirlpool::entity::light::oven_light::name` | Light | Lampa | Core-literal match |
| 14900 | 891322228 | `component::smlight::entity::update::z_wave_update::name` | Z-Wave firmware | Z-Wave firmware | Core-literal match |
| 14901 | 891322227 | `component::smlight::entity::button::z_wave_restart::name` | Z-Wave restart | Z-Wave omstart | Core-literal match |
| 14902 | 891322226 | `component::smlight::entity::button::z_wave_flash_mode::name` | Z-Wave flash mode | Z-Wave flashläge | Core-literal match |
| 14903 | 891322144 | `component::mikrotik::entity::sensor::memory_usage::name` | Memory usage | Minnesanvändning | Core-literal match |
| 14904 | 891322143 | `component::mikrotik::entity::sensor::disk_usage::name` | Disk usage | Diskanvändning | Core-literal match |
| 14905 | 891322142 | `component::mikrotik::entity::sensor::cpu_load::name` | CPU usage | CPU-användning | Core-literal match |
| 14906 | 891321926 | `component::karakeep::entity::sensor::tags::unit_of_measurement` | tags | taggar | Core-literal match |
| 14907 | 891321925 | `component::karakeep::entity::sensor::tags::name` | Tags | Taggar | Core-literal match |
| 14908 | 891321924 | `component::karakeep::entity::sensor::lists::unit_of_measurement` | lists | listor | Core-literal match |
| 14909 | 891321923 | `component::karakeep::entity::sensor::lists::name` | Lists | Listor | Core-literal match |
| 14910 | 891321922 | `component::karakeep::entity::sensor::highlights::unit_of_measurement` | highlights | höjdpunkter | Core-literal match |
| 14911 | 891321921 | `component::karakeep::entity::sensor::highlights::name` | Highlights | Höjdpunkter | Core-literal match |
| 14912 | 891321920 | `component::karakeep::entity::sensor::favorites::unit_of_measurement` | favorites | favoriter | Core-literal match |
| 14913 | 891321919 | `component::karakeep::entity::sensor::favorites::name` | Favorites | Favoriter | Core-literal match |
| 14914 | 891321918 | `component::karakeep::entity::sensor::bookmarks::unit_of_measurement` | bookmarks | bokmärken | Core-literal match |
| 14915 | 891321917 | `component::karakeep::entity::sensor::bookmarks::name` | Bookmarks | Bokmärken | Core-literal match |
| 14916 | 891321916 | `component::karakeep::entity::sensor::archived::unit_of_measurement` | items | föremål | Core-literal match |
| 14917 | 891321915 | `component::karakeep::entity::sensor::archived::name` | Archived | Arkiverad | Core-literal match |
| 14918 | 891321914 | `component::karakeep::config::step::user::description` | Connect to your Karakeep instance. | Anslut till din Karakeep instans. | Core-literal match |
| 14919 | 891321913 | `component::karakeep::config::step::user::data_description::verify_ssl` | Should SSL certificates be verified? This should be off for self-signed certificates. | Bör SSL certifikat verifieras? Detta borde vara avstängt för självsignerade certifikat. | Core-literal match |
| 14920 | 891321912 | `component::karakeep::config::step::user::data_description::url` | The URL of your Karakeep instance, including http:// or https://. | URL:en för din Karakeep instans, inklusive http:// eller https://. | Core-literal match |
| 14921 | 891321911 | `component::karakeep::config::step::user::data_description::token` | The API token used to connect to your Karakeep instance. | API-token som används för att ansluta till din Karakeep instans. | Core-literal match |
| 14922 | 891321910 | `component::karakeep::config::step::user::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 14923 | 891321909 | `component::karakeep::config::step::user::data::url` | URL | URL | Shared reference target checked |
| 14924 | 891321908 | `component::karakeep::config::step::user::data::token` | API token | API-token | Shared reference target checked |
| 14925 | 891321907 | `component::karakeep::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 14926 | 891321906 | `component::karakeep::config::error::invalid_url_format` | Enter a valid URL including http:// or https://. | Ange en giltig URL, inklusive http:// eller https://. | Core-literal match |
| 14927 | 891321905 | `component::karakeep::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 14928 | 891321904 | `component::karakeep::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 14929 | 891321903 | `component::karakeep::config::error::api_error` | The Karakeep API returned an unexpected response. | Karakeep-API:et returnerade ett oväntat svar. | Core-literal match |
| 14930 | 891321902 | `component::karakeep::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Shared reference target checked |
| 14931 | 891311840 | `component::nobo_hub::config::step::reconfigure::description` | Update the IP address for Nobø Ecohub with serial number {serial}. | Uppdatera IP-adressen för Nobø Ecohub med serienummer {serial}. | Core-literal match |
| 14932 | 891311839 | `component::nobo_hub::config::step::reconfigure::data_description::ip_address` | The IP address of your Nobø Ecohub. | IP-adressen för din Nobø Ecohub. | Shared reference target checked |
| 14933 | 891311838 | `component::nobo_hub::config::step::reconfigure::data::ip_address` | IP address | IP-adress | Shared reference target checked |
| 14934 | 891311837 | `component::nobo_hub::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 14935 | 891298387 | `component::harman_luxury::exceptions::unexpected_device::message` | The device at this address reports a different serial number than the configured device. | Enheten på den här adressen har ett annat serienummer än den konfigurerade enheten. | Core-literal match |
| 14936 | 891298386 | `component::harman_luxury::exceptions::command_failed::message` | Failed to send the command to the device. | Det gick inte att skicka kommandot till enheten. | Core-literal match |
| 14937 | 891298385 | `component::harman_luxury::config::step::user::data_description::host` | The hostname or IP address of your Harman Luxury device. | Värdnamnet eller IP-adressen för din Harman Luxury-enhet. | Core-literal match |
| 14938 | 891298384 | `component::harman_luxury::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 14939 | 891298383 | `component::harman_luxury::config::step::discovery_confirm::description` | Do you want to set up {name}? | Vill du konfigurera {name}? | Core-literal match |
| 14940 | 891298382 | `component::harman_luxury::config::flow_title` | {name} | {name} | Core-literal match |
| 14941 | 891298381 | `component::harman_luxury::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 14942 | 891298380 | `component::harman_luxury::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 14943 | 891298379 | `component::harman_luxury::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 14944 | 891296526 | `component::tesla_wall_connector::options::step::init::data_description::split_phase` | Enable if your Wall Connector is powered by single-phase / split-phase electrical service. This affects the calculation of the Total power sensor. Leave disabled for three-phase supply (default). | Aktivera om din Wall Connector drivs av enfas eller splittad fas. Detta påverkar beräkningen av den totala effektsensorn. Lämna inaktiverat för trefas (standard). | Shared reference target checked |
| 14945 | 891296525 | `component::tesla_wall_connector::options::step::init::data::split_phase` | Single-phase / Split-phase electrical service | Enfas / splittad fas elförsörjning | Shared reference target checked |
| 14946 | 891296524 | `component::tesla_wall_connector::config::step::user::data_description::split_phase` | Enable if your Wall Connector is powered by single-phase / split-phase electrical service. This affects the calculation of the Total power sensor. Leave disabled for three-phase supply (default). | Aktivera om din Wall Connector drivs av enfas eller splittad fas. Detta påverkar beräkningen av den totala effektsensorn. Lämna inaktiverat för trefas (standard). | Shared reference target checked |
| 14947 | 891296523 | `component::tesla_wall_connector::config::step::user::data::split_phase` | Single-phase / Split-phase electrical service | Enfas / splittad fas elförsörjning | Shared reference target checked |
| 14948 | 891296522 | `component::tesla_wall_connector::common::split_phase_description` | Enable if your Wall Connector is powered by single-phase / split-phase electrical service. This affects the calculation of the Total power sensor. Leave disabled for three-phase supply (default). | Aktivera om din Wall Connector drivs av enfas eller splittad fas. Detta påverkar beräkningen av den totala effektsensorn. Lämna inaktiverat för trefas (standard). | Core-literal match |
| 14949 | 891296521 | `component::tesla_wall_connector::common::split_phase` | Single-phase / Split-phase electrical service | Enfas / splittad fas elförsörjning | Core-literal match |
| 14950 | 891293888 | `component::energieleser::exceptions::unknown_device::message` | The device type for {device_id} is unknown or unsupported | Enhetstypen för {device_id} är okänd eller stöds inte | Core-literal match |
| 14951 | 891293887 | `component::energieleser::exceptions::connection_error::message` | An error occurred while connecting to the device {device_id} | Ett fel uppstod vid anslutning till enheten {device_id} | Core-literal match |
| 14952 | 891293886 | `component::energieleser::exceptions::communication_error::message` | An error occurred while communicating with the device {device_id} | Ett fel uppstod vid kommunikation med enheten {device_id} | Core-literal match |
| 14953 | 891287575 | `component::steam_online::entity::sensor::now_playing::state_attributes::app_id::name` | Steam App ID | Steam App-ID | Core-literal match |
| 14954 | 891287574 | `component::steam_online::entity::sensor::now_playing::name` | Now playing | Spelar nu | Core-literal match |
| 14955 | 891287573 | `component::steam_online::entity::sensor::level::name` | Level | Level | Core-literal match |
| 14956 | 891287572 | `component::steam_online::entity::sensor::last_online::name` | Last online | Senast online | Core-literal match |
| 14957 | 891287571 | `component::steam_online::entity::sensor::account::state_attributes::real_name::name` | Real name | Riktigt namn | Core-literal match |
| 14958 | 891287570 | `component::steam_online::entity::sensor::account::state_attributes::created::name` | Account created | Konto skapat | Core-literal match |
| 14959 | 890973044 | `component::energieleser::config::step::reconfigure::title` | Reconfigure energieleser | Konfigurera om energiläsare | Core-literal match |
| 14960 | 890973043 | `component::energieleser::config::step::reconfigure::description` | Update the IP address or hostname of your energieleser device. | Uppdatera IP-adressen eller värdnamnet för din energiläsarenhet. | Core-literal match |
| 14961 | 890973042 | `component::energieleser::config::step::reconfigure::data_description::host` | Local IP address or hostname of the device (e.g. 192.168.1.42). | Enhetens lokala IP-adress eller värdnamn (t.ex. 192.168.1.42). | Shared reference target checked |
| 14962 | 890973041 | `component::energieleser::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 14963 | 890973040 | `component::energieleser::config::abort::wrong_device` | The device at this IP address does not match the originally configured device. | Enheten på den här IP-adressen matchar inte den ursprungligen konfigurerade enheten. | Core-literal match |
| 14964 | 890973039 | `component::energieleser::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 14965 | 890963399 | `component::luci::config::step::user::data_description::verify_ssl` | Whether to verify the router's SSL certificate. | Anger om routerns SSL-certifikat ska verifieras. | Core-literal match |
| 14966 | 890963398 | `component::luci::config::step::user::data_description::username` | The username to log in to the OpenWrt router. | Användarnamnet för att logga in på OpenWrt-routern. | Core-literal match |
| 14967 | 890963397 | `component::luci::config::step::user::data_description::ssl` | Whether to connect to the router using SSL. | Anger om anslutning till routern ska ske via SSL. | Core-literal match |
| 14968 | 890963396 | `component::luci::config::step::user::data_description::password` | The password to log in to the OpenWrt router. | Lösenordet för att logga in på OpenWrt-routern. | Core-literal match |
| 14969 | 890963395 | `component::luci::config::step::user::data_description::host` | The hostname or IP address of your OpenWrt router. | Värdnamnet eller IP-adressen för din OpenWrt-router. | Core-literal match |
| 14970 | 890963394 | `component::luci::config::step::reauth_confirm::data_description::username` | The username to log in to the OpenWrt router. | Användarnamnet för att logga in på OpenWrt-routern. | Core-literal match |
| 14971 | 890963393 | `component::luci::config::step::reauth_confirm::data_description::password` | The password to log in to the OpenWrt router. | Lösenordet för att logga in på OpenWrt-routern. | Core-literal match |
| 14972 | 890926405 | `component::unifiprotect::exceptions::motion_detection_public_only::message` | Motion detection cannot be changed over the public API; configure it in the UniFi Protect app | Rörelsedetektering kan inte ändras via det publika API:t. Konfigurera det i UniFi Protect-appen istället. | Core-literal match |
| 14973 | 890924873 | `component::netatmo::options::step::public_weather_areas::data_description::weather_areas` | Configured weather areas to edit or remove. | Konfigurerade väderområden som ska redigeras eller tas bort. | Core-literal match |
| 14974 | 890924872 | `component::netatmo::options::step::public_weather_areas::data_description::new_area` | Name of a new weather area to add. | Namn på ett nytt väderområde som ska läggas till. | Core-literal match |
| 14975 | 890924871 | `component::netatmo::options::step::public_weather::data_description::show_on_map` | Whether to show the sensors on the map. | Anger om sensorerna ska visas på kartan. | Core-literal match |
| 14976 | 890924870 | `component::netatmo::options::step::public_weather::data_description::mode` | How values from multiple stations in the area are aggregated. | Hur värden från flera mätstationer i området ska sammanställas. | Core-literal match |
| 14977 | 890924869 | `component::netatmo::options::step::public_weather::data_description::lon_sw` | Longitude of the southwest corner of the area. | Longitud för områdets sydvästra hörn. | Core-literal match |
| 14978 | 890924868 | `component::netatmo::options::step::public_weather::data_description::lon_ne` | Longitude of the northeast corner of the area. | Longitud för områdets nordöstra hörn. | Core-literal match |
| 14979 | 890924867 | `component::netatmo::options::step::public_weather::data_description::lat_sw` | Latitude of the southwest corner of the area. | Latitud för områdets sydvästra hörn. | Core-literal match |
| 14980 | 890924866 | `component::netatmo::options::step::public_weather::data_description::lat_ne` | Latitude of the northeast corner of the area. | Latitud för områdets nordöstra hörn. | Core-literal match |
| 14981 | 890924865 | `component::netatmo::options::step::public_weather::data_description::area_name` | Name used to identify this weather area. | Det namn som används för att identifiera detta väderområde. | Core-literal match |
| 14982 | 890507503 | `component::permobil::issues::integration_removed::title` | The Permobil integration has been removed | Permobil-integrationen har tagits bort | Core-literal match |
| 14983 | 890507502 | `component::permobil::issues::integration_removed::description` | The Permobil integration has been removed from Home Assistant.<br><br>To resolve this issue, please remove the (now defunct) integration entries from your Home Assistant setup. [View your existing Permobil integration entries]({entries}). | Permobil-integrationen har tagits bort från Home Assistant.<br><br>För att lösa problemet tar du bort de numera obrukbara integrationsposterna från din Home Assistant-konfiguration. [Visa dina befintliga Permobil-integrationsposter]({entries}). | Core-literal match |
| 14984 | 890483172 | `component::picnic::entity::sensor::next_delivery_estimated_arrival::name` | Estimated arrival of next delivery | Beräknad ankomsttid för nästa leverans | Core-literal match |
| 14985 | 890474332 | `component::tesla_wall_connector::entity::sensor::wifi_rssi::name` | Wi-Fi RSSI | Wi-Fi-RSSI | Core-literal match |
| 14986 | 890474331 | `component::tesla_wall_connector::entity::sensor::vehicle_current_a::name` | Vehicle current | Fordonsström | Core-literal match |
| 14987 | 890474330 | `component::tesla_wall_connector::entity::sensor::energy_kwh::name` | Lifetime energy | Livstid energi | Core-literal match |
| 14988 | 890470329 | `component::reolink::entity::switch::pre_siren_on_event::name` | Pre-siren on event | Försiren vid händelse | Core-literal match |
| 14989 | 890470328 | `component::reolink::entity::button::pre_siren::name` | Pre-siren | Försiren | Core-literal match |
| 14990 | 890446225 | `component::simplisafe::exceptions::set_system_properties_not_v3::message` | System properties can only be set on V3 systems. | Systemegenskaper kan endast ställas in på V3-system. | Core-literal match |
| 14991 | 890446224 | `component::simplisafe::exceptions::no_system_for_device::message` | No SimpliSafe system could be found for device ID: {device_id} | Inget SimpliSafe-system kunde hittas för enhets-ID: {device_id} | Source-path follow-up open |
| 14992 | 890446223 | `component::simplisafe::exceptions::no_base_station::message` | No base station could be found for device ID: {device_id} | Ingen basstation kunde hittas för enhets-ID: {device_id} | Source-path follow-up open |
| 14993 | 890446222 | `component::simplisafe::exceptions::invalid_device_id::message` | No device could be found for ID: {device_id} | Ingen enhet kunde hittas med ID: {device_id} | Core-literal match |
| 14994 | 890446221 | `component::simplisafe::exceptions::error_while_executing::message` | Error while executing "{service}": {error} | Fel vid körning av "{service}": {error} | Core-literal match |
| 14995 | 890446220 | `component::enphase_envoy::issues::token_expiry::title` | {name} access token expires in {token_lifetime} days. | {name} åtkomsttoken upphör att gälla om {token_lifetime} dagar. | Core-literal match |
| 14996 | 890446219 | `component::enphase_envoy::issues::token_expiry::description` | The {name} access token expires in {token_lifetime} days and is configured for manual token entry. Make sure to enter a new token before the final expiry day. To update the token, go to the Home Assistant Enphase Envoy integration page and use the reconfigure menu option. | Åtkomsttokenet för {name} löper ut om {token_lifetime} dagar och är konfigurerat för manuell inmatning av token. Se till att ange ett nytt token innan den sista utgångsdagen. För att uppdatera din token, gå till integrationssidan för Home Assistant och Enphase Envoy och använd menyalternativet ”Konfigurera om”. | Core-literal match |
| 14997 | 890446218 | `component::enphase_envoy::exceptions::not_initialized::message` | {service}: Enphase Envoy is not yet initialized | {service}: Enphase Envoy har ännu inte initialiserats | Core-literal match |
| 14998 | 890446217 | `component::enphase_envoy::exceptions::no_token_auth::message` | {service}: Envoy token authorization is only used with firmware version 7.0 and later. | {service}: Auktorisering med Envoy-token används endast med firmwareversion 7.0 och senare. | Core-literal match |
| 14999 | 890446216 | `component::enphase_envoy::exceptions::envoy_token_lifetime_service_no_device_id::message` | No Envoy found by token lifetime action. Configure an Envoy or specify a `device_id` if more than 1 Envoy is configured. | Ingen Envoy hittades av åtgärden ”token lifetime”. Konfigurera en Envoy eller ange ett `device_id` om fler än en Envoy är konfigurerad. | Core-literal match |
| 15000 | 890446215 | `component::enphase_envoy::exceptions::envoy_token_lifetime_service_envoy_not_found::message` | No Envoy found by token lifetime action for device ID {device_id}. | Ingen Envoy hittades av åtgärden ”token lifetime” för enhets-ID:t {device_id}. | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 891311837 | `component::nobo_hub::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 890973039 | `component::energieleser::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 890446224 | `component::simplisafe::exceptions::no_system_for_device::message` | No SimpliSafe system could be found for device ID: {device_id} |
| 890446223 | `component::simplisafe::exceptions::no_base_station::message` | No base station could be found for device ID: {device_id} |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
