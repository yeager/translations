# Foundation – agents.json, granskningsomgång 5

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| AGENT_ISSUES → VILLAGER_HAS_NO_WORKPLACE | Couldn't find a workplace with the currently assigned job. | Kunde inte hitta en arbetsplats med det nuvarande tilldelade jobbet. | Kunde inte hitta en arbetsplats för det tilldelade arbetet. | l10n-lint: inga fel. Hunspell: inga fel. |
| BEHAVIOR_MESSAGES → I_AM_ON_FREE_TIME | I am on free time | Jag är på fritiden | Jag har ledigt | l10n-lint: inga fel. Hunspell: inga fel. |

Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.