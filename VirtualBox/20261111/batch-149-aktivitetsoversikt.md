# Batch 149: aktivitetsöversikt

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 30 aktiva meddelanden i `UIVMActivityOverviewWidget` har granskats
radvis i aktivitetsövervakarens översikt över värd och virtuella maskiner.

## Resultat

Ingen textändring behövdes. Prestandatermer, måttetiketter, förkortningar och
den specialiserade termen `VM-exits` används konsekvent och korrekt.

## Kontroller

- XPath-räkning: 30 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Ingen katalogändring uppstod och därmed finns
inget nytt att skicka till PR #848 från denna batch.
