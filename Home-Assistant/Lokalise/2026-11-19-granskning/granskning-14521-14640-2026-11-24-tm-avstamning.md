# Home Assistant Core – historisk avstämning 14521–14640

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 72 direkta källtexter matchar HA Core-källan; 46 referensanvändningar med 29 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 2 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 14521 | 894675946 | `component::denon_rs232::exceptions::unsupported_media_type::message` | Cannot play media of type {media_type}. Only tuner channels are supported. | Kan inte spela media av typen {media_type}. Endast tuner-kanaler stöds. | Core-literal match |
| 14522 | 894675945 | `component::denon_rs232::exceptions::invalid_tuner_channel::message` | {media_id} is not a valid tuner preset (A1-G8) or FM frequency in hundredths of MHz (8750-10800; for example, 9930 for 99.30 MHz). | {media_id} är inte en giltig förinställning (A1-G8) eller FM-frekvens angiven i hundradels MHz (8750-10800; till exempel 9930 för 99,30 MHz). | Core-literal match |
| 14523 | 894521943 | `component::harbor::exceptions::cannot_connect::message` | Could not connect to the Harbor camera. It may be offline or unreachable. | Det gick inte att ansluta till Harbor-kameran. Den kan vara offline eller inte tillgänglig. | Core-literal match |
| 14524 | 894521942 | `component::harbor::entity::sensor::wifi_strength::unit_of_measurement` | bars | pinnar | Core-literal match |
| 14525 | 894521941 | `component::harbor::entity::sensor::wifi_strength::name` | Wi-Fi strength | Wi-Fi-styrka | Core-literal match |
| 14526 | 894521940 | `component::harbor::entity::sensor::stream_quality::state::poor` | Poor | Dålig | Core-literal match |
| 14527 | 894521939 | `component::harbor::entity::sensor::stream_quality::state::good` | Good | Bra | Core-literal match |
| 14528 | 894521938 | `component::harbor::entity::sensor::stream_quality::state::fair` | Fair | Tillräcklig | Core-literal match |
| 14529 | 894521937 | `component::harbor::entity::sensor::stream_quality::state::excellent` | Excellent | Utmärkt | Core-literal match |
| 14530 | 894521936 | `component::harbor::entity::sensor::stream_quality::name` | Stream quality | Strömningskvalitet | Core-literal match |
| 14531 | 894521935 | `component::harbor::entity::sensor::num_viewers::unit_of_measurement` | viewers | tittare | Core-literal match |
| 14532 | 894521934 | `component::harbor::entity::sensor::num_viewers::name` | Viewers | Tittare | Core-literal match |
| 14533 | 894521933 | `component::harbor::entity::sensor::bitrate::name` | Bitrate | Bit-rate | Core-literal match |
| 14534 | 894521932 | `component::harbor::config::step::user::title` | Set up Harbor | Ställ in Harbor | Core-literal match |
| 14535 | 894521931 | `component::harbor::config::step::user::data_description::serial` | The 10-digit serial number printed on the Harbor device. | Det 10-siffriga serienumret som finns på Harbor-enheten. | Core-literal match |
| 14536 | 894521930 | `component::harbor::config::step::user::data_description::key_pem` | Paste the private key that matches the client certificate. | Klistra in den privata nyckeln som matchar klientcertifikatet. | Core-literal match |
| 14537 | 894521929 | `component::harbor::config::step::user::data_description::ip_address` | The local IP address of the Harbor device. | Harbor-enhetens lokala IP-adress. | Core-literal match |
| 14538 | 894521928 | `component::harbor::config::step::user::data_description::cert_pem` | Paste the client certificate from the Harbor app. | Klistra in klientcertifikatet från Harbor-appen. | Core-literal match |
| 14539 | 894521927 | `component::harbor::config::step::user::data::serial` | Serial number | Serienummer | Core-literal match |
| 14540 | 894521926 | `component::harbor::config::step::user::data::key_pem` | Private key | Privat nyckel | Core-literal match |
| 14541 | 894521925 | `component::harbor::config::step::user::data::ip_address` | IP address | IP-adress | Shared reference target checked |
| 14542 | 894521924 | `component::harbor::config::step::user::data::cert_pem` | Client certificate | Klientcertifikat | Core-literal match |
| 14543 | 894521923 | `component::harbor::config::error::invalid_serial` | The serial number must be exactly 10 digits | Serienumret måste vara exakt 10 siffror långt | Core-literal match |
| 14544 | 894521922 | `component::harbor::config::error::invalid_key` | The private key must be a valid PEM private key | Den privata nyckeln måste vara en giltig privat nyckel i PEM-format | Core-literal match |
| 14545 | 894521921 | `component::harbor::config::error::invalid_cert` | The client certificate must be a valid PEM certificate | Klientcertifikatet måste vara ett giltigt PEM-certifikat | Core-literal match |
| 14546 | 894521920 | `component::harbor::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 14547 | 894521919 | `component::harbor::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 14548 | 894293139 | `component::vibration::conditions::is_not_detected::name` | Vibration is not detected | Ingen vibration detekterad | Core-literal match |
| 14549 | 894293138 | `component::vibration::conditions::is_not_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 14550 | 894293137 | `component::vibration::conditions::is_not_detected::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 14551 | 894293136 | `component::vibration::conditions::is_not_detected::description` | Tests if one or more vibration sensors are not detecting vibration. | Testar om en eller flera vibrationssensorer inte detekterar vibrationer. | Core-literal match |
| 14552 | 894293135 | `component::vibration::conditions::is_detected::name` | Vibration is detected | Vibration detekterad | Core-literal match |
| 14553 | 894293134 | `component::vibration::conditions::is_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 14554 | 894293133 | `component::vibration::conditions::is_detected::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 14555 | 894293132 | `component::vibration::conditions::is_detected::description` | Tests if one or more vibration sensors are detecting vibration. | Testar om en eller flera vibrationssensorer detekterar vibrationer. | Core-literal match |
| 14556 | 894293131 | `component::vibration::common::condition_for_name` | For at least | I minst | Core-literal match |
| 14557 | 894293130 | `component::vibration::common::condition_behavior_name` | Condition passes if | Villkoret uppfylls om | Core-literal match |
| 14558 | 894285412 | `component::litellm::config_subentries::conversation::step::init::description` | Configure the conversation agent | Konfigurera konversationsagenten | Core-literal match |
| 14559 | 894285411 | `component::litellm::config_subentries::conversation::step::init::data_description::prompt` | Instruct how the LLM should respond. This can be a template. | Instruera hur LLM ska svara. Detta kan vara en mall. | Core-literal match |
| 14560 | 894285410 | `component::litellm::config_subentries::conversation::step::init::data_description::model` | The model to use for the conversation agent | Den modell som konversationsagenten ska använda | Core-literal match |
| 14561 | 894285409 | `component::litellm::config_subentries::conversation::step::init::data_description::llm_hass_api` | **Device control** only accesses the entities you expose to voice assistants. **Home Assistant** accesses everything and only works for administrators, not voice assistant devices. | **Enhetsstyrning** har endast åtkomst till de entiteter som du exponerar för röstassistenter. **Home Assistant** har åtkomst till allt och fungerar endast för administratörer, inte för röstassistentenheter. | Shared reference target checked |
| 14562 | 894285408 | `component::litellm::config_subentries::conversation::step::init::data::prompt` | Instructions | Instruktioner | Shared reference target checked |
| 14563 | 894285407 | `component::litellm::config_subentries::conversation::step::init::data::model` | Model | Modell | Shared reference target checked |
| 14564 | 894285406 | `component::litellm::config_subentries::conversation::step::init::data::llm_hass_api` | AI tools | AI-verktyg | Shared reference target checked |
| 14565 | 894285405 | `component::litellm::config_subentries::conversation::initiate_flow::user` | Add conversation agent | Lägg till konversationsagent | Core-literal match |
| 14566 | 894285404 | `component::litellm::config_subentries::conversation::initiate_flow::reconfigure` | Reconfigure conversation agent | Konfigurera om konversationsagenten | Core-literal match |
| 14567 | 894285403 | `component::litellm::config_subentries::conversation::entry_type` | Conversation agent | Konversationsagent | Core-literal match |
| 14568 | 894285402 | `component::litellm::config_subentries::conversation::abort::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 14569 | 894285401 | `component::litellm::config_subentries::conversation::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 14570 | 894285400 | `component::litellm::config_subentries::conversation::abort::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 14571 | 894285399 | `component::litellm::config_subentries::conversation::abort::entry_not_loaded` | The main integration entry is not loaded. Please ensure the integration is loaded before reconfiguring. | Huvudintegrationsposten har inte laddats. Se till att integrationen är laddad innan du konfigurerar om. | Core-literal match |
| 14572 | 894285398 | `component::litellm::config_subentries::conversation::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 14573 | 894285397 | `component::litellm::config::step::user::data_description::url` | The base URL of your LiteLLM proxy, including the host and port | Bas-URL:en för din LiteLLM-proxy, inklusive värd och port | Core-literal match |
| 14574 | 894285396 | `component::litellm::config::step::user::data_description::api_key` | An optional LiteLLM API key or virtual key. Leave empty if your proxy does not require authentication. | En valfri LiteLLM API-nyckel eller virtuell nyckel. Lämna tomt om din proxy inte kräver autentisering. | Core-literal match |
| 14575 | 894285395 | `component::litellm::config::step::user::data::url` | URL | URL | Shared reference target checked |
| 14576 | 894285394 | `component::litellm::config::step::user::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 14577 | 894285393 | `component::litellm::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 14578 | 894285392 | `component::litellm::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 14579 | 894285391 | `component::litellm::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 14580 | 894285390 | `component::litellm::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Shared reference target checked |
| 14581 | 894252268 | `component::gatus::config::step::reconfigure::description` | Enter the network details for your Gatus status page instance. Make sure to include the protocol (e.g., `http://` or `https://`) and the port number if you are not using a standard port. | Ange nätverksinformationen för din Gatus status sidans instans. Se till att inkludera protokollet (t.ex. `http://` eller `https://`) och portnumret om du inte använder en standardport. | Shared reference target checked |
| 14582 | 894252267 | `component::gatus::config::step::reconfigure::data_description::url` | The full base URL of your Gatus status page instance including protocol and port. | Den fullständiga bas-URL:en för din Gatus-statussidesinstans, inklusive protokoll och port. | Shared reference target checked |
| 14583 | 894252266 | `component::gatus::config::step::reconfigure::data::url` | URL | URL | Shared reference target checked |
| 14584 | 894252265 | `component::gatus::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 14585 | 894091991 | `component::knx::config_panel::project::group_addresses::title` | Group addresses | Gruppadresser | Shared reference target checked |
| 14586 | 894091990 | `component::knx::config_panel::project::devices::title` | Devices | Enheter | Core-literal match |
| 14587 | 894091989 | `component::knx::config_panel::project::devices::not_found` | No devices found in project data. | Inga enheter hittades i projektdata. | Core-literal match |
| 14588 | 894091988 | `component::knx::config_panel::project::devices::locations` | Locations | Platser | Core-literal match |
| 14589 | 894091987 | `component::knx::config_panel::project::devices::lines` | Lines | Rader | Core-literal match |
| 14590 | 894091986 | `component::knx::config_panel::project::devices::group_objects` | Group objects | Gruppera objekt | Core-literal match |
| 14591 | 894091985 | `component::knx::config_panel::project::devices::channels` | Channels | Kanaler | Core-literal match |
| 14592 | 893987957 | `component::whirlpool::issues::deprecated_oven_target_temperature_scripts::title` | The Whirlpool oven target temperature sensor is deprecated | Whirlpool-ugnens måltemperatursensor är föråldrad | Shared reference target checked |
| 14593 | 893987956 | `component::whirlpool::issues::deprecated_oven_target_temperature_scripts::description` | The `{entity_id}` ({entity_name}) sensor is deprecated and has been replaced by the **Target temperature** number entity, which can both read and change the oven target temperature.<br><br>It is still used in the following automations or scripts:<br>{items}<br><br>Update them to use the new number entity, then disable `{entity_id}` to have it removed. | Sensorn `{entity_id}` ({entity_name}) är föråldrad och har ersatts av **Måltemperatur**-entiteten, som både kan läsa och ändra ugnens måltemperatur.<br><br>Sensorn används fortfarande i följande automatiseringar eller skript:<br>{items}<br><br>Uppdatera dem för att använda den nya entiteten och inaktivera sedan `{entity_id}` för att lösa problemet. | Core-literal match |
| 14594 | 893987955 | `component::whirlpool::issues::deprecated_oven_target_temperature::title` | The Whirlpool oven target temperature sensor is deprecated | Whirlpool-ugnens måltemperatursensor är föråldrad | Core-literal match |
| 14595 | 893987954 | `component::whirlpool::issues::deprecated_oven_target_temperature::description` | The `{entity_id}` ({entity_name}) sensor is deprecated and has been replaced by the **Target temperature** number entity, which can both read and change the oven target temperature.<br><br>Update any dashboards, templates, automations or scripts to use the new number entity, then disable `{entity_id}` to have it removed. | Sensorn `{entity_id}` ({entity_name}) är föråldrad och har ersatts av **Måltemperatur**-entiteten, som både kan läsa och ändra ugnens måltemperatur.<br><br>Uppdatera alla kontrollpaneler, mallar, automatiseringar och skript för att använda den nya nummerentiteten och inaktivera sedan `{entity_id}` för att lösa problemet. | Core-literal match |
| 14596 | 893987953 | `component::whirlpool::entity::number::oven_target_temperature_upper::name` | Upper oven target temperature | Övre ugnens måltemperatur | Core-literal match |
| 14597 | 893987952 | `component::whirlpool::entity::number::oven_target_temperature_lower::name` | Lower oven target temperature | Nedre ugnens måltemperatur | Core-literal match |
| 14598 | 893987951 | `component::whirlpool::entity::number::oven_target_temperature::name` | Target temperature | Måltemperatur | Core-literal match |
| 14599 | 893985752 | `component::lg_thinq::exceptions::connection_error::message` | Failed to connect to the LG ThinQ cloud. Please try again later. | Misslyckades med att ansluta till LG ThinQ-molnet. Försök igen senare. | Core-literal match |
| 14600 | 893982323 | `component::victron_gx::entity::sensor::system_pv_on_grid_power_phase::name` | PV on grid power {phase} | PV på elnät effekt {phase} | Core-literal match |
| 14601 | 893982322 | `component::victron_gx::entity::sensor::system_pv_on_grid_phases::unit_of_measurement` | phases | faser | Core-literal match |
| 14602 | 893982321 | `component::victron_gx::entity::sensor::system_pv_on_grid_phases::name` | PV on grid phases | PV på elnät faser | Core-literal match |
| 14603 | 893982320 | `component::victron_gx::entity::sensor::system_pv_on_grid_current_phase::name` | PV on grid current {phase} | PV på elnät ström {phase} | Core-literal match |
| 14604 | 893982319 | `component::victron_gx::entity::select::battery_bms_mode::state::standby` | Standby | Viloläge | Shared reference target checked |
| 14605 | 893982318 | `component::victron_gx::entity::select::battery_bms_mode::state::on` | On | På | Shared reference target checked |
| 14606 | 893982317 | `component::victron_gx::entity::select::battery_bms_mode::state::off` | Off | Av | Shared reference target checked |
| 14607 | 893483022 | `component::google_health::entity::sensor::total_calories::name` | Total calories | Totalt antal kalorier | Core-literal match |
| 14608 | 893483021 | `component::google_health::entity::sensor::floors::name` | Floors | Våningar | Core-literal match |
| 14609 | 893483020 | `component::google_health::entity::sensor::body_fat::name` | Body fat | Kroppsfett | Core-literal match |
| 14610 | 893483019 | `component::google_health::entity::sensor::active_calories::name` | Active calories | Aktiva kalorier | Core-literal match |
| 14611 | 893242138 | `component::whirlpool::issues::deprecated_oven_cook_mode_scripts::title` | The Whirlpool oven cook mode sensor is deprecated | Whirlpool-ugnens tillagningslägessensor är föråldrad | Shared reference target checked |
| 14612 | 893242137 | `component::whirlpool::issues::deprecated_oven_cook_mode_scripts::description` | The `{entity_id}` ({entity_name}) sensor is deprecated and has been replaced by the **Cook mode** select entity, which can both read and change the oven cook mode.<br><br>It is still used in the following automations or scripts:<br>{items}<br><br>Update them to use the new select entity, then disable `{entity_id}` to have it removed. | Sensorentiteten `{entity_id}` ({entity_name}) är föråldrad och har ersatts av valentiteten **Tillagningsläge**, som både kan läsa och ändra ugnens tillagningsläge.<br><br>Den används fortfarande i följande automatiseringar eller skript:<br>{items}<br><br>Uppdatera dem så att de använder den nya valenheten. Inaktivera sedan `{entity_id}` för att ta bort den. | Core-literal match |
| 14613 | 893242136 | `component::whirlpool::issues::deprecated_oven_cook_mode::title` | The Whirlpool oven cook mode sensor is deprecated | Whirlpool-ugnens tillagningslägessensor är föråldrad | Core-literal match |
| 14614 | 893242135 | `component::whirlpool::issues::deprecated_oven_cook_mode::description` | The `{entity_id}` ({entity_name}) sensor is deprecated and has been replaced by the **Cook mode** select entity, which can both read and change the oven cook mode.<br><br>Update any dashboards, templates, automations or scripts to use the new select entity, then disable `{entity_id}` to have it removed. | Sensorentiteten `{entity_id}` ({entity_name}) är föråldrad och har ersatts av valentiteten **Tillagningsläge**, som både kan läsa och ändra ugnens tillagningsläge.<br><br>Uppdatera instrumentpaneler, mallar, automatiseringar och skript så att de använder den nya valenheten. Inaktivera sedan `{entity_id}` för att ta bort den. | Core-literal match |
| 14615 | 893242134 | `component::whirlpool::entity::select::oven_cook_mode_upper::state::standby` | Standby | Viloläge | Shared reference target checked |
| 14616 | 893242133 | `component::whirlpool::entity::select::oven_cook_mode_upper::state::keep_warm` | Keep warm | Varmhållning | Shared reference target checked |
| 14617 | 893242132 | `component::whirlpool::entity::select::oven_cook_mode_upper::state::convection_roast` | Convection roast | Konvektionsstekning | Shared reference target checked |
| 14618 | 893242131 | `component::whirlpool::entity::select::oven_cook_mode_upper::state::convection_broil` | Convection broil | Konvektionsgrillning | Shared reference target checked |
| 14619 | 893242130 | `component::whirlpool::entity::select::oven_cook_mode_upper::state::convection_bake` | Convection bake | Konvektionsbakning | Shared reference target checked |
| 14620 | 893242129 | `component::whirlpool::entity::select::oven_cook_mode_upper::state::broil` | Broil | Grilla | Shared reference target checked |
| 14621 | 893242128 | `component::whirlpool::entity::select::oven_cook_mode_upper::state::bake` | Bake | Grädda | Shared reference target checked |
| 14622 | 893242127 | `component::whirlpool::entity::select::oven_cook_mode_upper::state::air_fry` | Air fry | Luftfritering | Shared reference target checked |
| 14623 | 893242126 | `component::whirlpool::entity::select::oven_cook_mode_upper::name` | Upper oven cook mode | Tillagningsläge för övre ugnen | Core-literal match |
| 14624 | 893242125 | `component::whirlpool::entity::select::oven_cook_mode_lower::state::standby` | Standby | Viloläge | Shared reference target checked |
| 14625 | 893242124 | `component::whirlpool::entity::select::oven_cook_mode_lower::state::keep_warm` | Keep warm | Varmhållning | Shared reference target checked |
| 14626 | 893242123 | `component::whirlpool::entity::select::oven_cook_mode_lower::state::convection_roast` | Convection roast | Konvektionsstekning | Shared reference target checked |
| 14627 | 893242122 | `component::whirlpool::entity::select::oven_cook_mode_lower::state::convection_broil` | Convection broil | Konvektionsgrillning | Shared reference target checked |
| 14628 | 893242121 | `component::whirlpool::entity::select::oven_cook_mode_lower::state::convection_bake` | Convection bake | Konvektionsbakning | Shared reference target checked |
| 14629 | 893242120 | `component::whirlpool::entity::select::oven_cook_mode_lower::state::broil` | Broil | Grilla | Shared reference target checked |
| 14630 | 893242119 | `component::whirlpool::entity::select::oven_cook_mode_lower::state::bake` | Bake | Grädda | Shared reference target checked |
| 14631 | 893242118 | `component::whirlpool::entity::select::oven_cook_mode_lower::state::air_fry` | Air fry | Luftfritering | Shared reference target checked |
| 14632 | 893242117 | `component::whirlpool::entity::select::oven_cook_mode_lower::name` | Lower oven cook mode | Tillagningsläge för nedre ugnen | Core-literal match |
| 14633 | 893242116 | `component::whirlpool::entity::select::oven_cook_mode::state::standby` | Standby | Viloläge | Shared reference target checked |
| 14634 | 893242115 | `component::whirlpool::entity::select::oven_cook_mode::state::keep_warm` | Keep warm | Varmhållning | Core-literal match |
| 14635 | 893242114 | `component::whirlpool::entity::select::oven_cook_mode::state::convection_roast` | Convection roast | Konvektionsstekning | Core-literal match |
| 14636 | 893242113 | `component::whirlpool::entity::select::oven_cook_mode::state::convection_broil` | Convection broil | Konvektionsgrillning | Core-literal match |
| 14637 | 893242112 | `component::whirlpool::entity::select::oven_cook_mode::state::convection_bake` | Convection bake | Konvektionsbakning | Core-literal match |
| 14638 | 893242111 | `component::whirlpool::entity::select::oven_cook_mode::state::broil` | Broil | Grilla | Core-literal match |
| 14639 | 893242110 | `component::whirlpool::entity::select::oven_cook_mode::state::bake` | Bake | Grädda | Core-literal match |
| 14640 | 893242109 | `component::whirlpool::entity::select::oven_cook_mode::state::air_fry` | Air fry | Luftfritering | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 894285401 | `component::litellm::config_subentries::conversation::abort::reconfigure_successful` | Reconfiguration was successful |
| 894252265 | `component::gatus::config::abort::reconfigure_successful` | Reconfiguration was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
