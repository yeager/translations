# Home Assistant Core – historisk avstämning 19561–19680

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 95 direkta källtexter matchar HA Core-källan; 6 referensanvändningar med 6 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 19 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 19561 | 837199436 | `component::duco::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 19562 | 836990140 | `component::victron_gx::entity::device_tracker::gps_location::name` | Location | Plats | Shared reference target checked |
| 19563 | 836904032 | `component::unifi::options::step::statistics_sensors::data_description::allow_uptime_sensors` | Create uptime sensors for network clients. | Skapa sensorer för upptid för nätverksklienter. | Source-path follow-up open |
| 19564 | 836904031 | `component::unifi::options::step::statistics_sensors::data_description::allow_bandwidth_sensors` | Create bandwidth usage sensors for network clients. | Skapa sensorer för bandbreddsanvändning för nätverksklienter. | Source-path follow-up open |
| 19565 | 836904030 | `component::unifi::options::step::simple_options::data_description::track_devices` | Create device tracker entities for Ubiquiti network devices. | Skapa enhetsspårningsentiteter för Ubiquiti-nätverksenheter. | Source-path follow-up open |
| 19566 | 836904029 | `component::unifi::options::step::simple_options::data_description::track_clients` | Create device tracker entities for network clients. | Skapa enhetsspårningsentiteter för nätverksklienter. | Source-path follow-up open |
| 19567 | 836904028 | `component::unifi::options::step::simple_options::data_description::block_client` | Select clients whose network access you want to control via switches. | Välj klienter vars nätverksåtkomst du vill styra via brytare. | Source-path follow-up open |
| 19568 | 836904027 | `component::unifi::options::step::device_tracker::data_description::track_wired_clients` | Include wired clients in device tracking. | Inkludera trådbundna klienter i enhetsspårning. | Source-path follow-up open |
| 19569 | 836904026 | `component::unifi::options::step::device_tracker::data_description::track_devices` | Create device tracker entities for Ubiquiti network devices. | Skapa enhetsspårningsentiteter för Ubiquiti-nätverksenheter. | Source-path follow-up open |
| 19570 | 836904025 | `component::unifi::options::step::device_tracker::data_description::track_clients` | Create device tracker entities for network clients. | Skapa enhetsspårningsentiteter för nätverksklienter. | Source-path follow-up open |
| 19571 | 836904024 | `component::unifi::options::step::device_tracker::data_description::ssid_filter` | Only track wireless clients connected to selected SSIDs. | Spåra endast trådlösa klienter anslutna till utvalda SSID:er. | Source-path follow-up open |
| 19572 | 836904023 | `component::unifi::options::step::device_tracker::data_description::ignore_wired_bug` | Disable workaround for a UniFi Network bug that sometimes reports wired clients as wireless. | Inaktivera lösningen för ett UniFi Network-fel som ibland rapporterar trådbundna klienter som trådlösa. | Source-path follow-up open |
| 19573 | 836904022 | `component::unifi::options::step::device_tracker::data_description::detection_time` | Number of seconds since last seen before a client is considered away. | Antal sekunder sedan senast sedd innan en klient anses vara borta. | Source-path follow-up open |
| 19574 | 836904021 | `component::unifi::options::step::configure_entity_sources::data_description::client_source` | Select which network clients to create entities from. | Välj vilka nätverksklienter du vill skapa enheter från. | Source-path follow-up open |
| 19575 | 836904020 | `component::unifi::options::step::client_control::data_description::poe_clients` | Enable switches to control PoE power for clients. | Aktivera omkopplare för att styra PoE-strömförsörjningen till klienterna. | Source-path follow-up open |
| 19576 | 836904019 | `component::unifi::options::step::client_control::data_description::dpi_restrictions` | Enable switches to control DPI restriction groups. | Aktivera omkopplare för att styra DPI-begränsningsgrupper. | Source-path follow-up open |
| 19577 | 836904018 | `component::unifi::options::step::client_control::data_description::block_client` | Select clients whose network access you want to control via switches. | Välj klienter vars nätverksåtkomst du vill styra via brytare. | Source-path follow-up open |
| 19578 | 836904017 | `component::unifi::config::step::user::data_description::verify_ssl` | Whether to verify the SSL certificate of the UniFi Network. | Om SSL-certifikatet för UniFi Network ska verifieras. | Core-literal match |
| 19579 | 836904016 | `component::unifi::config::step::user::data_description::username` | The username of the local UniFi Network user. | Användarnamnet för den lokala användaren i UniFi Network. | Core-literal match |
| 19580 | 836904015 | `component::unifi::config::step::user::data_description::port` | The port your UniFi Network is running on. | Porten som UniFi Network körs på. | Core-literal match |
| 19581 | 836904014 | `component::unifi::config::step::user::data_description::password` | The password of the local UniFi Network user. | Lösenordet för den lokala användaren i UniFi Network. | Core-literal match |
| 19582 | 836904013 | `component::unifi::config::step::site::data_description::site` | The site ID of the UniFi Network site to manage. | Plats-ID för den UniFi Network-plats som ska hanteras. | Core-literal match |
| 19583 | 836873688 | `component::fumis::exceptions::unknown_error::message` | An unexpected error occurred while communicating with the Fumis online service: {error} | Ett oväntat fel uppstod vid kommunikation med Fumis onlinetjänst: {error} | Core-literal match |
| 19584 | 836873687 | `component::fumis::exceptions::stove_offline::message` | Your stove's Fumis WiRCU Wi-Fi module is not connected to the internet. | Din kamins Fumis WiRCU Wi-Fi-modul är inte ansluten till internet. | Core-literal match |
| 19585 | 836873686 | `component::fumis::exceptions::communication_error::message` | An error occurred while communicating with the Fumis online service: {error} | Ett fel uppstod vid kommunikation med Fumis onlinetjänst: {error} | Core-literal match |
| 19586 | 836873685 | `component::fumis::exceptions::authentication_error::message` | Authentication with the Fumis online service failed. Check your MAC address and PIN code. | Autentiseringen med Fumis onlinetjänst misslyckades. Kontrollera din MAC-adress och PIN-kod. | Core-literal match |
| 19587 | 836873684 | `component::fumis::config::step::user::description` | Integrate your Fumis-based pellet stove with Home Assistant to monitor and control it. You can see your stove's temperature, heating status, and adjust the target temperature right from your dashboard or use it in your automations. This way, you can make sure your home is always nice, warm, and comfortable. | Integrera din Fumis-baserade pelletskamin med Home Assistant för att övervaka och styra den. Du kan se kaminens temperatur och värmestatus samt justera måltemperaturen direkt från din kontrollpanel eller använda den i dina automatiseringar. På så sätt kan du se till att ditt hem alltid är skönt, varmt och behagligt. | Core-literal match |
| 19588 | 836873683 | `component::fumis::config::step::user::data_description::pin` | You can find the PIN code on the label of the Fumis WiRCU Wi-Fi module connected to your stove. | PIN-koden finns på etiketten på den Fumis WiRCU Wi-Fi-modul som är ansluten till din kamin. | Core-literal match |
| 19589 | 836873682 | `component::fumis::config::step::user::data_description::mac` | The MAC address is a unique code of letters and numbers that identifies your stove. You can find it on the label of the Fumis WiRCU Wi-Fi module connected to your stove. | MAC-adressen är en unik kod bestående av bokstäver och siffror som identifierar din kamin. Du hittar den på etiketten på Fumis WiRCU Wi-Fi-modul som är ansluten till din kamin. | Core-literal match |
| 19590 | 836873681 | `component::fumis::config::step::user::data::pin` | PIN code | PIN-kod | Shared reference target checked |
| 19591 | 836873680 | `component::fumis::config::step::user::data::mac` | MAC address | MAC-adress | Core-literal match |
| 19592 | 836873679 | `component::fumis::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 19593 | 836873678 | `component::fumis::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 19594 | 836873677 | `component::fumis::config::error::device_offline` | Your stove's Fumis WiRCU Wi-Fi module is not connected to the internet. Make sure the module has power and is connected to your Wi-Fi network. | Din kamins Fumis WiRCU Wi-Fi-modul är inte ansluten till internet. Se till att modulen har ström och är ansluten till ditt Wi-Fi-nätverk. | Core-literal match |
| 19595 | 836873676 | `component::fumis::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 19596 | 836873675 | `component::fumis::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 19597 | 836838637 | `component::actron_air::exceptions::temperature_missing::message` | Provide a temperature value when adjusting the climate entity. | Ange ett temperaturvärde när du justerar klimatenheten. | Core-literal match |
| 19598 | 836835391 | `component::technove::entity::sensor::status::state::ventilation_required` | Ventilation required | Ventilation krävs | Core-literal match |
| 19599 | 836835390 | `component::technove::entity::sensor::status::state::pilot_fault` | Pilot fault | Pilotfel | Core-literal match |
| 19600 | 836835389 | `component::technove::entity::sensor::status::state::ground_fault` | Ground fault | Jordfel | Core-literal match |
| 19601 | 836835388 | `component::technove::entity::sensor::status::state::evse_fault` | EVSE fault | EVSE-fel | Core-literal match |
| 19602 | 836800820 | `component::knx::config_panel::expose::create::copy_info` | Copying options of {entity_name} ({entity_id}). | Kopierar alternativ för {entity_name} ({entity_id}). | Core-literal match |
| 19603 | 836800819 | `component::knx::config_panel::common::group_addresses` | Group addresses | Gruppadresser | Core-literal match |
| 19604 | 836800818 | `component::knx::config_panel::common::group_address` | Group address | Gruppadress | Core-literal match |
| 19605 | 836747260 | `component::homeassistant::issues::unsupported_local_deps::title` | Deprecation notice: Installation method | Meddelande om utfasning: Installationsmetod | Core-literal match |
| 19606 | 836747259 | `component::homeassistant::issues::unsupported_local_deps::description` | This system is running Home Assistant outside a virtual environment or a Docker container. This is not supported and will not work after the release of Home Assistant 2026.11. | Det här systemet kör Home Assistant utanför en virtuell miljö eller en Docker-container. Detta stöds inte och kommer inte att fungera efter lanseringen av Home Assistant 2026.11. | Core-literal match |
| 19607 | 836719576 | `component::imgw_pib::entity::sensor::ice_phenomena::name` | Ice phenomena | Isfenomen | Core-literal match |
| 19608 | 836533380 | `component::nobo_hub::exceptions::hub_not_found::message` | Nobø Ecohub with serial {serial} not found on the network. The hub may be offline or on a different subnet; will retry. | Nobø Ecohub med serienummer {serial} hittades inte i nätverket. Hubben kan vara offline eller befinna sig i ett annat subnät. Ett nytt försök kommer att göras. | Source-path follow-up open |
| 19609 | 836533379 | `component::nobo_hub::exceptions::cannot_connect_rediscovered::message` | Unable to connect to Nobø Ecohub at rediscovered IP {ip}; will retry. | Det går inte att ansluta till Nobø Ecohub via den återupptäckta IP-adressen {ip}; försöker igen. | Source-path follow-up open |
| 19610 | 836533378 | `component::nobo_hub::exceptions::cannot_connect_manual::message` | Unable to connect to Nobø Ecohub with serial {serial} at {ip}. If the hub has moved to a new IP address, remove and re-add the integration. | Det går inte att ansluta till Nobø Ecohub via serienummer {serial} på {ip}. Om hubben har bytt IP-adress ska du ta bort och lägga till integrationen på nytt. | Source-path follow-up open |
| 19611 | 836505226 | `component::victron_gx::common::yield_yesterday` | Yield yesterday | Avkastning i går | Core-literal match |
| 19612 | 836505225 | `component::victron_gx::common::yield_today` | Yield today | Avkastning i dag | Core-literal match |
| 19613 | 836505224 | `component::victron_gx::common::warning` | Warning | Varning | Core-literal match |
| 19614 | 836505223 | `component::victron_gx::common::voltage_on_phase` | Voltage on {phase} | Spänning på {phase} | Core-literal match |
| 19615 | 836505222 | `component::victron_gx::common::voltage_current_limited` | Voltage/current limited | Spänning/ström begränsad | Core-literal match |
| 19616 | 836505221 | `component::victron_gx::common::voltage` | Voltage | Spänning | Core-literal match |
| 19617 | 836505220 | `component::victron_gx::common::user_settings_invalid` | User settings invalid | Ogiltiga användarinställningar | Core-literal match |
| 19618 | 836505219 | `component::victron_gx::common::unknown` | Unknown | Okänd | Core-literal match |
| 19619 | 836505218 | `component::victron_gx::common::total_yield` | Total yield | Total avkastning | Core-literal match |
| 19620 | 836505217 | `component::victron_gx::common::total_pv_yield_user` | Total PV yield user | Total PV-avkastning för användare | Core-literal match |
| 19621 | 836505216 | `component::victron_gx::common::terminals_overheated` | Terminals overheated | Terminaler överhettade | Core-literal match |
| 19622 | 836505215 | `component::victron_gx::common::temperature` | Temperature | Temperatur | Core-literal match |
| 19623 | 836505214 | `component::victron_gx::common::synchronized_charging_config_issue` | Synchronized charging config issue | Problem med konfiguration av synkroniserad laddning | Core-literal match |
| 19624 | 836505213 | `component::victron_gx::common::sustain_alt` | Sustain alt | Sustain alt | Core-literal match |
| 19625 | 836505212 | `component::victron_gx::common::sustain` | Sustain | Sustain | Core-literal match |
| 19626 | 836505211 | `component::victron_gx::common::storage` | Storage | Lagring | Core-literal match |
| 19627 | 836505210 | `component::victron_gx::common::state` | State | Tillstånd | Core-literal match |
| 19628 | 836505209 | `component::victron_gx::common::starting_up` | Starting up | Startar upp | Core-literal match |
| 19629 | 836505208 | `component::victron_gx::common::shore_power` | Shore power | Landström | Core-literal match |
| 19630 | 836505207 | `component::victron_gx::common::sensor_battery_voltage` | Sensor battery voltage | Sensor batterispänning | Core-literal match |
| 19631 | 836505206 | `component::victron_gx::common::self_consumption` | Self-consumption | Egenförbrukning | Core-literal match |
| 19632 | 836505205 | `component::victron_gx::common::scheduled_recharging` | Scheduled recharging | Schemalagd uppladdning | Core-literal match |
| 19633 | 836505204 | `component::victron_gx::common::ripple_alarm` | Ripple alarm | Rippellarm | Core-literal match |
| 19634 | 836505203 | `component::victron_gx::common::reserved` | Reserved | Reserverad | Core-literal match |
| 19635 | 836505202 | `component::victron_gx::common::repeated_absorption` | Repeated absorption | Upprepad absorption | Core-literal match |
| 19636 | 836505201 | `component::victron_gx::common::recharging` | Recharging | Uppladdar | Core-literal match |
| 19637 | 836505200 | `component::victron_gx::common::pv_power_total` | PV power total | PV-effekt totalt | Core-literal match |
| 19638 | 836505199 | `component::victron_gx::common::pv_bus_voltage` | PV bus voltage | PV-buss spänning | Core-literal match |
| 19639 | 836505198 | `component::victron_gx::common::power_supply` | Power supply | Strömförsörjning | Core-literal match |
| 19640 | 836505197 | `component::victron_gx::common::power_phase` | Power {phase} | Effekt {phase} | Core-literal match |
| 19641 | 836505196 | `component::victron_gx::common::power_on_phase` | Power on {phase} | Effekt på {phase} | Core-literal match |
| 19642 | 836505195 | `component::victron_gx::common::power_assist` | Power Assist | Power Assist | Core-literal match |
| 19643 | 836505194 | `component::victron_gx::common::power` | Power | Effekt | Core-literal match |
| 19644 | 836505193 | `component::victron_gx::common::passthrough` | Passthrough | Genomströmning | Core-literal match |
| 19645 | 836505192 | `component::victron_gx::common::overload_alarm` | Overload alarm | Överbelastningslarm | Core-literal match |
| 19646 | 836505191 | `component::victron_gx::common::output_voltage_phase` | Output voltage {phase} | Utgångsspänning {phase} | Core-literal match |
| 19647 | 836505190 | `component::victron_gx::common::output_power_phase` | Output power {phase} | Utgångseffekt {phase} | Core-literal match |
| 19648 | 836505189 | `component::victron_gx::common::output_current_phase` | Output current {phase} | Utgångsström {phase} | Core-literal match |
| 19649 | 836505188 | `component::victron_gx::common::output_apparent_power_phase` | Output apparent power {phase} | Skenbar utgångseffekt {phase} | Core-literal match |
| 19650 | 836505187 | `component::victron_gx::common::ok` | Ok | Ok | Core-literal match |
| 19651 | 836505186 | `component::victron_gx::common::not_connected` | Not connected | Inte ansluten | Core-literal match |
| 19652 | 836505185 | `component::victron_gx::common::not_available` | Not available | Inte tillgänglig | Core-literal match |
| 19653 | 836505184 | `component::victron_gx::common::no_error` | No error | Inget fel | Core-literal match |
| 19654 | 836505183 | `component::victron_gx::common::no_alarm` | No alarm | Inget larm | Core-literal match |
| 19655 | 836505182 | `component::victron_gx::common::network_misconfigured` | Network misconfigured | Nätverket är felkonfigurerat | Core-literal match |
| 19656 | 836505181 | `component::victron_gx::common::mppt_active` | MPPT active | MPPT aktiv | Core-literal match |
| 19657 | 836505180 | `component::victron_gx::common::max_power_yesterday` | Max power yesterday | Maxeffekt i går | Core-literal match |
| 19658 | 836505179 | `component::victron_gx::common::max_power_today` | Max power today | Maxeffekt i dag | Core-literal match |
| 19659 | 836505178 | `component::victron_gx::common::low_power` | Low power | Låg ström | Core-literal match |
| 19660 | 836505177 | `component::victron_gx::common::lost_communication_with_device` | Lost communication with device | Förlorade kommunikation med enheten | Core-literal match |
| 19661 | 836505176 | `component::victron_gx::common::inverting` | Inverting | Växelriktar | Core-literal match |
| 19662 | 836505175 | `component::victron_gx::common::inverter_only` | Inverter only | Endast växelriktare | Core-literal match |
| 19663 | 836505174 | `component::victron_gx::common::invalid_incompatible_firmware` | Invalid/incompatible firmware | Ogiltig/inkompatibel firmware | Core-literal match |
| 19664 | 836505173 | `component::victron_gx::common::input_voltage_too_high_solar_panel` | Input voltage too high (solar panel) | För hög ingångsspänning (solpanel) | Core-literal match |
| 19665 | 836505172 | `component::victron_gx::common::input_voltage` | Input voltage | Ingångsspänning | Core-literal match |
| 19666 | 836505171 | `component::victron_gx::common::input_shutdown_reverse_current` | Input shutdown (reverse current) | Ingångsavstängning (omvänd ström) | Core-literal match |
| 19667 | 836505170 | `component::victron_gx::common::input_shutdown_battery_voltage_too_high` | Input shutdown (battery voltage too high) | Ingångsavstängning (överspänning i batteri) | Core-literal match |
| 19668 | 836505169 | `component::victron_gx::common::input_power` | Input power | Ingångseffekt | Core-literal match |
| 19669 | 836505168 | `component::victron_gx::common::input_current_too_high_solar_panel` | Input current too high (solar panel) | För hög ingångsström (solpanel) | Core-literal match |
| 19670 | 836505167 | `component::victron_gx::common::input_current` | Input current | Ingångsström | Core-literal match |
| 19671 | 836505166 | `component::victron_gx::common::high_temperature_alarm` | High temperature alarm | Larm för hög temperatur | Core-literal match |
| 19672 | 836505165 | `component::victron_gx::common::grid` | Grid | Elnät | Core-literal match |
| 19673 | 836505164 | `component::victron_gx::common::generator` | Generator | Generator | Core-literal match |
| 19674 | 836505163 | `component::victron_gx::common::frequency` | Frequency | Frekvens | Core-literal match |
| 19675 | 836505162 | `component::victron_gx::common::float` | Float | Flytande | Core-literal match |
| 19676 | 836505161 | `component::victron_gx::common::factory_calibration_data_lost` | Factory calibration data lost | Fabriksinställningarna har gått förlorade | Core-literal match |
| 19677 | 836505160 | `component::victron_gx::common::external_control` | External control | Extern styrning | Core-literal match |
| 19678 | 836505159 | `component::victron_gx::common::ess_mode` | ESS mode | ESS-läge | Core-literal match |
| 19679 | 836505158 | `component::victron_gx::common::error_code` | Error code | Felkod | Core-literal match |
| 19680 | 836505157 | `component::victron_gx::common::equalize` | Equalize | Utjämna | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 837199436 | `component::duco::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 836904032 | `component::unifi::options::step::statistics_sensors::data_description::allow_uptime_sensors` | Create uptime sensors for network clients. |
| 836904031 | `component::unifi::options::step::statistics_sensors::data_description::allow_bandwidth_sensors` | Create bandwidth usage sensors for network clients. |
| 836904030 | `component::unifi::options::step::simple_options::data_description::track_devices` | Create device tracker entities for Ubiquiti network devices. |
| 836904029 | `component::unifi::options::step::simple_options::data_description::track_clients` | Create device tracker entities for network clients. |
| 836904028 | `component::unifi::options::step::simple_options::data_description::block_client` | Select clients whose network access you want to control via switches. |
| 836904027 | `component::unifi::options::step::device_tracker::data_description::track_wired_clients` | Include wired clients in device tracking. |
| 836904026 | `component::unifi::options::step::device_tracker::data_description::track_devices` | Create device tracker entities for Ubiquiti network devices. |
| 836904025 | `component::unifi::options::step::device_tracker::data_description::track_clients` | Create device tracker entities for network clients. |
| 836904024 | `component::unifi::options::step::device_tracker::data_description::ssid_filter` | Only track wireless clients connected to selected SSIDs. |
| 836904023 | `component::unifi::options::step::device_tracker::data_description::ignore_wired_bug` | Disable workaround for a UniFi Network bug that sometimes reports wired clients as wireless. |
| 836904022 | `component::unifi::options::step::device_tracker::data_description::detection_time` | Number of seconds since last seen before a client is considered away. |
| 836904021 | `component::unifi::options::step::configure_entity_sources::data_description::client_source` | Select which network clients to create entities from. |
| 836904020 | `component::unifi::options::step::client_control::data_description::poe_clients` | Enable switches to control PoE power for clients. |
| 836904019 | `component::unifi::options::step::client_control::data_description::dpi_restrictions` | Enable switches to control DPI restriction groups. |
| 836904018 | `component::unifi::options::step::client_control::data_description::block_client` | Select clients whose network access you want to control via switches. |
| 836533380 | `component::nobo_hub::exceptions::hub_not_found::message` | Nobø Ecohub with serial {serial} not found on the network. The hub may be offline or on a different subnet; will retry. |
| 836533379 | `component::nobo_hub::exceptions::cannot_connect_rediscovered::message` | Unable to connect to Nobø Ecohub at rediscovered IP {ip}; will retry. |
| 836533378 | `component::nobo_hub::exceptions::cannot_connect_manual::message` | Unable to connect to Nobø Ecohub with serial {serial} at {ip}. If the hub has moved to a new IP address, remove and re-add the integration. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
