# Open Shaders: expanderad höjddimma, källor och material, häfte 74

Detta häfte omfattar åtta aktuella, tidigare oarkiverade reglage för
himmel-IBL, vanlig dimma och volymetriska materialparametrar. Källtexterna
har jämförts med Open Shaders `dev` vid revision `c1b1ef1` den 27 oktober
2026 och med den svenska Weblate-exporten från 19 oktober 2026.

*Sky IBL* följer den befintliga termen *himmel-IBL*. *Albedo* och *emission*
behålls som etablerade grafiktekniska termer.

`open-shaders-exp-height-fog-source-sv-20261027.json` är ett delta på åtta
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint`, `svlang` och Gitleaks passerar. Samtliga
källnycklar matchar den engelska katalogen. Hunspell markerar endast
avsiktliga tekniska sammansättningar och förkortningar, bland annat
*himmel-IBL*, *utomhusinspridning*, *dimdensitet* och *albedo*.
