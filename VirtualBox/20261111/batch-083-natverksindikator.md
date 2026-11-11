# Batch 083: nätverksindikator

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 8 aktiva meddelanden i `UIIndicatorNetwork` har granskats radvis
och kontrollerats mot källkodens kabelkommentarer.

## Ändringar

Rättade den ofullständiga statusen för alla frånkopplade kablar. Källkoden
visar att `Connected` och `Disconnected` avser kabelstatus, så `Ansluten` och
`Frånkopplad` behålls. Ändringen finns i lokal commit `49c7f6f`.

## Kontroller

- XPath-räkning: 8 aktiva meddelanden i `UIIndicatorNetwork`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIIndicatorNetwork`-granskningen är lokalt
slutförd. Ändringarna är ännu inte pushade till PR #848, eftersom
kataloggranskningen fortsätter.
