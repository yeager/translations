# Stellarium – svenska översättningar

Datum: 2026-11-12  
Projekt: `o:stellarium:p:stellarium`  
Komponent: `po/stellarium-skycultures-descriptions/stellarium-skycultures-descriptions.pot` (master)  
Källa: Transifex API, oöversatta svenska strängar.  
Projektaktivitet: Stellarium v26.3 släpptes 2026-09-28.

## Batch 1

- Granskade: 1 oöversatt sträng.
- Ändrade: 1 sträng.
- Status: uppladdad till Transifex via API (HTTP 200). En ny API-avläsning efter synkronisering visar 0 oöversatta strängar i komponenten.
- Terminologi: se `TERMINOLOGY.md`.

## Kontroller

- `l10n-lint`, `svlang`, `git diff --check` och `gitleaks` passerade på deltafilen.
- `hunspell-sv` träffade `svalfisk`; termen behålls som en direkt återgivning av källans namn på motivet och är dokumenterad i deltafilens kontext.
- `msgfmt` kan inte köras på Transifex JSON-deltafilen. Ingen rå `.po`-export har ändrats.
