# Foundation – general.json, granskningsomgång 5

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Förslag | Resultat | Lint/stavning |
|---|---|---|---|---|---|
| GENERAL → PAUSE_BUILDING_CONSTRUCTION | Pause Construction | Pausa konstruktion | Pausa bygge | Sparad i Crowdin (HTTP 201). | l10n-lint: inga fel. Hunspell: inga fel. |
| GENERAL → CONSTRUCTION_PAUSE | Construction paused | Konstruktion pausad | Bygget är pausat | Sparad i Crowdin (HTTP 201). | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU → DECREASE_SPEED | Decrease Speed | Minska Hastigheten | Minska hastigheten | Dubblett i Crowdin. | l10n-lint: inga fel. Hunspell: inga fel. |
| MENU → INCREASE_SPEED | Increase Speed | Öka Hastigheten | Öka hastigheten | Dubblett i Crowdin. | l10n-lint: inga fel. Hunspell: inga fel. |

Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.