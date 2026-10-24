# PyPA Warehouse, svensk status

Kontrollerad i Hosted Weblate den 24 oktober 2026.

- 2 016 strängar totalt.
- 1 923 strängar är översatta.
- 93 strängar är ofärdiga, varav 60 är tomma och 33 behöver redigeras.
- Fem kontroller fallerar: en Python-formatkontroll, en kontroll för identiska pluralformer, två för återanvänd översättning och en XML-markering.

Komponenten är tillfälligt låst för bidrag. Hosted Weblate uppger att den automatiska låsningen beror på att arkivet inte kan slås samman. Ingen fil eller enskild översättning ska skickas upp förrän komponenten åter är upplåst och en ny export har hämtats.

## Förberett delta

`pypa-warehouse-sv-reviewed-provenance-20261024.delta.po` innehåller 95 radgranskade poster från den publika exporten: de 60 tomma posterna och de 33 poster vars tidigare svenska text var markerad för redigering. Deltat passerar `msgfmt --check --check-format`, svlang och Gitleaks. `l10n-lint` har två kvarvarande pluralvarningar för **intyg**, där singular och plural har samma naturliga svenska form och båda använder samma obligatoriska platshållare.
