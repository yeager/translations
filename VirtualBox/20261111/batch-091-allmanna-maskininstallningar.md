# Batch 091: allmänna maskininställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 8 aktiva meddelanden i `UIMachineSettingsGeneral` har granskats
radvis mot implementeringen i `UIMachineSettingsGeneral.cpp`.

## Resultat

Ingen textändring behövdes. Översättningarna för virtuell maskin,
diskkryptering, chiffertyp och lösenordsvalidering är korrekta i sitt
inställningssammanhang. Tangentbordsgenvägarna för beskrivning, kryptering,
identitet och funktioner är bevarade.

## Kontroller

- XPath-räkning: 8 aktiva meddelanden i `UIMachineSettingsGeneral`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIMachineSettingsGeneral`-granskningen är lokalt
slutförd. Ingen upstreamändring finns för denna komponent; kataloggranskningen
fortsätter.
