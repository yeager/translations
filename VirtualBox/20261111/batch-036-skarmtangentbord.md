# Batch 036: skärmtangentbord

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Skärmtangentbordets 76 aktiva meddelanden har granskats radvis, inklusive
layoutmetadata, medieknappar, webbläsarknappar, färgteman och filåtgärder.

## Ändringar

Rättade felaktiga värden i layoutmetadata, bland annat `Swedish` och
`Svenska`, till svenska fältnamn. Terminologin använder nu konsekvent
`skärmtangentbord`, och åtgärdstexter för ljud, mediespår, filhantering och
färger är idiomatiska. `%1`, acceleratorer och markup har bevarats.
Ändringarna finns i lokal commit `004479e`.

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
