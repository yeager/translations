# Rust Coreutils: svensk skiljeteckenkontroll

Nio Fluent-filer har rättats efter en kontextbevarad kontroll med svlang. Tio kommatecken före `och` i vanlig svensk löptext har tagits bort. CLI-syntax, platshållare och ASCII-ellipser har lämnats orörda.

Kontroller:

- `moz-fluent-lint`: godkänd
- `svlang`: inga kvarvarande relevanta träffar för komma före `och`, tankstreck, särskrivning, de/dem eller kända stavfel
- Gitleaks: inga hemligheter hittades

## Hosted Weblate-import

2026-10-22 accepterade Hosted Weblate 9 uppdaterade enheter. De tio rättade kommatecknen förekom i nio enheter; båda ändringarna i `kill` finns i samma enhet. 275 oförändrade enheter hoppades över och inga enheter saknades.
