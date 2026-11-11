# Batch 140: USB-filterdetaljer

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 19 aktiva meddelanden i `UIUSBFilterDetailsEditor` har granskats
radvis i USB-filterdialogen.

## Resultat

- `tillverkar-ID` och `produkt-ID` använder nu etablerad versalisering för
  den tekniska förkortningen.
- USB-filtrets omfattning beskriver nu korrekt både lokalt anslutna enheter
  och enheter anslutna till VRDP-klientens dator.

Ändringarna finns i lokal commit `49d5fbe` och är ännu inte pushade till PR:n.

## Kontroller

- XPath-räkning: 19 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Upstream-inskick väntar tills den fullständiga
kataloggranskningen är klar.
