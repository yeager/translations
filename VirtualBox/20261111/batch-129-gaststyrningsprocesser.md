# Batch 129: gäststyrningsprocesser

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 11 aktiva meddelanden i `UIGuestProcessControlWidget`,
`UIGuestProcessTreeItem` och `UIGuestSessionTreeItem` har granskats radvis
mot samma gäststyrningsträd.

## Resultat

Två etiketter har rättats. Den suspenderade sammansättningen är nu
`Session-/process-ID`, och den felstavade `Processtatus` är ersatt med den
tydliga formen `Status för process`. Övriga process- och sessionstermer är
konsekventa.

## Kontroller

- XPath-räkning: 11 aktiva meddelanden i de tre komponenterna.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella granskningen av de tre gäststyrningskomponenterna är
lokalt slutförd i commit `3ba2a5c` och ännu inte pushad till PR #848.
