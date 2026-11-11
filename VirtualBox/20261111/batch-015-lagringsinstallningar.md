# Batch 015: lagringsinställningar

Datum: 2026-11-11
Komponent: `UIStorageSettingsEditor`, 72 aktiva meddelanden. Ytterligare 41
meddelanden är utfasade eller föråldrade och ingår inte i den aktiva katalogen.

## Radvis granskning

Kontexten har granskats mot `UIStorageSettingsEditor.cpp`. Den täcker
lagringsstyrkort, virtuella hårddiskar, optiska skivor, disketter, I/O-cache,
genomströmning och trädvyns åtgärder.

## Ändringar

- Normaliserade värdens I/O-cache och SSD-enhet.
- Rättade beskrivningarna för hårddisk, optisk skiva och diskett till naturlig
  svenska med korrekt fackbetydelse.
- Rättade etiketter och acceleratorer för val av lagringsmedium, portantal,
  hårddisk och trädvyns fäll ut/fäll ihop-åtgärd.
- Förtydligade ATAPI-genomströmning, plats på lagringsstyrkort och utmatning
  av en virtuell skiva.

## Kontroll

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `l10n-lint`: endast de två avsiktliga `--`-värdena i språkmetadata.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckta hemligheter.

## Upstream

Ändringarna är lokalt commitade som `a92fb7f` och hålls kvar lokalt medan den
radvisa granskningen fortsätter.
