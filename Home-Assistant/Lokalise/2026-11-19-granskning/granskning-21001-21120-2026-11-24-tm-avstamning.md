# Home Assistant Core – historisk avstämning 21001–21120

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 46 direkta källtexter matchar HA Core-källan; 22 referensanvändningar med 22 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 52 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 21001 | 828726527 | `component::victron_gx::entity::sensor::system_state::state::sustain_alt` | Sustain alt | Sustain alt | Shared reference target checked |
| 21002 | 828726526 | `component::victron_gx::entity::sensor::system_state::state::sustain` | Sustain | Sustain | Shared reference target checked |
| 21003 | 828726525 | `component::victron_gx::entity::sensor::system_state::state::storage` | Storage | Lagring | Shared reference target checked |
| 21004 | 828726524 | `component::victron_gx::entity::sensor::system_state::state::starting_up` | Starting up | Startar upp | Shared reference target checked |
| 21005 | 828726523 | `component::victron_gx::entity::sensor::system_state::state::scheduled_recharging` | Scheduled recharging | Schemalagd uppladdning | Shared reference target checked |
| 21006 | 828726522 | `component::victron_gx::entity::sensor::system_state::state::repeated_absorption` | Repeated absorption | Upprepad absorption | Shared reference target checked |
| 21007 | 828726521 | `component::victron_gx::entity::sensor::system_state::state::recharging` | Recharging | Uppladdar | Shared reference target checked |
| 21008 | 828726520 | `component::victron_gx::entity::sensor::system_state::state::power_supply` | Power supply | Strömförsörjning | Shared reference target checked |
| 21009 | 828726519 | `component::victron_gx::entity::sensor::system_state::state::power_assist` | Power Assist | Power Assist | Shared reference target checked |
| 21010 | 828726518 | `component::victron_gx::entity::sensor::system_state::state::passthrough` | Passthrough | Genomströmning | Shared reference target checked |
| 21011 | 828726517 | `component::victron_gx::entity::sensor::system_state::state::off` | Off | Av | Shared reference target checked |
| 21012 | 828726516 | `component::victron_gx::entity::sensor::system_state::state::low_power` | Low power | Låg ström | Shared reference target checked |
| 21013 | 828726515 | `component::victron_gx::entity::sensor::system_state::state::inverting` | Inverting | Växelriktar | Shared reference target checked |
| 21014 | 828726514 | `component::victron_gx::entity::sensor::system_state::state::float` | Float | Flytande | Shared reference target checked |
| 21015 | 828726513 | `component::victron_gx::entity::sensor::system_state::state::fault` | Fault | Fel | Shared reference target checked |
| 21016 | 828726512 | `component::victron_gx::entity::sensor::system_state::state::external_control` | External control | Extern styrning | Shared reference target checked |
| 21017 | 828726511 | `component::victron_gx::entity::sensor::system_state::state::equalize` | Equalize | Utjämna | Shared reference target checked |
| 21018 | 828726510 | `component::victron_gx::entity::sensor::system_state::state::discharging` | Discharging | Laddar ur | Shared reference target checked |
| 21019 | 828726509 | `component::victron_gx::entity::sensor::system_state::state::bulk` | Bulk | Bulk | Shared reference target checked |
| 21020 | 828726508 | `component::victron_gx::entity::sensor::system_state::state::battery_safe` | Battery Safe | Batteri säkert | Shared reference target checked |
| 21021 | 828726507 | `component::victron_gx::entity::sensor::system_state::state::auto_equalize` | Auto equalize / recondition | Automatisk utjämning/rekonditionering | Shared reference target checked |
| 21022 | 828726506 | `component::victron_gx::entity::sensor::system_state::state::absorption` | Absorption | Absorption | Shared reference target checked |
| 21023 | 828726505 | `component::victron_gx::entity::sensor::system_state::name` | System state | Systemtillstånd | Core-literal match |
| 21024 | 828726504 | `component::victron_gx::entity::sensor::system_settings_dess_mode::state::sell` | Sell | Sälj | Source-path follow-up open |
| 21025 | 828726503 | `component::victron_gx::entity::sensor::system_settings_dess_mode::state::off` | Off | Av | Source-path follow-up open |
| 21026 | 828726502 | `component::victron_gx::entity::sensor::system_settings_dess_mode::state::node_red` | Node-RED | Node-RED | Source-path follow-up open |
| 21027 | 828726501 | `component::victron_gx::entity::sensor::system_settings_dess_mode::state::buy` | Buy | Köp | Source-path follow-up open |
| 21028 | 828726500 | `component::victron_gx::entity::sensor::system_settings_dess_mode::state::auto_vrm` | Auto / VRM | Auto / VRM | Source-path follow-up open |
| 21029 | 828726499 | `component::victron_gx::entity::sensor::system_settings_dess_mode::name` | DESS mode | DESS-läge | Source-path follow-up open |
| 21030 | 828726498 | `component::victron_gx::entity::sensor::system_relay_relay_custom_name::name` | Relay {relay} custom name | Relä {relay} anpassat namn | Core-literal match |
| 21031 | 828726497 | `component::victron_gx::entity::sensor::system_pv_on_output_power_phase::name` | PV on output power {phase} | PV på utgångseffekt {phase} | Core-literal match |
| 21032 | 828726496 | `component::victron_gx::entity::sensor::system_pv_on_output_phases::unit_of_measurement` | phases | faser | Core-literal match |
| 21033 | 828726495 | `component::victron_gx::entity::sensor::system_pv_on_output_phases::name` | PV on output phases | PV på utgångsfaser | Core-literal match |
| 21034 | 828726494 | `component::victron_gx::entity::sensor::system_pv_on_output_current_phase::name` | PV on output current {phase} | PV på utgångsström {phase} | Core-literal match |
| 21035 | 828726493 | `component::victron_gx::entity::sensor::system_heartbeat::name` | GX system heartbeat | GX-system hjärtslag | Core-literal match |
| 21036 | 828726492 | `component::victron_gx::entity::sensor::system_grid_power_phase::name` | Grid power {phase} | Elnätseffekt, fas {phase} | Core-literal match |
| 21037 | 828726491 | `component::victron_gx::entity::sensor::system_grid_phases::unit_of_measurement` | phases | faser | Core-literal match |
| 21038 | 828726490 | `component::victron_gx::entity::sensor::system_grid_phases::name` | Grid phases | Elnätsfaser | Core-literal match |
| 21039 | 828726489 | `component::victron_gx::entity::sensor::system_grid_current_phase::name` | Grid current {phase} | Elnätsström, fas {phase} | Core-literal match |
| 21040 | 828726488 | `component::victron_gx::entity::sensor::system_generator_load_phase::name` | Genset load {phase} | Genset belastning {phase} | Core-literal match |
| 21041 | 828726487 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_soc::name` | ESS BatteryLife schedule charge {slot} SOC | ESS BatteryLife schemalagd laddning {slot} SOC | Source-path follow-up open |
| 21042 | 828726486 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_duration::name` | ESS BatteryLife schedule charge {slot} duration | ESS BatteryLife schemalagd laddning {slot} varaktighet | Source-path follow-up open |
| 21043 | 828726485 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::weekends` | Weekends | Helger | Source-path follow-up open |
| 21044 | 828726484 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::weekdays` | Weekdays | Veckodagar | Source-path follow-up open |
| 21045 | 828726483 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::wednesday` | Wednesday | Onsdag | Source-path follow-up open |
| 21046 | 828726482 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::tuesday` | Tuesday | Tisdag | Source-path follow-up open |
| 21047 | 828726481 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::thursday` | Thursday | Torsdag | Source-path follow-up open |
| 21048 | 828726480 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::sunday` | Sunday | Söndag | Source-path follow-up open |
| 21049 | 828726479 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::saturday` | Saturday | Lördag | Source-path follow-up open |
| 21050 | 828726478 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::monday` | Monday | Måndag | Source-path follow-up open |
| 21051 | 828726477 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::friday` | Friday | Fredag | Source-path follow-up open |
| 21052 | 828726476 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::every_day` | Every day | Varje dag | Source-path follow-up open |
| 21053 | 828726475 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_weekend` | Disabled (Weekends) | Inaktiverad (helger) | Source-path follow-up open |
| 21054 | 828726474 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_weekdays` | Disabled (Weekdays) | Inaktiverad (veckodagar) | Source-path follow-up open |
| 21055 | 828726473 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_wednesday` | Disabled (Wednesday) | Inaktiverad (onsdag) | Source-path follow-up open |
| 21056 | 828726472 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_tuesday` | Disabled (Tuesday) | Inaktiverad (tisdag) | Source-path follow-up open |
| 21057 | 828726471 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_thursday` | Disabled (Thursday) | Inaktiverad (torsdag) | Source-path follow-up open |
| 21058 | 828726470 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_sunday` | Disabled (Sunday) | Inaktiverad (söndag) | Source-path follow-up open |
| 21059 | 828726469 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_saturday` | Disabled (Saturday) | Inaktiverad (lördag) | Source-path follow-up open |
| 21060 | 828726468 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_monday` | Disabled (Monday) | Inaktiverad (måndag) | Source-path follow-up open |
| 21061 | 828726467 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_friday` | Disabled (Friday) | Inaktiverad (fredag) | Source-path follow-up open |
| 21062 | 828726466 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_every_day` | Disabled (Every day) | Inaktiverad (varje dag) | Source-path follow-up open |
| 21063 | 828726465 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::name` | ESS BatteryLife schedule charge {slot} days | ESS BatteryLife schemalagd laddning {slot} dagar | Source-path follow-up open |
| 21064 | 828726464 | `component::victron_gx::entity::sensor::system_ess_mode::state::phase_compensation_enabled` | Optimized mode or 'keep batteries charged' and phase compensation enabled | Optimerat läge eller ”håll batterierna laddade” och faskompensering aktiverad | Source-path follow-up open |
| 21065 | 828726463 | `component::victron_gx::entity::sensor::system_ess_mode::state::phase_compensation_disabled` | Optimized mode or 'keep batteries charged' and phase compensation disabled | Optimerat läge eller ”håll batterierna laddade” och faskompensering inaktiverad | Source-path follow-up open |
| 21066 | 828726462 | `component::victron_gx::entity::sensor::system_ess_mode::state::external_control` | External control | Extern styrning | Source-path follow-up open |
| 21067 | 828726461 | `component::victron_gx::entity::sensor::system_ess_mode::name` | ESS mode (Hub4) | ESS-läge (Hub4) | Source-path follow-up open |
| 21068 | 828726460 | `component::victron_gx::entity::sensor::system_ess_min_soc_limit::name` | ESS min SOC limit | ESS minsta SOC-gräns | Source-path follow-up open |
| 21069 | 828726459 | `component::victron_gx::entity::sensor::system_ess_max_inverter_power_limit::name` | ESS max inverter power limit | ESS maximal växelriktare effektgräns | Source-path follow-up open |
| 21070 | 828726458 | `component::victron_gx::entity::sensor::system_ess_max_feed_in_power::name` | ESS max feed-in power | ESS maximal feed in-effekt | Source-path follow-up open |
| 21071 | 828726457 | `component::victron_gx::entity::sensor::system_ess_max_charge_voltage::name` | ESS max charge voltage | ESS maximal laddspänning | Source-path follow-up open |
| 21072 | 828726456 | `component::victron_gx::entity::sensor::system_ess_max_charge_power::name` | ESS max charge power limit | ESS maximal laddeffektgräns | Source-path follow-up open |
| 21073 | 828726455 | `component::victron_gx::entity::sensor::system_ess_max_charge_current::name` | ESS max charge current | ESS maximal laddström | Source-path follow-up open |
| 21074 | 828726454 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::with_battery_life` | Optimized mode with BatteryLife | Optimerat läge med BatteryLife | Source-path follow-up open |
| 21075 | 828726453 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::sustain` | Multi/Quattro is in sustain | Multi/Quattro är i sustain-läge | Source-path follow-up open |
| 21076 | 828726452 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::soc_below_soc_limit_24_hours` | SoC has been below SoC limit for more than 24 hours. Charging with battery with 5amps | SoC har legat under SoC-gränsen i mer än 24 timmar. Batteriet laddas med 5 ampere. | Source-path follow-up open |
| 21077 | 828726451 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::soc_below_battery_life_dynamic_soc_limit` | SoC below BatteryLife dynamic SoC limit | SoC ligger under BatteryLife:s dynamiska SoC-gräns | Source-path follow-up open |
| 21078 | 828726450 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::self_consumption_soc_exceeds_85` | Self consumption, SoC exceeds 85% | Egenförbrukning, SoC överstiger 85 % | Source-path follow-up open |
| 21079 | 828726449 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::self_consumption_soc_below_min` | Self consumption, SoC is below minimum SoC | Egenförbrukning, SoC under minsta SoC | Source-path follow-up open |
| 21080 | 828726448 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::self_consumption_soc_at_100` | Self consumption, SoC at 100% | Egenförbrukning, SoC på 100 % | Source-path follow-up open |
| 21081 | 828726447 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::self_consumption_soc_above_min` | Self consumption, SoC at or above minimum SoC | Egenförbrukning, SoC på eller över minsta SoC | Source-path follow-up open |
| 21082 | 828726446 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::self_consumption` | Self consumption | Egenförbrukning | Source-path follow-up open |
| 21083 | 828726445 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::recharge_no_battery_life` | Recharge, SOC dropped 5% or more below MinSOC (No BatteryLife) | Laddning, SOC sjönk 5 % eller mer under minsta SOC (utan BetteryLife) | Source-path follow-up open |
| 21084 | 828726444 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::recharge` | Recharge, SOC dropped 5% or more below MinSOC | Laddning, SOC sjönk 5 % eller mer under minsta SOC | Source-path follow-up open |
| 21085 | 828726443 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::keep_batteries_charged` | 'Keep batteries charged' mode enabled | Läget 'Håll batterierna laddade' är aktiverat | Source-path follow-up open |
| 21086 | 828726442 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::name` | ESS BatteryLife state | ESS BatteryLife-tillstånd | Source-path follow-up open |
| 21087 | 828726441 | `component::victron_gx::entity::sensor::system_dynamicess_target_soc::name` | Dynamic ESS target SoC | Dynamisk ESS målnivå SoC | Core-literal match |
| 21088 | 828726440 | `component::victron_gx::entity::sensor::system_dynamicess_strategy::state::targetsoc` | Target SoC | Målnivå SoC | Core-literal match |
| 21089 | 828726439 | `component::victron_gx::entity::sensor::system_dynamicess_strategy::state::selfconsume` | Self-consume | Egenkonsumtion | Core-literal match |
| 21090 | 828726438 | `component::victron_gx::entity::sensor::system_dynamicess_strategy::state::progrid` | Pro grid | Pro-elnät | Core-literal match |
| 21091 | 828726437 | `component::victron_gx::entity::sensor::system_dynamicess_strategy::state::probattery` | Pro battery | Pro-batteri | Core-literal match |
| 21092 | 828726436 | `component::victron_gx::entity::sensor::system_dynamicess_strategy::name` | Dynamic ESS strategy | Dynamisk ESS strategi | Core-literal match |
| 21093 | 828726435 | `component::victron_gx::entity::sensor::system_dynamicess_schedule_count::unit_of_measurement` | schedules | scheman | Core-literal match |
| 21094 | 828726434 | `component::victron_gx::entity::sensor::system_dynamicess_schedule_count::name` | Dynamic ESS number of schedules | Dynamisk ESS antal schemaläggningar | Core-literal match |
| 21095 | 828726433 | `component::victron_gx::entity::sensor::system_dynamicess_restrictions::state::no_restrictions` | No restrictions between battery and the grid | Inga begränsningar mellan batteri och elnät | Core-literal match |
| 21096 | 828726432 | `component::victron_gx::entity::sensor::system_dynamicess_restrictions::state::no_flow` | No energy flow between battery and grid | Inget energiflöde mellan batteri och elnät | Core-literal match |
| 21097 | 828726431 | `component::victron_gx::entity::sensor::system_dynamicess_restrictions::state::grid_to_battery_restricted` | Grid to battery energy flow restricted | Begränsat energiflöde från elnät till batteri | Core-literal match |
| 21098 | 828726430 | `component::victron_gx::entity::sensor::system_dynamicess_restrictions::state::battery_to_grid_restricted` | Battery to grid energy flow restricted | Begränsat energiflöde från batteri till elnät | Core-literal match |
| 21099 | 828726429 | `component::victron_gx::entity::sensor::system_dynamicess_restrictions::name` | Dynamic ESS restrictions | Dynamiska ESS restriktioner | Core-literal match |
| 21100 | 828726428 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::unscheduled_charge_catchup_targetsoc` | Unscheduled charge catch-up target SoC | Oschemalagd laddning återhämtningsmål SoC | Core-literal match |
| 21101 | 828726427 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::unknown_operating_mode` | Unknown operating mode | Okänt driftläge | Core-literal match |
| 21102 | 828726426 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::selfconsume_unpredicted` | Self-consume unpredicted | Egenkonsumtion oförutsett | Core-literal match |
| 21103 | 828726425 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::selfconsume_unmapped_state` | Self-consume unmapped state | Egenkonsumtion omappat tillstånd | Core-literal match |
| 21104 | 828726424 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::selfconsume_unexpected_exception` | Self-consume unexpected exception | Egenkonsumtion oväntat undantag | Core-literal match |
| 21105 | 828726423 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::selfconsume_no_grid` | Self-consume no grid | Egenkonsumtion utan elnät | Core-literal match |
| 21106 | 828726422 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::selfconsume_increased_discharge` | Self-consume increased discharge | Egenkonsumtion ökad urladdning | Core-literal match |
| 21107 | 828726421 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::selfconsume_faulty_chargerate` | Self-consume faulty charge rate | Egenkonsumtion felaktig laddningshastighet | Core-literal match |
| 21108 | 828726420 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::selfconsume_accept_discharge` | Self-consume accept discharge | Egenkonsumtion acceptera urladdning | Core-literal match |
| 21109 | 828726419 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::selfconsume_accept_charge` | Self-consume accept charge | Egenkonsumtion acceptera laddning | Core-literal match |
| 21110 | 828726418 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::scheduled_selfconsume` | Scheduled self-consume | Schemalagd egenkonsumtion | Core-literal match |
| 21111 | 828726417 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::scheduled_minimum_discharge` | Scheduled minimum discharge | Schemalagd minimum urladdning | Core-literal match |
| 21112 | 828726416 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::scheduled_discharge_smooth_transition` | Scheduled discharge smooth transition | Schemalagd urladdning smidig övergång | Core-literal match |
| 21113 | 828726415 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::scheduled_discharge` | Scheduled discharge | Schemalagd urladdning | Core-literal match |
| 21114 | 828726414 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::scheduled_charge_smooth_transition` | Scheduled charge smooth transition | Schemalagd laddning smidig övergång | Core-literal match |
| 21115 | 828726413 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::scheduled_charge_no_grid` | Scheduled charge no grid | Schemalagd laddning utan elnät | Core-literal match |
| 21116 | 828726412 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::scheduled_charge_feedin` | Scheduled charge feed-in | Schemalagd laddning inmatning | Core-literal match |
| 21117 | 828726411 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::scheduled_charge_enhanced` | Scheduled charge enhanced | Schemalagd laddning förbättrad | Core-literal match |
| 21118 | 828726410 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::scheduled_charge_allow_grid` | Scheduled charge allow grid | Schemalagd laddning tillåt nätanslutning | Core-literal match |
| 21119 | 828726409 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::no_window` | No window | Inget fönster | Core-literal match |
| 21120 | 828726408 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::keep_battery_charged` | Keep battery charged | Håll batteriet laddat | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 828726504 | `component::victron_gx::entity::sensor::system_settings_dess_mode::state::sell` | Sell |
| 828726503 | `component::victron_gx::entity::sensor::system_settings_dess_mode::state::off` | Off |
| 828726502 | `component::victron_gx::entity::sensor::system_settings_dess_mode::state::node_red` | Node-RED |
| 828726501 | `component::victron_gx::entity::sensor::system_settings_dess_mode::state::buy` | Buy |
| 828726500 | `component::victron_gx::entity::sensor::system_settings_dess_mode::state::auto_vrm` | Auto / VRM |
| 828726499 | `component::victron_gx::entity::sensor::system_settings_dess_mode::name` | DESS mode |
| 828726487 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_soc::name` | ESS BatteryLife schedule charge {slot} SOC |
| 828726486 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_duration::name` | ESS BatteryLife schedule charge {slot} duration |
| 828726485 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::weekends` | Weekends |
| 828726484 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::weekdays` | Weekdays |
| 828726483 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::wednesday` | Wednesday |
| 828726482 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::tuesday` | Tuesday |
| 828726481 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::thursday` | Thursday |
| 828726480 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::sunday` | Sunday |
| 828726479 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::saturday` | Saturday |
| 828726478 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::monday` | Monday |
| 828726477 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::friday` | Friday |
| 828726476 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::every_day` | Every day |
| 828726475 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_weekend` | Disabled (Weekends) |
| 828726474 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_weekdays` | Disabled (Weekdays) |
| 828726473 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_wednesday` | Disabled (Wednesday) |
| 828726472 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_tuesday` | Disabled (Tuesday) |
| 828726471 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_thursday` | Disabled (Thursday) |
| 828726470 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_sunday` | Disabled (Sunday) |
| 828726469 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_saturday` | Disabled (Saturday) |
| 828726468 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_monday` | Disabled (Monday) |
| 828726467 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_friday` | Disabled (Friday) |
| 828726466 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::state::disabled_every_day` | Disabled (Every day) |
| 828726465 | `component::victron_gx::entity::sensor::system_ess_schedule_charge_slot_days::name` | ESS BatteryLife schedule charge {slot} days |
| 828726464 | `component::victron_gx::entity::sensor::system_ess_mode::state::phase_compensation_enabled` | Optimized mode or 'keep batteries charged' and phase compensation enabled |
| 828726463 | `component::victron_gx::entity::sensor::system_ess_mode::state::phase_compensation_disabled` | Optimized mode or 'keep batteries charged' and phase compensation disabled |
| 828726462 | `component::victron_gx::entity::sensor::system_ess_mode::state::external_control` | External control |
| 828726461 | `component::victron_gx::entity::sensor::system_ess_mode::name` | ESS mode (Hub4) |
| 828726460 | `component::victron_gx::entity::sensor::system_ess_min_soc_limit::name` | ESS min SOC limit |
| 828726459 | `component::victron_gx::entity::sensor::system_ess_max_inverter_power_limit::name` | ESS max inverter power limit |
| 828726458 | `component::victron_gx::entity::sensor::system_ess_max_feed_in_power::name` | ESS max feed-in power |
| 828726457 | `component::victron_gx::entity::sensor::system_ess_max_charge_voltage::name` | ESS max charge voltage |
| 828726456 | `component::victron_gx::entity::sensor::system_ess_max_charge_power::name` | ESS max charge power limit |
| 828726455 | `component::victron_gx::entity::sensor::system_ess_max_charge_current::name` | ESS max charge current |
| 828726454 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::with_battery_life` | Optimized mode with BatteryLife |
| 828726453 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::sustain` | Multi/Quattro is in sustain |
| 828726452 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::soc_below_soc_limit_24_hours` | SoC has been below SoC limit for more than 24 hours. Charging with battery with 5amps |
| 828726451 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::soc_below_battery_life_dynamic_soc_limit` | SoC below BatteryLife dynamic SoC limit |
| 828726450 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::self_consumption_soc_exceeds_85` | Self consumption, SoC exceeds 85% |
| 828726449 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::self_consumption_soc_below_min` | Self consumption, SoC is below minimum SoC |
| 828726448 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::self_consumption_soc_at_100` | Self consumption, SoC at 100% |
| 828726447 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::self_consumption_soc_above_min` | Self consumption, SoC at or above minimum SoC |
| 828726446 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::self_consumption` | Self consumption |
| 828726445 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::recharge_no_battery_life` | Recharge, SOC dropped 5% or more below MinSOC (No BatteryLife) |
| 828726444 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::recharge` | Recharge, SOC dropped 5% or more below MinSOC |
| 828726443 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::state::keep_batteries_charged` | 'Keep batteries charged' mode enabled |
| 828726442 | `component::victron_gx::entity::sensor::system_ess_batterylife_state::name` | ESS BatteryLife state |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
