# Batch 139: USB-styrkort

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 6 aktiva meddelanden i `UIUSBControllerEditor` har granskats i
maskininställningarnas USB-styrkortsval.

## Resultat

Ingen textändring behövdes. Versionsnummer, acceleratorer, tekniknamnen OHCI,
EHCI och xHCI samt deras koppling till USB-versionerna är korrekt bevarade.

## Kontroller

- XPath-räkning: 6 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Ingen katalogändring uppstod och därmed finns
inget nytt att skicka till PR #848 från denna batch.
