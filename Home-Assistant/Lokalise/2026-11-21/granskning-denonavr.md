# Home Assistant Core – Denon AVR

Datum: 2026-11-21

Alla 34 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Konfiguration, Telnet-information, Audyssey och tjänster kontrollerades. `{name}` är intakt.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config::abort::cannot_connect` | `nät- och Ethernet-kablarna` | `ström- och Ethernet-kablarna` | `mains power` är ström, och Ethernet-sammansättningen behöver bindestreck. |
| `config::error::cannot_connect` | `Ethernetkablarna` | `Ethernet-kablarna` | Samma källtext och konsekvent teknisk term. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 051 poster.
