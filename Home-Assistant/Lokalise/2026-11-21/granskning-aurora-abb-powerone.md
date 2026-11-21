# Home Assistant Core – Aurora ABB PowerOne

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/aurora_abb_powerone/strings.json` och Lokalise API med direkt återläsning.

Status: samtliga 24 aktuella bladsträngar och referensmål är radgranskade. Åtta korrigeringar är sparade och återlästa.

| Nyckelgrupp | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `grid_current`, `grid_voltage` | `Elnät ström`, `Elnät spänning` | `Elnätsström`, `Elnätsspänning` | Korrekta svenska sammansättningar. |
| `current_in_[1-2]` | `Slinga [1-2] ström` | `Sträng [1-2]-ström` | *String* betyder solcellssträng i denna växelriktarkontext. |
| `power_in_[1-2]` | `Slinga [1-2] effekt` | `Sträng [1-2]-effekt` | Korrekt fackterm och sammansättning. |
| `voltage_in_[1-2]` | `Slinga [1-2] spänning` | `Sträng [1-2]-spänning` | Korrekt fackterm och sammansättning. |

Anslutningsinstruktioner, RS485/USB-RS485, LCD-panel, växelriktare, larmstatus, läckström, isolationsmotstånd och undantagstext är korrekta. TMX-ledgern har uppdaterats med de återlästa Lokalise-posterna.
