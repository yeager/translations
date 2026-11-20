# Home Assistant Core – IRM KMI

Datum: 2026-11-20. Komponenten granskas mot `origin/dev` i Home Assistant Core och aktuella Lokalise-rader. Referenser återställs som referenser; direkta pollenetiketter översätts med vedertagna svenska växtnamn.

| Fullständig nyckel | Engelsk källa | Svensk text | Status och motivering |
| --- | --- | --- | --- |
| `component::irm_kmi::entity::sensor::pollen_alder::name` | Alder pollen | Alpollen | Sparad och återläst i Lokalise (ID 984688749). Etablerad svensk sammansättning för pollenallergen. |
| `component::irm_kmi::entity::sensor::pollen_alder::state::green` | Green | Grön | Sparad och återläst i Lokalise (ID 984688751). Grundtillstånd för de refererande pollenraderna. |
| `component::irm_kmi::entity::sensor::pollen_alder::state::none` | None | Ingen | Sparad och återläst i Lokalise (ID 984688752). Grundtillstånd för de refererande pollenraderna. |
| `component::irm_kmi::entity::sensor::pollen_alder::state::orange` | Orange | Orange | Sparad och återläst i Lokalise (ID 984688753). Grundtillstånd för de refererande pollenraderna. |
| `component::irm_kmi::entity::sensor::pollen_alder::state::purple` | Purple | Lila | Sparad och återläst i Lokalise (ID 984688754). Grundtillstånd för de refererande pollenraderna. |
| `component::irm_kmi::entity::sensor::pollen_alder::state::red` | Red | Röd | Sparad och återläst i Lokalise (ID 984688755). Grundtillstånd för de refererande pollenraderna. |

## Pågående täckning

Den nya komponenten har omfattande, tomma referensrader för pollentillstånd. Källans sex grundtillstånd granskas först, därefter återställs respektive referens exakt enligt Core-källan. Inga ännu ej sparade förslag räknas som gjorda ändringar.
