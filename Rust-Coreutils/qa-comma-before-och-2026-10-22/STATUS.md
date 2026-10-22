# Rust Coreutils: svensk skiljeteckenkontroll

Nio Fluent-filer har rättats efter en kontextbevarad kontroll med svlang. Tio kommatecken före `och` i vanlig svensk löptext har tagits bort. CLI-syntax, platshållare och ASCII-ellipser har lämnats orörda.

Kontroller:

- `moz-fluent-lint`: godkänd
- `svlang`: inga kvarvarande relevanta träffar för komma före `och`, tankstreck, särskrivning, de/dem eller kända stavfel
- Gitleaks: inga hemligheter hittades
