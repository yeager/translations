# Home Assistant Core – historisk avstämning 21121–21240

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 53 direkta källtexter matchar HA Core-källan; 60 referensanvändningar med 53 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 7 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 21121 | 828726407 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::idle_scheduled_feedin` | Idle scheduled feed-in | Inaktiv schemalagd inmatning | Core-literal match |
| 21122 | 828726406 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::idle_no_opportunity` | Idle no opportunity | Inaktiv inget tillfälle | Core-literal match |
| 21123 | 828726405 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::idle_maintain_targetsoc` | Idle maintain target SoC | Inaktiv behåll mål för SoC | Core-literal match |
| 21124 | 828726404 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::idle_maintain_surplus` | Idle maintain surplus | Inaktiv behåll överskott | Core-literal match |
| 21125 | 828726403 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::ess_low_soc` | ESS low SoC | ESS låg SoC | Core-literal match |
| 21126 | 828726402 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::state::dess_disabled` | DESS disabled | DESS inaktiverad | Core-literal match |
| 21127 | 828726401 | `component::victron_gx::entity::sensor::system_dynamicess_reactive_strategy::name` | Dynamic ESS reactive strategy | Dynamisk ESS reaktiv strategi | Core-literal match |
| 21128 | 828726400 | `component::victron_gx::entity::sensor::system_dynamicess_minimum_soc::name` | Dynamic ESS minimum SoC | Dynamisk ESS minsta SoC | Core-literal match |
| 21129 | 828726399 | `component::victron_gx::entity::sensor::system_dynamicess_last_scheduled_start::name` | Dynamic ESS last scheduled start | Dynamisk ESS senaste schemalagda start | Core-literal match |
| 21130 | 828726398 | `component::victron_gx::entity::sensor::system_dynamicess_last_scheduled_end::name` | Dynamic ESS last scheduled end | Dynamisk ESS senaste schemalagda slut | Core-literal match |
| 21131 | 828726397 | `component::victron_gx::entity::sensor::system_dynamicess_error::state::soc_low` | SoC low | SoC låg | Core-literal match |
| 21132 | 828726396 | `component::victron_gx::entity::sensor::system_dynamicess_error::state::no_schedule` | No matching schedule | Inget matchande schema | Core-literal match |
| 21133 | 828726395 | `component::victron_gx::entity::sensor::system_dynamicess_error::state::no_ess` | No ESS | Ingen ESS | Core-literal match |
| 21134 | 828726394 | `component::victron_gx::entity::sensor::system_dynamicess_error::state::no_error` | No error | Inget fel | Shared reference target checked |
| 21135 | 828726393 | `component::victron_gx::entity::sensor::system_dynamicess_error::state::ess_mode` | ESS mode | ESS-läge | Shared reference target checked |
| 21136 | 828726392 | `component::victron_gx::entity::sensor::system_dynamicess_error::state::battry_capacity_not_configured` | Battery capacity not configured | Batterikapaciteten är inte konfigurerad | Core-literal match |
| 21137 | 828726391 | `component::victron_gx::entity::sensor::system_dynamicess_error::name` | Dynamic ESS error | Dynamisk ESS fel | Core-literal match |
| 21138 | 828726390 | `component::victron_gx::entity::sensor::system_dynamicess_available_overhead::name` | Dynamic ESS available overhead | Dynamisk ESS tillgänglig overhead | Core-literal match |
| 21139 | 828726389 | `component::victron_gx::entity::sensor::system_dc_pv_power::name` | PV power | PV effekt | Core-literal match |
| 21140 | 828726388 | `component::victron_gx::entity::sensor::system_dc_pv_energy::name` | PV energy | PV energi | Core-literal match |
| 21141 | 828726387 | `component::victron_gx::entity::sensor::system_dc_pv_current::name` | PV current | PV-ström | Shared reference target checked |
| 21142 | 828726386 | `component::victron_gx::entity::sensor::system_dc_consumption::name` | DC consumption | DC förbrukning | Core-literal match |
| 21143 | 828726385 | `component::victron_gx::entity::sensor::system_dc_battery_voltage::name` | DC battery voltage | DC-batteri spänning | Core-literal match |
| 21144 | 828726384 | `component::victron_gx::entity::sensor::system_dc_battery_state::state::idle` | Idle | Inaktiv | Shared reference target checked |
| 21145 | 828726383 | `component::victron_gx::entity::sensor::system_dc_battery_state::state::discharging` | Discharging | Laddar ur | Shared reference target checked |
| 21146 | 828726382 | `component::victron_gx::entity::sensor::system_dc_battery_state::state::charging` | Charging | Laddar | Shared reference target checked |
| 21147 | 828726381 | `component::victron_gx::entity::sensor::system_dc_battery_state::name` | DC battery state | DC-batteri tillstånd | Core-literal match |
| 21148 | 828726380 | `component::victron_gx::entity::sensor::system_dc_battery_soc::name` | DC battery charge | DC-batteri laddning | Core-literal match |
| 21149 | 828726379 | `component::victron_gx::entity::sensor::system_dc_battery_power::name` | DC battery power | DC-batteri effekt | Core-literal match |
| 21150 | 828726378 | `component::victron_gx::entity::sensor::system_dc_battery_discharge_energy::name` | DC battery discharge energy | DC-batteri urladdningsenergi | Core-literal match |
| 21151 | 828726377 | `component::victron_gx::entity::sensor::system_dc_battery_current::name` | DC battery current | DC-batteri ström | Core-literal match |
| 21152 | 828726376 | `component::victron_gx::entity::sensor::system_dc_battery_charge_energy::name` | DC battery charge energy | DC-batteri laddningsenergi | Core-literal match |
| 21153 | 828726375 | `component::victron_gx::entity::sensor::system_dc_alternator_power::name` | DC alternator power | DC-generator effekt | Core-literal match |
| 21154 | 828726374 | `component::victron_gx::entity::sensor::system_critical_loads_phase::name` | Critical loads on {phase} | Kritiska laster på {phase} | Core-literal match |
| 21155 | 828726373 | `component::victron_gx::entity::sensor::system_control_scheduled_soc::name` | Scheduled SoC | Schemalagd SoC | Core-literal match |
| 21156 | 828726372 | `component::victron_gx::entity::sensor::system_control_active_soc_limit::name` | Active SoC limit | Aktiv SoC-gräns | Core-literal match |
| 21157 | 828726371 | `component::victron_gx::entity::sensor::system_consumption_power_phase::name` | Consumption power {phase} | Förbrukning effekt {phase} | Core-literal match |
| 21158 | 828726370 | `component::victron_gx::entity::sensor::system_consumption_phases::unit_of_measurement` | phases | faser | Core-literal match |
| 21159 | 828726369 | `component::victron_gx::entity::sensor::system_consumption_phases::name` | Consumption phases | Förbrukning faser | Core-literal match |
| 21160 | 828726368 | `component::victron_gx::entity::sensor::system_consumption_on_output_phases::unit_of_measurement` | phases | faser | Core-literal match |
| 21161 | 828726367 | `component::victron_gx::entity::sensor::system_consumption_on_output_phases::name` | Consumption on output phases | Förbrukning på utgångsfaser | Core-literal match |
| 21162 | 828726366 | `component::victron_gx::entity::sensor::system_consumption_current_phase::name` | Consumption current {phase} | Förbrukning ström {phase} | Core-literal match |
| 21163 | 828726365 | `component::victron_gx::entity::sensor::system_ac_power_set_point::name` | AC power setpoint | AC-effekt börvärde | Source-path follow-up open |
| 21164 | 828726364 | `component::victron_gx::entity::sensor::system_ac_loads_phase::name` | AC loads on {phase} | AC-belastningar på {phase} | Core-literal match |
| 21165 | 828726363 | `component::victron_gx::entity::sensor::system_ac_input_limit::name` | AC input limit | AC-ingångsgräns | Source-path follow-up open |
| 21166 | 828726362 | `component::victron_gx::entity::sensor::system_ac_export_limit::name` | AC export limit | AC-exportgräns | Source-path follow-up open |
| 21167 | 828726361 | `component::victron_gx::entity::sensor::system_ac_active_input_source::state::unknown` | Unknown | Okänd | Shared reference target checked |
| 21168 | 828726360 | `component::victron_gx::entity::sensor::system_ac_active_input_source::state::shore_power` | Shore power | Landström | Shared reference target checked |
| 21169 | 828726359 | `component::victron_gx::entity::sensor::system_ac_active_input_source::state::not_connected` | Not connected | Inte ansluten | Shared reference target checked |
| 21170 | 828726358 | `component::victron_gx::entity::sensor::system_ac_active_input_source::state::grid` | Grid | Elnät | Shared reference target checked |
| 21171 | 828726357 | `component::victron_gx::entity::sensor::system_ac_active_input_source::state::generator` | Generator | Generator | Shared reference target checked |
| 21172 | 828726356 | `component::victron_gx::entity::sensor::system_ac_active_input_source::name` | AC active input source | Aktiv AC-ingångskälla | Core-literal match |
| 21173 | 828726355 | `component::victron_gx::entity::sensor::switchable_output_output_custom_name::name` | Switchable output {output} custom name | Omkopplingsbar utgång {output} anpassat namn | Source-path follow-up open |
| 21174 | 828726354 | `component::victron_gx::entity::sensor::switch_output_dimming::unit_of_measurement` | % | % | Source-path follow-up open |
| 21175 | 828726353 | `component::victron_gx::entity::sensor::switch_output_dimming::name` | {output} dimming | {output} dimning | Source-path follow-up open |
| 21176 | 828726352 | `component::victron_gx::entity::sensor::switch_output_custom_name::name` | {output} custom name | {output} anpassat namn | Source-path follow-up open |
| 21177 | 828726351 | `component::victron_gx::entity::sensor::solarcharger_yield_yesterday::name` | Yield yesterday | Avkastning i går | Shared reference target checked |
| 21178 | 828726350 | `component::victron_gx::entity::sensor::solarcharger_yield_total::name` | Total yield | Total avkastning | Shared reference target checked |
| 21179 | 828726349 | `component::victron_gx::entity::sensor::solarcharger_yield_today::name` | Yield today | Avkastning i dag | Shared reference target checked |
| 21180 | 828726348 | `component::victron_gx::entity::sensor::solarcharger_yield_power::name` | PV yield power | PV avkastning effekt | Core-literal match |
| 21181 | 828726347 | `component::victron_gx::entity::sensor::solarcharger_voltage::name` | PV bus voltage | PV-buss spänning | Shared reference target checked |
| 21182 | 828726346 | `component::victron_gx::entity::sensor::solarcharger_tracker_tracker_yield_today::name` | Tracker {tracker} yield today | Spårare {tracker} avkastning idag | Core-literal match |
| 21183 | 828726345 | `component::victron_gx::entity::sensor::solarcharger_tracker_tracker_voltage::name` | PV tracker {tracker} voltage | PV-spårare {tracker} spänning | Core-literal match |
| 21184 | 828726344 | `component::victron_gx::entity::sensor::solarcharger_tracker_tracker_power::name` | PV tracker {tracker} power | PV-spårare {tracker} effekt | Core-literal match |
| 21185 | 828726343 | `component::victron_gx::entity::sensor::solarcharger_tracker_tracker_operation_mode::state::voltage_current_limited` | Voltage/current limited | Spänning/ström begränsad | Shared reference target checked |
| 21186 | 828726342 | `component::victron_gx::entity::sensor::solarcharger_tracker_tracker_operation_mode::state::off` | Off | Av | Shared reference target checked |
| 21187 | 828726341 | `component::victron_gx::entity::sensor::solarcharger_tracker_tracker_operation_mode::state::not_available` | Not available | Inte tillgänglig | Shared reference target checked |
| 21188 | 828726340 | `component::victron_gx::entity::sensor::solarcharger_tracker_tracker_operation_mode::state::mppt_active` | MPPT active | MPPT aktiv | Shared reference target checked |
| 21189 | 828726339 | `component::victron_gx::entity::sensor::solarcharger_tracker_tracker_operation_mode::name` | PV tracker {tracker} operation mode | PV-spårare {tracker} driftläge | Core-literal match |
| 21190 | 828726338 | `component::victron_gx::entity::sensor::solarcharger_tracker_tracker_name::name` | PV tracker {tracker} name | PV-spårare {tracker} namn | Core-literal match |
| 21191 | 828726337 | `component::victron_gx::entity::sensor::solarcharger_tracker_tracker_max_voltage_today::name` | Tracker {tracker} max voltage today | Spårare {tracker} max spänning idag | Core-literal match |
| 21192 | 828726336 | `component::victron_gx::entity::sensor::solarcharger_tracker_tracker_max_power_today::name` | Tracker {tracker} max power today | Spårare {tracker} max effekt idag | Core-literal match |
| 21193 | 828726335 | `component::victron_gx::entity::sensor::solarcharger_time_in_float_today::name` | Time in float today | Tid i float idag | Core-literal match |
| 21194 | 828726334 | `component::victron_gx::entity::sensor::solarcharger_time_in_bulk_today::name` | Time in bulk today | Tid i bulk idag | Core-literal match |
| 21195 | 828726333 | `component::victron_gx::entity::sensor::solarcharger_time_in_absorption_today::name` | Time in absorption today | Tid i absorption idag | Core-literal match |
| 21196 | 828726332 | `component::victron_gx::entity::sensor::solarcharger_state::state::sustain_alt` | Sustain alt | Sustain alt | Shared reference target checked |
| 21197 | 828726331 | `component::victron_gx::entity::sensor::solarcharger_state::state::sustain` | Sustain | Sustain | Shared reference target checked |
| 21198 | 828726330 | `component::victron_gx::entity::sensor::solarcharger_state::state::storage` | Storage | Lagring | Shared reference target checked |
| 21199 | 828726329 | `component::victron_gx::entity::sensor::solarcharger_state::state::starting_up` | Starting up | Startar upp | Shared reference target checked |
| 21200 | 828726328 | `component::victron_gx::entity::sensor::solarcharger_state::state::scheduled_recharging` | Scheduled recharging | Schemalagd uppladdning | Shared reference target checked |
| 21201 | 828726327 | `component::victron_gx::entity::sensor::solarcharger_state::state::repeated_absorption` | Repeated absorption | Upprepad absorption | Shared reference target checked |
| 21202 | 828726326 | `component::victron_gx::entity::sensor::solarcharger_state::state::recharging` | Recharging | Uppladdar | Shared reference target checked |
| 21203 | 828726325 | `component::victron_gx::entity::sensor::solarcharger_state::state::power_supply` | Power supply | Strömförsörjning | Shared reference target checked |
| 21204 | 828726324 | `component::victron_gx::entity::sensor::solarcharger_state::state::power_assist` | Power Assist | Power Assist | Shared reference target checked |
| 21205 | 828726323 | `component::victron_gx::entity::sensor::solarcharger_state::state::passthrough` | Passthrough | Genomströmning | Shared reference target checked |
| 21206 | 828726322 | `component::victron_gx::entity::sensor::solarcharger_state::state::off` | Off | Av | Shared reference target checked |
| 21207 | 828726321 | `component::victron_gx::entity::sensor::solarcharger_state::state::low_power` | Low power | Låg ström | Shared reference target checked |
| 21208 | 828726320 | `component::victron_gx::entity::sensor::solarcharger_state::state::inverting` | Inverting | Växelriktar | Shared reference target checked |
| 21209 | 828726319 | `component::victron_gx::entity::sensor::solarcharger_state::state::float` | Float | Flytande | Shared reference target checked |
| 21210 | 828726318 | `component::victron_gx::entity::sensor::solarcharger_state::state::fault` | Fault | Fel | Shared reference target checked |
| 21211 | 828726317 | `component::victron_gx::entity::sensor::solarcharger_state::state::external_control` | External control | Extern styrning | Shared reference target checked |
| 21212 | 828726316 | `component::victron_gx::entity::sensor::solarcharger_state::state::equalize` | Equalize | Utjämna | Shared reference target checked |
| 21213 | 828726315 | `component::victron_gx::entity::sensor::solarcharger_state::state::discharging` | Discharging | Laddar ur | Shared reference target checked |
| 21214 | 828726314 | `component::victron_gx::entity::sensor::solarcharger_state::state::bulk` | Bulk | Bulk | Shared reference target checked |
| 21215 | 828726313 | `component::victron_gx::entity::sensor::solarcharger_state::state::battery_safe` | Battery Safe | Batteri säkert | Shared reference target checked |
| 21216 | 828726312 | `component::victron_gx::entity::sensor::solarcharger_state::state::auto_equalize` | Auto equalize / recondition | Automatisk utjämning/rekonditionering | Shared reference target checked |
| 21217 | 828726311 | `component::victron_gx::entity::sensor::solarcharger_state::state::absorption` | Absorption | Absorption | Shared reference target checked |
| 21218 | 828726310 | `component::victron_gx::entity::sensor::solarcharger_state::name` | State | Tillstånd | Shared reference target checked |
| 21219 | 828726309 | `component::victron_gx::entity::sensor::solarcharger_mppt_operation_mode::state::voltage_current_limited` | Voltage/current limited | Spänning/ström begränsad | Shared reference target checked |
| 21220 | 828726308 | `component::victron_gx::entity::sensor::solarcharger_mppt_operation_mode::state::off` | Off | Av | Shared reference target checked |
| 21221 | 828726307 | `component::victron_gx::entity::sensor::solarcharger_mppt_operation_mode::state::not_available` | Not available | Inte tillgänglig | Shared reference target checked |
| 21222 | 828726306 | `component::victron_gx::entity::sensor::solarcharger_mppt_operation_mode::state::mppt_active` | MPPT active | MPPT aktiv | Shared reference target checked |
| 21223 | 828726305 | `component::victron_gx::entity::sensor::solarcharger_mppt_operation_mode::name` | MPPT operation mode | MPPT-driftläge | Core-literal match |
| 21224 | 828726304 | `component::victron_gx::entity::sensor::solarcharger_min_battery_voltage_today::name` | Min battery voltage today | Lägsta batterispänning idag | Core-literal match |
| 21225 | 828726303 | `component::victron_gx::entity::sensor::solarcharger_max_power_yesterday::name` | Max power yesterday | Maxeffekt i går | Shared reference target checked |
| 21226 | 828726302 | `component::victron_gx::entity::sensor::solarcharger_max_power_today::name` | Max power today | Maxeffekt i dag | Shared reference target checked |
| 21227 | 828726301 | `component::victron_gx::entity::sensor::solarcharger_max_battery_voltage_today::name` | Max battery voltage today | Högsta batterispänning idag | Core-literal match |
| 21228 | 828726300 | `component::victron_gx::entity::sensor::solarcharger_load_current::name` | Load bus current | Lastbusström | Core-literal match |
| 21229 | 828726299 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::user_settings_invalid` | User settings invalid | Ogiltiga användarinställningar | Shared reference target checked |
| 21230 | 828726298 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::terminals_overheated` | Terminals overheated | Terminaler överhettade | Shared reference target checked |
| 21231 | 828726297 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::synchronized_charging_config_issue` | Synchronized charging config issue | Problem med konfiguration av synkroniserad laddning | Shared reference target checked |
| 21232 | 828726296 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::no_error` | No error | Inget fel | Shared reference target checked |
| 21233 | 828726295 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::network_misconfigured` | Network misconfigured | Nätverket är felkonfigurerat | Shared reference target checked |
| 21234 | 828726294 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::lost_communication_with_device` | Lost communication with device | Förlorade kommunikation med enheten | Shared reference target checked |
| 21235 | 828726293 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::invalid_incompatible_firmware` | Invalid/incompatible firmware | Ogiltig/inkompatibel firmware | Shared reference target checked |
| 21236 | 828726292 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::input_voltage_too_high` | Input voltage too high (solar panel) | För hög ingångsspänning (solpanel) | Shared reference target checked |
| 21237 | 828726291 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::input_shutdown_reverse_current` | Input shutdown (reverse current) | Ingångsavstängning (omvänd ström) | Shared reference target checked |
| 21238 | 828726290 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::input_shutdown_battery_voltage_too_high` | Input shutdown (battery voltage too high) | Ingångsavstängning (överspänning i batteri) | Shared reference target checked |
| 21239 | 828726289 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::input_current_too_high` | Input current too high (solar panel) | För hög ingångsström (solpanel) | Shared reference target checked |
| 21240 | 828726288 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::factory_calibration_data_lost` | Factory calibration data lost | Fabriksinställningarna har gått förlorade | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 828726365 | `component::victron_gx::entity::sensor::system_ac_power_set_point::name` | AC power setpoint |
| 828726363 | `component::victron_gx::entity::sensor::system_ac_input_limit::name` | AC input limit |
| 828726362 | `component::victron_gx::entity::sensor::system_ac_export_limit::name` | AC export limit |
| 828726355 | `component::victron_gx::entity::sensor::switchable_output_output_custom_name::name` | Switchable output {output} custom name |
| 828726354 | `component::victron_gx::entity::sensor::switch_output_dimming::unit_of_measurement` | % |
| 828726353 | `component::victron_gx::entity::sensor::switch_output_dimming::name` | {output} dimming |
| 828726352 | `component::victron_gx::entity::sensor::switch_output_custom_name::name` | {output} custom name |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
