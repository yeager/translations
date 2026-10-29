# Open Shaders: bokeh och skärpedjup, granskning 11

Det elfte häftet för `feature.post_processing` innehåller 25 nycklar för
bokeh och skärpedjupets fokus- och oskärpekontroller.

`Bokeh` och Cinematic Camera bevaras som etablerade tekniska namn.
`Circle of confusion` är förklarat som `oskärpecirkel` i hjälptexterna, medan
bländare, brännvidd, fokusplan och skärpedjup följer svensk fototerminologi.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och printf-markörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
