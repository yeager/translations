# Matter: sparad ändring i Lokalise

Den 19 november 2026 jämfördes aktuell källtext och svensk översättning. Ändringen sparades och återlästes i Lokalise.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::matter::entity::number::auto_relock_timer::name` | Auto-relock time | Timer för automatisk återlåsning | Tid till automatisk återlåsning |

Ändringen uttrycker tidsintervallet snarare än en timer. Källa: lokal rapport `granskning-38565-38569.md`.

## Pumpens driftlägen

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::matter::entity::select::pump_operation_mode::state::maximum` | Maximum | Maximal | Maximum |
| `component::matter::entity::select::pump_operation_mode::name` | mode | läge | Läge |

Sparade och återlästa i Lokalise. ”Maximum” används parallellt med befintliga ”Minimum”. Referensen `component::matter::entity::select::pump_operation_mode::state::normal` till `common::state::normal` behölls; målets aktuella engelska och svenska text kontrollerades till ”Normal”.
