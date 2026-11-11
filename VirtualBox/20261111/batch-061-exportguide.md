# Batch 061: guide för appliance-export

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 49 aktiva meddelanden i `UIWizardExportApp` har granskats radvis.

## Ändringar

Förbättrade svenska formuleringar för manifestfil, appliance-export,
NAT-nätverkskort och molnexport. OVF, OVA, Oracle Cloud Infrastructure och
markup har bevarats. Ändringarna finns i lokal commit `5405d76`.

## Kontroller

- XPath-räkning: 49 aktiva meddelanden i `UIWizardExportApp`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga `UIWizardExportApp`-granskningen är lokalt slutförd.
Ändringarna är ännu inte pushade till PR #848, eftersom kataloggranskningen
fortsätter.
