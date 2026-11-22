# Modern Forms: sensor-etiketter för insomningstid

Den 22 november 2026 granskades Modern Forms aktuella svenska sensor-etiketter
mot källtexten och komponentens övriga terminologi. Två etiketter använde
`Sovtimer`, medan samma komponent konsekvent använder `insomningstimer`.

| Fullständig nyckel | Tidigare svenska | Sparad svenska |
| --- | --- | --- |
| `component::modern_forms::entity::sensor::fan_timer_remaining_time::name` | `Fläkt sovtimer` | `Fläktens insomningstid` |
| `component::modern_forms::entity::sensor::light_timer_remaining_time::name` | `Lampa sovtimer` | `Lampans insomningstid` |

## Verifiering

- Båda ändringarna sparades och lästes tillbaka ordagrant via Lokalise API.
- Inga platshållare, markup- eller referenselement förekommer i strängarna.
- `hunspell-sv` gav inga träffar och `svlang check` gav 10,0/10 utan problem.
- Poster förs in i HA-TMX med respektive Lokalise-id och valideras innan commit.
