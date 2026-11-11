# Batch 106: globala avancerade inställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 9 aktiva meddelanden i `UIAdvancedSettingsDialogGlobal` har
granskats radvis.

## Resultat

Ingen textändring behövdes. Kategorierna för globala inställningar använder
korrekta svenska UI-termer. Mellanslagen och bindestrecket i fönstertiteln
`VirtualBox - Inställningar` följer källtextens format.

## Kontroller

- XPath-räkning: 9 aktiva meddelanden i `UIAdvancedSettingsDialogGlobal`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIAdvancedSettingsDialogGlobal`-granskningen är
lokalt slutförd. Ingen upstreamändring finns för denna komponent;
kataloggranskningen fortsätter.
