# Miele: hällens tillståndsreferenser

Kontrollerat i Lokalise den 19 november 2026. Tre svenska referenser avviker från källreferensernas stavning, men pekar på synliga målnycklar med ett extra kolon i nyckelns sista del. Detta kan vara en käll- eller exportavvikelse och behöver utredas innan någon av referenserna ändras.

| Fullständig nyckel | Engelsk källreferens | Svensk referens | Synligt svenskt mål |
|---|---|---|---|
| `component::miele::entity::sensor::plate::state:::220` | `[%key:component::miele::entity::sensor::plate::state::110%]` | `[%key:component::miele::entity::sensor::plate::state:::110%]` | `component::miele::entity::sensor::plate::state:::110`: Warming / Uppvärmning |
| `component::miele::entity::sensor::plate::state:::217` | `[%key:component::miele::entity::sensor::plate::state::117%]` | `[%key:component::miele::entity::sensor::plate::state:::117%]` | `component::miele::entity::sensor::plate::state:::117`: Boost / Boost |
| `component::miele::entity::sensor::plate::state:::118` | `[%key:component::miele::entity::sensor::plate::state::117%]` | `[%key:component::miele::entity::sensor::plate::state:::117%]` | Samma mål som ovan. |

Lokalises sökning efter `state::110` visade refererande nyckel men inget exakt mål `state::110`; sökningen efter `state:::110` visade däremot målet ovan. Detta räcker inte för att avgöra hur Home Assistants källfiler eller exportprocess löser referenserna. Kontrollera ursprungliga nycklar och export innan källan eller den fungerande svenska referensen justeras. Ingen översättning ändrades.

## Källkodskontroll

I Home Assistant Cores [Miele-källfil för version 2025.6.3](https://github.com/home-assistant/core/blob/2025.6.3/homeassistant/components/miele/strings.json) är tillståndsnycklarna `110` och `117` faktiska JSON-nycklar, och `118`, `217` och `220` hänvisar till dem med två kolon i den platta referensen. Den engelska referensstavningen motsvarar alltså denna historiska källfil. Lokalise visar däremot exporterade nyckelnamn med ett extra kolon före siffrorna. Detta talar för en skillnad i importerad nyckelrepresentation; orsaken och referensernas faktiska upplösning i exporten är fortfarande inte fastställda.

På [utvecklingsgrenens aktuella Miele-källa](https://github.com/home-assistant/core/blob/dev/homeassistant/components/miele/strings.json) har de numeriska tillstånden ersatts av namn som `plate_step_warm` och `plate_step_boost`. De gamla Lokalise-posterna kan därför vara föråldrade. Ingen ändring gjordes i Lokalise; verifiera version och export innan korrigering av historiska poster.
