# Batch 044: meddelandecentral, del 2

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Nästa sammanhängande del av meddelandecentralen har granskats radvis:
installation av tilläggspaket, skärmtangentbord, inspelning och lagringsbussar.

## Ändringar

Normaliserade termen `tilläggspaket`, förtydligade riskmeddelanden vid
osparade tangentbordslayouter, rättade två inspelningsfel och ersatte felaktig
styrkortsterminologi. Markup, kommandon och platshållare är bevarade.
Ändringarna finns i lokal commit `32dc311`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Meddelandecentralens återstående delar
granskas innan en samlad push till PR #848.
