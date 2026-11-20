# Foundation – general.json, granskningsomgång 1

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Förslag | Resultat | Lint/stavning |
|---|---|---|---|---|---|
| JOBS → BUILDER | Builder | Byggmästare | Byggare | Identisk översättning fanns redan i Crowdin; API:t rapporterade dubblett. | l10n-lint: inga fel. Hunspell: inga fel. |
| JOBS → GATHERER | Forager | Bärplockare | Samlare | Identisk översättning fanns redan i Crowdin; API:t rapporterade dubblett. | l10n-lint: inga fel. Hunspell: inga fel. |

Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.