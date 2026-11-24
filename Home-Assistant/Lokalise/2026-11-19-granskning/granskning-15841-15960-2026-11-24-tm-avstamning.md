# Home Assistant Core – historisk avstämning 15841–15960

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 95 direkta källtexter matchar HA Core-källan; 23 referensanvändningar med 14 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 2 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Fyra sun-trigger-konsumenter uppdaterades till exakt samma svenska mål som sina gemensamma referenser, sparades i Lokalise och verifierades med API-readback. Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 15841 | 882116433 | `component::victron_ble::entity::sensor::output_current::name` | Output current | Utgångsström | Core-literal match |
| 15842 | 882116432 | `component::victron_ble::entity::sensor::input_current::name` | Input current | Ingångsström | Core-literal match |
| 15843 | 882116431 | `component::victron_ble::entity::sensor::ac_voltage::name` | AC voltage | AC-spänning | Core-literal match |
| 15844 | 882116430 | `component::victron_ble::entity::sensor::ac_apparent_power::name` | AC apparent power | AC-skenbar effekt | Core-literal match |
| 15845 | 882099266 | `component::stiebel_eltron::entity::climate::climate::state_attributes::preset_mode::state::water_heating` | Water heating | Vattenuppvärmning | Core-literal match |
| 15846 | 882099265 | `component::stiebel_eltron::entity::climate::climate::state_attributes::preset_mode::state::ready` | Ready | Redo | Core-literal match |
| 15847 | 882099264 | `component::stiebel_eltron::entity::climate::climate::state_attributes::preset_mode::state::program` | Program | Program | Core-literal match |
| 15848 | 882099263 | `component::stiebel_eltron::entity::climate::climate::state_attributes::preset_mode::state::manual` | Manual | Manuell | Core-literal match |
| 15849 | 882099262 | `component::stiebel_eltron::entity::climate::climate::state_attributes::preset_mode::state::emergency` | Emergency | Nödsituation | Core-literal match |
| 15850 | 882099261 | `component::stiebel_eltron::entity::climate::climate::state_attributes::preset_mode::state::auto` | Auto | Auto | Core-literal match |
| 15851 | 882094530 | `component::synology_dsm::entity::select::fan_speed_mode::state::low_power` | Low-Power mode | Lågströmsläge | Core-literal match |
| 15852 | 882046250 | `component::steam_online::config::step::reconfigure::title` | Reconfigure {name} | Konfigurera om {name} | Core-literal match |
| 15853 | 882046249 | `component::steam_online::config::step::reconfigure::description` | You can find your Steam Web API key [**here**]({api_key_url}). | Du hittar din Steam Web API-nyckel [**här**]({api_key_url}). | Core-literal match |
| 15854 | 882046248 | `component::steam_online::config::step::reconfigure::data_description::api_key` | Your Steam Web API key | Din Steam Web API-nyckel | Shared reference target checked |
| 15855 | 882046247 | `component::steam_online::config::step::reconfigure::data::api_key` | Web API key | Web API-nyckel | Shared reference target checked |
| 15856 | 882046246 | `component::steam_online::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 15857 | 882045237 | `component::indevolt::entity::sensor::remaining_discharging_time::name` | Remaining discharging time | Återstående urladdningstid | Core-literal match |
| 15858 | 882045236 | `component::indevolt::entity::sensor::remaining_charging_time::name` | Remaining charging time | Återstående laddningstid | Core-literal match |
| 15859 | 881922264 | `component::airthings_ble::entity::sensor::radon_longterm_level::state::poor` | Poor | Dålig | Shared reference target checked |
| 15860 | 881922263 | `component::airthings_ble::entity::sensor::radon_longterm_level::state::good` | Good | Bra | Shared reference target checked |
| 15861 | 881922262 | `component::airthings_ble::entity::sensor::radon_longterm_level::state::fair` | Fair | Tillräcklig | Shared reference target checked |
| 15862 | 881922261 | `component::airthings_ble::entity::sensor::radon_1day_level::state::poor` | Poor | Dålig | Core-literal match |
| 15863 | 881922260 | `component::airthings_ble::entity::sensor::radon_1day_level::state::good` | Good | Bra | Core-literal match |
| 15864 | 881922259 | `component::airthings_ble::entity::sensor::radon_1day_level::state::fair` | Fair | Tillräcklig | Core-literal match |
| 15865 | 881497763 | `component::xiaomi_miio::entity::select::ptc_level::name` | Auxiliary heat level | Nivå för extravärme | Core-literal match |
| 15866 | 881497762 | `component::xiaomi_miio::entity::select::led_brightness::name` | LED brightness | LED-ljusstyrka | Core-literal match |
| 15867 | 881497761 | `component::xiaomi_miio::entity::select::display_orientation::name` | Display orientation | Skärmorientering | Core-literal match |
| 15868 | 881497760 | `component::xiaomi_miio::entity::select::airpurifier_mode::name` | Mode | Läge | Core-literal match |
| 15869 | 880052482 | `component::renault::entity::sensor::charging_settings_mode::state::delegated` | Delegated | Delegerad | Core-literal match |
| 15870 | 880041084 | `component::dropbox::exceptions::missing_scopes::message` | The Dropbox integration requires additional permissions to function correctly. | Dropbox-integrationen kräver ytterligare behörigheter för att fungera korrekt. | Shared reference target checked |
| 15871 | 880041083 | `component::dropbox::exceptions::missing_refresh_token::message` | The Dropbox integration needs to re-authenticate your account. | Dropbox-integrationen behöver autentisera ditt konto på nytt. | Shared reference target checked |
| 15872 | 880041082 | `component::dropbox::config::step::reauth_permissions::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 15873 | 880041081 | `component::dropbox::config::step::reauth_permissions::description` | The Dropbox integration requires additional permissions to function correctly. | Dropbox-integrationen kräver ytterligare behörigheter för att fungera korrekt. | Core-literal match |
| 15874 | 879995191 | `component::zha::entity::select::switch_type_l2::name` | Switch type L2 | Brytartyp L2 | Core-literal match |
| 15875 | 879995190 | `component::zha::entity::select::switch_type_l1::name` | Switch type L1 | Brytartyp L1 | Core-literal match |
| 15876 | 879995189 | `component::zha::entity::select::switch_action_l2::name` | Switch action L2 | Brytaråtgärd L2 | Core-literal match |
| 15877 | 879995188 | `component::zha::entity::select::switch_action_l1::name` | Switch action L1 | Brytaråtgärd L1 | Core-literal match |
| 15878 | 879995187 | `component::zha::entity::button::reset_energy::name` | Reset energy | Återställ energi | Core-literal match |
| 15879 | 879913599 | `component::matter::issues::ipv6_disabled::title` | IPv6 is disabled but required by Matter | IPv6 krävs av Matter men är inaktiverat | Core-literal match |
| 15880 | 879913598 | `component::matter::issues::ipv6_disabled::description` | Matter relies on IPv6 to communicate with some devices, but IPv6 is disabled on all of your connected network interfaces. Locally connected Wi-Fi and Ethernet devices may still work, but features such as using an external Thread border router need IPv6 enabled. Select "Learn more" to open the network settings. | Matter använder IPv6 för att kommunicera med vissa enheter, men IPv6 är inaktiverat på alla dina anslutna nätverksgränssnitt. Lokalt anslutna Wi-Fi- och Ethernet-enheter kan fortfarande fungera, men vissa funktioner, till exempel användning av en extern Thread-gränsrouter, kräver att IPv6 är aktiverat. Välj ”Läs mer” för att öppna nätverksinställningarna. | Core-literal match |
| 15881 | 879912143 | `component::steam_online::config::step::reauth_confirm::data_description::api_key` | Your Steam Web API key | Din Steam Web API-nyckel | Shared reference target checked |
| 15882 | 879912142 | `component::steam_online::config::step::reauth_confirm::data::api_key` | Web API key | Web API-nyckel | Shared reference target checked |
| 15883 | 879873295 | `component::sun::selector::twilight_type::options::any` | Any | Något | Core-literal match |
| 15884 | 879873294 | `component::sun::conditions::is_up::name` | Sun is up | Solen är uppe | Core-literal match |
| 15885 | 879873293 | `component::sun::conditions::is_up::description` | Tests if the sun is up. | Testar om solen är uppe. | Core-literal match |
| 15886 | 879873292 | `component::sun::conditions::is_set::name` | Sun is set | Solen är nere | Core-literal match |
| 15887 | 879873291 | `component::sun::conditions::is_set::description` | Tests if the sun is set. | Testar om solen är nere. | Core-literal match |
| 15888 | 879873290 | `component::sun::conditions::is_night::name` | It is night | Det är natt | Core-literal match |
| 15889 | 879873289 | `component::sun::conditions::is_night::description` | Tests if it is night. | Testar om det är natt. | Core-literal match |
| 15890 | 879873288 | `component::sun::conditions::is_morning_twilight::name` | It is morning twilight | Det är gryning | Core-literal match |
| 15891 | 879873287 | `component::sun::conditions::is_morning_twilight::fields::type::name` | Twilight type | Typ av skymning/gryning | Shared reference target checked |
| 15892 | 879873286 | `component::sun::conditions::is_morning_twilight::fields::type::description` | The phase of twilight. | Fasen av skymning/gryning. | Shared reference target checked |
| 15893 | 879873285 | `component::sun::conditions::is_morning_twilight::description` | Tests if it is morning twilight, optionally of a specific type. | Testar om det är gryning, eventuellt av en specifik typ. | Core-literal match |
| 15894 | 879873284 | `component::sun::conditions::is_evening_twilight::name` | It is evening twilight | Det är skymning | Core-literal match |
| 15895 | 879873283 | `component::sun::conditions::is_evening_twilight::fields::type::name` | Twilight type | Typ av skymning/gryning | Shared reference target checked |
| 15896 | 879873282 | `component::sun::conditions::is_evening_twilight::fields::type::description` | The phase of twilight. | Fasen av skymning/gryning. | Shared reference target checked |
| 15897 | 879873281 | `component::sun::conditions::is_evening_twilight::description` | Tests if it is evening twilight, optionally of a specific type. | Testar om det är skymning, eventuellt av en specifik typ. | Core-literal match |
| 15898 | 879873280 | `component::sun::conditions::is_descending::name` | Sun is descending | Solen går ner | Core-literal match |
| 15899 | 879873279 | `component::sun::conditions::is_descending::description` | Tests if the sun is descending. | Testar om solen går ner. | Core-literal match |
| 15900 | 879873278 | `component::sun::conditions::is_ascending::name` | Sun is ascending | Solen går upp | Core-literal match |
| 15901 | 879873277 | `component::sun::conditions::is_ascending::description` | Tests if the sun is ascending. | Testar om solen går upp. | Core-literal match |
| 15902 | 879873276 | `component::sun::conditions::elevation::name` | Sun elevation | Solhöjd | Core-literal match |
| 15903 | 879873275 | `component::sun::conditions::elevation::fields::threshold::name` | Threshold type | Gränsvärdestyp | Shared reference target checked |
| 15904 | 879873274 | `component::sun::conditions::elevation::description` | Tests the sun's elevation against a threshold you set. | Testar solens höljd mot ett gränsvärde du sätter. | Core-literal match |
| 15905 | 879873273 | `component::sun::common::condition_threshold_name` | Threshold type | Gränsvärdestyp | Core-literal match |
| 15906 | 879518175 | `component::matter::exceptions::addon_not_running::message` | The Matter Server app is not running yet. | Matter Server-appen körs inte än. | Core-literal match |
| 15907 | 879518174 | `component::matter::exceptions::addon_not_ready::message` | The Matter Server app is not ready yet. | Matter Server-appen är inte klar än. | Core-literal match |
| 15908 | 879518173 | `component::matter::exceptions::addon_not_installed::message` | The Matter Server app is not installed yet. | Matter Server-appen är inte installerad än. | Core-literal match |
| 15909 | 879475751 | `component::aqvify::entity::sensor::level_from_top::name` | Level from top | Nivå från toppen | Core-literal match |
| 15910 | 879475750 | `component::aqvify::entity::sensor::level_from_sensor::name` | Level from sensor | Nivå från sensorn | Core-literal match |
| 15911 | 879475749 | `component::aqvify::entity::sensor::available_volume::name` | Available volume | Tillgänglig volym | Core-literal match |
| 15912 | 879350116 | `component::music_assistant::services::play_media::fields::username::name` | Username | Användarnamn | Core-literal match |
| 15913 | 879350115 | `component::music_assistant::services::play_media::fields::username::description` | Music Assistant username used for the play media request. This affects the playlog entry and takes the user's provider filters into account. Defaults to the Music Assistant user linked to the Home Assistant user making the request. If there is no linked user, the request runs as the default account. | Användarnamnet för Music Assistant som används för uppspelningsbegäran. Detta påverkar uppspelningsloggposten och tar även hänsyn till leverantörsfilter för ett medieobjekt, om de är konfigurerade. Standardvärdet är den Home Assistant-användare som gjorde begäran, förutsatt att användarnamnet matchar med en Music Assistant-användare. | Core-literal match |
| 15914 | 879350114 | `component::music_assistant::exceptions::invalid_username::message` | The username {username} does not exist on the Music Assistant server. | Användarnamnet {username} finns inte på Music Assistant-servern. | Core-literal match |
| 15915 | 879142030 | `component::duco::entity::sensor::filter_remaining::name` | Filter remaining | Återstående filterlivslängd | Core-literal match |
| 15916 | 879063758 | `component::sun::triggers::sunset::name` | Sunset | Solnedgång | Core-literal match |
| 15917 | 879063757 | `component::sun::triggers::sunset::description` | Triggers when the sun sets. | Utlöses när solen går ner. | Core-literal match |
| 15918 | 879063756 | `component::sun::triggers::sunrise::name` | Sunrise | Soluppgång | Core-literal match |
| 15919 | 879063755 | `component::sun::triggers::sunrise::description` | Triggers when the sun rises. | Utlöses när solen går upp. | Core-literal match |
| 15920 | 879063754 | `component::sun::triggers::solar_noon::name` | Solar noon | Sann middag | Core-literal match |
| 15921 | 879063753 | `component::sun::triggers::solar_noon::description` | Triggers when the sun reaches its highest point. | Utlöses när solen når sin högsta punkt. | Core-literal match |
| 15922 | 879063752 | `component::sun::triggers::solar_midnight::name` | Solar midnight | Sann midnatt | Core-literal match |
| 15923 | 879063751 | `component::sun::triggers::solar_midnight::description` | Triggers when the sun reaches its lowest point. | Utlöses när solen når sin lägsta punkt. | Core-literal match |
| 15924 | 879063750 | `component::sun::triggers::elevation_crossed_threshold::name` | Sun elevation crossed threshold | Solhöjd passerade tröskelvärde | Core-literal match |
| 15925 | 879063749 | `component::sun::triggers::elevation_crossed_threshold::fields::threshold::name` | Threshold type | Gränsvärdestyp | Shared reference target checked |
| 15926 | 879063748 | `component::sun::triggers::elevation_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 15927 | 879063747 | `component::sun::triggers::elevation_crossed_threshold::description` | Triggers when the sun's elevation crosses a threshold you set. | Utlöses när solens höjd passerar ett tröskelvärde du har angett. | Core-literal match |
| 15928 | 879063746 | `component::sun::triggers::elevation_changed::name` | Sun elevation changed | Solhöjd ändrades | Core-literal match |
| 15929 | 879063745 | `component::sun::triggers::elevation_changed::fields::threshold::name` | Threshold type | Gränsvärdestyp | Shared reference target checked |
| 15930 | 879063744 | `component::sun::triggers::elevation_changed::description` | Triggers whenever the sun's elevation changes, optionally limited to a threshold or range you set. | Utlöses när solens höjd ändras, valfritt begränsad till ett tröskelvärde eller intervall som du anger. | Core-literal match |
| 15931 | 879063743 | `component::sun::triggers::dusk::name` | Dusk | Skymning | Core-literal match |
| 15932 | 879063742 | `component::sun::triggers::dusk::fields::type::name` | Twilight type | Typ av skymning/gryning | Shared reference target checked |
| 15933 | 879063741 | `component::sun::triggers::dusk::fields::type::description` | The phase of twilight. | Fasen av skymning/gryning. | Shared reference target checked |
| 15934 | 879063740 | `component::sun::triggers::dusk::description` | Triggers at dusk, when civil, nautical, or astronomical twilight ends. | Utlöses vid skymning, när borgerlig, nautisk, eller astronomisk skymning slutar. | Core-literal match |
| 15935 | 879063739 | `component::sun::triggers::dawn::name` | Dawn | Gryning | Core-literal match |
| 15936 | 879063738 | `component::sun::triggers::dawn::fields::type::name` | Twilight type | Typ av skymning/gryning | Shared reference target checked |
| 15937 | 879063737 | `component::sun::triggers::dawn::fields::type::description` | The phase of twilight. | Fasen av skymning/gryning. | Shared reference target checked |
| 15938 | 879063736 | `component::sun::triggers::dawn::description` | Triggers at dawn, when civil, nautical, or astronomical twilight begins. | Utlöses vid gryning, när borgerlig, nautisk, eller astronomisk gryning börjar. | Core-literal match |
| 15939 | 879063735 | `component::sun::selector::twilight_type::options::nautical` | Nautical | Nautisk | Core-literal match |
| 15940 | 879063734 | `component::sun::selector::twilight_type::options::civil` | Civil | Borgerlig | Core-literal match |
| 15941 | 879063733 | `component::sun::selector::twilight_type::options::astronomical` | Astronomical | Astronomisk | Core-literal match |
| 15942 | 879063732 | `component::sun::common::twilight_type_name` | Twilight type | Typ av skymning/gryning | Core-literal match |
| 15943 | 879063731 | `component::sun::common::twilight_type_description` | The phase of twilight. | Fasen av skymning/gryning. | Core-literal match |
| 15944 | 879063730 | `component::sun::common::trigger_threshold_name` | Threshold type | Gränsvärdestyp | Core-literal match |
| 15945 | 879063729 | `component::sun::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 15946 | 878826008 | `component::alexa_devices::exceptions::select_option_not_found::message` | Selected option not found: {option} | Det valda alternativet hittades inte: {option} | Core-literal match |
| 15947 | 878826007 | `component::alexa_devices::entity::select::dropin::state::off` | Don't allow drop in | Tillåt inte drop-in | Core-literal match |
| 15948 | 878826006 | `component::alexa_devices::entity::select::dropin::state::home` | Allow drop in from household members | Tillåt drop-in från hushållsmedlemmar | Core-literal match |
| 15949 | 878826005 | `component::alexa_devices::entity::select::dropin::state::all` | Allow drop in from anyone | Tillåt drop-in från vem som helst | Core-literal match |
| 15950 | 878826004 | `component::alexa_devices::entity::select::dropin::name` | Drop In | Drop-in | Core-literal match |
| 15951 | 878564988 | `component::vistapool::config::step::reauth_confirm::title` | Reauthenticate Vistapool | Återautentisera Vistapool | Core-literal match |
| 15952 | 878564987 | `component::vistapool::config::step::reauth_confirm::description` | The stored password for {username} is no longer accepted by Vistapool. Enter the current password to restore the connection. | Det sparade lösenordet för {username} accepteras inte längre av Vistapool. Ange det aktuella lösenordet för att återupprätta anslutningen. | Core-literal match |
| 15953 | 878564986 | `component::vistapool::config::step::reauth_confirm::data_description::password` | The password for your Vistapool account. | Lösenordet för ditt Vistapool-konto. | Core-literal match |
| 15954 | 878564985 | `component::vistapool::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 15955 | 878564984 | `component::vistapool::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 15956 | 878564955 | `component::vistapool::entity::select::pump_speed::state::slow` | Slow | Långsam | Core-literal match |
| 15957 | 878564954 | `component::vistapool::entity::select::pump_speed::state::medium` | Medium | Medel | Core-literal match |
| 15958 | 878564953 | `component::vistapool::entity::select::pump_speed::state::high` | High | Hög | Core-literal match |
| 15959 | 878564952 | `component::vistapool::entity::select::pump_speed::name` | Pump speed | Pumphastighet | Core-literal match |
| 15960 | 878564951 | `component::vistapool::entity::select::pump_mode::state::smart` | Smart | Smart | Core-literal match |

## Sparade referensrättningar

| Lokalise-nyckel-ID | Nyckel | Sparad svenska |
|---:|---|---|
| 879063742 | `component::sun::triggers::dusk::fields::type::name` | Typ av skymning/gryning |
| 879063741 | `component::sun::triggers::dusk::fields::type::description` | Fasen av skymning/gryning. |
| 879063738 | `component::sun::triggers::dawn::fields::type::name` | Typ av skymning/gryning |
| 879063737 | `component::sun::triggers::dawn::fields::type::description` | Fasen av skymning/gryning. |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 882046246 | `component::steam_online::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 878564984 | `component::vistapool::config::abort::reauth_successful` | Re-authentication was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
