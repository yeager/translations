# Home Assistant Core – Bryant Evolution

Datum: 2026-11-21

Källa: Home Assistant Core `2fdaa177`,
`homeassistant/components/bryant_evolution/strings.json` och direkt återläsning
från Lokalise API.

Alla 16 aktuella `component::bryant_evolution::*`-nycklar radgranskades.
En korrigering sparades och återlästes:

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `component::bryant_evolution::exceptions::failed_to_parse_hvac_mode::message` | Det går inte att tolka svaret från HVACMode: `{mode}` | Behåller det tekniska identifierarnamnet `HVACMode` exakt. |

Platshållaren `{mode}` verifierades oförändrad. Språkparet har lagts i den
kanoniska HA-TMX:n och validerats.
