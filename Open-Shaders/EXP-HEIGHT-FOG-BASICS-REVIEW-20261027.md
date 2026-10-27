# Open Shaders: expanderad höjddimma, grunder, häfte 68

Detta häfte omfattar tolv aktuella, tidigare oarkiverade grundreglage för
exponentiell höjddimma: nedtoning, färg, belysning, kubkarta, densitet,
djupfördelning och riktad ljusspridning. Källtexterna har jämförts med Open
Shaders `dev` vid revision `c1b1ef1` den 27 oktober 2026 och med den svenska
Weblate-exporten från 19 oktober 2026.

*Inscattering* översätts med den grafiktekniska termen *inspridning*.
*Directional light* uttrycks som *riktat ljus*, medan *forward scattering*
och *back scattering* blir *framåtspridning* respektive *bakåtspridning*.

`open-shaders-exp-height-fog-basics-sv-20261027.json` är ett delta på tolv
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint`, `svlang` och Gitleaks passerar. Samtliga
källnycklar matchar den engelska katalogen. Hunspell markerar enbart
grafiktekniska sammansättningar och egennamnet *Henyey–Greenstein*, bland
annat *inspridning*, *kubkarta* och *anisotropi*.
