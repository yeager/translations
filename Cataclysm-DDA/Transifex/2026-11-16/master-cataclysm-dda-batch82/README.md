# Cataclysm-DDA - svenska, batch 82

Datum: 2026-11-16
Komponent: `master-cataclysm-dda`
Kanal: Transifex REST API

Tio statusmeddelanden från styckning och dissektion har granskats rad för
rad i `src/butchery.cpp`. `styckning` används för den allmänna åtgärden,
medan `dissektion` reserveras för den mer precisa åtgärden med skalpell och
finkärande verktyg. Detta följer källkodens skilda verktygskrav.

## Kontroller före API-inskick

- JSON-syntax
- l10n-lint
- svlang för löpande svensk text
- Hunspell-sv
- kontroll av platshållare
- `msgfmt` är inte tillämpligt: detta är en Transifex-JSON-batch och ingen
  PO-katalog.

## Upstream-status

Skickad via Transifex REST API den 2026-11-16: 10 av 10 poster accepterades.
En separat API-återläsning bekräftade exakt måltext för samtliga 10 poster.
Detta bekräftar inskick och sparad översättning, inte upstream-granskning,
merge eller utgivning.
