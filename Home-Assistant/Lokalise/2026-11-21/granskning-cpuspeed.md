# Home Assistant Core – CPU Speed

Datum: 2026-11-21

Samtliga 5 aktuella strängar jämfördes med Core `2fdaa177` och återlästes direkt från Lokalise. En ändring sparades:

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `component::cpuspeed::config::step::user::description` | `Vill du starta installationen?` | `Vill du starta konfigurationen?` | `setup` avser konfigurationsflödet, inte installation av programvara. |

Övriga fyra strängar var korrekta i sammanhanget. Ändringen PUT-sparades och direkt återlästes. Platshållare saknas i den ändrade texten. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 015 poster.
