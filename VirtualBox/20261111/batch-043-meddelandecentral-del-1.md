# Batch 043: meddelandecentral, del 1

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Första sammanhängande delen av meddelandecentralens aktiva fel-, uppdaterings-
och tilläggspakettexter har granskats radvis. Återstående delar av samma
kontext hanteras i separata batcher.

## Ändringar

Rättade bland annat COM-serverstart, muspekarintegration, allvarliga fel,
versionskontroll, länkar till ny version, tilläggspaket, förhandsutgåvor och
filöverskrivning. HTML, URL:er och platshållare är bevarade. Ändringarna finns
i lokal commit `5e4ed58`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ändringarna inväntar fortsatt radvis
granskning av meddelandecentralen och därefter samlad push till PR #848.
