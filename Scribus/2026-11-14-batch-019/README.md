# Scribus svenska UI - granskningsbatch 019

Datum: 2026-11-14
Komponent: Scribus UI (`o:scribus:p:scribus:r:scribus`)
Språk: svenska (`sv`)

21 radgranskade strängar för PDF- och PostScript-export, objektstatus och
LaTeX-ramar.

Korrigerar bland annat CMYK- och färgtäckningsord, exportfel, svenska
statusord och återgivning i den konkreta ramdialogens UI-kontext.

Alla ändringar sparades via Transifex REST API och återlästes exakt.
`lrelease`, Hunspell-SV och svlang kördes lokalt. Svlangs varningar gäller
sammanslagna etiketter. Gitleaks kördes mot både API-deltat och
arkivbatchen före push.
