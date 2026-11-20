# Foundation – menu.json, granskningsomgång 35

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_GRAPHICS_SETTINGS → QUALITY_PRESET | Quality Preset | Kvalitetsalternativ | Kvalitetsförinställning | l10n-lint: inga fel. Hunspell: inga fel. |

”Förinställning” motsvarar specifikt en preset, till skillnad från ett godtyckligt kvalitetsalternativ. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.