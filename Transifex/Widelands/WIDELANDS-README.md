# Widelands – svensk granskning

Datum: 2026-11-12  
Projekt: `o:widelands:p:widelands`  
Komponent: `appdata`  
Källa: Transifex API, befintliga svenska översättningar.

## Status

- Widelands v1.3.1 släpptes 2026-02-22.
- Alla 34 komponenter har 0 oöversatta svenska strängar.
- Samtliga saknar dock Transifex granskningsmarkering; full språkgranskning sker komponentvis.
- `appdata`: 14 strängar granskade rad för rad, 6 verkliga språkfel rättade och uppladdade i en API-batch (HTTP 200). Läsning av varje enskild uppdatering via API bekräftade att den sparats.
- `editor`: 20 strängar granskade rad för rad, 8 verkliga språkfel rättade och uppladdade i en API-batch (HTTP 200). Läsning av varje enskild uppdatering via API bekräftade att den sparats.

## Kontroller

- `l10n-lint`, `svlang`, `git diff --check` och `gitleaks` passerade.
- `hunspell-sv` träffade endast produktnamnet Widelands.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil; ingen rå PO-export har ändrats.
