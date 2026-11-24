# Home Assistant Core – historisk avstämning 22321–22440

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 17 direkta källtexter matchar HA Core-källan; 47 referensanvändningar med 14 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 56 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 22321 | 823041873 | `component::power::triggers::crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22322 | 823041872 | `component::power::triggers::crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22323 | 823041871 | `component::power::triggers::changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22324 | 823041870 | `component::power::triggers::changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22325 | 823041869 | `component::power::common::trigger_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22326 | 823041868 | `component::power::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22327 | 823041867 | `component::power::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22328 | 823041866 | `component::moisture::triggers::crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22329 | 823041865 | `component::moisture::triggers::crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22330 | 823041864 | `component::moisture::triggers::changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22331 | 823041863 | `component::moisture::triggers::changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22332 | 823041862 | `component::moisture::common::trigger_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22333 | 823041861 | `component::moisture::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22334 | 823041860 | `component::moisture::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22335 | 823041859 | `component::light::triggers::brightness_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22336 | 823041858 | `component::light::triggers::brightness_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22337 | 823041857 | `component::light::triggers::brightness_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22338 | 823041856 | `component::light::triggers::brightness_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22339 | 823041855 | `component::light::common::trigger_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22340 | 823041854 | `component::light::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22341 | 823041853 | `component::light::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22342 | 823041852 | `component::illuminance::triggers::crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22343 | 823041851 | `component::illuminance::triggers::crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22344 | 823041850 | `component::illuminance::triggers::changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22345 | 823041849 | `component::illuminance::triggers::changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22346 | 823041848 | `component::illuminance::common::trigger_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22347 | 823041847 | `component::illuminance::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22348 | 823041846 | `component::illuminance::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22349 | 823041845 | `component::humidity::triggers::crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22350 | 823041844 | `component::humidity::triggers::crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22351 | 823041843 | `component::humidity::triggers::changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22352 | 823041842 | `component::humidity::triggers::changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22353 | 823041841 | `component::humidity::common::trigger_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22354 | 823041840 | `component::humidity::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22355 | 823041839 | `component::humidity::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22356 | 823041838 | `component::climate::triggers::target_temperature_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22357 | 823041837 | `component::climate::triggers::target_temperature_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22358 | 823041836 | `component::climate::triggers::target_temperature_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22359 | 823041835 | `component::climate::triggers::target_temperature_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22360 | 823041834 | `component::climate::triggers::target_humidity_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22361 | 823041833 | `component::climate::triggers::target_humidity_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22362 | 823041832 | `component::climate::triggers::target_humidity_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22363 | 823041831 | `component::climate::triggers::target_humidity_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22364 | 823041830 | `component::climate::common::trigger_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22365 | 823041829 | `component::climate::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22366 | 823041828 | `component::climate::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22367 | 823041827 | `component::air_quality::triggers::voc_ratio_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22368 | 823041826 | `component::air_quality::triggers::voc_ratio_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22369 | 823041825 | `component::air_quality::triggers::voc_ratio_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22370 | 823041824 | `component::air_quality::triggers::voc_ratio_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22371 | 823041823 | `component::air_quality::triggers::voc_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22372 | 823041822 | `component::air_quality::triggers::voc_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22373 | 823041821 | `component::air_quality::triggers::voc_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22374 | 823041820 | `component::air_quality::triggers::voc_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22375 | 823041819 | `component::air_quality::triggers::so2_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22376 | 823041818 | `component::air_quality::triggers::so2_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22377 | 823041817 | `component::air_quality::triggers::so2_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22378 | 823041816 | `component::air_quality::triggers::so2_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22379 | 823041815 | `component::air_quality::triggers::pm4_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22380 | 823041814 | `component::air_quality::triggers::pm4_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22381 | 823041813 | `component::air_quality::triggers::pm4_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22382 | 823041812 | `component::air_quality::triggers::pm4_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22383 | 823041811 | `component::air_quality::triggers::pm25_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22384 | 823041810 | `component::air_quality::triggers::pm25_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22385 | 823041809 | `component::air_quality::triggers::pm25_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22386 | 823041808 | `component::air_quality::triggers::pm25_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22387 | 823041807 | `component::air_quality::triggers::pm1_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22388 | 823041806 | `component::air_quality::triggers::pm1_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22389 | 823041805 | `component::air_quality::triggers::pm1_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22390 | 823041804 | `component::air_quality::triggers::pm1_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22391 | 823041803 | `component::air_quality::triggers::pm10_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22392 | 823041802 | `component::air_quality::triggers::pm10_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22393 | 823041801 | `component::air_quality::triggers::pm10_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22394 | 823041800 | `component::air_quality::triggers::pm10_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22395 | 823041799 | `component::air_quality::triggers::ozone_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22396 | 823041798 | `component::air_quality::triggers::ozone_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22397 | 823041797 | `component::air_quality::triggers::ozone_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22398 | 823041796 | `component::air_quality::triggers::ozone_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22399 | 823041795 | `component::air_quality::triggers::no_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22400 | 823041794 | `component::air_quality::triggers::no_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22401 | 823041793 | `component::air_quality::triggers::no_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22402 | 823041792 | `component::air_quality::triggers::no_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22403 | 823041791 | `component::air_quality::triggers::no2_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22404 | 823041790 | `component::air_quality::triggers::no2_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22405 | 823041789 | `component::air_quality::triggers::no2_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22406 | 823041788 | `component::air_quality::triggers::no2_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22407 | 823041787 | `component::air_quality::triggers::n2o_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22408 | 823041786 | `component::air_quality::triggers::n2o_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22409 | 823041785 | `component::air_quality::triggers::n2o_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22410 | 823041784 | `component::air_quality::triggers::n2o_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22411 | 823041783 | `component::air_quality::triggers::co_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22412 | 823041782 | `component::air_quality::triggers::co_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22413 | 823041781 | `component::air_quality::triggers::co_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22414 | 823041780 | `component::air_quality::triggers::co_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22415 | 823041779 | `component::air_quality::triggers::co2_crossed_threshold::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22416 | 823041778 | `component::air_quality::triggers::co2_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22417 | 823041777 | `component::air_quality::triggers::co2_changed::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 22418 | 823041776 | `component::air_quality::triggers::co2_changed::fields::threshold::description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22419 | 823041775 | `component::air_quality::common::trigger_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 22420 | 823041774 | `component::air_quality::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. | Vilken tröskelövergång som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22421 | 823041773 | `component::air_quality::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. | Vilka ändringar som ska utlösa samt tröskelvärden. | Source-path follow-up open |
| 22422 | 823041588 | `component::unifi_access::entity::sensor::door_lock_rule_ended_time::name` | Rule end time | Regelns sluttid | Core-literal match |
| 22423 | 823041587 | `component::unifi_access::entity::sensor::door_lock_rule::state::schedule` | Schedule | Schema | Core-literal match |
| 22424 | 823041586 | `component::unifi_access::entity::sensor::door_lock_rule::state::reset` | Reset | Återställ | Core-literal match |
| 22425 | 823041585 | `component::unifi_access::entity::sensor::door_lock_rule::state::lock_now` | Lock now | Lås nu | Core-literal match |
| 22426 | 823041584 | `component::unifi_access::entity::sensor::door_lock_rule::state::lock_early` | Lock early | Lås tidigt | Core-literal match |
| 22427 | 823041583 | `component::unifi_access::entity::sensor::door_lock_rule::state::keep_unlock` | Unlocked | Olåst | Core-literal match |
| 22428 | 823041582 | `component::unifi_access::entity::sensor::door_lock_rule::state::keep_lock` | Locked | Låst | Core-literal match |
| 22429 | 823041581 | `component::unifi_access::entity::sensor::door_lock_rule::state::custom` | Custom | Anpassad | Core-literal match |
| 22430 | 823041580 | `component::unifi_access::entity::sensor::door_lock_rule::name` | Lock rule | Låsregel | Core-literal match |
| 22431 | 823041524 | `component::wiim::config::abort::missing_homeassistant_url` | Failed to determine Home Assistant URL. Please make sure you have an internal URL set. | Kunde inte fastställa Home Assistants URL. Se till att du har angett en intern URL. | Source-path follow-up open |
| 22432 | 823038169 | `component::water_heater::entity_component::_::state_attributes::operation_mode::state::performance` | Performance | Prestanda | Shared reference target checked |
| 22433 | 823038168 | `component::water_heater::entity_component::_::state_attributes::operation_mode::state::off` | Off | Av | Shared reference target checked |
| 22434 | 823038167 | `component::water_heater::entity_component::_::state_attributes::operation_mode::state::high_demand` | High demand | Hög efterfrågan | Shared reference target checked |
| 22435 | 823038166 | `component::water_heater::entity_component::_::state_attributes::operation_mode::state::heat_pump` | Heat pump | Värmepump | Shared reference target checked |
| 22436 | 823038165 | `component::water_heater::entity_component::_::state_attributes::operation_mode::state::gas` | Gas | Gas | Shared reference target checked |
| 22437 | 823038164 | `component::water_heater::entity_component::_::state_attributes::operation_mode::state::electric` | Electric | Elektrisk | Shared reference target checked |
| 22438 | 823038163 | `component::water_heater::entity_component::_::state_attributes::operation_mode::state::eco` | Eco | Eko | Shared reference target checked |
| 22439 | 823038162 | `component::water_heater::entity_component::_::state_attributes::operation_mode::name` | Operation mode | Driftläge | Core-literal match |
| 22440 | 823037795 | `component::temperature::selector::condition_behavior::options::any` | Any | Något | Source-path follow-up open |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 823041872 | `component::power::triggers::crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041870 | `component::power::triggers::changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041868 | `component::power::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. |
| 823041867 | `component::power::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. |
| 823041865 | `component::moisture::triggers::crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041863 | `component::moisture::triggers::changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041861 | `component::moisture::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. |
| 823041860 | `component::moisture::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. |
| 823041858 | `component::light::triggers::brightness_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041856 | `component::light::triggers::brightness_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041854 | `component::light::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. |
| 823041853 | `component::light::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. |
| 823041851 | `component::illuminance::triggers::crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041849 | `component::illuminance::triggers::changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041847 | `component::illuminance::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. |
| 823041846 | `component::illuminance::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. |
| 823041844 | `component::humidity::triggers::crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041842 | `component::humidity::triggers::changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041840 | `component::humidity::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. |
| 823041839 | `component::humidity::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. |
| 823041837 | `component::climate::triggers::target_temperature_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041835 | `component::climate::triggers::target_temperature_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041833 | `component::climate::triggers::target_humidity_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041831 | `component::climate::triggers::target_humidity_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041829 | `component::climate::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. |
| 823041828 | `component::climate::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. |
| 823041826 | `component::air_quality::triggers::voc_ratio_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041824 | `component::air_quality::triggers::voc_ratio_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041822 | `component::air_quality::triggers::voc_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041820 | `component::air_quality::triggers::voc_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041818 | `component::air_quality::triggers::so2_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041816 | `component::air_quality::triggers::so2_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041814 | `component::air_quality::triggers::pm4_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041812 | `component::air_quality::triggers::pm4_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041810 | `component::air_quality::triggers::pm25_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041808 | `component::air_quality::triggers::pm25_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041806 | `component::air_quality::triggers::pm1_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041804 | `component::air_quality::triggers::pm1_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041802 | `component::air_quality::triggers::pm10_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041800 | `component::air_quality::triggers::pm10_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041798 | `component::air_quality::triggers::ozone_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041796 | `component::air_quality::triggers::ozone_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041794 | `component::air_quality::triggers::no_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041792 | `component::air_quality::triggers::no_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041790 | `component::air_quality::triggers::no2_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041788 | `component::air_quality::triggers::no2_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041786 | `component::air_quality::triggers::n2o_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041784 | `component::air_quality::triggers::n2o_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041782 | `component::air_quality::triggers::co_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041780 | `component::air_quality::triggers::co_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041778 | `component::air_quality::triggers::co2_crossed_threshold::fields::threshold::description` | Which threshold crossing to trigger on and threshold values. |
| 823041776 | `component::air_quality::triggers::co2_changed::fields::threshold::description` | Which changes to trigger on and threshold values. |
| 823041774 | `component::air_quality::common::trigger_threshold_crossed_description` | Which threshold crossing to trigger on and threshold values. |
| 823041773 | `component::air_quality::common::trigger_threshold_changed_description` | Which changes to trigger on and threshold values. |
| 823041524 | `component::wiim::config::abort::missing_homeassistant_url` | Failed to determine Home Assistant URL. Please make sure you have an internal URL set. |
| 823037795 | `component::temperature::selector::condition_behavior::options::any` | Any |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
