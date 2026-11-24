# Home Assistant Core – historisk avstämning 15601–15720

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 63 direkta källtexter matchar HA Core-källan; 54 referensanvändningar med 47 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 3 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Tre SQL-referenskonsumenter uppdaterades till exakt samma svenska mål som sina gemensamma referenser, sparades i Lokalise och verifierades med API-readback. Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 15601 | 886120590 | `component::victron_gx::entity::sensor::battery_high_internal_temperature::name` | High internal temperature | Hög inre temperatur | Core-literal match |
| 15602 | 886120589 | `component::victron_gx::entity::sensor::battery_high_cell_voltage::state::warning` | Warning | Varning | Shared reference target checked |
| 15603 | 886120588 | `component::victron_gx::entity::sensor::battery_high_cell_voltage::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 15604 | 886120587 | `component::victron_gx::entity::sensor::battery_high_cell_voltage::state::alarm` | Alarm | Larm | Shared reference target checked |
| 15605 | 886120586 | `component::victron_gx::entity::sensor::battery_high_cell_voltage::name` | High cell voltage | Hög cellspänning | Core-literal match |
| 15606 | 886120585 | `component::victron_gx::entity::sensor::battery_fuse_blown::state::warning` | Warning | Varning | Shared reference target checked |
| 15607 | 886120584 | `component::victron_gx::entity::sensor::battery_fuse_blown::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 15608 | 886120583 | `component::victron_gx::entity::sensor::battery_fuse_blown::state::alarm` | Alarm | Larm | Shared reference target checked |
| 15609 | 886120582 | `component::victron_gx::entity::sensor::battery_fuse_blown::name` | Fuse blown | Säkring har löst ut | Core-literal match |
| 15610 | 886120581 | `component::victron_gx::entity::sensor::battery_bms_cable::state::warning` | Warning | Varning | Shared reference target checked |
| 15611 | 886120580 | `component::victron_gx::entity::sensor::battery_bms_cable::state::no_alarm` | No alarm | Inget larm | Shared reference target checked |
| 15612 | 886120579 | `component::victron_gx::entity::sensor::battery_bms_cable::state::alarm` | Alarm | Larm | Shared reference target checked |
| 15613 | 886120578 | `component::victron_gx::entity::sensor::battery_bms_cable::name` | BMS cable | BMS-kabel | Core-literal match |
| 15614 | 886120577 | `component::victron_gx::entity::device_tracker::ev_gps_location::name` | Location | Plats | Shared reference target checked |
| 15615 | 886120576 | `component::victron_gx::entity::binary_sensor::ev_at_site::name` | At site | På plats | Core-literal match |
| 15616 | 886120575 | `component::victron_gx::entity::binary_sensor::battery_allow_to_discharge::name` | Allow to discharge | Tillåt urladdning | Core-literal match |
| 15617 | 886120574 | `component::victron_gx::entity::binary_sensor::battery_allow_to_charge::name` | Allow to charge | Tillåt laddning | Core-literal match |
| 15618 | 886120573 | `component::victron_gx::common::total_energy` | Total energy | Total energi | Core-literal match |
| 15619 | 886120572 | `component::victron_gx::common::low_temperature` | Low temperature | Låg temperatur | Core-literal match |
| 15620 | 886120571 | `component::victron_gx::common::dc_voltage` | DC voltage | DC-spänning | Core-literal match |
| 15621 | 886120570 | `component::victron_gx::common::dc_power` | DC power | DC-effekt | Core-literal match |
| 15622 | 886120569 | `component::victron_gx::common::dc_current` | DC current | DC-ström | Core-literal match |
| 15623 | 886106182 | `component::v2c::entity::select::charge_mode::state::threephasic` | Three-phase | Trefas | Core-literal match |
| 15624 | 886106181 | `component::v2c::entity::select::charge_mode::state::monophasic` | Monophasic | Enfas | Core-literal match |
| 15625 | 886106180 | `component::v2c::entity::select::charge_mode::state::mixed` | Mixed | Blandat | Core-literal match |
| 15626 | 886106179 | `component::v2c::entity::select::charge_mode::name` | Charge mode | Laddningsläge | Core-literal match |
| 15627 | 885994106 | `component::mikrotik::exceptions::mikrotik_api_error::message` | Mikrotik API error: {error} | Mikrotik API-fel: {error} | Core-literal match |
| 15628 | 885994105 | `component::mikrotik::exceptions::invalid_auth::message` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 15629 | 885994104 | `component::mikrotik::exceptions::cannot_retrieve_data::message` | Error retrieving data: {error} | Fel vid hämtning av data: {error} | Core-literal match |
| 15630 | 885994103 | `component::mikrotik::exceptions::cannot_login::message` | Cannot login: {error} | Det gick inte att logga in: {error} | Core-literal match |
| 15631 | 885994102 | `component::mikrotik::exceptions::cannot_connect::message` | Error connecting: {error} | Fel vid anslutning: {error} | Core-literal match |
| 15632 | 885982737 | `component::switchbot::exceptions::set_fan_state_failed::message` | Failed to send the command to the fan. | Det gick inte att skicka kommandot till fläkten. | Core-literal match |
| 15633 | 885982736 | `component::switchbot::entity::fan::standing_fan::state_attributes::preset_mode::state::sleep` | Sleep | Sovläge | Shared reference target checked |
| 15634 | 885982735 | `component::switchbot::entity::fan::standing_fan::state_attributes::preset_mode::state::normal` | Normal | Normal | Shared reference target checked |
| 15635 | 885982734 | `component::switchbot::entity::fan::standing_fan::state_attributes::preset_mode::state::natural` | Natural | Naturlig | Shared reference target checked |
| 15636 | 885982733 | `component::switchbot::entity::fan::standing_fan::state_attributes::preset_mode::state::custom_natural` | Custom natural | Anpassad naturlig | Core-literal match |
| 15637 | 885982732 | `component::switchbot::entity::fan::standing_fan::state_attributes::preset_mode::state::baby` | Baby | Bebis | Shared reference target checked |
| 15638 | 885973549 | `component::imou::entity::switch::white_light::name` | White light | Vitt ljus | Core-literal match |
| 15639 | 885973548 | `component::imou::entity::switch::switch::name` | Plug switch | Kontaktbrytare | Core-literal match |
| 15640 | 885973547 | `component::imou::entity::switch::motion_detect::name` | Motion detection | Rörelsedetektering | Core-literal match |
| 15641 | 885973546 | `component::imou::entity::switch::light::name` | Indicator light | Indikatorlampa | Core-literal match |
| 15642 | 885973545 | `component::imou::entity::switch::header_detect::name` | Human detection | Mänsklig detektering | Core-literal match |
| 15643 | 885973544 | `component::imou::entity::switch::close_camera::name` | Privacy mode | Sekretessläge | Core-literal match |
| 15644 | 885973543 | `component::imou::entity::switch::audio_encode_control::name` | Audio recording | Ljudinspelning | Core-literal match |
| 15645 | 885973542 | `component::imou::entity::switch::ab_alarm_sound::name` | Abnormal sound alarm | Onormalt ljudlarm | Core-literal match |
| 15646 | 885952829 | `component::netatmo::issues::deprecated_webhook_service::title` | Netatmo webhook actions are deprecated | Netatmo webhook-åtgärder är föråldrade | Core-literal match |
| 15647 | 885952828 | `component::netatmo::issues::deprecated_webhook_service::description` | The `register_webhook` and `unregister_webhook` actions are deprecated and will be removed in a future release. Netatmo manages the webhook automatically, so these actions are no longer needed. Please remove them from your automations and scripts. | Åtgärderna `register_webhook` och `unregister_webhook` är föråldrade och kommer att tas bort i en framtida version. Netatmo hanterar webhooken automatiskt, så dessa åtgärder behövs inte längre. Ta bort dem från dina automatiseringar och skript. | Core-literal match |
| 15648 | 885952827 | `component::netatmo::exceptions::entry_not_loaded::message` | The Netatmo integration is not loaded. Please set it up before calling this action. | Netatmo-integrationen har inte laddats. Konfigurera den innan du utför den här åtgärden. | Core-literal match |
| 15649 | 885777620 | `component::ecobee::exceptions::mfa_reauthentication_needed::message` | ecobee account requires MFA; reauthentication needed | ecobee-kontot kräver multifaktorautentisering (MFA). Omautentisering krävs. | Core-literal match |
| 15650 | 885777619 | `component::ecobee::exceptions::failed_to_refresh_tokens::message` | Failed to refresh ecobee tokens | Det gick inte att uppdatera ecobee-tokens | Core-literal match |
| 15651 | 885777618 | `component::ecobee::exceptions::credentials_rejected::message` | ecobee rejected the stored credentials | ecobee avvisade de sparade inloggningsuppgifterna | Core-literal match |
| 15652 | 885552694 | `component::modbus::title` | Manual Modbus | Manuell Modbus | Source-path follow-up open |
| 15653 | 885544600 | `component::weatherflow_cloud::entity::sensor::wind_speed::name` | Wind speed | Vindhastighet | Source-path follow-up open |
| 15654 | 885544599 | `component::weatherflow_cloud::entity::sensor::air_temperature::name` | Temperature | Temperatur | Source-path follow-up open |
| 15655 | 885498923 | `component::sensor::entity_component::radon::name` | Radon | Radon | Core-literal match |
| 15656 | 885498922 | `component::sensor::device_automation::trigger_type::radon` | {entity_name} radon concentration changes | {entity_name} förändringar i radonkoncentrationen | Core-literal match |
| 15657 | 885498921 | `component::sensor::device_automation::condition_type::is_radon` | Current {entity_name} radon concentration level | Aktuell radonkoncentration i {entity_name} | Core-literal match |
| 15658 | 885498920 | `component::number::entity_component::radon::name` | Radon | Radon | Shared reference target checked |
| 15659 | 885458352 | `component::smtp::config::error::timeout_connect` | Timeout while establishing a connection | Tidsgränsen överskreds när anslutningen upprättades. | Shared reference target checked |
| 15660 | 885344995 | `component::blebox::config::step::reconfigure::data_description::username` | The username for your BleBox device. | Användarnamnet för din BleBox-enhet. | Shared reference target checked |
| 15661 | 885344994 | `component::blebox::config::step::reconfigure::data_description::port` | The port of your BleBox device. | Porten på din BleBox-enhet. | Shared reference target checked |
| 15662 | 885344993 | `component::blebox::config::step::reconfigure::data_description::password` | The password for your BleBox device. | Lösenordet för din BleBox-enhet. | Shared reference target checked |
| 15663 | 885344992 | `component::blebox::config::step::reconfigure::data_description::host` | The IP address of your BleBox device. | IP-adressen till din BleBox-enhet. | Shared reference target checked |
| 15664 | 884491811 | `component::sql::options::step::init::sections::additional_options::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 15665 | 884491810 | `component::sql::options::step::init::sections::additional_options::description` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 15666 | 884491809 | `component::sql::options::step::init::sections::additional_options::data_description::value_template` | Template to extract a value from the payload (optional) | Mall för att extrahera ett värde från nyttolasten (valfritt) | Shared reference target checked |
| 15667 | 884491808 | `component::sql::options::step::init::sections::additional_options::data_description::unit_of_measurement` | The unit of measurement for the sensor (optional) | Måttenhet för sensorn (valfritt) | Shared reference target checked |
| 15668 | 884491807 | `component::sql::options::step::init::sections::additional_options::data_description::state_class` | The state class of the sensor | Sensorns tillståndsklass | Shared reference target checked |
| 15669 | 884491806 | `component::sql::options::step::init::sections::additional_options::data_description::device_class` | The type/class of the sensor to set the icon in the frontend | Typ/klass på den sensor vars ikon ska ställas in i gränssnittet | Shared reference target checked |
| 15670 | 884491805 | `component::sql::options::step::init::sections::additional_options::data::value_template` | Value template | Värdemall | Shared reference target checked |
| 15671 | 884491804 | `component::sql::options::step::init::sections::additional_options::data::unit_of_measurement` | Unit of measurement | Måttenhet | Shared reference target checked |
| 15672 | 884491803 | `component::sql::options::step::init::sections::additional_options::data::state_class` | State class | Tillståndsklass | Shared reference target checked |
| 15673 | 884491802 | `component::sql::options::step::init::sections::additional_options::data::device_class` | Device class | Enhetsklass | Shared reference target checked |
| 15674 | 884491801 | `component::sql::config::step::options::sections::additional_options::name` | Additional options | Ytterligare alternativ | Core-literal match |
| 15675 | 884491800 | `component::sql::config::step::options::sections::additional_options::description` | Provide additional configuration to the sensor | Specificera ytterligare konfiguration för sensorn | Core-literal match |
| 15676 | 884491799 | `component::sql::config::step::options::sections::additional_options::data_description::value_template` | Template to extract a value from the payload (optional) | Mall för att extrahera ett värde från nyttolasten (valfritt) | Core-literal match |
| 15677 | 884491798 | `component::sql::config::step::options::sections::additional_options::data_description::unit_of_measurement` | The unit of measurement for the sensor (optional) | Måttenhet för sensorn (valfritt) | Core-literal match |
| 15678 | 884491797 | `component::sql::config::step::options::sections::additional_options::data_description::state_class` | The state class of the sensor | Sensorns tillståndsklass | Core-literal match |
| 15679 | 884491796 | `component::sql::config::step::options::sections::additional_options::data_description::device_class` | The type/class of the sensor to set the icon in the frontend | Typ/klass på den sensor vars ikon ska ställas in i gränssnittet | Core-literal match |
| 15680 | 884491795 | `component::sql::config::step::options::sections::additional_options::data::value_template` | Value template | Värdemall | Core-literal match |
| 15681 | 884491794 | `component::sql::config::step::options::sections::additional_options::data::unit_of_measurement` | Unit of measurement | Måttenhet | Core-literal match |
| 15682 | 884491793 | `component::sql::config::step::options::sections::additional_options::data::state_class` | State class | Tillståndsklass | Core-literal match |
| 15683 | 884491792 | `component::sql::config::step::options::sections::additional_options::data::device_class` | Device class | Enhetsklass | Core-literal match |
| 15684 | 884491747 | `component::scrape::options::step::init::sections::additional::name` | Additional settings | Ytterligare inställningar | Shared reference target checked |
| 15685 | 884491746 | `component::scrape::options::step::init::sections::additional::description` | Provide additional settings for the resource. | Ange ytterligare inställningar för resursen. | Shared reference target checked |
| 15686 | 884491745 | `component::scrape::options::step::init::sections::additional::data_description::verify_ssl` | Enables/disables verification of SSL/TLS certificate, for example if it is self-signed. | Aktiverar/inaktiverar verifiering av SSL/TLS-certifikat, t.ex. om det är självsignerat. | Shared reference target checked |
| 15687 | 884491744 | `component::scrape::options::step::init::sections::additional::data_description::timeout` | Timeout for connection to website. | Timeout för anslutning till webbplats. | Shared reference target checked |
| 15688 | 884491743 | `component::scrape::options::step::init::sections::additional::data_description::headers` | Headers to use for the web request. | Headers att använda för webbförfrågan. | Shared reference target checked |
| 15689 | 884491742 | `component::scrape::options::step::init::sections::additional::data_description::encoding` | Character encoding to use. Defaults to UTF-8. | Teckenkodning att använda. Standard är UTF-8 | Shared reference target checked |
| 15690 | 884491741 | `component::scrape::options::step::init::sections::additional::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 15691 | 884491740 | `component::scrape::options::step::init::sections::additional::data::timeout` | Timeout | Tidsgräns | Shared reference target checked |
| 15692 | 884491739 | `component::scrape::options::step::init::sections::additional::data::headers` | Headers | Headers | Shared reference target checked |
| 15693 | 884491738 | `component::scrape::options::step::init::sections::additional::data::encoding` | Character encoding | Teckenkodning | Shared reference target checked |
| 15694 | 884491737 | `component::scrape::config_subentries::entity::step::user::sections::additional::name` | Additional settings | Ytterligare inställningar | Core-literal match |
| 15695 | 884491736 | `component::scrape::config_subentries::entity::step::user::sections::additional::description` | Provide additional settings for the sensor. | Ange ytterligare inställningar för sensorn. | Core-literal match |
| 15696 | 884491735 | `component::scrape::config_subentries::entity::step::user::sections::additional::data_description::value_template` | Defines a template to get the state of the sensor. | Definierar en mall för att hämta sensorns tillstånd. | Core-literal match |
| 15697 | 884491734 | `component::scrape::config_subentries::entity::step::user::sections::additional::data_description::unit_of_measurement` | Choose unit of measurement or create your own. | Välj måttenhet eller skapa din egen. | Core-literal match |
| 15698 | 884491733 | `component::scrape::config_subentries::entity::step::user::sections::additional::data_description::state_class` | The state_class of the sensor. | Sensorns state_class. | Core-literal match |
| 15699 | 884491732 | `component::scrape::config_subentries::entity::step::user::sections::additional::data_description::device_class` | The type/class of the sensor to set the icon in the frontend. | Typ/klass på den sensor vars ikon ska ställas in i gränssnittet | Core-literal match |
| 15700 | 884491731 | `component::scrape::config_subentries::entity::step::user::sections::additional::data_description::availability` | Defines a template to get the availability of the sensor. | Definierar en mall för att få information om sensorns tillgänglighet. | Core-literal match |
| 15701 | 884491730 | `component::scrape::config_subentries::entity::step::user::sections::additional::data_description::attribute` | Get value of an attribute on the selected tag. | Hämta värdet för ett attribut med den valda taggen. | Core-literal match |
| 15702 | 884491729 | `component::scrape::config_subentries::entity::step::user::sections::additional::data::value_template` | Value template | Värdemall | Core-literal match |
| 15703 | 884491728 | `component::scrape::config_subentries::entity::step::user::sections::additional::data::unit_of_measurement` | Unit of measurement | Måttenhet | Core-literal match |
| 15704 | 884491727 | `component::scrape::config_subentries::entity::step::user::sections::additional::data::state_class` | State class | Tillståndsklass | Core-literal match |
| 15705 | 884491726 | `component::scrape::config_subentries::entity::step::user::sections::additional::data::device_class` | Device class | Enhetsklass | Core-literal match |
| 15706 | 884491725 | `component::scrape::config_subentries::entity::step::user::sections::additional::data::availability` | Availability template | Tillgänglighetsmall | Core-literal match |
| 15707 | 884491724 | `component::scrape::config_subentries::entity::step::user::sections::additional::data::attribute` | Attribute | Attribut | Core-literal match |
| 15708 | 884491723 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::name` | Additional settings | Ytterligare inställningar | Shared reference target checked |
| 15709 | 884491722 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::description` | Provide additional settings for the sensor. | Ange ytterligare inställningar för sensorn. | Shared reference target checked |
| 15710 | 884491721 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::data_description::value_template` | Defines a template to get the state of the sensor. | Definierar en mall för att hämta sensorns tillstånd. | Shared reference target checked |
| 15711 | 884491720 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::data_description::unit_of_measurement` | Choose unit of measurement or create your own. | Välj måttenhet eller skapa din egen. | Shared reference target checked |
| 15712 | 884491719 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::data_description::state_class` | The state_class of the sensor. | Sensorns state_class. | Shared reference target checked |
| 15713 | 884491718 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::data_description::device_class` | The type/class of the sensor to set the icon in the frontend. | Typ/klass på den sensor vars ikon ska ställas in i gränssnittet | Shared reference target checked |
| 15714 | 884491717 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::data_description::availability` | Defines a template to get the availability of the sensor. | Definierar en mall för att få information om sensorns tillgänglighet. | Shared reference target checked |
| 15715 | 884491716 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::data_description::attribute` | Get value of an attribute on the selected tag. | Hämta värdet för ett attribut med den valda taggen. | Shared reference target checked |
| 15716 | 884491715 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::data::value_template` | Value template | Värdemall | Shared reference target checked |
| 15717 | 884491714 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::data::unit_of_measurement` | Unit of measurement | Måttenhet | Shared reference target checked |
| 15718 | 884491713 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::data::state_class` | State class | Tillståndsklass | Shared reference target checked |
| 15719 | 884491712 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::data::device_class` | Device class | Enhetsklass | Shared reference target checked |
| 15720 | 884491711 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::data::availability` | Availability template | Tillgänglighetsmall | Shared reference target checked |

## Sparade referensrättningar

| Lokalise-nyckel-ID | Nyckel | Sparad svenska |
|---:|---|---|
| 884491808 | `component::sql::options::step::init::sections::additional_options::data_description::unit_of_measurement` | Måttenhet för sensorn (valfritt) |
| 884491806 | `component::sql::options::step::init::sections::additional_options::data_description::device_class` | Typ/klass på den sensor vars ikon ska ställas in i gränssnittet |
| 884491804 | `component::sql::options::step::init::sections::additional_options::data::unit_of_measurement` | Måttenhet |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 885552694 | `component::modbus::title` | Manual Modbus |
| 885544600 | `component::weatherflow_cloud::entity::sensor::wind_speed::name` | Wind speed |
| 885544599 | `component::weatherflow_cloud::entity::sensor::air_temperature::name` | Temperature |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
