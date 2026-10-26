# Status för FreeSWITCHs svenska ljudpaket

## Uppdatering efter den exporterade granskningen

Den senaste exporterade Anton-granskningen godkänner 296 dåvarande kandidater med respektive ljudhash. Därefter rapporterades att Q (`ascii/113.wav`) lät som engelska ”queue”. Nya Q-kandidater för Anton och Lisa finns på den lokala granskningssidan och behöver separata lyssningsbeslut. Den tidigare Anton-byggnaden är därför inaktuell. Lisa saknar fortfarande exporterade lyssningsbeslut. Äldre siffror och uttalanden om att runtimeprov saknas längre ned är historiska ögonblicksbilder.

Ett isolerat FreeSWITCH-runtimeprov har nu visat fel filval för UTF-8-stavning av å, ä och ö samt kontrollerat en lokal korrigering. Det provade filval, inte ljuduppspelning eller allmän Unicode-hantering. Se [runtimekontrollen](sv-SE-utf8-spelling-runtime-20261026.md) och [patchförslaget](proposed-swedish-utf8-spelling.patch). Ingen av rösterna är färdig för distribution.

## Läget nu

Varken Lisa- eller Anton-paketet är klart att installera eller distribuera. De befintliga tar-arkiven är uttryckligen märkta som underkända. Användaren har godkänt enskilda Anton-kandidater för lyssning. Paketet som helhet är ännu inte godkänt: filnamn, manus, uttal och sammanfogade fraser måste verifieras tillsammans.

Den samlade lokala granskningssidan är [FreeSWITCH-ljudgranskning](http://127.0.0.1:8766/freeswitch-audio-review.html). Den har flikar för Anton och Lisa och visar 588 rader: 298 Anton (296 aktiva och två föreslagna) samt 290 Lisa. Varje befintligt ljudprov har en egen spelare och knappar. Hela klippet måste spelas före beslut; även ljud med manusutkast kan godkännas separat från manusgranskningen. Beslut sparas lokalt i webbläsaren och kan exporteras som JSON. Kandidaternas filbindningar och format kontrolleras när sidan byggs. Lyssningsbeslut sparas i webbläsaren och måste exporteras för att kunna användas utanför den.

## Kataloger och ljud

| Röst | Referenser | Manus granskade | Manusutkast | Nya ljudprov | Beslut |
|---|---:|---:|---:|---:|---|
| Anton | 296 aktiva, 2 föreslagna | 239 | 57 | 296 | Se lokala lyssningsbeslut |
| Lisa | 290 | 233 | 57 | 290 | Se lokala lyssningsbeslut |

Båda rösternas aktiva referenser har kandidater. De två föreslagna Anton-resurserna saknar ljud och nödvändig källändring. Tre äldre Lisa-prov är endast diagnosmaterial. Kandidaterna är inte färdiga paket: varje inspelning behöver granskas mot rätt referens och manus. Två tidigare Anton-prov har avvisats. Lisa-proven för G, Xerxes och maj är särskilda uttalstester som behöver lyssnas på.

Kandidaterna på granskningssidan har kontrollerats för identiska ljudhashar: ingen dubblett bland 296 Anton-kandidater eller 290 Lisa-kandidater. Olika hash bekräftar inte rätt ord eller uttal.

## Granskning och omtag

Den senaste exporterade Anton-granskningen innehåller 263 godkända och åtta avvisade kandidater, bundna till respektive ljudhash. Sex nya, ogranskade tagningar ersätter de avvisade kandidaterna för A, D, E, L, Urban och Xerxes; separata nya V- och X-prov finns också. Tidigare beslut överförs inte automatiskt till nya ljud. Användaren vill ha tydligare betoning och hårda bokstavsljud, bland annat för D, E, L, V och X. L-provet behöver särskilt kontrolleras så att det inte låter som amerikanskt ”äll”.

Användaren tycker att ett separat prov med ”snabel-a” låter bra. Den undersökta `mod_say_sv.c` använder `ascii/64` för tecknet @ i stavningsläget, medan `time/at.wav` inte anropas direkt i den undersökta källversionen. Provets uttal är uppskattat, men filens användning och paketkoppling kräver fortfarande verifiering. Lisa saknar en exporterad lyssningsgranskning i arbetsunderlaget.

## Senare granskningsbeslut och uttalsprov

Den senaste sparade Anton-filen innehåller användarens godkännande av A och snabel-a för `time/at.wav`. Beslut är kopplade till ljudhash och nya tagningar är ogranskade tills de har lyssnats på. Användaren har rapporterat fel uttal för E, O och Urban; det finns nya prov. Urban har på användarens förslag genererats med uttalsstödet ”urrbann” för både Anton och Lisa. Lisa-proven för E, O, David, Urban och snabel-a använder motsvarande Anton-prompter men kräver separat lyssning. Samma prompt innebär inte att de två rösterna uttalar orden likadant.

Den här beskrivningen ersätter inte export av senare beslut från granskningssidan. Inget färdigt paket eller FreeSWITCH-runtimeprov är verifierat.

## Manusgranskning och verktyg

Katalogerna innehåller 57 manusutkast per röst. Jag installerade `svlang 0.2.22`, `l10n-lint 1.23.30` och `hunspell-sv 2026.10.25` i en separat Python 3.12-miljö under `work/freeswitch-voice-tools/.venv312`. De aktuella katalogerna kontrollerades mot respektive kataloghash:

- `svlang skrivregler`: 0 träffar bland 296 Anton- och 290 Lisa-manus.
- `svlang svengelska`: 0 anglicismer i båda katalogerna.
- `l10n-lint --language sv --terminology` med `outputs/FREESWITCH-SV-GLOSSARY.tsv`: samtliga 296 respektive 290 manus kontrollerade, 0 fel och 0 varningar.
- De faktiska TTS-inmatningarna kontrollerades också separat: 296 Anton-prompter och 287 Lisa-prompter gav 0 skrivregelfel, 0 anglicismer och 0 l10n-fel/varningar. Resultatet gällde före tillägget av tre särskilda Lisa-testprompter för `ascii/103.wav`, `phonetic-ascii/120.wav` och `time/mon-4.wav`; dessa kräver röstspecifik lyssning och en uppdaterad promptkontroll. Skillnader mellan manus och TTS-inmatning finns i `work/freeswitch-voice-tools/prompt-mapping-audit.tsv`.
- De tre tillkomna testprompterna kontrollerades separat med svlang och l10n-lint: inga skrivregelfel, anglicismer, l10n-fel eller varningar. Hunspell flaggade `Särkses.`, som är ett avsiktligt uttalsförsök för Xerxes, inte målmanusets stavning. De två IPA-strängarna är heller inte vanliga svenska ord. Ingen av dessa kontroller bevisar att rösten uttalar dem rätt.
- Svensk Hunspell hittade nio specialord per manus-katalog. De är de svenska bokstavsnamnen `eff`, `ji`, `kå`, `ell`, `em`, `pe`, `ku`, `dubbelve` samt uttalsalfabetsordet `Qvintus`. Dessa har referensbunden kontextundantagslista i `work/freeswitch-voice-tools/hunspell-context-allowlist.tsv`; med den listan blir det inga okända ord. Det är stavningskontroll av manus, inte uttalsgodkännande.

Kommandoutdata och kataloghashar finns i `work/freeswitch-voice-tools/validation-summary-2026-10-26.json`. Verktygsmiljön går att återskapa från `work/freeswitch-voice-tools/`.

ElevenLabs-nyckeln lästes från systemets nyckelhanterare utan att sparas i arbetsfilerna. Separata kandidatfiler har genererats för båda rösterna efter användarens klartecken. Lisas genereringsregister finns i `freeswitch-lisa-direct-rebuild/api-generation-ledger.json`; kandidatmanifesten binder referens, prompt och filhash. Genererade kandidater är inte lyssningsgodkända. Automatisk taligenkänning är klar för 288 nygenererade Lisa-kandidater och visar ofta osäkra resultat för korta klipp; den ersätter inte lyssning. De två äldre hashbundna kandidaterna har tidigare diagnostiska transkriptioner.

Gitleaks kördes på de ändrade UI- och generatorfilerna; inga hemligheter hittades. Den installerade venvens tredjepartsfiler skannades inte.

## Kvar före ett användbart paket

- Lyssna på varje kandidat och spara hashbundna beslut; ersätt avvisade inspelningar.
- De nya Anton-kandidaterna för `digits/10.wav`, `digits/11.wav` och `digits/12.wav` har olika SHA-256-värden och visar respektive prompt ”tio.”, ”elva.” och ”tolv.” på granskningssidan. Detta avhjälper den tidigare byte-identiska filkollisionen i kandidatunderlaget, men bevisar inte att rätt ord hörs; alla tre behöver lyssnas på.
- Granska särskilt `voicemail/vm-valkommen-introduktion.wav`: utkastet saknar en tydlig meningsgräns mellan de två valen. FreeSWITCHs [engelska manusregister](https://github.com/signalwire/freeswitch/blob/master/docs/phrase/phrase_en.xml) anger att 1 startar introduktion och inställning och 2 hoppar över. Föreslagen text: ”Välkommen till din nya röstbrevlåda. För att lyssna på en introduktion och ställa in din röstbrevlåda, tryck 1. För att hoppa över, tryck 2.” Kontrollera kopplingen till den svenska makron och generera nya kandidater efter manusändringen; befintliga kandidater bygger på det tidigare utkastet.
  Vid kontroll av `conf/vanilla/lang/sv/vm/sounds.xml` i PR #3243:s head `02857682b56626f06f72b91730415084b892bfee` hittades ingen referens till `vm-valkommen-introduktion` eller någon makro med `tutorial` i namnet. Filens användning i annan konfiguration eller kod är inte därmed utesluten.
- Granska omtag och återstående ljud samt granska manusutkasten separat före färdig paketering.
- Lös kodningsfrågan för `ä`, `å` och `ö` i FreeSWITCHs `say_spell`-väg genom ett faktiskt runtimeprov.
- Kontrollera uttal och sammanfogad uppspelning i FreeSWITCH, bygg om alla samplingsfrekvenser från godkända masterfiler och verifiera arkiven.
- En enkel amplitudscreening av de 288 nygenererade Lisa-förhandsfilerna vid 8 kHz flaggade `digits/n-1.wav` för cirka 0,73 sekunder under amplitudtröskeln 160 i slutet. Det är en indikation, inte en ljudgranskning eller ett skäl att klippa automatiskt; lyssna på övergången i sitt sammanhang.
- Samma typ av grov kantkontroll på de 289 Anton-WAV-filerna i `api-candidates`, med amplitudtröskel 800 och gränserna 0,5 sekunder i början respektive 0,7 sekunder i slutet, flaggade ingen fil. Kontrollen täcker enbart dessa API-kandidater och bevisar inte att ljudens ord eller rytm är korrekta.
- Bekräfta om isolerade ElevenLabs-ljud får återlicensieras i det öppna paketet. De aktuella [EES-villkoren](https://elevenlabs.io/terms-of-use-eu) tillåter användning av nedladdat resultat utanför tjänsten och säger att användaren behåller rättigheterna till resultatet, men kommersiell användning kräver betald plan och användningspolicyn gäller. Villkoren säger inte uttryckligen om just dessa WAV-filer får återlicensieras under paketets öppna licens. Voice Library-rösternas API-åtkomst och kontoplan är inte verifierade; se även [Voice Library-dokumentationen](https://elevenlabs.io/docs/eleven-creative/voices/voice-library/).
- Kör CI och FreeSWITCH-runtimeprov för PR #3242 och #3243 när en byggmiljö finns; GitHub rapporterade inga checks vid senaste kontrollen.
- Få manusregisterkopia i `yeager/translations` granskad och slå ihop PR #4 när den godkänts.

## Aktuell käll- och PR-kontroll

FreeSWITCH-checkouten är på `fix-swedish-compound-numbers` vid `0285768`; arbetskatalogen är ren. PR #3242 är öppen med `REVIEW_REQUIRED`, head `481bfca36b78b82defb97326e2ac2590d589fd3b`; PR #3243 är öppen med `REVIEW_REQUIRED`, head `02857682b56626f06f72b91730415084b892bfee`. GitHub rapporterar inga checks eller granskningar för någon av dem vid kontrollen den 26 oktober 2026.

PR #3242 skiljer nu mellan `new:` och `saved:` i `voicemail_say_message_number`. Däremot använder `voicemail_greeting_selected` fortfarande `vm-meddelande_nummer.wav` före hälsningsnumret; hälsningsspecifika ljud och den föreslagna makrokorrigeringen är inte färdiga att aktiveras. PR #3243 byter till `digits/u-1` före `miljon`/`miljoner`, vilket motsvarar utrum i dessa talgrupper. Källkodsdiffarna klarar `git diff --check`, men ingen FreeSWITCH-runtime- eller CI-körning finns som bekräftar ljudflödet.

En direkt sökning i `conf/vanilla/lang/sv/vm/sounds.xml` vid PR #3243:s dokumenterade head fann endast två av de 40 återstående voicemailutkasten som exakta `data`-referenser: `vm-markerad.wav` i `voicemail_greeting_selected` och `vm-meddelande_nummer.wav` i både den makron och `voicemail_say_message_number`. Båda omfattas av betydelsekrocken ovan. De övriga utkastens användning kan inte avgöras av denna enskilda XML-fil; annan kod eller konfiguration kan referera till dem.

Manuskopian för Lisa har nu lagts till i [yeager/translations PR #4](https://github.com/yeager/translations/pull/4), commit `ce4b17336f7451eee580615c337172889828bb0d`. Där finns 290 TSV-poster och statusnoter, utan ljudfiler eller API-uppgifter. Senaste statusuppdateringen är commit `d4ee6615d63d164e5c5842a999f00ffcbce9a426`; PR:en är fortfarande öppen.
