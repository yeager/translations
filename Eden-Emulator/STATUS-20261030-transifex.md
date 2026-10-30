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
