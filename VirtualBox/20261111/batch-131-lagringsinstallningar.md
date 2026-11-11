# Batch 131: lagringsinställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 72 aktiva meddelanden i `UIStorageSettingsEditor` har granskats
radvis i källkoden för maskininställningarnas lagringsvy.

## Resultat

- Antalet portar uttrycks nu idiomatiskt: `en fler än` i stället för det
  felaktiga `ett större än`.
- Den generiska etiketten `Typ (format)` följer svensk versalanvändning.

Ändringarna finns i lokal commit `1058a35` och är ännu inte pushade till PR:n.

## Kontroller

- XPath-räkning: 72 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Upstream-inskick väntar tills den fullständiga
kataloggranskningen är klar.
