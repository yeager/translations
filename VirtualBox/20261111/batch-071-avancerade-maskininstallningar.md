# Batch 071: avancerade maskininställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 12 aktiva meddelanden i `UIAdvancedSettingsDialogMachine` har
granskats radvis.

## Ändringar

Förtydligade dialogens navigeringshjälp till idiomatisk svensk UI-text. Övriga
kategorinamn motsvarar de faktiska inställningssidorna. Ändringen finns i
lokal commit `be45645`.

## Kontroller

- XPath-räkning: 12 aktiva meddelanden i `UIAdvancedSettingsDialogMachine`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIAdvancedSettingsDialogMachine`-granskningen är
lokalt slutförd. Ändringarna är ännu inte pushade till PR #848, eftersom
kataloggranskningen fortsätter.
