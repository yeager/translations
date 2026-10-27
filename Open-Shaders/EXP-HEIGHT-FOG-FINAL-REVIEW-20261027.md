# Open Shaders: expanderad höjddimma, slutreglage, häfte 76

Detta häfte omfattar de fyra sista tidigare oarkiverade reglagen i
komponenten expanderad höjddimma: brushastighet, spridningsfördelning samt
volymetriska start- och visningsavstånd. Källtexterna har jämförts med Open
Shaders `dev` vid revision `c1b1ef1` den 27 oktober 2026 och med den svenska
Weblate-exporten från 19 oktober 2026.

*Noise velocity* blir *brushastighet* och *scattering distribution* blir
*fördelning av volymetrisk spridning*.

`open-shaders-exp-height-fog-final-sv-20261027.json` är ett delta på fyra
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint`, `svlang` och Gitleaks passerar. Samtliga
källnycklar matchar den engelska katalogen. Hunspell markerar bara
*brushastighet*, en avsiktlig teknisk sammansättning.
