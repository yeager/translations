# Home Assistant Core – Pure Energie

Datum: 2026-11-21  
Status: samtliga 11 aktuella bladnycklar är radgranskade mot `origin/dev`.

| Nyckel | Källa | Svenska | Bedömning |
| --- | --- | --- | --- |
| `component::pure_energie::config::{abort::already_configured,abort::cannot_connect,error::cannot_connect}` | Gemensamma konfigurationsreferenser | Samma referenser | Referenserna är bevarade och matchar aktuell Core-källa (Lokalise-ID `151283089`–`151283091`). |
| `component::pure_energie::config::flow_title` | `{model} ({host})` | `{model} ({host})` | Båda platshållarna är bevarade (ID `151283092`). |
| `component::pure_energie::config::step::user::data::host` | Gemensam värd-referens | Samma referens | Korrekt referens (ID `151283093`). |
| `component::pure_energie::config::step::user::data_description::host` | The IP address or hostname of your Pure Energie Meter. | IP-adressen eller värdnamnet för din Pure Energie-mätare. | Korrekt svensk formulering och produktnamn (ID `207439320`). |
| `component::pure_energie::config::step::zeroconf_confirm::description` | Do you want to add Pure Energie Meter (`{model}`) to Home Assistant? | Vill du lägga till Pure Energie Meter (`{model}`) till Home Assistant? | Korrekt; `{model}`, kodmarkering och det exakta produktnamnet Home Assistant är bevarade (ID `151283094`). |
| `component::pure_energie::config::step::zeroconf_confirm::title` | Discovered Pure Energie Meter device | Upptäckt Pure Energie Meter-enhet | Korrekt och tydlig rubrik (ID `151283095`). |
| `component::pure_energie::entity::sensor::{energy_consumption_total,energy_production_total,power_flow}::name` | Energy consumption; Energy production; Power flow | Elförbrukning; Elproduktion; Effektflöde | Korrekt energiterminologi (ID `347198317`–`347198319`). |

Inga ändringsförslag. Alla värden ovan är verifierade befintliga Lokalise-värden och har förts in i det kanoniska Home Assistant-TMX-minnet med spårbara Lokalise-ID:n.
