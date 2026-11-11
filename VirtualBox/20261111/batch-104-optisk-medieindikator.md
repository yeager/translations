# Batch 104: indikator för optiska medier

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 2 aktiva meddelanden i `UIIndicatorOpticalDisks` har granskats
radvis mot användningen i `UIIndicatorsPool.cpp`.

## Resultat

Två ändringar gjordes. Precis som för diskettindikatorn saknar källsträngarna
pluralformer. De använder nu antaloberoende svenska former för anslutna
enheter och monterade avbildningar, så även värdet 1 blir grammatiskt korrekt.

## Kontroller

- XPath-räkning: 2 aktiva meddelanden i `UIIndicatorOpticalDisks`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIIndicatorOpticalDisks`-granskningen är lokalt
slutförd. Ändringarna är verifierade lokalt i commit `f9051f9` och ännu inte
pushade till PR:n; hela kataloggranskningen fortsätter innan nästa PR-uppdatering.
