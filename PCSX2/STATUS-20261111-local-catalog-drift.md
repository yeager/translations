# PCSX2: lokal katalog avviker från verifierad Crowdin-status

Datum: 11 november 2026

## Handkontrollsformuleringar: fyrtionde granskningsbatchen

Fyra närliggande handkontrollstexter rättas. Ett felmeddelande ersätter den
krystade snedstreckskonstruktionen med tydlig svenska. Två pausinställningar
anger en handkontroll i singular, och den analoga PS1-handkontrollen får rätt
form.

Lokal deltafil: `pcsx2-sv-controller-wording-batch-40-20261111.xliff`
(sträng-ID 3611, 11418, 11430 och 17735). Lokal granskning och kontroller
genomfördes före arkivering och Crowdin-inskick.

XML-validering, exakt källtextjämförelse, l10n-lint, diffkontroll och Gitleaks
passerar. svlangs V2-varning är en falsk positiv på ett samordnat subjekt.
Hunspell-SV markerar endast `PS1-handkontroll` och XLIFF-entiteten `apos`.
`msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 4 strängar och 28 ord importerades, 0
godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända
förslagen är 449263, 449265, 449267 och 449269. Detta är ett upstream-inskick,
inte upstream-granskning eller merge.

## Multitap: trettionionde granskningsbatchen

Projektets not anger att `Multitap` är ett Sony-relaterat tekniskt namn och
det behålls därför. Fyra närliggande texter får i stället korrekt svensk
omgivande text: handkontroller skrivs ut, konsolport får gemen begynnelsebokstav
och hjälptexten blir idiomatisk.

Lokal deltafil: `pcsx2-sv-multitap-labels-batch-39-20261111.xliff`
(sträng-ID 3699, 3701, 3703 och 3705). Lokal granskning och kontroller
genomfördes före arkivering och Crowdin-inskick.

XML-validering, exakt källtextjämförelse, l10n-lint, diffkontroll och Gitleaks
passerar. svlang och Hunspell-SV markerar endast det avsiktligt bevarade
tekniska namnet `Multitap`. `msgfmt --check` kan inte tolka XLIFF och är därför
ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 4 strängar och 37 ord importerades, 0
godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända
förslagen är 449255, 449257, 449259 och 449261. Detta är ett upstream-inskick,
inte upstream-granskning eller merge.

## Handkontrollsmappning: trettioåttonde granskningsbatchen

Installationsguidens och inställningsdialogens närliggande etiketter
normaliseras till läsbara svenska. Felaktiga pluralformer och en felaktig
sammansättning ersätts med `handkontroll`, `typ av handkontroll` och
`handkontrollsmappning`. Den inbäddade HTML-hjälptexten förklarar nu tydligt
hur fysiska handkontroller mappas till emulerade handkontroller.

Lokal deltafil: `pcsx2-sv-controller-mapping-labels-batch-38-20261111.xliff`
(sträng-ID 7391, 7435, 7437, 9491, 10922 och 10924). Lokal granskning och
kontroller genomfördes före arkivering och Crowdin-inskick.

XML-validering, exakt källtextjämförelse, l10n-lint, diffkontroll och Gitleaks
passerar. svlangs enda V2-varning är en falsk positiv från XLIFF-HTML.
Hunspell-SV markerar bara markup och fackformen `mappning`. `msgfmt --check`
kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 6 strängar och 54 ord importerades, 0
godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända
förslagen är 449243, 449245, 449247, 449249, 449251 och 449253. Detta är ett
upstream-inskick, inte upstream-granskning eller merge.

## Installationsguidens handkontroller: trettiosjunde granskningsbatchen

Installationsguidens längre HTML-text för handkontroller granskas rad för rad.
Den har fått korrekt singularform, rättad stavning och idiomatisk svensk
ordföljd. `Multitap` behålls eftersom projektet anger det som ett
Sony-relaterat tekniskt namn. Länk, HTML-struktur och synliga menyval bevaras.

Lokal deltafil: `pcsx2-sv-setup-controller-guide-batch-37-20261111.xliff`
(sträng-ID 11112). Lokal granskning och kontroller genomfördes före arkivering
och Crowdin-inskick.

XML-validering, exakt källtextjämförelse, l10n-lint, diffkontroll och Gitleaks
passerar. svlangs V2-varningar är falska positiva från XLIFF-HTML och korrekta
infinitivfraser. Hunspell-SV markerar endast produktnamn, `Multitap` och
markup. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för
denna fil.

Crowdin-importen verifierades via API: 1 sträng och 126 ord importerades, 0
godkändes automatiskt och inget hoppades över. Det skapade, ännu ej godkända
förslaget är 449241. Detta är ett upstream-inskick, inte upstream-granskning
eller merge.

## Handkontroller i singular: trettiosjätte granskningsbatchen

Fem sammanhängande UI-texter använde felaktigt formen `handkontroller` om en
enda enhet. De normaliseras till `handkontroll`. Uppmaningen om att välja
knapp eller axel skrivs om så att den blir lättare att läsa och bevarar
funktionen i inmatningsdialogen.

Lokal deltafil: `pcsx2-sv-controller-singular-batch-36-20261111.xliff`
(sträng-ID 3589, 8027, 11374, 11434 och 11454). Lokal granskning och
kontroller genomfördes före arkivering och Crowdin-inskick.

XML-validering, exakt källtextjämförelse, l10n-lint, svlang, Hunspell-SV,
diffkontroll och Gitleaks passerar. `msgfmt --check` kan inte tolka XLIFF och
är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 5 strängar och 32 ord importerades, 0
godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända
förslagen är 449231, 449233, 449235, 449237 och 449239. Detta är ett
upstream-inskick, inte upstream-granskning eller merge.

## QT-värdens felmeddelanden: trettiofemte granskningsbatchen

Två meddelanden från QT-värden rättas. Sparfel för spelinställningar får
direkt och idiomatisk ordföljd utan dubbelt mellanslag. Meddelandet om en
ansluten handkontroll får korrekt singular form.

Lokal deltafil: `pcsx2-sv-qthost-errors-batch-35-20261111.xliff`
(sträng-ID 11448 och 11450). Lokal granskning och kontroller genomfördes före
arkivering och Crowdin-inskick.

XML-validering, exakt källtextjämförelse, l10n-lint, svlang, Hunspell-SV,
diffkontroll och Gitleaks passerar. `msgfmt --check` kan inte tolka XLIFF och
är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 2 strängar och 9 ord importerades, 0
godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända
förslagen är 449227 och 449229. Detta är ett upstream-inskick, inte
upstream-granskning eller merge.

## Gränssnittsinställningar: trettiofjärde granskningsbatchen

Hjälptexten för gränssnittsinställningarna hade en upprepad konjunktion och
en onödigt abstrakt formulering. Den förklarar nu direkt att alternativen styr
hur programmet ser ut och beter sig. Synliga kortkommandon, XLIFF-HTML och
panelens funktion bevaras.

Lokal deltafil: `pcsx2-sv-interface-settings-batch-34-20261111.xliff`
(sträng-ID 10874). Lokal granskning och kontroller genomfördes före
arkivering och Crowdin-inskick.

XML-validering, exakt källtextjämförelse, l10n-lint, svlang, diffkontroll och
Gitleaks passerar. Hunspell-SV markerar enbart XLIFF-entiteterna `br`, `gt`,
`hr` och `lt`. `msgfmt --check` kan inte tolka XLIFF och är därför ej
tillämplig för denna fil.

Crowdin-importen verifierades via API: 1 sträng och 33 ord importerades, 0
godkändes automatiskt och inget hoppades över. Det skapade, ännu ej godkända
förslaget är 449225. Detta är ett upstream-inskick, inte upstream-granskning
eller merge.

## Långsam uppspelning och snabbspolning: trettiotredje granskningsbatchen

Katalogen blandar tidigare `slowmotion`, `slow-motion` och den redan etablerade UI-formen `långsam uppspelning`. Fem sammanhängande etiketter och hjälptexter normaliseras till `långsam uppspelning`; snabbtangenter skrivs som begripliga fraser i stället för långa sammansättningar. Snabbspolningens hjälptext får också korrekt svensk ordföljd.

Lokal deltafil: `pcsx2-sv-slow-motion-batch-33-20261111.xliff` (sträng-ID 6361, 6369, 6371, 8121 och 6677). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, Hunspell-SV, diffkontroll och Gitleaks passerar. svlangs enda varning gäller en avsiktlig passiv form i en kort inställningsbeskrivning. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 5 strängar och 32 ord importerades, 0 godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända förslagen är 449215, 449217, 449219, 449221 och 449223. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

## Makrots tryckkänslighet: trettioandra granskningsbatchen

Hjälptexten för tryckkänsliga knappmakron förenklas till idiomatisk svenska. Reglagets funktion och villkoret att makrot är aktivt bevaras.

Lokal deltafil: `pcsx2-sv-macro-pressure-batch-32-20261111.xliff` (sträng-ID 6311). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, Hunspell-SV, diffkontroll och Gitleaks passerar. svlangs V2-varning är en falsk positiv för en korrekt inledd prepositionsfras. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 1 sträng och 20 ord importerades, 0 godkändes automatiskt och inget hoppades över. Det skapade, ännu ej godkända förslaget är 449213. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

## Analysalternativ: trettioförsta granskningsbatchen

Dialogens hjälptext får idiomatisk svensk ordföljd. Den skiljer nu också tydligt mellan den globala inställningsdialogen och dialogen för enskilda spel.

Lokal deltafil: `pcsx2-sv-analysis-options-batch-31-20261111.xliff` (sträng-ID 12610). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, Hunspell-SV, diffkontroll och Gitleaks passerar. svlangs V2-varningar är falska positiva för korrekt svensk ordföljd. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 1 sträng och 27 ord importerades, 0 godkändes automatiskt och inget hoppades över. Det skapade, ännu ej godkända förslaget är 449211. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

## SoundTouch-tidssträckning: trettionde granskningsbatchen

Tre sammanhängande ljudinställningar normaliseras till den etablerade termen `tidssträckning`, som även används i termbasen och i närliggande emulatorprojekt. `SoundTouch` behålls som produktnamn. Texten förklarar nu att ljudet sträcks eller krymps för att hålla bufferten inom gränserna, och procenttecknet får korrekt svenskt mellanrum.

Lokal deltafil: `pcsx2-sv-soundtouch-tidsstrackning-batch-30-20261111.xliff` (sträng-ID 3429, 11270 och 11324). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, diffkontroll och Gitleaks passerar. svlangs varningar kommer från den inbäddade HTML-strängen och det tekniska sammansatta namnet `SoundTouch-tidssträckaren`; Hunspell-SV markerar enbart detta produktnamn. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 3 strängar och 95 ord importerades, 0 godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända förslagen är 449205, 449207 och 449209. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

## GunCon2-hjälptext: tjugonionde granskningsbatchen

GunCon2:s hjälpruta för mus och ljuspistol rättas rad för rad. Stavfelet `kontrollera` ersätts med `handkontroll`, `Om inte` med korrekt `Annars` och `i stället` följer svensk stavning. `Relative Aiming` bevaras som synligt Sony-relaterat UI-namn.

Lokal deltafil: `pcsx2-sv-guncon2-help-batch-29-20261111.xliff` (sträng-ID 7883). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, diffkontroll och Gitleaks passerar. svlangs V2-varning och Hunspell-SV:s träffar gäller de bevarade UI- och produktnamnen `Relative Aiming` och `GunCon2`. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 1 sträng och 71 ord importerades, 0 godkändes automatiskt och inget hoppades över. Det skapade, ännu ej godkända förslaget är 449203. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

## Inloggningstoken för RetroAchievements: tjugoåttonde granskningsbatchen

En informationsruta i inloggningsdialogen får idiomatisk svensk ordföljd och normaliserad stavning av `i stället`. Meningen delas före tokenhanteringen, vilket gör att lösenordets behandling och åtkomsttokenens roll framgår tydligt.

Lokal deltafil: `pcsx2-sv-achievement-token-batch-28-20261111.xliff` (sträng-ID 7895). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, Hunspell-SV, diffkontroll och Gitleaks passerar. svlangs varningar kommer från HTML-markeringen och produktnamnen, inte den svenska formuleringen. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 1 sträng och 38 ord importerades, 0 godkändes automatiskt och inget hoppades över. Det skapade, ännu ej godkända förslaget är 449201. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

## Oavsiktliga dubbla mellanslag: tjugosjunde granskningsbatchen

Två vanliga UI-texter har oavsiktliga dubbla mellanslag. De reduceras till ett mellanslag. Formaterade kolumner i avlusarvyn lämnas uttryckligen utanför eftersom deras mellanslag är layoutdata.

Lokal deltafil: `pcsx2-sv-double-space-batch-27-20261111.xliff` (sträng-ID 11416 och 6413). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, diffkontroll och Gitleaks passerar. svlangs V2-varning gäller det synliga tekniska alternativnamnet `Spin GPU During Readbacks`. Hunspell-SV har inga språkträffar. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 2 strängar och 23 ord importerades, 0 godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända förslagen är 449197 och 449199. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

## I stället, fortsättning: tjugosjätte granskningsbatchen

Tre återstående granskade UI-texter med den sammanskrivna formen `istället` normaliseras till `i stället`. Ett tidigare förslag för realtidsklockan fanns redan upstream och lämnas därför utanför denna deltafil.

Lokal deltafil: `pcsx2-sv-i-stallet-batch-26-20261111.xliff` (sträng-ID 6237, 10982 och 7515). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, diffkontroll och Gitleaks passerar. svlangs V2-varningar gäller korrekta imperativ och tekniska formuleringar. Hunspell-SV markerar endast förkortningen `TLB`. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 3 strängar och 107 ord importerades, 0 godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända förslagen är 449191, 449193 och 449195. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

## Cykelhastighet och procent: tjugofemte granskningsbatchen

Sju synliga cykelhastighetsalternativ saknade svenskt mellanrum före procenttecknet. Etiketterna normaliseras enligt svensk typografi till exempelvis `50 % (Underklockning)`. Ingen sifferuppgift eller inställningsbetydelse ändras.

Lokal deltafil: `pcsx2-sv-cycle-rate-percent-spacing-batch-25-20261111.xliff` (sträng-ID 4233, 4235, 4237, 4239, 4241, 4243 och 4245). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, svlang, Hunspell-SV, diffkontroll och Gitleaks passerar utan språkfynd. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 7 strängar och 15 ord importerades, 0 godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända förslagen är 449177, 449179, 449181, 449183, 449185, 449187 och 449189. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

## Konsol, prestationer och VSync: tjugofjärde granskningsbatchen

Fem korta UI-texter innehöll antingen grammatisk felaktighet eller onödiga engelska restord. Den virtuella konsolen får rätt genus, `sparade spel` ersätts av den mer precisa formuleringen `sparningar i spelet`, och prestationshanteringen får korrekt bestämd form. `VSync` behålls som synligt tekniskt namn, medan `host` översätts till `värden` konsekvent i båda förekomsterna.

Lokal deltafil: `pcsx2-sv-console-achievements-vsync-batch-24-20261111.xliff` (sträng-ID 13068, 9615, 11460, 11476 och 11478). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, diffkontroll och Gitleaks passerar. svlangs V2-varning är en falsk träff på en grammatisk korrekt huvudsats. Hunspell-SV markerar endast produkt- och facktermerna PCSX2, RAIntegration, VSync, `bildrutetidtagning` och `sparningar`. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 5 strängar och 53 ord importerades, 0 godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända förslagen är 449167, 449169, 449171, 449173 och 449175. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

## I stället: tjugotredje granskningsbatchen

Nio UI-texter från inmatning, minneskort och grafik använder den sammanskrivna formen `istället`. De normaliseras till den rekommenderade stavningen `i stället`, utan att ändra funktion, platshållare eller synliga produktnamn.

Lokal deltafil: `pcsx2-sv-i-stallet-batch-23-20261111.xliff` (sträng-ID 3689, 3695, 13976, 12918, 11370, 10496, 6543, 10654 och 7557). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, diffkontroll och Gitleaks passerar. svlangs V2-varningar gäller korrekta imperativ och tekniska namn i UI-texterna. Hunspell-SV markerar endast tekniska namn och facktermer: DInput, DirectInput, framebuffer, SDL, XInput och `sparningsplatser`. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 9 strängar och 179 ord importerades, 0 godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända förslagen är 449149, 449151, 449153, 449155, 449157, 449159, 449161, 449163 och 449165. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

## CPU-spriterendering: tjugoandra granskningsbatchen

Sex etiketter och hjälptexter för samma grafikfunktion hade både engelska resttermer och tre olika svenska konstruktioner. `sprite` behålls som etablerad datorspels- och grafikterm, men `render` normaliseras till `rendering`. Den befintliga, redan konsekventa etiketten `CPU Sprite Render Size:` → `Storlek för CPU-spriterendering:` styr valet.

Lokal deltafil: `pcsx2-sv-cpu-sprite-rendering-batch-22-20261111.xliff` (sträng-ID 8299, 8303, 8305, 10522, 17359 och 17361). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, diffkontroll och Gitleaks passerar. svlang och Hunspell-SV markerar endast den sammansatta facktermen `CPU-spriterendering`, inte svensk prosa. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 6 strängar och 30 ord importerades, 0 godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända förslagen är 449137, 449139, 449141, 449143, 449145 och 449147. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

## Programvarurendering av CLUT: tjugoförsta granskningsbatchen

De två aktuella UI-etiketterna `Software CLUT Render` hade blandade svensk-engelska översättningar: `Mjukvarubaserad CLUT Render` och `Programvara CLUT Render`. De normaliseras till `Programvarurendering av CLUT`, i linje med den befintliga etiketten `Software CLUT Render:` → `Programvarurendering av CLUT:`. CLUT behålls som den etablerade tekniska förkortningen.

Lokal deltafil: `pcsx2-sv-software-clut-render-batch-21-20261111.xliff` (sträng-ID 8307 och 6535). Lokal granskning och kontroller genomförs före arkivering och Crowdin-inskick. Upstream-resultat förs in här först efter verifierad API-import.

XML-validering, exakt källtextjämförelse, l10n-lint, diffkontroll och Gitleaks passerar. svlang och Hunspell-SV markerar endast den tekniska förkortningen `CLUT`, inte svensk prosa. `msgfmt --check` kan inte tolka XLIFF och är därför ej tillämplig för denna fil.

Crowdin-importen verifierades via API: 2 strängar och 6 ord importerades, 0 godkändes automatiskt och inget hoppades över. De skapade, ännu ej godkända förslagen är 449133 för sträng-ID 8307 och 449135 för sträng-ID 6535. Detta är ett upstream-inskick, inte upstream-granskning eller merge.

Den lokala filen `pcsx2-qt_sv-SE.ts` kontrollerades inför nästa
kvalitetsgranskning. Den innehåller 4 057 meddelanden, varav 202 är markerade
`unfinished`. `l10n-lint` rapporterar därför 202 saknade översättningar, men
även 52 gränsteckenavvikelser, 45 procentmellanrumsvarningar, 27 lika
käll- och måltexter, 18 längdförhållanden och 8 konsekvensfynd.

Detta motsäger den senaste autentiserade Crowdin-kontrollen, som visar 5 313
av 5 313 översatta fraser i den aktiva svenska filen. Den lokala TS-filen är
alltså inte en tillräckligt aktuell källa för att skapa eller skicka en ny
deltafil. Inga översättningar har ändrats eller skickats i denna kontroll.

`svlang check --file` och Hunspell-SV på den fullständiga lokala katalogen
avbröts efter 30 sekunder utan resultat. De behöver köras mot en ny,
avgränsad export eller en mindre granskningsbatch. Detta är ett verktygs- och
inmatningsomfångsproblem, inte ett godkänt språktest.

Nästa steg är att hämta en färsk Crowdin-export, jämföra den mot denna
arkiverade fil och först därefter granska faktiska QA-fynd rad för rad.

## Färsk export 2026-11-11

En ny XLIFF-export, `pcsx2-qt_en_sv-SE.xliff`, hämtades lokalt och har nu
arkiverats som granskningens bas. XML-valideringen passerar. Exporten innehåller
5 345 käll- och målsegment och samtliga målsegment har status `translated`.

Den ersätter den äldre arkiverade exporten med 4 087 segment. Jämförelsen visar
1 983 nya segment, 725 borttagna segment och 58 ändrade gemensamma segment. Det
är därför den nya exporten, inte den gamla TS-filen, som används för fortsatt
radvis granskning. Ingen översättning har ändrats eller skickats i detta steg.

## Första åtgärdsbatchen

`l10n-lint` på den färska exporten pekar ut sju fel, fördelade på sex
meddelanden. Fem av dem var innehållsmässigt korrupta måltexter: två
Vulkan-poster innehöll ett orelaterat initieringsfel, en tidsformatpost och en
USB-etikett innehöll orelaterad text, och en inmatningsprofiltext saknade en
radbrytning. Den återstående träffen gällde multiplikationstecknet i en
Qt-platsmarkör och rättas genom att bevara källformatet `%1x%2 (%3x)`.

Den granskade importfilen
`pcsx2-sv-l10n-lint-errors-batch-01-20261111.xliff` innehåller de sex
korrekta måltexterna. XML-validering, l10n-lint, svlang, Hunspell-SV,
diffkontroll och Gitleaks har körts. svlangs enda anmärkning och Hunspell-SV:s
tre träffar gäller XLIFF-entiteten `apos` och Qt-platsmarkörerna, inte svensk
prosa. Batchen är lokalt granskad. Den skickades till Crowdins etablerade
importflöde den 11 november. Importresultatet var **0 tillagda**, **0
godkända** och **6 hoppade över** översättningar. Crowdins detaljrapport
redovisar noll behandlade strängar för `pcsx2-qt_en.ts`. Filen har alltså nått
upstreams importflöde, men inga av batchens ändringar har införts upstream.

Efter importsvaret jämfördes deltafilen med Crowdins kompletta XLIFF-export.
Varje måltext i den kompletta exporten har attributet `state="translated"`,
en verktygsdeklaration och en källkontext. Samma metadata har lagts till i den
lokala importkandidaten utan att någon källa eller svensk måltext har ändrats.
XML-validering, l10n-lint, diffkontroll och Gitleaks passerar även efter
formatändringen.

Den kontextbevarade filen skickades därefter på nytt, med alternativet som
tillåter en måltext lika med källtext aktiverat för avsiktliga UI-namn och
formatsträngar. Crowdins resultat var åter **0 tillagda**, **0 godkända** och
**6 hoppade över**. Importkanalen tar alltså emot filen men tillämpar inte de
sex posterna i den här rollen eller projektkonfigurationen. Fler identiska
återförsök görs inte automatiskt; ingen av batchens ändringar är verifierad
upstream.

## Livekontroll 2026-11-11

Den inloggade Crowdin-projektvyn för `pcsx2-emulator`, svenska, visar
**100 % översatt**, **0 % godkänt** och **0 ord** kvar. Den enda aktiva filen
är `pcsx2-qt_en.ts`, med 100 % översättning. Gränssnittets XLIFF-export valdes
för att hämta den aktuella katalogen, men Chrome blockerade den signerade
nedladdningsvärden med `ERR_BLOCKED_BY_CLIENT` innan någon fil sparades.
Detta inträffade före den färska export som senare arkiverades ovan.

## Senast lämnade TS-fil och kontroll av Crowdin-dubbletter

Filen `pcsx2-qt_sv-SE.ts` som lades i Hämtade den 11 november har filsystemets
skapande- och ändringstid `2026-10-10 14:18:09`. Den innehåller 4 057
meddelanden och 202 oavslutade poster och är därför samma äldre katalog som
beskrivs i början av detta dokument, inte en ny grund för import.

I Crowdins redigerare kontrollerades de två Vulkan-poster som l10n-lint
markerat. En korrekt svensk översättning, `Vulkan`, finns redan som förslag
från en annan översättare; de gamla felaktiga måltexterna finns fortfarande
som separata poster. Crowdin klassar ett nytt `Vulkan` som dubblett och erbjuder
bara röstning eller godkännande av originalet. Ingen röst, inget godkännande
och ingen dubblett sparades. Eventuella osparade försök rensades och editorn
visar därefter inga osparade översättningar.

## Dubblettspärr verifierad på nytt

I den aktuella svenska PCSX2-redigeraren kontrollerades den aktiva posten
`GraphicsSettingsWidget['Vulkan']` igen. Den felaktiga måltexten är fortfarande
`Fel vid initiering av Vulkan-renderare:\n{}`, medan den fristående korrekta
översättningen `Vulkan` finns i samma strängs förslagslista. När `Vulkan`
anges som ny måltext markerar Crowdin den som dubblett och inaktiverar vanlig
sparning med meddelandet att den ursprungliga översättningen ska röstas på
eller godkännas. Ändringen ångrades innan sidan lämnades.

Det bekräftar att den etablerade import- och redigerarrollen inte kan föra in
den här rättningen utan en projektgodkänd metod för dubbletter. Varken röstning
eller godkännande har utförts. Upstream-status för den lokala batchen är därför
fortfarande: **ej införd**.

## API-kontroll av första åtgärdsbatchen

Crowdin API kontrollerades därefter direkt för samtliga sex sträng-ID:n i
första åtgärdsbatchen. Varje korrekt måltext finns redan som en fristående
svensk översättning: den korrigerade inmatningsprofilen, det oförändrade
Qt-formatet `%1x%2 (%3x)`, båda Vulkan-namnen, tidsformatet `{}s` och USB-
etiketten `B 1`. De felaktiga äldre alternativen finns samtidigt kvar i
historiken. Resultatet förklarar de tidigare dubblettavvisningarna och
innebär att batchen inte ska skickas för tredje gången. Ingen röstning eller
godkännande har utförts.

## TS-export kontrollerad på nytt

Filen `pcsx2-qt_sv-SE.ts` i Hämtade kontrollerades på nytt den 11 november.
Den innehåller 5 297 meddelanden, varav fem är oavslutade, och kompilerar med
`lrelease` till 5 292 färdiga och fem oavslutade översättningar. De fem
posterna motsvarar två källtexter: `Target Page Rearranging` och dess
förklarande hjälptext.

De finns redan med de granskade måltexterna `Omordning av målsidor` respektive
`Ordnar om minnessidorna för ett mål om spelet ändrar layouten på den aktuella
VRAM-adressen.` i den nyare, kompletta XLIFF-exporten
`pcsx2-qt_en_sv-SE.xliff`. TS-filen är därför inte en grund för en ny
importfil. XML-validering, `lrelease` och Gitleaks passerade för TS-filen.
Ingen översättning ändrades eller skickades i denna kontroll.

## Ljudtidssträckning: andra granskningsbatchen

Två hjälprutor för SoundTouch-ljudtidssträckaren innehöll en språkligt
bristfällig formulering och saknade mellanrum före procenttecknet. De har
granskats i sin respektive Qt- och HTML-kontext och samlats i
`pcsx2-sv-audio-time-stretch-batch-02-20261111.xliff`:

- `AudioSettingsWidget` anger nu tydligt att det är emuleringen som körs med
  en annan hastighet än 100 %.
- `AudioStretchSettingsDialog` använder samma formulering i den bevarade
  HTML-hjälptexten.

Batchen har två strängar. XML-validering, l10n-lint, diffkontroll och
Gitleaks passerar. Hunspell-SV markerar endast den avsiktliga sammansättningen
`SoundTouch-ljudtidssträckarens`; svlang tolkar HTML-entiteterna och den
sammanhängande hjälprutan som formella respektive längdrelaterade träffar.
`msgfmt` är inte tillämpligt på XLIFF. Den äldre arkiverade PO-filen
`pcsx2-reviewed-crowdin-20260920.po` kan inte heller användas som surrogat:
den har redan 72 dubblettfel i historiska poster. Det är ett separat
arkivproblem och påverkar inte XLIFF-batchens XML- eller platshållarstruktur.
## Installationsguiden: fyrtioförsta granskningsbatchen

`pcsx2-sv-setup-wizard-wording-batch-41-20261111.xliff` granskar sex kortare
strängar i installationsguiden. Den normaliserar `Controller Port` till
`Handkontrollport`, ersätter engelska `game dumps` med `skivavbilder`, rättar
det felstavade `konfígurationsguiden` och gör den rekursiva katalogfrågan
idiomatisk. Texten för inloggningstoken använder preteritum så att tidpunkten
`%2` blir grammatiskt korrekt.

XML-validering, exakt källjämförelse, l10n-lint, diffkontroll och Gitleaks
passerar. svlang ger 10/10; Hunspell-SV markerar endast produktnamnet PCSX2
och XML-entiteterna `apos` och `quot`. `msgfmt` är inte tillämpligt på XLIFF.
Batchen är lokalt granskad.

Batchen skickades via Crowdin API till fil 15 för `sv-SE`. Importen skapade
6 översättningar med 91 ord; 0 godkändes automatiskt och inga strängar
hoppades över. De nya översättningsposterna har ID 449273, 449275, 449277,
449279, 449281 och 449283. De är upstream-inskickade för granskning men ännu
inte upstream-godkända.

## Installationsguiden: fyrtiofjärde granskningsbatchen

`pcsx2-sv-setup-wizard-actions-batch-44-20261111.xliff` normaliserar åtta
etiketter och åtgärder i installationsguiden. `Slutför` används för både
slutsteget och slutknappen. BIOS-mappen och spellistan får bestämd form,
profil- och inloggningsknapparna följer källans tre punkter, och menyalternativ
läggs till `i` respektive meny.

XML-validering, exakt källjämförelse, l10n-lint, diffkontroll och Gitleaks
passerar. svlang ger 10/10 och Hunspell-SV markerar endast produktnamnet
PCSX2. `msgfmt` är inte tillämpligt på XLIFF. Batchen är lokalt granskad och
arkiverad och pushad.

Batchen skickades via Crowdin API till fil 15 för `sv-SE`. Importen skapade
4 översättningar med 7 ord; 0 godkändes automatiskt. Fyra strängar hoppades
över av Crowdins dubblettkontroll, vilket bekräftar att motsvarande korrekta
text redan finns i flödet. De nya översättningsposterna har ID 449295,
449297, 449299 och 449301. De är upstream-inskickade för granskning men ännu
inte upstream-godkända.

## Densha Controller Type 2: fyrtiofemte granskningsbatchen

`pcsx2-sv-densha-controller-batch-45-20261111.xliff` normaliserar den
fysiska enheten till `handkontroll` och förtydligar kraft- och bromsaxlarnas
lägen. Produktnamnet Zuiki One Handle MasCon behålls.

XML-validering, exakt källjämförelse, l10n-lint, diffkontroll och Gitleaks
passerar. svlang och Hunspell-SV markerar endast produktnamn, formatentiteten
`quot`, sammansättningen `tågförarhandkontroll` och projekttermen `mappas`.
`msgfmt` är inte tillämpligt på XLIFF. Batchen är lokalt granskad.

Batchen skickades via Crowdin API till fil 15 för `sv-SE`. Importen skapade
1 översättning med 80 ord; 0 godkändes automatiskt och inga strängar hoppades
över. Den är upstream-inskickad för granskning men ännu inte upstream-godkänd.

## Ryojōhen Controller: fyrtiosjätte granskningsbatchen

`pcsx2-sv-ryojohen-controller-batch-46-20261111.xliff` använder samma
fysiska handkontrollsterminologi och klargör bromsaxelns tre lägen.
Crowdin-importen skapade 1 översättning med 95 ord; 0 godkändes automatiskt
och inga strängar hoppades över. Förslaget är inskickat för granskning men
inte upstream-godkänt.

## Spelkataloger: fyrtiotredje granskningsbatchen

`pcsx2-sv-search-directories-batch-43-20261111.xliff` ersätter den tekniska
formuleringen `Sök rekursivt` med det konkreta gränssnittsalternativet
`Sök i underkataloger` i både tabellkolumnen och följdfrågan. Hjälpetiketten
för sökkataloger använder `genomsöks efter spel`.

XML-validering, exakt källjämförelse, l10n-lint, svlang, Hunspell-SV,
diffkontroll och Gitleaks passerar utan varningar. `msgfmt` är inte
tillämpligt på XLIFF. Batchen är lokalt granskad.

Batchen skickades via Crowdin API till fil 15 för `sv-SE`. Importen skapade
3 översättningar med 11 ord; 0 godkändes automatiskt och inga strängar
hoppades över. De nya översättningsposterna har ID 449289, 449291 och
449293. De är upstream-inskickade för granskning men ännu inte
upstream-godkända.

## Installationsguiden: fyrtioandra granskningsbatchen

`pcsx2-sv-setup-wizard-help-batch-42-20261111.xliff` förtydligar de längre
hjälptexterna för BIOS och välkomststeget. Den använder `PS2-BIOS`,
`BIOS-avbild`, `skapa en BIOS-avbild`, `Gränssnittsinställningar` och en
kortare, idiomatisk formulering av uppdaterings- och nätverksvalen.

XML-validering, exakt källjämförelse, diffkontroll och Gitleaks passerar.
l10n-lint har inga fel; dess två URL-varningar beror på XML-kodad HTML.
svlang och Hunspell-SV analyserar HTML/CSS, URL-delar och produktnamnen som
vanliga ord och är därför inte relevanta språkvarningar. `msgfmt` är inte
tillämpligt på XLIFF. Batchen är lokalt granskad.

Batchen skickades via Crowdin API till fil 15 för `sv-SE`. Importen skapade
2 översättningar med 256 ord; 0 godkändes automatiskt och inga strängar
hoppades över. De nya översättningsposterna har ID 449285 och 449287. De är
upstream-inskickade för granskning men ännu inte upstream-godkända.

## VU-avrundning: femtonde granskningsbatchen

Två hjälprutor för Emotion Engines vektorenheter innehöll den oidiomatiska
slutfrasen `kommer orsaka instabilitet och/eller kraschar`. Båda använder nu
`kommer att orsaka instabilitet och/eller krascher`. Samtidigt har den
onödigt tungrodda formuleringen `den övervägande majoriteten av alla spel`
förkortats till `de allra flesta spel`, utan att innebörd eller kodnamnen
VU0 och VU1 ändras.

`pcsx2-sv-vu-rounding-stability-batch-15-20261111.xliff` är XML-validerad,
har exakt samma källsträngar som den lokala exporten och passerar l10n-lint,
diffkontroll och Gitleaks. Svlang markerar endast en falsk V2-varning i en
infinitivfras bakom den bevarade XML-kodade HTML-taggen. Hunspell-SV
markerar bara produkt- och komponentnamnen PCSX2, Vector Unit, EE, VU0 och
VU1. `msgfmt` är inte tillämpligt på XLIFF och avvisar därför filen som
icke-PO. Batchen är lokalt granskad.

Crowdin-importen är API-verifierad: 2 strängar och 94 ord importerades, inga
strängar hoppades över och 0 godkändes automatiskt. De nya
översättningsposterna är 449093 och 449095, båda skapade 2026-11-11 12:08
UTC. Batchen är upstream-inskickad för granskning men inte
upstream-godkänd.

## Shadercache på disk: sextonde granskningsbatchen

Hjälprutan för cacheinställningen blandade ihop läsning från disk med
allmän ”laddning”. `pcsx2-sv-shader-cache-loading-batch-16-20261111.xliff`
använder `inläsning och lagring`, vilket beskriver cachefunktionen exakt och
undviker att ordet för nätverksnedladdning används i fel sammanhang.

## Flyttalsintervall: sjuttonde granskningsbatchen

Fyra sammanhängande hjälprutor för FPU och VU använder nu konsekvent `de
allra flesta spel` i stället för de tungrodda varianterna `majoriteten av
spel` och `den övervägande majoriteten av alla spel`. VU-kodnamnen skrivs
dessutom korrekt som `VU0` och `VU1` utan extra mellanslag.

## Fusk- och patchvarningar: artonde granskningsbatchen

Den återkommande varningen för fusk och spelpatchar var både inkonsekvent och
delvis engelskspråkig. `pcsx2-sv-cheat-patch-warning-batch-18-20261111.xliff`
normaliserar de fyra förekomsterna till `låsningar` för `soft-locks` och
`skadade sparningar` för `broken saved games`. De längre varningarna använder
också raka uppmaningar och `på egen risk` i stället för ordagranna engelska
konstruktioner.

## VM-prestandavarningar: nittonde granskningsbatchen

Åtta sammanhängande statusvarningar i VM-hanteraren hade engelskinfluerade
kommateckenskonstruktioner, ett dubblerat `detta` och den oidiomatiska
formuleringen `kommer dumpa`. Batchen delar upp meddelandena i korta,
begripliga svenska meningar. Synliga inställningsnamn som `EE Cache`,
`Fastmem`, `Full` och `mVU Flag Hack` bevaras exakt.

## TV-shader: tjugonde granskningsbatchen

Grafikinställningarnas etikett `TV Shader` avvek från den projektspecifika
svenska termen i helskärm, efterbehandling och kortkommandon.
`pcsx2-sv-tv-shader-label-batch-20-20261111.xliff` normaliserar den enda
återstående förekomsten till `TV-shader`.

XML-validering, exakt källjämförelse, l10n-lint, diffkontroll och Gitleaks
passerar. Svlang ger 10/10; Hunspell-SV markerar endast fackordet `shader`.
`msgfmt` är inte tillämpligt på XLIFF och avvisar därför filen som icke-PO.
Batchen är lokalt granskad.

Crowdin-importen är API-verifierad: 1 sträng och 2 ord importerades, inget
hoppades över och 0 godkändes automatiskt. Den nya översättningsposten är
449131, skapad 2026-11-11 12:25 UTC. Batchen är upstream-inskickad för
granskning men inte upstream-godkänd.

XML-validering, exakt källjämförelse, l10n-lint, diffkontroll och Gitleaks
passerar. Svlang ger 8,8/10 och markerar enbart de bevarade synliga
inställningsnamnen; Hunspell-SV markerar samma fack- och produktnamn.
`msgfmt` är inte tillämpligt på XLIFF och avvisar därför filen som icke-PO.
Batchen är lokalt granskad.

Crowdin-importen är API-verifierad: 8 strängar och 74 ord importerades, inga
strängar hoppades över och 0 godkändes automatiskt. De nya
översättningsposterna är 449115, 449117, 449119, 449121, 449123, 449125,
449127 och 449129, alla skapade 2026-11-11 12:19 UTC. Batchen är
upstream-inskickad för granskning men inte upstream-godkänd.

XML-validering, exakt källjämförelse, l10n-lint, diffkontroll och Gitleaks
passerar. Svlangs V2-varningar är falska träffar på det korrekta
infinitivsubjektet `Att aktivera …`; Hunspell-SV markerar endast
produktsammansättningar och PCSX2-namnet. `msgfmt` är inte tillämpligt på
XLIFF och avvisar därför filen som icke-PO. Batchen är lokalt granskad.

Crowdin-importen är API-verifierad: 4 strängar och 89 ord importerades, inga
strängar hoppades över och 0 godkändes automatiskt. De nya
översättningsposterna är 449107, 449109, 449111 och 449113, alla skapade
2026-11-11 12:16 UTC. Batchen är upstream-inskickad för granskning men inte
upstream-godkänd.

XML-validering, exakt källjämförelse, l10n-lint, diffkontroll och Gitleaks
passerar. Svlangs träffar är falska V2-varningar för korrekta bisatser och
infinitivfraser samt de avsiktliga komponentnamnen. Hunspell-SV markerar
enbart produkt- och hårdvarunamn. `msgfmt` är inte tillämpligt på XLIFF och
avvisar därför filen som icke-PO. Batchen är lokalt granskad.

Crowdin-importen är API-verifierad: 4 strängar och 199 ord importerades,
inga strängar hoppades över och 0 godkändes automatiskt. De nya
översättningsposterna är 449099, 449101, 449103 och 449105, alla skapade
2026-11-11 12:13 UTC. Batchen är upstream-inskickad för granskning men inte
upstream-godkänd.

XML-validering, exakt källjämförelse, l10n-lint, diffkontroll och Gitleaks
passerar. Svlang ger 10/10 och markerar bara fackordet `shaders`; Hunspell-SV
markerar samma fackord. `msgfmt` är inte tillämpligt på XLIFF och avvisar
därför filen som icke-PO. Batchen är lokalt granskad.

Crowdin-importen är API-verifierad: 1 sträng och 10 ord importerades, inget
hoppades över och 0 godkändes automatiskt. Den nya översättningsposten är
449097, skapad 2026-11-11 12:10 UTC. Batchen är upstream-inskickad för
granskning men inte upstream-godkänd.

## Patchar och CRC:er: fjärde granskningsbatchen

Den projektbundna termbasen använder `patchar` för PCSX2:s användarval och
`CRC:er` för flera CRC-värden. Den skiljer därmed den här terminologin från
andra program där en patch kan heta korrigering. En radvis kontroll av
inställningsdialogerna hittade både inkonsekventa böjningar (`patcher`) och
flera oidiomatiska CRC-former (`CRCs`).

`pcsx2-sv-patches-crc-batch-04-20261111.xliff` innehåller 13 berörda
strängar: kompatibilitetspatchar, patchar som tar bort sammanflätning,
patchfiler, CRC:er, bildförhållande och den tillhörande hjälprutan. Den
bevarar samtliga formatnamn och `Auto Standard` som synligt UI-namn.

XML-validering, källjämförelse mot den färska XLIFF-exporten, l10n-lint,
diffkontroll och Gitleaks passerar. Hunspell-SV markerar endast den avsiktliga
facktermen `kompatibilitetspatchar` samt den böjda förkortningen `CRC:er`.
svlangs anglicismträffar för `patchar` är falska positiva i just PCSX2, eftersom
projektets termbas anger den termen; den enda V2-varningen är en felanalys av
en bisats. `msgfmt` är inte tillämpligt på XLIFF. Ingen ändring har ännu
skickats upstream i detta steg.

## Emuleringshastighet: femte granskningsbatchen

Sju korta etiketter för EE-cykelfrekvens använde engelskt procentformat utan
mellanrum. `pcsx2-sv-cycle-rate-percent-batch-05-20261111.xliff` infogar
svenskt mellanrum före procenttecknet i underklocknings-, normal- och
överklockningsvärdena. Källtexterna, talen och själva inställningarna är
oförändrade.

XML-validering, exakt källjämförelse mot den färska exporten, l10n-lint,
svlang, Hunspell-SV, diffkontroll och Gitleaks passerar. `msgfmt` är inte
tillämpligt på XLIFF. Ingen ändring har ännu skickats upstream i detta steg.

## Inställningsdialoger: sjätte granskningsbatchen

`pcsx2-sv-settings-copy-batch-06-20261111.xliff` rättar sex fristående
problem i inställningsdialogerna: två felmeddelanden med dubbelt mellanrum,
en felböjd handkontrollsetikett, en otymplig återställningsfråga, den
dubblerade formuleringen i gränssnittshjälpen och en upprepning i
teckensnittsdialogen. HTML-entiteter och radbrytningen före platsmarkören
`{}` bevaras.

XML-validering, exakt källjämförelse mot den färska exporten, l10n-lint,
Hunspell-SV, diffkontroll och Gitleaks passerar. svlang markerar bara tre
falska V2-varningar i annars korrekta huvudsatser och i XML-kodad HTML.
`msgfmt` är inte tillämpligt på XLIFF. Ingen ändring har ännu skickats
upstream i detta steg.

## Bildrutetakt och emulering: sjunde granskningsbatchen

Fyra längre hjälprutor i emuleringsinställningarna hade ordagranna eller
otydliga formuleringar. `pcsx2-sv-emulation-frame-pacing-batch-07-20261111.xliff`
gör texterna mer direkta och konsekventa: värdens uppdateringsfrekvens,
bildrutetakt, inmatningsfördröjning, bildrutegenerering och realtidsklocka.
Projektets termbas ligger till grund för `Bildrutetakt/latenskontroll`,
`Realtidsklocka` och `Ange realtidsklocka manuellt`.

Källtexternas betydelse, HTML-entiteter och tekniska namn bevaras. Svenskt
procentformat används i den berörda hjälprutan. XML-validering, exakt
källjämförelse, l10n-lint, Hunspell-SV, diffkontroll och Gitleaks passerar.
svlang markerar endast de sammansatta PCSX2-termerna som sällsynta och tre
falska V2-varningar. `msgfmt` är inte tillämpligt på XLIFF.

Batchen skickades via Crowdin API till fil 15 (`pcsx2-qt_en.ts`) för `sv-SE`.
Den skapade fyra översättningar 2026-11-11 11:38 UTC: Crowdin-ID 448993,
448995, 448997 och 448999. Automatisk granskning var uttryckligen avstängd;
batchen är därför inskickad men inte godkänd upstream. En omedelbar
kontrollimport gav 0 importerade, 0 godkända och 4 hoppade över som dubbletter.

## Helskärmsläge: åttonde granskningsbatchen

`pcsx2-sv-fullscreen-speed-percent-batch-08-20261111.xliff` normaliserar
svenskt procentformat i 23 hastighetsetiketter i helskärmsgränssnittet. Den
enda förändringen är mellanrummet före procenttecknet, exempelvis `100 %`
i stället för `100%`. Bildfrekvenserna, standardmarkeringen, NTSC, PAL och
den faktiska procentnivån lämnas orörda.

XML-validering, exakt källjämförelse, l10n-lint, svlang, Hunspell-SV,
diffkontroll och Gitleaks passerar. svlang listar enbart NTSC och PAL som
sällsynta ord. `msgfmt` är inte tillämpligt på XLIFF. Batchen är lokalt
granskad.

Batchen skickades via Crowdin API till fil 15 för `sv-SE`. Importen skapade
23 översättningar med 127 ord; 0 godkändes automatiskt och 0 hoppades över.

## Dynamiska procentvärden: nionde granskningsbatchen

Sex dynamiska procentvärden i ljud-, handkontroll-, inmatnings- och
emuleringsinställningar saknade svenskt mellanrum före procenttecknet.
`pcsx2-sv-dynamic-percent-batch-09-20261111.xliff` rättar enbart detta och
bevarar alla Qt-platsmarkörer, bildfrekvenser samt NTSC och PAL.

XML-validering, exakt källjämförelse, l10n-lint, svlang, Hunspell-SV,
diffkontroll och Gitleaks passerar. svlang listar bara NTSC och PAL som
sällsynta ord. `msgfmt` är inte tillämpligt på XLIFF. Batchen är lokalt
granskad.

Batchen skickades via Crowdin API till fil 15 för `sv-SE`. Importen skapade
4 översättningar med 20 ord; 0 godkändes automatiskt. Två poster hoppades
över av dubblettkontrollen.

## Palett-texturer: tionde granskningsbatchen

Tre grafiska inställningsetiketter och två tillhörande hjälprutor beskrev
`Palette Texture Draws` med olika och delvis obegripliga formuleringar.
`pcsx2-sv-palette-textures-batch-10-20261111.xliff` normaliserar dem till
`ritningar med palett-texturer` och använder projektets term
`ursprunglig upplösning`. Bindestrecket undviker en otillåten följd av tre t.

XML-validering, exakt källjämförelse, l10n-lint, svlang, Hunspell-SV,
diffkontroll och Gitleaks passerar utan språkvarningar. `msgfmt` är inte
tillämpligt på XLIFF. Batchen är lokalt granskad.

Batchen skickades via Crowdin API till fil 15 för `sv-SE`. Importen skapade
5 översättningar med 30 ord; 0 godkändes automatiskt och 0 hoppades över.

## Grafik- och inmatningsprocent: elfte granskningsbatchen

`pcsx2-sv-graphics-input-percent-batch-11-20261111.xliff` rättar svenskt
procentformat i en grafiketikett, två inmatningsvärden och den kodade
hjälprutan för vertikal utsträckning. HTML-entiteterna bevaras oförändrade.

XML-validering, exakt källjämförelse, l10n-lint, svlang, Hunspell-SV,
diffkontroll och Gitleaks passerar. svlangs enda träff kommer från de
bevarade HTML-entiteterna. `msgfmt` är inte tillämpligt på XLIFF. Batchen är
lokalt granskad.

Batchen skickades via Crowdin API till fil 15 för `sv-SE`. Importen skapade
3 översättningar med 17 ord; 0 godkändes automatiskt och 0 hoppades över.

## USB-färgetiketter: tolfte granskningsbatchen

Fyra Buzz-kontrollsetiketter använde `Orange` med engelsk versal. Svenska
färgnamn skrivs med liten bokstav i den här UI-kontexten, så
`pcsx2-sv-usb-orange-labels-batch-12-20261111.xliff` använder konsekvent
`Spelare 1 orange` till `Spelare 4 orange`.

XML-validering, exakt källjämförelse, l10n-lint, svlang, Hunspell-SV,
diffkontroll och Gitleaks passerar utan språkvarningar. `msgfmt` är inte
tillämpligt på XLIFF. Batchen är lokalt granskad.

Batchen skickades via Crowdin API till fil 15 för `sv-SE`. Importen skapade
4 översättningar med 12 ord; 0 godkändes automatiskt och 0 hoppades över.

## JogCon-riktningsknappar: trettonde granskningsbatchen

JogCon var den enda kontrolltypen som lämnade `D-Pad` på engelska, medan
övriga PS2- och USB-kontroller konsekvent använder `Riktningsknappar`.
`pcsx2-sv-jogcon-directional-buttons-batch-13-20261111.xliff` normaliserar
den enda avvikelsen.

## Renderingsterminologi: fjortonde granskningsbatchen

`pcsx2-sv-rendering-terminology-batch-14-20261111.xliff` harmoniserar fyra
grafikinställningar med projektets etablerade renderingsterminologi. De två
mipmapping-raderna använder nu `korrekt rendering` i stället för `återges
korrekt`. De två beskrivningarna av TV-shadern använder den projektspecifika
termen `TV-shader` och samma idiomatiska formulering i helskärms- och
grafikdialogen.

Batchen är lokalt granskad och ännu inte inskickad. XML-validering, exakt
källjämförelse, l10n-lint, svlang, Hunspell-SV, Gitleaks och diffkontroll
passerar. Svlang och Hunspell-SV markerar enbart de avsiktliga fackorden
`mipmapping` och `TV-shader`; det senare finns i PCSX2:s termbas.
`msgfmt` är inte tillämpligt på XLIFF och avvisar därför filen som icke-PO.

Crowdin-importen är verifierad via API: 4 strängar och 66 ord importerades,
0 godkändes automatiskt och inga strängar hoppades över. De fyra nya
översättningsposterna har ID 449079, 449081, 449083 och 449085. De är
upstream-inskickade för granskning men ännu inte upstream-godkända.

XML-validering, exakt källjämförelse, l10n-lint, svlang, Hunspell-SV,
diffkontroll och Gitleaks passerar. l10n-lint rapporterar endast den väntade
längdskillnaden mot den engelska förkortningen. `msgfmt` är inte tillämpligt
på XLIFF. Batchen är lokalt granskad.

Batchen skickades via Crowdin API till fil 15 för `sv-SE`. Importen skapade
0 översättningar och 0 ord; 0 godkändes automatiskt. Posten hoppades över av
dubblettkontrollen, vilket visar att den korrekta svenska texten redan finns
i Crowdins flöde.

## Installationsguiden: tredje granskningsbatchen

Installationsguidens HTML-hjälpruta för spelkataloger hade en inledande
avslutande HTML-tagg och blandade svenska med engelska formatbeskrivningar.
`pcsx2-sv-setup-wizard-batch-03-20261111.xliff` rättar den enda berörda
strängen. Den använder `skivavbild` i stället för engelska `dump`, behåller
formatnamnen Media Descriptor File och Compressed Hunks of Data, och bevarar
den ursprungliga länken, HTML-strukturen och samtliga filändelser.

XML-validering, diffkontroll och Gitleaks passerar. l10n-lint har inga fel;
dess enda URL-varning beror på att den analyserar den XML-kodade HTML-källan
som en sammanhängande URL, medan länken finns både i källa och mål. svlang
tolkar HTML, filformat och URL-delar som ord och ger därför en låg, ej
språkligt relevant poäng. Hunspell-SV markerar bara produktnamnet PCSX2 och
den tekniska sammansättningen `Gzip-komprimerad`.

Batchen skickades via Crowdin API till fil 15 för `sv-SE`. Importen skapade
1 översättning med 116 ord; 0 godkändes automatiskt och inga strängar
hoppades över. Den nya översättningsposten har ID 449271. Den är
upstream-inskickad för granskning men ännu inte upstream-godkänd.
