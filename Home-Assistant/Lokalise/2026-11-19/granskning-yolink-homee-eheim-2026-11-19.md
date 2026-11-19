# Home Assistant Core: YoLink, homee och Eheim

Kontrollerat i Lokalise den 19 november 2026 och jämfört med Core-minnets ögonblicksbild från 24 oktober. Ingen ändring har gjorts i Lokalise. Filtrerade resultat är inte bevis för ett sammanhängande ofiltrerat intervall. Tidigare rapporter och GitHubs kodsökning gav ingen träff för sökt YoLink-nyckel.

| Fullständig nyckel | Engelska | Befintlig svenska | Bedömning |
|---|---|---|---|
| `component::yolink::entity::valve::meter_valve_2_state::name` | Valve 2 | Ventil 2 | Behåll. |
| `component::yolink::entity::valve::meter_valve_1_state::name` | Valve 1 | Ventil 1 | Behåll. |
| `component::yolink::entity::sensor::water_meter_2_reading::name` | Water meter 2 reading | Vattenmätaravläsning 2 | Föreslå: Avläsning av vattenmätare 2. Siffran kopplas tydligare till mätaren. |
| `component::yolink::entity::sensor::water_meter_1_reading::name` | Water meter 1 reading | Vattenmätaravläsning 1 | Föreslå: Avläsning av vattenmätare 1. |
| `component::homee::exceptions::disarm_not_supported::message` | Disarm is not supported by homee. | Avaktivering stöds inte av Homee. | Behåll tills vidare; kontrollera varumärkets skrivning och om larmkontexten motiverar ”frånkoppling”. |
| `component::homee::entity::alarm_control_panel::homee_mode::name` | Status | Status | Behåll. |
| `component::eheimdigital::entity::select::filter_mode::state::pulse` | Pulse | Puls | Behåll. |
| `component::eheimdigital::entity::select::filter_mode::state::manual` | Manual | Manuell | Behåll. |
| `component::eheimdigital::entity::select::filter_mode::state::bio` | Bio | Bio | Behåll; produktens lägesnamn. |
| `component::eheimdigital::entity::select::filter_mode::name` | Filter mode | Filterläge | Behåll. |

De tio käll- och måltexterna överensstämmer med den historiska TMX-katalogen. YoLink har även en motsvarande befintlig onumrerad etikett ”Avläsning av vattenmätare”, vilket stöder förslagen. FOSS-termbanken stöder bland annat valve → ventil, mode → läge och manual → manuell; dess generella reading → läser avser en annan användning. Hunspell-sv och svlang gav inga relevanta träffar för förslagen. Inga platshållare, referenser eller pluralstrukturer förekom. Kontrollera eventuell ofiltrerad mellanliggande ordning innan positionsnummer tilldelas.
