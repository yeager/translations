# Batch 113: feluppgifter

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 6 aktiva meddelanden i `UIErrorString` har granskats radvis i
sammanhanget där detaljer för COM-fel visas.

## Resultat

Två ändringar gjordes. `Callee` var felaktigt översatt som `Anropare`.
Det avser den anropade parten och översätts nu som `Anropad`; även etiketten
för den anropades resultatkod har korrigerats. HTML-entiteten `&amp;nbsp;` är
bevarad.

## Kontroller

- XPath-räkning: 6 aktiva meddelanden i `UIErrorString`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIErrorString`-granskningen är lokalt slutförd.
Ändringarna är verifierade lokalt i commit `52ae590` och ännu inte pushade
till PR:n; hela kataloggranskningen fortsätter innan nästa PR-uppdatering.
