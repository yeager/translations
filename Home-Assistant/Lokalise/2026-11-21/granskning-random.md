# Home Assistant Core – Random

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/random/strings.json`  
Status: samtliga 21 aktuella strängar granskade mot Lokalise och källtext.

Referenserna är intakta och de aktuella fältnamnen, menyvalen och
alternativtexterna är korrekta. En tydlig sammansättningsmiss återstår i
Lokalise:

| Nyckel | Befintlig text | Föreslagen text | Motivering |
| --- | --- | --- | --- |
| `component::random::config::step::user::title` | `Skapa en slumpvärdes-hjälpare` | `Skapa en slumpvärdeshjälpare` | Svensk sammansättning skrivs utan bindestreck. |

Korrigeringen är sparad och återläst via Lokalise API 2026-11-21 och ingår i
den verifierade HA-TMX:en med översättnings-ID `3171377314`.
