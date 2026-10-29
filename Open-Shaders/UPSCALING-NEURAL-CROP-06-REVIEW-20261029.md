# Open Shaders: neural rendering och beskärning, granskning 6

Det sjätte uppskalningshäftet innehåller 25 nycklar för kalibrering,
karaktärsbeskärning och dialogbegränsning i Neural Rendering.

`Crop` är konsekvent `beskärning` och `crop fit` är `anpassning av
beskärning`. `Pass`, NR, DLSS och FSR behålls som tekniska benämningar.
Procentformatet `%.0f%%` i kalibreringsresultatet är oförändrat.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och samtliga formatmarkörer är kontrollerade
  mot den lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar enbart etablerade tekniska förkortningar och sammansatta
  fackord som har granskats manuellt.
- En ny Weblate-export krävs före import till den låsta komponenten.
