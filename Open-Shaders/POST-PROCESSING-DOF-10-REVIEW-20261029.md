# Open Shaders: tonmappning och skärpedjup, granskning 10

Det tionde häftet för `feature.post_processing` innehåller 25 nycklar för
tonmappning, sammansättning och skärpedjup.

Varu- och projektnamn som OpenDRT, Bloom, Lens Flare, Physical Glare,
Auto Exposure, Cinematic Camera och CEDEC bevaras. `Vibrance` översätts med
`färgintensitet` för att skilja funktionen från vanlig färgmättnad. Formeln i
hjälptexten bevarar alla identifierare exakt.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och printf-markörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
