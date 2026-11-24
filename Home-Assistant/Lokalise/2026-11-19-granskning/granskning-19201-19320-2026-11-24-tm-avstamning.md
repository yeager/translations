# Home Assistant Core – historisk avstämning 19201–19320

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 93 direkta källtexter matchar HA Core-källan; 15 referensanvändningar med 14 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 12 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 19201 | 843809021 | `component::template::selector::number_device_class::options::carbon_dioxide` | Carbon dioxide | Koldioxid | Source-path follow-up open |
| 19202 | 843809020 | `component::template::selector::number_device_class::options::blood_glucose_concentration` | Blood glucose concentration | Koncentration av blodsocker | Source-path follow-up open |
| 19203 | 843809019 | `component::template::selector::number_device_class::options::battery` | Battery | Batteri | Source-path follow-up open |
| 19204 | 843809018 | `component::template::selector::number_device_class::options::atmospheric_pressure` | Atmospheric pressure | Lufttryck | Source-path follow-up open |
| 19205 | 843809017 | `component::template::selector::number_device_class::options::area` | Area | Area | Source-path follow-up open |
| 19206 | 843809016 | `component::template::selector::number_device_class::options::aqi` | Air quality index | Luftkvalitetsindex | Source-path follow-up open |
| 19207 | 843809015 | `component::template::selector::number_device_class::options::apparent_power` | Apparent power | Skenbar effekt | Source-path follow-up open |
| 19208 | 843809014 | `component::template::selector::number_device_class::options::absolute_humidity` | Absolute humidity | Absolut luftfuktighet | Source-path follow-up open |
| 19209 | 843809013 | `component::template::options::step::number::data::device_class` | Device class | Enhetsklass | Shared reference target checked |
| 19210 | 843809012 | `component::template::config::step::number::data::device_class` | Device class | Enhetsklass | Shared reference target checked |
| 19211 | 843551363 | `component::onedrive::exceptions::filenames_do_not_exist::message` | The following files do not exist: {filenames} | Följande filer finns inte: {filenames} | Core-literal match |
| 19212 | 843546386 | `component::duco::exceptions::connection_error::message` | Could not connect to the Duco device. | Det gick inte att ansluta till Duco-enheten. | Core-literal match |
| 19213 | 843443334 | `component::vacuum::exceptions::areas_not_mapped::message` | The following areas are not mapped to any segments of targeted vacuums: {areas} | Följande områden är inte mappade till några segment för vald dammsugare: {areas} | Core-literal match |
| 19214 | 843070822 | `component::israel_rail::entity::sensor::departure_delay::name` | Departure delay | Avgångsförsening | Core-literal match |
| 19215 | 843025596 | `component::indevolt::services::discharge::name` | Discharge | Urladdning | Core-literal match |
| 19216 | 843025595 | `component::indevolt::services::discharge::fields::target_soc::name` | Target SOC | Mål-SOC | Shared reference target checked |
| 19217 | 843025594 | `component::indevolt::services::discharge::fields::target_soc::description` | Target state of charge percentage. | Målvärde för laddningsstatus i procent. | Shared reference target checked |
| 19218 | 843025593 | `component::indevolt::services::discharge::fields::power::name` | Max. power | Maxeffekt | Core-literal match |
| 19219 | 843025592 | `component::indevolt::services::discharge::fields::power::description` | Maximum discharging power in watts. | Maximal uteffekt i watt. | Core-literal match |
| 19220 | 843025591 | `component::indevolt::services::discharge::fields::device_id::name` | Device(s) | Enhet(er) | Shared reference target checked |
| 19221 | 843025590 | `component::indevolt::services::discharge::fields::device_id::description` | The Indevolt device(s) to start discharging. | Indevolt-enheten/enheterna börjar laddas ur. | Core-literal match |
| 19222 | 843025589 | `component::indevolt::services::discharge::description` | Real-time control: Starts discharging with configured power until the target SOC is reached. | Realtidskontroll: Börjar urladdning med konfigurerad effekt tills målvärde för SOC uppnås. | Core-literal match |
| 19223 | 843025588 | `component::indevolt::services::charge::name` | Charge | Laddning | Core-literal match |
| 19224 | 843025587 | `component::indevolt::services::charge::fields::target_soc::name` | Target SOC | Mål-SOC | Core-literal match |
| 19225 | 843025586 | `component::indevolt::services::charge::fields::target_soc::description` | Target state of charge percentage. | Målvärde för laddningsstatus i procent. | Core-literal match |
| 19226 | 843025585 | `component::indevolt::services::charge::fields::power::name` | Max. power | Max. effekt | Core-literal match |
| 19227 | 843025584 | `component::indevolt::services::charge::fields::power::description` | Maximum charging power in watts. | Maximal laddningseffekt i watt. | Core-literal match |
| 19228 | 843025583 | `component::indevolt::services::charge::fields::device_id::name` | Device(s) | Enhet(er) | Core-literal match |
| 19229 | 843025582 | `component::indevolt::services::charge::fields::device_id::description` | The Indevolt device(s) to start charging. | Indevolt-enheten/-enheterna att börja ladda. | Core-literal match |
| 19230 | 843025581 | `component::indevolt::services::charge::description` | Real-time control: Starts charging with configured power until the target SOC is reached. | Realtidskontroll: Börjar ladda med konfigurerad effekt tills mål-SOC uppnås. | Core-literal match |
| 19231 | 843025580 | `component::indevolt::exceptions::soc_below_minimum::message` | Target SOC ({target}%) is below the device minimum ({minimum_soc}%) | Målvärdet för SOC ({target}%) ligger under enhetens minimivärde ({minimum_soc}%) | Core-literal match |
| 19232 | 843025579 | `component::indevolt::exceptions::soc_below_emergency::message` | Target SOC ({target}%) is below emergency SOC ({emergency_soc}%) | Målvärdet för SOC ({target}%) ligger under nödvärdet för SOC ({emergency_soc}%) | Core-literal match |
| 19233 | 843025578 | `component::indevolt::exceptions::power_exceeds_max::message` | Power ({power}W) exceeds maximum ({max_power}W) for generation ({generation}) devices | Effekten ({power} W) överstiger högsta tillåtna värde ({max_power} W) för enheter av generation {generation} | Core-literal match |
| 19234 | 843025577 | `component::indevolt::exceptions::no_matching_target_entries::message` | No matching Indevolt devices found in the selected targets | Inga matchande Indevolt-enheter hittades | Core-literal match |
| 19235 | 843025576 | `component::indevolt::exceptions::multi_device_errors::message` | One or more devices reported errors: {errors} | En eller flera enheter har rapporterat fel: {errors} | Core-literal match |
| 19236 | 842273428 | `component::roborock::entity::select::cleaning_route::state::deep` | Deep | Djup | Shared reference target checked |
| 19237 | 842273427 | `component::roborock::entity::select::cleaning_route::state::balanced` | Balanced | Balanserad | Shared reference target checked |
| 19238 | 842273426 | `component::roborock::entity::select::cleaning_route::name` | Cleaning route | Rengöringsväg | Core-literal match |
| 19239 | 842273425 | `component::roborock::entity::button::reset_dock_strainer_consumable::name` | Reset strainer consumable | Återställ silen | Core-literal match |
| 19240 | 842273424 | `component::roborock::entity::button::reset_dock_cleaning_brush_consumable::name` | Reset cleaning brush consumable | Återställ rengöringsborstar | Core-literal match |
| 19241 | 842269115 | `component::unifiprotect::exceptions::global_alarm_manager::message` | The alarm manager on this UniFi Protect NVR is set to Global mode and cannot be controlled locally. | Larmhanteraren på denna UniFi Protect NVR är inställd på globalt läge och kan inte styras lokalt. | Core-literal match |
| 19242 | 842269114 | `component::unifiprotect::entity::alarm_control_panel::nvr_alarm::name` | Alarm Manager | Larmhanterare | Core-literal match |
| 19243 | 842260484 | `component::broadlink::exceptions::transmit_failed::message` | Failed to transmit RF command: {error} | Det gick inte att sända RF-kommandot: {error} | Core-literal match |
| 19244 | 842260483 | `component::broadlink::exceptions::frequency_not_supported::message` | Broadlink devices cannot transmit on {frequency} MHz | Broadlink-enheter kan inte sända på {frequency} MHz | Core-literal match |
| 19245 | 842193695 | `component::fumis::entity::button::sync_clock::name` | Sync clock | Synkronisera klocka | Core-literal match |
| 19246 | 842193616 | `component::duco::entity::sensor::box_temperature::name` | Box temperature | Ventilationsboxens temperatur | Source-path follow-up open |
| 19247 | 842193564 | `component::pvoutput::config::step::reconfigure::description` | Reconfigure your PVOutput integration. You can update your API key at {account_url}. | Konfigurera om din PVOutput-integration. Du kan uppdatera din API-nyckel på {account_url}. | Core-literal match |
| 19248 | 842193563 | `component::pvoutput::config::step::reconfigure::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 19249 | 842193562 | `component::pvoutput::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 19250 | 842193508 | `component::knx::config_panel::expose::create::notes::placeholder` | Add your notes here... | Lägg till dina anteckningar här... | Core-literal match |
| 19251 | 842193507 | `component::knx::config_panel::expose::create::notes::label` | Notes | Anteckningar | Core-literal match |
| 19252 | 842193496 | `component::solaredge::entity::sensor::storage_discharge_energy::name` | Storage discharge energy today | Lagring urladdningsenergi idag | Core-literal match |
| 19253 | 842193495 | `component::solaredge::entity::sensor::storage_charge_energy::name` | Storage charge energy today | Lagring laddningsenergi idag | Core-literal match |
| 19254 | 842193494 | `component::solaredge::entity::sensor::battery_state_of_charge::name` | State of charge | Laddningsnivå | Core-literal match |
| 19255 | 842193493 | `component::solaredge::entity::sensor::battery_power::name` | Power | Effekt | Source-path follow-up open |
| 19256 | 842193492 | `component::solaredge::entity::sensor::battery_discharge_energy::name` | Discharge energy today | Urladdningsenergi idag | Core-literal match |
| 19257 | 842193491 | `component::solaredge::entity::sensor::battery_charge_energy::name` | Charge energy today | Laddningsenergi idag | Core-literal match |
| 19258 | 840755121 | `component::nfandroidtv::config::step::reconfigure::description` | Reconfigure {name} | Konfigurera om {name} | Core-literal match |
| 19259 | 840755120 | `component::nfandroidtv::config::step::reconfigure::data_description::host` | The hostname or IP address of your TV. | Värdnamnet eller IP-adressen för din TV. | Shared reference target checked |
| 19260 | 840755119 | `component::nfandroidtv::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 19261 | 840755118 | `component::nfandroidtv::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 19262 | 840729280 | `component::matter::entity::number::sensitivity_level::name` | Sensitivity | Känslighet | Core-literal match |
| 19263 | 840729246 | `component::shelly::exceptions::unsupported_media_type::message` | Unsupported media type for Shelly device: {media_type} | Medietyp som inte stöds av Shelly-enheten: {media_type} | Core-literal match |
| 19264 | 840729245 | `component::shelly::exceptions::unsupported_media_id::message` | Unsupported media ID for Shelly device: {media_id} | Medie-ID som inte stöds för Shelly-enheten: {media_id} | Core-literal match |
| 19265 | 840729244 | `component::shelly::exceptions::unsupported_media_content_type::message` | Unsupported media content type for Shelly device: {media_content_type} | Medietyp som inte stöds av Shelly-enheten: {media_content_type} | Core-literal match |
| 19266 | 840680280 | `component::sensor::entity_component::uptime::name` | Uptime | Upptid | Core-literal match |
| 19267 | 840674766 | `component::honeywell_string_lights::config::step::user::data_description::transmitter` | The radio frequency transmitter to use for sending commands. | Den radiofrekvenssändare som ska användas för att skicka kommandon. | Shared reference target checked |
| 19268 | 840674765 | `component::honeywell_string_lights::config::step::user::data::transmitter` | Radio frequency transmitter | Sändare för radiofrekvens | Shared reference target checked |
| 19269 | 840674764 | `component::honeywell_string_lights::config::abort::no_transmitters` | No radio frequency transmitters are available. Please set up a device first. | Inga radiofrekvenssändare finns tillgängliga. Vänligen installera en enhet först. | Shared reference target checked |
| 19270 | 840674763 | `component::honeywell_string_lights::config::abort::no_compatible_transmitters` | No radio frequency transmitter supports {frequency} {modulation} transmissions. Please add a compatible transmitter first. | Ingen radiofrekvenssändare stöder {frequency} {modulation}-sändningar. Lägg först till en kompatibel sändare. | Shared reference target checked |
| 19271 | 840674762 | `component::honeywell_string_lights::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 19272 | 840654315 | `component::otp::config::step::user::description` | Creates a sensor that generates One-Time Passwords (OTP) for two-factor authentication. | Skapar en sensor som genererar engångslösenord (OTP) för tvåfaktorsautentisering. | Core-literal match |
| 19273 | 840654314 | `component::otp::config::step::user::data_description::token` | An existing secret key for import into Home Assistant. | En befintlig hemlig nyckel för import till Home Assistant. | Core-literal match |
| 19274 | 840654313 | `component::otp::config::step::user::data_description::new_token` | Generate a new secret key. You will be able to scan a QR code to import this token into your preferred authenticator app in the next step. | Skapa en ny hemlig nyckel. I nästa steg kan du skanna en QR-kod för att importera denna token till den autentiseringsapp du föredrar. | Core-literal match |
| 19275 | 840654312 | `component::otp::config::step::user::data_description::name` | The purpose of this sensor (for example, the name of the service or account for which the One-Time Password is used). | Syftet med denna sensor (till exempel namnet på den tjänst eller det konto för vilket engångslösenordet används). | Core-literal match |
| 19276 | 840654311 | `component::otp::config::step::confirm::data_description::code` | The six-digit code currently displayed in your authentication app. | Den sexsiffriga koden som för närvarande visas i din autentiseringsapp. | Core-literal match |
| 19277 | 840616900 | `component::bsblan::device::water_heater::name` | Water heater | Varmvattenberedare | Core-literal match |
| 19278 | 840616899 | `component::bsblan::device::heating_circuit::name` | Heating circuit {circuit} | Värmekrets {circuit} | Core-literal match |
| 19279 | 840495231 | `component::radio_frequency::exceptions::unsupported_modulation::message` | Radio Frequency entity `{entity_id}` does not support modulation {modulation} | Radiofrekvensenheten `{entity_id}` stöder inte modulering {modulation} | Core-literal match |
| 19280 | 840495230 | `component::radio_frequency::exceptions::unsupported_frequency::message` | Radio Frequency entity `{entity_id}` does not support frequency {frequency} Hz | Radiofrekvensenheten `{entity_id}` stöder inte frekvensen {frequency} Hz | Core-literal match |
| 19281 | 840495229 | `component::radio_frequency::exceptions::no_transmitters::message` | No Radio Frequency transmitters available | Inga radiosändare är tillgängliga | Core-literal match |
| 19282 | 840495228 | `component::radio_frequency::exceptions::entity_not_found::message` | Radio Frequency entity `{entity_id}` not found | Radiofrekvensenheten `{entity_id}` hittades inte | Core-literal match |
| 19283 | 840495227 | `component::radio_frequency::exceptions::component_not_loaded::message` | Radio Frequency component not loaded | Radiofrekvenskomponenten har inte laddats | Core-literal match |
| 19284 | 840494172 | `component::hr_energy_qube::entity::binary_sensor::user_pump::name` | User pump | Användarpump | Core-literal match |
| 19285 | 840494171 | `component::hr_energy_qube::entity::binary_sensor::three_way_valve::name` | Three-way valve | Trevägsventil | Core-literal match |
| 19286 | 840494170 | `component::hr_energy_qube::entity::binary_sensor::thermostat_demand::name` | Thermostat demand | Termostatbehov | Core-literal match |
| 19287 | 840494169 | `component::hr_energy_qube::entity::binary_sensor::summer_mode::name` | Summer mode | Sommarläge | Core-literal match |
| 19288 | 840494168 | `component::hr_energy_qube::entity::binary_sensor::source_pump::name` | Source pump | Källpump | Core-literal match |
| 19289 | 840494167 | `component::hr_energy_qube::entity::binary_sensor::source_flow::name` | Source flow | Källflöde | Core-literal match |
| 19290 | 840494166 | `component::hr_energy_qube::entity::binary_sensor::room_sensor_enabled::name` | Room sensor enabled | Rumssensor aktiverad | Core-literal match |
| 19291 | 840494165 | `component::hr_energy_qube::entity::binary_sensor::pv_surplus::name` | PV surplus | PV-överskott | Core-literal match |
| 19292 | 840494164 | `component::hr_energy_qube::entity::binary_sensor::plant_sensor_enabled::name` | Plant sensor enabled | Växtsensor aktiverad | Core-literal match |
| 19293 | 840494163 | `component::hr_energy_qube::entity::binary_sensor::plant_demand::name` | Plant demand | Växtbehov | Core-literal match |
| 19294 | 840494162 | `component::hr_energy_qube::entity::binary_sensor::keypad::name` | Keypad | Knappsats | Core-literal match |
| 19295 | 840494161 | `component::hr_energy_qube::entity::binary_sensor::heater_step_3::name` | Heater step 3 | Värmare steg 3 | Core-literal match |
| 19296 | 840494160 | `component::hr_energy_qube::entity::binary_sensor::heater_step_2::name` | Heater step 2 | Värmare steg 2 | Core-literal match |
| 19297 | 840494159 | `component::hr_energy_qube::entity::binary_sensor::heater_step_1::name` | Heater step 1 | Värmare steg 1 | Core-literal match |
| 19298 | 840494158 | `component::hr_energy_qube::entity::binary_sensor::four_way_valve::name` | Four-way valve | Fyrvägsventil | Core-literal match |
| 19299 | 840494157 | `component::hr_energy_qube::entity::binary_sensor::external_demand::name` | External demand | Extern efterfrågan | Core-literal match |
| 19300 | 840494156 | `component::hr_energy_qube::entity::binary_sensor::dhw_controller_enabled::name` | DHW controller enabled | Varmvattenregulatorn är aktiverad | Core-literal match |
| 19301 | 840494155 | `component::hr_energy_qube::entity::binary_sensor::dewpoint::name` | Dewpoint | Daggpunkt | Core-literal match |
| 19302 | 840494154 | `component::hr_energy_qube::entity::binary_sensor::day_mode::name` | Day mode | Dagläge | Core-literal match |
| 19303 | 840494153 | `component::hr_energy_qube::entity::binary_sensor::cooling_output::name` | Cooling output | Kylkapacitet | Core-literal match |
| 19304 | 840494152 | `component::hr_energy_qube::entity::binary_sensor::buffer_sensor_enabled::name` | Buffer sensor enabled | Buffertsensor aktiverad | Core-literal match |
| 19305 | 840494151 | `component::hr_energy_qube::entity::binary_sensor::buffer_pump::name` | Buffer pump | Buffertpump | Core-literal match |
| 19306 | 840494150 | `component::hr_energy_qube::entity::binary_sensor::booster_security::name` | Booster security | Ökad säkerhet | Core-literal match |
| 19307 | 840494149 | `component::hr_energy_qube::entity::binary_sensor::anti_legionella::name` | Anti-legionella | Anti-legionella | Core-literal match |
| 19308 | 840494148 | `component::hr_energy_qube::entity::binary_sensor::alarm_working_hours::name` | Working hours alarm | Larm om arbetstid | Core-literal match |
| 19309 | 840494147 | `component::hr_energy_qube::entity::binary_sensor::alarm_supply_too_hot::name` | Supply too hot alarm | Larm vid för varm tillförsel | Core-literal match |
| 19310 | 840494146 | `component::hr_energy_qube::entity::binary_sensor::alarm_source::name` | Source alarm | Källarm | Core-literal match |
| 19311 | 840494145 | `component::hr_energy_qube::entity::binary_sensor::alarm_heating::name` | Heating alarm | Värmelarm | Core-literal match |
| 19312 | 840494144 | `component::hr_energy_qube::entity::binary_sensor::alarm_global::name` | Global alarm | Globalt larm | Core-literal match |
| 19313 | 840494143 | `component::hr_energy_qube::entity::binary_sensor::alarm_flow::name` | Flow alarm | Flödeslarm | Core-literal match |
| 19314 | 840494142 | `component::hr_energy_qube::entity::binary_sensor::alarm_dhw_timeout::name` | DHW timeout alarm | Larm vid tidsöverskridning för varmvatten | Core-literal match |
| 19315 | 840494141 | `component::hr_energy_qube::entity::binary_sensor::alarm_dewpoint::name` | Dewpoint alarm | Daggpunktslarm | Core-literal match |
| 19316 | 840494140 | `component::hr_energy_qube::entity::binary_sensor::alarm_cooling::name` | Cooling alarm | Kylningslarm | Core-literal match |
| 19317 | 840494139 | `component::hr_energy_qube::entity::binary_sensor::alarm_compressor::name` | Compressor alarm | Kompressorlarm | Core-literal match |
| 19318 | 840494138 | `component::hr_energy_qube::entity::binary_sensor::alarm_central_heating::name` | Central heating alarm | Centralvärmelarm | Core-literal match |
| 19319 | 840494137 | `component::hr_energy_qube::entity::binary_sensor::alarm_antilegionella_timeout::name` | Anti-legionella timeout alarm | Larm vid tidsöverskridning för legionellabekämpning | Core-literal match |
| 19320 | 840176293 | `component::wled::entity::switch::segment_freeze::name` | Segment {segment} freeze | Segment {segment} frys | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 843809021 | `component::template::selector::number_device_class::options::carbon_dioxide` | Carbon dioxide |
| 843809020 | `component::template::selector::number_device_class::options::blood_glucose_concentration` | Blood glucose concentration |
| 843809019 | `component::template::selector::number_device_class::options::battery` | Battery |
| 843809018 | `component::template::selector::number_device_class::options::atmospheric_pressure` | Atmospheric pressure |
| 843809017 | `component::template::selector::number_device_class::options::area` | Area |
| 843809016 | `component::template::selector::number_device_class::options::aqi` | Air quality index |
| 843809015 | `component::template::selector::number_device_class::options::apparent_power` | Apparent power |
| 843809014 | `component::template::selector::number_device_class::options::absolute_humidity` | Absolute humidity |
| 842193616 | `component::duco::entity::sensor::box_temperature::name` | Box temperature |
| 842193562 | `component::pvoutput::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 842193493 | `component::solaredge::entity::sensor::battery_power::name` | Power |
| 840755118 | `component::nfandroidtv::config::abort::reconfigure_successful` | Reconfiguration was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
