# Home Assistant Core: kompletterande kontroll av Matter

Kontrollerat i Lokalise den 19 november 2026. Inga ändringar gjorda i Lokalise. De tre mellanliggande nycklarna och de gemensamma referensmålen kontrollerades därefter i Lokalise. Nästa nyckel i den tidigare dokumenterade ordningen är ID 653073959; jämför alltid med aktuell ordning.

| Fullständig nyckel | Engelska i Lokalise | Svenska i Lokalise | Bedömning |
|---|---|---|---|
| `component::matter::entity::sensor::esa_state::state::fault` | [%key:common::state::fault%] | [%key:common::state::fault%] | Behåll referensen. Målet har källtexten ”Fault” och svenska ”Fel”. |
| `component::matter::entity::sensor::esa_state::name` | Appliance energy state | Apparatens energistatus | Behåll. |
| `component::matter::entity::select::door_lock_sound_volume::state::silent` | Silent | Tyst | Behåll. |
| `component::matter::entity::select::door_lock_sound_volume::state::medium` | [%key:common::state::medium%] | [%key:common::state::medium%] | Behåll referensen; målet är ”Medium” → ”Medel”. |
| `component::matter::entity::select::door_lock_sound_volume::state::low` | [%key:common::state::low%] | [%key:common::state::low%] | Behåll referensen; målet är ”Low” → ”Låg”. |
| `component::matter::entity::select::door_lock_sound_volume::state::high` | [%key:common::state::high%] | [%key:common::state::high%] | Behåll referensen; målet är ”High” → ”Hög”. |
| `component::matter::entity::select::door_lock_sound_volume::name` | Sound volume | Ljudvolym | Behåll. |
| `component::matter::entity::sensor::window_covering_target_position::name` | Target opening position | Målöppningsposition | Föreslå: Målposition för öppning. Tydligare sammansättning. |
| `component::matter::entity::sensor::min_pin_code_length::name` | Min PIN code length | Minsta längd på PIN-kod | Behåll. |
| `component::matter::entity::sensor::max_pin_code_length::name` | Max PIN code length | Maximal längd på PIN-kod | Föreslå: Största längd på PIN-kod. Ger ett konsekvent par med ”minsta”. |

## Kompletterande ID-kontroll

Den 19 november kontrollerades nyckel-ID:n i Lokalises filtrerade sökresultat. De åtta nedanstående nycklarna har sammanhängande ID:n, men tabellen ovan är inte i samma ordning:

- 653073967: `component::matter::entity::sensor::window_covering_target_position::name`
- 653073966: `component::matter::entity::sensor::min_pin_code_length::name`
- 653073965: `component::matter::entity::sensor::max_pin_code_length::name`
- 653073964–653073960: `component::matter::entity::select::door_lock_sound_volume::state::silent`, `state::medium`, `state::low`, `state::high` respektive `name`.

ESA-nycklarna `state::fault` och `name` har ID 653106086 respektive 653106085. Detta stöder att rapporten täcker den misstänkta luckan 38 555–38 564, men filtrerade sökningar och ID-ordning bevisar inte den fullständiga ofiltrerade ordningen mellan dessa grupper. Verifiera därför intervallet mot en fullständig ögonblicksbild innan positionsluckan stängs.

## Avstämning mot den historiska PO-exporten

Den 19 november jämfördes angränsande nyckel-ID:n mot [Core-PO-ögonblicksbilden från 24 oktober](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core.po). Den föregående rapporten slutar med `esa_state::state::offline` (653106087) och den följande börjar med `pir_occupied_to_unoccupied_delay::name` (653073959). Bland posterna i PO-exporten finns exakt de tio nycklar som listas ovan med ID strikt mellan dessa båda gränser. De kommer i ordningen 653106086, 653106085 och 653073967–653073960.

Detta stärker stödet för att de tio dokumenterade Matter-nycklarna täcker den misstänkta positionsluckan i den historiska **icke arkiverade, tvåspråkiga PO-exporten**. Det fastställer inte att Lokalises äldre ofiltrerade lista hade samma urval eller att alla nuvarande nycklar är granskade; arkiverade, tomma och senare tillkomna poster kan saknas i exporten. Positionsluckan kan därför inte stängas för hela projektet enbart med detta underlag. Inga ändringar gjordes i Lokalise.


**Uppdatering:** Förslagen om målposition och maximal PIN-kodslängd har sparats och återlästs; se [ändringsloggen](sparade-andringar-matter-sensorer.md). Tabellens tidigare svenska värden är historiska.
