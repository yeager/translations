# Fullständig Home Assistant Core-kontroll: saknade Lokalise-poster

Datum: 2026-11-25  
Aktuell Core-revision: `86a2eabe7e43f526db5821ef068087ce8404ae07` (Home Assistant `dev`)  
Lokalise-projekt: `130246255a974bd3b5e8a1.51616605`

## Sammanfattning

- Aktuell HA Core-källa innehåller **67,213** strängnycklar. Lokalise-listningen omfattade **76,341** poster över 153 API-sidor.
- **203 aktuella källnycklar saknas helt i Lokalise.** Det är en upstream-synkfråga; en tidigare avgränsad `POST /keys`-kontroll gav HTTP 403 för tokenen.
- **521 källsträngar har fortfarande tomt svenskt mål i befintliga Lokalise-nycklar.** Av dessa är **68** engelska källor referenser till andra HA-nycklar. Alla fullständiga nycklar och källor finns i tabellerna nedan och i den bifogade JSON-filen.
- 18956 engelska nyckelreferenser jämfördes efter att ha följt aktuell Core-referens. Tre verkliga skillnader mellan Core-källtext och Lokalises engelska registrerades.
- Lokalise har dessutom 9,311 aktiva nycklar som inte finns i den aktuella Core-källsnapshoten. De kan vara historiska utgångna nycklar; de räknas inte som saknade nuvarande Core-nycklar och bör kontrolleras separat innan eventuell arkivering.

## Nya Core-strängar sedan tidigare inventering

Tre nycklar som tillkom efter föregående inventering fanns i Lokalise med tom svensk text. De granskades mot aktuella Shelly- och Tuya-källor, översattes och lästes tillbaka via API. De ingår därför inte längre i listan över tomma mål. Av dessa tidigare 641 tomma mål har nu 120 granskats och sparats; 521 återstår.

| Nyckel | Engelska | Svenska |
|---|---|---|
| `component::shelly::exceptions::storage_unavailable::message` | Storage unavailable for {device} | Lagringen är inte tillgänglig för {device}. |
| `component::shelly::exceptions::unexpected_identifier::message` | Unexpected identifier: {identifier} | Ogiltigt identifierarformat: {identifier} |
| `component::tuya::exceptions::cannot_connect::message` | Unable to connect to the Tuya cloud. | Det går inte att ansluta till Tuya-molnet. |

## Saknade aktuella källnycklar

För dessa nycklar finns ingen Lokalise-post att fylla. `source_resolved` följer eventuella `[%key:...%]`-referenser för att visa verklig engelska källtext; `source_raw` visar källans råa referens där sådan finns.

### Antal per komponent

| Komponent | Saknade nycklar |
|---|---:|
| `airgradient` | 7 |
| `denon_rs232` | 1 |
| `hdfury` | 16 |
| `huawei_lte` | 2 |
| `lametric` | 1 |
| `light` | 1 |
| `music_assistant` | 5 |
| `my_pv` | 20 |
| `roborock` | 2 |
| `schlage` | 12 |
| `tuya` | 13 |
| `wled` | 3 |
| `zwave_js` | 120 |

### Fullständig lista

| Fullständig nyckel | Källtext (referenser upplösta) |
|---|---|
| `component::airgradient::entity::select::co2_automatic_baseline_calibration::state::0` | Off (rå källa: `[%key:common::state::off%]`) |
| `component::airgradient::entity::select::co2_automatic_baseline_calibration::state::1` | 1 day |
| `component::airgradient::entity::select::co2_automatic_baseline_calibration::state::180` | 180 days |
| `component::airgradient::entity::select::co2_automatic_baseline_calibration::state::30` | 30 days |
| `component::airgradient::entity::select::co2_automatic_baseline_calibration::state::7` | 7 days |
| `component::airgradient::entity::select::co2_automatic_baseline_calibration::state::8` | 8 days |
| `component::airgradient::entity::select::co2_automatic_baseline_calibration::state::90` | 90 days |
| `component::denon_rs232::selector::model::options::other` | Other |
| `component::hdfury::entity::select::opmode::state::0` | Mode 0 - Splitter TX0/TX1 FRL5 VRR |
| `component::hdfury::entity::select::opmode::state::1` | Mode 1 - Splitter TX0/TX1 UPSCALE FRL5 |
| `component::hdfury::entity::select::opmode::state::2` | Mode 2 - Matrix TMDS |
| `component::hdfury::entity::select::opmode::state::3` | Mode 3 - Matrix FRL->TMDS |
| `component::hdfury::entity::select::opmode::state::4` | Mode 4 - Matrix DOWNSCALE |
| `component::hdfury::entity::select::opmode::state::5` | Mode 5 - Matrix RX0:FRL5 + RX1-3:TMDS |
| `component::hdfury::entity::select::portseltx0::state::0` | Input 0 |
| `component::hdfury::entity::select::portseltx0::state::1` | Input 1 |
| `component::hdfury::entity::select::portseltx0::state::2` | Input 2 |
| `component::hdfury::entity::select::portseltx0::state::3` | Input 3 |
| `component::hdfury::entity::select::portseltx0::state::4` | Copy TX1 |
| `component::hdfury::entity::select::portseltx1::state::0` | Input 0 |
| `component::hdfury::entity::select::portseltx1::state::1` | Input 1 |
| `component::hdfury::entity::select::portseltx1::state::2` | Input 2 |
| `component::hdfury::entity::select::portseltx1::state::3` | Input 3 |
| `component::hdfury::entity::select::portseltx1::state::4` | Copy TX0 |
| `component::huawei_lte::entity::sensor::operator_search_mode::state::0` | Auto (rå källa: `[%key:common::state::auto%]`) |
| `component::huawei_lte::entity::sensor::operator_search_mode::state::1` | Manual (rå källa: `[%key:common::state::manual%]`) |
| `component::lametric::selector::sound::options::win2` | Win 2 |
| `component::light::services::turn_on::fields::rgbw_color::description` | The color in RGBW format. A list of four integers between 0 and 255 representing the values of red, green, blue, and white. (rå källa: `[%key:component::light::common::field_rgbw_color_description%]`) |
| `component::music_assistant::entity::select::sleep::state::0` | Off (rå källa: `[%key:common::state::off%]`) |
| `component::music_assistant::entity::select::sleep::state::120` | 120 minutes |
| `component::music_assistant::entity::select::sleep::state::30` | 30 minutes |
| `component::music_assistant::entity::select::sleep::state::60` | 60 minutes |
| `component::music_assistant::entity::select::sleep::state::90` | 90 minutes |
| `component::my_pv::entity::select::bstmode::state::0` | Off (rå källa: `[%key:common::state::off%]`) |
| `component::my_pv::entity::select::bstmode::state::1` | On (rå källa: `[%key:common::state::on%]`) |
| `component::my_pv::entity::select::bstmode::state::3` | Relay |
| `component::my_pv::entity::select::bstmode::state::4` | SELV relay |
| `component::my_pv::entity::select::bstmode::state::5` | AUX relay |
| `component::my_pv::entity::sensor::cur_eth_mode::state::0` | LAN |
| `component::my_pv::entity::sensor::cur_eth_mode::state::1` | WLAN |
| `component::my_pv::entity::sensor::cur_eth_mode::state::2` | AP |
| `component::my_pv::entity::sensor::screen_mode_flag::state::0` | Standby (rå källa: `[%key:common::state::standby%]`) |
| `component::my_pv::entity::sensor::screen_mode_flag::state::1` | Heat |
| `component::my_pv::entity::sensor::screen_mode_flag::state::2` | Boost |
| `component::my_pv::entity::sensor::screen_mode_flag::state::3` | Heating finished |
| `component::my_pv::entity::sensor::screen_mode_flag::state::4` | No connection / Disabled |
| `component::my_pv::entity::sensor::screen_mode_flag::state::5` | Failure |
| `component::my_pv::entity::sensor::screen_mode_flag::state::6` | Block active |
| `component::my_pv::entity::sensor::wifi_signal::state::0` | Poor |
| `component::my_pv::entity::sensor::wifi_signal::state::1` | Low |
| `component::my_pv::entity::sensor::wifi_signal::state::2` | Average |
| `component::my_pv::entity::sensor::wifi_signal::state::3` | Good |
| `component::my_pv::entity::sensor::wifi_signal::state::4` | Strong |
| `component::roborock::entity::select::cleaning_cycles::state::one` | 1x |
| `component::roborock::entity::select::cleaning_cycles::state::two` | 2x |
| `component::schlage::entity::select::auto_lock_time::state::0` | Disabled (rå källa: `[%key:common::state::disabled%]`) |
| `component::schlage::entity::select::auto_lock_time::state::120` | 2 minutes |
| `component::schlage::entity::select::auto_lock_time::state::15` | 15 seconds |
| `component::schlage::entity::select::auto_lock_time::state::1800` | 30 minutes |
| `component::schlage::entity::select::auto_lock_time::state::240` | 4 minutes |
| `component::schlage::entity::select::auto_lock_time::state::30` | 30 seconds |
| `component::schlage::entity::select::auto_lock_time::state::300` | 5 minutes |
| `component::schlage::entity::select::auto_lock_time::state::360` | 6 minutes |
| `component::schlage::entity::select::auto_lock_time::state::5` | 5 seconds |
| `component::schlage::entity::select::auto_lock_time::state::60` | 1 minute |
| `component::schlage::entity::select::auto_lock_time::state::600` | 10 minutes |
| `component::schlage::entity::select::auto_lock_time::state::900` | 15 minutes |
| `component::tuya::entity::select::basic_anti_flicker::state::0` | Disabled (rå källa: `[%key:common::state::disabled%]`) |
| `component::tuya::entity::select::basic_anti_flicker::state::1` | 50 Hz |
| `component::tuya::entity::select::basic_anti_flicker::state::2` | 60 Hz |
| `component::tuya::entity::select::basic_nightvision::state::0` | Automatic |
| `component::tuya::entity::select::basic_nightvision::state::1` | Off (rå källa: `[%key:common::state::off%]`) |
| `component::tuya::entity::select::basic_nightvision::state::2` | On (rå källa: `[%key:common::state::on%]`) |
| `component::tuya::entity::select::decibel_sensitivity::state::0` | Low sensitivity |
| `component::tuya::entity::select::decibel_sensitivity::state::1` | High sensitivity |
| `component::tuya::entity::select::ipc_work_mode::state::0` | Low power mode |
| `component::tuya::entity::select::ipc_work_mode::state::1` | Continuous working mode |
| `component::tuya::entity::select::motion_sensitivity::state::0` | Low (rå källa: `[%key:common::state::low%]`) |
| `component::tuya::entity::select::motion_sensitivity::state::1` | Medium (rå källa: `[%key:common::state::medium%]`) |
| `component::tuya::entity::select::motion_sensitivity::state::2` | High (rå källa: `[%key:common::state::high%]`) |
| `component::wled::entity::select::live_override::state::0` | Off (rå källa: `[%key:common::state::off%]`) |
| `component::wled::entity::select::live_override::state::1` | On (rå källa: `[%key:common::state::on%]`) |
| `component::wled::entity::select::live_override::state::2` | Until device restarts |
| `component::zwave_js::selector::command_class::options::0` | No Operation (0) |
| `component::zwave_js::selector::command_class::options::100` | Humidity Control Setpoint (100) |
| `component::zwave_js::selector::command_class::options::102` | Barrier Operator (102) |
| `component::zwave_js::selector::command_class::options::103` | Network Management Installation and Maintenance (103) |
| `component::zwave_js::selector::command_class::options::104` | Z/IP Naming and Location (104) |
| `component::zwave_js::selector::command_class::options::105` | Mailbox (105) |
| `component::zwave_js::selector::command_class::options::106` | Window Covering (106) |
| `component::zwave_js::selector::command_class::options::107` | Irrigation (107) |
| `component::zwave_js::selector::command_class::options::108` | Supervision (108) |
| `component::zwave_js::selector::command_class::options::109` | Humidity Control Mode (109) |
| `component::zwave_js::selector::command_class::options::110` | Humidity Control Operating State (110) |
| `component::zwave_js::selector::command_class::options::111` | Entry Control (111) |
| `component::zwave_js::selector::command_class::options::112` | Configuration (112) |
| `component::zwave_js::selector::command_class::options::113` | Notification (113) |
| `component::zwave_js::selector::command_class::options::114` | Manufacturer Specific (114) |
| `component::zwave_js::selector::command_class::options::115` | Powerlevel (115) |
| `component::zwave_js::selector::command_class::options::116` | Inclusion Controller (116) |
| `component::zwave_js::selector::command_class::options::117` | Protection (117) |
| `component::zwave_js::selector::command_class::options::118` | Lock (118) |
| `component::zwave_js::selector::command_class::options::119` | Node Naming and Location (119) |
| `component::zwave_js::selector::command_class::options::120` | Node Provisioning (120) |
| `component::zwave_js::selector::command_class::options::121` | Sound Switch (121) |
| `component::zwave_js::selector::command_class::options::122` | Firmware Update Meta Data (122) |
| `component::zwave_js::selector::command_class::options::123` | Grouping Name (123) |
| `component::zwave_js::selector::command_class::options::124` | Remote Association Activation (124) |
| `component::zwave_js::selector::command_class::options::125` | Remote Association Configuration (125) |
| `component::zwave_js::selector::command_class::options::126` | Anti-Theft Unlock (126) |
| `component::zwave_js::selector::command_class::options::128` | Battery (128) |
| `component::zwave_js::selector::command_class::options::129` | Clock (129) |
| `component::zwave_js::selector::command_class::options::130` | Hail (130) |
| `component::zwave_js::selector::command_class::options::132` | Wake Up (132) |
| `component::zwave_js::selector::command_class::options::133` | Association (133) |
| `component::zwave_js::selector::command_class::options::134` | Version (134) |
| `component::zwave_js::selector::command_class::options::135` | Indicator (135) |
| `component::zwave_js::selector::command_class::options::136` | Proprietary (136) |
| `component::zwave_js::selector::command_class::options::137` | Language (137) |
| `component::zwave_js::selector::command_class::options::138` | Time (138) |
| `component::zwave_js::selector::command_class::options::139` | Time Parameters (139) |
| `component::zwave_js::selector::command_class::options::140` | Geographic Location (140) |
| `component::zwave_js::selector::command_class::options::142` | Multi Channel Association (142) |
| `component::zwave_js::selector::command_class::options::143` | Multi Command (143) |
| `component::zwave_js::selector::command_class::options::144` | Energy Production (144) |
| `component::zwave_js::selector::command_class::options::145` | Manufacturer Proprietary (145) |
| `component::zwave_js::selector::command_class::options::146` | Screen Meta Data (146) |
| `component::zwave_js::selector::command_class::options::147` | Screen Attributes (147) |
| `component::zwave_js::selector::command_class::options::148` | Simple AV Control (148) |
| `component::zwave_js::selector::command_class::options::152` | Security (152) |
| `component::zwave_js::selector::command_class::options::154` | IP Configuration (154) |
| `component::zwave_js::selector::command_class::options::155` | Association Command Configuration (155) |
| `component::zwave_js::selector::command_class::options::156` | Alarm Sensor (156) |
| `component::zwave_js::selector::command_class::options::157` | Alarm Silence (157) |
| `component::zwave_js::selector::command_class::options::158` | Sensor Configuration (158) |
| `component::zwave_js::selector::command_class::options::159` | Security 2 (159) |
| `component::zwave_js::selector::command_class::options::160` | IR Repeater (160) |
| `component::zwave_js::selector::command_class::options::161` | Authentication (161) |
| `component::zwave_js::selector::command_class::options::162` | Authentication Media Write (162) |
| `component::zwave_js::selector::command_class::options::163` | Generic Schedule (163) |
| `component::zwave_js::selector::command_class::options::32` | Basic (32) |
| `component::zwave_js::selector::command_class::options::33` | Controller Replication (33) |
| `component::zwave_js::selector::command_class::options::34` | Application Status (34) |
| `component::zwave_js::selector::command_class::options::35` | Z/IP (35) |
| `component::zwave_js::selector::command_class::options::37` | Binary Switch (37) |
| `component::zwave_js::selector::command_class::options::38` | Multilevel Switch (38) |
| `component::zwave_js::selector::command_class::options::39` | All Switch (39) |
| `component::zwave_js::selector::command_class::options::40` | Binary Toggle Switch (40) |
| `component::zwave_js::selector::command_class::options::41` | Multilevel Toggle Switch (41) |
| `component::zwave_js::selector::command_class::options::43` | Scene Activation (43) |
| `component::zwave_js::selector::command_class::options::44` | Scene Actuator Configuration (44) |
| `component::zwave_js::selector::command_class::options::45` | Scene Controller Configuration (45) |
| `component::zwave_js::selector::command_class::options::48` | Binary Sensor (48) |
| `component::zwave_js::selector::command_class::options::49` | Multilevel Sensor (49) |
| `component::zwave_js::selector::command_class::options::50` | Meter (50) |
| `component::zwave_js::selector::command_class::options::51` | Color Switch (51) |
| `component::zwave_js::selector::command_class::options::52` | Network Management Inclusion (52) |
| `component::zwave_js::selector::command_class::options::53` | Pulse Meter (53) |
| `component::zwave_js::selector::command_class::options::54` | Basic Tariff Information (54) |
| `component::zwave_js::selector::command_class::options::55` | HRV Status (55) |
| `component::zwave_js::selector::command_class::options::57` | HRV Control (57) |
| `component::zwave_js::selector::command_class::options::58` | Demand Control Plan Configuration (58) |
| `component::zwave_js::selector::command_class::options::59` | Demand Control Plan Monitor (59) |
| `component::zwave_js::selector::command_class::options::60` | Meter Table Configuration (60) |
| `component::zwave_js::selector::command_class::options::61` | Meter Table Monitor (61) |
| `component::zwave_js::selector::command_class::options::62` | Meter Table Push Configuration (62) |
| `component::zwave_js::selector::command_class::options::63` | Prepayment (63) |
| `component::zwave_js::selector::command_class::options::64` | Thermostat Mode (64) |
| `component::zwave_js::selector::command_class::options::65` | Prepayment Encapsulation (65) |
| `component::zwave_js::selector::command_class::options::66` | Thermostat Operating State (66) |
| `component::zwave_js::selector::command_class::options::67` | Thermostat Setpoint (67) |
| `component::zwave_js::selector::command_class::options::68` | Thermostat Fan Mode (68) |
| `component::zwave_js::selector::command_class::options::69` | Thermostat Fan State (69) |
| `component::zwave_js::selector::command_class::options::70` | Climate Control Schedule (70) |
| `component::zwave_js::selector::command_class::options::71` | Thermostat Setback (71) |
| `component::zwave_js::selector::command_class::options::72` | Rate Table Configuration (72) |
| `component::zwave_js::selector::command_class::options::73` | Rate Table Monitor (73) |
| `component::zwave_js::selector::command_class::options::74` | Tariff Table Configuration (74) |
| `component::zwave_js::selector::command_class::options::75` | Tariff Table Monitor (75) |
| `component::zwave_js::selector::command_class::options::76` | Door Lock Logging (76) |
| `component::zwave_js::selector::command_class::options::77` | Network Management Basic Node (77) |
| `component::zwave_js::selector::command_class::options::78` | Schedule Entry Lock (78) |
| `component::zwave_js::selector::command_class::options::79` | Z/IP 6LoWPAN (79) |
| `component::zwave_js::selector::command_class::options::80` | Basic Window Covering (80) |
| `component::zwave_js::selector::command_class::options::81` | Move To Position Window Covering (81) |
| `component::zwave_js::selector::command_class::options::82` | Network Management Proxy (82) |
| `component::zwave_js::selector::command_class::options::83` | Schedule (83) |
| `component::zwave_js::selector::command_class::options::84` | Network Management Primary (84) |
| `component::zwave_js::selector::command_class::options::85` | Transport Service (85) |
| `component::zwave_js::selector::command_class::options::86` | CRC-16 Encapsulation (86) |
| `component::zwave_js::selector::command_class::options::87` | Application Capability (87) |
| `component::zwave_js::selector::command_class::options::88` | Z/IP ND (88) |
| `component::zwave_js::selector::command_class::options::89` | Association Group Information (89) |
| `component::zwave_js::selector::command_class::options::90` | Device Reset Locally (90) |
| `component::zwave_js::selector::command_class::options::91` | Central Scene (91) |
| `component::zwave_js::selector::command_class::options::92` | IP Association (92) |
| `component::zwave_js::selector::command_class::options::93` | Anti-Theft (93) |
| `component::zwave_js::selector::command_class::options::94` | Z-Wave Plus Info (94) |
| `component::zwave_js::selector::command_class::options::95` | Z/IP Gateway (95) |
| `component::zwave_js::selector::command_class::options::96` | Multi Channel (96) |
| `component::zwave_js::selector::command_class::options::97` | Z/IP Portal (97) |
| `component::zwave_js::selector::command_class::options::98` | Door Lock (98) |
| `component::zwave_js::selector::command_class::options::99` | User Code (99) |

## Befintliga nycklar med tom svensk text

Dessa nycklar finns i Lokalise och har engelska källtext men tomt svenskt mål. Tabellen listar de 521 återstående tomma målen; 120 översatta poster dokumenteras i `2026-11-25-reviewed-empty-targets-001-120.json`. Referensbaserade engelska texter behöver följas till angivet mål innan en svensk text sparas.

### Antal per komponent

| Komponent | Tomma svenska mål |
|---|---:|
| `benq_projector_infrared` | 9 |
| `bosch_shc` | 12 |
| `bosch_smart_camera` | 3 |
| `cloud` | 3 |
| `control4` | 5 |
| `daikin_infrared` | 9 |
| `ecoforest` | 9 |
| `elkm1` | 6 |
| `elvia` | 6 |
| `foreca` | 29 |
| `fuelprices_dk` | 5 |
| `fujitsu_infrared` | 21 |
| `google_health` | 6 |
| `google_travel_time` | 7 |
| `hassio` | 2 |
| `hikvision` | 2 |
| `hr_energy_qube` | 4 |
| `hue_ble` | 12 |
| `huisbaasje` | 5 |
| `intesis_modbus` | 2 |
| `knx` | 3 |
| `lastfm` | 20 |
| `lektrico` | 1 |
| `marantz_infrared` | 5 |
| `matter` | 2 |
| `microsoft` | 223 |
| `modbus` | 1 |
| `myuplink` | 9 |
| `neopool` | 1 |
| `netatmo` | 1 |
| `netio` | 7 |
| `nexblue` | 4 |
| `omnilogic` | 4 |
| `opendisplay` | 2 |
| `poolsense` | 4 |
| `portainer` | 4 |
| `schlage` | 1 |
| `shelly` | 1 |
| `skoda` | 2 |
| `smartyplants` | 2 |
| `sonos` | 1 |
| `starlink` | 1 |
| `system_bridge` | 4 |
| `tellduslive` | 2 |
| `template` | 14 |
| `teslemetry` | 5 |
| `threema` | 1 |
| `unifi` | 8 |
| `upcloud` | 4 |
| `vesync` | 2 |
| `vicare` | 3 |
| `volkszaehler` | 4 |
| `weatherkit` | 6 |
| `workday` | 12 |

### Fullständig lista

| Fullständig nyckel | Key ID | Källtext (referenser upplösta) | Typ |
|---|---:|---|---|
| `component::benq_projector_infrared::exceptions::cooling_down::message` | 987266378 | The projector is cooling down and does not accept commands for another {seconds} seconds. | direkt text |
| `component::benq_projector_infrared::exceptions::emitter_not_found::message` | 987266379 | The infrared emitter used by this BenQ projector no longer exists. Remove this device and set it up again with another emitter. | direkt text |
| `component::benq_projector_infrared::exceptions::invalid_source::message` | 987266380 | Cannot select input source {invalid_source}. Valid sources: {valid_sources}. | direkt text |
| `component::benq_projector_infrared::exceptions::receiver_not_found::message` | 987266381 | The infrared receiver used by this BenQ projector no longer exists. Remove this device and set it up again with another receiver. | direkt text |
| `component::benq_projector_infrared::exceptions::warming_up::message` | 987266382 | The projector is warming up and does not accept commands for another {seconds} seconds. | direkt text |
| `component::benq_projector_infrared::options::step::init::data::cool_down_time` | 987266383 | Cool-down time | direkt text |
| `component::benq_projector_infrared::options::step::init::data::warm_up_time` | 987266384 | Warm-up time | direkt text |
| `component::benq_projector_infrared::options::step::init::data_description::cool_down_time` | 987266385 | How long the projector ignores commands after it is turned off. Commands sent during this time are refused. | direkt text |
| `component::benq_projector_infrared::options::step::init::data_description::warm_up_time` | 987266386 | How long the projector ignores commands after it is turned on. Commands sent during this time are refused. | direkt text |
| `component::bosch_shc::entity::binary_sensor::siren_ac_dc_error::name` | 987266515 | AC/DC error | direkt text |
| `component::bosch_shc::entity::binary_sensor::siren_battery_defect::name` | 987266516 | Battery defect | direkt text |
| `component::bosch_shc::entity::binary_sensor::siren_battery_temperature_abnormal::name` | 987266517 | Battery temperature abnormal | direkt text |
| `component::bosch_shc::entity::binary_sensor::siren_primary_power_supply_outage::name` | 987266518 | Primary power supply outage | direkt text |
| `component::bosch_shc::entity::button::preview_max_brightness::name` | 987262974 | Preview max brightness | direkt text |
| `component::bosch_shc::entity::button::preview_min_brightness::name` | 987262975 | Preview min brightness | direkt text |
| `component::bosch_shc::entity::button::reset_energy_summation::name` | 987004689 | Reset consumption value | direkt text |
| `component::bosch_shc::entity::number::comfort_temperature::name` | 987003160 | Comfort temperature | direkt text |
| `component::bosch_shc::entity::number::eco_temperature::name` | 987003161 | Eco temperature | direkt text |
| `component::bosch_shc::entity::update::controller_update::name` | 986931583 | Software update | direkt text |
| `component::bosch_shc::exceptions::update_install_failed::message` | 986931584 | Failed to start the firmware update on {name} | direkt text |
| `component::bosch_shc::exceptions::update_not_ready::message` | 986931585 | Firmware update for {name} cannot be activated right now (current state: {state}). | direkt text |
| `component::bosch_smart_camera::entity::light::camera_light::name` | 987092760 | Camera light | direkt text |
| `component::bosch_smart_camera::entity::sensor::wifi_signal_strength::name` | 987264805 | Wi-Fi signal strength | direkt text |
| `component::bosch_smart_camera::exceptions::light_failed::message` | 987092761 | Unable to switch the camera light. | direkt text |
| `component::cloud::issues::remote_client_certificate_error::description` | 987003708 | Remote access through Home Assistant Link is off because the client certificate authority file ({ca_file}) could not be loaded. Fix the file or update the SSL peer certificate in the network settings, then restart Home Assistant. | direkt text |
| `component::cloud::issues::remote_client_certificate_error::title` | 987003709 | Remote access client certificate authority could not be loaded | direkt text |
| `component::cloud::system_health::info::remote_client_certificate_required` | 987291164 | Remote client certificate required | direkt text |
| `component::control4::config::abort::wrong_account` | 987216213 | The new credentials belong to a different Control4 controller | direkt text |
| `component::control4::config::step::reauth_confirm::data::password` | 987216214 | Password (rå källa: `[%key:common::config_flow::data::password%]`) | referens |
| `component::control4::config::step::reauth_confirm::data_description::password` | 987216215 | The password of your Control4 account. | direkt text |
| `component::control4::config::step::reauth_confirm::description` | 987216216 | Enter the new password for the Control4 account {username}. | direkt text |
| `component::control4::config::step::reauth_confirm::title` | 987216217 | Authentication expired for {name} (rå källa: `[%key:common::config_flow::title::reauth%]`) | referens |
| `component::daikin_infrared::config::abort::already_configured` | 987297116 | Device is already configured (rå källa: `[%key:common::config_flow::abort::already_configured_device%]`) | referens |
| `component::daikin_infrared::config::abort::no_infrared_emitters` | 987297117 | No infrared emitter entities found. Please set up an infrared device first. (rå källa: `[%key:component::infrared::common::no_infrared_emitters%]`) | referens |
| `component::daikin_infrared::config::step::user::data::infrared_emitter_entity_id` | 987297118 | Infrared emitter (rå källa: `[%key:component::infrared::common::infrared_entity_id%]`) | referens |
| `component::daikin_infrared::config::step::user::data::infrared_receiver_entity_id` | 987297119 | Infrared receiver (rå källa: `[%key:component::infrared::common::infrared_receiver_entity_id%]`) | referens |
| `component::daikin_infrared::config::step::user::data_description::infrared_emitter_entity_id` | 987297120 | The infrared emitter entity to use for sending commands. (rå källa: `[%key:component::infrared::common::infrared_entity_id_description%]`) | referens |
| `component::daikin_infrared::config::step::user::data_description::infrared_receiver_entity_id` | 987297121 | Optional — allows the integration to update state when the physical remote is used. | direkt text |
| `component::daikin_infrared::config::step::user::description` | 987297122 | Select an infrared emitter for your Daikin AC. | direkt text |
| `component::daikin_infrared::config::step::user::title` | 987297123 | Set up Daikin AC | direkt text |
| `component::daikin_infrared::entity::climate::daikin_ac::state_attributes::fan_mode::state::silence` | 987297124 | Silence | direkt text |
| `component::ecoforest::config::abort::wrong_device` | 987216475 | The credentials belong to a different Ecoforest device than the one this entry is set up for. | direkt text |
| `component::ecoforest::config::step::reauth_confirm::data::password` | 987216476 | Password (rå källa: `[%key:common::config_flow::data::password%]`) | referens |
| `component::ecoforest::config::step::reauth_confirm::data::username` | 987216477 | Username (rå källa: `[%key:common::config_flow::data::username%]`) | referens |
| `component::ecoforest::config::step::reauth_confirm::data_description::password` | 987216478 | The password of your Ecoforest device. (rå källa: `[%key:component::ecoforest::config::step::user::data_description::password%]`) | referens |
| `component::ecoforest::config::step::reauth_confirm::data_description::username` | 987216479 | The username of your Ecoforest device. (rå källa: `[%key:component::ecoforest::config::step::user::data_description::username%]`) | referens |
| `component::ecoforest::config::step::reauth_confirm::description` | 987216480 | Authentication on the Ecoforest device at {host} failed. Enter the credentials again. | direkt text |
| `component::ecoforest::config::step::reauth_confirm::title` | 987216481 | Authentication expired for {name} (rå källa: `[%key:common::config_flow::title::reauth%]`) | referens |
| `component::ecoforest::config::step::user::data_description::password` | 987216482 | The password of your Ecoforest device. | direkt text |
| `component::ecoforest::config::step::user::data_description::username` | 987216483 | The username of your Ecoforest device. | direkt text |
| `component::elkm1::config::step::reauth_confirm::data::password` | 987216370 | Password (rå källa: `[%key:common::config_flow::data::password%]`) | referens |
| `component::elkm1::config::step::reauth_confirm::data::username` | 987216371 | Username (rå källa: `[%key:common::config_flow::data::username%]`) | referens |
| `component::elkm1::config::step::reauth_confirm::data_description::password` | 987216372 | The password of the Elk-M1 user. | direkt text |
| `component::elkm1::config::step::reauth_confirm::data_description::username` | 987216373 | The name of the Elk-M1 user. | direkt text |
| `component::elkm1::config::step::reauth_confirm::description` | 987216374 | The Elk-M1 panel rejected the credentials. Enter the current username and password. | direkt text |
| `component::elkm1::config::step::reauth_confirm::title` | 987216375 | Authentication expired for {name} (rå källa: `[%key:common::config_flow::title::reauth%]`) | referens |
| `component::elvia::config::abort::wrong_account` | 987216484 | The API token does not give access to the metering point of this entry. | direkt text |
| `component::elvia::config::step::reauth_confirm::data::api_token` | 987216485 | API token (rå källa: `[%key:common::config_flow::data::api_token%]`) | referens |
| `component::elvia::config::step::reauth_confirm::data_description::api_token` | 987216486 | The new meter value API token from Elvia. | direkt text |
| `component::elvia::config::step::reauth_confirm::description` | 987216487 | The Elvia API token is no longer valid. Enter a new one. | direkt text |
| `component::elvia::config::step::reauth_confirm::title` | 987216488 | Authentication expired for {name} (rå källa: `[%key:common::config_flow::title::reauth%]`) | referens |
| `component::elvia::exceptions::invalid_auth::message` | 987216489 | Authentication with Elvia failed | direkt text |
| `component::foreca::entity::sensor::aqi_co::name` | 987029787 | Carbon monoxide index | direkt text |
| `component::foreca::entity::sensor::aqi_no2::name` | 987029788 | Nitrogen dioxide index | direkt text |
| `component::foreca::entity::sensor::aqi_o3::name` | 987029789 | Ozone index | direkt text |
| `component::foreca::entity::sensor::aqi_pm10::name` | 987029790 | PM10 index | direkt text |
| `component::foreca::entity::sensor::aqi_pm25::name` | 987029791 | PM2.5 index | direkt text |
| `component::foreca::entity::sensor::aqi_so2::name` | 987029792 | Sulphur dioxide index | direkt text |
| `component::foreca::entity::sensor::dominant_pollutant::name` | 987029793 | Dominant pollutant | direkt text |
| `component::foreca::entity::sensor::dominant_pollutant::state::carbon_monoxide` | 987029794 | Carbon monoxide (rå källa: `[%key:component::sensor::entity_component::carbon_monoxide::name%]`) | referens |
| `component::foreca::entity::sensor::dominant_pollutant::state::nitrogen_dioxide` | 987029795 | Nitrogen dioxide (rå källa: `[%key:component::sensor::entity_component::nitrogen_dioxide::name%]`) | referens |
| `component::foreca::entity::sensor::dominant_pollutant::state::ozone` | 987029796 | Ozone (rå källa: `[%key:component::sensor::entity_component::ozone::name%]`) | referens |
| `component::foreca::entity::sensor::dominant_pollutant::state::pm10` | 987029797 | PM10 (rå källa: `[%key:component::sensor::entity_component::pm10::name%]`) | referens |
| `component::foreca::entity::sensor::dominant_pollutant::state::pm25` | 987029798 | PM2.5 (rå källa: `[%key:component::sensor::entity_component::pm25::name%]`) | referens |
| `component::foreca::entity::sensor::dominant_pollutant::state::sulphur_dioxide` | 987029799 | Sulphur dioxide (rå källa: `[%key:component::sensor::entity_component::sulphur_dioxide::name%]`) | referens |
| `component::foreca::entity::sensor::observed_precipitation::name` | 987255485 | Observed hourly precipitation | direkt text |
| `component::foreca::entity::sensor::observed_precipitation_type::name` | 987255486 | Observed precipitation type | direkt text |
| `component::foreca::entity::sensor::observed_precipitation_type::state::hail` | 987255487 | Hail | direkt text |
| `component::foreca::entity::sensor::observed_precipitation_type::state::icing` | 987255488 | Icing | direkt text |
| `component::foreca::entity::sensor::observed_precipitation_type::state::rain` | 987255489 | Rain | direkt text |
| `component::foreca::entity::sensor::observed_precipitation_type::state::sleet` | 987255490 | Sleet | direkt text |
| `component::foreca::entity::sensor::observed_precipitation_type::state::snow` | 987255491 | Snow | direkt text |
| `component::foreca::exceptions::air_quality_forecast_error::message` | 987262125 | Error fetching the air quality forecast. | direkt text |
| `component::foreca::exceptions::air_quality_update_error::message` | 987029800 | Error fetching the air quality. | direkt text |
| `component::foreca::exceptions::fifteen_minute_forecast_error::message` | 986991129 | Error fetching the 15-minute forecast. | direkt text |
| `component::foreca::services::get_15_minute_forecast::description` | 986991130 | Retrieves the forecast in 15-minute steps for the next three hours, in the weather entity's units. Every call makes a request to the Foreca Weather API and counts toward the daily limit of your plan. | direkt text |
| `component::foreca::services::get_15_minute_forecast::name` | 986991131 | Get 15-minute forecast | direkt text |
| `component::foreca::services::get_air_quality_forecast::description` | 987262126 | Retrieves the air quality index forecast, hourly for up to 85 hours or daily for 4 days. Every call makes a request to the Foreca Weather API and counts toward the daily limit of your plan. | direkt text |
| `component::foreca::services::get_air_quality_forecast::fields::type::description` | 987262127 | The forecast to return. | direkt text |
| `component::foreca::services::get_air_quality_forecast::fields::type::name` | 987262128 | Forecast type | direkt text |
| `component::foreca::services::get_air_quality_forecast::name` | 987262129 | Get air quality forecast | direkt text |
| `component::fuelprices_dk::config_subentries::station::step::user::description` | 987234636 | Try again to load the list of fuel companies. | direkt text |
| `component::fuelprices_dk::exceptions::cannot_connect::message` | 987248930 | Failed to connect (rå källa: `[%key:common::config_flow::error::cannot_connect%]`) | referens |
| `component::fuelprices_dk::exceptions::rate_limit_exceeded::message` | 987248931 | Too many requests to the API. Please try again later. (rå källa: `[%key:component::fuelprices_dk::config::abort::rate_limit_exceeded%]`) | referens |
| `component::fuelprices_dk::exceptions::request_timeout::message` | 987248932 | Timeout while establishing a connection (rå källa: `[%key:common::config_flow::error::timeout_connect%]`) | referens |
| `component::fuelprices_dk::exceptions::server_error::message` | 987248933 | Fuelprices.dk returned a server error. | direkt text |
| `component::fujitsu_infrared::config::abort::already_configured` | 987177212 | Device is already configured (rå källa: `[%key:common::config_flow::abort::already_configured_device%]`) | referens |
| `component::fujitsu_infrared::config::abort::no_infrared_emitters` | 987177213 | No infrared emitter entities found. Please set up an infrared device first. (rå källa: `[%key:component::infrared::common::no_infrared_emitters%]`) | referens |
| `component::fujitsu_infrared::config::error::no_hvac_modes` | 987177214 | Select at least one supported mode. | direkt text |
| `component::fujitsu_infrared::config::step::user::data::hvac_modes` | 987177215 | Supported modes | direkt text |
| `component::fujitsu_infrared::config::step::user::data::infrared_emitter_entity_id` | 987177216 | Infrared emitter (rå källa: `[%key:component::infrared::common::infrared_entity_id%]`) | referens |
| `component::fujitsu_infrared::config::step::user::data::infrared_receiver_entity_id` | 987177217 | Infrared receiver (rå källa: `[%key:component::infrared::common::infrared_receiver_entity_id%]`) | referens |
| `component::fujitsu_infrared::config::step::user::data::protocol` | 987177218 | Temperature steps | direkt text |
| `component::fujitsu_infrared::config::step::user::data_description::hvac_modes` | 987177219 | Select the operating modes your AC unit supports. Heat is not available on all models. | direkt text |
| `component::fujitsu_infrared::config::step::user::data_description::infrared_emitter_entity_id` | 987177220 | The infrared emitter entity to use for sending commands. (rå källa: `[%key:component::infrared::common::infrared_entity_id_description%]`) | referens |
| `component::fujitsu_infrared::config::step::user::data_description::infrared_receiver_entity_id` | 987177221 | Optional — allows the integration to update state when the physical remote is used. | direkt text |
| `component::fujitsu_infrared::config::step::user::data_description::protocol` | 987177222 | Half degrees are only carried by the extended message format. Select it if your remote's display shows half degrees in Celsius, such as 24.5. | direkt text |
| `component::fujitsu_infrared::config::step::user::description` | 987177223 | Select an infrared emitter and the modes your Fujitsu AC supports. | direkt text |
| `component::fujitsu_infrared::config::step::user::title` | 987177224 | Set up Fujitsu AC | direkt text |
| `component::fujitsu_infrared::entity::climate::fujitsu_ac::state_attributes::fan_mode::state::quiet` | 987177225 | Quiet | direkt text |
| `component::fujitsu_infrared::selector::hvac_modes::options::cool` | 987177226 | Cool | direkt text |
| `component::fujitsu_infrared::selector::hvac_modes::options::dry` | 987177227 | Dry | direkt text |
| `component::fujitsu_infrared::selector::hvac_modes::options::fan_only` | 987177228 | Fan only | direkt text |
| `component::fujitsu_infrared::selector::hvac_modes::options::heat` | 987177229 | Heat | direkt text |
| `component::fujitsu_infrared::selector::hvac_modes::options::heat_cool` | 987177230 | Heat/Cool | direkt text |
| `component::fujitsu_infrared::selector::protocol::options::extended` | 987177231 | Half degrees | direkt text |
| `component::fujitsu_infrared::selector::protocol::options::standard` | 987177232 | Whole degrees | direkt text |
| `component::google_health::entity::sensor::body_mass_index::name` | 987248841 | Body mass index | direkt text |
| `component::google_health::entity::sensor::heart_rate_variability::name` | 987248842 | Heart rate variability | direkt text |
| `component::google_health::entity::sensor::height::name` | 987248843 | Height | direkt text |
| `component::google_health::entity::sensor::oxygen_saturation::name` | 987248844 | Oxygen saturation | direkt text |
| `component::google_health::entity::sensor::respiratory_rate::name` | 987248845 | Respiratory rate | direkt text |
| `component::google_health::entity::sensor::vo2_max::name` | 987248846 | VO2 max | direkt text |
| `component::google_travel_time::config::error::invalid_referrer` | 986939754 | The HTTP referrer is not allowed for this API key. Check the website application restrictions of the API key. | direkt text |
| `component::google_travel_time::config::step::reconfigure::sections::api_key_options::data::referrer` | 986939755 | HTTP referrer | direkt text |
| `component::google_travel_time::config::step::reconfigure::sections::api_key_options::data_description::referrer` | 986939756 | Specify this only if the API key has a [website application restriction]({restricting_api_keys_url}) | direkt text |
| `component::google_travel_time::config::step::reconfigure::sections::api_key_options::name` | 986939757 | Optional API key options | direkt text |
| `component::google_travel_time::config::step::user::sections::api_key_options::data::referrer` | 986939758 | HTTP referrer | direkt text |
| `component::google_travel_time::config::step::user::sections::api_key_options::data_description::referrer` | 986939759 | Specify this only if the API key has a [website application restriction]({restricting_api_keys_url}) | direkt text |
| `component::google_travel_time::config::step::user::sections::api_key_options::name` | 986939760 | Optional API key options | direkt text |
| `component::hassio::issues::issue_core_deprecated_tcp_api_request::description` | 987248875 | Something in Home Assistant is calling the Supervisor API with the `{supervisor_token}` token, for example a request to `{reference}`.\n\nThis usually comes from a [Command line]({command_line_url}) or [Shell command]({shell_command_url}) configuration, or from a custom integration. Select Learn more to find out how to find and update it. | direkt text |
| `component::hassio::issues::issue_core_deprecated_tcp_api_request::title` | 987248876 | Deprecated use of the Supervisor API token | direkt text |
| `component::hikvision::config::step::user::data::verify_ssl` | 987248847 | Verify SSL certificate (rå källa: `[%key:common::config_flow::data::verify_ssl%]`) | referens |
| `component::hikvision::config::step::user::data_description::verify_ssl` | 987248848 | Disable if your device uses a self-signed certificate, which is what Hikvision devices ship with. Only applies when SSL is used | direkt text |
| `component::hr_energy_qube::entity::sensor::working_hours_cooling::name` | 987248934 | Working hours cooling | direkt text |
| `component::hr_energy_qube::entity::sensor::working_hours_dhw::name` | 987248935 | Working hours DHW | direkt text |
| `component::hr_energy_qube::entity::sensor::working_hours_heater::name` | 987248936 | Working hours heater {number} | direkt text |
| `component::hr_energy_qube::entity::sensor::working_hours_heating::name` | 987248937 | Working hours heating | direkt text |
| `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::candle` | 987257276 | Candle | direkt text |
| `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::cosmos` | 987257277 | Cosmos | direkt text |
| `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::enchant` | 987257278 | Enchant | direkt text |
| `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::fireplace` | 987257279 | Fireplace | direkt text |
| `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::glisten` | 987257280 | Glisten | direkt text |
| `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::opal` | 987257281 | Opal | direkt text |
| `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::prism` | 987257282 | Prism | direkt text |
| `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::sparkle` | 987257283 | Sparkle | direkt text |
| `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::sunbeam` | 987257284 | Sunbeam | direkt text |
| `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::sunrise` | 987257285 | Sunrise | direkt text |
| `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::sunset` | 987257286 | Sunset | direkt text |
| `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::underwater` | 987257287 | Underwater | direkt text |
| `component::huisbaasje::config::abort::wrong_account` | 987216821 | The credentials belong to a different EnergyFlip account than the one configured. | direkt text |
| `component::huisbaasje::config::step::reauth_confirm::data::password` | 987216822 | Password (rå källa: `[%key:common::config_flow::data::password%]`) | referens |
| `component::huisbaasje::config::step::reauth_confirm::data_description::password` | 987216823 | The current password of your EnergyFlip account. | direkt text |
| `component::huisbaasje::config::step::reauth_confirm::description` | 987216824 | The password for {username} is no longer valid. Enter the current password. | direkt text |
| `component::huisbaasje::config::step::reauth_confirm::title` | 987216825 | Authentication expired for {name} (rå källa: `[%key:common::config_flow::title::reauth%]`) | referens |
| `component::intesis_modbus::device::air_conditioner::name` | 987257189 | {gateway} air conditioner | direkt text |
| `component::intesis_modbus::exceptions::gateway_unavailable::message` | 987257190 | The gateway does not answer. | direkt text |
| `component::knx::config_panel::entities::create::_::knx::knx_group_address::used_by` | 987225837 | Used by | direkt text |
| `component::knx::exceptions::project_data_incompatible::message` | 986956444 | The KNX project data is for xknxproject {version}, which is not compatible with the installed xknxproject {installed_version}. | direkt text |
| `component::knx::exceptions::project_data_invalid::message` | 986956445 | Invalid KNX project data: {error} | direkt text |
| `component::lastfm::config::abort::auth_failed` | 987264113 | Last.fm authorization failed. Start authorization again to request a new token. | direkt text |
| `component::lastfm::config::abort::configuration_changed` | 987264114 | The Last.fm configuration changed. Start again to use the current settings. | direkt text |
| `component::lastfm::config::abort::wrong_account` | 987264115 | The authorized Last.fm account ({authorized_user}) does not match the configured account ({configured_user}). Start authorization again and use the configured account. | direkt text |
| `component::lastfm::config::error::api_secret_required` | 987264116 | Enter the API secret that matches the API key to enable authenticated access. | direkt text |
| `component::lastfm::config::error::cannot_connect` | 987264117 | Failed to connect (rå källa: `[%key:common::config_flow::error::cannot_connect%]`) | referens |
| `component::lastfm::config::step::auth_url::description` | 987264118 | Select the link below to open Last.fm and authorize Home Assistant with your account, then return here and select Submit. Setup may continue automatically once the authorization is detected. | direkt text |
| `component::lastfm::config::step::auth_url::title` | 987264119 | Authorize Home Assistant with Last.fm | direkt text |
| `component::lastfm::config::step::reauth_confirm::description` | 987264120 | Your Last.fm account needs to be authorized again. Select Submit to start authorization. | direkt text |
| `component::lastfm::config::step::reauth_confirm::title` | 987264121 | Reconnect to Last.fm | direkt text |
| `component::lastfm::config::step::reconfigure::data::api_key` | 987264122 | API key (rå källa: `[%key:common::config_flow::data::api_key%]`) | referens |
| `component::lastfm::config::step::reconfigure::data::api_secret` | 987264123 | API secret (rå källa: `[%key:component::lastfm::config::step::user::data::api_secret%]`) | referens |
| `component::lastfm::config::step::reconfigure::data::enable_authentication` | 987264124 | Enable authenticated access | direkt text |
| `component::lastfm::config::step::reconfigure::data::main_user` | 987264125 | Last.fm username (rå källa: `[%key:component::lastfm::config::step::user::data::main_user%]`) | referens |
| `component::lastfm::config::step::reconfigure::data_description::api_secret` | 987264126 | When authenticated access is enabled, leave blank to keep the existing secret. When changing the API key, enter its matching secret. | direkt text |
| `component::lastfm::config::step::reconfigure::data_description::enable_authentication` | 987264127 | Allows access to your own hidden listening information. Disabling this removes the saved authentication credentials; hidden listening information will no longer be accessible. | direkt text |
| `component::lastfm::config::step::reconfigure::data_description::main_user` | 987264128 | Select the Last.fm account to authorize. | direkt text |
| `component::lastfm::config::step::reconfigure::description` | 987264129 | Update the API credentials for this integration. Request an API account at {api_account_url}. | direkt text |
| `component::lastfm::config::step::user::data::api_secret` | 987264130 | API secret | direkt text |
| `component::lastfm::config::step::user::data_description::api_secret` | 987264131 | Optional. Lets the integration read listening information hidden by the user's Last.fm privacy settings. | direkt text |
| `component::lastfm::options::abort::configuration_changed` | 987264132 | The Last.fm configuration changed. Start again to use the current settings. (rå källa: `[%key:component::lastfm::config::abort::configuration_changed%]`) | referens |
| `component::lektrico::entity::switch::compatibility_mode::name` | 987248877 | Compatibility mode | direkt text |
| `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::aux_1` | 987275899 | Aux | direkt text |
| `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::aux_pm8006` | 987275900 | Aux | direkt text |
| `component::marantz_infrared::entity::switch::power_amp_direct::name` | 987275901 | Power amp direct | direkt text |
| `component::marantz_infrared::entity::switch::speaker_a::name` | 987275902 | Speaker A | direkt text |
| `component::marantz_infrared::entity::switch::speaker_b::name` | 987275903 | Speaker B | direkt text |
| `component::matter::entity::update::release_notes_messages::non_main_net_update_source` | 987004690 | Update provided by {update_source}. Installing this update is at your own risk and you may run into unexpected problems such as the need to re-add and factory reset your device. | direkt text |
| `component::matter::entity::update::release_notes_messages::update_duration` | 987004691 | The update process can take a while, especially for battery powered devices. Please be patient and wait until the update process is fully completed. The device may restart during the update process and be unavailable for several minutes. | direkt text |
| `component::microsoft::config::abort::already_configured` | 987217230 | Service is already configured (rå källa: `[%key:common::config_flow::abort::already_configured_service%]`) | referens |
| `component::microsoft::config::error::cannot_connect` | 987217231 | Failed to connect (rå källa: `[%key:common::config_flow::error::cannot_connect%]`) | referens |
| `component::microsoft::config::error::invalid_api_key` | 987217232 | The API key was rejected. Check that the API key is valid and that the region matches your Azure Speech resource. | direkt text |
| `component::microsoft::config::error::unknown` | 987217233 | Unexpected error (rå källa: `[%key:common::config_flow::error::unknown%]`) | referens |
| `component::microsoft::config::step::user::data::api_key` | 987217234 | API key (rå källa: `[%key:common::config_flow::data::api_key%]`) | referens |
| `component::microsoft::config::step::user::data::gender` | 987217235 | Gender | direkt text |
| `component::microsoft::config::step::user::data::language` | 987217236 | Language (rå källa: `[%key:common::config_flow::data::language%]`) | referens |
| `component::microsoft::config::step::user::data::region` | 987217237 | Region | direkt text |
| `component::microsoft::config::step::user::data::type` | 987217238 | Voice | direkt text |
| `component::microsoft::config::step::user::data_description::api_key` | 987217239 | A key of your Azure Speech resource. | direkt text |
| `component::microsoft::config::step::user::data_description::gender` | 987217240 | The gender of the voice. | direkt text |
| `component::microsoft::config::step::user::data_description::language` | 987217241 | The default language of the speech. | direkt text |
| `component::microsoft::config::step::user::data_description::region` | 987217242 | The location of your Azure Speech resource. | direkt text |
| `component::microsoft::config::step::user::data_description::type` | 987217243 | The name of the voice without the language prefix, for example `JennyNeural`. The voice must be available for the selected language. You can find the available voices in the [Microsoft documentation]({voices_url}). | direkt text |
| `component::microsoft::entity::tts::text_to_speech::name` | 987217244 | Text-to-speech | direkt text |
| `component::microsoft::exceptions::cannot_connect::message` | 987217245 | Could not connect to the Microsoft Text-to-Speech service. | direkt text |
| `component::microsoft::exceptions::invalid_api_key::message` | 987217246 | The Microsoft Text-to-Speech service rejected the API key. Check that the API key is valid and that the region matches your Azure Speech resource. | direkt text |
| `component::microsoft::exceptions::synthesis_failed::message` | 987217247 | Microsoft Text-to-Speech failed to synthesize the speech. | direkt text |
| `component::microsoft::issues::deprecated_yaml::description` | 987217248 | Configuring {integration_title} using YAML is being removed.\n\nYour existing YAML configuration has been imported into the UI automatically. The legacy `tts.{domain}_say` action (or the name you set with `service_name`) and the legacy `{domain}` text-to-speech engine keep working until you remove the YAML configuration. To fix this issue:\n\n1. Update your automations and scripts to use the `tts.speak` action with the new text-to-speech entity.\n2. Under **Settings** > **Voice assistants**, select the new text-to-speech entity in every assistant that uses the legacy `{domain}` engine.\n3. Remove the `{domain}` platform from the `tts` section of your configuration.yaml file and restart Home Assistant. | direkt text |
| `component::microsoft::issues::deprecated_yaml::title` | 987217249 | The {integration_title} YAML configuration is being removed (rå källa: `[%key:component::homeassistant::issues::deprecated_yaml::title%]`) | referens |
| `component::microsoft::issues::deprecated_yaml_import_issue_cannot_connect::description` | 987217250 | Configuring {integration_title} using YAML is being removed, but your YAML configuration could not be imported because Home Assistant could not connect to the Microsoft Text-to-Speech service.\n\nCheck the region in your YAML configuration and restart Home Assistant to try again, or remove the `{domain}` platform from the `tts` section of your configuration.yaml file and set up the integration in the UI. | direkt text |
| `component::microsoft::issues::deprecated_yaml_import_issue_cannot_connect::title` | 987217251 | The {integration_title} YAML configuration import failed | direkt text |
| `component::microsoft::issues::deprecated_yaml_import_issue_invalid_api_key::description` | 987217252 | Configuring {integration_title} using YAML is being removed, but your YAML configuration could not be imported because the API key was rejected.\n\nCheck the API key and region in your YAML configuration and restart Home Assistant to try again, or remove the `{domain}` platform from the `tts` section of your configuration.yaml file and set up the integration in the UI. | direkt text |
| `component::microsoft::issues::deprecated_yaml_import_issue_invalid_api_key::title` | 987217253 | The {integration_title} YAML configuration import failed (rå källa: `[%key:component::microsoft::issues::deprecated_yaml_import_issue_cannot_connect::title%]`) | referens |
| `component::microsoft::issues::deprecated_yaml_import_issue_unknown::description` | 987217254 | Configuring {integration_title} using YAML is being removed, but your YAML configuration could not be imported because of an unexpected error. Check the logs for details.\n\nRemove the `{domain}` platform from the `tts` section of your configuration.yaml file and set up the integration in the UI. | direkt text |
| `component::microsoft::issues::deprecated_yaml_import_issue_unknown::title` | 987217255 | The {integration_title} YAML configuration import failed (rå källa: `[%key:component::microsoft::issues::deprecated_yaml_import_issue_cannot_connect::title%]`) | referens |
| `component::microsoft::options::step::init::data::contour` | 987217256 | Pitch contour | direkt text |
| `component::microsoft::options::step::init::data::pitch` | 987217257 | Pitch | direkt text |
| `component::microsoft::options::step::init::data::rate` | 987217258 | Speaking rate | direkt text |
| `component::microsoft::options::step::init::data::volume` | 987217259 | Volume | direkt text |
| `component::microsoft::options::step::init::data_description::contour` | 987217260 | Changes of the pitch over the course of the speech, in SSML `contour` format. Leave empty to not change the pitch contour. | direkt text |
| `component::microsoft::options::step::init::data_description::pitch` | 987217261 | The pitch of the voice, for example `default`, `high` or `+10%`. | direkt text |
| `component::microsoft::options::step::init::data_description::rate` | 987217262 | Speed up or slow down the speech. | direkt text |
| `component::microsoft::options::step::init::data_description::volume` | 987217263 | Raise or lower the volume of the speech. | direkt text |
| `component::microsoft::selector::gender::options::female` | 987217264 | Female | direkt text |
| `component::microsoft::selector::gender::options::male` | 987217265 | Male | direkt text |
| `component::microsoft::selector::language::options::af-za` | 987217266 | Afrikaans (South Africa) | direkt text |
| `component::microsoft::selector::language::options::am-et` | 987217267 | Amharic (Ethiopia) | direkt text |
| `component::microsoft::selector::language::options::ar-ae` | 987217268 | Arabic (United Arab Emirates) | direkt text |
| `component::microsoft::selector::language::options::ar-bh` | 987217269 | Arabic (Bahrain) | direkt text |
| `component::microsoft::selector::language::options::ar-dz` | 987217270 | Arabic (Algeria) | direkt text |
| `component::microsoft::selector::language::options::ar-eg` | 987217271 | Arabic (Egypt) | direkt text |
| `component::microsoft::selector::language::options::ar-iq` | 987217272 | Arabic (Iraq) | direkt text |
| `component::microsoft::selector::language::options::ar-jo` | 987217273 | Arabic (Jordan) | direkt text |
| `component::microsoft::selector::language::options::ar-kw` | 987217274 | Arabic (Kuwait) | direkt text |
| `component::microsoft::selector::language::options::ar-lb` | 987217275 | Arabic (Lebanon) | direkt text |
| `component::microsoft::selector::language::options::ar-ly` | 987217276 | Arabic (Libya) | direkt text |
| `component::microsoft::selector::language::options::ar-ma` | 987217277 | Arabic (Morocco) | direkt text |
| `component::microsoft::selector::language::options::ar-om` | 987217278 | Arabic (Oman) | direkt text |
| `component::microsoft::selector::language::options::ar-qa` | 987217279 | Arabic (Qatar) | direkt text |
| `component::microsoft::selector::language::options::ar-sa` | 987217280 | Arabic (Saudi Arabia) | direkt text |
| `component::microsoft::selector::language::options::ar-sy` | 987217281 | Arabic (Syria) | direkt text |
| `component::microsoft::selector::language::options::ar-tn` | 987217282 | Arabic (Tunisia) | direkt text |
| `component::microsoft::selector::language::options::ar-ye` | 987217283 | Arabic (Yemen) | direkt text |
| `component::microsoft::selector::language::options::as-in` | 987217284 | Assamese (India) | direkt text |
| `component::microsoft::selector::language::options::az-az` | 987217285 | Azerbaijani (Latin, Azerbaijan) | direkt text |
| `component::microsoft::selector::language::options::bg-bg` | 987217286 | Bulgarian (Bulgaria) | direkt text |
| `component::microsoft::selector::language::options::bn-bd` | 987217287 | Bangla (Bangladesh) | direkt text |
| `component::microsoft::selector::language::options::bn-in` | 987217288 | Bengali (India) | direkt text |
| `component::microsoft::selector::language::options::bs-ba` | 987217289 | Bosnian (Bosnia and Herzegovina) | direkt text |
| `component::microsoft::selector::language::options::ca-es` | 987217290 | Catalan | direkt text |
| `component::microsoft::selector::language::options::cs-cz` | 987217291 | Czech (Czechia) | direkt text |
| `component::microsoft::selector::language::options::cy-gb` | 987217292 | Welsh (United Kingdom) | direkt text |
| `component::microsoft::selector::language::options::da-dk` | 987217293 | Danish (Denmark) | direkt text |
| `component::microsoft::selector::language::options::de-at` | 987217294 | German (Austria) | direkt text |
| `component::microsoft::selector::language::options::de-ch` | 987217295 | German (Switzerland) | direkt text |
| `component::microsoft::selector::language::options::de-de` | 987217296 | German (Germany) | direkt text |
| `component::microsoft::selector::language::options::el-gr` | 987217297 | Greek (Greece) | direkt text |
| `component::microsoft::selector::language::options::en-au` | 987217298 | English (Australia) | direkt text |
| `component::microsoft::selector::language::options::en-ca` | 987217299 | English (Canada) | direkt text |
| `component::microsoft::selector::language::options::en-gb` | 987217300 | English (United Kingdom) | direkt text |
| `component::microsoft::selector::language::options::en-hk` | 987217301 | English (Hong Kong SAR) | direkt text |
| `component::microsoft::selector::language::options::en-ie` | 987217302 | English (Ireland) | direkt text |
| `component::microsoft::selector::language::options::en-in` | 987217303 | English (India) | direkt text |
| `component::microsoft::selector::language::options::en-ke` | 987217304 | English (Kenya) | direkt text |
| `component::microsoft::selector::language::options::en-ng` | 987217305 | English (Nigeria) | direkt text |
| `component::microsoft::selector::language::options::en-nz` | 987217306 | English (New Zealand) | direkt text |
| `component::microsoft::selector::language::options::en-ph` | 987217307 | English (Philippines) | direkt text |
| `component::microsoft::selector::language::options::en-sg` | 987217308 | English (Singapore) | direkt text |
| `component::microsoft::selector::language::options::en-tz` | 987217309 | English (Tanzania) | direkt text |
| `component::microsoft::selector::language::options::en-us` | 987217310 | English (United States) | direkt text |
| `component::microsoft::selector::language::options::en-za` | 987217311 | English (South Africa) | direkt text |
| `component::microsoft::selector::language::options::es-ar` | 987217312 | Spanish (Argentina) | direkt text |
| `component::microsoft::selector::language::options::es-bo` | 987217313 | Spanish (Bolivia) | direkt text |
| `component::microsoft::selector::language::options::es-cl` | 987217314 | Spanish (Chile) | direkt text |
| `component::microsoft::selector::language::options::es-co` | 987217315 | Spanish (Colombia) | direkt text |
| `component::microsoft::selector::language::options::es-cr` | 987217316 | Spanish (Costa Rica) | direkt text |
| `component::microsoft::selector::language::options::es-cu` | 987217317 | Spanish (Cuba) | direkt text |
| `component::microsoft::selector::language::options::es-do` | 987217318 | Spanish (Dominican Republic) | direkt text |
| `component::microsoft::selector::language::options::es-ec` | 987217319 | Spanish (Ecuador) | direkt text |
| `component::microsoft::selector::language::options::es-es` | 987217320 | Spanish (Spain) | direkt text |
| `component::microsoft::selector::language::options::es-gq` | 987217321 | Spanish (Equatorial Guinea) | direkt text |
| `component::microsoft::selector::language::options::es-gt` | 987217322 | Spanish (Guatemala) | direkt text |
| `component::microsoft::selector::language::options::es-hn` | 987217323 | Spanish (Honduras) | direkt text |
| `component::microsoft::selector::language::options::es-mx` | 987217324 | Spanish (Mexico) | direkt text |
| `component::microsoft::selector::language::options::es-ni` | 987217325 | Spanish (Nicaragua) | direkt text |
| `component::microsoft::selector::language::options::es-pa` | 987217326 | Spanish (Panama) | direkt text |
| `component::microsoft::selector::language::options::es-pe` | 987217327 | Spanish (Peru) | direkt text |
| `component::microsoft::selector::language::options::es-pr` | 987217328 | Spanish (Puerto Rico) | direkt text |
| `component::microsoft::selector::language::options::es-py` | 987217329 | Spanish (Paraguay) | direkt text |
| `component::microsoft::selector::language::options::es-sv` | 987217330 | Spanish (El Salvador) | direkt text |
| `component::microsoft::selector::language::options::es-us` | 987217331 | Spanish (United States) | direkt text |
| `component::microsoft::selector::language::options::es-uy` | 987217332 | Spanish (Uruguay) | direkt text |
| `component::microsoft::selector::language::options::es-ve` | 987217333 | Spanish (Venezuela) | direkt text |
| `component::microsoft::selector::language::options::et-ee` | 987217334 | Estonian (Estonia) | direkt text |
| `component::microsoft::selector::language::options::eu-es` | 987217335 | Basque | direkt text |
| `component::microsoft::selector::language::options::fa-ir` | 987217336 | Persian (Iran) | direkt text |
| `component::microsoft::selector::language::options::fi-fi` | 987217337 | Finnish (Finland) | direkt text |
| `component::microsoft::selector::language::options::fil-ph` | 987217338 | Filipino (Philippines) | direkt text |
| `component::microsoft::selector::language::options::fr-be` | 987217339 | French (Belgium) | direkt text |
| `component::microsoft::selector::language::options::fr-ca` | 987217340 | French (Canada) | direkt text |
| `component::microsoft::selector::language::options::fr-ch` | 987217341 | French (Switzerland) | direkt text |
| `component::microsoft::selector::language::options::fr-fr` | 987217342 | French (France) | direkt text |
| `component::microsoft::selector::language::options::ga-ie` | 987217343 | Irish (Ireland) | direkt text |
| `component::microsoft::selector::language::options::gl-es` | 987217344 | Galician | direkt text |
| `component::microsoft::selector::language::options::gu-in` | 987217345 | Gujarati (India) | direkt text |
| `component::microsoft::selector::language::options::he-il` | 987217346 | Hebrew (Israel) | direkt text |
| `component::microsoft::selector::language::options::hi-in` | 987217347 | Hindi (India) | direkt text |
| `component::microsoft::selector::language::options::hr-hr` | 987217348 | Croatian (Croatia) | direkt text |
| `component::microsoft::selector::language::options::hu-hu` | 987217349 | Hungarian (Hungary) | direkt text |
| `component::microsoft::selector::language::options::hy-am` | 987217350 | Armenian (Armenia) | direkt text |
| `component::microsoft::selector::language::options::id-id` | 987217351 | Indonesian (Indonesia) | direkt text |
| `component::microsoft::selector::language::options::is-is` | 987217352 | Icelandic (Iceland) | direkt text |
| `component::microsoft::selector::language::options::it-it` | 987217353 | Italian (Italy) | direkt text |
| `component::microsoft::selector::language::options::iu-cans-ca` | 987217354 | Inuktitut (Syllabics, Canada) | direkt text |
| `component::microsoft::selector::language::options::iu-latn-ca` | 987217355 | Inuktitut (Latin, Canada) | direkt text |
| `component::microsoft::selector::language::options::ja-jp` | 987217356 | Japanese (Japan) | direkt text |
| `component::microsoft::selector::language::options::jv-id` | 987217357 | Javanese (Latin, Indonesia) | direkt text |
| `component::microsoft::selector::language::options::ka-ge` | 987217358 | Georgian (Georgia) | direkt text |
| `component::microsoft::selector::language::options::kk-kz` | 987217359 | Kazakh (Kazakhstan) | direkt text |
| `component::microsoft::selector::language::options::km-kh` | 987217360 | Khmer (Cambodia) | direkt text |
| `component::microsoft::selector::language::options::kn-in` | 987217361 | Kannada (India) | direkt text |
| `component::microsoft::selector::language::options::ko-kr` | 987217362 | Korean (Korea) | direkt text |
| `component::microsoft::selector::language::options::lo-la` | 987217363 | Lao (Laos) | direkt text |
| `component::microsoft::selector::language::options::lt-lt` | 987217364 | Lithuanian (Lithuania) | direkt text |
| `component::microsoft::selector::language::options::lv-lv` | 987217365 | Latvian (Latvia) | direkt text |
| `component::microsoft::selector::language::options::mk-mk` | 987217366 | Macedonian (North Macedonia) | direkt text |
| `component::microsoft::selector::language::options::ml-in` | 987217367 | Malayalam (India) | direkt text |
| `component::microsoft::selector::language::options::mn-mn` | 987217368 | Mongolian (Mongolia) | direkt text |
| `component::microsoft::selector::language::options::mr-in` | 987217369 | Marathi (India) | direkt text |
| `component::microsoft::selector::language::options::ms-my` | 987217370 | Malay (Malaysia) | direkt text |
| `component::microsoft::selector::language::options::mt-mt` | 987217371 | Maltese (Malta) | direkt text |
| `component::microsoft::selector::language::options::my-mm` | 987217372 | Burmese (Myanmar) | direkt text |
| `component::microsoft::selector::language::options::nb-no` | 987217373 | Norwegian Bokmål (Norway) | direkt text |
| `component::microsoft::selector::language::options::ne-np` | 987217374 | Nepali (Nepal) | direkt text |
| `component::microsoft::selector::language::options::nl-be` | 987217375 | Dutch (Belgium) | direkt text |
| `component::microsoft::selector::language::options::nl-nl` | 987217376 | Dutch (Netherlands) | direkt text |
| `component::microsoft::selector::language::options::or-in` | 987217377 | Odia (India) | direkt text |
| `component::microsoft::selector::language::options::pa-in` | 987217378 | Punjabi (India) | direkt text |
| `component::microsoft::selector::language::options::pl-pl` | 987217379 | Polish (Poland) | direkt text |
| `component::microsoft::selector::language::options::ps-af` | 987217380 | Pashto (Afghanistan) | direkt text |
| `component::microsoft::selector::language::options::pt-br` | 987217381 | Portuguese (Brazil) | direkt text |
| `component::microsoft::selector::language::options::pt-pt` | 987217382 | Portuguese (Portugal) | direkt text |
| `component::microsoft::selector::language::options::ro-ro` | 987217383 | Romanian (Romania) | direkt text |
| `component::microsoft::selector::language::options::ru-ru` | 987217384 | Russian (Russia) | direkt text |
| `component::microsoft::selector::language::options::si-lk` | 987217385 | Sinhala (Sri Lanka) | direkt text |
| `component::microsoft::selector::language::options::sk-sk` | 987217386 | Slovak (Slovakia) | direkt text |
| `component::microsoft::selector::language::options::sl-si` | 987217387 | Slovenian (Slovenia) | direkt text |
| `component::microsoft::selector::language::options::so-so` | 987217388 | Somali (Somalia) | direkt text |
| `component::microsoft::selector::language::options::sq-al` | 987217389 | Albanian (Albania) | direkt text |
| `component::microsoft::selector::language::options::sr-latn-rs` | 987217390 | Serbian (Latin, Serbia) | direkt text |
| `component::microsoft::selector::language::options::sr-rs` | 987217391 | Serbian (Cyrillic, Serbia) | direkt text |
| `component::microsoft::selector::language::options::su-id` | 987217392 | Sundanese (Indonesia) | direkt text |
| `component::microsoft::selector::language::options::sv-se` | 987217393 | Swedish (Sweden) | direkt text |
| `component::microsoft::selector::language::options::sw-ke` | 987217394 | Kiswahili (Kenya) | direkt text |
| `component::microsoft::selector::language::options::sw-tz` | 987217395 | Kiswahili (Tanzania) | direkt text |
| `component::microsoft::selector::language::options::ta-in` | 987217396 | Tamil (India) | direkt text |
| `component::microsoft::selector::language::options::ta-lk` | 987217397 | Tamil (Sri Lanka) | direkt text |
| `component::microsoft::selector::language::options::ta-my` | 987217398 | Tamil (Malaysia) | direkt text |
| `component::microsoft::selector::language::options::ta-sg` | 987217399 | Tamil (Singapore) | direkt text |
| `component::microsoft::selector::language::options::te-in` | 987217400 | Telugu (India) | direkt text |
| `component::microsoft::selector::language::options::th-th` | 987217401 | Thai (Thailand) | direkt text |
| `component::microsoft::selector::language::options::tr-tr` | 987217402 | Turkish (Türkiye) | direkt text |
| `component::microsoft::selector::language::options::uk-ua` | 987217403 | Ukrainian (Ukraine) | direkt text |
| `component::microsoft::selector::language::options::ur-in` | 987217404 | Urdu (India) | direkt text |
| `component::microsoft::selector::language::options::ur-pk` | 987217405 | Urdu (Pakistan) | direkt text |
| `component::microsoft::selector::language::options::uz-uz` | 987217406 | Uzbek (Latin, Uzbekistan) | direkt text |
| `component::microsoft::selector::language::options::vi-vn` | 987217407 | Vietnamese (Vietnam) | direkt text |
| `component::microsoft::selector::language::options::wuu-cn` | 987217408 | Chinese (Wu, Simplified) | direkt text |
| `component::microsoft::selector::language::options::yue-cn` | 987217409 | Chinese (Cantonese, Simplified) | direkt text |
| `component::microsoft::selector::language::options::zh-cn` | 987217410 | Chinese (Mandarin, Simplified) | direkt text |
| `component::microsoft::selector::language::options::zh-cn-guangxi` | 987217411 | Chinese (Guangxi Accent Mandarin, Simplified) | direkt text |
| `component::microsoft::selector::language::options::zh-cn-henan` | 987217412 | Chinese (Zhongyuan Mandarin Henan, Simplified) | direkt text |
| `component::microsoft::selector::language::options::zh-cn-liaoning` | 987217413 | Chinese (Northeastern Mandarin, Simplified) | direkt text |
| `component::microsoft::selector::language::options::zh-cn-shaanxi` | 987217414 | Chinese (Zhongyuan Mandarin Shaanxi, Simplified) | direkt text |
| `component::microsoft::selector::language::options::zh-cn-shandong` | 987217415 | Chinese (Jilu Mandarin, Simplified) | direkt text |
| `component::microsoft::selector::language::options::zh-cn-sichuan` | 987217416 | Chinese (Southwestern Mandarin, Simplified) | direkt text |
| `component::microsoft::selector::language::options::zh-hk` | 987217417 | Chinese (Cantonese, Traditional) | direkt text |
| `component::microsoft::selector::language::options::zh-tw` | 987217418 | Chinese (Taiwanese Mandarin, Traditional) | direkt text |
| `component::microsoft::selector::language::options::zu-za` | 987217419 | isiZulu (South Africa) | direkt text |
| `component::microsoft::selector::region::options::australiaeast` | 987217420 | Australia East | direkt text |
| `component::microsoft::selector::region::options::brazilsouth` | 987217421 | Brazil South | direkt text |
| `component::microsoft::selector::region::options::canadacentral` | 987217422 | Canada Central | direkt text |
| `component::microsoft::selector::region::options::canadaeast` | 987217423 | Canada East | direkt text |
| `component::microsoft::selector::region::options::centralindia` | 987217424 | Central India | direkt text |
| `component::microsoft::selector::region::options::centralus` | 987217425 | Central US | direkt text |
| `component::microsoft::selector::region::options::eastasia` | 987217426 | East Asia | direkt text |
| `component::microsoft::selector::region::options::eastus` | 987217427 | East US | direkt text |
| `component::microsoft::selector::region::options::eastus2` | 987217428 | East US 2 | direkt text |
| `component::microsoft::selector::region::options::francecentral` | 987217429 | France Central | direkt text |
| `component::microsoft::selector::region::options::germanywestcentral` | 987217430 | Germany West Central | direkt text |
| `component::microsoft::selector::region::options::italynorth` | 987217431 | Italy North | direkt text |
| `component::microsoft::selector::region::options::japaneast` | 987217432 | Japan East | direkt text |
| `component::microsoft::selector::region::options::japanwest` | 987217433 | Japan West | direkt text |
| `component::microsoft::selector::region::options::koreacentral` | 987217434 | Korea Central | direkt text |
| `component::microsoft::selector::region::options::northcentralus` | 987217435 | North Central US | direkt text |
| `component::microsoft::selector::region::options::northeurope` | 987217436 | North Europe | direkt text |
| `component::microsoft::selector::region::options::norwayeast` | 987217437 | Norway East | direkt text |
| `component::microsoft::selector::region::options::qatarcentral` | 987217438 | Qatar Central | direkt text |
| `component::microsoft::selector::region::options::southafricanorth` | 987217439 | South Africa North | direkt text |
| `component::microsoft::selector::region::options::southcentralus` | 987217440 | South Central US | direkt text |
| `component::microsoft::selector::region::options::southeastasia` | 987217441 | Southeast Asia | direkt text |
| `component::microsoft::selector::region::options::swedencentral` | 987217442 | Sweden Central | direkt text |
| `component::microsoft::selector::region::options::switzerlandnorth` | 987217443 | Switzerland North | direkt text |
| `component::microsoft::selector::region::options::switzerlandwest` | 987217444 | Switzerland West | direkt text |
| `component::microsoft::selector::region::options::uaenorth` | 987217445 | UAE North | direkt text |
| `component::microsoft::selector::region::options::uksouth` | 987217446 | UK South | direkt text |
| `component::microsoft::selector::region::options::ukwest` | 987217447 | UK West | direkt text |
| `component::microsoft::selector::region::options::westcentralus` | 987217448 | West Central US | direkt text |
| `component::microsoft::selector::region::options::westeurope` | 987217449 | West Europe | direkt text |
| `component::microsoft::selector::region::options::westus` | 987217450 | West US | direkt text |
| `component::microsoft::selector::region::options::westus2` | 987217451 | West US 2 | direkt text |
| `component::microsoft::selector::region::options::westus3` | 987217452 | West US 3 | direkt text |
| `component::modbus::exceptions::unknown_hub::message` | 987266420 | Modbus hub {hub} is not configured. | direkt text |
| `component::myuplink::exceptions::get_datapoint_error::message` | 986936339 | Failed to get value for datapoint {point} on device {device}. | direkt text |
| `component::myuplink::selector::datapoint::fields::datapoint_id::description` | 986936340 | The ID of the datapoint. Typically a five-digit number. | direkt text |
| `component::myuplink::selector::datapoint::fields::datapoint_id::name` | 986936341 | Datapoint | direkt text |
| `component::myuplink::services::get_datapoints::description` | 986936342 | Gets the values for a list of datapoint on a device. | direkt text |
| `component::myuplink::services::get_datapoints::fields::datapoints::description` | 986936343 | A list of datapoints to get, each containing a datapoint ID. | direkt text |
| `component::myuplink::services::get_datapoints::fields::datapoints::name` | 986936344 | Datapoints | direkt text |
| `component::myuplink::services::get_datapoints::fields::device_id::description` | 986936345 | The target device for this action. | direkt text |
| `component::myuplink::services::get_datapoints::fields::device_id::name` | 986936346 | Device | direkt text |
| `component::myuplink::services::get_datapoints::name` | 986936347 | Get datapoints | direkt text |
| `component::neopool::options::abort::entry_not_loaded` | 986956422 | The options can be changed once the device has been set up. | direkt text |
| `component::netatmo::entity::sensor::heating_power_request::name` | 986939998 | Heating power request | direkt text |
| `component::netio::entity::sensor::current::name` | 987318985 | {output_name} current | direkt text |
| `component::netio::entity::sensor::energy::name` | 987318986 | {output_name} energy | direkt text |
| `component::netio::entity::sensor::load::name` | 987318987 | {output_name} load | direkt text |
| `component::netio::entity::sensor::power_factor::name` | 987318988 | {output_name} power factor | direkt text |
| `component::netio::entity::sensor::reverse_energy::name` | 987318989 | {output_name} reverse energy | direkt text |
| `component::netio::entity::sensor::total_energy::name` | 987318990 | {output_name} total energy | direkt text |
| `component::netio::entity::sensor::total_reverse_energy::name` | 987318991 | {output_name} total reverse energy | direkt text |
| `component::nexblue::entity::number::dynamic_current_limit::name` | 986961143 | Current limit | direkt text |
| `component::nexblue::entity::sensor::household_consumption_month::name` | 987319094 | Household consumption this month | direkt text |
| `component::nexblue::entity::sensor::household_consumption_today::name` | 987319095 | Household consumption today | direkt text |
| `component::nexblue::entity::sensor::household_consumption_year::name` | 987319096 | Household consumption this year | direkt text |
| `component::omnilogic::config::step::reauth_confirm::data::password` | 987216381 | Password (rå källa: `[%key:common::config_flow::data::password%]`) | referens |
| `component::omnilogic::config::step::reauth_confirm::data_description::password` | 987216382 | The new password of your Hayward OmniLogic account. | direkt text |
| `component::omnilogic::config::step::reauth_confirm::description` | 987216383 | The password for {username} is no longer valid. Enter the new password. | direkt text |
| `component::omnilogic::config::step::reauth_confirm::title` | 987216384 | Authentication expired for {name} (rå källa: `[%key:common::config_flow::title::reauth%]`) | referens |
| `component::opendisplay::exceptions::device_not_configured::message` | 986960697 | The OpenDisplay device has no stored configuration. Configure it with the OpenDisplay website or CLI, then reload the integration. | direkt text |
| `component::opendisplay::exceptions::display_not_supported::message` | 986960698 | Images cannot be uploaded to this device: its configuration has no display, or a color scheme this integration does not support yet. | direkt text |
| `component::poolsense::config::step::reauth_confirm::data::password` | 987216572 | Password (rå källa: `[%key:common::config_flow::data::password%]`) | referens |
| `component::poolsense::config::step::reauth_confirm::data_description::password` | 987216573 | The new password of your PoolSense account. | direkt text |
| `component::poolsense::config::step::reauth_confirm::description` | 987216574 | Enter the new password for {email}. | direkt text |
| `component::poolsense::config::step::reauth_confirm::title` | 987216575 | Authentication expired for {name} (rå källa: `[%key:common::config_flow::title::reauth%]`) | referens |
| `component::portainer::entity::button::pull_image::name` | 987217211 | Pull image | direkt text |
| `component::portainer::entity::sensor::container_exit_code::name` | 986945706 | Last exit code | direkt text |
| `component::portainer::exceptions::image_pull_failed::message` | 987217212 | Failed to pull image {image}. If the image is in a private registry, recreate the container instead. | direkt text |
| `component::portainer::exceptions::image_pull_timeout::message` | 987217213 | Pulling the image took too long. | direkt text |
| `component::schlage::exceptions::schlage_command_failed::message` | 987248878 | Failed to send the command to the lock. | direkt text |
| `component::shelly::entity::update::release_notes_messages::multi_step_update` | 987226061 | This update reorganizes the device memory and can run in two steps. The device installs the update and restarts, and may come back still reporting the previous firmware version. About a minute and a half later, it downloads the update again and restarts once more on the new version. Do not restart, remove power from, or otherwise interrupt the device until it reports the new firmware version. If the device comes back on the previous version and the second step does not start within a few minutes, start the update again. | direkt text |
| `component::skoda::entity::climate::air_conditioning::name` | 987020991 | Air conditioning | direkt text |
| `component::skoda::exceptions::invalid_hvac_mode::message` | 987020992 | HVAC mode {hvac_mode} is not supported. Supported modes are: {hvac_modes}. | direkt text |
| `component::smartyplants::entity::binary_sensor::needs_attention::name` | 987006354 | Needs attention | direkt text |
| `component::smartyplants::entity::sensor::last_reported::name` | 987006355 | Last reported | direkt text |
| `component::sonos::exceptions::join_different_household::message` | 986938245 | Cannot join {entity_id} to {target_entity_id} because they belong to different Sonos households. | direkt text |
| `component::starlink::entity::sensor::signal_quality::name` | 987355994 | Signal quality | direkt text |
| `component::system_bridge::services::dismiss_message::description` | 987257099 | Closes a notification sent with the System Bridge send message action. Linux only. | direkt text |
| `component::system_bridge::services::dismiss_message::fields::id::description` | 987257100 | The ID returned by the System Bridge send message action. | direkt text |
| `component::system_bridge::services::dismiss_message::fields::id::name` | 987257101 | ID | direkt text |
| `component::system_bridge::services::dismiss_message::name` | 987257102 | Dismiss message | direkt text |
| `component::tellduslive::config::step::reauth_confirm::description` | 987209869 | Home Assistant can no longer access your Telldus Live account. Select **Submit** to authorize **Home Assistant** again. | direkt text |
| `component::tellduslive::config::step::reauth_confirm::title` | 987209870 | Authentication expired for {name} (rå källa: `[%key:common::config_flow::title::reauth%]`) | referens |
| `component::template::config::step::light::data::temperature_kelvin` | 987356740 | Color temperature | direkt text |
| `component::template::config::step::light::data_description::temperature_kelvin` | 987356741 | Defines a template to get the color temperature of the light in kelvin. | direkt text |
| `component::template::issues::deprecated_light_mireds_options::description` | 987356742 | The template light entity with `{identifier}` uses options in mireds. These options are deprecated and will be removed in a future version of Home Assistant.\n\nUpdate your YAML configuration by replacing the following options and change their templates to render kelvin instead of mireds:\n\n{options}\n\nThe lowest mireds value is the highest kelvin value, so `min_mireds` is replaced by `max_kelvin` and `max_mireds` by `min_kelvin`.\n\nAfter updating the configuration, reload the template entities or restart Home Assistant to fix this issue. | direkt text |
| `component::template::issues::deprecated_light_mireds_options::title` | 987356743 | Template light entity uses deprecated options in mireds ({identifier}) | direkt text |
| `component::template::issues::deprecated_light_mireds_options_blueprint::description` | 987356744 | The template light blueprint `{blueprint}` uses options in mireds. These options are deprecated and will be removed in a future version of Home Assistant.\n\nUpdate the blueprint by replacing the following options and change their templates to render kelvin instead of mireds:\n\n{options}\n\nThe lowest mireds value is the highest kelvin value, so `min_mireds` is replaced by `max_kelvin` and `max_mireds` by `min_kelvin`.\n\nIf the blueprint was imported, re-import it once its author has updated it instead. Then reload the template entities or restart Home Assistant to fix this issue. | direkt text |
| `component::template::issues::deprecated_light_mireds_options_blueprint::title` | 987356745 | Template light blueprint uses deprecated options in mireds ({blueprint}) | direkt text |
| `component::template::issues::deprecated_light_temperature::description` | 987356746 | The template light helper {name} defines its color temperature in mireds. This is deprecated and will stop working in Home Assistant Core {breaks_in_ha_version}.\n\nTo fix this issue, open the options of the template light helper and define the color temperature in kelvin, or remove the actions on set color temperature if the light should not support a color temperature. | direkt text |
| `component::template::issues::deprecated_light_temperature::title` | 987356747 | Template light helper {name} uses a color temperature in mireds | direkt text |
| `component::template::issues::deprecated_weather_template_options::description` | 987234710 | The template weather entity with `{identifier}` uses options ending in `_template`. These options are deprecated and will be removed in a future version of Home Assistant.\n\nUpdate your YAML configuration by renaming the following options:\n\n{options}\n\nAfter updating the configuration, reload the template entities or restart Home Assistant to fix this issue. | direkt text |
| `component::template::issues::deprecated_weather_template_options::title` | 987234711 | Template weather entity uses deprecated options ({identifier}) | direkt text |
| `component::template::issues::deprecated_weather_template_options_blueprint::description` | 987234712 | The template weather blueprint `{blueprint}` uses options ending in `_template`. These options are deprecated and will be removed in a future version of Home Assistant.\n\nUpdate the blueprint by renaming the following options:\n\n{options}\n\nIf the blueprint was imported, re-import it once its author has updated it instead. Then reload the template entities or restart Home Assistant to fix this issue. | direkt text |
| `component::template::issues::deprecated_weather_template_options_blueprint::title` | 987234713 | Template weather blueprint uses deprecated options ({blueprint}) | direkt text |
| `component::template::options::step::light::data::temperature_kelvin` | 987356748 | Color temperature (rå källa: `[%key:component::template::config::step::light::data::temperature_kelvin%]`) | referens |
| `component::template::options::step::light::data_description::temperature_kelvin` | 987356749 | Defines a template to get the color temperature of the light in kelvin. (rå källa: `[%key:component::template::config::step::light::data_description::temperature_kelvin%]`) | referens |
| `component::teslemetry::exceptions::energy_site_not_paired::message` | 987003127 | Teslemetry is not paired with the Powerwall system for {site}, pair it in the Teslemetry console or set up local control | direkt text |
| `component::teslemetry::issues::energy_site_not_paired::fix_flow::error::not_resolved` | 987003128 | Teslemetry still appears to be unpaired. Please complete the pairing at {link}, then try again. | direkt text |
| `component::teslemetry::issues::energy_site_not_paired::fix_flow::step::confirm::description` | 987003129 | Home Assistant cannot send battery commands, such as dispatching battery power, to {site} because Teslemetry is not paired with its Powerwall system and local control is not set up. Teslemetry can only send these commands through the cloud once its key is verified on the Powerwall gateway.\n\n1. Open {link}.\n2. Follow the prompts to pair Teslemetry with the Powerwall system.\n3. Select **Submit** below to re-check.\n\nAlternatively, set up local control for {site}. | direkt text |
| `component::teslemetry::issues::energy_site_not_paired::fix_flow::step::confirm::title` | 987003130 | Pair Teslemetry with the Powerwall system for {site} (rå källa: `[%key:component::teslemetry::issues::energy_site_not_paired::title%]`) | referens |
| `component::teslemetry::issues::energy_site_not_paired::title` | 987003131 | Pair Teslemetry with the Powerwall system for {site} | direkt text |
| `component::threema::entity::image::gateway_qr_code::name` | 987264435 | Gateway QR code | direkt text |
| `component::unifi::device::outlet::name` | 987217214 | Outlet {index} | direkt text |
| `component::unifi::entity::select::firewall_policy_schedule_mode::name` | 987257732 | {policy_name} schedule | direkt text |
| `component::unifi::entity::select::firewall_policy_schedule_mode::state::always` | 987257733 | Always | direkt text |
| `component::unifi::entity::select::firewall_policy_schedule_mode::state::custom` | 987257734 | Custom | direkt text |
| `component::unifi::entity::select::firewall_policy_schedule_mode::state::every_day` | 987257735 | Every day | direkt text |
| `component::unifi::entity::select::firewall_policy_schedule_mode::state::every_week` | 987257736 | Every week | direkt text |
| `component::unifi::entity::select::firewall_policy_schedule_mode::state::one_time` | 987257737 | One time | direkt text |
| `component::unifi::exceptions::schedule_mode_not_supported::message` | 987257738 | This schedule mode can only be set in UniFi Network | direkt text |
| `component::upcloud::config::step::reauth_confirm::data::password` | 987216826 | Password (rå källa: `[%key:common::config_flow::data::password%]`) | referens |
| `component::upcloud::config::step::reauth_confirm::data_description::password` | 987216827 | The new password of the UpCloud API user. | direkt text |
| `component::upcloud::config::step::reauth_confirm::description` | 987216828 | The password for {username} is no longer valid. | direkt text |
| `component::upcloud::config::step::reauth_confirm::title` | 987216829 | Authentication expired for {name} (rå källa: `[%key:common::config_flow::title::reauth%]`) | referens |
| `component::vesync::entity::sensor::hepa_filter_life::name` | 987257109 | HEPA filter lifetime | direkt text |
| `component::vesync::entity::sensor::voc::name` | 987257110 | Volatile organic compounds | direkt text |
| `component::vicare::entity::binary_sensor::boiler_internal_pump::name` | 987257357 | Internal pump | direkt text |
| `component::vicare::entity::sensor::boiler_internal_pump_modulation::name` | 987257358 | Internal pump modulation | direkt text |
| `component::vicare::entity::sensor::boiler_internal_pump_target_modulation::name` | 987257359 | Internal pump target modulation | direkt text |
| `component::volkszaehler::config::step::reconfigure::data::middleware` | 987261306 | Use middleware.php (rå källa: `[%key:component::volkszaehler::config::step::user::data::middleware%]`) | referens |
| `component::volkszaehler::config::step::reconfigure::data_description::middleware` | 987261307 | Enable if your Volkszaehler instance uses 'middleware.php' in the URL (standard setup). Disable for Docker setups or custom endpoints without 'middleware.php'. (rå källa: `[%key:component::volkszaehler::config::step::user::data_description::middleware%]`) | referens |
| `component::volkszaehler::config::step::user::data::middleware` | 987261308 | Use middleware.php | direkt text |
| `component::volkszaehler::config::step::user::data_description::middleware` | 987261309 | Enable if your Volkszaehler instance uses 'middleware.php' in the URL (standard setup). Disable for Docker setups or custom endpoints without 'middleware.php'. | direkt text |
| `component::weatherkit::config::step::reauth_confirm::data::key_id` | 987216385 | Key ID (rå källa: `[%key:component::weatherkit::config::step::user::data::key_id%]`) | referens |
| `component::weatherkit::config::step::reauth_confirm::data::key_pem` | 987216386 | Private key (.p8) (rå källa: `[%key:component::weatherkit::config::step::user::data::key_pem%]`) | referens |
| `component::weatherkit::config::step::reauth_confirm::data_description::key_id` | 987216387 | The ID of the new WeatherKit key. | direkt text |
| `component::weatherkit::config::step::reauth_confirm::data_description::key_pem` | 987216388 | The contents of the new private key file (.p8). | direkt text |
| `component::weatherkit::config::step::reauth_confirm::description` | 987216389 | Your WeatherKit key is no longer valid. Enter a new key ID and private key. | direkt text |
| `component::weatherkit::config::step::reauth_confirm::title` | 987216390 | Authentication expired for {name} (rå källa: `[%key:common::config_flow::title::reauth%]`) | referens |
| `component::workday::config::step::options::sections::country_settings::data::hindu_show_estimated` | 987217215 | Mark estimated Hindu holidays | direkt text |
| `component::workday::config::step::options::sections::country_settings::data::include_sundays` | 987217216 | Include Sundays as holidays | direkt text |
| `component::workday::config::step::options::sections::country_settings::data::islamic_show_estimated` | 987217217 | Mark estimated Islamic holidays | direkt text |
| `component::workday::config::step::options::sections::country_settings::data_description::hindu_show_estimated` | 987217218 | Add "estimated" to the name of Hindu holidays with an estimated date | direkt text |
| `component::workday::config::step::options::sections::country_settings::data_description::include_sundays` | 987217219 | Add all Sundays to the holidays of the country | direkt text |
| `component::workday::config::step::options::sections::country_settings::data_description::islamic_show_estimated` | 987217220 | Add "estimated" to the name of Islamic holidays with an estimated date | direkt text |
| `component::workday::options::step::init::sections::country_settings::data::hindu_show_estimated` | 987217221 | Mark estimated Hindu holidays (rå källa: `[%key:component::workday::config::step::options::sections::country_settings::data::hindu_show_estimated%]`) | referens |
| `component::workday::options::step::init::sections::country_settings::data::include_sundays` | 987217222 | Include Sundays as holidays (rå källa: `[%key:component::workday::config::step::options::sections::country_settings::data::include_sundays%]`) | referens |
| `component::workday::options::step::init::sections::country_settings::data::islamic_show_estimated` | 987217223 | Mark estimated Islamic holidays (rå källa: `[%key:component::workday::config::step::options::sections::country_settings::data::islamic_show_estimated%]`) | referens |
| `component::workday::options::step::init::sections::country_settings::data_description::hindu_show_estimated` | 987217224 | Add "estimated" to the name of Hindu holidays with an estimated date (rå källa: `[%key:component::workday::config::step::options::sections::country_settings::data_description::hindu_show_estimated%]`) | referens |
| `component::workday::options::step::init::sections::country_settings::data_description::include_sundays` | 987217225 | Add all Sundays to the holidays of the country (rå källa: `[%key:component::workday::config::step::options::sections::country_settings::data_description::include_sundays%]`) | referens |
| `component::workday::options::step::init::sections::country_settings::data_description::islamic_show_estimated` | 987217226 | Add "estimated" to the name of Islamic holidays with an estimated date (rå källa: `[%key:component::workday::config::step::options::sections::country_settings::data_description::islamic_show_estimated%]`) | referens |

## Skillnader i Lokalises engelska källtext

| Fullständig nyckel | Aktuell HA Core-källa | Lokalise engelska |
|---|---|---|
| `component::lyric::application_credentials::description` | To be able to log in to Honeywell Lyric the integration requires a client ID and secret. To acquire those, please follow the following steps.\n\n1. Go to the [Honeywell Lyric Developer Apps Dashboard]({developer_dashboard_url}).\n1. Sign up for a developer account if you don't have one yet. This is a separate account from your Honeywell account.\n1. Log in with your Honeywell Lyric developer account.\n1. Go to the **My Apps** section.\n1. Press the **CREATE NEW APP** button.\n1. Give the application a name of your choice.\n1. Set the **Callback URL** to `{redirect_url}`.\n1. Save your changes.\n1. Copy the **Consumer Key** and paste it here as the **Client ID**, then copy the **Consumer Secret** and paste it here as the **Client Secret**. | To be able to log in to Honeywell Lyric the integration requires a client ID and secret. To acquire those, please follow the following steps.\n\n1. Go to the [Honeywell Lyric Developer Apps Dashboard]({developer_dashboard_url}).\n1. Sign up for a developer account if you don't have one yet. This is a separate account from your Honeywell account.\n1. Log in with your Honeywell Lyric developer account.\n1. Go to the **My Apps** section.\n1. Press the **CREATE NEW APP** button.\n1. Give the application a name of your choice.\n1. Set the **Callback URL** to `{redirect_url}`.\n1. Save your changes.\n1. Copy the **Consumer Key** and paste it here as the **Client ID**, then copy the **Consumer Secret** and paste it here as the **Client Secret**. |
| `component::telegram_bot::services::edit_message::fields::title::description` | Optional title for your notification. Will be composed as '%title\n%message'. | Optional title for your notification. Will be composed as '%title\n%message'. |
| `component::telegram_bot::services::send_message::fields::title::description` | Optional title for your notification. Will be composed as '%title\n%message'. | Optional title for your notification. Will be composed as '%title\n%message'. |

Skillnaderna gäller escape-/radbrytning i Lyric och Telegram Bot. De bör jämföras i uppladdningsflödet; de ändrar inte räknandet av saknade strängar.

## Metod och avgränsningar

- Källnycklar genererades med Home Assistants officiella `script.hassfest.translation_data.generate_upload_data` mot ovanstående Core-revision.
- Lokalise-projektets samtliga 153 sidor hämtades via API med `include_translations=1`, utan skrivningar. Nycklar matchades på fullständigt `key_name.other`; arkiverade poster exkluderades från tomma mål.
- Strukturella, helt tomma käll-/målbehållare rapporteras i separat tomkällsrapport; de har inget översättningsbart innehåll.
- De 203 nycklarna som saknas helt kan inte skapas med nuvarande API-behörighet. Den tidigare kontrollen finns i `2026-11-21-core-missing-keys.md`; kör HA:s officiella `script.translations upload` med behörig miljö.

## Uppdatering 2026-11-25 – tidigare tomma mål

120 av de ursprungligen 641 tomma svenska målen har nu granskats mot aktuell HA Core-källa och sparats/återlästs i Lokalise. 521 återstår. 28 unika referensmål kontrollerades live; sex värden (inklusive ett gemensamt Azure-mål) synkroniserades och lästes tillbaka. TMX har uppdaterats. Se batchrapporten `../2026-11-19-granskning/granskning-empty-targets-001-120.md` och manifesten intill denna rapport.
