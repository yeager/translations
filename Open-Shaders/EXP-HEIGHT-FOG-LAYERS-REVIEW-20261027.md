# Open Shaders: expanderad höjddimma, skikt och samplning, häfte 73

Detta häfte omfattar tolv aktuella, tidigare oarkiverade reglage för ett
andra dimskikt, himmelsbelysning, tidsmässig historik, uppsamplingsjitter
och dynamiska kubkartor. Källtexterna har jämförts med Open Shaders `dev` vid
revision `c1b1ef1` den 27 oktober 2026 och med den svenska Weblate-exporten
från 19 oktober 2026.

*Layer* blir *skikt* och *line integrals* behåller den matematiska termen
*linjeintegraler*. Kodidentifieraren för UE lämnas orörd och *froxel* används
som etablerad grafikteknisk fackterm.

`open-shaders-exp-height-fog-layers-sv-20261027.json` är ett delta på tolv
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint`, `svlang` och Gitleaks passerar. Samtliga
källnycklar matchar den engelska katalogen. Hunspell markerar endast den
bevarade kodidentifieraren och tekniska sammansättningar som *dimskikt*,
*diminspridning*, *uppsamplingsjitter* och *froxlar*.
