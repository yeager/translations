# Wireshark, svensk granskning

Senast granskad 15 oktober 2026. Filerna kommer från Transifex-resurserna `po-master` och `qt-master`.

Validering: `msgfmt` för PO, `lrelease` för TS, `l10n-lint`, `svlang`, Hunspell, svensk terminologi, översättningsminne och Gitleaks. Transifex bekräftade 16 uppdateringar i PO-resursen och 90 skapade samt 4 uppdaterade översättningar i Qt-resursen.

Den 15 oktober 2026 korrigerades återstående l10n-lint-varningar i Qt-katalogen. Transifex bekräftade ytterligare 60 uppdateringar.

Den 12 november 2026 översattes de 423 strängar som då saknades i
`qt-master` i 21 kontrollerade API-batcher. Färsk kontroll via Transifex API
visade därefter 0 oöversatta strängar. Batchernas deltafiler, API-kvitton och
efterexporter finns under `Transifex/2026-11-12/`. Uppladdningen är verifierad;
upstreamgranskning eller publicering är inte verifierad.
