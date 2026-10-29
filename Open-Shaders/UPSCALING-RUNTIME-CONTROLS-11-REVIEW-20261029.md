# Open Shaders: uppskalning och körningsreglage, granskning 11

Det elfte uppskalningshäftet innehåller 25 nycklar för Reflex,
renderingsupplösning, Streamline-loggning och FPS-begränsning.

`Foveation`, `Neural Rendering`, `DisplayRes`, HMD, DX12 och filnamnet
`sl.reflex.dll` behålls som tekniska namn. `Upscale Preset` är konsekvent
översatt med `uppskalningsförinställning`. De fem profilmarkörerna `{}` är
bevarade.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och samtliga `{}`-markörer är kontrollerade mot
  den lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast tekniska namn och förkortningar som ska bevaras.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
