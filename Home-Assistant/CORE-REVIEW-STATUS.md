# Home Assistant Core – granskningsstatus

Senast uppdaterad: 2026-11-28
Källrevision: `1d07105b760c73093145526a51758938e87cc658`
Lokalise-projekt: `130246255a974bd3b5e8a1.51616605`

## Senaste batch: 76 097–76 216

120 strängar radgranskade: 65 direkta källmatchningar och 55 referensnycklar till 21 mål. Tidigare granskningsspår fanns för 120/120. Tre Lokalise-ID ändrades och lästes tillbaka; 55/55 referenser stämmer. Se [2026-11-28-reviewed-core-76097-76216.md](2026-11-28-reviewed-core-76097-76216.md). TM-manifestet innehåller 124 ägar-/referensmålposter och uppdaterar tre avvikande TM-värden. Canonical TMX valideras efter uppdateringen.

Nästa position: **76 217**. **1 440** positioner återstår av aktuell nyckelinventering; granskningen pågår.

## Öppna uppföljningar

- Foreca `icing`: API-dokumentationen anger nederbördstypen men definierar inte undergruppen; översatt brett som ”underkyld nederbörd”. Bekräfta exakt leverantörsbetydelse om dokumentationen kompletteras.

- Batch 75 137–75 256, 75 257–75 376, 75 377–75 496, 75 497–75 616, 75 617–75 736, 75 737–75 856, 75 857–75 976, 75 977–76 096 och 76 097–76 216: Lokalise-flaggan `Reviewed` kunde inte sättas med tillgänglig API-token (HTTP 403: `No permission to update translation status`); editorns massåtgärd visar bara `Unverified`. Innehållsgranskning och text-readback är genomförda; flaggan kräver en behörig reviewer.

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
