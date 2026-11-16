# Cataclysm-DDA - svenska, batch 78

Datum: 2026-11-16
Komponent: `master-cataclysm-dda`
Kanal: Transifex REST API

Åtta strängar från bionik- och rustningsgränssnittet har granskats rad för
rad. Källan i `src/bionics_ui.cpp` visar att de första fem hör till
vapeninstallation i ett bioniskt implantat. `src/body_status_ui.cpp` och
`src/armor_layers.cpp` bekräftar att de tre sista anger tom rustningslista
respektive innersta och yttersta rustningslagret.

Projektets etablerade term `bioniskt implantat` används konsekvent. Svenska
verb i menyer och felrutor är direkta och naturliga. Platshållare och
radbrytning i den längre felrutan har bevarats exakt.

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
