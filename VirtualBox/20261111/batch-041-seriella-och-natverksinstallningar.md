# Batch 041: seriella portar och nätverksinställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Medier, användarnamn och lösenord, seriella portar samt nätverksfunktioner:
73 aktiva meddelanden, samtliga granskade radvis.

## Ändringar

Förtydligade nummer och basadress för seriell port samt nätverksbrygga och
MAC-adress för nätverkskort. Tekniska format, exempel och platshållare är
bevarade. Ändringarna finns i lokal commit `aedd069`.

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
