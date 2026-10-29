# Open Shaders: OpenDRT och fysiskt bländljus, granskning 23

Det tjugotredje häftet för `feature.post_processing` innehåller 25 nycklar för
OpenDRT och fysiskt baserat bländljus.

Färgstandarderna D65 och D50, samt FFT och PSF, bevaras. `Glare` avser här
bländljus, medan `aperture` är bländare och `diffraction spikes` är
diffraktionstoppar.

Kontroller den 29 oktober 2026:

- JSON-syntax och 25 källnycklar är kontrollerade mot den lokala engelska
  katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
