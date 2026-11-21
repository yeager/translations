# Home Assistant Core – Broadlink

Datum: 2026-11-21

Källa: Home Assistant Core `2fdaa177`,
`homeassistant/components/broadlink/strings.json`, tidigare Broadlink-rapporter
och direkt återläsning från Lokalise API.

## Resultat

Alla 57 aktuella `component::broadlink::*`-nycklar lästes tillbaka direkt från
Lokalise. Två säkra korrigeringar sparades och återlästes:

| Nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::broadlink::exceptions::send_command_failed::message` | Det gick inte att skicka IR-kommando: `{error}` | Det gick inte att skicka kommandot: `{error}` | Källtexten är generisk; IR lades felaktigt till. |
| `component::broadlink::exceptions::transmit_failed::message` | Misslyckades med att överföra RF-kommando: `{error}` | Det gick inte att sända RF-kommandot: `{error}` | RF-kommandot sänds, det överförs inte. |

Platshållaren `{error}` verifierades oförändrad i båda posterna. Båda språkparen
finns i kanoniska HA-TMX:n och har formatvaliderats.

## Öppen referensfråga

`component::broadlink::exceptions::timing_too_long::message` behåller
”RF-timing”. Den tidigare uppföljningen konstaterar att den exakta tekniska
innebörden måste verifieras mot den kodversion som genererar felet; den aktuella
källfilen ger inte tillräckligt underlag för en säker svensk fackterm.
