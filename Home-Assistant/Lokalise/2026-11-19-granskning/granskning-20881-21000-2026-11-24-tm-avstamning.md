# Home Assistant Core – historisk avstämning 20881–21000

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 55 direkta källtexter matchar HA Core-källan; 54 referensanvändningar med 24 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 11 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 20881 | 828726647 | `component::victron_gx::entity::sensor::vebus_inverter_mode::state::inverter_only` | Inverter Only | Endast växelriktare | Source-path follow-up open |
| 20882 | 828726646 | `component::victron_gx::entity::sensor::vebus_inverter_mode::state::charger_only` | Charger Only | Endast laddare | Source-path follow-up open |
| 20883 | 828726645 | `component::victron_gx::entity::sensor::vebus_inverter_mode::name` | Mode | Läge | Source-path follow-up open |
| 20884 | 828726644 | `component::victron_gx::entity::sensor::vebus_inverter_input_voltage_phase::name` | Input voltage {phase} | Ingångsspänning {phase} | Core-literal match |
| 20885 | 828726643 | `component::victron_gx::entity::sensor::vebus_inverter_input_power_phase::name` | Input power {phase} | Ingångseffekt {phase} | Core-literal match |
| 20886 | 828726642 | `component::victron_gx::entity::sensor::vebus_inverter_input_frequency_phase::name` | Input frequency {phase} | Ingångsfrekvens {phase} | Core-literal match |
| 20887 | 828726641 | `component::victron_gx::entity::sensor::vebus_inverter_input_current_phase::name` | Input current {phase} | Ingångsström {phase} | Core-literal match |
| 20888 | 828726640 | `component::victron_gx::entity::sensor::vebus_inverter_input_apparent_power_phase::name` | Input apparent power {phase} | Ingångseffekt (skenbar) {phase} | Core-literal match |
| 20889 | 828726639 | `component::victron_gx::entity::sensor::vebus_inverter_ignoreacin1_state::state::on` | On | På | Shared reference target checked |
| 20890 | 828726638 | `component::victron_gx::entity::sensor::vebus_inverter_ignoreacin1_state::state::off` | Off | Av | Shared reference target checked |
| 20891 | 828726637 | `component::victron_gx::entity::sensor::vebus_inverter_ignoreacin1_state::name` | State of ignore AC-in-1 | Tillstånd för ignorera AC-in 1 | Core-literal match |
| 20892 | 828726636 | `component::victron_gx::entity::sensor::vebus_inverter_dc_voltage::name` | DC voltage | DC-spänning | Shared reference target checked |
| 20893 | 828726635 | `component::victron_gx::entity::sensor::vebus_inverter_dc_temperature::name` | DC temperature | DC-temperatur | Shared reference target checked |
| 20894 | 828726634 | `component::victron_gx::entity::sensor::vebus_inverter_dc_power::name` | DC power | DC-effekt | Shared reference target checked |
| 20895 | 828726633 | `component::victron_gx::entity::sensor::vebus_inverter_dc_current::name` | DC current | DC-ström | Shared reference target checked |
| 20896 | 828726632 | `component::victron_gx::entity::sensor::vebus_inverter_current_limit::name` | Current limit | Strömgräns | Shared reference target checked |
| 20897 | 828726631 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_voltage_sensor::state::warning` | Warning | Varning | Shared reference target checked |
| 20898 | 828726630 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_voltage_sensor::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 20899 | 828726629 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_voltage_sensor::state::alarm` | Alarm | Larm | Shared reference target checked |
| 20900 | 828726628 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_voltage_sensor::name` | Voltage sensor alarm | Spänningssensorlarm | Core-literal match |
| 20901 | 828726627 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_temperature_sensor::state::warning` | Warning | Varning | Shared reference target checked |
| 20902 | 828726626 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_temperature_sensor::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 20903 | 828726625 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_temperature_sensor::state::alarm` | Alarm | Larm | Shared reference target checked |
| 20904 | 828726624 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_temperature_sensor::name` | Temperature sensor alarm | Temperatursensorlarm | Core-literal match |
| 20905 | 828726623 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_ripple::state::warning` | Warning | Varning | Shared reference target checked |
| 20906 | 828726622 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_ripple::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 20907 | 828726621 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_ripple::state::alarm` | Alarm | Larm | Shared reference target checked |
| 20908 | 828726620 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_ripple::name` | Ripple alarm | Rippellarm | Shared reference target checked |
| 20909 | 828726619 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_phase_rotation::state::warning` | Warning | Varning | Shared reference target checked |
| 20910 | 828726618 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_phase_rotation::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 20911 | 828726617 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_phase_rotation::state::alarm` | Alarm | Larm | Shared reference target checked |
| 20912 | 828726616 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_phase_rotation::name` | Phase rotation alarm | Fasrotationslarm | Core-literal match |
| 20913 | 828726615 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_overload::state::warning` | Warning | Varning | Shared reference target checked |
| 20914 | 828726614 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_overload::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 20915 | 828726613 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_overload::state::alarm` | Alarm | Larm | Shared reference target checked |
| 20916 | 828726612 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_overload::name` | Overload alarm | Överbelastningslarm | Shared reference target checked |
| 20917 | 828726611 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_low_battery::state::warning` | Warning | Varning | Shared reference target checked |
| 20918 | 828726610 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_low_battery::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 20919 | 828726609 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_low_battery::state::alarm` | Alarm | Larm | Shared reference target checked |
| 20920 | 828726608 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_low_battery::name` | Low battery alarm | Larm för låg batterinivå | Shared reference target checked |
| 20921 | 828726607 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_high_temperature::state::warning` | Warning | Varning | Shared reference target checked |
| 20922 | 828726606 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_high_temperature::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 20923 | 828726605 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_high_temperature::state::alarm` | Alarm | Larm | Shared reference target checked |
| 20924 | 828726604 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_high_temperature::name` | High temperature alarm | Larm för hög temperatur | Shared reference target checked |
| 20925 | 828726603 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_high_dc_voltage::state::warning` | Warning | Varning | Shared reference target checked |
| 20926 | 828726602 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_high_dc_voltage::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 20927 | 828726601 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_high_dc_voltage::state::alarm` | Alarm | Larm | Shared reference target checked |
| 20928 | 828726600 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_high_dc_voltage::name` | High DC voltage alarm | Larm för hög DC-spänning | Core-literal match |
| 20929 | 828726599 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_high_dc_current::state::warning` | Warning | Varning | Shared reference target checked |
| 20930 | 828726598 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_high_dc_current::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 20931 | 828726597 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_high_dc_current::state::alarm` | Alarm | Larm | Shared reference target checked |
| 20932 | 828726596 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_high_dc_current::name` | High DC current alarm | Larm för hög DC-ström | Core-literal match |
| 20933 | 828726595 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_grid_lost::state::warning` | Warning | Varning | Shared reference target checked |
| 20934 | 828726594 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_grid_lost::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 20935 | 828726593 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_grid_lost::state::alarm` | Alarm | Larm | Shared reference target checked |
| 20936 | 828726592 | `component::victron_gx::entity::sensor::vebus_inverter_alarm_grid_lost::name` | Grid lost alarm | Larm om förlorat elnät | Core-literal match |
| 20937 | 828726591 | `component::victron_gx::entity::sensor::vebus_inverter_active_input::state::unknown` | Unknown | Okänd | Shared reference target checked |
| 20938 | 828726590 | `component::victron_gx::entity::sensor::vebus_inverter_active_input::state::shore_power` | Shore power | Landström | Shared reference target checked |
| 20939 | 828726589 | `component::victron_gx::entity::sensor::vebus_inverter_active_input::state::not_connected` | Not connected | Inte ansluten | Shared reference target checked |
| 20940 | 828726588 | `component::victron_gx::entity::sensor::vebus_inverter_active_input::state::grid` | Grid | Elnät | Shared reference target checked |
| 20941 | 828726587 | `component::victron_gx::entity::sensor::vebus_inverter_active_input::state::generator` | Generator | Generator | Shared reference target checked |
| 20942 | 828726586 | `component::victron_gx::entity::sensor::vebus_inverter_active_input::name` | Active AC input | Aktiv AC-ingång | Shared reference target checked |
| 20943 | 828726585 | `component::victron_gx::entity::sensor::vebus_energy_out_to_inverter::name` | Energy from out to inverter | Energi från ut till växelriktare | Core-literal match |
| 20944 | 828726584 | `component::victron_gx::entity::sensor::vebus_energy_inverter_to_ac_out::name` | Energy from inverter to AC-out | Energi från växelriktare till AC-ut | Core-literal match |
| 20945 | 828726583 | `component::victron_gx::entity::sensor::vebus_energy_inverter_to_ac_in2::name` | Energy from inverter to AC-in-2 | Energi från växelriktare till AC-in 2 | Core-literal match |
| 20946 | 828726582 | `component::victron_gx::entity::sensor::vebus_energy_inverter_to_ac_in1::name` | Energy from inverter to AC-in-1 | Energi från växelriktare till AC-in 1 | Core-literal match |
| 20947 | 828726581 | `component::victron_gx::entity::sensor::vebus_energy_ac_out_to_ac_in2::name` | Energy from AC-out to AC-in-2 | Energi från AC-ut till AC-in 2 | Core-literal match |
| 20948 | 828726580 | `component::victron_gx::entity::sensor::vebus_energy_ac_out_to_ac_in1::name` | Energy from AC-out to AC-in-1 | Energi från AC-ut till AC-in 1 | Core-literal match |
| 20949 | 828726579 | `component::victron_gx::entity::sensor::vebus_energy_ac_in2_to_inverter::name` | Energy from AC-in-2 to inverter | Energi från AC-in 2 till växelriktare | Core-literal match |
| 20950 | 828726578 | `component::victron_gx::entity::sensor::vebus_energy_ac_in2_to_ac_out::name` | Energy from AC-in-2 to AC-out | Energi från AC-in 2 till AC-ut | Core-literal match |
| 20951 | 828726577 | `component::victron_gx::entity::sensor::vebus_energy_ac_in1_to_inverter::name` | Energy from AC-in-1 to inverter | Energi från AC-in 1 till växelriktare | Core-literal match |
| 20952 | 828726576 | `component::victron_gx::entity::sensor::vebus_energy_ac_in1_to_ac_out::name` | Energy from AC-in-1 to AC-out | Energi från AC-in 1 till AC-ut | Core-literal match |
| 20953 | 828726575 | `component::victron_gx::entity::sensor::vebus_device_device_number_output_power_phase::name` | {device_number} line {phase} output power | {device_number} linje {phase} utgångseffekt | Core-literal match |
| 20954 | 828726574 | `component::victron_gx::entity::sensor::vebus_device_device_number_output_power_l1::name` | {device_number} line 1 output power | {device_number} linje 1 utgångseffekt | Core-literal match |
| 20955 | 828726573 | `component::victron_gx::entity::sensor::vebus_device_device_number_inverted_power::name` | {device_number} inverted power | {device_number} inverterad effekt | Core-literal match |
| 20956 | 828726572 | `component::victron_gx::entity::sensor::vebus_device_device_number_input_power_phase::name` | {device_number} line {phase} input power | {device_number} linje {phase} ingångseffekt | Core-literal match |
| 20957 | 828726571 | `component::victron_gx::entity::sensor::vebus_device_device_number_input_power_l1::name` | {device_number} line 1 input power | {device_number} linje 1 ingångseffekt | Core-literal match |
| 20958 | 828726570 | `component::victron_gx::entity::sensor::vebus_ac_power_setpoint_phase::name` | AC power setpoint {phase} | AC-effekt börvärde {phase} | Source-path follow-up open |
| 20959 | 828726569 | `component::victron_gx::entity::sensor::transfer_switch_generator_current_limit::name` | Generator AC current limit | Generatorns växelströmsgräns | Source-path follow-up open |
| 20960 | 828726568 | `component::victron_gx::entity::sensor::temperature_type::state::water_heater` | Water heater | Varmvattenberedare | Core-literal match |
| 20961 | 828726567 | `component::victron_gx::entity::sensor::temperature_type::state::room` | Room | Rum | Core-literal match |
| 20962 | 828726566 | `component::victron_gx::entity::sensor::temperature_type::state::outdoor` | Outdoor | Utomhus | Core-literal match |
| 20963 | 828726565 | `component::victron_gx::entity::sensor::temperature_type::state::generic` | Generic | Generisk | Core-literal match |
| 20964 | 828726564 | `component::victron_gx::entity::sensor::temperature_type::state::fridge` | Fridge | Kylskåp | Core-literal match |
| 20965 | 828726563 | `component::victron_gx::entity::sensor::temperature_type::state::freezer` | Freezer | Frys | Core-literal match |
| 20966 | 828726562 | `component::victron_gx::entity::sensor::temperature_type::state::battery` | Battery | Batteri | Core-literal match |
| 20967 | 828726561 | `component::victron_gx::entity::sensor::temperature_type::name` | Sensor type | Sensortyp | Core-literal match |
| 20968 | 828726560 | `component::victron_gx::entity::sensor::temperature_temperature::name` | Temperature | Temperatur | Shared reference target checked |
| 20969 | 828726559 | `component::victron_gx::entity::sensor::temperature_status::state::unknown` | Unknown | Okänd | Shared reference target checked |
| 20970 | 828726558 | `component::victron_gx::entity::sensor::temperature_status::state::short_circuited` | Short circuited | Kortsluten | Core-literal match |
| 20971 | 828726557 | `component::victron_gx::entity::sensor::temperature_status::state::reverse_polarity` | Reverse polarity | Omvänd polaritet | Core-literal match |
| 20972 | 828726556 | `component::victron_gx::entity::sensor::temperature_status::state::ok` | Ok | Ok | Shared reference target checked |
| 20973 | 828726555 | `component::victron_gx::entity::sensor::temperature_status::state::disconnected` | Disconnected | Frånkopplad | Shared reference target checked |
| 20974 | 828726554 | `component::victron_gx::entity::sensor::temperature_status::name` | Sensor status | Sensorstatus | Core-literal match |
| 20975 | 828726553 | `component::victron_gx::entity::sensor::temperature_scale::unit_of_measurement` | factor | faktor | Source-path follow-up open |
| 20976 | 828726552 | `component::victron_gx::entity::sensor::temperature_scale::name` | Scale factor | Skalfaktor | Source-path follow-up open |
| 20977 | 828726551 | `component::victron_gx::entity::sensor::temperature_pressure::unit_of_measurement` | hPa | hPa | Source-path follow-up open |
| 20978 | 828726550 | `component::victron_gx::entity::sensor::temperature_pressure::name` | Pressure | Tryck | Core-literal match |
| 20979 | 828726549 | `component::victron_gx::entity::sensor::temperature_offset::name` | Offset | Offset | Source-path follow-up open |
| 20980 | 828726548 | `component::victron_gx::entity::sensor::temperature_humidity::unit_of_measurement` | % | % | Source-path follow-up open |
| 20981 | 828726547 | `component::victron_gx::entity::sensor::temperature_humidity::name` | Humidity | Luftfuktighet | Core-literal match |
| 20982 | 828726546 | `component::victron_gx::entity::sensor::temperature_battery_voltage::name` | Sensor battery voltage | Sensor batterispänning | Shared reference target checked |
| 20983 | 828726545 | `component::victron_gx::entity::sensor::tank_temperature::name` | Temperature | Temperatur | Shared reference target checked |
| 20984 | 828726544 | `component::victron_gx::entity::sensor::tank_remaining::name` | Remaining | Återstående | Core-literal match |
| 20985 | 828726543 | `component::victron_gx::entity::sensor::tank_level::unit_of_measurement` | % | % | Source-path follow-up open |
| 20986 | 828726542 | `component::victron_gx::entity::sensor::tank_level::name` | Level | Nivå | Core-literal match |
| 20987 | 828726541 | `component::victron_gx::entity::sensor::tank_fluid_type::state::waste_water` | Waste water | Avloppsvatten | Core-literal match |
| 20988 | 828726540 | `component::victron_gx::entity::sensor::tank_fluid_type::state::raw_water` | Raw water | Råvatten | Core-literal match |
| 20989 | 828726539 | `component::victron_gx::entity::sensor::tank_fluid_type::state::oil` | Oil | Olja | Core-literal match |
| 20990 | 828726538 | `component::victron_gx::entity::sensor::tank_fluid_type::state::lpg` | Liquid petroleum gas (LPG) | Flytande petroleumgas (LPG) | Core-literal match |
| 20991 | 828726537 | `component::victron_gx::entity::sensor::tank_fluid_type::state::lng` | Liquid natural gas (LNG) | Flytande naturgas (LNG) | Core-literal match |
| 20992 | 828726536 | `component::victron_gx::entity::sensor::tank_fluid_type::state::live_well` | Live well | Levande brunn | Core-literal match |
| 20993 | 828726535 | `component::victron_gx::entity::sensor::tank_fluid_type::state::hydraulic_oil` | Hydraulic oil | Hydraulolja | Core-literal match |
| 20994 | 828726534 | `component::victron_gx::entity::sensor::tank_fluid_type::state::gasoline` | Gasoline | Bensin | Core-literal match |
| 20995 | 828726533 | `component::victron_gx::entity::sensor::tank_fluid_type::state::fuel` | Fuel | Bränsle | Core-literal match |
| 20996 | 828726532 | `component::victron_gx::entity::sensor::tank_fluid_type::state::fresh_water` | Fresh water | Färskvatten | Core-literal match |
| 20997 | 828726531 | `component::victron_gx::entity::sensor::tank_fluid_type::state::diesel` | Diesel | Diesel | Core-literal match |
| 20998 | 828726530 | `component::victron_gx::entity::sensor::tank_fluid_type::state::black_water` | Black water (sewage) | Svartvatten (avloppsvatten) | Core-literal match |
| 20999 | 828726529 | `component::victron_gx::entity::sensor::tank_fluid_type::name` | Fluid type | Vätsketyp | Core-literal match |
| 21000 | 828726528 | `component::victron_gx::entity::sensor::tank_battery_voltage::name` | Sensor battery voltage | Sensor batterispänning | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 828726647 | `component::victron_gx::entity::sensor::vebus_inverter_mode::state::inverter_only` | Inverter Only |
| 828726646 | `component::victron_gx::entity::sensor::vebus_inverter_mode::state::charger_only` | Charger Only |
| 828726645 | `component::victron_gx::entity::sensor::vebus_inverter_mode::name` | Mode |
| 828726570 | `component::victron_gx::entity::sensor::vebus_ac_power_setpoint_phase::name` | AC power setpoint {phase} |
| 828726569 | `component::victron_gx::entity::sensor::transfer_switch_generator_current_limit::name` | Generator AC current limit |
| 828726553 | `component::victron_gx::entity::sensor::temperature_scale::unit_of_measurement` | factor |
| 828726552 | `component::victron_gx::entity::sensor::temperature_scale::name` | Scale factor |
| 828726551 | `component::victron_gx::entity::sensor::temperature_pressure::unit_of_measurement` | hPa |
| 828726549 | `component::victron_gx::entity::sensor::temperature_offset::name` | Offset |
| 828726548 | `component::victron_gx::entity::sensor::temperature_humidity::unit_of_measurement` | % |
| 828726543 | `component::victron_gx::entity::sensor::tank_level::unit_of_measurement` | % |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
