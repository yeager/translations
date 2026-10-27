# Open Shaders: expanderad höjddimma, detaljreglage, häfte 72

Detta häfte omfattar tolv aktuella, tidigare oarkiverade reglage för
dimslöjornas täthet, storlek, vind och räckvidd samt för provjitter. Texterna
har jämförts med Open Shaders `dev` vid revision `c1b1ef1` den 27 oktober
2026 och med den svenska Weblate-exporten från 19 oktober 2026.

*Mist pocket* uttrycks som *dimslöja*. *Sample jitter* behåller den etablerade
grafiktekniska termen *provjitter*. Kodidentifieraren
`r.VolumetricFog.LightScatteringSampleJitterMultiplier` lämnas orörd.

`open-shaders-exp-height-fog-detail-sv-20261027.json` är ett delta på tolv
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Samtliga källnycklar matchar
den engelska katalogen. `svlang` rapporterar två felaktiga V2-varningar för
grammatiska huvudsatser. Hunspell markerar endast den bevarade
kodidentifieraren och tekniska termer, bland annat *provjitter*, *voxel* och
*Haltonföljden*.
