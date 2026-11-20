# Foundation – general.json, granskningsomgång 2

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| JOBS → STONE_CUTTER | Stone Cutter | Stenhuggare | Stenskärare | l10n-lint: inga fel. Hunspell: inga fel. |

Ändringen särskiljer yrket från `Stone Mason` (stenhuggare). Den skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.