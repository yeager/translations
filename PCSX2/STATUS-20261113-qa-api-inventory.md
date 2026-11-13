# PCSX2: svensk QA-inventering via Crowdin API, 13 november 2026

## Underlag

Crowdins API för projekt `PCSX2 Emulator` (`561203`), svenska och den aktiva filen `15` returnerade 1 626 diagnostikrader från QA-ändpunkten vid den förnyade hämtningen den 13 november. Progressändpunkten rapporterar samtidigt 1 544 misslyckade och 3 787 godkända QA-kontroller. De två ändpunkterna räknar alltså inte samma sak och siffrorna ska inte tolkas som en radvis språkgranskning.

| Kontrolltyp | Antal |
| --- | ---: |
| `spellcheck` | 1 486 |
| `special_symbols` | 71 |
| `punctuation` | 58 |
| `numbers` | 5 |
| `symbol_register` | 5 |
| `variables` | 1 |

De första posterna visar att stavningskontrollerna bland annat träffar `PCSX2`, `RetroAchievements`, `PlayStation`, `GitHub-förråd`, `MIPS-processortolkar` och `omkompilatorer`. Dessa är produktnamn, tekniska termer eller svenska sammansättningar och inte bevis på felaktig måltext.

En frekvensinventering av stavningskön bekräftar samma mönster: de vanligaste träffarna är bland annat `PCSX2`, `D-Pad`, `RetroAchievements`, `TV-shader`, `Bilinjär`, `Trilinjär`, `Bildrutehastighet` och `Förinläsning`. Hunspell-sv saknar flera av de projektbundna formerna, bland annat `PCSX2`, `TV-shader`, `Bildrutehastighet`, `Discord-närvaro` och den böjda formen `hårdvarurenderaren`; det är ordlisteluckor och inte automatiska språkfel. Svlang markerar på motsvarande sätt tekniska termer som sällsynta. Terminologilistan har uppdaterats för att styra fortsatt manuell granskning.

## Radgranskning: skiljetecken

Alla 58 rader i kategorin `punctuation` har lästs mot den aktuella XLIFF-exporten den 13 november. De fyra rader som använder den direkta kontrollen `punctuation_check` är `13366`, `15698`, `16059` och `16165`; samtliga är falska positiva. Svenska helmeningar har korrekt avslutande punkt även när källtexten saknar den, och citattecknen runt platshållaren `%1` i `13366` är korrekta.

Återstående 54 rader använder `spaces_after_punctuation_check`. De granskade exemplen innehåller HTML-kodning, avsiktligt oförändrade tekniska värden eller en redan existerande korrekt kandidat. Till exempel har post `6237` redan förslag `449191` med *i stället* i stället för den äldre aktiva formen *istället*. Inga dubblettförslag, röster eller QA-avfärdanden skapades i denna genomgång.

## Radgranskning: specialtecken

Genomgången av `special_symbols` identifierade två verkliga felaktiga aktiva val i exporten. Post `5379` har källformatet `%1 (%2)`, men den aktiva måltexten är den orelaterade nätverksstatusen *Ansluten till %1:%2: skickar begäran*. Den korrekta kandidaten `%1 (%2)` finns redan som förslag `252904`. Post `13439` har en äldre aktiv måltext med bland annat felaktigt mellanrum i `GPU: n`; tre nyare, radgranskade svenska kandidater finns redan som `448997`, `449477` och `449817`.

Ingen av dessa kandidater är vald eller upstreamgranskad. Därför skapades inga dubblettförslag och inga befintliga förslag manipulerades. De behöver väljas av en projektbehörig granskare innan den aktiva exporten kan betraktas som reparerad.

Kontrollerna `numbers` och `symbol_register` gav ytterligare en faktisk katalogskada: post `6067` är registerförkortningen `PC` (programräknare) men har aktiv måltext `st`. Den korrekta, avsiktligt oförändrade kandidaten `PC` finns redan som `255694`. Övriga träffar i dessa två kontrolltyper är korrekta tal utskrivna med svenska ord, avsiktlig versalisering av handkontrollknappen `START`, eller etablerade tekniska termer. Även dubbelposterna för TV-shader har redan granskat förslag (`449081` och `449079`).

## L10n-varningar med svensk måltext

L10n-lint träffade ett dubbelmellanrum i två felmeddelanden (`11416` och `11448`) och det dubbla ordet *och* i `10874`. Korrekt form finns redan som kandidaterna `449197`, `449227` och `449225`. Sträng `16251` träffas därför att *Välj* förekommer både som synligt knappnamn och som verb i instruktionen; formuleringen är grammatisk och ändrades inte. Inga nya kandidater behövdes.

Procentvarningarna granskades också mot UI-kontexten. Reglageetiketter och de två SoundTouch-hjälptexterna har redan korrekta svenska kandidater: `449207` och `449209` förbättrar den språkligt felaktiga ljudtidssträckningstexten, medan `119161`, `119879` och `449177` till `449189` använder svenskt mellanrum före procenttecknet. Inga dubblettförslag skapades.

## Beslut

Inga QA-poster har avfärdats eller massgodkänts. Formateringskontroller ska jämföras med exakt käll- och måltext före varje rättning. Stavningsposter behandlas endast när den konkreta svenska formuleringen är fel, inte därför att Crowdins ordlista saknar termen.

## Första radgranskade rättningen

Post `8827` är den parallella informationstexten i FullscreenUI. Den exporterade måltexten hade bland annat engelsk apostrof i `PS2&amp;apos;s`, oböjd term `Recompilers` och en oidiomatisk ordföljd. En ny, ogranskad Crowdin-kandidat med översättnings-id `449931` skickades via API den 13 november 2026 och återlästes direkt efteråt.

Under kontrollen upptäcktes att post `3113` i AboutDialog redan hade en bättre exporterad måltext än den nyss skapade kandidaten. Kandidaten `449927` drogs därför tillbaka och dess frånvaro bekräftades med API-svaret 404. En ännu tidigare kandidat, `449925`, som saknade HTML-strukturen, hade redan raderats. Ingen befintlig översättning eller godkännandestatus ändrades. Kandidaten `449931` är inskickad men ännu inte upstreamgranskad eller vald som aktiv översättning.

Post `10498` i FullscreenUI använder den källspecifika förklaringen "auto fire". Den tidigare svenska kandidaten behöll det engelska uttrycket. Efter kontroll mot källans inställningskontext skickades därför kandidat `449929` med *automateld*. Den återlästes direkt; Hunspell-sv hade inga träffar och svlang bedömde formuleringen som naturlig svenska. Även denna kandidat är ogranskad och inte vald som aktiv översättning.

## Fortsatt exportgranskning

Tre ytterligare FullscreenUI- och ljudinställningsposter skickades som ogranskade kandidater och återlästes via API:

| Sträng | Kandidat | Beslut |
| --- | ---: | --- |
| `11360` | `449933` | Rättar felaktig *utdatavolym* till *snabbspolningsvolym*. |
| `11304` | `449935` | *5.1 Surround* normaliseras till *5.1-surroundljud*. |
| `11306` | `449937` | *7.1 Surround* normaliseras till *7.1-surroundljud*. |

Hunspell-sv och svlang hade inga språkvarningar för dessa tre kandidater. Post `3449` för procentformatet hade redan kandidaten `%1 %`; Crowdins API avvisade en identisk inskickning med `Duplicate translation`. Ingen röst eller befintlig kandidat ändrades.

## Exportens radbrytningsfel

L10n-lint markerar post `10288` eftersom den aktiva översättningen saknar en av källtextens tre radbrytningar. Den svenska kandidaten `448991` har samma fyra stycken och tre radbrytningar som källtexten, korrekt böjning och konsekvent UI-terminologi. Den återlästes från Crowdins API den 13 november. Ingen ny kandidat skickades, eftersom den redan täcker rättningen. En senare kandidat, `449921`, har samma radbrytningsfel som den aktiva måltexten och ska inte väljas.

## FullscreenUI: beskrivande form

Post `17295` är hjälptexten för FXAA-kantutjämning. Källtexten beskriver vad inställningen gör, medan den aktiva svenska texten felaktigt använder uppmaningsformen *Tillämpa*. Den korrekta kandidat `449735`, *Tillämpar FXAA-kantutjämningsalgoritmen för att förbättra spelens visuella kvalitet.*, återlästes från Crowdins API den 13 november. Ingen ny kandidat skapades; den befintliga kandidaten är inte vald eller upstreamgranskad.
