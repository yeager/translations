# Home Assistant Core – granskningsstatus

Senast uppdaterad: 2026-11-28
Källrevision: `1d07105b760c73093145526a51758938e87cc658`
Lokalise-projekt: `130246255a974bd3b5e8a1.51616605`

## Senaste batch: 73 457–73 576

120 poster radgranskade; samtliga är LIFX-referenser till 120 mål. Alla engelska och svenska värden matchar; inga textändringar behövdes. En uppföljning kvarstår kring om `Holidays > Independence` ska preciseras till självständighetsdagen. Se [batchrapporten](2026-11-28-reviewed-core-73457-73576.md).

Nästa position: **73 577**. **4 080** positioner återstår av aktuell nyckelinventering; granskningen pågår.

## Öppna uppföljningar

- ABRP `calibrated_ref_cons`: kontrollera leverantörens exakta expansion av `ref_cons` om API-dokumentationen klargör termen.
- Broadlink `Heating`: kontrollera referenskontexten från den tidigare batchen.
- Victron `start`-status saknar aktiv källtext; Alexa äldre nyckel behöver historikkontroll.
- Govee `Marquee`-leverantörskontext; SOFAR-dubbla mjukstartsetiketter; Teslemetry saknad källtext.
- LIFX `Holidays > Independence`: kontrollera om det avsedda scenamnet syftar på USA:s självständighetsdag innan eventuell precisering.

Senaste rapport: `2026-11-28-reviewed-core-73457-73576.md`.
