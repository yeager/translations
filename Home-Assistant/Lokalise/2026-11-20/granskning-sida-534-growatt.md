# Home Assistant Core – svensk granskning, sida 534

Datum: 2026-11-20  
Status: sparat och återläst i Lokalise

Granskade nycklar omfattar Growatt Server. Rättningen följer etablerade mönster för batteriladdning, urladdning och ackumulerade livstidstal.

| Fullständig nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::growatt_server::entity::sensor::storage_power_flow::name` | `Batteri laddning/urladdning` | `Batteriladdning/batteriurladdning` | Korrekt svenska sammansättningar. |
| `component::growatt_server::entity::sensor::storage_pv_charging_voltage::name` | `PV1 laddningsspänning` | `PV1-laddningsspänning` | Korrekt bindestreck med förkortning. |
| `component::growatt_server::entity::sensor::storage_storage_production_lifetime::name` | `Elproduktion batteri totalt livslängd` | `Ackumulerad batteriproduktion` | Naturlig livstidsterm. |
| `component::growatt_server::entity::sensor::storage_storage_production_today::name` | `Elproduktion batteri i dag` | `Batteriproduktion i dag` | Korrekt svensk sammansättning. |
| `component::growatt_server::entity::sensor::tlx_all_batteries_charge_today::name` | `Alla batterier laddning i dag` | `Laddning av alla batterier i dag` | Korrekt svensk ordföljd. |
| `component::growatt_server::entity::sensor::tlx_all_batteries_charge_total::name` | `Alla batterier laddning totalt livslängd` | `Ackumulerad laddning av alla batterier` | Naturlig livstidsterm. |
| `component::growatt_server::entity::sensor::tlx_all_batteries_discharge_today::name` | `Alla batterier urladdadning i dag` | `Urladdning av alla batterier i dag` | Korrekt term, stavning och ordföljd. |
| `component::growatt_server::entity::sensor::tlx_all_batteries_discharge_total::name` | `Alla batterier urladdning totalt livslängd` | `Ackumulerad urladdning av alla batterier` | Naturlig livstidsterm. |
| `component::growatt_server::entity::sensor::tlx_amperage_input_4::name` | `Ingång 4 strömstyrka` | `Strömstyrka ingång 4` | Konsekvent svensk ordföljd. |
| `component::growatt_server::entity::sensor::tlx_battery_1_charge_total::name` | `Batteri 1 laddning totalt livslängd` | `Ackumulerad laddning av batteri 1` | Naturlig livstidsterm. |
| `component::growatt_server::entity::sensor::tlx_battery_1_charge_w::name` | `Batteri 1 laddning W` | `Laddning av batteri 1 (W)` | Korrekt svensk ordföljd och enhetsnotation. |
| `component::growatt_server::entity::sensor::tlx_battery_1_discharge_total::name` | `Batteri 1 urladdning totalt livslängd` | `Ackumulerad urladdning av batteri 1` | Naturlig livstidsterm. |
| `component::growatt_server::entity::sensor::tlx_battery_1_discharge_w::name` | `Batteri 1 urladdning W` | `Urladdning av batteri 1 (W)` | Korrekt svensk ordföljd och enhetsnotation. |
| `component::growatt_server::entity::sensor::tlx_battery_2_charge_total::name` | `Batteri 2 laddning totalt livslängd` | `Ackumulerad laddning av batteri 2` | Naturlig livstidsterm. |
| `component::growatt_server::entity::sensor::tlx_battery_2_charge_w::name` | `Batteri 2 laddning W` | `Laddning av batteri 2 (W)` | Korrekt svensk ordföljd och enhetsnotation. |
| `component::growatt_server::entity::sensor::tlx_battery_2_discharge_total::name` | `Batteri 2 urladdning totalt livslängd` | `Ackumulerad urladdning av batteri 2` | Naturlig livstidsterm. |
