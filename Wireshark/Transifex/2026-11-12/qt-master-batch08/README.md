# Wireshark Qt master, svenska – batch 08

- Datum: 2026-11-12
- Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`
- Omfattning: 24 strängar i dialogen för att skapa, ändra och exportera färgteman.
- Kontext: kontrollerad mot `ui/qt/theme_designer_dialog.ui`. Standardteckensnitt får en naturlig svensk förklaring som behåller innebörden att temat fungerar på andra system.

## Kontroller

- JSON och Transifex-ID:n verifierade mot färsk oöversatt-export.
- `l10n-lint`: godkänd utan anmärkningar.
- `svlang svengelska`: inga anglicismer.
- `git diff --check`: inga blankstegsproblem.
- `gitleaks detect --no-git --redact`: inga hemligheter.
- `msgfmt`: ej tillämpligt för Qt TS-resursen och Transifex JSON API-batchen.

## Upstreamstatus

Alla 24 strängar skickades i ett resursavgränsat API-anrop och bekräftades i svaret. Efterföljande avläsning visar 266 oöversatta strängar och inga av batchens sträng-ID:n bland dem. Formell granskning eller publicering har inte verifierats.
