# Audacity: väljarkommando, 2026-11-14

## Granskad post

`Select...` användes både för knappar som väljer fil- eller katalogplats i
timerinspelningen och för kommandot i `SelectCommand`. Den tidigare svenska
texten `Bläddra...` beskrev bara den ena användningen. Den är ändrad till
`Välj...`, som fungerar i båda sammanhangen.

## Underlag

Källan i `TimerRecordDialog.cpp` använder posten för att välja sökväg för att
spara eller exportera ett projekt. `SelectCommand.cpp` använder samma post för
kommandots synliga namn.

## Kontroller

- `msgfmt --check --statistics`: godkänd, 4 443 färdiga poster.
- `l10n-lint`: inga fel. Kvarvarande varningar gäller redan existerande
  kortkommandon, formatsträngar och avsiktliga namn.
- Riktad Hunspell-sv kördes med låg CPU-prioritet; `Välj` godkändes och ingen
  Hunspell-process fanns kvar efteråt.
- `git diff --check`: godkänd.
- Gitleaks: godkänd.

## Upstreamstatus

Commit [`1356c99`](https://github.com/yeager/audacity/commit/1356c99407cd8cca641d0458f0b65e47238ea5de)
är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).
PR:n är öppen och väntar på CI samt upstream-granskning; den är inte mergead.
