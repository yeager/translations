# Audacity: väljarkommando, 2026-11-14

## Granskad post

`Select...` användes både för knappar som väljer fil- eller katalogplats i
timerinspelningen och för kommandot i `SelectCommand`. Den tidigare svenska
texten `Bläddra...` beskrev bara den ena användningen. Den är ändrad till
`Välj...`, som fungerar i båda sammanhangen.

Två närliggande gränssnittsposter är också normaliserade: kommandonamnet
`Handle 'audacity://' url` börjar med `Hantera`, och EQ-kurvans reserverade
visningsnamn använder katalogens etablerade form `namnlös` med liten bokstav.

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

Commit [`ae9ae2c`](https://github.com/yeager/audacity/commit/ae9ae2c244e7af3f4d81469ecc8f2f4e1524d814)
är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).
PR:n är öppen och väntar på upstream-granskning; den är inte mergead.
CodeRabbit-kontrollen för committen har passerat, men ingen
underhållargranskning eller merge är verifierad.
