# Open Shaders: Effects11-stjärnor och sol, häfte 65

Detta häfte omfattar tolv aktuella, tidigare tomma parametrar för animerade
stjärnor samt solens färg, glöd, belysning och strålar i Effects11.
Källtexterna har jämförts med Open Shaders `dev` vid revision `c1b1ef1` den
27 oktober 2026 och med den svenska Weblate-exporten från 19 oktober 2026.

*Animation density* uttrycks som *animeringstäthet* för att beskriva mängden
animerade stjärnor utan att blanda ihop den med ljusintensitet. *Sun glow*
blir *solglöd* och den etablerade termen *solstrålar* behålls.

`open-shaders-effects11-stars-sun-sv-20261027.json` är ett delta på tolv
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint`, `svlang` och Gitleaks passerar. Samtliga
källnycklar matchar den engelska katalogen. Hunspell markerar bara
*solglödets* och *avmättnad*, som här är avsiktliga böjningar och tekniska
termer.
