# Home Assistant Core – DLNA DMR

Datum: 2026-11-21

Alla 25 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Digital Media Renderer-terminologi, URL-, XML- och händelselyssnarfält samt `{name}`, `{action}` och `{upnperror}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config::step::confirm::description` | `Vill du starta installationen?` | `Vill du starta konfigurationen?` | `setup` avser konfigurationsflödet. |

Ändringen PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 075 poster.
