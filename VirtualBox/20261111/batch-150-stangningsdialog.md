# Batch 150: stängningsdialog

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 12 aktiva meddelanden i `UIVMCloseDialog` har granskats radvis i
dialogen för avstängning, tillståndssparning och bakgrundskörning.

## Resultat

- Uppmaningen `Du vill:` har ersatts med den naturliga frågan `Vad vill du
  göra?`.
- Beskrivningen av bakgrundskörning hanterar nu korrekt flera maskinfönster,
  tar bort dubbelt mellanslag och använder `VirtualBox-hanteraren`.

Ändringarna finns i lokal commit `b00b984` och är ännu inte pushade till PR:n.

## Kontroller

- XPath-räkning: 12 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Upstream-inskick väntar tills den fullständiga
kataloggranskningen är klar.
