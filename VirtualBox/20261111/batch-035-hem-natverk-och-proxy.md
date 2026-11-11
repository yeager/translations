# Batch 035: hem, nätverk och proxy

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Startpanelen samt nätverkssvar, portomdirigering och proxy: 35 aktiva
meddelanden, samtliga granskade radvis.

## Ändringar

Startpanelen använder konsekvent `virtuell maskin` och idiomatisk vägledning.
Länkar, HTML, `%1` och produktnamn är bevarade. Nätverks- och proxytexterna
har förtydligats, bland annat åtkomstfel, HTTP-bibliotek, portomdirigering och
`Proxy-URL`. Ändringarna finns i lokal commit `fdd91c3`.

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
