# Home Assistant Core – historisk avstämning 19921–20040

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 91 direkta källtexter matchar HA Core-källan; 21 referensanvändningar med 14 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 8 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 19921 | 836100409 | `component::victron_gx::entity::number::system_ac_power_set_point::name` | AC power setpoint | AC-effekt börvärde | Core-literal match |
| 19922 | 836100408 | `component::victron_gx::entity::number::system_ac_input_limit::name` | AC input limit | AC-ingångsgräns | Core-literal match |
| 19923 | 836100407 | `component::victron_gx::entity::number::system_ac_export_limit::name` | AC export limit | AC-exportgräns | Core-literal match |
| 19924 | 836100406 | `component::victron_gx::entity::number::switch_output_dimming::name` | Dimming | Dimning | Core-literal match |
| 19925 | 836100405 | `component::victron_gx::entity::number::multiplus_assist_current_boost_factor::name` | Assist current boost factor | Assistansströms boostfaktor | Core-literal match |
| 19926 | 836100404 | `component::victron_gx::entity::number::multi_shore_current_limit::name` | Shore current limit | Gräns för landström | Core-literal match |
| 19927 | 836100403 | `component::victron_gx::entity::number::multi_ess_min_soc_limit::name` | ESS minimum SoC limit | ESS minsta SoC-gräns | Core-literal match |
| 19928 | 836100402 | `component::victron_gx::entity::number::multi_ess_ac_power_setpoint::name` | ESS AC power setpoint | ESS AC-effekt börvärde | Source-path follow-up open |
| 19929 | 836100401 | `component::victron_gx::entity::number::hub4_ac_grid_setpoint::name` | AC grid setpoint | AC-elnätsbörvärde | Core-literal match |
| 19930 | 836100400 | `component::victron_gx::entity::number::generator_gen_id_warm_up_timer::name` | Generator warm-up timer | Generator uppvärmningstimer | Core-literal match |
| 19931 | 836100399 | `component::victron_gx::entity::number::generator_gen_id_stop_on_voltage_timer::name` | Generator stop on voltage timer | Generator stopp vid spänning timer | Core-literal match |
| 19932 | 836100398 | `component::victron_gx::entity::number::generator_gen_id_stop_on_voltage::name` | Generator stop on voltage | Generator stopp vid spänning | Core-literal match |
| 19933 | 836100397 | `component::victron_gx::entity::number::generator_gen_id_stop_on_temp_timer::name` | Generator stop on temp timer | Generator stopp på temperatur timer | Core-literal match |
| 19934 | 836100396 | `component::victron_gx::entity::number::generator_gen_id_stop_on_soc_timer::name` | Generator stop on SoC timer | Generator stopp på SoC timer | Core-literal match |
| 19935 | 836100395 | `component::victron_gx::entity::number::generator_gen_id_stop_on_soc::name` | Generator stop on SoC | Generator stopp på SoC | Core-literal match |
| 19936 | 836100394 | `component::victron_gx::entity::number::generator_gen_id_start_on_voltage_timer::name` | Generator start on voltage timer | Generator start vid spänning timer | Core-literal match |
| 19937 | 836100393 | `component::victron_gx::entity::number::generator_gen_id_start_on_voltage::name` | Generator start on voltage | Generator start vid spänning | Core-literal match |
| 19938 | 836100392 | `component::victron_gx::entity::number::generator_gen_id_start_on_temp_timer::name` | Generator start on temp timer | Generator start på temperatur timer | Core-literal match |
| 19939 | 836100391 | `component::victron_gx::entity::number::generator_gen_id_start_on_soc_timer::name` | Generator start on SoC timer | Generator start på SoC timer | Core-literal match |
| 19940 | 836100390 | `component::victron_gx::entity::number::generator_gen_id_start_on_soc::name` | Generator start on SoC | Generator start på SoC | Core-literal match |
| 19941 | 836100389 | `component::victron_gx::entity::number::generator_gen_id_shut_down_timer::name` | Generator shutdown timer | Generator avstängningstimer | Core-literal match |
| 19942 | 836100388 | `component::victron_gx::entity::number::generator_gen_id_service_interval::name` | Generator service interval | Generator serviceintervall | Core-literal match |
| 19943 | 836100387 | `component::victron_gx::entity::number::generator_gen_id_qh_stop_on_voltage::name` | Generator QH stop on voltage | Generator QH stopp vid spänning | Core-literal match |
| 19944 | 836100386 | `component::victron_gx::entity::number::generator_gen_id_qh_stop_on_soc::name` | Generator QH stop on SoC | Generator QH stopp på SoC | Core-literal match |
| 19945 | 836100385 | `component::victron_gx::entity::number::generator_gen_id_qh_start_on_voltage::name` | Generator QH start on voltage | Generator QH start vid spänning | Core-literal match |
| 19946 | 836100384 | `component::victron_gx::entity::number::generator_gen_id_qh_start_on_soc::name` | Generator QH start on SoC | Generator QH start på SoC | Core-literal match |
| 19947 | 836100383 | `component::victron_gx::entity::number::generator_gen_id_cool_down_timer::name` | Generator cooldown timer | Generator nedkylningstimer | Core-literal match |
| 19948 | 836100382 | `component::victron_gx::entity::number::evcharger_set_current::name` | Charge current setpoint | Börvärde för laddningsström | Core-literal match |
| 19949 | 836100381 | `component::victron_gx::entity::number::alternator_charge_current_limit::name` | Charge current limit | Gräns för laddström | Shared reference target checked |
| 19950 | 836099641 | `component::russound_rio::selector::connection_type::options::tcp` | TCP/IP | TCP/IP | Core-literal match |
| 19951 | 836099640 | `component::russound_rio::selector::connection_type::options::serial` | Serial/USB | Seriell/USB | Core-literal match |
| 19952 | 836099639 | `component::russound_rio::config::step::user::description` | Choose how your controller is connected. All Russound RIO devices support connection over TCP/IP. Some older controllers can connected using USB-to-serial controllers for stability if the serial port has been configured for Russound RIO. | Välj hur din kontroller är ansluten. Alla Russound RIO-enheter stöder anslutning över TCP/IP. Vissa äldre kontroller kan anslutas med USB-till-seriell-kontroller för stabilitet om serieporten har konfigurerats för Russound RIO. | Core-literal match |
| 19953 | 836099638 | `component::russound_rio::config::step::user::data_description::type` | Select how your Russound controller is connected. | Välj hur din Russound-kontroller är ansluten. | Core-literal match |
| 19954 | 836099637 | `component::russound_rio::config::step::user::data::type` | Connection type | Anslutningstyp | Core-literal match |
| 19955 | 836099636 | `component::russound_rio::config::step::tcp::data_description::port` | The port of the Russound controller. | Porten på Russound-kontrollern. | Core-literal match |
| 19956 | 836099635 | `component::russound_rio::config::step::tcp::data_description::host` | The IP address of the Russound controller. | IP-adressen för Russound-kontrollern. | Core-literal match |
| 19957 | 836099634 | `component::russound_rio::config::step::tcp::data::port` | Port | Port | Shared reference target checked |
| 19958 | 836099633 | `component::russound_rio::config::step::tcp::data::name` | Name | Namn | Shared reference target checked |
| 19959 | 836099632 | `component::russound_rio::config::step::tcp::data::host` | Host | Värd | Shared reference target checked |
| 19960 | 836099631 | `component::russound_rio::config::step::serial::data_description::device` | Choose the serial port connected to your device. | Välj den seriella port som är ansluten till din enhet. | Core-literal match |
| 19961 | 836099630 | `component::russound_rio::config::step::serial::data_description::baudrate` | The communication speed of the serial connection. | Överföringshastigheten för den seriella anslutningen. | Core-literal match |
| 19962 | 836099629 | `component::russound_rio::config::step::serial::data::device` | Device | Enhet | Core-literal match |
| 19963 | 836099628 | `component::russound_rio::config::step::serial::data::baudrate` | Baud rate | Baudfrekvens | Core-literal match |
| 19964 | 835515726 | `component::glances::entity::sensor::disk_size::name` | {sensor_label} disk size | {sensor_label} diskstorlek | Core-literal match |
| 19965 | 835490950 | `component::switchbot::entity::sensor::battery_range::state::medium` | Medium | Medel | Shared reference target checked |
| 19966 | 835490949 | `component::switchbot::entity::sensor::battery_range::state::low` | Low | Låg | Shared reference target checked |
| 19967 | 835490948 | `component::switchbot::entity::sensor::battery_range::state::high` | High | Hög | Shared reference target checked |
| 19968 | 835490947 | `component::switchbot::entity::sensor::battery_range::state::critical` | Critical | Kritisk | Core-literal match |
| 19969 | 835490946 | `component::switchbot::entity::sensor::battery_range::name` | Battery range | Batteriräckvidd | Core-literal match |
| 19970 | 835489502 | `component::denon_rs232::selector::model::options` | Other | Annat | Source-path follow-up open |
| 19971 | 835489501 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::xm` | XM | XM | Core-literal match |
| 19972 | 835489500 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::vdp` | VDP | VDP | Core-literal match |
| 19973 | 835489499 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::vcr_3` | VCR 3 | VCR 3 | Core-literal match |
| 19974 | 835489498 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::vcr_2` | VCR 2 | VCR 2 | Core-literal match |
| 19975 | 835489497 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::vcr_1` | VCR 1 | VCR 1 | Core-literal match |
| 19976 | 835489496 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::v_aux` | V. Aux | V. Aux | Core-literal match |
| 19977 | 835489495 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::usb_ipod` | USB/iPod | USB/iPod | Core-literal match |
| 19978 | 835489494 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::tv_cbl` | TV/Cable | TV/Kabel | Core-literal match |
| 19979 | 835489493 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::tv` | TV Audio | TV-ljud | Core-literal match |
| 19980 | 835489492 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::tuner` | Tuner | Radio | Core-literal match |
| 19981 | 835489491 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::spotify` | Spotify | Spotify | Core-literal match |
| 19982 | 835489490 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::siriusxm` | SiriusXM | SiriusXM | Core-literal match |
| 19983 | 835489489 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::sirius` | Sirius | Sirius | Core-literal match |
| 19984 | 835489488 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::server` | Server | Server | Core-literal match |
| 19985 | 835489487 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::sat_cbl` | Satellite/Cable | Satellit/kabel | Core-literal match |
| 19986 | 835489486 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::sat` | Sat | Sat | Core-literal match |
| 19987 | 835489485 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::phono` | Phono | Phono | Core-literal match |
| 19988 | 835489484 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::pandora` | Pandora | Pandora | Core-literal match |
| 19989 | 835489483 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::net_usb` | Network/USB | Nätverk/USB | Core-literal match |
| 19990 | 835489482 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::net` | HEOS Music | HEOS Music | Core-literal match |
| 19991 | 835489481 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::mplay` | Media Player | Mediespelare | Core-literal match |
| 19992 | 835489480 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::md_tape2` | MD/Tape 2 | MD/Tape 2 | Core-literal match |
| 19993 | 835489479 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::lastfm` | Last.fm | Last.fm | Core-literal match |
| 19994 | 835489478 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::iradio` | Internet Radio | Internetradio | Core-literal match |
| 19995 | 835489477 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::ipod` | iPod | iPod | Core-literal match |
| 19996 | 835489476 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::hdradio` | HD Radio | HD Radio | Core-literal match |
| 19997 | 835489475 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::hdp` | HDP | HDP | Core-literal match |
| 19998 | 835489474 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::game` | Game | Spel | Core-literal match |
| 19999 | 835489473 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::flickr` | Flickr | Flickr | Core-literal match |
| 20000 | 835489472 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::favorites` | Favorites | Favoriter | Core-literal match |
| 20001 | 835489471 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::eight_k` | 8K | 8K | Core-literal match |
| 20002 | 835489470 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::dvr` | DVR | DVR | Core-literal match |
| 20003 | 835489469 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::dvd` | DVD | DVD | Core-literal match |
| 20004 | 835489468 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::dock` | Dock | Dock | Core-literal match |
| 20005 | 835489467 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::dbs_sat` | DBS/Sat | DBS/Sat | Core-literal match |
| 20006 | 835489466 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::dab` | DAB | DAB | Core-literal match |
| 20007 | 835489465 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::cdr_tape1` | CDR/Tape 1 | CDR/Tape 1 | Core-literal match |
| 20008 | 835489464 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::cd` | CD | CD | Core-literal match |
| 20009 | 835489463 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::bt` | Bluetooth | Bluetooth | Core-literal match |
| 20010 | 835489462 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::bd` | BD Player | BD Player | Core-literal match |
| 20011 | 835489461 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::aux2` | Aux 2 | Aux 2 | Core-literal match |
| 20012 | 835489460 | `component::denon_rs232::entity::media_player::receiver::state_attributes::source::state::aux1` | Aux 1 | Aux 1 | Core-literal match |
| 20013 | 835489459 | `component::denon_rs232::config::step::user::data_description::model` | Determines available features | Bestämmer tillgängliga funktioner | Core-literal match |
| 20014 | 835489458 | `component::denon_rs232::config::step::user::data_description::device` | Serial port path to connect to | Sökväg till den serieport som ska användas för anslutning | Core-literal match |
| 20015 | 835489457 | `component::denon_rs232::config::step::user::data::model` | Receiver model | Receivermodell | Core-literal match |
| 20016 | 835489456 | `component::denon_rs232::config::step::user::data::device` | Port | Port | Shared reference target checked |
| 20017 | 835489455 | `component::denon_rs232::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 20018 | 835489454 | `component::denon_rs232::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 20019 | 835489453 | `component::denon_rs232::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 20020 | 835432132 | `component::motion::conditions::is_not_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20021 | 835432131 | `component::motion::conditions::is_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20022 | 835432130 | `component::motion::common::condition_for_name` | For at least | I minst | Core-literal match |
| 20023 | 835420983 | `component::evohome::issues::deprecated_reset_system_service::title` | Evohome 'Reset system' action is deprecated | Funktionen ”Reset system” i Evohome är utfasad | Source-path follow-up open |
| 20024 | 835420982 | `component::evohome::issues::deprecated_reset_system_service::description` | The `reset_system` action is deprecated and will stop working in Home Assistant {breaks_in_ha_version}. Use the system's Reset button instead. | Åtgärden `reset_system` är utfasad och kommer att sluta fungera i Home Assistant {breaks_in_ha_version}. Använd istället systemets återställningsknapp. | Source-path follow-up open |
| 20025 | 835420981 | `component::evohome::issues::deprecated_preset_reset::title` | Evohome Reset preset is deprecated | Förinställningen ”Evohome Reset” är utfasad | Source-path follow-up open |
| 20026 | 835420980 | `component::evohome::issues::deprecated_preset_reset::description` | Using the `Reset` preset on an Evohome controller is deprecated and will stop working in Home Assistant {breaks_in_ha_version}. Use the system's Reset button instead. | Att använda förinställningen `Reset` på en Evohome-styrenhet är utfasat och kommer att sluta fungera i Home Assistant {breaks_in_ha_version}. Använd istället systemets återställningsknapp. | Source-path follow-up open |
| 20027 | 835420979 | `component::evohome::issues::deprecated_clear_zone_override_service::title` | Evohome 'Clear zone override' action is deprecated | Funktionen ”Clear zone override” i Evohome är utfasad | Source-path follow-up open |
| 20028 | 835420978 | `component::evohome::issues::deprecated_clear_zone_override_service::description` | The `clear_zone_override` action is deprecated and will stop working in Home Assistant {breaks_in_ha_version}. Use the zone's Reset button instead. | Åtgärden `clear_zone_override` är utfasad och kommer att sluta fungera i Home Assistant {breaks_in_ha_version}. Använd zonens återställningsknapp istället. | Source-path follow-up open |
| 20029 | 835336009 | `component::weheat::entity::sensor::electricity_used_standby::name` | Electricity used standby | Elförbrukning i standby | Core-literal match |
| 20030 | 834983039 | `component::window::triggers::opened::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20031 | 834983038 | `component::window::triggers::closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20032 | 834983037 | `component::window::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20033 | 834983036 | `component::water_heater::triggers::turned_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20034 | 834983035 | `component::water_heater::triggers::turned_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20035 | 834983034 | `component::water_heater::triggers::target_temperature_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20036 | 834983033 | `component::water_heater::triggers::operation_mode_changed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20037 | 834983032 | `component::water_heater::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20038 | 834983031 | `component::valve::triggers::opened::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20039 | 834983030 | `component::valve::triggers::closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20040 | 834983029 | `component::valve::common::trigger_for_name` | For at least | I minst | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 836100402 | `component::victron_gx::entity::number::multi_ess_ac_power_setpoint::name` | ESS AC power setpoint |
| 835489502 | `component::denon_rs232::selector::model::options` | Other |
| 835420983 | `component::evohome::issues::deprecated_reset_system_service::title` | Evohome 'Reset system' action is deprecated |
| 835420982 | `component::evohome::issues::deprecated_reset_system_service::description` | The `reset_system` action is deprecated and will stop working in Home Assistant {breaks_in_ha_version}. Use the system's Reset button instead. |
| 835420981 | `component::evohome::issues::deprecated_preset_reset::title` | Evohome Reset preset is deprecated |
| 835420980 | `component::evohome::issues::deprecated_preset_reset::description` | Using the `Reset` preset on an Evohome controller is deprecated and will stop working in Home Assistant {breaks_in_ha_version}. Use the system's Reset button instead. |
| 835420979 | `component::evohome::issues::deprecated_clear_zone_override_service::title` | Evohome 'Clear zone override' action is deprecated |
| 835420978 | `component::evohome::issues::deprecated_clear_zone_override_service::description` | The `clear_zone_override` action is deprecated and will stop working in Home Assistant {breaks_in_ha_version}. Use the zone's Reset button instead. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
