# Home Assistant Core – Datadog

Datum: 2026-11-21

Alla 22 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. `{domain}`, `{url}`, radbrytningarna och Markdown-länken är bevarade.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config::step::user::data::rate` | `Takt` | `Samplingsfrekvens` | Samma begrepp som den förklarande texten för UDP-paket. |
| `options::step::init::data::rate` | `Takt` | `Samplingsfrekvens` | Samma fält i alternativflödet. |
| `issues::deprecated_yaml_import_connection_error::description` | `{domain} -konfigurationen` | `{domain}-konfigurationen` | Korrekt sammansättning utan felaktigt mellanrum. |
| `issues::deprecated_yaml_import_connection_error::title` | `{domain} Import ...` | `{domain}: import ...` | Korrekt svensk rubrikform och versalisering. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 042 poster.
