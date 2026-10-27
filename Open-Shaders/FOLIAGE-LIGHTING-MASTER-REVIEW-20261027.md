# Open Shaders: lövverksbelysning, huvudreglage, häfte 78

Detta häfte omfattar de två sista tidigare oarkiverade huvudreglagen för
lövverksbelysning. Källtexterna har jämförts med Open Shaders `dev` vid
revision `c1b1ef1` den 27 oktober 2026 och med den svenska Weblate-exporten
från 19 oktober 2026.

Terminologin följer den befintliga komponentöversättningen: *foliage lighting*
är *lövverksbelysning*, *scattering* är *ljusspridning* och *ambient* är
*omgivningsljus*.

`open-shaders-foliage-lighting-master-sv-20261027.json` är ett delta på två
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Samtliga källnycklar matchar
den engelska katalogen. `svlang` rapporterar en felaktig V2-varning för en
grammatisk huvudsats. Hunspell markerar endast den avsiktliga tekniska
sammansättningen *lövverksbelysning*.
