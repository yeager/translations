# Home Assistant Core – historisk avstämning 21481–21600

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 19 direkta källtexter matchar HA Core-källan; 94 referensanvändningar med 62 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 7 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 21481 | 828726047 | `component::victron_gx::entity::sensor::evcharger_session_energy::name` | Last session energy | Senaste sessionen, energi | Core-literal match |
| 21482 | 828726046 | `component::victron_gx::entity::sensor::evcharger_session_cost::unit_of_measurement` | $ | $ | Source-path follow-up open |
| 21483 | 828726045 | `component::victron_gx::entity::sensor::evcharger_session_cost::name` | Last session cost | Senaste sessionen, kostnad | Core-literal match |
| 21484 | 828726044 | `component::victron_gx::entity::sensor::evcharger_power_phase::name` | Power {phase} | Effekt {phase} | Shared reference target checked |
| 21485 | 828726043 | `component::victron_gx::entity::sensor::evcharger_power::name` | Power | Effekt | Shared reference target checked |
| 21486 | 828726042 | `component::victron_gx::entity::sensor::evcharger_position::state::ac_out` | AC out | AC-utgång | Core-literal match |
| 21487 | 828726041 | `component::victron_gx::entity::sensor::evcharger_position::state::ac_input` | AC input | Växelströmsingång | Shared reference target checked |
| 21488 | 828726040 | `component::victron_gx::entity::sensor::evcharger_position::name` | Position | Position | Shared reference target checked |
| 21489 | 828726039 | `component::victron_gx::entity::sensor::evcharger_mode::state::scheduled_charge` | Scheduled Charge | Schemalagd debitering | Source-path follow-up open |
| 21490 | 828726038 | `component::victron_gx::entity::sensor::evcharger_mode::state::manual` | Manual | Manuell | Source-path follow-up open |
| 21491 | 828726037 | `component::victron_gx::entity::sensor::evcharger_mode::state::auto` | Auto | Auto | Source-path follow-up open |
| 21492 | 828726036 | `component::victron_gx::entity::sensor::evcharger_mode::name` | Mode | Läge | Source-path follow-up open |
| 21493 | 828726035 | `component::victron_gx::entity::sensor::evcharger_min_set_current::name` | Minimum set current | Minsta inställda ström | Source-path follow-up open |
| 21494 | 828726034 | `component::victron_gx::entity::sensor::evcharger_max_set_current::name` | Maximum set current | Högsta inställda ström | Source-path follow-up open |
| 21495 | 828726033 | `component::victron_gx::entity::sensor::evcharger_current::name` | Current | Ström | Shared reference target checked |
| 21496 | 828726032 | `component::victron_gx::entity::sensor::digitalinput_type::state::touch_input_control` | Touch input control | Touch-inmatning | Core-literal match |
| 21497 | 828726031 | `component::victron_gx::entity::sensor::digitalinput_type::state::smoke_alarm` | Smoke alarm | Röklarm | Core-literal match |
| 21498 | 828726030 | `component::victron_gx::entity::sensor::digitalinput_type::state::pulse_meter` | Pulse meter | Pulsmätare | Core-literal match |
| 21499 | 828726029 | `component::victron_gx::entity::sensor::digitalinput_type::state::generator` | Generator | Generator | Shared reference target checked |
| 21500 | 828726028 | `component::victron_gx::entity::sensor::digitalinput_type::state::fire_alarm` | Fire alarm | Brandlarm | Core-literal match |
| 21501 | 828726027 | `component::victron_gx::entity::sensor::digitalinput_type::state::door_alarm` | Door alarm | Dörrlarm | Core-literal match |
| 21502 | 828726026 | `component::victron_gx::entity::sensor::digitalinput_type::state::disabled` | Disabled | Inaktiverad | Shared reference target checked |
| 21503 | 828726025 | `component::victron_gx::entity::sensor::digitalinput_type::state::co2_alarm` | CO2 alarm | CO2-larm | Core-literal match |
| 21504 | 828726024 | `component::victron_gx::entity::sensor::digitalinput_type::state::burglar_alarm` | Burglar alarm | Inbrottslarm | Core-literal match |
| 21505 | 828726023 | `component::victron_gx::entity::sensor::digitalinput_type::state::bilge_pump` | Bilge pump | Länspump | Core-literal match |
| 21506 | 828726022 | `component::victron_gx::entity::sensor::digitalinput_type::state::bilge_alarm` | Bilge alarm | Länspumpslarm | Core-literal match |
| 21507 | 828726021 | `component::victron_gx::entity::sensor::digitalinput_type::name` | Type | Typ | Core-literal match |
| 21508 | 828726020 | `component::victron_gx::entity::sensor::digitalinput_state::state::yes` | Yes | Ja | Shared reference target checked |
| 21509 | 828726019 | `component::victron_gx::entity::sensor::digitalinput_state::state::stopped` | Stopped | Stoppad | Shared reference target checked |
| 21510 | 828726018 | `component::victron_gx::entity::sensor::digitalinput_state::state::running` | Running | Körs | Shared reference target checked |
| 21511 | 828726017 | `component::victron_gx::entity::sensor::digitalinput_state::state::open` | Open | Öppen | Shared reference target checked |
| 21512 | 828726016 | `component::victron_gx::entity::sensor::digitalinput_state::state::on` | On | På | Shared reference target checked |
| 21513 | 828726015 | `component::victron_gx::entity::sensor::digitalinput_state::state::ok` | Ok | Ok | Shared reference target checked |
| 21514 | 828726014 | `component::victron_gx::entity::sensor::digitalinput_state::state::off` | Off | Av | Shared reference target checked |
| 21515 | 828726013 | `component::victron_gx::entity::sensor::digitalinput_state::state::no` | No | Nej | Shared reference target checked |
| 21516 | 828726012 | `component::victron_gx::entity::sensor::digitalinput_state::state::low` | Low | Låg | Shared reference target checked |
| 21517 | 828726011 | `component::victron_gx::entity::sensor::digitalinput_state::state::high` | High | Hög | Shared reference target checked |
| 21518 | 828726010 | `component::victron_gx::entity::sensor::digitalinput_state::state::closed` | Closed | Stängd | Shared reference target checked |
| 21519 | 828726009 | `component::victron_gx::entity::sensor::digitalinput_state::state::alarm` | Alarm | Larm | Shared reference target checked |
| 21520 | 828726008 | `component::victron_gx::entity::sensor::digitalinput_state::name` | State | Tillstånd | Shared reference target checked |
| 21521 | 828726007 | `component::victron_gx::entity::sensor::digitalinput_input_state_raw::state::low_closed` | Low/closed | Lågt/stängt | Core-literal match |
| 21522 | 828726006 | `component::victron_gx::entity::sensor::digitalinput_input_state_raw::state::high_open` | High/open | Högt/öppet | Core-literal match |
| 21523 | 828726005 | `component::victron_gx::entity::sensor::digitalinput_input_state_raw::name` | Raw state | Tillstånd i rådata | Core-literal match |
| 21524 | 828726004 | `component::victron_gx::entity::sensor::digitalinput_alarm::state::warning` | Warning | Varning | Shared reference target checked |
| 21525 | 828726003 | `component::victron_gx::entity::sensor::digitalinput_alarm::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 21526 | 828726002 | `component::victron_gx::entity::sensor::digitalinput_alarm::state::alarm` | Alarm | Larm | Shared reference target checked |
| 21527 | 828726001 | `component::victron_gx::entity::sensor::digitalinput_alarm::name` | Alarm | Larm | Shared reference target checked |
| 21528 | 828726000 | `component::victron_gx::entity::sensor::dcsystem_voltage::name` | Voltage | Spänning | Shared reference target checked |
| 21529 | 828725999 | `component::victron_gx::entity::sensor::dcsystem_power::name` | Power | Effekt | Shared reference target checked |
| 21530 | 828725998 | `component::victron_gx::entity::sensor::dcsystem_current::name` | Current | Ström | Shared reference target checked |
| 21531 | 828725997 | `component::victron_gx::entity::sensor::dcsystem_aux_voltage::name` | Auxiliary voltage | Hjälpspänning | Core-literal match |
| 21532 | 828725996 | `component::victron_gx::entity::sensor::dcload_voltage::name` | Voltage | Spänning | Shared reference target checked |
| 21533 | 828725995 | `component::victron_gx::entity::sensor::dcload_power::name` | Power | Effekt | Shared reference target checked |
| 21534 | 828725994 | `component::victron_gx::entity::sensor::dcload_current::name` | Current | Ström | Shared reference target checked |
| 21535 | 828725993 | `component::victron_gx::entity::sensor::dcdc_state::state::sustain_alt` | Sustain alt | Sustain alt | Shared reference target checked |
| 21536 | 828725992 | `component::victron_gx::entity::sensor::dcdc_state::state::sustain` | Sustain | Sustain | Shared reference target checked |
| 21537 | 828725991 | `component::victron_gx::entity::sensor::dcdc_state::state::storage` | Storage | Lagring | Shared reference target checked |
| 21538 | 828725990 | `component::victron_gx::entity::sensor::dcdc_state::state::starting_up` | Starting up | Startar upp | Shared reference target checked |
| 21539 | 828725989 | `component::victron_gx::entity::sensor::dcdc_state::state::scheduled_recharging` | Scheduled recharging | Schemalagd uppladdning | Shared reference target checked |
| 21540 | 828725988 | `component::victron_gx::entity::sensor::dcdc_state::state::repeated_absorption` | Repeated absorption | Upprepad absorption | Shared reference target checked |
| 21541 | 828725987 | `component::victron_gx::entity::sensor::dcdc_state::state::recharging` | Recharging | Uppladdar | Shared reference target checked |
| 21542 | 828725986 | `component::victron_gx::entity::sensor::dcdc_state::state::power_supply` | Power supply | Strömförsörjning | Shared reference target checked |
| 21543 | 828725985 | `component::victron_gx::entity::sensor::dcdc_state::state::power_assist` | Power Assist | Power Assist | Shared reference target checked |
| 21544 | 828725984 | `component::victron_gx::entity::sensor::dcdc_state::state::passthrough` | Passthrough | Genomströmning | Shared reference target checked |
| 21545 | 828725983 | `component::victron_gx::entity::sensor::dcdc_state::state::off` | Off | Av | Shared reference target checked |
| 21546 | 828725982 | `component::victron_gx::entity::sensor::dcdc_state::state::low_power` | Low power | Låg ström | Shared reference target checked |
| 21547 | 828725981 | `component::victron_gx::entity::sensor::dcdc_state::state::inverting` | Inverting | Växelriktar | Shared reference target checked |
| 21548 | 828725980 | `component::victron_gx::entity::sensor::dcdc_state::state::float` | Float | Flytande | Shared reference target checked |
| 21549 | 828725979 | `component::victron_gx::entity::sensor::dcdc_state::state::fault` | Fault | Fel | Shared reference target checked |
| 21550 | 828725978 | `component::victron_gx::entity::sensor::dcdc_state::state::external_control` | External control | Extern styrning | Shared reference target checked |
| 21551 | 828725977 | `component::victron_gx::entity::sensor::dcdc_state::state::equalize` | Equalize | Utjämna | Shared reference target checked |
| 21552 | 828725976 | `component::victron_gx::entity::sensor::dcdc_state::state::discharging` | Discharging | Laddar ur | Shared reference target checked |
| 21553 | 828725975 | `component::victron_gx::entity::sensor::dcdc_state::state::bulk` | Bulk | Bulk | Shared reference target checked |
| 21554 | 828725974 | `component::victron_gx::entity::sensor::dcdc_state::state::battery_safe` | Battery Safe | Batteri säkert | Shared reference target checked |
| 21555 | 828725973 | `component::victron_gx::entity::sensor::dcdc_state::state::auto_equalize` | Auto equalize / recondition | Automatisk utjämning/rekonditionering | Shared reference target checked |
| 21556 | 828725972 | `component::victron_gx::entity::sensor::dcdc_state::state::absorption` | Absorption | Absorption | Shared reference target checked |
| 21557 | 828725971 | `component::victron_gx::entity::sensor::dcdc_state::name` | State | Tillstånd | Shared reference target checked |
| 21558 | 828725970 | `component::victron_gx::entity::sensor::dcdc_input_voltage::name` | Input voltage | Ingångsspänning | Shared reference target checked |
| 21559 | 828725969 | `component::victron_gx::entity::sensor::dcdc_input_power::name` | Input power | Ingångseffekt | Shared reference target checked |
| 21560 | 828725968 | `component::victron_gx::entity::sensor::dcdc_input_current::name` | Input current | Ingångsström | Shared reference target checked |
| 21561 | 828725967 | `component::victron_gx::entity::sensor::dcdc_dc_voltage::name` | DC output voltage | DC-utgångsspänning | Shared reference target checked |
| 21562 | 828725966 | `component::victron_gx::entity::sensor::dcdc_dc_power::name` | DC output power | DC-utgångseffekt | Shared reference target checked |
| 21563 | 828725965 | `component::victron_gx::entity::sensor::dcdc_dc_current::name` | DC output current | DC-utgångsström | Shared reference target checked |
| 21564 | 828725964 | `component::victron_gx::entity::sensor::charger_state::state::sustain_alt` | Sustain alt | Sustain alt | Shared reference target checked |
| 21565 | 828725963 | `component::victron_gx::entity::sensor::charger_state::state::sustain` | Sustain | Sustain | Shared reference target checked |
| 21566 | 828725962 | `component::victron_gx::entity::sensor::charger_state::state::storage` | Storage | Lagring | Shared reference target checked |
| 21567 | 828725961 | `component::victron_gx::entity::sensor::charger_state::state::starting_up` | Starting up | Startar upp | Shared reference target checked |
| 21568 | 828725960 | `component::victron_gx::entity::sensor::charger_state::state::scheduled_recharging` | Scheduled recharging | Schemalagd uppladdning | Shared reference target checked |
| 21569 | 828725959 | `component::victron_gx::entity::sensor::charger_state::state::repeated_absorption` | Repeated absorption | Upprepad absorption | Shared reference target checked |
| 21570 | 828725958 | `component::victron_gx::entity::sensor::charger_state::state::recharging` | Recharging | Uppladdar | Shared reference target checked |
| 21571 | 828725957 | `component::victron_gx::entity::sensor::charger_state::state::power_supply` | Power supply | Strömförsörjning | Shared reference target checked |
| 21572 | 828725956 | `component::victron_gx::entity::sensor::charger_state::state::power_assist` | Power Assist | Power Assist | Shared reference target checked |
| 21573 | 828725955 | `component::victron_gx::entity::sensor::charger_state::state::passthrough` | Passthrough | Genomströmning | Shared reference target checked |
| 21574 | 828725954 | `component::victron_gx::entity::sensor::charger_state::state::off` | Off | Av | Shared reference target checked |
| 21575 | 828725953 | `component::victron_gx::entity::sensor::charger_state::state::low_power` | Low power | Låg ström | Shared reference target checked |
| 21576 | 828725952 | `component::victron_gx::entity::sensor::charger_state::state::inverting` | Inverting | Växelriktar | Shared reference target checked |
| 21577 | 828725951 | `component::victron_gx::entity::sensor::charger_state::state::float` | Float | Flytande | Shared reference target checked |
| 21578 | 828725950 | `component::victron_gx::entity::sensor::charger_state::state::fault` | Fault | Fel | Shared reference target checked |
| 21579 | 828725949 | `component::victron_gx::entity::sensor::charger_state::state::external_control` | External control | Extern styrning | Shared reference target checked |
| 21580 | 828725948 | `component::victron_gx::entity::sensor::charger_state::state::equalize` | Equalize | Utjämna | Shared reference target checked |
| 21581 | 828725947 | `component::victron_gx::entity::sensor::charger_state::state::discharging` | Discharging | Laddar ur | Shared reference target checked |
| 21582 | 828725946 | `component::victron_gx::entity::sensor::charger_state::state::bulk` | Bulk | Bulk | Shared reference target checked |
| 21583 | 828725945 | `component::victron_gx::entity::sensor::charger_state::state::battery_safe` | Battery Safe | Batteri säkert | Shared reference target checked |
| 21584 | 828725944 | `component::victron_gx::entity::sensor::charger_state::state::auto_equalize` | Auto equalize / recondition | Automatisk utjämning/rekonditionering | Shared reference target checked |
| 21585 | 828725943 | `component::victron_gx::entity::sensor::charger_state::state::absorption` | Absorption | Absorption | Shared reference target checked |
| 21586 | 828725942 | `component::victron_gx::entity::sensor::charger_state::name` | State | Tillstånd | Shared reference target checked |
| 21587 | 828725941 | `component::victron_gx::entity::sensor::charger_nr_of_outputs::unit_of_measurement` | outputs | utgångar | Core-literal match |
| 21588 | 828725940 | `component::victron_gx::entity::sensor::charger_nr_of_outputs::name` | Number of outputs | Antal utgångar | Core-literal match |
| 21589 | 828725939 | `component::victron_gx::entity::sensor::charger_error_code::state::user_settings_invalid` | User settings invalid | Ogiltiga användarinställningar | Shared reference target checked |
| 21590 | 828725938 | `component::victron_gx::entity::sensor::charger_error_code::state::terminals_overheated` | Terminals overheated | Terminaler överhettade | Shared reference target checked |
| 21591 | 828725937 | `component::victron_gx::entity::sensor::charger_error_code::state::synchronized_charging_config_issue` | Synchronized charging config issue | Problem med konfiguration av synkroniserad laddning | Shared reference target checked |
| 21592 | 828725936 | `component::victron_gx::entity::sensor::charger_error_code::state::no_error` | No error | Inget fel | Shared reference target checked |
| 21593 | 828725935 | `component::victron_gx::entity::sensor::charger_error_code::state::network_misconfigured` | Network misconfigured | Nätverket är felkonfigurerat | Shared reference target checked |
| 21594 | 828725934 | `component::victron_gx::entity::sensor::charger_error_code::state::lost_communication_with_device` | Lost communication with device | Förlorade kommunikation med enheten | Shared reference target checked |
| 21595 | 828725933 | `component::victron_gx::entity::sensor::charger_error_code::state::invalid_incompatible_firmware` | Invalid/incompatible firmware | Ogiltig/inkompatibel firmware | Shared reference target checked |
| 21596 | 828725932 | `component::victron_gx::entity::sensor::charger_error_code::state::input_voltage_too_high` | Input voltage too high (solar panel) | För hög ingångsspänning (solpanel) | Shared reference target checked |
| 21597 | 828725931 | `component::victron_gx::entity::sensor::charger_error_code::state::input_shutdown_reverse_current` | Input shutdown (reverse current) | Ingångsavstängning (omvänd ström) | Shared reference target checked |
| 21598 | 828725930 | `component::victron_gx::entity::sensor::charger_error_code::state::input_shutdown_battery_voltage_too_high` | Input shutdown (battery voltage too high) | Ingångsavstängning (överspänning i batteri) | Shared reference target checked |
| 21599 | 828725929 | `component::victron_gx::entity::sensor::charger_error_code::state::input_current_too_high` | Input current too high (solar panel) | För hög ingångsström (solpanel) | Shared reference target checked |
| 21600 | 828725928 | `component::victron_gx::entity::sensor::charger_error_code::state::factory_calibration_data_lost` | Factory calibration data lost | Fabriksinställningarna har gått förlorade | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 828726046 | `component::victron_gx::entity::sensor::evcharger_session_cost::unit_of_measurement` | $ |
| 828726039 | `component::victron_gx::entity::sensor::evcharger_mode::state::scheduled_charge` | Scheduled Charge |
| 828726038 | `component::victron_gx::entity::sensor::evcharger_mode::state::manual` | Manual |
| 828726037 | `component::victron_gx::entity::sensor::evcharger_mode::state::auto` | Auto |
| 828726036 | `component::victron_gx::entity::sensor::evcharger_mode::name` | Mode |
| 828726035 | `component::victron_gx::entity::sensor::evcharger_min_set_current::name` | Minimum set current |
| 828726034 | `component::victron_gx::entity::sensor::evcharger_max_set_current::name` | Maximum set current |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
