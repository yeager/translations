# Home Assistant Core – historisk avstämning 21961–22080

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 69 direkta källtexter matchar HA Core-källan; 21 referensanvändningar med 19 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 30 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 21961 | 825626660 | `component::html5::services::send_message::fields::require_interaction::name` | Require interaction | Kräv interaktion | Core-literal match |
| 21962 | 825626659 | `component::html5::services::send_message::fields::require_interaction::description` | If enabled, the notification will remain active until the user clicks or dismisses it, rather than automatically closing after a few seconds. This provides the same behavior on desktop as on mobile platforms. | Om aktiverat förblir aviseringen aktiv tills användaren klickar på eller stänger den, istället för att stängas automatiskt efter några sekunder. Detta ger samma beteende på datorer som på mobila plattformar. | Core-literal match |
| 21963 | 825626658 | `component::html5::services::send_message::fields::renotify::name` | Renotify | Omavisering | Core-literal match |
| 21964 | 825626657 | `component::html5::services::send_message::fields::renotify::description` | If enabled, the user will be alerted again (sound/vibration) when a notification with the same tag replaces a previous one. | Om aktiverat får användaren en ny avisering (ljud/vibration) när en avisering med samma tagg ersätter en tidigare. | Core-literal match |
| 21965 | 825626656 | `component::html5::services::send_message::fields::message::name` | Message | Meddelande | Core-literal match |
| 21966 | 825626655 | `component::html5::services::send_message::fields::message::description` | The message body of the notification. | Aviseringens brödtext. | Core-literal match |
| 21967 | 825626654 | `component::html5::services::send_message::fields::lang::name` | Language | Språk | Core-literal match |
| 21968 | 825626653 | `component::html5::services::send_message::fields::lang::description` | The language of the notification's content. | Språk i aviseringens innehåll. | Core-literal match |
| 21969 | 825626652 | `component::html5::services::send_message::fields::image::name` | Image | Bild | Core-literal match |
| 21970 | 825626651 | `component::html5::services::send_message::fields::image::description` | URL or relative path of a larger image to display in the main body of the notification. Experimental support, may not be displayed on all platforms. | URL eller relativ sökväg till en större bild som ska visas i meddelandets huvuddel. Experimentellt stöd, visas eventuellt inte på alla plattformar. | Core-literal match |
| 21971 | 825626650 | `component::html5::services::send_message::fields::icon::name` | Icon | Ikon | Core-literal match |
| 21972 | 825626649 | `component::html5::services::send_message::fields::icon::description` | URL or relative path of an image to display as the main icon in the notification. Maximum size is 320px by 320px. | URL eller relativ sökväg till en bild som ska visas som huvudikon i aviseringen. Maximal storlek är 320 x 320 pixlar. | Core-literal match |
| 21973 | 825626648 | `component::html5::services::send_message::fields::dir::name` | Text direction | Textriktning | Core-literal match |
| 21974 | 825626647 | `component::html5::services::send_message::fields::dir::description` | The direction of the notification's text. Adopts the browser's language setting behavior by default. | Riktningen på aviseringens text. Använder webbläsarens språkinställning som standard. | Core-literal match |
| 21975 | 825626646 | `component::html5::services::send_message::fields::data::name` | Extra data | Extra data | Core-literal match |
| 21976 | 825626645 | `component::html5::services::send_message::fields::data::description` | Additional custom key-value pairs to include in the payload of the push message. This can be used to include extra information that can be accessed in the notification events. | Ytterligare anpassade nyckel-värdepar som ska inkluderas i push-meddelandets innehåll. Detta kan användas för att inkludera ytterligare information som kan hämtas i aviseringshändelserna. | Core-literal match |
| 21977 | 825626644 | `component::html5::services::send_message::fields::badge::name` | Badge | Märke | Core-literal match |
| 21978 | 825626643 | `component::html5::services::send_message::fields::badge::description` | URL or relative path of a small image to replace the browser icon on mobile platforms. Maximum size is 96px by 96px | URL eller relativ sökväg till en liten bild som ersätter webbläsarikonen på mobila plattformar. Maximal storlek är 96x96px | Core-literal match |
| 21979 | 825626642 | `component::html5::services::send_message::fields::actions::name` | Action buttons | Åtgärdsknappar | Core-literal match |
| 21980 | 825626641 | `component::html5::services::send_message::fields::actions::description` | Adds action buttons to the notification. When the user clicks a button, an event is sent back to Home Assistant. Amount of actions supported may vary between platforms. | Lägger till åtgärdsknappar i aviseringen. När användaren klickar på en knapp skickas en händelse tillbaka till Home Assistant. Antalet åtgärder som stöds kan variera mellan olika plattformar. | Core-literal match |
| 21981 | 825626640 | `component::html5::services::send_message::description` | Sends a message via HTML5 Push Notifications | Skickar en avisering via HTML5-pushmeddelanden | Core-literal match |
| 21982 | 825626639 | `component::html5::selector::urgency::options::normal` | Normal | Normal | Shared reference target checked |
| 21983 | 825626638 | `component::html5::selector::urgency::options::low` | Low | Låg | Shared reference target checked |
| 21984 | 825626637 | `component::html5::selector::urgency::options::high` | High | Hög | Shared reference target checked |
| 21985 | 825626636 | `component::html5::selector::dir::options::rtl` | Right-to-left | Höger till vänster | Core-literal match |
| 21986 | 825626635 | `component::html5::selector::dir::options::ltr` | Left-to-right | Vänster till höger | Core-literal match |
| 21987 | 825626634 | `component::html5::selector::dir::options::auto` | Auto | Auto | Shared reference target checked |
| 21988 | 825626633 | `component::html5::selector::actions::fields::title::name` | Title | Rubrik | Core-literal match |
| 21989 | 825626632 | `component::html5::selector::actions::fields::title::description` | The label of the button displayed to the user. | Den text som visas på knappen för användaren. | Core-literal match |
| 21990 | 825626631 | `component::html5::selector::actions::fields::icon::name` | Icon | Ikon | Core-literal match |
| 21991 | 825626630 | `component::html5::selector::actions::fields::icon::description` | URL of an image displayed as the icon for this button. | URL till en bild som ska visas som ikon för den här knappen. | Core-literal match |
| 21992 | 825626629 | `component::html5::selector::actions::fields::action::name` | Action identifier | Åtgärdsidentifierare | Core-literal match |
| 21993 | 825626628 | `component::html5::selector::actions::fields::action::description` | The identifier of the action. This will be sent back to Home Assistant when the user clicks the button. | Åtgärdens identifierare. Denna skickas tillbaka till Home Assistant när användaren klickar på knappen. | Core-literal match |
| 21994 | 825626627 | `component::html5::issues::deprecated_notify_action::title` | Detected use of deprecated action {action} | Användning av utfasad åtgärd har upptäckts: {action} | Source-path follow-up open |
| 21995 | 825626626 | `component::html5::issues::deprecated_notify_action::description` | The action `{action}` is deprecated and will be removed in a future release.<br><br>Please update your automations and scripts to use the notify entities with the `{new_action_1}` or `{new_action_2}` actions instead. | Åtgärden `{action}` är utfasad och kommer att tas bort i en framtida version.<br><br>Uppdatera dina automatiseringar och skript så att du istället använder åtgärderna `{new_action_1}` eller `{new_action_2}` för dina aviseringar. | Source-path follow-up open |
| 21996 | 825621013 | `component::open_router::config_subentries::conversation::step::init::data_description::web_search` | Allow the model to search the web for answers | Låt modellen söka efter svar på webben | Core-literal match |
| 21997 | 825621012 | `component::open_router::config_subentries::conversation::step::init::data_description::llm_hass_api` | **Device control** only accesses the entities you expose to voice assistants. **Home Assistant** accesses everything and only works for administrators, not voice assistant devices. | **Enhetsstyrning** har endast åtkomst till de entiteter som du exponerar för röstassistenter. **Home Assistant** har åtkomst till allt och fungerar endast för administratörer, inte för röstassistentenheter. | Shared reference target checked |
| 21998 | 825621011 | `component::open_router::config_subentries::conversation::step::init::data::web_search` | Enable web search | Aktivera webbsökning | Core-literal match |
| 21999 | 825621010 | `component::open_router::config_subentries::conversation::initiate_flow::reconfigure` | Reconfigure conversation agent | Konfigurera om konversationsagenten | Core-literal match |
| 22000 | 825621009 | `component::open_router::config_subentries::conversation::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 22001 | 825621008 | `component::open_router::config_subentries::ai_task_data::initiate_flow::reconfigure` | Reconfigure AI task | Konfigurera om AI-uppgiften | Core-literal match |
| 22002 | 825621007 | `component::open_router::config_subentries::ai_task_data::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 22003 | 825618680 | `component::zwave_js::issues::deprecated_legacy_door_tilt_state::title` | Deprecation: {entity_name} | Utfasning: {entity_name} | Core-literal match |
| 22004 | 825618679 | `component::zwave_js::issues::deprecated_legacy_door_tilt_state::description` | The binary sensor `{entity_id}` is deprecated because it has been replaced with the binary sensor `{replacement_entity_id}`.<br><br>The entity was found in the following automations or scripts:<br>{items}<br><br>Please update the above automations or scripts to use the binary sensor `{replacement_entity_id}` and disable the binary sensor `{entity_id}` and then restart Home Assistant, to fix this issue.<br><br>Note that `{replacement_entity_id}` is on only when the door or window is tilted. | Den binära sensorn `{entity_id}` är utfasad eftersom den har ersatts med den binära sensorn `{replacement_entity_id}`.<br><br>Entiteten hittades i följande automatiseringar eller skript:<br>{items}<br><br>Uppdatera ovanstående automatiseringar eller skript så att de använder den binära sensorn `{replacement_entity_id}` och inaktivera därefter den binära sensorn `{entity_id}`. Starta sedan om Home Assistant för att åtgärda problemet.<br><br>Observera att `{replacement_entity_id}` endast är aktiverad när dörren eller fönstret är lutat. | Core-literal match |
| 22005 | 825618678 | `component::zwave_js::issues::deprecated_legacy_door_open_state::title` | Deprecation: {entity_name} | Utfasning: {entity_name} | Core-literal match |
| 22006 | 825618677 | `component::zwave_js::issues::deprecated_legacy_door_open_state::description` | The binary sensor `{entity_id}` is deprecated because it has been replaced with the binary sensor `{replacement_entity_id}`.<br><br>The entity was found in the following automations or scripts:<br>{items}<br><br>Please update the above automations or scripts to use the binary sensor `{replacement_entity_id}` and disable the binary sensor `{entity_id}` and then restart Home Assistant, to fix this issue.<br><br>Note that `{replacement_entity_id}` is on when the door or window is open or tilted. | Den binära sensorn `{entity_id}` är utfasad eftersom den har ersatts med den binära sensorn `{replacement_entity_id}`.<br><br>Entiteten hittades i följande automatiseringar eller skript:<br>{items}<br><br>Uppdatera ovanstående automatiseringar eller skript så att de använder den binära sensorn `{replacement_entity_id}` och inaktivera därefter den binära sensorn `{entity_id}`. Starta sedan om Home Assistant för att åtgärda problemet.<br><br>Observera att `{replacement_entity_id}` är aktiverad när dörren eller fönstret är öppet eller lutat. | Core-literal match |
| 22007 | 825546548 | `component::unifi_access::config::step::reconfigure::description` | Update the connection settings of this UniFi Access controller. | Uppdatera anslutningsinställningarna för denna UniFi Access-kontroller. | Core-literal match |
| 22008 | 825546547 | `component::unifi_access::config::step::reconfigure::data_description::verify_ssl` | Verify the SSL certificate of the controller. | Verifiera styrenhetens SSL-certifikat. | Shared reference target checked |
| 22009 | 825546546 | `component::unifi_access::config::step::reconfigure::data_description::host` | Hostname or IP address of the UniFi Access controller. | Värdnamn eller IP-adress för UniFi Access-kontrollern. | Shared reference target checked |
| 22010 | 825546545 | `component::unifi_access::config::step::reconfigure::data_description::api_token` | API token generated in the UniFi Access settings. | API-token som genererats i inställningarna för UniFi Access. | Shared reference target checked |
| 22011 | 825546544 | `component::unifi_access::config::step::reconfigure::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 22012 | 825546543 | `component::unifi_access::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 22013 | 825546542 | `component::unifi_access::config::step::reconfigure::data::api_token` | API token | API-token | Shared reference target checked |
| 22014 | 825546541 | `component::unifi_access::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 22015 | 825546382 | `component::counter::selector::condition_behavior::options::any` | Any | Något | Source-path follow-up open |
| 22016 | 825546381 | `component::counter::selector::condition_behavior::options::all` | All | Alla | Source-path follow-up open |
| 22017 | 825546380 | `component::counter::conditions::is_value::name` | Counter value | Räknevärde | Core-literal match |
| 22018 | 825546379 | `component::counter::conditions::is_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22019 | 825546378 | `component::counter::conditions::is_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22020 | 825546377 | `component::counter::conditions::is_value::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Core-literal match |
| 22021 | 825546376 | `component::counter::conditions::is_value::fields::behavior::description` | How the state should match on the targeted counters. | Hur tillståndet ska matcha valda räknare. | Source-path follow-up open |
| 22022 | 825546375 | `component::counter::conditions::is_value::description` | Tests the value of one or more counters. | Testar värdet på en eller flera räknare. | Core-literal match |
| 22023 | 825517182 | `component::mqtt::issues::yaml_setup_without_active_setup::title` | MQTT is not set up correctly | MQTT är inte korrekt konfigurerat | Core-literal match |
| 22024 | 825517181 | `component::mqtt::issues::yaml_setup_without_active_setup::description` | Home Assistant detected manually configured MQTT items, but these items cannot be loaded because MQTT is not set up correctly. Make sure the MQTT broker is set up correctly, or remove the MQTT configuration from your `configuration.yaml` file and restart Home Assistant to fix this issue. | Home Assistant har upptäckt manuellt konfigurerade MQTT-objekt, men dessa objekt kan inte laddas eftersom MQTT inte är korrekt konfigurerat. Se till att MQTT-brokern är korrekt konfigurerad, eller ta bort MQTT-konfigurationen från filen `configuration.yaml` och starta om Home Assistant för att åtgärda problemet. | Core-literal match |
| 22025 | 825447172 | `component::synology_dsm::entity::button::shutdown::name` | Shut down | Stäng av | Core-literal match |
| 22026 | 825418924 | `component::huum::exceptions::unable_to_turn_on::message` | Unable to turn on the sauna. | Det går inte att slå på bastun. | Core-literal match |
| 22027 | 825418923 | `component::huum::exceptions::auth_failed::message` | Could not log in to Huum with the given credentials. | Kunde inte logga in på Huum med de angivna inloggningsuppgifterna. | Core-literal match |
| 22028 | 825301278 | `component::valve::triggers::opened::name` | Valve opened | Ventil öppnad | Core-literal match |
| 22029 | 825301277 | `component::valve::triggers::opened::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 22030 | 825301276 | `component::valve::triggers::opened::fields::behavior::description` | The behavior of the targeted valves to trigger on. | Det beteende som ska trigga för valda ventiler. | Source-path follow-up open |
| 22031 | 825301275 | `component::valve::triggers::opened::description` | Triggers when one or more valves open. | Utlöses när en eller flera ventiler öppnas. | Core-literal match |
| 22032 | 825301274 | `component::valve::triggers::closed::name` | Valve closed | Ventil stängdes | Core-literal match |
| 22033 | 825301273 | `component::valve::triggers::closed::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 22034 | 825301272 | `component::valve::triggers::closed::fields::behavior::description` | The behavior of the targeted valves to trigger on. | Det beteende som ska trigga för valda ventiler. | Source-path follow-up open |
| 22035 | 825301271 | `component::valve::triggers::closed::description` | Triggers when one or more valves close. | Utlöses när en eller flera ventiler stängs. | Core-literal match |
| 22036 | 825301270 | `component::valve::selector::trigger_behavior::options::last` | Last | Sista | Source-path follow-up open |
| 22037 | 825301269 | `component::valve::selector::trigger_behavior::options::first` | First | Första | Source-path follow-up open |
| 22038 | 825301268 | `component::valve::selector::trigger_behavior::options::any` | Any | Något | Source-path follow-up open |
| 22039 | 825301267 | `component::valve::common::trigger_behavior_name` | Trigger when | Utlös när | Core-literal match |
| 22040 | 825301266 | `component::valve::common::trigger_behavior_description` | The behavior of the targeted valves to trigger on. | Det beteende som ska trigga för valda ventiler. | Source-path follow-up open |
| 22041 | 824820285 | `component::pjlink::issues::deprecated_yaml_import_issue_unknown::title` | The {integration_title} YAML configuration is being removed | YAML-konfigurationen för {integration_title} tas bort | Source-path follow-up open |
| 22042 | 824820284 | `component::pjlink::issues::deprecated_yaml_import_issue_unknown::description` | Configuring {integration_title} via YAML is deprecated and will be removed in a future release. While importing your configuration, an unexpected exception occurred. Please correct your YAML configuration and restart Home Assistant, or remove the {domain} key from your configuration and configure the integration via the UI. | Konfigurering av {integration_title} via YAML är föråldrad och kommer att tas bort i en framtida version. Ett oväntat fel uppstod när din konfiguration importerades. Korrigera din YAML-konfiguration och starta om Home Assistant, eller ta bort {domain}-nyckeln från din konfiguration och konfigurera integrationen via användargränssnittet. | Source-path follow-up open |
| 22043 | 824820283 | `component::pjlink::issues::deprecated_yaml_import_issue_invalid_auth::title` | The {integration_title} YAML configuration is being removed | YAML-konfigurationen för {integration_title} tas bort | Source-path follow-up open |
| 22044 | 824820282 | `component::pjlink::issues::deprecated_yaml_import_issue_invalid_auth::description` | Configuring {integration_title} via YAML is deprecated and will be removed in a future release. While importing your configuration, invalid authentication details were found. Please correct your YAML configuration and restart Home Assistant, or remove the {domain} key from your configuration and configure the integration via the UI. | Konfigurering av {integration_title} via YAML är föråldrad och kommer att tas bort i en framtida version. Vid import av din konfiguration hittades ogiltiga autentiseringsdetaljer. Korrigera din YAML-konfiguration och starta om Home Assistant, eller ta bort {domain}-nyckeln från din konfiguration och konfigurera integrationen via användargränssnittet. | Source-path follow-up open |
| 22045 | 824820281 | `component::pjlink::issues::deprecated_yaml_import_issue_cannot_connect::title` | The {integration_title} YAML configuration is being removed | YAML-konfigurationen för {integration_title} tas bort | Source-path follow-up open |
| 22046 | 824820280 | `component::pjlink::issues::deprecated_yaml_import_issue_cannot_connect::description` | Configuring {integration_title} via YAML is deprecated and will be removed in a future release. While importing your configuration, a connection error occurred. Please correct your YAML configuration and restart Home Assistant, or remove the {domain} key from your configuration and configure the integration via the UI. | Konfigurering av {integration_title} via YAML är föråldrad och kommer att tas bort i en framtida version. Ett anslutningsfel uppstod när din konfiguration importerades. Korrigera din YAML-konfiguration och starta om Home Assistant, eller ta bort {domain}-nyckeln från din konfiguration och konfigurera integrationen via användargränssnittet. | Source-path follow-up open |
| 22047 | 824820279 | `component::pjlink::config::step::user::data::port` | Port | Port | Shared reference target checked |
| 22048 | 824820278 | `component::pjlink::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 22049 | 824820277 | `component::pjlink::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 22050 | 824820276 | `component::pjlink::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 22051 | 824820275 | `component::pjlink::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 22052 | 824820274 | `component::pjlink::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 22053 | 824820273 | `component::pjlink::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 22054 | 824812422 | `component::casper_glow::entity::select::dimming_time::name` | Dimming time | Dimningstid | Core-literal match |
| 22055 | 824812408 | `component::html5::entity::event::event::state_attributes::tag::name` | Tag | Tagg | Shared reference target checked |
| 22056 | 824812407 | `component::html5::entity::event::event::state_attributes::event_type::state::received` | Received | Mottagen | Core-literal match |
| 22057 | 824812406 | `component::html5::entity::event::event::state_attributes::event_type::state::closed` | Closed | Stängd | Core-literal match |
| 22058 | 824812405 | `component::html5::entity::event::event::state_attributes::event_type::state::clicked` | Clicked | Klickad | Core-literal match |
| 22059 | 824812404 | `component::html5::entity::event::event::state_attributes::action::name` | Action | Åtgärd | Core-literal match |
| 22060 | 824808721 | `component::unifi_access::exceptions::lock_rule_failed::message` | Failed to update the door lock rule. | Det gick inte att uppdatera dörrlåsregeln. | Core-literal match |
| 22061 | 824808720 | `component::unifi_access::entity::select::door_lock_rule::state::schedule` | Schedule | Schema | Core-literal match |
| 22062 | 824808719 | `component::unifi_access::entity::select::door_lock_rule::state::reset` | Reset | Återställ | Core-literal match |
| 22063 | 824808718 | `component::unifi_access::entity::select::door_lock_rule::state::lock_early` | Lock early | Lås tidigt | Core-literal match |
| 22064 | 824808717 | `component::unifi_access::entity::select::door_lock_rule::state::keep_unlock` | Keep unlocked | Fortsatt upplåst | Core-literal match |
| 22065 | 824808716 | `component::unifi_access::entity::select::door_lock_rule::state::keep_lock` | Keep locked | Fortsatt låst | Core-literal match |
| 22066 | 824808715 | `component::unifi_access::entity::select::door_lock_rule::state::custom` | Custom | Anpassad | Core-literal match |
| 22067 | 824808714 | `component::unifi_access::entity::select::door_lock_rule::name` | Lock rule | Låsregel | Core-literal match |
| 22068 | 824808713 | `component::microbees::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22069 | 824805068 | `component::transmission::entity::event::torrent::state_attributes::event_type::state::started` | Started | Startad | Core-literal match |
| 22070 | 824805067 | `component::transmission::entity::event::torrent::state_attributes::event_type::state::removed` | Removed | Borttagen | Core-literal match |
| 22071 | 824805066 | `component::transmission::entity::event::torrent::state_attributes::event_type::state::downloaded` | Downloaded | Nedladdad | Core-literal match |
| 22072 | 824805065 | `component::transmission::entity::event::torrent::name` | Torrent | Torrent | Core-literal match |
| 22073 | 824805058 | `component::monzo::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22074 | 824805056 | `component::google_assistant_sdk::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22075 | 824805055 | `component::google_mail::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22076 | 824805054 | `component::iotty::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22077 | 824805053 | `component::google_sheets::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22078 | 824805052 | `component::geocaching::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22079 | 824805051 | `component::husqvarna_automower::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 22080 | 824805048 | `component::lyric::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 825626627 | `component::html5::issues::deprecated_notify_action::title` | Detected use of deprecated action {action} |
| 825626626 | `component::html5::issues::deprecated_notify_action::description` | The action `{action}` is deprecated and will be removed in a future release.

Please update your automations and scripts to use the notify entities with the `{new_action_1}` or `{new_action_2}` actions instead. |
| 825621009 | `component::open_router::config_subentries::conversation::abort::reconfigure_successful` | Reconfiguration was successful |
| 825621007 | `component::open_router::config_subentries::ai_task_data::abort::reconfigure_successful` | Reconfiguration was successful |
| 825546541 | `component::unifi_access::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 825546382 | `component::counter::selector::condition_behavior::options::any` | Any |
| 825546381 | `component::counter::selector::condition_behavior::options::all` | All |
| 825546378 | `component::counter::conditions::is_value::fields::threshold::description` | What to test for and threshold values. |
| 825546376 | `component::counter::conditions::is_value::fields::behavior::description` | How the state should match on the targeted counters. |
| 825301276 | `component::valve::triggers::opened::fields::behavior::description` | The behavior of the targeted valves to trigger on. |
| 825301272 | `component::valve::triggers::closed::fields::behavior::description` | The behavior of the targeted valves to trigger on. |
| 825301270 | `component::valve::selector::trigger_behavior::options::last` | Last |
| 825301269 | `component::valve::selector::trigger_behavior::options::first` | First |
| 825301268 | `component::valve::selector::trigger_behavior::options::any` | Any |
| 825301266 | `component::valve::common::trigger_behavior_description` | The behavior of the targeted valves to trigger on. |
| 824820285 | `component::pjlink::issues::deprecated_yaml_import_issue_unknown::title` | The {integration_title} YAML configuration is being removed |
| 824820284 | `component::pjlink::issues::deprecated_yaml_import_issue_unknown::description` | Configuring {integration_title} via YAML is deprecated and will be removed in a future release. While importing your configuration, an unexpected exception occurred. Please correct your YAML configuration and restart Home Assistant, or remove the {domain} key from your configuration and configure the integration via the UI. |
| 824820283 | `component::pjlink::issues::deprecated_yaml_import_issue_invalid_auth::title` | The {integration_title} YAML configuration is being removed |
| 824820282 | `component::pjlink::issues::deprecated_yaml_import_issue_invalid_auth::description` | Configuring {integration_title} via YAML is deprecated and will be removed in a future release. While importing your configuration, invalid authentication details were found. Please correct your YAML configuration and restart Home Assistant, or remove the {domain} key from your configuration and configure the integration via the UI. |
| 824820281 | `component::pjlink::issues::deprecated_yaml_import_issue_cannot_connect::title` | The {integration_title} YAML configuration is being removed |
| 824820280 | `component::pjlink::issues::deprecated_yaml_import_issue_cannot_connect::description` | Configuring {integration_title} via YAML is deprecated and will be removed in a future release. While importing your configuration, a connection error occurred. Please correct your YAML configuration and restart Home Assistant, or remove the {domain} key from your configuration and configure the integration via the UI. |
| 824808713 | `component::microbees::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 824805058 | `component::monzo::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 824805056 | `component::google_assistant_sdk::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 824805055 | `component::google_mail::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 824805054 | `component::iotty::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 824805053 | `component::google_sheets::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 824805052 | `component::geocaching::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 824805051 | `component::husqvarna_automower::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 824805048 | `component::lyric::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
