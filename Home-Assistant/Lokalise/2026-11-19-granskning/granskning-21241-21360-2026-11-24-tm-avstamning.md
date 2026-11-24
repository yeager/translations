# Home Assistant Core – historisk avstämning 21241–21360

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 50 direkta källtexter matchar HA Core-källan; 65 referensanvändningar med 49 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 5 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 21241 | 828726287 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::current_sensor_issue` | Current sensor issue | Problem med strömsensorn | Shared reference target checked |
| 21242 | 828726286 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::converter_issue` | Converter issue | Problem med konverterare | Shared reference target checked |
| 21243 | 828726285 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::charger_temperature_too_high` | Charger temperature too high | Laddartemperaturen är för hög | Shared reference target checked |
| 21244 | 828726284 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::charger_over_current` | Charger over current | Laddare överström | Shared reference target checked |
| 21245 | 828726283 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::charger_current_reversed` | Charger current reversed | Laddström omvänd | Shared reference target checked |
| 21246 | 828726282 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::bulk_time_limit_exceeded` | Bulk time limit exceeded | Tidsgränsen för bulköverföring har överskridits | Shared reference target checked |
| 21247 | 828726281 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::bms_connection_lost` | BMS connection lost | BMS-anslutningen förlorad | Shared reference target checked |
| 21248 | 828726280 | `component::victron_gx::entity::sensor::solarcharger_error_code::state::battery_voltage_too_high` | Battery voltage too high | Batterispänningen är för hög | Shared reference target checked |
| 21249 | 828726279 | `component::victron_gx::entity::sensor::solarcharger_error_code::name` | Error code | Felkod | Shared reference target checked |
| 21250 | 828726278 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::switched_off_power_switch` | Switched off (power switch) | Avstängd (strömbrytare) | Core-literal match |
| 21251 | 828726277 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::switched_off_device_mode_register` | Switched off (device mode register) | Avstängd (enhetslägesregister) | Core-literal match |
| 21252 | 828726276 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::signal_from_bms` | Signal from BMS | Signal från BMS | Core-literal match |
| 21253 | 828726275 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::remote_input` | Remote input | Fjärringång | Core-literal match |
| 21254 | 828726274 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::protective_action` | Protection active | Skyddet är aktiverat | Core-literal match |
| 21255 | 828726273 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::none` | - | - | Core-literal match |
| 21256 | 828726272 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::no_panel_power` | No/low panel power | Ingen/låg strömförsörjning till panelen | Core-literal match |
| 21257 | 828726271 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::no_input_power` | No/low input power | Ingen/låg ingångseffekt | Core-literal match |
| 21258 | 828726270 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::no_battery_power` | No/low battery power | Ingen/låg batterinivå | Core-literal match |
| 21259 | 828726269 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::need_token` | Need token for operation | Token krävs för drift | Core-literal match |
| 21260 | 828726268 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::low_temperature` | Low temperature | Låg temperatur | Shared reference target checked |
| 21261 | 828726267 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::engine_shutdown` | Engine shutdown on low input voltage | Motoravstängning vid låg ingångsspänning | Core-literal match |
| 21262 | 828726266 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::analysing_input_voltage` | Analysing input voltage | Analyserar ingångsspänning | Core-literal match |
| 21263 | 828726265 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::state::active_alarm` | Active alarm | Aktivt larm | Core-literal match |
| 21264 | 828726264 | `component::victron_gx::entity::sensor::solarcharger_device_off_reason::name` | Device-off reason | Orsak till att enheten är avstängd | Core-literal match |
| 21265 | 828726263 | `component::victron_gx::entity::sensor::solarcharger_dc_voltage::name` | DC (battery) bus voltage | DC (batteri) busspänning | Core-literal match |
| 21266 | 828726262 | `component::victron_gx::entity::sensor::solarcharger_dc_current::name` | DC (battery) bus current | DC (batteri) busström | Core-literal match |
| 21267 | 828726261 | `component::victron_gx::entity::sensor::solarcharger_current::name` | PV bus current | PV busström | Core-literal match |
| 21268 | 828726260 | `component::victron_gx::entity::sensor::pvinverter_yield_total::name` | Total yield | Total avkastning | Shared reference target checked |
| 21269 | 828726259 | `component::victron_gx::entity::sensor::pvinverter_yield_phase::name` | Yield {phase} | Avkastning {phase} | Core-literal match |
| 21270 | 828726258 | `component::victron_gx::entity::sensor::pvinverter_voltage_phase::name` | Voltage {phase} | Spänning {phase} | Core-literal match |
| 21271 | 828726257 | `component::victron_gx::entity::sensor::pvinverter_power_total::name` | Power total | Total effekt | Core-literal match |
| 21272 | 828726256 | `component::victron_gx::entity::sensor::pvinverter_power_phase::name` | Power {phase} | Effekt {phase} | Shared reference target checked |
| 21273 | 828726255 | `component::victron_gx::entity::sensor::pvinverter_current_phase::name` | Current {phase} | Ström {phase} | Core-literal match |
| 21274 | 828726254 | `component::victron_gx::entity::sensor::platform_venus_firmware_installed_version::name` | Installed version | Installerad version | Core-literal match |
| 21275 | 828726253 | `component::victron_gx::entity::sensor::platform_venus_firmware_available_version::name` | Available version | Tillgänglig version | Core-literal match |
| 21276 | 828726252 | `component::victron_gx::entity::sensor::multiplus_assist_current_boost_factor::unit_of_measurement` | factor | faktor | Source-path follow-up open |
| 21277 | 828726251 | `component::victron_gx::entity::sensor::multiplus_assist_current_boost_factor::name` | Assist current boost factor | Assistansströms boostfaktor | Source-path follow-up open |
| 21278 | 828726250 | `component::victron_gx::entity::sensor::multi_yield_yesterday::name` | Yield yesterday | Avkastning i går | Shared reference target checked |
| 21279 | 828726249 | `component::victron_gx::entity::sensor::multi_yield_today::name` | Yield today | Avkastning i dag | Shared reference target checked |
| 21280 | 828726248 | `component::victron_gx::entity::sensor::multi_total_pv_yield::name` | Total PV yield user | Total PV-avkastning för användare | Shared reference target checked |
| 21281 | 828726247 | `component::victron_gx::entity::sensor::multi_state::state::sustain_alt` | Sustain alt | Sustain alt | Shared reference target checked |
| 21282 | 828726246 | `component::victron_gx::entity::sensor::multi_state::state::sustain` | Sustain | Sustain | Shared reference target checked |
| 21283 | 828726245 | `component::victron_gx::entity::sensor::multi_state::state::storage` | Storage | Lagring | Shared reference target checked |
| 21284 | 828726244 | `component::victron_gx::entity::sensor::multi_state::state::starting_up` | Starting up | Startar upp | Shared reference target checked |
| 21285 | 828726243 | `component::victron_gx::entity::sensor::multi_state::state::scheduled_recharging` | Scheduled recharging | Schemalagd uppladdning | Shared reference target checked |
| 21286 | 828726242 | `component::victron_gx::entity::sensor::multi_state::state::repeated_absorption` | Repeated absorption | Upprepad absorption | Shared reference target checked |
| 21287 | 828726241 | `component::victron_gx::entity::sensor::multi_state::state::recharging` | Recharging | Uppladdar | Shared reference target checked |
| 21288 | 828726240 | `component::victron_gx::entity::sensor::multi_state::state::power_supply` | Power supply | Strömförsörjning | Shared reference target checked |
| 21289 | 828726239 | `component::victron_gx::entity::sensor::multi_state::state::power_assist` | Power Assist | Power Assist | Shared reference target checked |
| 21290 | 828726238 | `component::victron_gx::entity::sensor::multi_state::state::passthrough` | Passthrough | Genomströmning | Shared reference target checked |
| 21291 | 828726237 | `component::victron_gx::entity::sensor::multi_state::state::off` | Off | Av | Shared reference target checked |
| 21292 | 828726236 | `component::victron_gx::entity::sensor::multi_state::state::low_power` | Low power | Låg ström | Shared reference target checked |
| 21293 | 828726235 | `component::victron_gx::entity::sensor::multi_state::state::inverting` | Inverting | Växelriktar | Shared reference target checked |
| 21294 | 828726234 | `component::victron_gx::entity::sensor::multi_state::state::float` | Float | Flytande | Shared reference target checked |
| 21295 | 828726233 | `component::victron_gx::entity::sensor::multi_state::state::fault` | Fault | Fel | Shared reference target checked |
| 21296 | 828726232 | `component::victron_gx::entity::sensor::multi_state::state::external_control` | External control | Extern styrning | Shared reference target checked |
| 21297 | 828726231 | `component::victron_gx::entity::sensor::multi_state::state::equalize` | Equalize | Utjämna | Shared reference target checked |
| 21298 | 828726230 | `component::victron_gx::entity::sensor::multi_state::state::discharging` | Discharging | Laddar ur | Shared reference target checked |
| 21299 | 828726229 | `component::victron_gx::entity::sensor::multi_state::state::bulk` | Bulk | Bulk | Shared reference target checked |
| 21300 | 828726228 | `component::victron_gx::entity::sensor::multi_state::state::battery_safe` | Battery Safe | Batteri säkert | Shared reference target checked |
| 21301 | 828726227 | `component::victron_gx::entity::sensor::multi_state::state::auto_equalize` | Auto equalize / recondition | Automatisk utjämning/rekonditionering | Shared reference target checked |
| 21302 | 828726226 | `component::victron_gx::entity::sensor::multi_state::state::absorption` | Absorption | Absorption | Shared reference target checked |
| 21303 | 828726225 | `component::victron_gx::entity::sensor::multi_state::name` | State | Tillstånd | Shared reference target checked |
| 21304 | 828726224 | `component::victron_gx::entity::sensor::multi_solar_to_battery::name` | Solar to battery | Solenergi till batteri | Core-literal match |
| 21305 | 828726223 | `component::victron_gx::entity::sensor::multi_solar_to_acout::name` | Solar to AC-out | Solenergi till AC-ut | Core-literal match |
| 21306 | 828726222 | `component::victron_gx::entity::sensor::multi_solar_to_acin1::name` | Solar to AC-in-1 | Solenergi till AC-in 1 | Core-literal match |
| 21307 | 828726221 | `component::victron_gx::entity::sensor::multi_shore_current_limit::name` | Shore current limit | Gräns för landström | Source-path follow-up open |
| 21308 | 828726220 | `component::victron_gx::entity::sensor::multi_pv_power_total::name` | PV power total | PV-effekt totalt | Shared reference target checked |
| 21309 | 828726219 | `component::victron_gx::entity::sensor::multi_phases::unit_of_measurement` | phases | faser | Core-literal match |
| 21310 | 828726218 | `component::victron_gx::entity::sensor::multi_phases::name` | Phases | Faser | Core-literal match |
| 21311 | 828726217 | `component::victron_gx::entity::sensor::multi_mppt_mpptnumber_voltage::name` | MPPT {mpptnumber} PV voltage | MPPT {mpptnumber} PV-spänning | Core-literal match |
| 21312 | 828726216 | `component::victron_gx::entity::sensor::multi_mppt_mpptnumber_state::state::voltage_current_limited` | Voltage/current limited | Spänning/ström begränsad | Shared reference target checked |
| 21313 | 828726215 | `component::victron_gx::entity::sensor::multi_mppt_mpptnumber_state::state::off` | Off | Av | Shared reference target checked |
| 21314 | 828726214 | `component::victron_gx::entity::sensor::multi_mppt_mpptnumber_state::state::not_available` | Not available | Inte tillgänglig | Shared reference target checked |
| 21315 | 828726213 | `component::victron_gx::entity::sensor::multi_mppt_mpptnumber_state::state::mppt_active` | MPPT active | MPPT aktiv | Shared reference target checked |
| 21316 | 828726212 | `component::victron_gx::entity::sensor::multi_mppt_mpptnumber_state::name` | MPPT {mpptnumber} state | MPPT {mpptnumber} tillstånd | Source-path follow-up open |
| 21317 | 828726211 | `component::victron_gx::entity::sensor::multi_mppt_mpptnumber_power::name` | MPPT {mpptnumber} power | MPPT {mpptnumber} effekt | Core-literal match |
| 21318 | 828726210 | `component::victron_gx::entity::sensor::multi_mppt_mppt_id_yield_yesterday::name` | MPPT {mppt_id} yield yesterday | MPPT {mppt_id} avkastning igår | Core-literal match |
| 21319 | 828726209 | `component::victron_gx::entity::sensor::multi_mppt_mppt_id_yield_today::name` | MPPT {mppt_id} yield today | MPPT {mppt_id} avkastning idag | Core-literal match |
| 21320 | 828726208 | `component::victron_gx::entity::sensor::multi_max_power_yesterday::name` | Max power yesterday | Maxeffekt i går | Shared reference target checked |
| 21321 | 828726207 | `component::victron_gx::entity::sensor::multi_max_power_today::name` | Max power today | Maxeffekt i dag | Shared reference target checked |
| 21322 | 828726206 | `component::victron_gx::entity::sensor::multi_inverter_to_acout::name` | Inverter to AC-out | Växelriktare till AC-ut | Core-literal match |
| 21323 | 828726205 | `component::victron_gx::entity::sensor::multi_inverter_to_acin1::name` | Inverter to AC-in-1 | Växelriktare till AC-in 1 | Core-literal match |
| 21324 | 828726204 | `component::victron_gx::entity::sensor::multi_inverter_power_setpoint::name` | Inverter power setpoint | Växelriktarens effektbörvärde | Core-literal match |
| 21325 | 828726203 | `component::victron_gx::entity::sensor::multi_ess_mode::state::self_consumption_batterylife` | Self-consumption (BatteryLife) | Egenförbrukning (BatteryLife) | Core-literal match |
| 21326 | 828726202 | `component::victron_gx::entity::sensor::multi_ess_mode::state::self_consumption` | Self-consumption | Egenförbrukning | Shared reference target checked |
| 21327 | 828726201 | `component::victron_gx::entity::sensor::multi_ess_mode::state::keep_charged` | Keep charged | Håll laddad | Core-literal match |
| 21328 | 828726200 | `component::victron_gx::entity::sensor::multi_ess_mode::state::external_control` | External control | Extern styrning | Shared reference target checked |
| 21329 | 828726199 | `component::victron_gx::entity::sensor::multi_ess_mode::name` | ESS mode | ESS-läge | Shared reference target checked |
| 21330 | 828726198 | `component::victron_gx::entity::sensor::multi_ess_min_soc_limit::name` | ESS minimum SOC limit | ESS minsta SOC-gräns | Source-path follow-up open |
| 21331 | 828726197 | `component::victron_gx::entity::sensor::multi_ess_ac_power_setpoint::name` | ESS AC power setpoint | ESS AC-effekt börvärde | Core-literal match |
| 21332 | 828726196 | `component::victron_gx::entity::sensor::multi_active_input::state::disconnected` | Disconnected | Frånkopplad | Shared reference target checked |
| 21333 | 828726195 | `component::victron_gx::entity::sensor::multi_active_input::state::ac_input_2` | AC input 2 | AC-ingång 2 | Core-literal match |
| 21334 | 828726194 | `component::victron_gx::entity::sensor::multi_active_input::state::ac_input_1` | AC input 1 | AC-ingång 1 | Core-literal match |
| 21335 | 828726193 | `component::victron_gx::entity::sensor::multi_active_input::name` | Active AC input | Aktiv AC-ingång | Shared reference target checked |
| 21336 | 828726192 | `component::victron_gx::entity::sensor::multi_acout_to_inverter::name` | AC-out to inverter | AC-ut till växelriktare | Core-literal match |
| 21337 | 828726191 | `component::victron_gx::entity::sensor::multi_acout_to_acin1::name` | AC-out to AC-in-1 | AC-ut till AC-in 1 | Core-literal match |
| 21338 | 828726190 | `component::victron_gx::entity::sensor::multi_acout_output_voltage_phase::name` | AC-out-{output} voltage on {phase} | AC-ut {output} spänning på {phase} | Core-literal match |
| 21339 | 828726189 | `component::victron_gx::entity::sensor::multi_acout_output_power_phase::name` | AC-out-{output} power on {phase} | AC-ut {output} effekt på {phase} | Core-literal match |
| 21340 | 828726188 | `component::victron_gx::entity::sensor::multi_acout_output_current_phase::name` | AC-out-{output} current on {phase} | AC-ut {output} ström på {phase} | Core-literal match |
| 21341 | 828726187 | `component::victron_gx::entity::sensor::multi_acin_voltage_phase::name` | Input voltage on {phase} | Ingångsspänning på {phase} | Core-literal match |
| 21342 | 828726186 | `component::victron_gx::entity::sensor::multi_acin_power_phase::name` | Input power on {phase} | Ingångseffekt på {phase} | Core-literal match |
| 21343 | 828726185 | `component::victron_gx::entity::sensor::multi_acin_current_phase::name` | Input current on {phase} | Ingångsström på {phase} | Core-literal match |
| 21344 | 828726184 | `component::victron_gx::entity::sensor::multi_acin1_to_inverter::name` | AC-in-1 to inverter | AC-in 1 till växelriktare | Core-literal match |
| 21345 | 828726183 | `component::victron_gx::entity::sensor::multi_acin1_to_acout::name` | AC-in-1 to AC-out | AC-in 1 till AC-ut | Core-literal match |
| 21346 | 828726182 | `component::victron_gx::entity::sensor::inverter_total_pv_yield_user::name` | Total PV yield user | Total PV-avkastning för användare | Shared reference target checked |
| 21347 | 828726181 | `component::victron_gx::entity::sensor::inverter_total_pv_yield_system::name` | Total PV yield system | Total PV-avkastning för system | Shared reference target checked |
| 21348 | 828726180 | `component::victron_gx::entity::sensor::inverter_state::state::sustain_alt` | Sustain alt | Sustain alt | Shared reference target checked |
| 21349 | 828726179 | `component::victron_gx::entity::sensor::inverter_state::state::sustain` | Sustain | Sustain | Shared reference target checked |
| 21350 | 828726178 | `component::victron_gx::entity::sensor::inverter_state::state::storage` | Storage | Lagring | Shared reference target checked |
| 21351 | 828726177 | `component::victron_gx::entity::sensor::inverter_state::state::starting_up` | Starting up | Startar upp | Shared reference target checked |
| 21352 | 828726176 | `component::victron_gx::entity::sensor::inverter_state::state::scheduled_recharging` | Scheduled recharging | Schemalagd uppladdning | Shared reference target checked |
| 21353 | 828726175 | `component::victron_gx::entity::sensor::inverter_state::state::repeated_absorption` | Repeated absorption | Upprepad absorption | Shared reference target checked |
| 21354 | 828726174 | `component::victron_gx::entity::sensor::inverter_state::state::recharging` | Recharging | Uppladdar | Shared reference target checked |
| 21355 | 828726173 | `component::victron_gx::entity::sensor::inverter_state::state::power_supply` | Power supply | Strömförsörjning | Shared reference target checked |
| 21356 | 828726172 | `component::victron_gx::entity::sensor::inverter_state::state::power_assist` | Power Assist | Power Assist | Shared reference target checked |
| 21357 | 828726171 | `component::victron_gx::entity::sensor::inverter_state::state::passthrough` | Passthrough | Genomströmning | Shared reference target checked |
| 21358 | 828726170 | `component::victron_gx::entity::sensor::inverter_state::state::off` | Off | Av | Shared reference target checked |
| 21359 | 828726169 | `component::victron_gx::entity::sensor::inverter_state::state::low_power` | Low power | Låg ström | Shared reference target checked |
| 21360 | 828726168 | `component::victron_gx::entity::sensor::inverter_state::state::inverting` | Inverting | Växelriktar | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 828726252 | `component::victron_gx::entity::sensor::multiplus_assist_current_boost_factor::unit_of_measurement` | factor |
| 828726251 | `component::victron_gx::entity::sensor::multiplus_assist_current_boost_factor::name` | Assist current boost factor |
| 828726221 | `component::victron_gx::entity::sensor::multi_shore_current_limit::name` | Shore current limit |
| 828726212 | `component::victron_gx::entity::sensor::multi_mppt_mpptnumber_state::name` | MPPT {mpptnumber} state |
| 828726198 | `component::victron_gx::entity::sensor::multi_ess_min_soc_limit::name` | ESS minimum SOC limit |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
