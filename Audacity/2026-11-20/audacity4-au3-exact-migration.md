# Audacity 4 – kontrollerad återanvändning från Audacity 3

Datum: 2026-11-20  
Målresurs: Transifex `o:audacity:p:audacity:r:audacity4`, språk `l:sv`  
Källfil: `audacity-sv-reviewed.po` (Audacity 3, GNU gettext)  
Målfil: `for_translation_audacity_audacity4_sv.ts` (Audacity 4, Qt TS/XML)

## Varför PO-filen inte gick att ladda upp

Audacity 4-resursen är en Qt-katalog (`QT`) och förväntar sig XML i
TS-format. Audacity 3-filen är en GNU gettext-PO. Transifex-felet
`not well-formed (invalid token): line 1, column 1` uppstod alltså när PO
användes mot en XML-resurs, inte på grund av en trasig svensk översättning.

## Underlag och kontroll

- PO-katalogen är syntaktiskt korrekt: `msgfmt --check` rapporterar 4&nbsp;443
  översatta meddelanden.
- Den nedladdade TS-katalogen är välformad XML (`TS` 2.1, `language="sv"`)
  med 4&nbsp;147 meddelanden.
- 1&nbsp;257 av TS-katalogens 3&nbsp;467 unika källtexter är exakta träffar i
  AU3-katalogen. Efter försiktig normalisering är överlappningen 1&nbsp;375.
- Av dessa målmeddelanden hade 1&nbsp;130 redan samma svenska värde.
- 479 målmeddelanden (442 unika källtexter) uppdaterades till den redan
  granskade AU3-översättningen. Samtliga övriga AU4-meddelanden bevarades.
- Kontroll av Qt-platshållare (`%1`, `%L1`, `%n`) och hakparentesplatshållare
  gav 0 avvikelser bland de 479 ändringarna.
- De 261 oöversatta AU4-posterna har ingen exakt motsvarighet i AU3-filen.
  De ska granskas i AU4-kontext i stället för att fyllas automatiskt.

## Uppladdning och verifiering

Den validerade TS-arbetskopian i samma katalog laddades upp med Transifex
asynkrona översättnings-API, `file_type: default` för Qt-resursen.

- Uppladdnings-ID: `da0e8682-46e4-491a-857e-81d8b7efeb61`
- Slutstatus: `succeeded`
- Transifex-resultat: `translations_updated: 479`,
  `translations_created: 0`

Arbetskopians SHA-256:

`04cf2d225cf15754b37853a908e6448aac9e7d6a5c08f6a18ef3128deac6d0cd`

Den gamla PO-filen laddades aldrig upp till AU4-resursen.

## AU4-källsträngar utan AU3-motsvarighet – batch 001

Efter migreringen återstod 261 oöversatta AU4-meddelanden. Batch 001
granskades mot respektive QML/C++-referens och omfattar 15 unika källtexter,
17 meddelanden: återställningsdialogen, menyåtgärder, exportmeddelandet och
OGG-kvalitetsetiketten. Den validerade arbetsfilen är
`audacity4-sv-review-batch-001-20261120.ts`
(`c9ce8038e92f1ae9145d828aae4e84ee8a7180c3c43051ae08c9f2672ae935f6`).

- XML- och platshållarkontroll: godkänd; 244 oöversatta meddelanden återstår
  i arbetsfilen.
- `svlang`: enbart kontextfria UI-etiketter samt produktnamn/MP3 gav
  granskningssignaler; inga språkfel identifierades vid manuell kontroll.
- Hunspell: inga träffar i de svenska huvudorden.
- Termbanken stödjer bland annat `Editing` → `Redigering`, `Macro Manager`
  → `Makrohanterare`, `Repeat` → `Upprepa` och `Quality` → `Kvalitet`.
- Transifex-uppladdning `184fca6e-8d6d-44e9-abe8-a5ba2300614e` avslutades
  med `succeeded`: `translations_created: 17`,
  `translations_updated: 0`.

## AU4-källsträngar utan AU3-motsvarighet – batch 002

Batch 002 granskar 14 unika källtexter (17 meddelanden) i meny- och
kommandomodulerna: molnturer, mediaimport, kanalmappning, tidslinjen,
uppspelning och ljudaktiverad inspelning. Två av strängarna är direkt
verifierade mot den lokala, tidigare kontrollerade AU4-katalogen:
`Select from a chosen time to the playback position` och
`Select from the playback position to a chosen time`.

- XML-kontroll godkänd. 227 oöversatta meddelanden återstår.
- `svlang` gav endast produktdomänerna `audio.com` och Audacity som sällsynta
  ord; de är avsedda egennamn.
- Transifex-uppladdning `e446d428-a68f-4d9c-b753-55042c57384d` avslutades
  med `succeeded`: `translations_created: 17`,
  `translations_updated: 0`.
- En sedan tidigare befintlig WavPack-rad med platshållaravvikelse upptäcktes
  i katalogens breda kontroll. Den har inte ändrats och hålls separat från
  denna batch för kontextgranskning.

## Slutlig komplettering och radgranskning

Den 20 november 2026 granskades även de återstående 227 AU4-meddelandena
rad för rad utifrån TS-katalogens kontext och källreferenser. Tillsammans med batch 001 och 002 omfattar
slutgranskningen 244 meddelanden som tidigare var oöversatta. Katalogen har
nu 4 147 meddelanden, med 0 tomma översättningar och 0
`type="unfinished"`-markeringar.

- XML validerades med `xmllint --noout`.
- Qt-pluralformer kontrollerades separat. De 10 pluralposterna har kompletta
  svenska former; fyra tidsuttryck använder avsiktligt *i går/förra veckan*
  i ental utan `%n`.
- Platshållare (`%1`, `%L1`, `%n`) stämmer mot källan i samtliga granskade
  meddelanden.
- Ett tydligt språkfel rättades i `macromanager`: `The macro could not be
  renamed` är nu `Det gick inte att byta namn på makrot`, i stället för den
  felaktigt reflexiva formuleringen att makrot självt kunde byta namn.

Slutlig arbetsfil och arkivkopia är byte-identiska efter rättelsen:

`21478acdbec87eebb0546a350080d9c9bcc802c795ca1909ef00e296ef8202cb`

Den korrigerade slutversionen är lokal och arkiverad. Den behöver laddas upp
till Transifex AU4-resursen när den säkra API-sessionen är tillgänglig i den
aktuella miljön.
