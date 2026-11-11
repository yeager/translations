# Batch 171: maskinhanterargrupp

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 9 aktiva meddelanden i `UIChooserItemGroup` har granskats i
VirtualBox-hanterarens grupperade lista över virtuella maskiner, inklusive
pluraler, verktygstips och knappar för att fälla in respektive ut en grupp.

## Resultat

Två pluralformer har förtydligats från `maskin` till `virtuell maskin`.
Källkodens `machine` avser här en VirtualBox-VM och inte värddatorn. Övriga
texter, markup och platshållare är korrekta; `(%n kör)` är idiomatiskt för
antalet körande virtuella maskiner.

## Kontroller

- XPath-räkning: 9 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Katalogändringen är verifierad lokalt och
avvaktar den samlade uppdateringen av PR #848 efter fullständig granskning.
