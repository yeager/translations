# Home Assistant Core – historisk avstämning 18001–18120

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 105 direkta källtexter matchar HA Core-källan; 9 referensanvändningar med 9 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 6 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 18001 | 856458202 | `component::zwave_js::exceptions::no_available_user_slots::message` | No available user slots on this device | Inga tillgängliga användarplatser på den här enheten | Core-literal match |
| 18002 | 856458201 | `component::zwave_js::exceptions::no_available_credential_slots::message` | No available {credential_type} credential slots on this device | Inga tillgängliga {credential_type} autentiseringsuppgifter på den här enheten | Core-literal match |
| 18003 | 856458200 | `component::zwave_js::exceptions::get_users_failed::message` | Failed to get users: {error} | Misslyckades med att hämta användare: {error} | Core-literal match |
| 18004 | 856458199 | `component::zwave_js::exceptions::get_credential_capabilities_failed::message` | Failed to get credential capabilities: {error} | Misslyckades med att hämta autentiseringsuppgifter: {error} | Core-literal match |
| 18005 | 856458198 | `component::zwave_js::exceptions::delete_user_failed::message` | Failed to delete user {user_id}: {error} | Misslyckades med att ta bort användaren {user_id}: {error} | Core-literal match |
| 18006 | 856458197 | `component::zwave_js::exceptions::delete_credential_failed::message` | Failed to delete credential: {error} | Misslyckades med att ta bort inloggningsuppgifter: {error} | Core-literal match |
| 18007 | 856458196 | `component::zwave_js::exceptions::delete_all_users_failed::message` | Failed to delete all users: {error} | Misslyckades med att ta bort alla användare: {error} | Core-literal match |
| 18008 | 856458195 | `component::zwave_js::exceptions::delete_all_credentials_partial_failure::message` | Failed to delete {failed_count} credentials for user {user_id}. See logs for details. | Misslyckades med att ta bort {failed_count} -autentiseringsuppgifter för användaren {user_id}. Se loggar för detaljer. | Core-literal match |
| 18009 | 856458194 | `component::zwave_js::exceptions::delete_all_credentials_failed::message` | Failed to delete all credentials for user {user_id}: {error} | Misslyckades med att ta bort alla autentiseringsuppgifter för användaren {user_id}: {error} | Core-literal match |
| 18010 | 856458193 | `component::zwave_js::exceptions::credential_type_not_supported::message` | Credential type {credential_type} is not supported on this device | Denna autentiseringstyp ({credential_type}) stöds inte på den här enheten | Core-literal match |
| 18011 | 856458192 | `component::zwave_js::exceptions::credential_slot_out_of_range::message` | Credential slot for {credential_type} must be between 1 and {max_slot}. | Autentiseringsplats för {credential_type} måste vara mellan 1 och {max_slot}. | Source-path follow-up open |
| 18012 | 856458191 | `component::zwave_js::exceptions::credential_rejected_wrong_uuid::message` | The device rejected the credential because the user unique identifier does not match. | Enheten avvisade referensen eftersom den unika identifieraren för användaren inte stämmer överens. | Core-literal match |
| 18013 | 856458190 | `component::zwave_js::exceptions::credential_rejected_unknown::message` | The device rejected the credential without giving a reason. | Enheten avvisade inloggningsuppgifterna utan att ange någon orsak. | Core-literal match |
| 18014 | 856458189 | `component::zwave_js::exceptions::credential_rejected_modify_empty::message` | Cannot modify credential: the slot is empty. | Det går inte att ändra autentiseringsuppgifterna: platsen är tom. | Core-literal match |
| 18015 | 856458188 | `component::zwave_js::exceptions::credential_rejected_manufacturer_rules::message` | The credential violates the device's manufacturer security rules (for example, it is too short, too long, or uses a disallowed pattern). | Autentiseringsuppgifterna strider mot enhetstillverkarens säkerhetsregler (de är till exempel för korta, för långa eller följer ett otillåtet mönster). | Core-literal match |
| 18016 | 856458187 | `component::zwave_js::exceptions::credential_rejected_duplicate::message` | This credential is already registered on the device. | Denna autentiseringsuppgift är redan registrerad på enheten. | Core-literal match |
| 18017 | 856458186 | `component::zwave_js::exceptions::credential_rejected_add_occupied::message` | Cannot add credential: the target slot is already in use. | Det går inte att lägga till autentiseringsuppgifter: målplatsen används redan. | Core-literal match |
| 18018 | 856458185 | `component::zwave_js::exceptions::credential_data_pin_not_digits::message` | PIN code must contain only digits. | PIN-koden får endast innehålla siffror. | Core-literal match |
| 18019 | 856458184 | `component::zwave_js::exceptions::credential_data_invalid_length::message` | Credential of type {credential_type} must be between {min_length} and {max_length} characters long. | Autentiseringsuppgifter av typen {credential_type} måste vara mellan {min_length} och {max_length} tecken långa. | Core-literal match |
| 18020 | 856458183 | `component::zwave_js::exceptions::access_control_not_supported::message` | Access control is not supported on this device | Åtkomstkontroll stöds inte på den här enheten | Core-literal match |
| 18021 | 856273151 | `component::cert_expiry::config::step::reconfigure::title` | Reconfigure the certificate to test | Konfigurera om certifikatet som ska testas | Core-literal match |
| 18022 | 856273150 | `component::cert_expiry::config::step::reconfigure::data::port` | Port | Port | Shared reference target checked |
| 18023 | 856273149 | `component::cert_expiry::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 18024 | 856273148 | `component::cert_expiry::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 18025 | 856232973 | `component::speedtestdotnet::options::step::init::data_description::server_name` | The Speedtest.net server to use for tests. Select auto detect to automatically choose a server. | Den Speedtest.net-server som ska användas för tester. Välj auto detect för att automatiskt välja en server. | Core-literal match |
| 18026 | 856175752 | `component::smlight::services::play_rtttl::name` | Play RTTTL tone | Spela RTTTL-ton | Core-literal match |
| 18027 | 856175751 | `component::smlight::services::play_rtttl::fields::octave::name` | Octave | Oktav | Core-literal match |
| 18028 | 856175750 | `component::smlight::services::play_rtttl::fields::octave::description` | Default octave (4–7). | Standardoktav (4–7). | Core-literal match |
| 18029 | 856175749 | `component::smlight::services::play_rtttl::fields::notes::name` | Notes | Noter | Core-literal match |
| 18030 | 856175748 | `component::smlight::services::play_rtttl::fields::notes::description` | The note sequence in RTTTL format, e.g. 8d,8d#,8e,c6. | Notföljden i RTTTL-format, t.ex. 8d, 8d#, 8e, c6. | Core-literal match |
| 18031 | 856175747 | `component::smlight::services::play_rtttl::fields::duration::name` | Duration | Varaktighet | Core-literal match |
| 18032 | 856175746 | `component::smlight::services::play_rtttl::fields::duration::description` | Default note duration (1, 2, 4, 8, 16 or 32). Omit to use the RTTTL default of 4. | Standardlängd för not (1, 2, 4, 8, 16 eller 32). Lämna fältet tomt för att använda RTTTL:s standardvärde 4. | Core-literal match |
| 18033 | 856175745 | `component::smlight::services::play_rtttl::fields::device_id::name` | Device | Enhet | Core-literal match |
| 18034 | 856175744 | `component::smlight::services::play_rtttl::fields::device_id::description` | The SMLIGHT device. | SMLIGHT-enheten. | Core-literal match |
| 18035 | 856175743 | `component::smlight::services::play_rtttl::fields::bpm::name` | BPM | BPM | Core-literal match |
| 18036 | 856175742 | `component::smlight::services::play_rtttl::fields::bpm::description` | Tempo in beats per minute. Omit to use the RTTTL default of 63. | Tempo i slag per minut (bpm). Utelämna detta för att använda RTTTL:s standardvärde på 63. | Core-literal match |
| 18037 | 856175741 | `component::smlight::services::play_rtttl::description` | Play an RTTTL melody on the SMLIGHT device buzzer. | Spela upp en RTTTL-melodi på SMLIGHT-enhetens summer. | Core-literal match |
| 18038 | 856175740 | `component::smlight::exceptions::play_tone_failed::message` | Failed to play tone on {device_name}: {error}. | Det gick inte att spela upp ljudet på {device_name}: {error}. | Core-literal match |
| 18039 | 856175739 | `component::smlight::exceptions::not_supported_buzzer::message` | The selected SMLIGHT device does not support the buzzer feature. This feature is only available on Ultima models. | Den valda SMLIGHT-enheten stöder inte summerfunktionen. Denna funktion finns endast på Ultima-modellerna. | Core-literal match |
| 18040 | 856175738 | `component::smlight::exceptions::no_device_found::message` | No valid SMLIGHT device found for the given targets. | Ingen giltig SMLIGHT-enhet hittades för de angivna målen. | Core-literal match |
| 18041 | 856175712 | `component::freebox::entity::switch::wifi::name` | Wi-Fi | Wi-Fi | Core-literal match |
| 18042 | 856175711 | `component::freebox::entity::sensor::rate_up::name` | Upload speed | Uppladdningshastighet | Core-literal match |
| 18043 | 856175710 | `component::freebox::entity::sensor::rate_down::name` | Download speed | Nedladdningshastighet | Core-literal match |
| 18044 | 856175709 | `component::freebox::entity::sensor::partition_free_space::name` | {partition} free space | {partition} fritt utrymme | Core-literal match |
| 18045 | 856175708 | `component::freebox::entity::sensor::missed::name` | Missed calls | Missade samtal | Core-literal match |
| 18046 | 856175707 | `component::freebox::entity::button::mark_calls_as_read::name` | Mark calls as read | Markera samtal som lästa | Core-literal match |
| 18047 | 856175706 | `component::freebox::entity::binary_sensor::raid_degraded::name` | RAID array {id} degraded | RAID-matris {id} degraderad | Core-literal match |
| 18048 | 856175705 | `component::freebox::entity::binary_sensor::cover::name` | Cover | Skydd | Core-literal match |
| 18049 | 856167442 | `component::homeassistant::issues::platform_setup_not_supported::title` | Unused YAML configuration for the {integration_domain} integration | Oanvänd YAML-konfiguration för integrationen {integration_domain} | Core-literal match |
| 18050 | 856167441 | `component::homeassistant::issues::platform_setup_not_supported::description` | It's not possible to configure {integration_domain} {platform_domain} by adding `{platform_key}` to the {platform_domain} configuration. Please check the documentation for more information on how to set up this integration.<br><br>To resolve this:<br><br>1. Remove `{platform_key}` occurrences from the `{platform_domain}:` configuration in your YAML configuration file.<br><br>2. Restart Home Assistant. | Det går inte att konfigurera {integration_domain} {platform_domain} genom att lägga till `{platform_key}` i {platform_domain} -konfigurationen. Mer information om hur du konfigurerar den här integrationen finns i dokumentationen. <br><br>Så här löser du problemet: <br><br>1. Ta bort förekomster av `{platform_key}` från konfigurationen `{platform_domain}:` i din YAML-konfigurationsfil. <br><br>2. Starta om Home Assistant. | Core-literal match |
| 18051 | 856167440 | `component::homeassistant::issues::platform_config_not_supported::title` | Unsupported YAML configuration for the {integration_domain} integration | YAML-konfiguration som inte stöds för {integration_domain} -integrationen | Core-literal match |
| 18052 | 856167439 | `component::homeassistant::issues::platform_config_not_supported::description` | Configuring the {integration_domain} integration by adding `{platform_key}` under the `{platform_domain}:` key is not supported. The {integration_domain} integration must be configured under its own `{integration_domain}:` key instead.<br><br>To resolve this:<br><br>1. Remove the following from your YAML configuration file:<br><br>{yaml_example}<br><br>2. Move the configuration under the `{integration_domain}:` key instead.<br><br>3. Restart Home Assistant.<br><br>To see the detailed documentation, select Learn more. | Det går inte att konfigurera {integration_domain} -integrationen genom att lägga till `{platform_key}` under nyckeln `{platform_domain}:`. Integrationen {integration_domain} måste istället konfigureras under sin egen nyckel `{integration_domain}:`. <br><br>Så här löser du detta: <br><br>1. Ta bort följande från din YAML-konfigurationsfil:<br><br>{yaml_example}<br><br>2. Flytta konfigurationen under nyckeln `{integration_domain}:` istället. <br><br>3. Starta om Home Assistant. <br><br>För att se den detaljerade dokumentationen, välj Läs mer. | Core-literal match |
| 18053 | 856164112 | `component::rflink::issues::yaml_migration::title` | Your {platform} RFLink configuration needs to be migrated | Din {platform} RFLink-konfiguration måste migreras | Source-path follow-up open |
| 18054 | 856164111 | `component::rflink::issues::yaml_migration::description` | Your current RFLink {platform} YAML configuration needs to be migrated to the new configuration format. | Din nuvarande RFLink {platform} YAML-konfiguration måste migreras till det nya konfigurationsformatet. | Source-path follow-up open |
| 18055 | 856103836 | `component::homekit::options::step::bridged_device_triggers::title` | Bridged device triggers | Bryggade enhetsutlösare | Core-literal match |
| 18056 | 856103835 | `component::homekit::options::step::bridged_device_triggers::description` | Programmable switches are created for each selected device. When a device trigger fires, HomeKit can be configured to run an automation or scene. | Programmerbara brytare skapas för varje vald enhet. När en enhetsutlösare utlöses kan HomeKit konfigureras för att köra en automatisering eller scen. | Core-literal match |
| 18057 | 856103834 | `component::homekit::options::step::bridged_device_triggers::data::devices` | Devices (Triggers) | Enheter (utlösare) | Core-literal match |
| 18058 | 856073034 | `component::solaredge::entity::sensor::storage_flow_direction::state::discharge` | Discharge | Urladdning | Core-literal match |
| 18059 | 856073033 | `component::solaredge::entity::sensor::storage_flow_direction::state::charge` | Charge | Laddning | Core-literal match |
| 18060 | 856073032 | `component::solaredge::entity::sensor::storage_flow_direction::name` | Storage flow direction | Flödesriktning för lagring | Core-literal match |
| 18061 | 856073031 | `component::solaredge::entity::sensor::grid_flow_direction::state::import` | Import | Import | Core-literal match |
| 18062 | 856073030 | `component::solaredge::entity::sensor::grid_flow_direction::state::export` | Export | Export | Core-literal match |
| 18063 | 856073029 | `component::solaredge::entity::sensor::grid_flow_direction::name` | Grid flow direction | Nätets flödesriktning | Core-literal match |
| 18064 | 856072697 | `component::jewish_calendar::selector::yearly_events::options::weekly_portion` | Torah portion | Torah-avsnitt | Core-literal match |
| 18065 | 856072696 | `component::jewish_calendar::selector::yearly_events::options::omer_count` | Omer count | Omer-räkning | Core-literal match |
| 18066 | 856072695 | `component::jewish_calendar::selector::yearly_events::options::holiday` | Jewish holidays | Judiska helgdagar | Core-literal match |
| 18067 | 856072694 | `component::jewish_calendar::selector::yearly_events::options::havdalah` | Havdalah | Havdalah | Core-literal match |
| 18068 | 856072693 | `component::jewish_calendar::selector::yearly_events::options::candle_lighting` | Candle lighting | Tändning av ljus | Core-literal match |
| 18069 | 856072692 | `component::jewish_calendar::selector::learning_schedule::options::daf_yomi` | Daf Yomi | Daf Yomi | Core-literal match |
| 18070 | 856072691 | `component::jewish_calendar::selector::daily_events::options::tset_hakohavim_tsom` | T'set Hakochavim (nightfall) | T'set Hakochavim (skymning) | Source-path follow-up open |
| 18071 | 856072690 | `component::jewish_calendar::selector::daily_events::options::sof_zman_tfilla_mga` | Sof Zman Tefilla (Mg"A) | Sof Zman Tefilla (Mg"A) | Core-literal match |
| 18072 | 856072689 | `component::jewish_calendar::selector::daily_events::options::sof_zman_tfilla_gra` | Sof Zman Tefilla (Gr"A) | Sof Zman Tefilla (Gr"A) | Core-literal match |
| 18073 | 856072688 | `component::jewish_calendar::selector::daily_events::options::sof_zman_shema_mga` | Sof Zman Shema (Mg"A) | Sof Zman Shema (Mg"A) | Core-literal match |
| 18074 | 856072687 | `component::jewish_calendar::selector::daily_events::options::sof_zman_shema_gra` | Sof Zman Shema (Gr"A) | Sof Zman Shema (Gr"A) | Core-literal match |
| 18075 | 856072686 | `component::jewish_calendar::selector::daily_events::options::shkia` | Shkia (sunset) | Shkia (solnedgång) | Core-literal match |
| 18076 | 856072685 | `component::jewish_calendar::selector::daily_events::options::plag_hamincha` | Plag Hamincha | Plag Hamincha | Core-literal match |
| 18077 | 856072684 | `component::jewish_calendar::selector::daily_events::options::netz_hachama` | Netz Hachama (sunrise) | Netz Hachama (soluppgång) | Core-literal match |
| 18078 | 856072683 | `component::jewish_calendar::selector::daily_events::options::mincha_ketana` | Mincha Ketana | Mincha Ketana | Core-literal match |
| 18079 | 856072682 | `component::jewish_calendar::selector::daily_events::options::mincha_gedola` | Mincha Gedola | Mincha Gedola | Core-literal match |
| 18080 | 856072681 | `component::jewish_calendar::selector::daily_events::options::date` | Hebrew date | Hebreiskt datum | Core-literal match |
| 18081 | 856072680 | `component::jewish_calendar::selector::daily_events::options::chatzot_hayom` | Chatzot Hayom (midday) | Chatzot Hayom (middag) | Core-literal match |
| 18082 | 856072679 | `component::jewish_calendar::selector::daily_events::options::alot_hashachar` | Alot Hashachar (dawn) | Alot Hashachar (gryning) | Core-literal match |
| 18083 | 856072678 | `component::jewish_calendar::options::step::init::data_description::yearly_events` | Select which yearly Jewish calendar events should be displayed in the Yearly Events calendar | Välj vilka årliga händelser enligt den judiska kalendern som ska visas i kalendern för årliga händelser | Core-literal match |
| 18084 | 856072677 | `component::jewish_calendar::options::step::init::data_description::learning_schedule` | Select which learning schedules should be displayed in the Learning Schedule calendar | Välj vilka studieplaner som ska visas i kalendern för studieplaner | Core-literal match |
| 18085 | 856072676 | `component::jewish_calendar::options::step::init::data_description::daily_events` | Select which daily Jewish calendar events should be displayed in the Daily Events calendar | Välj vilka händelser enligt den judiska kalendern som ska visas i kalendern för dagliga händelser | Core-literal match |
| 18086 | 856072675 | `component::jewish_calendar::options::step::init::data::yearly_events` | Yearly events to display | Årliga evenemang att visa | Core-literal match |
| 18087 | 856072674 | `component::jewish_calendar::options::step::init::data::learning_schedule` | Learning schedule to display | Visning av studieplan | Core-literal match |
| 18088 | 856072673 | `component::jewish_calendar::options::step::init::data::daily_events` | Daily events to display | Dagliga händelser att visa | Core-literal match |
| 18089 | 856072672 | `component::jewish_calendar::entity::calendar::yearly_events::name` | Yearly events | Årliga händelser | Core-literal match |
| 18090 | 856072671 | `component::jewish_calendar::entity::calendar::learning_schedule::name` | Learning schedule | Schema för inlärning | Core-literal match |
| 18091 | 856072670 | `component::jewish_calendar::entity::calendar::daily_events::name` | Daily events | Dagliga händelser | Core-literal match |
| 18092 | 856028744 | `component::miele::entity::sensor::program_id::state::pre_wash` | Pre-wash | Förtvätt | Core-literal match |
| 18093 | 856028743 | `component::miele::entity::sensor::program_id::state::pot_rests_and_filters` | Pot rests and filters | Kastrullunderlägg och filter | Core-literal match |
| 18094 | 855961920 | `component::compit::entity::switch::force_dhw::name` | Force domestic hot water | Tvinga varmvatten | Core-literal match |
| 18095 | 855961919 | `component::compit::entity::switch::device_on_off::name` | Device on/off | Enhet på/av | Core-literal match |
| 18096 | 855959776 | `component::command_line::exceptions::timeout_error::message` | Timeout trying to execute command: {command} | Timeout vid försök att utföra kommandot: {command} | Core-literal match |
| 18097 | 855959775 | `component::command_line::exceptions::command_error::message` | Error trying to execute command: {command}. Error: {error} | Fel vid försök att köra kommandot: {command}. Fel: {error} | Core-literal match |
| 18098 | 855905608 | `component::downloader::exceptions::invalid_value::message` | Invalid filename derived from {url} | Ogiltigt filnamn härrörande från {url} | Core-literal match |
| 18099 | 855905607 | `component::downloader::exceptions::connection_error::message` | Connection error occurred while downloading {url} | Anslutningsfel uppstod under nedladdningen av {url} | Core-literal match |
| 18100 | 855701615 | `component::anthropic::config_subentries::conversation::step::model::data_description::web_fetch_max_uses` | Limit the number of web fetches performed per response | Begränsa antalet webbhämtningar som utförs per svar | Core-literal match |
| 18101 | 855701614 | `component::anthropic::config_subentries::conversation::step::model::data_description::web_fetch` | The web fetch tool allows Claude to retrieve full content from specified web pages and PDF documents to augment Claude's context with live web content | Verktyget för webbhämtning låter Claude hämta hela innehållet från angivna webbsidor och PDF-dokument för att utöka Claudes kontext med aktuellt webbinnehåll. | Core-literal match |
| 18102 | 855701613 | `component::anthropic::config_subentries::conversation::step::model::data::web_fetch_max_uses` | Maximum web fetches | Maximalt antal webbhämtningar | Core-literal match |
| 18103 | 855701612 | `component::anthropic::config_subentries::conversation::step::model::data::web_fetch` | Enable web fetch | Aktivera webbhämtning | Core-literal match |
| 18104 | 855701611 | `component::anthropic::config_subentries::ai_task_data::step::model::data_description::web_fetch_max_uses` | Limit the number of web fetches performed per response | Begränsa antalet webbhämtningar som utförs per svar | Shared reference target checked |
| 18105 | 855701610 | `component::anthropic::config_subentries::ai_task_data::step::model::data_description::web_fetch` | The web fetch tool allows Claude to retrieve full content from specified web pages and PDF documents to augment Claude's context with live web content | Verktyget för webbhämtning låter Claude hämta hela innehållet från angivna webbsidor och PDF-dokument för att utöka Claudes kontext med aktuellt webbinnehåll. | Shared reference target checked |
| 18106 | 855701609 | `component::anthropic::config_subentries::ai_task_data::step::model::data::web_fetch_max_uses` | Maximum web fetches | Maximalt antal webbhämtningar | Shared reference target checked |
| 18107 | 855701608 | `component::anthropic::config_subentries::ai_task_data::step::model::data::web_fetch` | Enable web fetch | Aktivera webbhämtning | Shared reference target checked |
| 18108 | 855598252 | `component::cast::options::step::init::title` | Google Cast configuration | Google Cast-konfiguration | Shared reference target checked |
| 18109 | 855598251 | `component::cast::options::step::init::sections::more_options::name` | More options | Fler alternativ | Core-literal match |
| 18110 | 855598250 | `component::cast::options::step::init::sections::more_options::data_description::uuid` | A comma-separated list of UUIDs of Cast devices to add to Home Assistant. Use only if you don’t want to add all available cast devices. | En kommaseparerad lista med UUID:er för Cast-enheter som ska läggas till i Home Assistant. Använd endast om du inte vill lägga till alla tillgängliga Cast-enheter. | Core-literal match |
| 18111 | 855598249 | `component::cast::options::step::init::sections::more_options::data_description::ignore_cec` | A comma-separated list of Chromecasts that should ignore CEC data for determining the active input. This will be passed to pychromecast.IGNORE_CEC. | En kommaseparerad lista över Chromecasts som ska ignorera CEC-data för att bestämma den aktiva ingången. Detta kommer att skickas till pychromecast.IGNORE_CEC. | Core-literal match |
| 18112 | 855598248 | `component::cast::options::step::init::sections::more_options::data::uuid` | Allowed UUIDs | Tillåtna UUID:n | Core-literal match |
| 18113 | 855598247 | `component::cast::options::step::init::sections::more_options::data::ignore_cec` | Ignore CEC | Ignorera CEC | Core-literal match |
| 18114 | 855598246 | `component::cast::options::step::init::data_description::known_hosts` | Hostnames or IP addresses of cast devices, use if mDNS discovery is not working | Värdnamn eller IP-adresser för cast-enheter, använd om mDNS-upptäckt inte fungerar | Shared reference target checked |
| 18115 | 855598245 | `component::cast::options::step::init::data::known_hosts` | Add known host | Lägg till en känd värd | Shared reference target checked |
| 18116 | 855489392 | `component::tasmota::config::step::config::data_description::discovery_prefix` | Only change this if you use a custom Tasmota binary that does not use the default `tasmota/discovery` discovery topic prefix | Ändra detta endast om du använder en anpassad Tasmota-binär som inte använder standardprefixet för upptäcktsämne `tasmota/discovery` | Core-literal match |
| 18117 | 855466491 | `component::qbus::exceptions::invalid_option::message` | Option "{option}" is not valid. Valid options are: {options}. | Alternativet "{option}" är inte giltigt. Giltiga alternativ är: {options}. | Core-literal match |
| 18118 | 855452083 | `component::prusalink::entity::binary_sensor::sd_ready::name` | SD card | SD-kort | Core-literal match |
| 18119 | 855452082 | `component::prusalink::entity::binary_sensor::farm_mode::name` | Farm mode | Farmläge | Core-literal match |
| 18120 | 855448768 | `component::elkm1::issues::deprecated_sensor_scripts::title` | Deprecated sensor detected | Föråldrad sensor upptäckt | Source-path follow-up open |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 856458192 | `component::zwave_js::exceptions::credential_slot_out_of_range::message` | Credential slot for {credential_type} must be between 1 and {max_slot}. |
| 856273148 | `component::cert_expiry::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 856164112 | `component::rflink::issues::yaml_migration::title` | Your {platform} RFLink configuration needs to be migrated |
| 856164111 | `component::rflink::issues::yaml_migration::description` | Your current RFLink {platform} YAML configuration needs to be migrated to the new configuration format. |
| 856072691 | `component::jewish_calendar::selector::daily_events::options::tset_hakohavim_tsom` | T'set Hakochavim (nightfall) |
| 855448768 | `component::elkm1::issues::deprecated_sensor_scripts::title` | Deprecated sensor detected |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
