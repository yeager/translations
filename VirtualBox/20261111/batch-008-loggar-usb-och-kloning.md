# Batch 008: loggar, USB och kloning

Datum: 2026-11-11
Komponenter: `UIVMLogViewerWidget`, `UIVirtualCPUEditor`, `UIUSB*` och
`UIWizardCloneVM`.

## Granskade och ändrade områden

- Loggvisaren: rättade villkorstexter, stavfelet `komemr` och den trasiga
  instruktionen för att läsa in en loggmapp igen.
- CPU och USB: konsekventa svenska etiketter för processorer och enheter.
- Kloningsguiden: ersatte samtliga felaktiga konstruktioner med
  `När kryssad` och tydliggjorde effekten av respektive kloningsalternativ.

## Delkontroll

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckta hemligheter.

## Upstream

Ändringarna är lokala och inte pushade till PR #848. Full radvis granskning
och samlad slutkontroll återstår innan PR:n uppdateras.
