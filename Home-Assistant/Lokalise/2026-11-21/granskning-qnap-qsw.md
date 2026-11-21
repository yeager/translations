# Home Assistant Core – QNAP QSW

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/qnap_qsw/strings.json`  
Status: samtliga 19 aktuella källsträngar är radgranskade mot Lokalise.

## Osparade förslag

| Nyckel | Källa | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::qnap_qsw::entity::sensor::fan_1_speed::name` | Fan 1 speed | Fläkt 1 hastighet | Fläkt 1-hastighet | Sammansatt etikett behöver bindestreck. Lokalise-ID `369759167`. |
| `component::qnap_qsw::entity::sensor::fan_2_speed::name` | Fan 2 speed | Fläkt 2 hastighet | Fläkt 2-hastighet | Sammansatt etikett behöver bindestreck. Lokalise-ID `369759168`. |
| `component::qnap_qsw::entity::sensor::rx_speed::name` | RX speed | RX hastighet | RX-hastighet | Sammansatt etikett behöver bindestreck. Lokalise-ID `369759172`. |
| `component::qnap_qsw::entity::sensor::tx_speed::name` | TX speed | TX hastighet | TX-hastighet | Sammansatt etikett behöver bindestreck. Lokalise-ID `369759174`. |

## Verifierade befintliga värden

- Samtliga konfigurationsreferenser för enhet, anslutning, autentisering, användarnamn, lösenord och URL följer den aktuella källan exakt.
- `Device returned an invalid unique ID` är korrekt återgivet som `Enheten returnerade ett ogiltigt unikt ID`.
- Portar, RX, TX, RX-fel och tidsstämpel för drifttid är korrekta. `Uptime` använder den etablerade svenska referensen för drifttid.
- QNAP QSW bevaras som produktnamn.

Lokalise visar dessutom två avvecklingsposter som inte ingår i dagens `strings.json`: en rubrik och ett längre reparationsmeddelande för sensorn för drifttidssekunder (ID `550678532` respektive `550678531`). Det längre meddelandet behåller `Home Assistant` exakt som i källtexten och platshållarna `{entity}` och `{info}`; båda posterna lämnas orörda som historiska. De fyra förslagen ovan är inte sparade och förs inte in i TMX före sparning och återläsning.
