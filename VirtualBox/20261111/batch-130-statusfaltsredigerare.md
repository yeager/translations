# Batch 130: statusfältsredigerare

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 4 aktiva meddelanden i `UIStatusBarEditorWidget` har granskats
radvis i sin UI-kontext. Komponenten styr indikatorernas visning och ordning
i den virtuella maskinens statusrad.

## Resultat

Ingen textändring behövdes. `statusrad` skiljs konsekvent från
`verktygsfält`, och instruktionen `Dra och släpp` bevarar betydelsen av
`Drag&Drop` utan att ändra markupen.

## Kontroller

- XPath-räkning: 4 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Ingen katalogändring uppstod och därmed finns
inget nytt att skicka till PR #848 från denna batch.
