# Batch 053: guide för ny virtuell maskin

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 76 aktiva meddelanden i `UIWizardNewVM` har granskats radvis.

## Ändringar

Förtydligade konfiguration, installation av operativsystem, virtuell hårdvara,
resurstilldelning, namn och hårddiskstorlek. Terminologin för EFI,
ISO-avbildning och Gästtillägg är konsekvent. Ändringarna finns i lokal commit
`82733f4`.

## Kontroller

- XPath-räkning: 76 aktiva meddelanden i `UIWizardNewVM`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga `UIWizardNewVM`-granskningen är lokalt slutförd. Ändringarna
är ännu inte pushade till PR #848, eftersom kataloggranskningen fortsätter.
