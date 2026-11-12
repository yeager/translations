# Wireshark Qt master, svenska – batch 09

- Datum: 2026-11-12
- Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`
- Omfattning: 25 strängar i temaredigerarens förhandsvisning och temaåtgärder.
- Kontext: användargränssnitt för skapande, import, export, namnbyte och val av tema.

## Kontroller

- JSON och Transifex-ID:n verifierade mot färsk oöversatt-export.
- `l10n-lint`: godkänd utan anmärkningar.
- `svlang svengelska`: inga anglicismer.
- Hunspell-SV: endast sammansättningen `paketslista` återstod, men är en avsiktlig och korrekt UI-term.
- `git diff --check`: inga blankstegsproblem.
- `gitleaks detect --no-git --redact`: inga hemligheter.
- `msgfmt`: ej tillämpligt för Qt TS-resursen och Transifex JSON API-batchen.

## Upstreamstatus

Alla 25 strängar skickades i ett resursavgränsat API-anrop och bekräftades i svaret. Efterföljande avläsning visar 241 oöversatta strängar och inga av batchens sträng-ID:n bland dem. Formell granskning eller publicering har inte verifierats.
