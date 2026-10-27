# Open Shaders: expanderad höjddimma, dimslöjor, häfte 71

Detta häfte omfattar tolv aktuella, tidigare oarkiverade reglage för
dimslöjornas ljus, rörelse, vindstyrning och räckvidd. Källtexterna har
jämförts med Open Shaders `dev` vid revision `c1b1ef1` den 27 oktober 2026
och med den svenska Weblate-exporten från 19 oktober 2026.

*Mist* översätts konsekvent med *dimslöja*. Formaten för rörelseförskjutning
och hastighet behåller respektive formatmarkör oförändrad.

`open-shaders-exp-height-fog-mists-sv-20261027.json` är ett delta på tolv
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Samtliga källnycklar och
formatmarkörer matchar den engelska katalogen. `svlang` rapporterar två
felaktiga V2-varningar för regelbundna huvudsatser och markerar i övrigt
tekniska sammansättningar. Hunspell markerar endast formatdelen `.1f` och
tekniska termer som *inspridning* och *kubkarta*.
