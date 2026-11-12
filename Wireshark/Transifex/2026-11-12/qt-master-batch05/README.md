# Wireshark Qt master, svenska – batch 05

- Datum: 2026-11-12
- Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`
- Omfattning: 9 strängar för kataloghantering, statistikexport och inkapsling.
- Kontext: jämförd med befintlig Wireshark-svenska; `Frames` och `Encapsulation` använder etablerade formerna `ramar` respektive `inkapsling`.

## Kontroller

- JSON-struktur och Transifex-ID:n verifierade mot färsk oöversatt-export.
- `l10n-lint`: godkänd utan anmärkningar.
- `svlang svengelska`: inga anglicismer.
- Hunspell-SV: endast filformatens ändelser återstod.
- `git diff --check`: inga blankstegsproblem.
- `gitleaks detect --no-git --redact`: inga hemligheter.
- `msgfmt`: ej tillämpligt för Qt TS-resursen och Transifex JSON API-batchen.

## Upstreamstatus

Alla 9 strängar skickades i ett resursavgränsat API-anrop och bekräftades i svaret. Efterföljande avläsning visar 326 oöversatta strängar och inga av batchens sträng-ID:n bland dem. Formell granskning eller publicering har inte verifierats.
