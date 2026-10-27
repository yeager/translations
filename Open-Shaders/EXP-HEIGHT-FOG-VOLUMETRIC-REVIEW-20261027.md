# Open Shaders: expanderad höjddimma, volymetriskt brus, häfte 75

Detta häfte omfattar tolv aktuella, tidigare oarkiverade reglage för
volymetrisk dimma, gitteravstånd, utsläckning och volymetriskt brus.
Källtexterna har jämförts med Open Shaders `dev` vid revision `c1b1ef1` den
27 oktober 2026 och med den svenska Weblate-exporten från 19 oktober 2026.

*Extinction* blir *utsläckning*. *Value noise* uttrycks som *värdebrus* och
Hash, PCG Quintic samt den tekniska termen *origo* lämnas oförändrade.

`open-shaders-exp-height-fog-volumetric-sv-20261027.json` är ett delta på
tolv nycklar. Det får importeras först efter upplåsning och en ny jämförelse
med Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Samtliga källnycklar matchar
den engelska katalogen. `svlang` ger låg poäng och tre felaktiga
V2-varningar, eftersom texten innehåller nödvändiga grafiktekniska termer och
reglagefraser. Hunspell markerar samma tekniska termer, exempelvis
*utsläckningsskala*, *brusfält*, *PCG*, *Quintic* och *dimmansamlingar*.
