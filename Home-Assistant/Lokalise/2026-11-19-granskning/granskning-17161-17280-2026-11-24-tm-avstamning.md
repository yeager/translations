# Home Assistant Core – historisk avstämning 17161–17280

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 67 direkta källtexter matchar HA Core-källan; 50 referensanvändningar med 40 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 3 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 17161 | 863836562 | `component::toon::exceptions::communication_error::message` | An error occurred while communicating with the Toon device. | Ett fel uppstod vid kommunikationen med Toon-enheten. | Core-literal match |
| 17162 | 863777325 | `component::hassio::exceptions::supervisor_update_pending::message` | Supervisor was out-of-date during onboarding. Update triggered, will retry when complete | Supervisor var föråldrad under onboarding. Uppdatering påbörjad, försöker igen när den är klar | Core-literal match |
| 17163 | 863698176 | `component::lunatone::config::flow_title` | {name} ({model}) | {name} ({model}) | Core-literal match |
| 17164 | 863501735 | `component::ecovacs::exceptions::vacuum_send_command_not_supported::message` | The {command} command is not supported by {name} | Kommandot `{command}` stöds inte av {name} | Core-literal match |
| 17165 | 863361529 | `component::immich::exceptions::missing_api_permission::message` | Missing API permission ({msg}). | API-behörighet saknas ({msg}). | Core-literal match |
| 17166 | 863307248 | `component::mqtt::issues::protocol_5_migration::description` | The automatic migration to MQTT protocol version 5 failed. The currently configured protocol version for MQTT broker {broker} is {protocol}, but this protocol version is deprecated, and support for it will be removed.<br><br>Make sure your broker supports protocol version 5. Update your MQTT broker's connection settings, and restart Home Assistant to fix this issue. | Den automatiska migreringen till MQTT-protokollversion 5 misslyckades. Den för närvarande konfigurerade protokollversionen för MQTT-mäklaren {broker} är {protocol}, men den här protokollversionen är föråldrad och stödet för den kommer att tas bort. <br><br>Kontrollera att din mäklare stöder protokollversion 5. Uppdatera anslutningsinställningarna för din MQTT-mäklare och starta om Home Assistant för att åtgärda problemet. | Core-literal match |
| 17167 | 863055262 | `component::roborock::exceptions::network_error::message` | Network error connecting to Roborock servers. Check your internet connection and the Roborock service status. | Nätverksfel vid anslutning till Roborock-servrar. Kontrollera din internetanslutning och Roborock-tjänstens status. | Source-path follow-up open |
| 17168 | 862331896 | `component::analytics::exceptions::supervisor_not_ready::message` | Supervisor was not ready during setup, will retry | Supervisor var inte redo under konfigureringen. Försöker igen. | Core-literal match |
| 17169 | 862326118 | `component::apple_tv::exceptions::streaming_not_supported::message` | Streaming the requested media is not supported | Strömning av det begärda mediet stöds inte. | Core-literal match |
| 17170 | 862326117 | `component::apple_tv::exceptions::stream_failed::message` | Failed to stream media to the Apple TV | Det gick inte att strömma media till Apple TV. | Core-literal match |
| 17171 | 862313766 | `component::media_player::entity_component::projector::name` | Projector | Projektor | Core-literal match |
| 17172 | 862312310 | `component::broadlink::entity::radio_frequency::rf_transmitter::name` | RF transmitter | RF-sändare | Core-literal match |
| 17173 | 862261597 | `component::samsung_infrared::entity::button::yellow::name` | Yellow | Gul | Core-literal match |
| 17174 | 862261596 | `component::samsung_infrared::entity::button::up::name` | Up | Upp | Shared reference target checked |
| 17175 | 862261595 | `component::samsung_infrared::entity::button::tools::name` | Tools | Verktyg | Core-literal match |
| 17176 | 862261594 | `component::samsung_infrared::entity::button::source::name` | Source | Källa | Core-literal match |
| 17177 | 862261593 | `component::samsung_infrared::entity::button::settings::name` | Settings | Inställningar | Core-literal match |
| 17178 | 862261592 | `component::samsung_infrared::entity::button::right::name` | Right | Höger | Shared reference target checked |
| 17179 | 862261591 | `component::samsung_infrared::entity::button::rewind::name` | Rewind | Spola tillbaka | Core-literal match |
| 17180 | 862261590 | `component::samsung_infrared::entity::button::return::name` | Return | Retur | Core-literal match |
| 17181 | 862261589 | `component::samsung_infrared::entity::button::red::name` | Red | Röd | Core-literal match |
| 17182 | 862261588 | `component::samsung_infrared::entity::button::record::name` | Record | Spela in | Core-literal match |
| 17183 | 862261587 | `component::samsung_infrared::entity::button::previous_channel::name` | Previous channel | Föregående kanal | Core-literal match |
| 17184 | 862261586 | `component::samsung_infrared::entity::button::power::name` | Power | På/Av | Shared reference target checked |
| 17185 | 862261585 | `component::samsung_infrared::entity::button::ok::name` | OK | OK | Shared reference target checked |
| 17186 | 862261584 | `component::samsung_infrared::entity::button::num_9::name` | Number 9 | Nummer 9 | Shared reference target checked |
| 17187 | 862261583 | `component::samsung_infrared::entity::button::num_8::name` | Number 8 | Nummer 8 | Shared reference target checked |
| 17188 | 862261582 | `component::samsung_infrared::entity::button::num_7::name` | Number 7 | Nummer 7 | Shared reference target checked |
| 17189 | 862261581 | `component::samsung_infrared::entity::button::num_6::name` | Number 6 | Nummer 6 | Shared reference target checked |
| 17190 | 862261580 | `component::samsung_infrared::entity::button::num_5::name` | Number 5 | Nummer 5 | Shared reference target checked |
| 17191 | 862261579 | `component::samsung_infrared::entity::button::num_4::name` | Number 4 | Nummer 4 | Shared reference target checked |
| 17192 | 862261578 | `component::samsung_infrared::entity::button::num_3::name` | Number 3 | Nummer 3 | Shared reference target checked |
| 17193 | 862261577 | `component::samsung_infrared::entity::button::num_2::name` | Number 2 | Nummer 2 | Shared reference target checked |
| 17194 | 862261576 | `component::samsung_infrared::entity::button::num_1::name` | Number 1 | Nummer 1 | Shared reference target checked |
| 17195 | 862261575 | `component::samsung_infrared::entity::button::num_0::name` | Number 0 | Nummer 0 | Shared reference target checked |
| 17196 | 862261574 | `component::samsung_infrared::entity::button::left::name` | Left | Vänster | Shared reference target checked |
| 17197 | 862261573 | `component::samsung_infrared::entity::button::info::name` | Info | Info | Shared reference target checked |
| 17198 | 862261572 | `component::samsung_infrared::entity::button::home::name` | Home | Hem | Shared reference target checked |
| 17199 | 862261571 | `component::samsung_infrared::entity::button::green::name` | Green | Grön | Core-literal match |
| 17200 | 862261570 | `component::samsung_infrared::entity::button::fast_forward::name` | Fast forward | Spola fram | Core-literal match |
| 17201 | 862261569 | `component::samsung_infrared::entity::button::exit::name` | Exit | Avsluta | Shared reference target checked |
| 17202 | 862261568 | `component::samsung_infrared::entity::button::e_manual::name` | E-Manual | E-manual | Core-literal match |
| 17203 | 862261567 | `component::samsung_infrared::entity::button::down::name` | Down | Ner | Shared reference target checked |
| 17204 | 862261566 | `component::samsung_infrared::entity::button::browser::name` | Browser | Webbläsare | Core-literal match |
| 17205 | 862261565 | `component::samsung_infrared::entity::button::blue::name` | Blue | Blå | Core-literal match |
| 17206 | 862261564 | `component::samsung_infrared::entity::button::ad_subtitle::name` | AD/Subtitle | AD/Undertext | Core-literal match |
| 17207 | 861931600 | `component::ovhcloud_ai_endpoints::config::step::reauth_confirm::description` | The OVHcloud AI Endpoints API key is no longer valid. Please enter a new one. | API-nyckeln för OVHcloud AI Endpoints är inte längre giltig. Ange en ny. | Core-literal match |
| 17208 | 861931599 | `component::ovhcloud_ai_endpoints::config::step::reauth_confirm::data_description::api_key` | An OVHcloud AI Endpoints API key | En API-nyckel för OVHcloud AI Endpoints | Shared reference target checked |
| 17209 | 861931598 | `component::ovhcloud_ai_endpoints::config::step::reauth_confirm::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 17210 | 861931597 | `component::ovhcloud_ai_endpoints::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 17211 | 861797825 | `component::zone::triggers::occupancy_detected::name` | Zone occupancy detected | Närvaro i zonen har upptäckts | Core-literal match |
| 17212 | 861797824 | `component::zone::triggers::occupancy_detected::fields::zone::name` | Zone | Zon | Core-literal match |
| 17213 | 861797823 | `component::zone::triggers::occupancy_detected::fields::zone::description` | The zone to monitor. | Den zon som ska övervakas. | Core-literal match |
| 17214 | 861797822 | `component::zone::triggers::occupancy_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 17215 | 861797821 | `component::zone::triggers::occupancy_detected::description` | Triggers when one or more zones become occupied. | Utlöses när en eller flera zoner får närvaro. | Core-literal match |
| 17216 | 861797820 | `component::zone::triggers::occupancy_cleared::name` | Zone occupancy cleared | Ingen närvaro i zonen längre | Core-literal match |
| 17217 | 861797819 | `component::zone::triggers::occupancy_cleared::fields::zone::name` | Zone | Zon | Shared reference target checked |
| 17218 | 861797818 | `component::zone::triggers::occupancy_cleared::fields::zone::description` | The zone to monitor. | Den zon som ska övervakas. | Shared reference target checked |
| 17219 | 861797817 | `component::zone::triggers::occupancy_cleared::fields::for::name` | For at least | I minst | Shared reference target checked |
| 17220 | 861797816 | `component::zone::triggers::occupancy_cleared::description` | Triggers when one or more zones transition from occupied to unoccupied. | Utlöses när en eller flera zoner går från att ha närvaro till att vara tomma. | Core-literal match |
| 17221 | 861797815 | `component::zone::triggers::left::name` | Zone left | Lämnat zonen | Core-literal match |
| 17222 | 861797814 | `component::zone::triggers::left::fields::zone::name` | Zone | Zon | Shared reference target checked |
| 17223 | 861797813 | `component::zone::triggers::left::fields::zone::description` | The zone to trigger on. | Zon att utlösa på. | Shared reference target checked |
| 17224 | 861797812 | `component::zone::triggers::left::fields::for::name` | For at least | I minst | Shared reference target checked |
| 17225 | 861797811 | `component::zone::triggers::left::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 17226 | 861797810 | `component::zone::triggers::left::description` | Triggers when one or more persons or device trackers leave a zone. | Utlöses när en eller flera personer eller enhetsspårare lämnar en zon. | Core-literal match |
| 17227 | 861797809 | `component::zone::triggers::entered::name` | Zone entered | Gått in i zon | Core-literal match |
| 17228 | 861797808 | `component::zone::triggers::entered::fields::zone::name` | Zone | Zon | Shared reference target checked |
| 17229 | 861797807 | `component::zone::triggers::entered::fields::zone::description` | The zone to trigger on. | Zon att utlösa på. | Shared reference target checked |
| 17230 | 861797806 | `component::zone::triggers::entered::fields::for::name` | For at least | I minst | Shared reference target checked |
| 17231 | 861797805 | `component::zone::triggers::entered::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 17232 | 861797804 | `component::zone::triggers::entered::description` | Triggers when one or more persons or device trackers enter a zone. | Utlöses när en eller flera personer eller spårningsenheter går in i en zon. | Core-literal match |
| 17233 | 861797803 | `component::zone::common::trigger_zone_name` | Zone | Zon | Core-literal match |
| 17234 | 861797802 | `component::zone::common::trigger_zone_description` | The zone to trigger on. | Zon att utlösa på. | Core-literal match |
| 17235 | 861797801 | `component::zone::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 17236 | 861797800 | `component::zone::common::trigger_behavior_name` | Trigger when | Utlös när | Core-literal match |
| 17237 | 861275239 | `component::matter::entity::sensor::uptime::name` | Uptime | Upptid | Source-path follow-up open |
| 17238 | 861275238 | `component::matter::entity::sensor::reboot_count::name` | Reboot count | Antal omstarter | Core-literal match |
| 17239 | 861275237 | `component::matter::entity::sensor::boot_reason::state::unspecified` | Unspecified | Ospecificerad | Core-literal match |
| 17240 | 861275236 | `component::matter::entity::sensor::boot_reason::state::software_watchdog_reset` | Software watchdog reset | Omstart orsakad av programvarans övervakningstimer | Core-literal match |
| 17241 | 861275235 | `component::matter::entity::sensor::boot_reason::state::software_update_completed` | Software update completed | Programuppdatering slutförd | Core-literal match |
| 17242 | 861275234 | `component::matter::entity::sensor::boot_reason::state::software_reset` | Software reset | Omstart initierad av programvara | Core-literal match |
| 17243 | 861275233 | `component::matter::entity::sensor::boot_reason::state::power_on_reboot` | Power-on reboot | Omstart vid påslag | Core-literal match |
| 17244 | 861275232 | `component::matter::entity::sensor::boot_reason::state::hardware_watchdog_reset` | Hardware watchdog reset | Omstart orsakad av hårdvarans övervakningstimer | Core-literal match |
| 17245 | 861275231 | `component::matter::entity::sensor::boot_reason::state::brown_out_reset` | Brownout reset | Omstart vid spänningsfall | Core-literal match |
| 17246 | 861275230 | `component::matter::entity::sensor::boot_reason::name` | Boot reason | Startorsak | Core-literal match |
| 17247 | 861275229 | `component::matter::entity::binary_sensor::active_radio_faults::name` | Radio faults | Radiofel | Core-literal match |
| 17248 | 861275228 | `component::matter::entity::binary_sensor::active_network_faults::name` | Network faults | Nätverksfel | Core-literal match |
| 17249 | 861275227 | `component::matter::entity::binary_sensor::active_hardware_faults::name` | Hardware faults | Hårdvarufel | Core-literal match |
| 17250 | 861201938 | `component::tuya::entity::select::quick_heat_temperature::state::95` | 95 °C | 95 °C | Core-literal match |
| 17251 | 861201937 | `component::tuya::entity::select::quick_heat_temperature::state::90` | 90 °C | 90 °C | Core-literal match |
| 17252 | 861201936 | `component::tuya::entity::select::quick_heat_temperature::state::85` | 85 °C | 85 °C | Core-literal match |
| 17253 | 861201935 | `component::tuya::entity::select::quick_heat_temperature::state::80` | 80 °C | 80 °C | Core-literal match |
| 17254 | 861201934 | `component::tuya::entity::select::quick_heat_temperature::state::100` | 100 °C | 100 °C | Core-literal match |
| 17255 | 861201933 | `component::tuya::entity::select::quick_heat_temperature::name` | Quick heat temperature | Temperatur för snabb uppvärmning | Core-literal match |
| 17256 | 861201932 | `component::tuya::entity::select::kettle_work_mode::state::temp_setting` | Heat and keep warm | Värm upp och håll varmt | Core-literal match |
| 17257 | 861201931 | `component::tuya::entity::select::kettle_work_mode::state::temp_boiling` | Boil and keep warm | Koka upp och håll varmt | Core-literal match |
| 17258 | 861201930 | `component::tuya::entity::select::kettle_work_mode::state::setting_quick` | Quick heat | Snabb uppvärmning | Core-literal match |
| 17259 | 861201929 | `component::tuya::entity::select::kettle_work_mode::state::boiling_quick` | Quick boil | Snabbkokning | Core-literal match |
| 17260 | 861201928 | `component::tuya::entity::select::kettle_work_mode::name` | Work mode | Arbetsläge | Core-literal match |
| 17261 | 861156642 | `component::homeassistant_yellow::options::progress::uninstall_multiprotocol_addon` | Please wait while the {addon_name} app is uninstalled. | Vänta medan appen {addon_name} avinstalleras. | Shared reference target checked |
| 17262 | 861156641 | `component::homeassistant_yellow::options::progress::install_zigbee_firmware` | Please wait while Zigbee-only firmware is installed on your {hardware_name}. This can take several minutes. | Vänta medan Zigbee-only firmware installeras på din {hardware_name}. Detta kan ta flera minuter. | Shared reference target checked |
| 17263 | 861156640 | `component::homeassistant_yellow::issues::multi_pan_migration::title` | Multiprotocol support is deprecated | Stöd för flera protokoll är föråldrat | Core-literal match |
| 17264 | 861156639 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::step::uninstall_addon::title` | Remove IEEE 802.15.4 radio multiprotocol support | Ta bort stöd för multiprotokoll på IEEE 802.15.4-radio. | Shared reference target checked |
| 17265 | 861156638 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::step::uninstall_addon::description` | Multiprotocol support for the IEEE 802.15.4 radio in your {hardware_name} has been deprecated. Migrate the radio back to Zigbee-only firmware to keep it working in the future.<br><br>Disabling multiprotocol support will disable Thread support provided by the {hardware_name}. Your Thread devices will continue working only if you have another Thread border router nearby.<br><br>It will take a few minutes to install the Zigbee firmware and restore a backup. | Multiprotokollstödet för IEEE 802.15.4-radion i din {hardware_name} har tagits bort. Migrera radion tillbaka till enbart Zigbee-firmware för att den ska fungera i framtiden. <br><br>Om du inaktiverar multiprotokollstödet inaktiveras Thread-stödet som tillhandahålls av {hardware_name}. Dina Thread-enheter fortsätter att fungera endast om du har en annan Thread border-router i närheten. <br><br>Det tar några minuter att installera Zigbee-firmware och återställa en säkerhetskopia. | Core-literal match |
| 17266 | 861156637 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::step::uninstall_addon::data::disable_multi_pan` | Disable multiprotocol support | Inaktivera stöd för multiprotokoll | Shared reference target checked |
| 17267 | 861156636 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::progress::uninstall_multiprotocol_addon` | Please wait while the {addon_name} app is uninstalled. | Vänta medan appen {addon_name} avinstalleras. | Shared reference target checked |
| 17268 | 861156635 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::progress::install_zigbee_firmware` | Please wait while Zigbee-only firmware is installed on your {hardware_name}. This can take several minutes. | Vänta medan Zigbee-only firmware installeras på din {hardware_name}. Detta kan ta flera minuter. | Shared reference target checked |
| 17269 | 861156634 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::progress::install_addon` | Please wait while the {addon_name} app installation finishes. This can take several minutes. | Var god vänta medan installationen av tillägget {addon_name} slutförs. Detta kan ta flera minuter. | Shared reference target checked |
| 17270 | 861156633 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::abort::zha_migration_failed` | The ZHA migration did not succeed. | ZHA-migreringen misslyckades. | Shared reference target checked |
| 17271 | 861156632 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::abort::not_hassio` | The hardware options can only be configured on Home Assistant OS installations. | Hårdvarualternativen kan endast konfigureras på Home Assistant OS-installationer. | Shared reference target checked |
| 17272 | 861156631 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::abort::fw_install_failed` | {firmware_name} firmware failed to install, check Home Assistant logs for more information. | {firmware_name} firmware kunde inte installeras, kontrollera loggarna i Home Assistant för mer information. | Shared reference target checked |
| 17273 | 861156630 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::abort::addon_start_failed` | Failed to start the {addon_name} app. | Misslyckades att starta tillägget {addon_name}. | Shared reference target checked |
| 17274 | 861156629 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::abort::addon_set_config_failed` | Failed to set {addon_name} configuration. | Misslyckades med att spara konfigurationen för {addon_name}. | Shared reference target checked |
| 17275 | 861156628 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::abort::addon_install_failed` | Failed to install the {addon_name} app. | Misslyckades att installera tillägget {addon_name}. | Shared reference target checked |
| 17276 | 861156627 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::abort::addon_info_failed` | Failed to get {addon_name} app info. | Misslyckades med att hämta information om tillägget {addon_name}. | Shared reference target checked |
| 17277 | 861156626 | `component::homeassistant_yellow::issues::multi_pan_migration::fix_flow::abort::addon_already_running` | Failed to start the {addon_name} app because it is already running. | Det gick inte att starta tillägget {addon_name} eftersom det redan körs. | Shared reference target checked |
| 17278 | 861156625 | `component::homeassistant_sky_connect::options::progress::uninstall_multiprotocol_addon` | Please wait while the {addon_name} app is uninstalled. | Vänta medan appen {addon_name} avinstalleras. | Shared reference target checked |
| 17279 | 861156624 | `component::homeassistant_sky_connect::options::progress::install_zigbee_firmware` | Please wait while Zigbee-only firmware is installed on your {hardware_name}. This can take several minutes. | Vänta medan Zigbee-only firmware installeras på din {hardware_name}. Detta kan ta flera minuter. | Shared reference target checked |
| 17280 | 861156623 | `component::homeassistant_sky_connect::issues::multi_pan_migration::title` | Multiprotocol support is deprecated | Stöd för flera protokoll är utfasat | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 863055262 | `component::roborock::exceptions::network_error::message` | Network error connecting to Roborock servers. Check your internet connection and the Roborock service status. |
| 861931597 | `component::ovhcloud_ai_endpoints::config::abort::reauth_successful` | Re-authentication was successful |
| 861275239 | `component::matter::entity::sensor::uptime::name` | Uptime |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
