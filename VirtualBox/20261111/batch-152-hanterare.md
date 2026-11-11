# Batch 152: VirtualBox-hanteraren

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 5 aktiva meddelanden i `UIVirtualBoxManager` har granskats radvis i
filvalet och verktygsfältsmenyn i VirtualBox-hanteraren.

## Resultat

- De felaktiga formerna `virtuell maskin-fil` och `virtuella maskin-filer`
  har ersatts med idiomatiska filbeskrivningar.
- `Toolbar` använder nu den etablerade termen `verktygsfält`.

Ändringarna finns i lokal commit `c761881` och är ännu inte pushade till PR:n.

## Kontroller

- XPath-räkning: 5 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Upstream-inskick väntar tills den fullständiga
kataloggranskningen är klar.
