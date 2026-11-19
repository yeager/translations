# Sparade NWS-fält

Sparade och återlästa i Home Assistant Core i Lokalise 2026-11-19. Svenska fält var tomma före ändringen. De tre integrationsspecifika referensmålen har svensk text: stationskod ”METAR-stationskod”, platsentitet ”Platsentitet” och dess beskrivning ”Välj en person, enhetsspårare eller zon för att dynamiskt spåra vädret för dess plats.” Det gemensamma API-nyckelmålet kontrollerades i Lokalise: ”API key” / ”API-nyckel”.

| Fullständig nyckel | Engelska | Sparad svenska |
| --- | --- | --- |
| `component::nws::config::step::reconfigure::data_description::station` | If not specified, the closest station to the configured location will be used. | Om ingen station anges används stationen som ligger närmast den konfigurerade platsen. |
| `component::nws::config::step::reconfigure::data_description::location_entity` | [%key:component::nws::config::step::entity::data_description::location_entity%] | [%key:component::nws::config::step::entity::data_description::location_entity%] |
| `component::nws::config::step::reconfigure::data::station` | [%key:component::nws::config::step::location::data::station%] | [%key:component::nws::config::step::location::data::station%] |
| `component::nws::config::step::reconfigure::data::location_entity` | [%key:component::nws::config::step::entity::data::location_entity%] | [%key:component::nws::config::step::entity::data::location_entity%] |
| `component::nws::config::step::reconfigure::data::api_key` | [%key:common::config_flow::data::api_key%] | [%key:common::config_flow::data::api_key%] |
