# Home Assistant Core – DNSIP

Datum: 2026-11-21

Alla 47 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. IPv4/IPv6-fält, namnuppslagning, avancerade alternativ och resolverterminologi kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `entity::sensor::dnsip::state_attributes::resolver::name` | `Upplösare` | `DNS-resolver` | Etablerad teknisk term; direktöversättningen är olämplig i DNS-sammanhang. |

Ändringen PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 077 poster.
