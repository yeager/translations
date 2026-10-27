# Open Shaders: gräsoptimeringar, bortgallring, häfte 84

Detta häfte omfattar tolv tidigare oarkiverade nycklar för GPU-styrd
bortgallring, bildpunktsstorlek och densitetsreglage i gräsoptimeringar.
Källtexterna har jämförts med Open Shaders `dev` vid revision `c1b1ef1` den
27 oktober 2026 och med den svenska Weblate-exporten från 19 oktober 2026.

*Culling* blir *bortgallring*, *draw* blir *ritanrop* och *vertex shader*
följer terminologiregeln med *hörnpunktsskuggare*. Filnamnet `_LOD1.nif` och
förkortningarna GPU, Hi-Z och INI lämnas orörda.

`open-shaders-grass-optimizations-culling-sv-20261027.json` är ett delta på
tolv nycklar. Det får importeras först efter upplåsning och en ny jämförelse
med Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Samtliga källnycklar och
filnamn matchar den engelska katalogen. `svlang` ger låg poäng och sex
felaktiga V2-varningar på grund av nödvändiga gränssnittsfraser och
grafiktekniska termer. Hunspell markerar samma avsiktliga termer, bland annat
*ritanrop*, *hörnpunktsskuggare*, *mesh-nivå* och *Hi-Z-ocklusionsgallring*.
