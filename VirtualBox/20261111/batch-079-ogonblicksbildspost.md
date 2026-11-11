# Batch 079: ögonblicksbildspost

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 10 aktiva meddelanden i `UISnapshotItem` har granskats radvis och
kontrollerats mot `UISnapshotPane.cpp`.

## Ändringar

Rättade etiketter för `online` och `offline`. Källkoden visar att de beskriver
om ögonblicksbilden togs medan maskinen var igång, inte nätverksanslutning.
Översättningarna är därför `körande` och `avstängd`. Ändringarna finns i lokal
commit `07f89e7`.

## Kontroller

- XPath-räkning: 10 aktiva meddelanden i `UISnapshotItem`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UISnapshotItem`-granskningen är lokalt slutförd.
Ändringarna är ännu inte pushade till PR #848, eftersom kataloggranskningen
fortsätter.
