# Home Assistant Core – historiska intervall 10861–12000, TM-avstämning

Alla 1 140 rader hade redan radvisa granskningsrapporter. Granskningen uppdaterar TM retroaktivt från den nya fullständiga Lokalise API-exporten och uppdaterad HA Core-källa utan att upprepa eller skriva om redan godkända texter. Batchordningen fortsätter direkt efter den sparade raden 10860 (`924534622`).

## Resultat

- 1140/1 140 tidigare radgranskade rader avstämda mot aktuell Lokalise-snapshot. 829 direkta källtexter hittades; 829 matchar exakt. 261 referensanvändningar med 117 mål verifierades.
- Saknade referensmål: 0; mismatchar efter uppdatering: 0; tomma värden: 0; platshållarmismatch: 0.
- 40 poster saknar direkt eller alternativt källvärde i uppdaterat Core-träd och dokumenteras för uppföljning. 10 andra värden hittades i närliggande källsökväg.
- 146 äldre förslag jämfördes mot uppdaterad Lokalise-export. 140 är redan live. Avvikelser bedömdes manuellt; fem ändringar sparades i Lokalise (tre Silla Prism-texter, en Cloud STT-bekräftelse, en Persian Infrared-referenskonsument).
- Alla API-skrivningar lästes tillbaka. Gemensamma referensmål och deras konsumenter är synkroniserade.

## Ändringar sparade

| Fullständig nyckel | Tidigare svenska | Ny svenska |
|---|---|---|
| `component::silla_prism::config::step::user::data::base_topic` | Tidigare livevärde, se Lokalise manifest | Basämne |
| `component::silla_prism::config::error::no_device` | Tidigare livevärde, se Lokalise manifest | Inga Prism-meddelanden togs emot på detta basämne. Kontrollera att ämnet stämmer med det som konfigurerats i Silla-appen och att Prism är ansluten. |
| `component::silla_prism::config::error::invalid_base_topic` | Tidigare livevärde, se Lokalise manifest | Det här är inte ett giltigt MQTT-ämne. Ange ämnesprefixet från Silla-appen utan jokertecken. |
| `component::cloud::preview_features::stt_v2::disable_confirmation` | Tidigare livevärde, se Lokalise manifest | Tal för assistenter som använder den nya motorn transkriberas återigen av vår nuvarande tal-till-text-leverantör. |
| `component::persang_infrared::config::step::user::data_description::infrared_emitter_entity_id` | Tidigare livevärde, se Lokalise manifest | Sändarentiteten som ska användas för att skicka infraröda kommandon. |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|
| 923428298 | `component::sofar::config::step::reconfigure::data_description::port` | The Modbus TCP port to connect on. |
| 923428297 | `component::sofar::config::step::reconfigure::data_description::host` | The hostname or IP address of the inverter, or of the Modbus TCP bridge it's connected through. |
| 923428295 | `component::sofar::config::step::reconfigure::data::port` | Port |
| 923428294 | `component::sofar::config::step::reconfigure::data::host` | Host |
| 923428292 | `component::sofar::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 923427010 | `component::pushover::exceptions::attachment_open_failed::message` | Failed to open attachment {attachment}. |
| 923419103 | `component::sunsynk::entity::sensor::voltage::name` | Voltage |
| 923419102 | `component::sunsynk::entity::sensor::temperature::name` | Temperature |
| 923419097 | `component::sunsynk::entity::sensor::power::name` | Power |
| 923419085 | `component::sunsynk::entity::sensor::current::name` | Current |
| 923343434 | `component::centriconnect::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 923343433 | `component::centriconnect::config::abort::reauth_successful` | Re-authentication was successful |
| 923334536 | `component::imou::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |
| 923310145 | `component::solaredge_modbus::entity::sensor::vendor_status::name` | Vendor status |
| 923310123 | `component::solaredge_modbus::config::step::user::data::port` | Port |
| 923310122 | `component::solaredge_modbus::config::step::user::data::host` | Host |
| 923310108 | `component::solaredge_modbus::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 922028719 | `component::neopool::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 921275291 | `component::gatus::config::abort::reauth_successful` | Re-authentication was successful |
| 921245498 | `component::sofar::entity::sensor::waiting_ends::name` | Waiting ends |
| 921209147 | `component::remember_the_milk::config_subentries::list::abort::reconfigure_successful` | Reconfiguration was successful |
| 921119378 | `component::sun::triggers::polar_night_started::fields::offset_type::name` | Offset type |
| 921119377 | `component::sun::triggers::polar_night_started::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 921119372 | `component::sun::triggers::polar_night_ended::fields::offset_type::name` | Offset type |
| 921119371 | `component::sun::triggers::polar_night_ended::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 921119366 | `component::sun::triggers::midnight_sun_started::fields::offset_type::name` | Offset type |
| 921119365 | `component::sun::triggers::midnight_sun_started::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 921119360 | `component::sun::triggers::midnight_sun_ended::fields::offset_type::name` | Offset type |
| 921119359 | `component::sun::triggers::midnight_sun_ended::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 921119352 | `component::sun::triggers::golden_hour_started::fields::offset_type::name` | Offset type |
| 921119351 | `component::sun::triggers::golden_hour_started::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 921119344 | `component::sun::triggers::golden_hour_ended::fields::offset_type::name` | Offset type |
| 921119343 | `component::sun::triggers::golden_hour_ended::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 921119336 | `component::sun::triggers::blue_hour_started::fields::offset_type::name` | Offset type |
| 921119335 | `component::sun::triggers::blue_hour_started::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 921119328 | `component::sun::triggers::blue_hour_ended::fields::offset_type::name` | Offset type |
| 921119327 | `component::sun::triggers::blue_hour_ended::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 921086579 | `component::specialized_turbo::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 921086578 | `component::specialized_turbo::config::abort::reauth_successful` | Re-authentication was successful |
| 921058715 | `component::fronius::entity::switch::power_limit_enabled::name` | Power limiting |

## Fullständig radinventering

| Granskningsordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 10861 | 924534621 | `component::zonneplan::exceptions::invalid_auth::message` | An error occurred while trying to authenticate | Ett fel uppstod vid försök att autentisera | Core-literal match |
| 10862 | 924534620 | `component::zonneplan::exceptions::cannot_connect::message` | Error communicating with the Zonneplan API | Fel vid kommunikation med Zonneplan-API:t | Core-literal match |
| 10863 | 924534619 | `component::zonneplan::entity::sensor::lowest_electricity_price_tomorrow::name` | Lowest electricity price tomorrow | Lägsta elpris i morgon | Core-literal match |
| 10864 | 924534618 | `component::zonneplan::entity::sensor::lowest_electricity_price_today::name` | Lowest electricity price today | Lägsta elpris i dag | Core-literal match |
| 10865 | 924534617 | `component::zonneplan::entity::sensor::highest_electricity_price_tomorrow::name` | Highest electricity price tomorrow | Högsta elpris i morgon | Core-literal match |
| 10866 | 924534616 | `component::zonneplan::entity::sensor::highest_electricity_price_today::name` | Highest electricity price today | Högsta elpris i dag | Core-literal match |
| 10867 | 924534615 | `component::zonneplan::entity::sensor::gas_price_today::name` | Gas price daily | Dagens gaspris | Core-literal match |
| 10868 | 924534614 | `component::zonneplan::entity::sensor::electricity_prices_tomorrow_status::state::incoming` | Incoming | Inkommande | Core-literal match |
| 10869 | 924534613 | `component::zonneplan::entity::sensor::electricity_prices_tomorrow_status::state::available` | Available | Tillgängliga | Core-literal match |
| 10870 | 924534612 | `component::zonneplan::entity::sensor::electricity_prices_tomorrow_status::name` | Electricity prices tomorrow status | Status för morgondagens elpriser | Core-literal match |
| 10871 | 924534611 | `component::zonneplan::entity::sensor::electricity_price_low_tomorrow_start_time::name` | Electricity price low tomorrow start time | Starttid för lågt elpris i morgon | Core-literal match |
| 10872 | 924534610 | `component::zonneplan::entity::sensor::electricity_price_low_tomorrow_end_time::name` | Electricity price low tomorrow end time | Sluttid för lågt elpris i morgon | Core-literal match |
| 10873 | 924534609 | `component::zonneplan::entity::sensor::electricity_price_low_today_start_time::name` | Electricity price low today start time | Starttid för lågt elpris i dag | Core-literal match |
| 10874 | 924534608 | `component::zonneplan::entity::sensor::electricity_price_low_today_end_time::name` | Electricity price low today end time | Sluttid för lågt elpris i dag | Core-literal match |
| 10875 | 924534607 | `component::zonneplan::entity::sensor::current_electricity_price::name` | Current electricity price | Nuvarande elpris | Core-literal match |
| 10876 | 924534606 | `component::zonneplan::config::step::user::description` | Log in to Zonneplan with the email address associated with your account. You will be receiving a one-time password via email to complete the login process. | Logga in på Zonneplan med den e-postadress som är kopplad till ditt konto. Du kommer att få ett engångslösenord via e-post för att slutföra inloggningsprocessen. | Core-literal match |
| 10877 | 924534605 | `component::zonneplan::config::step::user::data_description::email` | Email address for your Zonneplan account. | E-postadress för ditt Zonneplan-konto. | Core-literal match |
| 10878 | 924534604 | `component::zonneplan::config::step::user::data::email` | Email | E-post | Shared reference checked |
| 10879 | 924534603 | `component::zonneplan::config::step::otp::description` | Within a few minutes, you will receive an email with a one-time password. Enter the password below to complete the login process. | Inom några minuter får du ett e-postmeddelande med ett engångslösenord. Ange lösenordet nedan för att slutföra inloggningsprocessen. | Core-literal match |
| 10880 | 924534602 | `component::zonneplan::config::step::otp::data_description::otp` | Enter the one-time password mailed to {email}. | Ange engångslösenordet som skickades till {email}. | Core-literal match |
| 10881 | 924534601 | `component::zonneplan::config::step::otp::data::otp` | One-time password | Engångslösenord | Core-literal match |
| 10882 | 924534600 | `component::zonneplan::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference checked |
| 10883 | 924534599 | `component::zonneplan::config::error::timeout_connect` | Timeout while communicating with the Zonneplan API | Tidsgränsen överskreds vid kommunikation med Zonneplan-API:t | Core-literal match |
| 10884 | 924534598 | `component::zonneplan::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference checked |
| 10885 | 924534597 | `component::zonneplan::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference checked |
| 10886 | 924534596 | `component::zonneplan::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference checked |
| 10887 | 924534168 | `component::nintendo_parental_controls::services::player_usage_report::name` | Get player usage report | Hämta rapport om spelarens användning | Core-literal match |
| 10888 | 924534167 | `component::nintendo_parental_controls::services::player_usage_report::fields::entity_id::name` | Player | Spelare | Core-literal match |
| 10889 | 924534166 | `component::nintendo_parental_controls::services::player_usage_report::fields::entity_id::description` | The player entity to get usage for. | Spelarentiteten som användningsinformationen ska hämtas för. | Core-literal match |
| 10890 | 924534165 | `component::nintendo_parental_controls::services::player_usage_report::fields::device_id::name` | Device | Enhet | Core-literal match |
| 10891 | 924534164 | `component::nintendo_parental_controls::services::player_usage_report::fields::device_id::description` | The ID of the device to get player usage details for. | ID:t för enheten som spelarens användningsinformation ska hämtas för. | Core-literal match |
| 10892 | 924534163 | `component::nintendo_parental_controls::services::player_usage_report::description` | Retrieves today's application usage details for a specific player. | Hämtar dagens information om appanvändning för en viss spelare. | Core-literal match |
| 10893 | 924534162 | `component::nintendo_parental_controls::services::device_usage_report::name` | Get device usage report | Hämta rapport om enhetsanvändning | Core-literal match |
| 10894 | 924534161 | `component::nintendo_parental_controls::services::device_usage_report::fields::device_id::name` | Device | Enhet | Core-literal match |
| 10895 | 924534160 | `component::nintendo_parental_controls::services::device_usage_report::fields::device_id::description` | The ID of the device to get usage details for. | ID för enheten som användningsinformation ska hämtas för. | Core-literal match |
| 10896 | 924534159 | `component::nintendo_parental_controls::services::device_usage_report::description` | Retrieves today's application usage details for a device. | Hämtar dagens information om appanvändning för en enhet. | Core-literal match |
| 10897 | 924534158 | `component::nintendo_parental_controls::exceptions::invalid_player::message` | The selected sensor is not a player sensor entity. Make sure you have selected the used screen time sensor for a specific player. | Den valda sensorn är inte en spelarsensor. Se till att du har valt sensorn för använd skärmtid för en viss spelare. | Core-literal match |
| 10898 | 924534157 | `component::nintendo_parental_controls::exceptions::invalid_entity::message` | The selected sensor is invalid, make sure you are selecting a Nintendo Parental Controls sensor. | Den valda sensorn är ogiltig. Välj en sensor från Nintendo Parental Controls. | Core-literal match |
| 10899 | 924518665 | `component::miele::entity::sensor::program_id::state::towels` | Towels | Handdukar | Core-literal match |
| 10900 | 924371428 | `component::lg_infrared::entity::switch::ion_generator::name` | Ion generator | Jongenerator | Core-literal match |
| 10901 | 924371427 | `component::lg_infrared::entity::switch::auto_clean::name` | Auto clean | Automatisk rengöring | Core-literal match |
| 10902 | 924346943 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_mode::state::swing` | Swing | Svängning | Core-literal match |
| 10903 | 924346942 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_mode::state::off` | Off | Av | Core-literal match |
| 10904 | 924346941 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_mode::state::middle_low` | Middle low | Medellåg | Core-literal match |
| 10905 | 924346940 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_mode::state::middle_high` | Middle high | Medelhög | Core-literal match |
| 10906 | 924346939 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_mode::state::lowest` | Lowest | Lägsta | Core-literal match |
| 10907 | 924346938 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_mode::state::low` | Low | Låg | Core-literal match |
| 10908 | 924346937 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_mode::state::highest` | Highest | Högsta | Core-literal match |
| 10909 | 924346936 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_mode::state::high` | High | Hög | Core-literal match |
| 10910 | 924346935 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_horizontal_mode::state::swing` | Swing | Svängning | Core-literal match |
| 10911 | 924346934 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_horizontal_mode::state::right_half` | Right half | Höger halva | Core-literal match |
| 10912 | 924346933 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_horizontal_mode::state::right` | Right | Höger | Core-literal match |
| 10913 | 924346932 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_horizontal_mode::state::off` | Off | Av | Core-literal match |
| 10914 | 924346931 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_horizontal_mode::state::middle_right` | Middle right | Mitten till höger | Core-literal match |
| 10915 | 924346930 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_horizontal_mode::state::middle_left` | Middle left | Mitten till vänster | Core-literal match |
| 10916 | 924346929 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_horizontal_mode::state::middle` | Middle | Mitten | Core-literal match |
| 10917 | 924346928 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_horizontal_mode::state::left_half` | Left half | Vänster halva | Core-literal match |
| 10918 | 924346927 | `component::lg_infrared::entity::climate::lg_ac::state_attributes::swing_horizontal_mode::state::left` | Left | Vänster | Core-literal match |
| 10919 | 923724960 | `component::tuya::entity::select::light_mode::state::on` | On | På | Shared reference checked |
| 10920 | 923428299 | `component::sofar::config::step::reconfigure::data_description::unit_id` | The inverter's Modbus unit ID, also called its Modbus device address. | Växelriktarens Modbus-enhets-ID, även kallat dess Modbus-enhetsadress. | Source found in adjacent Core path |
| 10921 | 923428298 | `component::sofar::config::step::reconfigure::data_description::port` | The Modbus TCP port to connect on. | Modbus TCP-porten att ansluta till. | Source-owner follow-up open |
| 10922 | 923428297 | `component::sofar::config::step::reconfigure::data_description::host` | The hostname or IP address of the inverter, or of the Modbus TCP bridge it's connected through. | Värdnamnet eller IP-adressen för växelriktaren, eller för Modbus TCP-bryggan den är ansluten via. | Source-owner follow-up open |
| 10923 | 923428296 | `component::sofar::config::step::reconfigure::data::unit_id` | Modbus unit ID | Modbus-enhets-ID | Source found in adjacent Core path |
| 10924 | 923428295 | `component::sofar::config::step::reconfigure::data::port` | Port | Port | Source-owner follow-up open |
| 10925 | 923428294 | `component::sofar::config::step::reconfigure::data::host` | Host | Värd | Source-owner follow-up open |
| 10926 | 923428293 | `component::sofar::config::abort::unique_id_mismatch` | Please reconfigure the same inverter you originally set up. | Konfigurera om samma växelriktare som du ursprungligen konfigurerade. | Core-literal match |
| 10927 | 923428292 | `component::sofar::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-owner follow-up open |
| 10928 | 923427182 | `component::elgato::exceptions::firmware_unknown_error::message` | An unknown error occurred while downloading the firmware from Elgato. | Ett okänt fel uppstod när den inbyggda programvaran hämtades från Elgato. | Core-literal match |
| 10929 | 923427181 | `component::elgato::exceptions::firmware_install_error::message` | The Elgato device did not accept the firmware: {error} | Elgato-enheten accepterade inte den inbyggda programvaran: {error} | Core-literal match |
| 10930 | 923427180 | `component::elgato::exceptions::firmware_communication_error::message` | An error occurred while downloading the firmware from Elgato. | Ett fel uppstod när den inbyggda programvaran hämtades från Elgato. | Core-literal match |
| 10931 | 923427010 | `component::pushover::exceptions::attachment_open_failed::message` | Failed to open attachment {attachment}. | Det gick inte att öppna bilagan {attachment}. | Source-owner follow-up open |
| 10932 | 923427009 | `component::pushover::exceptions::attachment_not_allowed::message` | Attachment path {attachment} is not allowed. | Sökvägen till bilagan {attachment} är inte tillåten. | Core-literal match |
| 10933 | 923422821 | `component::samsung_infrared::selector::device_type::options::ac` | Air Conditioner | Luftkonditionering | Core-literal match |
| 10934 | 923422809 | `component::mitsubishi_comfort::issues::missing_address::title` | Mitsubishi Comfort devices have no local IP address | Mitsubishi Comfort-enheterna saknar lokal IP-adress | Core-literal match |
| 10935 | 923422808 | `component::mitsubishi_comfort::issues::missing_address::fix_flow::step::confirm::title` | Issue is no longer relevant | Problemet är inte längre relevant | Core-literal match |
| 10936 | 923422807 | `component::mitsubishi_comfort::issues::missing_address::fix_flow::step::confirm::description` | The account this issue was created for no longer exists, so there is nothing left to fix. Confirm to dismiss the issue. | Kontot som problemet skapades för finns inte längre, så det finns inget kvar att åtgärda. Bekräfta för att avfärda problemet. | Core-literal match |
| 10937 | 923422806 | `component::mitsubishi_comfort::issues::missing_address::fix_flow::step::addresses::title` | Device IP addresses | Enheternas IP-adresser | Core-literal match |
| 10938 | 923422805 | `component::mitsubishi_comfort::issues::missing_address::fix_flow::step::addresses::description` | These devices have no known local IP address, so they have no entities yet. Enter the local IPv4 address for each device below; each field is labeled with the device's MAC address. Leave a field blank to keep waiting for DHCP discovery (which only works when the device is on the same network as Home Assistant). After you submit, the integration reloads and sets up every device that has an address. Devices: {devices} | Dessa enheter saknar en känd lokal IP-adress och har därför ännu inga entiteter. Ange den lokala IPv4-adressen för varje enhet nedan. Varje fält är märkt med enhetens MAC-adress. Lämna ett fält tomt om du vill fortsätta vänta på DHCP-upptäckt, som bara fungerar när enheten är i samma nätverk som Home Assistant. När du skickar in uppgifterna läses integrationen in på nytt och varje enhet med en adress konfigureras. Enheter: {devices} | Core-literal match |
| 10939 | 923422804 | `component::mitsubishi_comfort::issues::missing_address::fix_flow::error::invalid_ip` | One or more entries are not valid IPv4 addresses. | En eller flera poster är inte giltiga IPv4-adresser. | Core-literal match |
| 10940 | 923422803 | `component::mitsubishi_comfort::issues::missing_address::fix_flow::error::cannot_connect` | One or more devices did not respond at the entered address. | En eller flera enheter svarade inte på den angivna adressen. | Core-literal match |
| 10941 | 923422802 | `component::mitsubishi_comfort::config::error::no_usable_devices` | The cloud did not return complete local-control information for any device on this account. Wait a few minutes and try again. | Molnet returnerade inte fullständig information om lokal styrning för någon enhet på det här kontot. Vänta några minuter och försök igen. | Core-literal match |
| 10942 | 923419580 | `component::modern_forms::exceptions::sleep_timer_not_supported::message` | This fan does not support sleep timers | Den här fläkten stöder inte insomningstimers | Core-literal match |
| 10943 | 923419520 | `component::apple_tv::config::error::invalid_pin` | Invalid PIN | Ogiltig PIN-kod | Core-literal match |
| 10944 | 923419493 | `component::solaredge_modbus::entity::switch::negative_site_limit::name` | Negative site limit | Negativ gräns för anläggningen | Core-literal match |
| 10945 | 923419492 | `component::solaredge_modbus::entity::switch::external_production::name` | External production | Extern produktion | Core-literal match |
| 10946 | 923419478 | `component::frontier_silicon::entity::switch::dst::name` | Daylight Saving Time | Sommartid | Core-literal match |
| 10947 | 923419476 | `component::mcp_server::options::step::init::data_description::require_admin` | Only allow administrator accounts to use the main URL. Some tools always require an administrator account. | Tillåt endast administratörskonton att använda huvud-URL:en. Vissa verktyg kräver alltid ett administratörskonto. | Core-literal match |
| 10948 | 923419475 | `component::mcp_server::options::step::init::data::require_admin` | Require an administrator account | Kräv ett administratörskonto | Core-literal match |
| 10949 | 923419474 | `component::kaco_modbus::exceptions::sunspec_map_moved::message` | The inverter's SunSpec register map moved, so the integration is reloading to find it again: {error} | Växelriktarens SunSpec-registerkarta har flyttats, så integrationen laddas om för att hitta den igen: {error} | Core-literal match |
| 10950 | 923419473 | `component::kaco_modbus::exceptions::not_a_kaco_inverter::message` | The device at this address is not a KACO inverter: {error} | Enheten på den här adressen är inte en KACO-växelriktare: {error} | Core-literal match |
| 10951 | 923419472 | `component::kaco_modbus::exceptions::no_component_answered::message` | {name} accepted the connection but answered nothing. | {name} accepterade anslutningen men svarade inte. | Core-literal match |
| 10952 | 923419471 | `component::kaco_modbus::exceptions::cannot_connect::message` | Failed to reach the inverter: {error} | Det gick inte att nå växelriktaren: {error} | Core-literal match |
| 10953 | 923419470 | `component::kaco_modbus::entity::sensor::operating_state::state::throttled` | Throttled | Begränsad | Core-literal match |
| 10954 | 923419469 | `component::kaco_modbus::entity::sensor::operating_state::state::starting` | Starting up | Startar | Core-literal match |
| 10955 | 923419468 | `component::kaco_modbus::entity::sensor::operating_state::state::standby` | Standby | Viloläge | Shared reference checked |
| 10956 | 923419467 | `component::kaco_modbus::entity::sensor::operating_state::state::sleeping` | Asleep | Vilar | Core-literal match |
| 10957 | 923419466 | `component::kaco_modbus::entity::sensor::operating_state::state::shutting_down` | Shutting down | Stänger av | Core-literal match |
| 10958 | 923419465 | `component::kaco_modbus::entity::sensor::operating_state::state::off` | Off | Av | Shared reference checked |
| 10959 | 923419464 | `component::kaco_modbus::entity::sensor::operating_state::state::mppt` | Producing | Producerar | Core-literal match |
| 10960 | 923419463 | `component::kaco_modbus::entity::sensor::operating_state::state::fault` | Fault | Fel | Core-literal match |
| 10961 | 923419462 | `component::kaco_modbus::entity::sensor::operating_state::name` | Operating state | Driftstatus | Core-literal match |
| 10962 | 923419461 | `component::kaco_modbus::entity::sensor::lifetime_energy::name` | Total energy produced | Total producerad energi | Core-literal match |
| 10963 | 923419460 | `component::kaco_modbus::entity::sensor::ac_power::name` | AC power | AC-effekt | Core-literal match |
| 10964 | 923419459 | `component::kaco_modbus::config::step::user::description` | Enter the address of your KACO inverter. Modbus TCP must be enabled on the inverter, under its SunSpec or Modbus protocol settings. | Ange adressen till KACO-växelriktaren. Modbus TCP måste vara aktiverat på växelriktaren under dess SunSpec- eller Modbus-protokollinställningar. | Core-literal match |
| 10965 | 923419458 | `component::kaco_modbus::config::step::user::data_description::unit_id` | Leave at 1 unless the inverter is reached through an RS485-to-TCP gateway, which needs the address configured on that gateway. | Om växelriktaren nås via en RS485-till-TCP-gateway anger du adressen som är konfigurerad på gatewayen. Annars låter du värdet vara 1. | Core-literal match |
| 10966 | 923419457 | `component::kaco_modbus::config::step::user::data_description::port` | The Modbus TCP port. KACO inverters use 502 unless changed. | Modbus TCP-porten. KACO-växelriktare använder 502 om den inte har ändrats. | Core-literal match |
| 10967 | 923419456 | `component::kaco_modbus::config::step::user::data_description::host` | The inverter's hostname or IP address. | Växelriktarens värdnamn eller IP-adress. | Core-literal match |
| 10968 | 923419455 | `component::kaco_modbus::config::step::user::data::unit_id` | Unit ID | Enhets-ID | Core-literal match |
| 10969 | 923419454 | `component::kaco_modbus::config::step::user::data::port` | Port | Port | Shared reference checked |
| 10970 | 923419453 | `component::kaco_modbus::config::step::user::data::host` | Host | Värd | Shared reference checked |
| 10971 | 923419452 | `component::kaco_modbus::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference checked |
| 10972 | 923419451 | `component::kaco_modbus::config::error::not_a_sunspec_inverter` | That address answers Modbus, but not as a SunSpec inverter | Adressen svarar på Modbus, men inte som en SunSpec-växelriktare | Core-literal match |
| 10973 | 923419450 | `component::kaco_modbus::config::error::not_a_kaco_inverter` | That address answers, but the device is not a KACO inverter | Adressen svarar, men enheten är inte en KACO-växelriktare | Core-literal match |
| 10974 | 923419449 | `component::kaco_modbus::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference checked |
| 10975 | 923419448 | `component::kaco_modbus::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference checked |
| 10976 | 923419388 | `component::solaredge_modbus::entity::select::storage_default_mode::state::solar_only` | Solar only | Endast solenergi | Core-literal match |
| 10977 | 923419387 | `component::solaredge_modbus::entity::select::storage_default_mode::state::maximize_self_consumption` | Maximize self-consumption | Maximera egenförbrukningen | Core-literal match |
| 10978 | 923419386 | `component::solaredge_modbus::entity::select::storage_default_mode::state::discharge_to_minimize_import` | Discharge to minimize import | Ladda ur för att minimera importen | Core-literal match |
| 10979 | 923419385 | `component::solaredge_modbus::entity::select::storage_default_mode::state::discharge_to_maximize_export` | Discharge to maximize export | Ladda ur för att maximera exporten | Core-literal match |
| 10980 | 923419384 | `component::solaredge_modbus::entity::select::storage_default_mode::state::charge_from_solar_and_grid` | Charge from solar and grid | Ladda från solenergi och elnätet | Core-literal match |
| 10981 | 923419383 | `component::solaredge_modbus::entity::select::storage_default_mode::state::charge_from_solar` | Charge from solar | Ladda från solenergi | Core-literal match |
| 10982 | 923419382 | `component::solaredge_modbus::entity::select::storage_default_mode::state::charge_from_clipped_solar` | Charge from clipped solar | Ladda från begränsad solproduktion | Core-literal match |
| 10983 | 923419381 | `component::solaredge_modbus::entity::select::storage_default_mode::name` | Storage default mode | Standardläge för energilager | Core-literal match |
| 10984 | 923419380 | `component::solaredge_modbus::entity::select::storage_control_mode::state::time_of_use` | Time of use | Tidsstyrning | Core-literal match |
| 10985 | 923419379 | `component::solaredge_modbus::entity::select::storage_control_mode::state::remote_control` | Remote control | Fjärrstyrning | Core-literal match |
| 10986 | 923419378 | `component::solaredge_modbus::entity::select::storage_control_mode::state::maximize_self_consumption` | Maximize self-consumption | Maximera egenförbrukningen | Core-literal match |
| 10987 | 923419377 | `component::solaredge_modbus::entity::select::storage_control_mode::state::disabled` | Disabled | Inaktiverad | Shared reference checked |
| 10988 | 923419376 | `component::solaredge_modbus::entity::select::storage_control_mode::state::backup_only` | Backup only | Endast reservkraft | Core-literal match |
| 10989 | 923419375 | `component::solaredge_modbus::entity::select::storage_control_mode::name` | Storage control mode | Styrningsläge för energilager | Core-literal match |
| 10990 | 923419374 | `component::solaredge_modbus::entity::select::storage_command_mode::state::solar_only` | Solar only | Endast solenergi | Shared reference checked |
| 10991 | 923419373 | `component::solaredge_modbus::entity::select::storage_command_mode::state::maximize_self_consumption` | Maximize self-consumption | Maximera egenförbrukningen | Shared reference checked |
| 10992 | 923419372 | `component::solaredge_modbus::entity::select::storage_command_mode::state::discharge_to_minimize_import` | Discharge to minimize import | Ladda ur för att minimera importen | Shared reference checked |
| 10993 | 923419371 | `component::solaredge_modbus::entity::select::storage_command_mode::state::discharge_to_maximize_export` | Discharge to maximize export | Ladda ur för att maximera exporten | Shared reference checked |
| 10994 | 923419370 | `component::solaredge_modbus::entity::select::storage_command_mode::state::charge_from_solar_and_grid` | Charge from solar and grid | Ladda från solenergi och elnätet | Shared reference checked |
| 10995 | 923419369 | `component::solaredge_modbus::entity::select::storage_command_mode::state::charge_from_solar` | Charge from solar | Ladda från solenergi | Shared reference checked |
| 10996 | 923419368 | `component::solaredge_modbus::entity::select::storage_command_mode::state::charge_from_clipped_solar` | Charge from clipped solar | Ladda från begränsad solproduktion | Shared reference checked |
| 10997 | 923419367 | `component::solaredge_modbus::entity::select::storage_command_mode::name` | Storage command mode | Kommandoläge för energilager | Core-literal match |
| 10998 | 923419366 | `component::solaredge_modbus::entity::select::storage_ac_charge_policy::state::percent_of_production` | Percentage of production | Andel av produktionen | Core-literal match |
| 10999 | 923419365 | `component::solaredge_modbus::entity::select::storage_ac_charge_policy::state::fixed_energy_limit` | Fixed energy limit | Fast energigräns | Core-literal match |
| 11000 | 923419364 | `component::solaredge_modbus::entity::select::storage_ac_charge_policy::state::disabled` | Disabled | Inaktiverad | Shared reference checked |
| 11001 | 923419363 | `component::solaredge_modbus::entity::select::storage_ac_charge_policy::state::always` | Always | Alltid | Core-literal match |
| 11002 | 923419362 | `component::solaredge_modbus::entity::select::storage_ac_charge_policy::name` | Storage AC charge policy | Policy för AC-laddning av energilager | Core-literal match |
| 11003 | 923419361 | `component::solaredge_modbus::entity::select::export_control_mode::state::production_control` | Production control | Produktionsstyrning | Core-literal match |
| 11004 | 923419360 | `component::solaredge_modbus::entity::select::export_control_mode::state::export_control_export_import_meter` | Export and import meter | Export- och importmätare | Core-literal match |
| 11005 | 923419359 | `component::solaredge_modbus::entity::select::export_control_mode::state::export_control_consumption_meter` | Consumption meter | Förbrukningsmätare | Core-literal match |
| 11006 | 923419358 | `component::solaredge_modbus::entity::select::export_control_mode::state::disabled` | Disabled | Inaktiverad | Shared reference checked |
| 11007 | 923419357 | `component::solaredge_modbus::entity::select::export_control_mode::name` | Export limitation | Exportbegränsning | Core-literal match |
| 11008 | 923419356 | `component::solaredge_modbus::entity::select::export_control_limit_type::state::total` | Total | Total | Core-literal match |
| 11009 | 923419355 | `component::solaredge_modbus::entity::select::export_control_limit_type::state::per_phase` | Per phase | Per fas | Core-literal match |
| 11010 | 923419354 | `component::solaredge_modbus::entity::select::export_control_limit_type::name` | Export limit type | Typ av exportgräns | Core-literal match |
| 11011 | 923419353 | `component::peblar::exceptions::customization_update_first::message` | Install the customization update before the firmware update, the way the charger's own web interface does. | Installera anpassningsuppdateringen före uppdateringen av den inbyggda programvaran, på samma sätt som i laddarens eget webbgränssnitt. | Core-literal match |
| 11012 | 923419261 | `component::silla_prism::config::abort::mqtt_unavailable` | The MQTT integration is not available. Set it up first. | MQTT-integrationen är inte tillgänglig. Konfigurera den först. | Core-literal match |
| 11013 | 923419245 | `component::vistapool::entity::time::light_schedule_start::name` | Light schedule start | Start för ljusschema | Core-literal match |
| 11014 | 923419244 | `component::vistapool::entity::time::light_schedule_end::name` | Light schedule end | Slut för ljusschema | Core-literal match |
| 11015 | 923419243 | `component::vistapool::entity::select::light_schedule_frequency::state::weekly` | Weekly | Veckovis | Core-literal match |
| 11016 | 923419242 | `component::vistapool::entity::select::light_schedule_frequency::state::daily` | Daily | Dagligen | Core-literal match |
| 11017 | 923419241 | `component::vistapool::entity::select::light_schedule_frequency::name` | Light schedule frequency | Frekvens för ljusschema | Core-literal match |
| 11018 | 923419240 | `component::vistapool::entity::select::light_mode::state::on` | On | På | Core-literal match |
| 11019 | 923419239 | `component::vistapool::entity::select::light_mode::state::off` | Off | Av | Core-literal match |
| 11020 | 923419238 | `component::vistapool::entity::select::light_mode::state::auto` | Auto | Auto | Core-literal match |
| 11021 | 923419237 | `component::vistapool::entity::select::light_mode::name` | Light mode | Ljusläge | Core-literal match |
| 11022 | 923419103 | `component::sunsynk::entity::sensor::voltage::name` | Voltage | Spänning | Source-owner follow-up open |
| 11023 | 923419102 | `component::sunsynk::entity::sensor::temperature::name` | Temperature | Temperatur | Source-owner follow-up open |
| 11024 | 923419101 | `component::sunsynk::entity::sensor::state_of_charge::name` | State of charge | Laddningsnivå | Core-literal match |
| 11025 | 923419100 | `component::sunsynk::entity::sensor::solar_power::name` | Solar power | Soleffekt | Core-literal match |
| 11026 | 923419099 | `component::sunsynk::entity::sensor::solar_energy_total::name` | Solar energy total | Solenergi totalt | Core-literal match |
| 11027 | 923419098 | `component::sunsynk::entity::sensor::solar_energy_today::name` | Solar energy today | Solenergi i dag | Core-literal match |
| 11028 | 923419097 | `component::sunsynk::entity::sensor::power::name` | Power | Effekt | Source-owner follow-up open |
| 11029 | 923419096 | `component::sunsynk::entity::sensor::load_power::name` | Load power | Förbrukningseffekt | Core-literal match |
| 11030 | 923419095 | `component::sunsynk::entity::sensor::load_energy_total::name` | Load energy total | Förbrukningsenergi totalt | Core-literal match |
| 11031 | 923419094 | `component::sunsynk::entity::sensor::load_energy_today::name` | Load energy today | Förbrukningsenergi i dag | Core-literal match |
| 11032 | 923419093 | `component::sunsynk::entity::sensor::grid_power::name` | Grid power | Näteffekt | Core-literal match |
| 11033 | 923419092 | `component::sunsynk::entity::sensor::grid_import_total::name` | Grid import total | Import från nätet totalt | Core-literal match |
| 11034 | 923419091 | `component::sunsynk::entity::sensor::grid_import_today::name` | Grid import today | Import från nätet i dag | Core-literal match |
| 11035 | 923419090 | `component::sunsynk::entity::sensor::grid_frequency::name` | Grid frequency | Nätfrekvens | Core-literal match |
| 11036 | 923419089 | `component::sunsynk::entity::sensor::grid_export_total::name` | Grid export total | Export till nätet totalt | Core-literal match |
| 11037 | 923419088 | `component::sunsynk::entity::sensor::grid_export_today::name` | Grid export today | Export till nätet i dag | Core-literal match |
| 11038 | 923419087 | `component::sunsynk::entity::sensor::discharge_total::name` | Discharge total | Urladdning totalt | Core-literal match |
| 11039 | 923419086 | `component::sunsynk::entity::sensor::discharge_today::name` | Discharge today | Urladdning i dag | Core-literal match |
| 11040 | 923419085 | `component::sunsynk::entity::sensor::current::name` | Current | Ström | Source-owner follow-up open |
| 11041 | 923419084 | `component::sunsynk::entity::sensor::charge_total::name` | Charge total | Laddning totalt | Core-literal match |
| 11042 | 923419083 | `component::sunsynk::entity::sensor::charge_today::name` | Charge today | Laddning i dag | Core-literal match |
| 11043 | 923419082 | `component::sunsynk::config::step::user::description` | Connect to your Sunsynk Connect account to get data from your inverters. | Anslut till ditt Sunsynk Connect-konto för att hämta data från växelriktarna. | Core-literal match |
| 11044 | 923419081 | `component::sunsynk::config::step::user::data_description::username` | The email address of your Sunsynk Connect account. | E-postadressen för ditt Sunsynk Connect-konto. | Core-literal match |
| 11045 | 923419080 | `component::sunsynk::config::step::user::data_description::password` | The password of your Sunsynk Connect account. | Lösenordet för ditt Sunsynk Connect-konto. | Core-literal match |
| 11046 | 923419079 | `component::sunsynk::config::step::user::data::username` | Username | Användarnamn | Shared reference checked |
| 11047 | 923419078 | `component::sunsynk::config::step::user::data::password` | Password | Lösenord | Shared reference checked |
| 11048 | 923419077 | `component::sunsynk::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference checked |
| 11049 | 923419076 | `component::sunsynk::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference checked |
| 11050 | 923419075 | `component::sunsynk::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference checked |
| 11051 | 923385519 | `component::elgato::entity::sensor::wifi_signal_strength::name` | Wi-Fi signal strength | Wi-Fi-signalstyrka | Core-literal match |
| 11052 | 923385518 | `component::elgato::entity::sensor::wifi_rssi::name` | Wi-Fi RSSI | Wi-Fi-RSSI | Core-literal match |
| 11053 | 923385483 | `component::elgato::entity::number::power_on_temperature::name` | Power-on color temperature | Färgtemperatur vid påslagning | Core-literal match |
| 11054 | 923385482 | `component::elgato::entity::number::power_on_brightness::name` | Power-on brightness | Ljusstyrka vid påslagning | Core-literal match |
| 11055 | 923385480 | `component::led_infrared::selector::device_type::options::generic_10_key` | 10-key remote control | Fjärrkontroll med 10 knappar | Core-literal match |
| 11056 | 923385479 | `component::led_infrared::entity::light::light::state_attributes::effect::state::light` | Steady light | Fast sken | Core-literal match |
| 11057 | 923385478 | `component::led_infrared::entity::light::light::state_attributes::effect::state::candle` | Candle | Stearinljus | Core-literal match |
| 11058 | 923385477 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::timer_8h` | Timer 8h | Timer 8 h | Core-literal match |
| 11059 | 923385476 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::timer_6h` | Timer 6h | Timer 6 h | Core-literal match |
| 11060 | 923385475 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::timer_4h` | Timer 4h | Timer 4 h | Core-literal match |
| 11061 | 923385474 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::timer_2h` | Timer 2h | Timer 2 h | Core-literal match |
| 11062 | 923385473 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::light` | Steady light | Fast sken | Shared reference checked |
| 11063 | 923385472 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::candle` | Candle | Stearinljus | Shared reference checked |
| 11064 | 923385471 | `component::led_infrared::entity::button::timer_8h::name` | Timer 8h | Timer 8 h | Shared reference checked |
| 11065 | 923385470 | `component::led_infrared::entity::button::timer_6h::name` | Timer 6h | Timer 6 h | Shared reference checked |
| 11066 | 923385469 | `component::led_infrared::entity::button::timer_4h::name` | Timer 4h | Timer 4 h | Shared reference checked |
| 11067 | 923385468 | `component::led_infrared::entity::button::timer_2h::name` | Timer 2h | Timer 2 h | Shared reference checked |
| 11068 | 923385362 | `component::elgato::entity::select::power_on_behavior::state::use_defaults` | Use defaults | Använd standardvärden | Core-literal match |
| 11069 | 923385361 | `component::elgato::entity::select::power_on_behavior::state::restore_last` | Restore last state | Återställ senaste tillstånd | Core-literal match |
| 11070 | 923385360 | `component::elgato::entity::select::power_on_behavior::name` | Power-on behavior | Beteende vid påslagning | Core-literal match |
| 11071 | 923385357 | `component::duco::exceptions::invalid_bypass_supply_temperature_target_step::message` | The value {value} does not match the supported increment of {increment} starting at {minimum}. | Värdet {value} överensstämmer inte med den stödda stegstorleken {increment} med början på {minimum}. | Core-literal match |
| 11072 | 923385356 | `component::duco::exceptions::failed_to_set_bypass_supply_temperature_target::message` | Failed to set bypass supply target temperature. | Det gick inte att ange måltemperaturen för bypass-tilluft. | Core-literal match |
| 11073 | 923385355 | `component::duco::entity::number::bypass_supply_target_temperature_zone::name` | Bypass target {zone} | Bypassbörvärde {zone} | Core-literal match |
| 11074 | 923354383 | `component::synology_dsm::options::abort::entry_not_loaded` | The integration is not loaded, so the shares to back up to cannot be listed. | Integrationen har inte lästs in, så det går inte att visa de utdelade mappar som det går att säkerhetskopiera till. | Core-literal match |
| 11075 | 923346259 | `component::peblar::services::authorize_charge_session::name` | Authorize charge session | Auktorisera laddsession | Core-literal match |
| 11076 | 923346258 | `component::peblar::services::authorize_charge_session::fields::uid::name` | UID | UID | Core-literal match |
| 11077 | 923346257 | `component::peblar::services::authorize_charge_session::fields::uid::description` | The unique identifier of the RFID token to present. | Den unika identifieraren för den RFID-token som ska presenteras. | Core-literal match |
| 11078 | 923346256 | `component::peblar::services::authorize_charge_session::fields::description::name` | Description | Beskrivning | Core-literal match |
| 11079 | 923346255 | `component::peblar::services::authorize_charge_session::fields::description::description` | The label of the RFID token to present, instead of its UID. | Etiketten för den RFID-token som ska presenteras, i stället för dess UID. | Core-literal match |
| 11080 | 923346254 | `component::peblar::services::authorize_charge_session::fields::config_entry_id::name` | Peblar EV charger | Peblar EV-laddare | Core-literal match |
| 11081 | 923346253 | `component::peblar::services::authorize_charge_session::fields::config_entry_id::description` | The Peblar EV charger to present the token to. | Den Peblar-laddare som token ska presenteras för. | Core-literal match |
| 11082 | 923346252 | `component::peblar::services::authorize_charge_session::description` | Presents a token to the charger, as if it were held against the reader. This authorizes a session that is waiting for it, and stops one that is already running. | Presenterar en token för laddaren som om den hölls mot läsaren. Detta auktoriserar en session som väntar på den och stoppar en session som redan pågår. | Core-literal match |
| 11083 | 923346251 | `component::peblar::exceptions::managed_by_backoffice::message` | {charger} is managed over OCPP, so its sessions are authorized by the backoffice. | {charger} hanteras via OCPP, så dess sessioner auktoriseras av backoffice-systemet. | Core-literal match |
| 11084 | 923346250 | `component::peblar::exceptions::authorization_not_required::message` | {charger} is set to charge without authorization, so there is nothing to authorize. | {charger} är inställd på att ladda utan auktorisering, så det finns inget att auktorisera. | Core-literal match |
| 11085 | 923346239 | `component::nobo_hub::exceptions::set_disable_global_override_failed::message` | Failed to change whether global overrides are disabled for the zone. | Det gick inte att ändra om globala åsidosättningar är inaktiverade för zonen. | Core-literal match |
| 11086 | 923346238 | `component::nobo_hub::entity::switch::disable_global_override::name` | Disable global overrides | Inaktivera globala åsidosättningar | Core-literal match |
| 11087 | 923345189 | `component::mcp_server::options::step::init::description` | These settings apply to the main URL (`/api/mcp`). Each set of tools also has its own URL, which ignores these settings. See the [integration documentation]({more_info_url}) for setup instructions. | Se [integrationsdokumentationen]({more_info_url}) för installationsanvisningar. | Core-literal match |
| 11088 | 923345188 | `component::mcp_server::options::step::init::data_description::llm_hass_api` | **Device control** only accesses the entities you expose to voice assistants. **Home Assistant** accesses everything and requires an administrator account. | **Enhetsstyrning** har endast åtkomst till de enheter som du gör tillgängliga för röstassistenter. **Home Assistant** har åtkomst till allt och kräver ett administratörskonto. | Core-literal match |
| 11089 | 923345187 | `component::mcp_server::options::step::init::data::llm_hass_api` | AI tools | AI-verktyg | Shared reference checked |
| 11090 | 923345186 | `component::mcp_server::options::error::llm_api_required` | Select at least one set of tools or expose all AI tools. | Välj minst en uppsättning verktyg eller visa alla AI-verktyg. | Core-literal match |
| 11091 | 923343501 | `component::solaredge_modbus::exceptions::rejected_value::message` | The value was rejected for the SolarEdge inverter: {error} | Värdet avvisades av SolarEdge-växelriktaren: {error} | Core-literal match |
| 11092 | 923343500 | `component::solaredge_modbus::entity::number::site_limit::name` | Site export limit | Gräns för export från anläggningen | Core-literal match |
| 11093 | 923343499 | `component::solaredge_modbus::entity::number::external_production_max::name` | External production maximum | Maximal extern produktion | Core-literal match |
| 11094 | 923343498 | `component::solaredge_modbus::entity::number::discharge_limit::name` | Storage discharge limit | Gräns för urladdning av energilager | Core-literal match |
| 11095 | 923343497 | `component::solaredge_modbus::entity::number::cos_phi::name` | Power factor setpoint | Börvärde för effektfaktor | Core-literal match |
| 11096 | 923343496 | `component::solaredge_modbus::entity::number::charge_limit::name` | Storage charge limit | Gräns för laddning av energilager | Core-literal match |
| 11097 | 923343495 | `component::solaredge_modbus::entity::number::backup_reserve::name` | Backup reserve | Reserv för reservkraft | Core-literal match |
| 11098 | 923343494 | `component::solaredge_modbus::entity::number::active_power_limit::name` | Active power limit | Aktiv effektgräns | Core-literal match |
| 11099 | 923343474 | `component::solaredge_modbus::entity::binary_sensor::on_grid::state::on` | Yes | Ja | Shared reference checked |
| 11100 | 923343473 | `component::solaredge_modbus::entity::binary_sensor::on_grid::state::off` | No | Nej | Shared reference checked |
| 11101 | 923343472 | `component::solaredge_modbus::entity::binary_sensor::on_grid::name` | On grid | Ansluten till elnätet | Core-literal match |
| 11102 | 923343445 | `component::centriconnect::config::step::reconfigure::description` | Enter your CentriConnect/MyPropane device credentials. | Ange dina inloggningsuppgifter för CentriConnect/MyPropane-enheten. | Shared reference checked |
| 11103 | 923343444 | `component::centriconnect::config::step::reconfigure::data_description::username` | Your CentriConnect/MyPropane user ID | Ditt användar-ID för CentriConnect/MyPropane | Shared reference checked |
| 11104 | 923343443 | `component::centriconnect::config::step::reconfigure::data_description::password` | Your CentriConnect/MyPropane device authentication code | Din autentiseringskod för CentriConnect/MyPropane-enheten | Shared reference checked |
| 11105 | 923343442 | `component::centriconnect::config::step::reconfigure::data::username` | User ID | Användar-ID | Shared reference checked |
| 11106 | 923343441 | `component::centriconnect::config::step::reconfigure::data::password` | Device Authentication Code | Enhetsautentiseringskod | Shared reference checked |
| 11107 | 923343440 | `component::centriconnect::config::step::reauth_confirm::description` | Enter your CentriConnect/MyPropane device credentials. | Ange dina inloggningsuppgifter för CentriConnect/MyPropane-enheten. | Shared reference checked |
| 11108 | 923343439 | `component::centriconnect::config::step::reauth_confirm::data_description::username` | Your CentriConnect/MyPropane user ID | Ditt användar-ID för CentriConnect/MyPropane | Shared reference checked |
| 11109 | 923343438 | `component::centriconnect::config::step::reauth_confirm::data_description::password` | Your CentriConnect/MyPropane device authentication code | Din autentiseringskod för CentriConnect/MyPropane-enheten | Shared reference checked |
| 11110 | 923343437 | `component::centriconnect::config::step::reauth_confirm::data::username` | User ID | Användar-ID | Shared reference checked |
| 11111 | 923343436 | `component::centriconnect::config::step::reauth_confirm::data::password` | Device Authentication Code | Enhetsautentiseringskod | Shared reference checked |
| 11112 | 923343435 | `component::centriconnect::config::abort::wrong_device` | This CentriConnect/MyPropane device does not match the existing device ID. Please make sure you entered the credentials correctly. | Den här CentriConnect/MyPropane-enheten matchar inte det befintliga enhets-ID:t. Kontrollera att du har angett korrekta inloggningsuppgifter. | Core-literal match |
| 11113 | 923343434 | `component::centriconnect::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-owner follow-up open |
| 11114 | 923343433 | `component::centriconnect::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-owner follow-up open |
| 11115 | 923343346 | `component::solaredge_modbus::entity::sensor::temperature_max::name` | Maximum temperature | Högsta temperatur | Core-literal match |
| 11116 | 923343345 | `component::solaredge_modbus::entity::sensor::state_of_health::name` | State of health | Hälsostatus | Core-literal match |
| 11117 | 923343344 | `component::solaredge_modbus::entity::sensor::state_of_energy::name` | State of energy | Energistatus | Core-literal match |
| 11118 | 923343343 | `component::solaredge_modbus::entity::sensor::rated_energy::name` | Rated energy | Nominell energi | Core-literal match |
| 11119 | 923343342 | `component::solaredge_modbus::entity::sensor::max_discharge_power::name` | Maximum discharge power | Maximal urladdningseffekt | Core-literal match |
| 11120 | 923343341 | `component::solaredge_modbus::entity::sensor::max_discharge_peak_power::name` | Maximum discharge peak power | Maximal toppeffekt vid urladdning | Core-literal match |
| 11121 | 923343340 | `component::solaredge_modbus::entity::sensor::max_charge_power::name` | Maximum charge power | Maximal laddningseffekt | Core-literal match |
| 11122 | 923343339 | `component::solaredge_modbus::entity::sensor::max_charge_peak_power::name` | Maximum charge peak power | Maximal toppeffekt vid laddning | Core-literal match |
| 11123 | 923343338 | `component::solaredge_modbus::entity::sensor::energy_max::name` | Usable capacity | Användbar kapacitet | Core-literal match |
| 11124 | 923343337 | `component::solaredge_modbus::entity::sensor::energy_available::name` | Available energy | Tillgänglig energi | Core-literal match |
| 11125 | 923343336 | `component::solaredge_modbus::entity::sensor::battery_status::state::standby` | Standby | Viloläge | Shared reference checked |
| 11126 | 923343335 | `component::solaredge_modbus::entity::sensor::battery_status::state::preserve_charge` | Preserving charge | Bevarar laddning | Core-literal match |
| 11127 | 923343334 | `component::solaredge_modbus::entity::sensor::battery_status::state::power_saving` | Power saving | Energisparläge | Core-literal match |
| 11128 | 923343333 | `component::solaredge_modbus::entity::sensor::battery_status::state::off` | Off | Av | Shared reference checked |
| 11129 | 923343332 | `component::solaredge_modbus::entity::sensor::battery_status::state::init` | Initializing | Initierar | Core-literal match |
| 11130 | 923343331 | `component::solaredge_modbus::entity::sensor::battery_status::state::idle` | Idle | Inaktiv | Shared reference checked |
| 11131 | 923343330 | `component::solaredge_modbus::entity::sensor::battery_status::state::fault` | Fault | Fel | Core-literal match |
| 11132 | 923343329 | `component::solaredge_modbus::entity::sensor::battery_status::state::discharge` | Discharging | Laddar ur | Core-literal match |
| 11133 | 923343328 | `component::solaredge_modbus::entity::sensor::battery_status::state::charge` | Charging | Laddar | Core-literal match |
| 11134 | 923343327 | `component::solaredge_modbus::entity::sensor::battery_status::name` | Status | Status | Core-literal match |
| 11135 | 923335164 | `component::lunatone::entity::sensor::dali_line_status::state::ok` | OK | OK | Core-literal match |
| 11136 | 923335163 | `component::lunatone::entity::sensor::dali_line_status::state::not_reachable` | Not reachable | Inte nåbar | Core-literal match |
| 11137 | 923335162 | `component::lunatone::entity::sensor::dali_line_status::state::no_power` | Bus power failure | Strömavbrott på bussen | Core-literal match |
| 11138 | 923335161 | `component::lunatone::entity::sensor::dali_line_status::state::low_power` | Low bus power | Låg busseffekt | Core-literal match |
| 11139 | 923335160 | `component::lunatone::entity::sensor::dali_line_status::name` | Status | Status | Core-literal match |
| 11140 | 923335099 | `component::tailscale::entity::binary_sensor::connected_to_control::name` | Connected to control | Ansluten till kontroll | Core-literal match |
| 11141 | 923335094 | `component::lyric::entity::sensor::priority_status::state::vacation_hold` | Vacation hold | Semesterläge | Core-literal match |
| 11142 | 923335093 | `component::lyric::entity::sensor::priority_status::state::temporary_hold` | Temporary hold | Tillfällig åsidosättning | Core-literal match |
| 11143 | 923335092 | `component::lyric::entity::sensor::priority_status::state::permanent_hold` | Permanent hold | Permanent åsidosättning | Core-literal match |
| 11144 | 923335091 | `component::lyric::entity::sensor::priority_status::state::no_hold` | No hold | Ingen åsidosättning | Core-literal match |
| 11145 | 923335090 | `component::lyric::entity::sensor::priority_status::state::hold_until` | Hold until | Åsidosättning till | Core-literal match |
| 11146 | 923335089 | `component::lyric::entity::sensor::priority_status::name` | Priority status | Prioritetsstatus | Core-literal match |
| 11147 | 923335088 | `component::vicare::exceptions::quickmode_not_activated::message` | Unable to activate ViCare quickmode {quickmode}. Only one quickmode can be active at a time; another one may already be running. | Det gick inte att aktivera ViCare-snabbläget {quickmode}. Endast ett snabbläge kan vara aktivt åt gången; ett annat kan redan vara igång. | Core-literal match |
| 11148 | 923335087 | `component::vicare::entity::switch::quickmode_silent::name` | Silent | Tyst | Core-literal match |
| 11149 | 923335086 | `component::vicare::entity::switch::quickmode_forced_level_four::name` | Boost | Boost | Core-literal match |
| 11150 | 923335085 | `component::vicare::entity::switch::quickmode_eco::name` | Eco | Eko | Core-literal match |
| 11151 | 923335084 | `component::vicare::entity::switch::quickmode_comfort::name` | Intensive | Intensiv | Core-literal match |
| 11152 | 923334951 | `component::plugwise::exceptions::temperature_out_of_range::message` | Temperature must be between {min_temp} and {max_temp} {temperature_unit}. | Temperaturen måste vara mellan {min_temp} och {max_temp} {temperature_unit}. | Core-literal match |
| 11153 | 923334950 | `component::plugwise::entity::water_heater::dhw_temperature::name` | Domestic hot water | Tappvarmvatten | Core-literal match |
| 11154 | 923334888 | `component::mjpeg::exceptions::timeout_getting_image::message` | Timeout getting an image from {name}. | Tidsgränsen överskreds när en bild hämtades från {name}. | Core-literal match |
| 11155 | 923334887 | `component::mjpeg::exceptions::error_getting_image::message` | Error getting a new image from {name}. | Fel vid hämtning av ny bild från {name}. | Core-literal match |
| 11156 | 923334875 | `component::persang_infrared::config::step::user::title` | Set up Persang IR speaker | Konfigurera Persang IR-högtalare | Core-literal match |
| 11157 | 923334874 | `component::persang_infrared::config::step::user::description` | Select the infrared emitter entity to use for controlling your Persang speaker. | Välj den infraröda sändarentiteten som ska användas för att styra Persang-högtalaren. | Core-literal match |
| 11158 | 923334873 | `component::persang_infrared::config::step::user::data_description::infrared_emitter_entity_id` | The infrared emitter entity to use for sending commands. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Shared reference checked |
| 11159 | 923334872 | `component::persang_infrared::config::step::user::data::infrared_emitter_entity_id` | Infrared emitter | Infraröd sändare | Shared reference checked |
| 11160 | 923334871 | `component::persang_infrared::config::abort::no_emitters` | No infrared emitter entities found. Please set up an infrared device first. | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. | Shared reference checked |
| 11161 | 923334870 | `component::persang_infrared::config::abort::already_configured` | This Persang speaker has already been configured with this infrared emitter. | Den här Persang-högtalaren har redan konfigurerats med den här sändaren. | Core-literal match |
| 11162 | 923334728 | `component::sofar::entity::select::eps_control::state::turn_on_prohibit_cold_start` | Turn on, prohibit cold start | Slå på, förhindra kallstart | Core-literal match |
| 11163 | 923334727 | `component::sofar::entity::select::eps_control::state::turn_on_enable_cold_start` | Turn on, enable cold start | Slå på, aktivera kallstart | Core-literal match |
| 11164 | 923334726 | `component::sofar::entity::select::eps_control::state::turn_off` | Turn off | Slå av | Core-literal match |
| 11165 | 923334725 | `component::sofar::entity::select::eps_control::name` | EPS mode | EPS-läge | Core-literal match |
| 11166 | 923334724 | `component::sofar::entity::select::charger_use_mode::state::timing_mode` | Timing mode | Tidsstyrt läge | Core-literal match |
| 11167 | 923334723 | `component::sofar::entity::select::charger_use_mode::state::time_of_use` | Time of use | Användningstid | Core-literal match |
| 11168 | 923334722 | `component::sofar::entity::select::charger_use_mode::state::self_use` | Self use | Egenförbrukning | Core-literal match |
| 11169 | 923334721 | `component::sofar::entity::select::charger_use_mode::state::peak_cut_mode` | Peak cut mode | Effekttoppsbegränsning | Core-literal match |
| 11170 | 923334720 | `component::sofar::entity::select::charger_use_mode::state::passive_mode` | Passive mode | Passivt läge | Core-literal match |
| 11171 | 923334719 | `component::sofar::entity::select::charger_use_mode::state::off_grid_mode` | Off-grid mode | Ödriftsläge | Core-literal match |
| 11172 | 923334718 | `component::sofar::entity::select::charger_use_mode::state::generator_mode` | Generator mode | Generatorläge | Core-literal match |
| 11173 | 923334717 | `component::sofar::entity::select::charger_use_mode::state::feed_in_priority_mode` | Feed-in priority mode | Läge för prioriterad inmatning | Core-literal match |
| 11174 | 923334716 | `component::sofar::entity::select::charger_use_mode::name` | Charger use mode | Laddarens användningsläge | Core-literal match |
| 11175 | 923334592 | `component::smtp::services::send_message::fields::priority::name` | Priority | Prioritet | Core-literal match |
| 11176 | 923334591 | `component::smtp::services::send_message::fields::priority::description` | Priority of the email notification. Support for this setting varies between email clients. | Prioritet för e-postmeddelanden. Stödet för den här inställningen varierar mellan e-postklienter. | Core-literal match |
| 11177 | 923334590 | `component::smtp::selector::priority::options::normal` | Normal | Normal | Core-literal match |
| 11178 | 923334589 | `component::smtp::selector::priority::options::lowest` | Lowest | Lägsta | Core-literal match |
| 11179 | 923334588 | `component::smtp::selector::priority::options::low` | Low | Låg | Core-literal match |
| 11180 | 923334587 | `component::smtp::selector::priority::options::highest` | Highest | Högsta | Core-literal match |
| 11181 | 923334586 | `component::smtp::selector::priority::options::high` | High | Hög | Core-literal match |
| 11182 | 923334536 | `component::imou::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-owner follow-up open |
| 11183 | 923333293 | `component::solaredge_modbus::config::step::user::menu_options::tcp` | Modbus TCP | Modbus TCP | Shared reference checked |
| 11184 | 923333292 | `component::solaredge_modbus::config::step::user::menu_options::serial` | Serial port (Modbus RTU) | Seriell port (Modbus RTU) | Shared reference checked |
| 11185 | 923333291 | `component::solaredge_modbus::config::step::tcp::sections::more_options::name` | More options | Fler alternativ | Core-literal match |
| 11186 | 923333290 | `component::solaredge_modbus::config::step::tcp::sections::more_options::data_description::unit_id` | The Modbus device ID of the inverter, as configured on the inverter itself. The SolarEdge default is 1. | Modbus-enhets-ID för växelriktaren, så som det är konfigurerat på själva växelriktaren. SolarEdge-standardinställningen är 1. | Core-literal match |
| 11187 | 923333289 | `component::solaredge_modbus::config::step::tcp::sections::more_options::data::unit_id` | Device ID | Enhets-ID | Core-literal match |
| 11188 | 923333288 | `component::solaredge_modbus::config::step::tcp::description` | Set up an inverter reached over the network. | Konfigurera en växelriktare som nås via nätverket. | Core-literal match |
| 11189 | 923333287 | `component::solaredge_modbus::config::step::tcp::data_description::port` | The TCP port the inverter listens on for Modbus requests. The SolarEdge default is 1502. | TCP-porten som växelriktaren lyssnar på efter Modbus-förfrågningar. SolarEdges standardinställning är 1502. | Core-literal match |
| 11190 | 923333286 | `component::solaredge_modbus::config::step::tcp::data_description::host` | The hostname or IP address of your SolarEdge inverter. Modbus TCP has to be enabled on the inverter first, in the installer settings. | Värdnamnet eller IP-adressen för din SolarEdge-växelriktare. Modbus TCP måste först aktiveras på växelriktaren i installationsinställningarna. | Core-literal match |
| 11191 | 923333285 | `component::solaredge_modbus::config::step::tcp::data::port` | Port | Port | Shared reference checked |
| 11192 | 923333284 | `component::solaredge_modbus::config::step::tcp::data::host` | Host | Värd | Shared reference checked |
| 11193 | 923333283 | `component::solaredge_modbus::config::step::serial::sections::more_options::name` | More options | Fler alternativ | Shared reference checked |
| 11194 | 923333282 | `component::solaredge_modbus::config::step::serial::sections::more_options::data_description::unit_id` | The Modbus device ID of the inverter, as configured on the inverter itself. The SolarEdge default is 1. | Modbus-enhets-ID för växelriktaren, så som det är konfigurerat på själva växelriktaren. SolarEdge-standardinställningen är 1. | Shared reference checked |
| 11195 | 923333281 | `component::solaredge_modbus::config::step::serial::sections::more_options::data::unit_id` | Device ID | Enhets-ID | Shared reference checked |
| 11196 | 923333280 | `component::solaredge_modbus::config::step::serial::description` | Set up an inverter wired to this machine over RS485. | Konfigurera en växelriktare som är kopplad till den här maskinen via RS485. | Core-literal match |
| 11197 | 923333279 | `component::solaredge_modbus::config::step::serial::data_description::device` | Select a local serial port or a port shared over the network by a serial proxy. | Välj en lokal seriell port eller en port som delas över nätverket via en seriell proxy. | Shared reference checked |
| 11198 | 923333278 | `component::solaredge_modbus::config::step::serial::data_description::baudrate` | The baud rate of the RS485 bus, as configured on the inverter. The SolarEdge default is 115200. | Baudtalet för RS485-bussen, så som det är inställt på växelriktaren. SolarEdges standardvärde är 115200. | Core-literal match |
| 11199 | 923333277 | `component::solaredge_modbus::config::step::serial::data::device` | Serial port | Seriell port | Shared reference checked |
| 11200 | 923333276 | `component::solaredge_modbus::config::step::serial::data::baudrate` | Baud rate | Baudhastighet | Shared reference checked |
| 11201 | 923333275 | `component::solaredge_modbus::config::step::reconfigure::data_description::device` | Select a local serial port or a port shared over the network by a serial proxy. | Välj en lokal seriell port eller en port som delas över nätverket via en seriell proxy. | Shared reference checked |
| 11202 | 923333274 | `component::solaredge_modbus::config::step::reconfigure::data_description::baudrate` | The baud rate of the RS485 bus, as configured on the inverter. The SolarEdge default is 115200. | Baudtalet för RS485-bussen, så som det är inställt på växelriktaren. SolarEdges standardvärde är 115200. | Shared reference checked |
| 11203 | 923333273 | `component::solaredge_modbus::config::step::reconfigure::data::device` | Serial port | Seriell port | Shared reference checked |
| 11204 | 923333272 | `component::solaredge_modbus::config::step::reconfigure::data::baudrate` | Baud rate | Baudhastighet | Shared reference checked |
| 11205 | 923333266 | `component::update::exceptions::update_in_progress::message` | Update installation already in progress for {entity_id}. | Installation av uppdateringen för {entity_id} pågår redan. | Core-literal match |
| 11206 | 923333265 | `component::update::exceptions::unknown_version_to_skip::message` | Cannot skip an unknown version for {entity_id}. | Det går inte att hoppa över en okänd version för {entity_id}. | Core-literal match |
| 11207 | 923333264 | `component::update::exceptions::specific_version_not_supported::message` | Installing a specific version is not supported for {entity_id}. | Det går inte att installera en specifik version för {entity_id}. | Core-literal match |
| 11208 | 923333263 | `component::update::exceptions::skip_not_supported::message` | Skipping update is not supported for {entity_id}. | Det går inte att hoppa över uppdateringen för {entity_id}. | Core-literal match |
| 11209 | 923333262 | `component::update::exceptions::no_update_available_to_skip::message` | No update available to skip for {entity_id}. | Det finns ingen tillgänglig uppdatering att hoppa över för {entity_id}. | Core-literal match |
| 11210 | 923333261 | `component::update::exceptions::no_update_available::message` | No update available for {entity_id}. | Det finns ingen tillgänglig uppdatering för {entity_id}. | Core-literal match |
| 11211 | 923333260 | `component::update::exceptions::clear_skipped_not_supported::message` | Clearing skipped update is not supported for {entity_id}. | Det går inte att rensa den överhoppade uppdateringen för {entity_id}. | Core-literal match |
| 11212 | 923333259 | `component::update::exceptions::backup_not_supported::message` | Backup is not supported for {entity_id}. | Säkerhetskopiering stöds inte för {entity_id}. | Core-literal match |
| 11213 | 923333138 | `component::solaredge_modbus::entity::sensor::power_phase_c::name` | Power phase C | Effekt för fas C | Core-literal match |
| 11214 | 923333137 | `component::solaredge_modbus::entity::sensor::power_phase_b::name` | Power phase B | Effekt för fas B | Core-literal match |
| 11215 | 923333136 | `component::solaredge_modbus::entity::sensor::power_phase_a::name` | Power phase A | Effekt för fas A | Core-literal match |
| 11216 | 923333135 | `component::solaredge_modbus::entity::sensor::energy_imported_phase_c::name` | Energy imported phase C | Importerad energi för fas C | Core-literal match |
| 11217 | 923333134 | `component::solaredge_modbus::entity::sensor::energy_imported_phase_b::name` | Energy imported phase B | Importerad energi för fas B | Core-literal match |
| 11218 | 923333133 | `component::solaredge_modbus::entity::sensor::energy_imported_phase_a::name` | Energy imported phase A | Importerad energi för fas A | Core-literal match |
| 11219 | 923333132 | `component::solaredge_modbus::entity::sensor::energy_imported::name` | Energy imported | Importerad energi | Core-literal match |
| 11220 | 923333131 | `component::solaredge_modbus::entity::sensor::energy_exported_phase_c::name` | Energy exported phase C | Exporterad energi för fas C | Core-literal match |
| 11221 | 923333130 | `component::solaredge_modbus::entity::sensor::energy_exported_phase_b::name` | Energy exported phase B | Exporterad energi för fas B | Core-literal match |
| 11222 | 923333129 | `component::solaredge_modbus::entity::sensor::energy_exported_phase_a::name` | Energy exported phase A | Exporterad energi för fas A | Core-literal match |
| 11223 | 923333128 | `component::solaredge_modbus::entity::sensor::energy_exported::name` | Energy exported | Exporterad energi | Core-literal match |
| 11224 | 923333127 | `component::peblar::services::list_vehicle_tokens::name` | List autocharge vehicles | Lista fordon för automatisk laddning | Core-literal match |
| 11225 | 923333126 | `component::peblar::services::list_vehicle_tokens::fields::config_entry_id::name` | Peblar EV charger | Peblar EV-laddare | Core-literal match |
| 11226 | 923333125 | `component::peblar::services::list_vehicle_tokens::fields::config_entry_id::description` | The Peblar EV charger to list autocharge vehicles for. | Den Peblar-laddare som fordon för automatisk laddning ska listas för. | Core-literal match |
| 11227 | 923333124 | `component::peblar::services::list_vehicle_tokens::description` | Returns the vehicles configured in the charger's autocharge list. | Returnerar fordonen som är konfigurerade i laddarens lista för automatisk laddning. | Core-literal match |
| 11228 | 923333123 | `component::peblar::services::delete_vehicle_token::name` | Delete autocharge vehicle | Ta bort fordon för automatisk laddning | Core-literal match |
| 11229 | 923333122 | `component::peblar::services::delete_vehicle_token::fields::evcc_id::name` | EVCC ID | EVCC-ID | Core-literal match |
| 11230 | 923333121 | `component::peblar::services::delete_vehicle_token::fields::evcc_id::description` | The identifier of the vehicle to delete. | Identifieraren för det fordon som ska tas bort. | Core-literal match |
| 11231 | 923333120 | `component::peblar::services::delete_vehicle_token::fields::config_entry_id::name` | Peblar EV charger | Peblar EV-laddare | Core-literal match |
| 11232 | 923333119 | `component::peblar::services::delete_vehicle_token::fields::config_entry_id::description` | The Peblar EV charger to delete the vehicle from. | Den Peblar-laddare som fordonet ska tas bort från. | Core-literal match |
| 11233 | 923333118 | `component::peblar::services::delete_vehicle_token::description` | Deletes a vehicle from the charger's autocharge list. | Tar bort ett fordon från laddarens lista för automatisk laddning. | Core-literal match |
| 11234 | 923333117 | `component::peblar::services::add_vehicle_token::name` | Add autocharge vehicle | Lägg till fordon för automatisk laddning | Core-literal match |
| 11235 | 923333116 | `component::peblar::services::add_vehicle_token::fields::evcc_id::name` | EVCC ID | EVCC-ID | Core-literal match |
| 11236 | 923333115 | `component::peblar::services::add_vehicle_token::fields::evcc_id::description` | The identifier the vehicle presents to the charger. | Identifieraren som fordonet presenterar för laddaren. | Core-literal match |
| 11237 | 923333114 | `component::peblar::services::add_vehicle_token::fields::config_entry_id::name` | Peblar EV charger | Peblar EV-laddare | Core-literal match |
| 11238 | 923333113 | `component::peblar::services::add_vehicle_token::fields::config_entry_id::description` | The Peblar EV charger to add the vehicle to. | Den Peblar-laddare som fordonet ska läggas till i. | Core-literal match |
| 11239 | 923333112 | `component::peblar::services::add_vehicle_token::fields::alias::name` | Alias | Alias | Core-literal match |
| 11240 | 923333111 | `component::peblar::services::add_vehicle_token::fields::alias::description` | A human-readable label for this vehicle. | En läsbar etikett för det här fordonet. | Core-literal match |
| 11241 | 923333110 | `component::peblar::services::add_vehicle_token::description` | Adds a vehicle to the charger's autocharge list, so it is authorized to charge as soon as it is plugged in. | Lägger till ett fordon i laddarens lista för automatisk laddning så att det godkänns för laddning så snart det ansluts. | Core-literal match |
| 11242 | 923333109 | `component::peblar::exceptions::no_autocharge_hardware::message` | {charger} has no power line communication hardware, so it cannot use autocharge. | {charger} saknar hårdvara för kommunikation över kraftledningen och kan därför inte använda automatisk laddning. | Core-literal match |
| 11243 | 923333096 | `component::besen::entity::sensor::total_energy::name` | Total energy | Total energi | Core-literal match |
| 11244 | 923333095 | `component::besen::entity::sensor::session_energy::name` | Session energy | Energi för sessionen | Core-literal match |
| 11245 | 923333094 | `component::besen::entity::sensor::l3_voltage::name` | L3 voltage | Spänning för L3 | Core-literal match |
| 11246 | 923333093 | `component::besen::entity::sensor::l3_current::name` | L3 current | Ström för L3 | Core-literal match |
| 11247 | 923333092 | `component::besen::entity::sensor::l2_voltage::name` | L2 voltage | Spänning för L2 | Core-literal match |
| 11248 | 923333091 | `component::besen::entity::sensor::l2_current::name` | L2 current | Ström för L2 | Core-literal match |
| 11249 | 923333090 | `component::besen::entity::sensor::l1_voltage::name` | L1 voltage | Spänning för L1 | Core-literal match |
| 11250 | 923333089 | `component::besen::entity::sensor::l1_current::name` | L1 current | Ström för L1 | Core-literal match |
| 11251 | 923333088 | `component::besen::entity::sensor::internal_temperature::name` | Internal temperature | Intern temperatur | Core-literal match |
| 11252 | 923333087 | `component::besen::entity::sensor::external_temperature::name` | External temperature | Extern temperatur | Core-literal match |
| 11253 | 923333086 | `component::besen::entity::sensor::charging_power::name` | Charging power | Laddningseffekt | Core-literal match |
| 11254 | 923330435 | `component::victron_gx::config::step::ssdp_token_pairing::title` | Pair with GX device | Parkoppla med GX-enhet | Core-literal match |
| 11255 | 923330434 | `component::victron_gx::config::step::ssdp_token_pairing::description` | Enable pairing mode on the GX device before submitting:<br><br>- Via the GX user interface: **Settings** > **Integrations** > **MQTT Devices** > **Pairing mode**<br>- On GX devices without a built-in screen: Quickly double-press the built-in button<br><br>Pairing mode is active for 120 seconds. | Aktivera parkopplingsläget på GX-enheten innan du skickar in:<br><br>- Via GX-användargränssnittet: **Inställningar** > **Integrationer** > **MQTT-enheter** > **Parkopplingsläge**<br>- På GX-enheter utan inbyggd skärm: Tryck snabbt två gånger på den inbyggda knappen<br><br>Parkopplingsläget är aktivt i 120 sekunder. | Core-literal match |
| 11256 | 923330433 | `component::victron_gx::config::error::pairing_failed` | Token pairing failed. Ensure pairing mode is active on the GX device and try again. | Tokenparkopplingen misslyckades. Kontrollera att parkopplingsläget är aktivt på GX-enheten och försök igen. | Core-literal match |
| 11257 | 923329546 | `component::proxmoxve::entity::update::node_update::name` | Software update | Programuppdatering | Core-literal match |
| 11258 | 923327422 | `component::monzo::exceptions::invalid_api_response_with_details::message` | The Monzo API returned an invalid response. Enable debug logging for details. | Monzo-API:t returnerade ett ogiltigt svar. Aktivera felsökningsloggning för mer information. | Core-literal match |
| 11259 | 923327421 | `component::monzo::exceptions::invalid_api_response::message` | The Monzo API returned an invalid response. | Monzo-API:t returnerade ett ogiltigt svar. | Core-literal match |
| 11260 | 923321780 | `component::gatus::entity::sensor::dns_rcode::state::server_failure` | Server failure | Serverfel | Core-literal match |
| 11261 | 923321779 | `component::gatus::entity::sensor::dns_rcode::state::refused` | Refused | Avvisad | Core-literal match |
| 11262 | 923321778 | `component::gatus::entity::sensor::dns_rcode::state::not_implemented` | Not implemented | Inte implementerat | Core-literal match |
| 11263 | 923321777 | `component::gatus::entity::sensor::dns_rcode::state::non_existent_domain` | Non-existent domain | Icke-existerande domän | Core-literal match |
| 11264 | 923321776 | `component::gatus::entity::sensor::dns_rcode::state::no_error` | No error | Inget fel | Core-literal match |
| 11265 | 923321775 | `component::gatus::entity::sensor::dns_rcode::state::format_error` | Format error | Formatfel | Core-literal match |
| 11266 | 923321774 | `component::gatus::entity::sensor::dns_rcode::name` | DNS response code | DNS-svarskod | Core-literal match |
| 11267 | 923321255 | `component::knx::issues::entity_validation_error::title` | Invalid KNX entity configuration | Ogiltig KNX-entitetskonfiguration | Core-literal match |
| 11268 | 923321254 | `component::knx::issues::entity_validation_error::description` | The stored configuration of the following KNX {platform} entities is invalid, so they were not set up:<br><br>{entities}<br><br>Correct or delete them. Check the logs for details. | Den sparade konfigurationen för följande KNX {platform}-entiteter är ogiltig, så de har inte konfigurerats:<br><br>{entities}<br><br>Rätta till eller ta bort dem. Se loggarna för mer information. | Core-literal match |
| 11269 | 923321251 | `component::hue::entity::switch::motion_aware::name` | MotionAware | MotionAware | Core-literal match |
| 11270 | 923313446 | `component::mcp::config::step::hassio_confirm::title` | Model Context Protocol server via Home Assistant app | Model Context Protocol-server via Home Assistant-appen | Core-literal match |
| 11271 | 923313445 | `component::mcp::config::step::hassio_confirm::description` | Do you want to configure Home Assistant to connect to the Model Context Protocol server provided by the app {addon}? | Vill du konfigurera Home Assistant för att ansluta till Model Context Protocol-servern som tillhandahålls av appen: {addon}? | Core-literal match |
| 11272 | 923313444 | `component::mcp::config::abort::invalid_discovery_info` | Invalid discovery information received | Ogiltig upptäcktsinformation togs emot | Core-literal match |
| 11273 | 923310587 | `component::solaredge_modbus::config::step::zeroconf_confirm::title` | Discovered SolarEdge inverter | Upptäckt SolarEdge-växelriktare | Core-literal match |
| 11274 | 923310586 | `component::solaredge_modbus::config::step::zeroconf_confirm::description` | Do you want to set up {name} at {host}? | Vill du ställa in {name} på {host}? | Core-literal match |
| 11275 | 923310585 | `component::solaredge_modbus::config::abort::no_solaredge_device` | No SolarEdge inverter answers on that connection and device ID. | Ingen SolarEdge-växelriktare svarar på den anslutningen och enhets-ID:t. | Shared reference checked |
| 11276 | 923310584 | `component::solaredge_modbus::config::abort::no_serial_number` | The inverter did not report a serial number, which is needed to identify it. | Växelriktaren rapporterade inget serienummer, vilket behövs för att identifiera den. | Shared reference checked |
| 11277 | 923310583 | `component::solaredge_modbus::config::abort::ev_charger` | That device is a SolarEdge EV charger. It answers as an inverter, but serves no measurements over Modbus. | Den enheten är en SolarEdge-elbilsladdare. Den svarar som en växelriktare, men tillhandahåller inga mätvärden via Modbus. | Shared reference checked |
| 11278 | 923310582 | `component::solaredge_modbus::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference checked |
| 11279 | 923310157 | `component::solaredge_modbus::exceptions::wrong_inverter::message` | A different inverter is answering than the one this entry was set up for. Reconfigure the entry to point at the right device. | En annan växelriktare svarar än den som den här posten konfigurerades för. Konfigurera om posten så att den pekar mot rätt enhet. | Core-literal match |
| 11280 | 923310156 | `component::solaredge_modbus::exceptions::no_solaredge_device::message` | The configured Modbus device does not answer as a SolarEdge inverter. | Den konfigurerade Modbus-enheten svarar inte som en SolarEdge-växelriktare. | Core-literal match |
| 11281 | 923310155 | `component::solaredge_modbus::exceptions::measurements_unavailable::message` | The inverter did not report its measurements, so it is not yet known which sensors it offers. | Växelriktaren rapporterade inte sina mätningar, så det är ännu inte känt vilka sensorer den erbjuder. | Core-literal match |
| 11282 | 923310154 | `component::solaredge_modbus::exceptions::link_settings_in_use::message` | The inverter cannot be set up with these link settings: {error} | Växelriktaren kan inte konfigureras med dessa länkinställningar: {error} | Core-literal match |
| 11283 | 923310153 | `component::solaredge_modbus::exceptions::identity_unavailable::message` | The inverter did not report its identity, so it cannot be confirmed as the one this entry was set up for. | Växelriktaren rapporterade inte sin identitet, så det kan inte bekräftas att den är den som den här posten skapades för. | Core-literal match |
| 11284 | 923310152 | `component::solaredge_modbus::exceptions::communication_error::message` | An error occurred while communicating with the SolarEdge inverter: {error} | Ett fel uppstod vid kommunikation med SolarEdge-växelriktaren: {error} | Core-literal match |
| 11285 | 923310151 | `component::solaredge_modbus::entity::sensor::voltage_phase_cn::name` | Voltage phase C-N | Spänning mellan C och N | Core-literal match |
| 11286 | 923310150 | `component::solaredge_modbus::entity::sensor::voltage_phase_ca::name` | Voltage phase C-A | Spänning mellan C och A | Core-literal match |
| 11287 | 923310149 | `component::solaredge_modbus::entity::sensor::voltage_phase_bn::name` | Voltage phase B-N | Spänning mellan B och N | Core-literal match |
| 11288 | 923310148 | `component::solaredge_modbus::entity::sensor::voltage_phase_bc::name` | Voltage phase B-C | Spänning mellan B och C | Core-literal match |
| 11289 | 923310147 | `component::solaredge_modbus::entity::sensor::voltage_phase_an::name` | Voltage phase A-N | Spänning mellan A och N | Core-literal match |
| 11290 | 923310146 | `component::solaredge_modbus::entity::sensor::voltage_phase_ab::name` | Voltage phase A-B | Spänning mellan A och B | Core-literal match |
| 11291 | 923310145 | `component::solaredge_modbus::entity::sensor::vendor_status::name` | Vendor status | Leverantörsstatus | Source-owner follow-up open |
| 11292 | 923310144 | `component::solaredge_modbus::entity::sensor::inverter_status::state::throttled` | Throttled | Begränsad | Core-literal match |
| 11293 | 923310143 | `component::solaredge_modbus::entity::sensor::inverter_status::state::starting` | Starting | Startar | Core-literal match |
| 11294 | 923310142 | `component::solaredge_modbus::entity::sensor::inverter_status::state::standby` | Standby | Viloläge | Shared reference checked |
| 11295 | 923310141 | `component::solaredge_modbus::entity::sensor::inverter_status::state::sleeping` | Sleeping | Sover | Core-literal match |
| 11296 | 923310140 | `component::solaredge_modbus::entity::sensor::inverter_status::state::shutting_down` | Shutting down | Stänger av | Core-literal match |
| 11297 | 923310139 | `component::solaredge_modbus::entity::sensor::inverter_status::state::producing` | Producing | Producerar | Core-literal match |
| 11298 | 923310138 | `component::solaredge_modbus::entity::sensor::inverter_status::state::off` | Off | Av | Shared reference checked |
| 11299 | 923310137 | `component::solaredge_modbus::entity::sensor::inverter_status::state::fault` | Fault | Fel | Core-literal match |
| 11300 | 923310136 | `component::solaredge_modbus::entity::sensor::inverter_status::name` | Status | Status | Core-literal match |
| 11301 | 923310135 | `component::solaredge_modbus::entity::sensor::dc_voltage::name` | DC voltage | DC-spänning | Core-literal match |
| 11302 | 923310134 | `component::solaredge_modbus::entity::sensor::dc_power::name` | DC power | DC-effekt | Core-literal match |
| 11303 | 923310133 | `component::solaredge_modbus::entity::sensor::dc_current::name` | DC current | DC-ström | Core-literal match |
| 11304 | 923310132 | `component::solaredge_modbus::entity::sensor::current_phase_c::name` | Current phase C | Ström för fas C | Core-literal match |
| 11305 | 923310131 | `component::solaredge_modbus::entity::sensor::current_phase_b::name` | Current phase B | Ström för fas B | Core-literal match |
| 11306 | 923310130 | `component::solaredge_modbus::entity::sensor::current_phase_a::name` | Current phase A | Ström för fas A | Core-literal match |
| 11307 | 923310129 | `component::solaredge_modbus::config::step::user::sections::more_options::name` | More options | Fler alternativ | Source found in adjacent Core path |
| 11308 | 923310128 | `component::solaredge_modbus::config::step::user::sections::more_options::data_description::unit_id` | The Modbus device ID of the inverter, as configured on the inverter itself. The SolarEdge default is 1. | Modbus-enhets-ID för växelriktaren, så som det är konfigurerat på själva växelriktaren. SolarEdge-standardinställningen är 1. | Source found in adjacent Core path |
| 11309 | 923310127 | `component::solaredge_modbus::config::step::user::sections::more_options::data::unit_id` | Device ID | Enhets-ID | Source found in adjacent Core path |
| 11310 | 923310126 | `component::solaredge_modbus::config::step::user::description` | Connect to your SolarEdge inverter over Modbus to monitor your solar energy production locally. | Anslut till din SolarEdge-växelriktare via Modbus för att övervaka din solenergiproduktion lokalt. | Core-literal match |
| 11311 | 923310125 | `component::solaredge_modbus::config::step::user::data_description::port` | The TCP port the inverter listens on for Modbus requests. The SolarEdge default is 1502. | TCP-porten som växelriktaren lyssnar på efter Modbus-förfrågningar. SolarEdges standardinställning är 1502. | Source found in adjacent Core path |
| 11312 | 923310124 | `component::solaredge_modbus::config::step::user::data_description::host` | The hostname or IP address of your SolarEdge inverter. Modbus TCP has to be enabled on the inverter first, in the installer settings. | Värdnamnet eller IP-adressen för din SolarEdge-växelriktare. Modbus TCP måste först aktiveras på växelriktaren i installationsinställningarna. | Source found in adjacent Core path |
| 11313 | 923310123 | `component::solaredge_modbus::config::step::user::data::port` | Port | Port | Source-owner follow-up open |
| 11314 | 923310122 | `component::solaredge_modbus::config::step::user::data::host` | Host | Värd | Source-owner follow-up open |
| 11315 | 923310121 | `component::solaredge_modbus::config::step::reconfigure::sections::more_options::name` | More options | Fler alternativ | Shared reference checked |
| 11316 | 923310120 | `component::solaredge_modbus::config::step::reconfigure::sections::more_options::data_description::unit_id` | The Modbus device ID of the inverter, as configured on the inverter itself. The SolarEdge default is 1. | Modbus-enhets-ID för växelriktaren, så som det är konfigurerat på själva växelriktaren. SolarEdge-standardinställningen är 1. | Shared reference checked |
| 11317 | 923310119 | `component::solaredge_modbus::config::step::reconfigure::sections::more_options::data::unit_id` | Device ID | Enhets-ID | Shared reference checked |
| 11318 | 923310118 | `component::solaredge_modbus::config::step::reconfigure::description` | Update how this inverter is reached, for example after it moved to another address or its bus was rewired. | Uppdatera hur man ansluter till denna växelriktare, till exempel om den har flyttats till en annan adress eller om dess buss har dragits om. | Core-literal match |
| 11319 | 923310117 | `component::solaredge_modbus::config::step::reconfigure::data_description::port` | The TCP port the inverter listens on for Modbus requests. The SolarEdge default is 1502. | TCP-porten som växelriktaren lyssnar på efter Modbus-förfrågningar. SolarEdges standardinställning är 1502. | Shared reference checked |
| 11320 | 923310116 | `component::solaredge_modbus::config::step::reconfigure::data_description::host` | The hostname or IP address of your SolarEdge inverter. Modbus TCP has to be enabled on the inverter first, in the installer settings. | Värdnamnet eller IP-adressen för din SolarEdge-växelriktare. Modbus TCP måste först aktiveras på växelriktaren i installationsinställningarna. | Shared reference checked |
| 11321 | 923310115 | `component::solaredge_modbus::config::step::reconfigure::data::port` | Port | Port | Shared reference checked |
| 11322 | 923310114 | `component::solaredge_modbus::config::step::reconfigure::data::host` | Host | Värd | Shared reference checked |
| 11323 | 923310113 | `component::solaredge_modbus::config::error::no_solaredge_device` | No SolarEdge inverter answers on that connection and device ID. | Ingen SolarEdge-växelriktare svarar på den anslutningen och enhets-ID:t. | Core-literal match |
| 11324 | 923310112 | `component::solaredge_modbus::config::error::no_serial_number` | The inverter did not report a serial number, which is needed to identify it. | Växelriktaren rapporterade inget serienummer, vilket behövs för att identifiera den. | Core-literal match |
| 11325 | 923310111 | `component::solaredge_modbus::config::error::ev_charger` | That device is a SolarEdge EV charger. It answers as an inverter, but serves no measurements over Modbus. | Den enheten är en SolarEdge-elbilsladdare. Den svarar som en växelriktare, men tillhandahåller inga mätvärden via Modbus. | Core-literal match |
| 11326 | 923310110 | `component::solaredge_modbus::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference checked |
| 11327 | 923310109 | `component::solaredge_modbus::config::abort::wrong_device` | The inverter answering on that connection and device ID is a different one than this entry is set up for. | Växelriktaren som svarar på anslutningen och enhets-ID:t är inte den som posten är konfigurerad för. | Core-literal match |
| 11328 | 923310108 | `component::solaredge_modbus::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-owner follow-up open |
| 11329 | 923310107 | `component::solaredge_modbus::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference checked |
| 11330 | 923292992 | `component::abode::config::abort::wrong_account` | You must authenticate with the same Abode account that was originally configured. | Du måste autentisera med samma Abode-konto som ursprungligen konfigurerades. | Core-literal match |
| 11331 | 923292821 | `component::lichess::config::step::user::description` | Create a personal API token on the [Lichess API token page]({token_url}). Make sure the **Read preferences** permission is allowed. | Skapa en personlig API-token på [sidan för Lichess API-token]({token_url}). Se till att behörigheten **Läsinställningar** är aktiverad. | Core-literal match |
| 11332 | 923292816 | `component::peblar::entity::switch::socket_lock::name` | Keep socket locked | Håll uttaget låst | Core-literal match |
| 11333 | 923292815 | `component::peblar::entity::button::socket_unlock::name` | Unlock socket | Lås upp uttaget | Core-literal match |
| 11334 | 923292814 | `component::peblar::entity::binary_sensor::lock_state::name` | Socket lock | Uttagslås | Core-literal match |
| 11335 | 923292752 | `component::homeassistant::exceptions::oauth2_unknown_implementation::message` | The configured authentication method is no longer available, re-authentication required | Den konfigurerade autentiseringsmetoden är inte längre tillgänglig, omautentisering krävs | Core-literal match |
| 11336 | 923292751 | `component::homeassistant::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Shared reference checked |
| 11337 | 923292176 | `component::peblar::services::list_rfid_tokens::name` | List RFID tokens | Lista RFID-token | Core-literal match |
| 11338 | 923292175 | `component::peblar::services::list_rfid_tokens::fields::config_entry_id::name` | Peblar EV charger | Peblar EV-laddare | Core-literal match |
| 11339 | 923292174 | `component::peblar::services::list_rfid_tokens::fields::config_entry_id::description` | The Peblar EV charger to list RFID tokens for. | Den Peblar-laddare som RFID-token ska listas för. | Core-literal match |
| 11340 | 923292173 | `component::peblar::services::list_rfid_tokens::description` | Returns the RFID tokens configured in the charger's standalone authorization list. | Returnerar de RFID-token som är konfigurerade i laddarens fristående behörighetslista. | Core-literal match |
| 11341 | 923292172 | `component::peblar::services::delete_rfid_token::name` | Delete RFID token | Ta bort RFID-token | Core-literal match |
| 11342 | 923292171 | `component::peblar::services::delete_rfid_token::fields::uid::name` | UID | UID | Core-literal match |
| 11343 | 923292170 | `component::peblar::services::delete_rfid_token::fields::uid::description` | The unique identifier of the RFID token to delete. | Den unika identifieraren för den RFID-token som ska tas bort. | Core-literal match |
| 11344 | 923292169 | `component::peblar::services::delete_rfid_token::fields::config_entry_id::name` | Peblar EV charger | Peblar EV-laddare | Core-literal match |
| 11345 | 923292168 | `component::peblar::services::delete_rfid_token::fields::config_entry_id::description` | The Peblar EV charger to delete the RFID token from. | Den Peblar-laddare som RFID-token ska tas bort från. | Core-literal match |
| 11346 | 923292167 | `component::peblar::services::delete_rfid_token::description` | Deletes an RFID token from the charger's standalone authorization list. | Tar bort en RFID-token från laddarens fristående behörighetslista. | Core-literal match |
| 11347 | 923292166 | `component::peblar::services::add_rfid_token::name` | Add RFID token | Lägg till RFID-token | Core-literal match |
| 11348 | 923292165 | `component::peblar::services::add_rfid_token::fields::uid::name` | UID | UID | Core-literal match |
| 11349 | 923292164 | `component::peblar::services::add_rfid_token::fields::uid::description` | The unique identifier of the RFID token. | Den unika identifieraren för RFID-token. | Core-literal match |
| 11350 | 923292163 | `component::peblar::services::add_rfid_token::fields::description::name` | Description | Beskrivning | Core-literal match |
| 11351 | 923292162 | `component::peblar::services::add_rfid_token::fields::description::description` | A human-readable label for this RFID token. | En läsbar etikett för denna RFID-token. | Core-literal match |
| 11352 | 923292161 | `component::peblar::services::add_rfid_token::fields::config_entry_id::name` | Peblar EV charger | Peblar EV-laddare | Core-literal match |
| 11353 | 923292160 | `component::peblar::services::add_rfid_token::fields::config_entry_id::description` | The Peblar EV charger to add the RFID token to. | Den Peblar-laddare som RFID-token ska läggas till i. | Core-literal match |
| 11354 | 923292159 | `component::peblar::services::add_rfid_token::description` | Adds an RFID token to the charger's standalone authorization list. | Lägger till en RFID-token i laddarens fristående behörighetslista. | Core-literal match |
| 11355 | 923292158 | `component::peblar::exceptions::no_rfid_hardware::message` | {charger} has no RFID reader, so it has no standalone authorization list. | {charger} har ingen RFID-läsare och har därför ingen fristående behörighetslista. | Core-literal match |
| 11356 | 923287583 | `component::peblar::entity::select::led_brightness::state::off` | Off | Av | Shared reference checked |
| 11357 | 923287582 | `component::peblar::entity::select::led_brightness::state::medium` | Medium | Medel | Shared reference checked |
| 11358 | 923287581 | `component::peblar::entity::select::led_brightness::state::dim` | Dim | Dämpad | Core-literal match |
| 11359 | 923287580 | `component::peblar::entity::select::led_brightness::state::bright` | Bright | Ljus | Core-literal match |
| 11360 | 923287579 | `component::peblar::entity::select::led_brightness::state::automatic` | Auto | Auto | Shared reference checked |
| 11361 | 923287578 | `component::peblar::entity::select::led_brightness::name` | LED brightness | LED-ljusstyrka | Core-literal match |
| 11362 | 923287577 | `component::peblar::entity::select::buzzer_volume::state::off` | Off | Av | Shared reference checked |
| 11363 | 923287576 | `component::peblar::entity::select::buzzer_volume::state::medium` | Medium | Medel | Shared reference checked |
| 11364 | 923287575 | `component::peblar::entity::select::buzzer_volume::state::low_medium` | Low medium | Mellanlåg | Core-literal match |
| 11365 | 923287574 | `component::peblar::entity::select::buzzer_volume::state::low` | Low | Låg | Shared reference checked |
| 11366 | 923287573 | `component::peblar::entity::select::buzzer_volume::state::high` | High | Hög | Shared reference checked |
| 11367 | 923287572 | `component::peblar::entity::select::buzzer_volume::name` | Buzzer volume | Volym för summer | Core-literal match |
| 11368 | 923286668 | `component::peblar::entity::sensor::charge_current_limit_source::state::reserved` | Reserved | Reserverad | Core-literal match |
| 11369 | 923286667 | `component::peblar::entity::sensor::charge_current_limit_source::state::internal_power_limit` | Internal power limit | Intern effektgräns | Core-literal match |
| 11370 | 922974871 | `component::webostv::exceptions::screen_control_not_supported::message` | {name} does not support turning the screen on or off. | {name} stöder inte att slå på eller stänga av skärmen. | Core-literal match |
| 11371 | 922864682 | `component::google_sheets::exceptions::get_failed::message` | Failed to retrieve data from the Google Sheets document | Det gick inte att hämta data från Google Sheets-dokumentet | Core-literal match |
| 11372 | 922864681 | `component::google_sheets::exceptions::append_failed::message` | Failed to write data to the Google Sheets document | Det gick inte att skriva data till Google Sheets-dokumentet | Core-literal match |
| 11373 | 922554393 | `component::hassio::issues::issue_mount_mount_failed::fix_flow::step::mount_execute_remove::description` | Select **Submit** to remove the network storage `{reference}` from Home Assistant. Any data stored on the device itself is not affected, but automations, backups or apps relying on this storage will no longer have access to it.<br><br>You can add the network storage again later from [storage]({storage_url}). | Välj **Bekräfta** för att ta bort nätverkslagringen `{reference}` från Home Assistant. Data som lagras på själva enheten påverkas inte, men automatiseringar, säkerhetskopior eller appar som är beroende av denna lagring kommer inte längre att ha åtkomst till den.<br><br>Du kan lägga till nätverkslagringen igen senare från [lagring]({storage_url}). | Core-literal match |
| 11374 | 922536869 | `component::matter::entity::number::travel_time_up::name` | Travel time up | Gångtid upp | Core-literal match |
| 11375 | 922536868 | `component::matter::entity::number::travel_time_down::name` | Travel time down | Gångtid ner | Core-literal match |
| 11376 | 922536867 | `component::matter::entity::number::slat_rotation_time::name` | Slat rotation time | Rotationstid för lamell | Core-literal match |
| 11377 | 922536652 | `component::dlna_dmr::exceptions::request_error::message` | Error when calling device service for action {action}: {upnperror} | Fel vid anrop av enhetstjänst för åtgärd {action}: {upnperror} | Core-literal match |
| 11378 | 922536651 | `component::dlna_dmr::exceptions::request_connection_error::message` | Could not connect to device when calling service for action {action} | Det gick inte att ansluta till enheten när tjänsten anropades för åtgärden {action} | Core-literal match |
| 11379 | 922536615 | `component::knx::exceptions::device_trigger_invalid_config::message` | Invalid KNX telegram trigger configuration: {error} | Ogiltig konfiguration av KNX-telegramutlösare: {error} | Core-literal match |
| 11380 | 922096432 | `component::openevse::entity::sensor::status::state::vent_required` | Vent required | Ventilation krävs | Core-literal match |
| 11381 | 922096431 | `component::openevse::entity::sensor::status::state::stuck_relay` | Stuck relay | Reläet har fastnat | Core-literal match |
| 11382 | 922096430 | `component::openevse::entity::sensor::status::state::sleeping` | Sleeping | Sover | Core-literal match |
| 11383 | 922096429 | `component::openevse::entity::sensor::status::state::over_temperature` | Over temperature | Övertemperatur | Core-literal match |
| 11384 | 922096428 | `component::openevse::entity::sensor::status::state::not_connected` | Not connected | Inte ansluten | Core-literal match |
| 11385 | 922096427 | `component::openevse::entity::sensor::status::state::no_ground` | No ground | Ingen jord | Core-literal match |
| 11386 | 922096426 | `component::openevse::entity::sensor::status::state::gfci_self_test_failure` | GFCI self-test failure | Fel vid GFCI-självtest | Core-literal match |
| 11387 | 922096425 | `component::openevse::entity::sensor::status::state::gfci_fault` | GFCI fault | GFCI-fel | Core-literal match |
| 11388 | 922096424 | `component::openevse::entity::sensor::status::state::disabled` | Disabled | Inaktiverad | Core-literal match |
| 11389 | 922096423 | `component::openevse::entity::sensor::status::state::diode_check_failed` | Diode check failed | Diodkontroll misslyckades | Core-literal match |
| 11390 | 922096422 | `component::openevse::entity::sensor::status::state::connected` | Connected | Ansluten | Core-literal match |
| 11391 | 922096421 | `component::openevse::entity::sensor::status::state::charging` | Charging | Laddar | Core-literal match |
| 11392 | 922028730 | `component::neopool::config::step::reconfigure::title` | Reconfigure NeoPool Connection | Konfigurera om NeoPool-anslutningen | Core-literal match |
| 11393 | 922028729 | `component::neopool::config::step::reconfigure::description` | Update the connection settings for your NeoPool controller. | Uppdatera anslutningsinställningarna för din NeoPool-styrenhet. | Core-literal match |
| 11394 | 922028728 | `component::neopool::config::step::reconfigure::data_description::unit_id` | Modbus device address (1-247). Identifies the specific device on a shared bus. Most direct-connected devices use 1. Gateways may route requests to different addresses. | Modbus-enhetsadress (1–247). Identifierar den specifika enheten på en delad buss. De flesta direktanslutna enheter använder adress 1. Gateway-enheter kan dirigera förfrågningar till olika adresser. | Source found in adjacent Core path |
| 11395 | 922028727 | `component::neopool::config::step::reconfigure::data_description::port` | Standard Modbus TCP port (default: 502). Change only if your gateway uses a non-standard port. | Standardport för Modbus TCP, 502. Ändra bara om gatewayen använder en annan port. | Shared reference checked |
| 11396 | 922028726 | `component::neopool::config::step::reconfigure::data_description::modbus_framer` | Wire protocol used by the gateway. Select TCP for MBAP framing (default for Ethernet-native gateways). Select RTU for RTU framing tunnelled through a TCP socket, used by passthrough serial-to-TCP bridges like ESPHome's stream_server. | Protokollet som gatewayen använder. Välj TCP för MBAP-inramning, vilket är standard för Ethernet-baserade gatewayar. Välj RTU för RTU-inramning som tunnlas genom en TCP-socket. Det används av bryggor mellan serieport och TCP, till exempel ESPHomes stream_server. | Shared reference checked |
| 11397 | 922028725 | `component::neopool::config::step::reconfigure::data_description::host` | Enter the IP address of the Modbus TCP gateway connected to your pool controller. | Ange IP-adressen till Modbus TCP-gatewayen som är ansluten till poolstyrenheten. | Shared reference checked |
| 11398 | 922028724 | `component::neopool::config::step::reconfigure::data::unit_id` | Unit ID | Enhets-ID | Source found in adjacent Core path |
| 11399 | 922028723 | `component::neopool::config::step::reconfigure::data::port` | Port | Port | Shared reference checked |
| 11400 | 922028722 | `component::neopool::config::step::reconfigure::data::modbus_framer` | Modbus framer | Modbus-inramning | Shared reference checked |
| 11401 | 922028721 | `component::neopool::config::step::reconfigure::data::host` | Host | Värd | Shared reference checked |
| 11402 | 922028720 | `component::neopool::config::abort::serial_mismatch` | The device at this address has a different serial number than the one originally configured. | Enheten på den här adressen har ett annat serienummer än den enhet som ursprungligen konfigurerades. | Core-literal match |
| 11403 | 922028719 | `component::neopool::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-owner follow-up open |
| 11404 | 921985557 | `component::sofar::entity::button::rtc_sync::name` | RTC sync | RTC-synk | Core-literal match |
| 11405 | 921985556 | `component::sofar::entity::button::iv_curve_scan::name` | IV curve scan | IV-kurvskanning | Core-literal match |
| 11406 | 921717902 | `component::midea::entity::climate::climate::state_attributes::fan_mode::state::silent` | Silent | Tyst | Core-literal match |
| 11407 | 921717901 | `component::midea::entity::climate::climate::state_attributes::fan_mode::state::full` | Full | Full | Core-literal match |
| 11408 | 921478993 | `component::fronius::entity::switch::ac_power_limit_enabled::name` | AC power limiting | AC-effektbegränsning | Core-literal match |
| 11409 | 921478992 | `component::fronius::entity::number::ac_power_limit::name` | AC power limit | AC-effektgräns | Core-literal match |
| 11410 | 921297523 | `component::sofar::entity::sensor::voltage::name` | Voltage | Spänning | Core-literal match |
| 11411 | 921297522 | `component::sofar::entity::sensor::temperature::name` | Temperature | Temperatur | Core-literal match |
| 11412 | 921297521 | `component::sofar::entity::sensor::state_of_health::name` | State of health | Hälsotillstånd | Core-literal match |
| 11413 | 921297520 | `component::sofar::entity::sensor::state_of_charge::name` | State of charge | Laddningstillstånd | Core-literal match |
| 11414 | 921297519 | `component::sofar::entity::sensor::power::name` | Power | Effekt | Core-literal match |
| 11415 | 921297518 | `component::sofar::entity::sensor::current::name` | Current | Ström | Core-literal match |
| 11416 | 921297517 | `component::sofar::entity::sensor::charge_cycle::name` | Charge cycle | Laddningscykel | Core-literal match |
| 11417 | 921297516 | `component::sofar::device::pv_string::name` | PV string {number} | PV-sträng {number} | Core-literal match |
| 11418 | 921297515 | `component::sofar::device::battery::name` | Battery {number} | Batteri {number} | Core-literal match |
| 11419 | 921296995 | `component::matter::entity::switch::display::name` | Display | Display | Core-literal match |
| 11420 | 921275784 | `component::sofar::entity::sensor::offgrid_load_peak_ratio_l3::name` | Off-grid load peak ratio L3 | Off-grid topplast kvot L3 | Core-literal match |
| 11421 | 921275783 | `component::sofar::entity::sensor::offgrid_load_peak_ratio_l2::name` | Off-grid load peak ratio L2 | Off-grid topplast kvot L2 | Core-literal match |
| 11422 | 921275782 | `component::sofar::entity::sensor::offgrid_load_peak_ratio_l1::name` | Off-grid load peak ratio L1 | Off-grid topplast kvot L1 | Core-literal match |
| 11423 | 921275781 | `component::sofar::entity::sensor::offgrid_load_peak_ratio::name` | Off-grid load peak ratio | Off-grid topplast kvot | Core-literal match |
| 11424 | 921275311 | `component::gatus::config::step::user::data_description::username` | Optional username for HTTP Basic Authentication. | Valfritt användarnamn för HTTP Basic-autentisering. | Core-literal match |
| 11425 | 921275310 | `component::gatus::config::step::user::data_description::token` | Optional API token / Bearer token for authentication. | Valfri API-token/Bearer-token för autentisering. | Core-literal match |
| 11426 | 921275309 | `component::gatus::config::step::user::data_description::password` | Optional password for HTTP Basic Authentication. | Valfritt lösenord för HTTP Basic-autentisering. | Core-literal match |
| 11427 | 921275308 | `component::gatus::config::step::user::data::username` | Username | Användarnamn | Shared reference checked |
| 11428 | 921275307 | `component::gatus::config::step::user::data::token` | API key | API-nyckel | Shared reference checked |
| 11429 | 921275306 | `component::gatus::config::step::user::data::password` | Password | Lösenord | Shared reference checked |
| 11430 | 921275305 | `component::gatus::config::step::reconfigure::data_description::username` | Optional username for HTTP Basic Authentication. | Valfritt användarnamn för HTTP Basic-autentisering. | Shared reference checked |
| 11431 | 921275304 | `component::gatus::config::step::reconfigure::data_description::token` | Optional API token / Bearer token for authentication. | Valfri API-token/Bearer-token för autentisering. | Shared reference checked |
| 11432 | 921275303 | `component::gatus::config::step::reconfigure::data_description::password` | Optional password for HTTP Basic Authentication. | Valfritt lösenord för HTTP Basic-autentisering. | Shared reference checked |
| 11433 | 921275302 | `component::gatus::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference checked |
| 11434 | 921275301 | `component::gatus::config::step::reconfigure::data::token` | API key | API-nyckel | Shared reference checked |
| 11435 | 921275300 | `component::gatus::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference checked |
| 11436 | 921275299 | `component::gatus::config::step::reauth_confirm::description` | Please re-enter your credentials for Gatus. | Ange dina inloggningsuppgifter för Gatus igen. | Core-literal match |
| 11437 | 921275298 | `component::gatus::config::step::reauth_confirm::data_description::username` | Optional username for HTTP Basic Authentication. | Valfritt användarnamn för HTTP Basic-autentisering. | Shared reference checked |
| 11438 | 921275297 | `component::gatus::config::step::reauth_confirm::data_description::token` | Optional API token / Bearer token for authentication. | Valfri API-token/Bearer-token för autentisering. | Shared reference checked |
| 11439 | 921275296 | `component::gatus::config::step::reauth_confirm::data_description::password` | Optional password for HTTP Basic Authentication. | Valfritt lösenord för HTTP Basic-autentisering. | Shared reference checked |
| 11440 | 921275295 | `component::gatus::config::step::reauth_confirm::data::username` | Username | Användarnamn | Shared reference checked |
| 11441 | 921275294 | `component::gatus::config::step::reauth_confirm::data::token` | API key | API-nyckel | Shared reference checked |
| 11442 | 921275293 | `component::gatus::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference checked |
| 11443 | 921275292 | `component::gatus::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference checked |
| 11444 | 921275291 | `component::gatus::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-owner follow-up open |
| 11445 | 921275219 | `component::homematicip_cloud::entity::sensor::today_rain::name` | Today rain | Nederbörd i dag | Core-literal match |
| 11446 | 921275218 | `component::homematicip_cloud::entity::sensor::tilt_angle::name` | Tilt angle | Lutningsvinkel | Core-literal match |
| 11447 | 921275217 | `component::homematicip_cloud::entity::sensor::heating::name` | Heating | Värmer | Core-literal match |
| 11448 | 921275216 | `component::homematicip_cloud::entity::sensor::duty_cycle::name` | Duty cycle | Arbetscykel | Core-literal match |
| 11449 | 921275215 | `component::homematicip_cloud::entity::sensor::delta_temperature::name` | Delta temperature | Deltatemperatur | Core-literal match |
| 11450 | 921275214 | `component::homematicip_cloud::entity::sensor::channel_2_temperature::name` | Channel 2 temperature | Temperatur för kanal 2 | Core-literal match |
| 11451 | 921275213 | `component::homematicip_cloud::entity::sensor::channel_1_temperature::name` | Channel 1 temperature | Temperatur för kanal 1 | Core-literal match |
| 11452 | 921255163 | `component::neopool::entity::button::sync_time::name` | Synchronize device time | Synkronisera enhetens tid | Core-literal match |
| 11453 | 921255162 | `component::neopool::entity::button::reset_cell_partial::name` | Reset partial runtime counters | Återställ räknare för partiella körtider | Core-literal match |
| 11454 | 921255161 | `component::neopool::entity::button::escape::name` | Clear error messages | Rensa felmeddelanden | Core-literal match |
| 11455 | 921254570 | `component::gatus::entity::sensor::certificate_expiration::name` | Certificate expiration | Certifikatets utgångsdatum | Core-literal match |
| 11456 | 921252539 | `component::zhong_hong::issues::deprecated_yaml_import_issue_no_devices_found::title` | The {integration_title} YAML configuration could not be imported | YAML-konfigurationen för {integration_title} kunde inte importeras | Shared reference checked |
| 11457 | 921252538 | `component::zhong_hong::issues::deprecated_yaml_import_issue_no_devices_found::description` | Configuring {integration_title} using YAML is being removed, but the gateway at {host} did not report any air conditioners, so the configuration could not be imported.<br><br>Check that the air conditioners are switched on and addressed on the gateway, then restart Home Assistant. | Konfiguration av {integration_title} med YAML håller på att tas bort, men gatewayen på {host} rapporterade inga luftkonditioneringsenheter, så konfigurationen kunde inte importeras.<br><br>Kontrollera att luftkonditioneringsenheterna är påslagna och adresserade i gatewayen och starta sedan om Home Assistant. | Core-literal match |
| 11458 | 921252537 | `component::zhong_hong::issues::deprecated_yaml_import_issue_cannot_connect::title` | The {integration_title} YAML configuration could not be imported | YAML-konfigurationen för {integration_title} kunde inte importeras | Core-literal match |
| 11459 | 921252536 | `component::zhong_hong::issues::deprecated_yaml_import_issue_cannot_connect::description` | Configuring {integration_title} using YAML is being removed, but the gateway at {host} could not be reached, so the configuration could not be imported.<br><br>Check that the gateway is switched on and reachable at that address, then restart Home Assistant. If it is gone for good, remove the {domain} YAML configuration from your configuration.yaml file. | Konfiguration av {integration_title} med YAML håller på att tas bort, men gatewayen på {host} kunde inte nås, så konfigurationen kunde inte importeras.<br><br>Kontrollera att gatewayen är påslagen och kan nås på den adressen och starta sedan om Home Assistant. Om den är permanent borta tar du bort YAML-konfigurationen för {domain} från filen configuration.yaml. | Core-literal match |
| 11460 | 921252535 | `component::zhong_hong::exceptions::send_command_failed::message` | Failed to send {command} command to the ZhongHong gateway. | Det gick inte att skicka kommandot {command} till ZhongHong-gatewayen. | Core-literal match |
| 11461 | 921252534 | `component::zhong_hong::exceptions::no_devices_found::message` | The ZhongHong gateway at {host} did not report any air conditioners. | ZhongHong-gatewayen på {host} rapporterade inga luftkonditioneringsenheter. | Core-literal match |
| 11462 | 921252533 | `component::zhong_hong::exceptions::cannot_connect::message` | Failed to connect to the ZhongHong gateway at {host}. | Det gick inte att ansluta till ZhongHong-gatewayen på {host}. | Core-literal match |
| 11463 | 921252532 | `component::zhong_hong::config::step::user::data_description::port` | The port the gateway accepts connections on. This is 9999 unless it was changed on the gateway. | Porten som din gateway accepterar anslutningar på. Den är 9999 om den inte har ändrats. | Core-literal match |
| 11464 | 921252531 | `component::zhong_hong::config::step::user::data_description::host` | The hostname or IP address of the ZhongHong gateway on your network. | Värdnamnet eller IP-adressen för din ZhongHong-gateway i ditt nätverk. | Core-literal match |
| 11465 | 921252530 | `component::zhong_hong::config::step::user::data_description::gateway_address` | The address the gateway itself answers to, which is 1 from the factory. Change this only if the gateway was set to another address. | Adressen som din gateway själv svarar på; fabriksinställningen är 1. Ändra bara detta om din gateway har ställts in på en annan adress. | Core-literal match |
| 11466 | 921252529 | `component::zhong_hong::config::step::user::data::port` | Port | Port | Shared reference checked |
| 11467 | 921252528 | `component::zhong_hong::config::step::user::data::host` | Host | Värd | Shared reference checked |
| 11468 | 921252527 | `component::zhong_hong::config::step::user::data::gateway_address` | Gateway address | Gateway-adress | Core-literal match |
| 11469 | 921252526 | `component::zhong_hong::config::error::no_devices_found` | Connected to the gateway, but it did not report any air conditioners. | Ansluten till gatewayen, men den rapporterade inga luftkonditioneringsenheter. | Core-literal match |
| 11470 | 921252525 | `component::zhong_hong::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference checked |
| 11471 | 921252524 | `component::zhong_hong::config::abort::no_devices_found` | Connected to the gateway, but it did not report any air conditioners. | Ansluten till gatewayen, men den rapporterade inga luftkonditioneringsenheter. | Shared reference checked |
| 11472 | 921252523 | `component::zhong_hong::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference checked |
| 11473 | 921252522 | `component::zhong_hong::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference checked |
| 11474 | 921252344 | `component::homeassistant::config::abort::user_rejected_authorize` | Account linking rejected: {error} | Kontolänkning avvisades: {error} | Shared reference checked |
| 11475 | 921252343 | `component::homeassistant::config::abort::oauth_unauthorized` | OAuth authorization error while obtaining access token. | OAuth-auktoriseringsfel vid hämtning av åtkomsttoken. | Shared reference checked |
| 11476 | 921252342 | `component::homeassistant::config::abort::oauth_timeout` | Timeout while resolving the OAuth token. | Tidsgränsen överskreds när OAuth-token hämtades. | Shared reference checked |
| 11477 | 921252341 | `component::homeassistant::config::abort::oauth_implementation_unavailable` | No OAuth2 implementations are currently available. | Inga OAuth2-implementeringar finns tillgängliga för närvarande. | Shared reference checked |
| 11478 | 921252340 | `component::homeassistant::config::abort::oauth_failed` | Error while obtaining access token. | Fel vid hämtning av åtkomsttoken. | Shared reference checked |
| 11479 | 921252339 | `component::homeassistant::config::abort::oauth_error` | Received invalid token data. | Ogiltiga tokendata mottogs. | Shared reference checked |
| 11480 | 921252338 | `component::homeassistant::config::abort::no_url_available` | No URL available. For information about this error, [check the help section]({docs_url}) | Ingen webbadress är tillgänglig. [Se hjälpavsnittet]({docs_url}) för information om det här felet. | Shared reference checked |
| 11481 | 921252337 | `component::homeassistant::config::abort::missing_credentials` | The integration requires application credentials. | Integrationen kräver applikationsuppgifter. | Shared reference checked |
| 11482 | 921252336 | `component::homeassistant::config::abort::authorize_url_timeout` | Timeout while generating an authorization URL. | Tidsgränsen överskreds vid generering av en auktoriserings-URL. | Shared reference checked |
| 11483 | 921252256 | `component::velux::entity::cover::dual_roller_shutter_upper::state_attributes::speed::state::silent` | Silent | Tyst | Shared reference checked |
| 11484 | 921252255 | `component::velux::entity::cover::dual_roller_shutter_upper::state_attributes::speed::state::fast` | Fast | Snabb | Shared reference checked |
| 11485 | 921252254 | `component::velux::entity::cover::dual_roller_shutter_upper::state_attributes::speed::state::default` | Default | Standard | Shared reference checked |
| 11486 | 921252253 | `component::velux::entity::cover::dual_roller_shutter_lower::state_attributes::speed::state::silent` | Silent | Tyst | Shared reference checked |
| 11487 | 921252252 | `component::velux::entity::cover::dual_roller_shutter_lower::state_attributes::speed::state::fast` | Fast | Snabb | Shared reference checked |
| 11488 | 921252251 | `component::velux::entity::cover::dual_roller_shutter_lower::state_attributes::speed::state::default` | Default | Standard | Shared reference checked |
| 11489 | 921252250 | `component::velux::entity::cover::cover::state_attributes::speed::state::silent` | Silent | Tyst | Core-literal match |
| 11490 | 921252249 | `component::velux::entity::cover::cover::state_attributes::speed::state::fast` | Fast | Snabb | Shared reference checked |
| 11491 | 921252248 | `component::velux::entity::cover::cover::state_attributes::speed::state::default` | Default | Standard | Core-literal match |
| 11492 | 921252247 | `component::pushover::services::cancel::name` | Cancel emergency notification | Avbryt nödmeddelande | Core-literal match |
| 11493 | 921252246 | `component::pushover::services::cancel::fields::tag::name` | Tag | Tagg | Core-literal match |
| 11494 | 921252245 | `component::pushover::services::cancel::fields::tag::description` | Tag assigned to the message via the 'data.tags' field when sending. Omit to cancel all tracked emergency notifications for this account. | Tagg som tilldelas meddelandet via fältet ”data.tags” vid avsändning. Uteslut detta för att avbryta alla spårade nödmeddelanden för detta konto. | Core-literal match |
| 11495 | 921252244 | `component::pushover::services::cancel::fields::entry_id::name` | Pushover account | Pushover-konto | Core-literal match |
| 11496 | 921252243 | `component::pushover::services::cancel::fields::entry_id::description` | The Pushover account to cancel notifications for. | Pushover-kontot vars aviseringar ska avbrytas. | Core-literal match |
| 11497 | 921252242 | `component::pushover::services::cancel::description` | Cancels one or more Pushover emergency notifications (priority 2) that were previously sent through the targeted Pushover account. | Avbryter ett eller flera Pushover-nödmeddelanden (prioritet 2) som tidigare skickats via det valda Pushover-kontot. | Core-literal match |
| 11498 | 921245498 | `component::sofar::entity::sensor::waiting_ends::name` | Waiting ends | Väntan slutar | Source-owner follow-up open |
| 11499 | 921245497 | `component::opentherm_gw::entity::select::dhw_ovrd_mode::state::override_disabled` | Disabled | Inaktiverad | Shared reference checked |
| 11500 | 921245496 | `component::opentherm_gw::entity::select::dhw_ovrd_mode::state::force_on` | Force on | Tvinga på | Core-literal match |
| 11501 | 921245495 | `component::opentherm_gw::entity::select::dhw_ovrd_mode::state::force_off` | Force off | Tvinga av | Core-literal match |
| 11502 | 921245494 | `component::opentherm_gw::entity::select::dhw_ovrd_mode::name` | Hot water override | Varmvattenöverstyrning | Core-literal match |
| 11503 | 921245493 | `component::cloud::preview_features::stt_v2::name` | New speech-to-text engine | Ny tal-till-text-motor | Core-literal match |
| 11504 | 921245492 | `component::cloud::preview_features::stt_v2::enable_confirmation` | This feature is still in development and may change. While it's enabled, audio from your voice commands in supported languages is transcribed by Soniox instead of our current provider. | Denna funktion är fortfarande under utveckling och kan komma att ändras. När funktionen är aktiverad transkriberas ljudet från dina röstkommandon på de språk som stöds av Soniox istället för av vår nuvarande leverantör. | Core-literal match |
| 11505 | 921245491 | `component::cloud::preview_features::stt_v2::disable_confirmation` | Any Assistant currently using the new engine will go back to being transcribed by our current speech-to-text provider. | Tal för assistenter som använder den nya motorn transkriberas återigen av vår nuvarande tal-till-text-leverantör. | Core-literal match |
| 11506 | 921245490 | `component::cloud::preview_features::stt_v2::description` | We're testing a new speech-to-text engine for Home Assistant Link, the part of voice control that turns what you say into words. In our testing it copes better with accents, background noise, and languages other than English.<br><br>While this is enabled, any audio from your voice commands is processed by [Soniox](https://soniox.com/) rather than our current provider. This is relevant only to Assistants configured to use Home Assistant Link as an STT engine. It travels through a Nabu Casa proxy, which handles authentication and forwards it to the processing region closest to you. Nabu Casa doesn't process, store or log your audio at any point. Everything else about your voice pipeline stays the same, and you can turn this off again at any time. | Vi testar just nu en ny tal-till-text-motor för Home Assistant Link – den del av röststyrningen som omvandlar det du säger till text. Våra tester visar att den hanterar accenter, bakgrundsljud och andra språk än engelska bättre.<br><br>När denna funktion är aktiverad bearbetas allt ljud från dina röstkommandon av [Soniox](https://soniox.com/) istället för vår nuvarande leverantör. Detta gäller endast assistenter som är konfigurerade att använda Home Assistant Link som tal-till-text-motor. Ljudet går via en Nabu Casa-proxy, som hanterar autentiseringen och vidarebefordrar det till den bearbetningsregion som ligger närmast dig. Nabu Casa bearbetar, lagrar eller loggar inte ditt ljud vid något tillfälle. Allt annat i din röstpipeline förblir oförändrat, och du kan stänga av denna funktion när som helst. | Core-literal match |
| 11507 | 921231464 | `component::switchbot::entity::cover::roller_shade::state_attributes::speed::state::quiet` | Quiet | Tyst | Core-literal match |
| 11508 | 921231463 | `component::switchbot::entity::cover::roller_shade::state_attributes::speed::state::performance` | Performance | Prestanda | Core-literal match |
| 11509 | 921231462 | `component::switchbot::entity::cover::roller_shade::state_attributes::last_run_success::state::true` | OK | OK | Shared reference checked |
| 11510 | 921231461 | `component::switchbot::entity::cover::roller_shade::state_attributes::last_run_success::state::false` | Problem | Problem | Shared reference checked |
| 11511 | 921231218 | `component::simplisafe::entity::event::system_events::state_attributes::event_type::state::user_initiated_test` | User initiated test | Användarinitierat test | Core-literal match |
| 11512 | 921231217 | `component::simplisafe::entity::event::system_events::state_attributes::event_type::state::sensor_paired_and_named` | Sensor paired and named | Sensor parkopplad och namngiven | Core-literal match |
| 11513 | 921231216 | `component::simplisafe::entity::event::system_events::state_attributes::event_type::state::secret_alert_triggered` | Secret alert triggered | Hemlig larmsignal utlöst | Core-literal match |
| 11514 | 921231215 | `component::simplisafe::entity::event::system_events::state_attributes::event_type::state::device_test` | Device test | Enhetstest | Core-literal match |
| 11515 | 921231214 | `component::simplisafe::entity::event::system_events::state_attributes::event_type::state::automatic_test` | Automatic test | Automatiskt test | Core-literal match |
| 11516 | 921231213 | `component::simplisafe::entity::event::system_events::name` | System events | Systemhändelser | Core-literal match |
| 11517 | 921231212 | `component::simplisafe::entity::event::ring::state_attributes::event_type::state::ring` | Ring | Signal | Shared reference checked |
| 11518 | 921231211 | `component::simplisafe::entity::event::ring::name` | Ring | Ring | Core-literal match |
| 11519 | 921231210 | `component::simplisafe::entity::event::motion::state_attributes::event_type::state::camera_motion_detected` | Motion detected | Rörelse detekterad | Core-literal match |
| 11520 | 921231209 | `component::simplisafe::entity::event::motion::name` | Motion | Rörelse | Core-literal match |
| 11521 | 921231208 | `component::monarch_money::entity::sensor::owner::name` | Owner | Ägare | Core-literal match |
| 11522 | 921230906 | `component::vistapool::entity::switch::smart_mode_freeze::name` | Smart mode freeze | Frysning i smart läge | Core-literal match |
| 11523 | 921230905 | `component::vistapool::entity::switch::relay::name` | Relay {number} | Relä {number} | Core-literal match |
| 11524 | 921230904 | `component::vistapool::entity::switch::heating_climate::name` | Heating climate | Värmeklimat | Core-literal match |
| 11525 | 921230903 | `component::vistapool::entity::switch::filtration::name` | Filtration | Filtrering | Core-literal match |
| 11526 | 921230902 | `component::vistapool::entity::switch::electrolysis_cover::name` | Electrolysis cover | Elektrolysskydd | Core-literal match |
| 11527 | 921230901 | `component::vistapool::entity::switch::electrolysis_boost::name` | Electrolysis boost | Elektrolysförstärkning | Core-literal match |
| 11528 | 921223634 | `component::energyzero::exceptions::no_data::message` | No price data available for {date}. | Det finns inga prisuppgifter tillgängliga för {date}. | Core-literal match |
| 11529 | 921223633 | `component::energyzero::exceptions::invalid_range::message` | Invalid date range provided. End {end} must be after start {start}. | Det angivna datumintervallet är ogiltigt. Slutdatumet {end} måste ligga efter startdatumet {start}. | Core-literal match |
| 11530 | 921223618 | `component::nexia::entity::sensor::room_iq_temperature::name` | RoomIQ temperature | RoomIQ-temperatur | Core-literal match |
| 11531 | 921223617 | `component::nexia::entity::sensor::room_iq_humidity::name` | RoomIQ humidity | RoomIQ-luftfuktighet | Core-literal match |
| 11532 | 921223616 | `component::nexia::entity::sensor::room_iq_battery::name` | RoomIQ battery | RoomIQ-batteri | Core-literal match |
| 11533 | 921217210 | `component::hotspring::entity::light::light_zone::name` | Light zone {zone} | Ljuszon {zone} | Core-literal match |
| 11534 | 921209274 | `component::wattwaechter::exceptions::ota_failed::message` | Failed to start the firmware update. | Det gick inte att starta uppdateringen av den inbyggda programvaran. | Core-literal match |
| 11535 | 921209273 | `component::watergate::entity::number::auto_shut_off_volume_threshold::name` | Auto shut-off volume threshold | Tröskelvärde för volym vid automatisk avstängning | Core-literal match |
| 11536 | 921209272 | `component::watergate::entity::number::auto_shut_off_duration_threshold::name` | Auto shut-off duration threshold | Tröskelvärde för varaktighet för automatisk avstängning | Core-literal match |
| 11537 | 921209271 | `component::unifiprotect::exceptions::public_only_no_actions::message` | This action requires a local user; the entry is set up with an API key only. | Den här åtgärden kräver en lokal användare. Posten är konfigurerad med enbart en API-nyckel. | Core-literal match |
| 11538 | 921209270 | `component::unifiprotect::exceptions::cannot_connect::message` | Could not connect to the UniFi Protect console | Kunde inte ansluta till UniFi Protect-konsolen | Core-literal match |
| 11539 | 921209269 | `component::unifiprotect::config::step::user::menu_options::full` | API key and local user | Lokal användare och API-nyckel (full åtkomst) | Core-literal match |
| 11540 | 921209268 | `component::unifiprotect::config::step::user::menu_options::api_key` | API key only | Endast API-nyckel (begränsad funktionsuppsättning) | Core-literal match |
| 11541 | 921209267 | `component::unifiprotect::config::step::reconfigure_full::title` | Reconfigure UniFi Protect (local user) | Konfigurera om UniFi Protect (lokal användare) | Core-literal match |
| 11542 | 921209266 | `component::unifiprotect::config::step::reconfigure_full::description` | Update the configuration for your UniFi Protect device. Leave password and API key empty to keep your existing credentials. For more information: {local_user_documentation_url} | Uppdatera konfigurationen för din UniFi Protect-enhet. Lämna lösenord och API-nyckel tomma för att behålla dina befintliga inloggningsuppgifter. För mer information: {local_user_documentation_url} | Core-literal match |
| 11543 | 921209265 | `component::unifiprotect::config::step::reconfigure_full::data_description::verify_ssl` | Verify SSL certificate of the UniFi Protect device. | Verifiera SSL-certifikatet för UniFi Protect-enheten. | Shared reference checked |
| 11544 | 921209264 | `component::unifiprotect::config::step::reconfigure_full::data_description::username` | Username for your local (not cloud) user account. | Användarnamn för ditt lokala användarkonto, inte ditt molnkonto. | Shared reference checked |
| 11545 | 921209263 | `component::unifiprotect::config::step::reconfigure_full::data_description::port` | Port of your UniFi Protect device. | Port för din UniFi Protect-enhet. | Shared reference checked |
| 11546 | 921209262 | `component::unifiprotect::config::step::reconfigure_full::data_description::password` | Password for your local user account. Leave empty to keep your existing password. | Lösenord för ditt lokala användarkonto. Lämna tomt för att behålla ditt befintliga lösenord. | Shared reference checked |
| 11547 | 921209261 | `component::unifiprotect::config::step::reconfigure_full::data_description::host` | Hostname or IP address of your UniFi Protect device. | Värdnamn eller IP-adress för din UniFi Protect-enhet. | Shared reference checked |
| 11548 | 921209260 | `component::unifiprotect::config::step::reconfigure_full::data_description::api_key` | API key for your local user account. Leave empty to keep your existing API key. | API-nyckel för ditt lokala användarkonto. Lämna tomt för att behålla din befintliga API-nyckel. | Shared reference checked |
| 11549 | 921209259 | `component::unifiprotect::config::step::reconfigure_full::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference checked |
| 11550 | 921209258 | `component::unifiprotect::config::step::reconfigure_full::data::username` | Username | Användarnamn | Shared reference checked |
| 11551 | 921209257 | `component::unifiprotect::config::step::reconfigure_full::data::port` | Port | Port | Shared reference checked |
| 11552 | 921209256 | `component::unifiprotect::config::step::reconfigure_full::data::password` | Password | Lösenord | Shared reference checked |
| 11553 | 921209255 | `component::unifiprotect::config::step::reconfigure_full::data::host` | Host | Värd | Shared reference checked |
| 11554 | 921209254 | `component::unifiprotect::config::step::reconfigure_full::data::api_key` | API key | API-nyckel | Shared reference checked |
| 11555 | 921209253 | `component::unifiprotect::config::step::reconfigure_api_key::title` | Reconfigure UniFi Protect (API key) | Konfigurera om UniFi Protect (API-nyckel) | Core-literal match |
| 11556 | 921209252 | `component::unifiprotect::config::step::reconfigure_api_key::description` | Switch to (or update) API-key-only mode. Stored local user credentials are kept, so you can switch back at any time. Features the public Integration API does not offer yet are unavailable. For more information: {api_key_documentation_url} | Växla till eller uppdatera läget med enbart API-nyckel. Sparade inloggningsuppgifter för den lokala användaren behålls, så att du kan växla tillbaka när som helst. Funktioner som det offentliga integrations-API:t ännu inte erbjuder är inte tillgängliga. Mer information: {api_key_documentation_url} | Core-literal match |
| 11557 | 921209251 | `component::unifiprotect::config::step::reconfigure_api_key::data_description::verify_ssl` | Verify SSL certificate of the UniFi Protect device. | Verifiera SSL-certifikatet för UniFi Protect-enheten. | Shared reference checked |
| 11558 | 921209250 | `component::unifiprotect::config::step::reconfigure_api_key::data_description::port` | Port of your UniFi Protect device. | Port för din UniFi Protect-enhet. | Shared reference checked |
| 11559 | 921209249 | `component::unifiprotect::config::step::reconfigure_api_key::data_description::host` | Hostname or IP address of your UniFi Protect device. | Värdnamn eller IP-adress för din UniFi Protect-enhet. | Shared reference checked |
| 11560 | 921209248 | `component::unifiprotect::config::step::reconfigure_api_key::data_description::api_key` | API key from your UniFi OS Console. Only the public Integration API is used; some entities that require a local user are unavailable in this mode. | API-nyckel från din UniFi OS-konsol. Endast det offentliga integrations-API:t används. Vissa entiteter som kräver en lokal användare är inte tillgängliga i det här läget. | Shared reference checked |
| 11561 | 921209247 | `component::unifiprotect::config::step::reconfigure_api_key::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference checked |
| 11562 | 921209246 | `component::unifiprotect::config::step::reconfigure_api_key::data::port` | Port | Port | Shared reference checked |
| 11563 | 921209245 | `component::unifiprotect::config::step::reconfigure_api_key::data::host` | Host | Värd | Shared reference checked |
| 11564 | 921209244 | `component::unifiprotect::config::step::reconfigure_api_key::data::api_key` | API key | API-nyckel | Shared reference checked |
| 11565 | 921209243 | `component::unifiprotect::config::step::reconfigure::menu_options::reconfigure_full` | API key and local user | Lokal användare och API-nyckel (full åtkomst) | Core-literal match |
| 11566 | 921209242 | `component::unifiprotect::config::step::reconfigure::menu_options::reconfigure_api_key` | API key only | Endast API-nyckel (begränsad funktionsuppsättning) | Core-literal match |
| 11567 | 921209241 | `component::unifiprotect::config::step::reauth_api_key::title` | Reauth UniFi Protect (API key) | Återautentisera UniFi Protect (API-nyckel) | Core-literal match |
| 11568 | 921209240 | `component::unifiprotect::config::step::reauth_api_key::description` | Your API key seems to be missing or invalid. Enter a new API key from your UniFi OS Console. For more information: {api_key_documentation_url} | Din API-nyckel verkar saknas eller vara ogiltig. Ange en ny API-nyckel från din UniFi OS-konsol. Mer information: {api_key_documentation_url} | Core-literal match |
| 11569 | 921209239 | `component::unifiprotect::config::step::reauth_api_key::data_description::api_key` | API key from your UniFi OS Console. Only the public Integration API is used; some entities that require a local user are unavailable in this mode. | API-nyckel från din UniFi OS-konsol. Endast det offentliga integrations-API:t används. Vissa entiteter som kräver en lokal användare är inte tillgängliga i det här läget. | Shared reference checked |
| 11570 | 921209238 | `component::unifiprotect::config::step::reauth_api_key::data::api_key` | API key | API-nyckel | Shared reference checked |
| 11571 | 921209237 | `component::unifiprotect::config::step::full::title` | UniFi Protect setup (local user) | Konfiguration av UniFi Protect (lokal användare) | Core-literal match |
| 11572 | 921209236 | `component::unifiprotect::config::step::full::description` | You will need a local user created in your UniFi OS Console to log in with. Ubiquiti Cloud users will not work. For more information: {local_user_documentation_url} | Du behöver en lokal användare skapad i din UniFi OS-konsol för att kunna logga in. Ubiquiti Cloud-användare kommer inte att fungera. För mer information: {local_user_documentation_url} | Core-literal match |
| 11573 | 921209235 | `component::unifiprotect::config::step::full::data_description::verify_ssl` | Verify SSL certificate of the UniFi Protect device. | Verifiera SSL-certifikatet för UniFi Protect-enheten. | Core-literal match |
| 11574 | 921209234 | `component::unifiprotect::config::step::full::data_description::username` | Username for your local (not cloud) user account. | Användarnamn för ditt lokala användarkonto, inte ditt molnkonto. | Core-literal match |
| 11575 | 921209233 | `component::unifiprotect::config::step::full::data_description::port` | Port of your UniFi Protect device. | Port för din UniFi Protect-enhet. | Core-literal match |
| 11576 | 921209232 | `component::unifiprotect::config::step::full::data_description::password` | Password for your local user account. | Lösenord för ditt lokala användarkonto. | Core-literal match |
| 11577 | 921209231 | `component::unifiprotect::config::step::full::data_description::host` | Hostname or IP address of your UniFi Protect device. | Värdnamn eller IP-adress för din UniFi Protect-enhet. | Core-literal match |
| 11578 | 921209230 | `component::unifiprotect::config::step::full::data_description::api_key` | API key for your local user account. | API-nyckel för ditt lokala användarkonto. | Core-literal match |
| 11579 | 921209229 | `component::unifiprotect::config::step::full::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference checked |
| 11580 | 921209228 | `component::unifiprotect::config::step::full::data::username` | Username | Användarnamn | Shared reference checked |
| 11581 | 921209227 | `component::unifiprotect::config::step::full::data::port` | Port | Port | Shared reference checked |
| 11582 | 921209226 | `component::unifiprotect::config::step::full::data::password` | Password | Lösenord | Shared reference checked |
| 11583 | 921209225 | `component::unifiprotect::config::step::full::data::host` | Host | Värd | Shared reference checked |
| 11584 | 921209224 | `component::unifiprotect::config::step::full::data::api_key` | API key | API-nyckel | Shared reference checked |
| 11585 | 921209223 | `component::unifiprotect::config::step::discovery_full::title` | UniFi Protect discovered (local user) | UniFi Protect upptäckt (lokal användare) | Core-literal match |
| 11586 | 921209222 | `component::unifiprotect::config::step::discovery_full::description` | Do you want to set up {name} ({ip_address})? You will need a local user created in your UniFi OS Console to log in with. Ubiquiti Cloud users will not work. For more information: {local_user_documentation_url} | Vill du konfigurera {name} ({ip_address})? Du behöver en lokal användare som har skapats i din UniFi OS-konsol för att kunna logga in. Ubiquiti Cloud-användare fungerar inte. För mer information: {local_user_documentation_url} | Core-literal match |
| 11587 | 921209221 | `component::unifiprotect::config::step::discovery_full::data_description::verify_ssl` | Verify SSL certificate of the UniFi Protect device. | Verifiera SSL-certifikatet för UniFi Protect-enheten. | Shared reference checked |
| 11588 | 921209220 | `component::unifiprotect::config::step::discovery_full::data_description::username` | Username for your local (not cloud) user account. | Användarnamn för ditt lokala användarkonto, inte ditt molnkonto. | Shared reference checked |
| 11589 | 921209219 | `component::unifiprotect::config::step::discovery_full::data_description::port` | Port of your UniFi Protect device. | Port för din UniFi Protect-enhet. | Shared reference checked |
| 11590 | 921209218 | `component::unifiprotect::config::step::discovery_full::data_description::password` | Password for your local user account. | Lösenord för ditt lokala användarkonto. | Shared reference checked |
| 11591 | 921209217 | `component::unifiprotect::config::step::discovery_full::data_description::api_key` | API key for your local user account. | API-nyckel för ditt lokala användarkonto. | Shared reference checked |
| 11592 | 921209216 | `component::unifiprotect::config::step::discovery_full::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference checked |
| 11593 | 921209215 | `component::unifiprotect::config::step::discovery_full::data::username` | Username | Användarnamn | Shared reference checked |
| 11594 | 921209214 | `component::unifiprotect::config::step::discovery_full::data::port` | Port | Port | Shared reference checked |
| 11595 | 921209213 | `component::unifiprotect::config::step::discovery_full::data::password` | Password | Lösenord | Shared reference checked |
| 11596 | 921209212 | `component::unifiprotect::config::step::discovery_full::data::api_key` | API key | API-nyckel | Shared reference checked |
| 11597 | 921209211 | `component::unifiprotect::config::step::discovery_confirm::menu_options::discovery_full` | API key and local user | Lokal användare och API-nyckel (full åtkomst) | Core-literal match |
| 11598 | 921209210 | `component::unifiprotect::config::step::discovery_confirm::menu_options::discovery_api_key` | API key only | Endast API-nyckel (begränsad funktionsuppsättning) | Core-literal match |
| 11599 | 921209209 | `component::unifiprotect::config::step::discovery_api_key::title` | UniFi Protect discovered (API key) | UniFi Protect upptäckt (API-nyckel) | Core-literal match |
| 11600 | 921209208 | `component::unifiprotect::config::step::discovery_api_key::description` | Connect to {name} ({ip_address}) using only an API key. Features the public Integration API does not offer yet are unavailable. For more information: {api_key_documentation_url} | Anslut till {name} ({ip_address}) med enbart en API-nyckel. Funktioner som det offentliga integrations-API:t ännu inte erbjuder är inte tillgängliga. Mer information: {api_key_documentation_url} | Core-literal match |
| 11601 | 921209207 | `component::unifiprotect::config::step::discovery_api_key::data_description::port` | Port of your UniFi Protect device. | Port för din UniFi Protect-enhet. | Shared reference checked |
| 11602 | 921209206 | `component::unifiprotect::config::step::discovery_api_key::data_description::api_key` | API key from your UniFi OS Console. Only the public Integration API is used; some entities that require a local user are unavailable in this mode. | API-nyckel från din UniFi OS-konsol. Endast det offentliga integrations-API:t används. Vissa entiteter som kräver en lokal användare är inte tillgängliga i det här läget. | Shared reference checked |
| 11603 | 921209205 | `component::unifiprotect::config::step::discovery_api_key::data::port` | Port | Port | Shared reference checked |
| 11604 | 921209204 | `component::unifiprotect::config::step::discovery_api_key::data::api_key` | API key | API-nyckel | Shared reference checked |
| 11605 | 921209203 | `component::unifiprotect::config::step::api_key::title` | UniFi Protect setup (API key) | Konfiguration av UniFi Protect (API-nyckel) | Core-literal match |
| 11606 | 921209202 | `component::unifiprotect::config::step::api_key::description` | Connect using only an API key, without a local user. Features the public Integration API does not offer yet are unavailable. For more information: {api_key_documentation_url} | Anslut med enbart en API-nyckel, utan lokal användare. Funktioner som det offentliga integrations-API:t ännu inte erbjuder är inte tillgängliga. Mer information: {api_key_documentation_url} | Core-literal match |
| 11607 | 921209201 | `component::unifiprotect::config::step::api_key::data_description::verify_ssl` | Verify SSL certificate of the UniFi Protect device. | Verifiera SSL-certifikatet för UniFi Protect-enheten. | Core-literal match |
| 11608 | 921209200 | `component::unifiprotect::config::step::api_key::data_description::port` | Port of your UniFi Protect device. | Port för din UniFi Protect-enhet. | Core-literal match |
| 11609 | 921209199 | `component::unifiprotect::config::step::api_key::data_description::host` | Hostname or IP address of your UniFi Protect device. | Värdnamn eller IP-adress för din UniFi Protect-enhet. | Core-literal match |
| 11610 | 921209198 | `component::unifiprotect::config::step::api_key::data_description::api_key` | API key from your UniFi OS Console. Only the public Integration API is used; some entities that require a local user are unavailable in this mode. | API-nyckel från din UniFi OS-konsol. Endast det offentliga integrations-API:t används. Vissa entiteter som kräver en lokal användare är inte tillgängliga i det här läget. | Core-literal match |
| 11611 | 921209197 | `component::unifiprotect::config::step::api_key::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference checked |
| 11612 | 921209196 | `component::unifiprotect::config::step::api_key::data::port` | Port | Port | Shared reference checked |
| 11613 | 921209195 | `component::unifiprotect::config::step::api_key::data::host` | Host | Värd | Shared reference checked |
| 11614 | 921209194 | `component::unifiprotect::config::step::api_key::data::api_key` | API key | API-nyckel | Shared reference checked |
| 11615 | 921209193 | `component::roborock::entity::sensor::zeo_state::state::waiting_for_drying` | Waiting for drying | Väntar på torkning | Core-literal match |
| 11616 | 921209192 | `component::roborock::entity::sensor::zeo_state::state::updating` | Updating | Uppdaterar | Shared reference checked |
| 11617 | 921209191 | `component::roborock::entity::sensor::zeo_state::state::steam_caring` | Steam caring | Ångvård | Core-literal match |
| 11618 | 921209190 | `component::roborock::entity::sensor::zeo_state::state::pre_heating` | Preheating | Förvärmning | Core-literal match |
| 11619 | 921209189 | `component::roborock::entity::sensor::zeo_state::state::pre_heat_complete` | Preheating complete | Förvärmning klar | Core-literal match |
| 11620 | 921209188 | `component::roborock::entity::sensor::zeo_state::state::null` | Unknown | Okänd | Shared reference checked |
| 11621 | 921209187 | `component::roborock::entity::sensor::zeo_state::state::in_care` | In care | I vård | Core-literal match |
| 11622 | 921209186 | `component::roborock::entity::sensor::zeo_state::state::descaling` | Descaling | Avkalkning | Core-literal match |
| 11623 | 921209185 | `component::roborock::entity::sensor::zeo_state::state::cloth_ready` | Clothes ready | Kläder redo | Core-literal match |
| 11624 | 921209184 | `component::roborock::entity::sensor::q7_status::state::working_sleep` | Sleeping while working | Sover under arbete | Core-literal match |
| 11625 | 921209183 | `component::roborock::entity::sensor::q7_status::state::unknown` | Unknown | Okänd | Shared reference checked |
| 11626 | 921209182 | `component::roborock::entity::select::temperature::state::null` | Unknown | Okänd | Shared reference checked |
| 11627 | 921209181 | `component::roborock::entity::select::program::state::yoga` | Yoga wear | Yogakläder | Core-literal match |
| 11628 | 921209180 | `component::roborock::entity::select::program::state::wind_breaker` | Windbreaker | Vindjacka | Core-literal match |
| 11629 | 921209179 | `component::roborock::entity::select::program::state::timed_drying` | Timed drying | Tidsstyrd torkning | Core-literal match |
| 11630 | 921209178 | `component::roborock::entity::select::program::state::summer_quilt` | Summer quilt | Sommartäcke | Core-literal match |
| 11631 | 921209177 | `component::roborock::entity::select::program::state::suit` | Suit | Kostym | Core-literal match |
| 11632 | 921209176 | `component::roborock::entity::select::program::state::steam_care` | Steam care | Ångskötsel | Core-literal match |
| 11633 | 921209175 | `component::roborock::entity::select::program::state::sport_shoes` | Sport shoes | Sportskor | Core-literal match |
| 11634 | 921209174 | `component::roborock::entity::select::program::state::soaking` | Soaking | Blötläggning | Shared reference checked |
| 11635 | 921209173 | `component::roborock::entity::select::program::state::small_things_drying` | Small things drying | Torkning av småsaker | Core-literal match |
| 11636 | 921209172 | `component::roborock::entity::select::program::state::small_things` | Small things | Små saker | Core-literal match |
| 11637 | 921209171 | `component::roborock::entity::select::program::state::rack_drying` | Rack drying | Torkning på ställ | Core-literal match |
| 11638 | 921209170 | `component::roborock::entity::select::program::state::quilt_drying` | Quilt drying | Torkning av täcken | Core-literal match |
| 11639 | 921209169 | `component::roborock::entity::select::program::state::pet_care` | Pet care | Husdjursvård | Core-literal match |
| 11640 | 921209168 | `component::roborock::entity::select::program::state::outdoors` | Outdoors | Utomhus | Core-literal match |
| 11641 | 921209167 | `component::roborock::entity::select::program::state::outdoor_jackets` | Outdoor jackets | Utomhusjackor | Core-literal match |
| 11642 | 921209166 | `component::roborock::entity::select::program::state::mixing` | Mixed | Blandad | Core-literal match |
| 11643 | 921209165 | `component::roborock::entity::select::program::state::jeans` | Jeans | Jeans | Core-literal match |
| 11644 | 921209164 | `component::roborock::entity::select::program::state::flax` | Flax | Lin | Core-literal match |
| 11645 | 921209163 | `component::roborock::entity::select::program::state::descaling` | Descaling | Avkalkning | Shared reference checked |
| 11646 | 921209162 | `component::roborock::entity::select::program::state::deep_self_clean` | Deep self-clean | Djup självrengöring | Core-literal match |
| 11647 | 921209161 | `component::roborock::entity::select::program::state::bath_towel` | Bath towel | Badhandduk | Core-literal match |
| 11648 | 921209160 | `component::roborock::entity::select::mode::state::treatment` | Treatment | Behandling | Core-literal match |
| 11649 | 921209159 | `component::remember_the_milk::exceptions::invalid_auth::message` | Invalid authentication for the Remember The Milk API. | Ogiltig autentisering för Remember The Milk-API:t. | Core-literal match |
| 11650 | 921209158 | `component::remember_the_milk::exceptions::api_error::message` | Error communicating with the Remember The Milk API. | Fel vid kommunikation med Remember The Milk-API:t. | Core-literal match |
| 11651 | 921209157 | `component::remember_the_milk::config_subentries::list::step::user::description` | Enter a name for the new Remember The Milk list. | Ange ett namn på den nya listan i Remember The Milk. | Core-literal match |
| 11652 | 921209156 | `component::remember_the_milk::config_subentries::list::step::user::data_description::name` | A name for this To-do list. A new list with this name will also be created in your Remember The Milk account. | Ett namn för denna att-göra-lista. En ny lista med detta namn kommer också att skapas i ditt Remember The Milk-konto. | Core-literal match |
| 11653 | 921209155 | `component::remember_the_milk::config_subentries::list::step::user::data::name` | Name | Namn | Shared reference checked |
| 11654 | 921209154 | `component::remember_the_milk::config_subentries::list::step::reconfigure::description` | Rename the To-do list. | Byt namn på att-göra-listan. | Core-literal match |
| 11655 | 921209153 | `component::remember_the_milk::config_subentries::list::step::reconfigure::data_description::name` | The new name for this To-do list. The list will also be renamed in your Remember The Milk account. | Det nya namnet för denna att-göra-lista. Listan kommer också att byta namn i ditt Remember The Milk-konto. | Core-literal match |
| 11656 | 921209152 | `component::remember_the_milk::config_subentries::list::step::reconfigure::data::name` | Name | Namn | Shared reference checked |
| 11657 | 921209151 | `component::remember_the_milk::config_subentries::list::initiate_flow::user` | Add list | Lägg till lista | Core-literal match |
| 11658 | 921209150 | `component::remember_the_milk::config_subentries::list::error::unknown` | Unexpected error | Oväntat fel | Shared reference checked |
| 11659 | 921209149 | `component::remember_the_milk::config_subentries::list::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference checked |
| 11660 | 921209148 | `component::remember_the_milk::config_subentries::list::entry_type` | List | Lista | Core-literal match |
| 11661 | 921209147 | `component::remember_the_milk::config_subentries::list::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-owner follow-up open |
| 11662 | 921209146 | `component::remember_the_milk::config_subentries::list::abort::entry_not_loaded` | The Remember The Milk account must be loaded before adding or renaming a list. | Remember The Milk-kontot måste läsas in innan du lägger till eller byter namn på en lista. | Core-literal match |
| 11663 | 921209145 | `component::remember_the_milk::config_subentries::list::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference checked |
| 11664 | 921209144 | `component::neopool::options::step::init::data_description::use_cover_sensor` | Enables the hydrolysis cover reduction switch. | Aktiverar omkopplaren för reducering av hydrolysskydd. | Core-literal match |
| 11665 | 921209143 | `component::neopool::options::step::init::data_description::use_aux4` | Creates a switch entity for this auxiliary relay output. | Skapar en brytarentitet för denna hjälpreläutgång. | Shared reference checked |
| 11666 | 921209142 | `component::neopool::options::step::init::data_description::use_aux3` | Creates a switch entity for this auxiliary relay output. | Skapar en brytarentitet för denna hjälpreläutgång. | Shared reference checked |
| 11667 | 921209141 | `component::neopool::options::step::init::data_description::use_aux2` | Creates a switch entity for this auxiliary relay output. | Skapar en brytarentitet för denna hjälpreläutgång. | Shared reference checked |
| 11668 | 921209140 | `component::neopool::options::step::init::data_description::use_aux1` | Creates a switch entity for this auxiliary relay output. | Skapar en brytarentitet för denna hjälpreläutgång. | Core-literal match |
| 11669 | 921209139 | `component::neopool::options::step::init::data::use_cover_sensor` | Enable pool cover options | Aktivera alternativ för poolöverdrag | Core-literal match |
| 11670 | 921209138 | `component::neopool::options::step::init::data::use_aux4` | Enable Aux4 Relay | Aktivera Aux4-relä | Core-literal match |
| 11671 | 921209137 | `component::neopool::options::step::init::data::use_aux3` | Enable Aux3 Relay | Aktivera Aux3-relä | Core-literal match |
| 11672 | 921209136 | `component::neopool::options::step::init::data::use_aux2` | Enable Aux2 Relay | Aktivera Aux2-relä | Core-literal match |
| 11673 | 921209135 | `component::neopool::options::step::init::data::use_aux1` | Enable Aux1 Relay | Aktivera Aux1-relä | Core-literal match |
| 11674 | 921209134 | `component::neopool::exceptions::filtvalve_interval_not_set::message` | No backwash duration is configured. Set the backwash duration first, then start the backwash. | Ingen backspolningstid är konfigurerad. Ställ in backspolningens varaktighet först och starta sedan backspolningen. | Core-literal match |
| 11675 | 921209133 | `component::neopool::exceptions::filtvalve_in_auto_mode::message` | The backwash valve is currently in automatic mode. Change the mode to manual first to start or stop a backwash directly. | Backspolningsventilen är för närvarande inställd på automatiskt läge. Ställ först in den på manuellt läge för att direkt starta eller stoppa en backspolning. | Core-literal match |
| 11676 | 921209132 | `component::neopool::exceptions::filtration_not_manual_mode::message` | Filtration can only be switched on or off when the controller is in manual filtration mode. Change the filtration mode to Manual first. | Filtrering kan endast slås på eller av när styrenheten är i manuellt filtreringsläge. Ändra först filtreringsläget till Manuellt. | Core-literal match |
| 11677 | 921209131 | `component::neopool::exceptions::filtration_boost_active::message` | Filtration cannot be switched on or off while boost mode is active. Turn off boost mode first. | Filtrering kan inte slås på eller av medan boostläget är aktivt. Stäng av boostläget först. | Core-literal match |
| 11678 | 921209130 | `component::neopool::entity::switch::uv_mode::name` | UV mode | UV-läge | Core-literal match |
| 11679 | 921209129 | `component::neopool::entity::switch::smart_anti_freeze::name` | Smart antifreeze | Smart frostskydd | Core-literal match |
| 11680 | 921209128 | `component::neopool::entity::switch::hidro_temp_shutdown::name` | Enable hydrolysis shutdown on high temperature | Aktivera hydrolysavstängning vid hög temperatur | Core-literal match |
| 11681 | 921209127 | `component::neopool::entity::switch::hidro_cover_enable::name` | Enable cover reduction (when covered) | Aktivera täckningsreducering (vid täckning) | Core-literal match |
| 11682 | 921209126 | `component::neopool::entity::switch::filt_manual_state::name` | Filtration | Filtrering | Core-literal match |
| 11683 | 921209125 | `component::neopool::entity::switch::clima_onoff::name` | Climate mode for heating | Klimatläge för uppvärmning | Core-literal match |
| 11684 | 921209124 | `component::neopool::entity::switch::backwash::name` | Backwash | Backspolning | Core-literal match |
| 11685 | 921209123 | `component::neopool::entity::switch::aux::name` | Auxiliary relay {number} | Hjälprelä {number} | Core-literal match |
| 11686 | 921209122 | `component::iseo_argo_ble::exceptions::lock_rejected_identity::message` | Lock rejected the identity. Ensure the UUID is registered in the Argo app. | Låset avvisade identiteten. Se till att UUID:t är registrerat i Argo-appen. | Core-literal match |
| 11687 | 921209121 | `component::iseo_argo_ble::exceptions::lock_not_supported::message` | Manual locking is not supported by this device. The lock will automatically re-latch after being opened. | Manuell låsning stöds inte av den här enheten. Låset låses automatiskt igen efter att det öppnats. | Core-literal match |
| 11688 | 921209120 | `component::iseo_argo_ble::exceptions::device_not_found::message` | Could not find ISEO lock {address}. Make sure it is powered on and within Bluetooth range. | Det gick inte att hitta ISEO-låset {address}. Kontrollera att det är påslaget och befinner sig inom Bluetooth-räckvidden. | Core-literal match |
| 11689 | 921209119 | `component::iseo_argo_ble::exceptions::cannot_connect::message` | Could not connect to the lock. | Kunde inte ansluta till låset. | Core-literal match |
| 11690 | 921209118 | `component::iseo_argo_ble::config::step::user::description` | Select your lock from the list of nearby ISEO locks, sorted by signal strength. If your lock is not listed, make sure it is powered on and within Bluetooth range, then select **Submit** to scan again. | Välj ditt lås från listan över ISEO-lås i närheten, sorterade efter signalstyrka. Om ditt lås inte finns med i listan ska du kontrollera att det är påslaget och befinner sig inom Bluetooth-räckvidd. Välj sedan ”Bekräfta” för att söka igen. | Core-literal match |
| 11691 | 921209117 | `component::iseo_argo_ble::config::step::user::data_description::address` | Select the ISEO lock to set up. | Välj det ISEO-lås som ska konfigureras. | Core-literal match |
| 11692 | 921209116 | `component::iseo_argo_ble::config::step::user::data::address` | Device | Enhet | Shared reference checked |
| 11693 | 921209115 | `component::iseo_argo_ble::config::step::gw_register::title` | Register gateway | Registrera gateway | Core-literal match |
| 11694 | 921209114 | `component::iseo_argo_ble::config::step::gw_register::description` | To register Home Assistant as a Gateway:<br><br>**Warning:** Close the ARGO app before selecting **Submit**.<br><br>1. Select **Submit** below.<br>2. **Within 30 seconds**, scan your physical **Master Card** on the lock.<br><br>The lock will blink green once the card is read successfully. | Så här registrerar du Home Assistant som gateway:<br><br>**Varning:** Stäng ARGO-appen innan du klickar på Bekräfta.<br><br>1. Klicka på **Bekräfta** nedan.<br>2. **Inom 30 sekunder** ska du skanna ditt fysiska **Master-kort** mot låset.<br><br>Låset blinkar grönt när kortet har lästs in. | Core-literal match |
| 11695 | 921209113 | `component::iseo_argo_ble::config::step::bluetooth_confirm::title` | ISEO lock discovered | ISEO-lås upptäckt | Core-literal match |
| 11696 | 921209112 | `component::iseo_argo_ble::config::step::bluetooth_confirm::description` | Found a new ISEO lock nearby: **{name}**.<br><br>Select **Submit** to begin setup. | Hittade ett nytt ISEO-lås i närheten: **{name}**.<br><br>Klicka på **Bekräfta** för att påbörja installationen. | Core-literal match |
| 11697 | 921209111 | `component::iseo_argo_ble::config::flow_title` | {name} | {name} | Core-literal match |
| 11698 | 921209110 | `component::iseo_argo_ble::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference checked |
| 11699 | 921209109 | `component::iseo_argo_ble::config::error::cannot_connect` | Could not connect to the lock. Check it is powered on and within Bluetooth range. | Det gick inte att ansluta till låset. Kontrollera att det är påslaget och befinner sig inom Bluetooth-räckvidd. | Core-literal match |
| 11700 | 921209108 | `component::iseo_argo_ble::config::error::auth_failed` | The lock rejected the request. Make sure the Argo app is closed, then try again — scan a valid Master Card on the lock (the LED will blink green on success). | Låset avvisade begäran. Se till att Argo-appen är stängd och försök sedan igen – skanna ett giltigt Master-kort mot låset (LED-lampan blinkar grönt om det lyckas). | Core-literal match |
| 11701 | 921209107 | `component::iseo_argo_ble::config::abort::not_iseo_device` | This device does not appear to be an ISEO lock. | Den här enheten verkar inte vara ett ISEO-lås. | Core-literal match |
| 11702 | 921209106 | `component::iseo_argo_ble::config::abort::no_devices_found` | No devices found on the network | Inga enheter hittades i nätverket | Shared reference checked |
| 11703 | 921209105 | `component::iseo_argo_ble::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference checked |
| 11704 | 921209104 | `component::airgradient::exceptions::unsupported_error::message` | The Airgradient device does not support this operation: {error} | Airgradient-enheten stöder inte den här åtgärden: {error} | Core-literal match |
| 11705 | 921209103 | `component::airgradient::exceptions::forbidden_error::message` | The Airgradient device currently rejects local changes: {error} | Airgradient-enheten avvisar för närvarande lokala ändringar: {error} | Core-literal match |
| 11706 | 921209102 | `component::airgradient::exceptions::busy_error::message` | The Airgradient device is busy. Retry the operation later: {error} | Airgradient-enheten är upptagen. Försök igen senare: {error} | Core-literal match |
| 11707 | 921209101 | `component::airgradient::entity::switch::cloud_connection::name` | Cloud connection | Molnanslutning | Core-literal match |
| 11708 | 921209100 | `component::airgradient::entity::switch::buzzer_enabled::name` | Buzzer | Summer | Core-literal match |
| 11709 | 921209099 | `component::airgradient::entity::sensor::pm50_count::name` | PM5 particle count | PM5-partikelantal | Core-literal match |
| 11710 | 921209098 | `component::airgradient::entity::sensor::pm10_count::name` | PM10 particle count | PM10-partikelantal | Core-literal match |
| 11711 | 921209097 | `component::airgradient::entity::sensor::pm02_count::name` | PM2.5 particle count | Antal PM2,5-partiklar | Core-literal match |
| 11712 | 921209096 | `component::airgradient::entity::sensor::pm01_count::name` | PM1 particle count | PM1-partikelantal | Core-literal match |
| 11713 | 921209095 | `component::airgradient::entity::sensor::pm005_count::name` | PM0.5 particle count | Antal PM0,5-partiklar | Core-literal match |
| 11714 | 921209094 | `component::airgradient::entity::sensor::charge_voltage::name` | Input voltage | Ingångsspänning | Core-literal match |
| 11715 | 921209093 | `component::airgradient::entity::sensor::battery_voltage::name` | Battery voltage | Batterispänning | Core-literal match |
| 11716 | 921209092 | `component::airgradient::entity::sensor::battery_percentage::name` | Battery percentage | Batteriprocent | Core-literal match |
| 11717 | 921209091 | `component::airgradient::entity::select::touch_led_intensity::state::off` | Off | Av | Shared reference checked |
| 11718 | 921209090 | `component::airgradient::entity::select::touch_led_intensity::state::dim` | Dim | Dämpad | Core-literal match |
| 11719 | 921209089 | `component::airgradient::entity::select::touch_led_intensity::state::bright` | Bright | Ljus | Core-literal match |
| 11720 | 921209088 | `component::airgradient::entity::select::touch_led_intensity::name` | Touch LED intensity | Touch-LED-intensitet | Core-literal match |
| 11721 | 921209087 | `component::airgradient::entity::select::gps_mode::state::tracking` | Tracking | Spårning | Core-literal match |
| 11722 | 921209086 | `component::airgradient::entity::select::gps_mode::state::off` | Off | Av | Shared reference checked |
| 11723 | 921209085 | `component::airgradient::entity::select::gps_mode::state::always` | Always | Alltid | Core-literal match |
| 11724 | 921209084 | `component::airgradient::entity::select::gps_mode::name` | GPS mode | GPS-läge | Core-literal match |
| 11725 | 921209083 | `component::airgradient::entity::select::front_led_brightness::state::off` | Off | Av | Shared reference checked |
| 11726 | 921209082 | `component::airgradient::entity::select::front_led_brightness::state::mid` | Medium | Medel | Core-literal match |
| 11727 | 921209081 | `component::airgradient::entity::select::front_led_brightness::state::dim` | Dim | Dämpad | Core-literal match |
| 11728 | 921209080 | `component::airgradient::entity::select::front_led_brightness::state::bright` | Bright | Ljus | Core-literal match |
| 11729 | 921209079 | `component::airgradient::entity::select::front_led_brightness::name` | Front LED brightness | Främre LED-ljusstyrka | Core-literal match |
| 11730 | 921209078 | `component::airgradient::entity::select::co2_automatic_baseline_calibration::state:::7` | 7 days | 7 dagar | Core-literal match |
| 11731 | 921209077 | `component::airgradient::entity::select::back_led_brightness::state::off` | Off | Av | Shared reference checked |
| 11732 | 921209076 | `component::airgradient::entity::select::back_led_brightness::state::mid` | Medium | Medel | Core-literal match |
| 11733 | 921209075 | `component::airgradient::entity::select::back_led_brightness::state::dim` | Dim | Dämpad | Core-literal match |
| 11734 | 921209074 | `component::airgradient::entity::select::back_led_brightness::state::bright` | Bright | Ljus | Core-literal match |
| 11735 | 921209073 | `component::airgradient::entity::select::back_led_brightness::name` | Back LED brightness | Bakre LED-ljusstyrka | Core-literal match |
| 11736 | 921183614 | `component::silla_prism::entity::sensor::total_energy::name` | Total energy | Total energi | Core-literal match |
| 11737 | 921183613 | `component::silla_prism::entity::sensor::status::state::waiting` | Waiting | Väntar | Core-literal match |
| 11738 | 921183612 | `component::silla_prism::entity::sensor::status::state::paused` | Paused | Pausad | Shared reference checked |
| 11739 | 921183611 | `component::silla_prism::entity::sensor::status::state::idle` | Idle | Inaktiv | Shared reference checked |
| 11740 | 921183610 | `component::silla_prism::entity::sensor::status::state::charging` | Charging | Laddar | Shared reference checked |
| 11741 | 921183609 | `component::silla_prism::entity::sensor::status::name` | Status | Status | Core-literal match |
| 11742 | 921183608 | `component::silla_prism::entity::sensor::session_start::name` | Session start | Sessionsstart | Core-literal match |
| 11743 | 921183607 | `component::silla_prism::entity::sensor::session_energy::name` | Session energy | Energi för sessionen | Core-literal match |
| 11744 | 921183606 | `component::silla_prism::entity::sensor::pilot::name` | Pilot current | Pilotström | Core-literal match |
| 11745 | 921183605 | `component::silla_prism::entity::sensor::grid_power::name` | Grid power | Elnätseffekt | Core-literal match |
| 11746 | 921183604 | `component::silla_prism::entity::sensor::error::state::none` | None | Ingen | Core-literal match |
| 11747 | 921183603 | `component::silla_prism::entity::sensor::error::name` | Error | Fel | Core-literal match |
| 11748 | 921183602 | `component::silla_prism::config::step::user::title` | Connect your Silla Prism | Anslut din Silla Prism | Core-literal match |
| 11749 | 921183601 | `component::silla_prism::config::step::user::description` | Enter the MQTT base topic configured on the Prism (in the Silla app, under the MQTT settings). The default is "prism". | Ange MQTT-basämnet som konfigurerats på Prism i Silla-appens MQTT-inställningar. Standardvärdet är "prism". | Core-literal match |
| 11750 | 921183600 | `component::silla_prism::config::step::user::data_description::base_topic` | The MQTT topic prefix Prism publishes to, without a trailing slash. | Prefixet för MQTT-ämnet som Prism publicerar till, utan avslutande snedstreck. | Core-literal match |
| 11751 | 921183599 | `component::silla_prism::config::step::user::data::base_topic` | Base topic | Basämne | Core-literal match |
| 11752 | 921183598 | `component::silla_prism::config::step::discovery_confirm::title` | Set up Silla Prism | Konfigurera Silla Prism | Core-literal match |
| 11753 | 921183597 | `component::silla_prism::config::step::discovery_confirm::description` | Do you want to set up the discovered Prism {serial}? | Vill du konfigurera upptäckta Prism {serial}? | Core-literal match |
| 11754 | 921183596 | `component::silla_prism::config::flow_title` | {serial} | {serial} | Core-literal match |
| 11755 | 921183595 | `component::silla_prism::config::error::no_device` | No Prism messages were received on this base topic. Check that the topic matches the one configured in the Silla app and that Prism is online. | Inga Prism-meddelanden togs emot på detta basämne. Kontrollera att ämnet stämmer med det som konfigurerats i Silla-appen och att Prism är ansluten. | Core-literal match |
| 11756 | 921183594 | `component::silla_prism::config::error::mqtt_unavailable` | The MQTT integration is not available. Set it up first. | MQTT-integrationen är inte tillgänglig. Konfigurera den först. | Source found in adjacent Core path |
| 11757 | 921183593 | `component::silla_prism::config::error::invalid_base_topic` | This is not a valid MQTT topic. Enter the plain topic prefix from the Silla app, without wildcards. | Det här är inte ett giltigt MQTT-ämne. Ange ämnesprefixet från Silla-appen utan jokertecken. | Core-literal match |
| 11758 | 921183592 | `component::silla_prism::config::abort::invalid_discovery_info` | Invalid discovery information received. | Ogiltig upptäcktsinformation mottagen. | Core-literal match |
| 11759 | 921183591 | `component::silla_prism::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference checked |
| 11760 | 921123046 | `component::librenms::exceptions::update_error::message` | An error occurred while retrieving data from your LibreNMS instance: {error} | Ett fel uppstod när data hämtades från din LibreNMS-instans: {error} | Core-literal match |
| 11761 | 921123045 | `component::librenms::exceptions::cannot_connect::message` | Cannot connect to your LibreNMS instance. | Det går inte att ansluta till din LibreNMS-instans. | Core-literal match |
| 11762 | 921123044 | `component::librenms::exceptions::auth_error::message` | Authentication failed, please update your API key | Autentiseringen misslyckades. Uppdatera din API-nyckel. | Core-literal match |
| 11763 | 921123043 | `component::librenms::entity::binary_sensor::status::name` | Status | Status | Core-literal match |
| 11764 | 921123042 | `component::librenms::config::step::user::data_description::verify_ssl` | Whether to verify the SSL certificate when SSL encryption is used to connect to your LibreNMS instance. | Om SSL-certifikatet ska verifieras när SSL-kryptering används för att ansluta till din LibreNMS-instans. | Shared reference checked |
| 11765 | 921123041 | `component::librenms::config::step::user::data_description::url` | The full URL of your LibreNMS instance. | Den fullständiga URL:en till din LibreNMS-instans. | Shared reference checked |
| 11766 | 921123040 | `component::librenms::config::step::user::data_description::api_key` | API key to connect to your LibreNMS instance. | API-nyckel för att ansluta till din LibreNMS-instans. | Shared reference checked |
| 11767 | 921123039 | `component::librenms::config::step::user::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference checked |
| 11768 | 921123038 | `component::librenms::config::step::user::data::url` | URL | URL | Shared reference checked |
| 11769 | 921123037 | `component::librenms::config::step::user::data::api_key` | API key | API-nyckel | Shared reference checked |
| 11770 | 921123036 | `component::librenms::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference checked |
| 11771 | 921123035 | `component::librenms::config::error::invalid_url` | The provided URL is invalid. | Den angivna URL:en är ogiltig. | Core-literal match |
| 11772 | 921123034 | `component::librenms::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference checked |
| 11773 | 921123033 | `component::librenms::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference checked |
| 11774 | 921123032 | `component::librenms::config::abort::already_configured` | This LibreNMS instance is already configured. | Denna LibreNMS-instans är redan konfigurerad. | Core-literal match |
| 11775 | 921123031 | `component::librenms::common::data_desc_url` | The full URL of your LibreNMS instance. | Den fullständiga URL:en till din LibreNMS-instans. | Core-literal match |
| 11776 | 921123030 | `component::librenms::common::data_desc_ssl_verify` | Whether to verify the SSL certificate when SSL encryption is used to connect to your LibreNMS instance. | Om SSL-certifikatet ska verifieras när SSL-kryptering används för att ansluta till din LibreNMS-instans. | Core-literal match |
| 11777 | 921123029 | `component::librenms::common::data_desc_api_key` | API key to connect to your LibreNMS instance. | API-nyckel för att ansluta till din LibreNMS-instans. | Core-literal match |
| 11778 | 921119379 | `component::sun::triggers::polar_night_started::name` | Polar night started | Polarnatten startade | Core-literal match |
| 11779 | 921119378 | `component::sun::triggers::polar_night_started::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-owner follow-up open |
| 11780 | 921119377 | `component::sun::triggers::polar_night_started::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-owner follow-up open |
| 11781 | 921119376 | `component::sun::triggers::polar_night_started::fields::offset::name` | Offset | Förskjutning | Shared reference checked |
| 11782 | 921119375 | `component::sun::triggers::polar_night_started::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference checked |
| 11783 | 921119374 | `component::sun::triggers::polar_night_started::description` | Triggers when the polar night period starts and the sun stops rising. | Utlöses när polarnatten börjar och solen slutar gå upp. | Core-literal match |
| 11784 | 921119373 | `component::sun::triggers::polar_night_ended::name` | Polar night ended | Polarnatten slutade | Core-literal match |
| 11785 | 921119372 | `component::sun::triggers::polar_night_ended::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-owner follow-up open |
| 11786 | 921119371 | `component::sun::triggers::polar_night_ended::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-owner follow-up open |
| 11787 | 921119370 | `component::sun::triggers::polar_night_ended::fields::offset::name` | Offset | Förskjutning | Shared reference checked |
| 11788 | 921119369 | `component::sun::triggers::polar_night_ended::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference checked |
| 11789 | 921119368 | `component::sun::triggers::polar_night_ended::description` | Triggers when the polar night period ends and the sun rises again. | Utlöses när polarnatten tar slut och solen går upp igen. | Core-literal match |
| 11790 | 921119367 | `component::sun::triggers::midnight_sun_started::name` | Midnight sun started | Midnattssolen startade | Core-literal match |
| 11791 | 921119366 | `component::sun::triggers::midnight_sun_started::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-owner follow-up open |
| 11792 | 921119365 | `component::sun::triggers::midnight_sun_started::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-owner follow-up open |
| 11793 | 921119364 | `component::sun::triggers::midnight_sun_started::fields::offset::name` | Offset | Förskjutning | Shared reference checked |
| 11794 | 921119363 | `component::sun::triggers::midnight_sun_started::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference checked |
| 11795 | 921119362 | `component::sun::triggers::midnight_sun_started::description` | Triggers when the midnight sun period starts and the sun stops setting. | Utlöses när midnattsolsperioden börjar och solen slutar gå ner. | Core-literal match |
| 11796 | 921119361 | `component::sun::triggers::midnight_sun_ended::name` | Midnight sun ended | Midnattssolen slutade | Core-literal match |
| 11797 | 921119360 | `component::sun::triggers::midnight_sun_ended::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-owner follow-up open |
| 11798 | 921119359 | `component::sun::triggers::midnight_sun_ended::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-owner follow-up open |
| 11799 | 921119358 | `component::sun::triggers::midnight_sun_ended::fields::offset::name` | Offset | Förskjutning | Shared reference checked |
| 11800 | 921119357 | `component::sun::triggers::midnight_sun_ended::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference checked |
| 11801 | 921119356 | `component::sun::triggers::midnight_sun_ended::description` | Triggers when the midnight sun period ends and the sun sets again. | Utlöses när midnattssolsperioden slutar och solen går ner igen. | Core-literal match |
| 11802 | 921119355 | `component::sun::triggers::golden_hour_started::name` | Golden hour started | Gyllene timmen började | Core-literal match |
| 11803 | 921119354 | `component::sun::triggers::golden_hour_started::fields::period::name` | Period | Period | Shared reference checked |
| 11804 | 921119353 | `component::sun::triggers::golden_hour_started::fields::period::description` | The time of day to consider: the morning, the evening, or either. | Vilken tid på dagen som ska användas: morgonen, kvällen eller båda. | Shared reference checked |
| 11805 | 921119352 | `component::sun::triggers::golden_hour_started::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-owner follow-up open |
| 11806 | 921119351 | `component::sun::triggers::golden_hour_started::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-owner follow-up open |
| 11807 | 921119350 | `component::sun::triggers::golden_hour_started::fields::offset::name` | Offset | Förskjutning | Shared reference checked |
| 11808 | 921119349 | `component::sun::triggers::golden_hour_started::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference checked |
| 11809 | 921119348 | `component::sun::triggers::golden_hour_started::description` | Triggers when golden hour starts, in the morning, the evening, or either. | Utlöses när gyllene timmen börjar, på morgonen, kvällen eller båda. | Core-literal match |
| 11810 | 921119347 | `component::sun::triggers::golden_hour_ended::name` | Golden hour ended | Gyllene timmen slutade | Core-literal match |
| 11811 | 921119346 | `component::sun::triggers::golden_hour_ended::fields::period::name` | Period | Period | Shared reference checked |
| 11812 | 921119345 | `component::sun::triggers::golden_hour_ended::fields::period::description` | The time of day to consider: the morning, the evening, or either. | Vilken tid på dagen som ska användas: morgonen, kvällen eller båda. | Shared reference checked |
| 11813 | 921119344 | `component::sun::triggers::golden_hour_ended::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-owner follow-up open |
| 11814 | 921119343 | `component::sun::triggers::golden_hour_ended::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-owner follow-up open |
| 11815 | 921119342 | `component::sun::triggers::golden_hour_ended::fields::offset::name` | Offset | Förskjutning | Shared reference checked |
| 11816 | 921119341 | `component::sun::triggers::golden_hour_ended::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference checked |
| 11817 | 921119340 | `component::sun::triggers::golden_hour_ended::description` | Triggers when golden hour ends, in the morning, the evening, or either. | Utlöses när gyllene timmen slutar, på morgonen, kvällen eller båda. | Core-literal match |
| 11818 | 921119339 | `component::sun::triggers::blue_hour_started::name` | Blue hour started | Blå timmen började | Core-literal match |
| 11819 | 921119338 | `component::sun::triggers::blue_hour_started::fields::period::name` | Period | Period | Shared reference checked |
| 11820 | 921119337 | `component::sun::triggers::blue_hour_started::fields::period::description` | The time of day to consider: the morning, the evening, or either. | Vilken tid på dagen som ska användas: morgonen, kvällen eller båda. | Shared reference checked |
| 11821 | 921119336 | `component::sun::triggers::blue_hour_started::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-owner follow-up open |
| 11822 | 921119335 | `component::sun::triggers::blue_hour_started::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-owner follow-up open |
| 11823 | 921119334 | `component::sun::triggers::blue_hour_started::fields::offset::name` | Offset | Förskjutning | Shared reference checked |
| 11824 | 921119333 | `component::sun::triggers::blue_hour_started::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference checked |
| 11825 | 921119332 | `component::sun::triggers::blue_hour_started::description` | Triggers when blue hour starts, in the morning, the evening, or either. | Utlöses när blå timmen börjar, på morgonen, kvällen eller båda. | Core-literal match |
| 11826 | 921119331 | `component::sun::triggers::blue_hour_ended::name` | Blue hour ended | Blå timmen slutade | Core-literal match |
| 11827 | 921119330 | `component::sun::triggers::blue_hour_ended::fields::period::name` | Period | Period | Shared reference checked |
| 11828 | 921119329 | `component::sun::triggers::blue_hour_ended::fields::period::description` | The time of day to consider: the morning, the evening, or either. | Vilken tid på dagen som ska användas: morgonen, kvällen eller båda. | Shared reference checked |
| 11829 | 921119328 | `component::sun::triggers::blue_hour_ended::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-owner follow-up open |
| 11830 | 921119327 | `component::sun::triggers::blue_hour_ended::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-owner follow-up open |
| 11831 | 921119326 | `component::sun::triggers::blue_hour_ended::fields::offset::name` | Offset | Förskjutning | Shared reference checked |
| 11832 | 921119325 | `component::sun::triggers::blue_hour_ended::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference checked |
| 11833 | 921119324 | `component::sun::triggers::blue_hour_ended::description` | Triggers when blue hour ends, in the morning, the evening, or either. | Utlöses när blå timmen slutar, på morgonen, kvällen eller båda. | Core-literal match |
| 11834 | 921119323 | `component::sun::selector::period::options::morning` | Morning | Morgon | Core-literal match |
| 11835 | 921119322 | `component::sun::selector::period::options::evening` | Evening | Kväll | Core-literal match |
| 11836 | 921119321 | `component::sun::selector::period::options::any` | Any | Båda | Core-literal match |
| 11837 | 921119320 | `component::sun::conditions::is_polar_night::name` | It is polar night | Det är polarnatt | Core-literal match |
| 11838 | 921119319 | `component::sun::conditions::is_polar_night::description` | Tests if it is polar night. | Testar om det är polarnatt. | Core-literal match |
| 11839 | 921119318 | `component::sun::conditions::is_midnight_sun::name` | It is midnight sun | Det är midnattssol | Core-literal match |
| 11840 | 921119317 | `component::sun::conditions::is_midnight_sun::description` | Tests if it is midnight sun. | Testar om det är midnattssol. | Core-literal match |
| 11841 | 921119316 | `component::sun::conditions::is_golden_hour::name` | It is golden hour | Det är gyllene timmen | Core-literal match |
| 11842 | 921119315 | `component::sun::conditions::is_golden_hour::fields::period::name` | Period | Period | Shared reference checked |
| 11843 | 921119314 | `component::sun::conditions::is_golden_hour::fields::period::description` | The time of day to consider: the morning, the evening, or either. | Vilken tid på dagen som ska användas: morgonen, kvällen eller båda. | Shared reference checked |
| 11844 | 921119313 | `component::sun::conditions::is_golden_hour::description` | Tests if it is golden hour, optionally for a specific period. | Kontrollerar om det är gyllene timmen, vid behov för en viss tid på dagen. | Core-literal match |
| 11845 | 921119312 | `component::sun::conditions::is_blue_hour::name` | It is blue hour | Det är blå timmen | Core-literal match |
| 11846 | 921119311 | `component::sun::conditions::is_blue_hour::fields::period::name` | Period | Period | Shared reference checked |
| 11847 | 921119310 | `component::sun::conditions::is_blue_hour::fields::period::description` | The time of day to consider: the morning, the evening, or either. | Vilken tid på dagen som ska användas: morgonen, kvällen eller båda. | Shared reference checked |
| 11848 | 921119309 | `component::sun::conditions::is_blue_hour::description` | Tests if it is blue hour, optionally for a specific period. | Kontrollerar om det är blå timmen, vid behov för en viss tid på dagen. | Core-literal match |
| 11849 | 921119308 | `component::sun::common::period_name` | Period | Period | Core-literal match |
| 11850 | 921119307 | `component::sun::common::period_description` | The time of day to consider: the morning, the evening, or either. | Vilken tid på dagen som ska användas: morgonen, kvällen eller båda. | Core-literal match |
| 11851 | 921106454 | `component::guntamatic::entity::sensor::suction_fan::name` | Suction fan | Sugfläkt | Core-literal match |
| 11852 | 921106453 | `component::guntamatic::entity::sensor::service_date::name` | Service date | Servicedatum | Core-literal match |
| 11853 | 921106452 | `component::guntamatic::entity::sensor::secondary_air::name` | Secondary air | Sekundärluft | Core-literal match |
| 11854 | 921106451 | `component::guntamatic::entity::sensor::room_temperature::name` | Room temperature | Rumstemperatur | Core-literal match |
| 11855 | 921106450 | `component::guntamatic::entity::sensor::primary_air::name` | Primary air | Primärluft | Core-literal match |
| 11856 | 921106449 | `component::guntamatic::entity::sensor::operating_time::name` | Operating time | Driftstid | Core-literal match |
| 11857 | 921106448 | `component::guntamatic::entity::sensor::interruption::name` | Interruption {number} | Avbrott {number} | Core-literal match |
| 11858 | 921106447 | `component::guntamatic::entity::sensor::heating_circulation_pump::state::off` | Off | Av | Core-literal match |
| 11859 | 921106446 | `component::guntamatic::entity::sensor::heating_circulation_pump::state::nonstop` | Non-stop | Non-stop | Core-literal match |
| 11860 | 921106445 | `component::guntamatic::entity::sensor::heating_circulation_pump::state::auto` | Auto | Auto | Core-literal match |
| 11861 | 921106444 | `component::guntamatic::entity::sensor::heating_circulation_pump::name` | Pump | Pump | Core-literal match |
| 11862 | 921106443 | `component::guntamatic::entity::sensor::heating_circulation_program::state::timer` | Timer | Timer | Core-literal match |
| 11863 | 921106442 | `component::guntamatic::entity::sensor::heating_circulation_program::state::off` | Off | Av | Core-literal match |
| 11864 | 921106441 | `component::guntamatic::entity::sensor::heating_circulation_program::state::hibernate_to` | Away mode | Bortaläge | Core-literal match |
| 11865 | 921106440 | `component::guntamatic::entity::sensor::heating_circulation_program::state::hibernate` | Setback mode | Temperatursänkningsläge | Core-literal match |
| 11866 | 921106439 | `component::guntamatic::entity::sensor::heating_circulation_program::state::heat` | Heat | Värme | Core-literal match |
| 11867 | 921106438 | `component::guntamatic::entity::sensor::heating_circulation_program::name` | Program | Program | Core-literal match |
| 11868 | 921106437 | `component::guntamatic::entity::sensor::flue_gas_actuator_target::name` | Flue gas actuator target | Målvärde för rökgasställdon | Core-literal match |
| 11869 | 921106436 | `component::guntamatic::entity::sensor::extra_dhw_temperature::name` | Extra DHW circuit {circuit} temperature | Temperatur för extra varmvattenkrets {circuit} | Core-literal match |
| 11870 | 921106435 | `component::guntamatic::entity::sensor::extra_dhw_boost::state::off` | Off | Av | Core-literal match |
| 11871 | 921106434 | `component::guntamatic::entity::sensor::extra_dhw_boost::state::nonstop` | Non-stop | Non-stop | Core-literal match |
| 11872 | 921106433 | `component::guntamatic::entity::sensor::extra_dhw_boost::state::auto` | Auto | Auto | Core-literal match |
| 11873 | 921106432 | `component::guntamatic::entity::sensor::extra_dhw_boost::name` | Extra DHW pump {pump} | Extra varmvattenpump {pump} | Core-literal match |
| 11874 | 921106431 | `component::guntamatic::entity::sensor::extra_dhw_2_temperature::name` | Extra DHW 2 temperature | Temperatur för extra varmvatten 2 | Core-literal match |
| 11875 | 921106430 | `component::guntamatic::entity::sensor::extra_dhw_1_temperature::name` | Extra DHW 1 temperature | Temperatur för extra varmvatten 1 | Core-literal match |
| 11876 | 921106429 | `component::guntamatic::entity::sensor::domestic_hot_water_temperature::name` | Domestic hot water circuit {circuit} temperature | Temperatur för varmvattenkrets {circuit} | Core-literal match |
| 11877 | 921106428 | `component::guntamatic::entity::sensor::domestic_hot_water_2_temperature::name` | Domestic hot water circuit 2 temperature | Temperatur för varmvattenkrets 2 | Core-literal match |
| 11878 | 921106427 | `component::guntamatic::entity::sensor::domestic_hot_water_1_temperature::name` | Domestic hot water circuit 1 temperature | Temperatur för varmvattenkrets 1 | Core-literal match |
| 11879 | 921106426 | `component::guntamatic::entity::sensor::dhw_pump::name` | DHW pump {circuit} | Varmvattenpump {circuit} | Core-literal match |
| 11880 | 921106425 | `component::guntamatic::entity::sensor::co2_content::name` | Flue CO2 content | CO2-halt i rökgång | Core-literal match |
| 11881 | 921106424 | `component::guntamatic::entity::sensor::circuit_temperature::name` | Flow temperature | Framledningstemperatur | Core-literal match |
| 11882 | 921106423 | `component::guntamatic::entity::sensor::burner_output::name` | Burner output | Brännarens effekt | Core-literal match |
| 11883 | 921106422 | `component::guntamatic::entity::sensor::buffer_top_2_temperature::name` | Buffer 2 top temperature | Topptemperatur för buffert 2 | Core-literal match |
| 11884 | 921106421 | `component::guntamatic::entity::sensor::buffer_top_1_temperature::name` | Buffer 1 top temperature | Topptemperatur för buffert 1 | Core-literal match |
| 11885 | 921106420 | `component::guntamatic::entity::sensor::buffer_top_0_temperature::name` | Buffer 0 top temperature | Topptemperatur för buffert 0 | Core-literal match |
| 11886 | 921106419 | `component::guntamatic::entity::sensor::buffer_stage_top_temperature::name` | Buffer stage {tank} top temperature | Topptemperatur för buffertsteg {tank} | Core-literal match |
| 11887 | 921106418 | `component::guntamatic::entity::sensor::buffer_stage_bottom_temperature::name` | Buffer stage {tank} bottom temperature | Bottentemperatur för buffertsteg {tank} | Core-literal match |
| 11888 | 921106417 | `component::guntamatic::entity::sensor::buffer_bottom_2_temperature::name` | Buffer 2 bottom temperature | Bottentemperatur för buffert 2 | Core-literal match |
| 11889 | 921106416 | `component::guntamatic::entity::sensor::buffer_bottom_1_temperature::name` | Buffer 1 bottom temperature | Bottentemperatur för buffert 1 | Core-literal match |
| 11890 | 921106415 | `component::guntamatic::entity::sensor::buffer_bottom_0_temperature::name` | Buffer 0 bottom temperature | Bottentemperatur för buffert 0 | Core-literal match |
| 11891 | 921106414 | `component::guntamatic::entity::sensor::boiler_shunt_pump::name` | Boiler shunt pump | Pannans shuntpump | Core-literal match |
| 11892 | 921106413 | `component::guntamatic::entity::sensor::auxiliary_pump::state::off` | Off | Av | Core-literal match |
| 11893 | 921106412 | `component::guntamatic::entity::sensor::auxiliary_pump::state::nonstop` | Non-stop | Kontinuerligt | Core-literal match |
| 11894 | 921106411 | `component::guntamatic::entity::sensor::auxiliary_pump::state::auto` | Auto | Auto | Core-literal match |
| 11895 | 921106410 | `component::guntamatic::entity::sensor::auxiliary_pump::name` | Auxiliary pump {pump} | Hjälppump {pump} | Core-literal match |
| 11896 | 921097718 | `component::nexblue::entity::sensor::voltage::name` | Voltage {phase} | Spänning {phase} | Core-literal match |
| 11897 | 921097717 | `component::nexblue::entity::sensor::phase_charging::state::three_phase` | Three-phase | Trefas | Core-literal match |
| 11898 | 921097716 | `component::nexblue::entity::sensor::phase_charging::state::single_phase` | Single-phase | Enfas | Core-literal match |
| 11899 | 921097715 | `component::nexblue::entity::sensor::phase_charging::name` | Phase charging | Fasladdning | Core-literal match |
| 11900 | 921097714 | `component::nexblue::entity::sensor::network_status::state::wifi` | Wi-Fi | Wi-Fi | Core-literal match |
| 11901 | 921097713 | `component::nexblue::entity::sensor::network_status::state::none` | None | Ingen | Core-literal match |
| 11902 | 921097712 | `component::nexblue::entity::sensor::network_status::state::modem` | 4G | 4G | Core-literal match |
| 11903 | 921097711 | `component::nexblue::entity::sensor::network_status::state::ethernet` | Ethernet | Ethernet | Core-literal match |
| 11904 | 921097710 | `component::nexblue::entity::sensor::network_status::name` | Network status | Nätverksstatus | Core-literal match |
| 11905 | 921097709 | `component::nexblue::entity::sensor::lifetime_energy::name` | Lifetime energy | Total energi under livslängden | Core-literal match |
| 11906 | 921097708 | `component::nexblue::entity::sensor::current_limit::name` | Current limit | Strömgräns | Core-literal match |
| 11907 | 921097707 | `component::nexblue::entity::sensor::current::name` | Current {phase} | Ström {phase} | Core-literal match |
| 11908 | 921097706 | `component::nexblue::entity::sensor::circuit_fuse::name` | Circuit fuse | Kretssäkring | Core-literal match |
| 11909 | 921097705 | `component::nexblue::entity::sensor::charging_state::state::lb_waiting` | Waiting for available power | Väntar på tillgänglig effekt | Core-literal match |
| 11910 | 921097704 | `component::nexblue::entity::sensor::charging_state::state::idle` | Connect cable to charge | Anslut kabeln för att ladda | Core-literal match |
| 11911 | 921097703 | `component::nexblue::entity::sensor::charging_state::state::finished` | Charging complete | Laddning klar | Core-literal match |
| 11912 | 921097702 | `component::nexblue::entity::sensor::charging_state::state::ev_waiting` | Waiting for car response | Väntar på svar från bilen | Core-literal match |
| 11913 | 921097701 | `component::nexblue::entity::sensor::charging_state::state::error` | Charging unavailable | Laddning inte tillgänglig | Core-literal match |
| 11914 | 921097700 | `component::nexblue::entity::sensor::charging_state::state::delay_waiting` | Schedule waiting | Väntar på schemalagd laddning | Core-literal match |
| 11915 | 921097699 | `component::nexblue::entity::sensor::charging_state::state::connected` | Ready to charge | Redo att ladda | Core-literal match |
| 11916 | 921097698 | `component::nexblue::entity::sensor::charging_state::state::charging` | Charging | Laddar | Core-literal match |
| 11917 | 921097697 | `component::nexblue::entity::sensor::charging_state::name` | Charging state | Laddningsstatus | Core-literal match |
| 11918 | 921097696 | `component::nexblue::entity::sensor::cable_lock_mode::state::locked_while_charging` | Locked while charging | Låst under laddning | Core-literal match |
| 11919 | 921097695 | `component::nexblue::entity::sensor::cable_lock_mode::state::always_locked` | Always locked | Alltid låst | Core-literal match |
| 11920 | 921097694 | `component::nexblue::entity::sensor::cable_lock_mode::name` | Cable lock mode | Kabellåsläge | Core-literal match |
| 11921 | 921097693 | `component::nexblue::entity::sensor::cable_current_limit::name` | Cable rating | Kabelklassning | Core-literal match |
| 11922 | 921097692 | `component::nexblue::entity::sensor::brightness::name` | LED brightness | LED-ljusstyrka | Core-literal match |
| 11923 | 921097691 | `component::nexblue::entity::sensor::access_level::state::no_restrictions` | No restrictions | Inga restriktioner | Core-literal match |
| 11924 | 921097690 | `component::nexblue::entity::sensor::access_level::state::authorized_users_only` | Authorized users only | Endast auktoriserade användare | Core-literal match |
| 11925 | 921097689 | `component::nexblue::entity::sensor::access_level::name` | Access level | Åtkomstnivå | Core-literal match |
| 11926 | 921097688 | `component::nexblue::config::step::user::description` | Sign in with your NexBlue end-user account. | Logga in med ditt NexBlue-användarkonto. | Core-literal match |
| 11927 | 921097687 | `component::nexblue::config::step::user::data_description::username` | The email address or username used to sign in to NexBlue. | Den e-postadress eller det användarnamn som används för att logga in på NexBlue. | Core-literal match |
| 11928 | 921097686 | `component::nexblue::config::step::user::data_description::password` | The password for your NexBlue account. | Lösenordet för ditt NexBlue-konto. | Core-literal match |
| 11929 | 921097685 | `component::nexblue::config::step::user::data::username` | Username | Användarnamn | Shared reference checked |
| 11930 | 921097684 | `component::nexblue::config::step::user::data::password` | Password | Lösenord | Shared reference checked |
| 11931 | 921097683 | `component::nexblue::config::error::unknown` | NexBlue could not complete sign-in. Please try again later. | NexBlue kunde inte slutföra inloggningen. Försök igen senare. | Core-literal match |
| 11932 | 921097682 | `component::nexblue::config::error::invalid_auth` | NexBlue authentication failed. | NexBlue-autentiseringen misslyckades. | Core-literal match |
| 11933 | 921097681 | `component::nexblue::config::error::cannot_connect` | Cannot connect to NexBlue. | Det går inte att ansluta till NexBlue. | Core-literal match |
| 11934 | 921097680 | `component::nexblue::config::abort::already_configured` | This NexBlue account is already configured. | Detta NexBlue-konto är redan konfigurerat. | Core-literal match |
| 11935 | 921086633 | `component::specialized_turbo::entity::sensor::system_temp::name` | System temperature | Systemtemperatur | Core-literal match |
| 11936 | 921086632 | `component::specialized_turbo::entity::sensor::rider_power::name` | Rider power | Cyklistens effekt | Core-literal match |
| 11937 | 921086631 | `component::specialized_turbo::entity::sensor::range_short::name` | Range (short) | Räckvidd (kort) | Core-literal match |
| 11938 | 921086630 | `component::specialized_turbo::entity::sensor::range_long::name` | Range (long) | Räckvidd (lång) | Core-literal match |
| 11939 | 921086629 | `component::specialized_turbo::entity::sensor::odometer::name` | Odometer | Vägmätare | Core-literal match |
| 11940 | 921086628 | `component::specialized_turbo::entity::sensor::motor_temp::name` | Motor temperature | Motortemperatur | Core-literal match |
| 11941 | 921086627 | `component::specialized_turbo::entity::sensor::motor_power::name` | Motor power | Motoreffekt | Core-literal match |
| 11942 | 921086626 | `component::specialized_turbo::entity::sensor::kcal::name` | Calories | Kalorier | Core-literal match |
| 11943 | 921086625 | `component::specialized_turbo::entity::sensor::gradient::name` | Gradient | Lutning | Core-literal match |
| 11944 | 921086624 | `component::specialized_turbo::entity::sensor::consumption::name` | Consumption | Förbrukning | Core-literal match |
| 11945 | 921086623 | `component::specialized_turbo::entity::sensor::cadence::name` | Cadence | Kadens | Core-literal match |
| 11946 | 921086622 | `component::specialized_turbo::entity::sensor::battery_voltage::name` | Battery voltage | Batterispänning | Core-literal match |
| 11947 | 921086621 | `component::specialized_turbo::entity::sensor::battery_temp::name` | Battery temperature | Batteritemperatur | Core-literal match |
| 11948 | 921086620 | `component::specialized_turbo::entity::sensor::battery_remaining_wh::name` | Battery remaining | Återstående batterienergi | Core-literal match |
| 11949 | 921086619 | `component::specialized_turbo::entity::sensor::battery_health::name` | Battery health | Batterihälsa | Core-literal match |
| 11950 | 921086618 | `component::specialized_turbo::entity::sensor::battery_current::name` | Battery current | Batteriström | Core-literal match |
| 11951 | 921086617 | `component::specialized_turbo::entity::sensor::battery_charge_cycles::name` | Charge cycles | Laddningscykler | Core-literal match |
| 11952 | 921086616 | `component::specialized_turbo::entity::sensor::battery_capacity_wh::name` | Battery capacity | Batterikapacitet | Core-literal match |
| 11953 | 921086615 | `component::specialized_turbo::entity::sensor::assist_turbo_pct::name` | Turbo assist | Turboassistans | Core-literal match |
| 11954 | 921086614 | `component::specialized_turbo::entity::sensor::assist_trail_pct::name` | Trail assist | Stigassistans | Core-literal match |
| 11955 | 921086613 | `component::specialized_turbo::entity::sensor::assist_level::state::turbo` | Turbo | Turbo | Core-literal match |
| 11956 | 921086612 | `component::specialized_turbo::entity::sensor::assist_level::state::trail` | Trail | Stig | Core-literal match |
| 11957 | 921086611 | `component::specialized_turbo::entity::sensor::assist_level::state::off` | Off | Av | Shared reference checked |
| 11958 | 921086610 | `component::specialized_turbo::entity::sensor::assist_level::state::eco` | Eco | Eco | Core-literal match |
| 11959 | 921086609 | `component::specialized_turbo::entity::sensor::assist_level::name` | Assist level | Assistansnivå | Core-literal match |
| 11960 | 921086608 | `component::specialized_turbo::entity::sensor::assist_eco_pct::name` | ECO assist | Ekoassistans | Core-literal match |
| 11961 | 921086607 | `component::specialized_turbo::entity::sensor::altitude_gain::name` | Altitude gain | Höjdökning | Core-literal match |
| 11962 | 921086606 | `component::specialized_turbo::entity::sensor::altitude::name` | Altitude | Höjd | Core-literal match |
| 11963 | 921086605 | `component::specialized_turbo::config::step::user::title` | Add Specialized Turbo bike | Lägg till Specialized Turbo-cykel | Core-literal match |
| 11964 | 921086604 | `component::specialized_turbo::config::step::user::description` | Select your Specialized Turbo bike from the discovered devices. | Välj din Specialized Turbo-cykel bland de upptäckta enheterna. | Core-literal match |
| 11965 | 921086603 | `component::specialized_turbo::config::step::user::data_description::address` | Select the Specialized Turbo bike you want to add. | Välj den Specialized Turbo-cykel som du vill lägga till. | Core-literal match |
| 11966 | 921086602 | `component::specialized_turbo::config::step::user::data::address` | Bike | Cykel | Core-literal match |
| 11967 | 921086601 | `component::specialized_turbo::config::step::reconfigure::title` | Reconfigure Specialized Turbo | Konfigurera om Specialized Turbo | Core-literal match |
| 11968 | 921086600 | `component::specialized_turbo::config::step::reconfigure::description` | Replace the encryption key for your Specialized Turbo bike. | Byt ut krypteringsnyckeln till din Specialized Turbo-cykel. | Core-literal match |
| 11969 | 921086599 | `component::specialized_turbo::config::step::manual_key::title` | Enter wrapped bike key | Ange den krypterade cykelnyckeln | Core-literal match |
| 11970 | 921086598 | `component::specialized_turbo::config::step::manual_key::description` | Enter the 64-character wrapped key returned by the Specialized keystore service. | Ange den 64 tecken långa nyckeln som returneras av Specialized keystore-tjänsten. | Core-literal match |
| 11971 | 921086597 | `component::specialized_turbo::config::step::manual_key::data_description::wrapped_key` | The 64-character wrapped key for this bike. | Den 64 tecken långa nyckeln för den här cykeln. | Core-literal match |
| 11972 | 921086596 | `component::specialized_turbo::config::step::manual_key::data::wrapped_key` | Wrapped key | Krypterad nyckel | Core-literal match |
| 11973 | 921086595 | `component::specialized_turbo::config::step::key_source::title` | Choose encryption key source | Välj källa för krypteringsnyckel | Core-literal match |
| 11974 | 921086594 | `component::specialized_turbo::config::step::key_source::menu_options::manual_key` | Enter wrapped bike key | Ange den krypterade cykelnyckeln | Shared reference checked |
| 11975 | 921086593 | `component::specialized_turbo::config::step::key_source::menu_options::account` | Sign in to Specialized | Logga in på Specialized | Shared reference checked |
| 11976 | 921086592 | `component::specialized_turbo::config::step::key_source::description` | Use your Specialized account to retrieve the bike key automatically, or enter a wrapped key manually. | Använd ditt Specialized-konto för att hämta cykelnyckeln automatiskt, eller ange en krypterad nyckel manuellt. | Core-literal match |
| 11977 | 921086591 | `component::specialized_turbo::config::step::bluetooth_confirm::title` | Discovered Specialized Turbo bike | Upptäckt Specialized Turbo-cykel | Core-literal match |
| 11978 | 921086590 | `component::specialized_turbo::config::step::bluetooth_confirm::description` | A Specialized Turbo bike was found at {address} ({name}). Pairing prompts are handled by the active Bluetooth backend. | En Specialized Turbo-cykel hittades på {address} ({name}). Parkopplingsförfrågningar hanteras av den aktiva Bluetooth-modulen. | Core-literal match |
| 11979 | 921086589 | `component::specialized_turbo::config::step::account::title` | Sign in to Specialized | Logga in på Specialized | Core-literal match |
| 11980 | 921086588 | `component::specialized_turbo::config::step::account::description` | Your password is used only to retrieve this bike's encryption key. Home Assistant stores the per-bike wrapped key, not your password or account tokens. | Ditt lösenord används endast för att hämta krypteringsnyckeln för den här cykeln. Home Assistant lagrar den cykelspecifika krypterade nyckeln, inte ditt lösenord eller dina kontotoken. | Core-literal match |
| 11981 | 921086587 | `component::specialized_turbo::config::step::account::data_description::password` | The password is sent to Specialized only to retrieve the bike key. | Lösenordet skickas till Specialized enbart för att hämta cykelnyckeln. | Core-literal match |
| 11982 | 921086586 | `component::specialized_turbo::config::step::account::data_description::email` | The email address for your Specialized account. | E-postadressen för ditt Specialized-konto. | Core-literal match |
| 11983 | 921086585 | `component::specialized_turbo::config::step::account::data::password` | Password | Lösenord | Shared reference checked |
| 11984 | 921086584 | `component::specialized_turbo::config::step::account::data::email` | Email | E-post | Shared reference checked |
| 11985 | 921086583 | `component::specialized_turbo::config::error::key_unavailable` | The Specialized encryption key could not be retrieved. | Det gick inte att hämta krypteringsnyckeln från Specialized. | Core-literal match |
| 11986 | 921086582 | `component::specialized_turbo::config::error::invalid_wrapped_key` | The wrapped key is invalid. | Den krypterade nyckeln är ogiltig. | Core-literal match |
| 11987 | 921086581 | `component::specialized_turbo::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference checked |
| 11988 | 921086580 | `component::specialized_turbo::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference checked |
| 11989 | 921086579 | `component::specialized_turbo::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-owner follow-up open |
| 11990 | 921086578 | `component::specialized_turbo::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-owner follow-up open |
| 11991 | 921086577 | `component::specialized_turbo::config::abort::not_encrypted` | This bike has no stored encryption key to reconfigure. | Denna cykel har ingen lagrad krypteringsnyckel som behöver konfigureras om. | Core-literal match |
| 11992 | 921086576 | `component::specialized_turbo::config::abort::no_devices_found` | No devices found on the network | Inga enheter hittades i nätverket | Shared reference checked |
| 11993 | 921086575 | `component::specialized_turbo::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference checked |
| 11994 | 921058715 | `component::fronius::entity::switch::power_limit_enabled::name` | Power limiting | Effektbegränsning | Source-owner follow-up open |
| 11995 | 921058714 | `component::fronius::entity::switch::battery_grid_charging::name` | Battery grid charging | Batteriladdning från elnätet | Core-literal match |
| 11996 | 921058713 | `component::fronius::entity::switch::battery_discharge_power_limit_enabled::name` | Battery discharge power limiting | Gräns för batteriurladdningseffekt | Core-literal match |
| 11997 | 921058712 | `component::fronius::entity::switch::battery_charge_power_limit_enabled::name` | Battery charge power limiting | Gräns för batteriladdningseffekt | Core-literal match |
| 11998 | 921052603 | `component::vizio::config::step::reconfigure::description` | Update the address of your VIZIO SmartCast device. If your TV requires a new access token, you will be guided through the pairing process again. | Uppdatera adressen för din VIZIO SmartCast-enhet. Om TV:n behöver en ny åtkomsttoken leds du genom parkopplingsprocessen igen. | Core-literal match |
| 11999 | 921052602 | `component::vizio::config::step::reconfigure::data_description::host` | Hostname or IP address of your VIZIO SmartCast device. Optionally include the port as host:port; otherwise the standard SmartCast ports are tried. | Värdnamn eller IP-adress för din VIZIO SmartCast-enhet. Du kan även inkludera porten som host:port; annars testas standardportarna för SmartCast. | Shared reference checked |
| 12000 | 921052601 | `component::vizio::config::step::reconfigure::data::host` | Host | Värd | Shared reference checked |

## Historiska förslag som avviker

| Nyckel | Äldre förslag | Aktuell bedömning/live |
|---|---|---|
| `component::mitsubishi_comfort::issues::missing_address::fix_flow::step::addresses::description` | Dessa enheter saknar en känd lokal IP-adress och har därför ännu inga entiteter. Ange den lokala IPv4-adressen för varje enhet nedan. Varje fält är märkt med enhetens MAC-adress. Lämna ett fält tomt om du vill fortsätta vänta på DHCP-upptäckt, som bara fungerar när enheten är i samma nätverk som Home Assistant. När du skickar in uppgifterna läses integreringen in på nytt och varje enhet med en adress konfigureras. Enheter: {devices} | Dessa enheter saknar en känd lokal IP-adress och har därför ännu inga entiteter. Ange den lokala IPv4-adressen för varje enhet nedan. Varje fält är märkt med enhetens MAC-adress. Lämna ett fält tomt om du vill fortsätta vänta på DHCP-upptäckt, som bara fungerar när enheten är i samma nätverk som Home Assistant. När du skickar in uppgifterna läses integrationen in på nytt och varje enhet med en adress konfigureras. Enheter: {devices} |
| `component::kaco_modbus::config::step::user::data_description::unit_id` | Låt värdet vara 1 om växelriktaren inte nås via en RS485-till-TCP-gateway. Ange då i stället adressen som är konfigurerad på gatewayen. | Om växelriktaren nås via en RS485-till-TCP-gateway anger du adressen som är konfigurerad på gatewayen. Annars låter du värdet vara 1. |
| `component::synology_dsm::options::abort::entry_not_loaded` | Integreringen har inte lästs in, så det går inte att visa de utdelade mappar som det går att säkerhetskopiera till. | Integrationen har inte lästs in, så det går inte att visa de utdelade mappar som det går att säkerhetskopiera till. |
| `component::cloud::preview_features::stt_v2::disable_confirmation` | Röstkommandon för assistenter som använder den nya motorn kommer återigen att transkriberas av vår nuvarande tal-till-text-leverantör. | Tal för assistenter som använder den nya motorn transkriberas återigen av vår nuvarande tal-till-text-leverantör. |
| `component::roborock::entity::select::program::state::small_things_drying` | Torkning av små plagg | Torkning av småsaker |
| `component::silla_prism::config::error::invalid_base_topic` | Detta är inte ett giltigt MQTT-ämne. Ange ämnesprefixet från Silla-appen utan jokertecken. | Det här är inte ett giltigt MQTT-ämne. Ange ämnesprefixet från Silla-appen utan jokertecken. |

## Proveniens

- Källäget uppdaterades till HA Core `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- API-exporten återlästes den 2026-11-24. Komplett manifest och snapshotstatus är uppdaterade; PO/TMX-export valideras efter denna TM-uppdatering.
