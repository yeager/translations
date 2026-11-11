# Batch 090: seriella portar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 6 aktiva meddelanden i `UIMachineSettingsSerial` har granskats
radvis mot implementeringen i `UIMachineSettingsSerial.cpp`.

## Resultat

Ingen textändring behövdes. `Port`, `IRQ`, `I/O-port` och `portsökväg` är
korrekta i gränssnittets sammanhang. Kontrollmeddelandet om dubbletter har
också korrekt svensk innebörd.

## Kontroller

- XPath-räkning: 6 aktiva meddelanden i `UIMachineSettingsSerial`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIMachineSettingsSerial`-granskningen är lokalt
slutförd. Ingen upstreamändring finns för denna komponent; kataloggranskningen
fortsätter.
