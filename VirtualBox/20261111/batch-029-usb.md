# Batch 029: USB

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

`UIUSBControllerEditor`, `UIUSBMenu`, `UIUSBSettingsEditor` och `UIUSBTools`:
23 aktiva meddelanden, samtliga granskade radvis.

## Ändringar

- Den virtuella USB-kontrollern refererar idiomatiskt till den här maskinen.
- Enhetens och filtrets etiketter använder konsekvent `Tillverkar-ID` och
  `Produkt-ID`.

Ändringarna infördes i lokal commit `99e657b`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ändringarna inväntar samlad push till PR #848
efter fullständig radvis granskning.
