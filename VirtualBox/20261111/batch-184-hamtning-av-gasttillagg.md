# Batch 184: hämtning av Gästtillägg

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 2 aktiva meddelanden i `UIDownloaderGuestAdditions` har granskats i
dialogen som hämtar VirtualBox Guest Additions.

## Resultat

Sparfrågan har rättats från det vaga `Gästtilläggens avbildning` till
`diskavbildningen för Gästtillägg`. Källans `image` avser den hämtade
diskavbildningen (ISO) och inte en bild. Produktnamnet VirtualBox och den
etablerade termen Gästtillägg är bevarade.

## Kontroller

- XPath-räkning: 2 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Katalogändringen är verifierad lokalt och
avvaktar den samlade uppdateringen av PR #848 efter fullständig granskning.
