# Batch 211: skärmbildsvisare

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 3 aktiva meddelanden i `UIScreenshotViewer` har granskats i
skärmbildsvisaren för en virtuell maskin.

## Resultat

Två verktygstips har rättats. `oskalade skärmbilden` har ersatts med den
naturliga visningsbeskrivningen `skärmbilden i originalstorlek`, och den
skalade skärmbilden har fått korrekt artikel. Platshållarna `%1` och `%2` är
bevarade.

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
