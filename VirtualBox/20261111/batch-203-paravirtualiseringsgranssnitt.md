# Batch 203: paravirtualiseringsgränssnitt

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 2 aktiva meddelanden i `UIParavirtProviderEditor` har granskats i
maskininställningen för paravirtualiseringsgränssnitt.

## Resultat

Ingen textändring behövdes. `Paravirtualiseringsgränssnitt` återger den
tekniska termen korrekt och beskrivningen anger tydligt att valet gäller
gästsidan för den aktuella virtuella maskinen. Åtkomsttangenten är bevarad.

## Kontroller

- XPath-räkning: 2 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Ingen katalogändring uppstod och därmed finns
inget nytt att skicka till PR #848 från denna batch.
