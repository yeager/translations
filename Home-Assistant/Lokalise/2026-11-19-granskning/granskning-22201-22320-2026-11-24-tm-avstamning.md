# Home Assistant Core – historisk avstämning 22201–22320

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 30 direkta källtexter matchar HA Core-källan; 30 referensanvändningar med 15 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 60 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 22201 | 823405925 | `component::battery::triggers::not_low::fields::behavior::description` | The behavior of the targeted batteries to trigger on. | Det beteende som ska trigga för valda batterier. | Source-path follow-up open |
| 22202 | 823405924 | `component::battery::triggers::not_low::description` | Triggers after one or more batteries are no longer low. | Utlöses när ett eller flera batterier inte längre är låga. | Source-path follow-up open |
| 22203 | 823405923 | `component::battery::triggers::low::name` | Battery low | Låg batterinivå | Source-path follow-up open |
| 22204 | 823405922 | `component::battery::triggers::low::fields::behavior::name` | Trigger when | Utlös när | Source-path follow-up open |
| 22205 | 823405921 | `component::battery::triggers::low::fields::behavior::description` | The behavior of the targeted batteries to trigger on. | Det beteende som ska trigga för valda batterier. | Source-path follow-up open |
| 22206 | 823405920 | `component::battery::triggers::low::description` | Triggers after one or more batteries become low. | Utlöses när ett eller flera batterier blir låga. | Source-path follow-up open |
| 22207 | 823405919 | `component::battery::triggers::level_crossed_threshold::name` | Battery level crossed threshold | Batterinivån har passerat tröskelvärdet | Core-literal match |
| 22208 | 823405918 | `component::battery::triggers::level_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22209 | 823405917 | `component::battery::triggers::level_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22210 | 823405916 | `component::battery::triggers::level_crossed_threshold::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 22211 | 823405915 | `component::battery::triggers::level_crossed_threshold::fields::behavior::description` | The behavior of the targeted batteries to trigger on. | Det beteende som ska trigga för valda batterier. | Source-path follow-up open |
| 22212 | 823405914 | `component::battery::triggers::level_crossed_threshold::description` | Triggers when the battery level of one or more batteries crosses a threshold. | Utlöses när batterinivån för ett eller flera batterier passerar ett tröskelvärde. | Core-literal match |
| 22213 | 823405913 | `component::battery::triggers::level_changed::name` | Battery level changed | Batterinivå ändras | Core-literal match |
| 22214 | 823405912 | `component::battery::triggers::level_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22215 | 823405911 | `component::battery::triggers::level_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22216 | 823405910 | `component::battery::triggers::level_changed::description` | Triggers when the battery level of one or more batteries changes. | Utlöses när batterinivån för ett eller flera batterier förändras. | Core-literal match |
| 22217 | 823405909 | `component::battery::selector::trigger_behavior::options::last` | Last | Sista | Source-path follow-up open |
| 22218 | 823405908 | `component::battery::selector::trigger_behavior::options::first` | First | Första | Source-path follow-up open |
| 22219 | 823405907 | `component::battery::selector::trigger_behavior::options::any` | Any | Något | Source-path follow-up open |
| 22220 | 823405906 | `component::battery::common::trigger_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22221 | 823405905 | `component::battery::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22222 | 823405904 | `component::battery::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22223 | 823405903 | `component::battery::common::trigger_behavior_name` | Trigger when | Utlös när | Core-literal match |
| 22224 | 823405902 | `component::battery::common::trigger_behavior_description` | The behavior of the targeted batteries to trigger on. | Det beteende som ska trigga för valda batterier. | Source-path follow-up open |
| 22225 | 823247160 | `component::humidifier::triggers::mode_changed::name` | Humidifier mode changed | Luftfuktarens läge har ändrats | Core-literal match |
| 22226 | 823247159 | `component::humidifier::triggers::mode_changed::fields::mode::name` | Mode | Läge | Core-literal match |
| 22227 | 823247158 | `component::humidifier::triggers::mode_changed::fields::mode::description` | The operation modes to trigger on. | De driftlägen att utlösa på. | Core-literal match |
| 22228 | 823247157 | `component::humidifier::triggers::mode_changed::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 22229 | 823247156 | `component::humidifier::triggers::mode_changed::fields::behavior::description` | The behavior of the targeted humidifiers to trigger on. | Det beteende som ska trigga för valda luftfuktare. | Source-path follow-up open |
| 22230 | 823247155 | `component::humidifier::triggers::mode_changed::description` | Triggers when the operation mode of one or more humidifiers changes. | Utlöses när driftläget för en eller flera luftfuktare förändras. | Core-literal match |
| 22231 | 823059396 | `component::water_heater::triggers::operation_mode_changed::name` | Water heater operation mode changed | Driftläge för varmvattenberedare har ändrats | Core-literal match |
| 22232 | 823059395 | `component::water_heater::triggers::operation_mode_changed::fields::operation_mode::name` | Operation mode | Driftläge | Core-literal match |
| 22233 | 823059394 | `component::water_heater::triggers::operation_mode_changed::fields::operation_mode::description` | The operation modes to trigger on. | De driftlägen som ska utlösa automatiseringen. | Core-literal match |
| 22234 | 823059393 | `component::water_heater::triggers::operation_mode_changed::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 22235 | 823059392 | `component::water_heater::triggers::operation_mode_changed::fields::behavior::description` | The behavior of the targeted water heaters to trigger on. | Vilket beteende hos de valda varmvattenberedarna som ska utlösa automatiseringen. | Source-path follow-up open |
| 22236 | 823059391 | `component::water_heater::triggers::operation_mode_changed::description` | Triggers when the operation mode of one or more water heaters changes to a specific mode. | Utlöses när driftläget för en eller flera varmvattenberedare ändras till ett specifikt läge. | Core-literal match |
| 22237 | 823053419 | `component::water_heater::conditions::is_target_temperature::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22238 | 823053418 | `component::water_heater::conditions::is_target_temperature::fields::threshold::description` | What to test for and threshold values. | Vad som ska kontrolleras och vilka tröskelvärden som ska användas. | Source-path follow-up open |
| 22239 | 823053417 | `component::water_heater::common::condition_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22240 | 823053416 | `component::water_heater::common::condition_threshold_description` | What to test for and threshold values. | Vad som ska kontrolleras och vilka tröskelvärden som ska användas. | Source-path follow-up open |
| 22241 | 823053415 | `component::temperature::conditions::is_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22242 | 823053414 | `component::temperature::conditions::is_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22243 | 823053413 | `component::temperature::common::condition_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22244 | 823053412 | `component::temperature::common::condition_threshold_description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22245 | 823053411 | `component::power::conditions::is_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22246 | 823053410 | `component::power::conditions::is_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22247 | 823053409 | `component::power::common::condition_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22248 | 823053408 | `component::power::common::condition_threshold_description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22249 | 823053407 | `component::moisture::conditions::is_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22250 | 823053406 | `component::moisture::conditions::is_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22251 | 823053405 | `component::moisture::common::condition_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22252 | 823053404 | `component::moisture::common::condition_threshold_description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22253 | 823053403 | `component::illuminance::conditions::is_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22254 | 823053402 | `component::illuminance::conditions::is_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22255 | 823053401 | `component::illuminance::common::condition_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22256 | 823053400 | `component::illuminance::common::condition_threshold_description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22257 | 823053399 | `component::humidity::conditions::is_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22258 | 823053398 | `component::humidity::conditions::is_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22259 | 823053397 | `component::humidity::common::condition_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22260 | 823053396 | `component::humidity::common::condition_threshold_description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22261 | 823053395 | `component::humidifier::conditions::is_target_humidity::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22262 | 823053394 | `component::humidifier::conditions::is_target_humidity::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22263 | 823053393 | `component::humidifier::common::condition_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22264 | 823053392 | `component::humidifier::common::condition_threshold_description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22265 | 823053391 | `component::climate::conditions::target_temperature::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Source-path follow-up open |
| 22266 | 823053390 | `component::climate::conditions::target_temperature::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22267 | 823053389 | `component::climate::conditions::target_humidity::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Source-path follow-up open |
| 22268 | 823053388 | `component::climate::conditions::target_humidity::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22269 | 823053387 | `component::climate::common::condition_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22270 | 823053386 | `component::climate::common::condition_threshold_description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22271 | 823053385 | `component::battery::conditions::is_level::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22272 | 823053384 | `component::battery::conditions::is_level::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22273 | 823053383 | `component::battery::common::condition_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22274 | 823053382 | `component::battery::common::condition_threshold_description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22275 | 823053381 | `component::air_quality::conditions::is_voc_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22276 | 823053380 | `component::air_quality::conditions::is_voc_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22277 | 823053379 | `component::air_quality::conditions::is_voc_ratio_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22278 | 823053378 | `component::air_quality::conditions::is_voc_ratio_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22279 | 823053377 | `component::air_quality::conditions::is_so2_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22280 | 823053376 | `component::air_quality::conditions::is_so2_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22281 | 823053375 | `component::air_quality::conditions::is_pm4_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22282 | 823053374 | `component::air_quality::conditions::is_pm4_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22283 | 823053373 | `component::air_quality::conditions::is_pm25_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22284 | 823053372 | `component::air_quality::conditions::is_pm25_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22285 | 823053371 | `component::air_quality::conditions::is_pm1_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22286 | 823053370 | `component::air_quality::conditions::is_pm1_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22287 | 823053369 | `component::air_quality::conditions::is_pm10_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22288 | 823053368 | `component::air_quality::conditions::is_pm10_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22289 | 823053367 | `component::air_quality::conditions::is_ozone_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22290 | 823053366 | `component::air_quality::conditions::is_ozone_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22291 | 823053365 | `component::air_quality::conditions::is_no_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22292 | 823053364 | `component::air_quality::conditions::is_no_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22293 | 823053363 | `component::air_quality::conditions::is_no2_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22294 | 823053362 | `component::air_quality::conditions::is_no2_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22295 | 823053361 | `component::air_quality::conditions::is_n2o_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22296 | 823053360 | `component::air_quality::conditions::is_n2o_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22297 | 823053359 | `component::air_quality::conditions::is_co_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22298 | 823053358 | `component::air_quality::conditions::is_co_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22299 | 823053357 | `component::air_quality::conditions::is_co2_value::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22300 | 823053356 | `component::air_quality::conditions::is_co2_value::fields::threshold::description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22301 | 823053355 | `component::air_quality::common::condition_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22302 | 823053354 | `component::air_quality::common::condition_threshold_description` | What to test for and threshold values. | Vad man ska testa för och tröskelvärden. | Source-path follow-up open |
| 22303 | 823049066 | `component::growatt_server::exceptions::invalid_time_format_start_time::message` | 'Start time' must be in HH:MM or HH:MM:SS format. | 'Starttid' måste vara i formatet HH:MM eller HH:MM:SS. | Core-literal match |
| 22304 | 823049065 | `component::growatt_server::exceptions::invalid_time_format_period_start::message` | 'Period {period} start' must be in HH:MM or HH:MM:SS format. | 'Period {period} start' måste vara i formatet HH:MM eller HH:MM:SS. | Core-literal match |
| 22305 | 823049064 | `component::growatt_server::exceptions::invalid_time_format_period_end::message` | 'Period {period} end' must be in HH:MM or HH:MM:SS format. | 'Period {period} slut' måste vara i formatet HH:MM eller HH:MM:SS. | Core-literal match |
| 22306 | 823049063 | `component::growatt_server::exceptions::invalid_time_format_end_time::message` | 'End time' must be in HH:MM or HH:MM:SS format. | 'Sluttid' måste vara i formatet HH:MM eller HH:MM:SS. | Core-literal match |
| 22307 | 823041887 | `component::water_heater::triggers::target_temperature_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22308 | 823041886 | `component::water_heater::triggers::target_temperature_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken passage av tröskelvärdet som ska utlösa automatiseringen och vilka tröskelvärden som ska användas. | Source-path follow-up open |
| 22309 | 823041885 | `component::water_heater::triggers::target_temperature_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22310 | 823041884 | `component::water_heater::triggers::target_temperature_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa automatiseringen och vilka tröskelvärden som ska användas. | Source-path follow-up open |
| 22311 | 823041883 | `component::water_heater::common::trigger_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22312 | 823041882 | `component::water_heater::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. | Vilken passage av tröskelvärdet som ska utlösa automatiseringen och vilka tröskelvärden som ska användas. | Source-path follow-up open |
| 22313 | 823041881 | `component::water_heater::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa automatiseringen och vilka tröskelvärden som ska användas. | Source-path follow-up open |
| 22314 | 823041880 | `component::temperature::triggers::crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22315 | 823041879 | `component::temperature::triggers::crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22316 | 823041878 | `component::temperature::triggers::changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22317 | 823041877 | `component::temperature::triggers::changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22318 | 823041876 | `component::temperature::common::trigger_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22319 | 823041875 | `component::temperature::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22320 | 823041874 | `component::temperature::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 823405925 | `component::battery::triggers::not_low::fields::behavior::description` | The behavior of the targeted batteries to trigger on. |
| 823405924 | `component::battery::triggers::not_low::description` | Triggers after one or more batteries are no longer low. |
| 823405923 | `component::battery::triggers::low::name` | Battery low |
| 823405922 | `component::battery::triggers::low::fields::behavior::name` | Trigger when |
| 823405921 | `component::battery::triggers::low::fields::behavior::description` | The behavior of the targeted batteries to trigger on. |
| 823405920 | `component::battery::triggers::low::description` | Triggers after one or more batteries become low. |
| 823405917 | `component::battery::triggers::level_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823405915 | `component::battery::triggers::level_crossed_threshold::fields::behavior::description` | The behavior of the targeted batteries to trigger on. |
| 823405911 | `component::battery::triggers::level_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823405909 | `component::battery::selector::trigger_behavior::options::last` | Last |
| 823405908 | `component::battery::selector::trigger_behavior::options::first` | First |
| 823405907 | `component::battery::selector::trigger_behavior::options::any` | Any |
| 823405905 | `component::battery::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. |
| 823405904 | `component::battery::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. |
| 823405902 | `component::battery::common::trigger_behavior_description` | The behavior of the targeted batteries to trigger on. |
| 823247156 | `component::humidifier::triggers::mode_changed::fields::behavior::description` | The behavior of the targeted humidifiers to trigger on. |
| 823059392 | `component::water_heater::triggers::operation_mode_changed::fields::behavior::description` | The behavior of the targeted water heaters to trigger on. |
| 823053418 | `component::water_heater::conditions::is_target_temperature::fields::threshold::description` | What to test for and threshold values. |
| 823053416 | `component::water_heater::common::condition_threshold_description` | What to test for and threshold values. |
| 823053414 | `component::temperature::conditions::is_value::fields::threshold::description` | What to test for and threshold values. |
| 823053412 | `component::temperature::common::condition_threshold_description` | What to test for and threshold values. |
| 823053410 | `component::power::conditions::is_value::fields::threshold::description` | What to test for and threshold values. |
| 823053408 | `component::power::common::condition_threshold_description` | What to test for and threshold values. |
| 823053406 | `component::moisture::conditions::is_value::fields::threshold::description` | What to test for and threshold values. |
| 823053404 | `component::moisture::common::condition_threshold_description` | What to test for and threshold values. |
| 823053402 | `component::illuminance::conditions::is_value::fields::threshold::description` | What to test for and threshold values. |
| 823053400 | `component::illuminance::common::condition_threshold_description` | What to test for and threshold values. |
| 823053398 | `component::humidity::conditions::is_value::fields::threshold::description` | What to test for and threshold values. |
| 823053396 | `component::humidity::common::condition_threshold_description` | What to test for and threshold values. |
| 823053394 | `component::humidifier::conditions::is_target_humidity::fields::threshold::description` | What to test for and threshold values. |
| 823053392 | `component::humidifier::common::condition_threshold_description` | What to test for and threshold values. |
| 823053391 | `component::climate::conditions::target_temperature::fields::threshold::name` | Threshold type |
| 823053390 | `component::climate::conditions::target_temperature::fields::threshold::description` | What to test for and threshold values. |
| 823053389 | `component::climate::conditions::target_humidity::fields::threshold::name` | Threshold type |
| 823053388 | `component::climate::conditions::target_humidity::fields::threshold::description` | What to test for and threshold values. |
| 823053386 | `component::climate::common::condition_threshold_description` | What to test for and threshold values. |
| 823053384 | `component::battery::conditions::is_level::fields::threshold::description` | What to test for and threshold values. |
| 823053382 | `component::battery::common::condition_threshold_description` | What to test for and threshold values. |
| 823053380 | `component::air_quality::conditions::is_voc_value::fields::threshold::description` | What to test for and threshold values. |
| 823053378 | `component::air_quality::conditions::is_voc_ratio_value::fields::threshold::description` | What to test for and threshold values. |
| 823053376 | `component::air_quality::conditions::is_so2_value::fields::threshold::description` | What to test for and threshold values. |
| 823053374 | `component::air_quality::conditions::is_pm4_value::fields::threshold::description` | What to test for and threshold values. |
| 823053372 | `component::air_quality::conditions::is_pm25_value::fields::threshold::description` | What to test for and threshold values. |
| 823053370 | `component::air_quality::conditions::is_pm1_value::fields::threshold::description` | What to test for and threshold values. |
| 823053368 | `component::air_quality::conditions::is_pm10_value::fields::threshold::description` | What to test for and threshold values. |
| 823053366 | `component::air_quality::conditions::is_ozone_value::fields::threshold::description` | What to test for and threshold values. |
| 823053364 | `component::air_quality::conditions::is_no_value::fields::threshold::description` | What to test for and threshold values. |
| 823053362 | `component::air_quality::conditions::is_no2_value::fields::threshold::description` | What to test for and threshold values. |
| 823053360 | `component::air_quality::conditions::is_n2o_value::fields::threshold::description` | What to test for and threshold values. |
| 823053358 | `component::air_quality::conditions::is_co_value::fields::threshold::description` | What to test for and threshold values. |
| 823053356 | `component::air_quality::conditions::is_co2_value::fields::threshold::description` | What to test for and threshold values. |
| 823053354 | `component::air_quality::common::condition_threshold_description` | What to test for and threshold values. |
| 823041886 | `component::water_heater::triggers::target_temperature_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041884 | `component::water_heater::triggers::target_temperature_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041882 | `component::water_heater::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. |
| 823041881 | `component::water_heater::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. |
| 823041879 | `component::temperature::triggers::crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041877 | `component::temperature::triggers::changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041875 | `component::temperature::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. |
| 823041874 | `component::temperature::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
