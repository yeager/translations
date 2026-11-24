# Home Assistant Core – historisk avstämning 12961–13080

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 94 direkta källtexter matchar HA Core-källan; 19 referensanvändningar med 15 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 7 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 12961 | 918180313 | `component::midea::entity::select::direction::state::oscillate` | Oscillate | Oscillera | Core-literal match |
| 12962 | 918180312 | `component::midea::entity::select::direction::name` | Direction | Riktning | Core-literal match |
| 12963 | 918180311 | `component::midea::entity::select::detect_mode::state::pm_25` | PM2.5 | PM2,5 | Core-literal match |
| 12964 | 918180310 | `component::midea::entity::select::detect_mode::state::off` | Off | Av | Core-literal match |
| 12965 | 918180309 | `component::midea::entity::select::detect_mode::state::methanal` | Formaldehyde | Formaldehyd | Core-literal match |
| 12966 | 918180308 | `component::midea::entity::select::detect_mode::name` | Detect mode | Detekteringsläge | Core-literal match |
| 12967 | 918178818 | `component::shelly::issues::rtsp_disabled::title` | RTSP streams disabled on {device_name} | RTSP-strömmar inaktiverade på {device_name} | Core-literal match |
| 12968 | 918178817 | `component::shelly::issues::rtsp_disabled::fix_flow::step::init::title` | RTSP streams disabled on {device_name} | RTSP-strömmar inaktiverade på {device_name} | Shared reference target checked |
| 12969 | 918178816 | `component::shelly::issues::rtsp_disabled::fix_flow::step::init::menu_options::ignore` | Ignore | Ignorera | Shared reference target checked |
| 12970 | 918178815 | `component::shelly::issues::rtsp_disabled::fix_flow::step::init::menu_options::confirm` | Enable RTSP streams | Aktivera RTSP-strömmar | Core-literal match |
| 12971 | 918178814 | `component::shelly::issues::rtsp_disabled::fix_flow::step::init::description` | Your Shelly device {device_name} with IP address {ip_address} has camera RTSP streams disabled. RTSP must be enabled for camera entities to be created.<br><br>Select **Enable RTSP streams** to enable RTSP for all camera streams. | Din Shelly-enhet {device_name} med IP-adressen {ip_address} har kamerans RTSP-strömmar inaktiverade. RTSP måste vara aktiverat för att kameraentiteter ska kunna skapas.<br><br>Välj **Aktivera RTSP-strömmar** för att aktivera RTSP för alla kameraströmmar. | Core-literal match |
| 12972 | 918178813 | `component::shelly::issues::rtsp_disabled::fix_flow::abort::issue_ignored` | Issue ignored | Problemet ignorerat | Shared reference target checked |
| 12973 | 918178812 | `component::shelly::issues::rtsp_disabled::fix_flow::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 12974 | 918177097 | `component::remember_the_milk::issues::deprecated_yaml_import_issue_unknown::title` | The {integration_title} YAML configuration is being removed | YAML-konfigurationen för {integration_title} tas bort | Core-literal match |
| 12975 | 918177096 | `component::remember_the_milk::issues::deprecated_yaml_import_issue_unknown::description` | Configuring {integration_title} via YAML is deprecated and will be removed in a future release. While importing your configuration, an unknown error occurred. Please remove the {domain} configuration from your YAML and set the integration up via the UI. | Konfiguration av {integration_title} via YAML är föråldrad och kommer att tas bort i en framtida version. Ett okänt fel uppstod vid importen av din konfiguration. Ta bort konfigurationen "{domain}" från din YAML-fil och ställ in integrationen via användargränssnittet i stället. | Core-literal match |
| 12976 | 918177095 | `component::remember_the_milk::issues::deprecated_yaml_import_issue_invalid_auth::title` | The {integration_title} YAML configuration is being removed | YAML-konfigurationen för {integration_title} tas bort | Core-literal match |
| 12977 | 918177094 | `component::remember_the_milk::issues::deprecated_yaml_import_issue_invalid_auth::description` | Configuring {integration_title} via YAML is deprecated and will be removed in a future release. While importing your configuration, a stored authentication token could not be found or was invalid. Please remove the {domain} configuration from your YAML and set the integration up via the UI. | Konfigurationen av {integration_title} via YAML är föråldrad och kommer att tas bort i en framtida version. Vid importen av din konfiguration kunde ett lagrat autentiseringstoken inte hittas eller visade sig vara ogiltigt. Ta bort konfigurationen "{domain}" från din YAML-fil och ställ in integrationen via användargränssnittet i stället. | Core-literal match |
| 12978 | 918177093 | `component::remember_the_milk::issues::deprecated_yaml_import_issue_cannot_connect::title` | The {integration_title} YAML configuration is being removed | YAML-konfigurationen för {integration_title} tas bort | Core-literal match |
| 12979 | 918177092 | `component::remember_the_milk::issues::deprecated_yaml_import_issue_cannot_connect::description` | Configuring {integration_title} via YAML is deprecated and will be removed in a future release. While importing your configuration, a connection error occurred. Please restart Home Assistant to try again, or remove the {domain} configuration from your YAML and set the integration up via the UI. | Konfiguration av {integration_title} via YAML är föråldrad och kommer att tas bort i en framtida version. Ett anslutningsfel uppstod när din konfiguration importerades. Starta om Home Assistant för att försöka igen, eller ta bort konfigurationen "{domain}" från din YAML-fil och ställ in integrationen via användargränssnittet i stället. | Core-literal match |
| 12980 | 918177091 | `component::remember_the_milk::config::step::user::description` | Enter the API key and shared secret from a Remember The Milk API application. You can request these credentials using your Remember The Milk account. | Ange API-nyckeln och den delade hemligheten från en Remember The Milk API-applikation. Du kan begära dessa inloggningsuppgifter via ditt Remember The Milk-konto. | Core-literal match |
| 12981 | 918177090 | `component::remember_the_milk::config::step::user::data_description::shared_secret` | The shared secret of your Remember The Milk API application. | Den delade hemligheten för din Remember The Milk API-applikation. | Core-literal match |
| 12982 | 918177089 | `component::remember_the_milk::config::step::user::data_description::api_key` | The API key of your Remember The Milk API application. | API-nyckeln för din Remember The Milk API-applikation. | Core-literal match |
| 12983 | 918177088 | `component::remember_the_milk::config::step::user::data::shared_secret` | Shared secret | Delad hemlighet | Core-literal match |
| 12984 | 918177087 | `component::remember_the_milk::config::step::user::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 12985 | 918177086 | `component::remember_the_milk::config::step::auth::description` | Follow the link to authorize Home Assistant to access your Remember The Milk account. When done, select **Submit** to continue.<br><br>[Authorize]({url}) | Följ länken för att ge Home Assistant behörighet att komma åt ditt Remember The Milk-konto. När du är klar klickar du på knappen nedan för att fortsätta.<br><br>[Godkänn]({url}) | Core-literal match |
| 12986 | 918177085 | `component::remember_the_milk::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 12987 | 918177084 | `component::remember_the_milk::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 12988 | 918177083 | `component::remember_the_milk::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 12989 | 918177082 | `component::remember_the_milk::config::abort::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 12990 | 918177081 | `component::remember_the_milk::config::abort::timeout_token` | Timeout getting access token | Timeout vid hämtning av åtkomsttoken | Core-literal match |
| 12991 | 918177080 | `component::remember_the_milk::config::abort::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 12992 | 918177079 | `component::remember_the_milk::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 12993 | 918177078 | `component::remember_the_milk::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Shared reference target checked |
| 12994 | 918174719 | `component::centriconnect::exceptions::unexpected_response::message` | Unexpected response: {error} | Oväntat svar: {error} | Core-literal match |
| 12995 | 918174718 | `component::centriconnect::exceptions::entry_setup_failed::message` | Could not fetch device info | Det gick inte att hämta enhetsinformation | Core-literal match |
| 12996 | 918174717 | `component::centriconnect::exceptions::communication_error::message` | Error communicating with device: {error} | Fel vid kommunikation med enheten: {error} | Core-literal match |
| 12997 | 918171037 | `component::hotspring::entity::sensor::wifi_dongle_version::name` | Wi-Fi dongle version | Wi-Fi-dongelversion | Core-literal match |
| 12998 | 918171036 | `component::hotspring::entity::sensor::water_care_salt_value::name` | Salt value | Saltvärde | Core-literal match |
| 12999 | 918171035 | `component::hotspring::entity::sensor::water_care_120_day_timer::name` | Salt cartridge age | Saltpatronens ålder | Core-literal match |
| 13000 | 918171034 | `component::hotspring::entity::sensor::water_care_10_day_timer::name` | Salt 10-day check timer | Timer för kontroll av salt efter 10 dagar | Core-literal match |
| 13001 | 918171033 | `component::hotspring::entity::sensor::fwss_version::name` | FreshWater Salt System version | FreshWater Salt System-version | Core-literal match |
| 13002 | 918171032 | `component::hotspring::entity::sensor::current_temperature::name` | Current temperature | Aktuell temperatur | Core-literal match |
| 13003 | 918171031 | `component::hotspring::entity::sensor::control_box_version::name` | Control box version | Styrenhetens version | Core-literal match |
| 13004 | 918169874 | `component::portainer::entity::sensor::image_version::name` | Image version | Avbildningsversion | Core-literal match |
| 13005 | 918169873 | `component::portainer::entity::sensor::image_created::name` | Image created | Avbildning skapad | Core-literal match |
| 13006 | 918169329 | `component::simplepush::exceptions::title_or_message_too_long::message` | The notification title or message is too long. | Aviseringens titel eller brödtext är för lång. | Core-literal match |
| 13007 | 918169328 | `component::simplepush::exceptions::send_message_failed::message` | Failed to send the Simplepush notification. | Det gick inte att skicka Simplepush-aviseringen. | Core-literal match |
| 13008 | 918169172 | `component::homewizard::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 13009 | 918168923 | `component::switchbot_cloud::entity::select::night_light_control::state::soft` | Soft | Mjuk | Core-literal match |
| 13010 | 918168922 | `component::switchbot_cloud::entity::select::night_light_control::state::on` | On | På | Shared reference target checked |
| 13011 | 918168921 | `component::switchbot_cloud::entity::select::night_light_control::state::off` | Off | Av | Shared reference target checked |
| 13012 | 918168920 | `component::switchbot_cloud::entity::select::night_light_control::state::bright` | Bright | Ljus | Core-literal match |
| 13013 | 918168919 | `component::switchbot_cloud::entity::select::night_light_control::name` | Night light | Nattlampa | Core-literal match |
| 13014 | 918167277 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::watering_already_active` | Watering already active | Bevattning redan aktiv | Core-literal match |
| 13015 | 918167276 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::valve_motor_error` | Valve motor error | Fel i ventilmotor | Core-literal match |
| 13016 | 918167275 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::sprinkler_motor_error` | Sprinkler motor error | Fel på sprinklermotor | Core-literal match |
| 13017 | 918167274 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::rotation_sensor_error` | Rotation sensor error | Fel på rotationssensor | Core-literal match |
| 13018 | 918167273 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::rain_sensor` | Rain sensor | Regnsensor | Core-literal match |
| 13019 | 918167272 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::rain_pause` | Rain pause | Regnpaus | Core-literal match |
| 13020 | 918167271 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::position_changed` | Position changed | Position ändrad | Core-literal match |
| 13021 | 918167270 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::other_schedule_with_same_start_time` | Other schedule with same start time | Annat schema med samma starttid | Core-literal match |
| 13022 | 918167269 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::operational_mode_changed` | Operational mode changed | Driftläge ändrat | Core-literal match |
| 13023 | 918167268 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::none` | Inactive | Inaktiv | Core-literal match |
| 13024 | 918167267 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::no_water` | No water | Inget vatten | Core-literal match |
| 13025 | 918167266 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::manual_mode` | Manual mode | Manuellt läge | Core-literal match |
| 13026 | 918167265 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::irrigation_control_changed` | Irrigation control changed | Bevattningskontrollen har ändrats | Core-literal match |
| 13027 | 918167264 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::humidity_sensor` | Humidity sensor | Luftfuktighetssensor | Core-literal match |
| 13028 | 918167263 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::contour_not_enabled_for_position` | Contour not enabled for position | Kontur inte aktiverad för position | Core-literal match |
| 13029 | 918167262 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::contour_not_active` | Contour not active | Kontur inte aktiv | Core-literal match |
| 13030 | 918167261 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::contour_data_invalid` | Contour data invalid | Ogiltiga konturdata | Core-literal match |
| 13031 | 918167260 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::charging_cable_plugged` | Charging cable plugged | Laddningskabeln är ansluten | Core-literal match |
| 13032 | 918167259 | `component::gardena_bluetooth::entity::sensor::skipped_reason::state::battery_empty` | Battery empty | Batteriet är tomt | Core-literal match |
| 13033 | 918167258 | `component::gardena_bluetooth::entity::sensor::skipped_reason::name` | Skipped reason | Orsak till att bevattningen hoppades över | Core-literal match |
| 13034 | 918166807 | `component::openevse::entity::switch::solar_pv_divert::name` | Solar PV divert | Solcellsavledning | Core-literal match |
| 13035 | 918166806 | `component::openevse::entity::switch::manual_override::name` | Manual override | Manuell överstyrning | Core-literal match |
| 13036 | 918166805 | `component::openevse::entity::switch::current_shaper::name` | Current shaper | Strömformare | Core-literal match |
| 13037 | 918166750 | `component::lyngdorf::entity::number::trim_treble::name` | Trim treble | Trimma diskant | Core-literal match |
| 13038 | 918166749 | `component::lyngdorf::entity::number::trim_surround::name` | Trim surround | Trimma surround | Core-literal match |
| 13039 | 918166748 | `component::lyngdorf::entity::number::trim_lfe::name` | Trim LFE | Trimma LFE | Core-literal match |
| 13040 | 918166747 | `component::lyngdorf::entity::number::trim_height::name` | Trim height | Trimma höjd | Core-literal match |
| 13041 | 918166746 | `component::lyngdorf::entity::number::trim_centre::name` | Trim centre | Trimma center | Core-literal match |
| 13042 | 918166745 | `component::lyngdorf::entity::number::trim_bass::name` | Trim bass | Trimma bas | Core-literal match |
| 13043 | 918166744 | `component::lyngdorf::entity::number::lipsync::name` | Lip sync | Läppsynk | Core-literal match |
| 13044 | 917720464 | `component::hotspring::config::step::zeroconf_confirm::title` | Discovered Hot Spring spa | Upptäckt Hot Spring-spabad | Core-literal match |
| 13045 | 917720463 | `component::hotspring::config::step::zeroconf_confirm::description` | Do you want to add the Hot Spring spa named `{name}` to Home Assistant? | Vill du lägga till Hot Spring-spabadet med namnet ”{name}” i Home Assistant? | Core-literal match |
| 13046 | 917325498 | `component::shelly::entity::switch::camera_privacy::name` | Privacy | Integritet | Core-literal match |
| 13047 | 917254897 | `component::lyngdorf::config::step::reconfigure::title` | Lyngdorf device connection | Lyngdorf-enhetsanslutning | Shared reference target checked |
| 13048 | 917254896 | `component::lyngdorf::config::step::reconfigure::description` | Update the address Home Assistant uses to reach this device. It must be the same device; a different one will be rejected. | Uppdatera den adress som Home Assistant använder för att nå den här enheten. Det måste vara samma enhet; en annan enhet kommer att avvisas. | Core-literal match |
| 13049 | 917254895 | `component::lyngdorf::config::step::reconfigure::data_description::host` | Hostname or IP address of the Lyngdorf device | Värdnamn eller IP-adress för Lyngdorf-enheten | Shared reference target checked |
| 13050 | 917254894 | `component::lyngdorf::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 13051 | 917254893 | `component::lyngdorf::config::abort::unique_id_mismatch` | The device at this address is a different Lyngdorf device from the one this entry was set up with. | Enheten på den här adressen är en annan Lyngdorf-enhet än den som denna post skapades för. | Core-literal match |
| 13052 | 917254892 | `component::lyngdorf::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 13053 | 917212451 | `component::recorder::issues::database_engine_too_old::title` | Update {database_engine} to {min_version} or later to continue using the recorder | Uppdatera {database_engine} till {min_version} eller senare för att kunna fortsätta använda inspelaren | Core-literal match |
| 13054 | 917212450 | `component::recorder::issues::database_engine_too_old::description` | Support for version {server_version} of {database_engine} is ending; the minimum supported version will be {min_version}. Please upgrade your database software and restart Home Assistant. | Stödet för version {server_version} av {database_engine} upphör; den lägsta version som stöds kommer att vara {min_version}. Uppgradera din databasprogramvara och starta om Home Assistant. | Core-literal match |
| 13055 | 917212449 | `component::recorder::issues::database_engine_not_supported_lts::title` | Update {database_engine} to a supported LTS version to continue using the recorder | Uppdatera {database_engine} till en LTS-version som stöds för att kunna fortsätta använda inspelaren | Core-literal match |
| 13056 | 917212448 | `component::recorder::issues::database_engine_not_supported_lts::description` | Version {server_version} of {database_engine} is not a supported long-term support (LTS) release. Support for short-term releases and end-of-life LTS releases will be removed; please upgrade to one of the supported LTS versions ({lts_versions}) and restart Home Assistant to continue using the recorder. | Version {server_version} av {database_engine} är inte en version med långsiktigt stöd (LTS). Stödet för kortvariga versioner och LTS-versioner som inte längre stöds kommer att avslutas. Uppgradera till en av de LTS-versioner som stöds ({lts_versions}) och starta om Home Assistant för att kunna fortsätta använda inspelaren. | Core-literal match |
| 13057 | 917201288 | `component::shelly::entity::camera::stream::name` | Stream {stream_id} | Ström {stream_id} | Core-literal match |
| 13058 | 916938942 | `component::hassio::issues::issue_mount_mount_failed::fix_flow::step::mount_move_local_data::description` | Select **Submit** to move the local data blocking `{reference}` to a `{reference}_local_recovery` folder and set up the mount again.<br><br>No files are deleted. For media and share mounts the recovery folder is created next to the mount, where you can review and remove it. For backup mounts it is placed in local backup storage. | Välj **Bekräfta** för att flytta de lokala data som blockerar `{reference}` till mappen `{reference}_local_recovery` och konfigurera monteringen på nytt.<br><br>Inga filer raderas. För medie- och delningsmonteringar skapas återställningsmappen bredvid monteringen, där du kan granska och ta bort den. För säkerhetskopieringsmonteringar placeras den i det lokala säkerhetskopieringslagret. | Core-literal match |
| 13059 | 916938941 | `component::hassio::issues::issue_mount_mount_failed::fix_flow::step::fix_menu::menu_options::mount_move_local_data` | Move blocking local data away | Flytta bort lokal data som blockerar | Core-literal match |
| 13060 | 916751918 | `component::monzo::entity::sensor::spend_today::name` | Spent today | Spenderat i dag | Core-literal match |
| 13061 | 916751830 | `component::nfandroidtv::exceptions::invalid_interrupt::message` | Invalid interrupt value: {interrupt} | Ogiltigt avbrottsvärde: {interrupt} | Core-literal match |
| 13062 | 916751829 | `component::nfandroidtv::exceptions::invalid_duration::message` | Invalid duration value: {duration} | Ogiltigt varaktighetsvärde: {duration} | Core-literal match |
| 13063 | 916736809 | `component::androidtv_remote::exceptions::empty_key_code::message` | Command "{command}" is missing a key code after the direction prefix | Kommandot ”{command}” saknar en knappkod efter riktningsprefixet | Core-literal match |
| 13064 | 916736808 | `component::androidtv_remote::exceptions::direction_prefix_with_hold_secs::message` | Command "{command}" combines a direction prefix with hold_secs; specify only one | Kommandot ”{command}” kombinerar ett riktningsprefix med hold_secs; ange endast ett | Core-literal match |
| 13065 | 916686177 | `component::zwave_js::config::abort::addon_already_configured` | A configuration entry using the Z-Wave JS app already exists. Reconfigure or migrate that entry instead. | Det finns redan en konfigurationspost som använder Z-Wave JS-appen. Konfigurera om eller migrera den posten i stället. | Core-literal match |
| 13066 | 916347906 | `component::home_connect::config::step::scopes::title` | Scopes | Behörigheter | Source-path follow-up open |
| 13067 | 916347905 | `component::home_connect::config::step::scopes::description` | Select the optional scopes you want to enable for Home Connect authentication. | Välj vilka valfria behörigheter du vill aktivera för Home Connect-autentiseringen. | Source-path follow-up open |
| 13068 | 916347904 | `component::home_connect::config::step::scopes::data_description::images_scope` | Allows Home Assistant to access images from your Home Connect devices. | Gör det möjligt för Home Assistant att komma åt bilder från dina Home Connect-enheter. | Source-path follow-up open |
| 13069 | 916347903 | `component::home_connect::config::step::scopes::data::images_scope` | Images scope | Behörighet för bilder | Source-path follow-up open |
| 13070 | 916347902 | `component::home_connect::config::abort::user_rejected_authorize` | Account linking rejected: {error} | Kontolänkning avvisades: {error} | Source-path follow-up open |
| 13071 | 915462379 | `component::vallox::selector::profile::options::auto` | Auto | Auto | Shared reference target checked |
| 13072 | 915376948 | `component::roborock::issues::deprecated_mop_drying_scripts::title` | The Roborock mop drying binary sensor is deprecated | Roborocks binära sensor för mopptorkning är utfasad | Shared reference target checked |
| 13073 | 915376947 | `component::roborock::issues::deprecated_mop_drying_scripts::description` | The `{entity_id}` ({entity_name}) binary sensor is deprecated and has been replaced by the **Mop drying** switch, which reports the same state and can also start and stop drying.<br><br>It is still used in the following automations or scripts:<br>{items}<br><br>Update them to use the new switch entity, then disable `{entity_id}` to have it removed. | Den binära sensorn `{entity_id}` ({entity_name}) är utfasad och har ersatts av brytaren **Mopptorkning**, som rapporterar samma tillstånd och dessutom kan starta och stoppa torkningen.<br><br>Sensorn används fortfarande i följande automatiseringar eller skript:<br>{items}<br><br>Uppdatera dem så att de använder den nya brytarentiteten och inaktivera sedan `{entity_id}` för att ta bort den. | Core-literal match |
| 13074 | 915376946 | `component::roborock::issues::deprecated_mop_drying::title` | The Roborock mop drying binary sensor is deprecated | Roborocks binära sensor för mopptorkning är utfasad | Core-literal match |
| 13075 | 915376945 | `component::roborock::issues::deprecated_mop_drying::description` | The `{entity_id}` ({entity_name}) binary sensor is deprecated and has been replaced by the **Mop drying** switch, which reports the same state and can also start and stop drying.<br><br>Update any dashboards, templates, automations or scripts to use the new switch entity, then disable `{entity_id}` to have it removed. | Den binära sensorn `{entity_id}` ({entity_name}) är utfasad och har ersatts av brytaren **Mopptorkning**, som rapporterar samma tillstånd och dessutom kan starta och stoppa torkningen.<br><br>Uppdatera alla kontrollpaneler, mallar, automatiseringar och skript så att de använder den nya brytarentiteten och inaktivera sedan `{entity_id}` för att ta bort den. | Core-literal match |
| 13076 | 914726524 | `component::lunatone::entity::binary_sensor::scan_status::name` | Scan status | Skanningsstatus | Core-literal match |
| 13077 | 914585010 | `component::midea::exceptions::device_communication_error::message` | Error communicating with the device: {error} | Fel vid kommunikation med enheten: {error} | Core-literal match |
| 13078 | 914577676 | `component::transmission::entity::sensor::download_dir_free_space::name` | Available disk space | Ledigt diskutrymme | Core-literal match |
| 13079 | 914577600 | `component::intelliclima::entity::binary_sensor::filter_cleaning::name` | Filter cleaning required | Filterrengöring krävs | Core-literal match |
| 13080 | 914313001 | `component::ecovacs::entity::sensor::total_stats_time_mower::name` | Total mowing duration | Total klipptid | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 918169172 | `component::homewizard::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |
| 917254892 | `component::lyngdorf::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 916347906 | `component::home_connect::config::step::scopes::title` | Scopes |
| 916347905 | `component::home_connect::config::step::scopes::description` | Select the optional scopes you want to enable for Home Connect authentication. |
| 916347904 | `component::home_connect::config::step::scopes::data_description::images_scope` | Allows Home Assistant to access images from your Home Connect devices. |
| 916347903 | `component::home_connect::config::step::scopes::data::images_scope` | Images scope |
| 916347902 | `component::home_connect::config::abort::user_rejected_authorize` | Account linking rejected: {error} |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
