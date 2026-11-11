# Batch 033: globala inställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Globala inställningar för allmänt, proxy, språk och uppdateringar: 25 aktiva
meddelanden, samtliga granskade radvis.

## Införd del

Standardmappen för virtuella maskiner och VirtualBox-webbplatsen har
normaliserats i lokal commit `1523f64`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ytterligare radvis granskade formuleringar
tas in i en senare avgränsad batch.
