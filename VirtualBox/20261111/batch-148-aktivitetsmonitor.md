# Batch 148: aktivitetsövervakare

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 6 aktiva meddelanden i `UIVMActivityMonitorPaneContainer` har
granskats radvis i aktivitetsövervakarens inställningsflik.

## Resultat

Knapptexten `Återställ standardvärden` har förtydligats till
`Återställ standardinställningarna`, eftersom knappen återställer diagramvyns
inställningar och inte maskinens övervakningsdata.

Ändringen finns i lokal commit `f97dffa` och är ännu inte pushad till PR:n.

## Kontroller

- XPath-räkning: 6 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Upstream-inskick väntar tills den fullständiga
kataloggranskningen är klar.
