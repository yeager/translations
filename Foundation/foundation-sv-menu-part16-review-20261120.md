# Foundation – menu.json, granskningsomgång 16

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_MOD_PRIORITY → DISABLED_X | Disabled ({1}) | Inaktiverad ({1}) | Inaktiverade ({1}) | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_MOD_PRIORITY → OUTDATED_X | Outdated ({1}) | Utdaterad ({1}) | Inaktuella ({1}) | l10n-lint: inga fel. Hunspell: inga fel. |

Raderna räknar flera moddar och använder nu korrekt pluralform. Platshållaren `{1}` bevarades. Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.