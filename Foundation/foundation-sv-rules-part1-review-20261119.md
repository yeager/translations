# Foundation – regler I, svensk granskning 2026-11-19

Den första delen av `rules.json` har granskats via Crowdin API. Förslagen är utkast och har inte skickats till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 1002 | Job learning speed is increased by {IMG1}. | Hastighet för jobbinlärning ökas med {IMG1}. | Hastigheten för yrkesinlärning ökar med {IMG1}. |
| 2160 | Happiness is less impacted by {IMG1}. | Lycka påverkas mindre med {IMG1}. | Lyckan påverkas mindre av {IMG1}. |
| 2673 | {IMG1} is the right status for {IMG2} job. | {IMG1} är den rätta statusen för {IMG2} jobb. | {IMG1} är rätt status för {IMG2}-jobbet. |
| 2675 | {IMG1} is not a right status for {IMG2} job. | {IMG1} är inte den rätta statusen för {IMG2} jobb. | {IMG1} är inte rätt status för {IMG2}-jobbet. |
| 3952 | This building's {IMG1} is increased by {IMG2}. | Denna byggnads {IMG1} ökas med {IMG2}. | Den här byggnadens {IMG1} ökar med {IMG2}. |
| 5042 | Condition | Skick | Villkor |
| 6083 | Multiplies production by {1}. | Multiplicerar produktion med {1}. | Multiplicerar produktionen med {1}. |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Platshållarna `{IMG1}`, `{IMG2}` och `{1}` är bevarade.
