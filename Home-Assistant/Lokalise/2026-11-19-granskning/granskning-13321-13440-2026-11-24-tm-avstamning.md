# Home Assistant Core – historisk avstämning 13321–13440

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 77 direkta källtexter matchar HA Core-källan; 43 referensanvändningar med 43 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 0 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 13321 | 908724489 | `component::home_connect::selector::programs::options::laundry_care_washer_dryer_program_sensitive` | Sensitive | Känslig | Core-literal match |
| 13322 | 908724488 | `component::home_connect::selector::programs::options::laundry_care_washer_dryer_program_rinse` | Rinse | Sköljning | Core-literal match |
| 13323 | 908724487 | `component::home_connect::selector::programs::options::laundry_care_washer_dryer_program_drum_clean_and_dry_drum_care` | Drum care | Trumvård | Core-literal match |
| 13324 | 908724486 | `component::home_connect::selector::programs::options::laundry_care_washer_dryer_program_delicates_silk` | Delicates silk | Fintvätt och siden | Core-literal match |
| 13325 | 908724485 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_wool_finish` | Wool finish | Ullfinish | Core-literal match |
| 13326 | 908724484 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_time_cold_air_fluff` | Air fluff | Vädring med kalluft | Core-literal match |
| 13327 | 908724483 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_outdoor_sportswear` | Sportswear | Sportkläder | Core-literal match |
| 13328 | 908724482 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_maintenance_care_2_maintenance_care_2_depth_care` | Depth care | Djupgående vård | Core-literal match |
| 13329 | 908724481 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_maintenance_care_1_maintenance_care_1_quick_care` | Quick care | Snabbvård | Core-literal match |
| 13330 | 908724480 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_in_basket_wool_basket` | Wool basket | Ullkorg | Core-literal match |
| 13331 | 908724479 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_easy_care_easy_care` | Easy care | Lättskött | Core-literal match |
| 13332 | 908724478 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_cotton_eco_4060` | Cotton eco 40/60ºC | Bomull eko 40/60 °C | Core-literal match |
| 13333 | 908724477 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_cotton_cotton_eco` | Cotton eco | Bomull eko | Core-literal match |
| 13334 | 908724476 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_connected_dry` | Connected dry | Ansluten torr | Core-literal match |
| 13335 | 908724475 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_cold_refresh_cold_refresh_cold_refresh` | Cold refresh | Kall uppfriskning | Core-literal match |
| 13336 | 908724474 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_cold_refresh_business` | Cold refresh - Business | Kall uppfräschning – affärskläder | Core-literal match |
| 13337 | 908724473 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_cold_refresh_5_piece` | Cold refresh - 5 piece | Kall uppfriskning - 5 stycken | Core-literal match |
| 13338 | 908724472 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_cold_refresh_1_piece` | Cold refresh - 1 piece | Kall uppfriskning - 1 styck | Core-literal match |
| 13339 | 908724471 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_business_shirts_easy_iron` | Business shirts - Easy iron | Skjortor – lättstruket | Core-literal match |
| 13340 | 908724470 | `component::home_connect::selector::programs::options::laundry_care_dryer_program_bedlinens` | Bed linens | Sängkläder | Core-literal match |
| 13341 | 908724469 | `component::home_connect::selector::programs::options::dishcare_dishwasher_program_quick_d` | Quick d | Snabb d | Core-literal match |
| 13342 | 908724468 | `component::home_connect::selector::programs::options::dishcare_dishwasher_program_max_efficient` | Max efficient | Maximal effektivitet | Core-literal match |
| 13343 | 908724467 | `component::home_connect::selector::programs::options::dishcare_dishwasher_program_glass_shine` | Glass shine | Glasglans | Core-literal match |
| 13344 | 908724466 | `component::home_connect::selector::programs::options::cooking_oven_program_subsequent_mode_microwave` | Microwave | Mikrovågsugn | Core-literal match |
| 13345 | 908724465 | `component::home_connect::selector::programs::options::cooking_oven_program_subsequent_mode_leave_to_rest` | Leave to rest | Låt vila | Core-literal match |
| 13346 | 908724464 | `component::home_connect::selector::programs::options::cooking_oven_program_subsequent_mode_keep_warm` | Keep warm | Håll varm | Core-literal match |
| 13347 | 908724463 | `component::home_connect::selector::programs::options::cooking_oven_program_subsequent_mode_continue_cooking` | Continue cooking | Fortsätt tillagningen | Core-literal match |
| 13348 | 908724462 | `component::home_connect::selector::programs::options::cooking_oven_program_steam_modes_reheat` | Reheat | Uppvärmning | Core-literal match |
| 13349 | 908724461 | `component::home_connect::selector::programs::options::cooking_oven_program_steam_modes_dough_proving` | Dough proving | Jäsning av deg | Core-literal match |
| 13350 | 908724460 | `component::home_connect::selector::programs::options::cooking_oven_program_heating_mode_let_rest` | Let rest | Låt vila | Core-literal match |
| 13351 | 908724459 | `component::home_connect::selector::programs::options::cooking_oven_program_heating_mode_full_surface_grill` | Full surface grill | Grill, stor yta | Core-literal match |
| 13352 | 908724458 | `component::home_connect::selector::programs::options::cooking_oven_program_heating_mode_2_d_hot_air` | 2D hot air | 2D-varmluft | Core-literal match |
| 13353 | 908724457 | `component::home_connect::selector::programs::options::cooking_oven_program_dish_subsequent_cooking` | Subsequent cooking | Efterföljande tillagning | Core-literal match |
| 13354 | 908724456 | `component::home_connect::selector::programs::options::cooking_oven_program_dish_recommendation_full_steam_broccoli` | Broccoli | Broccoli | Core-literal match |
| 13355 | 908724455 | `component::home_connect::selector::programs::options::cooking_oven_program_dish_recommendation_conv_steam_part_cooked_bread_rolls_or_baguette` | Part cooked bread rolls or baguette | Delvis tillagade frallor eller baguette | Core-literal match |
| 13356 | 908724454 | `component::home_connect::selector::programs::options::cooking_oven_program_dish_recommendation_conv_steam_meat_probe_turkey_breast` | Turkey breast | Kalkonbröst | Core-literal match |
| 13357 | 908724453 | `component::home_connect::selector::programs::options::cooking_oven_program_dish_recommendation_conv_steam_meat_probe_boneless_pork_neck_joint` | Boneless pork neck joint | Benfri fläskhals | Core-literal match |
| 13358 | 908724452 | `component::home_connect::selector::programs::options::cooking_oven_program_dish_recommendation_conv_meat_probe_goose_breast` | Goose breast | Gåsbröst | Core-literal match |
| 13359 | 908724451 | `component::home_connect::selector::programs::options::cooking_oven_program_dish_automatic_microwave_pommes_frites` | Pommes frites | Pommes frites | Core-literal match |
| 13360 | 908724450 | `component::home_connect::selector::programs::options::cooking_oven_program_dish_automatic_microwave_haehnchenteile` | Chicken pieces | Kycklingbitar | Core-literal match |
| 13361 | 908724449 | `component::home_connect::selector::programs::options::cooking_oven_program_dish_automatic_microwave_gefluegelteile_auftauen` | Poultry defrost | Upptining av fjäderfä | Core-literal match |
| 13362 | 908724448 | `component::home_connect::selector::programs::options::cooking_oven_program_dish_automatic_conv_steam_boneless_pork_neck_joint` | Boneless pork neck joint | Benfri fläskhals | Core-literal match |
| 13363 | 908724447 | `component::home_connect::selector::programs::options::cooking_oven_program_cleaning_pyrolysis` | Pyrolysis | Pyrolys | Core-literal match |
| 13364 | 908724446 | `component::home_connect::selector::programs::options::cooking_oven_program_cleaning_modes_auto_steam_calibration` | Auto steam calibration | Automatisk ångkalibrering | Core-literal match |
| 13365 | 908724445 | `component::home_connect::selector::programs::options::cooking_oven_program_cleaning_ecolysis` | Ecolysis | Ekolys | Core-literal match |
| 13366 | 908724444 | `component::home_connect::selector::programs::options::cooking_oven_program_cleaning_drying` | Drying | Torkning | Core-literal match |
| 13367 | 908724443 | `component::home_connect::selector::programs::options::cooking_oven_program_cleaning_draining` | Draining | Dränering | Core-literal match |
| 13368 | 908724442 | `component::home_connect::selector::programs::options::cooking_hob_program_power_move_mode` | Power move mode | Effekt rörelseläge | Core-literal match |
| 13369 | 908724441 | `component::home_connect::selector::programs::options::cooking_hob_program_power_level_mode` | Power level mode | Effektnivåläge | Core-literal match |
| 13370 | 908724440 | `component::home_connect::selector::programs::options::cooking_hob_program_frying_sensor_mode` | Frying sensor mode | Steksensorläge | Core-literal match |
| 13371 | 908724439 | `component::home_connect::selector::programs::options::cooking_common_program_hood_interval` | Interval | Intervall | Core-literal match |
| 13372 | 908724438 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_my_coffee_my_coffee_8` | My coffee 8 | Mitt kaffe 8 | Core-literal match |
| 13373 | 908724437 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_my_coffee_my_coffee_7` | My coffee 7 | Mitt kaffe 7 | Core-literal match |
| 13374 | 908724436 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_my_coffee_my_coffee_6` | My coffee 6 | Mitt kaffe 6 | Core-literal match |
| 13375 | 908724435 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_my_coffee_my_coffee_5` | My coffee 5 | Mitt kaffe 5 | Core-literal match |
| 13376 | 908724434 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_my_coffee_my_coffee_4` | My coffee 4 | Mitt kaffe 4 | Core-literal match |
| 13377 | 908724433 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_my_coffee_my_coffee_3` | My coffee 3 | Mitt kaffe 3 | Core-literal match |
| 13378 | 908724432 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_my_coffee_my_coffee_2` | My coffee 2 | Mitt kaffe 2 | Core-literal match |
| 13379 | 908724431 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_my_coffee_my_coffee_1` | My coffee 1 | Mitt kaffe 1 | Core-literal match |
| 13380 | 908724430 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_coffee_world_slow_brew` | Slow brew | Långsam bryggning | Core-literal match |
| 13381 | 908724429 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_coffee_world_cold_brew_macchiato` | Cold brew macchiato | Kallbryggd macchiato | Core-literal match |
| 13382 | 908724428 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_coffee_world_cold_brew` | Cold brew | Kallbryggt kaffe | Core-literal match |
| 13383 | 908724427 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_rinse_milk_system` | Rinse milk system | Skölj mjölksystemet | Core-literal match |
| 13384 | 908724426 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_replace_water_filter` | Replace water filter | Byt vattenfilter | Core-literal match |
| 13385 | 908724425 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_remove_water_filter` | Remove water filter | Ta bort vattenfiltret | Core-literal match |
| 13386 | 908724424 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_frost_protection` | Frost protection | Frostskydd | Core-literal match |
| 13387 | 908724423 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_descale` | Descale | Avkalka | Core-literal match |
| 13388 | 908724422 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_clean_outlet_manually` | Clean outlet manually | Rengör utloppet manuellt | Core-literal match |
| 13389 | 908724421 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_clean_brewing_unit_manually_detailed` | Clean brewing unit manually detailed | Rengör bryggenheten manuellt i detalj | Core-literal match |
| 13390 | 908724420 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_clean_brewing_unit_manually` | Clean brewing unit manually | Rengör bryggenheten manuellt | Core-literal match |
| 13391 | 908724419 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_clean` | Clean | Rengör | Core-literal match |
| 13392 | 908724418 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_calc_n_clean` | Calc'N'Clean | Calc'N'Clean | Core-literal match |
| 13393 | 908724417 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_auto_descale` | Auto descale | Automatisk avkalkning | Core-literal match |
| 13394 | 908724416 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_auto_clean` | Auto clean | Automatisk rengöring | Core-literal match |
| 13395 | 908724415 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_appliance_on_rinsing` | Appliance on rinsing | Sköljning vid påslagning | Core-literal match |
| 13396 | 908724414 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_cleaning_modes_appliance_off_rinsing` | Appliance off rinsing | Sköljning vid avstängning | Core-literal match |
| 13397 | 908724413 | `component::home_connect::selector::programs::options::consumer_products_coffee_maker_program_beverage_coffee_pot` | Coffee pot | Kaffekanna | Core-literal match |
| 13398 | 908724412 | `component::home_connect::entity::select::selected_program::state::laundry_care_washer_program_wash_and_dry_90` | Wash and dry 90 min | Tvätta och torka 90 min | Shared reference target checked |
| 13399 | 908724411 | `component::home_connect::entity::select::selected_program::state::laundry_care_washer_program_wash_and_dry_60` | Wash and dry 60 min | Tvätta och torka 60 min | Shared reference target checked |
| 13400 | 908724410 | `component::home_connect::entity::select::selected_program::state::laundry_care_washer_program_super_153045_super_30` | Super 30 min | Super 30 min | Shared reference target checked |
| 13401 | 908724409 | `component::home_connect::entity::select::selected_program::state::laundry_care_washer_program_steaming_steaming` | Steaming | Ångbehandling | Shared reference target checked |
| 13402 | 908724408 | `component::home_connect::entity::select::selected_program::state::laundry_care_washer_program_sport_shoes` | Sport shoes | Sportskor | Shared reference target checked |
| 13403 | 908724407 | `component::home_connect::entity::select::selected_program::state::laundry_care_washer_program_my_time` | My time | Min tid | Shared reference target checked |
| 13404 | 908724406 | `component::home_connect::entity::select::selected_program::state::laundry_care_washer_dryer_program_wool` | Wool | Ull | Shared reference target checked |
| 13405 | 908724405 | `component::home_connect::entity::select::selected_program::state::laundry_care_washer_dryer_program_spin` | Spin | Centrifugering | Shared reference target checked |
| 13406 | 908724404 | `component::home_connect::entity::select::selected_program::state::laundry_care_washer_dryer_program_sensitive` | Sensitive | Känslig | Shared reference target checked |
| 13407 | 908724403 | `component::home_connect::entity::select::selected_program::state::laundry_care_washer_dryer_program_rinse` | Rinse | Sköljning | Shared reference target checked |
| 13408 | 908724402 | `component::home_connect::entity::select::selected_program::state::laundry_care_washer_dryer_program_drum_clean_and_dry_drum_care` | Drum care | Trumvård | Shared reference target checked |
| 13409 | 908724401 | `component::home_connect::entity::select::selected_program::state::laundry_care_washer_dryer_program_delicates_silk` | Delicates silk | Fintvätt och siden | Shared reference target checked |
| 13410 | 908724400 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_wool_finish` | Wool finish | Ullfinish | Shared reference target checked |
| 13411 | 908724399 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_time_cold_air_fluff` | Air fluff | Vädring med kalluft | Shared reference target checked |
| 13412 | 908724398 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_outdoor_sportswear` | Sportswear | Sportkläder | Shared reference target checked |
| 13413 | 908724397 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_maintenance_care_2_maintenance_care_2_depth_care` | Depth care | Djupgående vård | Shared reference target checked |
| 13414 | 908724396 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_maintenance_care_1_maintenance_care_1_quick_care` | Quick care | Snabbvård | Shared reference target checked |
| 13415 | 908724395 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_in_basket_wool_basket` | Wool basket | Ullkorg | Shared reference target checked |
| 13416 | 908724394 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_easy_care_easy_care` | Easy care | Lättskött | Shared reference target checked |
| 13417 | 908724393 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_cotton_eco_4060` | Cotton eco 40/60ºC | Bomull eko 40/60 °C | Shared reference target checked |
| 13418 | 908724392 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_cotton_cotton_eco` | Cotton eco | Bomull eko | Shared reference target checked |
| 13419 | 908724391 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_connected_dry` | Connected dry | Ansluten torr | Shared reference target checked |
| 13420 | 908724390 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_cold_refresh_cold_refresh_cold_refresh` | Cold refresh | Kall uppfriskning | Shared reference target checked |
| 13421 | 908724389 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_cold_refresh_business` | Cold refresh - Business | Kall uppfräschning – affärskläder | Shared reference target checked |
| 13422 | 908724388 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_cold_refresh_5_piece` | Cold refresh - 5 piece | Kall uppfriskning - 5 stycken | Shared reference target checked |
| 13423 | 908724387 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_cold_refresh_1_piece` | Cold refresh - 1 piece | Kall uppfriskning - 1 styck | Shared reference target checked |
| 13424 | 908724386 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_business_shirts_easy_iron` | Business shirts - Easy iron | Skjortor – lättstruket | Shared reference target checked |
| 13425 | 908724385 | `component::home_connect::entity::select::selected_program::state::laundry_care_dryer_program_bedlinens` | Bed linens | Sängkläder | Shared reference target checked |
| 13426 | 908724384 | `component::home_connect::entity::select::selected_program::state::dishcare_dishwasher_program_quick_d` | Quick d | Snabb d | Shared reference target checked |
| 13427 | 908724383 | `component::home_connect::entity::select::selected_program::state::dishcare_dishwasher_program_max_efficient` | Max efficient | Maximal effektivitet | Shared reference target checked |
| 13428 | 908724382 | `component::home_connect::entity::select::selected_program::state::dishcare_dishwasher_program_glass_shine` | Glass shine | Glasglans | Shared reference target checked |
| 13429 | 908724381 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_subsequent_mode_microwave` | Microwave | Mikrovågsugn | Shared reference target checked |
| 13430 | 908724380 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_subsequent_mode_leave_to_rest` | Leave to rest | Låt vila | Shared reference target checked |
| 13431 | 908724379 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_subsequent_mode_keep_warm` | Keep warm | Håll varm | Shared reference target checked |
| 13432 | 908724378 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_subsequent_mode_continue_cooking` | Continue cooking | Fortsätt tillagningen | Shared reference target checked |
| 13433 | 908724377 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_steam_modes_reheat` | Reheat | Uppvärmning | Shared reference target checked |
| 13434 | 908724376 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_steam_modes_dough_proving` | Dough proving | Jäsning av deg | Shared reference target checked |
| 13435 | 908724375 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_heating_mode_let_rest` | Let rest | Låt vila | Shared reference target checked |
| 13436 | 908724374 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_heating_mode_full_surface_grill` | Full surface grill | Grill, stor yta | Shared reference target checked |
| 13437 | 908724373 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_heating_mode_2_d_hot_air` | 2D hot air | 2D-varmluft | Shared reference target checked |
| 13438 | 908724372 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_dish_subsequent_cooking` | Subsequent cooking | Efterföljande tillagning | Shared reference target checked |
| 13439 | 908724371 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_dish_recommendation_full_steam_broccoli` | Broccoli | Broccoli | Shared reference target checked |
| 13440 | 908724370 | `component::home_connect::entity::select::selected_program::state::cooking_oven_program_dish_recommendation_conv_steam_part_cooked_bread_rolls_or_baguette` | Part cooked bread rolls or baguette | Delvis tillagade frallor eller baguette | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
