# Foundation – menu.json, granskningsomgång 39

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| OPEN_BOOK_TAXATION | Open Royal Book (Taxation page) | Öppna kungaboken (beskattningssida) | Öppna den kungliga boken (beskattningssidan) | l10n-lint/Hunspell: inga fel. |
| OPEN_BOOK_EDICTS_AND_PRIVILEGES | Open Royal Book (Edicts and Privileges page) | Öppna kungaboken (förordnanden och privilegier) | Öppna den kungliga boken (sidan Förordnanden och privilegier) | l10n-lint/Hunspell: inga fel. |
| OPEN_BOOK_TRADE_ROUTES | Open Royal Book (Trade Routes page) | Öppna Kungaboken (handelsvägar) | Öppna den kungliga boken (handelsvägssidan) | l10n-lint/Hunspell: inga fel. |

Royal Book-normaliseringen är nu konsekvent i dessa ytterligare tre genvägar. Samtliga ändringar skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.