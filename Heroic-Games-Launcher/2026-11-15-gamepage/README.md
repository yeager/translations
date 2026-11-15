# Heroic Games Launcher, gamepage — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Heroic Games Launcher `v2.22.4`
- Målkomponent: Hosted Weblate `heroic-games-launcher/gamepage`, svenska
- Status: inskickad och mottagen i Hosted Weblate.

## Verifiering

Hosted Weblate accepterade 19 översättningar och en tidigare fuzzy-sträng
granskades direkt. Komponenten står på 270 av 270 översatta strängar och 0
fuzzy.

De tre kontrollträffarna är medvetna undantag: `EXE-fil` är korrekt svensk
teknisk sammansättning, `OK` är etablerad UI-form och `Steam Family Sharing`
är ett produktnamn.

Kontroller: `jq empty`, `l10n-lint`, API-läsning, `git diff --check` och
Gitleaks.
