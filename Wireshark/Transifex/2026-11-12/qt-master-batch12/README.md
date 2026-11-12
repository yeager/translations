# Wireshark Qt master, svenska – batch 12

- Datum: 2026-11-12
- Omfattning: 5 färgfilter- och temafärgssträngar i `ThemeDesignerDialog`.

## Kontroller

- `l10n-lint`, `svlang svengelska`, `git diff --check` och `gitleaks detect --no-git --redact`: godkända.
- `msgfmt`: ej tillämpligt för Qt TS-resursen och Transifex JSON API-batchen.

## Upstreamstatus

Fem strängar skickades i ett resursavgränsat API-anrop och bekräftades i efterföljande avläsning. 206 oöversatta strängar återstår. Formell granskning eller publicering har inte verifierats.
