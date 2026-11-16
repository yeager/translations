# Cataclysm-DDA - svenska, batch 81

Datum: 2026-11-16
Komponent: `master-cataclysm-dda`
Kanal: Transifex REST API

Nio stridsegenskaper har granskats i `src/bonuses.cpp`. De används som
påverkade värden i effekt- och bonusbeskrivningar, inte som direktiv till
spelaren. Därför används substantiviska etiketter som `Undvikande` och
`Blockering`, medan `Chans till kritisk träff` behåller den läsbara svenska
konstruktionen.

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
