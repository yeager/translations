# Open Shaders: neural rendering och status, granskning 10

Det tionde uppskalningshäftet innehåller 25 nycklar för mellanrumshantering,
status, NGX-maskning och uppskalningsförinställningar.

Statusvärdet `{}` i den aktiva körmiljön är bevarat. `Frame generation` är
konsekvent `bildgenerering`, medan DLAA, DLSS-G, FSR, NGX och NVIDIA Reflex
är officiella tekniska namn som lämnas oförändrade.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och `{}` är kontrollerade mot den lokala
  engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast avsiktliga produktnamn och förkortningar.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
