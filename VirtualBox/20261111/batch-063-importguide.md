# Batch 063: guide för appliance-import

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 43 aktiva meddelanden i `UIWizardImportApp` har granskats radvis.

## Ändringar

Rättade signaturstatus till naturlig svensk form och normaliserade termer för
molnmaskiner, NAT-nätverkskort och molnprofilhanteraren. OVF, VDI och
appliance är bevarade där de är produktens tekniska termer. Ändringarna finns
i lokal commit `7cc27ec`.

## Kontroller

- XPath-räkning: 43 aktiva meddelanden i `UIWizardImportApp`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga `UIWizardImportApp`-granskningen är lokalt slutförd.
Ändringarna är ännu inte pushade till PR #848, eftersom kataloggranskningen
fortsätter.
