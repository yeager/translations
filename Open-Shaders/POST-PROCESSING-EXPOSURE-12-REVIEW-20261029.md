# Open Shaders: skärpedjup och autoexponering, granskning 12

Det tolfte häftet för `feature.post_processing` innehåller 25 nycklar för
skärpedjup, HDR-värden och histogramstyrd autoexponering.

Petzval, Bloom, ImageSpace, Cinematic Camera, HDR, RGB och EV100 bevaras som
tekniska beteckningar. `Bin` översätts med `fack`, vilket passar histogrammets
indelning i värdeintervall.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och printf-markörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
