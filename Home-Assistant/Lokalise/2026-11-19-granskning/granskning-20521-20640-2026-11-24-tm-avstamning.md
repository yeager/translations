# Home Assistant Core – historisk avstämning 20521–20640

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 49 direkta källtexter matchar HA Core-källan; 18 referensanvändningar med 14 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 53 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 20521 | 831486046 | `component::victron_gx::entity::switch::generator_gen_id_start_on_soc_enabled::name` | Generator start on SoC enabled | Generator start på SoC aktiverat | Core-literal match |
| 20522 | 831486045 | `component::victron_gx::entity::switch::generator_gen_id_quiet_hours_enabled::name` | Generator quiet hours enabled | Generator tysta timmar aktiverat | Core-literal match |
| 20523 | 831486044 | `component::victron_gx::entity::switch::generator_autorun::name` | Auto-start enabled | Autostart aktiverat | Core-literal match |
| 20524 | 831486043 | `component::victron_gx::entity::switch::evcharger_charge::name` | EV charging | Elbil laddar | Core-literal match |
| 20525 | 831486042 | `component::victron_gx::entity::switch::digitalinput_settings_invert_translation::name` | Invert digital input | Växelriktare digital ingång | Core-literal match |
| 20526 | 831328955 | `component::smartthings::entity::switch::purify::name` | Purify | Rena | Core-literal match |
| 20527 | 831313351 | `component::switchbot::entity::switch::wireless_charging::name` | Wireless charging | Trådlös laddning | Core-literal match |
| 20528 | 831313350 | `component::switchbot::entity::switch::child_lock::name` | Child lock | Barnlås | Core-literal match |
| 20529 | 831266107 | `component::ring::entity::event::ding::state_attributes::event_type::state::ring` | Ring | Signal | Shared reference target checked |
| 20530 | 831215555 | `component::tibber::exceptions::get_prices_timeout::message` | Timeout fetching energy prices from Tibber | Timeout för att hämta energipriser från Tibber | Core-literal match |
| 20531 | 831215554 | `component::tibber::exceptions::get_prices_invalid_login::message` | Could not authenticate with Tibber while fetching prices | Det gick inte att autentisera sig hos Tibber när priser skulle hämtas | Core-literal match |
| 20532 | 831215553 | `component::tibber::exceptions::get_prices_communication_failed::message` | Could not fetch energy prices from Tibber ({detail}) | Det gick inte att hämta energipriser från Tibber ({detail}) | Core-literal match |
| 20533 | 831106819 | `component::home_connect::services::set_program_and_options::fields::laundry_care_washer_option_i_dos_2_active::name` | i-Dos 2 Active | i-DOS 2 aktivt | Core-literal match |
| 20534 | 831106818 | `component::home_connect::services::set_program_and_options::fields::laundry_care_washer_option_i_dos_2_active::description` | Defines if the detergent feed is activated / deactivated. (i-Dos content 2) | Definierar om tvättmedelsmatningen är aktiverad/avaktiverad. (i-DOS-innehåll 2) | Core-literal match |
| 20535 | 831106817 | `component::home_connect::services::set_program_and_options::fields::laundry_care_washer_option_i_dos_1_active::name` | i-Dos 1 Active | i-DOS 1 aktivt | Core-literal match |
| 20536 | 831106816 | `component::home_connect::services::set_program_and_options::fields::laundry_care_washer_option_i_dos_1_active::description` | Defines if the detergent feed is activated / deactivated. (i-Dos content 1) | Definierar om tvättmedelsmatningen är aktiverad/avaktiverad. (i-DOS-innehåll 1) | Core-literal match |
| 20537 | 831106815 | `component::home_connect::services::set_program_and_options::fields::laundry_care_common_option_vario_perfect::name` | Vario perfect | Vario Perfect | Core-literal match |
| 20538 | 831106814 | `component::home_connect::services::set_program_and_options::fields::laundry_care_common_option_vario_perfect::description` | Defines if a cycle saves energy (Eco Perfect) or time (Speed Perfect). | Definierar om en tvättcykel sparar energi (Eco Perfect) eller tid (Speed Perfect). | Core-literal match |
| 20539 | 831106813 | `component::home_connect::services::set_program_and_options::fields::cooking_common_option_hood_venting_level::name` | Venting level | Ventilationsnivå | Core-literal match |
| 20540 | 831106812 | `component::home_connect::services::set_program_and_options::fields::cooking_common_option_hood_venting_level::description` | Defines the required fan setting. | Definierar önskad fläktinställning. | Core-literal match |
| 20541 | 831106811 | `component::home_connect::services::set_program_and_options::fields::cooking_common_option_hood_intensive_level::name` | Intensive level | Intensiv nivå | Core-literal match |
| 20542 | 831106810 | `component::home_connect::services::set_program_and_options::fields::cooking_common_option_hood_intensive_level::description` | Defines the intensive setting. | Definierar intensivinställningen. | Core-literal match |
| 20543 | 831106809 | `component::home_connect::services::set_program_and_options::fields::consumer_products_coffee_maker_option_bean_container_selection::name` | Bean container | Behållare för bönor | Core-literal match |
| 20544 | 831106808 | `component::home_connect::services::set_program_and_options::fields::consumer_products_coffee_maker_option_bean_container_selection::description` | Defines the preferred bean container. | Definierar den föredragna behållaren för bönor. | Core-literal match |
| 20545 | 831106807 | `component::home_connect::selector::programs::options::cooking_oven_program_heating_mode_3_d_hot_air` | 3D hot air | 3D-varmluft | Core-literal match |
| 20546 | 831106806 | `component::home_connect::selector::intensive_level::options::cooking_hood_enum_type_intensive_stage_intensive_stage_2` | Intensive stage 2 | Intensiv fas 2 | Core-literal match |
| 20547 | 831106805 | `component::home_connect::selector::intensive_level::options::cooking_hood_enum_type_intensive_stage_intensive_stage_1` | Intensive stage 1 | Intensiv fas 1 | Core-literal match |
| 20548 | 831106804 | `component::home_connect::selector::available_maps::options::consumer_products_cleaning_robot_enum_type_available_maps_map_3` | Map 3 | Karta 3 | Core-literal match |
| 20549 | 831106803 | `component::home_connect::selector::available_maps::options::consumer_products_cleaning_robot_enum_type_available_maps_map_2` | Map 2 | Karta 2 | Core-literal match |
| 20550 | 831106802 | `component::home_connect::selector::available_maps::options::consumer_products_cleaning_robot_enum_type_available_maps_map_1` | Map 1 | Karta 1 | Core-literal match |
| 20551 | 831106801 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_heating_mode_3_d_hot_air` | 3D hot air | 3D-varmluft | Shared reference target checked |
| 20552 | 831106800 | `component::home_connect::entity::select::reference_map_id::state::consumer_products_cleaning_robot_enum_type_available_maps_map_3` | Map 3 | Karta 3 | Shared reference target checked |
| 20553 | 831106799 | `component::home_connect::entity::select::reference_map_id::state::consumer_products_cleaning_robot_enum_type_available_maps_map_2` | Map 2 | Karta 2 | Shared reference target checked |
| 20554 | 831106798 | `component::home_connect::entity::select::reference_map_id::state::consumer_products_cleaning_robot_enum_type_available_maps_map_1` | Map 1 | Karta 1 | Shared reference target checked |
| 20555 | 831106797 | `component::home_connect::entity::select::intensive_level::state::cooking_hood_enum_type_intensive_stage_intensive_stage_2` | Intensive stage 2 | Intensiv fas 2 | Shared reference target checked |
| 20556 | 831106796 | `component::home_connect::entity::select::intensive_level::state::cooking_hood_enum_type_intensive_stage_intensive_stage_1` | Intensive stage 1 | Intensiv fas 1 | Shared reference target checked |
| 20557 | 831106795 | `component::home_connect::entity::select::current_map::state::consumer_products_cleaning_robot_enum_type_available_maps_map_3` | Map 3 | Karta 3 | Shared reference target checked |
| 20558 | 831106794 | `component::home_connect::entity::select::current_map::state::consumer_products_cleaning_robot_enum_type_available_maps_map_2` | Map 2 | Karta 2 | Shared reference target checked |
| 20559 | 831106793 | `component::home_connect::entity::select::current_map::state::consumer_products_cleaning_robot_enum_type_available_maps_map_1` | Map 1 | Karta 1 | Shared reference target checked |
| 20560 | 831106792 | `component::home_connect::entity::select::active_program::state::cooking_oven_program_heating_mode_3_d_hot_air` | 3D hot air | 3D-varmluft | Shared reference target checked |
| 20561 | 831105627 | `component::music_assistant::entity::switch::surround_3d::name` | Surround 3D | Surround 3D | Core-literal match |
| 20562 | 831105626 | `component::music_assistant::entity::switch::speaker_b::name` | Speaker B | Högtalare B | Core-literal match |
| 20563 | 831105625 | `component::music_assistant::entity::switch::speaker_a::name` | Speaker A | Högtalare A | Core-literal match |
| 20564 | 831105624 | `component::music_assistant::entity::switch::pure_direct::name` | Pure direct | Pure direkt | Core-literal match |
| 20565 | 831105623 | `component::music_assistant::entity::switch::party_mode::name` | Party mode | Partyläge | Core-literal match |
| 20566 | 831105622 | `component::music_assistant::entity::switch::extra_bass::name` | Extra bass | Extra bas | Core-literal match |
| 20567 | 831105621 | `component::music_assistant::entity::switch::enhancer::name` | Enhancer | Förbättrare | Core-literal match |
| 20568 | 831105620 | `component::music_assistant::entity::switch::clear_voice::name` | Clear voice | Klar röst | Core-literal match |
| 20569 | 831105619 | `component::music_assistant::entity::switch::bass_extension::name` | Bass extension | Basförlängning | Core-literal match |
| 20570 | 831105618 | `component::music_assistant::entity::switch::adaptive_drc::name` | Adaptive DRC | Adaptiv DRC | Core-literal match |
| 20571 | 831105614 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::warehouse_loft` | Warehouse loft | Lagerlokal | Source-path follow-up open |
| 20572 | 831105613 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::village_vanguard` | Village Vanguard | Village Vanguard | Source-path follow-up open |
| 20573 | 831105612 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::village_gate` | Village Gate | Village Gate | Source-path follow-up open |
| 20574 | 831105611 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::vienna` | Hall in Vienna | Hall i Wien | Source-path follow-up open |
| 20575 | 831105610 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::usa_b` | Hall in USA B | Hall i USA B | Source-path follow-up open |
| 20576 | 831105609 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::usa_a` | Hall in USA A | Hall i USA A | Source-path follow-up open |
| 20577 | 831105608 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::tv_program` | TV program | TV-program | Source-path follow-up open |
| 20578 | 831105607 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::tokyo` | Church in Tokyo | Kyrka i Tokyo | Source-path follow-up open |
| 20579 | 831105606 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::target` | Target | Target | Source-path follow-up open |
| 20580 | 831105605 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::talk_show` | Talk show | Talkshow | Source-path follow-up open |
| 20581 | 831105604 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::surr_decoder` | Surround decoder | Surround-dekoder | Source-path follow-up open |
| 20582 | 831105603 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::stuttgart` | Hall in Stuttgart | Hall i Stuttgart | Source-path follow-up open |
| 20583 | 831105602 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::straight` | Straight | Rakt | Source-path follow-up open |
| 20584 | 831105601 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::stereo` | Stereo | Stereo | Source-path follow-up open |
| 20585 | 831105600 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::standard` | Standard | Standard | Source-path follow-up open |
| 20586 | 831105599 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::sports` | Sports | Sport | Source-path follow-up open |
| 20587 | 831105598 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::spectacle` | Spectacle | Skådespel | Source-path follow-up open |
| 20588 | 831105597 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::sci-fi` | Sci-fi | Sci-fi | Source-path follow-up open |
| 20589 | 831105596 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::royaumont` | Church in Royaumont | Kyrka i Royaumont | Source-path follow-up open |
| 20590 | 831105595 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::roxy_theatre` | The Roxy Theatre | Roxy-teatern | Source-path follow-up open |
| 20591 | 831105594 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::roleplaying_game` | Roleplaying game | Rollspel | Source-path follow-up open |
| 20592 | 831105593 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::recital_opera` | Recital/opera | Konsert/opera | Source-path follow-up open |
| 20593 | 831105592 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::pavilion` | Pavilion | Paviljong | Source-path follow-up open |
| 20594 | 831105591 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::off` | Off | Av | Source-path follow-up open |
| 20595 | 831105590 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::my_surround` | My surround | Min surround | Source-path follow-up open |
| 20596 | 831105589 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::music_video` | Music video | Musikvideo | Source-path follow-up open |
| 20597 | 831105588 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::music` | Music | Musik | Source-path follow-up open |
| 20598 | 831105587 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::munich_b` | Hall in Munich B | Hall i München B | Source-path follow-up open |
| 20599 | 831105586 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::munich_a` | Hall in Munich A | Hall i München A | Source-path follow-up open |
| 20600 | 831105585 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::munich` | Hall in Munich | Hall i München | Source-path follow-up open |
| 20601 | 831105584 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::movie` | Movie | Film | Source-path follow-up open |
| 20602 | 831105583 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::mono_movie` | Mono movie | Film mono | Source-path follow-up open |
| 20603 | 831105582 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::jazz_club` | Jazz club | Jazzklubb | Source-path follow-up open |
| 20604 | 831105581 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::game` | Game | Spel | Source-path follow-up open |
| 20605 | 831105580 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::freiburg` | Church in Freiburg | Kyrka i Freiburg | Source-path follow-up open |
| 20606 | 831105579 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::frankfurt` | Hall in Frankfurt | Hall i Frankfurt | Source-path follow-up open |
| 20607 | 831105578 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::enhanced` | Enhanced | Förbättrad | Source-path follow-up open |
| 20608 | 831105577 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::drama` | Drama | Drama | Source-path follow-up open |
| 20609 | 831105576 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::disco` | Disco | Disco | Source-path follow-up open |
| 20610 | 831105575 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::concert` | Live concert | Livekonsert | Source-path follow-up open |
| 20611 | 831105574 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::chamber` | Chamber | Kammare | Source-path follow-up open |
| 20612 | 831105573 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::cellar_club` | Cellar club | Källarklubb | Source-path follow-up open |
| 20613 | 831105572 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::bottom_line` | The Bottom Line | Bottom-line | Source-path follow-up open |
| 20614 | 831105571 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::arena` | Arena | Arena | Source-path follow-up open |
| 20615 | 831105570 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::amsterdam` | Hall in Amsterdam | Hall i Amsterdam | Source-path follow-up open |
| 20616 | 831105569 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::all_ch_stereo` | All ch stereo | Alla kanaler stereo | Source-path follow-up open |
| 20617 | 831105568 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::adventure` | Adventure | Äventyr | Source-path follow-up open |
| 20618 | 831105567 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::action_game` | Action game | Actionspel | Source-path follow-up open |
| 20619 | 831105566 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::9ch_stereo` | 9ch stereo | 9-kanals stereo | Source-path follow-up open |
| 20620 | 831105565 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::7ch_stereo` | 7ch stereo | 7-kanals stereo | Source-path follow-up open |
| 20621 | 831105564 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::5ch_stereo` | 5ch stereo | 5-kanals stereo | Source-path follow-up open |
| 20622 | 831105563 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::2ch_stereo` | 2ch stereo | 2-kanals stereo | Source-path follow-up open |
| 20623 | 831105562 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::11ch_stereo` | 11ch stereo | 11-kanals stereo | Source-path follow-up open |
| 20624 | 831103755 | `component::sfr_box::entity::sensor::voip_infra::state::gprs` | GPRS | GPRS | Shared reference target checked |
| 20625 | 831103754 | `component::sfr_box::entity::sensor::voip_infra::state::ftth` | FTTH | FTTH | Shared reference target checked |
| 20626 | 831103753 | `component::sfr_box::entity::sensor::voip_infra::state::adsl` | ADSL | ADSL | Shared reference target checked |
| 20627 | 831103752 | `component::sfr_box::entity::sensor::voip_infra::name` | VoIP infrastructure | VoIP-infrastruktur | Core-literal match |
| 20628 | 831103751 | `component::sfr_box::entity::binary_sensor::voip_status::name` | VoIP status | VoIP-status | Core-literal match |
| 20629 | 831103750 | `component::sfr_box::entity::binary_sensor::voip_hook_status::state::on` | Off-hook | Off-hook | Core-literal match |
| 20630 | 831103749 | `component::sfr_box::entity::binary_sensor::voip_hook_status::state::off` | On-hook | On-hook | Core-literal match |
| 20631 | 831103748 | `component::sfr_box::entity::binary_sensor::voip_hook_status::name` | VoIP phone hook status | VoIP-telefonens kopplingsstatus | Core-literal match |
| 20632 | 831103747 | `component::sfr_box::entity::binary_sensor::voip_callhistory_active::name` | VoIP call history active | VoIP-samtalhistorik aktiv | Core-literal match |
| 20633 | 831103685 | `component::duco::exceptions::failed_to_set_state::message` | Failed to set ventilation state. | Det gick inte att ställa in ventilationsläget. | Core-literal match |
| 20634 | 831103684 | `component::duco::exceptions::cannot_connect::message` | Could not connect to the Duco device. | Det gick inte att ansluta till Duco-enheten. | Core-literal match |
| 20635 | 831103683 | `component::duco::exceptions::api_error::message` | Unexpected error from the Duco API. | Oväntat fel från Duco API:t. | Core-literal match |
| 20636 | 831103682 | `component::duco::entity::fan::ventilation::state_attributes::preset_mode::state::auto` | Auto | Auto | Shared reference target checked |
| 20637 | 831103681 | `component::duco::config::step::user::data_description::host` | IP address or hostname of your Duco ventilation box. | IP-adress eller värdnamn för din Duco-ventilationsbox. | Core-literal match |
| 20638 | 831103680 | `component::duco::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 20639 | 831103679 | `component::duco::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 20640 | 831103678 | `component::duco::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 831105614 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::warehouse_loft` | Warehouse loft |
| 831105613 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::village_vanguard` | Village Vanguard |
| 831105612 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::village_gate` | Village Gate |
| 831105611 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::vienna` | Hall in Vienna |
| 831105610 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::usa_b` | Hall in USA B |
| 831105609 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::usa_a` | Hall in USA A |
| 831105608 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::tv_program` | TV program |
| 831105607 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::tokyo` | Church in Tokyo |
| 831105606 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::target` | Target |
| 831105605 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::talk_show` | Talk show |
| 831105604 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::surr_decoder` | Surround decoder |
| 831105603 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::stuttgart` | Hall in Stuttgart |
| 831105602 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::straight` | Straight |
| 831105601 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::stereo` | Stereo |
| 831105600 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::standard` | Standard |
| 831105599 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::sports` | Sports |
| 831105598 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::spectacle` | Spectacle |
| 831105597 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::sci-fi` | Sci-fi |
| 831105596 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::royaumont` | Church in Royaumont |
| 831105595 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::roxy_theatre` | The Roxy Theatre |
| 831105594 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::roleplaying_game` | Roleplaying game |
| 831105593 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::recital_opera` | Recital/opera |
| 831105592 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::pavilion` | Pavilion |
| 831105591 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::off` | Off |
| 831105590 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::my_surround` | My surround |
| 831105589 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::music_video` | Music video |
| 831105588 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::music` | Music |
| 831105587 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::munich_b` | Hall in Munich B |
| 831105586 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::munich_a` | Hall in Munich A |
| 831105585 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::munich` | Hall in Munich |
| 831105584 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::movie` | Movie |
| 831105583 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::mono_movie` | Mono movie |
| 831105582 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::jazz_club` | Jazz club |
| 831105581 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::game` | Game |
| 831105580 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::freiburg` | Church in Freiburg |
| 831105579 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::frankfurt` | Hall in Frankfurt |
| 831105578 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::enhanced` | Enhanced |
| 831105577 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::drama` | Drama |
| 831105576 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::disco` | Disco |
| 831105575 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::concert` | Live concert |
| 831105574 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::chamber` | Chamber |
| 831105573 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::cellar_club` | Cellar club |
| 831105572 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::bottom_line` | The Bottom Line |
| 831105571 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::arena` | Arena |
| 831105570 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::amsterdam` | Hall in Amsterdam |
| 831105569 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::all_ch_stereo` | All ch stereo |
| 831105568 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::adventure` | Adventure |
| 831105567 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::action_game` | Action game |
| 831105566 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::9ch_stereo` | 9ch stereo |
| 831105565 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::7ch_stereo` | 7ch stereo |
| 831105564 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::5ch_stereo` | 5ch stereo |
| 831105563 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::2ch_stereo` | 2ch stereo |
| 831105562 | `component::music_assistant::entity::media_player::ma_media_player::state_attributes::sound_mode::state::11ch_stereo` | 11ch stereo |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
