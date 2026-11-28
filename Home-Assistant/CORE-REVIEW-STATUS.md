# Home Assistant Core – granskningsstatus

Senast uppdaterad: 2026-11-28
Källrevision: `1d07105b760c73093145526a51758938e87cc658`
Lokalise-projekt: `130246255a974bd3b5e8a1.51616605`

## Senaste batch: 75 377–75 496

120 strängar radgranskade: 69 direkta källmatchningar och 50 verifierade referenser; en Shelly-källa saknas i den pinnade snapshoten. Tio rättelser sparades och lästes tillbaka, 109 andra poster verifierades. Se [2026-11-28-reviewed-core-75377-75496.md](2026-11-28-reviewed-core-75377-75496.md). HA-TM uppdaterades.

Nästa position: **75 497**. **2 160** positioner återstår av aktuell nyckelinventering; granskningen pågår.

## Öppna uppföljningar

- Batch 75 137–75 256, 75 257–75 376 och 75 377–75 496: Lokalise-flaggan `Reviewed` kunde inte sättas med tillgänglig API-token (HTTP 403: `No permission to update translation status`); editorns massåtgärd visar bara `Unverified`. Innehållsgranskning och text-readback är genomförda; flaggan kräver en behörig reviewer.

- UniFi Protect batch 75 257–75 376: `entry_opened`, `entry_closed` och `tamper` behölls men behöver produkttext för att avgöra om svenska etiketter ska precisera dörr/port respektive sabotage/fysisk påverkan.
- Shelly `component::shelly::entity::update::release_notes_messages::do_not_unplug` saknas i pinnad källsnapshot; se batchrapporten innan källverifiering.
- ABRP `calibrated_ref_cons`: kontrollera leverantörens exakta expansion av `ref_cons` om API-dokumentationen klargör termen.
- Broadlink `Heating`: kontrollera referenskontexten från den tidigare batchen.
- Victron `start`-status saknar aktiv källtext; Alexa äldre nyckel behöver historikkontroll.
- Govee `Marquee`-leverantörskontext; SOFAR-dubbla mjukstartsetiketter; Teslemetry saknad källtext.
- LIFX `Holidays > Independence`: kontrollera om det avsedda scenamnet syftar på USA:s självständighetsdag innan eventuell precisering.
- LIFX `Archives > Old Glory`: kontrollera om namnet avser amerikanska flaggan eller en namngiven färgscen.

Senaste rapport: `2026-11-28-reviewed-core-75257-75376.md`.
