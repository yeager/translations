# Cataclysm-DDA – svenska, batch 77

Datum: 2026-11-16  
Komponent: `master-cataclysm-dda`  
Kanal: Transifex REST API

Åtta granskade list-, dialog- och menysträngar i bionikpanelen. Källkod i
`src/bionics_ui.cpp` har använts för att skilja tomlistor, genvägsbokstäver,
bränsleinställningar och vapenåtgärder åt. CBM skrivs ut som `bioniskt
implantat`, projektets etablerade svenska term.

## Kontroller före API-inskick

- JSON-syntax
- l10n-lint
- svlang för löpande svensk text
- Hunspell-sv
- kontroll av platshållare och radbrytningar
- `msgfmt` är inte tillämpligt: detta är en Transifex-JSON-batch och ingen
  PO-katalog.

## Upstream-status

Skickad via Transifex REST API den 2026-11-16: 8 av 8 poster accepterades.
En separat API-återläsning bekräftade exakt måltext för samtliga 8 poster.
Detta bekräftar inskick och sparad översättning, inte upstream-granskning,
merge eller utgivning.
