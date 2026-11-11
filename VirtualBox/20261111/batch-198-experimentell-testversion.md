# Batch 198: experimentell testversion

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Det enda aktiva meddelandet i `UIMachineWindow` har granskats. Det är
fönstertitelns tillägg när VirtualBox byggs med den experimentella
bleeding-edge-konfigurationen.

## Resultat

`byggnation` har ersatts med `testversion`. Den nya termen är naturlig i en
slutanvändares fönstertitel och är konsekvent med katalogens befintliga text
om experimentell testversion. Versions- och revisionsplatshållarna samt den
källstyrda avgränsaren är bevarade.

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
