# Batch 143: USB-inställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 2 aktiva meddelanden i `UIUSBSettingsEditor` har granskats i
maskininställningarnas USB-avsnitt.

## Resultat

Verktygstipsets `USB-kontroller` har normaliserats till `USB-styrkort`, samma
term som används i den tillhörande etiketten och övriga maskininställningar.

Ändringen finns i lokal commit `8054e3e` och är ännu inte pushad till PR:n.

## Kontroller

- XPath-räkning: 2 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Upstream-inskick väntar tills den fullständiga
kataloggranskningen är klar.
