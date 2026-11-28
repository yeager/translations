# Home Assistant Core – granskningsstatus

Senast uppdaterad: 2026-11-28
Källrevision: `1d07105b760c73093145526a51758938e87cc658`
Lokalise-projekt: `130246255a974bd3b5e8a1.51616605`

## Senaste batch: 75 857–75 976

120 strängar radgranskade: 106 direkta källmatchningar och 14 referensnycklar till 13 unika mål. Tidigare granskningsspår fanns för 120/120. Två Lokalise-ID ändrades och lästes tillbaka. Se [2026-11-28-reviewed-core-75857-75976.md](2026-11-28-reviewed-core-75857-75976.md). TM-manifestet innehåller 129 ägar-/referensmålposter; två TM-värden uppdaterades. Canonical TMX valideras med **41 006 poster**: 40 775 Lokalise-ID och 231 äldre källnycklar.

Nästa position: **75 977**. **1 680** positioner återstår av aktuell nyckelinventering; granskningen pågår.

## Öppna uppföljningar

- Batch 75 137–75 256, 75 257–75 376, 75 377–75 496, 75 497–75 616, 75 617–75 736 och 75 737–75 856 och 75 857–75 976: Lokalise-flaggan `Reviewed` kunde inte sättas med tillgänglig API-token (HTTP 403: `No permission to update translation status`); editorns massåtgärd visar bara `Unverified`. Innehållsgranskning och text-readback är genomförda; flaggan kräver en behörig reviewer.

- UniFi Protect batch 75 257–75 376: `entry_opened`, `entry_closed` och `tamper` behölls men behöver produkttext för att avgöra om svenska etiketter ska precisera dörr/port respektive sabotage/fysisk påverkan.
- Shelly `component::shelly::entity::update::release_notes_messages::do_not_unplug` saknas i pinnad källsnapshot; se batchrapporten innan källverifiering.
- ABRP `calibrated_ref_cons`: kontrollera leverantörens exakta expansion av `ref_cons` om API-dokumentationen klargör termen.
- Broadlink `Heating`: kontrollera referenskontexten från den tidigare batchen.
- Victron `start`-status saknar aktiv källtext; Alexa äldre nyckel behöver historikkontroll.
- Govee `Marquee`-leverantörskontext; SOFAR-dubbla mjukstartsetiketter; Teslemetry saknad källtext.
- LIFX `Holidays > Independence`: kontrollera om det avsedda scenamnet syftar på USA:s självständighetsdag innan eventuell precisering.
- LIFX `Archives > Old Glory`: kontrollera om namnet avser amerikanska flaggan eller en namngiven färgscen.
- Tuya `component::tuya::entity::binary_sensor::cover_alarm::name` och `...::terminal_alarm::name`: kontrollera elmätarens protokolldefinition innan etiketten preciseras.

Senaste rapport: [2026-11-28-reviewed-core-75857-75976.md](2026-11-28-reviewed-core-75857-75976.md).
