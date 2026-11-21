# Home Assistant Core – dormakaba dKey

Datum: 2026-11-21

Alla 16 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Aktiveringskoder, Bluetooth-räckvidd, dKey-adminappen och `{name}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config::step::associate::description` | `...skapar man ... väljer ...` | `...skapar du ... väljer ...` | Konsekvent direkt användartilltal i instruktionen. |

Ändringen PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 090 poster.
