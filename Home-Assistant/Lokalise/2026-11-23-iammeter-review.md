# Home Assistant Core – IAMMETER

Datum: 2026-11-23

Alla 21 aktuella etiketter hämtades och återlästes via Lokalise API. Tre
felaktigt segmenterade energi-termer sparades om; övriga poster behölls efter
kontroll mot källtext och etablerade Core-översättningar för importerad och
exporterad energi.

| Nyckel | Tidigare svenska | Sparad svenska | Bedömning |
| --- | --- | --- | --- |
| `component::iammeter::entity::sensor::current_a::name` | Ström A | Ström A | Korrekt. |
| `component::iammeter::entity::sensor::current_b::name` | Ström B | Ström B | Korrekt. |
| `component::iammeter::entity::sensor::current_c::name` | Ström C | Ström C | Korrekt. |
| `component::iammeter::entity::sensor::export_grid_a::name` | Nätexport A | Nätexport A | Korrekt. |
| `component::iammeter::entity::sensor::export_grid_b::name` | Nätexport B | Nätexport B | Korrekt. |
| `component::iammeter::entity::sensor::export_grid_c::name` | Nätexport C | Nätexport C | Korrekt. |
| `component::iammeter::entity::sensor::frequency_a::name` | Frekvens A | Frekvens A | Korrekt. |
| `component::iammeter::entity::sensor::frequency_b::name` | Frekvens B | Frekvens B | Korrekt. |
| `component::iammeter::entity::sensor::frequency_c::name` | Frekvens C | Frekvens C | Korrekt. |
| `component::iammeter::entity::sensor::import_energy_a::name` | Import Energi A | Importerad energi A | Följer Core-termen `Importerad energi`. |
| `component::iammeter::entity::sensor::import_energy_b::name` | Import Energi B | Importerad energi B | Följer Core-termen `Importerad energi`. |
| `component::iammeter::entity::sensor::import_energy_c::name` | Import Energi C | Importerad energi C | Följer Core-termen `Importerad energi`. |
| `component::iammeter::entity::sensor::pf_a::name` | PF A | PF A | Källans fackförkortning bevarad. |
| `component::iammeter::entity::sensor::pf_b::name` | PF B | PF B | Källans fackförkortning bevarad. |
| `component::iammeter::entity::sensor::pf_c::name` | PF C | PF C | Källans fackförkortning bevarad. |
| `component::iammeter::entity::sensor::power_a::name` | Effekt A | Effekt A | Korrekt. |
| `component::iammeter::entity::sensor::power_b::name` | Effekt B | Effekt B | Korrekt. |
| `component::iammeter::entity::sensor::power_c::name` | Effekt C | Effekt C | Korrekt. |
| `component::iammeter::entity::sensor::voltage_a::name` | Spänning A | Spänning A | Korrekt. |
| `component::iammeter::entity::sensor::voltage_b::name` | Spänning B | Spänning B | Korrekt. |
| `component::iammeter::entity::sensor::voltage_c::name` | Spänning C | Spänning C | Korrekt. |

Inga platshållare, pluralformer eller referenser förekommer. svlang gav 10,0
utan anmärkningar och hunspell godkände termen. Manifestet är återläst från
Lokalise och tillagt i det validerade Home Assistant-TMX-minnet.
