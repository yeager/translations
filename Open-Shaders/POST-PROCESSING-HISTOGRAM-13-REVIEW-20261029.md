# Open Shaders: histogram och autoexponering, granskning 13

Det trettonde häftet för `feature.post_processing` innehåller 25 nycklar för
histogramstyrd autoexponering, Purkinjeeffekten och funktionssammanfattningar.

Fototermen `exposure compensation` översätts med `exponeringskompensation`.
Den fysiologiska termen Purkinjeeffekten skrivs ihop på svenska. EV100 och
platsvariablerna i diagnostiksträngarna bevaras.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och printf-markörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
