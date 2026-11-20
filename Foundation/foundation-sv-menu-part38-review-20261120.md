# Foundation – menu.json, granskningsomgång 38

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| OPEN_BOOK | Open Royal Book | Öppna Kungaboken | Öppna den kungliga boken | l10n-lint/Hunspell: inga fel. |
| OPEN_BOOK_VILLAGERS | Open Royal Book (Villagers page) | Öppna kungaboken (sidan för bybor) | Öppna den kungliga boken (bybosidan) | l10n-lint/Hunspell: inga fel. |
| OPEN_BOOK_WORKPLACE | Open Royal Book (Buildings page) | Öppna Kungaboken (byggnadssida) | Öppna den kungliga boken (byggnadssidan) | l10n-lint/Hunspell: inga fel. |
| OPEN_BOOK_TRADE | Open Royal Book (Resources page) | Öppna kungaboken (resurssida) | Öppna den kungliga boken (resurssidan) | l10n-lint/Hunspell: inga fel. |
| OPEN_BOOK_BUDGET | Open Royal Book (Economy page) | Öppna kungaboken (ekonomisida) | Öppna den kungliga boken (ekonomisidan) | l10n-lint/Hunspell: inga fel. |
| OPEN_BOOK_LOGS | Open Royal Book (Logs page) | Öppna Kungaboken (Loggsida) | Öppna den kungliga boken (loggsidan) | l10n-lint/Hunspell: inga fel. |
| OPEN_BOOK_VILLAGE_OVERVIEW | Open Royal Book (Village Overview page) | Öppna Kungaboken (sidan med översikt över byn) | Öppna den kungliga boken (byöversiktssidan) | l10n-lint/Hunspell: inga fel. |

Royal Book är nu konsekvent ”den kungliga boken”. Samtliga sju ändringar skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.