# Home Assistant Core – Lokalise-granskning, sida 602

Datum: 2026-11-20  
Omfattning: Lokalise API, 20 Core-strängar (`elkm1`).

## Sparade ändringar

| Nyckel | Befintlig svensk text | Sparad svensk text | Motivering |
|---|---|---|---|
| `component::elkm1::services::alarm_clear_bypass::fields::code::description` | `Larmkod för att rensa förbikoppling av larmpanelen.` | `Larmkod för att godkänna borttagning av förbikopplingen i larmpanelen.` | Återger behörighetsfunktionen och vad som tas bort. |
| `component::elkm1::services::alarm_display_message::fields::clear::description` | `0 = rensa meddelande, 1 = rensa meddelande med * nyckel, 2 = Visa tills timeout.` | `0=rensa meddelande, 1=rensa meddelande med *-knappen, 2=visa tills tidsgränsen löper ut.` | Rättade ordval och stil. |
| `component::elkm1::services::alarm_display_message::fields::line1::description` | `Upp till 16 tecken (trunkeras om den är för lång).` | `Upp till 16 texttecken (korta av om texten är längre).` | Naturligare svenska och tydlig referens till texten. |
| `component::elkm1::services::alarm_display_message::fields::timeout::description` | `Tid att visa meddelande, 0=för alltid, max 65535.` | `Hur länge meddelandet ska visas; 0=för alltid, högst 65535.` | Förbättrad svensk satsstruktur. |
| `component::elkm1::services::sensor_counter_refresh::name` | `Uppdatering av sensorräknare` | `Uppdatera sensorräknare` | Tjänsten är en åtgärd och ska ha imperativ form. |

## Verifiering

Alla fem ändringar skickades med Lokalise API och återlästes. Referensen för rad 2 är fortsatt korrekt; övriga 14 strängar behöver ingen ändring.

Status: sparat och återläst i Lokalise.
