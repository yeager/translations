# Home Assistant Core – APsystems

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/apsystems/strings.json` och Lokalise API med direkt återläsning.

Status: samtliga 21 aktuella bladsträngar är radgranskade. Åtta korrigeringar är sparade och återlästa.

| Nyckelgrupp | Sparad svensk terminologi | Motivering |
|---|---|---|
| `lifetime_production*` | `Total livstidsproduktion`, `P1:s livstidsproduktion`, `P2:s livstidsproduktion` | Naturliga, kompakta sensorbenämningar utan otydliga parenteser. |
| `today_production*` | `Dagens produktion`, `Dagens produktion från P1`, `Dagens produktion från P2` | Rätt svensk tids- och relationsform. |
| `total_power_p1`, `total_power_p2` | `P1-effekt`, `P2-effekt` | Tydliga tekniska sammansättningar. |

Kontroll: ögonblicksbilden i `swedish-tm` innehöll felaktiga svenska översättnings-id för dessa åtta nycklar. Direkta API-svar identifierade i stället svenska poster genom `language_iso=sv`; alla ändringar sparades och återlästes med dessa auktoritativa id:n. Felet är dokumenterat för verktygsuppföljning, och den validerade TMX-ledgern använder de korrekta id:na (1 713 poster).
