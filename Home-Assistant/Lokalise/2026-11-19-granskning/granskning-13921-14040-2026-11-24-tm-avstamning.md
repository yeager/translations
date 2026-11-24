# Home Assistant Core – historisk avstämning 13921–14040

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120 nycklar avstämda: 118 översättningsbara och 2 strukturposter utan engelsk källtext. 86 direkta källtexter matchar HA Core-källan; 29 referensanvändningar med 28 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 3 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Inga äldre radvisa språkförslag för dessa 120 nycklar.
- 118 översättningsbara poster synkades retroaktivt till HA Core TM. Två nycklar har tom engelsk källtext och motsvarar `data: {}` i källan; de är dokumenterade som strukturposter och har inte lagts i TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 13921 | 901279962 | `component::template::issues::composite_device_id::fix_flow::step::select_device::data_description::device_id` | The device this template helper should be linked to. | Den enhet som den här mallhjälparen ska länkas till. | Core-literal match |
| 13922 | 901279961 | `component::template::issues::composite_device_id::fix_flow::step::select_device::data::device_id` | Device | Enhet | Shared reference target checked |
| 13923 | 901279960 | `component::template::issues::composite_device_id::fix_flow::error::invalid_device` | The selected device no longer exists | Den valda enheten finns inte längre | Core-literal match |
| 13924 | 901279959 | `component::template::issues::composite_device_id::fix_flow::abort::entry_removed` | The template helper has been removed | Mallhjälparen har tagits bort | Core-literal match |
| 13925 | 901085990 | `component::aidot::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 13926 | 901085939 | `component::slack::exceptions::invalid_message_data::message` | Invalid message data: {error} | Ogiltig meddelandedata: {error} | Core-literal match |
| 13927 | 901063562 | `component::reolink::entity::switch::privacy_mask_lens::name` | Privacy mask lens {channel} | Sekretessmasklins {channel} | Core-literal match |
| 13928 | 901047917 | `component::wiim::config::step::reconfigure::data_description::host` | The hostname or IP address of the WiiM device. | Värdnamn eller IP-adress för WiiM-enheten. | Core-literal match |
| 13929 | 901047916 | `component::wiim::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 13930 | 901047915 | `component::wiim::config::abort::unique_id_mismatch` | The host belongs to a different WiiM device. | Värden tillhör en annan WiiM-enhet. | Core-literal match |
| 13931 | 901047914 | `component::wiim::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 13932 | 900733335 | `component::dropbox::exceptions::cannot_connect::message` | Error communicating with Dropbox | Fel vid kommunikationen med Dropbox. | Core-literal match |
| 13933 | 900733334 | `component::dropbox::exceptions::authentication_failed::message` | Authentication with Dropbox failed | Autentisering med Dropbox misslyckades | Core-literal match |
| 13934 | 900733279 | `component::dropbox::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 13935 | 900550371 | `component::izone::exceptions::update_failed::message` | Error communicating with iZone controller: {error} | Fel vid kommunikation med i Zon kontrollen: {error} | Core-literal match |
| 13936 | 900550370 | `component::izone::exceptions::setup_rejected::message` | iZone controller at {host} rejected setup | iZone-kontrollen på {host} avvisade konfigurationen | Core-literal match |
| 13937 | 900550369 | `component::izone::exceptions::refresh_rejected::message` | iZone controller rejected refresh: {error} | i Zon kontrollen avvisade uppdatering: {error} | Core-literal match |
| 13938 | 900550368 | `component::izone::exceptions::no_eligible_controller::message` | No eligible iZone controller found to bind to legacy config entry | Ingen behörig i Zon kontroller hittades för att binda till äldre konfigurationsposter. | Core-literal match |
| 13939 | 900550367 | `component::izone::exceptions::multiple_eligible_controllers::message` | Multiple eligible iZone controllers found for a legacy config entry; delete this entry and re-add each controller individually | Flera kvalificerade i Zon kontroller hittades för en äldre konfigurationspost; ta bort den här posten och lägg till varje kontroller individuellt igen. | Core-literal match |
| 13940 | 900550366 | `component::izone::exceptions::missing_unique_id::message` | iZone config entry is missing unique_id | i Zon konfigurationsposten saknar unikt_id | Core-literal match |
| 13941 | 900550365 | `component::izone::exceptions::missing_host::message` | iZone config entry is missing host | i Zon konfigurationsposten saknar värd | Core-literal match |
| 13942 | 900550364 | `component::izone::exceptions::discovery_start_failed::message` | iZone discovery service failed to start | i Zon identifieringstjänsten kunde inte startas | Core-literal match |
| 13943 | 900550363 | `component::izone::exceptions::discovery_failed_legacy::message` | iZone discovery failed while resolving legacy config entry | i Zon identifiering misslyckades vid lösning av äldre konfigurationsposter | Core-literal match |
| 13944 | 900550362 | `component::izone::exceptions::discovery_failed_host::message` | iZone discovery failed while resolving config entry host | i Zon identifieringen misslyckades vid lösning av konfigurationspost värden | Core-literal match |
| 13945 | 900550361 | `component::izone::exceptions::controller_not_found::message` | No iZone controller found for unique_id {uid} | Ingen i Zon kontroller hittades för unikt_id {uid} | Core-literal match |
| 13946 | 900550360 | `component::izone::exceptions::cannot_connect::message` | Unable to connect to iZone controller at {host} | Det går inte att ansluta till iZone-kontrollen på {host} | Core-literal match |
| 13947 | 900550359 | `component::izone::exceptions::bridge_unpaired::message` | iZone Smart Hub is not paired with an air conditioner | i Zon bryggan är inte parad med en luftkonditionering | Core-literal match |
| 13948 | 900413159 | `component::monzo::config::step::connection_error::title` | Connection error | Anslutningsfel | Core-literal match |
| 13949 | 900413158 | `component::monzo::config::step::connection_error::description` | Home Assistant could not check whether access was approved. Check your internet connection and try again. | Home Assistant kunde inte kontrollera om åtkomsten var godkänd. Kontrollera din internetanslutning och försök igen. | Core-literal match |
| 13951 | 900413156 | `component::monzo::config::step::approval_timeout::title` | Approval timed out | Godkännandet har gått ut | Core-literal match |
| 13952 | 900413155 | `component::monzo::config::step::approval_timeout::description` | Approval was not received from Monzo. Approve the request in the Monzo app, then try again. | Godkännande mottogs inte från Monzo. Godkänn begäran i Monzo appen och försök sedan igen. | Core-literal match |
| 13954 | 900413153 | `component::monzo::config::progress::wait_for_approval` | Open the Monzo app and approve the request from Home Assistant. Setup will continue automatically once access is approved. | Öppna Monzo appen och godkänn begäran från Home Assistant. Installationen fortsätter automatiskt när åtkomsten har godkänts. | Core-literal match |
| 13955 | 900408472 | `component::melcloud::exceptions::set_number_failed::message` | Failed to send the value to the device. | Det gick inte att skicka värdet till enheten. | Core-literal match |
| 13956 | 900408471 | `component::melcloud::entity::number::flow_temperature::name` | Flow temperature | Flödestemperatur | Core-literal match |
| 13957 | 900360701 | `component::led_infrared::entity::button::timer::name` | Timer | Timer | Shared reference target checked |
| 13958 | 900360700 | `component::led_infrared::entity::button::brightness_up::name` | Brightness up | Ljusstyrka upp | Shared reference target checked |
| 13959 | 900360699 | `component::led_infrared::entity::button::brightness_down::name` | Brightness down | Ljusstyrka ner | Shared reference target checked |
| 13960 | 900357867 | `component::russound_rio::options::step::init::data_description::zone_source_exclusion` | When enabled, Home Assistant hides sources that are disabled for a zone from the source list for that zone. | När Home Assistant är aktiverat döljer den källor som är inaktiverade för en zon från källistan för den zonen. | Core-literal match |
| 13961 | 900357866 | `component::russound_rio::options::step::init::data::zone_source_exclusion` | Zone source exclusion | Undantag från zonkällor | Core-literal match |
| 13962 | 900354827 | `component::led_infrared::selector::device_type::options::generic_44_key` | 44-key remote control | Fjärrkontroll med 44 knappar | Core-literal match |
| 13963 | 900354826 | `component::led_infrared::selector::device_type::options::generic_40_key` | 40-key remote control | Fjärrkontroll med 40 knappar | Core-literal match |
| 13964 | 900354825 | `component::led_infrared::entity::light::light::state_attributes::effect::state::yellowish` | Color: Yellowish | Färg: Gulaktig | Core-literal match |
| 13965 | 900354824 | `component::led_infrared::entity::light::light::state_attributes::effect::state::pink` | Color: Pink | Färg: Rosa | Core-literal match |
| 13966 | 900354823 | `component::led_infrared::entity::light::light::state_attributes::effect::state::magenta` | Color: Magenta | Färg: Magenta | Core-literal match |
| 13967 | 900354822 | `component::led_infrared::entity::light::light::state_attributes::effect::state::light_cyan` | Color: Light Cyan | Färg: Ljus cyan | Core-literal match |
| 13968 | 900354821 | `component::led_infrared::entity::light::light::state_attributes::effect::state::lavender_blush` | Color: Lavender Blush | Färg: Lavendel Blush | Core-literal match |
| 13969 | 900354820 | `component::led_infrared::entity::light::light::state_attributes::effect::state::jump7` | Jump 7 | Hoppa 7 | Core-literal match |
| 13970 | 900354819 | `component::led_infrared::entity::light::light::state_attributes::effect::state::jump3` | Jump 3 | Hoppa 3 | Core-literal match |
| 13971 | 900354818 | `component::led_infrared::entity::light::light::state_attributes::effect::state::ghost_white` | Color: Ghost White | Färg: Spökvit | Core-literal match |
| 13972 | 900354817 | `component::led_infrared::entity::light::light::state_attributes::effect::state::floral_white` | Color: Floral White | Färg: Blommig vit | Core-literal match |
| 13973 | 900354816 | `component::led_infrared::entity::light::light::state_attributes::effect::state::fade7` | Fade 7 | Tona bort 7 | Core-literal match |
| 13974 | 900354815 | `component::led_infrared::entity::light::light::state_attributes::effect::state::fade3` | Fade 3 | Tona bort 3 | Core-literal match |
| 13975 | 900354814 | `component::led_infrared::entity::light::light::state_attributes::effect::state::diy6` | DIY 6 | Gör-det-själv 6 | Core-literal match |
| 13976 | 900354813 | `component::led_infrared::entity::light::light::state_attributes::effect::state::diy5` | DIY 5 | Gör-det-själv 5 | Core-literal match |
| 13977 | 900354812 | `component::led_infrared::entity::light::light::state_attributes::effect::state::diy4` | DIY 4 | Gör-det-själv 4 | Core-literal match |
| 13978 | 900354811 | `component::led_infrared::entity::light::light::state_attributes::effect::state::diy3` | DIY 3 | Gör-det-själv 3 | Core-literal match |
| 13979 | 900354810 | `component::led_infrared::entity::light::light::state_attributes::effect::state::diy2` | DIY 2 | Gör-det-själv 2 | Core-literal match |
| 13980 | 900354809 | `component::led_infrared::entity::light::light::state_attributes::effect::state::diy1` | DIY 1 | Gör-det-själv 1 | Core-literal match |
| 13981 | 900354808 | `component::led_infrared::entity::light::light::state_attributes::effect::state::deep_blue` | Color: Deep Blue | Färg: Djupblå | Core-literal match |
| 13982 | 900354807 | `component::led_infrared::entity::light::light::state_attributes::effect::state::auto` | Auto | Auto | Shared reference target checked |
| 13983 | 900354806 | `component::led_infrared::entity::light::light::state_attributes::effect::state::aqua` | Color: Aqua | Färg: Aqua | Core-literal match |
| 13984 | 900354805 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::yellowish` | Color: Yellowish | Färg: Gulaktig | Shared reference target checked |
| 13985 | 900354804 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::white_on` | White on | Vitt på | Core-literal match |
| 13986 | 900354803 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::white_off` | White off | Vit av | Core-literal match |
| 13987 | 900354802 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::white_brightness_up` | White brightness up | Vit ljusstyrka öka | Core-literal match |
| 13988 | 900354801 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::white_brightness_down` | White brightness down | Vit ljusstyrka minska | Core-literal match |
| 13989 | 900354800 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::white_brightness_75` | White brightness 75% | Vit ljusstyrka 75 % | Core-literal match |
| 13990 | 900354799 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::white_brightness_50` | White brightness 50% | Vit ljusstyrka 50 % | Core-literal match |
| 13991 | 900354798 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::white_brightness_25` | White brightness 25% | Vit ljusstyrka 25 % | Core-literal match |
| 13992 | 900354797 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::white_brightness_100` | White brightness 100% | Vit ljusstyrka 100 % | Core-literal match |
| 13993 | 900354796 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::slow` | Slow | Långsam | Core-literal match |
| 13994 | 900354795 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::red_up` | Red up | Röd upp | Core-literal match |
| 13995 | 900354794 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::red_down` | Red down | Röd ner | Core-literal match |
| 13996 | 900354793 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::quick` | Quick | Snabb | Core-literal match |
| 13997 | 900354792 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::pink` | Color: Pink | Färg: Rosa | Shared reference target checked |
| 13998 | 900354791 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::magenta` | Color: Magenta | Färg: Magenta | Shared reference target checked |
| 13999 | 900354790 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::light_cyan` | Color: Light Cyan | Färg: Ljus cyan | Shared reference target checked |
| 14000 | 900354789 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::lavender_blush` | Color: Lavender Blush | Färg: Lavendel Blush | Shared reference target checked |
| 14001 | 900354788 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::jump7` | Jump 7 | Hoppa 7 | Shared reference target checked |
| 14002 | 900354787 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::jump3` | Jump 3 | Hoppa 3 | Shared reference target checked |
| 14003 | 900354786 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::green_up` | Green up | Grön upp | Core-literal match |
| 14004 | 900354785 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::green_down` | Green down | Grön ner | Core-literal match |
| 14005 | 900354784 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::ghost_white` | Color: Ghost White | Färg: Spökvit | Shared reference target checked |
| 14006 | 900354783 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::floral_white` | Color: Floral White | Färg: Blommig vit | Shared reference target checked |
| 14007 | 900354782 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::fade7` | Fade 7 | Tona bort 7 | Shared reference target checked |
| 14008 | 900354781 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::fade3` | Fade 3 | Tona bort 3 | Shared reference target checked |
| 14009 | 900354780 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::diy6` | DIY 6 | Gör-det-själv 6 | Shared reference target checked |
| 14010 | 900354779 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::diy5` | DIY 5 | Gör-det-själv 5 | Shared reference target checked |
| 14011 | 900354778 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::diy4` | DIY 4 | Gör-det-själv 4 | Shared reference target checked |
| 14012 | 900354777 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::diy3` | DIY 3 | Gör-det-själv 3 | Shared reference target checked |
| 14013 | 900354776 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::diy2` | DIY 2 | Gör-det-själv 2 | Shared reference target checked |
| 14014 | 900354775 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::diy1` | DIY 1 | Gör-det-själv 1 | Shared reference target checked |
| 14015 | 900354774 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::deep_blue` | Color: Deep Blue | Färg: Djupblå | Shared reference target checked |
| 14016 | 900354773 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::blue_up` | Blue up | Blå upp | Core-literal match |
| 14017 | 900354772 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::blue_down` | Blue down | Blå ner | Core-literal match |
| 14018 | 900354771 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::auto` | Auto | Auto | Shared reference target checked |
| 14019 | 900354770 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::aqua` | Color: Aqua | Färg: Aqua | Shared reference target checked |
| 14020 | 900348998 | `component::yeelight::exceptions::set_music_mode_failed::message` | Unable to set music mode for {name}: {error}. Consider disabling the music mode option. | Det gick inte att ställa in musikläge för {name}: {error}. Överväg att inaktivera musikläge. | Core-literal match |
| 14021 | 900325963 | `component::enphase_envoy::entity::sensor::acb_battery_soc::name` | State of charge | Laddningstillstånd | Core-literal match |
| 14022 | 900325962 | `component::enphase_envoy::entity::sensor::acb_battery_sleep_state::state::waking` | Waking | Vaknar | Core-literal match |
| 14023 | 900325961 | `component::enphase_envoy::entity::sensor::acb_battery_sleep_state::state::going_to_sleep` | Going to sleep | Somnar | Core-literal match |
| 14024 | 900325960 | `component::enphase_envoy::entity::sensor::acb_battery_sleep_state::state::awake` | Awake | Vaken | Core-literal match |
| 14025 | 900325959 | `component::enphase_envoy::entity::sensor::acb_battery_sleep_state::state::asleep` | Asleep | Sover | Core-literal match |
| 14026 | 900325958 | `component::enphase_envoy::entity::sensor::acb_battery_sleep_state::name` | Sleep state | Sömnläge | Core-literal match |
| 14027 | 900325957 | `component::enphase_envoy::entity::sensor::acb_battery_sleep_soc_target::name` | Sleep SOC target | Sömn SOC-mål | Core-literal match |
| 14028 | 900325956 | `component::enphase_envoy::entity::sensor::acb_battery_charge_status::state::idle` | Idle | Inaktiv | Shared reference target checked |
| 14029 | 900325955 | `component::enphase_envoy::entity::sensor::acb_battery_charge_status::state::discharging` | Discharging | Laddar ur | Shared reference target checked |
| 14030 | 900325954 | `component::enphase_envoy::entity::sensor::acb_battery_charge_status::state::charging` | Charging | Laddar | Shared reference target checked |
| 14031 | 900325953 | `component::enphase_envoy::entity::sensor::acb_battery_charge_status::name` | Charge status | Laddningsstatus | Core-literal match |
| 14032 | 900325952 | `component::enphase_envoy::entity::sensor::acb_aggregate_sleep_state::state::waking` | Waking | Vaknar | Core-literal match |
| 14033 | 900325951 | `component::enphase_envoy::entity::sensor::acb_aggregate_sleep_state::state::mixed` | Mixed | Blandad | Core-literal match |
| 14034 | 900325950 | `component::enphase_envoy::entity::sensor::acb_aggregate_sleep_state::state::going_to_sleep` | Going to sleep | Somnar | Core-literal match |
| 14035 | 900325949 | `component::enphase_envoy::entity::sensor::acb_aggregate_sleep_state::state::awake` | Awake | Vaken | Core-literal match |
| 14036 | 900325948 | `component::enphase_envoy::entity::sensor::acb_aggregate_sleep_state::state::asleep` | Asleep | Sover | Core-literal match |
| 14037 | 900325947 | `component::enphase_envoy::entity::sensor::acb_aggregate_sleep_state::name` | Sleep state | Sömnläge | Core-literal match |
| 14038 | 900325946 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::95-100` | 95 - 100% | 95 - 100% | Core-literal match |
| 14039 | 900325945 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::90-95` | 90 - 95% | 90 - 95% | Core-literal match |
| 14040 | 900325944 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::85-90` | 85 - 90% | 85 - 90% | Core-literal match |

## Inte översättningsbara strukturposter

| Lokalise-nyckel-ID | Nyckel | Orsak |
|---:|---|---|
| 900413157 | `component::monzo::config::step::connection_error::data` | Tom engelsk källtext; motsvarande `data: {}` i HA Core |
| 900413154 | `component::monzo::config::step::approval_timeout::data` | Tom engelsk källtext; motsvarande `data: {}` i HA Core |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 901085990 | `component::aidot::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |
| 901047914 | `component::wiim::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 900733279 | `component::dropbox::config::abort::reconfigure_successful` | Reconfiguration was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
