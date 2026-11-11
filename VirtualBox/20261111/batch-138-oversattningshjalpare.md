# Batch 138: översättningshjälpare

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 19 aktiva meddelanden i `UITranslator` har granskats radvis i
hjälpfunktionerna för mängder, enheter och relativa tidsangivelser.

## Resultat

Den relativa tidsangivelsen för `%n day(s) ago` använder nu `dag/dagar` i
stället för `dygn`. Det speglar den kalenderbaserade enheten i källtexten och
är konsekvent med katalogens vanliga varaktighetsangivelse.

Ändringen finns i lokal commit `b87eebc` och är ännu inte pushad till PR:n.

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
