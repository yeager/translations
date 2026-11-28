# Home Assistant Core – granskningsstatus

Senast uppdaterad: 2026-11-28
Källrevision: `1d07105b760c73093145526a51758938e87cc658`
Lokalise-projekt: `130246255a974bd3b5e8a1.51616605`

## Senaste batch: 75 257–75 376

120 strängar radgranskade (84 direkta källtexter, 36 verifierade referenser); 18 unika rättelser sparades genom 19 API-sparningar (en Nibe-rad förfinades), 102 befintliga mål verifierades. Alla platshållare ja, alla pluralposter (0) granskade, tidigare granskningsspår hittades för alla 120. Se [2026-11-28-reviewed-core-75257-75376.md](2026-11-28-reviewed-core-75257-75376.md). HA-TM och HTML-terminologirapport uppdaterades.

Nästa position: **75 377**. **2 280** positioner återstår av aktuell nyckelinventering; granskningen pågår.

## Öppna uppföljningar

- Batch 75 137–75 256 och 75 257–75 376: Lokalise-flaggan `Reviewed` kunde inte sättas med tillgänglig API-token (HTTP 403: `No permission to update translation status`); editorns massåtgärd visar bara `Unverified`. Innehållsgranskning och text-readback är genomförda; flaggan kräver en behörig reviewer.

- UniFi Protect batch 75 257–75 376: `entry_opened`, `entry_closed` och `tamper` behölls men behöver produkttext för att avgöra om svenska etiketter ska precisera dörr/port respektive sabotage/fysisk påverkan.
- ABRP `calibrated_ref_cons`: kontrollera leverantörens exakta expansion av `ref_cons` om API-dokumentationen klargör termen.
- Broadlink `Heating`: kontrollera referenskontexten från den tidigare batchen.
- Victron `start`-status saknar aktiv källtext; Alexa äldre nyckel behöver historikkontroll.
- Govee `Marquee`-leverantörskontext; SOFAR-dubbla mjukstartsetiketter; Teslemetry saknad källtext.
- LIFX `Holidays > Independence`: kontrollera om det avsedda scenamnet syftar på USA:s självständighetsdag innan eventuell precisering.
- LIFX `Archives > Old Glory`: kontrollera om namnet avser amerikanska flaggan eller en namngiven färgscen.

Senaste rapport: `2026-11-28-reviewed-core-75257-75376.md`.
