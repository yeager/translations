# Batch 038: guide för virtuell hårddisk

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Guiden för nya virtuella hårddiskar: 11 aktiva meddelanden, samtliga
granskade radvis.

## Ändringar

Förklaringen av dynamiskt allokerade och fasta hårddiskfiler är språkligt
korrekt och behåller betydelsen. Texten om uppdelade diskfiler är förtydligad.
Markup och tekniska termer är bevarade. Ändringarna finns i lokal commit
`6a6739a`.

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
