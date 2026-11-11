# Batch 088: lagringsinställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 7 aktiva meddelanden i `UIMachineSettingsStorage` har granskats
radvis mot implementeringen i `UIMachineSettingsStorage.cpp`.

## Resultat

En ändring gjordes. I varningen om att samma disk redan används av en annan
maskin ändrades den verbala formen från den avslutade handlingen "anslutits"
till tillståndet "är ansluten". Därmed beskriver texten korrekt det aktuella
felet och följer programmets beteende.

Termerna `hårddisk`, `styrkort`, `lagringsstyrkort` och
`kretsuppsättning` har verifierats i sammanhanget.

## Kontroller

- XPath-räkning: 7 aktiva meddelanden i `UIMachineSettingsStorage`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIMachineSettingsStorage`-granskningen är lokalt
slutförd. Ändringen är verifierad lokalt i commit `43ea1fa` och ännu inte
pushad till PR:n; hela kataloggranskningen fortsätter innan nästa PR-uppdatering.
