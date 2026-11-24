# Home Assistant Core – historisk avstämning 22081–22200

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 71 direkta källtexter matchar HA Core-källan; 13 referensanvändningar med 9 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 36 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 22081 | 824805047 | `component::gentex_homelink::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22082 | 824805046 | `component::google_tasks::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22083 | 824797208 | `component::anthropic::exceptions::wrong_file_type::message` | The {model} model does not support {mime_type} file types (for `{file_path}`). | Modellen {model} stöder inte filtyperna {mime_type} (för `{file_path}`). | Core-literal match |
| 22084 | 824797207 | `component::anthropic::exceptions::wrong_file_path::message` | `{file_path}` does not exist. | `{file_path}` finns inte. | Core-literal match |
| 22085 | 824797206 | `component::anthropic::exceptions::user_message_not_found::message` | Last message must be a user message to add attachments. | Det sista meddelandet måste vara ett användarmeddelande för att bilagor ska kunna läggas till. | Core-literal match |
| 22086 | 824797205 | `component::anthropic::exceptions::unknown_issue_id::message` | Unknown issue ID. | Okänt problem-ID. | Core-literal match |
| 22087 | 824797204 | `component::anthropic::exceptions::unexpected_stream_object::message` | Expected a stream of messages. | En ström av meddelanden förväntades. | Core-literal match |
| 22088 | 824797203 | `component::anthropic::exceptions::unexpected_chat_log_content::message` | Unexpected content type in chat log: {type}. | Oväntad innehållstyp i chattloggen: {type}. | Core-literal match |
| 22089 | 824797202 | `component::anthropic::exceptions::system_message_not_found::message` | First message must be a system message. | Det första meddelandet måste vara ett systemmeddelande. | Core-literal match |
| 22090 | 824797201 | `component::anthropic::exceptions::subentry_not_found::message` | Subentry not found. | Underposten hittades inte. | Core-literal match |
| 22091 | 824797200 | `component::anthropic::exceptions::response_not_found::message` | Last content in chat log is not an AssistantContent. | Det senaste innehållet i chattloggen är inte ett AssistantContent. | Core-literal match |
| 22092 | 824797199 | `component::anthropic::exceptions::json_parse_error::message` | Error with Claude structured response. | Fel med Claudes strukturerade svar. | Core-literal match |
| 22093 | 824797198 | `component::anthropic::exceptions::api_refusal::message` | Potential policy violation detected. | Potentiell policyöverträdelse upptäckt. | Core-literal match |
| 22094 | 824797197 | `component::anthropic::exceptions::api_error::message` | Anthropic API error: {message}. | Anthropic API-fel: {message}. | Core-literal match |
| 22095 | 824797196 | `component::anthropic::exceptions::api_authentication_error::message` | Authentication error with Anthropic API: {message}. Reauthentication required. | Autentiseringsfel i Anthropics API: {message}. Återautentisering krävs. | Core-literal match |
| 22096 | 824756555 | `component::smlight::exceptions::send_ir_code_failed::message` | Failed to send IR code: {error}. | Det gick inte att skicka IR-koden: {error}. | Core-literal match |
| 22097 | 824756554 | `component::smlight::entity::remote::remote::name` | IR Remote | IR-fjärrkontroll | Source-path follow-up open |
| 22098 | 824722059 | `component::matter::entity::climate::thermostat::state_attributes::preset_mode::state::wake` | Wake | Vakna | Core-literal match |
| 22099 | 824722058 | `component::matter::entity::climate::thermostat::state_attributes::preset_mode::state::vacation` | Vacation | Semester | Core-literal match |
| 22100 | 824722057 | `component::matter::entity::climate::thermostat::state_attributes::preset_mode::state::going_to_sleep` | Going to sleep | Ska sova | Core-literal match |
| 22101 | 824722006 | `component::renault::services::charge_start::name` | Start charging | Börja ladda | Core-literal match |
| 22102 | 824722005 | `component::renault::services::charge_start::fields::when::name` | When | När | Core-literal match |
| 22103 | 824722004 | `component::renault::services::charge_start::fields::when::description` | Timestamp for charging to start (optional - defaults to now). | Tidsstämpel för när laddningen ska starta (valfritt – standardinställningen är ”nu”). | Core-literal match |
| 22104 | 824722003 | `component::renault::services::charge_start::fields::vehicle::name` | Vehicle | Fordon | Core-literal match |
| 22105 | 824722002 | `component::renault::services::charge_start::fields::vehicle::description` | The vehicle to send the command to. | Fordonet som kommandot ska skickas till. | Shared reference target checked |
| 22106 | 824722001 | `component::renault::services::charge_start::description` | Starts charging on vehicle. | Påbörjar laddning av fordon. | Core-literal match |
| 22107 | 824543597 | `component::google::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22108 | 824513269 | `component::nina::entity::binary_sensor::warning::name` | Warning {slot_id} | Varning {slot_id} | Core-literal match |
| 22109 | 824463952 | `component::miele::entity::sensor::program_id::state::table_linen` | Table linen | Bordslinne | Core-literal match |
| 22110 | 824420087 | `component::timer::selector::condition_behavior::options::any` | Any | Något | Source-path follow-up open |
| 22111 | 824420086 | `component::timer::selector::condition_behavior::options::all` | All | Alla | Source-path follow-up open |
| 22112 | 824420085 | `component::timer::conditions::is_paused::name` | Timer is paused | Timer är pausad | Core-literal match |
| 22113 | 824420084 | `component::timer::conditions::is_paused::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 22114 | 824420083 | `component::timer::conditions::is_paused::fields::behavior::description` | How the state should match on the targeted timers. | Hur tillståndet ska matcha valda timers. | Source-path follow-up open |
| 22115 | 824420082 | `component::timer::conditions::is_paused::description` | Tests if one or more timers are paused. | Testar om en eller flera timers är pausade. | Core-literal match |
| 22116 | 824420081 | `component::timer::conditions::is_idle::name` | Timer is idle | Timer är inaktiv | Core-literal match |
| 22117 | 824420080 | `component::timer::conditions::is_idle::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 22118 | 824420079 | `component::timer::conditions::is_idle::fields::behavior::description` | How the state should match on the targeted timers. | Hur tillståndet ska matcha valda timers. | Source-path follow-up open |
| 22119 | 824420078 | `component::timer::conditions::is_idle::description` | Tests if one or more timers are idle. | Testar om en eller flera timers är inaktiva. | Core-literal match |
| 22120 | 824420077 | `component::timer::conditions::is_active::name` | Timer is active | Timer är aktiv | Core-literal match |
| 22121 | 824420076 | `component::timer::conditions::is_active::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 22122 | 824420075 | `component::timer::conditions::is_active::fields::behavior::description` | How the state should match on the targeted timers. | Hur tillståndet ska matcha valda timers. | Source-path follow-up open |
| 22123 | 824420074 | `component::timer::conditions::is_active::description` | Tests if one or more timers are active. | Testar om en eller flera timers är aktiva. | Core-literal match |
| 22124 | 824420073 | `component::timer::common::condition_behavior_name` | Condition passes if | Villkoret uppfylls om | Core-literal match |
| 22125 | 824420072 | `component::timer::common::condition_behavior_description` | How the state should match on the targeted timers. | Hur tillståndet ska matcha valda timers. | Source-path follow-up open |
| 22126 | 824386081 | `component::miele::entity::sensor::program_id::state::booster` | Booster | Booster | Core-literal match |
| 22127 | 824386080 | `component::miele::entity::sensor::program_id::state::airfry` | AirFry | AirFry | Core-literal match |
| 22128 | 824316294 | `component::calendar::selector::condition_behavior::options::any` | Any | Något | Source-path follow-up open |
| 22129 | 824316293 | `component::calendar::selector::condition_behavior::options::all` | All | Alla | Source-path follow-up open |
| 22130 | 824316292 | `component::calendar::conditions::is_event_active::name` | Calendar event is active | Kalenderhändelse är aktiv | Core-literal match |
| 22131 | 824316291 | `component::calendar::conditions::is_event_active::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 22132 | 824316290 | `component::calendar::conditions::is_event_active::fields::behavior::description` | How the state should match on the targeted calendars. | Hur tillståndet ska matcha valda kalendrar. | Source-path follow-up open |
| 22133 | 824316289 | `component::calendar::conditions::is_event_active::description` | Tests if one or more calendars have an active event. | Testar om en eller flera kalendrar har en aktiv händelse. | Core-literal match |
| 22134 | 824316288 | `component::calendar::common::condition_behavior_name` | Condition passes if | Villkoret uppfylls om | Core-literal match |
| 22135 | 824316287 | `component::calendar::common::condition_behavior_description` | How the state should match on the targeted calendars. | Hur tillståndet ska matcha valda kalendrar. | Source-path follow-up open |
| 22136 | 824015719 | `component::smappee::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22137 | 823983137 | `component::select::selector::condition_behavior::options::any` | Any | Något | Source-path follow-up open |
| 22138 | 823983136 | `component::select::selector::condition_behavior::options::all` | All | Alla | Source-path follow-up open |
| 22139 | 823983135 | `component::select::conditions::is_option_selected::name` | Dropdown option is selected | Ett alternativ i rullgardinsmenyn valdes | Core-literal match |
| 22140 | 823983134 | `component::select::conditions::is_option_selected::fields::option::name` | Option | Alternativ | Core-literal match |
| 22141 | 823983133 | `component::select::conditions::is_option_selected::fields::option::description` | The options to check for. | Alternativen att kontrollera. | Core-literal match |
| 22142 | 823983132 | `component::select::conditions::is_option_selected::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Core-literal match |
| 22143 | 823983131 | `component::select::conditions::is_option_selected::fields::behavior::description` | Whether the condition should pass when any or all targeted entities match. | Om villkoret ska uppfyllas när någon eller alla valda entiteter uppfyller kriterierna. | Source-path follow-up open |
| 22144 | 823983130 | `component::select::conditions::is_option_selected::description` | Tests if one or more dropdowns have a specific option selected. | Testar om en eller flera rullgardinsmenyer har ett specifikt alternativ valt. | Core-literal match |
| 22145 | 823976284 | `component::valve::selector::condition_behavior::options::any` | Any | Något | Source-path follow-up open |
| 22146 | 823976283 | `component::valve::selector::condition_behavior::options::all` | All | Alla | Source-path follow-up open |
| 22147 | 823976282 | `component::valve::conditions::is_open::name` | Valve is open | Ventil är öppen | Core-literal match |
| 22148 | 823976281 | `component::valve::conditions::is_open::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 22149 | 823976280 | `component::valve::conditions::is_open::fields::behavior::description` | Whether the condition should pass when any or all targeted entities match. | Om villkoret ska uppfyllas när någon eller alla valda entiteter uppfyller kriterierna. | Source-path follow-up open |
| 22150 | 823976279 | `component::valve::conditions::is_open::description` | Tests if one or more valves are open. | Testar om en eller flera ventiler är öppna. | Core-literal match |
| 22151 | 823976278 | `component::valve::conditions::is_closed::name` | Valve is closed | Ventil är stängd | Core-literal match |
| 22152 | 823976277 | `component::valve::conditions::is_closed::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 22153 | 823976276 | `component::valve::conditions::is_closed::fields::behavior::description` | Whether the condition should pass when any or all targeted entities match. | Om villkoret ska uppfyllas när någon eller alla valda entiteter uppfyller kriterierna. | Source-path follow-up open |
| 22154 | 823976275 | `component::valve::conditions::is_closed::description` | Tests if one or more valves are closed. | Testar om en eller flera ventiler är stängda. | Core-literal match |
| 22155 | 823816812 | `component::mcp::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22156 | 823816811 | `component::google_photos::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22157 | 823816789 | `component::fitbit::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22158 | 823751829 | `component::aladdin_connect::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22159 | 823722805 | `component::tplink_lte::issues::integration_removed::title` | The TP-Link LTE integration has been removed | TP-Link LTE-integrationen har tagits bort | Core-literal match |
| 22160 | 823722804 | `component::tplink_lte::issues::integration_removed::description` | The TP-Link LTE integration has been removed from Home Assistant.<br><br>The integration has not been working since Home Assistant 2023.6.0, has no maintainer, and its underlying library depends on a package with a [critical security vulnerability]({ghsa_url}).<br><br>To resolve this issue, remove the `tplink_lte` configuration from your `configuration.yaml` file and restart Home Assistant. | TP-Link LTE-integrationen har tagits bort från Home Assistant.<br><br>Integrationen har inte fungerat sedan Home Assistant 2023.6.0, har ingen underhållare och dess underliggande bibliotek är beroende av ett paket med en [kritisk säkerhetsbrist]({ghsa_url}).<br><br>För att lösa problemet tar du bort `tplink_lte`-konfigurationen från din `configuration.yaml`-fil och starta om Home Assistant. | Core-literal match |
| 22161 | 823722783 | `component::matter::entity::sensor::radon_concentration::name` | Radon concentration | Radonkoncentration | Core-literal match |
| 22162 | 823708784 | `component::light::conditions::is_brightness::name` | Light brightness | Ljusstyrka | Core-literal match |
| 22163 | 823708783 | `component::light::conditions::is_brightness::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22164 | 823708782 | `component::light::conditions::is_brightness::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22165 | 823708781 | `component::light::conditions::is_brightness::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 22166 | 823708780 | `component::light::conditions::is_brightness::fields::behavior::description` | How the state should match on the targeted lights. | Hur tillståndet ska matcha valda lampor. | Source-path follow-up open |
| 22167 | 823708779 | `component::light::conditions::is_brightness::description` | Tests the brightness of one or more lights. | Testar ljusstyrkan hos en eller flera lampor. | Core-literal match |
| 22168 | 823708778 | `component::light::common::condition_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22169 | 823708777 | `component::light::common::condition_threshold_description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22170 | 823696351 | `component::proxmoxve::exceptions::no_permission_snapshot::message` | The configured Proxmox VE user does not have permission to create snapshots of VMs and containers. Please grant the user the 'VM.Snapshot' permission and try again. | Den konfigurerade Proxmox VE-användaren har inte behörighet att skapa ögonblicksbilder av virtuella maskiner och containrar. Ge användaren behörigheten ”VM.Snapshot” och försök igen. | Source-path follow-up open |
| 22171 | 823693805 | `component::humidifier::conditions::is_mode::name` | Humidifier is in mode | Luftfuktaren är i läge | Core-literal match |
| 22172 | 823693804 | `component::humidifier::conditions::is_mode::fields::mode::name` | Mode | Läge | Core-literal match |
| 22173 | 823693803 | `component::humidifier::conditions::is_mode::fields::mode::description` | The operation modes to check for. | De driftlägen som ska kontrolleras. | Core-literal match |
| 22174 | 823693802 | `component::humidifier::conditions::is_mode::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 22175 | 823693801 | `component::humidifier::conditions::is_mode::fields::behavior::description` | How the state should match on the targeted humidifiers. | Hur tillståndet ska matcha valda luftfuktare. | Source-path follow-up open |
| 22176 | 823693800 | `component::humidifier::conditions::is_mode::description` | Tests if one or more humidifiers are set to a specific mode. | Testar om en eller flera luftfuktare är inställda på ett specifikt läge. | Core-literal match |
| 22177 | 823645063 | `component::climate::conditions::is_hvac_mode::name` | Thermostat HVAC mode | Termostat HVAC-läge | Core-literal match |
| 22178 | 823645062 | `component::climate::conditions::is_hvac_mode::fields::hvac_mode::name` | Modes | Lägen | Core-literal match |
| 22179 | 823645061 | `component::climate::conditions::is_hvac_mode::fields::hvac_mode::description` | The HVAC modes to test for. | De HVAC-lägen som ska testas. | Core-literal match |
| 22180 | 823645060 | `component::climate::conditions::is_hvac_mode::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 22181 | 823645059 | `component::climate::conditions::is_hvac_mode::fields::behavior::description` | How the state should match on the targeted climate-control devices. | Hur tillståndet ska matcha valda klimatkontrollenheter. | Source-path follow-up open |
| 22182 | 823645058 | `component::climate::conditions::is_hvac_mode::description` | Tests if one or more thermostats are set to a specific HVAC mode. | Testar om en eller flera termostater är inställda på ett specifikt HVAC-läge. | Core-literal match |
| 22183 | 823599080 | `component::telegram_bot::selector::media::fields::verify_ssl` | Verify SSL | Verifiera SSL | Core-literal match |
| 22184 | 823599079 | `component::telegram_bot::selector::media::fields::username` | Username | Användarnamn | Core-literal match |
| 22185 | 823599078 | `component::telegram_bot::selector::media::fields::url` | URL | URL | Core-literal match |
| 22186 | 823599077 | `component::telegram_bot::selector::media::fields::password` | Password | Lösenord | Core-literal match |
| 22187 | 823599076 | `component::telegram_bot::selector::media::fields::media_type` | Media type | Mediatyp | Core-literal match |
| 22188 | 823599075 | `component::telegram_bot::selector::media::fields::file` | File | Fil | Core-literal match |
| 22189 | 823599074 | `component::telegram_bot::selector::media::fields::caption` | Caption | Bildtext | Core-literal match |
| 22190 | 823599073 | `component::telegram_bot::selector::media::fields::authentication` | Authentication | Autentisering | Core-literal match |
| 22191 | 823405935 | `component::battery::triggers::stopped_charging::name` | Battery stopped charging | Batteri slutar ladda | Core-literal match |
| 22192 | 823405934 | `component::battery::triggers::stopped_charging::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 22193 | 823405933 | `component::battery::triggers::stopped_charging::fields::behavior::description` | The behavior of the targeted batteries to trigger on. | Det beteende som ska trigga för valda batterier. | Source-path follow-up open |
| 22194 | 823405932 | `component::battery::triggers::stopped_charging::description` | Triggers when one or more batteries stop charging. | Utlöses när ett eller flera batterier slutar att ladda. | Core-literal match |
| 22195 | 823405931 | `component::battery::triggers::started_charging::name` | Battery started charging | Batteri börjar ladda | Core-literal match |
| 22196 | 823405930 | `component::battery::triggers::started_charging::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 22197 | 823405929 | `component::battery::triggers::started_charging::fields::behavior::description` | The behavior of the targeted batteries to trigger on. | Det beteende som ska trigga för valda batterier. | Source-path follow-up open |
| 22198 | 823405928 | `component::battery::triggers::started_charging::description` | Triggers when one or more batteries start charging. | Utlöses när ett eller flera batterier börjar att ladda. | Core-literal match |
| 22199 | 823405927 | `component::battery::triggers::not_low::name` | Battery not low | Batteri är inte lågt | Source-path follow-up open |
| 22200 | 823405926 | `component::battery::triggers::not_low::fields::behavior::name` | Trigger when | Utlös när | Source-path follow-up open |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 824805047 | `component::gentex_homelink::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 824805046 | `component::google_tasks::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 824756554 | `component::smlight::entity::remote::remote::name` | IR Remote |
| 824543597 | `component::google::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 824420087 | `component::timer::selector::condition_behavior::options::any` | Any |
| 824420086 | `component::timer::selector::condition_behavior::options::all` | All |
| 824420083 | `component::timer::conditions::is_paused::fields::behavior::description` | How the state should match on the targeted timers. |
| 824420079 | `component::timer::conditions::is_idle::fields::behavior::description` | How the state should match on the targeted timers. |
| 824420075 | `component::timer::conditions::is_active::fields::behavior::description` | How the state should match on the targeted timers. |
| 824420072 | `component::timer::common::condition_behavior_description` | How the state should match on the targeted timers. |
| 824316294 | `component::calendar::selector::condition_behavior::options::any` | Any |
| 824316293 | `component::calendar::selector::condition_behavior::options::all` | All |
| 824316290 | `component::calendar::conditions::is_event_active::fields::behavior::description` | How the state should match on the targeted calendars. |
| 824316287 | `component::calendar::common::condition_behavior_description` | How the state should match on the targeted calendars. |
| 824015719 | `component::smappee::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 823983137 | `component::select::selector::condition_behavior::options::any` | Any |
| 823983136 | `component::select::selector::condition_behavior::options::all` | All |
| 823983131 | `component::select::conditions::is_option_selected::fields::behavior::description` | Whether the condition should pass when any or all targeted entities match. |
| 823976284 | `component::valve::selector::condition_behavior::options::any` | Any |
| 823976283 | `component::valve::selector::condition_behavior::options::all` | All |
| 823976280 | `component::valve::conditions::is_open::fields::behavior::description` | Whether the condition should pass when any or all targeted entities match. |
| 823976276 | `component::valve::conditions::is_closed::fields::behavior::description` | Whether the condition should pass when any or all targeted entities match. |
| 823816812 | `component::mcp::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 823816811 | `component::google_photos::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 823816789 | `component::fitbit::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 823751829 | `component::aladdin_connect::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 823708782 | `component::light::conditions::is_brightness::fields::threshold::description` | What to test for and threshold values. |
| 823708780 | `component::light::conditions::is_brightness::fields::behavior::description` | How the state should match on the targeted lights. |
| 823708777 | `component::light::common::condition_threshold_description` | What to test for and threshold values. |
| 823696351 | `component::proxmoxve::exceptions::no_permission_snapshot::message` | The configured Proxmox VE user does not have permission to create snapshots of VMs and containers. Please grant the user the 'VM.Snapshot' permission and try again. |
| 823693801 | `component::humidifier::conditions::is_mode::fields::behavior::description` | How the state should match on the targeted humidifiers. |
| 823645059 | `component::climate::conditions::is_hvac_mode::fields::behavior::description` | How the state should match on the targeted climate-control devices. |
| 823405933 | `component::battery::triggers::stopped_charging::fields::behavior::description` | The behavior of the targeted batteries to trigger on. |
| 823405929 | `component::battery::triggers::started_charging::fields::behavior::description` | The behavior of the targeted batteries to trigger on. |
| 823405927 | `component::battery::triggers::not_low::name` | Battery not low |
| 823405926 | `component::battery::triggers::not_low::fields::behavior::name` | Trigger when |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
