# Wireshark Qt master, svenska – batch 04

- Datum: 2026-11-12
- Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`
- Omfattning: 13 MKA-etiketter i `QObject`.
- Kontext: granskad mot den faktiska dialogkoden i `ui/qt/mka_ca_dialog.cpp`.
- Terminologi: MKA, SCI, MI, SAK, KN och AN är oförändrade protokollförkortningar. `Key Server` återges som `nyckelserver`; den korta UI-märkningen blev därför `[NS]`.

## Kontroller

- JSON och samtliga Transifex-ID:n verifierade mot den färska exporten av oöversatta strängar.
- `l10n-lint`: godkänd utan anmärkningar.
- `svlang svengelska`: inga anglicismer.
- Hunspell-SV: endast protokollförkortningar och den tekniska verbformen `avkapsla` återstod.
- `git diff --check`: inga blankstegsproblem.
- `gitleaks detect --no-git --redact`: inga hemligheter.
- `msgfmt`: ej tillämpligt för denna Transifex JSON API-batch mot Qt TS-resursen.

## Upstreamstatus

De 13 strängarna skickades i ett resursavgränsat API-anrop och bekräftades i svaret. Efterföljande avläsning visar 335 oöversatta strängar och inga av batchens sträng-ID:n bland dem. Formell granskning eller publicering har inte verifierats.
