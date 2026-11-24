# Home Assistant Core – historisk avstämning 21841–21960

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 82 direkta källtexter matchar HA Core-källan; 19 referensanvändningar med 16 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 19 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 21841 | 827880645 | `component::smhi::entity::sensor::precipitation_category::state::snow` | Snow | Snö | Core-literal match |
| 21842 | 827880644 | `component::smhi::entity::sensor::precipitation_category::state::rain_snow_mixed` | Mixture of rain and snow | Snöblandat regn | Core-literal match |
| 21843 | 827880643 | `component::smhi::entity::sensor::precipitation_category::state::rain` | Rain | Regn | Core-literal match |
| 21844 | 827880642 | `component::smhi::entity::sensor::precipitation_category::state::no_precipitation` | No precipitation | Ingen nederbörd | Core-literal match |
| 21845 | 827880641 | `component::smhi::entity::sensor::precipitation_category::state::mixed_ice` | Mixed/ice | Blandad/is | Core-literal match |
| 21846 | 827880640 | `component::smhi::entity::sensor::precipitation_category::state::ice_pellets` | Ice pellets | Iskorn | Core-literal match |
| 21847 | 827880639 | `component::smhi::entity::sensor::precipitation_category::state::hail` | Hail | Hagel | Core-literal match |
| 21848 | 827880638 | `component::smhi::entity::sensor::precipitation_category::state::graupel` | Graupel | Snöhagel | Core-literal match |
| 21849 | 827880637 | `component::smhi::entity::sensor::precipitation_category::state::freezing_rain` | Freezing rain | Underkylt regn | Core-literal match |
| 21850 | 827880636 | `component::smhi::entity::sensor::precipitation_category::state::freezing_drizzle` | Freezing drizzle | Underkylt duggregn | Core-literal match |
| 21851 | 827880635 | `component::smhi::entity::sensor::precipitation_category::state::drizzle` | Drizzle | Duggregn | Core-literal match |
| 21852 | 827699053 | `component::actron_air::exceptions::setup_connection_error::message` | Failed to connect to the Actron Air API | Det gick inte att ansluta till Actron Air-API:et | Core-literal match |
| 21853 | 827565155 | `component::picotts::issues::deprecated_yaml::title` | The {integration_title} YAML configuration is being removed | YAML-konfigurationen för {integration_title} tas bort | Source-path follow-up open |
| 21854 | 827565154 | `component::picotts::issues::deprecated_yaml::description` | Configuring {integration_title} using YAML is being removed.<br><br>Your existing YAML configuration has been imported into the UI automatically.<br><br>The actions `tts.{domain}_*_say` will be removed and automations should be updated to use the `tts.speak` action with the new tts entities. Then remove the `{domain}` configuration from your configuration.yaml file and restart Home Assistant to fix this issue. | Konfigurationen av {integration_title} med hjälp av YAML kommer att tas bort.<br><br>Din befintliga YAML-konfiguration har importerats automatiskt till användargränssnittet.<br><br>Åtgärderna `tts.{domain}_*_say` kommer att tas bort och automatiseringarna bör uppdateras så att de använder åtgärden `tts.speak` med de nya tts-entiteterna. Ta sedan bort konfigurationen `{domain}` från din configuration.yaml-fil och starta om Home Assistant för att åtgärda detta problem. | Source-path follow-up open |
| 21855 | 827565153 | `component::picotts::exceptions::timeout_error::message` | Timeout running pico2wave | Timeout vid körning av pico2wave | Source-path follow-up open |
| 21856 | 827565152 | `component::picotts::exceptions::returncode_error::message` | Error running pico2wave, return code: {returncode} | Fel vid körning av pico2wave, returkod: {returncode} | Source-path follow-up open |
| 21857 | 827565151 | `component::picotts::exceptions::file_read_error::message` | Error trying to read {filename} | Fel vid läsning av {filename} | Source-path follow-up open |
| 21858 | 827565150 | `component::picotts::exceptions::binary_not_found::message` | pico2wave binary could not be found | pico2wave binärfil kunde inte hittas | Source-path follow-up open |
| 21859 | 827565149 | `component::picotts::config::step::user::data::language` | Language | Språk | Shared reference target checked |
| 21860 | 827565148 | `component::picotts::config::abort::binary_not_found` | pico2wave binary could not be found | pico2wave binärfil kunde inte hittas | Source-path follow-up open |
| 21861 | 827565147 | `component::picotts::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Shared reference target checked |
| 21862 | 827565146 | `component::picotts::common::binary_not_found` | pico2wave binary could not be found | pico2wave binärfil kunde inte hittas | Source-path follow-up open |
| 21863 | 827121830 | `component::nina::entity::sensor::start::name` | Start {slot_id} | Start {slot_id} | Core-literal match |
| 21864 | 827121829 | `component::nina::entity::sensor::severity::state::severe` | Severe | Allvarlig | Core-literal match |
| 21865 | 827121828 | `component::nina::entity::sensor::severity::state::moderate` | Moderate | Måttlig | Core-literal match |
| 21866 | 827121827 | `component::nina::entity::sensor::severity::state::minor` | Minor | Mindre | Core-literal match |
| 21867 | 827121826 | `component::nina::entity::sensor::severity::state::extreme` | Extreme | Extrem | Core-literal match |
| 21868 | 827121825 | `component::nina::entity::sensor::severity::name` | Severity {slot_id} | Allvarlighetsgrad {slot_id} | Core-literal match |
| 21869 | 827121824 | `component::nina::entity::sensor::sent::name` | Sent {slot_id} | Skickat {slot_id} | Core-literal match |
| 21870 | 827121823 | `component::nina::entity::sensor::sender::name` | Sender {slot_id} | Avsändare {slot_id} | Core-literal match |
| 21871 | 827121822 | `component::nina::entity::sensor::more_info_url::name` | More information URL {slot_id} | Mer informations-URL {slot_id} | Core-literal match |
| 21872 | 827121821 | `component::nina::entity::sensor::headline::name` | Headline {slot_id} | Rubrik {slot_id} | Core-literal match |
| 21873 | 827121820 | `component::nina::entity::sensor::expires::name` | Expires {slot_id} | Utgår {slot_id} | Core-literal match |
| 21874 | 827121819 | `component::nina::entity::sensor::affected_areas::name` | Affected areas {slot_id} | Berörda områden {slot_id} | Core-literal match |
| 21875 | 827119938 | `component::airos::exceptions::update_error::message` | Connection failed during firmware update | Anslutningen misslyckades under uppdatering av firmware | Core-literal match |
| 21876 | 827119937 | `component::airos::exceptions::update_connection_authentication_error::message` | Authentication or connection failed during firmware update | Autentisering eller anslutning misslyckades under uppdatering av firmware | Core-literal match |
| 21877 | 827118613 | `component::growatt_server::config::step::reconfigure::title` | Reconfigure Growatt | Konfigurera om Growatt | Core-literal match |
| 21878 | 827118612 | `component::growatt_server::config::step::reconfigure::description` | Update your credentials to continue using this integration. | Uppdatera dina inloggningsuppgifter för att fortsätta använda den här integrationen. | Core-literal match |
| 21879 | 827118611 | `component::growatt_server::config::step::reconfigure::data_description::username` | The email address or username for your Growatt account. | E-postadressen eller användarnamnet för ditt Growatt-konto. | Shared reference target checked |
| 21880 | 827118610 | `component::growatt_server::config::step::reconfigure::data_description::token` | The API token for your Growatt account. You can generate one via the Growatt web portal or ShinePhone app. | API-token för ditt Growatt-konto. Du kan generera en via Growatt-webbportalen eller ShinePhone-appen. | Shared reference target checked |
| 21881 | 827118609 | `component::growatt_server::config::step::reconfigure::data_description::region` | The server region that matches your Growatt account location. | Den serverregion som motsvarar platsen för ditt Growatt-konto. | Shared reference target checked |
| 21882 | 827118608 | `component::growatt_server::config::step::reconfigure::data_description::password` | The password for your Growatt account. | Lösenordet för ditt Growatt-konto. | Shared reference target checked |
| 21883 | 827118607 | `component::growatt_server::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference target checked |
| 21884 | 827118606 | `component::growatt_server::config::step::reconfigure::data::token` | API token | API-token | Shared reference target checked |
| 21885 | 827118605 | `component::growatt_server::config::step::reconfigure::data::region` | Server region | Serverregion | Shared reference target checked |
| 21886 | 827118604 | `component::growatt_server::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 21887 | 827118603 | `component::growatt_server::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 21888 | 827104639 | `component::opendisplay::entity::sensor::battery_voltage::name` | Battery voltage | Batterispänning | Core-literal match |
| 21889 | 827073155 | `component::forecast_solar::options::error::api_key_required` | An API key is required to add more than one plane. You can configure it in the integration options. | En API-nyckel krävs för att lägga till mer än ett plan. Du kan konfigurera den i integrationsalternativen. | Core-literal match |
| 21890 | 827073154 | `component::forecast_solar::exceptions::no_plane::message` | No plane configured, cannot set up Forecast.Solar | Inget plan konfigurerat, kan därför inte konfigurera Forecast.Solar | Core-literal match |
| 21891 | 827073153 | `component::forecast_solar::exceptions::api_key_required::message` | An API key is required when more than one plane is configured | En API-nyckel krävs när mer än ett plan är konfigurerat | Core-literal match |
| 21892 | 827073152 | `component::forecast_solar::config_subentries::plane::step::user::description` | Choose where the new plane's angles come from. Multiple planes are supported with a Forecast.Solar API subscription. | Lägg till ett solplan. Flera plan stöds med en Forecast.Solar API-prenumeration. | Core-literal match |
| 21893 | 827073151 | `component::forecast_solar::config_subentries::plane::step::user::data::modules_power` | Total Watt peak power of your solar modules | Total maxeffekt (Watt) på dina solpaneler | Source-path follow-up open |
| 21894 | 827073150 | `component::forecast_solar::config_subentries::plane::step::user::data::declination` | Declination (0 = Horizontal, 90 = Vertical) | Deklination (0° = horisontell, 90° = vertikal) | Source-path follow-up open |
| 21895 | 827073149 | `component::forecast_solar::config_subentries::plane::step::user::data::azimuth` | Azimuth (360 degrees, 0 = North, 90 = East, 180 = South, 270 = West) | Azimut (360 grader, 0° = norr, 90° = öster, 180° = söder, 270° = väster) | Source-path follow-up open |
| 21896 | 827073148 | `component::forecast_solar::config_subentries::plane::step::reconfigure::description` | Choose where this plane's angles come from. | Redigera solplanets konfiguration. | Core-literal match |
| 21897 | 827073147 | `component::forecast_solar::config_subentries::plane::step::reconfigure::data::modules_power` | Total Watt peak power of your solar modules | Total maxeffekt (Watt) på dina solpaneler | Source-path follow-up open |
| 21898 | 827073146 | `component::forecast_solar::config_subentries::plane::step::reconfigure::data::declination` | Declination (0 = Horizontal, 90 = Vertical) | Deklination (0° = horisontell, 90° = vertikal) | Source-path follow-up open |
| 21899 | 827073145 | `component::forecast_solar::config_subentries::plane::step::reconfigure::data::azimuth` | Azimuth (360 degrees, 0 = North, 90 = East, 180 = South, 270 = West) | Azimut (360 grader, 0° = norr, 90° = öster, 180° = söder, 270° = väster) | Source-path follow-up open |
| 21900 | 827073144 | `component::forecast_solar::config_subentries::plane::initiate_flow::user` | Add plane | Lägg till plan | Core-literal match |
| 21901 | 827073143 | `component::forecast_solar::config_subentries::plane::entry_type` | Plane | Plan | Core-literal match |
| 21902 | 827073142 | `component::forecast_solar::config_subentries::plane::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 21903 | 827073141 | `component::forecast_solar::config_subentries::plane::abort::max_planes` | You can add a maximum of 4 planes. | Du kan lägga till maximalt 4 plan. | Core-literal match |
| 21904 | 827073140 | `component::forecast_solar::config_subentries::plane::abort::api_key_required` | An API key is required to add more than one plane. You can configure it in the integration options. | En API-nyckel krävs för att lägga till mer än ett plan. Du kan konfigurera den i integrationsalternativen. | Core-literal match |
| 21905 | 826872635 | `component::apple_tv::services::set_keyboard_text::name` | Set keyboard text | Ställ in tangentbordstext | Core-literal match |
| 21906 | 826872634 | `component::apple_tv::services::set_keyboard_text::fields::text::name` | Text | Text | Core-literal match |
| 21907 | 826872633 | `component::apple_tv::services::set_keyboard_text::fields::text::description` | The text to set. | Den text som ska ställas in. | Core-literal match |
| 21908 | 826872632 | `component::apple_tv::services::set_keyboard_text::fields::config_entry_id::name` | Apple TV | Apple TV | Core-literal match |
| 21909 | 826872631 | `component::apple_tv::services::set_keyboard_text::fields::config_entry_id::description` | The Apple TV to send text to. | Den Apple TV som du vill skicka text till. | Core-literal match |
| 21910 | 826872630 | `component::apple_tv::services::set_keyboard_text::description` | Sets the text in the currently focused text input field on an Apple TV. | Ställer in texten i det just nu fokuserade textinmatningsfältet på en Apple TV. | Core-literal match |
| 21911 | 826872629 | `component::apple_tv::services::clear_keyboard_text::name` | Clear keyboard text | Rensa tangentbordstext | Core-literal match |
| 21912 | 826872628 | `component::apple_tv::services::clear_keyboard_text::fields::config_entry_id::name` | Apple TV | Apple TV | Shared reference target checked |
| 21913 | 826872627 | `component::apple_tv::services::clear_keyboard_text::fields::config_entry_id::description` | The Apple TV to send text to. | Den Apple TV som du vill skicka text till. | Shared reference target checked |
| 21914 | 826872626 | `component::apple_tv::services::clear_keyboard_text::description` | Clears the text in the currently focused text input field on an Apple TV. | Rensar texten i det just nu fokuserade textinmatningsfältet på en Apple TV. | Core-literal match |
| 21915 | 826872625 | `component::apple_tv::services::append_keyboard_text::name` | Append keyboard text | Lägg till tangentbordstext | Core-literal match |
| 21916 | 826872624 | `component::apple_tv::services::append_keyboard_text::fields::text::name` | Text | Text | Shared reference target checked |
| 21917 | 826872623 | `component::apple_tv::services::append_keyboard_text::fields::text::description` | The text to append. | Texten som ska läggas till. | Core-literal match |
| 21918 | 826872622 | `component::apple_tv::services::append_keyboard_text::fields::config_entry_id::name` | Apple TV | Apple TV | Shared reference target checked |
| 21919 | 826872621 | `component::apple_tv::services::append_keyboard_text::fields::config_entry_id::description` | The Apple TV to send text to. | Den Apple TV som du vill skicka text till. | Shared reference target checked |
| 21920 | 826872620 | `component::apple_tv::services::append_keyboard_text::description` | Appends text to the currently focused text input field on an Apple TV. | Lägger till text i det textinmatningsfält som just nu är fokuserat på en Apple TV. | Core-literal match |
| 21921 | 826872619 | `component::apple_tv::exceptions::not_connected::message` | Apple TV is not connected | Apple TV är inte ansluten | Core-literal match |
| 21922 | 826872618 | `component::apple_tv::exceptions::keyboard_not_focused::message` | No text input field is currently focused on the Apple TV | Just nu är inget textinmatningsfält fokuserat på Apple TV:n | Core-literal match |
| 21923 | 826872617 | `component::apple_tv::exceptions::keyboard_not_available::message` | Keyboard input is not supported by this device | Tangentbordsinmatning stöds inte av den här enheten | Core-literal match |
| 21924 | 826872616 | `component::apple_tv::exceptions::keyboard_error::message` | An error occurred while sending text to the Apple TV | Ett fel uppstod när texten skulle skickas till Apple TV:n | Core-literal match |
| 21925 | 826871324 | `component::evohome::exceptions::mode_not_supported::message` | The mode `{mode}` is not supported by this controller | Läget `{mode}` stöds inte av den här kontrollern | Core-literal match |
| 21926 | 826871323 | `component::evohome::exceptions::mode_cant_have_period::message` | The mode `{mode}` does not support 'Period'; use 'Duration' instead | Läget `{mode}` stöder inte 'Period'. Använd 'Duration' istället | Core-literal match |
| 21927 | 826871322 | `component::evohome::exceptions::mode_cant_have_duration::message` | The mode `{mode}` does not support 'Duration'; use 'Period' instead | Läget `{mode}` stöder inte 'Duration'. Använd 'Period' istället | Core-literal match |
| 21928 | 826871321 | `component::evohome::exceptions::mode_cant_be_temporary::message` | The mode `{mode}` does not support 'Duration' or 'Period' | Läget `{mode}` stöder inte 'Duration' eller 'Period' | Core-literal match |
| 21929 | 826871320 | `component::evohome::exceptions::invalid_system_mode::message` | The requested system mode is not supported: {error} | Det begärda systemläget stöds inte: {error} | Source-path follow-up open |
| 21930 | 826465725 | `component::shell_command::services::reload::name` | Reload | Ladda om | Shared reference target checked |
| 21931 | 826465724 | `component::shell_command::services::reload::description` | Reloads shell command configuration. | Laddar om konfigurationen för shell-kommando. | Core-literal match |
| 21932 | 826465723 | `component::shell_command::issues::reserved_reload_name::title` | Reserved shell command action name | Reserverat namn på shell-kommando | Core-literal match |
| 21933 | 826465722 | `component::shell_command::issues::reserved_reload_name::description` | The shell command name {name} is a reserved for the reload action and cannot be used for user-defined commands. Please rename or remove this entry from your configuration. | Shell-kommandot {name} är reserverat för en ladda om-åtgärd och kan inte användas för användardefinierade kommandon. Byt namn eller ta bort denna post från din konfiguration. | Core-literal match |
| 21934 | 826465721 | `component::freshr::config::step::reconfigure::description` | Update the password for your Fresh-r account `{username}`. | Uppdatera lösenordet för ditt Fresh-r-konto `{username}`. | Core-literal match |
| 21935 | 826465720 | `component::freshr::config::step::reconfigure::data_description::password` | Your Fresh-r account password. | Lösenordet till ditt Fresh-r-konto. | Shared reference target checked |
| 21936 | 826465719 | `component::freshr::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 21937 | 826404719 | `component::bmw_connected_drive::issues::integration_removed::title` | The BMW Connected Drive integration has been removed | BMW Connected Drive-integrationen har tagits bort | Core-literal match |
| 21938 | 826404718 | `component::bmw_connected_drive::issues::integration_removed::description` | The BMW Connected Drive integration has been removed from Home Assistant.<br><br>In September 2025, BMW blocked third-party access to their servers by adding additional security measures. For EU-registered cars, a community-developed [custom component]({custom_component_url}) using BMW's CarData API is available as an alternative.<br><br>To resolve this issue, please remove the (now defunct) integration entries from your Home Assistant setup. [View your existing BMW Connected Drive integration entries]({entries}). | Integrationen BMW Connected Drive har tagits bort från Home Assistant.<br><br>I september 2025 blockerade BMW tredjepartsåtkomst till sina servrar genom ytterligare säkerhetsåtgärder. För EU-registrerade bilar finns en [anpassad komponent] utvecklad av communityn({custom_component_url}) som använder BMW:s CarData API som alternativ.<br><br>För att lösa problemet tar du bort de numera obrukbara integrationsposterna från din Home Assistant-konfiguration. [Visa dina befintliga BMW Connected Drive-integrationsposter]({entries}). | Core-literal match |
| 21939 | 826397234 | `component::html5::services::dismiss_message::name` | Dismiss message | Stäng avisering | Core-literal match |
| 21940 | 826397233 | `component::html5::services::dismiss_message::fields::tag::name` | Tag | Tagg | Shared reference target checked |
| 21941 | 826397232 | `component::html5::services::dismiss_message::fields::tag::description` | The tag of the notifications to dismiss. If not specified, all notifications will be dismissed. | Taggen för de aviseringar som ska stängas. Om ingen tag anges kommer alla aviseringar att stängas. | Core-literal match |
| 21942 | 826397231 | `component::html5::services::dismiss_message::description` | Dismisses one or more HTML5 notifications. | Stänger en eller flera HTML5-aviseringar. | Core-literal match |
| 21943 | 826397230 | `component::html5::issues::deprecated_dismiss_action::title` | Detected use of deprecated action {action} | Användning av utfasad åtgärd har upptäckts: {action} | Source-path follow-up open |
| 21944 | 826397229 | `component::html5::issues::deprecated_dismiss_action::description` | The action `{action}` is deprecated and will be removed in a future release.<br><br>Please update your automations and scripts to use the notify entities with the `{new_action}` action instead. | Åtgärden `{action}` är utfasad och kommer att tas bort i en kommande version.<br><br>Uppdatera dina automatiseringar och skript så att du istället använder åtgärden `{new_action}` för dina aviseringar. | Source-path follow-up open |
| 21945 | 826345496 | `component::valve::common::condition_behavior_name` | Condition passes if | Villkoret uppfylls om | Core-literal match |
| 21946 | 825626675 | `component::html5::services::send_message::name` | Send message | Skicka meddelande | Core-literal match |
| 21947 | 825626674 | `component::html5::services::send_message::fields::vibrate::name` | Vibration pattern | Vibrationsmönster | Core-literal match |
| 21948 | 825626673 | `component::html5::services::send_message::fields::vibrate::description` | A vibration pattern to run with the notification. An array of integers representing alternating periods of vibration and silence in milliseconds. For example, [200, 100, 200] would vibrate for 200ms, pause for 100ms, then vibrate for another 200ms. | Ett vibrationsmönster som ska användas tillsammans med aviseringen. En array med heltal som anger alternerande perioder av vibration och tystnad i millisekunder. Till exempel skulle [200, 100, 200] innebära att enheten vibrerar i 200 ms, pausar i 100 ms och sedan vibrerar i ytterligare 200 ms. | Core-literal match |
| 21949 | 825626672 | `component::html5::services::send_message::fields::urgency::name` | Urgency | Brådskande | Core-literal match |
| 21950 | 825626671 | `component::html5::services::send_message::fields::urgency::description` | Whether the push service should try to deliver the notification immediately or defer it in accordance with the user's power saving preferences. | Anger om push-tjänsten ska försöka leverera aviseringen omedelbart eller skjuta upp den i enlighet med användarens inställningar för energisparläge. | Core-literal match |
| 21951 | 825626670 | `component::html5::services::send_message::fields::ttl::name` | Time to live | Tid att leva (TTL) | Core-literal match |
| 21952 | 825626669 | `component::html5::services::send_message::fields::ttl::description` | Specifies how long the push service should retain the message if the user's browser or device is offline. After this period, the notification expires. A value of 0 means the notification is discarded immediately if the target is not connected. Defaults to 1 day. | Anger hur länge push-tjänsten ska behålla aviseringen om användarens webbläsare eller enhet är offline. Efter denna period upphör aviseringen att gälla. Värdet 0 innebär att meddelandet ignoreras omedelbart om målet inte är anslutet. Standardvärdet är en (1) dag. | Core-literal match |
| 21953 | 825626668 | `component::html5::services::send_message::fields::title::name` | Title | Rubrik | Core-literal match |
| 21954 | 825626667 | `component::html5::services::send_message::fields::title::description` | Title for your notification message. | Rubrik för din avisering. | Core-literal match |
| 21955 | 825626666 | `component::html5::services::send_message::fields::timestamp::name` | Timestamp | Tidsstämpel | Core-literal match |
| 21956 | 825626665 | `component::html5::services::send_message::fields::timestamp::description` | The timestamp of the notification. By default, it uses the time when the notification is sent. | Tidsstämpeln för aviseringen. Som standard används tiden då aviseringen skickades. | Core-literal match |
| 21957 | 825626664 | `component::html5::services::send_message::fields::tag::name` | Tag | Tagg | Core-literal match |
| 21958 | 825626663 | `component::html5::services::send_message::fields::tag::description` | The identifier of the notification. Sending a new notification with the same tag will replace the existing one. If not specified, a unique tag will be generated for each notification. | Aviseringens identifierare. Om du skickar en ny avisering med samma tagg ersätts den befintliga. Om inget annat anges genereras en unik tagg för varje avisering. | Core-literal match |
| 21959 | 825626662 | `component::html5::services::send_message::fields::silent::name` | Silent | Tyst | Core-literal match |
| 21960 | 825626661 | `component::html5::services::send_message::fields::silent::description` | If enabled, the notification will not play sounds or trigger vibration, regardless of the device's notification settings. | Om aktiverat kommer aviseringen inte att avge ljud eller utlösa vibration, oavsett enhetens inställningar för aviseringar. | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 827565155 | `component::picotts::issues::deprecated_yaml::title` | The {integration_title} YAML configuration is being removed |
| 827565154 | `component::picotts::issues::deprecated_yaml::description` | Configuring {integration_title} using YAML is being removed.

Your existing YAML configuration has been imported into the UI automatically.

The actions `tts.{domain}_*_say` will be removed and automations should be updated to use the `tts.speak` action with the new tts entities. Then remove the `{domain}` configuration from your configuration.yaml file and restart Home Assistant to fix this issue. |
| 827565153 | `component::picotts::exceptions::timeout_error::message` | Timeout running pico2wave |
| 827565152 | `component::picotts::exceptions::returncode_error::message` | Error running pico2wave, return code: {returncode} |
| 827565151 | `component::picotts::exceptions::file_read_error::message` | Error trying to read {filename} |
| 827565150 | `component::picotts::exceptions::binary_not_found::message` | pico2wave binary could not be found |
| 827565148 | `component::picotts::config::abort::binary_not_found` | pico2wave binary could not be found |
| 827565146 | `component::picotts::common::binary_not_found` | pico2wave binary could not be found |
| 827118603 | `component::growatt_server::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 827073151 | `component::forecast_solar::config_subentries::plane::step::user::data::modules_power` | Total Watt peak power of your solar modules |
| 827073150 | `component::forecast_solar::config_subentries::plane::step::user::data::declination` | Declination (0 = Horizontal, 90 = Vertical) |
| 827073149 | `component::forecast_solar::config_subentries::plane::step::user::data::azimuth` | Azimuth (360 degrees, 0 = North, 90 = East, 180 = South, 270 = West) |
| 827073147 | `component::forecast_solar::config_subentries::plane::step::reconfigure::data::modules_power` | Total Watt peak power of your solar modules |
| 827073146 | `component::forecast_solar::config_subentries::plane::step::reconfigure::data::declination` | Declination (0 = Horizontal, 90 = Vertical) |
| 827073145 | `component::forecast_solar::config_subentries::plane::step::reconfigure::data::azimuth` | Azimuth (360 degrees, 0 = North, 90 = East, 180 = South, 270 = West) |
| 827073142 | `component::forecast_solar::config_subentries::plane::abort::reconfigure_successful` | Reconfiguration was successful |
| 826871320 | `component::evohome::exceptions::invalid_system_mode::message` | The requested system mode is not supported: {error} |
| 826397230 | `component::html5::issues::deprecated_dismiss_action::title` | Detected use of deprecated action {action} |
| 826397229 | `component::html5::issues::deprecated_dismiss_action::description` | The action `{action}` is deprecated and will be removed in a future release.

Please update your automations and scripts to use the notify entities with the `{new_action}` action instead. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
