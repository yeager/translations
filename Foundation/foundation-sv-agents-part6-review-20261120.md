# Foundation – agents.json, granskningsomgång 6

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| BEHAVIOR_MESSAGES → UNABLE_TO_FIND_HOUSE_DESIRABILITY | Can't find a house with enough Desirability for my status | Kan inte hitta ett hus med tillräcklig önskvärdhet för min status | Kan inte hitta ett hus med tillräcklig attraktivitet för min status | l10n-lint: inga fel. Hunspell: inga fel. |
| BEHAVIOR_MESSAGES → DESIRABILITY_REQUIREMENT | To have at least a {IMG1} Desirability | Ha minst {IMG1} önskvärdhet | Ha minst {IMG1} i attraktivitet | l10n-lint: inga fel. Hunspell: inga fel. |

`Desirability` behandlas konsekvent som spelmåttet ”attraktivitet”. Platshållaren `{IMG1}` bevarades. Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.