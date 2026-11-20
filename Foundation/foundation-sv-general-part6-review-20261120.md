# Foundation – general.json, granskningsomgång 6

Datum: 2026-11-20  
Metod: Crowdin API; förslaget kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Förslag | Resultat | Lint/stavning |
|---|---|---|---|---|---|
| TRADE → ALLEGIANCE | Allegiance: | Allians: | Lojalitet: | Identisk översättning fanns redan i Crowdin; API:t rapporterade dubblett. | l10n-lint: inga fel. Hunspell: inga fel. |

”Lojalitet” återger allegiance; ”allians” avser en överenskommelse mellan parter. Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.