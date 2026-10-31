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
