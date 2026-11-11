# Batch 047: meddelandecentral, del 5

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Nästa del av meddelandecentralen har granskats radvis: endast-värd-nätverk,
gästtillägg, USB-behörighet, styrkort, delat urklipp och avstängning.

## Ändringar

Förtydligade endast-värd-nätverk, åtkomst till USB-enheter och flera
säkerhets- och avstängningsmeddelanden. Terminologin för styrkort och delat
urklipp är konsekvent. Markup och platshållare är bevarade. Ändringarna finns
i lokal commit `6bb42b5`.

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
