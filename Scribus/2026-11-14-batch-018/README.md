# Scribus svenska UI - granskningsbatch 018

Datum: 2026-11-14
Komponent: Scribus UI (`o:scribus:p:scribus:r:scribus`)
Språk: svenska (`sv`)

27 radgranskade strängar för 3D-visning, konturer och utskriftsförhandsgranskning.

Korrigerar tryckterminologi, bland annat dekorfärg, processfärg, CMYK,
färgtäckning och underfärgsreducering, samt rena engelska UI-rester.

Alla ändringar sparades via Transifex REST API och återlästes exakt.
`lrelease`, Hunspell-SV och svlang kördes lokalt. Svlangs varningar gäller
korrekta facktermer och sammanslagna etiketter. Gitleaks kördes mot både
API-deltat och arkivbatchen före push.
