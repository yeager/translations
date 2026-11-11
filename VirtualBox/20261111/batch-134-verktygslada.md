# Batch 134: verktygslåda

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Det enda aktiva meddelandet i `UIToolBox` har granskats i dess knappverktygstips.

## Resultat

`Expanderar` har ersatts med UI-termen `Fäller ut`, som beskriver knappens
åtgärd naturligt och konsekvent med övriga expanderbara gränssnittselement.

Ändringen finns i lokal commit `3a7a2e5` och är ännu inte pushad till PR:n.

## Kontroller

- XPath-räkning: 1 aktivt meddelande.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Upstream-inskick väntar tills den fullständiga
kataloggranskningen är klar.
