# Batch 124: tangentbordsgenvägar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 6 aktiva meddelanden i `UIShortcutConfigurationEditor` har
granskats radvis mot redigeraren i globala inmatningsinställningar.

## Resultat

Två etiketter har förbättrats. `Hanterare för VirtualBox` är nu den
projektenliga och naturliga formen `VirtualBox-hanteraren`, med bevarad
tangentbordsgenväg. Filteretiketten syftar nu tydligt på den aktuella
genvägslistan.

## Kontroller

- XPath-räkning: 6 aktiva meddelanden i `UIShortcutConfigurationEditor`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIShortcutConfigurationEditor`-granskningen är
lokalt slutförd i commit `f7d90f7` och ännu inte pushad till PR #848.
