# Home Assistant Core – historisk avstämning 21361–21480

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 36 direkta källtexter matchar HA Core-källan; 49 referensanvändningar med 37 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 35 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 21361 | 828726167 | `component::victron_gx::entity::sensor::inverter_state::state::float` | Float | Flytande | Shared reference target checked |
| 21362 | 828726166 | `component::victron_gx::entity::sensor::inverter_state::state::fault` | Fault | Fel | Shared reference target checked |
| 21363 | 828726165 | `component::victron_gx::entity::sensor::inverter_state::state::external_control` | External control | Extern styrning | Shared reference target checked |
| 21364 | 828726164 | `component::victron_gx::entity::sensor::inverter_state::state::equalize` | Equalize | Utjämna | Shared reference target checked |
| 21365 | 828726163 | `component::victron_gx::entity::sensor::inverter_state::state::discharging` | Discharging | Laddar ur | Shared reference target checked |
| 21366 | 828726162 | `component::victron_gx::entity::sensor::inverter_state::state::bulk` | Bulk | Bulk | Shared reference target checked |
| 21367 | 828726161 | `component::victron_gx::entity::sensor::inverter_state::state::battery_safe` | Battery Safe | Batteri säkert | Shared reference target checked |
| 21368 | 828726160 | `component::victron_gx::entity::sensor::inverter_state::state::auto_equalize` | Auto equalize / recondition | Automatisk utjämning/rekonditionering | Shared reference target checked |
| 21369 | 828726159 | `component::victron_gx::entity::sensor::inverter_state::state::absorption` | Absorption | Absorption | Shared reference target checked |
| 21370 | 828726158 | `component::victron_gx::entity::sensor::inverter_state::name` | State | Tillstånd | Shared reference target checked |
| 21371 | 828726157 | `component::victron_gx::entity::sensor::inverter_pv_voltage::name` | PV bus voltage | PV-buss spänning | Shared reference target checked |
| 21372 | 828726156 | `component::victron_gx::entity::sensor::inverter_pv_power_total::name` | PV power total | PV-effekt totalt | Shared reference target checked |
| 21373 | 828726155 | `component::victron_gx::entity::sensor::inverter_output_voltage_phase::name` | Output voltage {phase} | Utgångsspänning {phase} | Shared reference target checked |
| 21374 | 828726154 | `component::victron_gx::entity::sensor::inverter_output_power_phase::name` | Output power {phase} | Utgångseffekt {phase} | Shared reference target checked |
| 21375 | 828726153 | `component::victron_gx::entity::sensor::inverter_output_current_phase::name` | Output current {phase} | Utgångsström {phase} | Shared reference target checked |
| 21376 | 828726152 | `component::victron_gx::entity::sensor::inverter_output_apparent_power_phase::name` | Output apparent power {phase} | Skenbar utgångseffekt {phase} | Shared reference target checked |
| 21377 | 828726151 | `component::victron_gx::entity::sensor::inverter_mode::state::off` | Off | Av | Source-path follow-up open |
| 21378 | 828726150 | `component::victron_gx::entity::sensor::inverter_mode::state::inverter` | Inverter | Växelriktare | Source-path follow-up open |
| 21379 | 828726149 | `component::victron_gx::entity::sensor::inverter_mode::state::eco` | Eco | Eco | Source-path follow-up open |
| 21380 | 828726148 | `component::victron_gx::entity::sensor::inverter_mode::name` | Mode | Läge | Source-path follow-up open |
| 21381 | 828726147 | `component::victron_gx::entity::sensor::hub4_ac_grid_setpoint::name` | AC grid setpoint | AC-elnätsbörvärde | Source-path follow-up open |
| 21382 | 828726146 | `component::victron_gx::entity::sensor::heatpump_voltage_phase::name` | Voltage on {phase} | Spänning på {phase} | Shared reference target checked |
| 21383 | 828726145 | `component::victron_gx::entity::sensor::heatpump_voltage::name` | Voltage | Spänning | Shared reference target checked |
| 21384 | 828726144 | `component::victron_gx::entity::sensor::heatpump_power_phase::name` | Power on {phase} | Effekt på {phase} | Shared reference target checked |
| 21385 | 828726143 | `component::victron_gx::entity::sensor::heatpump_power::name` | Power | Effekt | Shared reference target checked |
| 21386 | 828726142 | `component::victron_gx::entity::sensor::heatpump_frequency::name` | Frequency | Frekvens | Shared reference target checked |
| 21387 | 828726141 | `component::victron_gx::entity::sensor::heatpump_energy_forward_phase::name` | Consumption on {phase} | Förbrukning på {phase} | Shared reference target checked |
| 21388 | 828726140 | `component::victron_gx::entity::sensor::heatpump_energy_forward::name` | Consumption | Förbrukning | Shared reference target checked |
| 21389 | 828726139 | `component::victron_gx::entity::sensor::heatpump_current_phase::name` | Current on {phase} | Ström på {phase} | Shared reference target checked |
| 21390 | 828726138 | `component::victron_gx::entity::sensor::heatpump_current::name` | Current | Ström | Shared reference target checked |
| 21391 | 828726137 | `component::victron_gx::entity::sensor::grid_voltage_phase_next_phase::name` | Voltage {phase} to {next_phase} | Spänning {phase} till {next_phase} | Core-literal match |
| 21392 | 828726136 | `component::victron_gx::entity::sensor::grid_voltage_phase::name` | Voltage on {phase} | Spänning på {phase} | Shared reference target checked |
| 21393 | 828726135 | `component::victron_gx::entity::sensor::grid_voltage_pen::name` | Voltage on PEN | Spänning på PEN | Core-literal match |
| 21394 | 828726134 | `component::victron_gx::entity::sensor::grid_voltage::name` | Voltage | Spänning | Shared reference target checked |
| 21395 | 828726133 | `component::victron_gx::entity::sensor::grid_power_phase::name` | Power on {phase} | Effekt på {phase} | Shared reference target checked |
| 21396 | 828726132 | `component::victron_gx::entity::sensor::grid_power_factor_phase::unit_of_measurement` | factor | faktor | Source-path follow-up open |
| 21397 | 828726131 | `component::victron_gx::entity::sensor::grid_power_factor_phase::name` | Power factor on {phase} | Effektfaktor på fas {phase} | Shared reference target checked |
| 21398 | 828726130 | `component::victron_gx::entity::sensor::grid_power_factor::unit_of_measurement` | factor | faktor | Source-path follow-up open |
| 21399 | 828726129 | `component::victron_gx::entity::sensor::grid_power_factor::name` | Power factor | Effektfaktor | Shared reference target checked |
| 21400 | 828726128 | `component::victron_gx::entity::sensor::grid_power::name` | Power | Effekt | Shared reference target checked |
| 21401 | 828726127 | `component::victron_gx::entity::sensor::grid_frequency::name` | Frequency | Frekvens | Shared reference target checked |
| 21402 | 828726126 | `component::victron_gx::entity::sensor::grid_energy_reverse_phase::name` | Feed-in on {phase} | Inmatning på fas {phase} | Shared reference target checked |
| 21403 | 828726125 | `component::victron_gx::entity::sensor::grid_energy_reverse::name` | Feed-in | Inmatning | Shared reference target checked |
| 21404 | 828726124 | `component::victron_gx::entity::sensor::grid_energy_forward_phase::name` | Grid consumption on {phase} | Nätförbrukning på {phase} | Core-literal match |
| 21405 | 828726123 | `component::victron_gx::entity::sensor::grid_energy_forward::name` | Consumption | Förbrukning | Shared reference target checked |
| 21406 | 828726122 | `component::victron_gx::entity::sensor::grid_current_phase::name` | Current on {phase} | Ström på {phase} | Shared reference target checked |
| 21407 | 828726121 | `component::victron_gx::entity::sensor::grid_current_n::name` | Current on N | Ström på N | Core-literal match |
| 21408 | 828726120 | `component::victron_gx::entity::sensor::grid_current::name` | Current | Ström | Shared reference target checked |
| 21409 | 828726119 | `component::victron_gx::entity::sensor::gps_speed::name` | Speed | Hastighet | Source-path follow-up open |
| 21410 | 828726118 | `component::victron_gx::entity::sensor::gps_nrofsatellites::unit_of_measurement` | satellites | satelliter | Core-literal match |
| 21411 | 828726117 | `component::victron_gx::entity::sensor::gps_nrofsatellites::name` | Number of satellites | Antal satelliter | Core-literal match |
| 21412 | 828726116 | `component::victron_gx::entity::sensor::gps_longitude::unit_of_measurement` | long | long | Source-path follow-up open |
| 21413 | 828726115 | `component::victron_gx::entity::sensor::gps_longitude::name` | Longitude | Longitud | Source-path follow-up open |
| 21414 | 828726114 | `component::victron_gx::entity::sensor::gps_latitude::unit_of_measurement` | lat | lat | Source-path follow-up open |
| 21415 | 828726113 | `component::victron_gx::entity::sensor::gps_latitude::name` | Latitude | Latitud | Source-path follow-up open |
| 21416 | 828726112 | `component::victron_gx::entity::sensor::gps_course::unit_of_measurement` | ° | ° | Source-path follow-up open |
| 21417 | 828726111 | `component::victron_gx::entity::sensor::gps_course::name` | Course | Kurs | Source-path follow-up open |
| 21418 | 828726110 | `component::victron_gx::entity::sensor::gps_altitude::unit_of_measurement` | m | m | Source-path follow-up open |
| 21419 | 828726109 | `component::victron_gx::entity::sensor::gps_altitude::name` | Altitude | Höjd över havet | Source-path follow-up open |
| 21420 | 828726108 | `component::victron_gx::entity::sensor::generator_total_runtime::name` | Total runtime | Total körtid | Core-literal match |
| 21421 | 828726107 | `component::victron_gx::entity::sensor::generator_today_runtime::name` | Today runtime | Dagens körtid | Core-literal match |
| 21422 | 828726106 | `component::victron_gx::entity::sensor::generator_service_counter::name` | Service counter | Serviceräknare | Core-literal match |
| 21423 | 828726105 | `component::victron_gx::entity::sensor::generator_run_state::state::test_run` | Test run | Testkörning | Core-literal match |
| 21424 | 828726104 | `component::victron_gx::entity::sensor::generator_run_state::state::stopped` | Stopped | Stoppad | Shared reference target checked |
| 21425 | 828726103 | `component::victron_gx::entity::sensor::generator_run_state::state::stop_on_ac1` | Stop on AC1 | Stopp på AC1 | Core-literal match |
| 21426 | 828726102 | `component::victron_gx::entity::sensor::generator_run_state::state::soc` | SoC | SoC | Core-literal match |
| 21427 | 828726101 | `component::victron_gx::entity::sensor::generator_run_state::state::manual` | Manual | Manuell | Shared reference target checked |
| 21428 | 828726100 | `component::victron_gx::entity::sensor::generator_run_state::state::lost_comms` | Lost comms | Förlorad kommunikation | Core-literal match |
| 21429 | 828726099 | `component::victron_gx::entity::sensor::generator_run_state::state::inv_temp` | Inverter temperature | Växelriktarens temperatur | Core-literal match |
| 21430 | 828726098 | `component::victron_gx::entity::sensor::generator_run_state::state::inv_overload` | Inverter overload | Överbelastning av växelriktare | Core-literal match |
| 21431 | 828726097 | `component::victron_gx::entity::sensor::generator_run_state::state::battery_volts` | Battery volts | Batterispänning | Core-literal match |
| 21432 | 828726096 | `component::victron_gx::entity::sensor::generator_run_state::state::battery_current` | Battery current | Batteriström | Core-literal match |
| 21433 | 828726095 | `component::victron_gx::entity::sensor::generator_run_state::state::ac_load` | AC load | AC-belastning | Core-literal match |
| 21434 | 828726094 | `component::victron_gx::entity::sensor::generator_run_state::name` | Run state | Körtillstånd | Core-literal match |
| 21435 | 828726093 | `component::victron_gx::entity::sensor::generator_gen_id_warm_up_timer::name` | Generator warm-up timer | Generator uppvärmningstimer | Source-path follow-up open |
| 21436 | 828726092 | `component::victron_gx::entity::sensor::generator_gen_id_stop_on_voltage_timer::name` | Generator stop on voltage timer | Generator stopp vid spänning timer | Source-path follow-up open |
| 21437 | 828726091 | `component::victron_gx::entity::sensor::generator_gen_id_stop_on_voltage::name` | Generator stop on voltage | Generator stopp vid spänning | Source-path follow-up open |
| 21438 | 828726090 | `component::victron_gx::entity::sensor::generator_gen_id_stop_on_temp_timer::name` | Generator stop on temp timer | Generator stopp på temperatur timer | Source-path follow-up open |
| 21439 | 828726089 | `component::victron_gx::entity::sensor::generator_gen_id_stop_on_soc_timer::name` | Generator stop on SOC timer | Generator stopp på SOC timer | Source-path follow-up open |
| 21440 | 828726088 | `component::victron_gx::entity::sensor::generator_gen_id_stop_on_soc::name` | Generator stop on SOC | Generator stopp på SOC | Source-path follow-up open |
| 21441 | 828726087 | `component::victron_gx::entity::sensor::generator_gen_id_start_on_voltage_timer::name` | Generator start on voltage timer | Generator start vid spänning timer | Source-path follow-up open |
| 21442 | 828726086 | `component::victron_gx::entity::sensor::generator_gen_id_start_on_voltage::name` | Generator start on voltage | Generator start vid spänning | Source-path follow-up open |
| 21443 | 828726085 | `component::victron_gx::entity::sensor::generator_gen_id_start_on_temp_timer::name` | Generator start on temp timer | Generator start på temperatur timer | Source-path follow-up open |
| 21444 | 828726084 | `component::victron_gx::entity::sensor::generator_gen_id_start_on_soc_timer::name` | Generator start on SOC timer | Generator start på SOC timer | Source-path follow-up open |
| 21445 | 828726083 | `component::victron_gx::entity::sensor::generator_gen_id_start_on_soc::name` | Generator start on SOC | Generator start på SOC | Source-path follow-up open |
| 21446 | 828726082 | `component::victron_gx::entity::sensor::generator_gen_id_shut_down_timer::name` | Generator shutdown timer | Generator avstängningstimer | Source-path follow-up open |
| 21447 | 828726081 | `component::victron_gx::entity::sensor::generator_gen_id_service_interval::name` | Generator service interval | Generator serviceintervall | Source-path follow-up open |
| 21448 | 828726080 | `component::victron_gx::entity::sensor::generator_gen_id_qh_stop_on_voltage::name` | Generator QH stop on voltage | Generator QH stopp vid spänning | Source-path follow-up open |
| 21449 | 828726079 | `component::victron_gx::entity::sensor::generator_gen_id_qh_stop_on_soc::name` | Generator QH stop on SOC | Generator QH stopp på SOC | Source-path follow-up open |
| 21450 | 828726078 | `component::victron_gx::entity::sensor::generator_gen_id_qh_start_on_voltage::name` | Generator QH start on voltage | Generator QH start vid spänning | Source-path follow-up open |
| 21451 | 828726077 | `component::victron_gx::entity::sensor::generator_gen_id_qh_start_on_soc::name` | Generator QH start on SOC | Generator QH start på SOC | Source-path follow-up open |
| 21452 | 828726076 | `component::victron_gx::entity::sensor::generator_gen_id_cool_down_timer::name` | Generator cooldown timer | Generator nedkylningstimer | Source-path follow-up open |
| 21453 | 828726075 | `component::victron_gx::entity::sensor::evcharger_total_energy::name` | Total energy | Total energi | Shared reference target checked |
| 21454 | 828726074 | `component::victron_gx::entity::sensor::evcharger_status::state::welded_contacts_test_error` | Welded contacts test error | Fel vid test av svetsade kontakter | Core-literal match |
| 21455 | 828726073 | `component::victron_gx::entity::sensor::evcharger_status::state::waiting_for_sun` | Waiting for sun | Väntar på sol | Core-literal match |
| 21456 | 828726072 | `component::victron_gx::entity::sensor::evcharger_status::state::waiting_for_start` | Waiting for start | Väntar på start | Core-literal match |
| 21457 | 828726071 | `component::victron_gx::entity::sensor::evcharger_status::state::waiting_for_rfid` | Waiting for RFID | Väntar på RFID | Core-literal match |
| 21458 | 828726070 | `component::victron_gx::entity::sensor::evcharger_status::state::undervoltage_detected` | Undervoltage detected | Underspänning detekterad | Core-literal match |
| 21459 | 828726069 | `component::victron_gx::entity::sensor::evcharger_status::state::switching_to_3_phase` | Switching to 3 phase | Byte till 3-fas | Core-literal match |
| 21460 | 828726068 | `component::victron_gx::entity::sensor::evcharger_status::state::switching_to_1_phase` | Switching to 1 phase | Byte till 1-fas | Core-literal match |
| 21461 | 828726067 | `component::victron_gx::entity::sensor::evcharger_status::state::start_charging` | Start charging | Börja ladda | Core-literal match |
| 21462 | 828726066 | `component::victron_gx::entity::sensor::evcharger_status::state::residual_current_detected` | Residual current detected | Felström detekterad | Core-literal match |
| 21463 | 828726065 | `component::victron_gx::entity::sensor::evcharger_status::state::reserved19` | Reserved | Reserverad | Shared reference target checked |
| 21464 | 828726064 | `component::victron_gx::entity::sensor::evcharger_status::state::reserved18` | Reserved | Reserverad | Shared reference target checked |
| 21465 | 828726063 | `component::victron_gx::entity::sensor::evcharger_status::state::reserved17` | Reserved | Reserverad | Shared reference target checked |
| 21466 | 828726062 | `component::victron_gx::entity::sensor::evcharger_status::state::reserved16` | Reserved | Reserverad | Shared reference target checked |
| 21467 | 828726061 | `component::victron_gx::entity::sensor::evcharger_status::state::reserved15` | Reserved | Reserverad | Shared reference target checked |
| 21468 | 828726060 | `component::victron_gx::entity::sensor::evcharger_status::state::overvoltage_detected` | Overvoltage detected | Överspänning detekterad | Core-literal match |
| 21469 | 828726059 | `component::victron_gx::entity::sensor::evcharger_status::state::overheating_detected` | Overheating detected | Överhettning detekterad | Core-literal match |
| 21470 | 828726058 | `component::victron_gx::entity::sensor::evcharger_status::state::low_soc` | Low SoC | Låg batterinivå | Core-literal match |
| 21471 | 828726057 | `component::victron_gx::entity::sensor::evcharger_status::state::ground_test_error` | Ground test error | Fel vid jordtest | Core-literal match |
| 21472 | 828726056 | `component::victron_gx::entity::sensor::evcharger_status::state::disconnected` | Disconnected | Frånkopplad | Shared reference target checked |
| 21473 | 828726055 | `component::victron_gx::entity::sensor::evcharger_status::state::cp_input_test_error` | CP input test error | Fel vid test av CP-ingång | Core-literal match |
| 21474 | 828726054 | `component::victron_gx::entity::sensor::evcharger_status::state::connected` | Connected | Ansluten | Shared reference target checked |
| 21475 | 828726053 | `component::victron_gx::entity::sensor::evcharger_status::state::charging_limit` | Charging limit | Laddningsgräns | Core-literal match |
| 21476 | 828726052 | `component::victron_gx::entity::sensor::evcharger_status::state::charging` | Charging | Laddar | Shared reference target checked |
| 21477 | 828726051 | `component::victron_gx::entity::sensor::evcharger_status::state::charged` | Charged | Laddad | Core-literal match |
| 21478 | 828726050 | `component::victron_gx::entity::sensor::evcharger_status::name` | Status | Status | Shared reference target checked |
| 21479 | 828726049 | `component::victron_gx::entity::sensor::evcharger_set_current::name` | Set current | Ställ in strömstyrka | Source-path follow-up open |
| 21480 | 828726048 | `component::victron_gx::entity::sensor::evcharger_session_time::name` | Last session time | Senaste sessionen, tid | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 828726151 | `component::victron_gx::entity::sensor::inverter_mode::state::off` | Off |
| 828726150 | `component::victron_gx::entity::sensor::inverter_mode::state::inverter` | Inverter |
| 828726149 | `component::victron_gx::entity::sensor::inverter_mode::state::eco` | Eco |
| 828726148 | `component::victron_gx::entity::sensor::inverter_mode::name` | Mode |
| 828726147 | `component::victron_gx::entity::sensor::hub4_ac_grid_setpoint::name` | AC grid setpoint |
| 828726132 | `component::victron_gx::entity::sensor::grid_power_factor_phase::unit_of_measurement` | factor |
| 828726130 | `component::victron_gx::entity::sensor::grid_power_factor::unit_of_measurement` | factor |
| 828726119 | `component::victron_gx::entity::sensor::gps_speed::name` | Speed |
| 828726116 | `component::victron_gx::entity::sensor::gps_longitude::unit_of_measurement` | long |
| 828726115 | `component::victron_gx::entity::sensor::gps_longitude::name` | Longitude |
| 828726114 | `component::victron_gx::entity::sensor::gps_latitude::unit_of_measurement` | lat |
| 828726113 | `component::victron_gx::entity::sensor::gps_latitude::name` | Latitude |
| 828726112 | `component::victron_gx::entity::sensor::gps_course::unit_of_measurement` | ° |
| 828726111 | `component::victron_gx::entity::sensor::gps_course::name` | Course |
| 828726110 | `component::victron_gx::entity::sensor::gps_altitude::unit_of_measurement` | m |
| 828726109 | `component::victron_gx::entity::sensor::gps_altitude::name` | Altitude |
| 828726093 | `component::victron_gx::entity::sensor::generator_gen_id_warm_up_timer::name` | Generator warm-up timer |
| 828726092 | `component::victron_gx::entity::sensor::generator_gen_id_stop_on_voltage_timer::name` | Generator stop on voltage timer |
| 828726091 | `component::victron_gx::entity::sensor::generator_gen_id_stop_on_voltage::name` | Generator stop on voltage |
| 828726090 | `component::victron_gx::entity::sensor::generator_gen_id_stop_on_temp_timer::name` | Generator stop on temp timer |
| 828726089 | `component::victron_gx::entity::sensor::generator_gen_id_stop_on_soc_timer::name` | Generator stop on SOC timer |
| 828726088 | `component::victron_gx::entity::sensor::generator_gen_id_stop_on_soc::name` | Generator stop on SOC |
| 828726087 | `component::victron_gx::entity::sensor::generator_gen_id_start_on_voltage_timer::name` | Generator start on voltage timer |
| 828726086 | `component::victron_gx::entity::sensor::generator_gen_id_start_on_voltage::name` | Generator start on voltage |
| 828726085 | `component::victron_gx::entity::sensor::generator_gen_id_start_on_temp_timer::name` | Generator start on temp timer |
| 828726084 | `component::victron_gx::entity::sensor::generator_gen_id_start_on_soc_timer::name` | Generator start on SOC timer |
| 828726083 | `component::victron_gx::entity::sensor::generator_gen_id_start_on_soc::name` | Generator start on SOC |
| 828726082 | `component::victron_gx::entity::sensor::generator_gen_id_shut_down_timer::name` | Generator shutdown timer |
| 828726081 | `component::victron_gx::entity::sensor::generator_gen_id_service_interval::name` | Generator service interval |
| 828726080 | `component::victron_gx::entity::sensor::generator_gen_id_qh_stop_on_voltage::name` | Generator QH stop on voltage |
| 828726079 | `component::victron_gx::entity::sensor::generator_gen_id_qh_stop_on_soc::name` | Generator QH stop on SOC |
| 828726078 | `component::victron_gx::entity::sensor::generator_gen_id_qh_start_on_voltage::name` | Generator QH start on voltage |
| 828726077 | `component::victron_gx::entity::sensor::generator_gen_id_qh_start_on_soc::name` | Generator QH start on SOC |
| 828726076 | `component::victron_gx::entity::sensor::generator_gen_id_cool_down_timer::name` | Generator cooldown timer |
| 828726049 | `component::victron_gx::entity::sensor::evcharger_set_current::name` | Set current |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
