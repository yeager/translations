# Home Assistant Core – historisk avstämning 20761–20880

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 52 direkta källtexter matchar HA Core-källan; 36 referensanvändningar med 33 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 32 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 20761 | 829920978 | `component::victron_gx::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 20762 | 829920977 | `component::victron_gx::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 20763 | 829838273 | `component::mystrom::config::step::discovery_confirm::description` | Do you want to set up the myStrom device at {host}? | Vill du konfigurera myStrom-enheten på {host}? | Core-literal match |
| 20764 | 829838272 | `component::mystrom::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 20765 | 829586944 | `component::openai_conversation::config_subentries::conversation::step::advanced::data_description::store_responses` | If enabled, requests and responses are stored by OpenAI and visible in your OpenAI dashboard logs | Om aktiverat lagras förfrågningar och svar av OpenAI och syns i dina OpenAI-kontrollpanelloggar | Source-path follow-up open |
| 20766 | 829586943 | `component::openai_conversation::config_subentries::conversation::step::advanced::data::store_responses` | Store requests and responses in OpenAI | Lagra förfrågningar och svar i OpenAI | Source-path follow-up open |
| 20767 | 829586942 | `component::openai_conversation::config_subentries::ai_task_data::step::advanced::data_description::store_responses` | If enabled, requests and responses are stored by OpenAI and visible in your OpenAI dashboard logs | Om aktiverat lagras förfrågningar och svar av OpenAI och syns i dina OpenAI-kontrollpanelloggar | Source-path follow-up open |
| 20768 | 829586941 | `component::openai_conversation::config_subentries::ai_task_data::step::advanced::data::store_responses` | Store requests and responses in OpenAI | Lagra förfrågningar och svar i OpenAI | Source-path follow-up open |
| 20769 | 829586605 | `component::music_assistant::entity::number::treble::name` | Treble | Diskant | Core-literal match |
| 20770 | 829586604 | `component::music_assistant::entity::number::subwoofer_volume::name` | Subwoofer volume | Subwoofer-volym | Core-literal match |
| 20771 | 829586603 | `component::music_assistant::entity::number::equalizer_mid::name` | Equalizer mid | Equalizer mid | Core-literal match |
| 20772 | 829586602 | `component::music_assistant::entity::number::equalizer_low::name` | Equalizer low | Equalizer låg | Core-literal match |
| 20773 | 829586601 | `component::music_assistant::entity::number::equalizer_high::name` | Equalizer high | Equalizer hög | Core-literal match |
| 20774 | 829586600 | `component::music_assistant::entity::number::dts_dialogue_control::name` | DTS dialogue control | DTS-dialogkontroll | Core-literal match |
| 20775 | 829586599 | `component::music_assistant::entity::number::dialogue_lift::name` | Dialogue lift | Dialoglyft | Core-literal match |
| 20776 | 829586598 | `component::music_assistant::entity::number::dialogue_level::name` | Dialogue level | Dialognivå | Core-literal match |
| 20777 | 829586597 | `component::music_assistant::entity::number::bass::name` | Bass | Bas | Core-literal match |
| 20778 | 829576893 | `component::gardena_bluetooth::entity::text::position_name::name` | Position {number} | Position {number} | Core-literal match |
| 20779 | 829576892 | `component::gardena_bluetooth::entity::text::contour_name::name` | Contour {number} | Kontur {number} | Core-literal match |
| 20780 | 829394272 | `component::switchbot::entity::button::light_sensor::name` | Light sensor | Ljussensor | Core-literal match |
| 20781 | 828789998 | `component::victron_gx::entity::binary_sensor::vebus_inverter_setting_alarm_grid_lost::name` | Grid lost alarm setting | Inställning för larm vid förlorat elnät | Source-path follow-up open |
| 20782 | 828789997 | `component::victron_gx::entity::binary_sensor::vebus_inverter_ignoreacin1_onoff_control::name` | Control ignore AC-in-1 | Kontroll ignorera AC-in-1 | Source-path follow-up open |
| 20783 | 828789996 | `component::victron_gx::entity::binary_sensor::vebus_inverter_connected::name` | Connected | Ansluten | Shared reference target checked |
| 20784 | 828789995 | `component::victron_gx::entity::binary_sensor::vebus_device_device_number_power_assist_enabled::name` | {device_number} PowerAssist enabled | {device_number} PowerAssist aktiverat | Source-path follow-up open |
| 20785 | 828789994 | `component::victron_gx::entity::binary_sensor::system_settings_overvoltage_feedin::name` | PV DC overvoltage feed-in | PV DC-överspänning feed-in | Source-path follow-up open |
| 20786 | 828789993 | `component::victron_gx::entity::binary_sensor::system_relay_relay::name` | Relay {relay} state | Relä {relay} tillstånd | Source-path follow-up open |
| 20787 | 828789992 | `component::victron_gx::entity::binary_sensor::system_ess_schedule_charge_slot_enabled::name` | ESS BatteryLife schedule charge {slot} enabled | ESS BatteryLife schemalagd laddning {slot} aktiverad | Source-path follow-up open |
| 20788 | 828789991 | `component::victron_gx::entity::binary_sensor::system_ess_battery_use::name` | ESS only critical loads from battery | ESS endast kritiska belastningar från batteri | Source-path follow-up open |
| 20789 | 828789990 | `component::victron_gx::entity::binary_sensor::system_dynamicess_available::name` | Dynamic ESS available | Dynamisk ESS tillgänglig | Core-literal match |
| 20790 | 828789989 | `component::victron_gx::entity::binary_sensor::system_dynamicess_allow_gridfeedin::name` | Dynamic ESS allow grid feed-in | Dynamisk ESS tillåter feed-in | Core-literal match |
| 20791 | 828789988 | `component::victron_gx::entity::binary_sensor::system_dynamicess_active::name` | Dynamic ESS active | Dynamisk ESS aktiv | Core-literal match |
| 20792 | 828789987 | `component::victron_gx::entity::binary_sensor::switchable_output_output_state::name` | Switchable output {output} state | Omkopplingsbar utgång {output} tillstånd | Source-path follow-up open |
| 20793 | 828789986 | `component::victron_gx::entity::binary_sensor::switch_output_state::name` | State | Tillstånd | Shared reference target checked |
| 20794 | 828789985 | `component::victron_gx::entity::binary_sensor::solarcharger_relay_state::name` | Relay state | Relätillstånd | Source-path follow-up open |
| 20795 | 828789984 | `component::victron_gx::entity::binary_sensor::solarcharger_mode::name` | Mode | Läge | Source-path follow-up open |
| 20796 | 828789983 | `component::victron_gx::entity::binary_sensor::solarcharger_load_state::name` | Load state | Laststatus | Core-literal match |
| 20797 | 828789982 | `component::victron_gx::entity::binary_sensor::multi_relay0_state::name` | Relay on Multi RS state | Relä på Multi RS-läge | Source-path follow-up open |
| 20798 | 828789981 | `component::victron_gx::entity::binary_sensor::multi_disable_feed_in::name` | ESS disable feed-in | ESS inaktivera feed-in | Source-path follow-up open |
| 20799 | 828789980 | `component::victron_gx::entity::binary_sensor::multi_disable_charge::name` | ESS disable charge | ESS inaktivera laddning | Source-path follow-up open |
| 20800 | 828789979 | `component::victron_gx::entity::binary_sensor::inverter_alarm_ripple::name` | Ripple alarm | Rippellarm | Shared reference target checked |
| 20801 | 828789978 | `component::victron_gx::entity::binary_sensor::inverter_alarm_overload::name` | Overload alarm | Överbelastningslarm | Shared reference target checked |
| 20802 | 828789977 | `component::victron_gx::entity::binary_sensor::inverter_alarm_low_voltage_ac_out::name` | Low voltage AC-out alarm | Larm för lågspänning AC-utgång | Core-literal match |
| 20803 | 828789976 | `component::victron_gx::entity::binary_sensor::inverter_alarm_low_voltage::name` | Low voltage alarm | Larm för lågspänning | Core-literal match |
| 20804 | 828789975 | `component::victron_gx::entity::binary_sensor::inverter_alarm_low_temperature::name` | Low temperature alarm | Larm för låg temperatur | Core-literal match |
| 20805 | 828789974 | `component::victron_gx::entity::binary_sensor::inverter_alarm_high_voltage_ac_out::name` | High voltage AC-out alarm | Larm för högspänning AC-utgång | Core-literal match |
| 20806 | 828789973 | `component::victron_gx::entity::binary_sensor::inverter_alarm_high_voltage::name` | High voltage alarm | Larm för högspänning | Core-literal match |
| 20807 | 828789972 | `component::victron_gx::entity::binary_sensor::inverter_alarm_high_temperature::name` | High temperature alarm | Larm för hög temperatur | Shared reference target checked |
| 20808 | 828789971 | `component::victron_gx::entity::binary_sensor::gps_fix::name` | Fix | Fix | Source-path follow-up open |
| 20809 | 828789970 | `component::victron_gx::entity::binary_sensor::gps_connected::name` | Connected | Ansluten | Shared reference target checked |
| 20810 | 828789969 | `component::victron_gx::entity::binary_sensor::generator_manual_start::name` | Manual start | Manuell start | Source-path follow-up open |
| 20811 | 828789968 | `component::victron_gx::entity::binary_sensor::generator_gen_id_start_on_voltage_enabled::name` | Generator start on voltage enabled | Generator start vid spänning aktiverat | Source-path follow-up open |
| 20812 | 828789967 | `component::victron_gx::entity::binary_sensor::generator_gen_id_start_on_temp_enabled::name` | Generator start on high temp enabled | Generator start vid hög temperatur aktiverat | Source-path follow-up open |
| 20813 | 828789966 | `component::victron_gx::entity::binary_sensor::generator_gen_id_start_on_soc_enabled::name` | Generator start on SOC enabled | Generator start på SOC aktiverat | Source-path follow-up open |
| 20814 | 828789965 | `component::victron_gx::entity::binary_sensor::generator_gen_id_quiet_hours_enabled::name` | Generator quiet hours enabled | Generator tysta timmar aktiverat | Source-path follow-up open |
| 20815 | 828789964 | `component::victron_gx::entity::binary_sensor::generator_autorun::name` | Auto-start enabled | Autostart aktiverat | Source-path follow-up open |
| 20816 | 828789963 | `component::victron_gx::entity::binary_sensor::evcharger_connected::name` | Connected | Ansluten | Shared reference target checked |
| 20817 | 828789962 | `component::victron_gx::entity::binary_sensor::evcharger_charge::name` | EV charging | Elbil laddar | Source-path follow-up open |
| 20818 | 828789961 | `component::victron_gx::entity::binary_sensor::digitalinput_settings_invert_translation::name` | Invert digital input | Inverter digital ingång | Source-path follow-up open |
| 20819 | 828789960 | `component::victron_gx::entity::binary_sensor::dcdc_mode::name` | Mode | Läge | Source-path follow-up open |
| 20820 | 828789959 | `component::victron_gx::entity::binary_sensor::alternator_mode::name` | Mode | Läge | Source-path follow-up open |
| 20821 | 828778764 | `component::incomfort::entity::water_heater::boiler::state::starting_ch` | Starting central heating | Centralvärme startar | Core-literal match |
| 20822 | 828778763 | `component::incomfort::entity::water_heater::boiler::state::hp_error_recovery` | Heat pump error recovery | Återställning av fel på värmepump | Core-literal match |
| 20823 | 828778762 | `component::incomfort::entity::water_heater::boiler::state::central_heating_wait` | Central heating waiting | Centralvärme väntar | Core-literal match |
| 20824 | 828773677 | `component::roborock::options::step::drawables::data_description::show_walls` | Show the walls on the map. | Visa väggarna på kartan. | Core-literal match |
| 20825 | 828773676 | `component::roborock::options::step::drawables::data_description::show_rooms` | Show the rooms on the map. | Visa rummen på kartan. | Core-literal match |
| 20826 | 828773675 | `component::roborock::options::step::drawables::data::show_walls` | Show walls | Visa väggar | Core-literal match |
| 20827 | 828773674 | `component::roborock::options::step::drawables::data::show_rooms` | Show rooms | Visa rum | Core-literal match |
| 20828 | 828765849 | `component::tado::config::abort::api_rate_limit_reached` | Tado API rate limit reached. Please wait and try again later. | Gränsen för Tado API har nåtts. Vänta ett tag och försök igen senare. | Core-literal match |
| 20829 | 828761434 | `component::roborock::entity::sensor::vacuum_error::state::water_carriage_drop` | Water carriage dropped | Vattennivån sjönk | Core-literal match |
| 20830 | 828761433 | `component::roborock::entity::sensor::vacuum_error::state::up_water_exception` | Water supply exception | Undantag för vattenförsörjning | Core-literal match |
| 20831 | 828761432 | `component::roborock::entity::sensor::vacuum_error::state::optical_flow_sensor_dirt` | Optical flow sensor dirty | Optisk flödessensor smutsig | Core-literal match |
| 20832 | 828761431 | `component::roborock::entity::sensor::vacuum_error::state::drain_water_exception` | Drain water exception | Undantag för dräneringsvatten | Core-literal match |
| 20833 | 828761430 | `component::roborock::entity::sensor::vacuum_error::state::clean_carousel_water_full` | Cleaning carousel water full | Rengöringskarusell vatten fullt | Core-literal match |
| 20834 | 828761429 | `component::roborock::entity::sensor::vacuum_error::state::clean_carousel_exception` | Cleaning carousel error | Fel på rengöringskarusell | Core-literal match |
| 20835 | 828761428 | `component::roborock::entity::sensor::vacuum_error::state::check_clean_carouse` | Check the cleaning carousel | Kontrollera rengöringskarusellen | Core-literal match |
| 20836 | 828761427 | `component::roborock::entity::sensor::vacuum_error::state::audio_error` | Audio error | Ljudfel | Core-literal match |
| 20837 | 828761426 | `component::roborock::entity::sensor::status::state::waiting_to_charge` | Waiting to charge | Väntar på att ladda | Core-literal match |
| 20838 | 828761425 | `component::roborock::entity::sensor::status::state::transitioning` | Transitioning | Övergång | Core-literal match |
| 20839 | 828761424 | `component::roborock::entity::sensor::status::state::sweeping` | Sweeping | Sopar | Core-literal match |
| 20840 | 828761423 | `component::roborock::entity::sensor::status::state::sweep_and_mop` | Sweep and mop | Sopar och moppar | Core-literal match |
| 20841 | 828761422 | `component::roborock::entity::sensor::status::state::sleeping` | Sleeping | Sover | Core-literal match |
| 20842 | 828761421 | `component::roborock::entity::sensor::status::state::saving_map` | Saving map | Sparar karta | Core-literal match |
| 20843 | 828761420 | `component::roborock::entity::sensor::status::state::relocating` | Relocating | Flyttar | Core-literal match |
| 20844 | 828761419 | `component::roborock::entity::sensor::status::state::mopping` | Mopping | Moppar | Core-literal match |
| 20845 | 828761418 | `component::roborock::entity::sensor::side_brush_life::name` | Side brush time used | Använd tid sidoborste | Core-literal match |
| 20846 | 828761417 | `component::roborock::entity::sensor::sensor_life::name` | Sensor time used | Använd tid sensor | Core-literal match |
| 20847 | 828761416 | `component::roborock::entity::sensor::main_brush_life::name` | Main brush time used | Använd tid huvudborste | Core-literal match |
| 20848 | 828761415 | `component::roborock::entity::sensor::filter_life::name` | Filter time used | Använd tid filter | Core-literal match |
| 20849 | 828748597 | `component::casper_glow::entity::sensor::dimming_end_time::name` | Dimming end time | Sluttid för dimning | Core-literal match |
| 20850 | 828726881 | `component::proxmoxve::entity::button::resume_all::name` | Resume | Återuppta | Source-path follow-up open |
| 20851 | 828726677 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::sustain_alt` | Sustain alt | Sustain alt | Shared reference target checked |
| 20852 | 828726676 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::sustain` | Sustain | Sustain | Shared reference target checked |
| 20853 | 828726675 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::storage` | Storage | Lagring | Shared reference target checked |
| 20854 | 828726674 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::starting_up` | Starting up | Startar upp | Shared reference target checked |
| 20855 | 828726673 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::scheduled_recharging` | Scheduled recharging | Schemalagd uppladdning | Shared reference target checked |
| 20856 | 828726672 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::repeated_absorption` | Repeated absorption | Upprepad absorption | Shared reference target checked |
| 20857 | 828726671 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::recharging` | Recharging | Uppladdar | Shared reference target checked |
| 20858 | 828726670 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::power_supply` | Power supply | Strömförsörjning | Shared reference target checked |
| 20859 | 828726669 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::power_assist` | Power Assist | Power Assist | Shared reference target checked |
| 20860 | 828726668 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::passthrough` | Passthrough | Genomströmning | Shared reference target checked |
| 20861 | 828726667 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::off` | Off | Av | Shared reference target checked |
| 20862 | 828726666 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::low_power` | Low power | Låg ström | Shared reference target checked |
| 20863 | 828726665 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::inverting` | Inverting | Växelriktar | Shared reference target checked |
| 20864 | 828726664 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::float` | Float | Flytande | Shared reference target checked |
| 20865 | 828726663 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::fault` | Fault | Fel | Shared reference target checked |
| 20866 | 828726662 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::external_control` | External control | Extern styrning | Shared reference target checked |
| 20867 | 828726661 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::equalize` | Equalize | Utjämna | Shared reference target checked |
| 20868 | 828726660 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::discharging` | Discharging | Laddar ur | Shared reference target checked |
| 20869 | 828726659 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::bulk` | Bulk | Bulk | Shared reference target checked |
| 20870 | 828726658 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::battery_safe` | Battery Safe | Batteri säkert | Shared reference target checked |
| 20871 | 828726657 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::auto_equalize` | Auto equalize / recondition | Automatisk utjämning/rekonditionering | Shared reference target checked |
| 20872 | 828726656 | `component::victron_gx::entity::sensor::vebus_inverter_state::state::absorption` | Absorption | Absorption | Shared reference target checked |
| 20873 | 828726655 | `component::victron_gx::entity::sensor::vebus_inverter_state::name` | State | Tillstånd | Shared reference target checked |
| 20874 | 828726654 | `component::victron_gx::entity::sensor::vebus_inverter_output_voltage_phase::name` | Output voltage {phase} | Utgångsspänning {phase} | Shared reference target checked |
| 20875 | 828726653 | `component::victron_gx::entity::sensor::vebus_inverter_output_power_phase::name` | Output power {phase} | Utgångseffekt {phase} | Shared reference target checked |
| 20876 | 828726652 | `component::victron_gx::entity::sensor::vebus_inverter_output_frequency_phase::name` | Output frequency {phase} | Utgångsfrekvens {phase} | Core-literal match |
| 20877 | 828726651 | `component::victron_gx::entity::sensor::vebus_inverter_output_current_phase::name` | Output current {phase} | Utgångsström {phase} | Shared reference target checked |
| 20878 | 828726650 | `component::victron_gx::entity::sensor::vebus_inverter_output_apparent_power_phase::name` | Output apparent power {phase} | Skenbar utgångseffekt {phase} | Shared reference target checked |
| 20879 | 828726649 | `component::victron_gx::entity::sensor::vebus_inverter_mode::state::on` | On | På | Source-path follow-up open |
| 20880 | 828726648 | `component::victron_gx::entity::sensor::vebus_inverter_mode::state::off` | Off | Av | Source-path follow-up open |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 829920977 | `component::victron_gx::config::abort::reauth_successful` | Re-authentication was successful |
| 829586944 | `component::openai_conversation::config_subentries::conversation::step::advanced::data_description::store_responses` | If enabled, requests and responses are stored by OpenAI and visible in your OpenAI dashboard logs |
| 829586943 | `component::openai_conversation::config_subentries::conversation::step::advanced::data::store_responses` | Store requests and responses in OpenAI |
| 829586942 | `component::openai_conversation::config_subentries::ai_task_data::step::advanced::data_description::store_responses` | If enabled, requests and responses are stored by OpenAI and visible in your OpenAI dashboard logs |
| 829586941 | `component::openai_conversation::config_subentries::ai_task_data::step::advanced::data::store_responses` | Store requests and responses in OpenAI |
| 828789998 | `component::victron_gx::entity::binary_sensor::vebus_inverter_setting_alarm_grid_lost::name` | Grid lost alarm setting |
| 828789997 | `component::victron_gx::entity::binary_sensor::vebus_inverter_ignoreacin1_onoff_control::name` | Control ignore AC-in-1 |
| 828789995 | `component::victron_gx::entity::binary_sensor::vebus_device_device_number_power_assist_enabled::name` | {device_number} PowerAssist enabled |
| 828789994 | `component::victron_gx::entity::binary_sensor::system_settings_overvoltage_feedin::name` | PV DC overvoltage feed-in |
| 828789993 | `component::victron_gx::entity::binary_sensor::system_relay_relay::name` | Relay {relay} state |
| 828789992 | `component::victron_gx::entity::binary_sensor::system_ess_schedule_charge_slot_enabled::name` | ESS BatteryLife schedule charge {slot} enabled |
| 828789991 | `component::victron_gx::entity::binary_sensor::system_ess_battery_use::name` | ESS only critical loads from battery |
| 828789987 | `component::victron_gx::entity::binary_sensor::switchable_output_output_state::name` | Switchable output {output} state |
| 828789985 | `component::victron_gx::entity::binary_sensor::solarcharger_relay_state::name` | Relay state |
| 828789984 | `component::victron_gx::entity::binary_sensor::solarcharger_mode::name` | Mode |
| 828789982 | `component::victron_gx::entity::binary_sensor::multi_relay0_state::name` | Relay on Multi RS state |
| 828789981 | `component::victron_gx::entity::binary_sensor::multi_disable_feed_in::name` | ESS disable feed-in |
| 828789980 | `component::victron_gx::entity::binary_sensor::multi_disable_charge::name` | ESS disable charge |
| 828789971 | `component::victron_gx::entity::binary_sensor::gps_fix::name` | Fix |
| 828789969 | `component::victron_gx::entity::binary_sensor::generator_manual_start::name` | Manual start |
| 828789968 | `component::victron_gx::entity::binary_sensor::generator_gen_id_start_on_voltage_enabled::name` | Generator start on voltage enabled |
| 828789967 | `component::victron_gx::entity::binary_sensor::generator_gen_id_start_on_temp_enabled::name` | Generator start on high temp enabled |
| 828789966 | `component::victron_gx::entity::binary_sensor::generator_gen_id_start_on_soc_enabled::name` | Generator start on SOC enabled |
| 828789965 | `component::victron_gx::entity::binary_sensor::generator_gen_id_quiet_hours_enabled::name` | Generator quiet hours enabled |
| 828789964 | `component::victron_gx::entity::binary_sensor::generator_autorun::name` | Auto-start enabled |
| 828789962 | `component::victron_gx::entity::binary_sensor::evcharger_charge::name` | EV charging |
| 828789961 | `component::victron_gx::entity::binary_sensor::digitalinput_settings_invert_translation::name` | Invert digital input |
| 828789960 | `component::victron_gx::entity::binary_sensor::dcdc_mode::name` | Mode |
| 828789959 | `component::victron_gx::entity::binary_sensor::alternator_mode::name` | Mode |
| 828726881 | `component::proxmoxve::entity::button::resume_all::name` | Resume |
| 828726649 | `component::victron_gx::entity::sensor::vebus_inverter_mode::state::on` | On |
| 828726648 | `component::victron_gx::entity::sensor::vebus_inverter_mode::state::off` | Off |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
