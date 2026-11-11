# Batch 067: ögonblicksbildsdialog

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 18 aktiva meddelanden i `UITakeSnapshotDialog` har granskats radvis.

## Ändringar

Förtydligade varningen för en virtuell maskin som är igång och standardiserade
bekräftelseknapparna till `OK` och `Godkänn`. Pluralformer och `%n` är
bevarade. Ändringarna finns i lokal commit `766be4d`.

## Kontroller

- XPath-räkning: 18 aktiva meddelanden i `UITakeSnapshotDialog`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UITakeSnapshotDialog`-granskningen är lokalt
slutförd. Ändringarna är ännu inte pushade till PR #848, eftersom
kataloggranskningen fortsätter.
