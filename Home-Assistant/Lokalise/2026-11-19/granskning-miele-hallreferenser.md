# Miele: hällens tillståndsreferenser

Kontrollerat i Lokalise den 19 november 2026. Tre svenska referenser avviker från källreferensernas stavning, men pekar på synliga målnycklar med ett extra kolon i nyckelns sista del. Detta kan vara en käll- eller exportavvikelse och behöver utredas innan någon av referenserna ändras.

| Fullständig nyckel | Engelsk källreferens | Svensk referens | Synligt svenskt mål |
|---|---|---|---|
| `component::miele::entity::sensor::plate::state:::220` | `[%key:component::miele::entity::sensor::plate::state::110%]` | `[%key:component::miele::entity::sensor::plate::state:::110%]` | `component::miele::entity::sensor::plate::state:::110`: Warming / Uppvärmning |
| `component::miele::entity::sensor::plate::state:::217` | `[%key:component::miele::entity::sensor::plate::state::117%]` | `[%key:component::miele::entity::sensor::plate::state:::117%]` | `component::miele::entity::sensor::plate::state:::117`: Boost / Boost |
| `component::miele::entity::sensor::plate::state:::118` | `[%key:component::miele::entity::sensor::plate::state::117%]` | `[%key:component::miele::entity::sensor::plate::state:::117%]` | Samma mål som ovan. |

Lokalises sökning efter `state::110` visade refererande nyckel men inget exakt mål `state::110`; sökningen efter `state:::110` visade däremot målet ovan. Detta räcker inte för att avgöra hur Home Assistants källfiler eller exportprocess löser referenserna. Kontrollera ursprungliga nycklar och export innan källan eller den fungerande svenska referensen justeras. Ingen översättning ändrades.
