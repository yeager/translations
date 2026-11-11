# Batch 020: molnkonsoler

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

`UICloudConsoleManager`: 24 aktiva meddelanden, samtliga lästa radvis med
källtext och sammanhang.

## Ändringar

- Verktyget heter konsekvent `Hanterare för molnkonsoler`.
- Information om aktuell molnkonsol och konsol har naturlig bestämdhet.
- Fältens hjälpttexter använder korrekt `det här` och `den här`.
- Kryssrutealternativet `Visa i menyn` beskriver rätt funktion.

Ändringarna infördes i lokal commit `8eb3507`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ändringarna väntar på den slutliga samlade
pushen till PR #848 efter komplett radvis granskning.
