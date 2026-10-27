# Open Shaders: Effects11-sol och alternativ, häfte 66

Detta häfte omfattar nio aktuella, tidigare tomma parametrar för sol,
efterbehandling, beräkningssätt och vågor i Effects11. Källtexterna har
jämförts med Open Shaders `dev` vid revision `c1b1ef1` den 27 oktober 2026
och med den svenska Weblate-exporten från 19 oktober 2026.

*Sun specular* följer projektets etablerade term *solens spegelreflektion*.
*Post processing* översätts konsekvent med *efterbehandling* och
*procedural* med *procedurgenererad*.

`open-shaders-effects11-sun-options-sv-20261027.json` är ett delta på nio
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint`, `svlang` och Gitleaks passerar. Samtliga
källnycklar matchar den engelska katalogen. Hunspell markerar bara
*vågamplitud* och *gradientvikter*, båda avsiktliga tekniska
sammansättningar.
