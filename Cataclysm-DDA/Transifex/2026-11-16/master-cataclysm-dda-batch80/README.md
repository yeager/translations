# Cataclysm-DDA - svenska, batch 80

Datum: 2026-11-16
Komponent: `master-cataclysm-dda`
Kanal: Transifex REST API

Nio strängar från kroppsdiagrammet har granskats rad för rad i
`src/bodygraph.cpp`. Täckning, miljöskydd och skydd visas både för specifika
kroppsdelar och som genomsnitt. De två meddelandena om saknade kroppsdelar
använder samma svenska konstruktion eftersom den är korrekt för både andra
och tredje person utan att behöva gissa grammatiskt genus för den insatta
kroppsdelen.

## Kontroller före API-inskick

- JSON-syntax
- l10n-lint
- svlang för löpande svensk text
- Hunspell-sv
- kontroll av platshållare
- `msgfmt` är inte tillämpligt: detta är en Transifex-JSON-batch och ingen
  PO-katalog.

## Upstream-status

Skickad via Transifex REST API den 2026-11-16: 9 av 9 poster accepterades.
En separat API-återläsning bekräftade exakt måltext för samtliga 9 poster.
Detta bekräftar inskick och sparad översättning, inte upstream-granskning,
merge eller utgivning.
