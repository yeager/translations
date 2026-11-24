# Home Assistant Core – historisk avstämning 17041–17160

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 101 direkta källtexter matchar HA Core-källan; 17 referensanvändningar med 13 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 2 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 17041 | 865365159 | `component::template::config::step::device_tracker::data::in_zones` | Zones | Zoner | Core-literal match |
| 17042 | 865244080 | `component::wallbox::entity::button::resume_schedule::name` | Resume schedule | Fortsätt schema | Core-literal match |
| 17043 | 865234482 | `component::envertech_evt800::entity::sensor::total_energy_2::name` | Total Energy MPPT 2 | Total energi MPPT 2 | Core-literal match |
| 17044 | 865234481 | `component::envertech_evt800::entity::sensor::total_energy_1::name` | Total Energy MPPT 1 | Total energi MPPT 1 | Core-literal match |
| 17045 | 865234480 | `component::envertech_evt800::entity::sensor::temperature_2::name` | Temperature MPPT 2 | Temperatur MPPT 2 | Core-literal match |
| 17046 | 865234479 | `component::envertech_evt800::entity::sensor::temperature_1::name` | Temperature MPPT 1 | Temperatur MPPT 1 | Core-literal match |
| 17047 | 865234478 | `component::envertech_evt800::entity::sensor::power_2::name` | DC Power MPPT 2 | DC-effekt MPPT 2 | Core-literal match |
| 17048 | 865234477 | `component::envertech_evt800::entity::sensor::power_1::name` | DC Power MPPT 1 | DC-effekt MPPT 1 | Core-literal match |
| 17049 | 865234476 | `component::envertech_evt800::entity::sensor::mppt_id_2::name` | MPPT ID 2 | MPPT-ID 2 | Core-literal match |
| 17050 | 865234475 | `component::envertech_evt800::entity::sensor::mppt_id_1::name` | MPPT ID 1 | MPPT-ID 1 | Core-literal match |
| 17051 | 865234474 | `component::envertech_evt800::entity::sensor::input_voltage_2::name` | DC Voltage MPPT 2 | DC-spänning MPPT 2 | Core-literal match |
| 17052 | 865234473 | `component::envertech_evt800::entity::sensor::input_voltage_1::name` | DC Voltage MPPT 1 | DC-spänning MPPT 1 | Core-literal match |
| 17053 | 865234472 | `component::envertech_evt800::entity::sensor::current_2::name` | DC Current MPPT 2 | DC-ström MPPT 2 | Core-literal match |
| 17054 | 865234471 | `component::envertech_evt800::entity::sensor::current_1::name` | DC Current MPPT 1 | DC-ström MPPT 1 | Core-literal match |
| 17055 | 865234470 | `component::envertech_evt800::entity::sensor::ac_voltage_2::name` | AC Voltage MPPT 2 | AC-spänning MPPT 2 | Core-literal match |
| 17056 | 865234469 | `component::envertech_evt800::entity::sensor::ac_voltage_1::name` | AC Voltage MPPT 1 | AC-spänning MPPT 1 | Core-literal match |
| 17057 | 865234468 | `component::envertech_evt800::entity::sensor::ac_frequency_2::name` | AC Frequency MPPT 2 | AC-frekvens MPPT 2 | Core-literal match |
| 17058 | 865234467 | `component::envertech_evt800::entity::sensor::ac_frequency_1::name` | AC Frequency MPPT 1 | AC-frekvens MPPT 1 | Core-literal match |
| 17059 | 865234466 | `component::envertech_evt800::config::step::user::title` | Setup EVT800 device | Konfigurera EVT800-enheten | Core-literal match |
| 17060 | 865234465 | `component::envertech_evt800::config::step::user::description` | Enter your EVT800 device information. | Ange din EVT800-enhetsinformation. | Core-literal match |
| 17061 | 865234464 | `component::envertech_evt800::config::step::user::data_description::port` | The Port of your Envertech EVT800 device. | Porten på din Envertech EVT800-enhet. | Core-literal match |
| 17062 | 865234463 | `component::envertech_evt800::config::step::user::data_description::ip_address` | The IP address of your Envertech EVT800 device. | IP-adressen för din Envertech EVT800-enhet. | Core-literal match |
| 17063 | 865234462 | `component::envertech_evt800::config::step::user::data::port` | Port | Port | Shared reference target checked |
| 17064 | 865234461 | `component::envertech_evt800::config::step::user::data::ip_address` | IP address | IP-adress | Shared reference target checked |
| 17065 | 865234460 | `component::envertech_evt800::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 17066 | 865234459 | `component::envertech_evt800::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 17067 | 865207305 | `component::vistapool::entity::number::smart_minimum_temperature::name` | Smart minimum temperature | Smart lägsta temperatur | Core-literal match |
| 17068 | 865207304 | `component::vistapool::entity::number::smart_maximum_temperature::name` | Smart maximum temperature | Smart högsta temperatur | Core-literal match |
| 17069 | 865207303 | `component::vistapool::entity::number::redox_setpoint::name` | Redox setpoint | Redox-börvärde | Core-literal match |
| 17070 | 865207302 | `component::vistapool::entity::number::ph_minimum::name` | pH minimum | Lägsta pH-värde | Core-literal match |
| 17071 | 865207301 | `component::vistapool::entity::number::ph_maximum::name` | pH maximum | Högsta pH-värde | Core-literal match |
| 17072 | 865207300 | `component::vistapool::entity::number::intel_temperature::name` | Intel temperature | Temperatur intelligent läge | Core-literal match |
| 17073 | 865207299 | `component::vistapool::entity::number::hydrolysis_setpoint::name` | Hydrolysis setpoint | Börvärde för hydrolys | Core-literal match |
| 17074 | 865207298 | `component::vistapool::entity::number::heating_minimum_temperature::name` | Heating minimum temperature | Lägsta uppvärmningstemperatur | Core-literal match |
| 17075 | 865207297 | `component::vistapool::entity::number::heating_maximum_temperature::name` | Heating maximum temperature | Högsta uppvärmningstemperatur | Core-literal match |
| 17076 | 865207296 | `component::vistapool::entity::number::electrolysis_setpoint::name` | Electrolysis setpoint | Börvärde för elektrolys | Core-literal match |
| 17077 | 864757140 | `component::growatt_server::exceptions::unknown_auth_type::message` | Unknown authentication type in config entry | Okänd autentiseringstyp i konfigurationsposten | Core-literal match |
| 17078 | 864757139 | `component::growatt_server::exceptions::rate_limited::message` | Growatt API rate limited, will retry: {error} | Growatt API har begränsad bandbredd, försöker igen: {error} | Core-literal match |
| 17079 | 864757138 | `component::growatt_server::exceptions::login_failed::message` | Growatt login failed: {message} | Growatt-inloggning misslyckades: {message} | Core-literal match |
| 17080 | 864757137 | `component::growatt_server::exceptions::invalid_credentials::message` | Username, password, or URL may be incorrect | Användarnamn, lösenord eller webbadress kan vara felaktiga | Core-literal match |
| 17081 | 864757136 | `component::growatt_server::exceptions::fetch_data_failed::message` | Error fetching data from Growatt API: {error} | Fel vid hämtning av data från Growatt API: {error} | Core-literal match |
| 17082 | 864757135 | `component::growatt_server::exceptions::communication_error::message` | Error communicating with Growatt API: {error} | Fel vid kommunikation med Growatt API: {error} | Core-literal match |
| 17083 | 864757134 | `component::growatt_server::exceptions::auth_failed::message` | Authentication failed for Growatt API: {error} | Autentiseringen misslyckades för Growatt API: {error} | Core-literal match |
| 17084 | 864757133 | `component::growatt_server::exceptions::api_error_with_code::message` | API error: {error} (Code: {code}) | API-fel: {error} (Kod: {code}) | Core-literal match |
| 17085 | 864742966 | `component::victron_gx::entity::switch::vebus_inverter_prefer_renewable_energy::name` | Prefer renewable energy | Föredra förnybar energi | Core-literal match |
| 17086 | 864742965 | `component::victron_gx::entity::switch::hub4_force_charge::name` | Force charge | Tvinga laddning | Core-literal match |
| 17087 | 864742964 | `component::victron_gx::entity::sensor::solarcharger_tracker_tracker_current::name` | PV tracker {tracker} current | PV-tracker {tracker} ström | Core-literal match |
| 17088 | 864742963 | `component::victron_gx::entity::sensor::solarcharger_pv_current::name` | PV current | PV-ström | Shared reference target checked |
| 17089 | 864742962 | `component::victron_gx::entity::sensor::multi_mppt_mpptnumber_current::name` | MPPT {mpptnumber} current | MPPT {mpptnumber} ström | Core-literal match |
| 17090 | 864742961 | `component::victron_gx::entity::sensor::multi_acout_voltage_phase::name` | Output voltage on {phase} | Utgångsspänning på {phase} | Core-literal match |
| 17091 | 864742960 | `component::victron_gx::entity::sensor::multi_acout_power_phase::name` | Output power on {phase} | Utgångseffekt på {phase} | Core-literal match |
| 17092 | 864742959 | `component::victron_gx::entity::sensor::multi_acout_current_phase::name` | Output current on {phase} | Utgångsström på {phase} | Core-literal match |
| 17093 | 864742958 | `component::victron_gx::entity::sensor::meteo_todays_yield::name` | Today's yield | Dagens produktion | Core-literal match |
| 17094 | 864742957 | `component::victron_gx::entity::sensor::meteo_time_since_last_sun::name` | Time since last sun | Tid sedan senaste solstrålning | Core-literal match |
| 17095 | 864742956 | `component::victron_gx::entity::sensor::meteo_irradiance::name` | Irradiance | Bestrålning | Core-literal match |
| 17096 | 864742955 | `component::victron_gx::entity::sensor::meteo_installation_power::name` | Installation power | Installationseffekt | Core-literal match |
| 17097 | 864742954 | `component::victron_gx::entity::sensor::meteo_cell_temperature::name` | Cell temperature | Celltemperatur | Core-literal match |
| 17098 | 864742953 | `component::victron_gx::entity::sensor::meteo_battery_voltage::name` | Battery voltage | Batterispänning | Core-literal match |
| 17099 | 864742952 | `component::victron_gx::entity::sensor::meteo_alarm_low_battery::state::warning` | Warning | Varning | Shared reference target checked |
| 17100 | 864742951 | `component::victron_gx::entity::sensor::meteo_alarm_low_battery::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 17101 | 864742950 | `component::victron_gx::entity::sensor::meteo_alarm_low_battery::state::alarm` | Alarm | Larm | Shared reference target checked |
| 17102 | 864742949 | `component::victron_gx::entity::sensor::meteo_alarm_low_battery::name` | Low battery alarm | Larm för låg batterinivå | Shared reference target checked |
| 17103 | 864742948 | `component::victron_gx::entity::sensor::generator_next_test_run::name` | Next test run | Nästa testkörning | Core-literal match |
| 17104 | 864742947 | `component::victron_gx::entity::binary_sensor::vebus_inverter_remote_generator_selected::name` | Remote generator selected | Fjärrgenerator vald | Core-literal match |
| 17105 | 864742946 | `component::victron_gx::common::pv_current` | PV current | PV-ström | Core-literal match |
| 17106 | 864742945 | `component::victron_gx::common::low_battery_alarm` | Low battery alarm | Larm för låg batterinivå | Core-literal match |
| 17107 | 864724466 | `component::helty::entity::sensor::outdoor_temperature::name` | Outdoor temperature | Utomhustemperatur | Core-literal match |
| 17108 | 864724465 | `component::helty::entity::sensor::indoor_temperature::name` | Indoor temperature | Inomhustemperatur | Core-literal match |
| 17109 | 864724464 | `component::helty::entity::sensor::indoor_humidity::name` | Indoor humidity | Inomhusluftfuktighet | Core-literal match |
| 17110 | 864724009 | `component::blebox::config::step::reconfigure::title` | Reconfigure BleBox device | Konfigurera om BleBox-enheten | Core-literal match |
| 17111 | 864724008 | `component::blebox::config::step::reconfigure::description` | Update the connection settings for your BleBox device. | Uppdatera anslutningsinställningarna för din BleBox-enhet. | Core-literal match |
| 17112 | 864724007 | `component::blebox::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference target checked |
| 17113 | 864724006 | `component::blebox::config::step::reconfigure::data::port` | Port | Port | Shared reference target checked |
| 17114 | 864724005 | `component::blebox::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 17115 | 864724004 | `component::blebox::config::step::reconfigure::data::host` | IP address | IP-adress | Shared reference target checked |
| 17116 | 864724003 | `component::blebox::config::abort::unique_id_mismatch` | The device identifier does not match the previously configured device. | Enhetsidentifieraren matchar inte den tidigare konfigurerade enheten. | Core-literal match |
| 17117 | 864724002 | `component::blebox::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 17118 | 864646709 | `component::vistapool::config::flow_title` | Vistapool pool controller | Vistapool poolstyrenhet | Core-literal match |
| 17119 | 864646708 | `component::vistapool::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 17120 | 864482966 | `component::vistapool::exceptions::set_failed::message` | Failed to set {entity}. | Misslyckades med att ställa in {entity}. | Core-literal match |
| 17121 | 864482965 | `component::vistapool::entity::button::led_pulse::name` | LED next color | LED nästa färg | Core-literal match |
| 17122 | 864264455 | `component::husqvarna_automower_ble::exceptions::connection_failed::message` | Unable to connect to device {address} due to {error}: {reason} | Det går inte att ansluta till enheten {address} på grund av {error}: {reason} | Core-literal match |
| 17123 | 864264432 | `component::ld2410_ble::exceptions::device_not_found::message` | Could not find LD2410B device with address {address}: {reason} | Det gick inte att hitta LD2410B-enheten med adressen {address}: {reason} | Core-literal match |
| 17124 | 864264384 | `component::snooz::exceptions::device_not_found::message` | Could not find Snooz with address {address}: {reason} | Kunde inte hitta Snooz med adressen {address}: {reason} | Core-literal match |
| 17125 | 864264369 | `component::eq3btsmart::exceptions::device_not_found::message` | [{mac_address}] Device could not be found: {reason} | [{mac_address}] Enheten kunde inte hittas: {reason} | Core-literal match |
| 17126 | 864261077 | `component::helty::config::step::user::title` | Connect to your Helty Flow | Anslut till ditt Helty Flow | Core-literal match |
| 17127 | 864261076 | `component::helty::config::step::user::data_description::host` | The IP address or hostname of the Helty Flow unit on your network. | IP-adressen eller värdnamnet för Helty Flow-enheten i ditt nätverk. | Core-literal match |
| 17128 | 864261075 | `component::helty::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 17129 | 864261074 | `component::helty::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 17130 | 864261073 | `component::helty::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 17131 | 864261072 | `component::helty::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 17132 | 864259565 | `component::blebox::exceptions::update_failed::message` | Failed to fetch firmware update information from the BleBox device: {error} | Misslyckades med att hämta information om uppdatering av firmware från BleBox-enheten: {error} | Core-literal match |
| 17133 | 864257915 | `component::yalexs_ble::exceptions::device_not_advertising::message` | {local_name} ({address}) is not advertising yet: {reason} | {local_name} ({address}) annonserar inte än: {reason} | Core-literal match |
| 17134 | 864257896 | `component::airthings_ble::exceptions::device_not_found::message` | Could not find Airthings device with address {address}: {reason} | Det gick inte att hitta Airthings-enheten med adressen {address}: {reason} | Core-literal match |
| 17135 | 864257818 | `component::led_ble::exceptions::device_not_found::message` | Could not find LED BLE device with address {address}: {reason} | Det gick inte att hitta LED-BLE-enheten med adressen {address}: {reason} | Core-literal match |
| 17136 | 864257041 | `component::fluss::exceptions::command_failed::message` | Failed to send command to Fluss+ device | Det gick inte att skicka kommandot till Fluss+-enheten | Core-literal match |
| 17137 | 864256657 | `component::alexa_devices::exceptions::unknown_exception::message` | Unknown error occurred: {error} | Okänt fel inträffade: {error} | Core-literal match |
| 17138 | 864252998 | `component::matter::entity::sensor::wifi_rssi::name` | Wi-Fi RSSI | Wi-Fi-RSSI | Core-literal match |
| 17139 | 864252997 | `component::matter::entity::sensor::thread_routing_role::state::unspecified` | Unspecified | Ospecificerad | Core-literal match |
| 17140 | 864252996 | `component::matter::entity::sensor::thread_routing_role::state::unknown` | Unknown | Okänd | Core-literal match |
| 17141 | 864252995 | `component::matter::entity::sensor::thread_routing_role::state::unassigned` | Unassigned | Ej tilldelad | Core-literal match |
| 17142 | 864252994 | `component::matter::entity::sensor::thread_routing_role::state::sleepy_end_device` | Sleepy end device | Sovande slutenhet | Core-literal match |
| 17143 | 864252993 | `component::matter::entity::sensor::thread_routing_role::state::router` | Router | Router | Core-literal match |
| 17144 | 864252992 | `component::matter::entity::sensor::thread_routing_role::state::reed` | Router eligible end device | Slutenhet som kan bli router | Core-literal match |
| 17145 | 864252991 | `component::matter::entity::sensor::thread_routing_role::state::leader` | Leader | Ledare | Core-literal match |
| 17146 | 864252990 | `component::matter::entity::sensor::thread_routing_role::state::end_device` | End device | Slutenhet | Core-literal match |
| 17147 | 864252989 | `component::matter::entity::sensor::thread_routing_role::name` | Thread routing role | Routningsroll i Thread | Core-literal match |
| 17148 | 864252988 | `component::matter::entity::sensor::thread_network_name::name` | Thread network name | Thread-nätverksnamn | Core-literal match |
| 17149 | 864252987 | `component::matter::entity::sensor::thread_channel::name` | Thread channel | Thread-kanal | Core-literal match |
| 17150 | 864252954 | `component::yoto::exceptions::unknown_track::message` | Unknown track {track_key} on card {card_id} | Okänt spår ”{track_key}” på kort {card_id} | Core-literal match |
| 17151 | 864252953 | `component::yoto::exceptions::unknown_chapter::message` | Unknown chapter {chapter_key} on card {card_id} | Okänt kapitel ”{chapter_key}” på kort {card_id} | Core-literal match |
| 17152 | 864252952 | `component::yoto::exceptions::unknown_card::message` | Unknown Yoto card: {card_id} | Okänt Yoto-kort: {card_id} | Core-literal match |
| 17153 | 864252951 | `component::yoto::exceptions::play_failed::message` | Failed to play Yoto media. | Det gick inte att spela upp Yoto-mediefilen. | Core-literal match |
| 17154 | 864252950 | `component::yoto::exceptions::invalid_media_id::message` | Not a Yoto media identifier: {media_id} | Ingen Yoto-medieidentifierare: {media_id} | Core-literal match |
| 17155 | 864252949 | `component::yoto::exceptions::card_detail_failed::message` | Could not load the Yoto card details. | Det gick inte att läsa in uppgifterna för Yoto-kortet. | Core-literal match |
| 17156 | 864241216 | `component::upb::config::step::user::data_description::file_path` | Path and name of the UPStart UPB export file. | Sökväg och namn för UPStart UPB-exportfilen. | Core-literal match |
| 17157 | 864241215 | `component::upb::config::step::user::data_description::device` | The serial port or network address of the UPB PIM. | Serieporten eller nätverksadressen för UPB PIM. | Core-literal match |
| 17158 | 864241214 | `component::upb::config::step::user::data::device` | Device | Enhet | Core-literal match |
| 17159 | 864154838 | `component::tractive::device::tracker::name` | Tracker {id} | Tracker {id} | Core-literal match |
| 17160 | 863836563 | `component::toon::exceptions::invalid_response::message` | Received an invalid response from the Toon device. | Fick ett ogiltigt svar från Toon-enheten. | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 864724002 | `component::blebox::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 864646708 | `component::vistapool::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
