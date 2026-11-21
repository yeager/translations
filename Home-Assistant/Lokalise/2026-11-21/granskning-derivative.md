# Home Assistant Core – Derivative

Datum: 2026-11-21

Alla 32 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Konfigurations- och alternativflöden, SI-prefix, tidsenheter och YAML-tjänsten kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config::step::user::data_description::max_sub_interval` | `Om definierad så ...` | `Om det anges ...` | Fullständig och idiomatisk svensk sats. |
| `options::step::init::data_description::max_sub_interval` | `Om definierad så ...` | `Om det anges ...` | Samma text i parallellt flöde. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 053 poster.
