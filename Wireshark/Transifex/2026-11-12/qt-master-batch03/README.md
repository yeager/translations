# Wireshark Qt master, svenska – batch 03

- Datum: 2026-11-12
- Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`
- Omfattning: 25 strängar i `MkaCaDialog`, `PreferencesDialog` och tillhörande `QObject`-etiketter.
- Kontext: kontrollerad mot `ui/qt/mka_ca_dialog.cpp` i Wiresharks aktuella källkod.
- Särskilda termer: MKA, SCI, MI, SAK, CKN, KN och AN är protokollförkortningar och är därför bevarade. `Frames` följer befintlig Wireshark-svenska som `ramar`.

## Kontroller

- JSON-struktur och Transifex-ID:n verifierade mot en färsk export av oöversatta strängar.
- `l10n-lint`: godkänd utan anmärkningar.
- `svlang svengelska`: inga anglicismer.
- Hunspell-SV: endast protokollförkortningar och sammansatta tekniska termer återstod.
- `git diff --check`: inga blankstegsproblem.
- `gitleaks detect --no-git --redact`: inga hemligheter.
- `msgfmt`: ej tillämpligt; resursen är en Qt TS-resurs och denna batch är Transifex JSON API-data.

## Upstreamstatus

Alla 25 strängar skickades i ett resursavgränsat API-anrop och bekräftades i API-svaret. En efterföljande avläsning visar 348 oöversatta strängar och inga av batchens sträng-ID:n bland dem. Formell granskning eller publicering har inte verifierats.
