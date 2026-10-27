# Open Shaders: gräsoptimeringar, densitet och mesh-LOD, häfte 85

Detta häfte omfattar tolv tidigare oarkiverade nycklar för mesh-LOD,
kostnadsbias, övergångsband och densitetsreglage i gräsoptimeringar.
Källtexterna har jämförts med Open Shaders `dev` vid revision `c1b1ef1` den
27 oktober 2026 och med den svenska Weblate-exporten från 19 oktober 2026.

*Mesh* och *LOD* behålls som etablerade grafiktekniska termer. *Cost bias*
blir *kostnadsbias*, *transition band* blir *övergångsband* och *thinning*
uttrycks med *glesning*.

`open-shaders-grass-optimizations-density-sv-20261027.json` är ett delta på
tolv nycklar. Det får importeras först efter upplåsning och en ny jämförelse
med Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Samtliga källnycklar och
filnamn matchar den engelska katalogen. `svlang` ger låg poäng och tre
felaktiga V2-varningar för tekniska reglagefraser. Hunspell markerar enbart
avsiktliga grafiktekniska termer och filnamn, bland annat *mesh-LOD*,
*kostnadsbias*, *gräsmeshar* och `_LOD0.nif`.
