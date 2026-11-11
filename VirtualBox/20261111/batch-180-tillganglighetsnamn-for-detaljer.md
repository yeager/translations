# Batch 180: tillgänglighetsnamn för detaljer

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Det enda aktiva meddelandet i `UIDetailsItem` har granskats. Det används som
tillgänglighetsnamn för detaljavsnitt, exempelvis allmänna inställningar eller
lagring.

## Resultat

`%1-detaljer` har ändrats till `Detaljer: %1`. Platshållaren kan innehålla
etiketter med varierande ordklass, och kolonformen ger ett naturligt svenskt
tillgänglighetsnamn utan osäkra sammansättningar.

## Kontroller

- XPath-räkning: 1 aktivt meddelande.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Katalogändringen är verifierad lokalt och
avvaktar den samlade uppdateringen av PR #848 efter fullständig granskning.
