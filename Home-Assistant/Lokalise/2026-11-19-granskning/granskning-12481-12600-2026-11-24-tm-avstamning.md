# Home Assistant Core – historisk avstämning 12481–12600

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 76 direkta källtexter matchar HA Core-källan; 29 referensanvändningar med 21 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 15 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 12481 | 920778307 | `component::fronius::exceptions::modbus_write_failed::message` | Could not write the setting to the inverter: {error} | Det gick inte att spara inställningen i växelriktaren: {error} | Core-literal match |
| 12482 | 920778306 | `component::fronius::exceptions::modbus_model_unavailable::message` | The inverter no longer exposes the model this setting lives in | Växelriktaren tillhandahåller inte längre modellen där den här inställningen finns | Core-literal match |
| 12483 | 920778305 | `component::fronius::entity::number::power_limit::name` | Power limit | Effektgräns | Source-path follow-up open |
| 12484 | 920778304 | `component::fronius::entity::number::battery_minimum_reserve::name` | Battery minimum reserve | Minsta batterireserv | Core-literal match |
| 12485 | 920778303 | `component::fronius::entity::number::battery_discharge_power_limit::name` | Battery discharge power limit | Gräns för batteriets urladdningseffekt | Core-literal match |
| 12486 | 920778302 | `component::fronius::entity::number::battery_charge_power_limit::name` | Battery charge power limit | Gräns för batteriladdningseffekt | Core-literal match |
| 12487 | 920755923 | `component::esphome::config::error::provisioning_closed` | The ESPHome device closed its setup window and no longer accepts new connections. Power the device off and on again, then retry. | ESPHome-enheten stängde sitt installationsfönster och accepterar inte längre nya anslutningar. Stäng av enheten och slå på den igen, och försök sedan igen. | Core-literal match |
| 12488 | 920529952 | `component::collection_image::services::shuffle::name` | Shuffle | Blanda | Core-literal match |
| 12489 | 920529951 | `component::collection_image::services::shuffle::description` | Updates the image entity to a random image from the configured media. | Uppdaterar bildentiteten till en slumpmässig bild från det konfigurerade mediet. | Core-literal match |
| 12490 | 920449137 | `component::unifiprotect::issues::sense_setting_mirror_deprecated_no_replacement::title` | Read-only sensor setting entity deprecated | Skrivskyddad entitet för sensorinställning är föråldrad | Source-path follow-up open |
| 12491 | 920449136 | `component::unifiprotect::issues::sense_setting_mirror_deprecated_no_replacement::description` | The read-only entity `{entity_id}` is deprecated and will be removed in a future release. The sensor does not support this setting, so there is no replacement.<br><br>Update the following automations and scripts:<br>{items} | Den skrivskyddade entiteten `{entity_id}` är föråldrad och kommer att tas bort i en framtida version. Sensorn stöder inte den här inställningen, så det finns ingen ersättning.<br><br>Uppdatera följande automatiseringar och skript:<br>{items} | Source-path follow-up open |
| 12492 | 920449135 | `component::unifiprotect::issues::sense_setting_mirror_deprecated::title` | Read-only sensor setting entity deprecated | Skrivskyddad entitet för sensorinställning är föråldrad | Source-path follow-up open |
| 12493 | 920449134 | `component::unifiprotect::issues::sense_setting_mirror_deprecated::description` | The read-only entity `{entity_id}` is deprecated and will be removed in a future release; use `{replacement}` instead, which holds the same state and can also change it.<br><br>Update the following automations and scripts:<br>{items} | Den skrivskyddade entiteten `{entity_id}` är föråldrad och kommer att tas bort i en framtida version. Använd `{replacement}` i stället: den har samma tillstånd och kan även ändra det.<br><br>Uppdatera följande automatiseringar och skript:<br>{items} | Source-path follow-up open |
| 12494 | 920444176 | `component::fronius::entity::sensor::storage_energy_discharged_total::name` | Battery discharging energy total | Total batteriurladdningsenergi | Core-literal match |
| 12495 | 920444175 | `component::fronius::entity::sensor::storage_energy_charged_total::name` | Battery charging energy total | Total batteriladdningsenergi | Core-literal match |
| 12496 | 920444174 | `component::fronius::entity::sensor::modbus_mppt_voltage_dc::name` | DC voltage (Modbus) | Likspänning (Modbus) | Core-literal match |
| 12497 | 920444173 | `component::fronius::entity::sensor::modbus_mppt_power_dc::name` | DC power | Likströmseffekt | Core-literal match |
| 12498 | 920444172 | `component::fronius::entity::sensor::modbus_mppt_energy_dc::name` | MPPT {mppt_no} DC energy | MPPT {mppt_no} likströmsenergi | Source-path follow-up open |
| 12499 | 920444171 | `component::fronius::entity::sensor::modbus_mppt_current_dc::name` | DC current (Modbus) | Likström (Modbus) | Core-literal match |
| 12500 | 920444170 | `component::fronius::entity::sensor::energy_total_pv::name` | PV energy total | Total PV-energi | Core-literal match |
| 12501 | 920444169 | `component::fronius::config::step::user::data_description::modbus_port` | Port of the device's Modbus TCP interface. Only used when Modbus is enabled on the device's web interface. | Port för enhetens Modbus TCP-gränssnitt. Används endast när Modbus är aktiverat på enhetens webbgränssnitt. | Core-literal match |
| 12502 | 920444168 | `component::fronius::config::step::user::data::modbus_port` | Modbus port | Modbus-port | Core-literal match |
| 12503 | 920444167 | `component::fronius::config::step::reconfigure::data_description::modbus_port` | Port of the device's Modbus TCP interface. Only used when Modbus is enabled on the device's web interface. | Port för enhetens Modbus TCP-gränssnitt. Används endast när Modbus är aktiverat på enhetens webbgränssnitt. | Shared reference target checked |
| 12504 | 920444166 | `component::fronius::config::step::reconfigure::data::modbus_port` | Modbus port | Modbus-port | Shared reference target checked |
| 12505 | 920443990 | `component::wiim::exceptions::callback_host_unavailable::message` | Failed to determine a local address for WiiM device events | Misslyckades med att fastställa en lokal adress för WiiM-enhetshändelser | Core-literal match |
| 12506 | 920443922 | `component::tplink_omada::exceptions::unsupported_controller::message` | Omada controller version not supported. | Omada-styrenhetens version stöds inte. | Core-literal match |
| 12507 | 920443921 | `component::tplink_omada::exceptions::unexpected_error::message` | Unexpected error connecting to Omada controller. | Oväntat fel vid anslutning till Omada-styrenheten. | Core-literal match |
| 12508 | 920443920 | `component::tplink_omada::exceptions::switch_action_failed::message` | Failed to update the switch. | Misslyckades med att uppdatera switchen. | Core-literal match |
| 12509 | 920443919 | `component::tplink_omada::exceptions::reconnect_failed::message` | Failed to reconnect client with MAC {mac} | Det gick inte att återansluta klienten med MAC-adressen {mac} | Core-literal match |
| 12510 | 920443918 | `component::tplink_omada::exceptions::no_controllers::message` | No active TP-Link Omada controllers found | Inga aktiva TP-Link Omada-styrenheter hittades | Core-literal match |
| 12511 | 920443917 | `component::tplink_omada::exceptions::firmware_update_rejected::message` | Firmware update request rejected | Begäran om firmwareuppdatering avvisad | Core-literal match |
| 12512 | 920443916 | `component::tplink_omada::exceptions::firmware_update_failed::message` | Unable to send firmware update request. Check the controller is online. | Det gick inte att skicka begäran om firmwareuppdatering. Kontrollera att styrenheten är online. | Core-literal match |
| 12513 | 920443915 | `component::tplink_omada::exceptions::controller_unavailable::message` | The TP-Link Omada integration is not currently available | TP-Link Omada-integrationen är för närvarande inte tillgänglig | Core-literal match |
| 12514 | 920443914 | `component::tplink_omada::exceptions::controller_not_found::message` | Specified TP-Link Omada controller not found | Angiven TP-Link Omada-styrenhet hittades inte | Core-literal match |
| 12515 | 920443913 | `component::tplink_omada::exceptions::cannot_connect::message` | Omada controller could not be reached. | Omada-styrenheten kunde inte nås. | Core-literal match |
| 12516 | 920443912 | `component::tplink_omada::exceptions::auth_failed::message` | Omada controller refused login attempt. | Omada-styrenheten avvisade inloggningsförsöket. | Core-literal match |
| 12517 | 920443911 | `component::tplink_omada::exceptions::api_error::message` | Failed to communicate with the Omada controller. | Det gick inte att kommunicera med Omada-styrenheten. | Core-literal match |
| 12518 | 920412148 | `component::flexit::issues::deprecated_yaml_no_import::title` | The Flexit YAML configuration is being removed | Flexit-konfigurationen i YAML tas bort | Core-literal match |
| 12519 | 920412147 | `component::flexit::issues::deprecated_yaml_no_import::description` | Configuring Flexit using YAML is being removed.<br><br>Your existing YAML configuration could not be automatically imported because the Modbus connection details are configured separately, in a `modbus:` hub, which is not accessible from the `climate` platform configuration.<br><br>Remove the `flexit` configuration from your configuration.yaml file, then add the integration again from the Home Assistant UI, providing the Modbus connection details and unit ID of your Flexit unit. | Konfigurationen av Flexit med YAML tas bort.<br><br>Din befintliga YAML-konfiguration kunde inte importeras automatiskt eftersom Modbus-anslutningsuppgifterna konfigureras separat, i en `modbus:`-hubb, som inte är tillgänglig från `climate`-plattformens konfiguration.<br><br>Ta bort `flexit`-konfigurationen från din configuration.yaml-fil och lägg sedan till integrationen igen från Home Assistant-gränssnittet genom att ange Modbus-anslutningsuppgifterna och enhets-ID:t för din Flexit-enhet. | Core-literal match |
| 12520 | 920412146 | `component::flexit::config::step::user::menu_options::tcp` | Modbus TCP | Modbus TCP | Shared reference target checked |
| 12521 | 920412145 | `component::flexit::config::step::user::menu_options::serial` | Serial port (Modbus RTU) | Seriell port (Modbus RTU) | Shared reference target checked |
| 12522 | 920412144 | `component::flexit::config::step::tcp::data_description::unit` | The Modbus unit ID of your Flexit AC unit. | Modbus-enhets-ID:t för din Flexit AC-enhet. | Core-literal match |
| 12523 | 920412143 | `component::flexit::config::step::tcp::data_description::port` | The Modbus TCP port to connect to. | Modbus TCP-porten som anslutningen ska använda. | Shared reference target checked |
| 12524 | 920412142 | `component::flexit::config::step::tcp::data_description::host` | The hostname or IP address of your Flexit CI66 Modbus bridge. | Värdnamnet eller IP-adressen för din Flexit CI66 Modbus-brygga. | Core-literal match |
| 12525 | 920412141 | `component::flexit::config::step::tcp::data::unit` | Unit ID | Enhets-ID | Core-literal match |
| 12526 | 920412140 | `component::flexit::config::step::tcp::data::port` | Port | Port | Shared reference target checked |
| 12527 | 920412139 | `component::flexit::config::step::tcp::data::host` | Host | Värd | Shared reference target checked |
| 12528 | 920412138 | `component::flexit::config::step::serial::data_description::unit` | The Modbus unit ID of your Flexit AC unit. | Modbus-enhets-ID:t för din Flexit AC-enhet. | Core-literal match |
| 12529 | 920412137 | `component::flexit::config::step::serial::data_description::device` | Select a local serial port or a port shared over the network by a serial proxy. | Välj en lokal seriell port eller en port som delas över nätverket via en seriell proxy. | Shared reference target checked |
| 12530 | 920412136 | `component::flexit::config::step::serial::data_description::baudrate` | Match the baud rate configured on the device. | Ange den överföringshastighet som är konfigurerad på enheten. | Shared reference target checked |
| 12531 | 920412135 | `component::flexit::config::step::serial::data::unit` | Unit ID | Enhets-ID | Core-literal match |
| 12532 | 920412134 | `component::flexit::config::step::serial::data::device` | Serial port | Seriell port | Shared reference target checked |
| 12533 | 920412133 | `component::flexit::config::step::serial::data::baudrate` | Baud rate | Baudhastighet | Shared reference target checked |
| 12534 | 920412132 | `component::flexit::config::step::reconfigure::data_description::unit` | The Modbus unit ID of your Flexit AC unit. | Modbus-enhets-ID:t för din Flexit AC-enhet. | Shared reference target checked |
| 12535 | 920412131 | `component::flexit::config::step::reconfigure::data_description::port` | The Modbus TCP port to connect to. | Modbus TCP-porten som anslutningen ska använda. | Shared reference target checked |
| 12536 | 920412130 | `component::flexit::config::step::reconfigure::data_description::host` | The hostname or IP address of your Flexit CI66 Modbus bridge. | Värdnamnet eller IP-adressen för din Flexit CI66 Modbus-brygga. | Shared reference target checked |
| 12537 | 920412129 | `component::flexit::config::step::reconfigure::data_description::device` | Select a local serial port or a port shared over the network by a serial proxy. | Välj en lokal seriell port eller en port som delas över nätverket via en seriell proxy. | Shared reference target checked |
| 12538 | 920412128 | `component::flexit::config::step::reconfigure::data_description::baudrate` | Match the baud rate configured on the device. | Ange den överföringshastighet som är konfigurerad på enheten. | Shared reference target checked |
| 12539 | 920412127 | `component::flexit::config::step::reconfigure::data::unit` | Unit ID | Enhets-ID | Core-literal match |
| 12540 | 920412126 | `component::flexit::config::step::reconfigure::data::port` | Port | Port | Shared reference target checked |
| 12541 | 920412125 | `component::flexit::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 12542 | 920412124 | `component::flexit::config::step::reconfigure::data::device` | Serial port | Seriell port | Shared reference target checked |
| 12543 | 920412123 | `component::flexit::config::step::reconfigure::data::baudrate` | Baud rate | Baudhastighet | Shared reference target checked |
| 12544 | 920412122 | `component::flexit::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 12545 | 920412121 | `component::flexit::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 12546 | 920412120 | `component::flexit::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 12547 | 920412119 | `component::flexit::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 12548 | 920410872 | `component::sofar::exceptions::unrecognized_inverter_model::message` | Neither the serial number nor the register masks identify the Sofar inverter model. | Varken serienumret eller registermaskerna identifierar Sofar-växelriktarens modell. | Core-literal match |
| 12549 | 920410871 | `component::sofar::exceptions::no_component_answered::message` | No component answered. | Ingen komponent svarade. | Core-literal match |
| 12550 | 920410870 | `component::sofar::exceptions::modbus_error::message` | Error communicating with the inverter. | Fel vid kommunikation med växelriktaren. | Core-literal match |
| 12551 | 920410869 | `component::sofar::entity::sensor::solar_generation_total::name` | Solar generation total | Solenergiproduktion totalt | Core-literal match |
| 12552 | 920410868 | `component::sofar::entity::sensor::pv_power_total::name` | PV power total | PV-effekt totalt | Core-literal match |
| 12553 | 920410867 | `component::sofar::entity::sensor::pv_power_2::name` | PV power 2 | PV-effekt 2 | Source-path follow-up open |
| 12554 | 920410866 | `component::sofar::entity::sensor::pv_power_1::name` | PV power 1 | PV-effekt 1 | Source-path follow-up open |
| 12555 | 920410865 | `component::sofar::config::step::user::description` | A Sofar inverter can be set up in Home Assistant in two different ways.<br><br>You can reach it over the network, which covers a Modbus TCP bridge or a stick that speaks Modbus TCP, or over a serial port its RS485 terminals are wired to, which covers ports shared over the network by a serial proxy. | En Sofar-växelriktare kan konfigureras i Home Assistant på två olika sätt.<br><br>Du kan ansluta till den via nätverket, med en Modbus TCP-brygga eller en adapter som använder Modbus TCP, eller via en serieport som är ansluten till dess RS485-anslutningar. Det gäller även serieportar som delas via nätverket med en seriell proxy. | Core-literal match |
| 12556 | 920410864 | `component::sofar::config::step::user::data_description::unit_id` | The inverter's Modbus unit ID, also called its Modbus device address. | Växelriktarens Modbus-enhets-ID, även kallat dess Modbus-enhetsadress. | Source-path follow-up open |
| 12557 | 920410863 | `component::sofar::config::step::user::data_description::port` | The Modbus TCP port to connect on. | Modbus TCP-porten att ansluta till. | Source-path follow-up open |
| 12558 | 920410862 | `component::sofar::config::step::user::data_description::host` | The hostname or IP address of the inverter, or of the Modbus TCP bridge it's connected through. | Värdnamnet eller IP-adressen för växelriktaren, eller för Modbus TCP-bryggan den är ansluten via. | Source-path follow-up open |
| 12559 | 920410861 | `component::sofar::config::step::user::data::unit_id` | Modbus unit ID | Modbus-enhets-ID | Source-path follow-up open |
| 12560 | 920410860 | `component::sofar::config::step::user::data::port` | Port | Port | Source-path follow-up open |
| 12561 | 920410859 | `component::sofar::config::step::user::data::host` | Host | Värd | Source-path follow-up open |
| 12562 | 920410858 | `component::sofar::config::error::unrecognized_inverter` | The device answered, but neither its serial number nor its register masks identify a known Sofar model. | Enheten svarade, men varken serienumret eller registermaskerna identifierar en känd Sofar-modell. | Core-literal match |
| 12563 | 920410857 | `component::sofar::config::error::cannot_connect` | Failed to connect: {error} | Misslyckades med att ansluta: {error} | Core-literal match |
| 12564 | 920410856 | `component::sofar::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 12565 | 920409365 | `component::environment_canada::options::step::init::sections::time::name` | Time | Tid | Core-literal match |
| 12566 | 920409364 | `component::environment_canada::options::step::init::sections::time::data_description::radar_future_minutes` | Extend the radar loop past now using Environment Canada's short-term forecast (nowcast) layer, in minutes (up to 72, the limit of the available data). Only affects Rain and Snow; no effect on Precipitation type | Utöka radarloopen bortom nuet med hjälp av Environment Canadas korttidsprognoslager (nowcast), i minuter (upp till 72, vilket är gränsen för tillgängliga data). Påverkar endast regn och snö; har ingen inverkan på nederbördstypen | Core-literal match |
| 12567 | 920409363 | `component::environment_canada::options::step::init::sections::time::data_description::radar_duration` | How far back the radar animation goes, in minutes (0 for the full available history) | Hur långt tillbaka i tiden radaranimationen sträcker sig, i minuter (0 för hela den tillgängliga historiken) | Core-literal match |
| 12568 | 920409362 | `component::environment_canada::options::step::init::sections::time::data::radar_timestamp` | Show timestamp | Visa tidsstämpel | Core-literal match |
| 12569 | 920409361 | `component::environment_canada::options::step::init::sections::time::data::radar_future_minutes` | Future minutes | Framtida minuter | Core-literal match |
| 12570 | 920409360 | `component::environment_canada::options::step::init::sections::time::data::radar_duration` | Past minutes | Senaste minuterna | Core-literal match |
| 12571 | 920409359 | `component::environment_canada::options::step::init::sections::radar::name` | Radar | Radar | Core-literal match |
| 12572 | 920409358 | `component::environment_canada::options::step::init::sections::radar::data_description::radar_opacity` | Opacity of the radar layer overlay (0-100) | Opacitet för radaröverlagringen (0-100) | Core-literal match |
| 12573 | 920409357 | `component::environment_canada::options::step::init::sections::radar::data_description::radar_colors` | Number of colours in the rain/snow radar scale (has no effect on the precipitation type layer) | Antal färger på regn-/snöradarskalan (påverkar inte lagret för nederbördstyp) | Core-literal match |
| 12574 | 920409356 | `component::environment_canada::options::step::init::sections::radar::data::radar_opacity` | Radar opacity | Radaropacitet | Core-literal match |
| 12575 | 920409355 | `component::environment_canada::options::step::init::sections::radar::data::radar_legend` | Show legend | Visa förklaring | Core-literal match |
| 12576 | 920409354 | `component::environment_canada::options::step::init::sections::radar::data::radar_layer` | Radar type | Radartyp | Core-literal match |
| 12577 | 920409353 | `component::environment_canada::options::step::init::sections::radar::data::radar_colors` | Colour scale | Färgskala | Core-literal match |
| 12578 | 920409352 | `component::environment_canada::options::step::init::sections::map::name` | Map | Karta | Core-literal match |
| 12579 | 920409351 | `component::environment_canada::options::step::init::sections::map::data_description::radar_radius` | Radius of the radar map in kilometres | Radarkartans radie i kilometer | Core-literal match |
| 12580 | 920409350 | `component::environment_canada::options::step::init::sections::map::data::radar_radius` | Map radius | Kartradie | Core-literal match |
| 12581 | 920409349 | `component::environment_canada::options::step::init::sections::image::name` | Image | Bild | Core-literal match |
| 12582 | 920409348 | `component::environment_canada::options::step::init::sections::image::data_description::radar_interpolation` | Smooth the radar image instead of leaving it pixelated (uses more bandwidth) | Jämna ut radarbilden i stället för att låta den vara pixlig (kräver mer bandbredd) | Core-literal match |
| 12583 | 920409347 | `component::environment_canada::options::step::init::sections::image::data_description::radar_fps` | Frame rate of the radar animation | Bildfrekvens för radaranimationen | Core-literal match |
| 12584 | 920409346 | `component::environment_canada::options::step::init::sections::image::data::radar_interpolation` | Smooth radar image | Jämna ut radarbilden | Core-literal match |
| 12585 | 920409345 | `component::environment_canada::options::step::init::sections::image::data::radar_fps` | Loop frame rate | Bildfrekvens för animationen | Core-literal match |
| 12586 | 920409343 | `component::cloud::exceptions::no_pending_auto_login::message` | There is no registration waiting for an email confirmation. | Det finns ingen registrering som väntar på en e-postbekräftelse. | Core-literal match |
| 12587 | 920409342 | `component::cloud::exceptions::auto_login_failed_unexpected_error::message` | An unexpected error stopped us from signing you in. Please try signing in again. | Ett oväntat fel hindrade oss från att logga in dig. Försök att logga in igen. | Core-literal match |
| 12588 | 920409341 | `component::cloud::exceptions::auto_login_failed_timeout::message` | Your email was not confirmed in time, so we stopped waiting. Your account was created, so please confirm your email and sign in. | Din e-postadress bekräftades inte i tid, så vi slutade vänta. Ditt konto har skapats, så bekräfta din e-postadress och logga in. | Core-literal match |
| 12589 | 920409340 | `component::cloud::exceptions::auto_login_failed_cloud_error::message` | Could not reach Home Assistant Link to finish signing you in. Please try signing in again. | Det gick inte att ansluta till Home Assistant Link för att slutföra inloggningen. Försök att logga in igen. | Core-literal match |
| 12590 | 920409218 | `component::modern_forms::entity::number::breeze_intensity::name` | Breeze intensity | Brisintensitet | Core-literal match |
| 12591 | 920409217 | `component::number::entity_component::volatile_organic_compounds_parts::name` | Volatile organic compounds parts | Delar av flyktiga organiska föreningar (VOC) | Shared reference target checked |
| 12592 | 920409216 | `component::number::entity_component::monetary::name` | Monetary balance | Monetärt saldo | Shared reference target checked |
| 12593 | 920409215 | `component::number::entity_component::energy_distance::name` | Energy per distance | Energi per sträcka | Shared reference target checked |
| 12594 | 920409214 | `component::number::entity_component::duration::name` | Duration | Varaktighet | Shared reference target checked |
| 12595 | 920409213 | `component::number::entity_component::data_size::name` | Data size | Datastorlek | Shared reference target checked |
| 12596 | 920402707 | `component::wattwaechter::entity::sensor::ssid::name` | SSID | SSID | Core-literal match |
| 12597 | 920391766 | `component::proxmoxve::entity::button::pause::name` | Pause | Pausa | Core-literal match |
| 12598 | 920391736 | `component::mealie::services::update_mealplan::name` | Update a mealplan | Uppdatera en måltidsplan | Core-literal match |
| 12599 | 920391735 | `component::mealie::services::update_mealplan::fields::recipe_id::name` | Recipe ID | Recept-ID | Core-literal match |
| 12600 | 920391734 | `component::mealie::services::update_mealplan::fields::recipe_id::description` | The recipe ID or the slug of the recipe to set. | Recept-ID eller slug för receptet som ska anges. | Core-literal match |

## Sparade korrigeringar

| Lokalise-nyckel-ID | Nyckel | Tidigare svenska | Sparad svenska |
|---:|---|---|---|
| 920412133 | `component::flexit::config::step::serial::data::baudrate` | Baudfrekvens | Baudhastighet |
| 920412123 | `component::flexit::config::step::reconfigure::data::baudrate` | Baudfrekvens | Baudhastighet |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 920778305 | `component::fronius::entity::number::power_limit::name` | Power limit |
| 920449137 | `component::unifiprotect::issues::sense_setting_mirror_deprecated_no_replacement::title` | Read-only sensor setting entity deprecated |
| 920449136 | `component::unifiprotect::issues::sense_setting_mirror_deprecated_no_replacement::description` | The read-only entity `{entity_id}` is deprecated and will be removed in a future release. The sensor does not support this setting, so there is no replacement.

Update the following automations and scripts:
{items} |
| 920449135 | `component::unifiprotect::issues::sense_setting_mirror_deprecated::title` | Read-only sensor setting entity deprecated |
| 920449134 | `component::unifiprotect::issues::sense_setting_mirror_deprecated::description` | The read-only entity `{entity_id}` is deprecated and will be removed in a future release; use `{replacement}` instead, which holds the same state and can also change it.

Update the following automations and scripts:
{items} |
| 920444172 | `component::fronius::entity::sensor::modbus_mppt_energy_dc::name` | MPPT {mppt_no} DC energy |
| 920412120 | `component::flexit::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 920410867 | `component::sofar::entity::sensor::pv_power_2::name` | PV power 2 |
| 920410866 | `component::sofar::entity::sensor::pv_power_1::name` | PV power 1 |
| 920410864 | `component::sofar::config::step::user::data_description::unit_id` | The inverter's Modbus unit ID, also called its Modbus device address. |
| 920410863 | `component::sofar::config::step::user::data_description::port` | The Modbus TCP port to connect on. |
| 920410862 | `component::sofar::config::step::user::data_description::host` | The hostname or IP address of the inverter, or of the Modbus TCP bridge it's connected through. |
| 920410861 | `component::sofar::config::step::user::data::unit_id` | Modbus unit ID |
| 920410860 | `component::sofar::config::step::user::data::port` | Port |
| 920410859 | `component::sofar::config::step::user::data::host` | Host |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
