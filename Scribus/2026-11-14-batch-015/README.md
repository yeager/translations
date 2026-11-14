# Scribus svenska UI - granskningsbatch 015

Datum: 2026-11-14
Komponent: Scribus UI (`o:scribus:p:scribus:r:scribus`)
Språk: svenska (`sv`)

31 radgranskade strängar för dialoger med ramar, tabeller och skript,
samt lager- och linsverktyg.

Ändringarna normaliserar bland annat `läs in` för infogat innehåll,
texthanteraren, lagertransparens, trådramsvisning och fiskögonlins.

Alla ändringar sparades via Transifex REST API och återlästes exakt.
`lrelease`, Hunspell-SV och svlang kördes lokalt. Svlangs längd- och
V2-varningar beror på sammanslagen HTML-hjälptext och separata UI-etiketter,
inte på ett fel i översättningen. Gitleaks kördes mot både API-deltat och
arkivbatchen före push.
