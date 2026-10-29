# Open Shaders: foveerad uppskalning, granskning 2

Det andra uppskalningshäftet innehåller 25 nycklar för foveerad uppskalning
i VR. Det omfattar kantövergångar, DLSS-lägen och områdesmasker.

`Foveated` återges med `foveerad`, den etablerade fackformen i sammanhang där
bildens upplösning varierar med blickriktningen. `Dithering`, `Smoothstep`,
DLSS, FSR och VR lämnas som tekniska benämningar. `Preset` är konsekvent
`förinställning` och `upscaler` är `uppskalningsmetod`.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och samtliga formatmarkörer är kontrollerade
  mot den lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast tekniska termer och förkortningar som är avsiktliga
  i den här komponenten.
- En ny Weblate-export måste jämföras med häftet före import, eftersom
  komponenten fortfarande är låst.
