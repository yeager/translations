# Home Assistant Core – historisk avstämning 13801–13920

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 74 direkta källtexter matchar HA Core-källan; 30 referensanvändningar med 20 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 16 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 13801 | 902235475 | `component::ecovacs::entity::button::reset_lifespan_sewage_box::name` | Reset sewage box lifespan | Återställ avloppsbehållarens livslängd | Core-literal match |
| 13802 | 902235474 | `component::ecovacs::entity::button::reset_lifespan_cleaning_solution::name` | Reset cleaning solution lifespan | Återställ rengöringslösningens livslängd | Core-literal match |
| 13803 | 902235447 | `component::harbor::exceptions::switch_turn_on_failed::message` | Failed to turn on {switch}. | Misslyckades med att slå på {switch}. | Core-literal match |
| 13804 | 902235446 | `component::harbor::exceptions::switch_turn_off_failed::message` | Failed to turn off {switch}. | Misslyckades med att stänga av {switch}. | Core-literal match |
| 13805 | 902235445 | `component::harbor::entity::switch::video_flip::name` | Flip image | Vänd bild | Core-literal match |
| 13806 | 902235444 | `component::harbor::entity::switch::clock_display::name` | Clock overlay | Klocka i bild | Core-literal match |
| 13807 | 902235443 | `component::harbor::entity::switch::camera_on::name` | Camera | Kamera | Core-literal match |
| 13808 | 902124304 | `component::led_infrared::entity::button::white_on::name` | White on | Vitt på | Shared reference target checked |
| 13809 | 902124303 | `component::led_infrared::entity::button::white_off::name` | White off | Vit av | Shared reference target checked |
| 13810 | 902124302 | `component::led_infrared::entity::button::white_brightness_up::name` | White brightness up | Vit ljusstyrka öka | Shared reference target checked |
| 13811 | 902124301 | `component::led_infrared::entity::button::white_brightness_down::name` | White brightness down | Vit ljusstyrka minska | Shared reference target checked |
| 13812 | 902124300 | `component::led_infrared::entity::button::white_brightness_75::name` | White brightness 75% | Vit ljusstyrka 75 % | Shared reference target checked |
| 13813 | 902124299 | `component::led_infrared::entity::button::white_brightness_50::name` | White brightness 50% | Vit ljusstyrka 50 % | Shared reference target checked |
| 13814 | 902124298 | `component::led_infrared::entity::button::white_brightness_25::name` | White brightness 25% | Vit ljusstyrka 25 % | Shared reference target checked |
| 13815 | 902124297 | `component::led_infrared::entity::button::white_brightness_100::name` | White brightness 100% | Vit ljusstyrka 100 % | Shared reference target checked |
| 13816 | 902124296 | `component::led_infrared::entity::button::slow::name` | Slow | Långsam | Shared reference target checked |
| 13817 | 902124295 | `component::led_infrared::entity::button::red_up::name` | Red up | Röd upp | Shared reference target checked |
| 13818 | 902124294 | `component::led_infrared::entity::button::red_down::name` | Red down | Röd ner | Shared reference target checked |
| 13819 | 902124293 | `component::led_infrared::entity::button::quick::name` | Quick | Snabb | Shared reference target checked |
| 13820 | 902124292 | `component::led_infrared::entity::button::green_up::name` | Green up | Grön upp | Shared reference target checked |
| 13821 | 902124291 | `component::led_infrared::entity::button::green_down::name` | Green down | Grön ner | Shared reference target checked |
| 13822 | 902124290 | `component::led_infrared::entity::button::blue_up::name` | Blue up | Blå upp | Shared reference target checked |
| 13823 | 902124289 | `component::led_infrared::entity::button::blue_down::name` | Blue down | Blå ner | Shared reference target checked |
| 13824 | 902100830 | `component::lyric::entity::sensor::room_average_temperature::name` | Room average temperature | Genomsnittlig rumstemperatur | Core-literal match |
| 13825 | 902027789 | `component::roborock::services::set_vacuum_zoned_cleaning::name` | Clean zone | Rengör zon | Core-literal match |
| 13826 | 902027788 | `component::roborock::services::set_vacuum_zoned_cleaning::fields::y2::name` | Y2-coordinate | Y2-koordinat | Core-literal match |
| 13827 | 902027787 | `component::roborock::services::set_vacuum_zoned_cleaning::fields::y2::description` | The second y-coordinate of the zone. | Zonens andra y-koordinat. | Core-literal match |
| 13828 | 902027786 | `component::roborock::services::set_vacuum_zoned_cleaning::fields::y1::name` | Y1-coordinate | Y1-koordinat | Core-literal match |
| 13829 | 902027785 | `component::roborock::services::set_vacuum_zoned_cleaning::fields::y1::description` | The first y-coordinate of the zone. | Zonens första y-koordinat. | Core-literal match |
| 13830 | 902027784 | `component::roborock::services::set_vacuum_zoned_cleaning::fields::x2::name` | X2-coordinate | X2-koordinat | Core-literal match |
| 13831 | 902027783 | `component::roborock::services::set_vacuum_zoned_cleaning::fields::x2::description` | The second x-coordinate of the zone. | Zonens andra x-koordinat. | Core-literal match |
| 13832 | 902027782 | `component::roborock::services::set_vacuum_zoned_cleaning::fields::x1::name` | X1-coordinate | X1-koordinat | Core-literal match |
| 13833 | 902027781 | `component::roborock::services::set_vacuum_zoned_cleaning::fields::x1::description` | The first x-coordinate of the zone. | Zonens första x-koordinat. | Core-literal match |
| 13834 | 902027780 | `component::roborock::services::set_vacuum_zoned_cleaning::fields::repeats::name` | Repeats | Upprepningar | Core-literal match |
| 13835 | 902027779 | `component::roborock::services::set_vacuum_zoned_cleaning::fields::repeats::description` | The number of times the zone cleaning is repeated. '0' is just cleaning once. | Antalet gånger zonrengöringen upprepas. '0' är bara en rengöring. | Core-literal match |
| 13836 | 902027778 | `component::roborock::services::set_vacuum_zoned_cleaning::description` | Starts cleaning the specified zone. | Börjar rengöra den angivna zonen. | Core-literal match |
| 13837 | 902022788 | `component::doorbird::entity::image::last_ring::name` | Last ring | Senaste ringning | Shared reference target checked |
| 13838 | 902022787 | `component::doorbird::entity::image::last_motion::name` | Last motion | Senaste rörelse | Shared reference target checked |
| 13839 | 902022770 | `component::vicare::entity::sensor::extract_temperature::name` | Extract temperature | Frånluftstemperatur | Core-literal match |
| 13840 | 902022769 | `component::vicare::entity::sensor::extract_humidity::name` | Extract humidity | Frånluftens fuktighet | Core-literal match |
| 13841 | 902022768 | `component::vicare::entity::sensor::exhaust_temperature::name` | Exhaust temperature | Avluftstemperatur | Core-literal match |
| 13842 | 902022767 | `component::vicare::entity::sensor::exhaust_humidity::name` | Exhaust humidity | Avluftens fuktighet | Core-literal match |
| 13843 | 902022766 | `component::eurotronic_cometblue::exceptions::device_not_found::message` | Could not find Comet Blue device with address {address}: {reason} | Kunde inte hitta Comet Blue-enheten med adress {address}: {reason} | Core-literal match |
| 13844 | 901980824 | `component::vizio::exceptions::command_error::message` | Failed to send command to the device: {error} | Misslyckades med att skicka kommando till enheten: {error} | Core-literal match |
| 13845 | 901931433 | `component::hassio::issues::issue_addon_app_port_conflict::title` | App port conflict | Portkonflikt för app | Core-literal match |
| 13846 | 901931432 | `component::hassio::issues::issue_addon_app_port_conflict::fix_flow::step::fix_menu::menu_options::addon_execute_start` | Start after manual unblock | Starta efter manuell avblockering | Core-literal match |
| 13847 | 901931431 | `component::hassio::issues::issue_addon_app_port_conflict::fix_flow::step::fix_menu::menu_options::addon_clear_port_config` | Clear port configuration | Rensa portkonfigurationen | Core-literal match |
| 13848 | 901931430 | `component::hassio::issues::issue_addon_app_port_conflict::fix_flow::step::fix_menu::description` | App {addon} has a port conflict on port {port}. You can clear the port configuration in the app settings to automatically resolve this and start the app, or you can manually unblock the port by stopping or reconfiguring the other service using it. | Appen {addon} har en portkonflikt på port {port}. Du kan rensa portkonfigurationen i appinställningarna för att lösa detta automatiskt och starta appen, eller så kan du manuellt avblockera porten genom att stoppa eller konfigurera om den andra tjänsten som använder porten. | Core-literal match |
| 13849 | 901931429 | `component::hassio::issues::issue_addon_app_port_conflict::fix_flow::step::addon_execute_start::description` | App {addon} has a port conflict on port {port}. The app cannot change this in settings. Please uninstall the app or stop and reconfigure the other service using port {port}. Once unblocked, select this option again to start the app. | Appen {addon} har en portkonflikt på port {port}. Appen kan inte ändra detta i inställningarna. Avinstallera appen eller stoppa och konfigurera om den andra tjänsten på port {port}. När blockeringen är löst, välj det här alternativet igen för att starta appen. | Core-literal match |
| 13850 | 901931428 | `component::hassio::issues::issue_addon_app_port_conflict::fix_flow::abort::apply_suggestion_fail` | Could not apply the fix. Check the Supervisor logs for more details. | Kunde inte tillämpa korrigeringen. Kontrollera Supervisor-loggarna för mer information. | Core-literal match |
| 13851 | 901814624 | `component::sun::triggers::sunset::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-path follow-up open |
| 13852 | 901814623 | `component::sun::triggers::sunset::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-path follow-up open |
| 13853 | 901814622 | `component::sun::triggers::sunset::fields::offset::name` | Offset | Förskjutning | Shared reference target checked |
| 13854 | 901814621 | `component::sun::triggers::sunset::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference target checked |
| 13855 | 901814620 | `component::sun::triggers::sunrise::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-path follow-up open |
| 13856 | 901814619 | `component::sun::triggers::sunrise::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-path follow-up open |
| 13857 | 901814618 | `component::sun::triggers::sunrise::fields::offset::name` | Offset | Förskjutning | Shared reference target checked |
| 13858 | 901814617 | `component::sun::triggers::sunrise::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference target checked |
| 13859 | 901814616 | `component::sun::triggers::solar_noon::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-path follow-up open |
| 13860 | 901814615 | `component::sun::triggers::solar_noon::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-path follow-up open |
| 13861 | 901814614 | `component::sun::triggers::solar_noon::fields::offset::name` | Offset | Förskjutning | Shared reference target checked |
| 13862 | 901814613 | `component::sun::triggers::solar_noon::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference target checked |
| 13863 | 901814612 | `component::sun::triggers::solar_midnight::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-path follow-up open |
| 13864 | 901814611 | `component::sun::triggers::solar_midnight::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-path follow-up open |
| 13865 | 901814610 | `component::sun::triggers::solar_midnight::fields::offset::name` | Offset | Förskjutning | Shared reference target checked |
| 13866 | 901814609 | `component::sun::triggers::solar_midnight::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference target checked |
| 13867 | 901814608 | `component::sun::triggers::dusk::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-path follow-up open |
| 13868 | 901814607 | `component::sun::triggers::dusk::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-path follow-up open |
| 13869 | 901814606 | `component::sun::triggers::dusk::fields::offset::name` | Offset | Förskjutning | Shared reference target checked |
| 13870 | 901814605 | `component::sun::triggers::dusk::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference target checked |
| 13871 | 901814604 | `component::sun::triggers::dawn::fields::offset_type::name` | Offset type | Förskjutningstyp | Source-path follow-up open |
| 13872 | 901814603 | `component::sun::triggers::dawn::fields::offset_type::description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-path follow-up open |
| 13873 | 901814602 | `component::sun::triggers::dawn::fields::offset::name` | Offset | Förskjutning | Shared reference target checked |
| 13874 | 901814601 | `component::sun::triggers::dawn::fields::offset::description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Shared reference target checked |
| 13875 | 901814600 | `component::sun::selector::trigger_offset_type::options::before` | Before | Före | Source-path follow-up open |
| 13876 | 901814599 | `component::sun::selector::trigger_offset_type::options::after` | After | Efter | Source-path follow-up open |
| 13877 | 901814598 | `component::sun::common::trigger_offset_type_name` | Offset type | Förskjutningstyp | Source-path follow-up open |
| 13878 | 901814597 | `component::sun::common::trigger_offset_type_description` | Whether to trigger before or after the solar event. | Om den ska utlösas före eller efter solhändelsen. | Source-path follow-up open |
| 13879 | 901814596 | `component::sun::common::trigger_offset_name` | Offset | Förskjutning | Core-literal match |
| 13880 | 901814595 | `component::sun::common::trigger_offset_description` | Time to trigger before or after the solar event. | Tid att förskjuta utlösaren från solhändelsen. | Core-literal match |
| 13881 | 901630095 | `component::zha::entity::switch::remote_protection::name` | Remote protection | Fjärrskydd | Core-literal match |
| 13882 | 901630094 | `component::zha::entity::switch::metering_only_mode::name` | Metering only mode | Endast mätning | Core-literal match |
| 13883 | 901630093 | `component::zha::entity::switch::manual_mode::name` | Manual mode | Manuellt läge | Core-literal match |
| 13884 | 901630092 | `component::zha::entity::switch::local_control_id::name` | {id} local control | {id} lokal kontroll | Core-literal match |
| 13885 | 901630091 | `component::zha::entity::select::switch_type_id::name` | {id} switch type | {id} brytartyp | Core-literal match |
| 13886 | 901630090 | `component::zha::entity::select::switch_actions_id::name` | {id} switch actions | {id} brytaråtgärder | Core-literal match |
| 13887 | 901630089 | `component::zha::entity::select::mmwave_room_size_preset::name` | mmWave room size preset | Förinställd rumsstorlek för mmWave | Core-literal match |
| 13888 | 901630088 | `component::zha::entity::select::mmwave_detect_trigger::name` | mmWave target speed | Målhastighet för mmWave | Core-literal match |
| 13889 | 901630087 | `component::zha::entity::select::mmwave_detect_sensitivity::name` | mmWave sensitivity | Känslighet för mmWave | Core-literal match |
| 13890 | 901630086 | `component::zha::entity::select::light_on_presence_behavior::name` | Light on presence behavior | Beteende för ljus vid närvaro | Core-literal match |
| 13891 | 901630085 | `component::zha::entity::number::valve_position::name` | Valve position | Ventilposition | Core-literal match |
| 13892 | 901630084 | `component::zha::entity::number::red_led_brightness::name` | Red LED brightness | Ljusstyrka för röd lysdiod | Core-literal match |
| 13893 | 901630083 | `component::zha::entity::number::power_rise_threshold::name` | Power rise threshold | Tröskelvärde för effektökning | Core-literal match |
| 13894 | 901630082 | `component::zha::entity::number::power_drop_threshold::name` | Power drop threshold | Tröskelvärde för effektminskning | Core-literal match |
| 13895 | 901630081 | `component::zha::entity::number::mmwave_width_minimum_left::name` | mmWave width minimum (left) | mmWave: minsta bredd (vänster) | Core-literal match |
| 13896 | 901630080 | `component::zha::entity::number::mmwave_width_maximum_right::name` | mmWave width maximum (right) | mmWave: största bredd (höger) | Core-literal match |
| 13897 | 901630079 | `component::zha::entity::number::mmwave_hold_time::name` | mmWave hold time | Hålltid för mmWave | Core-literal match |
| 13898 | 901630078 | `component::zha::entity::number::mmwave_height_minimum_floor::name` | mmWave height minimum (floor) | mmWave: lägsta höjd (golv) | Core-literal match |
| 13899 | 901630077 | `component::zha::entity::number::mmwave_height_maximum_ceiling::name` | mmWave height maximum (ceiling) | mmWave: högsta höjd (tak) | Core-literal match |
| 13900 | 901630076 | `component::zha::entity::number::mmwave_depth_minimum_near::name` | mmWave depth minimum (near) | mmWave: minsta djup (nära) | Core-literal match |
| 13901 | 901630075 | `component::zha::entity::number::mmwave_depth_maximum_far::name` | mmWave depth maximum (far) | mmWave: största djup (långt bort) | Core-literal match |
| 13902 | 901630074 | `component::zha::entity::number::countdown_to_turn_on_top::name` | Countdown to turn on top | Nedräkning för att slå på övre | Core-literal match |
| 13903 | 901630073 | `component::zha::entity::number::countdown_to_turn_on_right::name` | Countdown to turn on right | Nedräkning för att slå på höger | Core-literal match |
| 13904 | 901630072 | `component::zha::entity::number::countdown_to_turn_on_left::name` | Countdown to turn on left | Nedräkning för att slå på vänster | Core-literal match |
| 13905 | 901630071 | `component::zha::entity::number::countdown_to_turn_on_bottom::name` | Countdown to turn on bottom | Nedräkning för att slå på nedre | Core-literal match |
| 13906 | 901630070 | `component::zha::entity::number::countdown_to_turn_on::name` | Countdown to turn on | Nedräkning för att slå på | Core-literal match |
| 13907 | 901630069 | `component::zha::entity::number::countdown_to_turn_off_top::name` | Countdown to turn off top | Nedräkning för att stänga av övre | Core-literal match |
| 13908 | 901630068 | `component::zha::entity::number::countdown_to_turn_off_right::name` | Countdown to turn off right | Nedräkning för att stänga av höger | Core-literal match |
| 13909 | 901630067 | `component::zha::entity::number::countdown_to_turn_off_left::name` | Countdown to turn off left | Nedräkning för att stänga av vänster | Core-literal match |
| 13910 | 901630066 | `component::zha::entity::number::countdown_to_turn_off_bottom::name` | Countdown to turn off bottom | Nedräkning för att stänga av nedre | Core-literal match |
| 13911 | 901630065 | `component::zha::entity::number::countdown_to_turn_off::name` | Countdown to turn off | Nedräkning för att stänga av | Core-literal match |
| 13912 | 901630064 | `component::zha::entity::button::reset_total_energy_top::name` | Reset top total energy | Återställ den övre totala energin | Core-literal match |
| 13913 | 901630063 | `component::zha::entity::button::reset_total_energy_right::name` | Reset right total energy | Återställ den högra totala energin | Core-literal match |
| 13914 | 901630062 | `component::zha::entity::button::reset_total_energy_left::name` | Reset left total energy | Återställ den vänsta totala energin | Core-literal match |
| 13915 | 901630061 | `component::zha::entity::button::reset_total_energy_bottom::name` | Reset bottom total energy | Återställ den nedre totala energin | Core-literal match |
| 13916 | 901630060 | `component::zha::entity::button::reset_total_energy::name` | Reset total energy | Återställ total energi | Core-literal match |
| 13917 | 901630059 | `component::zha::entity::binary_sensor::tilt::name` | Tilt | Lutning | Core-literal match |
| 13918 | 901279965 | `component::template::issues::composite_device_id::title` | Device for template helper {name} needs to be selected again | Enheten för mallhjälparen {name} måste väljas på nytt | Core-literal match |
| 13919 | 901279964 | `component::template::issues::composite_device_id::fix_flow::step::select_device::title` | Select device for {name} | Välj enhet för {name} | Core-literal match |
| 13920 | 901279963 | `component::template::issues::composite_device_id::fix_flow::step::select_device::description` | The template helper {name} was linked to a device which has been split into multiple devices. Until a device is selected, the helper is not linked to any device.<br><br>Select the device this helper should be linked to, or leave empty to not link it to a device. | Mallhjälparen {name} var kopplad till en enhet som har delats upp i flera enheter. Så länge ingen enhet har valts är hjälparen inte kopplad till någon enhet.<br><br>Välj den enhet som denna hjälpare ska kopplas till, eller lämna fältet tomt om du inte vill koppla den till någon enhet. | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 901814624 | `component::sun::triggers::sunset::fields::offset_type::name` | Offset type |
| 901814623 | `component::sun::triggers::sunset::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 901814620 | `component::sun::triggers::sunrise::fields::offset_type::name` | Offset type |
| 901814619 | `component::sun::triggers::sunrise::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 901814616 | `component::sun::triggers::solar_noon::fields::offset_type::name` | Offset type |
| 901814615 | `component::sun::triggers::solar_noon::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 901814612 | `component::sun::triggers::solar_midnight::fields::offset_type::name` | Offset type |
| 901814611 | `component::sun::triggers::solar_midnight::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 901814608 | `component::sun::triggers::dusk::fields::offset_type::name` | Offset type |
| 901814607 | `component::sun::triggers::dusk::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 901814604 | `component::sun::triggers::dawn::fields::offset_type::name` | Offset type |
| 901814603 | `component::sun::triggers::dawn::fields::offset_type::description` | Whether to trigger before or after the solar event. |
| 901814600 | `component::sun::selector::trigger_offset_type::options::before` | Before |
| 901814599 | `component::sun::selector::trigger_offset_type::options::after` | After |
| 901814598 | `component::sun::common::trigger_offset_type_name` | Offset type |
| 901814597 | `component::sun::common::trigger_offset_type_description` | Whether to trigger before or after the solar event. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
