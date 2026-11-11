# Batch 037: applianceguider

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Guiderna för export och import av virtuella appliances: 92 aktiva meddelanden,
samtliga granskade radvis.

## Ändringar

Rättade böjning, satsstruktur och konsekvent terminologi för appliance,
OVF, VDI, molnprofiler och virtuella maskiner. Acceleratorer, HTML och
tekniska formatnamn har bevarats. Ändringarna finns i lokal commit `ad4d5ca`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ändringarna inväntar fullständig radvis
granskning före samlad push till PR #848.
