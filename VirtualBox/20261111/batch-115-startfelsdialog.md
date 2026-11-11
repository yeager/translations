# Batch 115: startfelsdialog

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 11 aktiva meddelanden i `UIBootFailureDialog` har granskats radvis
mot `UIBootFailureDialog.cpp`.

## Resultat

En ändring gjordes. Informationstexten talade tidigare bara om en DVD med ett
operativsystem. Källtexten avser en installations-DVD, och den svenska texten
anger nu detta uttryckligen. ISO-fil, uppstartsordning, uppstartsmedium och
övriga åtgärdstexter är kontrollerade i sitt dialogsammanhang.

## Kontroller

- XPath-räkning: 11 aktiva meddelanden i `UIBootFailureDialog`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIBootFailureDialog`-granskningen är lokalt
slutförd. Ändringen är verifierad lokalt i commit `7509366` och ännu inte
pushad till PR:n; hela kataloggranskningen fortsätter innan nästa PR-uppdatering.
