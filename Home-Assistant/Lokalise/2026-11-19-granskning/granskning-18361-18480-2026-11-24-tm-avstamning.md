# Home Assistant Core – historisk avstämning 18361–18480

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 93 direkta källtexter matchar HA Core-källan; 22 referensanvändningar med 13 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 5 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 18361 | 853488078 | `component::guntamatic::entity::sensor::program::state::hibernate` | Setback mode | Temperatursänkningsläge | Core-literal match |
| 18362 | 853488077 | `component::guntamatic::entity::sensor::program::state::heat` | Heat | Värme | Core-literal match |
| 18363 | 853488076 | `component::guntamatic::entity::sensor::program::state::dhw_boost` | Domestic hot water boost | Varmvattenboost | Core-literal match |
| 18364 | 853488075 | `component::guntamatic::entity::sensor::program::state::dhw` | Domestic hot water | Varmvatten för hushållsbruk | Core-literal match |
| 18365 | 853488074 | `component::guntamatic::entity::sensor::program::name` | Program | Program | Core-literal match |
| 18366 | 853488073 | `component::guntamatic::entity::sensor::outdoor_temperature::name` | Outdoor temperature | Utomhustemperatur | Core-literal match |
| 18367 | 853488072 | `component::guntamatic::entity::sensor::domestic_hot_water_0_temperature::name` | Domestic hot water circuit 0 temperature | Temperatur för varmvattenkrets 0 | Core-literal match |
| 18368 | 853488071 | `component::guntamatic::entity::sensor::buffer_top_temperature::name` | Buffer top temperature | Temperatur i buffertens övre del | Core-literal match |
| 18369 | 853488070 | `component::guntamatic::entity::sensor::buffer_load::name` | Buffer load | Buffertlast | Core-literal match |
| 18370 | 853488069 | `component::guntamatic::entity::sensor::buffer_center_temperature::name` | Buffer center temperature | Temperatur i buffertens mitt | Core-literal match |
| 18371 | 853488068 | `component::guntamatic::entity::sensor::buffer_bottom_temperature::name` | Buffer bottom temperature | Temperatur i buffertens nedre del | Core-literal match |
| 18372 | 853488067 | `component::guntamatic::entity::sensor::boiler_temperature::name` | Boiler temperature | Panntemperatur | Core-literal match |
| 18373 | 853488066 | `component::guntamatic::config::step::user::data_description::host` | The hostname or IP address of your Guntamatic heater. | Värdnamn eller IP-adress för din Guntamatic-värmare. | Core-literal match |
| 18374 | 853488065 | `component::guntamatic::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 18375 | 853488064 | `component::guntamatic::config::step::discovery_confirm::title` | Discovered Guntamatic heater | Upptäckta Guntamatic-värmare | Core-literal match |
| 18376 | 853488063 | `component::guntamatic::config::step::discovery_confirm::description` | Do you want to set up this Guntamatic heater? | Vill du konfigurera den här Guntamatic-värmaren? | Core-literal match |
| 18377 | 853488062 | `component::guntamatic::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 18378 | 853488061 | `component::guntamatic::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18379 | 853488060 | `component::guntamatic::config::error::bad_data` | The heater did not provide the required identification information. Verify that the host points to a supported controller and the correct endpoint. | Värmaren tillhandahöll inte den nödvändiga identifieringsinformationen. Kontrollera att värden pekar på en stödd styrenhet och rätt slutpunkt. | Core-literal match |
| 18380 | 853488059 | `component::guntamatic::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18381 | 853488058 | `component::guntamatic::config::abort::bad_data` | The heater did not provide the required identification information. Verify that the host points to a supported controller and the correct endpoint. | Värmaren tillhandahöll inte den nödvändiga identifieringsinformationen. Kontrollera att värden pekar på en stödd styrenhet och rätt slutpunkt. | Core-literal match |
| 18382 | 853488057 | `component::guntamatic::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 18383 | 853466279 | `component::fritzbox::config::step::user::data_description::username` | Name of the user to connect Home Assistant to your FRITZ!Box. | Namn på användaren som ska ansluta Home Assistant till din FRITZ!Box. | Shared reference target checked |
| 18384 | 853466278 | `component::fritzbox::config::step::user::data_description::password` | Password for the user to connect Home Assistant to your FRITZ!Box. | Lösenord för användaren som ska ansluta Home Assistant till din FRITZ!Box. | Shared reference target checked |
| 18385 | 853466277 | `component::fritzbox::config::step::reauth_confirm::data_description::username` | Name of the user to connect Home Assistant to your FRITZ!Box. | Namn på användaren som ska ansluta Home Assistant till din FRITZ!Box. | Shared reference target checked |
| 18386 | 853466276 | `component::fritzbox::config::step::reauth_confirm::data_description::password` | Password for the user to connect Home Assistant to your FRITZ!Box. | Lösenord för användaren som ska ansluta Home Assistant till din FRITZ!Box. | Shared reference target checked |
| 18387 | 853466275 | `component::fritzbox::config::step::confirm::data_description::username` | Name of the user to connect Home Assistant to your FRITZ!Box. | Namn på användaren som ska ansluta Home Assistant till din FRITZ!Box. | Shared reference target checked |
| 18388 | 853466274 | `component::fritzbox::config::step::confirm::data_description::password` | Password for the user to connect Home Assistant to your FRITZ!Box. | Lösenord för användaren som ska ansluta Home Assistant till din FRITZ!Box. | Shared reference target checked |
| 18389 | 853466273 | `component::fritzbox::common::data_description_username` | Name of the user to connect Home Assistant to your FRITZ!Box. | Namn på användaren som ska ansluta Home Assistant till din FRITZ!Box. | Core-literal match |
| 18390 | 853466272 | `component::fritzbox::common::data_description_password` | Password for the user to connect Home Assistant to your FRITZ!Box. | Lösenord för användaren som ska ansluta Home Assistant till din FRITZ!Box. | Core-literal match |
| 18391 | 853466271 | `component::fritzbox::common::data_description_host` | The hostname or IP address of your FRITZ!Box router. | Värdnamnet eller IP-adressen för din FRITZ!Box-router. | Source-path follow-up open |
| 18392 | 853418303 | `component::data_grand_lyon::entity::binary_sensor::station_open::name` | Station open | Station öppen | Core-literal match |
| 18393 | 853143492 | `component::victron_gx::entity::button::platform_device_reboot::name` | Device reboot | Omstart av enhet | Core-literal match |
| 18394 | 853025816 | `component::lg_infrared::entity::button::power::name` | Power | På/Av | Shared reference target checked |
| 18395 | 852900341 | `component::asuswrt::config::error::pwd_and_ssh` | Please provide either password or SSH key file, not both | Ange antingen lösenord eller SSH-nyckelfil, inte båda | Core-literal match |
| 18396 | 852900284 | `component::workday::selector::category::options::yazidi` | Yazidi | Yazidi | Core-literal match |
| 18397 | 852900283 | `component::workday::selector::category::options::vlach` | Vlach | Vlach | Core-literal match |
| 18398 | 852900282 | `component::workday::selector::category::options::turkish` | Turkish | Turkiska | Core-literal match |
| 18399 | 852900281 | `component::workday::selector::category::options::serbian` | Serbian | Serbiska | Core-literal match |
| 18400 | 852900280 | `component::workday::selector::category::options::sabian` | Sabian | Sabianska | Core-literal match |
| 18401 | 852900279 | `component::workday::selector::category::options::roma` | Roma | Roma | Core-literal match |
| 18402 | 852900278 | `component::workday::selector::category::options::protestant` | Protestant | Protestantiska | Core-literal match |
| 18403 | 852900277 | `component::workday::selector::category::options::orthodox` | Orthodox | Ortodoxa | Core-literal match |
| 18404 | 852900276 | `component::workday::selector::category::options::de_facto` | De facto | De facto | Core-literal match |
| 18405 | 852900275 | `component::workday::selector::category::options::bosnian` | Bosnian | Bosniska | Core-literal match |
| 18406 | 852900274 | `component::workday::selector::category::options::armenian` | Armenian | Armeniska | Core-literal match |
| 18407 | 852900273 | `component::workday::selector::category::options::albanian` | Albanian | Albanska | Core-literal match |
| 18408 | 852898343 | `component::ohme::entity::switch::solar_boost::name` | Solar boost | Solboost | Core-literal match |
| 18409 | 852898021 | `component::asuswrt::config::step::user::sections::more_options::name` | More options | Fler alternativ | Core-literal match |
| 18410 | 852898020 | `component::asuswrt::config::step::user::sections::more_options::data::ssh_key` | Path to your SSH key file (instead of password) | Sökväg till din SSH-nyckelfil (istället för lösenord) | Core-literal match |
| 18411 | 852898019 | `component::asuswrt::config::step::user::sections::more_options::data::port` | Port (leave empty for protocol default) | Port (lämna tomt för standard) | Core-literal match |
| 18412 | 852880615 | `component::weatherflow_cloud::entity::sensor::uv_index::name` | UV index | UV-index | Core-literal match |
| 18413 | 852880614 | `component::weatherflow_cloud::entity::sensor::solar_radiation::name` | Solar radiation | Solstrålning | Core-literal match |
| 18414 | 852880613 | `component::weatherflow_cloud::entity::sensor::relative_humidity::name` | Relative humidity | Relativ luftfuktighet | Core-literal match |
| 18415 | 852880612 | `component::weatherflow_cloud::entity::sensor::illuminance::name` | Illuminance | Belysningsstyrka | Source-path follow-up open |
| 18416 | 852832846 | `component::unifi::options::step::init::sections::more_options::name` | More options | Fler alternativ | Core-literal match |
| 18417 | 852832845 | `component::unifi::options::step::init::sections::more_options::data_description::track_wired_clients` | Include wired clients in device tracking. | Inkludera trådbundna klienter i enhetsspårningen. | Core-literal match |
| 18418 | 852832844 | `component::unifi::options::step::init::sections::more_options::data_description::ssid_filter` | Only track wireless clients connected to selected SSIDs. | Spåra endast trådlösa klienter anslutna till utvalda SSID:er. | Core-literal match |
| 18419 | 852832843 | `component::unifi::options::step::init::sections::more_options::data_description::ignore_wired_bug` | Disable workaround for a UniFi Network bug that sometimes reports wired clients as wireless. | Inaktivera lösningen för ett UniFi Network-fel som ibland rapporterar trådbundna klienter som trådlösa. | Core-literal match |
| 18420 | 852832842 | `component::unifi::options::step::init::sections::more_options::data_description::dpi_restrictions` | Enable switches to control DPI restriction groups. | Aktivera växlar för att styra DPI-begränsningsgrupper. | Core-literal match |
| 18421 | 852832841 | `component::unifi::options::step::init::sections::more_options::data_description::detection_time` | Number of seconds since last seen before a client is considered away. | Antal sekunder sedan senast sedd innan en klient anses vara borta. | Core-literal match |
| 18422 | 852832840 | `component::unifi::options::step::init::sections::more_options::data_description::client_source` | Select which network clients to create entities from. | Välj vilka nätverksklienter du vill skapa enheter från. | Core-literal match |
| 18423 | 852832839 | `component::unifi::options::step::init::sections::more_options::data_description::allow_uptime_sensors` | Create uptime sensors for network clients. | Skapa sensorer för drifttid för nätverksklienter. | Core-literal match |
| 18424 | 852832838 | `component::unifi::options::step::init::sections::more_options::data_description::allow_bandwidth_sensors` | Create bandwidth usage sensors for network clients. | Skapa sensorer för bandbreddsanvändning för nätverksklienter. | Core-literal match |
| 18425 | 852832837 | `component::unifi::options::step::init::sections::more_options::data::track_wired_clients` | Include wired network clients | Inkludera klienter i trådbundna nätverk | Core-literal match |
| 18426 | 852832836 | `component::unifi::options::step::init::sections::more_options::data::ssid_filter` | Select SSIDs to track wireless clients on | Välj SSID för att spåra trådlösa klienter på | Core-literal match |
| 18427 | 852832835 | `component::unifi::options::step::init::sections::more_options::data::ignore_wired_bug` | Disable UniFi Network wired bug logic | Inaktivera bugglogik för trådbunden UniFi-nätverk | Core-literal match |
| 18428 | 852832834 | `component::unifi::options::step::init::sections::more_options::data::dpi_restrictions` | Allow control of DPI restriction groups | Tillåt kontroll av DPI-restriktionsgrupper | Core-literal match |
| 18429 | 852832833 | `component::unifi::options::step::init::sections::more_options::data::detection_time` | Time in seconds from last seen until considered away | Tid i sekunder från senast sedd tills betraktad som borta | Core-literal match |
| 18430 | 852832832 | `component::unifi::options::step::init::sections::more_options::data::client_source` | Create entities from network clients | Skapa entiteter från nätverksklienter | Core-literal match |
| 18431 | 852832831 | `component::unifi::options::step::init::sections::more_options::data::allow_uptime_sensors` | Uptime sensors for network clients | Sensorer för nätverklienters upptid | Core-literal match |
| 18432 | 852832830 | `component::unifi::options::step::init::sections::more_options::data::allow_bandwidth_sensors` | Bandwidth usage sensors for network clients | Sensorer för nätverksklienters bandbreddsanvändning | Core-literal match |
| 18433 | 852832829 | `component::unifi::options::step::init::data_description::track_devices` | Create device tracker entities for Ubiquiti network devices. | Skapa enhetsspårningsentiteter för Ubiquiti-nätverksenheter. | Core-literal match |
| 18434 | 852832828 | `component::unifi::options::step::init::data_description::track_clients` | Create device tracker entities for network clients. | Skapa enhetsspårningsentiteter för nätverksklienter. | Core-literal match |
| 18435 | 852832827 | `component::unifi::options::step::init::data_description::block_client` | Select clients whose network access you want to control via switches. | Välj klienter vars nätverksåtkomst du vill styra via brytare. | Core-literal match |
| 18436 | 852832826 | `component::unifi::options::step::init::data::track_devices` | Track network devices (Ubiquiti devices) | Spåra nätverksenheter (Ubiquiti-enheter) | Core-literal match |
| 18437 | 852832825 | `component::unifi::options::step::init::data::track_clients` | Track network clients | Spåra nätverksklienter | Core-literal match |
| 18438 | 852832824 | `component::unifi::options::step::init::data::block_client` | Network access controlled clients | Klienter vars nätverksåtkomst kontrolleras | Core-literal match |
| 18439 | 852831851 | `component::data_grand_lyon::exceptions::update_failed_all::message` | Error fetching Data Grand Lyon data: all requests failed. | Fel vid hämtning av data från Data Grand Lyon: alla förfrågningar misslyckades. | Source-path follow-up open |
| 18440 | 852831850 | `component::data_grand_lyon::entity::sensor::electrical_removable_battery_bikes::unit_of_measurement` | bikes | cyklar | Shared reference target checked |
| 18441 | 852831849 | `component::data_grand_lyon::entity::sensor::electrical_removable_battery_bikes::name` | Electrical removable battery bikes | Elcyklar med löstagbart batteri | Core-literal match |
| 18442 | 852831848 | `component::data_grand_lyon::entity::sensor::electrical_internal_battery_bikes::unit_of_measurement` | bikes | cyklar | Shared reference target checked |
| 18443 | 852831847 | `component::data_grand_lyon::entity::sensor::electrical_internal_battery_bikes::name` | Electrical internal battery bikes | Elcyklar med inbyggt batteri | Core-literal match |
| 18444 | 852831846 | `component::data_grand_lyon::entity::sensor::capacity::unit_of_measurement` | stands | ställ | Shared reference target checked |
| 18445 | 852831845 | `component::data_grand_lyon::entity::sensor::capacity::name` | Capacity | Kapacitet | Core-literal match |
| 18446 | 852831844 | `component::data_grand_lyon::entity::sensor::available_stands::unit_of_measurement` | stands | ställ | Core-literal match |
| 18447 | 852831843 | `component::data_grand_lyon::entity::sensor::available_stands::name` | Available stands | Tillgängliga ställ | Core-literal match |
| 18448 | 852831842 | `component::data_grand_lyon::entity::sensor::available_mechanical_bikes::unit_of_measurement` | bikes | cyklar | Shared reference target checked |
| 18449 | 852831841 | `component::data_grand_lyon::entity::sensor::available_mechanical_bikes::name` | Available mechanical bikes | Tillgängliga mekaniska cyklar | Core-literal match |
| 18450 | 852831840 | `component::data_grand_lyon::entity::sensor::available_electrical_bikes::unit_of_measurement` | bikes | cyklar | Shared reference target checked |
| 18451 | 852831839 | `component::data_grand_lyon::entity::sensor::available_electrical_bikes::name` | Available electrical bikes | Tillgängliga elcyklar | Core-literal match |
| 18452 | 852831838 | `component::data_grand_lyon::entity::sensor::available_bikes::unit_of_measurement` | bikes | cyklar | Core-literal match |
| 18453 | 852831837 | `component::data_grand_lyon::entity::sensor::available_bikes::name` | Available bikes | Tillgängliga cyklar | Core-literal match |
| 18454 | 852831836 | `component::data_grand_lyon::config_subentries::velov_station::step::user::data::station_id` | Station | Station | Core-literal match |
| 18455 | 852831835 | `component::data_grand_lyon::config_subentries::velov_station::initiate_flow::user` | Add Vélo'v station | Lägg till Vélo'v-station | Core-literal match |
| 18456 | 852831834 | `component::data_grand_lyon::config_subentries::velov_station::entry_type` | Vélo'v station | Vélo'v-station | Core-literal match |
| 18457 | 852831833 | `component::data_grand_lyon::config_subentries::velov_station::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Shared reference target checked |
| 18458 | 852828639 | `component::androidtv::config::step::user::sections::more_options::name` | More options | Fler alternativ | Core-literal match |
| 18459 | 852828638 | `component::androidtv::config::step::user::sections::more_options::data::adbkey` | Path to your ADB key file (leave empty to auto generate) | Sökväg till din ADB-nyckelfil (lämna fältet tomt för automatisk generering) | Core-literal match |
| 18460 | 852828637 | `component::androidtv::config::step::user::sections::more_options::data::adb_server_port` | Port of the ADB server | Port för ADB-servern | Core-literal match |
| 18461 | 852828636 | `component::androidtv::config::step::user::sections::more_options::data::adb_server_ip` | IP address of the ADB server (leave empty to not use) | ADB-serverns IP-adress (lämna tomt om du inte vill använda den). | Core-literal match |
| 18462 | 852827667 | `component::kitchen_sink::config_subentries::infrared_fan::step::user::data::infrared_receiver_entity_id` | Infrared receiver | Infraröd mottagare | Shared reference target checked |
| 18463 | 852827666 | `component::kitchen_sink::config_subentries::infrared_fan::abort::no_infrared_entities` | No infrared entities found. Please set up an infrared device first. | Inga infraröda entiteter hittades. Konfigurera först en infraröd enhet. | Shared reference target checked |
| 18464 | 852827665 | `component::infrared::exceptions::receiver_not_found::message` | Infrared receiver entity `{entity_id}` not found | Den infraröda mottagarentiteten `{entity_id}` hittades inte | Core-literal match |
| 18465 | 852827664 | `component::infrared::entity_component::receiver::name` | Infrared receiver | Infraröd mottagare | Core-literal match |
| 18466 | 852827663 | `component::infrared::entity_component::_::name` | Infrared emitter | Infraröd sändare | Source-path follow-up open |
| 18467 | 852823703 | `component::sonarr::config::step::user::sections::more_options::name` | More options | Fler alternativ | Core-literal match |
| 18468 | 852823702 | `component::sonarr::config::step::user::sections::more_options::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 18469 | 852823603 | `component::nzbget::config::step::user::sections::more_options::name` | More options | Fler alternativ | Core-literal match |
| 18470 | 852823602 | `component::nzbget::config::step::user::sections::more_options::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 18471 | 852817806 | `component::onvif::options::step::onvif_devices::sections::more_options::name` | More options | Fler alternativ | Core-literal match |
| 18472 | 852817805 | `component::onvif::options::step::onvif_devices::sections::more_options::data::use_wallclock_as_timestamps` | Use wall clock as timestamps | Använd väggklocka som tidsstämplar | Core-literal match |
| 18473 | 852817410 | `component::risco::options::step::init::sections::more_options::name` | More options | Fler alternativ | Core-literal match |
| 18474 | 852817409 | `component::risco::options::step::init::sections::more_options::data::scan_interval` | How often to poll Risco Cloud (in seconds) | Hur ofta ska Risco Cloud pollas (i sekunder) | Source-path follow-up open |
| 18475 | 852817408 | `component::risco::options::step::init::sections::more_options::data::concurrency` | Maximum concurrent requests in Risco local | Maximalt antal samtidiga förfrågningar i Risco lokal | Core-literal match |
| 18476 | 852817390 | `component::coolmaster::config::step::user::sections::more_options::name` | More options | Fler alternativ | Core-literal match |
| 18477 | 852817389 | `component::coolmaster::config::step::user::sections::more_options::data_description::send_wakeup_prompt` | Send the coolmaster unit an empty command before issuing any actual command. This is required for serial models. | Skicka ett tomt kommando till CoolMaster-enheten innan du ger något egentligt kommando. Detta krävs för seriemodeller. | Core-literal match |
| 18478 | 852817388 | `component::coolmaster::config::step::user::sections::more_options::data::send_wakeup_prompt` | Send wakeup prompt | Skicka väckningsmeddelande | Core-literal match |
| 18479 | 852816882 | `component::cambridge_audio::entity::number::volume_limit::name` | Volume limit | Volymgräns | Core-literal match |
| 18480 | 852816764 | `component::backup::entity::event::automatic_backup_event::state_attributes::failed_reason::state::upload_failed` | Upload failed | Uppladdning misslyckades | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 853466271 | `component::fritzbox::common::data_description_host` | The hostname or IP address of your FRITZ!Box router. |
| 852880612 | `component::weatherflow_cloud::entity::sensor::illuminance::name` | Illuminance |
| 852831851 | `component::data_grand_lyon::exceptions::update_failed_all::message` | Error fetching Data Grand Lyon data: all requests failed. |
| 852827663 | `component::infrared::entity_component::_::name` | Infrared emitter |
| 852817409 | `component::risco::options::step::init::sections::more_options::data::scan_interval` | How often to poll Risco Cloud (in seconds) |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
