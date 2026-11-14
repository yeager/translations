# Scribus svenska UI - granskningsbatch 011

Datum: 2026-11-14
Komponent: Scribus UI (`o:scribus:p:scribus:r:scribus`)
Språk: svenska (`sv`)

12 radgranskade strängar för styckeriktning, Word- och EPS-import,
bildeffekter och bitmappexport. Konkreta fel som bokstavliga
`(new line)`-markörer och den krystade utmatningskatalogen ersattes
med fungerande, naturlig UI-text.

Alla ändringar sparades med Transifex REST API och återlästes exakt.
`lrelease`, Hunspell-SV och svlang kördes lokalt. Gitleaks körs mot
arkivbatchen före push.
