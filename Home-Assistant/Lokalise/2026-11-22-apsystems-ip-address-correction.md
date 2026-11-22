# Home Assistant Core – APsystems: felkopplad IP-adress

Live-kontroll av `component::apsystems::config::step::user::data::ip_address`
visade att den svenska texten felaktigt var `Total livstidsproduktion`, trots
källan `IP address`. Den rättades till `IP-adress` och återlästes via API.

Detta korrigerar en tidigare APsystems-granskning där sensoröversättningen
råkade kopplas till konfigurationsnyckeln. Sensorposten för
`lifetime_production` har ett eget live-ID och påverkas inte av denna rättning.
