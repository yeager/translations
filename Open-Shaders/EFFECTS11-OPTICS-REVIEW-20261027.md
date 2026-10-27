# Open Shaders: Effects11-optik och gradienter, häfte 61

Detta häfte omfattar tolv aktuella, tidigare tomma dim-, optik- och
gradientparametrar för Effects11. Källtexterna har jämförts med Open Shaders
`dev` vid revision `c1b1ef1` den 27 oktober 2026 och med den svenska
Weblate-exporten från 19 oktober 2026.

*Fresnel* bevaras som etablerad optikterm. *Gamma curve* blir
*gammakurva*. De sammansatta parametrarna skrivs ihop på svenska, exempelvis
*Fresnelmultiplikator* och *gradientavmättnad*.

`open-shaders-effects11-optics-sv-20261027.json` är ett delta på tolv nycklar.
Det får importeras först efter upplåsning och en ny jämförelse med Hosted
Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint`, `svlang` och Gitleaks passerar. Samtliga källnycklar
matchar den engelska katalogen. Hunspell markerar bara optiktermen `Fresnel`
och de tekniska sammansättningarna.
