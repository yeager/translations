# Home Assistant Core – historisk avstämning 16681–16800

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120 nycklar avstämda: 119 översättningsbara och 1 strukturposter utan engelsk källtext. 81 direkta källtexter matchar HA Core-källan; 29 referensanvändningar med 26 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 9 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Inga äldre radvisa språkförslag för dessa 120 nycklar.
- 119 översättningsbara poster synkades retroaktivt till HA Core TM. En nyckel har tom engelsk källtext och motsvarar `data: {}` i källan; de är dokumenterade som strukturposter och har inte lagts i TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 16681 | 871578739 | `component::vistapool::entity::binary_sensor::redox_module::name` | Redox module | Redoxmodul | Core-literal match |
| 16682 | 871578738 | `component::vistapool::entity::binary_sensor::ph_pump_alarm::name` | pH pump alarm | Larm för pH-pump | Core-literal match |
| 16683 | 871578737 | `component::vistapool::entity::binary_sensor::ph_module::name` | pH module | pH-modul | Core-literal match |
| 16684 | 871578736 | `component::vistapool::entity::binary_sensor::ph_base_pump::name` | pH base pump | pH-baspump | Core-literal match |
| 16685 | 871578735 | `component::vistapool::entity::binary_sensor::ph_acid_pump::name` | pH acid pump | pH-syrapump | Core-literal match |
| 16686 | 871578734 | `component::vistapool::entity::binary_sensor::io_module::name` | IO module | IO-modul | Core-literal match |
| 16687 | 871578733 | `component::vistapool::entity::binary_sensor::hydrolysis_low::name` | Hydrolysis low | Låg hydrolys | Core-literal match |
| 16688 | 871578732 | `component::vistapool::entity::binary_sensor::hidro_module::name` | Hidro module | Hidro-modul | Core-literal match |
| 16689 | 871578731 | `component::vistapool::entity::binary_sensor::hidro_flow::name` | Hidro flow | Hidro-flöde | Core-literal match |
| 16690 | 871578730 | `component::vistapool::entity::binary_sensor::hidro_fl2::name` | Hidro FL2 | Hidro FL2 | Core-literal match |
| 16691 | 871578729 | `component::vistapool::entity::binary_sensor::hidro_cover_reduction::name` | Hidro cover reduction | Hidro skydd reducering | Core-literal match |
| 16692 | 871578728 | `component::vistapool::entity::binary_sensor::heating::name` | Heating | Värmer | Core-literal match |
| 16693 | 871578727 | `component::vistapool::entity::binary_sensor::filtration::name` | Filtration | Filtrering | Core-literal match |
| 16694 | 871578726 | `component::vistapool::entity::binary_sensor::electrolysis_low::name` | Electrolysis low | Låg elektrolys | Core-literal match |
| 16695 | 871578725 | `component::vistapool::entity::binary_sensor::dosing_tank::name` | Dosing tank | Doseringstank | Core-literal match |
| 16696 | 871578724 | `component::vistapool::entity::binary_sensor::conductivity_module::name` | Conductivity module | Konduktivitetsmodul | Core-literal match |
| 16697 | 871578723 | `component::vistapool::entity::binary_sensor::chlorine_pump::name` | Chlorine pump | Klorpump | Core-literal match |
| 16698 | 871578722 | `component::vistapool::entity::binary_sensor::chlorine_module::name` | Chlorine module | Klormodul | Core-literal match |
| 16699 | 871578721 | `component::vistapool::entity::binary_sensor::backwash::name` | Backwash | Backspolning | Core-literal match |
| 16700 | 871512372 | `component::smtp::config::step::reconfigure::title` | Reconfigure SMTP | Konfigurera om SMTP | Core-literal match |
| 16701 | 871512371 | `component::smtp::config::step::reconfigure::data_description::verify_ssl` | Enable certificate verification for secure SSL/TLS connections. | Aktivera certifikatverifiering för säkra SSL/TLS-anslutningar. | Shared reference target checked |
| 16702 | 871512370 | `component::smtp::config::step::reconfigure::data_description::username` | Username used to authenticate with the SMTP server. | Användarnamn som används för att autentisera sig hos SMTP-servern. | Shared reference target checked |
| 16703 | 871512369 | `component::smtp::config::step::reconfigure::data_description::server` | Hostname or IP address of the SMTP server. For example, `smtp.example.com`. | SMTP-serverns värdnamn eller IP-adress. Till exempel `smtp.example.com`. | Shared reference target checked |
| 16704 | 871512368 | `component::smtp::config::step::reconfigure::data_description::sender_name` | Display name shown as the email sender. | Det namn som visas som avsändare i e-postmeddelandet. | Shared reference target checked |
| 16705 | 871512367 | `component::smtp::config::step::reconfigure::data_description::sender` | Email address that will appear in the From field. | E-postadress som kommer att visas i fältet ”Från”. | Shared reference target checked |
| 16706 | 871512366 | `component::smtp::config::step::reconfigure::data_description::port` | Port number used by your SMTP server. Common values are `587` (STARTTLS) and `465` (TLS). | Portnummer som används av din SMTP-server. Vanliga värden är `587` (STARTTLS) och `465` (TLS). | Shared reference target checked |
| 16707 | 871512365 | `component::smtp::config::step::reconfigure::data_description::password` | Password or app-specific password for the SMTP account. | Lösenord eller appspecifikt lösenord för SMTP-kontot. | Shared reference target checked |
| 16708 | 871512364 | `component::smtp::config::step::reconfigure::data_description::encryption` | Encryption method used for the SMTP connection. **STARTTLS** upgrades a plain connection to encrypted (recommended). **SSL/TLS** uses encryption from the start. **None** sends without encryption. | Krypteringsmetod som används för SMTP-anslutningen. **STARTTLS** uppgraderar en okrypterad anslutning till en krypterad (rekommenderas). **SSL/TLS** använder kryptering från början. **Ingen** skickar utan kryptering. | Shared reference target checked |
| 16709 | 871512363 | `component::smtp::config::step::reconfigure::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 16710 | 871512362 | `component::smtp::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference target checked |
| 16711 | 871512361 | `component::smtp::config::step::reconfigure::data::server` | Host | Värd | Shared reference target checked |
| 16712 | 871512360 | `component::smtp::config::step::reconfigure::data::sender_name` | Sender name | Avsändarens namn | Shared reference target checked |
| 16713 | 871512359 | `component::smtp::config::step::reconfigure::data::sender` | Sender email | Avsändarens e-postadress | Shared reference target checked |
| 16714 | 871512358 | `component::smtp::config::step::reconfigure::data::port` | Port | Port | Shared reference target checked |
| 16715 | 871512357 | `component::smtp::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 16716 | 871512356 | `component::smtp::config::step::reconfigure::data::encryption` | Connection security | Anslutningssäkerhet | Shared reference target checked |
| 16717 | 871512355 | `component::smtp::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 16718 | 871426765 | `component::satel_integra::selector::arm_home_mode::options::3` | 3 - No interior zones or entry delay | 3 - Inga inomhuszoner eller ingångsfördröjning | Core-literal match |
| 16719 | 871426764 | `component::satel_integra::selector::arm_home_mode::options::2` | 2 - No interior zones | 2 - Inga inomhuszoner | Core-literal match |
| 16720 | 871426763 | `component::satel_integra::selector::arm_home_mode::options::1` | 1 - Full arming + bypasses | 1 - Fullständig tillkoppling + förbikopplingar | Core-literal match |
| 16721 | 871377969 | `component::aqvify::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 16722 | 871112536 | `component::imou::entity::camera::camera_sd::name` | Live view SD | Livevy SD | Core-literal match |
| 16723 | 871112535 | `component::imou::entity::camera::camera_hd::name` | Live view HD | Livevy HD | Core-literal match |
| 16724 | 871082648 | `component::melcloud_home::exceptions::timeout_connect::message` | Timeout while communicating with MELCloud Home API | Tidsgräns vid kommunikation med MELCloud Home API | Core-literal match |
| 16725 | 871082647 | `component::melcloud_home::exceptions::invalid_auth::message` | An error occurred while trying to authenticate | Ett fel uppstod vid inloggningen | Core-literal match |
| 16726 | 871082646 | `component::melcloud_home::exceptions::cannot_connect::message` | Error communicating with MELCloud Home API | Fel vid kommunikation med MELCloud Home API | Core-literal match |
| 16727 | 871082645 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_mode::state::swing` | Swing | Svänga | Core-literal match |
| 16728 | 871082644 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_mode::state::position_5` | Position 5 | Position 5 | Core-literal match |
| 16729 | 871082643 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_mode::state::position_4` | Position 4 | Position 4 | Core-literal match |
| 16730 | 871082642 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_mode::state::position_3` | Position 3 | Position 3 | Core-literal match |
| 16731 | 871082641 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_mode::state::position_2` | Position 2 | Position 2 | Core-literal match |
| 16732 | 871082640 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_mode::state::position_1` | Position 1 | Position 1 | Core-literal match |
| 16733 | 871082639 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_mode::state::auto` | Auto | Auto | Shared reference target checked |
| 16734 | 871082638 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_horizontal_mode::state::swing` | Swing | Svänga | Core-literal match |
| 16735 | 871082637 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_horizontal_mode::state::right_centre` | Right centre | Höger centrum | Core-literal match |
| 16736 | 871082636 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_horizontal_mode::state::right` | Right | Höger | Core-literal match |
| 16737 | 871082635 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_horizontal_mode::state::left_centre` | Left centre | Vänster centrum | Core-literal match |
| 16738 | 871082634 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_horizontal_mode::state::left` | Left | Vänster | Core-literal match |
| 16739 | 871082633 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_horizontal_mode::state::centre` | Centre | Centrerad | Core-literal match |
| 16740 | 871082632 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::swing_horizontal_mode::state::auto` | Auto | Auto | Shared reference target checked |
| 16741 | 871082631 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::fan_mode::state::speed_5` | Speed 5 | Hastighet 5 | Core-literal match |
| 16742 | 871082630 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::fan_mode::state::speed_4` | Speed 4 | Hastighet 4 | Core-literal match |
| 16743 | 871082629 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::fan_mode::state::speed_3` | Speed 3 | Hastighet 3 | Core-literal match |
| 16744 | 871082628 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::fan_mode::state::speed_2` | Speed 2 | Hastighet 2 | Core-literal match |
| 16745 | 871082627 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::fan_mode::state::speed_1` | Speed 1 | Hastighet 1 | Core-literal match |
| 16746 | 871082626 | `component::melcloud_home::entity::climate::ata_unit::state_attributes::fan_mode::state::auto` | Auto | Auto | Shared reference target checked |
| 16747 | 871082625 | `component::melcloud_home::config::step::user::description` | Log in to MELCloud Home with the email address and password associated with your account. | Logga in på MELCloud Home med den e-postadress och det lösenord som är kopplade till ditt konto. | Core-literal match |
| 16748 | 871082624 | `component::melcloud_home::config::step::user::data_description::password` | Password for your MELCloud Home account. | Lösenord för ditt MELCloud Home-konto. | Core-literal match |
| 16749 | 871082623 | `component::melcloud_home::config::step::user::data_description::email` | Email address for your MELCloud Home account. | E-postadress för ditt MELCloud Home-konto. | Core-literal match |
| 16750 | 871082622 | `component::melcloud_home::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 16751 | 871082621 | `component::melcloud_home::config::step::user::data::email` | Email | E-post | Shared reference target checked |
| 16752 | 871082620 | `component::melcloud_home::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 16753 | 871082619 | `component::melcloud_home::config::error::timeout_connect` | Timeout while communicating with MELCloud Home API | Timeout vid kommunikation med MELCloud Home API | Core-literal match |
| 16754 | 871082618 | `component::melcloud_home::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 16755 | 871082617 | `component::melcloud_home::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16756 | 871082616 | `component::melcloud_home::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 16757 | 870971063 | `component::klik_aan_klik_uit::config::step::user::description` | Choose the transmitter and configure your device settings. | Välj sändaren och konfigurera enhetens inställningar. | Core-literal match |
| 16758 | 870971062 | `component::klik_aan_klik_uit::config::step::user::data_description::transmitter` | The radio frequency transmitter to use for sending commands. | Den radiofrekvenssändare som ska användas för att skicka kommandon. | Shared reference target checked |
| 16759 | 870971061 | `component::klik_aan_klik_uit::config::step::user::data_description::group` | Whether to send commands to the group address instead of a single device. | Om kommandon ska skickas till gruppadressen istället för en enskild enhet. | Core-literal match |
| 16760 | 870971060 | `component::klik_aan_klik_uit::config::step::user::data_description::device_id` | The unique KlikAanKlikUit device ID. | Det unika KlikAanKlikUit-enhets-ID:t. | Core-literal match |
| 16761 | 870971059 | `component::klik_aan_klik_uit::config::step::user::data_description::channel` | The channel of the target KlikAanKlikUit device (1-16). | Kanalen för målenheten KlikAanKlikUit (1-16). | Core-literal match |
| 16762 | 870971058 | `component::klik_aan_klik_uit::config::step::user::data::transmitter` | Radio frequency transmitter | Sändare för radiofrekvens | Shared reference target checked |
| 16763 | 870971057 | `component::klik_aan_klik_uit::config::step::user::data::group` | Group | Grupp | Core-literal match |
| 16764 | 870971056 | `component::klik_aan_klik_uit::config::step::user::data::device_id` | Device ID | Enhets-ID | Core-literal match |
| 16765 | 870971055 | `component::klik_aan_klik_uit::config::step::user::data::channel` | Channel | Kanal | Core-literal match |
| 16766 | 870971054 | `component::klik_aan_klik_uit::config::step::pairing_result::title` | Confirm pairing | Bekräfta parkoppling | Core-literal match |
| 16767 | 870971053 | `component::klik_aan_klik_uit::config::step::pairing_result::description` | Select Yes to continue setup. Select No to return to learn mode and resend the learn command. | Välj Ja för att fortsätta installationen. Välj Nej för att återgå till inlärningsläge och skicka inlärningskommandot igen. | Core-literal match |
| 16768 | 870971052 | `component::klik_aan_klik_uit::config::step::pairing_result::data_description::device_responded` | Select Yes if the target device reacted to the learn command. | Välj Ja om målenheten reagerade på inlärningskommandot. | Core-literal match |
| 16769 | 870971051 | `component::klik_aan_klik_uit::config::step::pairing_result::data::device_responded` | Did the device respond? | Svarade enheten? | Core-literal match |
| 16770 | 870971050 | `component::klik_aan_klik_uit::config::step::pairing_mode::title` | Pair device | Koppla ihop enheten | Core-literal match |
| 16771 | 870971049 | `component::klik_aan_klik_uit::config::step::pairing_mode::description` | Bring the device into learn mode by pushing its button for more than 2 seconds, then press OK. | Sätt enheten i inlärningsläge genom att hålla knappen intryckt i mer än 2 sekunder och tryck sedan på OK. | Core-literal match |
| 16773 | 870971047 | `component::klik_aan_klik_uit::config::abort::no_transmitters` | No radio frequency transmitters are available. Please set up a device first. | Inga radiofrekvenssändare finns tillgängliga. Vänligen installera en enhet först. | Shared reference target checked |
| 16774 | 870971046 | `component::klik_aan_klik_uit::config::abort::no_compatible_transmitters` | No compatible radio frequency transmitter is available for this integration. | Det finns ingen kompatibel radiosändare för denna integration. | Core-literal match |
| 16775 | 870971045 | `component::klik_aan_klik_uit::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 16776 | 870915492 | `component::environment_canada::selector::radar_layer::options::snow` | Snow | Snö | Core-literal match |
| 16777 | 870915491 | `component::environment_canada::selector::radar_layer::options::rain` | Rain | Regn | Core-literal match |
| 16778 | 870915490 | `component::environment_canada::selector::radar_layer::options::precip_type` | Precipitation type | Nederbördstyp | Core-literal match |
| 16779 | 870915489 | `component::environment_canada::options::step::init::title` | Radar camera options | Alternativ för radarkamera | Core-literal match |
| 16780 | 870915488 | `component::environment_canada::options::step::init::data_description::radar_radius` | Radius of the radar map in kilometres | Radarkartans radie i kilometer | Source-path follow-up open |
| 16781 | 870915487 | `component::environment_canada::options::step::init::data_description::radar_opacity` | Opacity of the radar layer overlay (0-100) | Opacitet för radaröverlagringen (0-100) | Source-path follow-up open |
| 16782 | 870915486 | `component::environment_canada::options::step::init::data::radar_timestamp` | Show timestamp | Visa tidsstämpel | Source-path follow-up open |
| 16783 | 870915485 | `component::environment_canada::options::step::init::data::radar_radius` | Map radius | Kartradie | Source-path follow-up open |
| 16784 | 870915484 | `component::environment_canada::options::step::init::data::radar_opacity` | Radar opacity | Radaropacitet | Source-path follow-up open |
| 16785 | 870915483 | `component::environment_canada::options::step::init::data::radar_legend` | Show legend | Visa förklaring | Source-path follow-up open |
| 16786 | 870915482 | `component::environment_canada::options::step::init::data::radar_layer` | Radar type | Radartyp | Source-path follow-up open |
| 16787 | 870590811 | `component::github::entity::sensor::public_repos::unit_of_measurement` | repositories | kodförråd | Core-literal match |
| 16788 | 870590810 | `component::github::entity::sensor::public_repos::name` | Public repositories | Offentliga kodförråd | Core-literal match |
| 16789 | 870590809 | `component::github::entity::sensor::public_gists::unit_of_measurement` | gists | gists | Core-literal match |
| 16790 | 870590808 | `component::github::entity::sensor::public_gists::name` | Public gists | Offentliga gists | Core-literal match |
| 16791 | 870590807 | `component::github::entity::sensor::following::unit_of_measurement` | users | användare | Core-literal match |
| 16792 | 870590806 | `component::github::entity::sensor::following::name` | Following | Följer | Core-literal match |
| 16793 | 870590805 | `component::github::entity::sensor::followers::unit_of_measurement` | followers | följare | Core-literal match |
| 16794 | 870590804 | `component::github::entity::sensor::followers::name` | Followers | Följare | Core-literal match |
| 16795 | 870555937 | `component::smtp::options::step::init::data_description::timeout` | Maximum time to wait for a response from the SMTP server before the connection attempt is aborted. Defaults to 60 seconds. | Maximal väntetid på svar från SMTP servern innan anslutningsförsöket avbryts. Standardinställningen är 60 sekunder. | Core-literal match |
| 16796 | 870555936 | `component::smtp::options::step::init::data::timeout` | Connection timeout | Timeout för anslutning | Core-literal match |
| 16797 | 870132706 | `component::aqvify::exceptions::invalid_api_key::message` | Invalid API key. Please verify your API key and try to reauthenticate. | Ogiltig API-nyckel. Verifiera din API-nyckel och försök att autentisera igen. | Core-literal match |
| 16798 | 870132705 | `component::aqvify::exceptions::api_timeout::message` | Timeout occurred while communicating with the Aqvify API for {entry} | Tidsgränsen överskreds vid kommunikation med Aqvifys API för {entry} | Core-literal match |
| 16799 | 870132704 | `component::aqvify::exceptions::api_error::message` | An error occurred while communicating with the Aqvify API for {entry} | Ett fel uppstod vid kommunikation med Aqvifys API för {entry} | Core-literal match |
| 16800 | 869690083 | `component::aqvify::config::step::reauth_confirm::description` | Reauthentication required. Please enter your updated API key. | Återautentisering krävs. Ange din uppdaterade API-nyckel. | Core-literal match |

## Inte översättningsbara strukturposter

| Lokalise-nyckel-ID | Nyckel | Orsak |
|---:|---|---|
| 870971048 | `component::klik_aan_klik_uit::config::error` | Tom engelsk källtext; motsvarande `data: {}` i HA Core |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 871512355 | `component::smtp::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 871377969 | `component::aqvify::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 870915488 | `component::environment_canada::options::step::init::data_description::radar_radius` | Radius of the radar map in kilometres |
| 870915487 | `component::environment_canada::options::step::init::data_description::radar_opacity` | Opacity of the radar layer overlay (0-100) |
| 870915486 | `component::environment_canada::options::step::init::data::radar_timestamp` | Show timestamp |
| 870915485 | `component::environment_canada::options::step::init::data::radar_radius` | Map radius |
| 870915484 | `component::environment_canada::options::step::init::data::radar_opacity` | Radar opacity |
| 870915483 | `component::environment_canada::options::step::init::data::radar_legend` | Show legend |
| 870915482 | `component::environment_canada::options::step::init::data::radar_layer` | Radar type |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
