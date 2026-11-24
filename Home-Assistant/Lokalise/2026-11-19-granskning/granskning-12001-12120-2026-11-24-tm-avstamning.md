# Home Assistant Core – historisk avstämning 12001–12120

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader kontrollerade. 116 direkta strängar matchar aktuell Core-källa; 2 referensanvändningar med 2 mål stämmer. Två globala återställningsmeddelanden verifierades mot `homeassistant/strings.json`.
- Saknade referensmål: 0; referensmismatchar: 0; tomma värden: 0; platshållarmismatch: 0.
- Alla äldre föreslagna värden är redan live utom Mideas `Fresh produce`. Den befintliga formuleringen `Färsk frukt och grönt` behölls eftersom den är konkretare än rapportförslaget `Färska råvaror`. Inga API-skrivningar behövdes.
- Samtliga 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 12001 | 921052600 | `component::vizio::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | shared-reference |
| 12002 | 921052599 | `component::vizio::config::step::reauth_confirm::description` | The stored access token is no longer valid, so the device needs to be paired again. Make sure the TV is powered on and connected to the network, then continue to display a pairing code on the TV screen. | Den sparade åtkomsttokenen är inte längre giltig, så enheten måste parkopplas igen. Kontrollera att TV:n är påslagen och ansluten till nätverket och fortsätt därefter för att visa en parkopplingskod på TV-skärmen. | literal-match |
| 12003 | 921052598 | `component::vizio::config::abort::unique_id_mismatch` | Please ensure you reconfigure against the same device. | Kontrollera att du konfigurerar om samma enhet. | literal-match |
| 12004 | 921052597 | `component::vizio::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | shared Core common string |
| 12005 | 921052596 | `component::vizio::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | shared Core common string |
| 12006 | 921018296 | `component::forecast_solar::services::get_forecast::name` | Get forecast | Hämta prognos | literal-match |
| 12007 | 921018295 | `component::forecast_solar::services::get_forecast::fields::start::name` | Start | Start | literal-match |
| 12008 | 921018294 | `component::forecast_solar::services::get_forecast::fields::start::description` | Earliest period start to return (inclusive). If omitted, the response begins at the start of the cached forecast. | Tidigaste starttid för perioder som ska ingå i resultatet, inklusive den angivna tiden. Om den utelämnas börjar svaret vid början av den cachelagrade prognosen. | literal-match |
| 12009 | 921018293 | `component::forecast_solar::services::get_forecast::fields::resolution::name` | Resolution | Upplösning | literal-match |
| 12010 | 921018292 | `component::forecast_solar::services::get_forecast::fields::resolution::description` | Resolution of the returned series. 'Native' uses the upstream Forecast.Solar resolution (15-minute on paid accounts, hourly on the free tier). 'Hourly' aggregates to whole-hour buckets. | Upplösning för den returnerade serien. ”Native” använder upplösningen från Forecast.Solar: 15 minuter för betalkonton och en timme för gratiskonton. ”Hourly” sammanställer värdena per hel timme. | literal-match |
| 12011 | 921018291 | `component::forecast_solar::services::get_forecast::fields::end::name` | End | Slut | literal-match |
| 12012 | 921018290 | `component::forecast_solar::services::get_forecast::fields::end::description` | Latest period start to return (exclusive). If omitted, the response includes the full cached forecast. | Övre gräns för periodernas starttid. Perioder som börjar vid eller efter denna tid ingår inte. Om den utelämnas innehåller svaret hela den cachelagrade prognosen. | literal-match |
| 12013 | 921018289 | `component::forecast_solar::services::get_forecast::fields::config_entry::name` | Forecast.Solar entry | Forecast.Solar-konfigurationspost | literal-match |
| 12014 | 921018288 | `component::forecast_solar::services::get_forecast::fields::config_entry::description` | The Forecast.Solar configuration entry to query. | Forecast.Solar-konfigurationen som prognosen ska hämtas för. | literal-match |
| 12015 | 921018287 | `component::forecast_solar::services::get_forecast::description` | Returns the solar production forecast time series for a configured Forecast.Solar entry. | Returnerar tidsserien för prognosen av solenergiproduktionen för en konfigurerad Forecast.Solar-post. | literal-match |
| 12016 | 921018286 | `component::forecast_solar::selector::forecast_resolution::options::raw` | Native (15-minute or hourly, depending on account) | Automatisk (var 15:e minut eller varje timme, beroende på konto) | literal-match |
| 12017 | 921018285 | `component::forecast_solar::selector::forecast_resolution::options::hourly` | Aggregated to whole hours | Aggregerat till hela timmar | literal-match |
| 12018 | 921018284 | `component::forecast_solar::exceptions::end_before_start::message` | The end time must be after the start time. | Sluttiden måste vara efter starttiden. | literal-match |
| 12019 | 921018129 | `component::homeassistant::config::abort::cloud_not_connected` | Not connected to Home Assistant Cloud. | Ej ansluten till Home Assistant Cloud. | shared-reference |
| 12020 | 921007162 | `component::midea::entity::time::timing_regeneration::name` | Regeneration time | Regenereringstid | literal-match |
| 12021 | 921004817 | `component::midea::entity::sensor::water_temperature::name` | Water temperature | Vattentemperatur | literal-match |
| 12022 | 921004816 | `component::midea::entity::sensor::water_consumption_big::name` | Water consumption aggregated | Sammanlagd vattenförbrukning | literal-match |
| 12023 | 921004815 | `component::midea::entity::sensor::water_consumption_average::name` | Water consumption average | Genomsnittlig vattenförbrukning | literal-match |
| 12024 | 921004814 | `component::midea::entity::sensor::water_consumption::name` | Water consumption | Vattenförbrukning | literal-match |
| 12025 | 921004813 | `component::midea::entity::sensor::wash_time::name` | Wash time | Tvättid | literal-match |
| 12026 | 921004812 | `component::midea::entity::sensor::variable_mode::state::zero_fresh` | Zero fresh | Noll färskhet | literal-match |
| 12027 | 921004811 | `component::midea::entity::sensor::variable_mode::state::soft_freezing` | Soft freezing | Mjuk frysning | literal-match |
| 12028 | 921004810 | `component::midea::entity::sensor::variable_mode::state::partial_freezing` | Partial freezing | Delvis frysning | literal-match |
| 12029 | 921004809 | `component::midea::entity::sensor::variable_mode::state::none` | None | Ingen | literal-match |
| 12030 | 921004808 | `component::midea::entity::sensor::variable_mode::state::fresh_product` | Fresh produce | Färsk frukt och grönt | literal-match |
| 12031 | 921004807 | `component::midea::entity::sensor::variable_mode::state::freeze_warm` | Freeze / warm | Frysning / uppvärmning | literal-match |
| 12032 | 921004806 | `component::midea::entity::sensor::variable_mode::state::dry_zone` | Dry zone | Torr zon | literal-match |
| 12033 | 921004805 | `component::midea::entity::sensor::variable_mode::state::cold_drink` | Cold drink | Kall dryck | literal-match |
| 12034 | 921004804 | `component::midea::entity::sensor::variable_mode::name` | Variable mode | Variabelt läge | literal-match |
| 12035 | 921004803 | `component::midea::entity::sensor::use_days::name` | Days of use | Användningsdagar | literal-match |
| 12036 | 921004802 | `component::midea::entity::sensor::tvoc::name` | TVOC | TVOC | literal-match |
| 12037 | 921004801 | `component::midea::entity::sensor::total_produced_energy::name` | Total produced energy | Total producerad energi | literal-match |
| 12038 | 921004800 | `component::midea::entity::sensor::total_energy_consumption::name` | Total energy consumption | Total energiförbrukning | literal-match |
| 12039 | 921004799 | `component::midea::entity::sensor::top_temperature::name` | Top temperature | Topptemperatur | literal-match |
| 12040 | 921004798 | `component::midea::entity::sensor::top_compartment_temperature::name` | Top compartment temperature | Övre fackets temperatur | literal-match |
| 12041 | 921004797 | `component::midea::entity::sensor::temperature_raw::name` | Raw temperature | Rå temperatur | literal-match |
| 12042 | 921004796 | `component::midea::entity::sensor::temperature_compensate::name` | Temperature compensation | Temperaturkompensation | literal-match |
| 12043 | 921004795 | `component::midea::entity::sensor::temp_tw_out::name` | Water outlet temperature | Vattenutloppstemperatur | literal-match |
| 12044 | 921004794 | `component::midea::entity::sensor::temp_tw_in::name` | Water inlet temperature | Vatteninloppstemperatur | literal-match |
| 12045 | 921004793 | `component::midea::entity::sensor::target_temperature::name` | Target temperature | Måltemperatur | literal-match |
| 12046 | 921004792 | `component::midea::entity::sensor::target_indoor_fan_speed::name` | Target indoor fan speed | Målhastighet för inomhusfläkt | literal-match |
| 12047 | 921004791 | `component::midea::entity::sensor::target_compressor_frequency::name` | Target compressor frequency | Målfrekvens för kompressor | literal-match |
| 12048 | 921004790 | `component::midea::entity::sensor::tank_level::name` | Tank level | Tanknivå | literal-match |
| 12049 | 921004789 | `component::midea::entity::sensor::tank_actual_temperature::name` | Tank temperature | Tanktemperatur | literal-match |
| 12050 | 921004788 | `component::midea::entity::sensor::softwater_available::name` | Soft water available | Mjukt vatten tillgängligt | literal-match |
| 12051 | 921004787 | `component::midea::entity::sensor::soak_time::name` | Soak time | Blötläggningstid | literal-match |
| 12052 | 921004786 | `component::midea::entity::sensor::seat_temperature::name` | Seat temperature | Sätestemperatur | literal-match |
| 12053 | 921004785 | `component::midea::entity::sensor::salt_available::name` | Salt available | Salt tillgängligt | literal-match |
| 12054 | 921004784 | `component::midea::entity::sensor::right_flex_zone_setting_temp::name` | Right flex zone setting temperature | Högra flexzonens inställda temperatur | literal-match |
| 12055 | 921004783 | `component::midea::entity::sensor::right_flex_zone_actual_temp::name` | Right flex zone actual temperature | Högra flexzonens faktiska temperatur | literal-match |
| 12056 | 921004782 | `component::midea::entity::sensor::remaining_days::name` | Remaining days | Återstående dagar | literal-match |
| 12057 | 921004781 | `component::midea::entity::sensor::refrigerator_setting_temp::name` | Refrigerator setting temperature | Kylskåpets inställda temperatur | literal-match |
| 12058 | 921004780 | `component::midea::entity::sensor::refrigerator_actual_temp::name` | Refrigerator actual temperature | Kylskåpets faktiska temperatur | literal-match |
| 12059 | 921004779 | `component::midea::entity::sensor::realtime_power::name` | Real-time power | Effekt i realtid | literal-match |
| 12060 | 921004778 | `component::midea::entity::sensor::pmv::name` | Predicted mean vote | Förväntat medelvärde (pmv) | literal-match |
| 12061 | 921004777 | `component::midea::entity::sensor::outdoor_temperature::name` | Outdoor temperature | Utomhustemperatur | literal-match |
| 12062 | 921004776 | `component::midea::entity::sensor::out_tds::name` | Out TDS | Ut TDS | literal-match |
| 12063 | 921004775 | `component::midea::entity::sensor::mode::state::yoghourt` | Yoghourt | Yoghurt | literal-match |
| 12064 | 921004774 | `component::midea::entity::sensor::mode::state::yellow_wheat_rice` | Yellow wheat rice | Gult veteris | literal-match |
| 12065 | 921004773 | `component::midea::entity::sensor::mode::state::warm_milk` | Warm milk | Varm mjölk | literal-match |
| 12066 | 921004772 | `component::midea::entity::sensor::mode::state::vegetable_rice` | Vegetable rice | Grönsaksris | literal-match |
| 12067 | 921004771 | `component::midea::entity::sensor::mode::state::vegetable_porridge` | Vegetable porridge | Grönsaksgröt | literal-match |
| 12068 | 921004770 | `component::midea::entity::sensor::mode::state::uncap_boil` | Uncap boil | Ta av locket och låt koka | literal-match |
| 12069 | 921004769 | `component::midea::entity::sensor::mode::state::trichromatic_coarse_grain` | Trichromatic coarse grain | Trikromatisk grovkornig | literal-match |
| 12070 | 921004768 | `component::midea::entity::sensor::mode::state::sushi_rice` | Sushi rice | Sushiris | literal-match |
| 12071 | 921004767 | `component::midea::entity::sensor::mode::state::stone_bowl_rice` | Stone bowl rice | Stenskålsris | literal-match |
| 12072 | 921004766 | `component::midea::entity::sensor::mode::state::stewing` | Stewing | Gryta | literal-match |
| 12073 | 921004765 | `component::midea::entity::sensor::mode::state::stew_soup` | Stew soup | Grytsoppa | literal-match |
| 12074 | 921004764 | `component::midea::entity::sensor::mode::state::steep_rice` | Steep rice | Blötlägg ris | literal-match |
| 12075 | 921004763 | `component::midea::entity::sensor::mode::state::steame_fish` | Steamed fish | Ångkokt fisk | literal-match |
| 12076 | 921004762 | `component::midea::entity::sensor::mode::state::steam_ribs` | Steam ribs | Ångkokta ribs | literal-match |
| 12077 | 921004761 | `component::midea::entity::sensor::mode::state::steam_red_potato` | Steam red potato | Ångad röd potatis | literal-match |
| 12078 | 921004760 | `component::midea::entity::sensor::mode::state::steam_egg` | Steam egg | Ångkokt ägg | literal-match |
| 12079 | 921004759 | `component::midea::entity::sensor::mode::state::steam_corn` | Steam corn | Ångmajs | literal-match |
| 12080 | 921004758 | `component::midea::entity::sensor::mode::state::standard_cook_rice` | Standard cook rice | Standardkokt ris | literal-match |
| 12081 | 921004757 | `component::midea::entity::sensor::mode::state::sprout_rice` | Sprout rice | Risgroddar | literal-match |
| 12082 | 921004756 | `component::midea::entity::sensor::mode::state::soup_rice` | Soup rice | Soppris | literal-match |
| 12083 | 921004755 | `component::midea::entity::sensor::mode::state::smart` | Smart | Smart | literal-match |
| 12084 | 921004754 | `component::midea::entity::sensor::mode::state::shelled_rice` | Shelled rice | Skalat ris | literal-match |
| 12085 | 921004753 | `component::midea::entity::sensor::mode::state::service` | Service | Service | literal-match |
| 12086 | 921004752 | `component::midea::entity::sensor::mode::state::roughage_rice` | Roughage rice | Grovfoderris | literal-match |
| 12087 | 921004751 | `component::midea::entity::sensor::mode::state::rice_wine` | Rice wine | Risvin | literal-match |
| 12088 | 921004750 | `component::midea::entity::sensor::mode::state::rice_soup` | Rice soup | Rissoppa | literal-match |
| 12089 | 921004749 | `component::midea::entity::sensor::mode::state::rice_paste` | Rice paste | Rispasta | literal-match |
| 12090 | 921004748 | `component::midea::entity::sensor::mode::state::resveratrol_rice` | Resveratrol rice | Resveratrolris | literal-match |
| 12091 | 921004747 | `component::midea::entity::sensor::mode::state::reserve` | Reserve | Reserv | literal-match |
| 12092 | 921004746 | `component::midea::entity::sensor::mode::state::regimen_soup` | Regimen soup | Regimen-soppa | literal-match |
| 12093 | 921004745 | `component::midea::entity::sensor::mode::state::regimen_congee` | Regimen congee | Regimen-risgröt | literal-match |
| 12094 | 921004744 | `component::midea::entity::sensor::mode::state::red_potato` | Red potato | Röd potatis | literal-match |
| 12095 | 921004743 | `component::midea::entity::sensor::mode::state::quick_freeze_bun` | Quick freeze bun | Snabbfryst bulle | literal-match |
| 12096 | 921004742 | `component::midea::entity::sensor::mode::state::pottery_jar_soup` | Pottery jar soup | Keramikburksoppa | literal-match |
| 12097 | 921004741 | `component::midea::entity::sensor::mode::state::pork_porridge` | Pork porridge | Fläskgröt | literal-match |
| 12098 | 921004740 | `component::midea::entity::sensor::mode::state::original_steame` | Original steam | Original ånga | literal-match |
| 12099 | 921004739 | `component::midea::entity::sensor::mode::state::online_celebrity_rice` | Online celebrity rice | Online celebrity-ris | literal-match |
| 12100 | 921004738 | `component::midea::entity::sensor::mode::state::one_two_cook` | One two cook | Ett två laga mat | literal-match |
| 12101 | 921004737 | `component::midea::entity::sensor::mode::state::olla_pan_rice` | Olla pan rice | Olla pan-ris | literal-match |
| 12102 | 921004736 | `component::midea::entity::sensor::mode::state::older_rice` | Older rice | Äldre ris | literal-match |
| 12103 | 921004735 | `component::midea::entity::sensor::mode::state::nutrition_stew` | Nutrition stew | Näringsgryta | literal-match |
| 12104 | 921004734 | `component::midea::entity::sensor::mode::state::northeast_stew` | Northeast stew | Nordöstlig gryta | literal-match |
| 12105 | 921004733 | `component::midea::entity::sensor::mode::state::normal_continus` | Normal continuous | Normal kontinuerlig | literal-match |
| 12106 | 921004732 | `component::midea::entity::sensor::mode::state::normal` | Normal | Normal | literal-match |
| 12107 | 921004731 | `component::midea::entity::sensor::mode::state::no_water_treat` | No water treat | Ingen vattenbehandling | literal-match |
| 12108 | 921004730 | `component::midea::entity::sensor::mode::state::millet_mixed_rice` | Millet mixed rice | Risblandning med hirs | literal-match |
| 12109 | 921004729 | `component::midea::entity::sensor::mode::state::millet_congee` | Millet congee | Hirsrisgröt | literal-match |
| 12110 | 921004728 | `component::midea::entity::sensor::mode::state::make_cake` | Make cake | Baka tårta | literal-match |
| 12111 | 921004727 | `component::midea::entity::sensor::mode::state::luscious_rice` | Luscious rice | Läckert ris | literal-match |
| 12112 | 921004726 | `component::midea::entity::sensor::mode::state::luscious_boiled` | Luscious boiled | Läckert kokt | literal-match |
| 12113 | 921004725 | `component::midea::entity::sensor::mode::state::low_sugar_rice` | Low sugar rice | Lågsockerris | literal-match |
| 12114 | 921004724 | `component::midea::entity::sensor::mode::state::keep_warm` | Keep warm | Håll varmt | literal-match |
| 12115 | 921004723 | `component::midea::entity::sensor::mode::state::keep_fresh` | Keep fresh | Håll färskt | literal-match |
| 12116 | 921004722 | `component::midea::entity::sensor::mode::state::iron_pan_rice` | Iron pan rice | Järnpannris | literal-match |
| 12117 | 921004721 | `component::midea::entity::sensor::mode::state::infant_congee` | Infant congee | Spädbarnsrisgröt | literal-match |
| 12118 | 921004720 | `component::midea::entity::sensor::mode::state::hot_spring_egg` | Hot spring egg | Onsenägg | literal-match |
| 12119 | 921004719 | `component::midea::entity::sensor::mode::state::hot_fast_rice` | Hot fast rice | Varmt snabbris | literal-match |
| 12120 | 921004718 | `component::midea::entity::sensor::mode::state::heat_rice` | Heat rice | Värm ris | literal-match |

## Äldre förslag som inte följdes

| Nyckel | Äldre förslag | Aktuell svenska |
|---|---|---|
| `component::midea::entity::sensor::variable_mode::state::fresh_product` | Färska råvaror | Färsk frukt och grönt |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Full manifest finns bredvid denna rapport; HA Core snapshot och kanonisk TMX uppdaterade.
