# Cataclysm-DDA - svenska, batch 79

Datum: 2026-11-16
Komponent: `master-cataclysm-dda`
Kanal: Transifex REST API

Fjorton strängar har granskats rad för rad i kroppsstatusens ImGui-gränssnitt.
Källan `src/body_status_ui.cpp` bekräftar bland annat att `Bel.` är
kolumnrubriken för belastning och att `Dold` markerar rustningsföremål som
är dolda. `MEDICAL` förekommer även i receptkategorier och har därför fått
den breda översättningen `MEDICINSK`.

## Kontroller före API-inskick

- JSON-syntax
- l10n-lint
- svlang för löpande svensk text
- Hunspell-sv
- kontroll av platshållare
- `msgfmt` är inte tillämpligt: detta är en Transifex-JSON-batch och ingen
  PO-katalog.

## Upstream-status

Skickad via Transifex REST API den 2026-11-16: 14 av 14 poster accepterades.
En separat API-återläsning bekräftade exakt måltext för samtliga 14 poster.
Detta bekräftar inskick och sparad översättning, inte upstream-granskning,
merge eller utgivning.
