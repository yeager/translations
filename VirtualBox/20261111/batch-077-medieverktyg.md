# Batch 077: medieverktyg

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 10 aktiva meddelanden i `UIMediumTools` har granskats radvis.

## Ändringar

Normaliserade diskettfil som term och återgav `Choose/Create` med den
konsekventa UI-formen `Välj eller skapa`. Platshållaren `%1` och
filtypsmönstren är bevarade. Ändringarna finns i lokal commit `3430207`.

## Kontroller

- XPath-räkning: 10 aktiva meddelanden i `UIMediumTools`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIMediumTools`-granskningen är lokalt slutförd.
Ändringarna är ännu inte pushade till PR #848, eftersom kataloggranskningen
fortsätter.
