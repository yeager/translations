# Batch 126: miniverktygsfält

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 4 aktiva meddelanden i `UIMiniToolBar` har granskats radvis mot
verktygsfältet som visas i helskärmsläge och sömlöst läge.

## Resultat

`verktygsraden` har standardiserats till `verktygsfältet`, i linje med
övrig svensk VirtualBox-text och den vedertagna UI-termen. Övriga åtgärder
för minimering, lägesbyte och stängning var korrekta.

## Kontroller

- XPath-räkning: 4 aktiva meddelanden i `UIMiniToolBar`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIMiniToolBar`-granskningen är lokalt slutförd i
commit `2786bae` och ännu inte pushad till PR #848.
