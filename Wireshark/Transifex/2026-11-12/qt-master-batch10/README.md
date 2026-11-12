# Wireshark Qt master, svenska – batch 10

- Datum: 2026-11-12
- Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`
- Omfattning: 25 strängar för temahantering, validering och teckensnittsinställningar.

## Kontroller

- JSON och Transifex-ID:n verifierade mot färsk oöversatt-export.
- `l10n-lint`: godkänd utan anmärkningar.
- `svlang svengelska`: en träff på engelska källordet `Parses` i JSON-underlaget; ingen svensk anglicism.
- Hunspell-SV: förväntade träffar för produktnamn, filändelsen `.jsonc`, Lua och avsiktliga UI-sammansättningar.
- `git diff --check`: inga blankstegsproblem.
- `gitleaks detect --no-git --redact`: inga hemligheter.
- `msgfmt`: ej tillämpligt för Qt TS-resursen och Transifex JSON API-batchen.

## Upstreamstatus

Alla 25 strängar skickades i ett resursavgränsat API-anrop och bekräftades i svaret. Efterföljande avläsning visar 216 oöversatta strängar och inga av batchens sträng-ID:n bland dem. Formell granskning eller publicering har inte verifierats.
