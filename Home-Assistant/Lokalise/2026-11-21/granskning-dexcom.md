# Home Assistant Core – Dexcom

Datum: 2026-11-21

Alla 24 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Share-konfiguration, glukoslägen, måttenhet och återautentisering kontrollerades. `{username}` och `{name}` är intakta.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `entity::sensor::glucose_trend::name` | `Glukos trend` | `Glukostrend` | Korrekt svensk sammansättning. |

Ändringen PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 063 poster.
