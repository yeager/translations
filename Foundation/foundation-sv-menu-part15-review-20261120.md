# Foundation – menu.json, granskningsomgång 15

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MODS_BROWSER → UP_TO_DATE | Up-to-date | Uppdaterad | Aktuell | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_MODS_BROWSER → OUTDATED | Outdated | Utdaterad | Inaktuell | l10n-lint: inga fel. Hunspell: inga fel. |

Statusarna beskriver nu konsekvent om en mod är aktuell eller inaktuell. Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.