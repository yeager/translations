# Batch 072: mediumplats och storlek

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 11 aktiva meddelanden i `UIMediumSizeAndPathGroupBox` har granskats
radvis.

## Ändringar

Förtydligade hjälpen för filval och omformulerade grupprubriken till naturlig
svensk ordföljd. Lagringsstorlek, filnamn och sökvägsstatus är i övrigt
korrekta. Ändringarna finns i lokal commit `f26489a`.

## Kontroller

- XPath-räkning: 11 aktiva meddelanden i `UIMediumSizeAndPathGroupBox`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIMediumSizeAndPathGroupBox`-granskningen är
lokalt slutförd. Ändringarna är ännu inte pushade till PR #848, eftersom
kataloggranskningen fortsätter.
