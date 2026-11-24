# Home Assistant Core – historisk avstämning 16081–16200

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 89 direkta källtexter matchar HA Core-källan; 27 referensanvändningar med 14 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 4 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 16081 | 878430084 | `component::synology_dsm::entity::select::fan_speed_mode::name` | Fan speed mode | Läge för fläkthastighet | Core-literal match |
| 16082 | 878422209 | `component::bsblan::issues::outdated_firmware::title` | Update your BSB-LAN firmware | Uppdatera firmware för BSB-LAN | Core-literal match |
| 16083 | 878422208 | `component::bsblan::issues::outdated_firmware::description` | Your BSB-LAN device is running firmware {firmware_version}, which uses an older JSON-API version that only supports a reduced set of features. Update your BSB-LAN firmware to enable full support, including multiple heating circuits. | Din BSB-LAN-enhet kör firmwareversionen {firmware_version}, som använder en äldre version av JSON-API som endast stöder en begränsad uppsättning funktioner. Uppdatera din BSB-LAN-firmware för att få fullt stöd, inklusive flera värmekretsar. | Core-literal match |
| 16084 | 878422207 | `component::bsblan::exceptions::setup_outdated_firmware::message` | Your BSB-LAN device is running firmware {firmware_version}, which is no longer supported. Please update your BSB-LAN board firmware to a newer version to keep using this integration. | Din BSB-LAN-enhet kör firmwareversionen {firmware_version}, som inte längre stöds. Uppdatera firmware på ditt BSB-LAN-kort till en nyare version för att kunna fortsätta använda denna integration. | Core-literal match |
| 16085 | 878422206 | `component::bsblan::exceptions::coordinator_state_error::message` | Error while fetching state data for heating circuit {circuit} from the BSB-LAN device at {host} | Fel vid hämtning av tillståndsdata för värmekretsen {circuit} från BSB-LAN-enheten på {host} | Core-literal match |
| 16086 | 878422182 | `component::yoto::entity::switch::night_mode_auto_brightness::name` | Night mode automatic brightness | Nattläge automatisk ljusstyrka | Core-literal match |
| 16087 | 878422181 | `component::yoto::entity::switch::max_headphone_volume::name` | Maximum headphone volume | Högsta volym för hörlurar | Core-literal match |
| 16088 | 878422180 | `component::yoto::entity::switch::day_mode_auto_brightness::name` | Day mode automatic brightness | Dagläge automatisk ljusstyrka | Core-literal match |
| 16089 | 878422179 | `component::yoto::entity::switch::bluetooth_pairing::name` | Bluetooth pairing | Bluetooth-parkoppling | Core-literal match |
| 16090 | 878419875 | `component::airos::exceptions::unknown::message` | Unexpected error | Oväntat fel | Shared reference target checked |
| 16091 | 878418700 | `component::melcloud_home::entity::binary_sensor::holiday_mode::name` | Holiday mode | Semesterläge | Core-literal match |
| 16092 | 878267658 | `component::aqvify::entity::sensor::stored_volume::name` | Stored volume | Lagrad volym | Source-path follow-up open |
| 16093 | 878267657 | `component::aqvify::entity::sensor::out_volume::name` | Outflow | Utflöde | Core-literal match |
| 16094 | 878267656 | `component::aqvify::entity::sensor::in_flow::name` | Inflow | Inflöde | Core-literal match |
| 16095 | 878267655 | `component::aqvify::entity::sensor::ground_water_level::name` | Ground water level | Grundvattennivå | Core-literal match |
| 16096 | 878111774 | `component::saj::issues::deprecated_yaml_import_issue_unknown::title` | {domain} YAML configuration import failed | {domain} Import av YAML-konfiguration misslyckades | Shared reference target checked |
| 16097 | 878111773 | `component::saj::issues::deprecated_yaml_import_issue_unknown::description` | Configuring {integration_title} using the YAML sensor platform is deprecated.<br><br>An unexpected error occurred while importing your configuration. Restart Home Assistant to try again, or remove the `sensor` / `saj` YAML and add the integration from the UI. | Konfigurering av {integration_title} med YAML sensorplattformen är föråldrat.<br><br>Ett oväntat fel uppstod när din konfiguration importerades. Starta om Home Assistant för att försöka igen, eller ta bort `sensor` / `saj` från YAML och lägg till integrationen via användargränssnittet istället. | Core-literal match |
| 16098 | 878111772 | `component::saj::issues::deprecated_yaml_import_issue_invalid_auth::title` | {domain} YAML configuration import failed | {domain} Import av YAML-konfiguration misslyckades | Core-literal match |
| 16099 | 878111771 | `component::saj::issues::deprecated_yaml_import_issue_invalid_auth::description` | Configuring {integration_title} using the YAML sensor platform is deprecated.<br><br>The username or password in your YAML was rejected. Update the credentials in YAML and restart, or remove the `sensor` / `saj` YAML and set up the integration from the UI. | Konfigurering av {integration_title} med YAML sensorplattformen är föråldrat.<br><br>Användarnamnet eller lösenordet i din YAML avvisades. Uppdatera inloggningsuppgifterna i YAML och starta om, eller ta bort `sensor` / `saj` från YAML och lägg till integrationen via användargränssnittet istället. | Core-literal match |
| 16100 | 878111770 | `component::saj::issues::deprecated_yaml_import_issue_cannot_connect::title` | {domain} YAML configuration import failed | {domain} Import av YAML-konfiguration misslyckades | Core-literal match |
| 16101 | 878111769 | `component::saj::issues::deprecated_yaml_import_issue_cannot_connect::description` | Configuring {integration_title} using the YAML sensor platform is deprecated.<br><br>Home Assistant could not reach the inverter while importing your configuration. Check the host, network, and that the device is an SAJ inverter, then restart to retry the import, or remove the `sensor` / `saj` YAML and add the integration from the UI. | Konfigurering av {integration_title} med YAML sensorplattformen är föråldrat.<br><br>Home Assistant kunde inte nå växelriktaren när din konfiguration importerades. Kontrollera värd, nätverk och att enheten är en SAJ-växelriktare. Starta sedan om för att försöka importera igen, eller ta bort `sensor` / `saj` från YAML och lägg till integrationen via användargränssnittet istället. | Core-literal match |
| 16102 | 878111768 | `component::saj::config::step::user::description` | Configure your SAJ solar inverter. Enter the IP address or hostname. If you use Wi-Fi, username and password are optional here (open networks); if login is required you can enter them now or on the next step after we detect the inverter. | Konfigurera din SAJ-solcellsväxelriktare. Ange IP-adressen eller värdnamnet. Om du använder Wi-Fi är användarnamn och lösenord valfria här (öppna nätverk). Om inloggning krävs kan du ange dem nu eller i nästa steg, efter att vi har identifierat växelriktaren. | Core-literal match |
| 16103 | 878111767 | `component::saj::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 16104 | 878111766 | `component::saj::config::step::user::data::type` | Connection type | Anslutningstyp | Core-literal match |
| 16105 | 878111765 | `component::saj::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 16106 | 878111764 | `component::saj::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 16107 | 878111763 | `component::saj::config::step::device_credentials::title` | Device credentials | Enhetsuppgifter | Core-literal match |
| 16108 | 878111762 | `component::saj::config::step::device_credentials::description` | The inverter requires a Wi-Fi login. Enter or correct username and password. | Växelriktaren krävde inloggning via Wi-Fi. Ange eller korrigera användarnamn och lösenord. | Core-literal match |
| 16109 | 878111761 | `component::saj::config::step::device_credentials::data::username` | Username | Användarnamn | Shared reference target checked |
| 16110 | 878111760 | `component::saj::config::step::device_credentials::data::password` | Password | Lösenord | Shared reference target checked |
| 16111 | 878111759 | `component::saj::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 16112 | 878111758 | `component::saj::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 16113 | 878111757 | `component::saj::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16114 | 878111756 | `component::saj::config::abort::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 16115 | 878111755 | `component::saj::config::abort::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 16116 | 878111754 | `component::saj::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16117 | 878111753 | `component::saj::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 16118 | 877884340 | `component::steam_online::config::step::user::data_description::api_key` | Your Steam Web API key | Din Steam Web API-nyckel | Core-literal match |
| 16119 | 877884339 | `component::steam_online::config::step::user::data_description::account` | Your Steam account ID (SteamID64) | Ditt Steam konto-ID (SteamID64) | Core-literal match |
| 16120 | 877853263 | `component::nest::entity::sensor::fan_timer_timeout::name` | Fan timer timeout | Timeout för fläkttimer | Core-literal match |
| 16121 | 877546447 | `component::unifiprotect::issues::rtsp_disabled::title` | No stream is available for camera {camera} | Ingen ström är tillgänglig för kameran {camera} | Core-literal match |
| 16122 | 877546446 | `component::unifiprotect::issues::rtsp_disabled::fix_flow::step::start::title` | No stream is available for camera {camera} | Ingen ström är tillgänglig för kameran {camera} | Core-literal match |
| 16123 | 877546445 | `component::unifiprotect::issues::rtsp_disabled::fix_flow::step::start::description` | No RTSPS stream is available for the camera {camera}, so it cannot live stream within Home Assistant. Until a stream is enabled, live views fall back to rapidly pulling snapshots (effectively a slideshow), which can put significant load on your UniFi Protect console. Confirm this repair and Home Assistant will create the highest quality RTSPS stream for you through the UniFi Protect public API. | Det finns ingen RTSPS-ström tillgänglig för kameran {camera}, vilket innebär att den inte kan livestreamas i Home Assistant. Tills en ström aktiveras faller livevisningarna tillbaka till att snabbt hämta ögonblicksbilder (i praktiken ett bildspel), vilket kan belasta din UniFi Protect-konsol avsevärt. Om du bekräftar denna åtgärd så kommer Home Assistant att skapa en RTSPS-ström av högsta kvalitet åt dig via UniFi Protects offentliga API. | Core-literal match |
| 16124 | 877546444 | `component::unifiprotect::issues::rtsp_disabled::fix_flow::step::confirm::title` | No stream is available for camera {camera} | Ingen ström är tillgänglig för kameran {camera} | Shared reference target checked |
| 16125 | 877546443 | `component::unifiprotect::issues::rtsp_disabled::fix_flow::step::confirm::description` | Home Assistant could not enable an RTSPS stream for {camera}. You may need to enable a stream manually on the camera, or disable the camera entity if you only need snapshots. | Home Assistant kunde inte aktivera en RTSPS-ström för {camera}. Du kan behöva aktivera strömmen manuellt på kameran, eller inaktivera kameraentiteten om du endast behöver stillbilder. | Core-literal match |
| 16126 | 877546442 | `component::unifiprotect::issues::insecure_camera_removed::title` | Insecure camera entity removed | Osäker kameraentitet har tagits bort | Core-literal match |
| 16127 | 877546441 | `component::unifiprotect::issues::insecure_camera_removed::description` | The camera entity `{entity_id}` used plain RTSP, which is no longer available now that streams come from the UniFi Protect public API (RTSPS only). It has been removed; use `{replacement}` instead.<br><br>Update the following automations and scripts:<br>{items} | Kameraentiteten `{entity_id}` använde vanlig RTSP, vilket inte längre är tillgängligt nu när strömmar kommer från UniFi Protects publika API (endast RTSPS). Den har nu tagits bort - använd `{replacement}` istället.<br><br>Uppdatera följande automatiseringar och skript:<br>{items} | Core-literal match |
| 16128 | 877546440 | `component::unifiprotect::exceptions::public_bootstrap_failed::message` | Could not load the public API bootstrap for camera streams | Det gick inte att läsa in initieringsdata från det offentliga API:et för kameraströmmar. | Core-literal match |
| 16129 | 877520224 | `component::overkiz::entity::sensor::battery::state::absence` | Absent | Frånvarande | Core-literal match |
| 16130 | 877260391 | `component::wattwaechter::exceptions::update_failed::message` | Failed to fetch data: {error} | Det gick inte att hämta data: {error} | Core-literal match |
| 16131 | 877260390 | `component::wattwaechter::exceptions::no_meter_data::message` | No meter data available from {host} yet | Det finns ännu inga mätdata tillgängliga från {host} | Core-literal match |
| 16132 | 877260389 | `component::wattwaechter::exceptions::cannot_connect::message` | Cannot connect to {host} | Kan inte ansluta till {host} | Core-literal match |
| 16133 | 877260388 | `component::wattwaechter::exceptions::auth_failed::message` | Authentication failed: {error} | Autentiseringen misslyckades: {error} | Core-literal match |
| 16134 | 877260387 | `component::wattwaechter::entity::sensor::voltage_phase::name` | Voltage {phase} | Spänning {phase} | Core-literal match |
| 16135 | 877260386 | `component::wattwaechter::entity::sensor::power_factor_phase::name` | Power factor {phase} | Effektfaktor {phase} | Core-literal match |
| 16136 | 877260385 | `component::wattwaechter::entity::sensor::import_total::name` | Total consumption | Total förbrukning | Core-literal match |
| 16137 | 877260384 | `component::wattwaechter::entity::sensor::import_tariff_2::name` | Consumption tariff 2 | Förbrukningstariff 2 | Core-literal match |
| 16138 | 877260383 | `component::wattwaechter::entity::sensor::import_tariff_1::name` | Consumption tariff 1 | Förbrukningstariff 1 | Core-literal match |
| 16139 | 877260382 | `component::wattwaechter::entity::sensor::frequency::name` | Grid frequency | Nätfrekvens | Core-literal match |
| 16140 | 877260381 | `component::wattwaechter::entity::sensor::export_total::name` | Total feed-in | Total inmatning | Core-literal match |
| 16141 | 877260380 | `component::wattwaechter::entity::sensor::export_tariff_2::name` | Feed-in tariff 2 | Inmatningstariff 2 | Core-literal match |
| 16142 | 877260379 | `component::wattwaechter::entity::sensor::export_tariff_1::name` | Feed-in tariff 1 | Inmatningstariff 1 | Core-literal match |
| 16143 | 877260378 | `component::wattwaechter::entity::sensor::current_phase::name` | Current {phase} | Ström {phase} | Core-literal match |
| 16144 | 877260377 | `component::wattwaechter::entity::sensor::active_power_phase::name` | Active power {phase} | Aktiv effekt {phase} | Core-literal match |
| 16145 | 877260376 | `component::wattwaechter::entity::sensor::active_power::name` | Active power | Aktiv effekt | Core-literal match |
| 16146 | 877260375 | `component::wattwaechter::config::step::zeroconf_confirm::title` | WattWächter discovered | WattWächter Plus har upptäckts | Core-literal match |
| 16147 | 877260374 | `component::wattwaechter::config::step::zeroconf_confirm::description` | A WattWächter device was found on your network.<br><br>Model: {model}<br>Firmware: {firmware}<br>Host: {host}<br>Device ID: {device_id} | En WattWächter-enhet hittades i ditt nätverk.<br><br>Modell: {model}<br>Inbyggd programvara: {firmware}<br>Värd: {host}<br>Enhets-ID: {device_id} | Core-literal match |
| 16148 | 877260373 | `component::wattwaechter::config::step::user::title` | Add WattWächter | Lägg till WattWächter Plus | Core-literal match |
| 16149 | 877260372 | `component::wattwaechter::config::step::user::data_description::host` | The hostname or IP address of your WattWächter device. | Värdnamnet eller IP-adressen för din WattWächter Plus-enhet. | Core-literal match |
| 16150 | 877260371 | `component::wattwaechter::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 16151 | 877260370 | `component::wattwaechter::config::step::auth::title` | Authentication required | Autentisering krävs | Core-literal match |
| 16152 | 877260369 | `component::wattwaechter::config::step::auth::data_description::token` | The API token for your WattWächter device. | API-token för din WattWächter Plus-enhet. | Core-literal match |
| 16153 | 877260368 | `component::wattwaechter::config::step::auth::data::token` | API token | API-token | Shared reference target checked |
| 16154 | 877260367 | `component::wattwaechter::config::error::unknown` | Unexpected error | Oväntat fel | Source-path follow-up open |
| 16155 | 877260366 | `component::wattwaechter::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 16156 | 877260365 | `component::wattwaechter::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16157 | 877260364 | `component::wattwaechter::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16158 | 877260363 | `component::wattwaechter::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 16159 | 877219410 | `component::melcloud_home::entity::binary_sensor::overheat_protection::name` | Overheat protection | Överhettningsskydd | Core-literal match |
| 16160 | 877219409 | `component::melcloud_home::entity::binary_sensor::frost_protection::name` | Frost protection | Frostskydd | Core-literal match |
| 16161 | 877205912 | `component::homeassistant::exceptions::service_found_no_config_entry_for_domain::message` | Could not find config entry for integration {domain}. | Kunde inte hitta någon konfigurationspost för integration {domain}. | Core-literal match |
| 16162 | 877205911 | `component::homeassistant::exceptions::service_found_multiple_config_entry_for_domain::message` | Found multiple config entries for integration {domain}. | Hittade flera konfigurationsposter för integration {domain}. | Core-literal match |
| 16163 | 877185806 | `component::chef_iq::entity::sensor::soc_temperature::name` | SoC temperature | SoC-temperatur | Core-literal match |
| 16164 | 877185805 | `component::chef_iq::entity::sensor::probe_tip_4_temperature::name` | Probe tip 4 temperature | Temperatur på sondspets 4 | Core-literal match |
| 16165 | 877185804 | `component::chef_iq::entity::sensor::probe_tip_3_temperature::name` | Probe tip 3 temperature | Temperatur på sondspets 3 | Core-literal match |
| 16166 | 877185803 | `component::chef_iq::entity::sensor::probe_tip_2_temperature::name` | Probe tip 2 temperature | Temperatur på sondspets 2 | Core-literal match |
| 16167 | 877185802 | `component::chef_iq::entity::sensor::probe_tip_1_temperature::name` | Probe tip 1 temperature | Temperatur på sondspets 1 | Core-literal match |
| 16168 | 877185801 | `component::chef_iq::entity::sensor::food_temperature::name` | Food temperature | Matens temperatur | Core-literal match |
| 16169 | 877185800 | `component::chef_iq::entity::sensor::ambient_temperature::name` | Ambient temperature | Omgivningstemperatur | Core-literal match |
| 16170 | 877185799 | `component::chef_iq::config::step::user::description` | Choose a device to set up | Välj en enhet att konfigurera | Shared reference target checked |
| 16171 | 877185798 | `component::chef_iq::config::step::user::data_description::address` | Select the Chef iQ probe you want to set up | Välj den Chef iQ-sond som du vill ställa in | Core-literal match |
| 16172 | 877185797 | `component::chef_iq::config::step::user::data::address` | Device | Enhet | Shared reference target checked |
| 16173 | 877185796 | `component::chef_iq::config::step::bluetooth_confirm::description` | Do you want to set up {name}? | Vill du konfigurera {name}? | Shared reference target checked |
| 16174 | 877185795 | `component::chef_iq::config::flow_title` | {name} | {name} | Core-literal match |
| 16175 | 877185794 | `component::chef_iq::config::abort::not_supported` | Device not supported | Enheten stöds inte | Core-literal match |
| 16176 | 877185793 | `component::chef_iq::config::abort::no_devices_found` | No devices found on the network | Inga enheter hittades i nätverket | Shared reference target checked |
| 16177 | 877185792 | `component::chef_iq::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 16178 | 877185791 | `component::chef_iq::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 16179 | 877183065 | `component::energieleser::entity::sensor::water_today_consumption::name` | Water today | Vatten idag | Core-literal match |
| 16180 | 877183064 | `component::energieleser::entity::sensor::water_flow_rate_m3::name` | Volume flow rate | Flödeshastighet | Source-path follow-up open |
| 16181 | 877183063 | `component::energieleser::entity::sensor::water_flow_rate::name` | Water flow rate | Vattenflödeshastighet | Core-literal match |
| 16182 | 877183062 | `component::energieleser::entity::sensor::water_consumption::name` | Total water | Total vattenförbrukning | Core-literal match |
| 16183 | 877183061 | `component::energieleser::entity::sensor::pulse_count::name` | Pulse count | Pulsräkning | Core-literal match |
| 16184 | 877183060 | `component::energieleser::entity::sensor::power_total::name` | Active power | Aktiv effekt | Core-literal match |
| 16185 | 877183059 | `component::energieleser::entity::sensor::power_phase::name` | Phase {phase} power | Effekt, fas {phase} | Core-literal match |
| 16186 | 877183058 | `component::energieleser::entity::sensor::heat_volume_flow::name` | Volume flow | Flödesvolym | Core-literal match |
| 16187 | 877183057 | `component::energieleser::entity::sensor::heat_total_volume::name` | Total volume | Total volym | Core-literal match |
| 16188 | 877183056 | `component::energieleser::entity::sensor::heat_return_temperature::name` | Return temperature | Returflödestemperatur | Core-literal match |
| 16189 | 877183055 | `component::energieleser::entity::sensor::heat_flow_temperature::name` | Flow temperature | Flödestemperatur | Core-literal match |
| 16190 | 877183054 | `component::energieleser::entity::sensor::heat_energy_tariff::name` | Energy tariff {tariff} | Energitariff {tariff} | Core-literal match |
| 16191 | 877183053 | `component::energieleser::entity::sensor::gas_consumption::name` | Total gas | Total gasförbrukning | Core-literal match |
| 16192 | 877183052 | `component::energieleser::entity::sensor::flow_rate::name` | Gas flow rate | Gasflödeshastighet | Core-literal match |
| 16193 | 877183051 | `component::energieleser::entity::sensor::energy_import::name` | Imported energy | Importerad energi | Core-literal match |
| 16194 | 877183050 | `component::energieleser::entity::sensor::energy_export::name` | Exported energy | Exporterad energi | Core-literal match |
| 16195 | 877183049 | `component::energieleser::config::step::zeroconf_confirm::title` | Add discovered device | Lägg till upptäckt enhet | Core-literal match |
| 16196 | 877183048 | `component::energieleser::config::step::zeroconf_confirm::description` | Found a {device_type} ({device_id}) at {host}. Add it to Home Assistant? | Hittade en {device_type} ({device_id}) på {host}. Lägga till den i Home Assistant? | Core-literal match |
| 16197 | 877183047 | `component::energieleser::config::step::user::title` | Add an energieleser device | Lägg till en energieleser-enhet | Core-literal match |
| 16198 | 877183046 | `component::energieleser::config::step::user::description` | Connect to a local energieleser device (stromleser.one, gasleser, wasserleser, or wärmeleser). | Anslut till en lokal energimätare (stromleser.one, gasmätare, vattenmätare eller värmemätare). | Core-literal match |
| 16199 | 877183045 | `component::energieleser::config::step::user::data_description::host` | Local IP address or hostname of the device (e.g. 192.168.1.42). | Enhetens lokala IP-adress eller värdnamn (t.ex. 192.168.1.42). | Core-literal match |
| 16200 | 877183044 | `component::energieleser::config::step::user::data::host` | Host | Värd | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 878267658 | `component::aqvify::entity::sensor::stored_volume::name` | Stored volume |
| 877260367 | `component::wattwaechter::config::error::unknown` | Unexpected error |
| 877185792 | `component::chef_iq::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |
| 877183064 | `component::energieleser::entity::sensor::water_flow_rate_m3::name` | Volume flow rate |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
