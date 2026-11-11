# Batch 181: information om virtuella maskiner

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Det enda aktiva meddelandet i `UIDetailsView` har granskats. Det är
tillgänglighetsbeskrivningen för vyn som visar uppgifter om virtuella
maskiner.

## Resultat

`virtuella maskindetaljer` har skrivits om till `information om virtuella
maskiner`. Omskrivningen undviker en tung och tvetydig sammansättning utan att
ändra användargränssnittets innebörd.

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
