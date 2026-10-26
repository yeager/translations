# Svenskt manusregister för FreeSWITCH med Anton

Det här är en text- och granskningskopia för FreeSWITCHs svenska ljudresurser. Den innehåller inga ljudfiler eller API-uppgifter och är inte ett färdigt eller distribuerbart ljudpaket.

## Manusstatus per 2026-10-26

Katalogen omfattar 290 historiska inventeringsreferenser och sex kompletterande resurser i den aktiva FreeSWITCH-checkouten: totalt 296 manus. I grundinventeringen är 233 manus granskade och 57 återstår som utkast. En batch granskade 20 manus mot hashverifierade originalinspelningar i Jakob 1.0.50; varje manus matchade den svenska ASR-transkriptionen exakt efter normalisering och klarade svensk textgranskning. De sex kompletterande resurserna är också granskade, vilket ger 239 granskade manus och 57 utkast totalt. Detta godkänner inte ljud.

De sex tilläggen finns i `sv-SE-current-checkout-voicemail-supplement-20261026.tsv`; deras separata granskning är inbäddad i `review_notes` och `review_evidence`. `sv-SE-voice-script-draft-20261025.tsv` innehåller den kompletta 296-raderskatalogen med exakta manus, TTS-promptar, hashbindning, granskningsstatus och källbevis.

## Textkontroller

De sparade target-only-resultaten för katalogen visar 0 l10n-lint-fel/varningar, 0 svlang-skrivregelträffar och 0 anglicismer. Den nya 20-manusbatchen kontrollerades separat: 0 l10n-lint-fel/varningar, 0 svlang-skrivregelträffar/anglicismer och 0 okända ord i Hunspell. Svensk Hunspell flaggar korta bokstavs- och kodnamn för mänsklig bedömning. Kontrollerna ersätter inte källbaserad manusgranskning eller ljudlyssning.

## Genereringsram

Användaren har godkänt ramen på 4 112 tecken för hela Anton-katalogen. Sju prov har hittills använt 32 tecken; 4 080 återstår. De sju aktuella proven är `tio.`, `e.`, `de.`, `söndag.`, `eff.`, den IPA-styrda bokstaven G och `noll.`. Två har avvisats efter mänsklig granskning; fem väntar på lyssning. Ingen massgenerering har körts eftersom `ELEVENLABS_API_KEY` och verifierat Anton-röst-ID saknas i den aktuella processen. Uppdaterad hash- och ASR-status finns i `sv-SE-current-audio-candidates-20261026.tsv`.

## Ljud och felmappning

**Ljudgodkännanden: 0 av 296.** Användaren rapporterade att Anton-ljuden säger fel ord. Alla historiska ljud och tidigare kandidater är avvisade och får inte återanvändas eller distribueras. En verifierad mappningskollision finns mellan `digits/10.wav`, `digits/11.wav` och `digits/12.wav`, som hade identiska ljuddata trots olika målord. En tidigare kandidatgrupp innehöll dessutom 31 promptmanus som avvek från den kanoniska texten; aktuell TTS-promptmappning finns i `sv-SE-current-audio-candidates-20261026.tsv` och den uppdaterade arbetsrapporten. Enskilda ASR-träffar och korrekta WAV-format räcker inte som godkännande.

Nya ljud kräver en separat inspelning per granskat manus, verifierbar bindning mellan prompt och ljudhash, ord-för-ord-lyssning och kontroll av sammanfogade FreeSWITCH-flöden. API-generering är inte tillgänglig i aktuell process eftersom `ELEVENLABS_API_KEY` och verifierat Anton-röst-ID saknas.

## Öppet arbete

- Granska återstående 57 basmanus mot aktiv FreeSWITCH-kod, PR #3242/#3243 och svensk terminologi.
- Återställ en verifierbar ElevenLabs-exportväg och skapa nya separata tagningar när åtkomst och röst-ID finns.
- Kontrollera samtliga tagningar och kompletta sekvenser genom lyssning; skapa därefter 8, 16, 32 och 48 kHz-varianter.
- Kör release-preflight, Gitleaks på ändrade text- och kodfiler samt paket- och runtimekontroller efter ljudgranskningen.
- Skriftlig klarering för öppen omdistribution av ElevenLabs-genererade ljud är inte fastställd.

De 20 nygranskade manusen och ASR-/hashunderlaget finns i `historical-jakob-asr-script-review-batch-2026-10-26.json`; Jakob-ljuden används enbart som manusreferens och ingår inte som Anton/Lisa-ljud.

Ett separat konfigurationsfel i `voicemail_greeting_selected` gör att den svenska sekvensen talar om meddelandenummer där engelska källan väljer en hälsning. En lokal korrigeringsdiff finns, men den kräver nya resursreferenser och ingår inte i den här 296-posters ljudkatalogen.

Källcheckout: `02857682b56626f06f72b91730415084b892bfee`. PR #3242 och #3243 är underlag för kontext; denna draft gör inte anspråk på maintainer-godkännande, ljudklarering eller releasegodkännande.
## Föreslagna manus för vald hälsning

PR #3242:s svenska `voicemail_greeting_selected` återanvänder `vm-meddelande_nummer` och `vm-markerad`, vilket ger fel betydelse och kongruens. Förslaget lägger till separata manus `Hälsning nummer` och `är vald` och ändrar makrot att använda dem. De två posterna finns separat i `sv-SE-proposed-greeting-selected-resources-20261026.tsv`; källpatchen finns i `proposed-pr3242-greeting-selected-correction.patch`. De är inte del av den aktiva 296-posterskön, och ljuden är inte genererade, lyssnade eller godkända.


## Kodningskontroll för svenska bokstäver

Ett separat bytevis modelltest visar att CP437-byten för ä, å och ö leder till resurs-ID 132, 134 och 148, medan UTF-8-byten leder till två andra ID:n per bokstav. Källkoden skickar bytevärdena direkt till `ascii/%d`; den lokala checkouten saknar bygg- och runtimefiler, så anroparnas faktiska kodning är inte fastställd. `ascii/132.wav`, `ascii/134.wav` och `ascii/148.wav` förblir utkast. Underlaget `sv-SE-spell-byte-mapping-runtime-model-20261026.json` är en modell, inte ett runtimeprov.

## Aktuell granskningssida

Den lokala Anton-granskningssidan innehåller 296 aktiva resurser och två föreslagna voicemailresurser som kräver källpatchen. Sju aktiva kandidater har ljud; två har avvisats i sparad användargranskning och fem väntar på lyssning. 290 aktiva resurser saknar nya tagningar. De två förslagen saknar ljud och går inte att godkänna. Se `sv-SE-anton-audio-review-status-20261026.md` och `sv-SE-current-audio-candidates-20261026.tsv`.
