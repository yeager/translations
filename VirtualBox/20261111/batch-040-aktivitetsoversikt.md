# Batch 040: aktivitetsöversikt

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Aktivitetsöversikten för värd och virtuella maskiner: 38 aktiva meddelanden,
samtliga granskade radvis.

## Ändringar

Förtydligade CPU-belastning, VM-namn, diskhastigheter och verktygstips.
Den tekniska termen `VM-exits` är bevarad. Ändringarna finns i lokal commit
`dc5663f`.

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
