# Batch 074: filvägsväljare

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 11 aktiva meddelanden i `UIFilePathSelector` har granskats radvis.

## Ändringar

Rättade den tomma statusen till könsneutrala `&lt;inget valt&gt;`, som fungerar
för både fil- och mappval. Acceleratorer, markup och sökvägstext är bevarade.
Ändringen finns i lokal commit `a1ef75b`.

## Kontroller

- XPath-räkning: 11 aktiva meddelanden i `UIFilePathSelector`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIFilePathSelector`-granskningen är lokalt
slutförd. Ändringarna är ännu inte pushade till PR #848, eftersom
kataloggranskningen fortsätter.
