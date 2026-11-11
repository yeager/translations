# Batch 172: virtuell maskingrupp

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Det enda aktiva meddelandet i `UIChooserNodeGroup` har granskats. Texten är
nodbeskrivningen för en grupp i VirtualBox-hanterarens träd över virtuella
maskiner.

## Resultat

`Maskingrupp` har ändrats till `Virtuell maskingrupp`. Det gör referensen till
VirtualBox-VM:ar tydlig och överensstämmer med åtgärderna för att gruppera och
sortera virtuella maskingrupper i samma gränssnitt.

## Kontroller

- XPath-räkning: 1 aktivt meddelande.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Katalogändringen är verifierad lokalt och
avvaktar den samlade uppdateringen av PR #848 efter fullständig granskning.
