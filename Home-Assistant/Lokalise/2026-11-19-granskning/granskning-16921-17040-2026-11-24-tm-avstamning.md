# Home Assistant Core – historisk avstämning 16921–17040

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 80 direkta källtexter matchar HA Core-källan; 38 referensanvändningar med 26 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 2 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Tre Edifier infrared-konsumenter uppdaterades till exakt samma svenska mål som sina gemensamma referenser, sparades i Lokalise och verifierades med API-readback. Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 16921 | 868110389 | `component::roborock::config::step::custom_url::description` | Enter the Roborock server URL to connect to. | Ange URL:en för Roborock-servern som du vill ansluta till. | Core-literal match |
| 16922 | 868110388 | `component::roborock::config::step::custom_url::data_description::roborock_server_url` | The URL of the Roborock server. | URL-adressen till Roborock-servern. | Core-literal match |
| 16923 | 868110387 | `component::roborock::config::step::custom_url::data::roborock_server_url` | Roborock Server URL | Roborock-serverns URL | Core-literal match |
| 16924 | 868110386 | `component::roborock::config::error::invalid_url_format` | The URL must start with http:// or https:// and include a valid host. | URL:en måste börja med http:// eller https:// och innehålla en giltig värd. | Core-literal match |
| 16925 | 867623121 | `component::device_tracker::entity_component::_::state_attributes::tracking_type::state::position` | Position | Position | Core-literal match |
| 16926 | 867623120 | `component::device_tracker::entity_component::_::state_attributes::tracking_type::state::connection` | Connection | Anslutning | Core-literal match |
| 16927 | 867623119 | `component::device_tracker::entity_component::_::state_attributes::tracking_type::name` | Tracking type | Spårningstyp | Core-literal match |
| 16928 | 867598927 | `component::blebox::entity::sensor::open_status::state::unclosed_or_unlocked` | Unclosed or unlocked | Ej stängd eller olåst | Core-literal match |
| 16929 | 867598926 | `component::blebox::entity::sensor::open_status::state::open` | Open | Öppen | Shared reference target checked |
| 16930 | 867598925 | `component::blebox::entity::sensor::open_status::state::closed_but_unlocked` | Closed but unlocked | Stängd men olåst | Core-literal match |
| 16931 | 867598924 | `component::blebox::entity::sensor::open_status::state::closed` | Closed | Stängd | Shared reference target checked |
| 16932 | 867598923 | `component::blebox::entity::sensor::open_status::state::ajar` | Ajar | På glänt | Core-literal match |
| 16933 | 867598916 | `component::vistapool::entity::light::pool_light::name` | Light | Lampa | Shared reference target checked |
| 16934 | 867598650 | `component::evohome::issues::deprecated_refresh_system_service::title` | Evohome 'Refresh system' action is deprecated | Funktionen ”Refresh system” i Evohome är utfasad | Core-literal match |
| 16935 | 867598649 | `component::evohome::issues::deprecated_refresh_system_service::description` | The `refresh_system` action is deprecated and will stop working in Home Assistant {breaks_in_ha_version}. Instead, use the `homeassistant.update_entity` action, targeting the controller's climate entity. | Åtgärden `refresh_system` är utfasad och kommer inte längre att fungera i Home Assistant {breaks_in_ha_version}. Använd istället åtgärden `homeassistant.update_entity` och rikta den mot styrenhetens klimatentitet. | Core-literal match |
| 16936 | 867588155 | `component::samsung_infrared::exceptions::invalid_source::message` | Cannot select input source {invalid_source} for media player. Valid sources: {valid_sources}. | Det går inte att välja ingångskälla {invalid_source} för mediaspelare. Giltiga källor: {valid_sources}. | Core-literal match |
| 16937 | 867588154 | `component::samsung_infrared::entity::media_player::samsung_ir_tv::state_attributes::source::state::tv` | TV | TV | Shared reference target checked |
| 16938 | 867588153 | `component::samsung_infrared::entity::media_player::samsung_ir_tv::state_attributes::source::state::hdmi_4` | HDMI 4 | HDMI 4 | Core-literal match |
| 16939 | 867588152 | `component::samsung_infrared::entity::media_player::samsung_ir_tv::state_attributes::source::state::hdmi_3` | HDMI 3 | HDMI 3 | Core-literal match |
| 16940 | 867588151 | `component::samsung_infrared::entity::media_player::samsung_ir_tv::state_attributes::source::state::hdmi_2` | HDMI 2 | HDMI 2 | Core-literal match |
| 16941 | 867588150 | `component::samsung_infrared::entity::media_player::samsung_ir_tv::state_attributes::source::state::hdmi_1` | HDMI 1 | HDMI 1 | Core-literal match |
| 16942 | 867580305 | `component::vistapool::config::step::reconfigure::title` | Reconfigure Vistapool | Konfigurera om Vistapool | Core-literal match |
| 16943 | 867580304 | `component::vistapool::config::step::reconfigure::description` | Update the stored password for {username}. | Uppdatera det lagrade lösenordet för {username}. | Core-literal match |
| 16944 | 867580303 | `component::vistapool::config::step::reconfigure::data_description::password` | The password for your Vistapool account. | Lösenordet för ditt Vistapool-konto. | Shared reference target checked |
| 16945 | 867580302 | `component::vistapool::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 16946 | 867580301 | `component::vistapool::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 16947 | 867580300 | `component::vistapool::config::abort::account_mismatch` | The credentials entered are for a different Vistapool account than the one being reconfigured. | De autentiseringsuppgifter som anges är för ett annat Vistapool-konto än det som omkonfigureras. | Core-literal match |
| 16948 | 867558830 | `component::blebox::exceptions::install_failed::message` | Failed to install firmware update on the BleBox device: {error} | Misslyckades med att installera firmwareuppdateringen på BleBox-enheten: {error} | Core-literal match |
| 16949 | 867558829 | `component::blebox::exceptions::effect_not_found::message` | The specified light effect is not available on this device: {error} | Den angivna ljuseffekten är inte tillgänglig på den här enheten: {error} | Core-literal match |
| 16950 | 867558828 | `component::blebox::exceptions::data_update_failed::message` | An error occurred while communicating with the BleBox device: {error} | Ett fel uppstod vid kommunikation med BleBox-enheten: {error} | Core-literal match |
| 16951 | 867558827 | `component::blebox::exceptions::command_failed::message` | Failed to execute command on the BleBox device: {error} | Misslyckades med att utföra kommandot på BleBox-enheten: {error} | Core-literal match |
| 16952 | 867558826 | `component::blebox::exceptions::bad_value::message` | Turning on the light failed: {error} | Det gick inte att tända lampan: {error} | Core-literal match |
| 16953 | 867262174 | `component::swisscom::issues::deprecated_yaml_import_issue_credentials_required::title` | The {integration_title} YAML configuration is being removed | YAML-konfigurering för {integration_title} tas bort | Core-literal match |
| 16954 | 867262173 | `component::swisscom::issues::deprecated_yaml_import_issue_credentials_required::description` | Configuring the {integration_title} integration through YAML is deprecated. The integration now requires a username and password to authenticate to your Internet-Box, which cannot be safely carried over from YAML.<br><br>Set up the integration through the UI to provide your credentials (your existing host `{host}` will need to be re-entered), then remove the `{domain}` entry from your `configuration.yaml` file and restart Home Assistant. | Konfigurationen av {integration_title} -integrationen via YAML är föråldrad. Integrationen kräver nu ett användarnamn och lösenord för att autentisera till din Internetbox, vilket inte kan överföras säkert från YAML. <br><br>Konfigurera integrationen via användargränssnittet för att ange dina autentiseringsuppgifter (din befintliga värd `{host}` måste anges igen), ta sedan bort posten `{domain}` från din `configuration.yaml`-fil och starta om Home Assistant. | Core-literal match |
| 16955 | 867262172 | `component::swisscom::config::step::user::data_description::username` | The administrator username, normally "admin". | Administratörens användarnamn, normalt "admin". | Core-literal match |
| 16956 | 867262171 | `component::swisscom::config::step::user::data_description::password` | The administrator password printed on the bottom of the box. | Administratörslösenordet som står tryckt på undersidan av boxen. | Core-literal match |
| 16957 | 867262170 | `component::swisscom::config::step::user::data_description::host` | The hostname or IP address of your Swisscom Internet-Box. | Värdnamnet eller IP-adressen för din Swisscom Internet-Box. | Core-literal match |
| 16958 | 867262169 | `component::swisscom::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 16959 | 867262168 | `component::swisscom::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 16960 | 867262167 | `component::swisscom::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 16961 | 867262166 | `component::swisscom::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 16962 | 867262165 | `component::swisscom::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 16963 | 867262164 | `component::swisscom::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16964 | 867262163 | `component::swisscom::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 16965 | 867092431 | `component::helty::exceptions::set_fan_mode_failed::message` | Failed to set the ventilation mode. | Det gick inte att ställa in ventilationsläget. | Core-literal match |
| 16966 | 867092430 | `component::helty::exceptions::reset_filter_failed::message` | Failed to reset the filter. | Det gick inte att återställa filtret. | Core-literal match |
| 16967 | 867092429 | `component::helty::entity::button::reset_filter::name` | Reset filter | Återställ filter | Core-literal match |
| 16968 | 866665500 | `component::powerwall::entity::sensor::operation_mode::state::self_consumption` | Self-consumption | Egenförbrukning | Core-literal match |
| 16969 | 866665499 | `component::powerwall::entity::sensor::operation_mode::state::backup` | Backup | Backup | Core-literal match |
| 16970 | 866665498 | `component::powerwall::entity::sensor::operation_mode::state::autonomous` | Autonomous | Autonom | Core-literal match |
| 16971 | 866665497 | `component::powerwall::entity::sensor::operation_mode::name` | Operation mode | Driftläge | Core-literal match |
| 16972 | 866517239 | `component::edifier_infrared::config::step::user::title` | Set up Edifier IR speaker | Konfigurera Edifier IR-högtalare | Core-literal match |
| 16973 | 866517238 | `component::edifier_infrared::config::step::user::description` | Configure your Edifier speaker for IR control. | Konfigurera din Edifier-högtalare för IR-styrning. | Core-literal match |
| 16974 | 866517237 | `component::edifier_infrared::config::step::user::data_description::model` | Choose your Edifier speaker model from the list. | Välj din Edifier-högtalarmodell från listan. | Core-literal match |
| 16975 | 866517236 | `component::edifier_infrared::config::step::user::data_description::infrared_entity_id` | The infrared emitter entity to use for sending commands. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Shared reference target checked |
| 16976 | 866517235 | `component::edifier_infrared::config::step::user::data::model` | Speaker model | Högtalarmodell | Core-literal match |
| 16977 | 866517234 | `component::edifier_infrared::config::step::user::data::infrared_entity_id` | Infrared emitter | Infraröd sändare | Shared reference target checked |
| 16978 | 866517233 | `component::edifier_infrared::config::abort::no_emitters` | No infrared emitter entities found. Please set up an infrared device first. | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. | Shared reference target checked |
| 16979 | 866517232 | `component::edifier_infrared::config::abort::already_configured` | This Edifier device has already been configured with this infrared emitter. | Denna Edifier-enhet har redan konfigurerats med denna sändare. | Core-literal match |
| 16980 | 866515108 | `component::incomfort::exceptions::invalid_auth::message` | Invalid credentials. | Ogiltiga inloggningsuppgifter. | Shared reference target checked |
| 16981 | 866469078 | `component::opendisplay::exceptions::config_entry_not_found::message` | Config entry not found: `{address}` | Konfigurationsposten hittades inte: `{address}` | Source-path follow-up open |
| 16982 | 866462751 | `component::openevse::entity::binary_sensor::vehicle::name` | Vehicle connected | Fordon anslutet | Core-literal match |
| 16983 | 866462750 | `component::openevse::entity::binary_sensor::using_ethernet::name` | Ethernet connected | Ethernet ansluten | Core-literal match |
| 16984 | 866462749 | `component::openevse::entity::binary_sensor::shaper_active::name` | Shaper active | Shaper aktiv | Core-literal match |
| 16985 | 866462748 | `component::openevse::entity::binary_sensor::mqtt_connected::name` | MQTT connected | MQTT ansluten | Core-literal match |
| 16986 | 866462747 | `component::openevse::entity::binary_sensor::has_limit::name` | Limit active | Begränsning aktiv | Core-literal match |
| 16987 | 866462746 | `component::openevse::entity::binary_sensor::divert_active::name` | Divert active | Vidarekoppling aktiv | Core-literal match |
| 16988 | 866455165 | `component::rabbitair::entity::fan::rabbitair::state_attributes::preset_mode::state::pollen` | Pollen | Pollen | Core-literal match |
| 16989 | 866455164 | `component::rabbitair::entity::fan::rabbitair::state_attributes::preset_mode::state::manual` | Manual | Manuell | Shared reference target checked |
| 16990 | 866455163 | `component::rabbitair::entity::fan::rabbitair::state_attributes::preset_mode::state::auto` | Auto | Auto | Shared reference target checked |
| 16991 | 865665066 | `component::avea::exceptions::device_not_found::message` | Could not find Avea device with address {address}: {reason} | Kunde inte hitta Avea-enheten med adress {address}: {reason} | Core-literal match |
| 16992 | 865535416 | `component::zone::conditions::occupancy_is_not_detected::name` | Zone occupancy is not detected | Ingen närvaro upptäckt i zonen | Core-literal match |
| 16993 | 865535415 | `component::zone::conditions::occupancy_is_not_detected::fields::zone::name` | Zone | Zon | Shared reference target checked |
| 16994 | 865535414 | `component::zone::conditions::occupancy_is_not_detected::fields::zone::description` | The zone to monitor. | Den zon som ska övervakas. | Shared reference target checked |
| 16995 | 865535413 | `component::zone::conditions::occupancy_is_not_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 16996 | 865535412 | `component::zone::conditions::occupancy_is_not_detected::description` | Tests if one or more zones are unoccupied. | Testar om en eller flera zoner är tomma. | Core-literal match |
| 16997 | 865535411 | `component::zone::conditions::occupancy_is_detected::name` | Zone occupancy is detected | Närvaro upptäckt i zonen | Core-literal match |
| 16998 | 865535410 | `component::zone::conditions::occupancy_is_detected::fields::zone::name` | Zone | Zon | Shared reference target checked |
| 16999 | 865535409 | `component::zone::conditions::occupancy_is_detected::fields::zone::description` | The zone to monitor. | Den zon som ska övervakas. | Core-literal match |
| 17000 | 865535408 | `component::zone::conditions::occupancy_is_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 17001 | 865535407 | `component::zone::conditions::occupancy_is_detected::description` | Tests if one or more zones are occupied. | Testar om en eller flera zoner har närvaro. | Core-literal match |
| 17002 | 865532249 | `component::imou::selector::api_url::options::sg` | Singapore (Asia-Pacific) | Singapore (Asien-Stillahavsområdet) | Core-literal match |
| 17003 | 865532248 | `component::imou::selector::api_url::options::na` | North America | Nordamerika | Core-literal match |
| 17004 | 865532247 | `component::imou::selector::api_url::options::eu` | Europe | Europa | Core-literal match |
| 17005 | 865532246 | `component::imou::selector::api_url::options::cn` | China | Kina | Core-literal match |
| 17006 | 865532245 | `component::imou::entity::button::ptz_up::name` | PTZ up | PTZ uppåt | Core-literal match |
| 17007 | 865532244 | `component::imou::entity::button::ptz_right::name` | PTZ right | PTZ höger | Core-literal match |
| 17008 | 865532243 | `component::imou::entity::button::ptz_left::name` | PTZ left | PTZ vänster | Core-literal match |
| 17009 | 865532242 | `component::imou::entity::button::ptz_down::name` | PTZ down | PTZ nedåt | Core-literal match |
| 17010 | 865532241 | `component::imou::entity::button::mute::name` | Mute | Mute | Core-literal match |
| 17011 | 865532240 | `component::imou::config::step::user::title` | Log in to Imou cloud | Logga in på Imou Cloud | Core-literal match |
| 17012 | 865532239 | `component::imou::config::step::user::data_description::app_secret` | The app secret obtained from the Imou cloud platform | Apphemligheten som hämtats från Imous molnplattform | Core-literal match |
| 17013 | 865532238 | `component::imou::config::step::user::data_description::app_id` | The app ID obtained from the Imou cloud platform | Det App-ID som hämtats från Imous molnplattform | Core-literal match |
| 17014 | 865532237 | `component::imou::config::step::user::data_description::api_url` | Select the server region closest to your location | Välj den serverregion som ligger närmast din plats | Core-literal match |
| 17015 | 865532236 | `component::imou::config::step::user::data::app_secret` | App secret | Apphemlighet | Core-literal match |
| 17016 | 865532235 | `component::imou::config::step::user::data::app_id` | App ID | App-ID | Core-literal match |
| 17017 | 865532234 | `component::imou::config::step::user::data::api_url` | Server region | Serverregion | Core-literal match |
| 17018 | 865532233 | `component::imou::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 17019 | 865532232 | `component::imou::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 17020 | 865532231 | `component::imou::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 17021 | 865532230 | `component::imou::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 17022 | 865476537 | `component::zone::conditions::not_in_zone::name` | Is not in zone | Är inte i zonen | Core-literal match |
| 17023 | 865476536 | `component::zone::conditions::not_in_zone::fields::zone::name` | Zone | Zon | Shared reference target checked |
| 17024 | 865476535 | `component::zone::conditions::not_in_zone::fields::zone::description` | The zone to test against. | Den zon som ska testas. | Shared reference target checked |
| 17025 | 865476534 | `component::zone::conditions::not_in_zone::fields::for::name` | For at least | I minst | Shared reference target checked |
| 17026 | 865476533 | `component::zone::conditions::not_in_zone::fields::behavior::name` | Check when | Kontrollera när | Shared reference target checked |
| 17027 | 865476532 | `component::zone::conditions::not_in_zone::description` | Tests if one or more persons or device trackers are not in a zone. | Testar om en eller flera personer eller enhetsspårare inte befinner sig i en zon. | Core-literal match |
| 17028 | 865476531 | `component::zone::conditions::in_zone::name` | Is in zone | Är i zonen | Core-literal match |
| 17029 | 865476530 | `component::zone::conditions::in_zone::fields::zone::name` | Zone | Zon | Shared reference target checked |
| 17030 | 865476529 | `component::zone::conditions::in_zone::fields::zone::description` | The zone to test against. | Den zon som ska testas. | Shared reference target checked |
| 17031 | 865476528 | `component::zone::conditions::in_zone::fields::for::name` | For at least | I minst | Shared reference target checked |
| 17032 | 865476527 | `component::zone::conditions::in_zone::fields::behavior::name` | Check when | Kontrollera när | Shared reference target checked |
| 17033 | 865476526 | `component::zone::conditions::in_zone::description` | Tests if one or more persons or device trackers are in a zone. | Testar om en eller flera personer eller enhetsspårare befinner sig i en zon. | Core-literal match |
| 17034 | 865476525 | `component::zone::common::condition_zone_name` | Zone | Zon | Core-literal match |
| 17035 | 865476524 | `component::zone::common::condition_zone_description` | The zone to test against. | Den zon som ska testas. | Core-literal match |
| 17036 | 865476523 | `component::zone::common::condition_for_name` | For at least | I minst | Core-literal match |
| 17037 | 865476522 | `component::zone::common::condition_behavior_name` | Check when | Kontrollera när | Core-literal match |
| 17038 | 865365162 | `component::template::options::step::device_tracker::data_description::in_zones` | Defines a template that returns a list of zones the device tracker is currently in. The template should return a list of zone entity IDs. If the device tracker is not in any zone, the template should return an empty list. | Definierar en mall som returnerar en lista över zoner som enhetsspåraren för närvarande befinner sig i. Mallen ska returnera en lista över zonens enhets-ID:n. Om enhetsspåraren inte finns i någon zon ska mallen returnera en tom lista. | Shared reference target checked |
| 17039 | 865365161 | `component::template::options::step::device_tracker::data::in_zones` | Zones | Zoner | Shared reference target checked |
| 17040 | 865365160 | `component::template::config::step::device_tracker::data_description::in_zones` | Defines a template that returns a list of zones the device tracker is currently in. The template should return a list of zone entity IDs. If the device tracker is not in any zone, the template should return an empty list. | Definierar en mall som returnerar en lista över zoner som enhetsspåraren för närvarande befinner sig i. Mallen ska returnera en lista över zonens enhets-ID:n. Om enhetsspåraren inte finns i någon zon ska mallen returnera en tom lista. | Core-literal match |

## Sparade referensrättningar

| Lokalise-nyckel-ID | Nyckel | Sparad svenska |
|---:|---|---|
| 866517236 | `component::edifier_infrared::config::step::user::data_description::infrared_entity_id` | Sändarentiteten som ska användas för att skicka infraröda kommandon. |
| 866517234 | `component::edifier_infrared::config::step::user::data::infrared_entity_id` | Infraröd sändare |
| 866517233 | `component::edifier_infrared::config::abort::no_emitters` | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 867580301 | `component::vistapool::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 866469078 | `component::opendisplay::exceptions::config_entry_not_found::message` | Config entry not found: `{address}` |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
