# Home Assistant Core – granskningsstatus

Senast uppdaterad: 2026-11-28
Källrevision: `1d07105b760c73093145526a51758938e87cc658`
Lokalise-projekt: `130246255a974bd3b5e8a1.51616605`

## Senaste batch: 75 137–75 256

120 strängar radgranskade: 71 direkta källmatchningar och 49 verifierade referenser. Tio rättelser sparades och lästes tillbaka via API; övriga 110 verifierades. Se [2026-11-28-reviewed-core-75137-75256.md](2026-11-28-reviewed-core-75137-75256.md). HA-TM och terminologilistan uppdaterades.

Nästa position: **75 257**. **2 400** positioner återstår av aktuell nyckelinventering; granskningen pågår.

## Öppna uppföljningar

- Batch 75 137–75 256: Lokalise-flaggan `Reviewed` kunde inte sättas med tillgänglig API-token (HTTP 403: `No permission to update translation status`); editorns massåtgärd visar bara `Unverified`. Innehållsgranskning och text-readback är genomförda; flaggan kräver en behörig reviewer.

- ABRP `calibrated_ref_cons`: kontrollera leverantörens exakta expansion av `ref_cons` om API-dokumentationen klargör termen.
- Broadlink `Heating`: kontrollera referenskontexten från den tidigare batchen.
- Victron `start`-status saknar aktiv källtext; Alexa äldre nyckel behöver historikkontroll.
- Govee `Marquee`-leverantörskontext; SOFAR-dubbla mjukstartsetiketter; Teslemetry saknad källtext.
- LIFX `Holidays > Independence`: kontrollera om det avsedda scenamnet syftar på USA:s självständighetsdag innan eventuell precisering.
- LIFX `Archives > Old Glory`: kontrollera om namnet avser amerikanska flaggan eller en namngiven färgscen.

Senaste rapport: `2026-11-28-reviewed-core-74417-74536.md`.
