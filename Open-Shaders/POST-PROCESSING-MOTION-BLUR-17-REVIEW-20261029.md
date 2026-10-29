# Open Shaders: rörelseoskärpa och OpenDRT, granskning 17

Det sjuttonde häftet för `feature.post_processing` innehåller 25 nycklar för
LUT, rörelseoskärpa och OpenDRT.

Rörelseoskärpa, slutare och exponering följer svensk foto- och
grafikterminologi. OpenDRT, HDR Grey Boost och identifierare i de tekniska
hjälptexterna bevaras.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och printf-markörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
