# Batch 174: sökning i hanteraren

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 4 aktiva meddelanden i `UIChooserSearchWidget` har granskats i
VirtualBox-hanterarens sökruta för virtuella maskiner.

## Resultat

Fyra verktygstips har skrivits om till kortare, idiomatisk UI-svenska.
`träff` används för ett sökresultat och den tekniska interntermen `widget`
har ersatts med den synliga komponenten `sökruta`.

## Kontroller

- XPath-räkning: 4 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Katalogändringen är verifierad lokalt och
avvaktar den samlade uppdateringen av PR #848 efter fullständig granskning.
