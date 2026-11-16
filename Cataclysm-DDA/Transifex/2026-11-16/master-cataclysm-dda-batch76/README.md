# Cataclysm-DDA – svenska, batch 76

Datum: 2026-11-16  
Komponent: `master-cataclysm-dda`  
Kanal: Transifex REST API

Åtta granskade status- och informationssträngar från panelen för bioniska
implantat. Källkontext är kontrollerad i `src/bionics_ui.cpp` på projektets
aktuella huvudgren. De engelska, kompakta etiketterna för energikostnad har
skrivits ut på svenska för att undvika tvetydiga förkortningar.

## Kontroller före API-inskick

- JSON-syntax
- l10n-lint
- svlang för löpande svensk text
- Hunspell-sv
- kontroll av platshållare
- `msgfmt` är inte tillämpligt: detta är en Transifex-JSON-batch och ingen
  PO-katalog.

## Upstream-status

Skickad via Transifex REST API den 2026-11-16: 8 av 8 poster accepterades.
En separat API-återläsning bekräftade exakt måltext för samtliga 8 poster.
Detta bekräftar inskick och sparad översättning, inte upstream-granskning,
merge eller utgivning.
