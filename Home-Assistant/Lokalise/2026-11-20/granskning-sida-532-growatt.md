# Home Assistant Core – svensk granskning, sida 532

Datum: 2026-11-20  
Status: sparat och återläst i Lokalise

Granskade nycklar omfattar Growatt Server. Etiketterna harmoniserades med elnät-, PV- och livstidstermer från de föregående Growatt-sidorna.

| Fullständig nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::growatt_server::entity::sensor::mix_import_from_grid_today_combined::name` | `Import från nätet i dag (last + laddning)` | `Import från elnätet i dag (last + laddning)` | Konsekvent och exakt nätterm. |
| `component::growatt_server::entity::sensor::mix_last_update::name` | `Senaste datauppdatering` | `Senaste datauppdateringen` | Korrekt bestämd form. |
| `component::growatt_server::entity::sensor::mix_load_consumption_lifetime::name` | `Elförbrukning totalt livslängd` | `Ackumulerad elförbrukning` | Naturlig term för livstidstotal. |
| `component::growatt_server::entity::sensor::mix_load_consumption_total::name` | `Elförbrukning totalt livslängd` | `Ackumulerad total elförbrukning` | Naturlig term för total livstidstotal. |
| `component::growatt_server::entity::sensor::mix_pv1_voltage::name` | `PV1 spänning` | `PV1-spänning` | Korrekt bindestreck med förkortning. |
| `component::growatt_server::entity::sensor::mix_pv2_voltage::name` | `PV2 spänning` | `PV2-spänning` | Korrekt bindestreck med förkortning. |
| `component::growatt_server::entity::sensor::mix_solar_generation_today::name` | `Solproduktion i dag` | `Solenergiproduktion i dag` | Tydliggör energistorheten. |
| `component::growatt_server::entity::sensor::mix_system_production_today::name` | `Systemproduktion i dag (egenkonsumtion + export)` | `Systemproduktion i dag (egenförbrukning + export)` | Konsekvent svensk elterm. |
| `component::growatt_server::entity::sensor::mix_wattage_pv_1::name` | `PV1 effekt` | `PV1-effekt` | Korrekt bindestreck med förkortning. |
| `component::growatt_server::entity::sensor::mix_wattage_pv_2::name` | `PV2 effekt` | `PV2-effekt` | Korrekt bindestreck med förkortning. |
| `component::growatt_server::entity::sensor::mix_wattage_pv_all::name` | `Alla solceller effekt` | `Total PV-effekt` | Korrekt svensk term och ordföljd. |
| `component::growatt_server::entity::sensor::storage_ac_output_frequency::name` | `AC utgångsfrekvens` | `AC-utgångsfrekvens` | Korrekt sammansättning. |
