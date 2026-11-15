# Home Assistant Core – ecosmart prisprognoser, svenska

Datum: 2026-11-15

Sju texter i ecosmarts elprisflöde har granskats, sparats via Lokalise API och
återlästs. API, `ICP` och platsmarkörerna är bevarade.

| Källa | Svenska |
| --- | --- |
| Connection point | Anslutningspunkt |
| Get price forecast | Hämta prisprognos |
| Retrieves the wholesale price forecast for a connection point. | Hämtar grossistprisprognosen för en anslutningspunkt. |
| The connection point (ICP) to get the price forecast for. | Anslutningspunkten (ICP) som prisprognosen ska hämtas för. |

De tre återstående felmeddelandena är också sparade och återlästa med
`{retry_after}`, `{icp}` respektive `{device_id}` oförändrade.

## Upstreamstatus

- Lokal granskning: klar.
- Sparad via Lokalise API: klar, sju översättningar.
- API-återläsning: klar; samtliga sju har `sv` och `is_unverified=false`.
- Projektgranskning och release: inte verifierade.
