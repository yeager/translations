# Home Assistant Core – DirecTV

Datum: 2026-11-21

Alla 8 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Konfiguration och platshållarna `{name}`, `{command}` och `{device}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `exceptions::send_command_failed::message` | `Skickar kommando {command}till ...` | `Det gick inte att skicka kommandot {command} till ...` | Saknat mellanrum och felaktig svensk sats korrigerades; platshållarna är bevarade. |

Ändringen PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 067 poster.
