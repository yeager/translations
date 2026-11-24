# Home Assistant Core – historisk avstämning 17641–17760

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 88 direkta källtexter matchar HA Core-källan; 32 referensanvändningar med 17 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 0 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 17641 | 860335671 | `component::ouman_eh_800::entity::select::home_away_mode::state::home` | Home | Hemma | Shared reference target checked |
| 17642 | 860335670 | `component::ouman_eh_800::entity::select::home_away_mode::state::away` | Away | Borta | Shared reference target checked |
| 17643 | 860335669 | `component::ouman_eh_800::entity::select::home_away_mode::name` | Home/Away mode | Hemma/Borta-läge | Core-literal match |
| 17644 | 860312753 | `component::homewizard::issues::battery_mode_cloud_disabled::title` | Enable cloud connection for smart charging strategy | Aktivera molnanslutning för smart laddningsstrategi | Core-literal match |
| 17645 | 860312752 | `component::homewizard::issues::battery_mode_cloud_disabled::fix_flow::step::confirm::title` | Enable cloud connection for smart charging strategy | Aktivera molnanslutning för smart laddningsstrategi | Shared reference target checked |
| 17646 | 860312751 | `component::homewizard::issues::battery_mode_cloud_disabled::fix_flow::step::confirm::description` | Smart charging strategy is enabled for your battery group, but cloud connection is disabled. These settings are not compatible, as smart charging requires cloud connectivity.<br><br>Select **Submit** to enable cloud connection. | Funktionen för smart laddning är aktiverad för din batterigrupp, men molnanslutningen är inaktiverad. Dessa inställningar är inte kompatibla, eftersom smart laddning kräver molnanslutning.<br><br>Välj **Bekräfta** för att aktivera molnanslutningen. | Core-literal match |
| 17647 | 860312750 | `component::homewizard::issues::battery_mode_cloud_disabled::fix_flow::error::network_error` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 17648 | 860293743 | `component::ouman_eh_800::entity::number::water_out_minimum_temperature::name` | Water out minimum temperature | Lägsta temperatur för utgående vatten | Core-literal match |
| 17649 | 860293742 | `component::ouman_eh_800::entity::number::water_out_maximum_temperature::name` | Water out maximum temperature | Högsta temperatur för utgående vatten | Core-literal match |
| 17650 | 860293741 | `component::ouman_eh_800::entity::number::trend_sampling_interval::name` | Trend sampling interval | Trendprovtagningsintervall | Core-literal match |
| 17651 | 860293740 | `component::ouman_eh_800::entity::number::temperature_drop::name` | Temperature drop | Temperaturfall | Core-literal match |
| 17652 | 860293739 | `component::ouman_eh_800::entity::number::room_temperature_fine_tuning::name` | Room temperature fine tuning | Finjustering av rumstemperaturen | Core-literal match |
| 17653 | 860293738 | `component::ouman_eh_800::entity::number::curve_minus_20_temperature::name` | Curve -20°C temperature | Kurva -20°C temperatur | Core-literal match |
| 17654 | 860293737 | `component::ouman_eh_800::entity::number::curve_minus_10_temperature::name` | Curve -10°C temperature | Kurva -10°C temperatur | Core-literal match |
| 17655 | 860293736 | `component::ouman_eh_800::entity::number::curve_20_temperature::name` | Curve 20°C temperature | Kurva 20°C temperatur | Core-literal match |
| 17656 | 860293735 | `component::ouman_eh_800::entity::number::curve_10_temperature::name` | Curve 10°C temperature | Kurva 10°C temperatur | Core-literal match |
| 17657 | 860293734 | `component::ouman_eh_800::entity::number::curve_0_temperature::name` | Curve 0°C temperature | Kurva 0°C temperatur | Core-literal match |
| 17658 | 860293733 | `component::ouman_eh_800::entity::number::constant_temp_setpoint::name` | Constant temperature setpoint | Konstant temperaturbörvärde | Core-literal match |
| 17659 | 860293732 | `component::ouman_eh_800::entity::number::big_temperature_drop::name` | Big temperature drop | Stort temperaturfall | Core-literal match |
| 17660 | 860287030 | `component::youtube::entity::sensor::videos::name` | Videos | Videor | Core-literal match |
| 17661 | 860287029 | `component::mqtt::selector::platform::options::time` | Time | Tid | Shared reference target checked |
| 17662 | 860287028 | `component::mqtt::selector::platform::options::datetime` | Date/Time | Datum/tid | Shared reference target checked |
| 17663 | 860287027 | `component::mqtt::selector::platform::options::date` | Date | Datum | Shared reference target checked |
| 17664 | 860287026 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::data_description::timezone` | Set to a valid [IANA time zone identifier]({tz_abbr_url}). Do not set this option if the date/time structure is providing time zone information via the status update. | Ställ in en giltig [IANA-tidszonskod]({tz_abbr_url}). Ställ inte in detta alternativ om datum- och tidsstrukturen tillhandahåller tidszonsinformation via statusuppdateringen. | Core-literal match |
| 17665 | 860287025 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::data::timezone` | Time zone | Tidszon | Core-literal match |
| 17666 | 860287024 | `component::homewizard::entity::sensor::battery_group_power_w::name` | Battery group power | Effekt i batterigrupp | Core-literal match |
| 17667 | 860130582 | `component::ouman_eh_800::entity::valve::valve_position_setpoint::name` | Valve position setpoint | Ventilens börvärde | Core-literal match |
| 17668 | 860071296 | `component::homewizard::entity::sensor::battery_group_target_power_w::name` | Battery group target power | Måleffekt för batterigrupp | Core-literal match |
| 17669 | 859784954 | `component::miele::entity::sensor::program_phase::state::paused` | Paused | Pausad | Core-literal match |
| 17670 | 859784953 | `component::miele::entity::sensor::program_phase::state::cancelled` | Cancelled | Avbruten | Core-literal match |
| 17671 | 859784779 | `component::edl21::config::step::user::data_description::serial_port` | Serial port path to connect to | Sökväg till serieporten att anslutas till | Core-literal match |
| 17672 | 859601798 | `component::indevolt::entity::sensor::main_mos_temperature::name` | Main MOS temperature | Huvudsaklig MOS-temperatur | Core-literal match |
| 17673 | 859548008 | `component::axis::config::abort::no_serial_number` | Could not retrieve a serial number from the device. Please check device connectivity and try again. | Kunde inte hämta serienumret från enheten. Kontrollera enhetens anslutning och försök igen. | Core-literal match |
| 17674 | 859515119 | `component::homeassistant::exceptions::scene_config_reload_failed::message` | Failed to reload the Home Assistant scene platform configuration - {error} | Det gick inte att ladda om konfigurationen för Home Assistant-scenplattformen - {error} | Core-literal match |
| 17675 | 859515118 | `component::homeassistant::exceptions::core_config_reload_failed::message` | Failed to reload the Home Assistant Core configuration - {error} | Det gick inte att ladda om Home Assistant Core-konfigurationen - {error} | Core-literal match |
| 17676 | 859251970 | `component::lichess::entity::sensor::ultra_bullet_rating::name` | UltraBullet rating | UltraBullet-rating | Core-literal match |
| 17677 | 859251969 | `component::lichess::entity::sensor::ultra_bullet_games::unit_of_measurement` | games | spel | Shared reference target checked |
| 17678 | 859251968 | `component::lichess::entity::sensor::ultra_bullet_games::name` | UltraBullet games | UltraBullet-spel | Core-literal match |
| 17679 | 859251967 | `component::lichess::entity::sensor::three_check_rating::name` | Three-check rating | Tre-check-rating | Core-literal match |
| 17680 | 859251966 | `component::lichess::entity::sensor::three_check_games::unit_of_measurement` | games | spel | Shared reference target checked |
| 17681 | 859251965 | `component::lichess::entity::sensor::three_check_games::name` | Three-check games | Tre-check-spel | Core-literal match |
| 17682 | 859251964 | `component::lichess::entity::sensor::racing_kings_rating::name` | Racing Kings rating | Racing Kings-rating | Core-literal match |
| 17683 | 859251963 | `component::lichess::entity::sensor::racing_kings_games::unit_of_measurement` | games | spel | Shared reference target checked |
| 17684 | 859251962 | `component::lichess::entity::sensor::racing_kings_games::name` | Racing Kings games | Racing Kings-spel | Core-literal match |
| 17685 | 859251961 | `component::lichess::entity::sensor::king_of_the_hill_rating::name` | King of the Hill rating | King of the Hill-rating | Core-literal match |
| 17686 | 859251960 | `component::lichess::entity::sensor::king_of_the_hill_games::unit_of_measurement` | games | spel | Shared reference target checked |
| 17687 | 859251959 | `component::lichess::entity::sensor::king_of_the_hill_games::name` | King of the Hill games | King of the Hill-spel | Core-literal match |
| 17688 | 859251958 | `component::lichess::entity::sensor::horde_rating::name` | Horde rating | Horde-rating | Core-literal match |
| 17689 | 859251957 | `component::lichess::entity::sensor::horde_games::unit_of_measurement` | games | spel | Shared reference target checked |
| 17690 | 859251956 | `component::lichess::entity::sensor::horde_games::name` | Horde games | Horde-spel | Core-literal match |
| 17691 | 859251955 | `component::lichess::entity::sensor::crazyhouse_rating::name` | Crazyhouse rating | Crazyhouse-rating | Core-literal match |
| 17692 | 859251954 | `component::lichess::entity::sensor::crazyhouse_games::unit_of_measurement` | games | spel | Shared reference target checked |
| 17693 | 859251953 | `component::lichess::entity::sensor::crazyhouse_games::name` | Crazyhouse games | Crazyhouse-spel | Core-literal match |
| 17694 | 859251952 | `component::lichess::entity::sensor::correspondence_rating::name` | Correspondence rating | Korrespondensrating | Core-literal match |
| 17695 | 859251951 | `component::lichess::entity::sensor::correspondence_games::unit_of_measurement` | games | spel | Shared reference target checked |
| 17696 | 859251950 | `component::lichess::entity::sensor::correspondence_games::name` | Correspondence games | Korrespondensspel | Core-literal match |
| 17697 | 859251949 | `component::lichess::entity::sensor::chess960_rating::name` | Chess960 rating | Chess960-rating | Core-literal match |
| 17698 | 859251948 | `component::lichess::entity::sensor::chess960_games::unit_of_measurement` | games | spel | Shared reference target checked |
| 17699 | 859251947 | `component::lichess::entity::sensor::chess960_games::name` | Chess960 games | Chess960-spel | Core-literal match |
| 17700 | 859251946 | `component::lichess::entity::sensor::atomic_rating::name` | Atomic rating | Atom-rating | Core-literal match |
| 17701 | 859251945 | `component::lichess::entity::sensor::atomic_games::unit_of_measurement` | games | spel | Shared reference target checked |
| 17702 | 859251944 | `component::lichess::entity::sensor::atomic_games::name` | Atomic games | Atomspel | Core-literal match |
| 17703 | 859251943 | `component::lichess::entity::sensor::antichess_rating::name` | Antichess rating | Antischack-rating | Core-literal match |
| 17704 | 859251942 | `component::lichess::entity::sensor::antichess_games::unit_of_measurement` | games | spel | Shared reference target checked |
| 17705 | 859251941 | `component::lichess::entity::sensor::antichess_games::name` | Antichess games | Antischackspel | Core-literal match |
| 17706 | 859249224 | `component::indevolt::config::step::zeroconf_confirm::title` | Discovered Indevolt {model} | Upptäckte Indevolt {model} | Core-literal match |
| 17707 | 859249223 | `component::indevolt::config::step::zeroconf_confirm::description` | Do you want to add {model} ({host}) to Home Assistant? | Vill du lägga till {model} ({host}) i Home Assistant? | Core-literal match |
| 17708 | 859249200 | `component::victron_gx::entity::switch::system_settings_prevent_ac_feedin::name` | AC-coupled PV - feed in excess | AC-kopplad PV - inmatning överskott | Core-literal match |
| 17709 | 859249199 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::state::with_battery_life` | Optimized mode with BatteryLife | Optimerat läge med BatteryLife | Core-literal match |
| 17710 | 859249198 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::state::sustain` | Multi/Quattro is in sustain | Multi/Quattro är i sustain-läge | Core-literal match |
| 17711 | 859249197 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::state::soc_below_soc_limit_24_hours` | SoC has been below SoC limit for more than 24 hours. Charging battery with 5 amps | SoC har legat under SoC-gränsen i mer än 24 timmar. Batteriet laddas med 5 ampere. | Core-literal match |
| 17712 | 859249196 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::state::soc_below_battery_life_dynamic_soc_limit` | SoC below BatteryLife dynamic SoC limit | SoC ligger under BatteryLife:s dynamiska SoC-gräns | Core-literal match |
| 17713 | 859249195 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::state::self_consumption_soc_exceeds_85` | Self-consumption, SoC exceeds 85% | Egenförbrukning, SoC överstiger 85 % | Core-literal match |
| 17714 | 859249194 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::state::self_consumption_soc_below_min` | Self-consumption, SoC is below minimum SoC | Egenförbrukning, SoC under minsta SoC | Core-literal match |
| 17715 | 859249193 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::state::self_consumption_soc_at_100` | Self-consumption, SoC at 100% | Egenförbrukning, SoC på 100 % | Core-literal match |
| 17716 | 859249192 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::state::self_consumption_soc_above_min` | Self-consumption, SoC at or above minimum SoC | Egenförbrukning, SoC på eller över minsta SoC | Core-literal match |
| 17717 | 859249191 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::state::self_consumption` | Self-consumption | Egenförbrukning | Shared reference target checked |
| 17718 | 859249190 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::state::recharge_no_battery_life` | Recharge, SoC dropped 5% or more below minimum SoC (No BatteryLife) | Laddning, SoC sjönk 5 % eller mer under minsta SoC (utan BetteryLife) | Core-literal match |
| 17719 | 859249189 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::state::recharge` | Recharge, SoC dropped 5% or more below minimum SoC | Laddning, SoC sjönk 5 % eller mer under minsta SoC | Core-literal match |
| 17720 | 859249188 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::state::keep_batteries_charged` | 'Keep batteries charged' mode enabled | Läget 'Håll batterierna laddade' är aktiverat | Core-literal match |
| 17721 | 859249187 | `component::victron_gx::entity::sensor::system_ess_batterylife_state_sensor::name` | ESS BatteryLife state | ESS BatteryLife-tillstånd | Core-literal match |
| 17722 | 859249186 | `component::victron_gx::entity::sensor::switch_output_state::name` | State | Tillstånd | Shared reference target checked |
| 17723 | 859249185 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::optimized_no_battery_life` | Optimized (without BatteryLife) | Optimerad (utan BatteryLife) | Core-literal match |
| 17724 | 859249184 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::optimized_battery_life` | Optimized (with BatteryLife) | Optimerad (med BatteryLife) | Core-literal match |
| 17725 | 859249183 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::external_control` | External control | Extern styrning | Shared reference target checked |
| 17726 | 859249182 | `component::victron_gx::entity::select::system_ac_input_2_type::state::shore` | Shore | Land | Shared reference target checked |
| 17727 | 859249181 | `component::victron_gx::entity::select::system_ac_input_2_type::state::not_used` | Not used | Ej använd | Shared reference target checked |
| 17728 | 859249180 | `component::victron_gx::entity::select::system_ac_input_2_type::state::grid` | Grid | Elnät | Shared reference target checked |
| 17729 | 859249179 | `component::victron_gx::entity::select::system_ac_input_2_type::state::generator` | Generator | Generator | Shared reference target checked |
| 17730 | 859249178 | `component::victron_gx::entity::select::system_ac_input_2_type::name` | AC input 2 source type | AC-ingång 2 källtyp | Core-literal match |
| 17731 | 859249177 | `component::victron_gx::entity::select::system_ac_input_1_type::state::shore` | Shore | Land | Shared reference target checked |
| 17732 | 859249176 | `component::victron_gx::entity::select::system_ac_input_1_type::state::not_used` | Not used | Ej använd | Shared reference target checked |
| 17733 | 859249175 | `component::victron_gx::entity::select::system_ac_input_1_type::state::grid` | Grid | Elnät | Shared reference target checked |
| 17734 | 859249174 | `component::victron_gx::entity::select::system_ac_input_1_type::state::generator` | Generator | Generator | Shared reference target checked |
| 17735 | 859249173 | `component::victron_gx::entity::select::system_ac_input_1_type::name` | AC input 1 source type | AC-ingång 1 källtyp | Core-literal match |
| 17736 | 859249172 | `component::victron_gx::entity::select::switch_output_state::name` | State | Tillstånd | Shared reference target checked |
| 17737 | 859249171 | `component::victron_gx::entity::number::switch_output_state::name` | State | Tillstånd | Shared reference target checked |
| 17738 | 859249170 | `component::victron_gx::entity::number::solarcharger_charge_current_limit::name` | Charge current limit | Gräns för laddström | Shared reference target checked |
| 17739 | 859249169 | `component::victron_gx::common::shore` | Shore | Land | Core-literal match |
| 17740 | 859249168 | `component::victron_gx::common::not_used` | Not used | Ej använd | Core-literal match |
| 17741 | 859249167 | `component::victron_gx::common::charge_current_limit` | Charge current limit | Gräns för laddström | Core-literal match |
| 17742 | 859070726 | `component::homee::exceptions::connection_failed::message` | Connection to homee failed. | Anslutningen till Homee misslyckades. | Core-literal match |
| 17743 | 859070725 | `component::homee::exceptions::auth_failed::message` | Authentication to homee failed. | Autentiseringen mot Homee misslyckades. | Core-literal match |
| 17744 | 858730030 | `component::vistapool::exceptions::update_failed::message` | Error fetching data from Vistapool. | Fel vid hämtning av data från Vistapool. | Core-literal match |
| 17745 | 858730029 | `component::vistapool::exceptions::no_pools::message` | No pools were found on this account. | Inga pooler hittades på detta konto. | Core-literal match |
| 17746 | 858730028 | `component::vistapool::exceptions::invalid_credentials::message` | Invalid Vistapool credentials. | Ogiltiga inloggningsuppgifter för Vistapool. | Core-literal match |
| 17747 | 858730027 | `component::vistapool::entity::sensor::uv::name` | UV | UV | Core-literal match |
| 17748 | 858730026 | `component::vistapool::entity::sensor::rssi::name` | Wi-Fi signal strength | Wi-Fi-signalstyrka | Core-literal match |
| 17749 | 858730025 | `component::vistapool::entity::sensor::redox_potential::name` | Redox potential | Redoxpotential | Core-literal match |
| 17750 | 858730024 | `component::vistapool::entity::sensor::hydrolysis::name` | Hydrolysis | Hydrolys | Core-literal match |
| 17751 | 858730023 | `component::vistapool::entity::sensor::filtration_intel_time::name` | Filtration intel time | Filtreringstid intelligent läge | Core-literal match |
| 17752 | 858730022 | `component::vistapool::entity::sensor::electrolysis::name` | Electrolysis | Elektrolys | Core-literal match |
| 17753 | 858730021 | `component::vistapool::entity::sensor::conductivity::name` | Conductivity | Konduktivitet | Core-literal match |
| 17754 | 858730020 | `component::vistapool::entity::sensor::chlorine::name` | Chlorine | Klor | Core-literal match |
| 17755 | 858730019 | `component::vistapool::config::step::user::title` | Authentication | Autentisering | Core-literal match |
| 17756 | 858730018 | `component::vistapool::config::step::user::description` | Enter your Vistapool credentials. All pools on the account will be added automatically. | Ange dina inloggningsuppgifter för Vistapool. Alla pooler på kontot läggs till automatiskt. | Core-literal match |
| 17757 | 858730017 | `component::vistapool::config::step::user::data_description::username` | The email used for your Vistapool account | E-postadressen för ditt Vistapool-konto | Core-literal match |
| 17758 | 858730016 | `component::vistapool::config::step::user::data_description::password` | The password for your Vistapool account | Lösenordet för ditt Vistapool-konto | Core-literal match |
| 17759 | 858730015 | `component::vistapool::config::step::user::data::username` | Vistapool Username | Vistapool-användarnamn | Core-literal match |
| 17760 | 858730014 | `component::vistapool::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
