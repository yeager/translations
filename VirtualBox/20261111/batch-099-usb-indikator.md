# Batch 099: USB-indikator

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 4 aktiva meddelanden i `UIIndicatorUSB` har granskats radvis mot
användningen i `UIIndicatorsPool.cpp`.

## Resultat

En ändring gjordes. Källtexten saknar pluralform för antalet USB-enheter,
vilket skulle ha gett felaktig svensk form vid värdet 1. Översättningen
använder därför den neutrala räknarformen `Antal anslutna USB-enheter: %1`,
som är korrekt oavsett antal.

## Kontroller

- XPath-räkning: 4 aktiva meddelanden i `UIIndicatorUSB`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIIndicatorUSB`-granskningen är lokalt slutförd.
Ändringen är verifierad lokalt i commit `73085cd` och ännu inte pushad till
PR:n; hela kataloggranskningen fortsätter innan nästa PR-uppdatering.
