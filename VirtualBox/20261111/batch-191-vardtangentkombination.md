# Batch 191: värdtangentkombination

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 2 aktiva meddelanden i `UIIndicatorKeyboardExtension` har granskats
i statusradsindikatorn för VirtualBox värdtangentkombination.

## Resultat

`kombination för värdtangent` har normaliserats till katalogens etablerade
term `värdtangentkombination`. Verktygstipset har skrivits om till idiomatisk
svenska och förklarar konkret att kombinationen växlar mellan att fånga och
släppa tangentbordet och musen. Markupen `<br>` och platshållaren `%1` är
bevarade.

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
