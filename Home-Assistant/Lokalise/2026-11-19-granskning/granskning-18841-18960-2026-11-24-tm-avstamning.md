# Home Assistant Core – historisk avstämning 18841–18960

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 68 direkta källtexter matchar HA Core-källan; 38 referensanvändningar med 27 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 14 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 18841 | 847314432 | `component::mqtt::issues::protocol_5_migration::fix_flow::step::confirm::title` | MQTT protocol change required | Ändring av MQTT-protokollet krävs | Source-path follow-up open |
| 18842 | 847314431 | `component::mqtt::issues::protocol_5_migration::fix_flow::step::confirm::description` | Home Assistant needs to migrate to MQTT protocol version 5. The currently configured protocol version for broker {broker} is {protocol}. This protocol version is deprecated, and support for it will be removed.<br><br>Submitting this form will attempt to migrate your MQTT broker configuration to use protocol version 5 to fix this issue. If the broker cannot be reached using MQTT protocol version 5, for example because it does not support it, the migration will be aborted. | Home Assistant måste uppgraderas till MQTT-protokollversion 5. Den protokollversion som för närvarande är konfigurerad för mäklaren {broker} är {protocol}. Denna protokollversion är utfasad och stödet för den kommer att tas bort.<br><br>När du skickar in detta formulär kommer systemet att försöka migrera din MQTT-mäklarkonfiguration till protokollversion 5 för att åtgärda detta problem. Om mäklaren inte kan nås med MQTT-protokollversion 5, till exempel för att den inte stöder den, kommer migreringen att avbrytas. | Source-path follow-up open |
| 18843 | 847314430 | `component::mqtt::issues::protocol_5_migration::fix_flow::abort::mqtt_broker_migration_to_v5_failed` | Migrating the broker ({broker}) protocol version from {protocol} to 5 failed, and the migration has been aborted.<br><br>Your broker may not support MQTT protocol version 5.<br><br>Please [reconfigure your MQTT broker settings]({url_mqtt_broker_configuration}) or upgrade your broker to support MQTT protocol version 5 to fix this issue. | Migreringen av mäklarens ({broker}) protokollversion från {protocol} till 5 misslyckades, och migreringen har avbrutits.<br><br>Din mäklare stöder kanske inte MQTT-protokollversion 5.<br><br>[Konfigurera om inställningarna för din MQTT-mäklare]({url_mqtt_broker_configuration}) eller uppgradera din mäklare så att den stöder MQTT-protokollversion 5 för att lösa problemet. | Source-path follow-up open |
| 18844 | 846991894 | `component::media_player::triggers::unmuted::name` | Media player unmuted | Mediaspelare har avtystats | Core-literal match |
| 18845 | 846991893 | `component::media_player::triggers::unmuted::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18846 | 846991892 | `component::media_player::triggers::unmuted::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 18847 | 846991891 | `component::media_player::triggers::unmuted::description` | Triggers when one or more media players are unmuted. | Utlöses när en eller flera mediespelare avtystas. | Core-literal match |
| 18848 | 846975354 | `component::volvo::entity::sensor::charging_power_status::state::initialization` | Initialization | Initialisering | Core-literal match |
| 18849 | 846919987 | `component::media_player::triggers::muted::name` | Media player muted | Mediaspelare har tystats | Core-literal match |
| 18850 | 846919986 | `component::media_player::triggers::muted::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18851 | 846919985 | `component::media_player::triggers::muted::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 18852 | 846919984 | `component::media_player::triggers::muted::description` | Triggers when one or more media players are muted. | Utlöses när en eller flera mediaspelare tystas. | Core-literal match |
| 18853 | 846905534 | `component::airnow::config::step::user::data_description::radius` | The radius in miles around your location to search for reporting stations. | Radien i engelska mil runt din plats för att söka efter rapporteringsstationer. | Source-path follow-up open |
| 18854 | 846905533 | `component::airnow::config::step::user::data_description::longitude` | The longitude of your location. | Longitud för din position. | Source-path follow-up open |
| 18855 | 846905532 | `component::airnow::config::step::user::data_description::latitude` | The latitude of your location. | Latitud för din position. | Source-path follow-up open |
| 18856 | 846905531 | `component::airnow::config::step::user::data_description::api_key` | To generate an API key, go to {api_key_url}. | Gå till {api_key_url} för att skapa en API-nyckel. | Core-literal match |
| 18857 | 846845399 | `component::mitsubishi_comfort::exceptions::update_failed::message` | {device_name} returned no data | {device_name} returnerade inga data | Core-literal match |
| 18858 | 846845398 | `component::mitsubishi_comfort::exceptions::no_devices::message` | No devices were found in your Mitsubishi Comfort account | Inga enheter hittades i ditt Mitsubishi Comfort-konto | Core-literal match |
| 18859 | 846845397 | `component::mitsubishi_comfort::exceptions::communication_error::message` | Error communicating with {device_name} | Fel vid kommunikation med {device_name} | Core-literal match |
| 18860 | 846845396 | `component::mitsubishi_comfort::config::step::user::data_description::username` | The email address for your Kumo Cloud account. | E-postadressen för ditt Kumo Cloud-konto. | Core-literal match |
| 18861 | 846845395 | `component::mitsubishi_comfort::config::step::user::data_description::password` | The password for your Kumo Cloud account. | Lösenordet för ditt Kumo Cloud-konto. | Core-literal match |
| 18862 | 846845394 | `component::mitsubishi_comfort::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 18863 | 846845393 | `component::mitsubishi_comfort::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 18864 | 846845392 | `component::mitsubishi_comfort::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 18865 | 846845391 | `component::mitsubishi_comfort::config::error::no_devices` | No devices were found on this account | Inga enheter hittades på det här kontot | Core-literal match |
| 18866 | 846845390 | `component::mitsubishi_comfort::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 18867 | 846845389 | `component::mitsubishi_comfort::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18868 | 846845388 | `component::mitsubishi_comfort::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 18869 | 846841868 | `component::ptdevices::exceptions::invalid_access_token::message` | Invalid access token: {error} | Ogiltig åtkomsttoken: {error} | Core-literal match |
| 18870 | 846841867 | `component::ptdevices::exceptions::cannot_connect::message` | Failed to connect: {error} | Misslyckades med att ansluta: {error} | Core-literal match |
| 18871 | 846841866 | `component::ptdevices::entity::sensor::wifi_signal::name` | Wi-Fi signal strength | Wi-Fi-signalstyrka | Core-literal match |
| 18872 | 846841865 | `component::ptdevices::entity::sensor::volume_level::name` | Level volume | Nivå volym | Core-literal match |
| 18873 | 846841864 | `component::ptdevices::entity::sensor::tx_signal::name` | LoRa signal strength | LoRa-signalstyrka | Core-literal match |
| 18874 | 846841863 | `component::ptdevices::entity::sensor::status::state::working` | Working | Fungerar | Core-literal match |
| 18875 | 846841862 | `component::ptdevices::entity::sensor::status::state::transmitter_not_reporting` | Transmitter not reporting | Sändaren rapporterar inte | Core-literal match |
| 18876 | 846841861 | `component::ptdevices::entity::sensor::status::state::press_transmitter_connect_button` | Press transmitter connect button | Tryck på sändarens anslutningsknapp | Core-literal match |
| 18877 | 846841860 | `component::ptdevices::entity::sensor::status::state::power_internet_out_or_receiver_not_working` | Power or internet out or receiver not working | Strömavbrott, internetavbrott eller mottagaren fungerar inte | Core-literal match |
| 18878 | 846841859 | `component::ptdevices::entity::sensor::status::state::not_connected_yet` | Not connected yet | Inte ansluten än | Core-literal match |
| 18879 | 846841858 | `component::ptdevices::entity::sensor::status::state::not_connected` | Not connected | Inte ansluten | Core-literal match |
| 18880 | 846841857 | `component::ptdevices::entity::sensor::status::name` | Status | Status | Core-literal match |
| 18881 | 846841856 | `component::ptdevices::entity::sensor::probe_temperature::name` | Probe temperature | Sondtemperatur | Core-literal match |
| 18882 | 846841855 | `component::ptdevices::entity::sensor::percent_level::name` | Level percent | Nivå procent | Core-literal match |
| 18883 | 846841854 | `component::ptdevices::entity::sensor::depth_level::name` | Level depth | Nivå djup | Core-literal match |
| 18884 | 846841853 | `component::ptdevices::entity::sensor::battery_voltage::name` | Battery voltage | Batterispänning | Core-literal match |
| 18885 | 846841852 | `component::ptdevices::config::step::user::description` | Enter the API token for your PTDevices account | Ange API-token för ditt PTDevices-konto | Core-literal match |
| 18886 | 846841851 | `component::ptdevices::config::step::user::data_description::api_token` | The API token for your PTDevices account. | API-token för ditt PTDevices-konto. | Core-literal match |
| 18887 | 846841850 | `component::ptdevices::config::step::user::data::api_token` | API token | API-token | Shared reference target checked |
| 18888 | 846841849 | `component::ptdevices::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 18889 | 846841848 | `component::ptdevices::config::error::no_devices_found` | No devices are registered to your PTDevices account. | Inga enheter är registrerade på ditt PTDevices-konto. | Core-literal match |
| 18890 | 846841847 | `component::ptdevices::config::error::invalid_access_token` | Invalid access token | Ogiltig åtkomsttoken | Shared reference target checked |
| 18891 | 846841846 | `component::ptdevices::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18892 | 846841845 | `component::ptdevices::config::abort::invalid_access_token` | Invalid access token | Ogiltig åtkomsttoken | Shared reference target checked |
| 18893 | 846841844 | `component::ptdevices::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 18894 | 846835275 | `component::nordpool::entity::binary_sensor::tomorrow_price_available::name` | Tomorrow price available | Morgondagens pris tillgängligt | Core-literal match |
| 18895 | 846835233 | `component::portainer::system_health::info::can_reach_server` | Reach Portainer server | Anslut till Portainer-server | Core-literal match |
| 18896 | 846835179 | `component::command_line::issues::platform_yaml_not_supported::title` | Platform YAML is not supported in Command Line | Plattforms-YAML stöds inte i Command Line | Source-path follow-up open |
| 18897 | 846835178 | `component::command_line::issues::platform_yaml_not_supported::description` | Platform YAML setup is not supported.<br>Change from configuring it using the `{platform}:` key to using the `command_line:` key directly in configuration.yaml and restart Home Assistant to resolve the issue.<br>To see the detailed documentation, select Learn more. | YAML-konfigurationen för plattformen stöds inte. Ändra från att konfigurera den med hjälp av nyckeln `{platform}:` till att använda nyckeln `command_line:` direkt i configuration.yaml och starta om Home Assistant för att lösa problemet. För att se den detaljerade dokumentationen, välj Läs mer. | Source-path follow-up open |
| 18898 | 846833873 | `component::overkiz::services::set_cover_position_and_tilt::name` | Set cover position and tilt | Ställ in skyddets position och lutning | Core-literal match |
| 18899 | 846833872 | `component::overkiz::services::set_cover_position_and_tilt::fields::tilt_position::name` | Tilt position | Lutningsläge | Core-literal match |
| 18900 | 846833871 | `component::overkiz::services::set_cover_position_and_tilt::fields::tilt_position::description` | Target tilt position. 0 means closed, 100 means fully open. | Lutningsposition. 0 betyder stängd, 100 betyder helt öppen. | Core-literal match |
| 18901 | 846833870 | `component::overkiz::services::set_cover_position_and_tilt::fields::position::name` | Position | Position | Core-literal match |
| 18902 | 846833869 | `component::overkiz::services::set_cover_position_and_tilt::fields::position::description` | Target vertical position. 0 means closed, 100 means fully open. | Mål för vertikal position. 0 betyder stängt, 100 betyder helt öppet. | Core-literal match |
| 18903 | 846833868 | `component::overkiz::services::set_cover_position_and_tilt::description` | Moves the cover and tilt to the target position simultaneously, preventing the motor from stopping between movements. | Förflyttar enheten och lutar det samtidigt till målpositionen, vilket förhindrar att motorn stannar mellan rörelserna. | Core-literal match |
| 18904 | 846833867 | `component::overkiz::exceptions::unsupported_set_position_and_tilt::message` | This device does not support setting position and tilt simultaneously. | Den här enheten stöder inte samtidig inställning av position och lutning. | Core-literal match |
| 18905 | 846833427 | `component::onedrive::services::delete::name` | Delete files | Ta bort filer | Core-literal match |
| 18906 | 846833426 | `component::onedrive::services::delete::fields::destination_path::name` | Destination paths | Destinationssökvägar | Core-literal match |
| 18907 | 846833425 | `component::onedrive::services::delete::fields::destination_path::example` | ["photos/snapshots/image.jpg", "photos/snapshots/image2.jpg"] | ["photos/snapshots/image.jpg", "photos/snapshots/image2.jpg"] | Core-literal match |
| 18908 | 846833424 | `component::onedrive::services::delete::fields::destination_path::description` | One or more paths to files inside the OneDrive app folder (Apps/Home Assistant) to delete. | En eller flera sökvägar till filer i OneDrive-appmappen (Appar/Home Assistant) som ska raderas. | Core-literal match |
| 18909 | 846833423 | `component::onedrive::services::delete::fields::config_entry_id::name` | Config entry ID | ID för konfigurationspost | Core-literal match |
| 18910 | 846833422 | `component::onedrive::services::delete::fields::config_entry_id::description` | The config entry representing the OneDrive you want to delete from. | Konfigurationsposten som representerar den OneDrive som du vill ta bort från. | Core-literal match |
| 18911 | 846833421 | `component::onedrive::services::delete::description` | Deletes one or more files from OneDrive. | Tar bort en eller flera filer från OneDrive. | Core-literal match |
| 18912 | 846833420 | `component::onedrive::exceptions::invalid_destination_path::message` | Invalid destination path `{destination_path}`: must be non-empty, must not contain `:` or `..` path segments | Ogiltig destinationssökväg `{destination_path}`: får inte vara blank, får inte innehålla `:` eller `..` i sökvägssegment | Core-literal match |
| 18913 | 846833419 | `component::onedrive::exceptions::delete_error::message` | Failed to delete from OneDrive: {paths} | Misslyckades med att ta bort från OneDrive: {paths} | Core-literal match |
| 18914 | 846833418 | `component::onedrive::exceptions::connection_error::message` | Failed to connect to OneDrive. | Misslyckades med att ansluta till OneDrive. | Shared reference target checked |
| 18915 | 846831327 | `component::nordpool::config::error::no_areas` | No area(s) selected | Inget område valt | Core-literal match |
| 18916 | 846794199 | `component::proxmoxve::exceptions::no_vmlxc_found::message` | No LXC or VM were found on the Proxmox VE server. | Inga LXC eller VM hittades på Proxmox VE-servern. | Core-literal match |
| 18917 | 846794198 | `component::proxmoxve::config::error::no_vmlxc_found` | No LXC or VM were found on the Proxmox VE server. | Inga LXC eller VM hittades på Proxmox VE-servern. | Core-literal match |
| 18918 | 846794197 | `component::proxmoxve::config::error::api_error_no_details` | An error occurred while communicating with the Proxmox VE instance. | Ett fel inträffade under kommunikationen med Proxmox VE-instansen. | Core-literal match |
| 18919 | 846758601 | `component::dnsip::options::step::init::data_description::resolver_ipv6` | Resolver used for the IPv6 lookup. | Resolver som används för IPv6-uppslagning. | Shared reference target checked |
| 18920 | 846758600 | `component::dnsip::options::step::init::data_description::resolver` | Resolver used for the IPv4 lookup. | Resolver som används för IPv4-uppslagning. | Shared reference target checked |
| 18921 | 846758599 | `component::dnsip::options::step::init::data_description::port_ipv6` | Port used for the IPv6 lookup. | Port som används för IPv6-uppslagning. | Shared reference target checked |
| 18922 | 846758598 | `component::dnsip::options::step::init::data_description::port` | Port used for the IPv4 lookup. | Port som används för IPv4-uppslagning. | Shared reference target checked |
| 18923 | 846758597 | `component::dnsip::config::step::user::data_description::resolver_ipv6` | Resolver used for the IPv6 lookup. | Namnserver som används för IPv6-uppslagning. | Source-path follow-up open |
| 18924 | 846758596 | `component::dnsip::config::step::user::data_description::resolver` | Resolver used for the IPv4 lookup. | Namnserver som används för IPv4-uppslagning. | Source-path follow-up open |
| 18925 | 846758595 | `component::dnsip::config::step::user::data_description::port_ipv6` | Port used for the IPv6 lookup. | Port som används för IPv6-uppslagning. | Source-path follow-up open |
| 18926 | 846758594 | `component::dnsip::config::step::user::data_description::port` | Port used for the IPv4 lookup. | Port som används för IPv4-uppslagning. | Source-path follow-up open |
| 18927 | 846758593 | `component::dnsip::config::step::user::data_description::hostname` | The hostname for which to perform the DNS query. | Det värdnamn som DNS-frågan ska ställas för. | Core-literal match |
| 18928 | 846724854 | `component::nest::entity::event::chime::state_attributes::event_type::state::ring` | Ring | Signal | Shared reference target checked |
| 18929 | 846721567 | `component::actron_air::config::step::reconfigure_confirm::title` | Reconfigure Actron Air | Konfigurera om Actron Air | Core-literal match |
| 18930 | 846721566 | `component::actron_air::config::step::reconfigure_confirm::description` | Reconfigure your Actron Air account. You will be prompted to log in again. Note: you must use the same account that was originally configured. | Konfigurera om ditt Actron Air-konto. Du kommer att uppmanas att logga in igen. Observera: du måste använda samma konto som ursprungligen konfigurerades. | Core-literal match |
| 18931 | 846721565 | `component::actron_air::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 18932 | 846382239 | `component::openevse::config::step::reauth_confirm::description` | The credentials for your OpenEVSE charger at {host} are no longer valid. Please enter your current username and password. | Inloggningsuppgifterna för din OpenEVSE-laddare på {host} är inte längre giltiga. Ange ditt nuvarande användarnamn och lösenord. | Core-literal match |
| 18933 | 846382238 | `component::openevse::config::step::reauth_confirm::data_description::username` | The username to access your OpenEVSE charger | Användarnamnet för att komma åt din OpenEVSE-laddare | Shared reference target checked |
| 18934 | 846382237 | `component::openevse::config::step::reauth_confirm::data_description::password` | The password to access your OpenEVSE charger | Lösenordet för att komma åt din OpenEVSE-laddare | Shared reference target checked |
| 18935 | 846382236 | `component::openevse::config::step::reauth_confirm::data::username` | Username | Användarnamn | Shared reference target checked |
| 18936 | 846382235 | `component::openevse::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 18937 | 846382234 | `component::openevse::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 18938 | 846242506 | `component::openai_conversation::selector::reasoning_summary::options::concise` | Concise | Kortfattad | Core-literal match |
| 18939 | 846219631 | `component::ohme::entity::number::state_of_charge_input::name` | State of charge input | Laddningsstatusingång | Core-literal match |
| 18940 | 846175453 | `component::nobo_hub::config::error::cannot_connect_ip` | Failed to connect - check IP address | Misslyckades med att ansluta - kontrollera IP-adressen | Core-literal match |
| 18941 | 846134696 | `component::uptime_kuma::entity::sensor::type::state::oracledb` | Oracle Database | Oracle-databas | Core-literal match |
| 18942 | 846035965 | `component::unifiprotect::entity::select::nvr_arm_profile::name` | Alarm profile | Larmprofil | Core-literal match |
| 18943 | 846020173 | `component::nobo_hub::exceptions::cannot_connect::message` | Unable to connect to Nobø Ecohub with serial {serial} at {ip}; will retry. If the hub is on a different network from Home Assistant and has changed IP address, reconfigure the integration with the new IP address. | Det går inte att ansluta till Nobø Ecohub med serienumret {serial} på {ip}. Ett nytt försök kommer att göras. Om hubben befinner sig i ett annat nätverk än Home Assistant och har bytt IP-adress ska du konfigurera om integrationen med den nya IP-adressen. | Core-literal match |
| 18944 | 846005385 | `component::water_heater::conditions::is_target_temperature::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18945 | 846005384 | `component::water_heater::conditions::is_operation_mode::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18946 | 846005383 | `component::water_heater::conditions::is_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18947 | 846005382 | `component::valve::conditions::is_open::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18948 | 846005381 | `component::valve::conditions::is_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18949 | 846005380 | `component::valve::common::condition_for_name` | For at least | I minst | Core-literal match |
| 18950 | 846005379 | `component::todo::conditions::incomplete::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18951 | 846005378 | `component::text::conditions::is_equal_to::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18952 | 846005377 | `component::text::common::condition_for_name` | For at least | I minst | Core-literal match |
| 18953 | 846005376 | `component::temperature::conditions::is_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18954 | 846005375 | `component::temperature::common::condition_for_name` | For at least | I minst | Core-literal match |
| 18955 | 846005374 | `component::select::conditions::is_option_selected::fields::for::name` | For at least | I minst | Core-literal match |
| 18956 | 846005373 | `component::power::conditions::is_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18957 | 846005372 | `component::power::common::condition_for_name` | For at least | I minst | Core-literal match |
| 18958 | 846005371 | `component::moisture::conditions::is_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18959 | 846005370 | `component::media_player::conditions::is_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18960 | 846005369 | `component::media_player::conditions::is_not_playing::fields::for::name` | For at least | I minst | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 847314432 | `component::mqtt::issues::protocol_5_migration::fix_flow::step::confirm::title` | MQTT protocol change required |
| 847314431 | `component::mqtt::issues::protocol_5_migration::fix_flow::step::confirm::description` | Home Assistant needs to migrate to MQTT protocol version 5. The currently configured protocol version for broker {broker} is {protocol}. This protocol version is deprecated, and support for it will be removed.

Submitting this form will attempt to migrate your MQTT broker configuration to use protocol version 5 to fix this issue. If the broker cannot be reached using MQTT protocol version 5, for example because it does not support it, the migration will be aborted. |
| 847314430 | `component::mqtt::issues::protocol_5_migration::fix_flow::abort::mqtt_broker_migration_to_v5_failed` | Migrating the broker ({broker}) protocol version from {protocol} to 5 failed, and the migration has been aborted.

Your broker may not support MQTT protocol version 5.

Please [reconfigure your MQTT broker settings]({url_mqtt_broker_configuration}) or upgrade your broker to support MQTT protocol version 5 to fix this issue. |
| 846905534 | `component::airnow::config::step::user::data_description::radius` | The radius in miles around your location to search for reporting stations. |
| 846905533 | `component::airnow::config::step::user::data_description::longitude` | The longitude of your location. |
| 846905532 | `component::airnow::config::step::user::data_description::latitude` | The latitude of your location. |
| 846835179 | `component::command_line::issues::platform_yaml_not_supported::title` | Platform YAML is not supported in Command Line |
| 846835178 | `component::command_line::issues::platform_yaml_not_supported::description` | Platform YAML setup is not supported.
Change from configuring it using the `{platform}:` key to using the `command_line:` key directly in configuration.yaml and restart Home Assistant to resolve the issue.
To see the detailed documentation, select Learn more. |
| 846758597 | `component::dnsip::config::step::user::data_description::resolver_ipv6` | Resolver used for the IPv6 lookup. |
| 846758596 | `component::dnsip::config::step::user::data_description::resolver` | Resolver used for the IPv4 lookup. |
| 846758595 | `component::dnsip::config::step::user::data_description::port_ipv6` | Port used for the IPv6 lookup. |
| 846758594 | `component::dnsip::config::step::user::data_description::port` | Port used for the IPv4 lookup. |
| 846721565 | `component::actron_air::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 846382234 | `component::openevse::config::abort::reauth_successful` | Re-authentication was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
