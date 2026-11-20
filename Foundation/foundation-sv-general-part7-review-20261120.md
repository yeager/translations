# Foundation – general.json, granskningsomgång 7

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Förslag | Resultat | Lint/stavning |
|---|---|---|---|---|---|
| MONUMENTS → MONUMENT_EFFECT_ON_ESTATES | Monument Effect On Estates: | Monumentens inflytande på ständer: | Monumentets inflytande på stånden: | Dubblett i Crowdin. | l10n-lint: inga fel. Hunspell: inga fel. |
| MONUMENTS → START_CONSTRUCTION | Start Construction | Starta konstruktion | Starta bygget | Sparad i Crowdin (HTTP 201). | l10n-lint: inga fel. Hunspell: inga fel. |

Det efterföljande blanksteget efter kolonet bevarades. Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.