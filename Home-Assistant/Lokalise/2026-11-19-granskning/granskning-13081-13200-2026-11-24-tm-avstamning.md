# Home Assistant Core – historisk avstämning 13081–13200

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 92 direkta källtexter matchar HA Core-källan; 26 referensanvändningar med 20 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 2 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 13081 | 914313000 | `component::ecovacs::entity::sensor::total_stats_cleanings_mower::name` | Total mowings | Totalt antal klippningar | Core-literal match |
| 13082 | 914312999 | `component::ecovacs::entity::sensor::total_stats_area_mower::name` | Total area mowed | Total klippt yta | Core-literal match |
| 13083 | 914312998 | `component::ecovacs::entity::sensor::stats_time_mower::name` | Mowing duration | Klipptid | Core-literal match |
| 13084 | 914312997 | `component::ecovacs::entity::sensor::stats_area_mower::name` | Area mowed | Klippt yta | Core-literal match |
| 13085 | 914181238 | `component::forked_daapd::exceptions::output_not_found::message` | The output for entity {entity_id} no longer exists on the OwnTone server. | Utgången för entiteten {entity_id} finns inte längre på OwnTone-servern. | Core-literal match |
| 13086 | 914181237 | `component::forked_daapd::exceptions::not_forked_daapd_output::message` | Entity {entity_id} is not an output of this OwnTone server. | Entiteten {entity_id} är inte en utgång på den här OwnTone-servern. | Core-literal match |
| 13087 | 914181236 | `component::forked_daapd::exceptions::entity_not_found::message` | Entity {entity_id} not found. | Entitet {entity_id} hittades inte. | Core-literal match |
| 13088 | 914115527 | `component::lyngdorf::entity::sensor::zone_b_streaming_source::name` | Zone B streaming source | Strömningskälla för zon B | Core-literal match |
| 13089 | 914115526 | `component::lyngdorf::entity::sensor::zone_b_audio_input::name` | Zone B audio input | Ljudingång för zon B | Core-literal match |
| 13090 | 914115525 | `component::lyngdorf::entity::sensor::video_input::name` | Video input | Videoingång | Core-literal match |
| 13091 | 914115524 | `component::lyngdorf::entity::sensor::video_information::name` | Video information | Videoinformation | Core-literal match |
| 13092 | 914115523 | `component::lyngdorf::entity::sensor::streaming_source::name` | Streaming source | Strömningskälla | Core-literal match |
| 13093 | 914115522 | `component::lyngdorf::entity::sensor::audio_input::name` | Audio input | Ljudingång | Core-literal match |
| 13094 | 914115521 | `component::lyngdorf::entity::sensor::audio_information::name` | Audio information | Ljudinformation | Core-literal match |
| 13095 | 913938356 | `component::onedrive_for_business::exceptions::connection_error::message` | Failed to connect to OneDrive. | Misslyckades med att ansluta till OneDrive. | Shared reference target checked |
| 13096 | 913796059 | `component::zwave_js::config::error::usb_and_socket_path` | Select either a USB device or a socket path, not both. | Välj antingen en USB-enhet eller en socket-sökväg, inte båda. | Core-literal match |
| 13097 | 913796058 | `component::zwave_js::config::error::missing_usb_or_socket_path` | Select a USB device or provide a socket path. | Välj en USB-enhet eller ange en socket-sökväg. | Core-literal match |
| 13098 | 913790147 | `component::zwave_js::config::abort::invalid_discovery_info` | The discovery information is invalid. | Upptäcktsinformationen är ogiltig. | Core-literal match |
| 13099 | 913303581 | `component::karakeep::exceptions::invalid_auth::message` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 13100 | 913303580 | `component::karakeep::config::step::reauth_confirm::description` | The API token for your Karakeep instance is no longer valid. Enter a new one to reconnect. | API-tokenet för din Karakeep-instans är inte längre giltigt. Ange ett nytt för att återansluta. | Core-literal match |
| 13101 | 913303579 | `component::karakeep::config::step::reauth_confirm::data_description::token` | The API token used to connect to your Karakeep instance. | API-token som används för att ansluta till din Karakeep instans. | Shared reference target checked |
| 13102 | 913303578 | `component::karakeep::config::step::reauth_confirm::data::token` | API token | API-token | Shared reference target checked |
| 13103 | 913303577 | `component::karakeep::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 13104 | 913193625 | `component::hotspring::config::abort::unique_id_mismatch` | The MAC address does not match the configured device. Please ensure you reconfigure against the same device. | MAC-adressen matchar inte den konfigurerade enheten. Se till att du konfigurerar om mot samma enhet. | Core-literal match |
| 13105 | 913193624 | `component::hotspring::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 13106 | 913032667 | `component::scrape::config_subentries::entity::step::user::data_description::name` | Provide a name for the sensor. | Ange ett namn för sensorn. | Core-literal match |
| 13107 | 913032666 | `component::scrape::config_subentries::entity::step::user::data::name` | Name | Namn | Shared reference target checked |
| 13108 | 913011174 | `component::lyric::entity::binary_sensor::device_pairing_enabled::name` | Device pairing enabled | Enhetsparkoppling aktiverad | Core-literal match |
| 13109 | 913009593 | `component::srp_energy::config::step::user::data::name` | Name | Namn | Shared reference target checked |
| 13110 | 912945707 | `component::sma::config::step::reconfigure::data_description::password` | The password for your SMA device | Lösenordet till din SMA-enhet | Shared reference target checked |
| 13111 | 912844401 | `component::lyric::entity::sensor::schedule_status::name` | Schedule status | Schemastatus | Core-literal match |
| 13112 | 912781616 | `component::roborock::entity::switch::mop_washing::name` | Mop washing | Mopptvätt | Core-literal match |
| 13113 | 912781615 | `component::roborock::entity::switch::mop_drying::name` | Mop drying | Mopptorkning | Core-literal match |
| 13114 | 912781614 | `component::roborock::entity::switch::dust_emptying::name` | Dust emptying | Dammtömning | Core-literal match |
| 13115 | 912753093 | `component::flow_it::exceptions::update_failed::message` | Error communicating with API | Fel i kommunikationen med API:et | Core-literal match |
| 13116 | 912753092 | `component::flow_it::exceptions::command_failed::message` | Failed to send command to AriaQ VMC | Det gick inte att skicka kommandot till AriaQ VMC | Core-literal match |
| 13117 | 912753091 | `component::flow_it::exceptions::auth_failed::message` | Authentication failed when communicating with AriaQ VMC | Autentiseringen misslyckades vid kommunikation med AriaQ VMC | Core-literal match |
| 13118 | 912753090 | `component::flow_it::config::step::zeroconf_confirm::title` | Discovered AriaQ | Upptäckt AriaQ | Core-literal match |
| 13119 | 912753089 | `component::flow_it::config::step::zeroconf_confirm::description` | Do you want to set up {name}? | Vill du konfigurera {name}? | Core-literal match |
| 13120 | 912753088 | `component::flow_it::config::step::zeroconf_confirm::data_description::username` | The default username is 'api'. | Standardanvändarnamnet är 'api'. | Shared reference target checked |
| 13121 | 912753087 | `component::flow_it::config::step::zeroconf_confirm::data_description::password` | The password is available on the physical device LCD display, by interacting with the menu, clicking on the 'settings' icon and then on the 'wifi icon'. | Lösenordet visas på enhetens LCD-skärm. Öppna menyn, välj ikonen ”Inställningar” och sedan Wi-Fi-ikonen. | Shared reference target checked |
| 13122 | 912753086 | `component::flow_it::config::step::zeroconf_confirm::data::username` | Username | Användarnamn | Shared reference target checked |
| 13123 | 912753085 | `component::flow_it::config::step::zeroconf_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 13124 | 912753084 | `component::flow_it::config::step::user::title` | Configure AriaQ | Konfigurera AriaQ | Core-literal match |
| 13125 | 912753083 | `component::flow_it::config::step::user::data_description::username` | The default username is 'api'. | Standardanvändarnamnet är 'api'. | Core-literal match |
| 13126 | 912753082 | `component::flow_it::config::step::user::data_description::password` | The password is available on the physical device LCD display, by interacting with the menu, clicking on the 'settings' icon and then on the 'wifi icon'. | Lösenordet visas på enhetens LCD-skärm. Öppna menyn, välj ikonen ”Inställningar” och sedan Wi-Fi-ikonen. | Core-literal match |
| 13127 | 912753081 | `component::flow_it::config::step::user::data_description::host` | The hostname or IP address of the AriaQ device. | Värdnamnet eller IP-adressen för AriaQ-enheten. | Core-literal match |
| 13128 | 912753080 | `component::flow_it::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 13129 | 912753079 | `component::flow_it::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 13130 | 912753078 | `component::flow_it::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 13131 | 912753077 | `component::flow_it::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 13132 | 912753076 | `component::flow_it::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 13133 | 912753075 | `component::flow_it::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 13134 | 912753074 | `component::flow_it::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 13135 | 912737163 | `component::switchbot::entity::sensor::radar_triggered_level::name` | Radar triggered level | Radarutlöst nivå | Core-literal match |
| 13136 | 912737162 | `component::switchbot::entity::sensor::radar_triggered_distance::name` | Radar triggered distance | Radarutlöst avstånd | Core-literal match |
| 13137 | 912737161 | `component::switchbot::entity::sensor::pir_triggered_level::name` | PIR triggered level | PIR-utlöst nivå | Core-literal match |
| 13138 | 912737160 | `component::switchbot::entity::binary_sensor::low_temperature::name` | Low temperature | Låg temperatur | Core-literal match |
| 13139 | 912737159 | `component::switchbot::entity::binary_sensor::lockout_alarm::name` | Lockout alarm | Lockout alarm | Core-literal match |
| 13140 | 912737158 | `component::switchbot::entity::binary_sensor::high_temperature::name` | High temperature | Hög temperatur | Core-literal match |
| 13141 | 912737157 | `component::switchbot::entity::binary_sensor::duress_alarm::name` | Duress alarm | Överfallslarm | Core-literal match |
| 13142 | 912689509 | `component::home_connect::exceptions::start_program_option_not_writable::message` | Option {option} is not writable for program {program} | Alternativet "{option}" är inte skrivbart för programmet "{program}" | Core-literal match |
| 13143 | 912689384 | `component::smlight::exceptions::unknown_effect::message` | Unknown effect: {effect}. | Okänd effekt: {effect}. | Core-literal match |
| 13144 | 912689383 | `component::smlight::exceptions::reboot_timeout::message` | Timeout waiting for {hostname} to reboot after update | Timeout vid väntan på att {hostname} ska starta om efter uppdateringen | Core-literal match |
| 13145 | 912686816 | `component::twinkly::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 13146 | 912570441 | `component::homematicip_cloud::exceptions::alarm_activation_failed::message` | The alarm system did not accept the requested state | Larmsystemet accepterade inte det begärda tillståndet | Core-literal match |
| 13147 | 912570440 | `component::homematicip_cloud::exceptions::alarm_activation_blocked::message` | The alarm system was not armed because the following devices report a problem: {devices} | Larmsystemet har inte aktiverats eftersom följande enheter rapporterade problem: {devices} | Core-literal match |
| 13148 | 912227597 | `component::technove::exceptions::invalid_response::message` | Invalid response from TechnoVE API. | Ogiltigt svar från TechnoVE-API:et. | Core-literal match |
| 13149 | 912227596 | `component::technove::exceptions::communication_error::message` | Error communicating with TechnoVE API. | Fel vid kommunikation med TechnoVE-API:et. | Core-literal match |
| 13150 | 911962118 | `component::home_connect::services::set_program_and_options::fields::heating_ventilation_air_conditioning_air_conditioner_option_setpoint_temperature::name` | Setpoint temperature | Börvärde för temperatur | Shared reference target checked |
| 13151 | 911962117 | `component::home_connect::services::set_program_and_options::fields::heating_ventilation_air_conditioning_air_conditioner_option_setpoint_temperature::description` | Defines the target temperature, which will be held by the air conditioner. | Anger den måltemperatur som luftkonditioneringen ska hålla. | Core-literal match |
| 13152 | 911262395 | `component::actron_air::entity::cover::damper::name` | Damper | Spjäll | Core-literal match |
| 13153 | 911233975 | `component::harbor::exceptions::select_option_failed::message` | Failed to select {option} for {select}. | Misslyckades med att välja {option} för {select}. | Core-literal match |
| 13154 | 911233974 | `component::harbor::entity::select::night_mode_preference::state::on` | On | På | Shared reference target checked |
| 13155 | 911233973 | `component::harbor::entity::select::night_mode_preference::state::off` | Off | Av | Shared reference target checked |
| 13156 | 911233972 | `component::harbor::entity::select::night_mode_preference::state::auto` | Auto | Auto | Shared reference target checked |
| 13157 | 911233971 | `component::harbor::entity::select::night_mode_preference::name` | Night mode | Nattläge | Core-literal match |
| 13158 | 911211971 | `component::knx::config_panel::selectors::knx-select-options-selector::option` | Option name | Alternativnamn | Core-literal match |
| 13159 | 911211970 | `component::knx::config_panel::selectors::knx-select-options-selector::add_option` | Add option | Lägg till alternativ | Core-literal match |
| 13160 | 911211969 | `component::knx::config_panel::entities::create::select::knx::options_source::title` | Options | Alternativ | Core-literal match |
| 13161 | 911211968 | `component::knx::config_panel::entities::create::select::knx::options_source::options::from_dpt::label` | Options from data point type | Alternativ från datapunktstyp | Core-literal match |
| 13162 | 911211967 | `component::knx::config_panel::entities::create::select::knx::options_source::options::from_dpt::description` | The options are derived from the values of an enum data point type. | Alternativen härleds från värdena för en enum-datapunktstyp. | Core-literal match |
| 13163 | 911211966 | `component::knx::config_panel::entities::create::select::knx::options_source::options::custom::label` | Custom options | Anpassade alternativ | Core-literal match |
| 13164 | 911211965 | `component::knx::config_panel::entities::create::select::knx::options_source::options::custom::description` | Define the options and the value each one sends manually. | Definiera manuellt alternativen och det värde som varje alternativ skickar. | Core-literal match |
| 13165 | 911211964 | `component::knx::config_panel::entities::create::select::knx::options_source::ga_enum::label` | Group address | Gruppadress | Shared reference target checked |
| 13166 | 911211963 | `component::knx::config_panel::entities::create::select::knx::options_source::ga_enum::description` | Group address the selected value is sent to and read from. | Gruppadressen som det valda värdet skickas till och läses från. | Shared reference target checked |
| 13167 | 911211962 | `component::knx::config_panel::entities::create::select::knx::options_source::ga_custom::label` | Group address | Gruppadress | Shared reference target checked |
| 13168 | 911211961 | `component::knx::config_panel::entities::create::select::knx::options_source::ga_custom::description` | Group address the selected value is sent to and read from. | Gruppadressen som det valda värdet skickas till och läses från. | Core-literal match |
| 13169 | 911211960 | `component::knx::config_panel::entities::create::select::knx::options_source::description` | Choose how the selectable options are defined. | Välj hur de valbara alternativen definieras. | Core-literal match |
| 13170 | 911211959 | `component::knx::config_panel::entities::create::select::knx::options_source::custom_options::label` | Options | Alternativ | Core-literal match |
| 13171 | 911211958 | `component::knx::config_panel::entities::create::select::knx::options_source::custom_options::description` | Define the selectable options and the value each one sends. | Definiera de valbara alternativen och det värde som varje alternativ skickar. | Core-literal match |
| 13172 | 911211957 | `component::knx::config_panel::entities::create::select::description` | The KNX select platform lets you present a list of named options and map each to a value sent to and read from the KNX bus. | KNX select-plattformen låter dig presentera en lista med namngivna alternativ och mappa vart och ett till ett värde som skickas till och läses från KNX-bussen. | Core-literal match |
| 13173 | 911211664 | `component::vizio::services::send_text::name` | Send text | Skicka text | Core-literal match |
| 13174 | 911211663 | `component::vizio::services::send_text::fields::text::name` | Text | Text | Core-literal match |
| 13175 | 911211662 | `component::vizio::services::send_text::fields::text::description` | The text to type. | Text att skriva. | Core-literal match |
| 13176 | 911211661 | `component::vizio::services::send_text::description` | Types text into the focused on-screen field, such as a search box or PIN entry. Only ASCII characters are supported. | Skriver text i det aktiva fältet på skärmen, till exempel en sökruta eller ett fält för PIN-kod. Endast ASCII-tecken stöds. | Core-literal match |
| 13177 | 911211573 | `component::knx::config_panel::entities::create::weather::knx::section_day_night::title` | Day/Night | Dag/Natt | Core-literal match |
| 13178 | 911211572 | `component::knx::config_panel::entities::create::weather::knx::section_day_night::description` | Day and night state used to determine the weather condition. | Tillståndet för dag eller natt används för att avgöra väderförhållandena. | Core-literal match |
| 13179 | 911211571 | `component::knx::config_panel::entities::create::weather::knx::section_brightness::title` | Brightness | Ljusstyrka | Core-literal match |
| 13180 | 911211570 | `component::knx::config_panel::entities::create::weather::knx::section_brightness::description` | Brightness readings used to determine the weather condition. | Avläsningar av ljusstyrka som används för att fastställa väderförhållandena. | Core-literal match |
| 13181 | 911211569 | `component::knx::config_panel::entities::create::weather::knx::section_alarms::title` | Alarms | Larm | Core-literal match |
| 13182 | 911211568 | `component::knx::config_panel::entities::create::weather::knx::section_alarms::description` | Binary states used to determine the weather condition. | Binära tillstånd som används för att bestämma väderförhållandena. | Core-literal match |
| 13183 | 911211567 | `component::knx::config_panel::entities::create::weather::knx::invert_day_night::label` | Invert day/night | Invertera dag/natt | Core-literal match |
| 13184 | 911211566 | `component::knx::config_panel::entities::create::weather::knx::invert_day_night::description` | By default `0` is interpreted as day and `1` as night (DPT 1.024). Enable to invert this. | Som standard tolkas `0` som dag och `1` som natt (DPT 1.024). Aktivera för att invertera detta. | Core-literal match |
| 13185 | 911211565 | `component::knx::config_panel::entities::create::weather::knx::ga_wind_speed::label` | Wind speed | Vindhastighet | Core-literal match |
| 13186 | 911211564 | `component::knx::config_panel::entities::create::weather::knx::ga_wind_speed::description` | Group address for reading the current wind speed. | Gruppadress för avläsning av aktuell vindhastighet. | Core-literal match |
| 13187 | 911211563 | `component::knx::config_panel::entities::create::weather::knx::ga_wind_bearing::label` | Wind bearing | Vindriktning | Core-literal match |
| 13188 | 911211562 | `component::knx::config_panel::entities::create::weather::knx::ga_wind_bearing::description` | Group address for reading the current wind bearing. | Gruppadress för avläsning av aktuell vindriktning. | Core-literal match |
| 13189 | 911211561 | `component::knx::config_panel::entities::create::weather::knx::ga_wind_alarm::label` | Wind alarm | Vindlarm | Core-literal match |
| 13190 | 911211560 | `component::knx::config_panel::entities::create::weather::knx::ga_wind_alarm::description` | Group address for reading whether the wind alarm is active. | Gruppadress för avläsning av om vindlarmet är aktivt. | Core-literal match |
| 13191 | 911211559 | `component::knx::config_panel::entities::create::weather::knx::ga_temperature::label` | Temperature | Temperatur | Core-literal match |
| 13192 | 911211558 | `component::knx::config_panel::entities::create::weather::knx::ga_temperature::description` | Group address for reading the current outside temperature. | Gruppadress för avläsning av aktuell utetemperatur. | Core-literal match |
| 13193 | 911211557 | `component::knx::config_panel::entities::create::weather::knx::ga_rain_alarm::label` | Rain alarm | Regnlarm | Core-literal match |
| 13194 | 911211556 | `component::knx::config_panel::entities::create::weather::knx::ga_rain_alarm::description` | Group address for reading whether the rain alarm is active. | Gruppadress för avläsning av om regnlarmet är aktivt. | Core-literal match |
| 13195 | 911211555 | `component::knx::config_panel::entities::create::weather::knx::ga_humidity::label` | Humidity | Fuktighet | Core-literal match |
| 13196 | 911211554 | `component::knx::config_panel::entities::create::weather::knx::ga_humidity::description` | Group address for reading the current humidity. | Gruppadress för avläsning av aktuell luftfuktighet. | Core-literal match |
| 13197 | 911211553 | `component::knx::config_panel::entities::create::weather::knx::ga_frost_alarm::label` | Frost alarm | Frostlarm | Core-literal match |
| 13198 | 911211552 | `component::knx::config_panel::entities::create::weather::knx::ga_frost_alarm::description` | Group address for reading whether the frost alarm is active. | Gruppadress för avläsning av om frostlarmet är aktivt. | Core-literal match |
| 13199 | 911211551 | `component::knx::config_panel::entities::create::weather::knx::ga_day_night::label` | Day/Night | Dag/Natt | Core-literal match |
| 13200 | 911211550 | `component::knx::config_panel::entities::create::weather::knx::ga_day_night::description` | Group address for reading whether it is day or night. | Gruppadress för att läsa av om det är dag eller natt. | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 913303577 | `component::karakeep::config::abort::reauth_successful` | Re-authentication was successful |
| 913193624 | `component::hotspring::config::abort::reconfigure_successful` | Reconfiguration was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
