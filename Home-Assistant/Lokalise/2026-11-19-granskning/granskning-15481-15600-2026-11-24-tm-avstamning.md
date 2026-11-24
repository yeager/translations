# Home Assistant Core – historisk avstämning 15481–15600

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 56 direkta källtexter matchar HA Core-källan; 62 referensanvändningar med 31 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 2 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 15481 | 886190092 | `component::llama_cpp::exceptions::api_error::message` | API error: {message}. | API-fel: {message} | Core-literal match |
| 15482 | 886190091 | `component::llama_cpp::config_subentries::conversation::step::init::data_description::top_p` | Select the top P value for response diversity. | Välj det högsta P-värdet för variationen i svaren. | Core-literal match |
| 15483 | 886190090 | `component::llama_cpp::config_subentries::conversation::step::init::data_description::temperature` | Select the temperature for response variability. | Välj temperatur för variationen i responsen. | Core-literal match |
| 15484 | 886190089 | `component::llama_cpp::config_subentries::conversation::step::init::data_description::recommended` | Select whether to use recommended model settings. | Välj om rekommenderade modellinställningar ska användas. | Core-literal match |
| 15485 | 886190088 | `component::llama_cpp::config_subentries::conversation::step::init::data_description::prompt` | Instruct how the LLM should respond. This can be a template. | Instruera hur LLM:en ska svara. Detta kan vara en mall. | Core-literal match |
| 15486 | 886190087 | `component::llama_cpp::config_subentries::conversation::step::init::data_description::max_tokens` | Select the maximum number of tokens to return. | Välj det maximala antalet tokens som ska returneras. | Core-literal match |
| 15487 | 886190086 | `component::llama_cpp::config_subentries::conversation::step::init::data_description::llm_hass_api` | **Device control** only accesses the entities you expose to voice assistants. **Home Assistant** accesses everything and only works for administrators, not voice assistant devices. | **Enhetsstyrning** har endast åtkomst till de entiteter som du exponerar för röstassistenter. **Home Assistant** har åtkomst till allt och fungerar endast för administratörer, inte för röstassistentenheter. | Shared reference target checked |
| 15488 | 886190085 | `component::llama_cpp::config_subentries::conversation::step::init::data_description::chat_model` | Select the model to use. | Välj den modell som ska användas. | Core-literal match |
| 15489 | 886190084 | `component::llama_cpp::config_subentries::conversation::step::init::data::top_p` | Top P | Top P | Core-literal match |
| 15490 | 886190083 | `component::llama_cpp::config_subentries::conversation::step::init::data::temperature` | Temperature | Temperatur | Core-literal match |
| 15491 | 886190082 | `component::llama_cpp::config_subentries::conversation::step::init::data::recommended` | Recommended model settings | Rekommenderade modellinställningar | Core-literal match |
| 15492 | 886190081 | `component::llama_cpp::config_subentries::conversation::step::init::data::prompt` | Instructions | Instruktioner | Shared reference target checked |
| 15493 | 886190080 | `component::llama_cpp::config_subentries::conversation::step::init::data::name` | Name | Namn | Shared reference target checked |
| 15494 | 886190079 | `component::llama_cpp::config_subentries::conversation::step::init::data::max_tokens` | Maximum tokens to return in response | Maximalt antal tokens att returnera i svar | Core-literal match |
| 15495 | 886190078 | `component::llama_cpp::config_subentries::conversation::step::init::data::llm_hass_api` | AI tools | AI-verktyg | Shared reference target checked |
| 15496 | 886190077 | `component::llama_cpp::config_subentries::conversation::step::init::data::chat_model` | Model | Modell | Shared reference target checked |
| 15497 | 886190076 | `component::llama_cpp::config_subentries::conversation::initiate_flow::user` | Add conversation agent | Lägg till konversationsagent | Core-literal match |
| 15498 | 886190075 | `component::llama_cpp::config_subentries::conversation::entry_type` | Conversation agent | Konversationsagent | Core-literal match |
| 15499 | 886190074 | `component::llama_cpp::config_subentries::conversation::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 15500 | 886190073 | `component::llama_cpp::config_subentries::conversation::abort::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 15501 | 886190072 | `component::llama_cpp::config_subentries::conversation::abort::entry_not_loaded` | Cannot add things while the configuration is disabled. | Det går inte att lägga till saker när konfigurationen är inaktiverad. | Core-literal match |
| 15502 | 886190071 | `component::llama_cpp::config_subentries::conversation::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15503 | 886190070 | `component::llama_cpp::config::step::user::data_description::base_url` | Base URL of your running OpenAI-compatible server (e.g. http://localhost:8080/v1). | Bas-URL för din aktiva OpenAI-kompatibla server (t.ex. http://localhost:8080/v1). | Core-literal match |
| 15504 | 886190069 | `component::llama_cpp::config::step::user::data_description::api_key` | API key for the server (optional). | API-nyckel för servern (valfritt). | Core-literal match |
| 15505 | 886190068 | `component::llama_cpp::config::step::user::data::base_url` | URL | URL | Shared reference target checked |
| 15506 | 886190067 | `component::llama_cpp::config::step::user::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 15507 | 886190066 | `component::llama_cpp::config::step::model::data_description::chat_model` | Select the model to use. | Välj den modell som ska användas. | Core-literal match |
| 15508 | 886190065 | `component::llama_cpp::config::step::model::data::chat_model` | Model | Modell | Shared reference target checked |
| 15509 | 886190064 | `component::llama_cpp::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 15510 | 886190063 | `component::llama_cpp::config::error::timeout` | Connection timed out. | Tidsgränsen för anslutningen har överskridits. | Core-literal match |
| 15511 | 886190062 | `component::llama_cpp::config::error::quota_exceeded` | Your account or API key has insufficient credits. | Ditt konto eller din API-nyckel har otillräckliga krediter. | Core-literal match |
| 15512 | 886190061 | `component::llama_cpp::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 15513 | 886190060 | `component::llama_cpp::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15514 | 886190059 | `component::llama_cpp::config::error::api_error` | Unexpected error | Oväntat fel | Shared reference target checked |
| 15515 | 886190058 | `component::llama_cpp::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Shared reference target checked |
| 15516 | 886180628 | `component::media_source::exceptions::search_not_supported::message` | Search is not supported for media with content ID {media_content_id} | Sökning stöds inte för media med innehålls-ID {media_content_id} | Core-literal match |
| 15517 | 886180627 | `component::media_source::exceptions::search_media_failed::message` | Failed to search media with content ID {media_content_id}: {error} | Det gick inte att söka efter media med innehålls-ID {media_content_id}: {error} | Core-literal match |
| 15518 | 886178107 | `component::nextcloud::config::step::config::description` | Enter your Nextcloud information. | Ange din Nextcloud-information. | Core-literal match |
| 15519 | 886178106 | `component::nextcloud::config::step::config::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 15520 | 886178105 | `component::nextcloud::config::step::config::data::username` | Username | Användarnamn | Shared reference target checked |
| 15521 | 886178104 | `component::nextcloud::config::step::config::data::url` | URL | URL | Shared reference target checked |
| 15522 | 886178103 | `component::nextcloud::config::step::config::data::password` | Password | Lösenord | Shared reference target checked |
| 15523 | 886178102 | `component::nextcloud::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 15524 | 886174416 | `component::teslemetry::entity::select::climate_state_seat_fan_front_right::state::off` | Off | Av | Shared reference target checked |
| 15525 | 886174415 | `component::teslemetry::entity::select::climate_state_seat_fan_front_right::state::medium` | Medium | Medel | Shared reference target checked |
| 15526 | 886174414 | `component::teslemetry::entity::select::climate_state_seat_fan_front_right::state::low` | Low | Låg | Shared reference target checked |
| 15527 | 886174413 | `component::teslemetry::entity::select::climate_state_seat_fan_front_right::state::high` | High | Hög | Shared reference target checked |
| 15528 | 886174412 | `component::teslemetry::entity::select::climate_state_seat_fan_front_right::name` | Seat cooler front right | Säteskylare fram höger | Core-literal match |
| 15529 | 886174411 | `component::teslemetry::entity::select::climate_state_seat_fan_front_left::state::off` | Off | Av | Shared reference target checked |
| 15530 | 886174410 | `component::teslemetry::entity::select::climate_state_seat_fan_front_left::state::medium` | Medium | Medel | Shared reference target checked |
| 15531 | 886174409 | `component::teslemetry::entity::select::climate_state_seat_fan_front_left::state::low` | Low | Låg | Shared reference target checked |
| 15532 | 886174408 | `component::teslemetry::entity::select::climate_state_seat_fan_front_left::state::high` | High | Hög | Shared reference target checked |
| 15533 | 886174407 | `component::teslemetry::entity::select::climate_state_seat_fan_front_left::name` | Seat cooler front left | Säteskylare fram vänster | Core-literal match |
| 15534 | 886151065 | `component::infrared::entity_component::emitter::name` | Infrared emitter | Infraröd sändare | Core-literal match |
| 15535 | 886120656 | `component::victron_gx::entity::switch::system_dvcc::name` | DVCC | DVCC | Core-literal match |
| 15536 | 886120655 | `component::victron_gx::entity::sensor::system_dvcc_state::state::on` | On | På | Shared reference target checked |
| 15537 | 886120654 | `component::victron_gx::entity::sensor::system_dvcc_state::state::off` | Off | Av | Shared reference target checked |
| 15538 | 886120653 | `component::victron_gx::entity::sensor::system_dvcc_state::state::forced_on` | Forced on | Forcerad på | Core-literal match |
| 15539 | 886120652 | `component::victron_gx::entity::sensor::system_dvcc_state::state::forced_off` | Forced off | Forcerad av | Core-literal match |
| 15540 | 886120651 | `component::victron_gx::entity::sensor::system_dvcc_state::name` | DVCC state | DVCC tillstånd | Core-literal match |
| 15541 | 886120650 | `component::victron_gx::entity::sensor::ev_vin::name` | VIN | VIN | Core-literal match |
| 15542 | 886120649 | `component::victron_gx::entity::sensor::ev_target_soc::name` | Target state of charge | Målladdningsnivå | Core-literal match |
| 15543 | 886120648 | `component::victron_gx::entity::sensor::ev_soc::name` | State of charge | Laddningsnivå (SOC) | Core-literal match |
| 15544 | 886120647 | `component::victron_gx::entity::sensor::ev_range_to_go::name` | Range to go | Återstående räckvidd | Core-literal match |
| 15545 | 886120646 | `component::victron_gx::entity::sensor::ev_odometer::name` | Odometer | Mätarställning | Core-literal match |
| 15546 | 886120645 | `component::victron_gx::entity::sensor::ev_last_ev_contact::name` | Last EV contact | Senaste kontakt med EV | Core-literal match |
| 15547 | 886120644 | `component::victron_gx::entity::sensor::ev_dc_voltage::name` | DC voltage | DC-spänning | Shared reference target checked |
| 15548 | 886120643 | `component::victron_gx::entity::sensor::ev_dc_power::name` | DC power | DC-effekt | Shared reference target checked |
| 15549 | 886120642 | `component::victron_gx::entity::sensor::ev_dc_current::name` | DC current | DC-ström | Shared reference target checked |
| 15550 | 886120641 | `component::victron_gx::entity::sensor::ev_charging_state::state::wake_up` | Wake up | Vakna upp | Core-literal match |
| 15551 | 886120640 | `component::victron_gx::entity::sensor::ev_charging_state::state::unavailable` | Unavailable | Otillgänglig | Core-literal match |
| 15552 | 886120639 | `component::victron_gx::entity::sensor::ev_charging_state::state::sustain` | Sustain | Sustain | Shared reference target checked |
| 15553 | 886120638 | `component::victron_gx::entity::sensor::ev_charging_state::state::scheduled_charging` | Scheduled charging | Schemalagd laddning | Core-literal match |
| 15554 | 886120637 | `component::victron_gx::entity::sensor::ev_charging_state::state::not_charging` | Not charging | Laddar inte | Core-literal match |
| 15555 | 886120636 | `component::victron_gx::entity::sensor::ev_charging_state::state::low_power_mode` | Low power mode | Lågeffektsläge | Core-literal match |
| 15556 | 886120635 | `component::victron_gx::entity::sensor::ev_charging_state::state::discharging` | Discharging | Laddar ur | Shared reference target checked |
| 15557 | 886120634 | `component::victron_gx::entity::sensor::ev_charging_state::state::charging` | Charging | Laddar | Shared reference target checked |
| 15558 | 886120633 | `component::victron_gx::entity::sensor::ev_charging_state::state::blocked` | Blocked | Blockerad | Core-literal match |
| 15559 | 886120632 | `component::victron_gx::entity::sensor::ev_charging_state::name` | Charging state | Laddningsstatus | Core-literal match |
| 15560 | 886120631 | `component::victron_gx::entity::sensor::ev_charging_started::name` | Charging started | Laddning startade | Core-literal match |
| 15561 | 886120630 | `component::victron_gx::entity::sensor::ev_battery_temperature::name` | Battery temperature | Batteritemperatur | Core-literal match |
| 15562 | 886120629 | `component::victron_gx::entity::sensor::ev_battery_capacity::name` | Battery capacity | Batterikapacitet | Core-literal match |
| 15563 | 886120628 | `component::victron_gx::entity::sensor::ev_alarm_starter_battery_low::state::warning` | Warning | Varning | Shared reference target checked |
| 15564 | 886120627 | `component::victron_gx::entity::sensor::ev_alarm_starter_battery_low::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 15565 | 886120626 | `component::victron_gx::entity::sensor::ev_alarm_starter_battery_low::state::alarm` | Alarm | Larm | Shared reference target checked |
| 15566 | 886120625 | `component::victron_gx::entity::sensor::ev_alarm_starter_battery_low::name` | Starter battery low | Startbatteri lågt | Core-literal match |
| 15567 | 886120624 | `component::victron_gx::entity::sensor::ev_ac_voltage::name` | AC voltage | AC-spänning | Core-literal match |
| 15568 | 886120623 | `component::victron_gx::entity::sensor::ev_ac_power::name` | AC power | AC-effekt | Core-literal match |
| 15569 | 886120622 | `component::victron_gx::entity::sensor::ev_ac_nr_of_phases::name` | Number of phases | Antal faser | Shared reference target checked |
| 15570 | 886120621 | `component::victron_gx::entity::sensor::ev_ac_min_charge_current::name` | Min charge current | Minsta laddningsström | Core-literal match |
| 15571 | 886120620 | `component::victron_gx::entity::sensor::ev_ac_max_charge_current::name` | Max charge current | Max laddningsström | Core-literal match |
| 15572 | 886120619 | `component::victron_gx::entity::sensor::ev_ac_energy_forward::name` | Total energy | Total energi | Shared reference target checked |
| 15573 | 886120618 | `component::victron_gx::entity::sensor::ev_ac_current::name` | AC current | AC-ström | Core-literal match |
| 15574 | 886120617 | `component::victron_gx::entity::sensor::battery_state_of_health_alarm::state::warning` | Warning | Varning | Shared reference target checked |
| 15575 | 886120616 | `component::victron_gx::entity::sensor::battery_state_of_health_alarm::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 15576 | 886120615 | `component::victron_gx::entity::sensor::battery_state_of_health_alarm::state::alarm` | Alarm | Larm | Shared reference target checked |
| 15577 | 886120614 | `component::victron_gx::entity::sensor::battery_state_of_health_alarm::name` | State of health alarm | Larm om hälsotillstånd | Core-literal match |
| 15578 | 886120613 | `component::victron_gx::entity::sensor::battery_low_voltage::state::warning` | Warning | Varning | Shared reference target checked |
| 15579 | 886120612 | `component::victron_gx::entity::sensor::battery_low_voltage::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 15580 | 886120611 | `component::victron_gx::entity::sensor::battery_low_voltage::state::alarm` | Alarm | Larm | Shared reference target checked |
| 15581 | 886120610 | `component::victron_gx::entity::sensor::battery_low_voltage::name` | Low voltage | Lågspänning | Core-literal match |
| 15582 | 886120609 | `component::victron_gx::entity::sensor::battery_low_temperature::state::warning` | Warning | Varning | Shared reference target checked |
| 15583 | 886120608 | `component::victron_gx::entity::sensor::battery_low_temperature::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 15584 | 886120607 | `component::victron_gx::entity::sensor::battery_low_temperature::state::alarm` | Alarm | Larm | Shared reference target checked |
| 15585 | 886120606 | `component::victron_gx::entity::sensor::battery_low_temperature::name` | Low temperature | Låg temperatur | Shared reference target checked |
| 15586 | 886120605 | `component::victron_gx::entity::sensor::battery_low_soc::state::warning` | Warning | Varning | Shared reference target checked |
| 15587 | 886120604 | `component::victron_gx::entity::sensor::battery_low_soc::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 15588 | 886120603 | `component::victron_gx::entity::sensor::battery_low_soc::state::alarm` | Alarm | Larm | Shared reference target checked |
| 15589 | 886120602 | `component::victron_gx::entity::sensor::battery_low_soc::name` | Low state of charge | Låg laddningsnivå | Core-literal match |
| 15590 | 886120601 | `component::victron_gx::entity::sensor::battery_high_voltage::state::warning` | Warning | Varning | Shared reference target checked |
| 15591 | 886120600 | `component::victron_gx::entity::sensor::battery_high_voltage::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 15592 | 886120599 | `component::victron_gx::entity::sensor::battery_high_voltage::state::alarm` | Alarm | Larm | Shared reference target checked |
| 15593 | 886120598 | `component::victron_gx::entity::sensor::battery_high_voltage::name` | High voltage | Högspänning | Core-literal match |
| 15594 | 886120597 | `component::victron_gx::entity::sensor::battery_high_temperature::state::warning` | Warning | Varning | Shared reference target checked |
| 15595 | 886120596 | `component::victron_gx::entity::sensor::battery_high_temperature::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 15596 | 886120595 | `component::victron_gx::entity::sensor::battery_high_temperature::state::alarm` | Alarm | Larm | Shared reference target checked |
| 15597 | 886120594 | `component::victron_gx::entity::sensor::battery_high_temperature::name` | High temperature | Hög temperatur | Core-literal match |
| 15598 | 886120593 | `component::victron_gx::entity::sensor::battery_high_internal_temperature::state::warning` | Warning | Varning | Shared reference target checked |
| 15599 | 886120592 | `component::victron_gx::entity::sensor::battery_high_internal_temperature::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 15600 | 886120591 | `component::victron_gx::entity::sensor::battery_high_internal_temperature::state::alarm` | Alarm | Larm | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 886190074 | `component::llama_cpp::config_subentries::conversation::abort::reauth_successful` | Re-authentication was successful |
| 886178102 | `component::nextcloud::config::abort::reconfigure_successful` | Reconfiguration was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
