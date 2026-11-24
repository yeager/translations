# Home Assistant Core – historisk avstämning 18601–18720

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 80 direkta källtexter matchar HA Core-källan; 34 referensanvändningar med 23 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 6 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 18601 | 850740760 | `component::centriconnect::entity::sensor::lte_signal_strength::name` | LTE signal strength | LTE-signalstyrka | Core-literal match |
| 18602 | 850740759 | `component::centriconnect::entity::sensor::lte_signal_level::name` | LTE signal level | LTE-signalnivå | Core-literal match |
| 18603 | 850740758 | `component::centriconnect::entity::sensor::device_temperature::name` | Device temperature | Enhetstemperatur | Core-literal match |
| 18604 | 850740757 | `component::centriconnect::entity::sensor::battery_voltage::name` | Battery voltage | Batterispänning | Core-literal match |
| 18605 | 850740756 | `component::centriconnect::entity::sensor::altitude::name` | Altitude | Höjd över havet | Core-literal match |
| 18606 | 850740755 | `component::centriconnect::entity::sensor::alert_status::state::no_alert` | No alert | Ingen varning | Core-literal match |
| 18607 | 850740754 | `component::centriconnect::entity::sensor::alert_status::state::low_level` | Low level | Låg nivå | Core-literal match |
| 18608 | 850740753 | `component::centriconnect::entity::sensor::alert_status::state::critical_level` | Critical level | Kritisk nivå | Core-literal match |
| 18609 | 850740752 | `component::centriconnect::entity::sensor::alert_status::name` | Alert status | Varningsstatus | Core-literal match |
| 18610 | 850740751 | `component::centriconnect::config::step::user::description` | Enter your CentriConnect/MyPropane device credentials. | Ange dina inloggningsuppgifter för CentriConnect/MyPropane-enheten. | Core-literal match |
| 18611 | 850740750 | `component::centriconnect::config::step::user::data_description::username` | Your CentriConnect/MyPropane user ID | Ditt användar-ID för CentriConnect/MyPropane | Core-literal match |
| 18612 | 850740749 | `component::centriconnect::config::step::user::data_description::password` | Your CentriConnect/MyPropane device authentication code | Din autentiseringskod för CentriConnect/MyPropane-enheten | Core-literal match |
| 18613 | 850740748 | `component::centriconnect::config::step::user::data_description::device_id` | Your CentriConnect/MyPropane device ID | Ditt enhets-ID för CentriConnect/MyPropane | Core-literal match |
| 18614 | 850740747 | `component::centriconnect::config::step::user::data::username` | User ID | Användar-ID | Core-literal match |
| 18615 | 850740746 | `component::centriconnect::config::step::user::data::password` | Device Authentication Code | Enhetsautentiseringskod | Core-literal match |
| 18616 | 850740745 | `component::centriconnect::config::step::user::data::device_id` | Device ID | Enhets-ID | Core-literal match |
| 18617 | 850740744 | `component::centriconnect::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 18618 | 850740743 | `component::centriconnect::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 18619 | 850740742 | `component::centriconnect::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18620 | 850740741 | `component::centriconnect::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 18621 | 850726891 | `component::mqtt::services::publish::fields::message_expiry_interval::name` | Message Expiry Interval | Meddelandets utgångsintervall | Core-literal match |
| 18622 | 850726890 | `component::mqtt::services::publish::fields::message_expiry_interval::description` | Expires a publish message after the interval in case the device subscriber was temporarily offline, or the message was set as a retained message. Only supported with MQTT protocol version 5.0. | Gör att ett publicerat meddelande upphör att gälla efter det angivna intervallet om prenumeranten tillfälligt var offline eller om meddelandet markerades som ett bevarat meddelande. Stöds endast med MQTT-protokollversion 5.0. | Core-literal match |
| 18623 | 850726889 | `component::mqtt::exceptions::mqtt_message_expiry_interval_not_supported::message` | Publishing to topic {topic} with a Message Expiry Interval is not supported for protocol version {protocol}. | Publicering till topic {topic} med ett intervall för meddelandets giltighetstid stöds inte för protokollversionen {protocol}. | Core-literal match |
| 18624 | 850661879 | `component::tuya::entity::switch::motion_detection_zone::name` | Use motion detection zone | Använd rörelsedetekteringszon | Core-literal match |
| 18625 | 850661878 | `component::tuya::entity::switch::auto_siren::name` | Auto-trigger siren | Auto-trigga siren | Core-literal match |
| 18626 | 850661877 | `component::tuya::entity::number::video_sharpness::name` | Video sharpness | Videoskärpa | Core-literal match |
| 18627 | 850661876 | `component::tuya::entity::number::video_contrast::name` | Video contrast | Videokontrast | Core-literal match |
| 18628 | 850661875 | `component::tuya::entity::number::video_brightness::name` | Video brightness | Videoljusstyrka | Core-literal match |
| 18629 | 850658515 | `component::tuya::entity::sensor::last_watering_time::name` | Last watering time | Senaste bevattningstillfälle | Core-literal match |
| 18630 | 850658514 | `component::tuya::entity::sensor::irrigation_status::state::manual` | Manual | Manuell | Shared reference target checked |
| 18631 | 850658513 | `component::tuya::entity::sensor::irrigation_status::state::idle` | Idle | Inaktiv | Shared reference target checked |
| 18632 | 850658512 | `component::tuya::entity::sensor::irrigation_status::state::auto` | Auto | Auto | Shared reference target checked |
| 18633 | 850658511 | `component::tuya::entity::sensor::irrigation_status::name` | Status | Status | Core-literal match |
| 18634 | 850648645 | `component::nintendo_parental_controls::entity::sensor::player_playing_time::name` | {nickname} used screen time | {nickname} använd skärmtid | Core-literal match |
| 18635 | 850471479 | `component::data_grand_lyon::config::step::reconfigure::data_description::username` | Your username on data.grandlyon.com. | Ditt användarnamn på data.grandlyon.com. | Shared reference target checked |
| 18636 | 850471478 | `component::data_grand_lyon::config::step::reconfigure::data_description::password` | Your password on data.grandlyon.com. | Ditt lösenord på data.grandlyon.com. | Shared reference target checked |
| 18637 | 850471477 | `component::data_grand_lyon::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference target checked |
| 18638 | 850471476 | `component::data_grand_lyon::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 18639 | 850471475 | `component::data_grand_lyon::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 18640 | 850128499 | `component::prusalink::entity::button::continue_job::name` | Continue job | Fortsätt jobb | Core-literal match |
| 18641 | 850040302 | `component::easyenergy::exceptions::connection_error::message` | Error communicating with the easyEnergy API. | Fel vid kommunikation med easyEnergy API:t. | Core-literal match |
| 18642 | 850040301 | `component::uptimerobot::entity::sensor::monitor_status::state::started` | Started | Startad | Core-literal match |
| 18643 | 850031681 | `component::easyenergy::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18644 | 850031510 | `component::data_grand_lyon::exceptions::update_failed_all_stops::message` | Error fetching Data Grand Lyon data: all requests failed. | Fel vid hämtning av data från Data Grand Lyon: alla förfrågningar misslyckades. | Source-path follow-up open |
| 18645 | 850031509 | `component::data_grand_lyon::exceptions::auth_failed::message` | Authentication failed for Data Grand Lyon. | Autentisering misslyckades för Data Grand Lyon. | Core-literal match |
| 18646 | 849997248 | `component::novy_cooker_hood::config::step::reconfigure::description` | After you submit, Home Assistant will toggle the hood light on and off to verify the code works. | Efter att du bekräftat så kommer home assistant att tända och släcka fläktens lampa för att verifiera att koden fungerar. | Shared reference target checked |
| 18647 | 849997247 | `component::novy_cooker_hood::config::step::reconfigure::data_description::transmitter` | The radio frequency transmitter to use for sending commands. | Den radiofrekvenssändare som ska användas för att skicka kommandon. | Shared reference target checked |
| 18648 | 849997246 | `component::novy_cooker_hood::config::step::reconfigure::data_description::code` | The code your hood is paired with (1-10). Code 1 is the factory default. | Koden som din fläkt är parad med (1-10). Kod 1 är fabriksinställning. | Shared reference target checked |
| 18649 | 849997245 | `component::novy_cooker_hood::config::step::reconfigure::data::transmitter` | Radio frequency transmitter | Sändare för radiofrekvens | Shared reference target checked |
| 18650 | 849997244 | `component::novy_cooker_hood::config::step::reconfigure::data::code` | Code | Kod | Shared reference target checked |
| 18651 | 849997243 | `component::novy_cooker_hood::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 18652 | 849771952 | `component::duco::system_health::info::write_requests_remaining` | Remaining write requests today | Återstående skrivförfrågningar idag | Core-literal match |
| 18653 | 849768458 | `component::nobo_hub::config::abort::cannot_discover` | Could not detect a Nobø Ecohub at the discovered IP address. | Det gick inte att upptäcka någon Nobø Ecohub på den upptäckta IP-adressen. | Core-literal match |
| 18654 | 849768457 | `component::nobo_hub::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 18655 | 849599821 | `component::hr_energy_qube::exceptions::set_temperature_failed::message` | Failed to set the target temperature. | Misslyckades med att ställa in måltemperaturen. | Core-literal match |
| 18656 | 849599820 | `component::hr_energy_qube::entity::water_heater::water_heater::name` | Domestic hot water | Varmvatten för hushållsbruk | Core-literal match |
| 18657 | 849542570 | `component::data_grand_lyon::config::step::reauth_confirm::data_description::username` | Your username on data.grandlyon.com. | Ditt användarnamn på data.grandlyon.com. | Shared reference target checked |
| 18658 | 849542569 | `component::data_grand_lyon::config::step::reauth_confirm::data_description::password` | Your password on data.grandlyon.com. | Ditt lösenord på data.grandlyon.com. | Shared reference target checked |
| 18659 | 849542568 | `component::data_grand_lyon::config::step::reauth_confirm::data::username` | Username | Användarnamn | Shared reference target checked |
| 18660 | 849542567 | `component::data_grand_lyon::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 18661 | 849542566 | `component::data_grand_lyon::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 18662 | 849370828 | `component::switchbot_cloud::exceptions::device_offline::message` | SwitchBot Cloud device is offline. | SwitchBot Cloud-enheten är offline. | Core-literal match |
| 18663 | 849370827 | `component::switchbot_cloud::exceptions::connection_error::message` | Error communicating with SwitchBot Cloud: {error} | Fel vid kommunikation med SwitchBot Cloud: {error} | Core-literal match |
| 18664 | 849370826 | `component::switchbot_cloud::exceptions::command_failed::message` | SwitchBot Cloud command failed: {error} | SwitchBot Cloud-kommandot misslyckades: {error} | Core-literal match |
| 18665 | 849370139 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::swing` | Swing | Svängning | Core-literal match |
| 18666 | 849370138 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos9` | Position 9 | Position 9 | Core-literal match |
| 18667 | 849370137 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos8` | Position 8 | Position 8 | Core-literal match |
| 18668 | 849370136 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos7` | Position 7 | Position 7 | Core-literal match |
| 18669 | 849370135 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos6` | Position 6 | Position 6 | Core-literal match |
| 18670 | 849370134 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos5` | Position 5 | Position 5 | Core-literal match |
| 18671 | 849370133 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos4` | Position 4 | Position 4 | Core-literal match |
| 18672 | 849370132 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos3` | Position 3 | Position 3 | Core-literal match |
| 18673 | 849370131 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos2` | Position 2 | Position 2 | Core-literal match |
| 18674 | 849370130 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos15` | Position 15 | Position 15 | Core-literal match |
| 18675 | 849370129 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos14` | Position 14 | Position 14 | Core-literal match |
| 18676 | 849370128 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos13` | Position 13 | Position 13 | Core-literal match |
| 18677 | 849370127 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos12` | Position 12 | Position 12 | Core-literal match |
| 18678 | 849370126 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos11` | Position 11 | Position 11 | Core-literal match |
| 18679 | 849370125 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos10` | Position 10 | Position 10 | Core-literal match |
| 18680 | 849370124 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::pos1` | Position 1 | Position 1 | Core-literal match |
| 18681 | 849370123 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::auto_stop` | Auto Stop | Autostopp | Core-literal match |
| 18682 | 849370122 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::auto` | Auto | Auto | Shared reference target checked |
| 18683 | 849370121 | `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::adjust` | Adjust | Justera | Core-literal match |
| 18684 | 849370120 | `component::cielo_home::entity::climate::climate_device::state_attributes::fan_mode::state::ultra_high` | Ultra high | Ultrahög | Core-literal match |
| 18685 | 849370119 | `component::cielo_home::entity::climate::climate_device::state_attributes::fan_mode::state::super_high` | Super high | Superhög | Core-literal match |
| 18686 | 849370118 | `component::cielo_home::entity::climate::climate_device::state_attributes::fan_mode::state::quiet` | Quiet | Tyst | Core-literal match |
| 18687 | 849370117 | `component::cielo_home::entity::climate::climate_device::state_attributes::fan_mode::state::medium` | Medium | Medel | Shared reference target checked |
| 18688 | 849370116 | `component::cielo_home::entity::climate::climate_device::state_attributes::fan_mode::state::low` | Low | Låg | Shared reference target checked |
| 18689 | 849370115 | `component::cielo_home::entity::climate::climate_device::state_attributes::fan_mode::state::high` | High | Hög | Shared reference target checked |
| 18690 | 849370114 | `component::cielo_home::entity::climate::climate_device::state_attributes::fan_mode::state::auto` | Auto | Auto | Shared reference target checked |
| 18691 | 849370113 | `component::cielo_home::config::step::user::title` | Connect to Cielo Home | Anslut till Cielo Home | Core-literal match |
| 18692 | 849370112 | `component::cielo_home::config::step::user::description` | Sign in with your Cielo Home API key. Follow the [documentation]({url}) to learn how to get your API key. | Logga in med API-nyckeln för ditt Cielo Home-konto. Följ [dokumentationen]({url}) om hur du hämtar API-nyckeln. | Core-literal match |
| 18693 | 849370111 | `component::cielo_home::config::step::user::data_description::api_key` | The API key from your Cielo Home account | API-nyckeln från ditt Cielo Home-konto | Core-literal match |
| 18694 | 849370110 | `component::cielo_home::config::step::user::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 18695 | 849370109 | `component::cielo_home::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 18696 | 849370108 | `component::cielo_home::config::error::no_user_id` | No valid user information found for the API key | Ingen giltig användarinformation hittades för API-nyckeln | Core-literal match |
| 18697 | 849370107 | `component::cielo_home::config::error::no_devices` | No devices found; make sure devices are set up in the Cielo Home app | Inga enheter hittades. Se till att enheterna är konfigurerade i Cielo Home-appen | Core-literal match |
| 18698 | 849370106 | `component::cielo_home::config::error::invalid_auth` | Invalid or expired API key; generate a new one | Ogiltig eller utgången API-nyckel. Generera en ny | Core-literal match |
| 18699 | 849370105 | `component::cielo_home::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18700 | 849370104 | `component::cielo_home::config::abort::single_instance_allowed` | Already configured. Only a single configuration is possible. | Redan konfigurerad. Endast en konfiguration kan göras. | Source-path follow-up open |
| 18701 | 849370103 | `component::cielo_home::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 18702 | 849367760 | `component::hr_energy_qube::exceptions::switch_command_failed::message` | Failed to send command to the heat pump. | Misslyckades med att skicka kommando till värmepumpen. | Core-literal match |
| 18703 | 849367759 | `component::hr_energy_qube::entity::switch::summer_mode::name` | Summer mode | Sommarläge | Core-literal match |
| 18704 | 849367758 | `component::hr_energy_qube::entity::switch::heating_demand::name` | Heating demand | Värmebehov | Core-literal match |
| 18705 | 849367757 | `component::hr_energy_qube::entity::switch::heating_curve::name` | Heating curve | Värmekurva | Core-literal match |
| 18706 | 849367756 | `component::hr_energy_qube::entity::switch::anti_legionella_cycle::name` | Anti-legionella cycle | Anti-legionellacykel | Core-literal match |
| 18707 | 849367564 | `component::data_grand_lyon::entity::sensor::next_departure_3_type::state::theoretical` | Theoretical | Teoretisk | Shared reference target checked |
| 18708 | 849367563 | `component::data_grand_lyon::entity::sensor::next_departure_3_type::state::estimated` | Estimated | Uppskattad | Shared reference target checked |
| 18709 | 849367562 | `component::data_grand_lyon::entity::sensor::next_departure_3_type::name` | Next departure 3 type | Typ för nästa avgång 3 | Core-literal match |
| 18710 | 849367561 | `component::data_grand_lyon::entity::sensor::next_departure_3_direction::name` | Next departure 3 direction | Riktning för nästa avgång 3 | Core-literal match |
| 18711 | 849367560 | `component::data_grand_lyon::entity::sensor::next_departure_3::name` | Next departure 3 | Nästa avgång 3 | Core-literal match |
| 18712 | 849367559 | `component::data_grand_lyon::entity::sensor::next_departure_2_type::state::theoretical` | Theoretical | Teoretisk | Shared reference target checked |
| 18713 | 849367558 | `component::data_grand_lyon::entity::sensor::next_departure_2_type::state::estimated` | Estimated | Uppskattad | Shared reference target checked |
| 18714 | 849367557 | `component::data_grand_lyon::entity::sensor::next_departure_2_type::name` | Next departure 2 type | Typ för nästa avgång 2 | Core-literal match |
| 18715 | 849367556 | `component::data_grand_lyon::entity::sensor::next_departure_2_direction::name` | Next departure 2 direction | Riktning för nästa avgång 2 | Core-literal match |
| 18716 | 849367555 | `component::data_grand_lyon::entity::sensor::next_departure_2::name` | Next departure 2 | Nästa avgång 2 | Core-literal match |
| 18717 | 849367554 | `component::data_grand_lyon::entity::sensor::next_departure_1_type::state::theoretical` | Theoretical | Teoretisk | Core-literal match |
| 18718 | 849367553 | `component::data_grand_lyon::entity::sensor::next_departure_1_type::state::estimated` | Estimated | Uppskattad | Core-literal match |
| 18719 | 849367552 | `component::data_grand_lyon::entity::sensor::next_departure_1_type::name` | Next departure 1 type | Typ för nästa avgång 1 | Core-literal match |
| 18720 | 849367551 | `component::data_grand_lyon::entity::sensor::next_departure_1_direction::name` | Next departure 1 direction | Riktning för nästa avgång 1 | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 850471475 | `component::data_grand_lyon::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 850031510 | `component::data_grand_lyon::exceptions::update_failed_all_stops::message` | Error fetching Data Grand Lyon data: all requests failed. |
| 849997243 | `component::novy_cooker_hood::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 849768457 | `component::nobo_hub::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |
| 849542566 | `component::data_grand_lyon::config::abort::reauth_successful` | Re-authentication was successful |
| 849370104 | `component::cielo_home::config::abort::single_instance_allowed` | Already configured. Only a single configuration is possible. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
