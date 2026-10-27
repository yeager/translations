# Open Shaders: Effects11-punktbelysning, häfte 64

Detta häfte omfattar elva aktuella, tidigare tomma parametrar för
punktbelysning, procedurgenererade gradientvikter och ljusspridning i
Effects11. Källtexterna har jämförts med Open Shaders `dev` vid revision
`c1b1ef1` den 27 oktober 2026 och med den svenska Weblate-exporten från
19 oktober 2026.

*Point lighting* följer den tidigare terminologin som *punktbelysning*.
*Scattering* översätts konsekvent med *spridning*. Den tekniska egenskapen
*opacity* har inte ingått i häftet, medan *reflection* översätts med
*reflektion* i den aktuella reglagekontexten.

`open-shaders-effects11-point-lighting-sv-20261027.json` är ett delta på elva
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint`, `svlang` och Gitleaks passerar. Samtliga
källnycklar matchar den engelska katalogen. Hunspell markerar bara
*avmättnad* och *gradientvikter*, båda avsiktliga tekniska sammansättningar.
