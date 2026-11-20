# Foundation – agents.json, granskningsomgång 4

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| BEHAVIOR_MESSAGES → WORKPLACE_IS_DISABLED | My workplace is unusable | Min arbetsplats är otillgänglig | Min arbetsplats kan inte användas | l10n-lint: inga fel. Hunspell: inga fel. |

Den nya formuleringen återger att arbetsplatsen är avstängd/obrukbar, inte nödvändigtvis geografiskt oåtkomlig. Ändringen skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.