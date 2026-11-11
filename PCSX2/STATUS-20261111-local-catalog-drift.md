# PCSX2: lokal katalog avviker från verifierad Crowdin-status

Datum: 11 november 2026

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
