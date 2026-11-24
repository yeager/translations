# Home Assistant Core – historisk avstämning 12241–12360

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 83 direkta källtexter matchar HA Core-källan; 0 referensanvändningar med 0 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 37 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 12241 | 920808843 | `component::sofar::entity::sensor::system_state::state::recoverable_fault` | Recoverable fault | Återställbart fel | Core-literal match |
| 12242 | 920808842 | `component::sofar::entity::sensor::system_state::state::permanent_fault` | Permanent fault | Permanent fel | Core-literal match |
| 12243 | 920808841 | `component::sofar::entity::sensor::system_state::state::grid_connected` | Grid connected | Ansluten till elnätet | Core-literal match |
| 12244 | 920808840 | `component::sofar::entity::sensor::system_state::state::emergency_power_supply` | Emergency power supply | Nödströmförsörjning | Core-literal match |
| 12245 | 920808839 | `component::sofar::entity::sensor::system_state::state::checking` | Checking | Kontrollerar | Core-literal match |
| 12246 | 920808838 | `component::sofar::entity::sensor::system_state::name` | System state | Systemtillstånd | Core-literal match |
| 12247 | 920808837 | `component::sofar::entity::sensor::sync_rtc_result::state::successful` | Successful | Lyckades | Core-literal match |
| 12248 | 920808836 | `component::sofar::entity::sensor::sync_rtc_result::state::operation_in_progress` | Operation in progress | Åtgärd pågår | Core-literal match |
| 12249 | 920808835 | `component::sofar::entity::sensor::sync_rtc_result::state::operation_failed_parameter_access_failed` | Operation failed: parameter access failed | Åtgärden misslyckades: parameteråtkomst misslyckades | Core-literal match |
| 12250 | 920808834 | `component::sofar::entity::sensor::sync_rtc_result::state::operation_failed_no_response_from_the_controller` | Operation failed: no response from the controller | Åtgärden misslyckades: inget svar från styrenheten | Core-literal match |
| 12251 | 920808833 | `component::sofar::entity::sensor::sync_rtc_result::state::operation_failed_input_parameters_incorrect` | Operation failed: input parameters incorrect | Åtgärden misslyckades: inmatningsparametrar felaktiga | Core-literal match |
| 12252 | 920808832 | `component::sofar::entity::sensor::sync_rtc_result::state::operation_failed_current_function_disabled` | Operation failed: current function disabled | Åtgärden misslyckades: aktuell funktion inaktiverad | Core-literal match |
| 12253 | 920808831 | `component::sofar::entity::sensor::sync_rtc_result::state::operation_failed_controller_refused_to_respond` | Operation failed: controller refused to respond | Åtgärden misslyckades: styrenheten vägrade svara | Core-literal match |
| 12254 | 920808830 | `component::sofar::entity::sensor::sync_rtc_result::state::enabled_discharging` | Enabled discharging | Aktiverad urladdning | Core-literal match |
| 12255 | 920808829 | `component::sofar::entity::sensor::sync_rtc_result::state::disabled` | Disabled | Inaktiverad | Core-literal match |
| 12256 | 920808828 | `component::sofar::entity::sensor::sync_rtc_result::name` | Update system time operation result | Resultat för uppdatering av systemtid | Core-literal match |
| 12257 | 920808827 | `component::sofar::entity::sensor::solar_generation_today::name` | Solar generation today | Solenergiproduktion i dag | Core-literal match |
| 12258 | 920808826 | `component::sofar::entity::sensor::software_version::name` | Software version | Programvaruversion | Source-path follow-up open |
| 12259 | 920808825 | `component::sofar::entity::sensor::serial_number::name` | Serial number | Serienummer | Source-path follow-up open |
| 12260 | 920808824 | `component::sofar::entity::sensor::rtc::name` | System time | Systemtid | Source-path follow-up open |
| 12261 | 920808823 | `component::sofar::entity::sensor::reactive_power_pcc_total::name` | Reactive power PCC total | Reaktiv effekt PCC totalt | Core-literal match |
| 12262 | 920808822 | `component::sofar::entity::sensor::reactive_power_pcc_l3::name` | Reactive power PCC L3 | Reaktiv effekt PCC L3 | Core-literal match |
| 12263 | 920808821 | `component::sofar::entity::sensor::reactive_power_pcc_l2::name` | Reactive power PCC L2 | Reaktiv effekt PCC L2 | Core-literal match |
| 12264 | 920808820 | `component::sofar::entity::sensor::reactive_power_pcc_l1::name` | Reactive power PCC L1 | Reaktiv effekt PCC L1 | Core-literal match |
| 12265 | 920808819 | `component::sofar::entity::sensor::reactive_power_output_total::name` | Reactive power output total | Total reaktiv uteffekt | Core-literal match |
| 12266 | 920808818 | `component::sofar::entity::sensor::reactive_power_output_l3::name` | Reactive power output L3 | Reaktiv uteffekt L3 | Core-literal match |
| 12267 | 920808817 | `component::sofar::entity::sensor::reactive_power_output_l2::name` | Reactive power output L2 | Reaktiv uteffekt L2 | Core-literal match |
| 12268 | 920808816 | `component::sofar::entity::sensor::reactive_power_output_l1::name` | Reactive power output L1 | Reaktiv uteffekt L1 | Core-literal match |
| 12269 | 920808815 | `component::sofar::entity::sensor::reactive_power_offgrid_total::name` | Reactive power off-grid total | Total reaktiv effekt vid ödrift | Core-literal match |
| 12270 | 920808814 | `component::sofar::entity::sensor::pv_voltage_9::name` | PV voltage 9 | PV-spänning 9 | Source-path follow-up open |
| 12271 | 920808813 | `component::sofar::entity::sensor::pv_voltage_8::name` | PV voltage 8 | PV-spänning 8 | Source-path follow-up open |
| 12272 | 920808812 | `component::sofar::entity::sensor::pv_voltage_7::name` | PV voltage 7 | PV-spänning 7 | Source-path follow-up open |
| 12273 | 920808811 | `component::sofar::entity::sensor::pv_voltage_6::name` | PV voltage 6 | PV-spänning 6 | Source-path follow-up open |
| 12274 | 920808810 | `component::sofar::entity::sensor::pv_voltage_5::name` | PV voltage 5 | PV-spänning 5 | Source-path follow-up open |
| 12275 | 920808809 | `component::sofar::entity::sensor::pv_voltage_4::name` | PV voltage 4 | PV-spänning 4 | Source-path follow-up open |
| 12276 | 920808808 | `component::sofar::entity::sensor::pv_voltage_3::name` | PV voltage 3 | PV-spänning 3 | Source-path follow-up open |
| 12277 | 920808807 | `component::sofar::entity::sensor::pv_voltage_2::name` | PV voltage 2 | PV-spänning 2 | Source-path follow-up open |
| 12278 | 920808806 | `component::sofar::entity::sensor::pv_voltage_10::name` | PV voltage 10 | PV-spänning 10 | Source-path follow-up open |
| 12279 | 920808805 | `component::sofar::entity::sensor::pv_voltage_1::name` | PV voltage 1 | PV-spänning 1 | Source-path follow-up open |
| 12280 | 920808804 | `component::sofar::entity::sensor::pv_power_9::name` | PV power 9 | PV-effekt 9 | Source-path follow-up open |
| 12281 | 920808803 | `component::sofar::entity::sensor::pv_power_8::name` | PV power 8 | PV-effekt 8 | Source-path follow-up open |
| 12282 | 920808802 | `component::sofar::entity::sensor::pv_power_7::name` | PV power 7 | PV-effekt 7 | Source-path follow-up open |
| 12283 | 920808801 | `component::sofar::entity::sensor::pv_power_6::name` | PV power 6 | PV-effekt 6 | Source-path follow-up open |
| 12284 | 920808800 | `component::sofar::entity::sensor::pv_power_5::name` | PV power 5 | PV-effekt 5 | Source-path follow-up open |
| 12285 | 920808799 | `component::sofar::entity::sensor::pv_power_4::name` | PV power 4 | PV-effekt 4 | Source-path follow-up open |
| 12286 | 920808798 | `component::sofar::entity::sensor::pv_power_3::name` | PV power 3 | PV-effekt 3 | Source-path follow-up open |
| 12287 | 920808797 | `component::sofar::entity::sensor::pv_power_10::name` | PV power 10 | PV-effekt 10 | Source-path follow-up open |
| 12288 | 920808796 | `component::sofar::entity::sensor::pv_current_9::name` | PV current 9 | PV-ström 9 | Source-path follow-up open |
| 12289 | 920808795 | `component::sofar::entity::sensor::pv_current_8::name` | PV current 8 | PV-ström 8 | Source-path follow-up open |
| 12290 | 920808794 | `component::sofar::entity::sensor::pv_current_7::name` | PV current 7 | PV-ström 7 | Source-path follow-up open |
| 12291 | 920808793 | `component::sofar::entity::sensor::pv_current_6::name` | PV current 6 | PV-ström 6 | Source-path follow-up open |
| 12292 | 920808792 | `component::sofar::entity::sensor::pv_current_5::name` | PV current 5 | PV-ström 5 | Source-path follow-up open |
| 12293 | 920808791 | `component::sofar::entity::sensor::pv_current_4::name` | PV current 4 | PV-ström 4 | Source-path follow-up open |
| 12294 | 920808790 | `component::sofar::entity::sensor::pv_current_3::name` | PV current 3 | PV-ström 3 | Source-path follow-up open |
| 12295 | 920808789 | `component::sofar::entity::sensor::pv_current_2::name` | PV current 2 | PV-ström 2 | Source-path follow-up open |
| 12296 | 920808788 | `component::sofar::entity::sensor::pv_current_10::name` | PV current 10 | PV-ström 10 | Source-path follow-up open |
| 12297 | 920808787 | `component::sofar::entity::sensor::pv_current_1::name` | PV current 1 | PV-ström 1 | Source-path follow-up open |
| 12298 | 920808786 | `component::sofar::entity::sensor::power_factor_pcc_l3::name` | Power factor PCC L3 | Effektfaktor PCC L3 | Core-literal match |
| 12299 | 920808785 | `component::sofar::entity::sensor::power_factor_pcc_l2::name` | Power factor PCC L2 | Effektfaktor PCC L2 | Core-literal match |
| 12300 | 920808784 | `component::sofar::entity::sensor::power_factor_pcc_l1::name` | Power factor PCC L1 | Effektfaktor PCC L1 | Core-literal match |
| 12301 | 920808783 | `component::sofar::entity::sensor::power_factor_output_l3::name` | Power factor output L3 | Effektfaktor för utgång L3 | Core-literal match |
| 12302 | 920808782 | `component::sofar::entity::sensor::power_factor_output_l2::name` | Power factor output L2 | Effektfaktor för utgång L2 | Core-literal match |
| 12303 | 920808781 | `component::sofar::entity::sensor::power_factor_output_l1::name` | Power factor output L1 | Effektfaktor för utgång L1 | Core-literal match |
| 12304 | 920808780 | `component::sofar::entity::sensor::passive_eps_wait_time::name` | EPS wait time | EPS-väntetid | Core-literal match |
| 12305 | 920808779 | `component::sofar::entity::sensor::offgrid_voltage_output_l2n::name` | Off-grid voltage output L2N | Utspänning L2N vid ödrift | Core-literal match |
| 12306 | 920808778 | `component::sofar::entity::sensor::offgrid_voltage_output_l1n::name` | Off-grid voltage output L1N | Utspänning L1N vid ödrift | Core-literal match |
| 12307 | 920808777 | `component::sofar::entity::sensor::offgrid_voltage_l3::name` | Off-grid voltage L3 | Spänning vid ödrift L3 | Core-literal match |
| 12308 | 920808776 | `component::sofar::entity::sensor::offgrid_voltage_l2::name` | Off-grid voltage L2 | Spänning vid ödrift L2 | Core-literal match |
| 12309 | 920808775 | `component::sofar::entity::sensor::offgrid_voltage_l1::name` | Off-grid voltage L1 | Spänning vid ödrift L1 | Core-literal match |
| 12310 | 920808774 | `component::sofar::entity::sensor::offgrid_voltage::name` | Off-grid voltage | Spänning vid ödrift | Core-literal match |
| 12311 | 920808773 | `component::sofar::entity::sensor::offgrid_reactive_power_output_l3::name` | Off-grid reactive power output L3 | Reaktiv effekt på utgång L3 vid ödrift | Core-literal match |
| 12312 | 920808772 | `component::sofar::entity::sensor::offgrid_reactive_power_output_l2::name` | Off-grid reactive power output L2 | Reaktiv effekt på utgång L2 vid ödrift | Core-literal match |
| 12313 | 920808771 | `component::sofar::entity::sensor::offgrid_reactive_power_output_l1::name` | Off-grid reactive power output L1 | Reaktiv effekt på utgång L1 vid ödrift | Core-literal match |
| 12314 | 920808770 | `component::sofar::entity::sensor::offgrid_reactive_power_output::name` | Off-grid reactive power output | Reaktiv effekt på utgången vid ödrift | Core-literal match |
| 12315 | 920808769 | `component::sofar::entity::sensor::offgrid_loadpeakratio_l3::name` | Off-grid load peak ratio L3 | Off-grid topplast kvot L3 | Source-path follow-up open |
| 12316 | 920808768 | `component::sofar::entity::sensor::offgrid_loadpeakratio_l2::name` | Off-grid load peak ratio L2 | Off-grid topplast kvot L2 | Source-path follow-up open |
| 12317 | 920808767 | `component::sofar::entity::sensor::offgrid_loadpeakratio_l1::name` | Off-grid load peak ratio L1 | Off-grid topplast kvot L1 | Source-path follow-up open |
| 12318 | 920808766 | `component::sofar::entity::sensor::offgrid_loadpeakratio::name` | Off-grid load peak ratio | Off-grid topplast kvot | Source-path follow-up open |
| 12319 | 920808765 | `component::sofar::entity::sensor::offgrid_frequency::name` | Off-grid frequency | Frekvens vid ödrift | Core-literal match |
| 12320 | 920808764 | `component::sofar::entity::sensor::offgrid_current_output_l3::name` | Off-grid current output L3 | Utström L3 vid ödrift | Core-literal match |
| 12321 | 920808763 | `component::sofar::entity::sensor::offgrid_current_output_l2n::name` | Off-grid current output L2N | Utström L2N vid ödrift | Core-literal match |
| 12322 | 920808762 | `component::sofar::entity::sensor::offgrid_current_output_l2::name` | Off-grid current output L2 | Utström L2 vid ödrift | Core-literal match |
| 12323 | 920808761 | `component::sofar::entity::sensor::offgrid_current_output_l1n::name` | Off-grid current output L1N | Utström L1N vid ödrift | Core-literal match |
| 12324 | 920808760 | `component::sofar::entity::sensor::offgrid_current_output_l1::name` | Off-grid current output L1 | Utström L1 vid ödrift | Core-literal match |
| 12325 | 920808759 | `component::sofar::entity::sensor::offgrid_current_output::name` | Off-grid current output | Ström på utgången vid ödrift | Core-literal match |
| 12326 | 920808758 | `component::sofar::entity::sensor::offgrid_apparent_power_output_l3::name` | Off-grid apparent power output L3 | Skenbar effekt på utgång L3 vid ödrift | Core-literal match |
| 12327 | 920808757 | `component::sofar::entity::sensor::offgrid_apparent_power_output_l2::name` | Off-grid apparent power output L2 | Skenbar effekt på utgång L2 vid ödrift | Core-literal match |
| 12328 | 920808756 | `component::sofar::entity::sensor::offgrid_apparent_power_output_l1::name` | Off-grid apparent power output L1 | Skenbar effekt på utgång L1 vid ödrift | Core-literal match |
| 12329 | 920808755 | `component::sofar::entity::sensor::offgrid_apparent_power_output::name` | Off-grid apparent power output | Skenbar effekt på utgången vid ödrift | Core-literal match |
| 12330 | 920808754 | `component::sofar::entity::sensor::offgrid_active_power_output_l3::name` | Off-grid active power output L3 | Aktiv effekt på utgång L3 vid ödrift | Core-literal match |
| 12331 | 920808753 | `component::sofar::entity::sensor::offgrid_active_power_output_l2n::name` | Off-grid active power output L2N | Aktiv effekt på utgång L2N vid ödrift | Core-literal match |
| 12332 | 920808752 | `component::sofar::entity::sensor::offgrid_active_power_output_l2::name` | Off-grid active power output L2 | Aktiv effekt på utgång L2 vid ödrift | Core-literal match |
| 12333 | 920808751 | `component::sofar::entity::sensor::offgrid_active_power_output_l1n::name` | Off-grid active power output L1N | Aktiv effekt på utgång L1N vid ödrift | Core-literal match |
| 12334 | 920808750 | `component::sofar::entity::sensor::offgrid_active_power_output_l1::name` | Off-grid active power output L1 | Aktiv effekt på utgång L1 vid ödrift | Core-literal match |
| 12335 | 920808749 | `component::sofar::entity::sensor::offgrid_active_power_output::name` | Off-grid active power output | Aktiv effekt på utgången vid ödrift | Core-literal match |
| 12336 | 920808748 | `component::sofar::entity::sensor::module_temperature_2::name` | Module temperature 2 | Modultemperatur 2 | Core-literal match |
| 12337 | 920808747 | `component::sofar::entity::sensor::module_temperature_1::name` | Module temperature 1 | Modultemperatur 1 | Core-literal match |
| 12338 | 920808746 | `component::sofar::entity::sensor::load_consumption_total::name` | Load consumption total | Lastförbrukning totalt | Core-literal match |
| 12339 | 920808745 | `component::sofar::entity::sensor::load_consumption_today::name` | Load consumption today | Lastförbrukning i dag | Core-literal match |
| 12340 | 920808744 | `component::sofar::entity::sensor::inverter_temperature_2::name` | Inverter temperature 2 | Växelriktartemperatur 2 | Core-literal match |
| 12341 | 920808743 | `component::sofar::entity::sensor::inverter_temperature_1::name` | Inverter temperature 1 | Växelriktartemperatur 1 | Core-literal match |
| 12342 | 920808742 | `component::sofar::entity::sensor::import_energy_total::name` | Import energy total | Importerad energi totalt | Core-literal match |
| 12343 | 920808741 | `component::sofar::entity::sensor::import_energy_today::name` | Import energy today | Importerad energi i dag | Core-literal match |
| 12344 | 920808740 | `component::sofar::entity::sensor::heatsink_temperature_2::name` | Heatsink temperature 2 | Kylflänstemperatur 2 | Core-literal match |
| 12345 | 920808739 | `component::sofar::entity::sensor::heatsink_temperature_1::name` | Heatsink temperature 1 | Kylflänstemperatur 1 | Core-literal match |
| 12346 | 920808738 | `component::sofar::entity::sensor::hardware_version::name` | Hardware version | Hårdvaruversion | Source-path follow-up open |
| 12347 | 920808737 | `component::sofar::entity::sensor::grid_frequency::name` | Grid frequency | Nätfrekvens | Core-literal match |
| 12348 | 920808736 | `component::sofar::entity::sensor::export_energy_total::name` | Export energy total | Exporterad energi totalt | Core-literal match |
| 12349 | 920808735 | `component::sofar::entity::sensor::export_energy_today::name` | Export energy today | Exporterad energi i dag | Core-literal match |
| 12350 | 920808734 | `component::sofar::entity::sensor::current_pcc_l3::name` | Current PCC L3 | Ström PCC L3 | Core-literal match |
| 12351 | 920808733 | `component::sofar::entity::sensor::current_pcc_l2n::name` | Current PCC L2N | Ström PCC L2N | Core-literal match |
| 12352 | 920808732 | `component::sofar::entity::sensor::current_pcc_l2::name` | Current PCC L2 | Ström PCC L2 | Core-literal match |
| 12353 | 920808731 | `component::sofar::entity::sensor::current_pcc_l1n::name` | Current PCC L1N | Ström PCC L1N | Core-literal match |
| 12354 | 920808730 | `component::sofar::entity::sensor::current_pcc_l1::name` | Current PCC L1 | Ström PCC L1 | Core-literal match |
| 12355 | 920808729 | `component::sofar::entity::sensor::current_output_l3::name` | Current output L3 | Utström L3 | Core-literal match |
| 12356 | 920808728 | `component::sofar::entity::sensor::current_output_l2n::name` | Current output L2N | Utström L2N | Core-literal match |
| 12357 | 920808727 | `component::sofar::entity::sensor::current_output_l2::name` | Current output L2 | Utström L2 | Core-literal match |
| 12358 | 920808726 | `component::sofar::entity::sensor::current_output_l1n::name` | Current output L1N | Utström L1N | Core-literal match |
| 12359 | 920808725 | `component::sofar::entity::sensor::current_output_l1::name` | Current output L1 | Utström L1 | Core-literal match |
| 12360 | 920808724 | `component::sofar::entity::sensor::battery_voltage_8::name` | Battery voltage 8 | Batterispänning 8 | Source-path follow-up open |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 920808826 | `component::sofar::entity::sensor::software_version::name` | Software version |
| 920808825 | `component::sofar::entity::sensor::serial_number::name` | Serial number |
| 920808824 | `component::sofar::entity::sensor::rtc::name` | System time |
| 920808814 | `component::sofar::entity::sensor::pv_voltage_9::name` | PV voltage 9 |
| 920808813 | `component::sofar::entity::sensor::pv_voltage_8::name` | PV voltage 8 |
| 920808812 | `component::sofar::entity::sensor::pv_voltage_7::name` | PV voltage 7 |
| 920808811 | `component::sofar::entity::sensor::pv_voltage_6::name` | PV voltage 6 |
| 920808810 | `component::sofar::entity::sensor::pv_voltage_5::name` | PV voltage 5 |
| 920808809 | `component::sofar::entity::sensor::pv_voltage_4::name` | PV voltage 4 |
| 920808808 | `component::sofar::entity::sensor::pv_voltage_3::name` | PV voltage 3 |
| 920808807 | `component::sofar::entity::sensor::pv_voltage_2::name` | PV voltage 2 |
| 920808806 | `component::sofar::entity::sensor::pv_voltage_10::name` | PV voltage 10 |
| 920808805 | `component::sofar::entity::sensor::pv_voltage_1::name` | PV voltage 1 |
| 920808804 | `component::sofar::entity::sensor::pv_power_9::name` | PV power 9 |
| 920808803 | `component::sofar::entity::sensor::pv_power_8::name` | PV power 8 |
| 920808802 | `component::sofar::entity::sensor::pv_power_7::name` | PV power 7 |
| 920808801 | `component::sofar::entity::sensor::pv_power_6::name` | PV power 6 |
| 920808800 | `component::sofar::entity::sensor::pv_power_5::name` | PV power 5 |
| 920808799 | `component::sofar::entity::sensor::pv_power_4::name` | PV power 4 |
| 920808798 | `component::sofar::entity::sensor::pv_power_3::name` | PV power 3 |
| 920808797 | `component::sofar::entity::sensor::pv_power_10::name` | PV power 10 |
| 920808796 | `component::sofar::entity::sensor::pv_current_9::name` | PV current 9 |
| 920808795 | `component::sofar::entity::sensor::pv_current_8::name` | PV current 8 |
| 920808794 | `component::sofar::entity::sensor::pv_current_7::name` | PV current 7 |
| 920808793 | `component::sofar::entity::sensor::pv_current_6::name` | PV current 6 |
| 920808792 | `component::sofar::entity::sensor::pv_current_5::name` | PV current 5 |
| 920808791 | `component::sofar::entity::sensor::pv_current_4::name` | PV current 4 |
| 920808790 | `component::sofar::entity::sensor::pv_current_3::name` | PV current 3 |
| 920808789 | `component::sofar::entity::sensor::pv_current_2::name` | PV current 2 |
| 920808788 | `component::sofar::entity::sensor::pv_current_10::name` | PV current 10 |
| 920808787 | `component::sofar::entity::sensor::pv_current_1::name` | PV current 1 |
| 920808769 | `component::sofar::entity::sensor::offgrid_loadpeakratio_l3::name` | Off-grid load peak ratio L3 |
| 920808768 | `component::sofar::entity::sensor::offgrid_loadpeakratio_l2::name` | Off-grid load peak ratio L2 |
| 920808767 | `component::sofar::entity::sensor::offgrid_loadpeakratio_l1::name` | Off-grid load peak ratio L1 |
| 920808766 | `component::sofar::entity::sensor::offgrid_loadpeakratio::name` | Off-grid load peak ratio |
| 920808738 | `component::sofar::entity::sensor::hardware_version::name` | Hardware version |
| 920808724 | `component::sofar::entity::sensor::battery_voltage_8::name` | Battery voltage 8 |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
