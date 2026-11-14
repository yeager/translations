# Scribus svenska UI - granskningsbatch 017

Datum: 2026-11-14
Komponent: Scribus UI (`o:scribus:p:scribus:r:scribus`)
Språk: svenska (`sv`)

20 radgranskade strängar för dokumentinställningar, marginaler, noder,
notstilar och OpenOffice.org Draw-import.

Korrigerar böjning, stavning, rena engelska rester, notterminologi och
gränssnittstexter. Produkt- och formatnamn behölls där de är avsiktliga.

Alla ändringar sparades via Transifex REST API och återlästes exakt.
`lrelease`, Hunspell-SV och svlang kördes lokalt. Svlangs längd- och
V2-varningar beror på sammanslagna etiketter, inte på ett fel i
översättningen. Gitleaks kördes mot både API-deltat och arkivbatchen före
push.
