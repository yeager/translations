# Batch 009: konsol och terminologi

Datum: 2026-11-11
Komponenter: molnkonsol-, system- och import/exporttexter samt gemensam
terminologi.

## Granskade och ändrade områden

- Rättade samtliga aktiva förekomster av den felaktiga formen `konsoll` till
  `konsol`, inklusive sammansättningar för molnkonsol, program, anslutning och
  fel.
- Rättade nästlad sidindelning, VISO-medium, sökvägsbeskrivningar och
  återstående formuleringar med `När kryssad`.
- Lade till `terminologi.md` med beslut för VirtualBox-domänens återkommande
  termer, filformat och kodlitteraler.

## Delkontroll

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: konsekvent.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckta hemligheter.

## Upstream

Ändringarna är lokala och inte pushade till PR #848. Full radvis granskning
och samlad slutkontroll återstår innan PR:n uppdateras.
