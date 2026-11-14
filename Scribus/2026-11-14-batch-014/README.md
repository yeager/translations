# Scribus svenska UI - granskningsbatch 014

Datum: 2026-11-14
Komponent: Scribus UI (`o:scribus:p:scribus:r:scribus`)
Språk: svenska (`sv`)

Nitton radgranskade strängar för import av ODF, PostScript, QuarkXPress,
Dia, Kivio, XPS och Zoner Draw samt infogning av sidor och ramar.

Kvarlämnad engelska, felaktiga axelbeteckningar och grammatikfel rättades.
Format- och produktnamn behölls där de är avsiktliga.

Alla ändringar sparades via Transifex REST API och återlästes exakt.
`lrelease`, Hunspell-SV och svlang kördes lokalt. Hunspell-SV markerade
endast formatnamn, produktnamn och filändelser. Gitleaks kördes mot både
API-deltat och arkivbatchen före push.
