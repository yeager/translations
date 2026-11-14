# Scribus svenska UI - granskningsbatch 016

Datum: 2026-11-14
Komponent: Scribus UI (`o:scribus:p:scribus:r:scribus`)
Språk: svenska (`sv`)

34 radgranskade strängar för exempeltext, märken, dokumentimport,
nätförvrängning och flerduplicering.

Rättar bland annat kvarlämnad engelska, felaktiga uttryck som
`Marknadschef`, mark- och notterminologi, filfilter, funktionstexter och
svenska UI-termer.

Alla ändringar sparades via Transifex REST API och återlästes exakt.
`lrelease`, Hunspell-SV och svlang kördes lokalt. Svlangs längd- och
V2-varningar beror på sammanslagna etiketter, inte på ett fel i
översättningen. Gitleaks kördes mot både API-deltat och arkivbatchen före
push.
