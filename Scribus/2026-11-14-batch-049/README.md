# Scribus svenska UI - granskningsbatch 049

Datum: 2026-11-14
Komponent: Scribus UI (`o:scribus:p:scribus:r:scribus`)
Språk: svenska (`sv`)

21 radgranskade ändringar för OpenOffice-import och PDF-export. Fel som
`LådaBox`, utskriftsområde för export, felaktiga PDF-artiklar och otydliga
beskrivningar av PDF-inställningar har rättats med hänsyn till den konkreta
dialogkontexten.

Ändringarna sparades en och en via Transifex REST API och återlästes
exakt. `lrelease`, diffkontroll, Gitleaks, Hunspell-SV och svlang
kördes lokalt. Hunspell-SV markerade endast produktnamn, format och
facktermer; svlang-varningarna bedömdes vara falska positiva för
imperativ, bisats och produktnamn.

Upstreamstatus: sparad via API och läsverifierad; ingen separat
upstreamgranskning har verifierats.
