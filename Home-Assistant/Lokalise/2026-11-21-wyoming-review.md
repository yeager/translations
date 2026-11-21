# Home Assistant Core – Wyoming

Datum: 2026-11-21

Alla 33 Wyoming-strängar har granskats mot aktuell källa och tidigare sparat arbete. Två Zeroconf-texter är korrigerade, sparade och API-återlästa.

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `config::step::zeroconf_confirm::description` | `... Wyoming-tjänsten {name}?` | Tog bort felaktigt blanksteg före frågetecken och bevarade platshållaren. |
| `config::step::zeroconf_confirm::title` | `Wyoming-tjänst har upptäckts` | Rättat den felaktiga verbformen `Upptäckte`. |

Övriga tjänste-, protokoll- och assistanssträngar är korrekta. Variablerna `{name}`, `{host}`, `{port}` och `{error}` är kontrollerade.
