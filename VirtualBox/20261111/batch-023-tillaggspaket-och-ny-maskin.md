# Batch 023: tilläggspaket och ny virtuell maskin

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- `UIExtensionPackManager`: 14 aktiva meddelanden.
- `UIUpdateManager`: 11 aktiva meddelanden utan ändringsbehov.
- `UIWizardNewVM`: 75 aktiva meddelanden.

Samtliga 100 aktiva meddelanden lästes radvis. `UIWizardNewVMPageUnattended`
finns inte i den aktuella katalogen.

## Ändringar

- `Hanterare för tilläggspaket` används som verktygsnamn, och paketets status
  har korrekt neutrum.
- Guiden använder `Sammanfattning`, produktnamnet `Gästtillägg` och
  `installationsmedium` konsekvent.
- ISO-avbildningens och den virtuella maskinens relation beskrivs korrekt.

Ändringarna infördes i lokal commit `bc91842`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ändringarna inväntar fullständig radvis
granskning innan PR #848 uppdateras.
