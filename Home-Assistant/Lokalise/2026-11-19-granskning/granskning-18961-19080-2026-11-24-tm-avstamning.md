# Home Assistant Core – historisk avstämning 18961–19080

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 74 direkta källtexter matchar HA Core-källan; 40 referensanvändningar med 13 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 6 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 18961 | 846005368 | `component::light::conditions::is_brightness::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18962 | 846005367 | `component::illuminance::conditions::is_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18963 | 846005366 | `component::humidity::conditions::is_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18964 | 846005365 | `component::humidity::common::condition_for_name` | For at least | I minst | Core-literal match |
| 18965 | 846005364 | `component::humidifier::conditions::is_target_humidity::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18966 | 846005363 | `component::humidifier::conditions::is_mode::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18967 | 846005362 | `component::humidifier::conditions::is_humidifying::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18968 | 846005361 | `component::humidifier::conditions::is_drying::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18969 | 846005360 | `component::counter::conditions::is_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18970 | 846005359 | `component::counter::common::condition_for_name` | For at least | I minst | Core-literal match |
| 18971 | 846005358 | `component::climate::conditions::target_temperature::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 18972 | 846005357 | `component::climate::conditions::target_humidity::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 18973 | 846005356 | `component::climate::conditions::is_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18974 | 846005355 | `component::climate::conditions::is_hvac_mode::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18975 | 846005354 | `component::climate::conditions::is_heating::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18976 | 846005353 | `component::climate::conditions::is_drying::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18977 | 846005352 | `component::climate::conditions::is_cooling::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18978 | 846005351 | `component::battery::conditions::is_level::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18979 | 846005350 | `component::alarm_control_panel::conditions::is_armed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18980 | 846005349 | `component::air_quality::conditions::is_voc_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18981 | 846005348 | `component::air_quality::conditions::is_voc_ratio_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18982 | 846005347 | `component::air_quality::conditions::is_so2_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18983 | 846005346 | `component::air_quality::conditions::is_pm4_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18984 | 846005345 | `component::air_quality::conditions::is_pm25_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18985 | 846005344 | `component::air_quality::conditions::is_pm1_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18986 | 846005343 | `component::air_quality::conditions::is_pm10_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18987 | 846005342 | `component::air_quality::conditions::is_ozone_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18988 | 846005341 | `component::air_quality::conditions::is_no_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18989 | 846005340 | `component::air_quality::conditions::is_no2_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18990 | 846005339 | `component::air_quality::conditions::is_n2o_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18991 | 846005338 | `component::air_quality::conditions::is_co_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18992 | 846005337 | `component::air_quality::conditions::is_co2_value::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18993 | 845702975 | `component::duco::entity::sensor::time_state_end::name` | State end time | Sluttid för läge | Core-literal match |
| 18994 | 845702974 | `component::duco::entity::sensor::target_flow_level::name` | Target flow level | Målflödesnivå | Core-literal match |
| 18995 | 845702155 | `component::indevolt::entity::sensor::inverter_temperature::name` | Inverter temperature | Inverterens temperatur | Core-literal match |
| 18996 | 845014165 | `component::comelit::exceptions::device_storage_failure::message` | Device SD card read failure. The card may be corrupted or failing; replacement is recommended. | Det gick inte att läsa enhetens SD-kort. SD-kortet kan vara skadat eller defekt; det rekommenderas att det byts ut. | Core-literal match |
| 18997 | 845010087 | `component::fumis::entity::switch::timer::name` | Timer | Timer | Core-literal match |
| 18998 | 845010086 | `component::fumis::entity::switch::eco_mode::name` | Eco mode | Eko-läge | Core-literal match |
| 18999 | 844977310 | `component::broadlink::entity::infrared::infrared_emitter::name` | IR emitter | IR-sändare | Core-literal match |
| 19000 | 844888314 | `component::gardena_bluetooth::entity::sensor::remaining_watering_timestamp::name` | Watering finished | Bevattning klar | Core-literal match |
| 19001 | 844861543 | `component::indevolt::entity::binary_sensor::meter_connected::name` | Meter connected | Mätare ansluten | Core-literal match |
| 19002 | 844861542 | `component::indevolt::entity::binary_sensor::main_electric_heating_state::name` | Main electric heating | Huvudsaklig eluppvärmning | Core-literal match |
| 19003 | 844861541 | `component::indevolt::entity::binary_sensor::electric_heating_state::name` | Electric heating | Eluppvärmning | Core-literal match |
| 19004 | 844861540 | `component::indevolt::entity::binary_sensor::battery_pack_5_electric_heating_state::name` | Battery pack 5 electric heating | Batteripaket 5 elektrisk uppvärmning | Core-literal match |
| 19005 | 844861539 | `component::indevolt::entity::binary_sensor::battery_pack_4_electric_heating_state::name` | Battery pack 4 electric heating | Batteripaket 4 elektrisk uppvärmning | Core-literal match |
| 19006 | 844861538 | `component::indevolt::entity::binary_sensor::battery_pack_3_electric_heating_state::name` | Battery pack 3 electric heating | Batteripaket 3 elektrisk uppvärmning | Core-literal match |
| 19007 | 844861537 | `component::indevolt::entity::binary_sensor::battery_pack_2_electric_heating_state::name` | Battery pack 2 electric heating | Batteripaket 2 elektrisk uppvärmning | Core-literal match |
| 19008 | 844861536 | `component::indevolt::entity::binary_sensor::battery_pack_1_electric_heating_state::name` | Battery pack 1 electric heating | Batteripaket 1 elektrisk uppvärmning | Core-literal match |
| 19009 | 844814899 | `component::mobile_app::exceptions::timeout_sending_notification::message` | Timeout sending notification to {device_name} | Tidsgräns vid sändning av meddelande till {device_name} | Core-literal match |
| 19010 | 844814898 | `component::mobile_app::exceptions::rate_limit_exceeded_sending_notification::message` | Rate limit exceeded sending notification to {device_name} | Gränsen för antal förfrågningar har överskridits – meddelande skickas till {device_name} | Core-literal match |
| 19011 | 844814897 | `component::mobile_app::exceptions::error_sending_notification::message` | Error sending notification to {device_name} | Fel vid sändning av meddelande till {device_name} | Core-literal match |
| 19012 | 844814896 | `component::mobile_app::exceptions::device_not_connected_for_local_push_notifications::message` | Device {device_name} is not connected for local push notifications | Enhets- {device_name} en är inte ansluten för lokala push-meddelanden | Core-literal match |
| 19013 | 844764931 | `component::timer::triggers::started::name` | Timer started | Timern har startats | Core-literal match |
| 19014 | 844764930 | `component::timer::triggers::started::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19015 | 844764929 | `component::timer::triggers::started::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 19016 | 844764928 | `component::timer::triggers::started::description` | Triggers when one or more timers are started. | Utlöses när en eller flera timers startas. | Core-literal match |
| 19017 | 844764927 | `component::timer::triggers::restarted::name` | Timer restarted | Timern har startats om | Core-literal match |
| 19018 | 844764926 | `component::timer::triggers::restarted::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19019 | 844764925 | `component::timer::triggers::restarted::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 19020 | 844764924 | `component::timer::triggers::restarted::description` | Triggers when one or more timers are restarted. | Utlöses när en eller flera timers startas om. | Core-literal match |
| 19021 | 844764923 | `component::timer::triggers::paused::name` | Timer paused | Timern pausad | Core-literal match |
| 19022 | 844764922 | `component::timer::triggers::paused::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19023 | 844764921 | `component::timer::triggers::paused::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 19024 | 844764920 | `component::timer::triggers::paused::description` | Triggers when one or more timers are paused. | Utlöses när en eller flera timers är pausade. | Core-literal match |
| 19025 | 844764919 | `component::timer::triggers::finished::name` | Timer finished | Timern är klar | Core-literal match |
| 19026 | 844764918 | `component::timer::triggers::finished::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19027 | 844764917 | `component::timer::triggers::finished::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 19028 | 844764916 | `component::timer::triggers::finished::description` | Triggers when one or more timers finish. | Utlöses när en eller flera timers är klara. | Core-literal match |
| 19029 | 844764915 | `component::timer::triggers::cancelled::name` | Timer cancelled | Timern har avbrutits | Core-literal match |
| 19030 | 844764914 | `component::timer::triggers::cancelled::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19031 | 844764913 | `component::timer::triggers::cancelled::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 19032 | 844764912 | `component::timer::triggers::cancelled::description` | Triggers when one or more timers are cancelled. | Utlöses när en eller flera timers avbryts. | Core-literal match |
| 19033 | 844764911 | `component::timer::selector::trigger_behavior::options::last` | Last | Sista | Source-path follow-up open |
| 19034 | 844764910 | `component::timer::selector::trigger_behavior::options::first` | First | Första | Source-path follow-up open |
| 19035 | 844764909 | `component::timer::selector::trigger_behavior::options::any` | Any | Något | Source-path follow-up open |
| 19036 | 844764908 | `component::timer::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 19037 | 844764907 | `component::timer::common::trigger_behavior_name` | Trigger when | Utlös när | Core-literal match |
| 19038 | 844566225 | `component::omie::entity::sensor::pt_spot_price::name` | Portugal spot price | Portugals spotpris | Core-literal match |
| 19039 | 844566224 | `component::omie::entity::sensor::es_spot_price::name` | Spain spot price | Spaniens spotpris | Core-literal match |
| 19040 | 844566223 | `component::omie::config::step::user::description` | Do you want to start setup? | Vill du starta installationen? | Shared reference target checked |
| 19041 | 844566222 | `component::omie::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 19042 | 844566221 | `component::omie::config::abort::single_instance_allowed` | Already configured. Only a single configuration is possible. | Redan konfigurerad. Endast en konfiguration kan göras. | Source-path follow-up open |
| 19043 | 844443872 | `component::timer::entity_component::_::state_attributes::last_transition::state::started` | Started | Startad | Core-literal match |
| 19044 | 844443871 | `component::timer::entity_component::_::state_attributes::last_transition::state::restarted` | Restarted | Omstartad | Core-literal match |
| 19045 | 844443870 | `component::timer::entity_component::_::state_attributes::last_transition::state::paused` | Paused | Pausad | Core-literal match |
| 19046 | 844443869 | `component::timer::entity_component::_::state_attributes::last_transition::state::finished` | Finished | Färdig | Core-literal match |
| 19047 | 844443868 | `component::timer::entity_component::_::state_attributes::last_transition::state::cancelled` | Cancelled | Avbruten | Core-literal match |
| 19048 | 844443867 | `component::timer::entity_component::_::state_attributes::last_transition::name` | Last transition | Senaste övergången | Core-literal match |
| 19049 | 844252165 | `component::fumis::entity::sensor::error::state::tc1_alarm` | TC1 alarm | TC1-larm | Core-literal match |
| 19050 | 844252164 | `component::fumis::entity::sensor::error::state::sensor_t04` | Sensor T04 malfunction | Fel på sensor T04 | Core-literal match |
| 19051 | 844252163 | `component::fumis::entity::sensor::error::state::sensor_t03_t05` | Sensor T03/T05 malfunction | Fel på sensor T03/T05 | Core-literal match |
| 19052 | 844252162 | `component::fumis::entity::sensor::error::state::sensor_t02` | Sensor T02 malfunction | Fel på sensor T02 | Core-literal match |
| 19053 | 844252161 | `component::fumis::entity::sensor::error::state::sensor_t01_t03` | Sensor T01/T03 malfunction | Fel på sensor T01/T03 | Core-literal match |
| 19054 | 844252160 | `component::fumis::entity::sensor::error::state::sensor_t01_t02` | Sensor T01/T02 malfunction | Fel på sensor T01/T02 | Core-literal match |
| 19055 | 844252159 | `component::fumis::entity::sensor::error::state::safety_switch` | Safety switch tripped | Säkerhetsbrytaren har löst ut | Core-literal match |
| 19056 | 844252158 | `component::fumis::entity::sensor::error::state::pressure_sensor_off` | Pressure sensor off | Trycksensor avstängd | Core-literal match |
| 19057 | 844252157 | `component::fumis::entity::sensor::error::state::pressure_alarm` | Pressure alarm | Trycklarm | Core-literal match |
| 19058 | 844252156 | `component::fumis::entity::sensor::error::state::ntc3_alarm` | NTC3 alarm | NTC3-larm | Core-literal match |
| 19059 | 844252155 | `component::fumis::entity::sensor::error::state::ntc2_alarm` | NTC2 alarm | NTC2-larm | Core-literal match |
| 19060 | 844252154 | `component::fumis::entity::sensor::error::state::ntc1_alarm` | NTC1 alarm | NTC1-larm | Core-literal match |
| 19061 | 844252153 | `component::fumis::entity::sensor::error::state::none` | No error | Inget fel | Core-literal match |
| 19062 | 844252152 | `component::fumis::entity::sensor::error::state::no_pellet_alarm` | No pellet alarm | Inget pelletslarm | Core-literal match |
| 19063 | 844252151 | `component::fumis::entity::sensor::error::state::mfdoor_alarm` | MFDoor alarm | MFDoor-larm | Core-literal match |
| 19064 | 844252150 | `component::fumis::entity::sensor::error::state::ignition_failed` | Ignition failed | Tändningen misslyckades | Core-literal match |
| 19065 | 844252149 | `component::fumis::entity::sensor::error::state::grate_error` | Grate error | Gallerfel | Core-literal match |
| 19066 | 844252148 | `component::fumis::entity::sensor::error::state::general_error` | General error | Allmänt fel | Core-literal match |
| 19067 | 844252147 | `component::fumis::entity::sensor::error::state::gas_alarm` | Gas alarm | Gaslarm | Core-literal match |
| 19068 | 844252146 | `component::fumis::entity::sensor::error::state::fuel_ignition_timeout` | Fuel ignition timeout | Tidsgräns för bränsletändning | Core-literal match |
| 19069 | 844252145 | `component::fumis::entity::sensor::error::state::flue_gas_overtemp` | Flue gas overtemperature | Övertemperatur i rökgasen | Core-literal match |
| 19070 | 844252144 | `component::fumis::entity::sensor::error::state::fire_error` | Fire error | Eldfel | Core-literal match |
| 19071 | 844252143 | `component::fumis::entity::sensor::error::state::door_alarm` | Door alarm | Dörrlarm | Core-literal match |
| 19072 | 844252142 | `component::fumis::entity::sensor::error::state::chimney_dirty` | Chimney or burning pot dirty | Skorsten eller brännpanna smutsig | Core-literal match |
| 19073 | 844252141 | `component::fumis::entity::sensor::error::state::chimney_alarm` | Chimney alarm | Skorstenslarm | Core-literal match |
| 19074 | 844252140 | `component::fumis::entity::sensor::error::name` | Error | Fel | Core-literal match |
| 19075 | 844252139 | `component::fumis::entity::sensor::alert::state::speed_sensor_failure` | Speed sensor failure | Fel på hastighetssensorn | Core-literal match |
| 19076 | 844252138 | `component::fumis::entity::sensor::alert::state::service_due` | Service due | Service förfaller | Core-literal match |
| 19077 | 844252137 | `component::fumis::entity::sensor::alert::state::none` | No alert | Ingen varning | Core-literal match |
| 19078 | 844252136 | `component::fumis::entity::sensor::alert::state::low_fuel` | Low fuel level | Låg bränslenivå | Core-literal match |
| 19079 | 844252135 | `component::fumis::entity::sensor::alert::state::low_battery` | Low battery | Lågt batteri | Core-literal match |
| 19080 | 844252134 | `component::fumis::entity::sensor::alert::state::flue_gas_warning` | Flue gas temperature warning | Varning för rökgastemperatur | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 846005358 | `component::climate::conditions::target_temperature::fields::for::name` | For at least |
| 846005357 | `component::climate::conditions::target_humidity::fields::for::name` | For at least |
| 844764911 | `component::timer::selector::trigger_behavior::options::last` | Last |
| 844764910 | `component::timer::selector::trigger_behavior::options::first` | First |
| 844764909 | `component::timer::selector::trigger_behavior::options::any` | Any |
| 844566221 | `component::omie::config::abort::single_instance_allowed` | Already configured. Only a single configuration is possible. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
