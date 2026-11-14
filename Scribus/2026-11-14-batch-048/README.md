# Scribus svenska UI - granskningsbatch 048

Datum: 2026-11-14
Komponent: Scribus UI (`o:scribus:p:scribus:r:scribus`)
Språk: svenska (`sv`)

26 radgranskade ändringar för korta ord, tangentinställningar,
stilhantering, texthanteraren och banverktyg. Bland annat normaliserades
menynamnet `Arkiv`, tangentterminologi och formuleringar i verktygstips.

Ändringarna sparades en och en via Transifex REST API och återlästes
exakt. `lrelease`, diffkontroll, Gitleaks, Hunspell-SV och svlang
kördes lokalt. Hunspell-SV markerade bara facktermer och mnemonikod;
svlang-varningarna bedömdes vara falska positiva för en bisats,
ensamma UI-etiketter och Scribus-specifika termer.

Upstreamstatus: sparad via API och läsverifierad; ingen separat
upstreamgranskning har verifierats.
