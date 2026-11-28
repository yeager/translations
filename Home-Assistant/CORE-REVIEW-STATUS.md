# Home Assistant Core – granskningsstatus

Senast uppdaterad: 2026-11-28
Källrevision: `1d07105b760c73093145526a51758938e87cc658`
Lokalise-projekt: `130246255a974bd3b5e8a1.51616605`

## Senaste batch: 73 697–73 816

120 poster radgranskade: en direkt sträng och 119 LIFX-referenser. Sex initiala referensavvikelser åtgärdades, inklusive en retroaktiv ägarsträng. Sju översättningar sparades och API-readback-verifierades; samtliga referenspar matchar. Se [2026-11-28-reviewed-core-73697-73816.md](2026-11-28-reviewed-core-73697-73816.md).

Nästa position: **73 817**. **3 840** positioner återstår av aktuell nyckelinventering; granskningen pågår.

## Öppna uppföljningar

- ABRP `calibrated_ref_cons`: kontrollera leverantörens exakta expansion av `ref_cons` om API-dokumentationen klargör termen.
- Broadlink `Heating`: kontrollera referenskontexten från den tidigare batchen.
- Victron `start`-status saknar aktiv källtext; Alexa äldre nyckel behöver historikkontroll.
- Govee `Marquee`-leverantörskontext; SOFAR-dubbla mjukstartsetiketter; Teslemetry saknad källtext.
- LIFX `Holidays > Independence`: kontrollera om det avsedda scenamnet syftar på USA:s självständighetsdag innan eventuell precisering.

Senaste rapport: `2026-11-28-reviewed-core-73697-73816.md`.
