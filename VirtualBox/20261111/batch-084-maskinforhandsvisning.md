# Batch 084: maskinförhandsvisning

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 8 aktiva meddelanden i `UIMachinePreview` har granskats radvis.

## Ändringar

Ersatte den ovanliga UI-statusen `Oåtkomlig` med `Inte tillgänglig`.
Förhandsvisningens uppdateringsintervall och övriga tillstånd är korrekta.
Ändringen finns i lokal commit `a19576b`.

## Kontroller

- XPath-räkning: 8 aktiva meddelanden i `UIMachinePreview`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIMachinePreview`-granskningen är lokalt slutförd.
Ändringarna är ännu inte pushade till PR #848, eftersom kataloggranskningen
fortsätter.
