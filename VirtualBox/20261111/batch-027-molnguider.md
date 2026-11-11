# Batch 027: molnguider

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- `UIWizardAddCloudVM`: 12 aktiva meddelanden.
- `UIWizardNewCloudVM`: 18 aktiva meddelanden.
- `UIAcquireCloudMachineCloneNameDialog`: 2 aktiva meddelanden.

Samtliga 32 aktiva meddelanden granskades radvis.

## Ändringar

- Konsekvent terminologi: `molnmaskin`, `molntjänstleverantör`,
  `molntjänstprofil`, `instans` och `avbildning`.
- Guideinstruktionerna är idiomatiska och beskriver korrekt urvalet av
  instans, plats och avbildning.
- Hanteraren för molnprofiler använder samma verktygsnamn som övriga
  gränssnittet.

Ändringarna infördes i lokal commit `cba0297`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ändringarna väntar på den samlade PR-pushen
efter fullständig radvis granskning.
