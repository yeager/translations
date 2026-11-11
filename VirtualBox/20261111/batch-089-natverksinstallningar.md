# Batch 089: nätverksinställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 10 aktiva meddelanden i `UIMachineSettingsNetwork` har granskats
radvis.

## Resultat

Tre ändringar gjordes. För bryggad adapter, adapter för endast-värd-nätverk
och allmän drivrutin beskriver källtexten att ett val saknas. Den svenska
texten använder därför nu "har valts". Namn som saknas använder fortsatt
"har angivits", eftersom det är ett fältvärde och inte ett val.

`endast-värd-nätverk`, `NAT-nätverk`, `molnnätverk`, MAC-adress och
unicast-adress har kontrollerats mot den tekniska kontexten.

## Kontroller

- XPath-räkning: 10 aktiva meddelanden i `UIMachineSettingsNetwork`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIMachineSettingsNetwork`-granskningen är lokalt
slutförd. Ändringarna är verifierade lokalt i commit `a3345c0` och ännu inte
pushade till PR:n; hela kataloggranskningen fortsätter innan nästa PR-uppdatering.
