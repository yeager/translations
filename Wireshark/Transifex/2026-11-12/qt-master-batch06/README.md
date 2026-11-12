# Wireshark Qt master, svenska – batch 06

- Datum: 2026-11-12
- Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`
- Omfattning: 18 strängar i temaredigeraren.

## Kontroller

- JSON och Transifex-ID:n verifierade mot färsk oöversatt-export.
- `l10n-lint`: godkänd utan anmärkningar.
- `svlang svengelska`: inga anglicismer.
- `git diff --check`: inga blankstegsproblem.
- `gitleaks detect --no-git --redact`: inga hemligheter.
- `msgfmt`: ej tillämpligt för Qt TS-resursen och Transifex JSON API-batchen.

## Upstreamstatus

Alla 18 strängar skickades i ett resursavgränsat API-anrop och bekräftades i svaret. Efterföljande avläsning, efter Transifex synkfördröjning, visar 308 oöversatta strängar och inga av batchens sträng-ID:n bland dem. Formell granskning eller publicering har inte verifierats.
