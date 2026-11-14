# Scribus svenska UI - granskningsbatch 021

Datum: 2026-11-14
Komponent: Scribus UI (`o:scribus:p:scribus:r:scribus`)
Språk: svenska (`sv`)

16 radgranskade strängar för PDF-import, säkerhetsdialog, bildsökning,
bildstatus och bildsamlingar.

Korrigerar sidintervall, UI-termer, bild- och sidobjektterminologi samt
felaktigt översatta CSS-egenskaper i inbäddad HTML.

Alla ändringar sparades via Transifex REST API och återlästes exakt.
`lrelease`, Hunspell-SV och svlang kördes lokalt. Språkverktygens varningar
för denna batch kommer från inbäddad HTML/CSS, som återställdes till korrekt
originalsyntax. Gitleaks kördes mot både API-deltat och arkivbatchen före
push.
