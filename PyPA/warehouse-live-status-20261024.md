# PyPA Warehouse, svensk status

Kontrollerad i Hosted Weblate den 24 oktober 2026.

- 2 016 strängar totalt.
- 1 923 strängar är översatta.
- 93 strängar är ofärdiga, varav 60 är tomma och 33 behöver redigeras.
- Fem kontroller fallerar: en Python-formatkontroll, en kontroll för identiska pluralformer, två för återanvänd översättning och en XML-markering.

Komponenten är tillfälligt låst för bidrag. Hosted Weblate uppger att den automatiska låsningen beror på att arkivet inte kan slås samman. Ingen fil eller enskild översättning ska skickas upp förrän komponenten åter är upplåst och en ny export har hämtats.

## Förberett delta

`pypa-warehouse-sv-reviewed-provenance-20261024.delta.po` innehåller 95 radgranskade poster från den publika exporten: de 60 tomma posterna och de 33 poster vars tidigare svenska text var markerad för redigering. Deltat passerar `msgfmt --check --check-format`, svlang och Gitleaks. `l10n-lint` har två kvarvarande pluralvarningar för **intyg**, där singular och plural har samma naturliga svenska form och båda använder samma obligatoriska platshållare.

Uppföljning 2026-10-26: Hosted Weblate visar fortfarande att komponenten är automatiskt låst eftersom arkivet inte kunnat slås samman. Antalen är oförändrade: 2 016 totalt, 1 923 översatta, 93 ofärdiga (60 tomma och 33 som behöver redigeras). Deltat är fortfarande inte inskickat. Vid upplåsning ska källtexter, aktuell måltext och pluralformer jämföras på nytt före uppladdning.
