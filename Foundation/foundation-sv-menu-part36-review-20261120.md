# Foundation – menu.json, granskningsomgång 36

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| MENU_CONTROL_REMAPPER_SETTINGS → CONFLICTS_POPUP_MESSAGE | The newest controls conflict with the current key binding configuration. Would you like to restore defaults or adjust them manually? | De senaste kontrollerna är i konflikt med den aktuella konfigurationen för nyckelbindning. Vill du återställa standardvärdena eller justera dem manuellt? | De nya kontrollerna står i konflikt med den aktuella tangentbindningskonfigurationen. Vill du återställa standardvärdena eller justera dem manuellt? | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU_CONTROL_REMAPPER_CONTROL_NAMES → CONTROL_QUICK_GAME_RELOAD | Quickload | Snabbinläsning | Snabbladda | l10n-lint: inga fel. Hunspell: inga fel. |

Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.