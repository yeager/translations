# Stirling PDF: MCP-autentisering förtydligad, 16 november 2026

PR [#7833](https://github.com/Stirling-Tools/Stirling-PDF/pull/7833)
granskades mot den aktuella grentoppen efter en konkret CodeRabbit-kommentar.

## Ändring

Commit
[`220c4cc0c2d6d646a26472e5710994f79396795f`](https://github.com/yeager/Stirling-PDF/commit/220c4cc0c2d6d646a26472e5710994f79396795f)
förtydligar den svenska MCP-beskrivningen: slutpunkten kan använda OAuth eller
API-nyckelautentisering. Det stämmer med projektets testkonfiguration, som
täcker båda lägena.

Samma ändring ersätter ett tankstreck med punkt i den närliggande svenska
texten. Källtexten använder inte tankstreck där.

## Kontroller

- TOML-syntax: godkänd med Python `tomllib`.
- Diffkontroll: godkänd.
- Gitleaks: inga hemligheter hittades.
- `l10n-lint`: inga fel. Två varningar återstår på oförändrade rader i samma
  fil (ett upprepat tal och Unicode-normalisering).
- Hunspell kördes på den ändrade terminologin; tekniska namn är inte ett
  stavningsfel.

En engelsk uppföljning finns i PR:en. Efter push är den ursprungliga
CodeRabbit-tråden automatiskt markerad som inaktuell.

## Upstreamstatus

Ändringen är pushad till PR-grenen. PR:n är fortfarande öppen och väntar på
upstreamgranskning; den är varken godkänd, sammanfogad eller släppt.
