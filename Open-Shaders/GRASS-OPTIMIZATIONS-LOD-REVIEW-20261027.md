# Open Shaders: gräsoptimeringar, LOD, häfte 83

Detta häfte omfattar tolv tidigare oarkiverade nycklar för gräsoptimeringars
bortgallring, avtoning och LOD-band. Källtexterna har jämförts med Open
Shaders `dev` vid revision `c1b1ef1` den 27 oktober 2026 och med den svenska
Weblate-exporten från 19 oktober 2026.

*Culling* blir *bortgallring*, *draw calls* blir *ritanrop* och *instancing*
blir *instansiering*. Filnamn, sökväg och markören `<source-mesh-name>`
bevaras exakt.

`open-shaders-grass-optimizations-lod-sv-20261027.json` är ett delta på tolv
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Samtliga källnycklar,
filnamn och sökvägar matchar den engelska katalogen. `svlang` rapporterar två
felaktiga V2-varningar i tekniska formuleringar. Hunspell markerar enbart
avsedda grafiktekniska termer, filändelser och sökvägsdelar som *mesh*,
*LOD*, *ritanrop*, `.nif` och `source-mesh-name`.
