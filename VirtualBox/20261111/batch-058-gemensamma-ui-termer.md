# Batch 058: gemensamma UI-termer

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 278 aktiva meddelanden i `UICommon` har granskats radvis. Den äldre
räkningen 281 omfattade även tre poster med `translation type="vanished"`.

## Ändringar

Rättade bindestreck för kombinerad PS/2- och USB-mus, prepositionen i
lagringsformuleringar, versal för `video/ljud` och statusar för gästsessioner
och processer. Ändringarna finns i lokal commit `e3a131b`.

## Kontroller

- XPath-räkning: 278 aktiva meddelanden i `UICommon`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UICommon`-granskningen är lokalt slutförd.
Ändringarna är ännu inte pushade till PR #848, eftersom kataloggranskningen
fortsätter.
