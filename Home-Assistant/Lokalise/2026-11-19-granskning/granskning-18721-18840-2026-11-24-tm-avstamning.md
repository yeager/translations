# Home Assistant Core – historisk avstämning 18721–18840

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 61 direkta källtexter matchar HA Core-källan; 30 referensanvändningar med 20 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 29 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 18721 | 849367550 | `component::data_grand_lyon::entity::sensor::next_departure_1::name` | Next departure 1 | Nästa avgång 1 | Core-literal match |
| 18722 | 849367549 | `component::data_grand_lyon::config_subentries::stop::step::user::data::stop_id` | Stop | Hållplats | Core-literal match |
| 18723 | 849367548 | `component::data_grand_lyon::config_subentries::stop::step::user::data::line` | Line | Linje | Source-path follow-up open |
| 18724 | 849367547 | `component::data_grand_lyon::config_subentries::stop::initiate_flow::user` | Add transit stop | Lägg till hållplats | Core-literal match |
| 18725 | 849367546 | `component::data_grand_lyon::config_subentries::stop::entry_type` | Transit stop | Hållplats | Core-literal match |
| 18726 | 849367545 | `component::data_grand_lyon::config_subentries::stop::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Shared reference target checked |
| 18727 | 849367544 | `component::data_grand_lyon::config::step::user::data_description::username` | Your username on data.grandlyon.com. | Ditt användarnamn på data.grandlyon.com. | Core-literal match |
| 18728 | 849367543 | `component::data_grand_lyon::config::step::user::data_description::password` | Your password on data.grandlyon.com. | Ditt lösenord på data.grandlyon.com. | Core-literal match |
| 18729 | 849367542 | `component::data_grand_lyon::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 18730 | 849367541 | `component::data_grand_lyon::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 18731 | 849367540 | `component::data_grand_lyon::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 18732 | 849367539 | `component::data_grand_lyon::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 18733 | 849367538 | `component::data_grand_lyon::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18734 | 849367537 | `component::data_grand_lyon::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Shared reference target checked |
| 18735 | 849365810 | `component::vicare::issues::update_redirect_uri::title` | Update your API client in the Viessmann Developer Portal | Uppdatera din API-klient i Viessmann Developer Portal | Core-literal match |
| 18736 | 849365809 | `component::vicare::issues::update_redirect_uri::description` | ViCare has been migrated to OAuth2 authentication. Your existing session will continue to work, but if re-authentication is ever needed, you must first add a redirect URI to your API client.<br><br>Go to the [Viessmann Developer Portal]({viessmann_developer_portal}) and add the following redirect URI to your API client:<br><br>`{redirect_url}`<br><br>This is not urgent, but we recommend doing it soon. | ViCare har övergått till OAuth2-autentisering. Din nuvarande session kommer att fortsätta att fungera, men om du någon gång behöver autentisera dig på nytt måste du först lägga till en omdirigerings-URI i din API-klient.<br><br>Gå till [Viessmann Developer Portal]({viessmann_developer_portal}) och lägg till följande omdirigerings-URI till din API-klient:<br><br>`{redirect_url}`<br><br>Detta är inte brådskande, men vi rekommenderar att du gör det snart. | Core-literal match |
| 18737 | 849365808 | `component::vicare::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 18738 | 849365807 | `component::vicare::config::step::pick_implementation::title` | Pick authentication method | Välj autentiseringsmetod | Shared reference target checked |
| 18739 | 849365806 | `component::vicare::config::create_entry::default` | Successfully authenticated | Autentisering lyckades | Shared reference target checked |
| 18740 | 849365805 | `component::vicare::config::abort::user_rejected_authorize` | Account linking rejected: {error} | Kontolänkning avvisades: {error} | Source-path follow-up open |
| 18741 | 849365804 | `component::vicare::config::abort::oauth_unauthorized` | OAuth authorization error while obtaining access token. | OAuth-auktoriseringsfel vid hämtning av åtkomsttoken. | Source-path follow-up open |
| 18742 | 849365803 | `component::vicare::config::abort::oauth_timeout` | Timeout while resolving the OAuth token. | Tidsgränsen överskreds när OAuth-token hämtades. | Source-path follow-up open |
| 18743 | 849365802 | `component::vicare::config::abort::oauth_failed` | Error while obtaining access token. | Fel vid hämtning av åtkomsttoken. | Source-path follow-up open |
| 18744 | 849365801 | `component::vicare::config::abort::oauth_error` | Received invalid token data. | Ogiltiga tokendata mottogs. | Source-path follow-up open |
| 18745 | 849365800 | `component::vicare::config::abort::no_url_available` | No URL available. For information about this error, [check the help section]({docs_url}) | Ingen webbadress är tillgänglig. [Se hjälpavsnittet]({docs_url}) för information om det här felet. | Source-path follow-up open |
| 18746 | 849365799 | `component::vicare::config::abort::missing_credentials` | The integration requires application credentials. | Integrationen kräver applikationsuppgifter. | Source-path follow-up open |
| 18747 | 849365798 | `component::vicare::config::abort::missing_configuration` | The component is not configured. Please follow the documentation. | Komponenten har inte konfigurerats. Följ dokumentationen. | Shared reference target checked |
| 18748 | 849365797 | `component::vicare::config::abort::authorize_url_timeout` | Timeout while generating an authorization URL. | Tidsgränsen överskreds vid generering av en auktoriserings-URL. | Source-path follow-up open |
| 18749 | 849365796 | `component::vicare::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 18750 | 849365606 | `component::lg_thinq::issues::deprecated_fan_speed_number_scripts::title` | Fan speed number entity deprecated | Fläkthastighetsnummerentitet är föråldrad | Source-path follow-up open |
| 18751 | 849365605 | `component::lg_thinq::issues::deprecated_fan_speed_number_scripts::fix_flow::step::confirm::title` | Fan speed number entity deprecated | Fläkthastighetsnummerentitet är föråldrad | Source-path follow-up open |
| 18752 | 849365604 | `component::lg_thinq::issues::deprecated_fan_speed_number_scripts::fix_flow::step::confirm::description` | The number entity {entity_name} (`{entity_id}`) is deprecated because it has been replaced with a fan entity.<br><br>The entity was used in the following automations or scripts:<br>{items}<br><br>Please update the above automations or scripts to use the new fan entity.<br><br>After updating, select **Submit** to disable the number entity and fix this issue. | Nummerenheten {entity_name} (`{entity_id}`) är föråldrad eftersom den har ersatts med en fläkt-entitet.<br><br>Entiteten användes i följande automatiseringar eller skript:<br>{items}<br><br>Uppdatera ovanstående automatiseringar eller skript för att använda den nya fläkt-entiteten.<br><br>Efter uppdateringen klickar du på **Bekräfta** för att inaktivera nummerenheten och åtgärda problemet. | Source-path follow-up open |
| 18753 | 849365603 | `component::lg_thinq::issues::deprecated_fan_speed_number::title` | Fan speed number entity deprecated | Fläkthastighetsnummerentitet är föråldrad | Source-path follow-up open |
| 18754 | 849365602 | `component::lg_thinq::issues::deprecated_fan_speed_number::fix_flow::step::confirm::title` | Fan speed number entity deprecated | Fläkthastighetsnummerentitet är föråldrad | Source-path follow-up open |
| 18755 | 849365601 | `component::lg_thinq::issues::deprecated_fan_speed_number::fix_flow::step::confirm::description` | The number entity {entity_name} (`{entity_id}`) is deprecated because it has been replaced with a fan entity.<br><br>Please update your dashboards and templates to use the new fan entity.<br><br>After updating, select **Submit** to disable the number entity and fix this issue. | Nummerenheten {entity_name} (`{entity_id}`) är föråldrad eftersom den har ersatts med en fläkt-entitet.<br><br>Uppdatera dina instrumentpaneler och mallar för att använda den nya fläkt-entiteten.<br><br>Efter uppdateringen klickar du på **Skicka** för att inaktivera nummerenheten och åtgärda problemet. | Source-path follow-up open |
| 18756 | 849365600 | `component::lg_thinq::entity::fan::fan_speed::name` | Hood | Kåpa | Core-literal match |
| 18757 | 849365057 | `component::dnsip::options::step::init::description` | Optionally change resolvers and ports. | Du kan vid behov byta ut resolver och portar. | Core-literal match |
| 18758 | 849365056 | `component::dnsip::config::step::user::sections::advanced_options::name` | Additional options | Ytterligare alternativ | Source-path follow-up open |
| 18759 | 849365055 | `component::dnsip::config::step::user::sections::advanced_options::description` | Optionally change resolvers and ports. | Du kan vid behov byta ut resolver och portar. | Source-path follow-up open |
| 18760 | 849365054 | `component::dnsip::config::step::user::sections::advanced_options::data_description::resolver_ipv6` | Resolver used for the IPv6 lookup. | Namnserver som används för IPv6-uppslagning. | Source-path follow-up open |
| 18761 | 849365053 | `component::dnsip::config::step::user::sections::advanced_options::data_description::resolver` | Resolver used for the IPv4 lookup. | Namnserver som används för IPv4-uppslagning. | Source-path follow-up open |
| 18762 | 849365052 | `component::dnsip::config::step::user::sections::advanced_options::data_description::port_ipv6` | Port used for the IPv6 lookup. | Port som används för IPv6-uppslagning. | Source-path follow-up open |
| 18763 | 849365051 | `component::dnsip::config::step::user::sections::advanced_options::data_description::port` | Port used for the IPv4 lookup. | Port som används för IPv4-uppslagning. | Source-path follow-up open |
| 18764 | 849365050 | `component::dnsip::config::step::user::sections::advanced_options::data::resolver_ipv6` | IPv6 resolver | IPv6-resolver | Source-path follow-up open |
| 18765 | 849365049 | `component::dnsip::config::step::user::sections::advanced_options::data::resolver` | IPv4 resolver | IPv4-resolver | Source-path follow-up open |
| 18766 | 849365048 | `component::dnsip::config::step::user::sections::advanced_options::data::port_ipv6` | IPv6 port | IPv6-port | Source-path follow-up open |
| 18767 | 849365047 | `component::dnsip::config::step::user::sections::advanced_options::data::port` | IPv4 port | IPv4-port | Source-path follow-up open |
| 18768 | 849356231 | `component::fritz::exceptions::error_parse_device_info::message` | Error parsing device info. Please check the system event log of your FRITZ!Box for malformed data and clear the event list. | Fel vid tolkning av enhetsinformation. Kontrollera systemloggen för din FRITZ!Box för felaktiga data och rensa händelselistan. | Core-literal match |
| 18769 | 849356188 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::youtube` | YouTube | YouTube | Core-literal match |
| 18770 | 849356187 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::wifi` | Wi-Fi | Wi-Fi | Core-literal match |
| 18771 | 849356186 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::usb` | USB | USB | Core-literal match |
| 18772 | 849356185 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::phono` | Phono | Phono | Core-literal match |
| 18773 | 849356184 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::optical` | Optical | Optisk | Core-literal match |
| 18774 | 849356183 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::network` | Network | Nätverk | Core-literal match |
| 18775 | 849356182 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::melon` | Melon | Melon | Core-literal match |
| 18776 | 849356181 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::hdmi6` | HDMI 6 | HDMI 6 | Core-literal match |
| 18777 | 849356180 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::hdmi5` | HDMI 5 | HDMI 5 | Core-literal match |
| 18778 | 849356179 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::hdmi4` | HDMI 4 | HDMI 4 | Core-literal match |
| 18779 | 849356178 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::hdmi3` | HDMI 3 | HDMI 3 | Core-literal match |
| 18780 | 849356177 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::hdmi2` | HDMI 2 | HDMI 2 | Core-literal match |
| 18781 | 849356176 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::hdmi1` | HDMI 1 | HDMI 1 | Core-literal match |
| 18782 | 849356175 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::hdmi` | HDMI | HDMI | Core-literal match |
| 18783 | 849356174 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::fm` | FM | FM | Core-literal match |
| 18784 | 849356173 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::digital_tv` | Digital TV | Digital-TV | Core-literal match |
| 18785 | 849356172 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::digital_input` | Digital input | Digital ingång | Core-literal match |
| 18786 | 849356171 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::digital` | Digital | Digital | Core-literal match |
| 18787 | 849356170 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::coaxial` | Coaxial | Koaxial | Core-literal match |
| 18788 | 849356169 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::cd` | CD | CD | Core-literal match |
| 18789 | 849356168 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::bluetooth` | Bluetooth | Bluetooth | Core-literal match |
| 18790 | 849356167 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::aux` | AUX | AUX | Core-literal match |
| 18791 | 849356166 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::analog3` | Analog 3 | Analog 3 | Core-literal match |
| 18792 | 849356165 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::analog2` | Analog 2 | Analog 2 | Core-literal match |
| 18793 | 849356164 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::analog1` | Analog 1 | Analog 1 | Core-literal match |
| 18794 | 849356163 | `component::smartthings::entity::media_player::media_player::state_attributes::source::state::am` | AM | AM | Core-literal match |
| 18795 | 849257489 | `component::paj_gps::config::step::user::title` | PAJ GPS configuration | PAJ GPS-konfiguration | Core-literal match |
| 18796 | 849257488 | `component::paj_gps::config::step::user::description` | Set credentials for your PAJ GPS account (finder-portal.com). | Ange inloggningsuppgifter för ditt PAJ GPS-konto (finder-portal.com). | Core-literal match |
| 18797 | 849257487 | `component::paj_gps::config::step::user::data_description::password` | Password used to log in to Finder Portal (finder-portal.com) | Lösenord som används för att logga in på Finder Portal (finder-portal.com) | Core-literal match |
| 18798 | 849257486 | `component::paj_gps::config::step::user::data_description::email` | Email used to log in to Finder Portal (finder-portal.com) | E-postadress som används för att logga in på Finder Portal (finder-portal.com) | Core-literal match |
| 18799 | 849257485 | `component::paj_gps::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 18800 | 849257484 | `component::paj_gps::config::step::user::data::email` | Email | E-post | Shared reference target checked |
| 18801 | 849257483 | `component::paj_gps::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 18802 | 849257482 | `component::paj_gps::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 18803 | 849257481 | `component::paj_gps::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18804 | 849257480 | `component::paj_gps::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 18805 | 849222731 | `component::prusalink::entity::sensor::y_position::name` | Y-Position | Y-position | Core-literal match |
| 18806 | 849222730 | `component::prusalink::entity::sensor::x_position::name` | X-Position | X-position | Core-literal match |
| 18807 | 849222729 | `component::prusalink::entity::sensor::min_extrusion_temp::name` | Minimum extrusion temperature | Lägsta extruderingstemperatur | Core-literal match |
| 18808 | 849222728 | `component::prusalink::entity::sensor::location::name` | Location | Plats | Source-path follow-up open |
| 18809 | 849205291 | `component::tuya::entity::siren::siren::name` | Siren | Siren | Shared reference target checked |
| 18810 | 848159545 | `component::media_player::conditions::is_volume::name` | Media player volume | Mediaspelares volym | Core-literal match |
| 18811 | 848159544 | `component::media_player::conditions::is_volume::fields::threshold::name` | Threshold | Tröskelvärde | Shared reference target checked |
| 18812 | 848159543 | `component::media_player::conditions::is_volume::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18813 | 848159542 | `component::media_player::conditions::is_volume::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 18814 | 848159541 | `component::media_player::conditions::is_volume::description` | Tests the volume of one or more media players. | Testar volymen på en eller flera mediaspelare. | Core-literal match |
| 18815 | 848159540 | `component::media_player::common::condition_threshold_name` | Threshold | Tröskelvärde | Core-literal match |
| 18816 | 848139924 | `component::media_player::conditions::is_unmuted::name` | Media player is not muted | Mediaspelare är inte tystad | Core-literal match |
| 18817 | 848139923 | `component::media_player::conditions::is_unmuted::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18818 | 848139922 | `component::media_player::conditions::is_unmuted::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 18819 | 848139921 | `component::media_player::conditions::is_unmuted::description` | Tests if one or more media players are not muted. | Testar om en eller flera mediaspelare inte är tystade. | Core-literal match |
| 18820 | 848139920 | `component::media_player::conditions::is_muted::name` | Media player is muted | Mediaspelare är tystad | Core-literal match |
| 18821 | 848139919 | `component::media_player::conditions::is_muted::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18822 | 848139918 | `component::media_player::conditions::is_muted::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 18823 | 848139917 | `component::media_player::conditions::is_muted::description` | Tests if one or more media players are muted. | Testar om en eller flera mediaspelare är tystade. | Core-literal match |
| 18824 | 847956867 | `component::media_player::triggers::volume_crossed_threshold::name` | Media player volume crossed threshold | Mediaspelares volym har passerat tröskelvärdet | Core-literal match |
| 18825 | 847956866 | `component::media_player::triggers::volume_crossed_threshold::fields::threshold::name` | Threshold | Tröskelvärde | Shared reference target checked |
| 18826 | 847956865 | `component::media_player::triggers::volume_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 18827 | 847956864 | `component::media_player::triggers::volume_crossed_threshold::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 18828 | 847956863 | `component::media_player::triggers::volume_crossed_threshold::description` | Triggers when the volume of one or more media players crosses a threshold. | Utlöses när volymen på en eller flera mediespelare passerar ett tröskelvärde. | Core-literal match |
| 18829 | 847956862 | `component::media_player::triggers::volume_changed::name` | Media player volume changed | Mediaspelares volym har förändrats | Core-literal match |
| 18830 | 847956861 | `component::media_player::triggers::volume_changed::fields::threshold::name` | Threshold | Tröskelvärde | Shared reference target checked |
| 18831 | 847956860 | `component::media_player::triggers::volume_changed::description` | Triggers when the volume of one or more media players changes. | Utlöses när volymen på en eller flera mediespelare förändras. | Core-literal match |
| 18832 | 847956859 | `component::media_player::common::trigger_threshold_name` | Threshold | Tröskelvärde | Core-literal match |
| 18833 | 847803137 | `component::zinvolt::entity::select::battery_mode::state::connected_solar_panels` | Connected solar panels | Anslutna solpaneler | Core-literal match |
| 18834 | 847650889 | `component::timer::triggers::time_remaining::name` | Timer time remaining | Återstående timertid | Source-path follow-up open |
| 18835 | 847650888 | `component::timer::triggers::time_remaining::fields::remaining::name` | Time remaining | Återstående tid | Source-path follow-up open |
| 18836 | 847650887 | `component::timer::triggers::time_remaining::description` | Triggers when one or more timers reach a specific remaining time. | Utlöses när en eller flera timers når en viss återstående tid. | Source-path follow-up open |
| 18837 | 847551053 | `component::v2c::entity::light::logo_led::name` | Logo LED | Logotyp-LED | Core-literal match |
| 18838 | 847551052 | `component::v2c::entity::light::light_led::name` | Light LED | Ljus-LED | Core-literal match |
| 18839 | 847504645 | `component::switchbot::entity::number::display_time_offset::name` | Display time offset | Visningstidsförskjutning | Core-literal match |
| 18840 | 847314433 | `component::mqtt::issues::protocol_5_migration::title` | MQTT protocol migration failed | Migreringen av MQTT-protokollet misslyckades | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 849367548 | `component::data_grand_lyon::config_subentries::stop::step::user::data::line` | Line |
| 849365805 | `component::vicare::config::abort::user_rejected_authorize` | Account linking rejected: {error} |
| 849365804 | `component::vicare::config::abort::oauth_unauthorized` | OAuth authorization error while obtaining access token. |
| 849365803 | `component::vicare::config::abort::oauth_timeout` | Timeout while resolving the OAuth token. |
| 849365802 | `component::vicare::config::abort::oauth_failed` | Error while obtaining access token. |
| 849365801 | `component::vicare::config::abort::oauth_error` | Received invalid token data. |
| 849365800 | `component::vicare::config::abort::no_url_available` | No URL available. For information about this error, [check the help section]({docs_url}) |
| 849365799 | `component::vicare::config::abort::missing_credentials` | The integration requires application credentials. |
| 849365797 | `component::vicare::config::abort::authorize_url_timeout` | Timeout while generating an authorization URL. |
| 849365606 | `component::lg_thinq::issues::deprecated_fan_speed_number_scripts::title` | Fan speed number entity deprecated |
| 849365605 | `component::lg_thinq::issues::deprecated_fan_speed_number_scripts::fix_flow::step::confirm::title` | Fan speed number entity deprecated |
| 849365604 | `component::lg_thinq::issues::deprecated_fan_speed_number_scripts::fix_flow::step::confirm::description` | The number entity {entity_name} (`{entity_id}`) is deprecated because it has been replaced with a fan entity.

The entity was used in the following automations or scripts:
{items}

Please update the above automations or scripts to use the new fan entity.

After updating, select **Submit** to disable the number entity and fix this issue. |
| 849365603 | `component::lg_thinq::issues::deprecated_fan_speed_number::title` | Fan speed number entity deprecated |
| 849365602 | `component::lg_thinq::issues::deprecated_fan_speed_number::fix_flow::step::confirm::title` | Fan speed number entity deprecated |
| 849365601 | `component::lg_thinq::issues::deprecated_fan_speed_number::fix_flow::step::confirm::description` | The number entity {entity_name} (`{entity_id}`) is deprecated because it has been replaced with a fan entity.

Please update your dashboards and templates to use the new fan entity.

After updating, select **Submit** to disable the number entity and fix this issue. |
| 849365056 | `component::dnsip::config::step::user::sections::advanced_options::name` | Additional options |
| 849365055 | `component::dnsip::config::step::user::sections::advanced_options::description` | Optionally change resolvers and ports. |
| 849365054 | `component::dnsip::config::step::user::sections::advanced_options::data_description::resolver_ipv6` | Resolver used for the IPv6 lookup. |
| 849365053 | `component::dnsip::config::step::user::sections::advanced_options::data_description::resolver` | Resolver used for the IPv4 lookup. |
| 849365052 | `component::dnsip::config::step::user::sections::advanced_options::data_description::port_ipv6` | Port used for the IPv6 lookup. |
| 849365051 | `component::dnsip::config::step::user::sections::advanced_options::data_description::port` | Port used for the IPv4 lookup. |
| 849365050 | `component::dnsip::config::step::user::sections::advanced_options::data::resolver_ipv6` | IPv6 resolver |
| 849365049 | `component::dnsip::config::step::user::sections::advanced_options::data::resolver` | IPv4 resolver |
| 849365048 | `component::dnsip::config::step::user::sections::advanced_options::data::port_ipv6` | IPv6 port |
| 849365047 | `component::dnsip::config::step::user::sections::advanced_options::data::port` | IPv4 port |
| 849222728 | `component::prusalink::entity::sensor::location::name` | Location |
| 847650889 | `component::timer::triggers::time_remaining::name` | Timer time remaining |
| 847650888 | `component::timer::triggers::time_remaining::fields::remaining::name` | Time remaining |
| 847650887 | `component::timer::triggers::time_remaining::description` | Triggers when one or more timers reach a specific remaining time. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
