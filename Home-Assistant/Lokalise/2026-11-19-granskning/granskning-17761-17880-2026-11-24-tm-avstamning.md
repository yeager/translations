# Home Assistant Core – historisk avstämning 17761–17880

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 88 direkta källtexter matchar HA Core-källan; 30 referensanvändningar med 12 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 2 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 17761 | 858730013 | `component::vistapool::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 17762 | 858730012 | `component::vistapool::config::error::no_pools` | No pools were found on this account. | Inga pooler hittades på detta konto. | Core-literal match |
| 17763 | 858730011 | `component::vistapool::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 17764 | 858730010 | `component::vistapool::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 17765 | 858730009 | `component::vistapool::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 17766 | 858722343 | `component::vallox::exceptions::failed_to_set_profile_for_duration::message` | Failed to set profile to {profile} for {duration} minutes | Det gick inte att ställa in profilen till {profile} under {duration} minuter | Core-literal match |
| 17767 | 858722342 | `component::vallox::exceptions::failed_to_set_profile::message` | Failed to set profile to {profile} | Det gick inte att ställa in profilen till {profile} | Core-literal match |
| 17768 | 858722341 | `component::vallox::exceptions::failed_to_set_fan_speed_for_profile::message` | Failed to set fan speed to {fan_speed}% for profile {profile} | Det gick inte att ställa in fläkthastigheten till {fan_speed}% för profilen {profile} | Core-literal match |
| 17769 | 858675526 | `component::shelly::selector::ble_scanner_mode::options::auto` | Auto (recommended, saves device battery) | Auto (rekommenderas, sparar enhetens batteri) | Core-literal match |
| 17770 | 858672989 | `component::lichess::entity::sensor::puzzle_rating::name` | Puzzle rating | Pussel-rating | Core-literal match |
| 17771 | 858672988 | `component::lichess::entity::sensor::puzzle_games::unit_of_measurement` | games | spel | Shared reference target checked |
| 17772 | 858672987 | `component::lichess::entity::sensor::puzzle_games::name` | Puzzle games | Pusselspel | Core-literal match |
| 17773 | 858640979 | `component::esphome::selector::bluetooth_scanning_mode::options::passive` | Passive (lowest device battery use, some details may be missing) | Passiv (lägre batteriförbrukning på enheten, vissa detaljer kan saknas) | Core-literal match |
| 17774 | 858640978 | `component::esphome::selector::bluetooth_scanning_mode::options::auto` | Auto (recommended, saves device battery) | Auto (rekommenderas, sparar enhetens batteri) | Core-literal match |
| 17775 | 858640977 | `component::esphome::selector::bluetooth_scanning_mode::options::active` | Active (uses more device battery, fastest updates) | Aktiv (högre batteriförbrukning på enheten, uppdaterar snabbast) | Core-literal match |
| 17776 | 858640976 | `component::esphome::options::step::init::data_description::bluetooth_scanning_mode` | Auto is recommended for most setups. It saves battery on your Bluetooth devices while still catching new devices and updates quickly. | Auto rekommenderas för de flesta konfigurationer. Det sparar batteri på dina Bluetooth-enheter samtidigt som det snabbt fångar upp nya enheter och uppdateringar. | Core-literal match |
| 17777 | 858640975 | `component::esphome::options::step::init::data::bluetooth_scanning_mode` | Bluetooth scanning mode | Skannerläge för Bluetooth | Core-literal match |
| 17778 | 858640678 | `component::bluetooth::selector::mode::options::passive` | Passive (lowest device battery use, some details may be missing) | Passiv (lägst batteriförbrukning på enheten, vissa detaljer kan saknas) | Core-literal match |
| 17779 | 858640677 | `component::bluetooth::selector::mode::options::auto` | Auto (recommended, saves device battery) | Auto (rekommenderas, sparar enhetens batteri) | Core-literal match |
| 17780 | 858640676 | `component::bluetooth::selector::mode::options::active` | Active (uses more device battery, fastest updates) | Aktiv (högre batteriförbrukning på enheten, uppdaterar snabbast) | Core-literal match |
| 17781 | 858640675 | `component::bluetooth::options::step::init::data_description::mode` | Auto is recommended for most setups. It saves battery on your Bluetooth devices while still catching new devices and updates quickly. | Auto rekommenderas för de flesta konfigurationer. Det sparar batteri på dina Bluetooth-enheter samtidigt som det snabbt fångar upp nya enheter och uppdateringar. | Core-literal match |
| 17782 | 858640674 | `component::bluetooth::options::step::init::data::mode` | Scanning mode | Skanningsläge | Core-literal match |
| 17783 | 858636366 | `component::konnected::issues::integration_removed::title` | The Konnected.io (Legacy) integration has been removed | Integrationen med Konnected.io (äldre version) har tagits bort | Core-literal match |
| 17784 | 858636365 | `component::konnected::issues::integration_removed::description` | The Konnected.io (Legacy) integration relied on Konnected's deprecated firmware and has been removed from Home Assistant. Konnected recommends migrating to their ESPHome based firmware and the corresponding Home Assistant integration by following the [migration guide]({kb_page_url}).<br><br>To resolve this issue, migrate your Konnected device(s) to the ESPHome based firmware, then remove any `konnected:` YAML configuration from your `configuration.yaml` file, and remove the (now defunct) integration entries from your Home Assistant setup. [View your existing Konnected.io (Legacy) integration entries]({entries}). | Integrationen med Konnected.io (Legacy) byggde på Konnecteds utfasade firmware och har tagits bort från Home Assistant. Konnected rekommenderar att du migrerar till deras ESPHome-baserade firmware och motsvarande Home Assistant-integration genom att följa [migreringsguiden]({kb_page_url}).<br><br>För att lösa problemet migrerar du dina Konnected-enheter till den ESPHome-baserade firmwareversionen. Ta sedan bort alla `konnected:`-konfigurationer från din `configuration.yaml`-fil och de numera obrukbara integrationsposterna från din Home Assistant-konfiguration. [Visa dina befintliga Konnected.io (Legacy)-integrationsposter]({entries}). | Core-literal match |
| 17785 | 858636364 | `component::arcam_fmj::config::step::reconfigure::description` | Please enter the host name or IP address of device. | Ange värdnamnet eller IP-adressen för enheten. | Shared reference target checked |
| 17786 | 858636363 | `component::arcam_fmj::config::step::reconfigure::data::port` | Port | Port | Shared reference target checked |
| 17787 | 858636362 | `component::arcam_fmj::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 17788 | 858636361 | `component::arcam_fmj::config::abort::unique_id_mismatch` | Please ensure you reconfigure against the same device. | Se till att du konfigurerar om mot samma enhet. | Core-literal match |
| 17789 | 858636360 | `component::arcam_fmj::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 17790 | 858592710 | `component::openrgb::exceptions::cannot_connect::message` | Failed to connect to OpenRGB SDK server {server_address}: {error} | Det gick inte att ansluta till OpenRGB SDK-servern {server_address}: {error} | Core-literal match |
| 17791 | 858583209 | `component::mqtt::config_subentries::device::step::device::sections::mqtt_settings::data_description::message_expiry_interval` | Retention time interval for published message. | Lagringstid för publicerade meddelanden. | Core-literal match |
| 17792 | 858583208 | `component::mqtt::config_subentries::device::step::device::sections::mqtt_settings::data::message_expiry_interval` | Message Expiry Interval | Meddelandets utgångsintervall | Core-literal match |
| 17793 | 858375066 | `component::system_bridge::selector::power_command::options::sleep` | Sleep | Sova | Core-literal match |
| 17794 | 858375065 | `component::system_bridge::selector::power_command::options::shutdown` | Shutdown | Stäng av | Core-literal match |
| 17795 | 858375064 | `component::system_bridge::selector::power_command::options::restart` | Restart | Starta om | Shared reference target checked |
| 17796 | 858375063 | `component::system_bridge::selector::power_command::options::logout` | Logout | Logga ut | Core-literal match |
| 17797 | 858375062 | `component::system_bridge::selector::power_command::options::lock` | Lock | Lås | Core-literal match |
| 17798 | 858375061 | `component::system_bridge::selector::power_command::options::hibernate` | Hibernate | Viloläge | Core-literal match |
| 17799 | 858368182 | `component::homewizard::entity::select::battery_group_mode::state::predictive` | Smart charging | Smart laddning | Core-literal match |
| 17800 | 858244143 | `component::hue::services::activate_scene::sections::scene_customization::name` | Scene customization | Anpassning av scen | Core-literal match |
| 17801 | 858244104 | `component::telegram_bot::services::set_message_reaction::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17802 | 858244103 | `component::telegram_bot::services::send_voice::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17803 | 858244102 | `component::telegram_bot::services::send_video::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17804 | 858244101 | `component::telegram_bot::services::send_sticker::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17805 | 858244100 | `component::telegram_bot::services::send_poll::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17806 | 858244099 | `component::telegram_bot::services::send_photo::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17807 | 858244098 | `component::telegram_bot::services::send_message_draft::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17808 | 858244097 | `component::telegram_bot::services::send_message::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Core-literal match |
| 17809 | 858244096 | `component::telegram_bot::services::send_media_group::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17810 | 858244095 | `component::telegram_bot::services::send_location::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17811 | 858244094 | `component::telegram_bot::services::send_document::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17812 | 858244093 | `component::telegram_bot::services::send_chat_action::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17813 | 858244092 | `component::telegram_bot::services::send_animation::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17814 | 858244091 | `component::telegram_bot::services::leave_chat::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17815 | 858244090 | `component::telegram_bot::services::edit_replymarkup::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17816 | 858244089 | `component::telegram_bot::services::edit_message_media::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17817 | 858244088 | `component::telegram_bot::services::edit_message::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17818 | 858244087 | `component::telegram_bot::services::edit_caption::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17819 | 858244086 | `component::telegram_bot::services::delete_message::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17820 | 858166185 | `component::alexa_devices::exceptions::invalid_auth::message` | Invalid authentication credentials: {error} | Ogiltiga autentiseringsuppgifter: {error} | Core-literal match |
| 17821 | 858165522 | `component::uptimerobot::exceptions::api_switch_exception::message` | Could not turn on/off monitoring: {error} | Det gick inte att slå på/av övervakningen: {error} | Core-literal match |
| 17822 | 858165521 | `component::uptimerobot::exceptions::api_key_wrong_type::message` | Wrong API key type detected, use the 'main' API key | Fel API-nyckeltyp upptäckt, använd "huvud-API-nyckeln" | Core-literal match |
| 17823 | 858165520 | `component::uptimerobot::exceptions::api_generic_exception::message` | API error: {error} | API-fel: {error} | Core-literal match |
| 17824 | 858165519 | `component::uptimerobot::exceptions::api_authentication_exception::message` | API authentication failed, please check your API key | API-autentisering misslyckades, kontrollera din API-nyckel | Core-literal match |
| 17825 | 858114404 | `component::system_bridge::entity::sensor::space_used::name` | {partition} space used | {partition} utnyttjat utrymme | Core-literal match |
| 17826 | 858114403 | `component::system_bridge::entity::sensor::processes_load_cpu::name` | Load CPU {cpu_id} | CPU-belastning {cpu_id} | Core-literal match |
| 17827 | 858114402 | `component::system_bridge::entity::sensor::memory_used_percentage::name` | Memory usage | Använt minne (%) | Core-literal match |
| 17828 | 858114401 | `component::system_bridge::entity::sensor::gpu_usage_percentage::name` | {gpu_name} usage % | {gpu_name} användningsgrad (%) | Core-literal match |
| 17829 | 858114400 | `component::system_bridge::entity::sensor::gpu_temperature::name` | {gpu_name} temperature | {gpu_name} temperatur | Core-literal match |
| 17830 | 858114399 | `component::system_bridge::entity::sensor::gpu_power_usage::name` | {gpu_name} power usage | {gpu_name} strömförbrukning | Core-literal match |
| 17831 | 858114398 | `component::system_bridge::entity::sensor::gpu_memory_used_percentage::name` | {gpu_name} memory usage | {gpu_name} minne använt % | Core-literal match |
| 17832 | 858114397 | `component::system_bridge::entity::sensor::gpu_memory_used::name` | {gpu_name} memory used | {gpu_name} minne använt | Core-literal match |
| 17833 | 858114396 | `component::system_bridge::entity::sensor::gpu_memory_free::name` | {gpu_name} memory free | {gpu_name} minne ledigt | Core-literal match |
| 17834 | 858114395 | `component::system_bridge::entity::sensor::gpu_memory_clock_speed::name` | {gpu_name} memory clock speed | {gpu_name} minnesklockhastighet | Core-literal match |
| 17835 | 858114394 | `component::system_bridge::entity::sensor::gpu_fan_speed::name` | {gpu_name} fan speed | {gpu_name} fläkthastighet | Core-literal match |
| 17836 | 858114393 | `component::system_bridge::entity::sensor::gpu_core_clock_speed::name` | {gpu_name} clock speed | {gpu_name} klockhastighet | Core-literal match |
| 17837 | 858114392 | `component::system_bridge::entity::sensor::display_resolution_y::name` | Display {display_id} resolution y | Skärm {display_id} upplösning y | Core-literal match |
| 17838 | 858114391 | `component::system_bridge::entity::sensor::display_resolution_x::name` | Display {display_id} resolution x | Skärm {display_id} upplösning x | Core-literal match |
| 17839 | 858114390 | `component::system_bridge::entity::sensor::display_refresh_rate::name` | Display {display_id} refresh rate | Skärm {display_id} uppdateringsfrekvens | Core-literal match |
| 17840 | 858114389 | `component::system_bridge::entity::sensor::cpu_power_core::name` | CPU core {cpu_id} power | CPU-kärna {cpu_id} effekt | Core-literal match |
| 17841 | 858095169 | `component::webostv::exceptions::device_not_valid::message` | Device {device_id} is not a valid LG webOS TV device. | Enheten {device_id} är inte en giltig LG webOS TV-enhet. | Core-literal match |
| 17842 | 858095168 | `component::webostv::exceptions::device_config_entry_not_loaded::message` | The LG webOS TV integration for device {device_id} is not loaded. | LG webOS TV-integration för enhet {device_id} har inte laddats in. | Core-literal match |
| 17843 | 858095167 | `component::webostv::exceptions::auth_failed::message` | Pairing for {device} failed, make sure to accept the pairing request on your TV. | Parkopplingen för {device} misslyckades. Se till att acceptera parkopplingsbegäran på din TV. | Core-literal match |
| 17844 | 857979605 | `component::portainer::services::recreate_container::name` | Recreate container | Återskapa containern | Core-literal match |
| 17845 | 857979604 | `component::portainer::services::recreate_container::fields::timeout::name` | Timeout | Tidsgräns | Core-literal match |
| 17846 | 857979603 | `component::portainer::services::recreate_container::fields::timeout::description` | The time to wait for the container to stop before killing it. If not provided, a default of 5 minutes will be used. | Den tid man ska vänta på att containern ska stanna innan den avslutas. Om inget värde anges används standardvärdet 5 minuter. | Core-literal match |
| 17847 | 857979602 | `component::portainer::services::recreate_container::fields::pull_image::name` | Pull image | Hämta avbildning | Core-literal match |
| 17848 | 857979601 | `component::portainer::services::recreate_container::fields::pull_image::description` | Whether to pull the image before recreating the container. This can be used to update the container to the latest version of the image. | Om bilden ska hämtas innan Containern återskapas. Detta kan användas för att uppdatera Containern till den senaste versionen av bilden. | Core-literal match |
| 17849 | 857979600 | `component::portainer::services::recreate_container::fields::container_device_id::name` | Container | Container | Core-literal match |
| 17850 | 857979599 | `component::portainer::services::recreate_container::fields::container_device_id::description` | The container to recreate. | Container som ska återskapas. | Core-literal match |
| 17851 | 857979598 | `component::portainer::services::recreate_container::description` | Recreates a container on a Portainer endpoint. This is more disruptive than a restart as the container will be stopped, removed, and then re-created with the same configuration. Use with caution. | Skapar om en container på en Portainer-ändpunkt. Detta medför större avbrott än en omstart, eftersom containern stoppas, tas bort och sedan skapas om med samma konfiguration. Använd med försiktighet. | Core-literal match |
| 17852 | 857959055 | `component::pooldose::exceptions::update_timeout::message` | Timeout fetching data from PoolDose device | Timeout vid hämtning av data från PoolDose-enheten | Core-literal match |
| 17853 | 857959054 | `component::pooldose::exceptions::update_connect_failed::message` | Failed to connect to PoolDose device while fetching data | Det gick inte att ansluta till PoolDose-enheten vid hämtning av data | Core-literal match |
| 17854 | 857959053 | `component::pooldose::exceptions::no_data_received::message` | No data received from API | Ingen data mottagen från API:et | Core-literal match |
| 17855 | 857959052 | `component::pooldose::exceptions::connect_timeout::message` | Timeout connecting to PoolDose device | Tidsgränsen överskreds vid anslutning till PoolDose-enheten. | Core-literal match |
| 17856 | 857959051 | `component::pooldose::exceptions::connect_failed::message` | Failed to connect to PoolDose device | Det gick inte att ansluta till PoolDose-enheten | Core-literal match |
| 17857 | 857959050 | `component::pooldose::exceptions::client_init_failed::message` | Failed to initialize PoolDose client: {status} | Det gick inte att initiera PoolDose-klienten: {status} | Core-literal match |
| 17858 | 857959049 | `component::pooldose::exceptions::api_status_error::message` | API returned status code: {status} | API returnerade statuskod: {status} | Core-literal match |
| 17859 | 857953572 | `component::smhi::config::step::user::data_description::location` | Choose a location in Sweden. | Välj en plats i Sverige. | Shared reference target checked |
| 17860 | 857953571 | `component::smhi::config::step::user::data::location` | Location | Plats | Shared reference target checked |
| 17861 | 857953570 | `component::smhi::config::step::reconfigure::data_description::location` | Choose a location in Sweden. | Välj en plats i Sverige. | Core-literal match |
| 17862 | 857953569 | `component::smhi::config::step::reconfigure::data::location` | Location | Plats | Shared reference target checked |
| 17863 | 857952113 | `component::samsungtv::exceptions::invalid_device::message` | Device with ID {device_id} is invalid or not found. | Enhet med ID {device_id} är ogiltig eller hittades inte. | Core-literal match |
| 17864 | 857952112 | `component::downloader::config::step::user::data_description::download_dir` | The directory where downloaded files will be stored. This can be an absolute path or a path relative to the Home Assistant configuration directory. | Den katalog där nedladdade filer ska sparas. Det kan vara en absolut sökväg eller en relativ sökväg i förhållande till Home Assistants konfigurationskatalog. | Core-literal match |
| 17865 | 857952111 | `component::downloader::config::step::user::data::download_dir` | Download directory | Sökväg för nedladdade filer | Core-literal match |
| 17866 | 857944571 | `component::ecobee::entity::number::fan_min_on_time::name` | Fan minimum on time | Fläkt minsta tillslagstid | Core-literal match |
| 17867 | 857944175 | `component::system_bridge::exceptions::send_message_failed::message` | Failed to send message to {title} ({host}) due to a connection error | Det gick inte att skicka meddelandet till {title} ({host}) på grund av ett anslutningsfel | Core-literal match |
| 17868 | 857938614 | `component::simplefin::config::step::user::data::access_url` | Setup token | Installationstoken | Core-literal match |
| 17869 | 857809320 | `component::lunatone::exceptions::missing_device_info::message` | Unable to read device information. Please verify the device's network connection. | Det gick inte att läsa enhetsinformationen. Kontrollera enhetens nätverksanslutning. | Core-literal match |
| 17870 | 857626889 | `component::homematicip_cloud::entity::binary_sensor::cloud_connection::name` | Cloud connection | Molnanslutning | Core-literal match |
| 17871 | 857436864 | `component::opendisplay::services::upload_image::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Core-literal match |
| 17872 | 857434863 | `component::incomfort::exceptions::update_failed_with_error_message::message` | Update failed, got {error}. | Uppdateringen misslyckades, fick {error}. | Core-literal match |
| 17873 | 857434862 | `component::incomfort::exceptions::incorrect_credentials::message` | Incorrect credentials. | Felaktiga inloggningsuppgifter. | Source-path follow-up open |
| 17874 | 857418624 | `component::music_assistant::services::search::sections::search_options::name` | Search options | Sökalternativ | Core-literal match |
| 17875 | 857418623 | `component::music_assistant::services::get_library::sections::pagination::name` | Pagination | Sidnumrering | Core-literal match |
| 17876 | 857418354 | `component::mqtt::services::publish::sections::publish_options::name` | Publish options | Publiceringsalternativ | Core-literal match |
| 17877 | 857357099 | `component::unifiprotect::exceptions::unknown_camera_id::message` | Unknown camera ID: {camera_id} | Okänt kamera-ID: {camera_id} | Core-literal match |
| 17878 | 857357098 | `component::unifiprotect::exceptions::unexpected_identifier::message` | Unexpected identifier: {identifier} | Oväntad identifierare: {identifier} | Core-literal match |
| 17879 | 857357097 | `component::unifiprotect::exceptions::event_ongoing::message` | Event is still ongoing | Event pågår fortfarande | Core-literal match |
| 17880 | 857357096 | `component::unifiprotect::exceptions::entry_auth_failed::message` | Authentication failed, please reauthenticate | Autentisering misslyckades, autentisera igen | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 858636360 | `component::arcam_fmj::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 857434862 | `component::incomfort::exceptions::incorrect_credentials::message` | Incorrect credentials. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
