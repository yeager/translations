# Home Assistant Core – historisk avstämning 19681–19800

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 93 direkta källtexter matchar HA Core-källan; 22 referensanvändningar med 15 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 5 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 19681 | 836505156 | `component::victron_gx::common::dc_temperature` | DC temperature | DC-temperatur | Core-literal match |
| 19682 | 836505155 | `component::victron_gx::common::dc_output_voltage` | DC output voltage | DC-utgångsspänning | Core-literal match |
| 19683 | 836505154 | `component::victron_gx::common::dc_output_power` | DC output power | DC-utgångseffekt | Core-literal match |
| 19684 | 836505153 | `component::victron_gx::common::dc_output_current` | DC output current | DC-utgångsström | Core-literal match |
| 19685 | 836505152 | `component::victron_gx::common::current_sensor_issue` | Current sensor issue | Problem med strömsensorn | Core-literal match |
| 19686 | 836505151 | `component::victron_gx::common::current_phase` | Current {phase} | Ström {phase} | Source-path follow-up open |
| 19687 | 836505150 | `component::victron_gx::common::current_on_phase` | Current on {phase} | Ström på {phase} | Core-literal match |
| 19688 | 836505149 | `component::victron_gx::common::current_limit` | Current limit | Strömgräns | Core-literal match |
| 19689 | 836505148 | `component::victron_gx::common::current` | Current | Ström | Core-literal match |
| 19690 | 836505147 | `component::victron_gx::common::converter_issue` | Converter issue | Problem med konverterare | Core-literal match |
| 19691 | 836505146 | `component::victron_gx::common::consumption_on_phase` | Consumption on {phase} | Förbrukning på {phase} | Core-literal match |
| 19692 | 836505145 | `component::victron_gx::common::consumption` | Consumption | Förbrukning | Core-literal match |
| 19693 | 836505144 | `component::victron_gx::common::charger_temperature_too_high` | Charger temperature too high | Laddartemperaturen är för hög | Core-literal match |
| 19694 | 836505143 | `component::victron_gx::common::charger_over_current` | Charger over current | Laddare överström | Core-literal match |
| 19695 | 836505142 | `component::victron_gx::common::charger_only` | Charger only | Endast laddare | Core-literal match |
| 19696 | 836505141 | `component::victron_gx::common::charger_current_reversed` | Charger current reversed | Laddström omvänd | Core-literal match |
| 19697 | 836505140 | `component::victron_gx::common::bulk_time_limit_exceeded` | Bulk time limit exceeded | Tidsgränsen för bulköverföring har överskridits | Core-literal match |
| 19698 | 836505139 | `component::victron_gx::common::bulk` | Bulk | Bulk | Core-literal match |
| 19699 | 836505138 | `component::victron_gx::common::bms_connection_lost` | BMS connection lost | BMS-anslutningen förlorad | Core-literal match |
| 19700 | 836505137 | `component::victron_gx::common::battery_voltage_too_high` | Battery voltage too high | Batterispänningen är för hög | Core-literal match |
| 19701 | 836505136 | `component::victron_gx::common::battery_safe` | Battery Safe | Batteri säkert | Core-literal match |
| 19702 | 836505135 | `component::victron_gx::common::auto_equalize_recondition` | Auto equalize / recondition | Automatisk utjämning/rekonditionering | Core-literal match |
| 19703 | 836505134 | `component::victron_gx::common::alarm` | Alarm | Larm | Core-literal match |
| 19704 | 836505133 | `component::victron_gx::common::active_ac_input` | Active AC input | Aktiv AC-ingång | Core-literal match |
| 19705 | 836505132 | `component::victron_gx::common::absorption` | Absorption | Absorption | Core-literal match |
| 19706 | 836442924 | `component::music_assistant::entity::select::tone_control_mode::state::manual` | Manual | Manuell | Shared reference target checked |
| 19707 | 836442923 | `component::music_assistant::entity::select::tone_control_mode::state::bypass` | Bypass | Bypass | Core-literal match |
| 19708 | 836442922 | `component::music_assistant::entity::select::tone_control_mode::state::auto` | Auto | Auto | Shared reference target checked |
| 19709 | 836442921 | `component::music_assistant::entity::select::tone_control_mode::name` | Tone control mode | Tonkontrollläge | Core-literal match |
| 19710 | 836442920 | `component::music_assistant::entity::select::surround_decoder_type::state::toggle` | Toggle | Växla | Shared reference target checked |
| 19711 | 836442919 | `component::music_assistant::entity::select::surround_decoder_type::state::dts_neural_x` | DTS Neural:X | DTS Neural:X | Core-literal match |
| 19712 | 836442918 | `component::music_assistant::entity::select::surround_decoder_type::state::dts_neo6_music` | DTS Neo:6 Music | DTS Neo:6 Musik | Core-literal match |
| 19713 | 836442917 | `component::music_assistant::entity::select::surround_decoder_type::state::dts_neo6_cinema` | DTS Neo:6 Cinema | DTS Neo:6 Cinema | Core-literal match |
| 19714 | 836442916 | `component::music_assistant::entity::select::surround_decoder_type::state::dolby_surround` | Dolby Surround | Dolby Surround | Core-literal match |
| 19715 | 836442915 | `component::music_assistant::entity::select::surround_decoder_type::state::dolby_pl2x_music` | Dolby ProLogic 2x Music | Dolby ProLogic 2x Musik | Core-literal match |
| 19716 | 836442914 | `component::music_assistant::entity::select::surround_decoder_type::state::dolby_pl2x_movie` | Dolby ProLogic 2x Movie | Dolby ProLogic 2x Film | Core-literal match |
| 19717 | 836442913 | `component::music_assistant::entity::select::surround_decoder_type::state::dolby_pl2x_game` | Dolby ProLogic 2x Game | Dolby ProLogic 2x-spel | Core-literal match |
| 19718 | 836442912 | `component::music_assistant::entity::select::surround_decoder_type::state::dolby_pl` | Dolby ProLogic | Dolby ProLogic | Core-literal match |
| 19719 | 836442911 | `component::music_assistant::entity::select::surround_decoder_type::state::auto` | Auto | Auto | Shared reference target checked |
| 19720 | 836442910 | `component::music_assistant::entity::select::surround_decoder_type::name` | Surround decoder type | Typ av surroundavkodare | Core-literal match |
| 19721 | 836442909 | `component::music_assistant::entity::select::sleep::state:::90` | 90 minutes | 90 minuter | Core-literal match |
| 19722 | 836442908 | `component::music_assistant::entity::select::sleep::state:::60` | 60 minutes | 60 minuter | Core-literal match |
| 19723 | 836442907 | `component::music_assistant::entity::select::sleep::state:::30` | 30 minutes | 30 minuter | Core-literal match |
| 19724 | 836442906 | `component::music_assistant::entity::select::sleep::state:::120` | 120 minutes | 120 minuter | Core-literal match |
| 19725 | 836442905 | `component::music_assistant::entity::select::sleep::state:::0` | Off | Av | Shared reference target checked |
| 19726 | 836442904 | `component::music_assistant::entity::select::sleep::name` | Sleep timer | Insomningstimer | Core-literal match |
| 19727 | 836442903 | `component::music_assistant::entity::select::link_control::state::standard` | Standard | Standard | Core-literal match |
| 19728 | 836442902 | `component::music_assistant::entity::select::link_control::state::stability` | Stability | Stabilitet | Core-literal match |
| 19729 | 836442901 | `component::music_assistant::entity::select::link_control::state::speed` | Speed | Hastighet | Core-literal match |
| 19730 | 836442900 | `component::music_assistant::entity::select::link_control::name` | Link control | Länkkontroll | Core-literal match |
| 19731 | 836442899 | `component::music_assistant::entity::select::link_audio_quality::state::uncompressed` | Uncompressed | Okomprimerad | Core-literal match |
| 19732 | 836442898 | `component::music_assistant::entity::select::link_audio_quality::state::compressed` | Compressed | Komprimerad | Core-literal match |
| 19733 | 836442897 | `component::music_assistant::entity::select::link_audio_quality::name` | Link audio quality | Länkljudkvalitet | Core-literal match |
| 19734 | 836442896 | `component::music_assistant::entity::select::link_audio_delay::state::lip_sync` | Lip synchronization | Läppsynkronisering | Core-literal match |
| 19735 | 836442895 | `component::music_assistant::entity::select::link_audio_delay::state::balanced` | Balanced | Balanserad | Core-literal match |
| 19736 | 836442894 | `component::music_assistant::entity::select::link_audio_delay::state::audio_sync_on` | Audio synchronization on | Ljudsynkronisering på | Core-literal match |
| 19737 | 836442893 | `component::music_assistant::entity::select::link_audio_delay::state::audio_sync_off` | Audio synchronization off | Ljudsynkronisering av | Core-literal match |
| 19738 | 836442892 | `component::music_assistant::entity::select::link_audio_delay::state::audio_sync` | Audio synchronization | Ljudsynkronisering | Core-literal match |
| 19739 | 836442891 | `component::music_assistant::entity::select::link_audio_delay::name` | Link audio delay | Länkljudfördröjning | Core-literal match |
| 19740 | 836442890 | `component::music_assistant::entity::select::equalizer_mode::state::manual` | Manual | Manuell | Shared reference target checked |
| 19741 | 836442889 | `component::music_assistant::entity::select::equalizer_mode::state::bypass` | Bypass | Bypass | Core-literal match |
| 19742 | 836442888 | `component::music_assistant::entity::select::equalizer_mode::state::auto` | Auto | Auto | Shared reference target checked |
| 19743 | 836442887 | `component::music_assistant::entity::select::equalizer_mode::name` | Equalizer mode | Equalizer-läge | Core-literal match |
| 19744 | 836442886 | `component::music_assistant::entity::select::dimmer::state::auto` | Auto | Auto | Shared reference target checked |
| 19745 | 836442885 | `component::music_assistant::entity::select::dimmer::name` | Dimmer | Dimmer | Core-literal match |
| 19746 | 836299652 | `component::duco::exceptions::rate_limit_exceeded::message` | The Duco device has reached its daily write limit. Try again tomorrow. | Duco-enheten har nått sin dagliga skrivgräns. Försök igen i morgon. | Core-literal match |
| 19747 | 836293290 | `component::broadlink::exceptions::send_command_failed::message` | Failed to send command: {error} | Det gick inte att skicka kommandot: {error} | Core-literal match |
| 19748 | 836293289 | `component::broadlink::entity::infrared::infrared::name` | IR transmitter | IR-sändare | Source-path follow-up open |
| 19749 | 836276602 | `component::duco::config::step::discovery_confirm::description` | Do you want to set up {name}? | Vill du konfigurera {name}? | Core-literal match |
| 19750 | 836276601 | `component::duco::config::abort::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 19751 | 836276600 | `component::duco::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 19752 | 836276599 | `component::duco::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 19753 | 836252151 | `component::anthropic::selector::thinking_effort::options::xhigh` | X-High | Extra hög | Source-path follow-up open |
| 19754 | 836231391 | `component::victron_gx::entity::switch::evcharger_auto_start::name` | Auto start | Auto-start | Core-literal match |
| 19755 | 836231390 | `component::victron_gx::entity::sensor::multi_dc_temperature::name` | DC temperature | DC-temperatur | Shared reference target checked |
| 19756 | 836231389 | `component::victron_gx::entity::sensor::charger_dc_voltage_output::name` | DC output {output} voltage | DC-utgång {output} spänning | Core-literal match |
| 19757 | 836231388 | `component::victron_gx::entity::sensor::charger_dc_current_output::name` | DC output {output} current | DC-utgång {output} ström | Core-literal match |
| 19758 | 836231387 | `component::victron_gx::entity::sensor::charger_ac_in_current_phase::name` | AC input current {phase} | AC-ingångsström, fas {phase} | Core-literal match |
| 19759 | 836231285 | `component::anthropic::config_subentries::conversation::step::model::data_description::max_tokens` | Limit the number of response tokens. | Begränsa antalet svarstokens. | Core-literal match |
| 19760 | 836231284 | `component::anthropic::config_subentries::conversation::step::model::data::max_tokens` | Maximum tokens to return in response | Maximalt antal tokens att returnera i svar | Core-literal match |
| 19761 | 836231283 | `component::anthropic::config_subentries::ai_task_data::step::model::data_description::max_tokens` | Limit the number of response tokens. | Begränsa antalet svarstokens. | Shared reference target checked |
| 19762 | 836231282 | `component::anthropic::config_subentries::ai_task_data::step::model::data::max_tokens` | Maximum tokens to return in response | Maximalt antal tokens att returnera i svar | Shared reference target checked |
| 19763 | 836231281 | `component::anthropic::config_subentries::ai_task_data::error::thinking_budget_too_large` | Thinking budget must be less than the Maximum tokens. | Tankebudget måste vara lägre än det maximala antalet tokens. | Shared reference target checked |
| 19764 | 836231094 | `component::kiosker::entity::sensor::last_motion::name` | Last motion | Senaste rörelse | Core-literal match |
| 19765 | 836231093 | `component::kiosker::entity::sensor::last_interaction::name` | Last interaction | Senaste interaktion | Core-literal match |
| 19766 | 836231092 | `component::kiosker::entity::sensor::ambient_light::name` | Ambient light | Omgivande ljus | Core-literal match |
| 19767 | 836231091 | `component::kiosker::config::step::zeroconf_confirm::title` | Discovered Kiosker App | Upptäckt: Kiosker-appen | Core-literal match |
| 19768 | 836231090 | `component::kiosker::config::step::zeroconf_confirm::submit` | Pair | Para ihop | Core-literal match |
| 19769 | 836231089 | `component::kiosker::config::step::zeroconf_confirm::description` | You are about to pair `{name}` at `{host}` with Home Assistant.<br><br>Please provide the API token to complete setup. | Du är på väg att para ihop `{name}` på `{host}` med Home Assistant.<br><br>Ange API-token för att slutföra installationen. | Core-literal match |
| 19770 | 836231088 | `component::kiosker::config::step::zeroconf_confirm::data_description::verify_ssl` | Verify SSL certificate. Enable for valid certificates only. | Verifiera SSL-certifikat. Aktivera endast för giltiga certifikat. | Core-literal match |
| 19771 | 836231087 | `component::kiosker::config::step::zeroconf_confirm::data_description::api_token` | The API token for the Kiosker App. This can be generated in the app API settings. | API-token för Kiosker-appen. Denna kan genereras i appens API-inställningar. | Core-literal match |
| 19772 | 836231086 | `component::kiosker::config::step::zeroconf_confirm::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 19773 | 836231085 | `component::kiosker::config::step::zeroconf_confirm::data::api_token` | API token | API-token | Shared reference target checked |
| 19774 | 836231084 | `component::kiosker::config::step::zeroconf::description` | Do you want to configure {name} at {host}? | Vill du konfigurera {name} på {host}? | Core-literal match |
| 19775 | 836231083 | `component::kiosker::config::step::user::title` | Pair Kiosker App | Koppla ihop Kiosker-appen | Core-literal match |
| 19776 | 836231082 | `component::kiosker::config::step::user::description` | Enable the API in Kiosker settings to pair with Home Assistant. | Aktivera API:et i Kiosker-inställningarna för att koppla ihop med Home Assistant. | Core-literal match |
| 19777 | 836231081 | `component::kiosker::config::step::user::data_description::verify_ssl` | Verify SSL certificate. Enable for valid certificates only. | Verifiera SSL-certifikat. Aktivera endast för giltiga certifikat. | Core-literal match |
| 19778 | 836231080 | `component::kiosker::config::step::user::data_description::ssl` | Connect to the Kiosker App using HTTPS. The Kiosker API has to be configured for SSL. | Anslut till Kiosk-appen med HTTPS. Kiosk-API:et måste konfigureras för SSL. | Core-literal match |
| 19779 | 836231079 | `component::kiosker::config::step::user::data_description::host` | The hostname or IP address of the device running the Kiosker App | Värdnamnet eller IP-adressen för enheten som kör Kiosk-appen | Core-literal match |
| 19780 | 836231078 | `component::kiosker::config::step::user::data_description::api_token` | The API token for the Kiosker App. This can be generated in the app API settings. | API-token för Kiosk-appen. Denna kan genereras i appens API-inställningar. | Core-literal match |
| 19781 | 836231077 | `component::kiosker::config::step::user::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 19782 | 836231076 | `component::kiosker::config::step::user::data::ssl` | Uses an SSL certificate | Använder ett SSL-certifikat | Shared reference target checked |
| 19783 | 836231075 | `component::kiosker::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 19784 | 836231074 | `component::kiosker::config::step::user::data::api_token` | API token | API-token | Shared reference target checked |
| 19785 | 836231073 | `component::kiosker::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 19786 | 836231072 | `component::kiosker::config::error::tls_error` | TLS verification failed. Check your SSL settings. | TLS-verifieringen misslyckades. Kontrollera dina SSL-inställningar. | Core-literal match |
| 19787 | 836231071 | `component::kiosker::config::error::invalid_ip_auth` | IP authentication failed. Check your IP whitelist. | IP-autentisering misslyckades. Kontrollera din IP whitelist. | Core-literal match |
| 19788 | 836231070 | `component::kiosker::config::error::invalid_auth` | Authentication failed. Check your API token. | Autentiseringen misslyckades. Kontrollera din API-token. | Core-literal match |
| 19789 | 836231069 | `component::kiosker::config::error::cannot_connect` | Failed to connect to the Kiosker device. | Det gick inte att ansluta till Kiosker-enheten. | Core-literal match |
| 19790 | 836231068 | `component::kiosker::config::error::bad_request` | Invalid request. Check your configuration. | Ogiltig begäran. Kontrollera din konfiguration. | Core-literal match |
| 19791 | 836231067 | `component::kiosker::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 19792 | 836231066 | `component::kiosker::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 19793 | 836231048 | `component::ruckus_unleashed::options::step::init::data_description::mac_filter` | Select specific clients to track. If none are selected, all clients will be tracked. | Välj specifika klienter att spåra. Om inga är valda kommer alla klienter att spåras. | Core-literal match |
| 19794 | 836231047 | `component::ruckus_unleashed::options::step::init::data::mac_filter` | Clients to track | Klienter att spåra | Core-literal match |
| 19795 | 836231007 | `component::melcloud::entity::sensor::return_temperature_boiler::name` | Boiler return temperature | Pannans returtemperatur | Core-literal match |
| 19796 | 836231006 | `component::melcloud::entity::sensor::mixing_tank_temperature::name` | Mixing tank temperature | Blandningstankens temperatur | Core-literal match |
| 19797 | 836231005 | `component::melcloud::entity::sensor::flow_temperature_boiler::name` | Boiler flow temperature | Pannans flödestemperatur | Core-literal match |
| 19798 | 836231004 | `component::melcloud::entity::sensor::demand_percentage::name` | Demand percentage | Efterfrågan i procent | Core-literal match |
| 19799 | 836231003 | `component::melcloud::entity::sensor::daily_hot_water_energy_produced::name` | Daily hot water energy produced | Daglig energi producerad för varmvatten | Core-literal match |
| 19800 | 836231002 | `component::melcloud::entity::sensor::daily_hot_water_energy_consumed::name` | Daily hot water energy consumed | Daglig energiförbrukning för varmvatten | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 836505151 | `component::victron_gx::common::current_phase` | Current {phase} |
| 836293289 | `component::broadlink::entity::infrared::infrared::name` | IR transmitter |
| 836276599 | `component::duco::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |
| 836252151 | `component::anthropic::selector::thinking_effort::options::xhigh` | X-High |
| 836231067 | `component::kiosker::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
