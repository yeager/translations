# Eden Emulator – svensk Transifex-status 2026-10-30

Eden Emulators Qt-resurs `qt-translations` ändrades 30 oktober 2026. De sex
nya svenska UI-strängarna för fuskkoder hämtades via Transifex REST-API och
granskades rad för rad mot källtext och förekomst:

- standardaktivering av fuskkoder och dess hjälptext,
- menyalternativet `&Cheats`, med bevarad Qt-åtkomsttangent,
- aktivering och inaktivering av alla fuskkoder,
- namnet för en namnlös fuskkod.

Batchen finns i `eden-qt-sv-20261030-cheats-batch.json`. l10n-lint och
svlangs skrivregler passerar. Hunspell markerar bara den avsiktligt bevarade
produkttermen `Master Code`.

Samtliga sex poster skickades som vanliga, ogranskade översättningar genom
Transifex REST-API med HTTP 200 och återlästes därefter exakt. Resursstatistik
visar 1 943 av 1 943 svenska strängar översatta och 0 oöversatta.

Färskhetskontroll: den lokala aktuella källan har taggen `build-51` från
30 oktober 2026.

## Android-resurs – uppföljning 31 oktober 2026

Den aktuella Android-resursen `android-translations` hade sju svenska
oöversatta strängar: en uppdaterad hjälptipsrad för bloom samt sex strängar
för fuskkoder. De granskades och skickades via Transifex REST-API. Underlaget
finns i
[`eden-android-sv-batch-001-20261031.json`](../eden/eden-android-sv-batch-001-20261031.json).

`l10n-lint` och svlangs skrivregelskontroll gav inga fynd. Hunspell-SV
markerade endast den avsedda grafiktermen `bloom` och spelnamnet `Burnout`.
Alla sju API-svar var HTTP 200 och varje måltext lästes tillbaka exakt.
Resursstatistiken visar därefter 1 082 av 1 082 svenska Android-strängar
översatta och 0 oöversatta.

## Qt-resurs – Eglantine-uppföljning 31 oktober 2026

Eglantine synkar sin svenska Qt-katalog från Edens `qt-translations`-resurs.
En korrekturgranskning identifierade en oavsiktlig dubbelpunkt i
Nintendo-friskrivningen för `AboutDialog`. Rättningen passerade HTML-,
platshållar-, l10n-lint-, svlang-, Hunspell- och Gitleaks-kontroller innan
den skickades med Transifex REST-API. API:t svarade HTTP 200 och måltexten
återlästes exakt. Underlag och sändningsbevis finns i
`eden-qt-sv-eglantine-punctuation-20261031.json` respektive
`eden-qt-sv-eglantine-punctuation-submission-20261031.md`.

## Qt-resurs – styrenhetsgranskning 7 november 2026

En källuppdatering lade till 190 oöversatta svenska Qt-strängar. De
granskades i fem batcher med fokus på styrenheter, Steam Input,
inmatningsprofiler och spelartilldelning:

- `eden-qt-sv-20261107-controller-batch-01.json`
- `eden-qt-sv-20261107-input-profiles-batch-02.json`
- `eden-qt-sv-20261107-player-assignment-batch-03.json`
- `eden-qt-sv-20261107-player-feedback-batch-04.json`
- `eden-qt-sv-20261107-final-controller-ui-batch-05.json`

Platshållare och radbrytningar kontrollerades före varje API-inskick;
`l10n-lint` gav inga fel. Transifex REST-API bekräftade ändringarna och varje
skickad måltext återlästes exakt. Slutlig resursstatistik från API:t visar
2 122 av 2 122 svenska Qt-strängar översatta och 0 oöversatta. Detta anger
översättningsstatus, inte en eventuell separat granskningsstatus i Transifex.

## Livekontroll av Qt-resursen 11 november 2026

Den inloggade Transifex-redigeraren kontrollerades direkt för
`edenemu/eden-emulator`, resursen `qt-translations`, svenska. Båda
filtren visade **0 Inte översatta** respektive **0 Inte granskade**. Detta
verifierar den aktuella UI-statusen för Qt-resursen; ingen ny översättning
eller extern ändring skickades vid kontrollen.

## Android-resurs – fuskmenyn 13 november 2026

Aktuell Android-källkod vid `63e957b` lade till två nya tillståndsbeskrivningar
för en öppningsbar fuskmeny: `Expanded` och `Collapsed`. Källan visar att
texterna används med Androids `ViewCompat.setStateDescription`, alltså som
tillgänglighetsbeskrivning av menyns faktiska tillstånd. De översattes därför
till **Utfälld** respektive **Hopfälld**, efter kontroll mot den svenska
gränssnittsterminologin för utfällbara paneler.

Batchen i `eden-android-sv-cheat-submenu-20261113.json` har validerats med
JSON-syntax, käll- och kontextjämförelse, Hunspell-SV, diffkontroll och
Gitleaks. `l10n-lint` felmarkerar API-payloaden eftersom den kräver en
pluralform `one` trots att båda Androidsträngarna är singulara; det är inte
ett problem i måltexterna eller Transifex-resursen.

De båda posterna skickades som en Transifex API-batch och lästes tillbaka
exakt. API-statistiken efter inskicket visar **1 084 av 1 084** svenska
Androidsträngar översatta och **0 oöversatta**. Båda posterna är ännu inte
markerade som upstreamgranskade.
