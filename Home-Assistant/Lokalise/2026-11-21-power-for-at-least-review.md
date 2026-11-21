# Home Assistant Core – power: tidsvillkor

Granskad: 2026-11-21  
Omfattning: `component::power` – fyra etiketter för tidsvillkoret `For at least`.

| Nyckel | Tidigare svensk text | Sparad svensk text | Motivering |
|---|---|---|---|
| `component::power::common::trigger_for_name` | I åtminstone | I minst | Fast svensk konstruktion för ett tidsvillkor. |
| `component::power::triggers::crossed_threshold::fields::for::name` | I åtminstone | I minst | Samma fält i tröskelutlösaren. |
| `component::power::common::condition_for_name` | I åtminstone | I minst | Samma konstruktion i villkor. |
| `component::power::conditions::is_value::fields::for::name` | I åtminstone | I minst | Samma fält i värdevillkoret. |

Alla fyra poster sparades med Lokalise API och lästes sedan tillbaka via API. Det innebär innehållsverifiering, inte att Lokalises separata granskningsstatus har satts; den statusen saknar behörighet via den använda API-anslutningen.

TMX-källa: `Home-Assistant/2026-11-21-power-for-at-least-verified.json` i `swedish-tm`.
