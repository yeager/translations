# Home Assistant Core – historisk avstämning 20401–20520

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 91 direkta källtexter matchar HA Core-källan; 22 referensanvändningar med 19 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 7 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 20401 | 832086550 | `component::tailwind::config::step::reconfigure::data::token` | Local control key token | Lokal kontrollnyckel | Shared reference target checked |
| 20402 | 832086549 | `component::tailwind::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 20403 | 832086548 | `component::tailwind::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 20404 | 832086547 | `component::tailwind::config::abort::different_device` | The entered information is for a different Tailwind device. | Den angivna informationen gäller en annan Tailwind-enhet. | Core-literal match |
| 20405 | 831760495 | `component::twentemilieu::exceptions::unknown_error::message` | An unknown error occurred while communicating with the Twente Milieu service. | Ett okänt fel uppstod vid kommunikation med Twente Milieu-tjänsten. | Core-literal match |
| 20406 | 831760494 | `component::twentemilieu::exceptions::communication_error::message` | An error occurred while communicating with the Twente Milieu service. | Ett fel uppstod vid kommunikation med Twente Milieu-tjänsten. | Core-literal match |
| 20407 | 831760493 | `component::elgato::exceptions::unknown_error::message` | An unknown error occurred while communicating with the Elgato device. | Ett okänt fel uppstod vid kommunikation med Elgato-enheten. | Core-literal match |
| 20408 | 831760492 | `component::elgato::exceptions::communication_error::message` | An error occurred while communicating with the Elgato device. | Ett fel uppstod vid kommunikationen med Elgato-enheten. | Core-literal match |
| 20409 | 831760464 | `component::elgato::config::abort::no_devices_found` | No devices found on the network | Inga enheter hittades i nätverket | Shared reference target checked |
| 20410 | 831755438 | `component::eurotronic_cometblue::config::step::pick_device::data_description::address` | Select device to continue. | Välj enhet för att fortsätta. | Core-literal match |
| 20411 | 831755437 | `component::eurotronic_cometblue::config::step::pick_device::data::address` | Discovered devices | Upptäckta enheter | Core-literal match |
| 20412 | 831755436 | `component::eurotronic_cometblue::config::step::bluetooth_confirm::data_description::pin` | 6-digit device PIN | 6-siffrig PIN-kod för enhet | Core-literal match |
| 20413 | 831755435 | `component::eurotronic_cometblue::config::step::bluetooth_confirm::data::pin` | PIN code | PIN-kod | Shared reference target checked |
| 20414 | 831755434 | `component::eurotronic_cometblue::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 20415 | 831755433 | `component::eurotronic_cometblue::config::error::timeout_connect` | Timeout while establishing a connection | Tidsgränsen överskreds när anslutningen upprättades. | Shared reference target checked |
| 20416 | 831755432 | `component::eurotronic_cometblue::config::error::invalid_pin` | Invalid device PIN | Ogiltig PIN-kod för enhet | Core-literal match |
| 20417 | 831755431 | `component::eurotronic_cometblue::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 20418 | 831755430 | `component::eurotronic_cometblue::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 20419 | 831755429 | `component::eurotronic_cometblue::config::abort::no_devices_found` | No Comet Blue Bluetooth TRVs discovered. | Inga Comet Blue Bluetooth-termostatventiler hittades. | Core-literal match |
| 20420 | 831755428 | `component::eurotronic_cometblue::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 20421 | 831755198 | `component::waze_travel_time::services::get_travel_times::fields::base_coordinates::name` | Base coordinates | Baskoordinater | Shared reference target checked |
| 20422 | 831755197 | `component::waze_travel_time::services::get_travel_times::fields::base_coordinates::description` | When Waze finds multiple matching locations for an address, it selects the one closest to these coordinates. | När Waze hittar flera matchande platser för en adress väljer den den som ligger närmast dessa koordinater. | Shared reference target checked |
| 20423 | 831755196 | `component::waze_travel_time::options::step::init::data_description::base_coordinates` | When Waze finds multiple matching locations for an address, it selects the one closest to these coordinates. | När Waze hittar flera matchande platser för en adress väljer den den som ligger närmast dessa koordinater. | Core-literal match |
| 20424 | 831755195 | `component::waze_travel_time::options::step::init::data::base_coordinates` | Base coordinates | Baskoordinater | Core-literal match |
| 20425 | 831755078 | `component::subaru::entity::button::remote_stop::name` | Remote stop | Fjärrstopp | Core-literal match |
| 20426 | 831755077 | `component::subaru::entity::button::remote_start::name` | Remote start | Fjärrstart | Core-literal match |
| 20427 | 831732196 | `component::iaqualink::config::step::reauth_confirm::title` | Reauthenticate iAquaLink | Återautentisera iAquaLink | Core-literal match |
| 20428 | 831732195 | `component::iaqualink::config::step::reauth_confirm::description` | Please enter the username and password for your iAquaLink account. | Ange användarnamn och lösenord för ditt iAquaLink-konto. | Shared reference target checked |
| 20429 | 831732194 | `component::iaqualink::config::step::reauth_confirm::data::username` | Username | Användarnamn | Shared reference target checked |
| 20430 | 831732193 | `component::iaqualink::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 20431 | 831732192 | `component::iaqualink::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 20432 | 831702234 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::warehouse_loft` | Warehouse loft | Lagerlokal | Core-literal match |
| 20433 | 831702233 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::village_vanguard` | Village Vanguard | Village Vanguard | Core-literal match |
| 20434 | 831702232 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::village_gate` | Village Gate | Village Gate | Core-literal match |
| 20435 | 831702231 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::vienna` | Hall in Vienna | Hall i Wien | Core-literal match |
| 20436 | 831702230 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::usa_b` | Hall in USA B | Hall i USA B | Core-literal match |
| 20437 | 831702229 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::usa_a` | Hall in USA A | Hall i USA A | Core-literal match |
| 20438 | 831702228 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::tv_program` | TV program | TV-program | Core-literal match |
| 20439 | 831702227 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::tokyo` | Church in Tokyo | Kyrka i Tokyo | Core-literal match |
| 20440 | 831702226 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::target` | Target | Target | Core-literal match |
| 20441 | 831702225 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::talk_show` | Talk show | Talkshow | Core-literal match |
| 20442 | 831702224 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::surr_decoder` | Surround decoder | Surround-dekoder | Core-literal match |
| 20443 | 831702223 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::stuttgart` | Hall in Stuttgart | Hall i Stuttgart | Core-literal match |
| 20444 | 831702222 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::straight` | Straight | Rakt | Core-literal match |
| 20445 | 831702221 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::stereo` | Stereo | Stereo | Core-literal match |
| 20446 | 831702220 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::standard` | Standard | Standard | Core-literal match |
| 20447 | 831702219 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::sports` | Sports | Sport | Core-literal match |
| 20448 | 831702218 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::spectacle` | Spectacle | Skådespel | Core-literal match |
| 20449 | 831702217 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::sci-fi` | Sci-fi | Sci-fi | Core-literal match |
| 20450 | 831702216 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::royaumont` | Church in Royaumont | Kyrka i Royaumont | Core-literal match |
| 20451 | 831702215 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::roxy_theatre` | The Roxy Theatre | Roxy-teatern | Core-literal match |
| 20452 | 831702214 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::roleplaying_game` | Roleplaying game | Rollspel | Core-literal match |
| 20453 | 831702213 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::recital_opera` | Recital/opera | Konsert/opera | Core-literal match |
| 20454 | 831702212 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::pavilion` | Pavilion | Paviljong | Core-literal match |
| 20455 | 831702211 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::off` | Off | Av | Shared reference target checked |
| 20456 | 831702210 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::my_surround` | My surround | Min surround | Core-literal match |
| 20457 | 831702209 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::music_video` | Music video | Musikvideo | Core-literal match |
| 20458 | 831702208 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::music` | Music | Musik | Core-literal match |
| 20459 | 831702207 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::munich_b` | Hall in Munich B | Hall i München B | Core-literal match |
| 20460 | 831702206 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::munich_a` | Hall in Munich A | Hall i München A | Core-literal match |
| 20461 | 831702205 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::munich` | Hall in Munich | Hall i München | Core-literal match |
| 20462 | 831702204 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::movie` | Movie | Film | Core-literal match |
| 20463 | 831702203 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::mono_movie` | Mono movie | Film mono | Core-literal match |
| 20464 | 831702202 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::jazz_club` | Jazz club | Jazzklubb | Core-literal match |
| 20465 | 831702201 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::game` | Game | Spel | Core-literal match |
| 20466 | 831702200 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::freiburg` | Church in Freiburg | Kyrka i Freiburg | Core-literal match |
| 20467 | 831702199 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::frankfurt` | Hall in Frankfurt | Hall i Frankfurt | Core-literal match |
| 20468 | 831702198 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::enhanced` | Enhanced | Förbättrad | Core-literal match |
| 20469 | 831702197 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::drama` | Drama | Drama | Core-literal match |
| 20470 | 831702196 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::disco` | Disco | Disco | Core-literal match |
| 20471 | 831702195 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::concert` | Live concert | Livekonsert | Core-literal match |
| 20472 | 831702194 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::chamber` | Chamber | Kammare | Core-literal match |
| 20473 | 831702193 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::cellar_club` | Cellar club | Källarklubb | Core-literal match |
| 20474 | 831702192 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::bottom_line` | The Bottom Line | Bottom-line | Core-literal match |
| 20475 | 831702191 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::bass_booster` | Bass booster | Bas-booster | Core-literal match |
| 20476 | 831702190 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::arena` | Arena | Arena | Core-literal match |
| 20477 | 831702189 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::amsterdam` | Hall in Amsterdam | Hall i Amsterdam | Core-literal match |
| 20478 | 831702188 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::all_ch_stereo` | All ch stereo | Alla kanaler stereo | Core-literal match |
| 20479 | 831702187 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::adventure` | Adventure | Äventyr | Core-literal match |
| 20480 | 831702186 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::action_game` | Action game | Actionspel | Core-literal match |
| 20481 | 831702185 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::9ch_stereo` | 9ch stereo | 9-kanals stereo | Core-literal match |
| 20482 | 831702184 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::7ch_stereo` | 7ch stereo | 7-kanals stereo | Core-literal match |
| 20483 | 831702183 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::5ch_stereo` | 5ch stereo | 5-kanals stereo | Core-literal match |
| 20484 | 831702182 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::2ch_stereo` | 2ch stereo | 2-kanals stereo | Core-literal match |
| 20485 | 831702181 | `component::music_assistant::entity::media_player::media_player::state_attributes::sound_mode::state::11ch_stereo` | 11ch stereo | 11-kanals stereo | Core-literal match |
| 20486 | 831600256 | `component::anthropic::config_subentries::conversation::error::model_not_found` | Model not found | Modellen hittades inte | Core-literal match |
| 20487 | 831600255 | `component::anthropic::config_subentries::conversation::error::api_error` | Unable to get model info: {message} | Det gick inte att hämta modellinformation: {message} | Core-literal match |
| 20488 | 831600254 | `component::anthropic::config_subentries::ai_task_data::error::model_not_found` | Model not found | Modellen hittades inte | Shared reference target checked |
| 20489 | 831600253 | `component::anthropic::config_subentries::ai_task_data::error::api_error` | Unable to get model info: {message} | Det gick inte att hämta modellinformation: {message} | Shared reference target checked |
| 20490 | 831540344 | `component::vizio::exceptions::unknown_command::message` | Unknown remote command `{command}`. Valid commands for this device are listed in the integration documentation. | Okänt fjärrkommando `{command}`. Giltiga kommandon för den här enheten anges i integrationens dokumentation. | Core-literal match |
| 20491 | 831537563 | `component::google_weather::exceptions::auth_error::message` | Authentication failed: {error} | Autentiseringen misslyckades: {error} | Core-literal match |
| 20492 | 831537562 | `component::google_weather::config_subentries::location::initiate_flow::reconfigure` | Reconfigure location | Konfigurera om plats | Core-literal match |
| 20493 | 831537561 | `component::google_weather::config_subentries::location::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 20494 | 831537560 | `component::google_weather::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 20495 | 831537559 | `component::google_weather::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 20496 | 831520852 | `component::satel_integra::config::step::user::data_description::encryption_key` | If the alarm panel requires encryption, enter the integration encryption key here. | Om larmpanelen kräver kryptering, ange integrationskrypteringsnyckeln här. | Shared reference target checked |
| 20497 | 831520851 | `component::satel_integra::config::step::user::data::encryption_key` | Integration encryption key | Integrationskrypteringsnyckel | Shared reference target checked |
| 20498 | 831520850 | `component::satel_integra::config::step::reconfigure::data_description::encryption_key` | If the alarm panel requires encryption, enter the integration encryption key here. | Om larmpanelen kräver kryptering, ange integrationskrypteringsnyckeln här. | Shared reference target checked |
| 20499 | 831520849 | `component::satel_integra::config::step::reconfigure::data::encryption_key` | Integration encryption key | Integrationskrypteringsnyckel | Shared reference target checked |
| 20500 | 831520848 | `component::satel_integra::common::encryption_key_description` | If the alarm panel requires encryption, enter the integration encryption key here. | Om larmpanelen kräver kryptering, ange integrationskrypteringsnyckeln här. | Core-literal match |
| 20501 | 831520847 | `component::satel_integra::common::encryption_key` | Integration encryption key | Integrationskrypteringsnyckel | Core-literal match |
| 20502 | 831520472 | `component::comelit::entity::binary_sensor::motion::name` | Motion | Rörelse | Source-path follow-up open |
| 20503 | 831520471 | `component::comelit::entity::binary_sensor::faulty::name` | Faulty | Felaktig | Core-literal match |
| 20504 | 831520470 | `component::comelit::entity::binary_sensor::anomaly::name` | Anomaly | Anomali | Core-literal match |
| 20505 | 831486062 | `component::victron_gx::entity::switch::vebus_inverter_setting_alarm_grid_lost::name` | Grid lost alarm setting | Inställning för larm vid förlorat elnät | Core-literal match |
| 20506 | 831486061 | `component::victron_gx::entity::switch::vebus_inverter_ignoreacin1_onoff_control::name` | Control ignore AC-in-1 | Kontroll ignorera AC-in-1 | Core-literal match |
| 20507 | 831486060 | `component::victron_gx::entity::switch::vebus_device_device_number_power_assist_enabled::name` | {device_number} PowerAssist enabled | {device_number} PowerAssist aktiverat | Core-literal match |
| 20508 | 831486059 | `component::victron_gx::entity::switch::system_settings_overvoltage_feedin::name` | DC-coupled PV - feed in excess | DC-kopplad PV - inmatning överskott | Core-literal match |
| 20509 | 831486058 | `component::victron_gx::entity::switch::system_relay_relay::name` | Relay {relay} state | Relä {relay} tillstånd | Core-literal match |
| 20510 | 831486057 | `component::victron_gx::entity::switch::system_ess_schedule_charge_slot_enabled::name` | ESS BatteryLife schedule charge {slot} enabled | ESS BatteryLife schemalagd laddning {slot} aktiverad | Core-literal match |
| 20511 | 831486056 | `component::victron_gx::entity::switch::system_ess_battery_use::name` | ESS only critical loads from battery | ESS endast kritiska belastningar från batteri | Core-literal match |
| 20512 | 831486055 | `component::victron_gx::entity::switch::switchable_output_output_state::name` | State | Tillstånd | Shared reference target checked |
| 20513 | 831486054 | `component::victron_gx::entity::switch::switch_output_state::name` | State | Tillstånd | Shared reference target checked |
| 20514 | 831486053 | `component::victron_gx::entity::switch::solarcharger_relay_state::name` | Relay state | Relätillstånd | Core-literal match |
| 20515 | 831486052 | `component::victron_gx::entity::switch::multi_relay0_state::name` | Relay on Multi RS state | Relä på Multi RS-läge | Core-literal match |
| 20516 | 831486051 | `component::victron_gx::entity::switch::multi_disable_feed_in::name` | ESS disable feed-in | ESS inaktivera feed-in | Core-literal match |
| 20517 | 831486050 | `component::victron_gx::entity::switch::multi_disable_charge::name` | ESS disable charge | ESS inaktivera laddning | Core-literal match |
| 20518 | 831486049 | `component::victron_gx::entity::switch::generator_manual_start::name` | Manual start | Manuell start | Core-literal match |
| 20519 | 831486048 | `component::victron_gx::entity::switch::generator_gen_id_start_on_voltage_enabled::name` | Generator start on voltage enabled | Generator start vid spänning aktiverat | Core-literal match |
| 20520 | 831486047 | `component::victron_gx::entity::switch::generator_gen_id_start_on_temp_enabled::name` | Generator start on high temp enabled | Generator start vid hög temperatur aktiverat | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 832086548 | `component::tailwind::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 831755430 | `component::eurotronic_cometblue::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 831732192 | `component::iaqualink::config::abort::reauth_successful` | Re-authentication was successful |
| 831537561 | `component::google_weather::config_subentries::location::abort::reconfigure_successful` | Reconfiguration was successful |
| 831537560 | `component::google_weather::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 831537559 | `component::google_weather::config::abort::reauth_successful` | Re-authentication was successful |
| 831520472 | `component::comelit::entity::binary_sensor::motion::name` | Motion |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
