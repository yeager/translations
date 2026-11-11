# Batch 060: maskindetaljer

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 107 aktiva meddelanden i `UIDetails` har granskats radvis. Den äldre
granskningen omfattade 102 meddelanden, och den aktuella källan har därför
kontrollerats på nytt.

## Ändringar

Rättade ofullständig sats i USB-styrkortets tillgänglighetsstatus och pluralen
under rubriken `Delade mappar`. Ändringarna finns i lokal commit `6a23a06`.

## Kontroller

- XPath-räkning: 107 aktiva meddelanden i `UIDetails`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIDetails`-granskningen är lokalt slutförd.
Ändringarna är ännu inte pushade till PR #848, eftersom kataloggranskningen
fortsätter.
