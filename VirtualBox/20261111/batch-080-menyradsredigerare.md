# Batch 080: menyradsredigerare

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 9 aktiva meddelanden i `UIMenuBarEditorWidget` har granskats radvis.

## Ändringar

Rättade bestämd form i åtgärden för att aktivera menyraden. Virtuell skärm,
skalning, mappning och menyåtgärder är i övrigt korrekta. Ändringen finns i
lokal commit `d0dea3a`.

## Kontroller

- XPath-räkning: 9 aktiva meddelanden i `UIMenuBarEditorWidget`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIMenuBarEditorWidget`-granskningen är lokalt
slutförd. Ändringarna är ännu inte pushade till PR #848, eftersom
kataloggranskningen fortsätter.
