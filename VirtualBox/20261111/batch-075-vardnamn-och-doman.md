# Batch 075: värdnamn och domän

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 10 aktiva meddelanden i `UIHostnameDomainNameEditor` har granskats
radvis.

## Ändringar

Rättade en dubbel preposition i hjälpen för domännamnets tilldelning. DNS-
regler, produktnyckel och värdnamnsterminologi är i övrigt korrekta.
Ändringen finns i lokal commit `699cb54`.

## Kontroller

- XPath-räkning: 10 aktiva meddelanden i `UIHostnameDomainNameEditor`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIHostnameDomainNameEditor`-granskningen är lokalt
slutförd. Ändringarna är ännu inte pushade till PR #848, eftersom
kataloggranskningen fortsätter.
