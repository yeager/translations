# Foundation – general.json, granskningsomgång 4

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| GENERAL → BUILD_RIGHT_TAXES | Build right taxes | Bygg rätt skatter | Byggrättsskatter | l10n-lint: inga fel. Hunspell: inga fel. |
| GENERAL → BELL_TOWER_SOUND | Bell tower sound: | Klockornas klang: | Klocktornets ljud: | l10n-lint: inga fel. Hunspell: inga fel. |
| GENERAL → PRIORITIZE_BUILDING_CONSTRUCTION | Prioritize Construction | Prioritera konstruktion | Prioritera bygge | l10n-lint: inga fel. Hunspell: inga fel. |

Samtliga ändringar skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.