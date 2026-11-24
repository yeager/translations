# Home Assistant Core – historisk avstämning 15961–16080

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 92 direkta källtexter matchar HA Core-källan; 26 referensanvändningar med 19 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 2 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- En vakuumtrigger uppdaterades till exakt samma svenska mål som sin gemensamma referens, sparades i Lokalise och verifierades med API-readback. Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 15961 | 878564950 | `component::vistapool::entity::select::pump_mode::state::manual` | Manual | Manuell | Core-literal match |
| 15962 | 878564949 | `component::vistapool::entity::select::pump_mode::state::intel` | Intel | Intelligent | Core-literal match |
| 15963 | 878564948 | `component::vistapool::entity::select::pump_mode::state::heat` | Heat | Värme | Core-literal match |
| 15964 | 878564947 | `component::vistapool::entity::select::pump_mode::state::auto` | Auto | Auto | Core-literal match |
| 15965 | 878564946 | `component::vistapool::entity::select::pump_mode::name` | Pump mode | Pumpläge | Core-literal match |
| 15966 | 878564945 | `component::vistapool::entity::select::filtration_timer_speed::state::slow` | Slow | Långsam | Shared reference target checked |
| 15967 | 878564944 | `component::vistapool::entity::select::filtration_timer_speed::state::medium` | Medium | Medel | Shared reference target checked |
| 15968 | 878564943 | `component::vistapool::entity::select::filtration_timer_speed::state::high` | High | Hög | Shared reference target checked |
| 15969 | 878564942 | `component::vistapool::entity::select::filtration_timer_speed::name` | Filtration timer speed {number} | Filtreringstimer hastighet {number} | Core-literal match |
| 15970 | 878564033 | `component::nfandroidtv::exceptions::setup_connection_error::message` | Failed to connect to {name} | Det gick inte att ansluta till {name} | Core-literal match |
| 15971 | 878564032 | `component::nfandroidtv::exceptions::notify_connection_error::message` | Failed to send notification to {name} due to a connection error | Det gick inte att skicka meddelandet till {name} på grund av ett anslutningsfel | Core-literal match |
| 15972 | 878563408 | `component::lg_thinq::entity::sensor::energy_usage_today::name` | Energy today | Energi idag | Core-literal match |
| 15973 | 878563349 | `component::openevse::entity::button::restart_wifi::name` | Restart Wi-Fi | Starta om Wi-Fi | Core-literal match |
| 15974 | 878563348 | `component::openevse::entity::button::restart::name` | Restart | Starta om | Source-path follow-up open |
| 15975 | 878563328 | `component::melcloud_home::entity::switch::overheat_protection::name` | Overheat protection | Överhettningsskydd | Core-literal match |
| 15976 | 878563327 | `component::melcloud_home::entity::switch::frost_protection::name` | Frost protection | Frostskydd | Core-literal match |
| 15977 | 878562979 | `component::overkiz::config::error::application_not_allowed` | Your setup cannot be accessed through this application. | Det går inte att komma åt din konfiguration via den här applikationen. | Core-literal match |
| 15978 | 878562829 | `component::steam_online::entity::sensor::account::state_attributes::level::name` | Level | Level | Core-literal match |
| 15979 | 878562828 | `component::steam_online::entity::sensor::account::state_attributes::last_online::name` | Last online | Senast online | Core-literal match |
| 15980 | 878562827 | `component::steam_online::entity::sensor::account::state_attributes::game_image_main::name` | Game image | Spelbild | Core-literal match |
| 15981 | 878562826 | `component::steam_online::entity::sensor::account::state_attributes::game_image_header::name` | Game header image | Bild för spelhuvud | Core-literal match |
| 15982 | 878562825 | `component::steam_online::entity::sensor::account::state_attributes::game_id::name` | Game ID | Spel-ID | Core-literal match |
| 15983 | 878562824 | `component::steam_online::entity::sensor::account::state_attributes::game_icon::name` | Game icon | Spelikon | Core-literal match |
| 15984 | 878562823 | `component::steam_online::entity::sensor::account::state_attributes::game::name` | Game | Spel | Core-literal match |
| 15985 | 878562822 | `component::steam_online::entity::sensor::account::state::snooze` | Snooze | Snooze | Core-literal match |
| 15986 | 878562821 | `component::steam_online::entity::sensor::account::state::online` | Online | Online | Core-literal match |
| 15987 | 878562820 | `component::steam_online::entity::sensor::account::state::offline` | Offline | Offline | Core-literal match |
| 15988 | 878562819 | `component::steam_online::entity::sensor::account::state::looking_to_trade` | Looking to trade | Vill byta | Core-literal match |
| 15989 | 878562818 | `component::steam_online::entity::sensor::account::state::looking_to_play` | Looking to play | Vill spela | Core-literal match |
| 15990 | 878562817 | `component::steam_online::entity::sensor::account::state::busy` | Busy | Upptagen | Core-literal match |
| 15991 | 878562816 | `component::steam_online::entity::sensor::account::state::away` | Away | Borta | Core-literal match |
| 15992 | 878547215 | `component::wolflink::config::abort::no_devices` | No devices were found on this account. | Inga enheter hittades för det här kontot. | Core-literal match |
| 15993 | 878518387 | `component::icloud::config::step::verification_code::data::request_new_code` | Request a new verification code | Begär en ny verifieringskod | Core-literal match |
| 15994 | 878518307 | `component::unifiprotect::issues::package_binary_sensor_removed::title` | Package binary sensor removed | Binära paketsensor har tagits bort | Core-literal match |
| 15995 | 878518306 | `component::unifiprotect::issues::package_binary_sensor_removed::description` | The binary sensor `{entity_id}` for package detection has been removed. Package detection is a momentary smart-detect event, so it is now provided by the package event entity instead.<br><br>Update the following automations and scripts:<br>{items} | Den binära sensorn `{entity_id}` för paketdetektering har tagits bort. Paketdetektering är en kortvarig smart-detect-händelse, så den hanteras nu av en entitet för pakethändelser istället.<br><br>Uppdatera följande automatiseringar och skript:<br>{items} | Core-literal match |
| 15996 | 878518305 | `component::unifiprotect::entity::event::package::state_attributes::event_type::state::detected` | Detected | Detekterad | Core-literal match |
| 15997 | 878518304 | `component::unifiprotect::entity::event::package::name` | Package | Paket | Core-literal match |
| 15998 | 878514870 | `component::hr_energy_qube::entity::select::sg_ready_mode::state::plus` | Plus | Plus | Core-literal match |
| 15999 | 878514869 | `component::hr_energy_qube::entity::select::sg_ready_mode::state::off` | Off | Av | Shared reference target checked |
| 16000 | 878514868 | `component::hr_energy_qube::entity::select::sg_ready_mode::state::max` | Max | Max | Core-literal match |
| 16001 | 878514867 | `component::hr_energy_qube::entity::select::sg_ready_mode::state::block` | Block | Blockera | Core-literal match |
| 16002 | 878514866 | `component::hr_energy_qube::entity::select::sg_ready_mode::name` | Smart grid ready mode | Läge för smart elnät | Core-literal match |
| 16003 | 878508024 | `component::wattwaechter::config::step::reauth_confirm::title` | Re-authenticate WattWächter | Återautentisera WattWächter Plus | Core-literal match |
| 16004 | 878508023 | `component::wattwaechter::config::step::reauth_confirm::description` | The API token for {host} is no longer valid. Enter a new token to reconnect. | API-token för {host} är inte längre giltig. Ange en ny token för att återansluta. | Core-literal match |
| 16005 | 878508022 | `component::wattwaechter::config::step::reauth_confirm::data_description::token` | The API token for your WattWächter device. | API-token för din WattWächter Plus-enhet. | Shared reference target checked |
| 16006 | 878508021 | `component::wattwaechter::config::step::reauth_confirm::data::token` | API token | API-token | Shared reference target checked |
| 16007 | 878508020 | `component::wattwaechter::config::abort::wrong_device` | The device does not match the original WattWächter device. | Enheten matchar inte den ursprungliga WattWächter Plus-enheten. | Core-literal match |
| 16008 | 878508019 | `component::wattwaechter::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 16009 | 878507939 | `component::litterrobot::exceptions::update_failed::message` | Unable to update {entity_id} | Det gick inte att uppdatera {entity_id} | Core-literal match |
| 16010 | 878507938 | `component::litterrobot::entity::time::sleep_mode_start_time_wednesday::name` | Wednesday sleep mode start time | Sömnläge onsdag starttid | Core-literal match |
| 16011 | 878507937 | `component::litterrobot::entity::time::sleep_mode_start_time_tuesday::name` | Tuesday sleep mode start time | Sömnläge tisdag starttid | Core-literal match |
| 16012 | 878507936 | `component::litterrobot::entity::time::sleep_mode_start_time_thursday::name` | Thursday sleep mode start time | Sömnläge torsdag starttid | Core-literal match |
| 16013 | 878507935 | `component::litterrobot::entity::time::sleep_mode_start_time_sunday::name` | Sunday sleep mode start time | Sömnläge söndag starttid | Core-literal match |
| 16014 | 878507934 | `component::litterrobot::entity::time::sleep_mode_start_time_saturday::name` | Saturday sleep mode start time | Sömnläge lördag starttid | Core-literal match |
| 16015 | 878507933 | `component::litterrobot::entity::time::sleep_mode_start_time_monday::name` | Monday sleep mode start time | Sömnläge måndag starttid | Core-literal match |
| 16016 | 878507932 | `component::litterrobot::entity::time::sleep_mode_start_time_friday::name` | Friday sleep mode start time | Sömnläge fredag starttid | Core-literal match |
| 16017 | 878507931 | `component::litterrobot::entity::time::sleep_mode_end_time_wednesday::name` | Wednesday sleep mode end time | Sömnläge onsdag sluttid | Core-literal match |
| 16018 | 878507930 | `component::litterrobot::entity::time::sleep_mode_end_time_tuesday::name` | Tuesday sleep mode end time | Sömnläge tisdag sluttid | Core-literal match |
| 16019 | 878507929 | `component::litterrobot::entity::time::sleep_mode_end_time_thursday::name` | Thursday sleep mode end time | Sömnläge torsdag sluttid | Core-literal match |
| 16020 | 878507928 | `component::litterrobot::entity::time::sleep_mode_end_time_sunday::name` | Sunday sleep mode end time | Sömnläge söndag sluttid | Core-literal match |
| 16021 | 878507927 | `component::litterrobot::entity::time::sleep_mode_end_time_saturday::name` | Saturday sleep mode end time | Sömnläge lördag sluttid | Core-literal match |
| 16022 | 878507926 | `component::litterrobot::entity::time::sleep_mode_end_time_monday::name` | Monday sleep mode end time | Sömnläge måndag sluttid | Core-literal match |
| 16023 | 878507925 | `component::litterrobot::entity::time::sleep_mode_end_time_friday::name` | Friday sleep mode end time | Sömnläge fredag sluttid | Core-literal match |
| 16024 | 878507924 | `component::litterrobot::entity::switch::sleep_mode_wednesday::name` | Wednesday sleep mode | Sömnläge onsdag | Core-literal match |
| 16025 | 878507923 | `component::litterrobot::entity::switch::sleep_mode_tuesday::name` | Tuesday sleep mode | Sömnläge tisdag | Core-literal match |
| 16026 | 878507922 | `component::litterrobot::entity::switch::sleep_mode_thursday::name` | Thursday sleep mode | Sömnläge torsdag | Core-literal match |
| 16027 | 878507921 | `component::litterrobot::entity::switch::sleep_mode_sunday::name` | Sunday sleep mode | Sömnläge söndag | Core-literal match |
| 16028 | 878507920 | `component::litterrobot::entity::switch::sleep_mode_saturday::name` | Saturday sleep mode | Sömnläge lördag | Core-literal match |
| 16029 | 878507919 | `component::litterrobot::entity::switch::sleep_mode_monday::name` | Monday sleep mode | Sömnläge måndag | Core-literal match |
| 16030 | 878507918 | `component::litterrobot::entity::switch::sleep_mode_friday::name` | Friday sleep mode | Sömnläge fredag | Core-literal match |
| 16031 | 878507216 | `component::renault::entity::sensor::charge_state::state::v2l_connected` | Vehicle to load connected | Vehicle to load anslutet | Core-literal match |
| 16032 | 878507215 | `component::renault::entity::sensor::charge_state::state::v2g_discharging` | Vehicle to grid discharging | Vehicle to grid-urladdning | Core-literal match |
| 16033 | 878507214 | `component::renault::entity::sensor::charge_state::state::v2g_charging_waiting` | Vehicle to grid charging waiting | Vehicle to grid-laddning väntar | Core-literal match |
| 16034 | 878507213 | `component::renault::entity::sensor::charge_state::state::v2g_charging_normal` | Vehicle to grid charging | Vehicle to grid-laddning | Core-literal match |
| 16035 | 878500764 | `component::vacuum::triggers::returned_to_dock::name` | Vacuum cleaner returned to dock | Dammsugaren återvände till dockan | Core-literal match |
| 16036 | 878500763 | `component::vacuum::triggers::returned_to_dock::fields::for::name` | For at least | I minst | Shared reference target checked |
| 16037 | 878500762 | `component::vacuum::triggers::returned_to_dock::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 16038 | 878500761 | `component::vacuum::triggers::returned_to_dock::description` | Triggers when one or more vacuum cleaners have returned to dock. | Utlöses när en eller fler dammsugare har återvänt till dockan. | Core-literal match |
| 16039 | 878500760 | `component::update::triggers::became_available::name` | Update became available | Uppdatering blev tillgänglig | Core-literal match |
| 16040 | 878500759 | `component::update::triggers::became_available::fields::for::name` | For at least | I minst | Shared reference target checked |
| 16041 | 878500758 | `component::update::triggers::became_available::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 16042 | 878500757 | `component::update::triggers::became_available::description` | Triggers when one or more updates become available. | Utlöses när en eller flera uppdateringar blir tillgängliga. | Core-literal match |
| 16043 | 878500756 | `component::timer::triggers::remaining_time_reached::name` | Timer remaining time reached | Timer återstående tid uppnådd | Core-literal match |
| 16044 | 878500755 | `component::timer::triggers::remaining_time_reached::fields::remaining::name` | Time remaining | Återstående tid | Core-literal match |
| 16045 | 878500754 | `component::timer::triggers::remaining_time_reached::description` | Triggers when one or more timers reach a specific remaining time. | Utlöses när en eller fler timers når en specifik kvarvarande tid. | Core-literal match |
| 16046 | 878500753 | `component::schedule::triggers::block_started::name` | Schedule block started | Schemablock startat | Core-literal match |
| 16047 | 878500752 | `component::schedule::triggers::block_started::fields::for::name` | For at least | I minst | Shared reference target checked |
| 16048 | 878500751 | `component::schedule::triggers::block_started::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 16049 | 878500750 | `component::schedule::triggers::block_started::description` | Triggers when one or more schedule blocks start. | Utlöses när ett eller flera schemablock börjar. | Core-literal match |
| 16050 | 878500749 | `component::schedule::triggers::block_ended::name` | Schedule block ended | Schemablock avslutat | Core-literal match |
| 16051 | 878500748 | `component::schedule::triggers::block_ended::fields::for::name` | For at least | I minst | Shared reference target checked |
| 16052 | 878500747 | `component::schedule::triggers::block_ended::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 16053 | 878500746 | `component::schedule::triggers::block_ended::description` | Triggers when one or more schedule blocks end. | Utlöses när ett eller flera schemablock slutar. | Core-literal match |
| 16054 | 878500745 | `component::lawn_mower::triggers::returned_to_dock::name` | Lawn mower returned to dock | Gräsklippare har återvänt till dockan | Core-literal match |
| 16055 | 878500744 | `component::lawn_mower::triggers::returned_to_dock::fields::for::name` | For at least | I minst | Shared reference target checked |
| 16056 | 878500743 | `component::lawn_mower::triggers::returned_to_dock::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 16057 | 878500742 | `component::lawn_mower::triggers::returned_to_dock::description` | Triggers when one or more lawn mowers have returned to dock. | Utlöses när en eller flera gräsklippare har återvänt till dockan. | Core-literal match |
| 16058 | 878500741 | `component::climate::conditions::is_target_temperature::name` | Thermostat target temperature | Termostatens måltemperatur | Core-literal match |
| 16059 | 878500740 | `component::climate::conditions::is_target_temperature::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 16060 | 878500739 | `component::climate::conditions::is_target_temperature::fields::for::name` | For at least | I minst | Shared reference target checked |
| 16061 | 878500738 | `component::climate::conditions::is_target_temperature::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 16062 | 878500737 | `component::climate::conditions::is_target_temperature::description` | Tests the temperature setpoint of one or more thermostats. | Testar börvärdet för temperaturen för en eller flera termostater. | Core-literal match |
| 16063 | 878500736 | `component::climate::conditions::is_target_humidity::name` | Thermostat target humidity | Termostatens målfuktighet | Core-literal match |
| 16064 | 878500735 | `component::climate::conditions::is_target_humidity::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 16065 | 878500734 | `component::climate::conditions::is_target_humidity::fields::for::name` | For at least | I minst | Shared reference target checked |
| 16066 | 878500733 | `component::climate::conditions::is_target_humidity::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 16067 | 878500732 | `component::climate::conditions::is_target_humidity::description` | Tests the humidity setpoint of one or more thermostats. | Testar börvärdet för luftfuktighet för en eller flera termostater. | Core-literal match |
| 16068 | 878500731 | `component::battery::triggers::no_longer_low::name` | Battery no longer low | Batterinivå är inte längre låg | Core-literal match |
| 16069 | 878500730 | `component::battery::triggers::no_longer_low::fields::for::name` | For at least | I minst | Shared reference target checked |
| 16070 | 878500729 | `component::battery::triggers::no_longer_low::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 16071 | 878500728 | `component::battery::triggers::no_longer_low::description` | Triggers when one or more batteries are no longer low. | Utlöses när en eller flera batterinivåer inte längre är låga. | Core-literal match |
| 16072 | 878500727 | `component::battery::triggers::became_low::name` | Battery became low | Batterinivå blev låg | Core-literal match |
| 16073 | 878500726 | `component::battery::triggers::became_low::fields::for::name` | For at least | I minst | Shared reference target checked |
| 16074 | 878500725 | `component::battery::triggers::became_low::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 16075 | 878500724 | `component::battery::triggers::became_low::description` | Triggers when one or more batteries become low. | Utlöses när en eller flera batterinivåer börjar bli låga. | Core-literal match |
| 16076 | 878435645 | `component::alexa_devices::entity::todo::todo::name` | To-do list | Att-göra-lista | Core-literal match |
| 16077 | 878435644 | `component::alexa_devices::entity::todo::shop::name` | Shopping list | Inköpslista | Core-literal match |
| 16078 | 878430087 | `component::synology_dsm::entity::select::fan_speed_mode::state::quiet` | Quiet mode | Tyst läge | Core-literal match |
| 16079 | 878430086 | `component::synology_dsm::entity::select::fan_speed_mode::state::full_speed` | Full-speed mode | Fullhastighetsläge | Core-literal match |
| 16080 | 878430085 | `component::synology_dsm::entity::select::fan_speed_mode::state::cool` | Cool mode | Kylningsläge | Core-literal match |

## Sparade referensrättningar

| Lokalise-nyckel-ID | Nyckel | Sparad svenska |
|---:|---|---|
| 878500762 | `component::vacuum::triggers::returned_to_dock::fields::behavior::name` | Utlös när |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 878563348 | `component::openevse::entity::button::restart::name` | Restart |
| 878508019 | `component::wattwaechter::config::abort::reauth_successful` | Re-authentication was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
