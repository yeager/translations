# ComfyUI svensk ombasning, källmanifest för `main.json`

Efter den manuella genomgången av samtliga aktuella `main.json`-nycklar har
källmanifestet uppdaterats till den nuvarande engelska filens Git-objekt.

`pnpm locale:check` rapporterar därmed inga svenska `main.json`-strängar som
behöver översättas. Återstående arbete är 1 321 nya strängar i `sv/nodeDefs.json`,
samt upstream-pruning och 15 skyddade tokenavvikelser i node-definitionerna.

Kontroller: `pnpm locale:check`, `git diff --check` och avgränsad Gitleaks.
