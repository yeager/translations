# Batch 092: startordning

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 4 aktiva meddelanden i `UIBootOrderEditor` har granskats radvis mot
`UIBootOrderEditor.cpp`.

## Resultat

Ingen textändring behövdes. `uppstartsordning`, `enheter`, BIOS och UEFI
uttrycks korrekt och funktionstexterna för att flytta enheter bevarar sin
exakta betydelse.

## Kontroller

- XPath-räkning: 4 aktiva meddelanden i `UIBootOrderEditor`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIBootOrderEditor`-granskningen är lokalt slutförd.
Ingen upstreamändring finns för denna komponent; kataloggranskningen fortsätter.
