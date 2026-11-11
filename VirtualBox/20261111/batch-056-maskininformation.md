# Batch 056: maskininformation

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 85 aktiva meddelanden i `UIVMInformationDialog` har granskats radvis.

## Ändringar

Rättade termen för nätverkshastighet, virtualiseringstermerna `VM-exits` och
`Disk-I/O`, sammansättningen `fjärrskrivbordsserverport` samt några
användargränssnittstexter. Ändringarna finns i lokal commit `3e6854f`.

## Kontroller

- XPath-räkning: 85 aktiva meddelanden i `UIVMInformationDialog`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga `UIVMInformationDialog`-granskningen är lokalt slutförd.
Ändringarna är ännu inte pushade till PR #848, eftersom kataloggranskningen
fortsätter.
