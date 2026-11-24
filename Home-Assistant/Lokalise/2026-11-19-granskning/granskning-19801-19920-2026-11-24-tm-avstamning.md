# Home Assistant Core – historisk avstämning 19801–19920

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 96 direkta källtexter matchar HA Core-källan; 16 referensanvändningar med 12 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 8 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 19801 | 836231001 | `component::melcloud::entity::sensor::daily_heating_energy_produced::name` | Daily heating energy produced | Daglig producerad värmeenergi | Core-literal match |
| 19802 | 836231000 | `component::melcloud::entity::sensor::daily_heating_energy_consumed::name` | Daily heating energy consumed | Daglig förbrukning av värmeenergi | Core-literal match |
| 19803 | 836230999 | `component::melcloud::entity::sensor::daily_cooling_energy_produced::name` | Daily cooling energy produced | Daglig producerad kylenergi | Core-literal match |
| 19804 | 836230998 | `component::melcloud::entity::sensor::daily_cooling_energy_consumed::name` | Daily cooling energy consumed | Daglig förbrukning av kylenergi | Core-literal match |
| 19805 | 836230997 | `component::earn_e_p1::entity::sensor::wifi_rssi::name` | Wi-Fi RSSI | Wi-Fi-RSSI | Core-literal match |
| 19806 | 836230996 | `component::earn_e_p1::entity::sensor::voltage_l1::name` | Voltage L1 | Spänning L1 | Source-path follow-up open |
| 19807 | 836230995 | `component::earn_e_p1::entity::sensor::power_imported::name` | Power imported | Importerad effekt | Core-literal match |
| 19808 | 836230994 | `component::earn_e_p1::entity::sensor::power_exported::name` | Power exported | Exporterad effekt | Core-literal match |
| 19809 | 836230993 | `component::earn_e_p1::entity::sensor::gas_consumed::name` | Gas consumed | Gasförbrukning | Core-literal match |
| 19810 | 836230992 | `component::earn_e_p1::entity::sensor::energy_imported_tariff2::name` | Energy imported tariff 2 | Tariff för importerad energi 2 | Core-literal match |
| 19811 | 836230991 | `component::earn_e_p1::entity::sensor::energy_imported_tariff1::name` | Energy imported tariff 1 | Tariff för importerad energi 1 | Core-literal match |
| 19812 | 836230990 | `component::earn_e_p1::entity::sensor::energy_exported_tariff2::name` | Energy exported tariff 2 | Tariff för exporterad energi 2 | Core-literal match |
| 19813 | 836230989 | `component::earn_e_p1::entity::sensor::energy_exported_tariff1::name` | Energy exported tariff 1 | Tariff för exporterad energi 1 | Core-literal match |
| 19814 | 836230988 | `component::earn_e_p1::entity::sensor::current_l1::name` | Current L1 | Ström L1 | Source-path follow-up open |
| 19815 | 836230987 | `component::earn_e_p1::config::step::user::title` | Connect to EARN-E P1 meter | Anslut till EARN-E P1-mätaren | Core-literal match |
| 19816 | 836230986 | `component::earn_e_p1::config::step::user::description` | No device was automatically discovered. Enter the IP address of your EARN-E energy monitor manually. | Ingen enhet hittades automatiskt. Ange IP-adressen till din EARN-E-energimätare manuellt. | Core-literal match |
| 19817 | 836230985 | `component::earn_e_p1::config::step::user::data_description::host` | The local IP address of your EARN-E P1 meter (e.g. 192.168.1.100). | Den lokala IP-adressen för din EARN-E P1-mätare (t.ex. 192.168.1.100). | Core-literal match |
| 19818 | 836230984 | `component::earn_e_p1::config::step::user::data::host` | IP address | IP-adress | Shared reference target checked |
| 19819 | 836230983 | `component::earn_e_p1::config::step::discovery_confirm::title` | Discovered EARN-E P1 meter | Upptäckt EARN-E P1-mätare | Core-literal match |
| 19820 | 836230982 | `component::earn_e_p1::config::step::discovery_confirm::description` | An EARN-E P1 meter was found at **{host}**. | En EARN-E P1-mätare hittades på **{host}**. | Core-literal match |
| 19821 | 836230981 | `component::earn_e_p1::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 19822 | 836230980 | `component::earn_e_p1::config::error::cannot_connect` | Cannot connect — no data received from the device. Verify the IP address and that the EARN-E is powered on. | Kan inte ansluta — ingen data tas emot från enheten. Kontrollera IP-adressen och att EARN-E är påslagen. | Core-literal match |
| 19823 | 836230979 | `component::earn_e_p1::config::abort::unknown` | Unexpected error | Oväntat fel | Core-literal match |
| 19824 | 836230978 | `component::earn_e_p1::config::abort::cannot_connect` | Cannot connect — no data received from the device. | Kan inte ansluta — ingen data tas emot från enheten. | Core-literal match |
| 19825 | 836230977 | `component::earn_e_p1::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 19826 | 836230953 | `component::teleinfo::exceptions::timeout_error::message` | Timeout waiting for Teleinfo data | Timeout vid väntan på data från Teleinfo | Core-literal match |
| 19827 | 836230952 | `component::teleinfo::exceptions::decode_error::message` | Failed to decode Teleinfo frame | Det gick inte att avkoda Teleinfo-ramen | Core-literal match |
| 19828 | 836230951 | `component::teleinfo::exceptions::communication_error::message` | Failed to communicate with Teleinfo dongle | Det gick inte att kommunicera med Teleinfo-dongeln | Core-literal match |
| 19829 | 836230950 | `component::teleinfo::entity::sensor::white_day_peak_index::name` | White day peak index | Vit dag peak-index | Core-literal match |
| 19830 | 836230949 | `component::teleinfo::entity::sensor::white_day_off_peak_index::name` | White day off-peak index | Lågtrafikindex för vit dag | Core-literal match |
| 19831 | 836230948 | `component::teleinfo::entity::sensor::tomorrow_color::state::white` | White | Vit | Core-literal match |
| 19832 | 836230947 | `component::teleinfo::entity::sensor::tomorrow_color::state::red` | Red | Röd | Core-literal match |
| 19833 | 836230946 | `component::teleinfo::entity::sensor::tomorrow_color::state::blue` | Blue | Blå | Core-literal match |
| 19834 | 836230945 | `component::teleinfo::entity::sensor::tomorrow_color::name` | Tomorrow color | Färg imorgon | Core-literal match |
| 19835 | 836230944 | `component::teleinfo::entity::sensor::red_day_peak_index::name` | Red day peak index | Röd dag peak-index | Core-literal match |
| 19836 | 836230943 | `component::teleinfo::entity::sensor::red_day_off_peak_index::name` | Red day off-peak index | Lågtrafikindex för röd dag | Core-literal match |
| 19837 | 836230942 | `component::teleinfo::entity::sensor::peak_mobile_hours_index::name` | Peak mobile hours index | Index för mobila timmar | Core-literal match |
| 19838 | 836230941 | `component::teleinfo::entity::sensor::peak_index::name` | Peak index | Peak-index | Core-literal match |
| 19839 | 836230940 | `component::teleinfo::entity::sensor::off_peak_index::name` | Off-peak index | Lågtrafikindex | Core-literal match |
| 19840 | 836230939 | `component::teleinfo::entity::sensor::normal_hours_index::name` | Normal hours index | Index för normala timmar | Core-literal match |
| 19841 | 836230938 | `component::teleinfo::entity::sensor::instantaneous_current::name` | Instantaneous current | Momentan ström | Core-literal match |
| 19842 | 836230937 | `component::teleinfo::entity::sensor::ejp_warning::name` | EJP warning | EJP-varning | Core-literal match |
| 19843 | 836230936 | `component::teleinfo::entity::sensor::current_tariff_period::state::peak_white_day` | Peak white day | Peak vit dag | Core-literal match |
| 19844 | 836230935 | `component::teleinfo::entity::sensor::current_tariff_period::state::peak_red_day` | Peak red day | Peak röd dag | Core-literal match |
| 19845 | 836230934 | `component::teleinfo::entity::sensor::current_tariff_period::state::peak_blue_day` | Peak blue day | Peak blå dag | Core-literal match |
| 19846 | 836230933 | `component::teleinfo::entity::sensor::current_tariff_period::state::peak` | Peak | Peak | Core-literal match |
| 19847 | 836230932 | `component::teleinfo::entity::sensor::current_tariff_period::state::off_peak_white_day` | Off-peak white day | Lågtrafik under vit dag | Core-literal match |
| 19848 | 836230931 | `component::teleinfo::entity::sensor::current_tariff_period::state::off_peak_red_day` | Off-peak red day | Lågtrafik under röd dag | Core-literal match |
| 19849 | 836230930 | `component::teleinfo::entity::sensor::current_tariff_period::state::off_peak_blue_day` | Off-peak blue day | Lågtrafik under blå dag | Core-literal match |
| 19850 | 836230929 | `component::teleinfo::entity::sensor::current_tariff_period::state::off_peak` | Off-peak | Lågtrafik | Core-literal match |
| 19851 | 836230928 | `component::teleinfo::entity::sensor::current_tariff_period::state::normal_hours` | Normal hours | Vanliga timmar | Core-literal match |
| 19852 | 836230927 | `component::teleinfo::entity::sensor::current_tariff_period::state::mobile_peak` | Mobile peak | Mobil topp | Core-literal match |
| 19853 | 836230926 | `component::teleinfo::entity::sensor::current_tariff_period::state::all_hours` | All hours | Alla timmar | Core-literal match |
| 19854 | 836230925 | `component::teleinfo::entity::sensor::current_tariff_period::name` | Current tariff period | Nuvarande tariffperiod | Core-literal match |
| 19855 | 836230924 | `component::teleinfo::entity::sensor::blue_day_peak_index::name` | Blue day peak index | Blå dag peak-index | Core-literal match |
| 19856 | 836230923 | `component::teleinfo::entity::sensor::blue_day_off_peak_index::name` | Blue day off-peak index | Lågtrafikindex för blå dag | Core-literal match |
| 19857 | 836230922 | `component::teleinfo::entity::sensor::base_index::name` | Index | Index | Core-literal match |
| 19858 | 836230921 | `component::teleinfo::entity::sensor::apparent_power::name` | Apparent power | Skenbar effekt | Source-path follow-up open |
| 19859 | 836230920 | `component::teleinfo::config::step::user::data_description::serial_port` | The path to the serial port connected to the Teleinfo module, e.g. /dev/ttyUSB0. | Sökvägen till den seriella porten som är ansluten till Teleinfo-modulen, t.ex. /dev/ttyUSB0. | Core-literal match |
| 19860 | 836230919 | `component::teleinfo::config::step::user::data::serial_port` | Serial port | Serieport | Core-literal match |
| 19861 | 836230918 | `component::teleinfo::config::step::usb_confirm::description` | A Teleinfo device was detected. Do you want to set it up? | En Teleinfo-enhet har upptäckts. Vill du konfigurera den? | Core-literal match |
| 19862 | 836230917 | `component::teleinfo::config::flow_title` | {name} | {name} | Core-literal match |
| 19863 | 836230916 | `component::teleinfo::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 19864 | 836230915 | `component::teleinfo::config::error::timeout_connect` | Timeout while establishing a connection | Tidsgränsen överskreds när anslutningen upprättades. | Shared reference target checked |
| 19865 | 836230914 | `component::teleinfo::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 19866 | 836230913 | `component::teleinfo::config::abort::not_teleinfo_device` | The device does not appear to be a Teleinfo module | Enheten verkar inte vara en Teleinfo-modul | Core-literal match |
| 19867 | 836230912 | `component::teleinfo::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 19868 | 836230559 | `component::unifi_access::services::set_lock_rule::name` | Set lock rule | Ställ in låsregel | Core-literal match |
| 19869 | 836230558 | `component::unifi_access::services::set_lock_rule::fields::rule::name` | Rule | Regel | Core-literal match |
| 19870 | 836230557 | `component::unifi_access::services::set_lock_rule::fields::rule::description` | The lock rule to apply. | Den låsregel som ska tillämpas. | Core-literal match |
| 19871 | 836230556 | `component::unifi_access::services::set_lock_rule::fields::interval::name` | Interval | Intervall | Core-literal match |
| 19872 | 836230555 | `component::unifi_access::services::set_lock_rule::fields::interval::description` | How long the rule stays active. Defaults to 10 minutes. | Hur länge regeln är aktiv. Standardinställningen är 10 minuter. | Core-literal match |
| 19873 | 836230554 | `component::unifi_access::services::set_lock_rule::fields::device_id::name` | Door | Dörr | Core-literal match |
| 19874 | 836230553 | `component::unifi_access::services::set_lock_rule::fields::device_id::description` | The UniFi Access door to update. | Den UniFi Access-dörr som ska uppdateras. | Core-literal match |
| 19875 | 836230552 | `component::unifi_access::services::set_lock_rule::description` | Apply a temporary lock rule to a UniFi Access door. | Tillämpa en tillfällig låsregel på en UniFi Access-dörr. | Core-literal match |
| 19876 | 836230551 | `component::unifi_access::selector::rule::options::reset` | Reset | Återställ | Core-literal match |
| 19877 | 836230550 | `component::unifi_access::selector::rule::options::lock_early` | Lock early | Lås tidigt | Core-literal match |
| 19878 | 836230549 | `component::unifi_access::selector::rule::options::keep_unlock` | Keep unlocked | Fortsatt upplåst | Core-literal match |
| 19879 | 836230548 | `component::unifi_access::selector::rule::options::keep_lock` | Keep locked | Fortsatt låst | Core-literal match |
| 19880 | 836230547 | `component::unifi_access::selector::rule::options::custom` | Custom | Anpassad | Core-literal match |
| 19881 | 836230546 | `component::unifi_access::exceptions::invalid_target::message` | The selected device is not a UniFi Access door. | Den valda enheten är inte en UniFi Access-dörr. | Core-literal match |
| 19882 | 836230545 | `component::unifi_access::exceptions::invalid_lock_rule_type::message` | The provided lock rule type is invalid. | Den angivna låsregeltypen är ogiltig. | Core-literal match |
| 19883 | 836230529 | `component::satel_integra::exceptions::panel_busy::message` | Successfully connected, but alarm panel reports it's busy. Please check no other connections are active. | Ansluten, men larmpanelen rapporterar att den är upptagen. Kontrollera att inga andra anslutningar är aktiva. | Shared reference target checked |
| 19884 | 836230528 | `component::satel_integra::exceptions::connection_initialization_failed::message` | Successfully connected, but failed to read data from the panel. Please check the integration encryption key is correct if your panel requires encryption. | Ansluten, men det gick inte att läsa data från panelen. Kontrollera att integrationskrypteringsnyckeln är korrekt ifall din panel kräver kryptering. | Shared reference target checked |
| 19885 | 836230527 | `component::satel_integra::exceptions::cannot_connect::message` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 19886 | 836230526 | `component::satel_integra::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 19887 | 836230525 | `component::satel_integra::config::error::panel_busy` | Successfully connected, but alarm panel reports it's busy. Please check no other connections are active. | Ansluten, men larmpanelen rapporterar att den är upptagen. Kontrollera att inga andra anslutningar är aktiva. | Core-literal match |
| 19888 | 836230524 | `component::satel_integra::config::error::connection_initialization_failed` | Successfully connected, but failed to read data from the panel. Please check the integration encryption key is correct if your panel requires encryption. | Ansluten, men det gick inte att läsa data från panelen. Kontrollera att integrationskrypteringsnyckeln är korrekt ifall din panel kräver kryptering. | Core-literal match |
| 19889 | 836124532 | `component::victron_gx::entity::time::system_ess_schedule_charge_slot_start::name` | ESS BatteryLife schedule charge {slot} start | ESS BatteryLife schemalagd laddning {slot} start | Core-literal match |
| 19890 | 836118490 | `component::myneomitis::entity::climate::myneomitis::state_attributes::preset_mode::state::standby` | Standby | Viloläge | Shared reference target checked |
| 19891 | 836118489 | `component::myneomitis::entity::climate::myneomitis::state_attributes::preset_mode::state::setpoint` | Setpoint | Börvärde | Core-literal match |
| 19892 | 836118488 | `component::myneomitis::entity::climate::myneomitis::state_attributes::preset_mode::state::eco` | Eco | Eco | Core-literal match |
| 19893 | 836118487 | `component::myneomitis::entity::climate::myneomitis::state_attributes::preset_mode::state::comfort_plus` | Comfort + | Comfort + | Core-literal match |
| 19894 | 836118486 | `component::myneomitis::entity::climate::myneomitis::state_attributes::preset_mode::state::comfort` | Comfort | Komfort | Core-literal match |
| 19895 | 836118485 | `component::myneomitis::entity::climate::myneomitis::state_attributes::preset_mode::state::boost` | Boost | Boost | Core-literal match |
| 19896 | 836118484 | `component::myneomitis::entity::climate::myneomitis::state_attributes::preset_mode::state::auto` | Auto | Auto | Shared reference target checked |
| 19897 | 836118483 | `component::myneomitis::entity::climate::myneomitis::state_attributes::preset_mode::state::antifrost` | Frost protection | Frostskydd | Core-literal match |
| 19898 | 836111420 | `component::evohome::services::set_system_mode::fields::entity_id::name` | Entity | Entitet | Source-path follow-up open |
| 19899 | 836111419 | `component::evohome::services::set_system_mode::fields::entity_id::description` | The Evohome controller climate entity. | Evohome-styrenhetens klimatentitet. | Source-path follow-up open |
| 19900 | 836111418 | `component::evohome::issues::deprecated_controller_service::title` | Untargeted Evohome controller action is deprecated | Oriktad Evohome-kontrollåtgärd är utfasad | Source-path follow-up open |
| 19901 | 836111417 | `component::evohome::issues::deprecated_controller_service::description` | The `{service}` action without `entity_id` is deprecated and will stop working in Home Assistant {breaks_in_ha_version}. Update any automation or script to include `entity_id`, targeting the controller's climate entity. | Åtgärden `{service}` utan `entity_id` är utfasad och kommer inte längre att fungera i Home Assistant {breaks_in_ha_version}. Uppdatera alla automatiseringar eller skript så att de inkluderar `entity_id` och riktar sig mot styrenhetens klimatentitet. | Source-path follow-up open |
| 19902 | 836111416 | `component::evohome::exceptions::entity_not_found::message` | The specified entity `{entity_id}` could not be found | Den valda entiteten `{entity_id}` kunde inte hittas | Source-path follow-up open |
| 19903 | 836111415 | `component::evohome::exceptions::controller_only_service::message` | Only Evohome controllers support the `{service}` action | Endast Evohome-kontroller stöder åtgärden `{service}` | Core-literal match |
| 19904 | 836109900 | `component::lutron::entity::select::led_state::state::slow_flash` | Slow flash | Långsam blixt | Core-literal match |
| 19905 | 836109899 | `component::lutron::entity::select::led_state::state::on` | On | På | Shared reference target checked |
| 19906 | 836109898 | `component::lutron::entity::select::led_state::state::off` | Off | Av | Shared reference target checked |
| 19907 | 836109897 | `component::lutron::entity::select::led_state::state::fast_flash` | Fast flash | Snabb blixt | Core-literal match |
| 19908 | 836100422 | `component::victron_gx::entity::number::vebus_inverter_current_limit::name` | Current limit | Strömgräns | Shared reference target checked |
| 19909 | 836100421 | `component::victron_gx::entity::number::vebus_ac_power_setpoint_phase::name` | AC power setpoint {phase} | AC-effekt börvärde {phase} | Core-literal match |
| 19910 | 836100420 | `component::victron_gx::entity::number::transfer_switch_generator_current_limit::name` | Generator AC current limit | Generatorns växelströmsgräns | Core-literal match |
| 19911 | 836100419 | `component::victron_gx::entity::number::temperature_scale::name` | Scale factor | Skalfaktor | Core-literal match |
| 19912 | 836100418 | `component::victron_gx::entity::number::temperature_offset::name` | Offset | Offset | Core-literal match |
| 19913 | 836100417 | `component::victron_gx::entity::number::system_ess_schedule_charge_slot_soc::name` | ESS BatteryLife schedule charge {slot} SoC | ESS BatteryLife schemalagd laddning {slot} SoC | Core-literal match |
| 19914 | 836100416 | `component::victron_gx::entity::number::system_ess_schedule_charge_slot_duration::name` | ESS BatteryLife schedule charge {slot} duration | ESS BatteryLife schemalagd laddning {slot} varaktighet | Core-literal match |
| 19915 | 836100415 | `component::victron_gx::entity::number::system_ess_min_soc_limit::name` | ESS min SoC limit | ESS minsta SoC-gräns | Core-literal match |
| 19916 | 836100414 | `component::victron_gx::entity::number::system_ess_max_inverter_power_limit::name` | ESS max inverter power limit | ESS maximal växelriktare effektgräns | Core-literal match |
| 19917 | 836100413 | `component::victron_gx::entity::number::system_ess_max_feed_in_power::name` | ESS max feed-in power | ESS maximal feed in-effekt | Core-literal match |
| 19918 | 836100412 | `component::victron_gx::entity::number::system_ess_max_charge_voltage::name` | ESS max charge voltage | ESS maximal laddspänning | Core-literal match |
| 19919 | 836100411 | `component::victron_gx::entity::number::system_ess_max_charge_power::name` | ESS max charge power limit | ESS maximal laddeffektgräns | Core-literal match |
| 19920 | 836100410 | `component::victron_gx::entity::number::system_ess_max_charge_current::name` | ESS max charge current | ESS maximal laddström | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 836230996 | `component::earn_e_p1::entity::sensor::voltage_l1::name` | Voltage L1 |
| 836230988 | `component::earn_e_p1::entity::sensor::current_l1::name` | Current L1 |
| 836230921 | `component::teleinfo::entity::sensor::apparent_power::name` | Apparent power |
| 836111420 | `component::evohome::services::set_system_mode::fields::entity_id::name` | Entity |
| 836111419 | `component::evohome::services::set_system_mode::fields::entity_id::description` | The Evohome controller climate entity. |
| 836111418 | `component::evohome::issues::deprecated_controller_service::title` | Untargeted Evohome controller action is deprecated |
| 836111417 | `component::evohome::issues::deprecated_controller_service::description` | The `{service}` action without `entity_id` is deprecated and will stop working in Home Assistant {breaks_in_ha_version}. Update any automation or script to include `entity_id`, targeting the controller's climate entity. |
| 836111416 | `component::evohome::exceptions::entity_not_found::message` | The specified entity `{entity_id}` could not be found |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
