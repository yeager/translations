# Open Shaders: efterbehandling och färgkorrigering, granskning 5

Det femte häftet för `feature.post_processing` innehåller 25 nycklar för COD
Bloom och färgkorrigering.

`Color Grading` är översatt med `färgkorrigering` i linje med Blender- och
översättningsminnets etablerade användning. `Bloom`, ASC CDL, MIP, RGB och
varumärket Call of Duty lämnas oförändrade. `Clip Point` blir `klippunkt` och
följer regeln att inte skriva tre lika konsonanter i följd.

Kontroller den 29 oktober 2026:

- JSON-syntax och 25 källnycklar är kontrollerade mot den lokala engelska
  katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast avsiktliga tekniska namn och sammansatta
  grafiktermer som har granskats manuellt.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
