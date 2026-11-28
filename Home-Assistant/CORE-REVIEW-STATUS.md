# Home Assistant Core – granskningsstatus

Senast uppdaterad: 2026-11-28
Källrevision: `1d07105b760c73093145526a51758938e87cc658`
Lokalise-projekt: `130246255a974bd3b5e8a1.51616605`

## Senaste batch: 74 417–74 536

120 poster radgranskade: 119 direkta källträffar och en referensverifiering. En kontextfelaktig VeSync-sensoröversättning korrigerades, sparades och återlästes via API. TMX och backup uppdaterades. Se [2026-11-28-reviewed-core-74417-74536.md](2026-11-28-reviewed-core-74417-74536.md).

Nästa position: **74 537**. **3 120** positioner återstår av aktuell nyckelinventering; granskningen pågår.

## Öppna uppföljningar

- ABRP `calibrated_ref_cons`: kontrollera leverantörens exakta expansion av `ref_cons` om API-dokumentationen klargör termen.
- Broadlink `Heating`: kontrollera referenskontexten från den tidigare batchen.
- Victron `start`-status saknar aktiv källtext; Alexa äldre nyckel behöver historikkontroll.
- Govee `Marquee`-leverantörskontext; SOFAR-dubbla mjukstartsetiketter; Teslemetry saknad källtext.
- LIFX `Holidays > Independence`: kontrollera om det avsedda scenamnet syftar på USA:s självständighetsdag innan eventuell precisering.
- LIFX `Archives > Old Glory`: kontrollera om namnet avser amerikanska flaggan eller en namngiven färgscen.

Senaste rapport: `2026-11-28-reviewed-core-74417-74536.md`.
