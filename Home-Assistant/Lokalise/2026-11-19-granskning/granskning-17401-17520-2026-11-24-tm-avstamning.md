# Home Assistant Core – historisk avstämning 17401–17520

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 90 direkta källtexter matchar HA Core-källan; 25 referensanvändningar med 17 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 5 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 17401 | 860566129 | `component::elkm1::services::switch_output_turn_on_for::name` | Switch output turn on for | Aktivera utgång i | Core-literal match |
| 17402 | 860566128 | `component::elkm1::services::switch_output_turn_on_for::fields::duration::name` | Duration | Varaktighet | Core-literal match |
| 17403 | 860566127 | `component::elkm1::services::switch_output_turn_on_for::fields::duration::description` | Length of time to turn the output on for. | Hur länge utgången ska vara aktiverad. | Core-literal match |
| 17404 | 860566126 | `component::elkm1::services::switch_output_turn_on_for::description` | Turns on an output for a specified length of time. | Aktiverar en utgång under en angiven tidsperiod. | Core-literal match |
| 17405 | 860566024 | `component::google_air_quality::services::get_forecast::name` | Get forecast | Hämta prognos | Core-literal match |
| 17406 | 860566023 | `component::google_air_quality::services::get_forecast::fields::hours::name` | Hours | Timmar | Core-literal match |
| 17407 | 860566022 | `component::google_air_quality::services::get_forecast::fields::hours::description` | How many hours into the future to forecast. | Hur många timmar in i framtiden att prognostisera. | Core-literal match |
| 17408 | 860566021 | `component::google_air_quality::services::get_forecast::fields::device_id::name` | Location | Plats | Core-literal match |
| 17409 | 860566020 | `component::google_air_quality::services::get_forecast::fields::device_id::description` | The location to fetch the forecast for. | Den plats för vilken prognosen ska hämtas. | Core-literal match |
| 17410 | 860566019 | `component::google_air_quality::services::get_forecast::description` | Get an air quality forecast for a configured location. | Få en luftkvalitetsprognos för en konfigurerad plats. | Core-literal match |
| 17411 | 860566018 | `component::google_air_quality::exceptions::device_not_found::message` | Location not found. | Platsen hittades inte. | Core-literal match |
| 17412 | 860563378 | `component::indevolt::entity::sensor::main_cycles::name` | Main cycles | Huvudcykler | Core-literal match |
| 17413 | 860563377 | `component::indevolt::entity::sensor::equivalent_full_cycles::name` | Equivalent full cycles | Motsvarande hela cykler | Core-literal match |
| 17414 | 860563376 | `component::indevolt::entity::sensor::battery_pack_5_cycles::name` | Battery pack 5 cycles | Batteripaket 5 cykler | Core-literal match |
| 17415 | 860563375 | `component::indevolt::entity::sensor::battery_pack_4_cycles::name` | Battery pack 4 cycles | Batteripaket 4 cykler | Core-literal match |
| 17416 | 860563374 | `component::indevolt::entity::sensor::battery_pack_3_cycles::name` | Battery pack 3 cycles | Batteripaket 3 cykler | Core-literal match |
| 17417 | 860563373 | `component::indevolt::entity::sensor::battery_pack_2_cycles::name` | Battery pack 2 cycles | Batteripaket 2 cykler | Core-literal match |
| 17418 | 860563372 | `component::indevolt::entity::sensor::battery_pack_1_cycles::name` | Battery pack 1 cycles | Batteripaket 1 cykler | Core-literal match |
| 17419 | 860562894 | `component::lg_tv_rs232::exceptions::command_rejected::message` | The TV rejected the command: {error} | TV:n avvisade kommandot: {error} | Core-literal match |
| 17420 | 860562893 | `component::lg_tv_rs232::exceptions::command_failed::message` | Failed to send the command to the TV: {error} | Det gick inte att skicka kommandot till TV:n: {error} | Core-literal match |
| 17421 | 860562892 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::rgb_pc` | RGB PC | RGB PC | Core-literal match |
| 17422 | 860562891 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::hdmi4` | HDMI 4 | HDMI 4 | Core-literal match |
| 17423 | 860562890 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::hdmi3` | HDMI 3 | HDMI 3 | Core-literal match |
| 17424 | 860562889 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::hdmi2` | HDMI 2 | HDMI 2 | Core-literal match |
| 17425 | 860562888 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::hdmi1` | HDMI 1 | HDMI 1 | Core-literal match |
| 17426 | 860562887 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::dtv_cable` | Digital TV (cable) | Digital-TV (kabel) | Core-literal match |
| 17427 | 860562886 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::dtv_antenna` | Digital TV (antenna) | Digital-TV (antenn) | Core-literal match |
| 17428 | 860562885 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::component3` | Component 3 | Komponent 3 | Core-literal match |
| 17429 | 860562884 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::component2` | Component 2 | Komponent 2 | Core-literal match |
| 17430 | 860562883 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::component1` | Component 1 | Komponent 1 | Core-literal match |
| 17431 | 860562882 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::av2` | AV 2 | AV 2 | Core-literal match |
| 17432 | 860562881 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::av1` | AV 1 | AV 1 | Core-literal match |
| 17433 | 860562880 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::analog_cable` | Analog (cable) | Analog (kabel) | Core-literal match |
| 17434 | 860562879 | `component::lg_tv_rs232::entity::media_player::tv::state_attributes::source::state::analog_antenna` | Analog (antenna) | Analog (antenn) | Core-literal match |
| 17435 | 860562878 | `component::lg_tv_rs232::config::step::user::data_description::set_id` | The set ID configured on the TV. Leave this at 1 unless you have multiple TVs daisy-chained on the same RS-232 bus. | Det set-ID som är konfigurerat på TV:n. Låt detta vara 1 om du inte har flera TV-apparater kopplade i serie på samma RS-232-buss. | Core-literal match |
| 17436 | 860562877 | `component::lg_tv_rs232::config::step::user::data_description::device` | Serial port path to connect to. The TV must be powered on for the initial connection. | Sökväg till den seriella porten som ska anslutas till. TV:n måste vara påslagen vid den första anslutningen. | Core-literal match |
| 17437 | 860562876 | `component::lg_tv_rs232::config::step::user::data::set_id` | Set ID | Ange ID | Core-literal match |
| 17438 | 860562875 | `component::lg_tv_rs232::config::step::user::data::device` | Port | Port | Shared reference target checked |
| 17439 | 860562874 | `component::lg_tv_rs232::config::step::troubleshoot::title` | Connection failed | Anslutningen misslyckades | Core-literal match |
| 17440 | 860562873 | `component::lg_tv_rs232::config::step::troubleshoot::description` | Home Assistant could not communicate with the LG TV over the serial port.<br><br>The most common cause is that **RS-232C Control** is not enabled on the TV. On most LG models this setting is in a hidden service menu (often called **InStart**); the exact location varies by model, so check your TV's documentation.<br><br>Also make sure that:<br>- The TV is powered on.<br>- The serial cable is a null-modem (cross-over) cable and is fully seated. LG's RS-232 jack is recessed, so push the plug in until it clicks.<br>- The correct serial port was selected.<br><br>Select **Submit** to try again. | Home Assistant kunde inte kommunicera med LG-TV:n via den seriella porten.<br><br>Den vanligaste orsaken är att **RS-232C-kontroll** inte är aktiverad på TV:n. På de flesta LG-modeller finns denna inställning i en dold servicemeny (ofta kallad **InStart**). Menyns exakta placeringen varierar beroende på modell, så kontrollera dokumentationen till din TV.<br><br>Se också till att:<br>- TV:n är påslagen.<br>- Den seriella kabeln är en nullmodemkabel (korsad kabel) och sitter i ordentligt. LG:s RS-232-uttag är infällt, så tryck in kontakten tills den klickar på plats.<br>- Rätt seriell port har valts.<br><br>Välj **Bekräfta** för att försöka igen. | Core-literal match |
| 17441 | 860562872 | `component::lg_tv_rs232::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 17442 | 860562871 | `component::lg_tv_rs232::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 17443 | 860562870 | `component::lg_tv_rs232::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 17444 | 860562734 | `component::opensensemap::issues::deprecated_yaml_import_issue_invalid_station::title` | The {integration_title} YAML configuration import failed | Importen av YAML-konfigurationen för {integration_title} misslyckades | Source-path follow-up open |
| 17445 | 860562733 | `component::opensensemap::issues::deprecated_yaml_import_issue_invalid_station::description` | Configuring {integration_title} using YAML is being removed but the configured station could not be found.<br><br>Verify the station ID and restart Home Assistant to try again or remove the {integration_title} YAML configuration from your configuration.yaml file and continue to set up the integration manually. | Konfigurationen av {integration_title} med YAML håller på att tas bort, men den konfigurerade stationen kunde inte hittas.<br><br>Kontrollera stationens ID och starta om Home Assistant för att försöka igen, eller ta bort YAML-konfigurationen för {integration_title} från din configuration.yaml-fil och fortsätt att ställa in integrationen manuellt. | Source-path follow-up open |
| 17446 | 860562732 | `component::opensensemap::issues::deprecated_yaml_import_issue_cannot_connect::title` | The {integration_title} YAML configuration import failed | Importen av YAML-konfigurationen för {integration_title} misslyckades | Source-path follow-up open |
| 17447 | 860562731 | `component::opensensemap::issues::deprecated_yaml_import_issue_cannot_connect::description` | Configuring {integration_title} using YAML is being removed but there was a connection error importing your YAML configuration.<br><br>Ensure connection to {integration_title} works and restart Home Assistant to try again or remove the {integration_title} YAML configuration from your configuration.yaml file and continue to set up the integration manually. | Konfigurationen av {integration_title} via YAML håller på att tas bort, men ett anslutningsfel uppstod vid importen av din YAML-konfiguration.<br><br>Kontrollera att anslutningen till {integration_title} fungerar och starta om Home Assistant för att försöka igen, eller ta bort YAML-konfigurationen för {integration_title} från din configuration.yaml-fil och fortsätt att konfigurera integrationen manuellt. | Source-path follow-up open |
| 17448 | 860562730 | `component::opensensemap::config::step::user::title` | Add openSenseMap station | Lägg till en openSenseMap-station | Core-literal match |
| 17449 | 860562729 | `component::opensensemap::config::step::user::description` | Add an openSenseMap station to monitor its measurements. | Lägg till en openSenseMap-station för att övervaka dess mätvärden. | Core-literal match |
| 17450 | 860562728 | `component::opensensemap::config::step::user::data_description::station_id` | The unique identifier of your openSenseMap station. You can find it in the URL when viewing the station on opensensemap.org. | Den unika identifieraren för din openSenseMap-station. Du hittar den i webbadressen när du visar stationen på opensensemap.org. | Core-literal match |
| 17451 | 860562727 | `component::opensensemap::config::step::user::data::station_id` | Station ID | Stations-ID | Core-literal match |
| 17452 | 860562726 | `component::opensensemap::config::error::invalid_station` | The provided station ID does not exist on openSenseMap. | Den angivna stations-ID:n finns inte på openSenseMap. | Shared reference target checked |
| 17453 | 860562725 | `component::opensensemap::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 17454 | 860562724 | `component::opensensemap::config::abort::invalid_station` | The provided station ID does not exist on openSenseMap. | Den angivna stations-ID:n finns inte på openSenseMap. | Core-literal match |
| 17455 | 860562723 | `component::opensensemap::config::abort::cannot_connect` | Failed to connect to openSenseMap. | Det gick inte att ansluta till openSenseMap. | Core-literal match |
| 17456 | 860562722 | `component::opensensemap::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Shared reference target checked |
| 17457 | 860562314 | `component::israel_rail::entity::sensor::trains2::name` | Trains +2 | Tåg +2 | Core-literal match |
| 17458 | 860562313 | `component::israel_rail::entity::sensor::trains1::name` | Trains +1 | Tåg +1 | Core-literal match |
| 17459 | 860562312 | `component::israel_rail::entity::sensor::train_number2::name` | Train number +2 | Tågnummer +2 | Core-literal match |
| 17460 | 860562311 | `component::israel_rail::entity::sensor::train_number1::name` | Train number +1 | Tågnummer +1 | Core-literal match |
| 17461 | 860562310 | `component::israel_rail::entity::sensor::platform2::name` | Platform +2 | Plattform +2 | Core-literal match |
| 17462 | 860562309 | `component::israel_rail::entity::sensor::platform1::name` | Platform +1 | Plattform +1 | Core-literal match |
| 17463 | 860562308 | `component::israel_rail::entity::sensor::departure_delay2::name` | Departure delay +2 | Avgångsförsening +2 | Core-literal match |
| 17464 | 860562307 | `component::israel_rail::entity::sensor::departure_delay1::name` | Departure delay +1 | Avgångsförsening +1 | Core-literal match |
| 17465 | 860562213 | `component::switchbot::entity::button::half_lock::name` | Half lock | Halvlås | Core-literal match |
| 17466 | 860562212 | `component::switchbot::entity::binary_sensor::half_locked::name` | Half locked | Halvlåst | Core-literal match |
| 17467 | 860562211 | `component::switchbot::entity::binary_sensor::half_lock_calibration::name` | Half-lock calibration | Halvlåskalibrering | Core-literal match |
| 17468 | 860561200 | `component::cert_expiry::config::step::user::data_description::port` | The port to connect to on the server. | Den port som du ska ansluta till på servern. | Core-literal match |
| 17469 | 860561199 | `component::cert_expiry::config::step::user::data_description::host` | The hostname or IP address of the server to monitor. | Värdnamnet eller IP-adressen för den server som ska övervakas. | Core-literal match |
| 17470 | 860561198 | `component::cert_expiry::config::step::reconfigure::data_description::port` | The port to connect to on the server. | Den port som du ska ansluta till på servern. | Core-literal match |
| 17471 | 860561197 | `component::cert_expiry::config::step::reconfigure::data_description::host` | The hostname or IP address of the server to monitor. | Värdnamnet eller IP-adressen för den server som ska övervakas. | Core-literal match |
| 17472 | 860561116 | `component::lyric::entity::select::room_priority::state::follow_me` | Follow me | Följ mig | Core-literal match |
| 17473 | 860561115 | `component::lyric::entity::select::room_priority::name` | Room priority | Rumsprioritet | Core-literal match |
| 17474 | 860561089 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::step::init::description` | Configure the conversation agent | Konfigurera konversationsagenten | Core-literal match |
| 17475 | 860561088 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::step::init::data_description::prompt` | Instruct how the LLM should respond. This can be a template. | Instruera hur LLM:en ska svara. Detta kan vara en mall. | Core-literal match |
| 17476 | 860561087 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::step::init::data_description::model` | The model to use for the conversation agent | Modellen som ska användas för konversationsagenten | Core-literal match |
| 17477 | 860561086 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::step::init::data_description::llm_hass_api` | **Device control** only accesses the entities you expose to voice assistants. **Home Assistant** accesses everything and only works for administrators, not voice assistant devices. | **Enhetsstyrning** har endast åtkomst till de entiteter som du exponerar för röstassistenter. **Home Assistant** har åtkomst till allt och fungerar endast för administratörer, inte för röstassistentenheter. | Shared reference target checked |
| 17478 | 860561085 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::step::init::data::prompt` | Instructions | Instruktioner | Shared reference target checked |
| 17479 | 860561084 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::step::init::data::model` | Model | Modell | Shared reference target checked |
| 17480 | 860561083 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::step::init::data::llm_hass_api` | AI tools | AI-verktyg | Shared reference target checked |
| 17481 | 860561082 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::initiate_flow::user` | Add conversation agent | Lägg till konversationsagent | Core-literal match |
| 17482 | 860561081 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::entry_type` | Conversation agent | Konversationsagent | Core-literal match |
| 17483 | 860561080 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::abort::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 17484 | 860561079 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::abort::entry_not_loaded` | The main integration entry is not loaded. Please ensure the integration is loaded before configuring. | Huvudintegrationsposten har inte laddats. Se till att integrationen är laddad innan konfigurering. | Core-literal match |
| 17485 | 860561078 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 17486 | 860561077 | `component::ovhcloud_ai_endpoints::config::step::user::data_description::api_key` | An OVHcloud AI Endpoints API key | En API-nyckel för OVHcloud AI Endpoints | Core-literal match |
| 17487 | 860561076 | `component::ovhcloud_ai_endpoints::config::step::user::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 17488 | 860561075 | `component::ovhcloud_ai_endpoints::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 17489 | 860561074 | `component::ovhcloud_ai_endpoints::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 17490 | 860561073 | `component::ovhcloud_ai_endpoints::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 17491 | 860561072 | `component::ovhcloud_ai_endpoints::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Shared reference target checked |
| 17492 | 860560404 | `component::duco::exceptions::unsupported_board::message` | This Duco system is not supported by this integration. The integration requires a Duco Connectivity Board running public API 2.1 or newer. | Det här Duco-systemet stöds inte av integrationen. Integrationen kräver ett Duco Connectivity Board med Public API 2.1 eller senare. | Shared reference target checked |
| 17493 | 860560403 | `component::duco::config::error::unsupported_board` | This Duco system is not supported by this integration. The integration requires a Duco Connectivity Board running public API 2.1 or newer. | Det här Duco-systemet stöds inte av integrationen. Integrationen kräver ett Duco Connectivity Board med Public API 2.1 eller senare. | Shared reference target checked |
| 17494 | 860560402 | `component::duco::config::abort::unsupported_board` | This Duco system is not supported by this integration. The integration requires a Duco Connectivity Board running public API 2.1 or newer. | Det här Duco-systemet stöds inte av integrationen. Integrationen kräver ett Duco Connectivity Board med Public API 2.1 eller senare. | Core-literal match |
| 17495 | 860560038 | `component::homee::exceptions::homeegram_turn_off_not_supported::message` | Turning off homeegrams is not supported. | Det går inte att stänga av Homeegram. | Core-literal match |
| 17496 | 860559952 | `component::ecobee::config::step::reauth_confirm::description` | Reauthenticate the ecobee account for **{username}**. | Återautentisera ecobee-kontot för **{username}**. | Core-literal match |
| 17497 | 860559951 | `component::ecobee::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 17498 | 860559950 | `component::ecobee::config::step::mfa::description` | ecobee requires multi-factor authentication. Enter the {mfa_type} code from your authenticator app. | ecobee kräver multifaktorautentisering. Ange koden ”{mfa_type}” från din autentiseringsapp. | Core-literal match |
| 17499 | 860559949 | `component::ecobee::config::step::mfa::data::code` | MFA code | MFA-kod | Core-literal match |
| 17500 | 860559948 | `component::ecobee::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 17501 | 860559947 | `component::ecobee::config::error::invalid_mfa_code` | The MFA code was not accepted by ecobee; please try again. | MFA-koden accepterades inte av ecobee. Försök igen. | Core-literal match |
| 17502 | 860559946 | `component::ecobee::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 17503 | 860559782 | `component::alexa_devices::entity::event::voice_event::state_attributes::event_type::state::triggered` | Triggered | Utlöst | Core-literal match |
| 17504 | 860559781 | `component::alexa_devices::entity::event::voice_event::name` | Voice event | Rösthändelse | Core-literal match |
| 17505 | 860557517 | `component::unifiprotect::entity::switch::detections_bark::name` | Barking detection | Detektioner: skällande | Shared reference target checked |
| 17506 | 860556949 | `component::system_bridge::selector::key::options::up` | Up | Upp | Shared reference target checked |
| 17507 | 860556948 | `component::system_bridge::selector::key::options::tab` | Tab | Tabb | Core-literal match |
| 17508 | 860556947 | `component::system_bridge::selector::key::options::space` | Space | Mellanslag | Core-literal match |
| 17509 | 860556946 | `component::system_bridge::selector::key::options::shift` | Shift | Shift | Core-literal match |
| 17510 | 860556945 | `component::system_bridge::selector::key::options::right_shift` | Shift right | Shift höger | Core-literal match |
| 17511 | 860556944 | `component::system_bridge::selector::key::options::right` | Right | Höger | Shared reference target checked |
| 17512 | 860556943 | `component::system_bridge::selector::key::options::printscreen` | Print screen | Print screen | Core-literal match |
| 17513 | 860556942 | `component::system_bridge::selector::key::options::pageup` | Page up | Page up | Core-literal match |
| 17514 | 860556941 | `component::system_bridge::selector::key::options::pagedown` | Page down | Page down | Core-literal match |
| 17515 | 860556940 | `component::system_bridge::selector::key::options::numpad_9` | NumPad 9 | NumPad 9 | Core-literal match |
| 17516 | 860556939 | `component::system_bridge::selector::key::options::numpad_8` | NumPad 8 | NumPad 8 | Core-literal match |
| 17517 | 860556938 | `component::system_bridge::selector::key::options::numpad_7` | NumPad 7 | NumPad 7 | Core-literal match |
| 17518 | 860556937 | `component::system_bridge::selector::key::options::numpad_6` | NumPad 6 | NumPad 6 | Core-literal match |
| 17519 | 860556936 | `component::system_bridge::selector::key::options::numpad_5` | NumPad 5 | NumPad 5 | Core-literal match |
| 17520 | 860556935 | `component::system_bridge::selector::key::options::numpad_4` | NumPad 4 | NumPad 4 | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 860562734 | `component::opensensemap::issues::deprecated_yaml_import_issue_invalid_station::title` | The {integration_title} YAML configuration import failed |
| 860562733 | `component::opensensemap::issues::deprecated_yaml_import_issue_invalid_station::description` | Configuring {integration_title} using YAML is being removed but the configured station could not be found.

Verify the station ID and restart Home Assistant to try again or remove the {integration_title} YAML configuration from your configuration.yaml file and continue to set up the integration manually. |
| 860562732 | `component::opensensemap::issues::deprecated_yaml_import_issue_cannot_connect::title` | The {integration_title} YAML configuration import failed |
| 860562731 | `component::opensensemap::issues::deprecated_yaml_import_issue_cannot_connect::description` | Configuring {integration_title} using YAML is being removed but there was a connection error importing your YAML configuration.

Ensure connection to {integration_title} works and restart Home Assistant to try again or remove the {integration_title} YAML configuration from your configuration.yaml file and continue to set up the integration manually. |
| 860559946 | `component::ecobee::config::abort::reauth_successful` | Re-authentication was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
