# Batch 032: tangentbord

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Tangentbordsfångst, kortkommandon, pekdon och visuellt tangentbord: 76 aktiva
meddelanden, samtliga granskade radvis.

## Införd del

Den verifierade delbatchen normaliserar kortkommandon, skanningskod,
tangentplacering och tangenttexter. Ändringarna finns i lokal commit
`1fa7a09`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Resterande radvis granskade, separata
skärmtangentbordstexter tas in i en senare avgränsad batch.
