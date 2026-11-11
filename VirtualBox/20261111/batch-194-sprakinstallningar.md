# Batch 194: språkinställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 3 aktiva meddelanden i `UILanguageSettingsEditor` har granskats i
VirtualBox globala språkinställningar.

## Resultat

`Upphovsperson(er)` har rättats till `Översättare:`. Fältet fylls av
`translatorName()` i källkoden och visar alltså översättarens namn, inte
upphovspersoner. De övriga texterna är korrekta.

## Kontroller

- XPath-räkning: 3 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Katalogändringen är verifierad lokalt och
avvaktar den samlade uppdateringen av PR #848 efter fullständig granskning.
