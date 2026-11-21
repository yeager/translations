# Home Assistant Core – devolo Home Control

Datum: 2026-11-21

Alla 27 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Konfigurations- och återautentiseringsflöden, produktnamn och platshållarna `{key}` och `{placeholder}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `exceptions::connection_failed::message` | `devolo Home Control centralenhet` | `devolo Home Control-centralenhet` | Korrekt svensk produktnamnssammansättning. |

Ändringen PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 057 poster.
