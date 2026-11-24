# Home Assistant Core – nya strängar, 714 poster

Granskning av aktuella Lokalise-strängar som tillkommit efter ögonblicksbilden 2026-11-19. Ordningen återställdes med aktuell nyckelmetadata och avgränsades vid senaste nyckeln i den sparade ögonblicksbilden (`983141395`). Samtliga 714 rader hämtades via Lokalise API.

## Resultat

- 714/714 poster granskade; engelska och svenska värden återlästa från Lokalise API. Fem tomma svenska värden kompletterades.
- 465 strängar matchar direkt aktuell Home Assistant Core-källa; 248 referensanvändningar med 116 unika mål kontrollerades. Referensmål saknas: 0; avvikande konsumenter efter rättelse: 0.
- En HomeWizard-reparationsnyckel saknar direkt motsvarande `fix_flow.error` i `strings.json`; källans repair flow använder `network_error`, och Lokalise-källan är `Failed to connect`. Den är redovisad för källägaruppföljning.
- Platshållarmismatch efter rättelser: 0. Tomma texter: 0. Pluralposter: 0.
- 13 värden i den nya batchen kompletterades/korrigerades och två delade referensmål uppdaterades; samtliga 15 Lokalise-skrivningar API-lästes tillbaka. MA-målet `get_library::offset::name` synkades till `Förskjutning` och LiteLLM:s STT-mål synkades med TTS-konsumenten.
- `example.com` förekom inte i dessa 714 käll- eller måltexter.

## Ändringar sparade

| Fullständig nyckel | Tidigare svenska | Ny svenska |
|---|---|---|
| `component::marketplace::exceptions::resource_archive_without_resource::message` | (tom) | {file} innehåller ingen {resource} i rotkatalogen eller i någon av dess mappar. |
| `component::marketplace::exceptions::resource_archive_unusable::message` | (tom) | {file} är inte ett giltigt ZIP-arkiv. |
| `component::yardian::config::step::user::data_description::access_token` | (tom) | Åtkomsttoken för din Yardian Smart Sprinkler Controller. Du hittar den i Yardian-appen. |
| `component::yardian::config::step::reauth_confirm::data_description::access_token` | (tom) | Åtkomsttoken för din Yardian Smart Sprinkler Controller. Du hittar den i Yardian-appen. |
| `component::specialized_turbo::config::error::incomplete_advertisement` | (tom) | Home Assistant fick inte de Bluetooth-data som behövs för att identifiera din cykel. Håll cykeln vaken och inom räckhåll och försök igen. |
| `component::tado::exceptions::tado_x_unsupported::message` | Tidigare värde finns i Lokalise-historik | I hemmet ”{home}” används Tado X-enheter, som inte stöds av den här integrationen. Tado X använder ett annat API som Tado inte gör tillgängligt för tredje part. För att använda enheterna med Home Assistant konfigurerar du dem i stället via Matter-integrationen med en Thread-gränsrouter. |
| `component::tado::config::abort::tado_x_unsupported` | Tidigare värde finns i Lokalise-historik | Tado X-enheter stöds inte av den här integrationen. Tado X använder ett annat API som Tado inte gör tillgängligt för tredje part. Konfigurera enheterna via Matter-integrationen med en Thread-gränsrouter för att använda dem med Home Assistant. |
| `component::litellm::config_subentries::tts::abort::entry_not_loaded` | Tidigare värde finns i Lokalise-historik | Huvudposten för integrationen är inte inläst. Läs in integrationen innan du konfigurerar om den. |
| `component::smartthings::exceptions::quota_exceeded::message` | Tidigare värde finns i Lokalise-historik | SmartThings API-kvoten har överskridits. För att få åtkomst till SmartThings API:er krävs en aktiv API-plan med kvarvarande anropskvot. Hantera dina planer i SmartThings Developer Center: {manage_plans_url} |
| `component::smartthings::config::error::quota_exceeded` | Tidigare värde finns i Lokalise-historik | SmartThings API-kvoten har överskridits. För att få åtkomst till SmartThings API:er krävs en aktiv API-plan med kvarvarande anropskvot. Hantera dina planer i SmartThings Developer Center: {manage_plans_url} |
| `component::smartthings::config::abort::quota_exceeded` | Tidigare värde finns i Lokalise-historik | SmartThings API-kvoten har överskridits. För att få åtkomst till SmartThings API:er krävs en aktiv API-plan med kvarvarande anropskvot. Hantera dina planer i SmartThings Developer Center: {manage_plans_url} |
| `component::synology_dsm::config::abort::wrong_nas` | Tidigare värde finns i Lokalise-historik | NAS-enheten på den här adressen är inte den som konfigurerades för den här posten (annat serienummer). |
| `component::music_assistant::services::get_queue::fields::username::description` | Tidigare värde finns i Lokalise-historik | Music Assistant-användarnamnet som används för att hämta objekt från kön. Begäran misslyckas om användaren inte har åtkomst till spelaren. Som standard används det Music Assistant-konto som är kopplat till Home Assistant-användaren som gör begäran. Om inget konto är kopplat används standardkontot. |
| `component::music_assistant::services::get_library::fields::offset::name` | Offset | Förskjutning |

## Fullständig radinventering

| Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---|---|---|---|
| 986788155 | `component::marketplace::exceptions::resource_archive_without_resource::message` | {file} has no {resource} in its root or in a folder at its root. | {file} innehåller ingen {resource} i rotkatalogen eller i någon av dess mappar. | Core-literal match |
| 986788154 | `component::marketplace::exceptions::resource_archive_unusable::message` | {file} is not a valid ZIP archive. | {file} är inte ett giltigt ZIP-arkiv. | Core-literal match |
| 986649629 | `component::yardian::config::step::user::data_description::access_token` | Access token for your Yardian Smart Sprinkler Controller. You can find it in the Yardian app. | Åtkomsttoken för din Yardian Smart Sprinkler Controller. Du hittar den i Yardian-appen. | Core-literal match |
| 986649628 | `component::yardian::config::step::reauth_confirm::data_description::access_token` | Access token for your Yardian Smart Sprinkler Controller. You can find it in the Yardian app. | Åtkomsttoken för din Yardian Smart Sprinkler Controller. Du hittar den i Yardian-appen. | Shared reference target checked |
| 986543208 | `component::specialized_turbo::config::error::incomplete_advertisement` | Home Assistant did not receive the Bluetooth data it needs to identify your bike. Keep the bike awake and in range, then try again. | Home Assistant fick inte de Bluetooth-data som behövs för att identifiera din cykel. Håll cykeln vaken och inom räckhåll och försök igen. | Core-literal match |
| 986488182 | `component::infrared::common::missing_infrared_entity` | Select an infrared emitter or receiver. | Välj en infraröd sändare eller mottagare. | Core-literal match |
| 986488181 | `component::infrared::common::infrared_receiver_entity_id_description` | The infrared receiver entity to use for receiving signals. | Mottagarentiteten som ska användas för att ta emot infraröda signaler. | Core-literal match |
| 986446935 | `component::broadlink::exceptions::invalid_rf_timings::message` | Broadlink devices cannot transmit these RF timings | Broadlink-enheter kan inte sända dessa RF-timings | Core-literal match |
| 986436843 | `component::teslemetry::issues::missing_scopes::title` | Tesla authorization is missing permissions | Tesla-auktorisering saknar behörigheter | Core-literal match |
| 986436842 | `component::teslemetry::issues::missing_scopes::description` | Tesla is refusing to share vehicle data with Teslemetry because your Tesla authorization is missing the required permissions. Select **Learn more** to sign in with Tesla again and grant the missing permissions, including Vehicle Information, then reload the integration. | Tesla vägrar att dela fordonsdata med Teslemetry eftersom din Tesla-auktorisering saknar de behörigheter som krävs. Välj **Läs mer** för att logga in på Tesla igen och bevilja de behörigheter som saknas, inklusive fordonsinformation, och ladda sedan om integrationen. | Core-literal match |
| 986436841 | `component::teslemetry::exceptions::update_failed_missing_scopes::message` | Tesla authorization is missing the permissions to read vehicle data | Tesla-auktoriseringen saknar behörigheter att läsa fordonsdata | Core-literal match |
| 986431879 | `component::bluetooth::exceptions::adapter_not_found::message` | Bluetooth adapter with address {address} not found | Bluetooth-adapter med adressen {address} hittades inte | Core-literal match |
| 986392312 | `component::evohome::exceptions::mode_unknown::message` | The mode `{mode}` is not a valid system mode | Läget `{mode} ` är inte ett giltigt systemläge | Core-literal match |
| 986392181 | `component::zwave_js::entity::update::release_notes_messages::sleeping_device_wakeup` | This is a battery powered sleeping device. You may need to wake it up manually for the update to begin. To wake up this device:<br><br>{wakeup_instructions} | Detta är en batteridriven enhet i viloläge. Du kan behöva väcka den manuellt för att uppdateringen ska starta. Så här väcker du enheten:<br><br>{wakeup_instructions} | Core-literal match |
| 986392180 | `component::zwave_js::entity::update::release_notes_messages::sleeping_device` | This is a battery powered sleeping device. You may need to wake it up manually for the update to begin. | Detta är en batteridriven enhet i viloläge. Du kan behöva väcka den manuellt för att uppdateringen ska starta. | Core-literal match |
| 986389530 | `component::tado::exceptions::tado_x_unsupported::message` | The home "{home}" uses Tado X devices, which are not supported by this integration. Tado X uses a different API that Tado does not allow third parties to access. To use these devices with Home Assistant, set them up via the Matter integration with a Thread border router instead. | I hemmet ”{home}” används Tado X-enheter, som inte stöds av den här integrationen. Tado X använder ett annat API som Tado inte gör tillgängligt för tredje part. För att använda enheterna med Home Assistant konfigurerar du dem i stället via Matter-integrationen med en Thread-gränsrouter. | Core-literal match |
| 986389529 | `component::tado::config::abort::tado_x_unsupported` | Tado X devices are not supported by this integration. Tado X uses a different API that Tado does not allow third parties to access. To use these devices with Home Assistant, set them up via the Matter integration with a Thread border router instead. | Tado X-enheter stöds inte av den här integrationen. Tado X använder ett annat API som Tado inte gör tillgängligt för tredje part. Konfigurera enheterna via Matter-integrationen med en Thread-gränsrouter för att använda dem med Home Assistant. | Core-literal match |
| 986389229 | `component::homeassistant::exceptions::update_failed_timeout::message` | Timed out while fetching the data | Tidsgränsen överskreds vid hämtning av data | Core-literal match |
| 986389228 | `component::homeassistant::exceptions::update_failed::message` | Failed to fetch the data | Det gick inte att hämta uppgifterna | Core-literal match |
| 986389162 | `component::infrared::common::no_infrared_entities` | No infrared entities found. Please set up an infrared device first. | Inga infraröda entiteter hittades. Konfigurera först en infraröd enhet. | Core-literal match |
| 986389161 | `component::infrared::common::no_infrared_emitters` | No infrared emitter entities found. Please set up an infrared device first. | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. | Core-literal match |
| 986389160 | `component::infrared::common::infrared_receiver_entity_id` | Infrared receiver | Infraröd mottagare | Core-literal match |
| 986389159 | `component::infrared::common::infrared_entity_id_description` | The infrared emitter entity to use for sending commands. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Core-literal match |
| 986389158 | `component::infrared::common::infrared_entity_id` | Infrared emitter | Infraröd sändare | Core-literal match |
| 986387813 | `component::melcloud_home::entity::sensor::operation_status::state::legionella_prevention` | Legionella prevention | Förebyggande av legionella | Core-literal match |
| 986201708 | `component::zha::exceptions::no_warning_device::message` | Device {ieee} is not an IAS warning device, so this action cannot be performed. | Anordning {ieee} är inte en IAS-varningsenhet, så den här åtgärden kan inte utföras. | Core-literal match |
| 986201707 | `component::zha::exceptions::group_not_found::message` | Group {group_id} was not found. | Grupp {group_id} hittades inte. | Core-literal match |
| 986201706 | `component::zha::exceptions::device_not_found::message` | Device {ieee} was not found. | Enheten {ieee} hittades inte. | Core-literal match |
| 986170573 | `component::esphome::entity::timer_list::timers::name` | Timers | Timers | Core-literal match |
| 986128161 | `component::zha::entity::update::release_notes_messages::network_reliability` | If you are having issues updating a specific device, make sure that you've eliminated [common environmental issues]({docs_url}) that could be affecting network reliability. OTA updates require a reliable network. | Om du har problem med att uppdatera en viss enhet bör du först se till att du har uteslutit [vanliga miljörelaterade problem]({docs_url}) som kan påverka nätverkets stabilitet. OTA-uppdateringar kräver ett stabilt nätverk. | Core-literal match |
| 986128160 | `component::zha::entity::update::release_notes_messages::battery_powered` | Battery powered devices can sometimes take multiple hours to update and you may need to wake the device for the update to begin. | Det kan ibland ta flera timmar att uppdatera batteridrivna enheter, och du kan behöva väcka enheten för att uppdateringen ska påbörjas. | Core-literal match |
| 986102174 | `component::google_health::entity::sensor::vigorous_activity::name` | Vigorous activity | Kraftfull aktivitet | Core-literal match |
| 986102173 | `component::google_health::entity::sensor::sedentary_time::name` | Sedentary time | Stillasittande tid | Core-literal match |
| 986102172 | `component::google_health::entity::sensor::peak_active_zone_minutes::name` | Peak active zone minutes | Aktiva minuter i Maximalt aktiv zon | Core-literal match |
| 986102171 | `component::google_health::entity::sensor::moderate_activity::name` | Moderate activity | Måttlig aktivitet | Core-literal match |
| 986102170 | `component::google_health::entity::sensor::light_activity::name` | Light activity | Lätt aktivitet | Core-literal match |
| 986102169 | `component::google_health::entity::sensor::fat_burn_active_zone_minutes::name` | Fat burn active zone minutes | Aktiva minuter för fettförbränning | Core-literal match |
| 986102168 | `component::google_health::entity::sensor::elevation::name` | Elevation | Höjdskillnad | Core-literal match |
| 986102167 | `component::google_health::entity::sensor::cardio_active_zone_minutes::name` | Cardio active zone minutes | Minuter i den aktiva konditionszonen | Core-literal match |
| 986102166 | `component::google_health::entity::sensor::active_zone_minutes::name` | Active zone minutes | Aktiv zon minuter | Core-literal match |
| 985994681 | `component::nintendo_parental_controls::entity::sensor::last_sync::name` | Last synced | Senast synkroniserad | Core-literal match |
| 985818030 | `component::litellm::config_subentries::tts::step::init::description` | Select the text-to-speech model and voice. LiteLLM does not report language capabilities for individual backend models. | Välj text-till-tal-modell och röst. LiteLLM anger inte vilka språk som stöds för enskilda bakgrundsmodeller. | Core-literal match |
| 985818029 | `component::litellm::config_subentries::tts::step::init::data_description::voice` | The voice to speak with. The listed voices are OpenAI voices; enter the voice name of your backend for other models. | Rösten som ska användas. De angivna rösterna är röster från OpenAI; ange namnet på rösten i din backend för andra modeller. | Core-literal match |
| 985818028 | `component::litellm::config_subentries::tts::step::init::data_description::model` | The model to use to generate speech | Modellen som ska användas för att generera tal | Core-literal match |
| 985818027 | `component::litellm::config_subentries::tts::step::init::data::voice` | Voice | Röst | Core-literal match |
| 985818026 | `component::litellm::config_subentries::tts::step::init::data::model` | Model | Modell | Shared reference target checked |
| 985818025 | `component::litellm::config_subentries::tts::initiate_flow::user` | Add text-to-speech service | Lägg till tjänst för text-till-tal | Core-literal match |
| 985818024 | `component::litellm::config_subentries::tts::initiate_flow::reconfigure` | Reconfigure text-to-speech service | Konfigurera om tjänst för text-till-tal | Core-literal match |
| 985818023 | `component::litellm::config_subentries::tts::entry_type` | Text-to-speech | Text-till-tal | Core-literal match |
| 985818022 | `component::litellm::config_subentries::tts::abort::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 985818021 | `component::litellm::config_subentries::tts::abort::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 985818020 | `component::litellm::config_subentries::tts::abort::entry_not_loaded` | The main integration entry is not loaded. Please ensure the integration is loaded before reconfiguring. | Huvudposten för integrationen är inte inläst. Läs in integrationen innan du konfigurerar om den. | Shared reference target checked |
| 985818019 | `component::litellm::config_subentries::tts::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 985811216 | `component::aemet::config::step::reconfigure::description` | Enter a new AEMET OpenData API key. AEMET API keys expire periodically, and you can generate a new one at {api_key_url} | Ange en ny AEMET OpenData API-nyckel. AEMET API-nycklar upphör att gälla med jämna mellanrum, och du kan skapa en ny på {api_key_url} | Core-literal match |
| 985811215 | `component::aemet::config::step::reconfigure::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 985811214 | `component::aemet::config::abort::unique_id_mismatch` | The location of this entry does not match its identifier. Remove the integration and add it again. | Den här postens plats stämmer inte överens med dess identifierare. Ta bort integrationen och lägg till den igen. | Core-literal match |
| 985711053 | `component::alexa_devices::entity::number::inactive_brightness::name` | Inactive brightness | Inaktiv ljusstyrka | Core-literal match |
| 985711052 | `component::alexa_devices::entity::number::active_brightness::name` | Active brightness | Aktiv ljusstyrka | Core-literal match |
| 985689501 | `component::recorder::services::get_history::name` | Get Recorder history | Hämta inspelningshistoriken | Core-literal match |
| 985689500 | `component::recorder::services::get_history::fields::start_time::name` | Start time | Starttid | Core-literal match |
| 985689499 | `component::recorder::services::get_history::fields::start_time::description` | The start time for the history query. | Starttiden för historikfrågan. | Core-literal match |
| 985689498 | `component::recorder::services::get_history::fields::entity_id::name` | Entities | Entiteter | Core-literal match |
| 985689497 | `component::recorder::services::get_history::fields::entity_id::description` | The entity IDs to return history for. | De enhets-ID:n för vilka historik ska hämtas. | Core-literal match |
| 985689496 | `component::recorder::services::get_history::fields::end_time::name` | End time | Sluttid | Core-literal match |
| 985689495 | `component::recorder::services::get_history::fields::end_time::description` | The end time for the history query. If omitted, returns all history from start time onward. | Sluttid för historikfrågan. Om detta utelämnas returneras all historik från starttiden och framåt. | Core-literal match |
| 985689494 | `component::recorder::services::get_history::fields::allow_truncation::name` | Allow truncation | Tillåt avkortning | Core-literal match |
| 985689493 | `component::recorder::services::get_history::fields::allow_truncation::description` | Truncate the returned history instead of raising an error when an entity exceeds the limit of recorded state changes. The limit applies to recorded state changes, not returned segments. | Korta ned den returnerade historiken istället för att generera ett fel när en entitet överskrider gränsen för registrerade tillståndsförändringar. Gränsen gäller registrerade tillståndsförändringar, inte returnerade segment. | Core-literal match |
| 985689492 | `component::recorder::services::get_history::description` | Retrieves history data for entities within a specific time period. | Hämtar historikdata för enheter inom en viss tidsperiod. | Core-literal match |
| 985689491 | `component::recorder::exceptions::start_time_in_future::message` | Start time must be in the past | Starttiden måste ligga i det förflutna | Core-literal match |
| 985689490 | `component::recorder::exceptions::max_records_exceeded::message` | More than {max_records} state changes were recorded for {entity_id} in the requested period. Use a shorter period or set allow truncation. | Över {max_records} ändringar av tillstånd registrerades för {entity_id} under den begärda tidsperioden. Använd en kortare tidsperiod eller aktivera avkortning. | Core-literal match |
| 985689489 | `component::recorder::exceptions::max_entities_exceeded::message` | Cannot request history for more than {max_entities} entities. | Det går inte att begära historik för fler än {max_entities} -objekt. | Core-literal match |
| 985689488 | `component::recorder::exceptions::end_time_before_start_time::message` | End time must be greater than or equal to start time | Sluttiden måste vara efter eller lika med starttiden | Core-literal match |
| 985345251 | `component::evohome::exceptions::request_invalid::message` | The request is not valid | Begäran är inte giltig | Core-literal match |
| 985345250 | `component::evohome::exceptions::override_request_invalid::message` | The override can't be set as requested | Åsidosättningen kan inte ställas in enligt begäran. | Core-literal match |
| 985345249 | `component::evohome::exceptions::override_not_in_future::message` | The override must end in the future (if the duration is 0, the next scheduled setpoint may have already passed) | Åsidosättningen måste sluta i framtiden (om varaktigheten är 0 kan nästa schemalagda börvärde redan ha passerat). | Core-literal match |
| 985345248 | `component::evohome::exceptions::mode_timespan_required::message` | The mode `{mode}` requires a 'Duration' or 'Period' | Läget `{mode}` kräver ”Varaktighet” eller ”Period”. | Core-literal match |
| 985345247 | `component::evohome::exceptions::mode_timespan_not_in_future::message` | The 'Duration' or 'Period' of the mode `{mode}` must end in the future | ”Varaktighet” eller ”Period” för läget `{mode}` måste sluta i framtiden. | Core-literal match |
| 985345246 | `component::evohome::exceptions::mode_request_invalid::message` | The mode `{mode}` can't be set as requested | Det går inte att ställa in läget `{mode}` enligt begäran. | Core-literal match |
| 985333076 | `component::smartthings::exceptions::quota_exceeded::message` | SmartThings API quota exceeded. SmartThings requires an active API plan with remaining API usage quotas to access the SmartThings APIs. Visit the SmartThings Developer Center to manage your plans: {manage_plans_url} | SmartThings API-kvoten har överskridits. För att få åtkomst till SmartThings API:er krävs en aktiv API-plan med kvarvarande anropskvot. Hantera dina planer i SmartThings Developer Center: {manage_plans_url} | Core-literal match |
| 985333075 | `component::smartthings::exceptions::entitlement_required::message` | SmartThings subscription required. Reconnect your SmartThings account to restore access. | SmartThings-prenumeration krävs. Återanslut ditt SmartThings-konto för att återställa åtkomsten. | Core-literal match |
| 985333074 | `component::smartthings::config::step::reauth_method::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 985333073 | `component::smartthings::config::step::reauth_method::menu_options::new_app` | Create a new app | Skapa en ny app | Core-literal match |
| 985333072 | `component::smartthings::config::step::reauth_method::menu_options::auth` | Reconnect with the existing app | Återanslut med den befintliga appen | Core-literal match |
| 985333071 | `component::smartthings::config::step::reauth_method::description` | Reconnect with the SmartThings app Home Assistant created for you, or enter a new Personal Access Token to create a replacement app, for example after the app was deleted. | Återanslut med SmartThings-appen som Home Assistant skapade åt dig eller ange en ny personlig åtkomsttoken för att skapa en ersättningsapp, till exempel efter att appen har tagits bort. | Core-literal match |
| 985333070 | `component::smartthings::config::step::pat::data_description::pat_token` | A Personal Access Token used to create your own SmartThings app. | En personlig åtkomsttoken som används för att skapa en egen SmartThings-app. | Core-literal match |
| 985333069 | `component::smartthings::config::step::pat::data::pat_token` | Personal Access Token | Personlig åtkomsttoken | Core-literal match |
| 985333068 | `component::smartthings::config::error::quota_exceeded` | SmartThings API quota exceeded. SmartThings requires an active API plan with remaining API usage quotas to access the SmartThings APIs. Visit the SmartThings Developer Center to manage your plans: {manage_plans_url} | SmartThings API-kvoten har överskridits. För att få åtkomst till SmartThings API:er krävs en aktiv API-plan med kvarvarande anropskvot. Hantera dina planer i SmartThings Developer Center: {manage_plans_url} | Shared reference target checked |
| 985333067 | `component::smartthings::config::error::invalid_pat` | Invalid Personal Access Token. Please make sure you have entered it correctly and that it has not expired. | Ogiltig personlig åtkomsttoken. Kontrollera att du har angett den korrekt och att den inte har upphört att gälla. | Core-literal match |
| 985333066 | `component::smartthings::config::error::entitlement_required` | SmartThings API Plan required. Please subscribe to a plan before setting up this integration and ensure your Personal Access token has 'application' scopes enabled. | SmartThings API-plan krävs. Prenumerera på en plan innan du konfigurerar den här integrationen och se till att din personliga åtkomsttoken har aktiverade behörighetsomfång för program. | Core-literal match |
| 985333065 | `component::smartthings::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 985333064 | `component::smartthings::config::abort::quota_exceeded` | SmartThings API quota exceeded. SmartThings requires an active API plan with remaining API usage quotas to access the SmartThings APIs. Visit the SmartThings Developer Center to manage your plans: {manage_plans_url} | SmartThings API-kvoten har överskridits. För att få åtkomst till SmartThings API:er krävs en aktiv API-plan med kvarvarande anropskvot. Hantera dina planer i SmartThings Developer Center: {manage_plans_url} | Core-literal match |
| 985333063 | `component::smartthings::config::abort::entitlement_required` | SmartThings API Plan required. Please subscribe to a plan before setting up this integration and ensure your Personal Access token has 'application' scopes enabled. | SmartThings API-plan krävs. Prenumerera på en plan innan du konfigurerar den här integrationen och se till att din personliga åtkomsttoken har aktiverade behörighetsomfång för program. | Shared reference target checked |
| 985241964 | `component::hassio::exceptions::supervisor_update_error::message` | Error updating Home Assistant Supervisor: {error} | Fel vid uppdatering av Home Assistant Supervisor: {error} | Core-literal match |
| 985237300 | `component::workday::options::step::init::sections::custom_holidays::name` | Custom holidays | Anpassade helgdagar | Shared reference target checked |
| 985237299 | `component::workday::options::step::init::sections::custom_holidays::data_description::remove_holidays` | Remove holidays as YYYY-MM-DD, as range using `,` as separator or by using partial of name | Ta bort helgdagar som ÅÅÅÅ-MM-DD, som intervall med `,` som avgränsare eller med en del av namnet | Shared reference target checked |
| 985237298 | `component::workday::options::step::init::sections::custom_holidays::data_description::add_holidays` | Add custom holidays as YYYY-MM-DD or as range using `,` as separator | Lägg till anpassade helgdagar som ÅÅÅÅ-MM-DD eller som intervall med `,` som avgränsare | Shared reference target checked |
| 985237297 | `component::workday::options::step::init::sections::custom_holidays::data::remove_holidays` | Remove holidays | Ta bort helgdagar | Shared reference target checked |
| 985237296 | `component::workday::options::step::init::sections::custom_holidays::data::add_holidays` | Add holidays | Lägg till helgdagar | Shared reference target checked |
| 985237295 | `component::workday::options::step::init::sections::country_settings::name` | Country settings | Landsinställningar | Shared reference target checked |
| 985237294 | `component::workday::options::step::init::sections::country_settings::data_description::province` | State, territory, province or region of country | Landets delstat, territorium, provins eller region | Shared reference target checked |
| 985237293 | `component::workday::options::step::init::sections::country_settings::data_description::language` | Language to use when configuring named holiday exclusions | Språk som ska användas när undantag för namngivna helgdagar konfigureras | Shared reference target checked |
| 985237292 | `component::workday::options::step::init::sections::country_settings::data_description::category` | Select additional categories to include as holidays | Välj ytterligare kategorier som ska inkluderas som helgdagar | Shared reference target checked |
| 985237291 | `component::workday::options::step::init::sections::country_settings::data::province` | Subdivision of country | Landets underindelning | Shared reference target checked |
| 985237290 | `component::workday::options::step::init::sections::country_settings::data::language` | Language for named holidays | Språk för namngivna helgdagar | Shared reference target checked |
| 985237289 | `component::workday::options::step::init::sections::country_settings::data::category` | Additional category as holiday | Ytterligare kategori som helgdag | Shared reference target checked |
| 985237288 | `component::workday::config::step::options::sections::custom_holidays::name` | Custom holidays | Anpassade helgdagar | Core-literal match |
| 985237287 | `component::workday::config::step::options::sections::custom_holidays::data_description::remove_holidays` | Remove holidays as YYYY-MM-DD, as range using `,` as separator or by using partial of name | Ta bort helgdagar som ÅÅÅÅ-MM-DD, som intervall med `,` som avgränsare eller med en del av namnet | Core-literal match |
| 985237286 | `component::workday::config::step::options::sections::custom_holidays::data_description::add_holidays` | Add custom holidays as YYYY-MM-DD or as range using `,` as separator | Lägg till anpassade helgdagar som ÅÅÅÅ-MM-DD eller som intervall med `,` som avgränsare | Core-literal match |
| 985237285 | `component::workday::config::step::options::sections::custom_holidays::data::remove_holidays` | Remove holidays | Ta bort helgdagar | Core-literal match |
| 985237284 | `component::workday::config::step::options::sections::custom_holidays::data::add_holidays` | Add holidays | Lägg till helgdagar | Core-literal match |
| 985237283 | `component::workday::config::step::options::sections::country_settings::name` | Country settings | Landsinställningar | Core-literal match |
| 985237282 | `component::workday::config::step::options::sections::country_settings::data_description::province` | State, territory, province or region of country | Landets delstat, territorium, provins eller region | Core-literal match |
| 985237281 | `component::workday::config::step::options::sections::country_settings::data_description::language` | Language to use when configuring named holiday exclusions | Språk som ska användas när undantag för namngivna helgdagar konfigureras | Core-literal match |
| 985237280 | `component::workday::config::step::options::sections::country_settings::data_description::category` | Select additional categories to include as holidays | Välj ytterligare kategorier som ska inkluderas som helgdagar | Core-literal match |
| 985237279 | `component::workday::config::step::options::sections::country_settings::data::province` | Subdivision of country | Landets underindelning | Core-literal match |
| 985237278 | `component::workday::config::step::options::sections::country_settings::data::language` | Language for named holidays | Språk för namngivna helgdagar | Core-literal match |
| 985237277 | `component::workday::config::step::options::sections::country_settings::data::category` | Additional category as holiday | Ytterligare kategori som helgdag | Core-literal match |
| 985050967 | `component::alexa_devices::entity::climate::thermostat::state_attributes::fan_mode::state::on` | On | På | Shared reference target checked |
| 985050966 | `component::alexa_devices::entity::climate::thermostat::state_attributes::fan_mode::state::circulate` | Circulate | Cirkulera | Core-literal match |
| 985050965 | `component::alexa_devices::entity::climate::thermostat::state_attributes::fan_mode::state::auto` | Auto | Auto | Shared reference target checked |
| 985046665 | `component::portainer::entity::sensor::stack_last_deployed::name` | Last deployed | Senast driftsatt | Core-literal match |
| 984980517 | `component::nextdns::entity::switch::block_rotating_ad_domains::name` | Block rotating ad domains | Blockera roterande annonsdomäner | Core-literal match |
| 984980516 | `component::nextdns::entity::switch::block_algorithmically_generated_domains::name` | Block algorithmically generated domains | Blockera algoritmiskt genererade domäner | Core-literal match |
| 984980512 | `component::schlage::exceptions::schlage_invalid_schedule_timezone::message` | Start or end datetime falls within an ambiguous or invalid daylight saving time transition. | Start- eller sluttiden infaller under en tvetydig eller ogiltig övergång till eller från sommartid. | Core-literal match |
| 984980511 | `component::schlage::entity::select::auto_lock_time::state:::900` | 15 minutes | 15 minuter | Core-literal match |
| 984980510 | `component::schlage::entity::select::auto_lock_time::state:::1800` | 30 minutes | 30 minuter | Core-literal match |
| 984916639 | `component::paj_gps::exceptions::invalid_auth::message` | Authentication with the PAJ GPS account failed. Please reauthenticate. | Autentiseringen med PAJ GPS-kontot misslyckades. Autentisera igen. | Core-literal match |
| 984916638 | `component::paj_gps::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 984916637 | `component::paj_gps::config::step::reauth_confirm::description` | The password for {email} is no longer valid. Please enter the current password. | Lösenordet för {email} är inte längre giltigt. Ange det aktuella lösenordet. | Core-literal match |
| 984916636 | `component::paj_gps::config::step::reauth_confirm::data_description::password` | Password used to log in to Finder Portal (finder-portal.com) | Lösenord som används för att logga in på Finder Portal (finder-portal.com) | Shared reference target checked |
| 984916635 | `component::paj_gps::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 984916634 | `component::paj_gps::config::abort::unique_id_mismatch` | The provided credentials belong to a different PAJ GPS account. | De angivna inloggningsuppgifterna tillhör ett annat PAJ GPS-konto. | Core-literal match |
| 984916623 | `component::synology_dsm::config::abort::wrong_nas` | The NAS at this address is not the one this entry was set up for (different serial number). | NAS-enheten på den här adressen är inte den som konfigurerades för den här posten (annat serienummer). | Core-literal match |
| 984916379 | `component::flux_led::config::step::reconfigure::data_description::host` | The hostname or IP address of your Magic Home device. | Värdnamnet eller IP-adressen för din Magic Home-enhet. | Core-literal match |
| 984916378 | `component::flux_led::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 984916377 | `component::flux_led::config::abort::unique_id_mismatch` | Please ensure you reconfigure against the same device. | Se till att du konfigurerar om samma enhet. | Core-literal match |
| 984916376 | `component::twinkly::config::step::reconfigure::data_description::host` | Hostname or IP address of your Twinkly device. | Värdnamn eller IP-adress för din Twinkly-enhet. | Shared reference target checked |
| 984916375 | `component::twinkly::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 984916374 | `component::twinkly::config::abort::unique_id_mismatch` | Please ensure you reconfigure against the same device. | Se till att du konfigurerar om samma enhet. | Core-literal match |
| 984916373 | `component::glances::config::step::reconfigure::data_description::host` | The hostname or IP address of the system running your Glances system monitor. | Värdnamnet eller IP-adressen för det system som kör din Glances systemmonitor. | Shared reference target checked |
| 984916372 | `component::glances::config::step::reconfigure::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 984916371 | `component::glances::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference target checked |
| 984916370 | `component::glances::config::step::reconfigure::data::ssl` | Uses an SSL certificate | Använder ett SSL-certifikat | Shared reference target checked |
| 984916369 | `component::glances::config::step::reconfigure::data::port` | Port | Port | Shared reference target checked |
| 984916368 | `component::glances::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 984916367 | `component::glances::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 984916366 | `component::xiaomi_miio::config::step::reconfigure::description` | You will need the 32 character API token, see {retrieving_token_url} for instructions. Please note that this API token is different from the key used by the Xiaomi Aqara integration. | Du behöver en API-token med 32 tecken. Se {retrieving_token_url} för instruktioner. Observera att denna API-token skiljer sig från nyckeln som används av Xiaomi Aqara-integrationen. | Shared reference target checked |
| 984916365 | `component::xiaomi_miio::config::step::reconfigure::data::token` | API token | API-token | Shared reference target checked |
| 984916364 | `component::xiaomi_miio::config::step::reconfigure::data::host` | IP address | IP-adress | Shared reference target checked |
| 984916363 | `component::xiaomi_miio::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 984916362 | `component::xiaomi_miio::config::abort::unique_id_mismatch` | The device at this address is not the device that was originally set up. | Enheten på den här adressen är inte den enhet som ursprungligen konfigurerades. | Core-literal match |
| 984916220 | `component::aprilaire::config::step::reconfigure::data_description::port` | Usually 7000 or 8000 | Vanligtvis 7000 eller 8000 | Shared reference target checked |
| 984916219 | `component::aprilaire::config::step::reconfigure::data::port` | Port | Port | Shared reference target checked |
| 984916218 | `component::aprilaire::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 984916217 | `component::aprilaire::config::abort::wrong_device` | The thermostat at this host is not the one that was originally configured. | Termostaten på den här värden är inte den som ursprungligen konfigurerades. | Core-literal match |
| 984916138 | `component::samsung_infrared::config::step::reconfigure::title` | Reconfigure infrared remote | Konfigurera om infraröd fjärrkontroll | Core-literal match |
| 984916137 | `component::samsung_infrared::config::step::reconfigure::description` | Select the infrared emitter entity to use for controlling your device. | Välj den infraröda sändarentiteten som ska användas för att styra enheten. | Core-literal match |
| 984916136 | `component::samsung_infrared::config::step::reconfigure::data_description::infrared_emitter_entity_id` | The infrared emitter entity to use for sending commands. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Shared reference target checked |
| 984916135 | `component::samsung_infrared::config::step::reconfigure::data_description::device_type` | The type of device to control. | Typ av enhet att styra. | Core-literal match |
| 984916134 | `component::samsung_infrared::config::step::reconfigure::data::infrared_emitter_entity_id` | Infrared emitter | Infraröd sändare | Shared reference target checked |
| 984916133 | `component::samsung_infrared::config::step::reconfigure::data::device_type` | Device type | Enhetstyp | Core-literal match |
| 984916132 | `component::knx::config::step::remove_knxkeys::title` | Remove KNX keyring | Ta bort KNX-nyckelring | Core-literal match |
| 984916131 | `component::knx::config::step::remove_knxkeys::description` | The imported `.knxkeys` file of project `{keyring_project}` will be deleted. It currently provides KNX Data Secure keys for {data_secure_count} group addresses. KNX IP Secure and KNX Data Secure keys from this file will no longer be available. | Den importerade filen `.knxkeys` för projektet `{keyring_project}` kommer att tas bort. Den innehåller för närvarande KNX Data Secure-nycklar för {data_secure_count} gruppadresser. KNX IP Secure- och KNX Data Secure-nycklar från filen blir inte längre tillgängliga. | Core-literal match |
| 984916130 | `component::knx::config::step::reconfigure::menu_options::remove_knxkeys` | Remove KNX keyring file | Ta bort KNX-nyckelringsfil | Core-literal match |
| 984916129 | `component::knx::config::abort::keyring_required` | The current connection uses the keyring file for KNX IP Secure. Reconfigure the connection with manual credentials or another connection type before removing it. | Den aktuella anslutningen använder nyckelringsfilen för KNX IP Secure. Konfigurera om anslutningen med manuella autentiseringsuppgifter eller en annan anslutningstyp innan du tar bort den. | Core-literal match |
| 984916105 | `component::indi_allsky::config::step::reconfigure::description` | Update the connection details for your INDI Allsky instance. | Uppdatera anslutningsuppgifterna för din INDI Allsky-instans. | Core-literal match |
| 984916104 | `component::indi_allsky::config::step::reconfigure::data_description::verify_ssl` | Verify the SSL certificate of the INDI Allsky server. | Verifiera SSL-certifikatet för INDI Allsky-servern. | Core-literal match |
| 984916103 | `component::indi_allsky::config::step::reconfigure::data_description::username` | Username for your INDI Allsky user account, if authentication is enabled. | Användarnamn för ditt INDI Allsky-konto, om autentisering är aktiverad. | Core-literal match |
| 984916102 | `component::indi_allsky::config::step::reconfigure::data_description::ssl` | Connect using SSL/HTTPS. | Anslut med SSL/HTTPS. | Core-literal match |
| 984916101 | `component::indi_allsky::config::step::reconfigure::data_description::port` | The port number of your INDI Allsky web server. | Portnumret för din INDI Allsky-webbserver. | Core-literal match |
| 984916100 | `component::indi_allsky::config::step::reconfigure::data_description::password` | Password for your INDI Allsky user account, if authentication is enabled. | Lösenord för ditt INDI Allsky-konto, om autentisering är aktiverad. | Core-literal match |
| 984916099 | `component::indi_allsky::config::step::reconfigure::data_description::host` | The hostname or IP address of your INDI Allsky server. | Värdnamnet eller IP-adressen för din INDI Allsky-server. | Core-literal match |
| 984916098 | `component::indi_allsky::config::step::reconfigure::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 984916097 | `component::indi_allsky::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference target checked |
| 984916096 | `component::indi_allsky::config::step::reconfigure::data::ssl` | Uses an SSL certificate | Använder ett SSL-certifikat | Shared reference target checked |
| 984916095 | `component::indi_allsky::config::step::reconfigure::data::port` | Port | Port | Shared reference target checked |
| 984916094 | `component::indi_allsky::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 984916093 | `component::indi_allsky::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 984916092 | `component::croma_infrared::config::step::reconfigure::title` | Reconfigure Croma IR TV | Konfigurera om Croma IR-TV | Core-literal match |
| 984916091 | `component::croma_infrared::config::step::reconfigure::description` | Change the infrared emitter used to control your Croma TV. | Ändra den infraröda sändare som används för att styra din Croma-TV. | Core-literal match |
| 984916090 | `component::croma_infrared::config::step::reconfigure::data_description::infrared_emitter_entity_id` | The infrared emitter entity to use for sending commands. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Shared reference target checked |
| 984916089 | `component::croma_infrared::config::step::reconfigure::data::infrared_emitter_entity_id` | Infrared emitter | Infraröd sändare | Shared reference target checked |
| 984916051 | `component::smartyplants::config::step::reconfigure_secret::title` | Reconfigure SmartyPlants | Konfigurera om SmartyPlants | Shared reference target checked |
| 984916050 | `component::smartyplants::config::step::reconfigure_secret::description` | Update the API key, or the signing secret used to verify pushed updates. Home Assistant currently has no address reachable from the internet, so the webhook URL cannot be shown. The webhook you already added in the SmartyPlants app is unaffected, and its secret can still be changed here, or cleared to use polling only. | Uppdatera API-nyckeln eller signeringshemligheten som används för att verifiera skickade uppdateringar. Home Assistant har för närvarande ingen adress som kan nås från internet, därför kan webhook-URL:en inte visas. Webhooken som du redan har lagt till i SmartyPlants-appen påverkas inte, och dess hemlighet kan fortfarande ändras här eller tas bort för att endast använda avsökning. | Core-literal match |
| 984916049 | `component::smartyplants::config::step::reconfigure_secret::data_description::webhook_secret` | The signing secret from the SmartyPlants app. Leave it empty to use polling only. | Signeringshemligheten från SmartyPlants-appen. Lämna den tom om du endast vill använda avsökning. | Shared reference target checked |
| 984916048 | `component::smartyplants::config::step::reconfigure_secret::data_description::api_key` | Create this in the SmartyPlants app, under Settings. It identifies your account to Home Assistant. | Skapa API-nyckeln i SmartyPlants-appen under Inställningar. Den identifierar ditt konto för Home Assistant. | Shared reference target checked |
| 984916047 | `component::smartyplants::config::step::reconfigure_secret::data::webhook_secret` | Webhook secret | Webhook-hemlighet | Shared reference target checked |
| 984916046 | `component::smartyplants::config::step::reconfigure_secret::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 984916045 | `component::smartyplants::config::step::reconfigure_key::title` | Reconfigure SmartyPlants | Konfigurera om SmartyPlants | Shared reference target checked |
| 984916044 | `component::smartyplants::config::step::reconfigure_key::description` | Update the API key. This integration was set up without a webhook, so there is no signing secret to change and readings arrive by polling. | Uppdatera API-nyckeln. Integrationen konfigurerades utan en webhook, så det finns ingen signeringshemlighet att ändra och avläsningar hämtas med avsökning. | Core-literal match |
| 984916043 | `component::smartyplants::config::step::reconfigure_key::data_description::api_key` | Create this in the SmartyPlants app, under Settings. It identifies your account to Home Assistant. | Skapa API-nyckeln i SmartyPlants-appen under Inställningar. Den identifierar ditt konto för Home Assistant. | Shared reference target checked |
| 984916042 | `component::smartyplants::config::step::reconfigure_key::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 984916041 | `component::smartyplants::config::step::reconfigure::title` | Reconfigure SmartyPlants | Konfigurera om SmartyPlants | Core-literal match |
| 984916040 | `component::smartyplants::config::step::reconfigure::description` | Update the API key, or the signing secret used to verify pushed updates. The webhook URL is unchanged, so there is nothing to update in the SmartyPlants app.<br><br>`{webhook_url}`<br><br>Leave the secret empty to use polling only. | Uppdatera API-nyckeln eller signeringshemligheten som används för att verifiera skickade uppdateringar. Webhook-URL:en är oförändrad, så det finns inget att uppdatera i SmartyPlants-appen.<br><br>`{webhook_url}`<br><br>Lämna hemligheten tom om du endast vill använda avsökning. | Core-literal match |
| 984916039 | `component::smartyplants::config::step::reconfigure::data_description::webhook_secret` | The signing secret from the SmartyPlants app. Leave it empty to use polling only. | Signeringshemligheten från SmartyPlants-appen. Lämna den tom om du endast vill använda avsökning. | Core-literal match |
| 984916038 | `component::smartyplants::config::step::reconfigure::data_description::api_key` | Create this in the SmartyPlants app, under Settings. It identifies your account to Home Assistant. | Skapa API-nyckeln i SmartyPlants-appen under Inställningar. Den identifierar ditt konto för Home Assistant. | Shared reference target checked |
| 984916037 | `component::smartyplants::config::step::reconfigure::data::webhook_secret` | Webhook secret | Webhook-hemlighet | Shared reference target checked |
| 984916036 | `component::smartyplants::config::step::reconfigure::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 984916035 | `component::aemet::exceptions::invalid_api_key::message` | The AEMET OpenData API key is invalid or has expired | AEMET OpenData API-nyckeln är ogiltig eller har upphört att gälla. | Core-literal match |
| 984916034 | `component::aemet::config::step::reauth_confirm::description` | The AEMET OpenData API key is no longer valid. AEMET API keys expire periodically, so you need to generate a new one at {api_key_url} | AEMET OpenData API-nyckeln är inte längre giltig. AEMET API-nycklar upphör regelbundet att gälla, så du måste generera en ny på {api_key_url}. | Core-literal match |
| 984916033 | `component::aemet::config::step::reauth_confirm::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 984916032 | `component::aemet::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 984916019 | `component::foreca::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 984916018 | `component::foreca::config::step::reauth_confirm::description` | The Foreca API rejected the API key. Enter a new key from the My API page. | Foreca API avvisade API-nyckeln. Ange en ny nyckel från sidan My API. | Core-literal match |
| 984916017 | `component::foreca::config::step::reauth_confirm::data_description::api_key` | Your Foreca Weather API key from the My API page | Din Foreca Weather API-nyckel från sidan My API | Shared reference target checked |
| 984916016 | `component::foreca::config::step::reauth_confirm::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 984913768 | `component::wiim::config::abort::ipv6_not_supported` | IPv6 is not supported. | IPv6 stöds inte. | Core-literal match |
| 984913767 | `component::livisi::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 984913766 | `component::livisi::config::step::reauth_confirm::description` | Enter the new (local) password of the SHC. | Ange SHC:ns nya (lokala) lösenord. | Core-literal match |
| 984913765 | `component::livisi::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 984913764 | `component::ephember::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 984913763 | `component::ephember::config::step::reauth_confirm::description` | The EPH Ember password for {username} was rejected. Enter the password you now use in the EPH Ember app. | EPH Ember-lösenordet för {username} avvisades. Ange lösenordet som du nu använder i EPH Ember-appen. | Core-literal match |
| 984913762 | `component::ephember::config::step::reauth_confirm::data_description::password` | The password you use in the EPH Ember app. | Lösenordet du använder i EPH Ember-appen. | Shared reference target checked |
| 984913761 | `component::ephember::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 984913760 | `component::ephember::config::abort::unique_id_mismatch` | This password belongs to a different EPH Ember account. Log in with the account that was originally set up. | Det här lösenordet tillhör ett annat EPH Ember-konto. Logga in med kontot som ursprungligen konfigurerades. | Core-literal match |
| 984913727 | `component::any_list::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 984913726 | `component::any_list::config::step::reauth_confirm::description` | Enter the password of the AnyList account {email}. | Ange lösenordet för AnyList-kontot {email}. | Core-literal match |
| 984913725 | `component::any_list::config::step::reauth_confirm::data_description::password` | The password used to sign in to your AnyList account. | Lösenordet som används för att logga in på ditt AnyList-konto. | Shared reference target checked |
| 984913724 | `component::any_list::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 984913723 | `component::any_list::config::abort::wrong_account` | You must sign in with the same AnyList account that was originally configured. | Du måste logga in med samma AnyList-konto som ursprungligen konfigurerades. | Core-literal match |
| 984913722 | `component::solyx_energy_cloud::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 984913721 | `component::solyx_energy_cloud::config::step::reauth_confirm::description` | Solyx Energy Cloud rejected the client secret of client ID {client_id}. Enter a new client secret from the Solyx Energy app. | Solyx Energy Cloud avvisade klienthemligheten för klient-id {client_id}. Ange en ny klienthemlighet från Solyx Energy-appen. | Core-literal match |
| 984913720 | `component::solyx_energy_cloud::config::step::reauth_confirm::data_description::nymo_client_secret` | The Client secret that is copied from the Solyx Energy app. | Klienthemligheten som kopieras från Solyx Energy-appen. | Shared reference target checked |
| 984913719 | `component::solyx_energy_cloud::config::step::reauth_confirm::data::nymo_client_secret` | Client secret | Klienthemlighet | Shared reference target checked |
| 984913718 | `component::rainbowminer::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 984913717 | `component::rainbowminer::config::step::reauth_confirm::description` | The RainbowMiner API of {name} rejected the credentials. Enter the API username and password. | RainbowMiner API för {name} avvisade inloggningsuppgifterna. Ange API-användarnamnet och lösenordet. | Core-literal match |
| 984913716 | `component::rainbowminer::config::step::reauth_confirm::data_description::username` | The API username. | API-användarnamnet. | Core-literal match |
| 984913715 | `component::rainbowminer::config::step::reauth_confirm::data_description::password` | The API password. | API-lösenordet. | Core-literal match |
| 984913714 | `component::rainbowminer::config::step::reauth_confirm::data::username` | Username | Användarnamn | Shared reference target checked |
| 984913713 | `component::rainbowminer::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 984913712 | `component::accuweather::config::step::reconfigure::data_description::api_key` | API key generated in the AccuWeather APIs portal. | API-nyckel genererad i AccuWeather APIs portalen. | Shared reference target checked |
| 984913711 | `component::accuweather::config::step::reconfigure::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 984785918 | `component::holiday::options::step::init::data_description::islamic_show_estimated` | Add "estimated" to the name of Islamic holidays with an estimated date | Lägg till ”uppskattad” i namnet på islamiska helgdagar med uppskattat datum | Shared reference target checked |
| 984785917 | `component::holiday::options::step::init::data_description::include_sundays` | Add all Sundays to the holidays of the country | Lägg till alla söndagar bland landets helgdagar | Shared reference target checked |
| 984785916 | `component::holiday::options::step::init::data_description::hindu_show_estimated` | Add "estimated" to the name of Hindu holidays with an estimated date | Lägg till ”uppskattad” i namnet på hinduiska helgdagar med uppskattat datum | Shared reference target checked |
| 984785915 | `component::holiday::options::step::init::data::islamic_show_estimated` | Mark estimated Islamic holidays | Markera uppskattade islamiska helgdagar | Shared reference target checked |
| 984785914 | `component::holiday::options::step::init::data::include_sundays` | Include Sundays as holidays | Inkludera söndagar som helgdagar | Shared reference target checked |
| 984785913 | `component::holiday::options::step::init::data::hindu_show_estimated` | Mark estimated Hindu holidays | Markera uppskattade hinduiska helgdagar | Shared reference target checked |
| 984785912 | `component::holiday::config::step::reconfigure::data_description::islamic_show_estimated` | Add "estimated" to the name of Islamic holidays with an estimated date | Lägg till ”uppskattad” i namnet på islamiska helgdagar med uppskattat datum | Shared reference target checked |
| 984785911 | `component::holiday::config::step::reconfigure::data_description::include_sundays` | Add all Sundays to the holidays of the country | Lägg till alla söndagar bland landets helgdagar | Shared reference target checked |
| 984785910 | `component::holiday::config::step::reconfigure::data_description::hindu_show_estimated` | Add "estimated" to the name of Hindu holidays with an estimated date | Lägg till ”uppskattad” i namnet på hinduiska helgdagar med uppskattat datum | Shared reference target checked |
| 984785909 | `component::holiday::config::step::reconfigure::data::islamic_show_estimated` | Mark estimated Islamic holidays | Markera uppskattade islamiska helgdagar | Shared reference target checked |
| 984785908 | `component::holiday::config::step::reconfigure::data::include_sundays` | Include Sundays as holidays | Inkludera söndagar som helgdagar | Shared reference target checked |
| 984785907 | `component::holiday::config::step::reconfigure::data::hindu_show_estimated` | Mark estimated Hindu holidays | Markera uppskattade hinduiska helgdagar | Shared reference target checked |
| 984785906 | `component::holiday::config::step::options::data_description::islamic_show_estimated` | Add "estimated" to the name of Islamic holidays with an estimated date | Lägg till ”uppskattad” i namnet på islamiska helgdagar med uppskattat datum | Core-literal match |
| 984785905 | `component::holiday::config::step::options::data_description::include_sundays` | Add all Sundays to the holidays of the country | Lägg till alla söndagar bland landets helgdagar | Core-literal match |
| 984785904 | `component::holiday::config::step::options::data_description::hindu_show_estimated` | Add "estimated" to the name of Hindu holidays with an estimated date | Lägg till ”uppskattad” i namnet på hinduiska helgdagar med uppskattat datum | Core-literal match |
| 984785903 | `component::holiday::config::step::options::data::islamic_show_estimated` | Mark estimated Islamic holidays | Markera uppskattade islamiska helgdagar | Core-literal match |
| 984785902 | `component::holiday::config::step::options::data::include_sundays` | Include Sundays as holidays | Inkludera söndagar som helgdagar | Core-literal match |
| 984785901 | `component::holiday::config::step::options::data::hindu_show_estimated` | Mark estimated Hindu holidays | Markera uppskattade hinduiska helgdagar | Core-literal match |
| 984781778 | `component::adguard::services::pause_protection::name` | Pause protection | Pausa skydd | Core-literal match |
| 984781777 | `component::adguard::services::pause_protection::fields::duration::name` | Duration | Varaktighet | Core-literal match |
| 984781776 | `component::adguard::services::pause_protection::fields::duration::description` | How long to pause protection for. | Hur länge skyddet ska pausas. | Core-literal match |
| 984781775 | `component::adguard::services::pause_protection::description` | Pauses protection in AdGuard Home for a duration, after which AdGuard Home enables it again. | Pausar skyddet i AdGuard Home under en tidsperiod, varefter AdGuard Home aktiverar det igen. | Core-literal match |
| 984781729 | `component::velbus::exceptions::invalid_access_token::message` | Invalid access token | Ogiltig åtkomsttoken | Shared reference target checked |
| 984781728 | `component::velbus::config::step::user::menu_options::manager` | Via Velbus Manager | Via Velbus Manager | Core-literal match |
| 984781727 | `component::velbus::config::step::reauth_confirm::title` | Reauthenticate Velbus Manager | Autentisera Velbus Manager igen | Core-literal match |
| 984781726 | `component::velbus::config::step::reauth_confirm::description` | The Velbus Manager rejected the access token. Provide a new token. | Velbus Manager avvisade åtkomsttokenen. Ange en ny token. | Core-literal match |
| 984781725 | `component::velbus::config::step::reauth_confirm::data_description::access_token` | Bearer token when Velbus Manager authentication is enabled. | Bearer-token när autentisering i Velbus Manager är aktiverad. | Core-literal match |
| 984781724 | `component::velbus::config::step::reauth_confirm::data::access_token` | Access token | Åtkomsttoken | Shared reference target checked |
| 984781723 | `component::velbus::config::step::manager::title` | Velbus Manager | Velbus Manager | Core-literal match |
| 984781722 | `component::velbus::config::step::manager::description` | Connect through Velbus Manager REST and WebSocket instead of the Velbus TCP bus. | Anslut via Velbus Manager REST och WebSocket i stället för Velbus TCP-bussen. | Core-literal match |
| 984781721 | `component::velbus::config::step::manager::data_description::port` | Velbus Manager HTTP port (default 4201). | HTTP-port för Velbus Manager (standard är 4201). | Core-literal match |
| 984781720 | `component::velbus::config::step::manager::data_description::host` | Hostname or IP of Velbus Manager (use manager for the Home Assistant app on the same host). | Värdnamn eller IP-adress för Velbus Manager (använd manager för Home Assistant-appen på samma värd). | Core-literal match |
| 984781719 | `component::velbus::config::step::manager::data_description::access_token` | Bearer token when Velbus Manager authentication is enabled. | Bearer-token när autentisering i Velbus Manager är aktiverad. | Core-literal match |
| 984781718 | `component::velbus::config::step::manager::data::port` | Port | Port | Shared reference target checked |
| 984781717 | `component::velbus::config::step::manager::data::host` | Host | Värd | Shared reference target checked |
| 984781716 | `component::velbus::config::step::manager::data::access_token` | Access token | Åtkomsttoken | Shared reference target checked |
| 984781715 | `component::velbus::config::error::invalid_access_token` | Invalid access token | Ogiltig åtkomsttoken | Shared reference target checked |
| 984767848 | `component::shelly::entity::update::release_notes_messages::do_not_unplug` | Do not unplug or power off the device during the update. | Koppla inte ur eller stäng av enheten under uppdateringen. | Core-literal match |
| 984763784 | `component::fritz::entity::update::release_notes_messages::internet_interruption` | If this FRITZ!Box is your main internet router, your internet connection will be interrupted during the update. Depending on the model and the connection type, this can take up to 10 minutes. | Om denna FRITZ!Box är din huvudsakliga internetrouter avbryts internetanslutningen under uppdateringen. Beroende på modell och anslutningstyp kan det ta upp till 10 minuter. | Core-literal match |
| 984730791 | `component::irm_kmi::services::get_forecasts_radar::name` | Get radar forecasts | Hämta radarprognoser | Core-literal match |
| 984730790 | `component::irm_kmi::services::get_forecasts_radar::fields::include_past_forecasts::name` | Include past forecasts | Inkludera tidigare prognoser | Core-literal match |
| 984730789 | `component::irm_kmi::services::get_forecasts_radar::fields::include_past_forecasts::description` | Whether to also return past radar frames. The current frame is always returned. | Anger om tidigare radarbildrutor också ska returneras. Den aktuella bildrutan returneras alltid. | Core-literal match |
| 984730788 | `component::irm_kmi::services::get_forecasts_radar::description` | Retrieves the available rain radar forecast. | Hämtar tillgänglig regnradarprognos. | Core-literal match |
| 984730787 | `component::irm_kmi::exceptions::no_radar_forecast::message` | The rain radar reported no forecast for this location. | Regnradarn rapporterade ingen prognos för den här platsen. | Core-literal match |
| 984730779 | `component::seafile::issues::library_deleted::title` | Seafile library "{name}" not found | Seafile-biblioteket ”{name}” hittades inte | Core-literal match |
| 984730778 | `component::seafile::issues::library_deleted::fix_flow::step::confirm::title` | Seafile library "{name}" not found | Seafile-biblioteket ”{name}” hittades inte | Shared reference target checked |
| 984730777 | `component::seafile::issues::library_deleted::fix_flow::step::confirm::description` | The library "{name}" no longer exists on the Seafile server, or this account no longer has access to it. Its entities are unavailable and it can no longer be used as a backup location.<br><br>Select **Submit** to remove the library and its device from Home Assistant. If the library comes back, for example because it was shared again, this issue is resolved automatically. | Biblioteket ”{name}” finns inte längre på Seafile-servern eller så har det här kontot inte längre åtkomst till det. Dess entiteter är inte tillgängliga och det kan inte längre användas som säkerhetskopieringsplats.<br><br>Välj **Skicka** för att ta bort biblioteket och dess enhet från Home Assistant. Om biblioteket kommer tillbaka, till exempel för att det delas igen, löses problemet automatiskt. | Core-literal match |
| 984730699 | `component::jellyfin::exceptions::update_failed::message` | Error communicating with the Jellyfin server: {error} | Fel vid kommunikation med Jellyfin-servern: {error} | Core-literal match |
| 984730698 | `component::jellyfin::exceptions::server_unreachable::message` | Unable to reach the Jellyfin server | Det gick inte att nå Jellyfin-servern | Core-literal match |
| 984730571 | `component::bluetti_modbus::exceptions::battery_firmware_unreadable::message` | The firmware version of the built-in battery could not be read from the BLUETTI power station. | Det gick inte att läsa inbyggda batteriets inbyggda programvaruversion från BLUETTI-kraftstationen. | Core-literal match |
| 984730570 | `component::bluetti_modbus::entity::sensor::total_discharged_energy::name` | Total discharged energy | Total urladdad energi | Core-literal match |
| 984730569 | `component::bluetti_modbus::entity::sensor::total_charged_energy::name` | Total charged energy | Total laddad energi | Core-literal match |
| 984730568 | `component::bluetti_modbus::entity::sensor::soh::name` | SoH | SoH | Core-literal match |
| 984730567 | `component::bluetti_modbus::entity::sensor::soc::name` | SoC | SoC | Core-literal match |
| 984730566 | `component::bluetti_modbus::entity::sensor::cycle_count::name` | Cycle count | Antal cykler | Core-literal match |
| 984730565 | `component::bluetti_modbus::device::built_in_battery::name` | Built-in battery | Inbyggt batteri | Core-literal match |
| 984730564 | `component::webdav::services::upload::name` | Upload files | Överför filer | Core-literal match |
| 984730563 | `component::webdav::services::upload::fields::filename::name` | Filenames | Filnamn | Core-literal match |
| 984730562 | `component::webdav::services::upload::fields::filename::example` | {example_image_path} | {example_image_path} | Core-literal match |
| 984730561 | `component::webdav::services::upload::fields::filename::description` | One or more paths to files to upload. Supports wildcards, for example `/config/www/*.jpg` to upload all JPG files in a folder, or `/config/www/**/*.jpg` to also include subfolders. Subfolders matched by a wildcard are recreated inside the destination folder. The characters `*`, `?` and `[` are treated as wildcards; to upload a file whose name contains one of these characters literally, make sure the file exists under that exact name. | En eller flera sökvägar till filer som ska överföras. Jokertecken stöds, till exempel `/config/www/*.jpg` för att överföra alla JPG-filer i en mapp eller `/config/www/**/*.jpg` för att även inkludera undermappar. Undermappar som matchas av ett jokertecken återskapas i målmappen. Tecknen `*`, `?` och `[` behandlas som jokertecken. Om du vill överföra en fil vars namn bokstavligen innehåller något av dessa tecken måste filen finnas under exakt det namnet. | Core-literal match |
| 984730560 | `component::webdav::services::upload::fields::destination_folder::name` | Destination folder | Målmapp | Core-literal match |
| 984730559 | `component::webdav::services::upload::fields::destination_folder::example` | photos/snapshots | foton/ögonblicksbilder | Core-literal match |
| 984730558 | `component::webdav::services::upload::fields::destination_folder::description` | Folder on the WebDAV server, relative to the configured URL, you want to upload the files to. Will be created if it does not exist. | Mapp på WebDAV-servern, relativt den konfigurerade URL:en, som du vill överföra till. | Core-literal match |
| 984730557 | `component::webdav::services::upload::fields::config_entry_id::name` | Config entry ID | Konfigurationspost-id | Core-literal match |
| 984730556 | `component::webdav::services::upload::fields::config_entry_id::description` | The config entry representing the WebDAV server you want to upload to. | Konfigurationsposten som representerar WebDAV-servern som du vill överföra till. | Core-literal match |
| 984730555 | `component::webdav::services::upload::description` | Uploads one or more files to a WebDAV server. | Överför en eller flera filer till en WebDAV-server. | Core-literal match |
| 984730554 | `component::webdav::exceptions::upload_error::message` | Failed to upload to WebDAV server: {message} | Det gick inte att överföra till WebDAV-servern: {message} | Core-literal match |
| 984730553 | `component::webdav::exceptions::no_files_match_pattern::message` | No files match the following patterns: {patterns} | Inga filer matchar följande mönster: {patterns} | Core-literal match |
| 984730552 | `component::webdav::exceptions::no_access_to_path::message` | Cannot read {filename}, no access to path; `allowlist_external_dirs` may need to be adjusted in `configuration.yaml` | Det går inte att läsa {filename}; saknar åtkomst till sökvägen. `allowlist_external_dirs` kan behöva justeras i `configuration.yaml`. | Core-literal match |
| 984730551 | `component::webdav::exceptions::invalid_destination_path::message` | Invalid destination path `{destination_path}` | Ogiltig målsökväg `{destination_path}` | Core-literal match |
| 984730550 | `component::webdav::exceptions::filenames_do_not_exist::message` | The following files do not exist: {filenames} | Följande filer finns inte: {filenames} | Core-literal match |
| 984730549 | `component::webdav::exceptions::duplicate_destination_path::message` | Multiple files would be uploaded to the same destination: {paths} | Flera filer skulle överföras till samma mål: {paths} | Core-literal match |
| 984730548 | `component::webdav::exceptions::create_folder_error::message` | Failed to create folder on WebDAV server: {message} | Det gick inte att skapa mapp på WebDAV-servern: {message} | Core-literal match |
| 984730544 | `component::bosch_smart_camera::exceptions::privacy_mode_failed::message` | Unable to change the privacy mode at Bosch. | Det gick inte att ändra integritetsläget hos Bosch. | Core-literal match |
| 984730543 | `component::bosch_smart_camera::entity::switch::privacy_mode::name` | Privacy mode | Integritetsläge | Core-literal match |
| 984730534 | `component::nobo_hub::device::zone::name` | Heating | Uppvärmning | Core-literal match |
| 984730533 | `component::foreca::services::get_minute_forecast::name` | Get minute forecast | Hämta minutprognos | Core-literal match |
| 984730532 | `component::foreca::services::get_minute_forecast::description` | Retrieves the precipitation rate for each minute of the next hour, in the weather entity's precipitation unit per hour. Every call makes a request to the Foreca Weather API and counts toward the daily limit of your plan. | Hämtar nederbördshastigheten för varje minut under nästa timme, i väderentitetens nederbördsenhet per timme. Varje anrop gör en förfrågan till Foreca Weather API och räknas mot den dagliga gränsen för din plan. | Core-literal match |
| 984730531 | `component::foreca::exceptions::minute_forecast_error::message` | Error fetching the minute forecast. | Fel vid hämtning av minutprognosen. | Core-literal match |
| 984730530 | `component::abrp::services::send_telemetry::name` | Send telemetry | Skicka telemetri | Core-literal match |
| 984730529 | `component::abrp::services::send_telemetry::fields::vehicle::name` | Vehicle | Fordon | Core-literal match |
| 984730528 | `component::abrp::services::send_telemetry::fields::vehicle::description` | The A Better Routeplanner vehicle to send the telemetry for. | A Better Routeplanner-fordonet som telemetrin ska skickas för. | Core-literal match |
| 984730527 | `component::abrp::services::send_telemetry::fields::time::name` | Time | Tid | Core-literal match |
| 984730526 | `component::abrp::services::send_telemetry::fields::time::description` | When the values were measured. Defaults to now. | När värdena mättes. Standard är nu. | Core-literal match |
| 984730525 | `component::abrp::services::send_telemetry::fields::soc::name` | State of charge | Laddningsnivå | Core-literal match |
| 984730524 | `component::abrp::services::send_telemetry::fields::soc::description` | Battery state of charge, in %. | Batteriets laddningsnivå i %. | Core-literal match |
| 984730523 | `component::abrp::services::send_telemetry::fields::power::name` | Power | Effekt | Core-literal match |
| 984730522 | `component::abrp::services::send_telemetry::fields::power::description` | Battery power, in kW. Negative while charging, positive while driving. | Batterieffekt i kW. Negativ vid laddning, positiv under körning. | Core-literal match |
| 984730521 | `component::abrp::services::send_telemetry::fields::odometer::name` | Odometer | Vägmätarställning | Core-literal match |
| 984730520 | `component::abrp::services::send_telemetry::fields::odometer::description` | Odometer reading, in km. | Vägmätarställning i km. | Core-literal match |
| 984730519 | `component::abrp::services::send_telemetry::fields::location::name` | Location | Plats | Core-literal match |
| 984730518 | `component::abrp::services::send_telemetry::fields::location::description` | Position of the vehicle. | Fordonets position. | Core-literal match |
| 984730517 | `component::abrp::services::send_telemetry::fields::estimated_range::name` | Estimated range | Beräknad räckvidd | Core-literal match |
| 984730516 | `component::abrp::services::send_telemetry::fields::estimated_range::description` | Remaining range estimated by the vehicle, in km. | Återstående räckvidd som beräknas av fordonet, i km. | Core-literal match |
| 984730515 | `component::abrp::services::send_telemetry::fields::charging_state::name` | Charging state | Laddningsstatus | Core-literal match |
| 984730514 | `component::abrp::services::send_telemetry::fields::charging_state::description` | Whether the vehicle is plugged in or charging. | Om fordonet är anslutet eller laddar. | Core-literal match |
| 984730513 | `component::abrp::services::send_telemetry::fields::battery_temperature::name` | Battery temperature | Batteritemperatur | Core-literal match |
| 984730512 | `component::abrp::services::send_telemetry::fields::battery_temperature::description` | Battery temperature, in °C. | Batteritemperatur i °C. | Core-literal match |
| 984730511 | `component::abrp::services::send_telemetry::description` | Sends a telemetry point for a vehicle to A Better Routeplanner, for example the state of charge reported by another integration. | Skickar en telemetripunkt för ett fordon till A Better Routeplanner, till exempel laddningsnivån som rapporteras av en annan integration. | Core-literal match |
| 984730510 | `component::abrp::selector::charging_state::options::plugged_in` | Plugged in | Ansluten | Shared reference target checked |
| 984730509 | `component::abrp::selector::charging_state::options::not_charging` | Not charging | Laddar inte | Shared reference target checked |
| 984730508 | `component::abrp::selector::charging_state::options::charging_unknown` | Charging | Laddar | Shared reference target checked |
| 984730507 | `component::abrp::selector::charging_state::options::charging_dc` | Charging (DC) | Laddar (DC) | Shared reference target checked |
| 984730506 | `component::abrp::selector::charging_state::options::charging_ac` | Charging (AC) | Laddar (AC) | Shared reference target checked |
| 984730505 | `component::abrp::exceptions::vehicle_not_in_garage::message` | {vehicle} is not in the A Better Routeplanner garage of this account. | {vehicle} finns inte i A Better Routeplanner-garaget för det här kontot. | Core-literal match |
| 984730504 | `component::abrp::exceptions::telemetry_write_not_granted::message` | Home Assistant is not allowed to send telemetry to A Better Routeplanner yet; please re-authenticate to grant it. | Home Assistant har ännu inte behörighet att skicka telemetri till A Better Routeplanner. Autentisera igen för att ge behörighet. | Core-literal match |
| 984730503 | `component::abrp::exceptions::send_telemetry_failed::message` | Failed to send telemetry to A Better Routeplanner. | Det gick inte att skicka telemetri till A Better Routeplanner. | Core-literal match |
| 984730486 | `component::smhi::exceptions::radar_update_failed::message` | Failed to retrieve the radar from the SMHI API | Det gick inte att hämta radar från SMHI API | Core-literal match |
| 984730485 | `component::smhi::exceptions::radar_image_failed::message` | Failed to retrieve the radar image from the SMHI API | Det gick inte att hämta radarbilden från SMHI API | Core-literal match |
| 984730484 | `component::smhi::entity::sensor::radar_reflectivity::name` | Radar reflectivity | Radarreflektivitet | Core-literal match |
| 984730483 | `component::smhi::entity::sensor::radar_precipitation_intensity::name` | Radar precipitation intensity | Radarns nederbördsintensitet | Core-literal match |
| 984730482 | `component::smhi::entity::image::radar::name` | Radar | Radar | Core-literal match |
| 984730429 | `component::foreca::entity::sensor::observed_wind_speed::name` | Observed wind speed | Observerad vindhastighet | Core-literal match |
| 984730428 | `component::foreca::entity::sensor::observed_wind_gust_speed::name` | Observed wind gust speed | Observerad vindbyhastighet | Core-literal match |
| 984730427 | `component::foreca::entity::sensor::observed_wind_direction::name` | Observed wind direction | Observerad vindriktning | Core-literal match |
| 984730426 | `component::foreca::entity::sensor::observed_visibility::name` | Observed visibility | Observerad sikt | Core-literal match |
| 984730425 | `component::foreca::entity::sensor::observed_temperature::name` | Observed temperature | Observerad temperatur | Core-literal match |
| 984730424 | `component::foreca::entity::sensor::observed_snow_depth::name` | Observed snow depth | Observerat snödjup | Core-literal match |
| 984730423 | `component::foreca::entity::sensor::observed_pressure::name` | Observed pressure | Observerat lufttryck | Core-literal match |
| 984730422 | `component::foreca::entity::sensor::observed_humidity::name` | Observed humidity | Observerad luftfuktighet | Core-literal match |
| 984730421 | `component::foreca::entity::sensor::observed_condition::state::sunny` | Sunny | Soligt | Shared reference target checked |
| 984730420 | `component::foreca::entity::sensor::observed_condition::state::snowy-rainy` | Snowy, rainy | Snöblandat regn | Shared reference target checked |
| 984730419 | `component::foreca::entity::sensor::observed_condition::state::snowy` | Snowy | Snö | Shared reference target checked |
| 984730418 | `component::foreca::entity::sensor::observed_condition::state::rainy` | Rainy | Regn | Shared reference target checked |
| 984730417 | `component::foreca::entity::sensor::observed_condition::state::pouring` | Pouring | Ösregn | Shared reference target checked |
| 984730416 | `component::foreca::entity::sensor::observed_condition::state::partlycloudy` | Partly cloudy | Växlande molnighet | Shared reference target checked |
| 984730415 | `component::foreca::entity::sensor::observed_condition::state::lightning-rainy` | Lightning, rainy | Åska och regn | Shared reference target checked |
| 984730414 | `component::foreca::entity::sensor::observed_condition::state::fog` | Fog | Dimma | Shared reference target checked |
| 984730413 | `component::foreca::entity::sensor::observed_condition::state::cloudy` | Cloudy | Molnigt | Shared reference target checked |
| 984730412 | `component::foreca::entity::sensor::observed_condition::state::clear-night` | Clear, night | Klart, natt | Shared reference target checked |
| 984730411 | `component::foreca::entity::sensor::observed_condition::name` | Observed condition | Observerat väder | Core-literal match |
| 984730410 | `component::foreca::entity::sensor::observed_apparent_temperature::name` | Observed apparent temperature | Observerad känslotemperatur | Core-literal match |
| 984730409 | `component::foreca::entity::sensor::observation_time::name` | Observation time | Observationstid | Core-literal match |
| 984730408 | `component::foreca::entity::sensor::observation_station::name` | Observation station | Observationsstation | Core-literal match |
| 984730405 | `component::knx::selector::tunneling_type::options::tunneling_tcp_secure` | Secure Tunneling (TCP) | Säker tunnling (TCP) | Core-literal match |
| 984730404 | `component::knx::selector::tunneling_type::options::tunneling_tcp` | TCP (Tunneling v2) | TCP (tunnling v2) | Core-literal match |
| 984730403 | `component::knx::selector::tunneling_type::options::tunneling` | UDP (Tunneling v1) | UDP (tunnling v1) | Core-literal match |
| 984730402 | `component::knx::selector::secure_key_source::options::manual` | Configure IP Secure credentials manually | Konfigurera IP Secure-autentiseringsuppgifter manuellt | Core-literal match |
| 984730401 | `component::knx::selector::secure_key_source::options::knxkeys_upload` | Import a `.knxkeys` file providing IP Secure keys | Importera en `.knxkeys`-fil som tillhandahåller IP Secure-nycklar | Core-literal match |
| 984730400 | `component::knx::selector::secure_key_source::options::knxkeys_existing` | Use the currently imported `.knxkeys` file | Använd den för närvarande importerade `.knxkeys`-filen | Core-literal match |
| 984730399 | `component::knx::selector::connection_type::options::tunneling` | Tunneling | Tunnling | Core-literal match |
| 984730398 | `component::knx::selector::connection_type::options::routing` | Routing | Routing | Core-literal match |
| 984730397 | `component::knx::selector::connection_type::options::automatic` | Automatic | Automatisk | Core-literal match |
| 984730396 | `component::knx::config::step::secure_tunnel::title` | Secure tunneling | Säker tunnling | Core-literal match |
| 984730395 | `component::knx::config::step::secure_tunnel::description` | Please enter your IP Secure information.<br><br>Keys for KNX Data Secure can be added later with 'Import KNX keyring file' in the connection settings. | Ange din IP Secure-information.<br><br>Nycklar för KNX Data Secure kan läggas till senare med ”Importera KNX-nyckelringsfil” i anslutningsinställningarna. | Core-literal match |
| 984730394 | `component::knx::config::step::secure_tunnel::data_description::user_password` | Password for the specific tunnel connection set in the 'Properties' panel of the tunnel in ETS. | Lösenord för den aktuella tunnelanslutningen, angett på panelen Properties för tunneln i ETS. | Core-literal match |
| 984730393 | `component::knx::config::step::secure_tunnel::data_description::user_id` | This usually is tunnel number +1. So first tunnel in the list presented in ETS would have User-ID `2`. | Detta är vanligtvis tunnelnummer +1. Den första tunneln i listan som visas i ETS har alltså användar-ID `2`. | Core-literal match |
| 984730392 | `component::knx::config::step::secure_tunnel::data_description::knxkeys_password` | The password to open the `.knxkeys` file was set when exporting. | Lösenordet för att öppna filen `.knxkeys` angavs vid export. | Shared reference target checked |
| 984730391 | `component::knx::config::step::secure_tunnel::data_description::knxkeys_file` | Select a `.knxkeys` file. This can be exported from ETS. | Välj en `.knxkeys`-fil. Detta kan exporteras från ETS. | Shared reference target checked |
| 984730390 | `component::knx::config::step::secure_tunnel::data_description::key_source` | Select where the KNX IP Secure keys should be taken from. | Välj varifrån KNX IP Secure-nycklarna ska hämtas. | Core-literal match |
| 984730389 | `component::knx::config::step::secure_tunnel::data_description::device_authentication` | This is set in the 'IP' panel of the interface in ETS. | Detta ställs in på panelen IP i ETS-gränssnittet. | Core-literal match |
| 984730388 | `component::knx::config::step::secure_tunnel::data::user_password` | User password | Användarlösenord | Core-literal match |
| 984730387 | `component::knx::config::step::secure_tunnel::data::user_id` | User ID | Användar-ID | Core-literal match |
| 984730386 | `component::knx::config::step::secure_tunnel::data::knxkeys_password` | Keyring password | Nyckelringslösenord | Shared reference target checked |
| 984730385 | `component::knx::config::step::secure_tunnel::data::knxkeys_file` | Keyring file | Nyckelringsfil | Shared reference target checked |
| 984730384 | `component::knx::config::step::secure_tunnel::data::key_source` | Key source | Nyckelkälla | Core-literal match |
| 984730383 | `component::knx::config::step::secure_tunnel::data::device_authentication` | Device authentication password | Enhetsautentiseringslösenord | Core-literal match |
| 984730382 | `component::knx::config::step::secure_routing::title` | Secure routing | Säker routing | Core-literal match |
| 984730381 | `component::knx::config::step::secure_routing::description` | Please enter your IP Secure information.<br><br>Keys for KNX Data Secure can be added later with 'Import KNX keyring file' in the connection settings. | Ange din IP Secure-information.<br><br>Nycklar för KNX Data Secure kan läggas till senare med ”Importera KNX-nyckelringsfil” i anslutningsinställningarna. | Shared reference target checked |
| 984730380 | `component::knx::config::step::secure_routing::data_description::sync_latency_tolerance` | Should be equal to the backbone configuration of your ETS project. Default is `1000` | Ska motsvara stamnätskonfigurationen för ETS-projektet. Standardvärdet är `1000`. | Core-literal match |
| 984730379 | `component::knx::config::step::secure_routing::data_description::knxkeys_password` | The password to open the `.knxkeys` file was set when exporting. | Lösenordet för att öppna filen `.knxkeys` angavs vid export. | Shared reference target checked |
| 984730378 | `component::knx::config::step::secure_routing::data_description::knxkeys_file` | Select a `.knxkeys` file. This can be exported from ETS. | Välj en `.knxkeys`-fil. Detta kan exporteras från ETS. | Shared reference target checked |
| 984730377 | `component::knx::config::step::secure_routing::data_description::key_source` | Select where the KNX IP Secure keys should be taken from. | Välj varifrån KNX IP Secure-nycklarna ska hämtas. | Shared reference target checked |
| 984730376 | `component::knx::config::step::secure_routing::data_description::backbone_key` | Can be seen in the 'Security' report of your ETS project. Eg. `00112233445566778899AABBCCDDEEFF` | Finns i rapporten Security i ETS-projektet, till exempel `00112233445566778899AABBCCDDEEFF`. | Core-literal match |
| 984730375 | `component::knx::config::step::secure_routing::data::sync_latency_tolerance` | Network latency tolerance | Tolerans för nätverksfördröjning | Core-literal match |
| 984730374 | `component::knx::config::step::secure_routing::data::knxkeys_password` | Keyring password | Nyckelringslösenord | Shared reference target checked |
| 984730373 | `component::knx::config::step::secure_routing::data::knxkeys_file` | Keyring file | Nyckelringsfil | Shared reference target checked |
| 984730372 | `component::knx::config::step::secure_routing::data::key_source` | Key source | Nyckelkälla | Shared reference target checked |
| 984730371 | `component::knx::config::step::secure_routing::data::backbone_key` | Backbone key | Stamnätsnyckel | Core-literal match |
| 984730370 | `component::knx::config::step::reconfigure::description` | Current connection: `{current_connection}`<br><br>Imported keyring: {keyring_project}<br>KNX Data Secure group addresses: {data_secure_count} | Aktuell anslutning: `{current_connection}`<br><br>Importerad nyckelring: {keyring_project}<br>KNX Data Secure-gruppadresser: {data_secure_count} | Core-literal match |
| 984730325 | `component::nibe_heatpump::options::step::log_set_unavailable::title` | LOG.SET for MODBUS40 | LOG.SET för MODBUS40 | Core-literal match |
| 984730324 | `component::nibe_heatpump::options::step::log_set_unavailable::description` | A LOG.SET file selects the registers the pump sends without being asked. It can only be created while the integration is loaded. | En LOG.SET-fil väljer de register som värmepumpen skickar utan att tillfrågas. Den kan bara skapas medan integrationen är inläst. | Core-literal match |
| 984730323 | `component::nibe_heatpump::options::step::log_set::title` | LOG.SET for MODBUS40 | LOG.SET för MODBUS40 | Core-literal match |
| 984730322 | `component::nibe_heatpump::options::step::log_set::description` | A LOG.SET file selects the registers the pump sends without being asked. Download {link} and load it from a USB stick on the pump.<br><br>The pump only sends the first 20 slots, where 32-bit registers take two. Read-only registers are placed first, and the remaining registers are polled. | En LOG.SET-fil väljer de register som värmepumpen skickar utan att tillfrågas. Hämta {link} och läs in den från ett USB-minne i värmepumpen.<br><br>Värmepumpen skickar endast de första 20 platserna, där 32-bitarsregister tar två. Skrivskyddade register placeras först och återstående register avläses. | Core-literal match |
| 984730321 | `component::nibe_heatpump::entity::image::heating_curve::name` | Heating curve {system} | Värmekurva {system} | Core-literal match |
| 984730272 | `component::kaco_modbus::device::mppt::name` | MPPT {number} | MPPT {number} | Core-literal match |
| 984729485 | `component::tomorrowio::services::get_minute_forecast::name` | Get minute forecast | Hämta minutprognos | Core-literal match |
| 984729484 | `component::tomorrowio::services::get_minute_forecast::description` | Retrieves the minute-level forecast (nowcast) for a location, in intervals of the length configured for that location. The data comes from the latest scheduled update, so this action does not use any API requests. Precipitation is the amount expected in each interval, in the weather entity's precipitation unit. | Hämtar minutprognosen (nowcast) för en plats i intervall med den längd som har konfigurerats för platsen. Uppgifterna kommer från den senaste schemalagda uppdateringen, så åtgärden använder inga API-anrop. Nederbörden är den förväntade mängden för varje intervall, i väderentitetens nederbördsenhet. | Core-literal match |
| 984729349 | `component::unifiprotect::entity::event::alarm_hub_input::state_attributes::event_type::state::tamper` | Tampered | Manipulerad | Shared reference target checked |
| 984729348 | `component::unifiprotect::entity::event::alarm_hub_input::state_attributes::event_type::state::smoke` | Smoke | Rök | Shared reference target checked |
| 984729347 | `component::unifiprotect::entity::event::alarm_hub_input::state_attributes::event_type::state::motion` | Motion | Rörelse | Shared reference target checked |
| 984729346 | `component::unifiprotect::entity::event::alarm_hub_input::state_attributes::event_type::state::glass_break` | Glass break | Glaskross | Shared reference target checked |
| 984729345 | `component::unifiprotect::entity::event::alarm_hub_input::state_attributes::event_type::state::entry_opened` | Entry opened | Ingång öppnad | Shared reference target checked |
| 984729344 | `component::unifiprotect::entity::event::alarm_hub_input::state_attributes::event_type::state::entry_closed` | Entry closed | Ingång stängd | Shared reference target checked |
| 984729343 | `component::unifiprotect::entity::event::alarm_hub_input::state_attributes::event_type::state::button_press` | Button pressed | Knapp nedtryckt | Shared reference target checked |
| 984729342 | `component::unifiprotect::entity::event::alarm_hub_input::name` | Input {input} | Ingång {input} | Core-literal match |
| 984729341 | `component::unifiprotect::entity::event::alarm_hub::state_attributes::event_type::state::tamper` | Tampered | Manipulerad | Core-literal match |
| 984729340 | `component::unifiprotect::entity::event::alarm_hub::state_attributes::event_type::state::smoke` | Smoke | Rök | Shared reference target checked |
| 984729339 | `component::unifiprotect::entity::event::alarm_hub::state_attributes::event_type::state::relay_switched` | Relay switched | Relä omkopplat | Core-literal match |
| 984729338 | `component::unifiprotect::entity::event::alarm_hub::state_attributes::event_type::state::motion` | Motion | Rörelse | Shared reference target checked |
| 984729337 | `component::unifiprotect::entity::event::alarm_hub::state_attributes::event_type::state::glass_break` | Glass break | Glaskross | Shared reference target checked |
| 984729336 | `component::unifiprotect::entity::event::alarm_hub::state_attributes::event_type::state::entry_opened` | Entry opened | Ingång öppnad | Core-literal match |
| 984729335 | `component::unifiprotect::entity::event::alarm_hub::state_attributes::event_type::state::entry_closed` | Entry closed | Ingång stängd | Core-literal match |
| 984729334 | `component::unifiprotect::entity::event::alarm_hub::state_attributes::event_type::state::device_tamper` | Hub tampered | Hubben har manipulerats | Core-literal match |
| 984729333 | `component::unifiprotect::entity::event::alarm_hub::state_attributes::event_type::state::button_press` | Button pressed | Knapp nedtryckt | Core-literal match |
| 984729332 | `component::unifiprotect::entity::event::alarm_hub::state_attributes::event_type::state::battery_low` | Battery low | Låg batterinivå | Shared reference target checked |
| 984729331 | `component::unifiprotect::entity::event::alarm_hub::state_attributes::event_type::state::battery_connected` | Battery connected | Batteri anslutet | Core-literal match |
| 984729327 | `component::husqvarna_automower_ble::exceptions::reconnect_failed::message` | Unable to reconnect to device {address} | Det gick inte att återansluta till enheten {address} | Core-literal match |
| 984728342 | `component::fronius::entity::sensor::battery_power_limit_reference::name` | Battery power limit reference | Referens för batterieffektgräns | Core-literal match |
| 984728341 | `component::fronius::entity::sensor::ac_power_limit_reference::name` | AC power limit reference | Referens för AC-effektgräns | Core-literal match |
| 984723662 | `component::rainforest_eagle::entity::binary_sensor::meter_connectivity::name` | Meter connectivity | Mätaranslutning | Core-literal match |
| 984722073 | `component::enphase_envoy::entity::sensor::generator_warm_up_mins::name` | Warm-up time | Uppvärmningstid | Core-literal match |
| 984722072 | `component::enphase_envoy::entity::sensor::generator_stop_soc::name` | Stop battery level | Stoppbatterinivå | Core-literal match |
| 984722071 | `component::enphase_envoy::entity::sensor::generator_start_soc::name` | Start battery level | Startbatterinivå | Core-literal match |
| 984722070 | `component::enphase_envoy::entity::sensor::generator_start_method::name` | Start method | Startmetod | Core-literal match |
| 984722069 | `component::enphase_envoy::entity::sensor::generator_requested_mode::name` | Requested mode | Begärt läge | Core-literal match |
| 984722068 | `component::enphase_envoy::entity::sensor::generator_oper_state::name` | Operating state | Driftstatus | Core-literal match |
| 984722067 | `component::enphase_envoy::entity::sensor::generator_nameplate_rating::name` | Nameplate rating | Märkskyltens märkdata | Core-literal match |
| 984722066 | `component::enphase_envoy::entity::sensor::generator_max_continuous_current::name` | Maximum continuous current | Högsta kontinuerliga ström | Core-literal match |
| 984722065 | `component::enphase_envoy::entity::sensor::generator_gen_type::name` | Generator type | Generatortyp | Core-literal match |
| 984722064 | `component::enphase_envoy::entity::sensor::generator_cool_down_mins::name` | Cool-down time | Avsvalningstid | Core-literal match |
| 984722063 | `component::enphase_envoy::entity::sensor::generator_admin_state::name` | Admin state | Administratörsstatus | Shared reference target checked |
| 984722062 | `component::enphase_envoy::entity::binary_sensor::generator_schedule_enabled::name` | Schedule enabled | Schema aktiverat | Core-literal match |
| 984722061 | `component::enphase_envoy::entity::binary_sensor::generator_present::name` | Present | Närvarande | Core-literal match |
| 984722057 | `component::libresync::exceptions::unsupported_hub::message` | The hub at {host} is built on Libre's newer {module} module, which this integration does not support yet. | Hubben på {host} bygger på Libres nyare {module}-modul, som den här integrationen ännu inte stöder. | Core-literal match |
| 984722056 | `component::libresync::config::abort::unsupported_hub` | This hub is built on Libre's newer {module} module, like the Stereo Hub HT and the Surround Hub, which this integration does not support yet. | Den här hubben bygger på Libres nyare {module}-modul, såsom Stereo Hub HT och Surround Hub, som den här integrationen ännu inte stöder. | Core-literal match |
| 984722043 | `component::victron_gx::entity::switch::system_pv_disable::name` | Disable all PV | Inaktivera all PV | Core-literal match |
| 984722042 | `component::victron_gx::entity::switch::hub4_pv_disable::name` | Disable PV inverters | Inaktivera PV-växelriktare | Core-literal match |
| 984722041 | `component::victron_gx::entity::switch::acsystem_pv_disable::name` | Disable PV | Inaktivera PV | Core-literal match |
| 984722040 | `component::victron_gx::entity::sensor::vebus_nominal_inverter_power_phase::name` | Nominal inverter power {phase} | Nominell växelriktareffekt {phase} | Core-literal match |
| 984722039 | `component::victron_gx::entity::sensor::vebus_nominal_inverter_power::name` | Nominal inverter power | Nominell växelriktareffekt | Core-literal match |
| 984722038 | `component::victron_gx::entity::sensor::vebus_microgrid_operation::state::standard` | Standard operation | Standarddrift | Shared reference target checked |
| 984722037 | `component::victron_gx::entity::sensor::vebus_microgrid_operation::state::microgrid` | Microgrid operation | Mikronätsdrift | Shared reference target checked |
| 984722036 | `component::victron_gx::entity::sensor::vebus_microgrid_operation::name` | Microgrid operation | Mikronätsdrift | Shared reference target checked |
| 984722035 | `component::victron_gx::entity::sensor::vebus_microgrid_droop_q_ref::name` | Microgrid droop reactive power reference | Referens för reaktiv effekt vid droop-reglering i mikronät | Core-literal match |
| 984722034 | `component::victron_gx::entity::sensor::vebus_microgrid_droop_p_ref::name` | Microgrid droop active power reference | Referens för aktiv effekt vid droop-reglering i mikronät | Core-literal match |
| 984722033 | `component::victron_gx::entity::sensor::vebus_microgrid_direct_drive_q_ref::name` | Microgrid grid-following reactive power reference | Referens för reaktiv effekt vid nätdrift i mikronät | Core-literal match |
| 984722032 | `component::victron_gx::entity::sensor::vebus_microgrid_direct_drive_p_ref::name` | Microgrid grid-following active power reference | Referens för aktiv effekt vid nätdrift i mikronät | Core-literal match |
| 984722031 | `component::victron_gx::entity::sensor::vebus_inverter_led_temperature::state::on` | On | På | Shared reference target checked |
| 984722030 | `component::victron_gx::entity::sensor::vebus_inverter_led_temperature::state::off` | Off | Av | Shared reference target checked |
| 984722029 | `component::victron_gx::entity::sensor::vebus_inverter_led_temperature::state::blinking_inverted` | Blinking inverted | Blinkar inverterat | Shared reference target checked |
| 984722028 | `component::victron_gx::entity::sensor::vebus_inverter_led_temperature::state::blinking` | Blinking | Blinkar | Shared reference target checked |
| 984722027 | `component::victron_gx::entity::sensor::vebus_inverter_led_temperature::name` | Temperature LED | Temperatur-LED | Core-literal match |
| 984722026 | `component::victron_gx::entity::sensor::vebus_inverter_led_overload::state::on` | On | På | Shared reference target checked |
| 984722025 | `component::victron_gx::entity::sensor::vebus_inverter_led_overload::state::off` | Off | Av | Shared reference target checked |
| 984722024 | `component::victron_gx::entity::sensor::vebus_inverter_led_overload::state::blinking_inverted` | Blinking inverted | Blinkar inverterat | Shared reference target checked |
| 984722023 | `component::victron_gx::entity::sensor::vebus_inverter_led_overload::state::blinking` | Blinking | Blinkar | Shared reference target checked |
| 984722022 | `component::victron_gx::entity::sensor::vebus_inverter_led_overload::name` | Overload LED | Överbelastnings-LED | Core-literal match |
| 984722021 | `component::victron_gx::entity::sensor::vebus_inverter_led_mains::state::on` | On | På | Shared reference target checked |
| 984722020 | `component::victron_gx::entity::sensor::vebus_inverter_led_mains::state::off` | Off | Av | Shared reference target checked |
| 984722019 | `component::victron_gx::entity::sensor::vebus_inverter_led_mains::state::blinking_inverted` | Blinking inverted | Blinkar inverterat | Shared reference target checked |
| 984722018 | `component::victron_gx::entity::sensor::vebus_inverter_led_mains::state::blinking` | Blinking | Blinkar | Shared reference target checked |
| 984722017 | `component::victron_gx::entity::sensor::vebus_inverter_led_mains::name` | Mains LED | Nät-LED | Core-literal match |
| 984722016 | `component::victron_gx::entity::sensor::vebus_inverter_led_low_battery::state::on` | On | På | Shared reference target checked |
| 984722015 | `component::victron_gx::entity::sensor::vebus_inverter_led_low_battery::state::off` | Off | Av | Shared reference target checked |
| 984722014 | `component::victron_gx::entity::sensor::vebus_inverter_led_low_battery::state::blinking_inverted` | Blinking inverted | Blinkar inverterat | Shared reference target checked |
| 984722013 | `component::victron_gx::entity::sensor::vebus_inverter_led_low_battery::state::blinking` | Blinking | Blinkar | Shared reference target checked |
| 984722012 | `component::victron_gx::entity::sensor::vebus_inverter_led_low_battery::name` | Low battery LED | LED för låg batterinivå | Core-literal match |
| 984722011 | `component::victron_gx::entity::sensor::vebus_inverter_led_inverter::state::on` | On | På | Shared reference target checked |
| 984722010 | `component::victron_gx::entity::sensor::vebus_inverter_led_inverter::state::off` | Off | Av | Shared reference target checked |
| 984722009 | `component::victron_gx::entity::sensor::vebus_inverter_led_inverter::state::blinking_inverted` | Blinking inverted | Blinkar inverterat | Shared reference target checked |
| 984722008 | `component::victron_gx::entity::sensor::vebus_inverter_led_inverter::state::blinking` | Blinking | Blinkar | Shared reference target checked |
| 984722007 | `component::victron_gx::entity::sensor::vebus_inverter_led_inverter::name` | Inverter LED | Växelriktar-LED | Core-literal match |
| 984722006 | `component::victron_gx::entity::sensor::vebus_inverter_led_float::state::on` | On | På | Shared reference target checked |
| 984722005 | `component::victron_gx::entity::sensor::vebus_inverter_led_float::state::off` | Off | Av | Shared reference target checked |
| 984722004 | `component::victron_gx::entity::sensor::vebus_inverter_led_float::state::blinking_inverted` | Blinking inverted | Blinkar inverterat | Shared reference target checked |
| 984722003 | `component::victron_gx::entity::sensor::vebus_inverter_led_float::state::blinking` | Blinking | Blinkar | Shared reference target checked |
| 984722002 | `component::victron_gx::entity::sensor::vebus_inverter_led_float::name` | Float LED | Underhållsladdnings-LED | Core-literal match |
| 984722001 | `component::victron_gx::entity::sensor::vebus_inverter_led_bulk::state::on` | On | På | Shared reference target checked |
| 984722000 | `component::victron_gx::entity::sensor::vebus_inverter_led_bulk::state::off` | Off | Av | Shared reference target checked |
| 984721999 | `component::victron_gx::entity::sensor::vebus_inverter_led_bulk::state::blinking_inverted` | Blinking inverted | Blinkar inverterat | Shared reference target checked |
| 984721998 | `component::victron_gx::entity::sensor::vebus_inverter_led_bulk::state::blinking` | Blinking | Blinkar | Shared reference target checked |
| 984721997 | `component::victron_gx::entity::sensor::vebus_inverter_led_bulk::name` | Bulk LED | Bulk-LED | Core-literal match |
| 984721996 | `component::victron_gx::entity::sensor::vebus_inverter_led_absorption::state::on` | On | På | Shared reference target checked |
| 984721995 | `component::victron_gx::entity::sensor::vebus_inverter_led_absorption::state::off` | Off | Av | Shared reference target checked |
| 984721994 | `component::victron_gx::entity::sensor::vebus_inverter_led_absorption::state::blinking_inverted` | Blinking inverted | Blinkar inverterat | Shared reference target checked |
| 984721993 | `component::victron_gx::entity::sensor::vebus_inverter_led_absorption::state::blinking` | Blinking | Blinkar | Shared reference target checked |
| 984721992 | `component::victron_gx::entity::sensor::vebus_inverter_led_absorption::name` | Absorption LED | Absorptions-LED | Core-literal match |
| 984721991 | `component::victron_gx::entity::sensor::evcharger_session_saved_cost::name` | Session saved cost | Sparad sessionskostnad | Core-literal match |
| 984721990 | `component::victron_gx::entity::sensor::battery_high_current::state::warning` | Warning | Varning | Shared reference target checked |
| 984721989 | `component::victron_gx::entity::sensor::battery_high_current::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 984721988 | `component::victron_gx::entity::sensor::battery_high_current::state::alarm` | Alarm | Larm | Shared reference target checked |
| 984721987 | `component::victron_gx::entity::sensor::battery_high_current::name` | High current | Hög ström | Core-literal match |
| 984721986 | `component::victron_gx::entity::sensor::battery_contactor::state::warning` | Warning | Varning | Shared reference target checked |
| 984721985 | `component::victron_gx::entity::sensor::battery_contactor::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 984721984 | `component::victron_gx::entity::sensor::battery_contactor::state::alarm` | Alarm | Larm | Shared reference target checked |
| 984721983 | `component::victron_gx::entity::sensor::battery_contactor::name` | Contactor | Kontaktor | Core-literal match |
| 984721982 | `component::victron_gx::entity::select::vebus_weak_ac_input::state::weak` | Weak | Svag | Core-literal match |
| 984721981 | `component::victron_gx::entity::select::vebus_weak_ac_input::state::strong` | Strong | Stark | Core-literal match |
| 984721980 | `component::victron_gx::entity::select::vebus_weak_ac_input::name` | AC input strength | AC-ingångsstyrka | Core-literal match |
| 984721979 | `component::victron_gx::entity::select::vebus_microgrid_operation::state::standard` | Standard operation | Standarddrift | Shared reference target checked |
| 984721978 | `component::victron_gx::entity::select::vebus_microgrid_operation::state::microgrid` | Microgrid operation | Mikronätsdrift | Shared reference target checked |
| 984721977 | `component::victron_gx::entity::select::vebus_microgrid_operation::name` | Microgrid operation | Mikronätsdrift | Shared reference target checked |
| 984721976 | `component::victron_gx::entity::binary_sensor::vebus_microgrid_operation_reset_pending::name` | Microgrid operation change pending reset | Ändring av mikronätsdrift väntar på återställning | Core-literal match |
| 984721975 | `component::victron_gx::entity::binary_sensor::vebus_microgrid_allow_black_start::name` | Microgrid black start allowed | Mikronätets svartstart tillåts | Core-literal match |
| 984721974 | `component::victron_gx::entity::binary_sensor::vebus_device_device_number_relay_test_ok::name` | {device_number} relay test OK | Relätest OK för {device_number} | Core-literal match |
| 984721973 | `component::victron_gx::common::standard_operation` | Standard operation | Standarddrift | Core-literal match |
| 984721972 | `component::victron_gx::common::microgrid_operation` | Microgrid operation | Mikronätsdrift | Core-literal match |
| 984721971 | `component::victron_gx::common::blinking_inverted` | Blinking inverted | Blinkar inverterat | Core-literal match |
| 984721970 | `component::victron_gx::common::blinking` | Blinking | Blinkar | Core-literal match |
| 984714731 | `component::shelly::entity::switch::auto_brightness::name` | Auto display brightness | Automatisk skärmljusstyrka | Core-literal match |
| 984714730 | `component::shelly::entity::number::min_auto_display_brightness::name` | Minimum auto display brightness | Minsta automatiska skärmljusstyrka | Core-literal match |
| 984714729 | `component::shelly::entity::number::display_brightness::name` | Display brightness | Skärmens ljusstyrka | Core-literal match |
| 984714120 | `component::shelly::services::command::name` | Send command | Skicka kommando | Core-literal match |
| 984714119 | `component::shelly::services::command::fields::params::name` | Parameters | Parametrar | Core-literal match |
| 984714118 | `component::shelly::services::command::fields::params::description` | Optional parameters of the command in the format of key value pairs. | Valfria kommandoparametrar i formatet nyckel-värde-par. | Core-literal match |
| 984714117 | `component::shelly::services::command::fields::device_id::name` | Device | Enhet | Core-literal match |
| 984714116 | `component::shelly::services::command::fields::device_id::description` | The ID of the Shelly device to send the command to. | ID:t för Shelly-enheten som kommandot ska skickas till. | Core-literal match |
| 984714115 | `component::shelly::services::command::fields::command::name` | Command | Kommando | Core-literal match |
| 984714114 | `component::shelly::services::command::fields::command::description` | The RPC method for generation 2 and newer devices, for example `Switch.Set`, or the HTTP endpoint for generation 1 devices, for example `relay/0`. | RPC-metoden för generation 2 och nyare enheter, till exempel `Switch.Set`, eller HTTP-slutpunkten för generation 1-enheter, till exempel `relay/0`. | Core-literal match |
| 984714113 | `component::shelly::services::command::description` | Sends a command to a Shelly device and returns the device response. | Skickar ett kommando till en Shelly-enhet och returnerar enhetens svar. | Core-literal match |
| 984714112 | `component::shelly::exceptions::command_sleeping_device::message` | {device} is a sleeping device and does not support commands | {device} är en sovande enhet och har inte stöd för kommandon | Core-literal match |
| 984714111 | `component::shelly::exceptions::command_rpc_error::message` | Command {command} failed for {device} with error {code}: {message} | Kommandot {command} misslyckades för {device} med felet {code}: {message} | Core-literal match |
| 984714110 | `component::shelly::exceptions::command_not_allowed::message` | Command {command} is not allowed for {device} | Kommandot {command} är inte tillåtet för {device} | Core-literal match |
| 984714109 | `component::shelly::exceptions::command_invalid_params::message` | Command parameters for {device} must be text, number or boolean values | Kommandoparametrarna för {device} måste vara text-, tal- eller booleska värden | Core-literal match |
| 984714108 | `component::shelly::exceptions::command_http_error::message` | Command {command} failed for {device} with HTTP status {status} | Kommandot {command} misslyckades för {device} med HTTP-status {status} | Core-literal match |
| 984690382 | `component::irm_kmi::entity::sensor::next_warning::name` | Next warning | Nästa varning | Core-literal match |
| 984690381 | `component::irm_kmi::entity::binary_sensor::warning::state_attributes::warnings::name` | Warnings | Varningar | Core-literal match |
| 984690380 | `component::irm_kmi::entity::binary_sensor::warning::name` | Warning | Varning | Core-literal match |
| 984688804 | `component::irm_kmi::entity::sensor::pollen_oak::state::yellow` | Yellow | Gul | Shared reference target checked |
| 984688803 | `component::irm_kmi::entity::sensor::pollen_oak::state::red` | Red | Röd | Shared reference target checked |
| 984688802 | `component::irm_kmi::entity::sensor::pollen_oak::state::purple` | Purple | Lila | Shared reference target checked |
| 984688801 | `component::irm_kmi::entity::sensor::pollen_oak::state::orange` | Orange | Orange | Shared reference target checked |
| 984688800 | `component::irm_kmi::entity::sensor::pollen_oak::state::none` | None | Ingen | Shared reference target checked |
| 984688799 | `component::irm_kmi::entity::sensor::pollen_oak::state::green` | Green | Grön | Shared reference target checked |
| 984688798 | `component::irm_kmi::entity::sensor::pollen_oak::state::active` | Active | Aktiv | Shared reference target checked |
| 984688797 | `component::irm_kmi::entity::sensor::pollen_oak::name` | Oak pollen | Ekpollen | Core-literal match |
| 984688796 | `component::irm_kmi::entity::sensor::pollen_mugwort::state::yellow` | Yellow | Gul | Shared reference target checked |
| 984688795 | `component::irm_kmi::entity::sensor::pollen_mugwort::state::red` | Red | Röd | Shared reference target checked |
| 984688794 | `component::irm_kmi::entity::sensor::pollen_mugwort::state::purple` | Purple | Lila | Shared reference target checked |
| 984688793 | `component::irm_kmi::entity::sensor::pollen_mugwort::state::orange` | Orange | Orange | Shared reference target checked |
| 984688792 | `component::irm_kmi::entity::sensor::pollen_mugwort::state::none` | None | Ingen | Shared reference target checked |
| 984688791 | `component::irm_kmi::entity::sensor::pollen_mugwort::state::green` | Green | Grön | Shared reference target checked |
| 984688790 | `component::irm_kmi::entity::sensor::pollen_mugwort::state::active` | Active | Aktiv | Shared reference target checked |
| 984688789 | `component::irm_kmi::entity::sensor::pollen_mugwort::name` | Mugwort pollen | Gråbopollen | Core-literal match |
| 984688788 | `component::irm_kmi::entity::sensor::pollen_hazel::state::yellow` | Yellow | Gul | Shared reference target checked |
| 984688787 | `component::irm_kmi::entity::sensor::pollen_hazel::state::red` | Red | Röd | Shared reference target checked |
| 984688786 | `component::irm_kmi::entity::sensor::pollen_hazel::state::purple` | Purple | Lila | Shared reference target checked |
| 984688785 | `component::irm_kmi::entity::sensor::pollen_hazel::state::orange` | Orange | Orange | Shared reference target checked |
| 984688784 | `component::irm_kmi::entity::sensor::pollen_hazel::state::none` | None | Ingen | Shared reference target checked |
| 984688783 | `component::irm_kmi::entity::sensor::pollen_hazel::state::green` | Green | Grön | Shared reference target checked |
| 984688782 | `component::irm_kmi::entity::sensor::pollen_hazel::state::active` | Active | Aktiv | Shared reference target checked |
| 984688781 | `component::irm_kmi::entity::sensor::pollen_hazel::name` | Hazel pollen | Hasselpollen | Core-literal match |
| 984688780 | `component::irm_kmi::entity::sensor::pollen_grasses::state::yellow` | Yellow | Gul | Shared reference target checked |
| 984688779 | `component::irm_kmi::entity::sensor::pollen_grasses::state::red` | Red | Röd | Shared reference target checked |
| 984688778 | `component::irm_kmi::entity::sensor::pollen_grasses::state::purple` | Purple | Lila | Shared reference target checked |
| 984688777 | `component::irm_kmi::entity::sensor::pollen_grasses::state::orange` | Orange | Orange | Shared reference target checked |
| 984688776 | `component::irm_kmi::entity::sensor::pollen_grasses::state::none` | None | Ingen | Shared reference target checked |
| 984688775 | `component::irm_kmi::entity::sensor::pollen_grasses::state::green` | Green | Grön | Shared reference target checked |
| 984688774 | `component::irm_kmi::entity::sensor::pollen_grasses::state::active` | Active | Aktiv | Shared reference target checked |
| 984688773 | `component::irm_kmi::entity::sensor::pollen_grasses::name` | Grass pollen | Gräspollen | Core-literal match |
| 984688772 | `component::irm_kmi::entity::sensor::pollen_birch::state::yellow` | Yellow | Gul | Shared reference target checked |
| 984688771 | `component::irm_kmi::entity::sensor::pollen_birch::state::red` | Red | Röd | Shared reference target checked |
| 984688770 | `component::irm_kmi::entity::sensor::pollen_birch::state::purple` | Purple | Lila | Shared reference target checked |
| 984688769 | `component::irm_kmi::entity::sensor::pollen_birch::state::orange` | Orange | Orange | Shared reference target checked |
| 984688768 | `component::irm_kmi::entity::sensor::pollen_birch::state::none` | None | Ingen | Shared reference target checked |
| 984688767 | `component::irm_kmi::entity::sensor::pollen_birch::state::green` | Green | Grön | Shared reference target checked |
| 984688766 | `component::irm_kmi::entity::sensor::pollen_birch::state::active` | Active | Aktiv | Shared reference target checked |
| 984688765 | `component::irm_kmi::entity::sensor::pollen_birch::name` | Birch pollen | Björkpollen | Core-literal match |
| 984688764 | `component::irm_kmi::entity::sensor::pollen_ash::state::yellow` | Yellow | Gul | Shared reference target checked |
| 984688763 | `component::irm_kmi::entity::sensor::pollen_ash::state::red` | Red | Röd | Shared reference target checked |
| 984688762 | `component::irm_kmi::entity::sensor::pollen_ash::state::purple` | Purple | Lila | Shared reference target checked |
| 984688761 | `component::irm_kmi::entity::sensor::pollen_ash::state::orange` | Orange | Orange | Shared reference target checked |
| 984688760 | `component::irm_kmi::entity::sensor::pollen_ash::state::none` | None | Ingen | Shared reference target checked |
| 984688759 | `component::irm_kmi::entity::sensor::pollen_ash::state::green` | Green | Grön | Shared reference target checked |
| 984688758 | `component::irm_kmi::entity::sensor::pollen_ash::state::active` | Active | Aktiv | Shared reference target checked |
| 984688757 | `component::irm_kmi::entity::sensor::pollen_ash::name` | Ash pollen | Askpollen | Core-literal match |
| 984688756 | `component::irm_kmi::entity::sensor::pollen_alder::state::yellow` | Yellow | Gul | Core-literal match |
| 984688755 | `component::irm_kmi::entity::sensor::pollen_alder::state::red` | Red | Röd | Core-literal match |
| 984688754 | `component::irm_kmi::entity::sensor::pollen_alder::state::purple` | Purple | Lila | Core-literal match |
| 984688753 | `component::irm_kmi::entity::sensor::pollen_alder::state::orange` | Orange | Orange | Core-literal match |
| 984688752 | `component::irm_kmi::entity::sensor::pollen_alder::state::none` | None | Ingen | Core-literal match |
| 984688751 | `component::irm_kmi::entity::sensor::pollen_alder::state::green` | Green | Grön | Core-literal match |
| 984688750 | `component::irm_kmi::entity::sensor::pollen_alder::state::active` | Active | Aktiv | Shared reference target checked |
| 984688749 | `component::irm_kmi::entity::sensor::pollen_alder::name` | Alder pollen | Alpollen | Core-literal match |
| 984458735 | `component::hotspring::entity::sensor::total_power::name` | Total apparent power | Total skenbar effekt | Core-literal match |
| 984458734 | `component::hotspring::entity::sensor::small_loads_power::name` | Small loads apparent power | Skenbar effekt för små laster | Core-literal match |
| 984458733 | `component::hotspring::entity::sensor::small_loads_current::name` | Small loads current | Ström för små laster | Core-literal match |
| 984458732 | `component::hotspring::entity::sensor::jet3_power::name` | Jet 3 apparent power | Skenbar effekt för jet 3 | Core-literal match |
| 984458731 | `component::hotspring::entity::sensor::jet3_current::name` | Jet 3 current | Ström för jet 3 | Core-literal match |
| 984458730 | `component::hotspring::entity::sensor::jet1_jet2_blower_power::name` | Jets 1, 2, and blower apparent power | Skenbar effekt för jet 1, 2 och fläkt | Core-literal match |
| 984458729 | `component::hotspring::entity::sensor::jet1_jet2_blower_current::name` | Jets 1, 2, and blower current | Ström för jet 1, 2 och fläkt | Core-literal match |
| 984458728 | `component::hotspring::entity::sensor::heater_power::name` | Heater power | Värmarens effekt | Core-literal match |
| 984458727 | `component::hotspring::entity::sensor::heater_current::name` | Heater current | Värmarens ström | Core-literal match |
| 984451507 | `component::evohome::exceptions::api_credentials_invalid::message` | The vendor's API rejected the username or password | Leverantörens API avvisade användarnamnet eller lösenordet | Core-literal match |
| 984279363 | `component::tankerkoenig::services::get_opening_times::name` | Get opening times | Hämta öppettider | Core-literal match |
| 984279362 | `component::tankerkoenig::services::get_opening_times::description` | Retrieves the opening times of a gas station and their temporary changes. | Hämtar en bensinstations öppettider och tillfälliga ändringar. | Core-literal match |
| 984043162 | `component::timer_list::triggers::timer_unpaused::name` | Timer resumed | Timer återupptagen | Core-literal match |
| 984043161 | `component::timer_list::triggers::timer_unpaused::description` | Triggers when a timer is resumed on a timer list. | Utlöses när en timer återupptas i en timerlista. | Core-literal match |
| 984043160 | `component::timer_list::triggers::timer_time_changed::name` | Timer time changed | Timerns tid ändrad | Core-literal match |
| 984043159 | `component::timer_list::triggers::timer_time_changed::description` | Triggers when time is added to or subtracted from a timer on a timer list. | Utlöses när tid läggs till eller dras av från en timer i en timerlista. | Core-literal match |
| 984043158 | `component::timer_list::triggers::timer_paused::name` | Timer paused | Timer pausad | Core-literal match |
| 984043157 | `component::timer_list::triggers::timer_paused::description` | Triggers when a timer is paused on a timer list. | Utlöses när en timer pausas i en timerlista. | Core-literal match |
| 984043156 | `component::timer_list::triggers::timer_finished::name` | Timer finished | Timer avslutad | Core-literal match |
| 984043155 | `component::timer_list::triggers::timer_finished::description` | Triggers when a timer finishes on a timer list. | Utlöses när en timer avslutas i en timerlista. | Core-literal match |
| 984043154 | `component::timer_list::triggers::timer_created::name` | Timer created | Timer skapad | Core-literal match |
| 984043153 | `component::timer_list::triggers::timer_created::description` | Triggers when a timer is created on a timer list. | Utlöses när en timer skapas i en timerlista. | Core-literal match |
| 984043152 | `component::timer_list::triggers::timer_cancelled::name` | Timer cancelled | Timer avbruten | Core-literal match |
| 984043151 | `component::timer_list::triggers::timer_cancelled::description` | Triggers when a timer is cancelled on a timer list. | Utlöses när en timer avbryts i en timerlista. | Core-literal match |
| 984043150 | `component::timer_list::title` | Timer list | Timerlista | Core-literal match |
| 984043149 | `component::timer_list::services::unpause_timer::name` | Resume timer | Återuppta timer | Core-literal match |
| 984043148 | `component::timer_list::services::unpause_timer::fields::timer_id::name` | Timer ID | Timer-ID | Core-literal match |
| 984043147 | `component::timer_list::services::unpause_timer::fields::timer_id::description` | The id of the timer to resume. | ID:t för timern som ska återupptas. | Core-literal match |
| 984043146 | `component::timer_list::services::unpause_timer::description` | Resumes a paused timer. | Återupptar en pausad timer. | Core-literal match |
| 984043145 | `component::timer_list::services::subtract_time::name` | Subtract time | Dra av tid | Core-literal match |
| 984043144 | `component::timer_list::services::subtract_time::fields::timer_id::name` | Timer ID | Timer-ID | Core-literal match |
| 984043143 | `component::timer_list::services::subtract_time::fields::timer_id::description` | The id of the timer to subtract time from. | ID:t för timern som tiden ska dras av från. | Core-literal match |
| 984043142 | `component::timer_list::services::subtract_time::fields::duration::name` | Duration | Varaktighet | Core-literal match |
| 984043141 | `component::timer_list::services::subtract_time::fields::duration::description` | How much time to subtract from the timer. | Den tid som ska dras av från timern. | Core-literal match |
| 984043140 | `component::timer_list::services::subtract_time::description` | Subtracts time from a timer. | Drar av tid från en timer. | Core-literal match |
| 984043139 | `component::timer_list::services::remove_timer::name` | Remove timer | Ta bort timer | Core-literal match |
| 984043138 | `component::timer_list::services::remove_timer::fields::timer_id::name` | Timer ID | Timer-ID | Core-literal match |
| 984043137 | `component::timer_list::services::remove_timer::fields::timer_id::description` | The id of the timer to remove. | ID:t för timern som ska tas bort. | Core-literal match |
| 984043136 | `component::timer_list::services::remove_timer::description` | Removes a timer from a timer list. | Tar bort en timer från en timerlista. | Core-literal match |
| 984043135 | `component::timer_list::services::pause_timer::name` | Pause timer | Pausa timer | Core-literal match |
| 984043134 | `component::timer_list::services::pause_timer::fields::timer_id::name` | Timer ID | Timer-ID | Core-literal match |
| 984043133 | `component::timer_list::services::pause_timer::fields::timer_id::description` | The id of the timer to pause. | ID:t för timern som ska pausas. | Core-literal match |
| 984043132 | `component::timer_list::services::pause_timer::description` | Pauses an active timer. | Pausar en aktiv timer. | Core-literal match |
| 984043131 | `component::timer_list::services::get_timers::name` | Get timers | Hämta timers | Core-literal match |
| 984043130 | `component::timer_list::services::get_timers::fields::status::name` | Status | Status | Core-literal match |
| 984043129 | `component::timer_list::services::get_timers::fields::status::description` | Only return timers with the specified statuses. | Returnerar endast timers med angiven status. | Core-literal match |
| 984043128 | `component::timer_list::services::get_timers::description` | Gets the timers on a timer list. | Hämtar timers i en timerlista. | Core-literal match |
| 984043127 | `component::timer_list::services::finish_timer::name` | Finish timer | Avsluta timer | Core-literal match |
| 984043126 | `component::timer_list::services::finish_timer::fields::timer_id::name` | Timer ID | Timer-ID | Core-literal match |
| 984043125 | `component::timer_list::services::finish_timer::fields::timer_id::description` | The id of the timer to finish. | ID:t för timern som ska avslutas. | Core-literal match |
| 984043124 | `component::timer_list::services::finish_timer::description` | Finishes a timer early, as if its remaining time had elapsed. | Avslutar en timer i förtid, som om dess återstående tid hade löpt ut. | Core-literal match |
| 984043123 | `component::timer_list::services::create_timer::name` | Create timer | Skapa timer | Core-literal match |
| 984043122 | `component::timer_list::services::create_timer::fields::name::name` | Name | Namn | Core-literal match |
| 984043121 | `component::timer_list::services::create_timer::fields::name::description` | Optional name for the timer. | Valfritt namn för timern. | Core-literal match |
| 984043120 | `component::timer_list::services::create_timer::fields::duration::name` | Duration | Varaktighet | Core-literal match |
| 984043119 | `component::timer_list::services::create_timer::fields::duration::description` | How long the timer should run for. | Hur länge timern ska vara igång. | Core-literal match |
| 984043118 | `component::timer_list::services::create_timer::description` | Creates a new timer on a timer list and starts it counting down. | Skapar en ny timer i en timerlista och startar nedräkningen. | Core-literal match |
| 984043117 | `component::timer_list::services::cancel_timer::name` | Cancel timer | Avbryt timer | Core-literal match |
| 984043116 | `component::timer_list::services::cancel_timer::fields::timer_id::name` | Timer ID | Timer-ID | Core-literal match |
| 984043115 | `component::timer_list::services::cancel_timer::fields::timer_id::description` | The id of the timer to cancel. | ID:t för timern som ska avbrytas. | Core-literal match |
| 984043114 | `component::timer_list::services::cancel_timer::description` | Cancels a timer without finishing it. | Avbryter en timer utan att avsluta den. | Core-literal match |
| 984043113 | `component::timer_list::services::add_time::name` | Add time | Lägg till tid | Core-literal match |
| 984043112 | `component::timer_list::services::add_time::fields::timer_id::name` | Timer ID | Timer-ID | Core-literal match |
| 984043111 | `component::timer_list::services::add_time::fields::timer_id::description` | The id of the timer to add time to. | ID:t för timern vars tid ska utökas. | Core-literal match |
| 984043110 | `component::timer_list::services::add_time::fields::duration::name` | Duration | Varaktighet | Core-literal match |
| 984043109 | `component::timer_list::services::add_time::fields::duration::description` | How much time to add to the timer. | Hur mycket tid som ska läggas till på timern. | Core-literal match |
| 984043108 | `component::timer_list::services::add_time::description` | Adds time to a timer. | Lägger till tid på en timer. | Core-literal match |
| 984043107 | `component::timer_list::selector::status::options::paused` | Paused | Pausad | Core-literal match |
| 984043106 | `component::timer_list::selector::status::options::finished` | Finished | Avslutad | Core-literal match |
| 984043105 | `component::timer_list::selector::status::options::cancelled` | Cancelled | Avbruten | Core-literal match |
| 984043104 | `component::timer_list::selector::status::options::active` | Active | Aktiv | Core-literal match |
| 984043103 | `component::timer_list::exceptions::timer_not_found::message` | Unable to find timer with id: {timer_id} | Det gick inte att hitta en timer med ID:t {timer_id} | Core-literal match |
| 984043102 | `component::timer_list::entity_component::_::name` | Timer list | Timerlista | Shared reference target checked |
| 984025038 | `component::homewizard::issues::migrate_to_v2_api::fix_flow::step::authorize_timeout::title` | Authorize | Auktorisera | Shared reference target checked |
| 984025037 | `component::homewizard::issues::migrate_to_v2_api::fix_flow::step::authorize_timeout::description` | The button on the HomeWizard device was not pressed within five minutes. Select the button below to try again. | Knappen på HomeWizard-enheten trycktes inte in inom fem minuter. Välj knappen nedan för att försöka igen. | Shared reference target checked |
| 984025036 | `component::homewizard::issues::migrate_to_v2_api::fix_flow::progress::wait_for_button` | Press the button on the HomeWizard device for two seconds. The reconfiguration continues automatically once the button is pressed. | Tryck på knappen på HomeWizard-enheten i två sekunder. Omkonfigureringen fortsätter automatiskt när knappen har tryckts ned. | Core-literal match |
| 984001370 | `component::tile_ble::config::step::user::description` | Log in to your Tile account to get the names of your Tiles and the keys needed to ring them. Only the key of the Tile you set up is stored, not your credentials. | Logga in på ditt Tile-konto för att hämta namnen på dina Tile-enheter och de nycklar som behövs för att få dem att ringa. Endast nyckeln till den Tile du konfigurerar lagras, inte dina inloggningsuppgifter. | Core-literal match |
| 984001369 | `component::tile_ble::config::step::user::data_description::username` | The email address of your Tile account. | E-postadressen till ditt Tile-konto. | Core-literal match |
| 984001368 | `component::tile_ble::config::step::user::data_description::password` | The password of your Tile account. | Lösenordet till ditt Tile-konto. | Core-literal match |
| 984001367 | `component::tile_ble::config::step::user::data::username` | Email | E-post | Shared reference target checked |
| 984001366 | `component::tile_ble::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 984001365 | `component::tile_ble::config::step::device::description` | Pick the Tile you want to set up. | Välj den Tile du vill konfigurera. | Core-literal match |
| 984001364 | `component::tile_ble::config::step::device::data_description::address` | Your Tiles are listed by name. A Tile listed by its address could not be matched to your account; Home Assistant connects to it to find out which Tile it is. | Dina Tile-enheter visas med namn. En Tile som visas med sin adress kunde inte kopplas till ditt konto. Home Assistant ansluter till den för att ta reda på vilken Tile det är. | Core-literal match |
| 984001363 | `component::tile_ble::config::step::device::data::address` | Device | Enhet | Shared reference target checked |
| 984001362 | `component::tile_ble::config::error::wrong_tile` | The Tile did not accept the key from your Tile account. Pick another Tile. | Tile-enheten accepterade inte nyckeln från ditt Tile-konto. Välj en annan Tile-enhet. | Core-literal match |
| 984001361 | `component::tile_ble::config::error::unknown_tile` | This Tile is not in your Tile account. Pick another Tile. | Den här Tile-enheten finns inte på ditt Tile-konto. Välj en annan Tile-enhet. | Core-literal match |
| 984001360 | `component::tile_ble::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 984001359 | `component::tile_ble::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 984001358 | `component::tile_ble::config::abort::no_tiles` | No Tiles were found in this Tile account. | Inga Tile-enheter hittades på det här Tile-kontot. | Core-literal match |
| 984001357 | `component::tile_ble::config::abort::no_devices_found` | No devices found on the network | Inga enheter hittades i nätverket | Shared reference target checked |
| 984001356 | `component::tile_ble::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 983929727 | `component::homewizard::issues::migrate_to_v2_api::fix_flow::step::confirm_identify::title` | Update the authentication method for {title} | Uppdatera autentiseringsmetoden för {title} | Shared reference target checked |
| 983929726 | `component::homewizard::issues::migrate_to_v2_api::fix_flow::step::confirm_identify::description` | Your {title} now supports a more secure and feature-rich communication method. To take advantage of this, you need to reconfigure the integration.<br><br>To help you find the device, its status light blinks until the reconfiguration is done.<br><br>Select **Submit** to start the reconfiguration. | Din {title} har nu stöd för en säkrare och mer funktionsrik kommunikationsmetod. Du måste konfigurera om integrationen för att använda den.<br><br>För att hjälpa dig hitta enheten blinkar dess statuslampa i upp till fem minuter eller tills du väljer **Skicka**.<br><br>Välj **Skicka** för att starta omkonfigureringen. | Core-literal match |
| 983927185 | `component::homewizard::issues::migrate_to_v2_api::fix_flow::error::network_error` | Failed to connect | Det gick inte att ansluta | Source follow-up open |
| 983926323 | `component::hdfury::entity::number::tcp_port::name` | IP interrupt port | Port för IP-avbrott | Core-literal match |
| 983913086 | `component::hdfury::entity::switch::ipinterrupt::name` | IP interrupt | IP-avbrott | Core-literal match |
| 983752177 | `component::homewizard::config::step::authorize_timeout::title` | Authorize | Auktorisera | Shared reference target checked |
| 983752176 | `component::homewizard::config::step::authorize_timeout::description` | The button on the HomeWizard device was not pressed within five minutes. Select the button below to try again. | Knappen på HomeWizard-enheten trycktes inte in inom fem minuter. Välj knappen nedan för att försöka igen. | Core-literal match |
| 983752175 | `component::homewizard::config::progress::wait_for_button` | Press the button on the HomeWizard device for two seconds. Setup continues automatically once the button is pressed. | Håll knappen på HomeWizard-enheten intryckt i två sekunder. Konfigurationen fortsätter automatiskt när du har tryckt på knappen. | Core-literal match |
| 983752174 | `component::homewizard::config::abort::flow_closed` | The setup was closed before the device was authorized. | Konfigurationen stängdes innan enheten auktoriserades. | Core-literal match |
| 983689300 | `component::philips_js::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 983689299 | `component::philips_js::config::step::reconfigure::data::api_version` | API Version | API-version | Shared reference target checked |
| 983689298 | `component::philips_js::config::abort::unique_id_mismatch` | The host you entered belongs to a different Philips TV. | Värden du angav tillhör en annan Philips-tv. | Core-literal match |
| 983610816 | `component::ipp::exceptions::cannot_connect::message` | Could not connect to the printer | Det gick inte att ansluta till skrivaren | Core-literal match |
| 983542912 | `component::lyric::exceptions::failed_to_set_emergency_heat::message` | Failed to set emergency heat | Det gick inte att ställa in nödvärme. | Core-literal match |
| 983542911 | `component::lyric::entity::switch::emergency_heat::name` | Emergency heat | Nödvärme | Core-literal match |
| 983506608 | `component::music_assistant::services::get_queue::fields::username::name` | Username | Användarnamn | Shared reference target checked |
| 983506607 | `component::music_assistant::services::get_queue::fields::username::description` | Music Assistant username used to request the queue items. The request fails when this user may not access the player. Defaults to the Music Assistant user linked to the Home Assistant user making the request. If there is no linked user, the request runs as the default account. | Music Assistant-användarnamnet som används för att hämta objekt från kön. Begäran misslyckas om användaren inte har åtkomst till spelaren. Som standard används det Music Assistant-konto som är kopplat till Home Assistant-användaren som gör begäran. Om inget konto är kopplat används standardkontot. | Core-literal match |
| 983506606 | `component::music_assistant::services::get_queue::fields::offset::name` | Offset | Förskjutning | Shared reference target checked |
| 983506605 | `component::music_assistant::services::get_queue::fields::offset::description` | Number of queue items to skip. Requires a limit. | Antal objekt i kön som ska hoppas över. Kräver en gräns. | Core-literal match |
| 983506604 | `component::music_assistant::services::get_queue::fields::limit::name` | Limit | Gräns | Shared reference target checked |
| 983506603 | `component::music_assistant::services::get_queue::fields::limit::description` | Maximum number of queue items to return. Leave at 0 to only return the queue details. | Maximalt antal objekt i kön som ska returneras. Låt värdet vara 0 för att bara returnera information om kön. | Core-literal match |
| 983506602 | `component::music_assistant::exceptions::server_too_old::message` | This action requires a newer Music Assistant server version. | Den här åtgärden kräver en nyare version av Music Assistant-servern. | Core-literal match |
| 983506601 | `component::music_assistant::exceptions::offset_needs_limit::message` | An offset requires a limit greater than 0. | Offset kräver en gräns större än 0. | Core-literal match |
| 983506600 | `component::music_assistant::exceptions::no_active_queue::message` | The player is not playing from a Music Assistant queue. | Spelaren spelar inte upp från en Music Assistant-kö. | Core-literal match |
| 983319699 | `component::jellyfin::exceptions::cannot_remove_server_device::message` | The Jellyfin server device cannot be removed. Remove the Jellyfin integration instead. | Jellyfin-serverns enhet kan inte tas bort. Ta bort Jellyfin-integrationen i stället. | Core-literal match |
| 983319698 | `component::jellyfin::exceptions::cannot_remove_active_device::message` | This device is still connected to Jellyfin. It cannot be removed while the client is active. Disable or hide it instead. | Den här enheten är fortfarande ansluten till Jellyfin. Den kan inte tas bort medan klienten är aktiv. Inaktivera eller dölj den i stället. | Core-literal match |

## Källägaruppföljning

| Nyckel | English source |
|---|---|
| `component::homewizard::issues::migrate_to_v2_api::fix_flow::error::network_error` | Failed to connect |

## Metod och data

- Home Assistant Core source checkout uppdaterad fast-forward till `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5` (2026-11-24).
- Alla 714 nycklar kontrollerade individuellt mot API-källtext, svensk live-text, ordlista och kontext. `svlang natural` kördes på alla befintliga 709 översättningar och kördes om för ändrade texter. Hunspell-SV-signaler granskades manuellt; tekniska termer, varumärken och sammansättningar bedömdes i sitt sammanhang. Swedish FOSS-terminology och HA-TM användes som referens.
- Fullständigt manifest sparat bredvid denna rapport. Home Assistant Core snapshot, PO/TMX och kanonisk gransknings-TMX uppdaterades.
