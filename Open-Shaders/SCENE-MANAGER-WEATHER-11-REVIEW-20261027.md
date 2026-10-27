# Scene Manager: väder 11 — granskningsprotokoll

## Omfattning

De sista 10 källsträngarna i `feature.scene_manager`: väderval, grupper, status och SPID-nyckel.

## Terminologi

- `weather` är **väder** i hela flödet.
- `scene settings` är **sceninställningar**.
- `SPID key` är **SPID-nyckel**, i linje med platsmålets motsvarande sträng.
- `unsupported type` återges med den naturliga svenska UI-formuleringen **typ stöds inte**.

## Kontrollkedja

JSON, `l10n-lint`, `svlang`, Hunspell, Gitleaks samt markör- och radbrytningsjämförelse körs mot batchfilen. Inga formatmarkörer eller källradbrytningar förekommer.
