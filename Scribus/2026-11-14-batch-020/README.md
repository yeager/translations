# Scribus svenska UI - granskningsbatch 020

Datum: 2026-11-14
Komponent: Scribus UI (`o:scribus:p:scribus:r:scribus`)
Språk: svenska (`sv`)

39 radgranskade strängar för mallsidor, sidinställningar, banverktyg,
formoperationer och mönsteregenskaper.

Normaliserar Scribus-termer som bana, kontur, punkt och banoperation samt
rättar kvarlämnad engelska, felaktiga böjningar och axelbeteckningar.

Alla 39 unika ändringar sparades via Transifex REST API och återlästes exakt.
`lrelease`, Hunspell-SV och svlang kördes lokalt. Svlangs varningar gäller
HTML-taggar och sammanslagna etiketter. Gitleaks kördes mot både API-deltat
och arkivbatchen före push.
