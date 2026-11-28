# Home Assistant Core – granskningsstatus

Senast uppdaterad: 2026-11-28
Källrevision: `1d07105b760c73093145526a51758938e87cc658`
Lokalise-projekt: `130246255a974bd3b5e8a1.51616605`

## Senaste batch: 74 177–74 296

120 direkta LIFX-temaetiketter radgranskade; en stavningsrättning sparades och API-readback-verifierades. Verktygsgranskningen hittade och rättade en felaktig landsnamnspost i swedish-foss-terminology samt lade till `Chanukka` i Hunspell-sv. Se [2026-11-28-reviewed-core-74177-74296.md](2026-11-28-reviewed-core-74177-74296.md).

Nästa position: **74 297**. **3 360** positioner återstår av aktuell nyckelinventering; granskningen pågår.

## Öppna uppföljningar

- ABRP `calibrated_ref_cons`: kontrollera leverantörens exakta expansion av `ref_cons` om API-dokumentationen klargör termen.
- Broadlink `Heating`: kontrollera referenskontexten från den tidigare batchen.
- Victron `start`-status saknar aktiv källtext; Alexa äldre nyckel behöver historikkontroll.
- Govee `Marquee`-leverantörskontext; SOFAR-dubbla mjukstartsetiketter; Teslemetry saknad källtext.
- LIFX `Holidays > Independence`: kontrollera om det avsedda scenamnet syftar på USA:s självständighetsdag innan eventuell precisering.

Senaste rapport: `2026-11-28-reviewed-core-74177-74296.md`.
