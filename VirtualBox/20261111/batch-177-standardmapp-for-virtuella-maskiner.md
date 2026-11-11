# Batch 177: standardmapp för virtuella maskiner

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 2 aktiva meddelanden i `UIDefaultMachineFolderEditor` har granskats
i VirtualBox globala inställningar för den mapp där nya virtuella maskiner
skapas som standard.

## Resultat

Etiketten har rättats från det missvisande singulara `Standardmapp för
maskin` till `Standardmapp för virtuella maskiner`. Åtkomsttangenten bevaras
på `virtuella`. Den beskrivande hjälptexten var redan korrekt.

## Kontroller

- XPath-räkning: 2 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Katalogändringen är verifierad lokalt och
avvaktar den samlade uppdateringen av PR #848 efter fullständig granskning.
