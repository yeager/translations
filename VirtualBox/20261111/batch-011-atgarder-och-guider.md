# Batch 011: åtgärder och guider

Datum: 2026-11-11
Komponenter: `UIActionPool`, `UIMessageCenter`, `UIVMCloseDialog`,
`UIWizardAddCloudVM`, `UIWizardCloneVM`, `UIWizardNewVD` och
`UIUpdateSettingsEditor`.

## Granskade och ändrade områden

- Rättade åtgärder för paus, snabbmeny, avstängning, konsol och delat urklipp.
- Ersatte en trasig lång hjälptext om mus- och tangentbordsfångst med idiomatisk
  svenska och bevarad HTML, bildreferens och värdtangentterminologi.
- Rättade källor, profiler, instanser och NAT-adresser i moln- och
  kloningsguiderna samt plural- och böjningsfel i hårddiskguiden.
- Normaliserade förhandsutgåvor och testbyggen.

## Delkontroll

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: konsekvent.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckta hemligheter.

## Upstream

Ändringarna är lokala och inte pushade till PR #848. Full radvis granskning
och samlad slutkontroll återstår innan PR:n uppdateras.
