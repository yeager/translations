# Batch 123: skalningsfaktor

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 7 aktiva meddelanden i `UIScaleFactorEditor` har granskats radvis
mot reglaget för global och skärmspecifik gästskalning.

## Resultat

En grammatisk brist har rättats: `den virtuella gästskärm` är nu `den
virtuella gästskärmen`. Övrig terminologi för skärm och skalningsfaktor är
konsekvent med reglagets funktion.

## Kontroller

- XPath-räkning: 7 aktiva meddelanden i `UIScaleFactorEditor`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIScaleFactorEditor`-granskningen är lokalt
slutförd i commit `b21621e` och ännu inte pushad till PR #848.
