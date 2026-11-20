# Home Assistant Core — granskning sida 477 (Home Assistant Yellow, ZHA och Assist)

Datum: 2026-11-20  
Status: dokumenterade förslag; **inte sparade i Lokalise**

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::homeassistant_yellow::options::abort::write_hw_settings_error` | `Misslyckades med att skriva hårdvaruinställningar` | `Misslyckades med att skriva hårdvaruinställningarna` | Bestämd form ska vara konsekvent med motsvarande fel vid läsning av inställningarna. |
| `component::homeassistant_yellow::options::step::main_menu::menu_options::multipan_settings` | `Konfigurera IEEE 802.15.4 radio multiprotokoll stöd` | `Konfigurera stöd för multiprotokoll för IEEE 802.15.4-radio` | Korrigerar särskrivning, ordföljd och sammansättning i den tekniska menyn. |
| `component::zha::config::step::verify_radio::description` | `Den radio du använder ({name}) rekommenderas inte och stödet för den kan komma att tas bort i framtiden. Se Zigbee Home Automation-integrationens dokumentation för [en lista över rekommenderade adaptrar]({docs_recommended_adapters_url}).` | `Adaptern du använder ({name}) rekommenderas inte och stödet för den kan komma att tas bort i framtiden. Se Zigbee Home Automation-integrationens dokumentation för [en lista över rekommenderade adaptrar]({docs_recommended_adapters_url}).` | Källtexten avser en adapter; ”radio” är här både mindre precist och inkonsekvent med titelns ”Adapter”. Platshållare och länk bevaras. |
| `component::assist_pipeline::entity::binary_sensor::assist_in_progress::name` | `Assistans pågår` | `Assist pågår` | `Assist` är produktnamnet och ska inte ersättas med det svenska generiska ordet ”assistans”. |

Övriga 16 nycklar på sidan granskades utan dokumenterat ändringsförslag. Tre nycklar är direkta referenser; `component::esphome::entity::binary_sensor::assist_in_progress::name` följer Assist-postens måltext.
