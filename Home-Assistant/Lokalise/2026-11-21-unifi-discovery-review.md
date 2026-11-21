# Home Assistant Core – UniFi Discovery

Datum: 2026-11-21

Tre strängar har kontrollerats mot aktuell källa och tidigare granskningsrapport.

| Nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::unifi_discovery::config::abort::discovery_started` | `Upptäckten startades` | `Upptäckten har startat` | Perfekt uttrycker det aktuella resultatläget på naturlig svenska, utan att byta bort den etablerade termen *upptäckt*. |

`already_in_progress` och den automatiska konfigurationsbeskrivningen är korrekta och oförändrade. Ändringen är sparad och API-återläst; inga platshållare eller referenser berörs.
