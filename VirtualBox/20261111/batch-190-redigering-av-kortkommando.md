# Batch 190: redigering av kortkommando

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 2 aktiva meddelanden i `UIHotKeyEditor` har granskats. De är
verktygstips för knappar som återställer respektive rensar ett kortkommando.

## Resultat

Båda texterna har fått bestämd form. `Unset shortcut` har dessutom rättats
från den tvetydiga åtgärden `Ta bort` till `Rensa kortkommandot`, vilket
beskriver att bindningen avlägsnas utan att något objekt tas bort.

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
