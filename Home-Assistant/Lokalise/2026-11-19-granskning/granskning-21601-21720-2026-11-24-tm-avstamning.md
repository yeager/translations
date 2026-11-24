# Home Assistant Core – historisk avstämning 21601–21720

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 53 direkta källtexter matchar HA Core-källan; 58 referensanvändningar med 40 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 9 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 21601 | 828725927 | `component::victron_gx::entity::sensor::charger_error_code::state::current_sensor_issue` | Current sensor issue | Problem med strömsensorn | Shared reference target checked |
| 21602 | 828725926 | `component::victron_gx::entity::sensor::charger_error_code::state::converter_issue` | Converter issue | Problem med konverterare | Shared reference target checked |
| 21603 | 828725925 | `component::victron_gx::entity::sensor::charger_error_code::state::charger_temperature_too_high` | Charger temperature too high | Laddartemperaturen är för hög | Shared reference target checked |
| 21604 | 828725924 | `component::victron_gx::entity::sensor::charger_error_code::state::charger_over_current` | Charger over current | Laddare överström | Shared reference target checked |
| 21605 | 828725923 | `component::victron_gx::entity::sensor::charger_error_code::state::charger_current_reversed` | Charger current reversed | Laddström omvänd | Shared reference target checked |
| 21606 | 828725922 | `component::victron_gx::entity::sensor::charger_error_code::state::bulk_time_limit_exceeded` | Bulk time limit exceeded | Tidsgränsen för bulköverföring har överskridits | Shared reference target checked |
| 21607 | 828725921 | `component::victron_gx::entity::sensor::charger_error_code::state::bms_connection_lost` | BMS connection lost | BMS-anslutningen förlorad | Shared reference target checked |
| 21608 | 828725920 | `component::victron_gx::entity::sensor::charger_error_code::state::battery_voltage_too_high` | Battery voltage too high | Batterispänningen är för hög | Shared reference target checked |
| 21609 | 828725919 | `component::victron_gx::entity::sensor::charger_error_code::name` | Error code | Felkod | Shared reference target checked |
| 21610 | 828725918 | `component::victron_gx::entity::sensor::charger_dc_voltage::name` | DC output voltage | DC-utgång spänning | Source-path follow-up open |
| 21611 | 828725917 | `component::victron_gx::entity::sensor::charger_dc_current::name` | DC output current | DC-utgång ström | Source-path follow-up open |
| 21612 | 828725916 | `component::victron_gx::entity::sensor::charge_mode::name` | Charge mode | Laddningsläge | Core-literal match |
| 21613 | 828725915 | `component::victron_gx::entity::sensor::battery_voltage::name` | DC bus voltage | DC-busspänning | Core-literal match |
| 21614 | 828725914 | `component::victron_gx::entity::sensor::battery_total_charge_cycles::unit_of_measurement` | cycles | cykler | Core-literal match |
| 21615 | 828725913 | `component::victron_gx::entity::sensor::battery_total_charge_cycles::name` | Total charge cycles | Totalt antal laddningscykler | Core-literal match |
| 21616 | 828725912 | `component::victron_gx::entity::sensor::battery_time_to_go::name` | Time to go | Tid kvar | Core-literal match |
| 21617 | 828725911 | `component::victron_gx::entity::sensor::battery_time_since_last_full_charge::unit_of_measurement` | seconds | sekunder | Source-path follow-up open |
| 21618 | 828725910 | `component::victron_gx::entity::sensor::battery_time_since_last_full_charge::name` | Time since last full charge | Tid sedan senaste fulla laddning | Core-literal match |
| 21619 | 828725909 | `component::victron_gx::entity::sensor::battery_temperature::name` | Temperature | Temperatur | Shared reference target checked |
| 21620 | 828725908 | `component::victron_gx::entity::sensor::battery_soh::unit_of_measurement` | % | % | Source-path follow-up open |
| 21621 | 828725907 | `component::victron_gx::entity::sensor::battery_soh::name` | State of health | Hälsotillstånd | Core-literal match |
| 21622 | 828725906 | `component::victron_gx::entity::sensor::battery_soc::name` | Charge | Laddning | Core-literal match |
| 21623 | 828725905 | `component::victron_gx::entity::sensor::battery_power::name` | Power | Effekt | Shared reference target checked |
| 21624 | 828725904 | `component::victron_gx::entity::sensor::battery_nr_modules_online::unit_of_measurement` | modules | moduler | Core-literal match |
| 21625 | 828725903 | `component::victron_gx::entity::sensor::battery_nr_modules_online::name` | Number of modules online | Antal moduler online | Core-literal match |
| 21626 | 828725902 | `component::victron_gx::entity::sensor::battery_nr_modules_offline::unit_of_measurement` | modules | moduler | Core-literal match |
| 21627 | 828725901 | `component::victron_gx::entity::sensor::battery_nr_modules_offline::name` | Number of modules offline | Antal moduler offline | Core-literal match |
| 21628 | 828725900 | `component::victron_gx::entity::sensor::battery_nr_modules_blocking_discharge::unit_of_measurement` | modules | moduler | Core-literal match |
| 21629 | 828725899 | `component::victron_gx::entity::sensor::battery_nr_modules_blocking_discharge::name` | Number of modules blocking discharge | Antal moduler som blockerar urladdning | Core-literal match |
| 21630 | 828725898 | `component::victron_gx::entity::sensor::battery_nr_modules_blocking_charge::unit_of_measurement` | modules | moduler | Core-literal match |
| 21631 | 828725897 | `component::victron_gx::entity::sensor::battery_nr_modules_blocking_charge::name` | Number of modules blocking charge | Antal moduler som blockerar laddning | Core-literal match |
| 21632 | 828725896 | `component::victron_gx::entity::sensor::battery_minimum_voltage::name` | Minimum voltage | Lägsta spänning | Core-literal match |
| 21633 | 828725895 | `component::victron_gx::entity::sensor::battery_min_voltage_cell_id::name` | Minimum voltage cell ID | Lägsta spänning cell-ID | Core-literal match |
| 21634 | 828725894 | `component::victron_gx::entity::sensor::battery_min_temperature_cell_id::name` | Minimum temperature cell ID | Lägsta temperatur cell-ID | Core-literal match |
| 21635 | 828725893 | `component::victron_gx::entity::sensor::battery_min_cell_voltage::name` | Minimum cell voltage | Lägsta cellspänning | Core-literal match |
| 21636 | 828725892 | `component::victron_gx::entity::sensor::battery_min_cell_temperature::name` | Minimum cell temperature | Lägsta celltemperatur | Core-literal match |
| 21637 | 828725891 | `component::victron_gx::entity::sensor::battery_mid_voltage_deviation::unit_of_measurement` | % | % | Source-path follow-up open |
| 21638 | 828725890 | `component::victron_gx::entity::sensor::battery_mid_voltage_deviation::name` | DC bus mid voltage deviation | DC-bussens mellanspänning, avvikelse | Core-literal match |
| 21639 | 828725889 | `component::victron_gx::entity::sensor::battery_mid_voltage::name` | DC bus mid voltage | DC-bussens mellanspänning | Core-literal match |
| 21640 | 828725888 | `component::victron_gx::entity::sensor::battery_maximum_voltage::name` | Maximum voltage | Högsta spänning | Core-literal match |
| 21641 | 828725887 | `component::victron_gx::entity::sensor::battery_max_voltage_cell_id::name` | Maximum voltage cell ID | Högsta spänning cell-ID | Core-literal match |
| 21642 | 828725886 | `component::victron_gx::entity::sensor::battery_max_temperature_cell_id::name` | Maximum temperature cell ID | Högsta temperatur cell-ID | Core-literal match |
| 21643 | 828725885 | `component::victron_gx::entity::sensor::battery_max_discharge_current::name` | Maximum allowed discharge current | Högsta tillåtna urladdningsström | Core-literal match |
| 21644 | 828725884 | `component::victron_gx::entity::sensor::battery_max_charge_voltage::name` | Maximum allowed charging voltage | Högsta tillåtna laddningsspänning | Core-literal match |
| 21645 | 828725883 | `component::victron_gx::entity::sensor::battery_max_charge_current::name` | Maximum allowed charge current | Högsta tillåtna laddningsström | Core-literal match |
| 21646 | 828725882 | `component::victron_gx::entity::sensor::battery_max_cell_voltage::name` | Maximum cell voltage | Högsta cellspänning | Core-literal match |
| 21647 | 828725881 | `component::victron_gx::entity::sensor::battery_max_cell_temperature::name` | Maximum cell temperature | Högsta celltemperatur | Core-literal match |
| 21648 | 828725880 | `component::victron_gx::entity::sensor::battery_low_charge_temperature::state::warning` | Warning | Varning | Shared reference target checked |
| 21649 | 828725879 | `component::victron_gx::entity::sensor::battery_low_charge_temperature::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 21650 | 828725878 | `component::victron_gx::entity::sensor::battery_low_charge_temperature::state::alarm` | Alarm | Larm | Shared reference target checked |
| 21651 | 828725877 | `component::victron_gx::entity::sensor::battery_low_charge_temperature::name` | Low charge temperature | Låg laddningstemperatur | Core-literal match |
| 21652 | 828725876 | `component::victron_gx::entity::sensor::battery_low_cell_voltage::state::warning` | Warning | Varning | Shared reference target checked |
| 21653 | 828725875 | `component::victron_gx::entity::sensor::battery_low_cell_voltage::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 21654 | 828725874 | `component::victron_gx::entity::sensor::battery_low_cell_voltage::state::alarm` | Alarm | Larm | Shared reference target checked |
| 21655 | 828725873 | `component::victron_gx::entity::sensor::battery_low_cell_voltage::name` | Low cell voltage | Låg cellspänning | Core-literal match |
| 21656 | 828725872 | `component::victron_gx::entity::sensor::battery_last_discharge::name` | Last discharge | Senaste urladdning | Core-literal match |
| 21657 | 828725871 | `component::victron_gx::entity::sensor::battery_internal_failure::state::warning` | Warning | Varning | Shared reference target checked |
| 21658 | 828725870 | `component::victron_gx::entity::sensor::battery_internal_failure::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 21659 | 828725869 | `component::victron_gx::entity::sensor::battery_internal_failure::state::alarm` | Alarm | Larm | Shared reference target checked |
| 21660 | 828725868 | `component::victron_gx::entity::sensor::battery_internal_failure::name` | Internal failure | Internt fel | Core-literal match |
| 21661 | 828725867 | `component::victron_gx::entity::sensor::battery_installed_capacity::unit_of_measurement` | Ah | Ah | Source-path follow-up open |
| 21662 | 828725866 | `component::victron_gx::entity::sensor::battery_installed_capacity::name` | Installed capacity | Installerad kapacitet | Core-literal match |
| 21663 | 828725865 | `component::victron_gx::entity::sensor::battery_high_discharge_current::state::warning` | Warning | Varning | Shared reference target checked |
| 21664 | 828725864 | `component::victron_gx::entity::sensor::battery_high_discharge_current::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 21665 | 828725863 | `component::victron_gx::entity::sensor::battery_high_discharge_current::state::alarm` | Alarm | Larm | Shared reference target checked |
| 21666 | 828725862 | `component::victron_gx::entity::sensor::battery_high_discharge_current::name` | High discharge current | Hög urladdningsström | Core-literal match |
| 21667 | 828725861 | `component::victron_gx::entity::sensor::battery_high_charge_temperature::state::warning` | Warning | Varning | Shared reference target checked |
| 21668 | 828725860 | `component::victron_gx::entity::sensor::battery_high_charge_temperature::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 21669 | 828725859 | `component::victron_gx::entity::sensor::battery_high_charge_temperature::state::alarm` | Alarm | Larm | Shared reference target checked |
| 21670 | 828725858 | `component::victron_gx::entity::sensor::battery_high_charge_temperature::name` | High charge temperature | Hög laddningstemperatur | Core-literal match |
| 21671 | 828725857 | `component::victron_gx::entity::sensor::battery_high_charge_current::state::warning` | Warning | Varning | Shared reference target checked |
| 21672 | 828725856 | `component::victron_gx::entity::sensor::battery_high_charge_current::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 21673 | 828725855 | `component::victron_gx::entity::sensor::battery_high_charge_current::state::alarm` | Alarm | Larm | Shared reference target checked |
| 21674 | 828725854 | `component::victron_gx::entity::sensor::battery_high_charge_current::name` | High charge current | Hög laddningsström | Core-literal match |
| 21675 | 828725853 | `component::victron_gx::entity::sensor::battery_discharged_energy::name` | Discharged energy | Urladdad energi | Core-literal match |
| 21676 | 828725852 | `component::victron_gx::entity::sensor::battery_deepest_discharge::name` | Deepest discharge | Djupaste urladdning | Core-literal match |
| 21677 | 828725851 | `component::victron_gx::entity::sensor::battery_current::name` | DC bus current | DC-busström | Core-literal match |
| 21678 | 828725850 | `component::victron_gx::entity::sensor::battery_cumulative_ah_drawn::unit_of_measurement` | Ah | Ah | Source-path follow-up open |
| 21679 | 828725849 | `component::victron_gx::entity::sensor::battery_cumulative_ah_drawn::name` | Cumulative Ah drawn | Ackumulerad urtagen laddning (Ah) | Core-literal match |
| 21680 | 828725848 | `component::victron_gx::entity::sensor::battery_consumed_amphours::unit_of_measurement` | Ah | Ah | Source-path follow-up open |
| 21681 | 828725847 | `component::victron_gx::entity::sensor::battery_consumed_amphours::name` | Consumed amp-hours | Förbrukade amperetimmar | Core-literal match |
| 21682 | 828725846 | `component::victron_gx::entity::sensor::battery_charged_energy::name` | Charged energy | Laddad energi | Core-literal match |
| 21683 | 828725845 | `component::victron_gx::entity::sensor::battery_cell_voltage_deviation::name` | Cell voltage deviation | Cellspänningsavvikelse | Core-literal match |
| 21684 | 828725844 | `component::victron_gx::entity::sensor::battery_cell_imbalance::state::warning` | Warning | Varning | Shared reference target checked |
| 21685 | 828725843 | `component::victron_gx::entity::sensor::battery_cell_imbalance::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 21686 | 828725842 | `component::victron_gx::entity::sensor::battery_cell_imbalance::state::alarm` | Alarm | Larm | Shared reference target checked |
| 21687 | 828725841 | `component::victron_gx::entity::sensor::battery_cell_imbalance::name` | Cell imbalance | Cellobalans | Core-literal match |
| 21688 | 828725840 | `component::victron_gx::entity::sensor::battery_cell_cell_id_voltage::name` | Cell {cell_id} voltage | Cell {cell_id} spänning | Core-literal match |
| 21689 | 828725839 | `component::victron_gx::entity::sensor::battery_capacity::unit_of_measurement` | Ah | Ah | Source-path follow-up open |
| 21690 | 828725838 | `component::victron_gx::entity::sensor::battery_capacity::name` | Capacity | Kapacitet | Core-literal match |
| 21691 | 828725837 | `component::victron_gx::entity::sensor::battery_average_discharge::name` | Average discharge | Genomsnittlig urladdning | Core-literal match |
| 21692 | 828725836 | `component::victron_gx::entity::sensor::battery_automatic_syncs::unit_of_measurement` | syncs | synkroniseringar | Core-literal match |
| 21693 | 828725835 | `component::victron_gx::entity::sensor::battery_automatic_syncs::name` | Automatic syncs | Automatiska synkroniseringar | Core-literal match |
| 21694 | 828725834 | `component::victron_gx::entity::sensor::auxiliary_battery_voltage::name` | Auxiliary battery voltage | Hjälpbatteriets spänning | Core-literal match |
| 21695 | 828725833 | `component::victron_gx::entity::sensor::alternator_state::state::sustain_alt` | Sustain alt | Sustain alt | Shared reference target checked |
| 21696 | 828725832 | `component::victron_gx::entity::sensor::alternator_state::state::sustain` | Sustain | Sustain | Shared reference target checked |
| 21697 | 828725831 | `component::victron_gx::entity::sensor::alternator_state::state::storage` | Storage | Lagring | Shared reference target checked |
| 21698 | 828725830 | `component::victron_gx::entity::sensor::alternator_state::state::starting_up` | Starting up | Startar upp | Shared reference target checked |
| 21699 | 828725829 | `component::victron_gx::entity::sensor::alternator_state::state::scheduled_recharging` | Scheduled recharging | Schemalagd uppladdning | Shared reference target checked |
| 21700 | 828725828 | `component::victron_gx::entity::sensor::alternator_state::state::repeated_absorption` | Repeated absorption | Upprepad absorption | Shared reference target checked |
| 21701 | 828725827 | `component::victron_gx::entity::sensor::alternator_state::state::recharging` | Recharging | Uppladdar | Shared reference target checked |
| 21702 | 828725826 | `component::victron_gx::entity::sensor::alternator_state::state::power_supply` | Power supply | Strömförsörjning | Shared reference target checked |
| 21703 | 828725825 | `component::victron_gx::entity::sensor::alternator_state::state::power_assist` | Power Assist | Power Assist | Shared reference target checked |
| 21704 | 828725824 | `component::victron_gx::entity::sensor::alternator_state::state::passthrough` | Passthrough | Genomströmning | Shared reference target checked |
| 21705 | 828725823 | `component::victron_gx::entity::sensor::alternator_state::state::off` | Off | Av | Shared reference target checked |
| 21706 | 828725822 | `component::victron_gx::entity::sensor::alternator_state::state::low_power` | Low power | Låg ström | Shared reference target checked |
| 21707 | 828725821 | `component::victron_gx::entity::sensor::alternator_state::state::inverting` | Inverting | Växelriktar | Shared reference target checked |
| 21708 | 828725820 | `component::victron_gx::entity::sensor::alternator_state::state::float` | Float | Flytande | Shared reference target checked |
| 21709 | 828725819 | `component::victron_gx::entity::sensor::alternator_state::state::fault` | Fault | Fel | Shared reference target checked |
| 21710 | 828725818 | `component::victron_gx::entity::sensor::alternator_state::state::external_control` | External control | Extern styrning | Shared reference target checked |
| 21711 | 828725817 | `component::victron_gx::entity::sensor::alternator_state::state::equalize` | Equalize | Utjämna | Shared reference target checked |
| 21712 | 828725816 | `component::victron_gx::entity::sensor::alternator_state::state::discharging` | Discharging | Laddar ur | Shared reference target checked |
| 21713 | 828725815 | `component::victron_gx::entity::sensor::alternator_state::state::bulk` | Bulk | Bulk | Shared reference target checked |
| 21714 | 828725814 | `component::victron_gx::entity::sensor::alternator_state::state::battery_safe` | Battery Safe | Batteri säkert | Shared reference target checked |
| 21715 | 828725813 | `component::victron_gx::entity::sensor::alternator_state::state::auto_equalize` | Auto equalize / recondition | Automatisk utjämning/rekonditionering | Shared reference target checked |
| 21716 | 828725812 | `component::victron_gx::entity::sensor::alternator_state::state::absorption` | Absorption | Absorption | Shared reference target checked |
| 21717 | 828725811 | `component::victron_gx::entity::sensor::alternator_state::name` | State | Tillstånd | Shared reference target checked |
| 21718 | 828725810 | `component::victron_gx::entity::sensor::alternator_input_voltage::name` | Input voltage | Ingångsspänning | Shared reference target checked |
| 21719 | 828725809 | `component::victron_gx::entity::sensor::alternator_input_power::name` | Input power | Ingångseffekt | Shared reference target checked |
| 21720 | 828725808 | `component::victron_gx::entity::sensor::alternator_input_current::name` | Input current | Ingångsström | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 828725918 | `component::victron_gx::entity::sensor::charger_dc_voltage::name` | DC output voltage |
| 828725917 | `component::victron_gx::entity::sensor::charger_dc_current::name` | DC output current |
| 828725911 | `component::victron_gx::entity::sensor::battery_time_since_last_full_charge::unit_of_measurement` | seconds |
| 828725908 | `component::victron_gx::entity::sensor::battery_soh::unit_of_measurement` | % |
| 828725891 | `component::victron_gx::entity::sensor::battery_mid_voltage_deviation::unit_of_measurement` | % |
| 828725867 | `component::victron_gx::entity::sensor::battery_installed_capacity::unit_of_measurement` | Ah |
| 828725850 | `component::victron_gx::entity::sensor::battery_cumulative_ah_drawn::unit_of_measurement` | Ah |
| 828725848 | `component::victron_gx::entity::sensor::battery_consumed_amphours::unit_of_measurement` | Ah |
| 828725839 | `component::victron_gx::entity::sensor::battery_capacity::unit_of_measurement` | Ah |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
