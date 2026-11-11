# Batch 034: notifieringar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Notifieringscenter, notifieringsnedladdare, förloppsdialog och
inställningsserialisering: 10 aktiva meddelanden, samtliga granskade radvis.

## Ändringar

Sorteringsriktning, slutförda förlopp/notifieringar och placering längst upp
eller ned har tydligare och idiomatisk svenska i lokal commit `02c13e7`.

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
